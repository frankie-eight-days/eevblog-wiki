# Concept co-occurrence graph — EEVblog

Generated from /Users/frankwalsh/Documents/vibecoding/eevblog_wiki/census/captions-v2, /Users/frankwalsh/Documents/vibecoding/eevblog_wiki/census/full-v1 plus `canon/`.

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
| candidate concepts (>=5 videos) | 4,878 |
| isolated (no surviving edge), dropped | 917 |
| **nodes in graph** | **3,961** |
| raw candidate edges | 134,473 |
| edges after weight>=2 | 21,083 |
| **edges after top-8 prune** | **13,883** |
| hierarchy (broader) edges | 331 |
| communities | 49 |

Node types: component 1187, tool-equipment 626, concept-principle 620, technique 529, company-product 272, manufacturing 238, standard-protocol 182, software 131

## Largest communities

| # | size | members (most-covered first) |
|---|---|---|
| 23 | 442 | `oscilloscope`, `sample-rate`, `oscilloscope-bandwidth`, `oscilloscope-probe`, `keysight`, `coaxial-cable`, `ac-coupling`, `bnc-connector`, `waveform`, `agilent` |
| 6 | 399 | `usb`, `firmware`, `ethernet`, `processor`, `wifi`, `rs-232`, `hdmi`, `ram`, `bluetooth`, `usb-c` |
| 17 | 360 | `resistor`, `led`, `op-amp`, `transistor`, `mosfet`, `voltage-reference`, `integrated-circuit`, `breadboard`, `trimmer-potentiometer`, `ohms-law` |
| 26 | 258 | `power-supply`, `heat-sink`, `voltage-regulator`, `power-consumption`, `cooling-fan`, `fan`, `power-rail`, `current-limit`, `power-dissipation`, `linear-regulator` |
| 7 | 257 | `microcontroller`, `analog-to-digital-converter`, `fpga`, `adc`, `i2c`, `flash-memory`, `shielding`, `memory`, `spi`, `jtag` |
| 20 | 251 | `multimeter`, `ebay`, `calibration`, `current-measurement`, `fluke`, `resistance-measurement`, `voltage-measurement`, `auto-ranging`, `capacitance-measurement`, `backlight` |
| 29 | 238 | `capacitor`, `diode`, `inductor`, `electrolytic-capacitor`, `dc-dc-converter`, `oscillator`, `ceramic-capacitor`, `capacitance`, `equivalent-series-resistance`, `tantalum-capacitor` |
| 11 | 227 | `pcb`, `lcd`, `ribbon-cable`, `flat-flex-cable`, `lcd-display`, `connector`, `speaker`, `lcd-driver`, `single-sided-pcb`, `screw` |
| 48 | 219 | `relay`, `transformer`, `fuse`, `bridge-rectifier`, `current-shunt-resistor`, `switch-mode-power-supply`, `input-protection`, `common-mode-choke`, `metal-oxide-varistor`, `optocoupler` |
| 35 | 214 | `soldering`, `surface-mount-technology`, `soldering-iron`, `surface-mount-component`, `bga`, `solder-joint`, `hand-soldering`, `user-interface`, `reflow-soldering`, `microscope` |
| 36 | 187 | `pcb-layout`, `solder-mask`, `bypass-capacitor`, `ground-plane`, `pcb-trace`, `silkscreen`, `via`, `double-sided-pcb`, `pcb-routing`, `pcb-design` |
| 28 | 179 | `battery`, `battery-life`, `battery-capacity`, `short-circuit`, `battery-pack`, `lithium-ion-battery`, `aa-battery`, `9-volt-battery`, `electronic-load`, `patent` |
| 34 | 158 | `solar-panel`, `kickstarter`, `inverter`, `electric-vehicle`, `solar-cell`, `series-connection`, `solar-power`, `solar-roadways`, `prototype`, `solar-power-system` |
| 18 | 147 | `youtube`, `eevblog-forum`, `camera`, `twitter`, `webcam`, `macro-lens`, `led-lighting`, `frame-rate`, `evblog-store`, `google` |
| 3 | 122 | `datasheet`, `schematic`, `texas-instruments`, `digi-key`, `service-manual`, `reverse-engineering`, `bill-of-materials`, `test-point`, `component-sourcing`, `mouser` |
| 37 | 61 | `motor`, `sensor`, `magnetic-field`, `accelerometer`, `coil`, `solenoid`, `dremel`, `magnet`, `artificial-intelligence`, `printer` |
| 45 | 60 | `antenna`, `power-amplifier`, `grounding`, `radio-frequency`, `ferrite`, `rfi`, `receiver`, `sim-card`, `5g`, `chassis-ground` |
| 31 | 53 | `crystal-oscillator`, `frequency-counter`, `low-pass-filter`, `phase-locked-loop`, `band-pass-filter`, `parts-per-million`, `voltage-controlled-oscillator`, `local-oscillator`, `high-pass-filter`, `rubidium-frequency-standard` |
| 46 | 24 | `bond-wire`, `silicon-chip`, `electronics-australia`, `electronics-magazine`, `mechanical-engineering`, `job-interview`, `resume`, `rf-transmitter`, `electrical-engineering`, `die` |
| 24 | 19 | `nasa`, `satellite`, `spacex`, `memory-module`, `apollo-11`, `telemetry`, `starlink`, `apollo-program`, `starship`, `rocket-engine` |

Build time 2s.
