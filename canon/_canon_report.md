# Canonicalisation report — EEVblog concept census

Source: /Users/frankwalsh/Documents/vibecoding/eevblog_wiki/census/captions-v2, /Users/frankwalsh/Documents/vibecoding/eevblog_wiki/census/full-v1 (2,064 videos, 223,239 mentions).
Additive layer; no census file was modified.

## Headline

| metric | value |
|---|---|
| raw distinct concept strings | 65,311 |
| canonical concepts | 61,280 |
| compression | 6.2% fewer entries |
| total mentions (unchanged) | 223,239 |
| concepts in >=10 videos | 2,051 |
| singletons (1 mention, no alias) | 39,738 |
| `broader` relations recorded | 7,033 |

## Stages

| stage | method | result |
|---|---|---|
| 1 hygiene | junk `type` remapped to the canonical 16; leaked `depth` reset | 77 fixes |
| 2 normalise | case / unicode / punctuation / whitespace fold | folded into stage 3 |
| 3 variants | plural + hyphen + spacing, only when both forms observed | 759 pairs |
| 4 embeddings | `text-embedding-3-small`, cosine >= 0.8, top-25 neighbours | 50,675 candidates |
| 5 rule merge | identical stemmed token sequence + compatible type | 268 pairs |
| 6 rule reject | differing digit signature, or both-singleton below 0.86 | 25,929 pairs |
| 7 acronym | deterministic initials match (embeddings are blind to these) | 470 pairs |
| 8 adjudication | `gpt-5.6-luna`, effort low, 60/request | 24,380 pairs, $0.88 |

An acronym gets exactly one expansion: the highest-mention one, plus spelling
variants of it. 4074 homonym expansions were rejected this way
(full list in `_acronym_rejects.json`).

## Biggest merge clusters

