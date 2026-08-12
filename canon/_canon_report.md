# Canonicalisation report — EEVblog concept census

Source: /Users/frankwalsh/Documents/vibecoding/eevblog_wiki/census/captions-v1, /Users/frankwalsh/Documents/vibecoding/eevblog_wiki/census/full-v1 (2,064 videos, 181,561 mentions).
Additive layer; no census file was modified.

## Headline

| metric | value |
|---|---|
| raw distinct concept strings | 56,457 |
| canonical concepts | 53,087 |
| compression | 6.0% fewer entries |
| total mentions (unchanged) | 181,561 |
| concepts in >=10 videos | 1,699 |
| singletons (1 mention, no alias) | 34,918 |
| `broader` relations recorded | 5,647 |

## Stages

| stage | method | result |
|---|---|---|
| 1 hygiene | junk `type` remapped to the canonical 16; leaked `depth` reset | 60 fixes |
| 2 normalise | case / unicode / punctuation / whitespace fold | folded into stage 3 |
| 3 variants | plural + hyphen + spacing, only when both forms observed | 672 pairs |
| 4 embeddings | `text-embedding-3-small`, cosine >= 0.8, top-25 neighbours | 40,659 candidates |
| 5 rule merge | identical stemmed token sequence + compatible type | 210 pairs |
| 6 rule reject | differing digit signature, or both-singleton below 0.86 | 21,031 pairs |
| 7 acronym | deterministic initials match (embeddings are blind to these) | 419 pairs |
| 8 adjudication | `gpt-5.6-luna`, effort low, 60/request | 19,337 pairs, $0.69 |

An acronym gets exactly one expansion: the highest-mention one, plus spelling
variants of it. 3601 homonym expansions were rejected this way
(full list in `_acronym_rejects.json`).

## Biggest merge clusters

