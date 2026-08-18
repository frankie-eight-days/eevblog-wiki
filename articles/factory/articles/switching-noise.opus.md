# switching noise

Switching noise is the high-frequency disturbance a switch-mode converter injects onto its own output, onto the rails around it, and into the space near it, as a consequence of the hard-edged switching that makes the converter efficient in the first place.[324][1122] It is effectively universal with DC-to-DC converters: the mechanism is inherent to the topology rather than a defect of a particular sample.[324] It matters because it lands on precisely the rails that sensitive analog and sampling circuitry depends on, and because it sits far above the low-frequency ripple that supply specifications usually quote, so it is easy to miss and easy to underestimate.[1265][324]

## Where it comes from

The switching element itself is the source. In an isolated DC-to-DC converter the coupling path is the parasitic capacitance between the primary and secondary windings of the internal transformer, and that capacitance largely determines how much switching noise reaches the output — shorting primary to secondary makes the noise vanish.[324] A switching step-down regulator on a small add-on board produces the same signature, high-frequency switching riding on the output.[1122] Switched-capacitor converters are no exception: a classic 7660-style inverter generating −3 V from +3 V is a switching element and generates switching noise that must be filtered and budgeted for.[72] Even a mains light dimmer counts, the switching triac being the noise source.[1049]

The noise is not confined to one rail. Multiple switch-mode controllers inside an instrument couple into its own analog front end and show up as internal spikes at 500 µV per division.[692] Switching elements inside a computer put visible rubbish onto the boards connected to it.[1081] Common-mode switching noise arrives through the mains input between earth and neutral, so it appears on a measurement regardless of which oscilloscope is used — it is inherent to the setup, not to the instrument.[442] Noise also radiates: the scope's own screen couples switching noise into a probe held near it, and moving a hand changes what is picked up.[765][970]

Faster devices make the problem worse. Silicon carbide switches faster than the IGBTs it displaced, and fast edges make noise when they switch; at high voltages the blazing-fast edge is not needed, so the noise is not worth paying for.[1737]

## Frequencies and amplitudes

Switching frequency is the first thing to identify, and it varies widely by design: 65 kHz on an inexpensive DIY bench supply at 3 A and 10 V output,[1030] 120 kHz on a 360 W programmable bench supply,[1691] and 315 kHz spikes from a converter inside an instrument, with the harmonics of that fundamental clearly visible in the spectrum.[1557]

The content extends far higher than the fundamental. Measured on a USB DC-to-DC converter with the oscilloscope's bandwidth limit switched off, the high-frequency component reaches beyond 70 MHz.[324] Amplitudes on a well-behaved supply are small: 137 mV peak-to-peak against 5 mV RMS at 5 V output, and around 7.5 mV RMS in constant-current mode at high current.[1691] Amplitudes on a poor one are not — a cheap regulator module produced switching noise described as absolutely horrible even under no load at 45 V output.[1265]

Specification sheets frequently understate this. A quoted 100 mV peak-to-peak figure may describe only the low-frequency ripple and say nothing at all about the switching noise sitting on top of it.[1265]

## Measuring it

Measurement technique dominates the result, and most of the classic errors inflate the number.

Bandwidth limiting is the first trap. Leaving the scope's bandwidth limit on when the noise contains tens of megahertz of content means fooling yourself about the actual level.[324] The second trap is the probe ground connection. A long ground lead is an antenna and an inductive loop; a big ground lead routed near a transformer produced an output that looked horrible, when the high-frequency switching content on screen was in fact pickup from the lead rather than anything present on the output.[1122] Replacing the lead with a low-inductance connection pushed directly into the probe point took the same measurement from roughly 600 mV peak-to-peak down to around 200 mV — the amplitude that is really there.[324]

