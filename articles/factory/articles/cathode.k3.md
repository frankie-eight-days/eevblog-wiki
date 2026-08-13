# cathode

The cathode is the electrode from which electrons enter a device: in vacuum tubes it is the heated electron source, and in semiconductor diodes it is the terminal toward which conventional current flows (the negative end in forward conduction).[524][837][1747] Because the cathode's identity determines correct polarity, emission behaviour, and in many vacuum devices the service life of the part, it is one of the most frequently checked terminals on the bench.[682][1676]

## Thermionic cathodes

In thermionic vacuum devices a heater (filament) raises the cathode temperature until electrons boil off its surface; a positive anode then attracts them, establishing electron flow from cathode to anode — opposite in sense to conventional current flow.[837][524] In a typical valve, a 6 V heater heats the cathode, and the emitted electrons pass through the control, screen, and suppressor grids to the plate (anode) when grid voltages permit; valves can be thought of as "JFETs with pilot lights".[837] This thermionic emission principle is the same one used in the electron gun of a linear accelerator, where the heated cathode's output is injected into the accelerator structure.[836]

Cathode temperature has direct operational consequences:

- **Warm-up time.** A valve only conducts properly once its cathode is hot; data sheets specify cathode heating time explicitly — one example gives 12 seconds nominal, 18 seconds maximum. A cathode still hot from recent operation restores function almost immediately after a brief power interruption.[837]
- **Under-running the filament.** Running a nominally 6.3 V filament slightly low, around 5.5 V, is a deliberate practice in some preamplifier designs, but running too far under risks stripping the thorium coating off the cathode.[629]

## Cathodes in beam and display devices

- **Cathode ray tubes.** A heater warms the cathode, and the emitted electrons are accelerated into a beam by the high-voltage anode — typically 5 to 20 kV, connected via the insulated plug on the side of the CRT envelope and protected by a shield over the wiring.[524]
- **Vacuum fluorescent displays.** The cathode consists of tungsten wires strung across the top of the display (commonly two, with three used on taller devices), driven with an AC voltage that heats them so they emit electrons toward fluorescent anode segments; the structure works exactly like an old-school triode valve.[1601][717] The cathode pins sit at opposite ends of the glass and are the easiest pins to identify when reverse-engineering a pinout.[717]
- **Nixie tubes.** These are cold-cathode devices: a mesh anode receives the positive voltage, and the shaped digit electrodes are the cathodes, glowing when given sufficient negative voltage and current. The fill gas is mostly neon, often with mercury and possibly argon, so each digit behaves like a small neon lamp.[948]
- **Travelling wave tubes.** A TWT is a velocity-modulated tube built around a cathode with a filament; electrons shot from the cathode travel the length of the tube, through a helix structure, to the anode (collector), with the cathode-to-anode voltage serving as the acceleration voltage.[XqakD0dXdjM]
- **Image intensifier tubes.** A cathode at the front face and a fluorescent screen at the back, run at roughly 14 kV, form the core of a night-vision tube, with optics required on both faces.[618]
- **Cesium beam tubes.** In a cesium frequency standard, about 7.2–7.5 g of cesium is coated onto the cathode at the bottom of the tube and is gradually boiled off over the tube's life, transferring to the anode; once the cesium is exhausted the tube must be replaced, and ageing tubes grow noisier.[423]

## Semiconductor diodes: identifying the cathode

On through-hole diodes the cathode is marked with a band; on SMD parts it is the end carrying the printed line(s).[aQ2AVLs8_7k][1306] Colour coding is not universal — a green line may or may not be present — so the band alone is the reliable indicator, and on some packages the cathode end is the one closer to the internal die.[1306] Schematically the cathode is marked with a K even though the word is spelled with a C: "cathode is marked with a K, and it's spelled with a C".[1747]

Getting the cathode orientation wrong is a real assembly failure mode: a Zener diode soldered in backwards, with its banded cathode end toward a base that should have seen the anode, is enough to stop a timer circuit working.[1676] When testing a bridge rectifier in circuit, the two diodes whose cathodes join the positive output terminal should each show a roughly half-volt diode drop from the AC inputs to that terminal; anything else indicates damage.[682] Handheld LCR/component testers with a diode mode can identify anode and cathode directly, displaying which probe corresponds to which terminal, though units with low test voltage cannot light or measure LEDs at all.[81]