# Concept co-occurrence graph — EEVblog

Generated from /Users/frankwalsh/Documents/vibecoding/eevblog_wiki/census/captions-v1, /Users/frankwalsh/Documents/vibecoding/eevblog_wiki/census/full-v1 plus `canon/`.

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
| candidate concepts (>=5 videos) | 4,048 |
| isolated (no surviving edge), dropped | 939 |
| **nodes in graph** | **3,109** |
| raw candidate edges | 92,988 |
| edges after weight>=2 | 13,761 |
| **edges after top-8 prune** | **9,844** |
| hierarchy (broader) edges | 230 |
| communities | 48 |

Node types: component 950, tool-equipment 523, concept-principle 472, technique 392, company-product 220, manufacturing 181, standard-protocol 139, software 111

## Largest communities

| # | size | members (most-covered first) |
|---|---|---|
| 26 | 361 | `oscilloscope`, `ebay`, `sample-rate`, `bnc-connector`, `oscilloscope-bandwidth`, `oscilloscope-probe`, `agilent`, `coaxial-cable`, `sine-wave`, `keysight` |
| 39 | 298 | `resistor`, `datasheet`, `led`, `diode`, `transistor`, `mosfet`, `integrated-circuit`, `breadboard`, `ohms-law`, `ground` |
| 8 | 294 | `usb`, `firmware`, `ethernet`, `hdmi`, `rs-232`, `wi-fi`, `arduino`, `usb-c`, `bluetooth`, `open-source-hardware` |
| 13 | 284 | `multimeter`, `fuse`, `current-shunt-resistor`, `input-protection`, `fluke`, `current-measurement`, `voltage-measurement`, `resistance-measurement`, `auto-ranging`, `shielding` |
| 34 | 231 | `pcb`, `schematic`, `ground-plane`, `solder-mask`, `pcb-layout`, `bypass-capacitor`, `pcb-trace`, `service-manual`, `bill-of-materials`, `reverse-engineering` |
| 32 | 184 | `heat-sink`, `relay`, `transformer`, `bridge-rectifier`, `power-consumption`, `fan`, `cooling-fan`, `switch-mode-power-supply`, `common-mode-choke`, `linear-regulator` |
| 10 | 174 | `microcontroller`, `analog-to-digital-converter`, `fpga`, `adc`, `crystal-oscillator`, `ram`, `bga`, `flash-memory`, `memory`, `asic` |
| 4 | 162 | `capacitor`, `inductor`, `electrolytic-capacitor`, `dc-dc-converter`, `potentiometer`, `ceramic-capacitor`, `capacitance`, `oscillator`, `tantalum-capacitor`, `equivalent-series-resistance` |
| 9 | 141 | `lcd`, `ribbon-cable`, `processor`, `flat-flex-cable`, `connector`, `speaker`, `board-to-board-interconnect`, `lcd-display`, `lcd-driver`, `microphone` |
| 31 | 139 | `soldering`, `surface-mount-technology`, `soldering-iron`, `solder-joint`, `hand-soldering`, `microscope`, `reflow-soldering`, `desoldering`, `through-hole-technology`, `through-hole-component` |
| 44 | 134 | `battery`, `lithium-ion-battery`, `battery-life`, `battery-capacity`, `battery-pack`, `aa-battery`, `backlight`, `switch`, `9-volt-battery`, `alkaline-battery` |
| 16 | 128 | `solar-panel`, `kickstarter`, `inverter`, `electric-vehicle`, `solar-cell`, `solar-power`, `series-connection`, `solar-roadways`, `air-conditioning`, `solar-power-system` |
| 33 | 125 | `power-supply`, `voltage-regulator`, `short-circuit`, `current-limit`, `hard-drive`, `motherboard`, `power-rail`, `processor-board`, `electronic-load`, `bench-power-supply` |
| 25 | 75 | `op-amp`, `voltage-reference`, `calibration`, `comparator`, `differential-amplifier`, `temperature-coefficient`, `operational-amplifier`, `oscillation`, `lm324`, `output-capacitance` |
| 27 | 62 | `antenna`, `low-pass-filter`, `radio-frequency`, `filter`, `audio-amplifier`, `rf-shielding`, `pci`, `band-pass-filter`, `local-oscillator`, `sim-card` |
| 29 | 58 | `youtube`, `twitter`, `youtube-channel`, `facebook`, `mailbag`, `google`, `nasa`, `dick-smith`, `youtube-algorithm`, `gpu` |
| 21 | 48 | `i2c`, `spi`, `jtag`, `uart`, `clock-signal`, `can-bus`, `timer`, `serial-decoding`, `gpio`, `ascii` |
| 38 | 46 | `digi-key`, `texas-instruments`, `analog-devices`, `component-sourcing`, `mouser`, `buzzer`, `linear-technology`, `national-semiconductor`, `battery-terminal`, `msp430` |
| 22 | 38 | `camera`, `frame-rate`, `apple`, `electronics-lab`, `depth-of-field`, `ibm`, `white-balance`, `computer`, `autofocus`, `working-distance` |
| 17 | 34 | `3d-printing`, `product-design`, `injection-molding`, `silicon-chip`, `electronics-australia`, `form-factor`, `3d-printer`, `mechanical-engineering`, `resume`, `laser-cutting` |

Build time 2s.
