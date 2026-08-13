#!/usr/bin/env python3
"""Canonicalisation primitives: load, hygiene, normalisation, and the rule stages.

The census transcribes what was *said*, so one thing arrives under many surface
strings -- `pcb`, `printed circuit board`, `PCBs`. This layer collapses them.
It is ADDITIVE: nothing under census/ is ever modified.

Ordering is deliberate and cheap-first. Every pair a deterministic rule can
decide is a pair the LLM never has to see, and the rules are also the only stages
that can be audited by reading them. The expensive stages (embeddings,
adjudication) exist to catch what the rules cannot: synonyms that share no
tokens, and acronyms embeddings are blind to.

Rebuilt from canon/_canon_report.md -- the original scripts were never committed.
Stage numbering follows that report so the two can be read side by side.
"""
import json, pathlib, re, unicodedata
from collections import Counter, defaultdict

# The sixteen the census prompt is allowed to emit. Anything else is a model slip
# and gets remapped rather than trusted; the mapping is the report's, verbatim.
TYPES = {
    "component", "company-product", "software", "technique", "manufacturing",
    "concept-principle", "tool-equipment", "business-model", "standard-protocol",
    "career", "media-resource", "community-event", "engineering-practice",
    "industry-economics", "person", "other",
}
JUNK_TYPE = {
    "logistics": "industry-economics", "technology": "concept-principle",
    "material": "component", "financial-instrument": "business-model",
    "failure-mode": "concept-principle", "legal": "industry-economics",
    "security": "concept-principle", "financial?": "business-model",
    "opinion": "concept-principle", "chemical": "component",
    "project": "media-resource", "infrastructure": "other",
    "systems-integration": "engineering-practice", "application": "concept-principle",
    "standards-protocol": "standard-protocol",
}
DEPTHS = {"mention", "explains", "opinion"}

# Types that may merge. A person and a company are never the same entity even if
# the strings look alike (`fluke` the brand vs a surname); a tool and the practice
# of using it routinely are.
COMPATIBLE = [
    {"component", "tool-equipment", "company-product"},
    {"technique", "engineering-practice", "manufacturing", "concept-principle"},
    {"software", "tool-equipment", "media-resource"},
    {"business-model", "industry-economics", "career"},
    {"standard-protocol", "concept-principle"},
]

# TWO stemmers, deliberately. The aggressive one folds -ing/-er/-ed, which is
# right for generating merge CANDIDATES but disastrous as a merge rule: it makes
# `3d-printer` and `3d-printing` identical, and a printer is not printing. Stage 3
# is supposed to be safe-by-construction, so it gets the plural-only stemmer and
# never sees a derivation.
SUFFIXES = ("ing", "ers", "ies", "es", "er", "ed", "s")
PLURAL_SUFFIXES = ("ies", "es", "s")


def stem(word):
    for suf in SUFFIXES:
        if word.endswith(suf) and len(word) - len(suf) >= 3:
            return word[: -len(suf)]
    return word


def plural_stem(word):
    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"
    for suf in ("es", "s"):
        if word.endswith(suf) and len(word) - len(suf) >= 3:
            return word[: -len(suf)]
    return word