The test equipment itself can be the source. An electronic load added switching at 142 Hz to a supply's output; swapping it for a resistive dummy load at a comparable current made the artifact vanish entirely, and only differential probing established that the noise was not coming from the supply under test.[594] The same class of error appears as 50 Hz hum contributed by an electronic load, plus minimum-load effects on the converter.[324] Careful attribution of where the noise is coming from is therefore part of the measurement, not an afterthought.[594]

Display technology affects what is seen but not what is present. Common-mode switching noise appears identically on analog and digital oscilloscopes at the same 5 mV per division sensitivity, but a digital scope reveals it more readily through its sampling and effective persistence.[442] Turning the intensity down on an analog scope produces a clean-looking flat line that hides noise which is genuinely there — an inherent advantage for the digital instrument, since the analog display invites the wrong conclusion.[442] Switching noise on the waveform can also capture the trigger intermittently, which is what makes a displayed trace jump around.[324]

Instrumentation exists to inject the disturbance deliberately: a controlled noise component of a chosen amplitude, for example 50 mV RMS at 1 kHz, can be summed onto a 3.3 V supply rail to test a circuit's tolerance, though the achievable frequency falls well short of a realistic 100 kHz switching rate.[1552]

## Reducing it

The most complete fix is to remove the switching element. A boost converter can be shut down and the load run directly from the battery through the converter's own inductor and a Schottky diode, at a cost of 0.3 to 0.4 V of diode drop and perhaps half a volt at most, plus a negligible drop across a 0.01 Ω inductor — leaving no switching noise while the circuit still operates.[259] For designs working at the microvolt level, introducing a switching element at all is a bad idea.[72] A linear pass element avoids the noise outright, at the cost of dissipation: an instrument dissipating around 14 W in its linear stages has no real switching noise to be had.[1701] The intermediate approach is a linear low-dropout regulator following a switch-mode stage to clean up the output, dissipating on the order of a watt each, which is why the presence of an LDO can often be inferred from a product's switching noise figures.[875]

Where the switching stays, the remedies are filtering, layout, and synchronisation:

- A common-mode choke, such as a bifilar-wound inductor presenting inductance in common mode but not differential mode, suppresses the switching noise leaving a triac dimmer. Omitting it — a common economy in the cheapest units — leaves the product to radiate and conduct that interference outward.[1049]
- Ground planes, loop area, and how grounds relate to the switching elements are decisive; a board that crosses ground domains without a plane is where these effects show up most clearly.[1081]
- Layout separation matters at the routing level: an analog connector placed in the middle of a group of DC-to-DC converters may require extra board layers so the signal can be run through an internal channel, away from the switching noise.[810]
- Synchronising a converter's switching clock to a system's sampling clock, rather than letting it free-run at an arbitrary frequency, allows an ADC to reject the switching frequencies rather than alias them into the measurement.[1115]
- Additional output filtering can be added to a rough supply if the application warrants it.[1030]

Downstream circuits can filter what remains. A low-pass filter ahead of a current-sense amplifier removes switching and transient noise contributed by the loads,[259] and a 1 kHz low-pass filter mode on a multimeter serves the same purpose for a measurement.[249]

One unusual sensitivity is that the switching components themselves — multilayer ceramic capacitors and inductors — respond to physical vibration, and mechanically exciting a supply changes its output noise. Around 250 Hz the measured noise fell to about 1.3 mV peak-to-peak, substantially lower than at neighbouring excitation frequencies.[1607]

## Design judgment

Whether switching noise matters at all is an application question, and it belongs on the selection checklist alongside switching frequency, footprint, power-good outputs, reference stability over temperature, and transient response. For many applications the answer is that it is simply not critical.[139]

Where it does matter, sourcing is the practical lever. Load-dependent behaviour is characteristic: an unbranded "one-hung low" plug pack produced no switching noise at all with no load, and gross noise the moment it was loaded down, which is what made it the culprit behind noise from a set of LED light panels while a quality plug pack driving the same panels caused no problem whatsoever.[765] The engineering conclusion drawn consistently is that anonymous, unbranded switching supplies of this kind are not fit to power anything sensitive.[765][1265]
