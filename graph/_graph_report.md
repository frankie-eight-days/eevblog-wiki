# Concept co-occurrence graph — EEVblog

Generated from census/captions-v2, census/full-v2 plus `canon/`.

## Build parameters

| parameter | value |
|---|---|
| min videos per node | 5 |
| co-occurrence window | +/- 2 paragraphs |
| edge weight | distinct videos co-occurring |
| min edge weight | 2 |
| top-K prune per node | 8 |
| Louvain resolution | 1.6 |

## Counts

| metric | value |
|---|---|
| candidate concepts (>=5 videos) | 6,062 |
| isolated (no surviving edge), dropped | 1,020 |
| **nodes in graph** | **5,042** |
| raw candidate edges | 178,610 |
| edges after weight>=2 | 28,456 |
| **edges after top-8 prune** | **17,898** |
| hierarchy (broader) edges | 322 |
| communities | 57 |

Node types: component 1419, tool-equipment 822, concept-principle 744, technique 675, company-product 388, manufacturing 307, standard-protocol 219, software 189

## Largest communities

| # | size | members (most-covered first) |
|---|---|---|
| 29 | 524 | `oscilloscope`, `sample-rate`, `oscilloscope-bandwidth`, `oscilloscope-probe`, `keysight`, `function-generator`, `agilent`, `rigol`, `ac-coupling`, `bandwidth` |
| 38 | 465 | `resistor`, `capacitor`, `led`, `diode`, `inductor`, `voltage-regulator`, `transistor`, `op-amp`, `integrated-circuit`, `connector` |
| 52 | 379 | `usb`, `ethernet`, `serial-port`, `wi-fi`, `hdmi`, `rs-232`, `arduino`, `bluetooth`, `sd-card`, `usb-c` |
| 34 | 373 | `microcontroller`, `analog-to-digital-converter`, `fpga`, `adc`, `processor`, `voltage-reference`, `ram`, `flash-memory`, `memory`, `jtag` |
| 35 | 346 | `pcb`, `pcb-layout`, `solder-mask`, `bypass-capacitor`, `ground-plane`, `pcb-trace`, `bga`, `silkscreen`, `breadboard`, `double-sided-pcb` |
| 27 | 326 | `multimeter`, `calibration`, `bnc-connector`, `current-measurement`, `fluke`, `resistance-measurement`, `voltage-measurement`, `capacitance-measurement`, `auto-ranging`, `backlight` |
| 17 | 298 | `relay`, `transformer`, `fuse`, `electrolytic-capacitor`, `bridge-rectifier`, `input-protection`, `common-mode-choke`, `metal-oxide-varistor`, `filter-capacitor`, `current-shunt` |
| 32 | 286 | `power-supply`, `heat-sink`, `switch-mode-power-supply`, `power-consumption`, `dc-dc-converter`, `cooling-fan`, `short-circuit`, `fan`, `temperature-sensor`, `linear-regulator` |
| 53 | 280 | `youtube`, `camera`, `eevblog-forum`, `microscope`, `twitter`, `webcam`, `macro-lens`, `eevblog`, `video-editing`, `led-driver` |
| 18 | 240 | `solar-panel`, `kickstarter`, `electric-vehicle`, `inverter`, `solar-cell`, `solar-roadways`, `solar-power-system`, `prototype`, `series-connection`, `solar-power` |
| 33 | 211 | `lcd`, `ribbon-cable`, `flat-flex-cable`, `lcd-display`, `shielding`, `board-to-board-interconnect`, `seven-segment-display`, `lcd-driver`, `display`, `rotary-encoder` |
| 41 | 211 | `soldering`, `surface-mount-technology`, `soldering-iron`, `hand-soldering`, `solder-joint`, `reflow-soldering`, `through-hole-technology`, `through-hole-component`, `pick-and-place-machine`, `heat-shrink` |
| 48 | 191 | `firmware`, `schematic`, `service-manual`, `open-source-hardware`, `reverse-engineering`, `bill-of-materials`, `firmware-update`, `software`, `test-point`, `ground` |
| 47 | 190 | `battery`, `battery-life`, `battery-capacity`, `aa-battery`, `battery-pack`, `lithium-ion-battery`, `9-volt-battery`, `electronic-load`, `battery-charging`, `alkaline-battery` |
| 25 | 102 | `mosfet`, `current-shunt-resistor`, `sot-23`, `current-sensing`, `bipolar-transistor`, `differential-amplifier`, `current-sense-resistor`, `n-channel-mosfet`, `cmos`, `npn-transistor` |
| 22 | 97 | `datasheet`, `digi-key`, `texas-instruments`, `component-sourcing`, `analog-devices`, `mouser`, `aliexpress`, `calculator`, `farnell`, `linear-technology` |
| 24 | 95 | `speaker`, `microphone`, `power-amplifier`, `audio-amplifier`, `o-ring`, `o-ring-seal`, `waterproofing`, `ferrite`, `headphone`, `loctite` |
| 45 | 93 | `ebay`, `teardown`, `test-equipment`, `jaycar`, `repair`, `amazon`, `electronics`, `electronics-kit`, `electronics-australia`, `silicon-chip` |
| 20 | 61 | `crystal-oscillator`, `frequency-counter`, `low-pass-filter`, `phase-locked-loop`, `band-pass-filter`, `pal`, `high-pass-filter`, `voltage-controlled-oscillator`, `rubidium-frequency-standard`, `parts-per-million` |
| 44 | 61 | `antenna`, `magnetic-field`, `rf-shielding`, `receiver`, `rfi`, `infrared`, `5g`, `transmitter`, `electric-field`, `near-field-communication` |

Build time 5s.