def normalise(s):
    """Stage 2: case / unicode / punctuation / whitespace fold."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().strip()
    s = s.replace("'", "").replace("’", "")
    s = re.sub(r"[\s_/]+", "-", s)
    s = re.sub(r"[^a-z0-9+.#-]", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s


def tokens(name):
    return [t for t in name.split("-") if t]


def stem_key(name):
    """Identical stemmed token SEQUENCE -- order matters, so `board-test` and
    `test-board` stay apart."""
    return tuple(stem(t) for t in tokens(name))


def digits(name):
    """Part numbers are the classic false merge: LM317 and LM319 differ by one
    character and embed almost identically. Any difference in the digit runs is
    an automatic reject, whatever the cosine says."""
    return tuple(re.findall(r"\d+", name))


def acronym_of(name):
    ts = tokens(name)
    if len(ts) < 2:
        return None
    letters = "".join(t[0] for t in ts if t and t[0].isalpha())
    return letters if 2 <= len(letters) <= 6 else None


def compatible(t1, t2):
    if t1 == t2 or "other" in (t1, t2):
        return True
    return any(t1 in g and t2 in g for g in COMPATIBLE)


class Corpus:
    """Every mention across every census directory, with hygiene applied."""

    def __init__(self, census_dirs):
        self.fixes = []
        self.by_name = defaultdict(lambda: {
            "mentions": 0, "episodes": set(), "types": Counter(),
            "snippets": [], "asr_suspect": 0})
        self.episodes = 0
        for d in census_dirs:
            for f in sorted(pathlib.Path(d).glob("*.json")):
                if f.name.startswith("_"):
                    continue
                try:
                    doc = json.loads(f.read_text())
                except json.JSONDecodeError:
                    continue
                self.episodes += 1
                for m in doc.get("mentions", []):
                    self._add(f.stem, m)

    def _add(self, stem_id, m):
        name = m.get("concept")
        if not name:
            return
        t = m.get("type")
        if t not in TYPES:
            mapped = JUNK_TYPE.get(t, "other")
            self.fixes.append({"kind": "type", "from": t, "to": mapped,
                               "concept": name, "episode": stem_id})
            t = mapped
        d = m.get("depth")
        if d not in DEPTHS:
            # Stage 1 field-leakage: a type string turning up in `depth`.
            self.fixes.append({"kind": "depth", "from": d, "to": "mention",
                               "concept": name, "episode": stem_id})
            d = "mention"
        e = self.by_name[normalise(name)]
        e["mentions"] += 1
        e["episodes"].add(stem_id)
        e["types"][t] += 1
        e["asr_suspect"] += bool(m.get("asr_suspect"))
        if len(e["snippets"]) < 3 and m.get("context_snippet"):
            e["snippets"].append(m["context_snippet"])

    def names(self):
        return list(self.by_name)

    def type_of(self, name):
        return self.by_name[name]["types"].most_common(1)[0][0]

    def mentions(self, name):
        return self.by_name[name]["mentions"]


def variant_pairs(names):
    """Stage 3: plural and hyphen/spacing variants, but ONLY where both surface
    forms were actually observed. Never invent a form the corpus never used --
    that is how `bus` and `buses` merge safely while `bu` never appears."""
    out, seen = [], set(names)
    by_stem = defaultdict(list)
    for n in names:
        # plural-only: `bus`/`buses` merge, `3d-printer`/`3d-printing` do not
        by_stem[tuple(plural_stem(t) for t in tokens(n))].append(n)
    for group in by_stem.values():
        if len(group) < 2:
            continue
        group = sorted(group)
        for i, a in enumerate(group):
            for b in group[i + 1:]:
                out.append((a, b, "plural"))
    # collapsed-spacing variants: `heatsink` vs `heat-sink`
    flat = defaultdict(list)
    for n in names:
        flat["".join(tokens(n))].append(n)
    for group in flat.values():
        if len(group) > 1:
            group = sorted(group)
            for i, a in enumerate(group):
                for b in group[i + 1:]:
                    out.append((a, b, "spacing"))
    # The digit guard has to apply HERE too, not only in rule_verdict. Joining
    # tokens to test spacing also joins digits: `1-2-volt-rail` and `12-volt-rail`
    # both collapse to "12voltrail", so a 1.2 V core rail was merged into a 12 V
    # bulk rail -- and stage 3 runs before rule_verdict, so the part-number guard
    # never saw it. Measured on the real vocabulary: 7 merges corrupted this way,
    # including `7-4-series-logic` into `74-series-logic` and `fluke-875` into
    # `fluke-87-5`. Every decimal quantity in the corpus is exposed to this,
    # because the census slugifies "1.2 volt" to "1-2-volt".
    return {(a, b): k for a, b, k in out
            if a in seen and b in seen and digits(a) == digits(b)}


def acronym_pairs(corpus):
    """Stage 7. Embeddings cannot see that `pcb` == `printed-circuit-board`; the
    strings share no substring and no context. Deterministic initials matching is
    the only thing that finds these.

    An acronym gets exactly ONE expansion -- the highest-mention one. `ul` keeps
    `underwriters-laboratories` and rejects `ultraviolet-laser`; without that rule
    every homonym collapses into a single wrong node."""
    short = {n for n in corpus.names() if 2 <= len(n) <= 6 and "-" not in n}
    cands = defaultdict(list)
    for n in corpus.names():
        a = acronym_of(n)
        if a and a in short:
            cands[a].append(n)
    out, rejected = {}, []
    for a, expansions in cands.items():
        expansions.sort(key=lambda e: -corpus.mentions(e))
        best = expansions[0]
        out[(a, best)] = "acronym"
        for other in expansions[1:]:
            # a co-expansion only survives if it is a spelling variant of the winner
            if stem_key(other) == stem_key(best):
                out[(a, other)] = "acronym-variant"
            else:
                rejected.append({"acronym": a, "kept": best, "rejected": other})
    return out, rejected


def rule_verdict(a, b, corpus, cos=None):
    """Stages 5 and 6: decide a pair without asking the model, or defer.

    -> "SAME" | "DISTINCT" | None (None means: send it to adjudication)
    """
    ta, tb = corpus.type_of(a), corpus.type_of(b)
    if digits(a) != digits(b):
        return "DISTINCT"                      # part numbers, process nodes, model IDs
    if not compatible(ta, tb):
        return "DISTINCT"
    if stem_key(a) == stem_key(b):
        return "SAME"                          # stage 5 auto-merge
    if cos is not None and cos < 0.86 and \
            corpus.mentions(a) == 1 and corpus.mentions(b) == 1:
        # two one-off strings that are only vaguely close: not worth a model call,
        # and a wrong merge here is invisible because neither has evidence behind it
        return "DISTINCT"
    return None


class Union:
    def __init__(self, items):
        self.p = {i: i for i in items}

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra

    def groups(self):
        g = defaultdict(list)
        for x in self.p:
            g[self.find(x)].append(x)
        return g
