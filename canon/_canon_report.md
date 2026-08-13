# Canonicalisation report — EEVblog concept census

Source: census/captions-v2, census/full-v2 (2,846 videos, 275,643 mentions).
Additive layer; no census file was modified.

## Headline

| metric | value |
|---|---|
| raw distinct concept strings | 79,095 |
| canonical concepts | 73,874 |
| compression | 6.6% fewer entries |
| total mentions (unchanged) | 275,643 |
| concepts in >=10 videos | 2,661 |
| singletons (1 mention, no alias) | 47,812 |
| `broader` relations recorded | 6,850 |

## Stages

| stage | method | result |
|---|---|---|
| 1 hygiene | junk `type` remapped to the canonical 16; leaked `depth` reset | 99 fixes |
| 2 normalise | case / unicode / punctuation / whitespace fold | folded into stage 3 |
| 3 variants | plural + hyphen + spacing, only when both forms observed | 1,012 pairs |
| 4 embeddings | `text-embedding-3-small`, cosine >= 0.8, top-25 neighbours | 64,755 candidates |
| 5 rule merge | identical stemmed token sequence + compatible type | 0 pairs |
| 6 rule reject | differing digit signature, or both-singleton below 0.86 | 17,985 pairs |
| 7 acronym | deterministic initials match (embeddings are blind to these) | 551 pairs |
| 8 adjudication | `gpt-5.6-luna`, effort low, 60/request | 46,566 pairs, $1.65 |

An acronym gets exactly one expansion: the highest-mention one, plus spelling
variants of it. 5393 homonym expansions were rejected this way
(full list in `_acronym_rejects.json`).

## Biggest merge clusters

