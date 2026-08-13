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
| candidate concepts (>=5 videos) | 6,060 |
| isolated (no surviving edge), dropped | 1,019 |
| **nodes in graph** | **5,041** |
| raw candidate edges | 178,586 |
| edges after weight>=2 | 28,471 |
| **edges after top-8 prune** | **17,901** |
| hierarchy (broader) edges | 322 |
| communities | 58 |

Node types: component 1418, tool-equipment 822, concept-principle 744, technique 675, company-product 388, manufacturing 307, standard-protocol 219, software 189

## Largest communities

| # | size | members (most-covered first) |
|---|---|---|
| 18 | 525 | `oscilloscope`, `sample-rate`, `oscilloscope-bandwidth`, `bnc-connector`, `oscilloscope-probe`, `keysight`, `function-generator`, `agilent`, `rigol`, `ac-coupling` |
| 51 | 367 | `usb`, `ethernet`, `serial-port`, `wi-fi`, `hdmi`, `rs-232`, `bluetooth`, `sd-card`, `usb-c`, `hard-drive` |
| 13 | 356 | `microcontroller`, `firmware`, `analog-to-digital-converter`, `fpga`, `adc`, `texas-instruments`, `ram`, `flash-memory`, `memory`, `jtag` |
| 40 | 343 | `resistor`, `led`, `diode`, `transistor`, `op-amp`, `voltage-reference`, `integrated-circuit`, `trimmer-potentiometer`, `potentiometer`, `pwm` |
| 29 | 309 | `multimeter`, `calibration`, `current-measurement`, `fluke`, `current-shunt-resistor`, `resistance-measurement`, `voltage-measurement`, `capacitance-measurement`, `auto-ranging`, `backlight` |
| 22 | 306 | `pcb`, `lcd`, `ribbon-cable`, `processor`, `flat-flex-cable`, `connector`, `lcd-display`, `shielding`, `speaker`, `board-to-board-interconnect` |
| 20 | 269 | `power-supply`, `heat-sink`, `voltage-regulator`, `switch-mode-power-supply`, `cooling-fan`, `short-circuit`, `fan`, `temperature-sensor`, `linear-regulator`, `motherboard` |
| 1 | 263 | `relay`, `transformer`, `fuse`, `bridge-rectifier`, `input-protection`, `common-mode-choke`, `metal-oxide-varistor`, `filter-capacitor`, `current-shunt`, `optocoupler` |
| 47 | 262 | `pcb-layout`, `solder-mask`, `bypass-capacitor`, `ground-plane`, `pcb-trace`, `bga`, `silkscreen`, `double-sided-pcb`, `via`, `single-sided-pcb` |
| 46 | 241 | `solar-panel`, `kickstarter`, `electric-vehicle`, `inverter`, `solar-cell`, `solar-roadways`, `solar-power-system`, `prototype`, `series-connection`, `solar-power` |
| 37 | 222 | `soldering`, `surface-mount-technology`, `soldering-iron`, `hand-soldering`, `solder-joint`, `microscope`, `reflow-soldering`, `through-hole-technology`, `through-hole-component`, `pick-and-place-machine` |
| 4 | 205 | `capacitor`, `inductor`, `electrolytic-capacitor`, `dc-dc-converter`, `switch`, `ceramic-capacitor`, `equivalent-series-resistance`, `capacitance`, `tantalum-capacitor`, `lcr-meter` |
| 3 | 199 | `camera`, `microphone`, `motor`, `sensor`, `macro-lens`, `accelerometer`, `color-temperature`, `o-ring`, `o-ring-seal`, `image-sensor` |
| 31 | 198 | `battery`, `battery-life`, `battery-capacity`, `aa-battery`, `battery-pack`, `lithium-ion-battery`, `9-volt-battery`, `electronic-load`, `battery-charging`, `alkaline-battery` |
| 16 | 153 | `youtube`, `eevblog-forum`, `twitter`, `webcam`, `eevblog`, `video-editing`, `frame-rate`, `google`, `4k-video`, `eevblog-store` |
| 50 | 151 | `schematic`, `service-manual`, `breadboard`, `open-source-hardware`, `reverse-engineering`, `test-point`, `ground`, `open-source-software`, `user-manual`, `troubleshooting` |
| 32 | 137 | `datasheet`, `mosfet`, `digi-key`, `bill-of-materials`, `component-sourcing`, `mouser`, `sot-23`, `power-resistor`, `aliexpress`, `current-sensing` |
| 19 | 110 | `ebay`, `teardown`, `test-equipment`, `jaycar`, `repair`, `amazon`, `electrostatic-discharge`, `electronics`, `electronics-kit`, `electronics-australia` |
| 55 | 86 | `arduino`, `raspberry-pi`, `3d-printing`, `stepper-motor`, `3d-printer`, `injection-molding`, `rs-485`, `artificial-intelligence`, `laser-cutting`, `makerbot` |
| 41 | 70 | `antenna`, `gps`, `patent`, `apple`, `smartphone`, `samsung`, `receiver`, `rfi`, `infrared`, `ibm` |

Build time 4s.
