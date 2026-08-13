# transformer

A transformer is a passive component comprising two or more magnetically coupled windings that transfers AC energy between circuits, changing voltage and current levels according to its turns ratio while providing electrical isolation between primary and secondary.[279][714] It operates only on alternating current — which is why every switch-mode converter first chops its DC input back into AC before feeding it through the transformer.[1417] Transformers appear at nearly every scale of electronics, from pole-mounted substation units down to PCB-planar magnetics, and serve two fundamentally different roles: bulk power conversion and signal coupling or isolation.[2vJ0c0ioAXY][1104]

## Operating principles

The ratio of primary to secondary turns sets the voltage transformation: a 1:1 winding fed 1 V AC delivers 1 V out, while a large step-up ratio can multiply a signal enormously — an electrostatic speaker driver measured 1.1 Ω on its primary against roughly 1.5 kΩ on its secondary, a step-up of about a thousand times.[469][1150] The inverse also holds for measurement: in a step-down transformer the secondary carries the higher current and is therefore wound with visibly thicker wire, which is a quick way to identify which side is which.[1152]

Transformers are rated in VA, not watts, because winding and conductor sizing must account for apparent power — the product of volts and amps regardless of phase difference between them.[1730] Real power is dissipated only in resistances: in a transformer that means the winding resistance, since the ideal reactive (magnetic) component dissipates nothing.[1730] This winding resistance is also a practical diagnostic — a healthy small mains transformer primary typically measures in the tens of ohms, with measured examples of 45 Ω and 54 Ω on bench gear.[905][1189] A flyback primary may read much lower, around 2.2 Ω, with a secondary reading nearly a short because its turns ratio is small.[1726]

## Isolation

Physical and electrical separation between primary and secondary windings means there is no direct electrical path between the two sides — only a small amount of interwinding capacitance.[279] This property, traditionally called galvanic isolation, is exploited both for safety and for noise control.[1110][bg6QsTT0Plw] A two-pin (unearthed) supply with an isolated transformer secondary is electrically equivalent to a battery supply from an oscilloscope-grounding standpoint, which is why checking for a short between output ground and mains earth with an ohmmeter determines whether a supply is isolated.[279]

Precision instruments use transformer isolation deliberately to break ground loops: the Keithley DMM7510 uses a custom-wound toroidal transformer delivering ±6 V AC solely to isolate the analog board's grounds from the noisy switching supply grounds.[731] Similarly, multi-channel lab supplies route each channel through separate transformer secondaries and rectifiers so the channels are galvanically isolated from each other.[1174] Wideband injection transformers — essentially 1:1 transformers spanning 1 Hz to 10 MHz with CAT-rated isolation — exist specifically to inject disturbances into control loops for Bode-plot measurement without a DC connection.[1103][1104]

## Mains-voltage configuration and taps

Because transformers are wound for a specific mains voltage, equipment without a switch-mode front end is generally sold as fixed-voltage models; 115/230 V operation, where offered, is implemented either as a voltage-selection tap on the primary or as a split primary whose two coils are paralleled for 115 V or placed in series for 230 V — the series configuration roughly doubling the measured primary resistance.[166][596][1189] Multiple secondary taps supply different rails or ranges from a single core: vintage instruments tap the transformer for each AC range, and linear supplies tap the secondary to feed separate regulators.[549][1097]

A center-tapped secondary provides a ground-referenced midpoint, used, for example, to generate a differential high-voltage drive in electrostatic speakers without a separate high-voltage generator, and historically as the injection point for microphone phantom power, where the DC supply connects via a resistor to the audio transformer's center tap.[616][1150]

## Switch-mode and power-conversion roles

In switch-mode supplies the transformer is driven by a switching transistor at frequencies far above mains — a measured example ran at about 27 kHz — allowing much smaller magnetics than a 50/60 Hz transformer of equivalent power.[1301] The sharp rise and fall times and high breakdown capability of gallium-nitride switches have pushed this further, enabling extremely small, efficient converters such as 60 W adapters.[o2NxHu5Bsnk]

Transformers in UPS inverters are driven by an H-bridge of MOSFETs from the battery, with the secondary producing the AC output; in some topologies the same transformer works backwards, with the H-bridge pushing power back through it to charge the batteries, eliminating a separate charger.[504] Bidirectional hybrid solar inverters similarly pass multi-kilowatt power both ways through a single large toroidal transformer on its own heatsink.[1620] In resonant-mode converters such as the LLC, the transformer's magnetizing and leakage (resonant) inductances become deliberate circuit elements that must be designed in matched ratios, parasitics included.[1294] Series-input, parallel-output (ISOP) multi-level topologies exploit the property that paralleled transformer secondaries force the series-connected inputs to share voltage equally, giving automatic balancing across devices.[1737]

A transformer secondary is also the usual source for voltage-multiplier chains: a Cockcroft-Walton ladder multiplies the transformer's peak AC by two per stage, so a 1 kV secondary can be stacked to 10 kV or more.[469] For low-voltage doubling, however, a transformer is unnecessary overhead; a Dickson charge-pump doubler driven directly from a microcontroller pin replaces it.[473]

## Signal, sensing, and RF uses

Many transducers and interfaces are functionally transformers even when not called one:

- Ribbon microphones produce such low voltage at sub-ohm impedance that a step-up transformer with an extreme turns ratio is required to get a usable signal.[602]
- Contactless payment cards and their readers couple through air-core coils that behave as a transformer, not an RF antenna — which is why placing a passive load coil nearby corrupts the 847.5 kHz load-modulated data.[889][890]
- A current transformer is a toroidal core with many turns on the secondary and the measured conductor passing through as a single primary turn — 1 A in yields roughly 1 mA out — and multiple current transformers can be paralleled to sum currents from separate feeds.[1390]
- A metal detector's drive and sense coils on a shared ferrite rod form a transformer; nearby metal draws energy from the coupling and drops the sense-coil amplitude.[714]
- Ethernet ports use one small magnetics transformer per channel pair for isolation and common-mode rejection.[I-9dGvk3BW8]
- Small step-up transformers generate the high voltages for vacuum fluorescent display filaments and photon-counter outputs.[717][936]

## Failure modes and practical bench notes

Loose laminations vibrate at the mains frequency, producing the classic 50–60 Hz hum; switch-mode transformers can whine at audible frequencies for the same reason if their switching frequency or a subharmonic falls in the audible band.[855] Magnetizing current is sometimes palpable as vibration through the chassis of a receiver even before any secondary rail comes up.[1394]

Overvoltaging a fixed-voltage transformer burns the enamel insulation off the windings, releasing a large volume of smoke in seconds; even if the unit still works afterward, the compromised winding insulation means it should not be trusted.[1152] Thermal fuses buried in the windings are a common protection, and their absence — together with a missing primary fuse — is a recognised safety defect in cheap soldering stations.[1160][452]

On the bench, transformers foil some measurements: a transformer winding acts as a low impedance that wrecks in-circuit capacitance measurement below about 10 µF.[1474] In simulation, a transformer's galvanically isolated secondary has no DC path to ground, causing a singular-matrix error unless a ground reference is added on the secondary side.[1445] Mechanically, heavy parts such as transformers contribute to board flexure on drop, which can crack nearby ceramic capacitors.[1037] A deliberate PCB spark gap between primary and secondary provides a controlled air-gap breakdown path — tested examples held 1,000 V and sparked by 2,500 V — diverting surges across the isolation barrier.[678]