| canonical | type | videos | mentions | aliases | sample |
|---|---|---|---|---|---|
| `power-supply` | tool-equipment | 517 | 898 | 3 | `power-supply-circuit`, `power-supply-circuitry`, `power-supply-unit` |
| `heat-sink` | tool-equipment | 356 | 592 | 6 | `computer-heatsink`, `cpu-heatsink`, `custom-heat-sink`, `custom-heatsink`, `heatsink`, `processor-heat-sink` |
| `schematic` | media-resource | 277 | 423 | 5 | `circuit-diagram`, `circuit-schematic`, `electrical-schematic`, `electronic-schematic`, `schematic-diagram` |
| `fpga` | component | 211 | 511 | 6 | `field-programmable-gate-array`, `fpga-data-sheet`, `fpga-datasheet`, `fpga-i-o`, `fpga-io`, `fpgas` |
| `switch-mode-power-supply` | component | 207 | 292 | 7 | `isolated-switch-mode-power-supply`, `switch-mode-converter`, `switch-mode-power-converter`, `switched-mode-power-supply`, `switching-converter`, `switching-power-supply` |
| `solder-mask` | manufacturing | 202 | 329 | 3 | `pcb-solder-mask`, `red-solder-mask`, `solder-mask-pcb` |
| `dc-dc-converter` | component | 182 | 296 | 6 | `ac-dc`, `ac-dc-conversion`, `ac-dc-converter`, `ac-to-dc-conversion`, `ac-to-dc-converter`, `dc-to-dc-converter` |
| `bridge-rectifier` | component | 178 | 322 | 5 | `diode-bridge`, `diode-bridge-rectifier`, `discrete-bridge-rectifier`, `full-bridge-rectifier`, `full-wave-bridge-rectifier` |
| `serial-port` | standard-protocol | 161 | 209 | 3 | `serial-communications-interface`, `serial-interface`, `serial-port-interface` |
| `battery-life` | concept-principle | 155 | 240 | 6 | `battery-lifespan`, `battery-lifetime`, `battery-longevity`, `battery-operating-life`, `battery-runtime`, `battery-service-life` |
| `crystal-oscillator` | component | 144 | 212 | 5 | `crystal-controlled-oscillator`, `oven-controlled-crystal-oscillator`, `ovenized-crystal-oscillator`, `quartz-crystal-oscillator`, `quartz-oscillator` |
| `solar-panel` | component | 133 | 613 | 4 | `photovoltaic-module`, `photovoltaic-panel`, `solar-module`, `solar-panel-module` |
| `flat-flex-cable` | component | 131 | 226 | 5 | `flat-cable`, `flat-flex-ribbon`, `flat-flex-ribbon-cable`, `flat-flexible-cable`, `flexible-flat-cable` |
| `rs-232` | standard-protocol | 129 | 177 | 4 | `rs-232c`, `rs232`, `rs232-protocol`, `rs232c` |
| `silkscreen` | manufacturing | 127 | 185 | 6 | `pcb-silk-screen`, `pcb-silkscreen`, `silk-screen`, `silk-screen-printing`, `silk-screening`, `silkscreening` |
| `solder-joint` | component | 111 | 175 | 7 | `bad-solder-joint`, `cold-solder-joint`, `dry-solder-joint`, `poor-solder-joint`, `solder-connection`, `solder-junction` |
| `waveform` | concept-principle | 108 | 167 | 3 | `waveform-software`, `waveforms`, `waveforms-software` |
| `trimmer-potentiometer` | component | 105 | 137 | 7 | `10-turn-trimmer`, `10-turn-trimmer-potentiometer`, `carbon-trimmer-potentiometer`, `gain-trim-potentiometer`, `potentiometer-trimmer`, `trim-potentiometer` |
| `double-sided-pcb` | manufacturing | 101 | 139 | 4 | `double-layer-pcb`, `dual-layer-pcb`, `dual-sided-pcb`, `two-layer-pcb` |
| `reflow-soldering` | technique | 98 | 139 | 6 | `infrared-reflow`, `infrared-reflow-soldering`, `pcb-reflow-soldering`, `solder-paste-reflow`, `solder-reflow`, `surface-mount-reflow-soldering` |
| `firmware-update` | software | 94 | 137 | 4 | `device-firmware-upgrade`, `field-firmware-update`, `firmware-updating`, `software-firmware-update` |
| `motherboard` | component | 84 | 105 | 5 | `computer-motherboard`, `main-board`, `mainboard`, `mains-board`, `mains-power-board` |
| `arbitrary-waveform-generator` | tool-equipment | 71 | 139 | 3 | `arbitrary-function-waveform-generator`, `awg`, `awg-wire-gauge` |
| `sot-23` | component | 70 | 114 | 3 | `sot-23-package`, `sot23`, `sot23-package` |
| `9-volt-battery` | component | 68 | 113 | 3 | `9-v-battery`, `9v-battery`, `nine-volt-battery` |
| `battery-charging` | technique | 66 | 102 | 6 | `battery-charge-circuit`, `battery-charger-circuit`, `battery-charging-circuit`, `battery-charging-circuitry`, `battery-recharging`, `battery-recharging-circuitry` |
| `analog-oscilloscope` | tool-equipment | 65 | 159 | 3 | `analog-crt-oscilloscope`, `analogue-oscilloscope`, `crt-oscilloscope` |
| `rohde-and-schwarz` | company-product | 65 | 114 | 3 | `roehde-and-schwarz`, `roehde-schwarz`, `rohde-schwarz` |
| `test-equipment` | tool-equipment | 65 | 82 | 3 | `test-and-measurement-equipment`, `test-gear`, `testing-equipment` |
| `pcb-assembly` | manufacturing | 65 | 75 | 3 | `circuit-board-assembly`, `pcba`, `printed-circuit-board-assembly` |
| `thermal-camera` | tool-equipment | 63 | 104 | 7 | `flir-camera`, `flir-infrared-camera`, `flir-thermal-camera`, `flir-thermal-imaging-camera`, `infrared-thermal-camera`, `thermal-imager` |
| `quad-flat-package` | component | 63 | 80 | 3 | `qfp`, `qfp-package`, `quad-flat-pack` |
| `rigol-oscilloscope` | tool-equipment | 61 | 116 | 5 | `rigol-2000`, `rigol-2000-oscilloscope`, `rigol-2000-series`, `rigol-2000-series-oscilloscope`, `rigol-ds2000` |
| `resistor-divider` | technique | 60 | 100 | 3 | `resistive-divider`, `resistive-voltage-divider`, `resistor-voltage-divider` |
| `user-manual` | media-resource | 60 | 71 | 3 | `instruction-manual`, `owner-manual`, `user-guide` |
| `surface-mount-device` | component | 60 | 70 | 4 | `smd`, `smd-component`, `smd-device`, `smd-part` |
| `pin-header` | component | 59 | 82 | 3 | `pcb-header`, `pcb-pin-header`, `pin-header-connector` |
| `5-volt-rail` | component | 57 | 110 | 6 | `5-v-rail`, `5-volt-power-rail`, `5v-rail`, `five-volt-power-rail`, `five-volt-rail`, `five-volt-supply-rail` |
| `processor-board` | component | 57 | 76 | 3 | `cpu-board`, `main-processing-board`, `main-processor-board` |
| `micro-sd-card` | component | 57 | 71 | 3 | `micro-sd`, `microsd`, `microsd-card` |

Run time 9425s.