| canonical | type | videos | mentions | aliases | sample |
|---|---|---|---|---|---|
| `heat-sink` | tool-equipment | 293 | 504 | 5 | `cpu-heatsink`, `external-heat-sink`, `heatsink`, `processor-heat-sink`, `thermal-heat-sink` |
| `schematic` | media-resource | 218 | 346 | 3 | `circuit-diagram`, `machine-schematic`, `schematic-diagram` |
| `bridge-rectifier` | component | 146 | 271 | 5 | `diode-bridge`, `diode-bridge-rectifier`, `discrete-bridge-rectifier`, `full-bridge-rectifier`, `full-wave-bridge-rectifier` |
| `surface-mount-technology` | manufacturing | 141 | 183 | 3 | `smt`, `smt-process`, `surface-mount` |
| `switch-mode-power-supply` | tool-equipment | 136 | 195 | 3 | `switched-mode-power-supply`, `switching-power-supply`, `switchmode-power-supply` |
| `battery-life` | concept-principle | 113 | 165 | 4 | `battery-lifespan`, `battery-lifetime`, `battery-longevity`, `battery-service-life` |
| `flat-flex-cable` | component | 108 | 192 | 4 | `flat-flex-ribbon`, `flat-flex-ribbon-cable`, `flat-flexible-cable`, `flexible-flat-cable` |
| `rs-232` | standard-protocol | 108 | 150 | 4 | `rs-232c`, `rs232`, `rs232-protocol`, `rs232c` |
| `surface-mount-component` | component | 101 | 129 | 4 | `smd`, `smd-component`, `smd-part`, `surface-mount-device` |
| `fluke` | company-product | 95 | 173 | 3 | `fluke-brand`, `fluke-corporation`, `fluke-trademark` |
| `waveform` | concept-principle | 93 | 143 | 3 | `waveform-software`, `waveforms`, `waveforms-software` |
| `solar-panel` | component | 92 | 454 | 4 | `photovoltaic-module`, `photovoltaic-panel`, `solar-module`, `solar-panel-module` |
| `trimmer-potentiometer` | component | 86 | 115 | 4 | `carbon-trimmer-potentiometer`, `potentiometer-trimmer`, `trim-potentiometer`, `trimming-potentiometer` |
| `reflow-soldering` | technique | 81 | 119 | 3 | `pcb-reflow-soldering`, `smd-reflow`, `solder-reflow` |
| `motherboard` | component | 76 | 96 | 5 | `computer-motherboard`, `main-board`, `mainboard`, `mains-board`, `pc-motherboard` |
| `double-sided-pcb` | manufacturing | 75 | 112 | 3 | `dual-layer-pcb`, `dual-sided-pcb`, `two-layer-pcb` |
| `time-base` | tool-equipment | 65 | 115 | 3 | `horizontal-time-base`, `horizontal-timebase`, `timebase` |
| `sot-23` | component | 60 | 104 | 4 | `six-pin-sot23`, `sot-23-package`, `sot23`, `sot23-package` |
| `resistor-divider` | technique | 59 | 101 | 4 | `high-voltage-resistor-divider`, `resistive-divider`, `resistive-voltage-divider`, `resistor-voltage-divider` |
| `processor-board` | component | 54 | 73 | 4 | `cpu-board`, `main-processing-board`, `main-processor-board`, `processing-board` |
| `quad-flat-package` | component | 52 | 66 | 3 | `qfp`, `qfp-package`, `quad-flat-pack` |
| `pin-header` | component | 50 | 71 | 3 | `pcb-header`, `pcb-pin-header`, `pin-header-connector` |
| `user-manual` | media-resource | 49 | 58 | 4 | `installation-manual`, `instruction-manual`, `owner-manual`, `user-guide` |
| `thermal-camera` | tool-equipment | 48 | 86 | 6 | `flir-camera`, `flir-infrared-camera`, `flir-thermal-camera`, `flir-thermal-imaging-camera`, `infrared-thermal-camera`, `thermal-imaging-camera` |
| `4000-series-cmos` | component | 44 | 60 | 4 | `4000-cmos`, `4000-series-cmos-logic`, `4000-series-logic`, `cd4000-series-cmos` |
| `5-volt-rail` | component | 42 | 91 | 4 | `5-v-rail`, `5-volt-power-rail`, `5v-rail`, `plus-5-volt-rail` |
| `webcam` | tool-equipment | 42 | 52 | 3 | `usb-camera`, `usb-webcam`, `webcam-camera` |
| `pcb-assembly` | manufacturing | 42 | 47 | 3 | `circuit-board-assembly`, `pcba`, `printed-circuit-board-assembly` |
| `bar-graph-display` | tool-equipment | 41 | 56 | 4 | `bar-graph`, `bar-graph-indicator`, `bargraph`, `bargraph-display` |
| `micro-sd-card` | component | 41 | 53 | 3 | `micro-sd`, `microsd`, `microsd-card` |
| `led-backlight` | component | 39 | 60 | 4 | `backlight-led`, `backlit-led`, `lcd-backlight`, `led-backlighting` |
| `microampere` | concept-principle | 37 | 43 | 5 | `microamp`, `microamp-current-measurement`, `microamp-measurement`, `microampere-current-measurement`, `microampere-measurement` |
| `solar-roadways` | company-product | 36 | 320 | 5 | `solar-freakin-roadways`, `solar-freaking-roadways`, `solar-highway`, `solar-road`, `solar-roadway` |
| `usb-flash-drive` | tool-equipment | 36 | 48 | 5 | `usb-drive`, `usb-memory`, `usb-memory-stick`, `usb-stick`, `usb-thumb-drive` |
| `soldering-tip` | tool-equipment | 35 | 117 | 7 | `fine-point-soldering-tip`, `fine-soldering-tip`, `modern-soldering-iron-tip`, `pace-soldering-tip`, `solder-tip`, `soldering-iron-contact-tip` |
| `solar-power-system` | tool-equipment | 35 | 93 | 5 | `photovoltaic-solar`, `photovoltaic-system`, `solar-panel-system`, `solar-photovoltaic-system`, `solar-pv` |
| `serial-decoding` | technique | 33 | 54 | 3 | `hardware-serial-decoding`, `serial-communication-decoding`, `serial-data-decoding` |
| `oscilloscope-memory-depth` | tool-equipment | 33 | 49 | 3 | `deep-memory-oscilloscope`, `long-memory-oscilloscope`, `oscilloscope-deep-memory` |
| `bandwidth-limit` | technique | 33 | 45 | 3 | `bandwidth-limitation`, `bandwidth-limiting`, `frequency-bandwidth-limit` |
| `3-3v-rail` | component | 31 | 62 | 4 | `3-3-v-rail`, `3-3-volt-power-rail`, `3-3-volt-rail`, `3.3v-rail` |

Run time 5303s.
