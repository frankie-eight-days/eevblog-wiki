# solder mask expansion

Solder mask expansion is the amount by which the opening in a board's solder mask is enlarged relative to the copper pad beneath it: the mask opening expands past the width of the pad, leaving a ring of bare laminate around the copper before the mask begins.[1353] It is set as a design rule in PCB CAD, and it governs whether a sliver of mask survives between adjacent pins of a fine-pitch package.[1353][127] Getting it wrong in either direction is a manufacturing problem rather than an electrical one — too much expansion removes the mask between pins and invites solder bridges, too little leaves a mask feature the board house cannot reliably print.[255][193]

## Why the mask between pins matters

Without solder mask between the pins of a package, shorts happen easily during assembly.[127] Excess solder applied by hand, by drag soldering, or by reflow has nothing to stop it walking from one pad to the next and bridging.[1353] A mask sliver between the pads gives the solder a physical barrier, which is why a well-designed footprint with mask between the pins is one of the preconditions for soldering fine-pitch surface-mount parts quickly and cleanly with nothing more than a chisel-tip iron and fine solder.[186]

The failure is visible in CAD before it is visible on a board. Where expansion is set too large, the individual openings merge into one solid block over the whole package outline, and a quad flat pack laid out that way will bridge across its pins on assembly.[255][1262] The same condition arises from the opposite error — pads drawn slightly too wide for the pitch, so that even a modest expansion consumes the gap.[425] A footprint that would have broken through in this way can be repaired by narrowing the pad rather than by touching the global rule, leaving a mask gap of roughly four or five thou between pads.[244]

## Typical values

Expansion is a small number, and the useful range is narrow. Around four thou is a reasonable general-purpose value for an ordinary board.[193] On a dense package it must come down: 0.05 mm, or two thou, is a very small expansion used where the pin pitch leaves no room for more.[193] An expansion of 1.5 thou on a 44-pin quad flat pack of reasonable pitch yields a measured mask width of 5.5 mil between the pads, which is more than adequate to manufacture.[127] Setting 0.025 mm on a fine-pitch part likewise leaves 0.1 mm — four thou — of mask between the pads.[1353]

At the other end, 0.1 mm is a huge expansion despite sounding negligible, wide enough to swallow the gap entirely.[1353] Pushing the value down to one thou to win clearance is possible in the editor but not necessarily on the panel: a board house is unlikely to be able to hold it, and will price accordingly if it accepts the job at all.[193] The sliver left at that setting is negligible in practice.[193]

Fabricators publish their own floor, and it is the binding constraint. One prototype service specifies a minimum solder mask opening of 0.05 mm around pads without stating a mask sliver width directly; a design carrying 0.025 mm expansion can be automatically rejected against that rule, sending an apparently finished board back to the global rules for rework.[1353]

## Where the value is set

Expansion can be applied globally across the board, per component or package, or pin by pin, and which level is appropriate depends on the package in use.[1353] Because it is a rule rather than a per-pad drawing, a single global change propagates to every footprint, which is what makes an out-of-range default so easy to ship unnoticed.[1353][1262]

Footprints brought in from another tool are a specific hazard: an imported layout can arrive with the mask opening cut under the entire part rather than around the individual pads, a state that must be fixed before Gerbers are generated.[1374]

## Checking it in 3D

The standard check is the 3D view with the component models suppressed, looking directly at the mask over the pads to answer whether mask survives between every pin.[990] Design rule checks can catch some of this, but a visual look at what the board will physically be is the more reliable confirmation, and it is a principal reason to use 3D mode at all.[990][Ep4r-wD7PPs][244] Early KiCad's 3D mode omitted solder mask rendering altogether, which removes most of the point of having one.[254] The mask can be rendered in the intended colour, so the pads read as copper and the surrounding expansion as mask.[1353][193]

## Vias and tenting

Expansion interacts with via tenting. A via left open near a pad allows solder paste to flow into it and short out, so vias under and around fine-pitch parts are force-tented — the mask is deliberately carried over the via with no expansion at all.[193] Tented and untented vias are conveyed to the fabricator implicitly through the Gerbers, which encode the mask expansion; setting the tenting option at Gerber generation is sufficient and no separate instruction is needed.[500]

Expansion also constrains via geometry directly. On a 0.4 mm pitch FPGA a 0.3 mm via will not fit between the pads at all, and a 0.2 mm via becomes feasible only if the surrounding expansion is reduced.[193]

## Deliberate expansion

Mask expansion is sometimes wanted at maximum. Fiducials are built as a plain pad — 1 mm in one panelisation example, with no hole — that simply has the solder mask expanded over it.[127][239] Older wave-soldered assemblies used enormous openings with no mask between pins whatsoever, and had no bridging trouble doing so.[1111] One such board prompted the observation that "This has to be the world's largest solder mask expansion."[1111]

## Reading shorts under fine-pitch packages

Absence of expansion explains a recurring diagnostic puzzle. Where a manufacturer has removed the mask under a quad flat pack as one large square, adjacent pins sit on bare board with no mask sliver between them.[1353] A designer routing a trace between two pads — a long-standing and legitimate practice — then produces what looks on inspection like a solder short.[1353] The tell is position combined with mask state: a bridge sitting precisely in the centre of the pads on a package with no mask expansion is almost certainly a deliberate connection rather than an assembly defect, and this is a common design technique.[1353] It remains poor layout practice, since the trace could have been routed around the package once it was known that no mask expansion would be present.[1353]

## Fabrication and tolerance

Mask expansion is a designer's decision, not a fabricator's. A board house is entitled to make minor adjustments where process requires it — a specified 1 mm finished hole may be drilled at 1.05 or 1.1 mm to allow for plating — but altering solder mask expansion, enlarging pads, or removing ground fill falls outside that latitude.[500] The board should be manufactured as sent.[500]

Realised expansion also depends on mask quality. Cheaper prototype boards use a dot-matrix-printed mask rather than a photo-imageable one, giving thick, coarse outlines; alignment around the pad can still be good enough that a thin sliver of mask survives between pins, which is acceptable for a prototype.[997] Comparisons between low-cost fabricators show cases where the mask was neither expanded nor broken between pads, and cases of imperfect registration that nonetheless did not encroach on the pad.[241]
