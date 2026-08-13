# ac coupling

AC coupling is the insertion of a series capacitor into a signal path so that the AC component of a signal passes while any DC offset is blocked. It is used both as a measurement mode in instruments (oscilloscopes, multimeters, counters) and as a circuit-design technique wherever a signal riding on an unwanted DC level must be passed between stages at different bias points, such as amplifier inputs and outputs, video lines, and RF chains.[600][594][598] Its principal measurement benefit is that removing the DC content lets a small AC variation — power-supply ripple, for example — be examined at high vertical sensitivity instead of being pushed off screen by the DC level.[594][224]

## Implementation in instruments

In an oscilloscope front end, AC coupling is implemented as a physical capacitor switched into the signal path by a relay — mechanical or solid-state — which simply shorts the capacitor out again when DC coupling is selected.[1223][1761][1540][1717][1723] The switching element is frequently a Cosmo or Fujitsu solid-state relay located immediately after the BNC input and termination network, and the user often hears an audible click when toggling coupling or 50-ohm termination.[1563][1717][620] A high-value resistor to ground, typically 10 MΩ, is placed on the downstream side of the coupling capacitor to establish the DC reference for the now-floating node.[1129][675] Instruments commonly provide separate 1 MΩ and 50 Ω input paths, with the AC/DC coupling selection applied on the 1 MΩ path.[1639][1503][1545]

In classic analog oscilloscope front ends, the high-frequency amplifier chain may itself be permanently AC coupled and only able to amplify high-frequency content, with the DC component tapped off separately and recombined, because the waveform must be biased inside the front-end amplifier for vertical position control.[675]

Multimeters implement AC coupling in the AC volts function: the input signal passes through a series capacitor so that the DC component is removed before the RMS converter, which is why a meter's AC range inherently performs an AC-only (standard deviation) measurement.[1223][1667] A high-voltage-rated part may be used for this — for example, a 0.22 µF 1000 V peak capacitor directly coupling the AC input into the resistive divider and true-RMS converter.[731]

Vintage analog multimeters carried the same idea under the confusing name "output" terminal: despite the label, it was an input identical to the regular volts/ohms/amps jack but with a large series capacitor that removed any DC content.[1067][634][648][899]

## Measurement practice

For power-supply ripple and noise measurements, AC coupling is the standard setup: the DC content must be removed so the channel can be run at a few millivolts per division, in combination with bandwidth limiting.[594][224][855] With a 500 mV ripple input, for instance, a linear regulator under test showed almost identical input and output ripple at 10 kHz — roughly 60 mV peak-to-peak — a comparison only visible because both channels were AC coupled at 50 mV per division.[1116] AC coupling is likewise used to check whether a low-dropout regulator oscillates as it is pulled below its dropout voltage.[972]

For power-rail probing the opposite rule applies. AC coupling must not be used, because a power rail carries meaningful low-frequency content that the coupling capacitor strips away; DC coupling with a probe or front end that can offset the rail's DC voltage is required to use the full dynamic range of the ADC.[1735][1733] Dedicated power-rail probes exist precisely because ordinary active probes often lack input AC coupling options and cannot handle the DC offset.[1733]

A DC offset that originates *after* the instrument's coupling capacitor — internal front-end offset — is not removed by selecting AC coupling, so a residual offset can persist on screen even in AC mode; self-calibration removes such offsets.[1223] AC coupling can also introduce its own display artifacts, such as overshoot on captured digital packets.[762]

A software equivalent exists: the standard-deviation measurement on a DC-coupled channel is the AC RMS value, effectively AC coupling the signal in software while still displaying the DC offset, whereas the RMS measurement by definition includes the DC component (AC+DC mode).[1223]

## AC trigger coupling

Trigger coupling is a separate control from input coupling: AC trigger coupling removes the DC component only in the trigger path.[699][685] Its practical value appears when probing unknown circuits whose signals sit on different, unknown DC offsets — with DC trigger coupling the trigger level must be re-adjusted for every new signal, while AC trigger coupling lets a single trigger point near zero work across all of them.[685] Some oscilloscopes have exhibited severe trigger jitter specifically in AC trigger-coupling mode — on the Rigol DS1000Z and DS2000 series the jitter was inherent to the mode and could not be removed, while other scopes, including the older DS1052E, triggered cleanly.[683][699]