| canonical | type | videos | mentions | aliases | sample |
|---|---|---|---|---|---|
| `multimeter` | tool-equipment | 390 | 874 | 5 | `compact-multimeter`, `electrical-multimeter`, `precision-multimeter`, `system-multimeter`, `systems-multimeter` |
| `inductor` | component | 183 | 290 | 3 | `induction-coil`, `inductive-coil`, `inductor-coil` |
| `surface-mount-technology` | manufacturing | 132 | 160 | 3 | `surface-mount`, `surface-mount-assembly`, `surface-mount-construction` |
| `bridge-rectifier` | component | 126 | 199 | 5 | `diode-bridge`, `diode-bridge-rectifier`, `full-bridge-rectifier`, `full-wave-bridge-rectifier`, `full-wave-diode-bridge` |
| `pcb-layout` | technique | 125 | 191 | 4 | `pcb-layout-design`, `pcb-layout-engineering`, `pcb-layout-practice`, `printed-circuit-board-layout` |
| `sample-rate` | concept-principle | 120 | 207 | 3 | `effective-sample-rate`, `sampling-frequency`, `sampling-rate` |
| `solar-panel` | component | 88 | 395 | 3 | `photovoltaic-module`, `photovoltaic-panel`, `solar-module` |
| `flat-flex-cable` | component | 88 | 142 | 4 | `flat-flex-ribbon`, `flat-flex-ribbon-cable`, `flat-flexible-cable`, `flexible-flat-cable` |
| `lithium-ion-battery` | component | 85 | 142 | 3 | `lithium-ion-polymer-battery`, `lithium-polymer-battery`, `rechargeable-lithium-ion-battery` |
| `touchscreen` | component | 70 | 122 | 4 | `touch-screen`, `touch-screen-monitor`, `touchscreen-display`, `touchscreen-monitor` |
| `waveform` | concept-principle | 70 | 90 | 3 | `waveform-software`, `waveforms`, `waveforms-software` |
| `reflow-soldering` | manufacturing | 68 | 102 | 7 | `infrared-reflow`, `infrared-reflow-soldering`, `pcb-reflow-soldering`, `reflow-soldering-practice`, `smd-reflow`, `smd-reflow-soldering` |
| `eevblog-forum` | community-event | 65 | 78 | 3 | `eevblog-forums`, `evblog-forum`, `evblog-forums` |
| `current-shunt` | component | 63 | 84 | 3 | `current-measurement-shunt`, `current-sense-shunt`, `current-sensing-shunt` |
| `desoldering` | technique | 61 | 74 | 3 | `component-desoldering`, `desoldering-technique`, `solder-removal` |
| `motherboard` | component | 60 | 80 | 5 | `main-board`, `main-pcb`, `mainboard`, `mains-board`, `mains-pcb` |
| `trimmer-potentiometer` | component | 59 | 76 | 5 | `carbon-trimmer-potentiometer`, `carbon-trimmer-resistor`, `fine-trim-potentiometer`, `potentiometer-trimmer`, `trim-potentiometer` |
| `tactile-switch` | component | 55 | 92 | 6 | `tact-switch`, `tactile-button`, `tactile-dome`, `tactile-dome-button`, `tactile-dome-switch`, `tactile-switch-dome` |
| `single-shot-capture` | technique | 54 | 83 | 3 | `single-shot`, `single-shot-acquisition`, `single-shot-mode` |
| `oscilloscope-channel` | tool-equipment | 51 | 73 | 6 | `oscilloscope-channel-control`, `oscilloscope-channel-controls`, `oscilloscope-control`, `oscilloscope-controls`, `oscilloscope-display`, `oscilloscope-screen` |
| `sot-23` | component | 50 | 82 | 3 | `sot-23-package`, `sot23`, `sot23-package` |
| `rohde-schwarz` | company-product | 49 | 87 | 7 | `roehde-and-schwarz`, `roehde-schwarz`, `rohd-and-schwarz`, `rohd-schwarz`, `rohde-and-schwarz`, `rohe-and-schwarz` |
| `switching-regulator` | component | 42 | 58 | 4 | `power-switching-regulator`, `switch-mode-regulator`, `switch-mode-voltage-regulator`, `switching-voltage-regulator` |
| `thermal-camera` | tool-equipment | 41 | 78 | 3 | `thermal-imager`, `thermal-imaging`, `thermal-imaging-camera` |
| `pcb-manufacturing` | manufacturing | 41 | 66 | 3 | `pcb-manufacturer`, `pcb-manufacturing-process`, `pcb-production` |
| `micro-sd-card` | component | 40 | 50 | 3 | `micro-sd`, `microsd`, `microsd-card` |
| `solar-roadways` | company-product | 34 | 241 | 6 | `solar-freakin-roadways`, `solar-freaking-roadways`, `solar-road`, `solar-roads`, `solar-roadway`, `solaroads` |
| `5-volt-rail` | component | 32 | 67 | 5 | `5-v-rail`, `5-volt-power-rail`, `5v-power-rail`, `5v-rail`, `plus-5-volt-rail` |
| `bipolar-transistor` | component | 32 | 53 | 3 | `bipolar-junction-transistor`, `bjt`, `bjt-transistor` |
| `bar-graph-display` | tool-equipment | 31 | 39 | 3 | `bar-graph`, `bargraph`, `bargraph-display` |
| `isolation-transformer` | component | 30 | 34 | 3 | `isolated-transformer`, `power-isolation-transformer`, `transformer-isolator` |
| `input-fuse` | component | 29 | 31 | 3 | `incoming-fuse`, `inline-fuse`, `line-fuse` |
| `soldering-iron-tip` | tool-equipment | 28 | 91 | 3 | `bent-soldering-tip`, `point-soldering-tip`, `soldering-tip` |
| `bandwidth-limit` | technique | 27 | 40 | 3 | `bandwidth-filtering`, `bandwidth-limiter`, `bandwidth-limiting` |
| `dot-matrix-display` | component | 26 | 31 | 3 | `dot-matrix-led-display`, `led-dot-matrix-display`, `led-matrix-display` |
| `18650-battery` | component | 25 | 44 | 4 | `18650`, `18650-battery-cell`, `18650-cell`, `18650-lithium-ion-battery` |
| `solar-array` | tool-equipment | 23 | 40 | 4 | `dc-solar-array`, `photovoltaic-array`, `photovoltaic-solar-array`, `solar-panel-array` |
| `creepage-distance` | concept-principle | 22 | 38 | 5 | `clearance-and-creepage`, `creepage`, `creepage-and-clearance`, `creepage-clearance`, `pcb-creepage-and-clearance` |
| `so8-package` | component | 22 | 28 | 3 | `so-8`, `so-8-package`, `so8` |
| `hot-glue` | manufacturing | 22 | 25 | 3 | `hot-glue-adhesive`, `hot-melt-adhesive`, `hot-melt-glue` |

Run time 4252s.