## Circuit design applications

AC coupling appears throughout analog and RF design:

- **Amplifiers.** Op-amp configurations are normally DC coupled, but any of them can be AC coupled by adding capacitors on the inputs and outputs.[600] Valve and audio stages are conventionally AC coupled at the output.[837][1243]
- **Microphones and audio.** An electret microphone is biased from the rail — 2.2 kΩ being the most common value — and the signal is then AC coupled into the amplifier; line inputs and headphone stages are coupled the same way.[713][271] A node after a coupling capacitor needs a defined DC reference, such as a pull-high resistor, or it floats and depends on leakage paths.[267][611]
- **Video.** Composite and analog video signals are routinely AC coupled into processing ICs, a series cap being a reliable tell on a board that a trace carries video.[598][969][1021]
- **RF.** Spectrum-analyser and signal-generator inputs are AC coupled (e.g., through a series capacitor ahead of the first switch or attenuator), and coupling capacitors bridge breaks in shielding between RF blocks.[892][1109][823] A common pattern powers a remote RF device — amplifier, transducer, receiver — through an inductor that is open circuit to RF, while the signal is tapped off through an AC coupling capacitor.[940][827][956] EMC probes and line-impedance stabilization networks AC couple conducted noise off a power line into a spectrum analyzer while the inductor presents a fixed 50 Ω impedance to the source.[1178][548][546][993]
- **High-speed digital.** USB 3.0 SuperSpeed differential pairs carry series AC coupling capacitors on the board, and Ethernet termination networks are often AC coupled to ground.[340][934]
- **Detection and feedback.** Coupling capacitors feed sampled RF back to a microcontroller for transmit-verification in an EPIRB, couple energy off a resonant oscillator for rectification in energy-harvesting front ends, and provide capacitive pickup of ambient fields.[368][664][441]

## Component selection and biasing

Ceramic capacitors are acceptable for AC coupling at input, interstage, and output positions in typical audio-frequency circuits.[827] Electrolytics remain hard to avoid where very low frequencies must pass, because of the large capacitance required in a small volume, despite their unreliability.[33] Where a DC path must coexist with the block — for example injecting a signal onto a coax line that also carries DC power — the DC feed must be lifted or the generator itself AC coupled, since the coupling capacitor otherwise blocks the injected signal or the DC upsets the source.[966]

## Limitations

Because AC coupling is a high-pass function, it discards low-frequency information along with the DC, which is precisely why it is unsuitable for power-rail integrity work.[1735] The absence of AC coupling in a low-cost instrument is regarded as a serious deficiency: a pocket oscilloscope offering DC-only coupling was judged practically useless for general signal viewing.[359] Conversely, flawed AC-coupling implementations — the Rigol trigger-path jitter being the notable example — can make the mode unusable even when present.[683]

## AC coupling in photovoltaic systems

In residential solar and battery systems, "AC coupling" has a distinct meaning: a second, independent PV system — typically microinverters — connects onto the AC bus rather than into the hybrid inverter's DC side.[1682][gAu8CvMjDrU] Because each microinverter feeds the common AC bus and is individually addressed by serial number, the hybrid inverter has no direct communication with that system; instead a current clamp on the grid connection detects excess power flowing toward the grid, and the inverter diverts that surplus into battery charging rather than exporting it.[gAu8CvMjDrU][1634][1682] On Deye hybrid inverters this behaviour is enabled as an "AC couple on grid side" mode, located in the generator-port settings, with configurable start and stop battery-capacity thresholds (e.g., 95% and 100%).[1634][gAu8CvMjDrU][BXVgk-uoxn8] The feature allows, for example, roughly 2 kW of otherwise-exported energy from a separate Enphase microinverter system to be added to the battery charge rate on top of the inverter's own array contribution.[gAu8CvMjDrU][1719] On at least one Deye configuration, enabling a microinverter (generator-port) input disables the grid-side AC coupling option, so the two cannot necessarily operate together.[BXVgk-uoxn8]