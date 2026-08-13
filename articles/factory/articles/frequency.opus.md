# frequency

Frequency is the number of cycles a repeating signal completes in one second, measured in hertz: a light that stays on for half a second and off for half a second completes one cycle per second and is therefore blinking at 1 Hz.[NvIv-0-R6qQ] It is the inverse of the time period, and the conversion between the two — t equals one over f — is one of the most fundamental relationships in all of electronics.[1417] Frequency matters far beyond describing a waveform, because almost every property of a real component and almost every failure mode of a real circuit is frequency-dependent: reactance, impedance, noise, radiated interference and measurement accuracy all move as frequency moves.[1660][1728][528][933]

## Period, angular frequency and the time domain

Because period and frequency are reciprocal, the two are interchangeable on the bench. A 1 kHz waveform has a period of essentially exactly 1 ms, and that period must be known before cursor-based phase calculations can be performed on it.[1751] A pulse train at 3.9 Hz can equally be described by its mark and space times in milliseconds, with the instrument deriving the hertz reading from them; lengthening the space lowers the frequency.[1681] Cursor deltas convert directly: a heartbeat interval measured as roughly 980 millihertz is slightly faster than 1 Hz, and so slightly above 60 beats per minute.[660]

In AC analysis frequency usually appears in angular form. Omega is simply shorthand for 2 pi f, in units of radians per second, and carries the frequency component inside every phasor expression.[1417][1469] This is why scientific calculators carry degrees, radians and gradients modes at all.[1417]

## Reactance and impedance

Inductive reactance is omega L — 2 pi times the frequency times the inductance in henries — expressed in ohms.[1660] It behaves like resistance in the sense that a larger value impedes current more, so for a given inductor, rising frequency raises the AC resistance and further impedes current flow.[1660] Capacitance inverts the same relationship: capacitive reactance is one over 2 pi times frequency times capacitance, with frequency in hertz and capacitance in farads.[1715][1660] At 1 GHz a one picofarad input capacitance is already a significant load, which is why probe input capacitance dominates high-frequency probing.[1715]

The impedance of a lumped component changes with every hertz of frequency change.[1728] The characteristic impedance of a distributed-element transmission line does not — it is broadly flat with frequency apart from a roll-off at the extreme, and conflating the two terms is an error.[1728]

## Measurement frequency and component measurement

Because component values are measured by exciting them, the measurement frequency is part of the result. An LCR meter displays impedance and phase angle at a chosen frequency, selectable from 100 Hz upwards.[757] Stray capacitance on a solderless breadboard reads about half a picofarad at 100 Hz, where it is barely measurable and down in the noise, just over 2 pF at 1 kHz, and 2.25 pF at 10 kHz.[568] Raising the frequency also buys resolution: a handheld LCR meter offering only 0.1 pF resolution at 120 Hz gains a digit at 1 kHz, reaching 10 fF, and reaches 1 fF resolution at 10 kHz.[568]

The opposite rule applies to in-circuit measurement. Large capacitors — the values realistically measurable in circuit — should be measured at the lowest frequency available, 100 Hz or 120 Hz, because raising the frequency actually makes the situation worse for large values, collapsing the signal level until nothing useful remains.[1474] Small values in circuit, such as 100 nF surrounded by active silicon, cannot be measured accurately at any frequency.[1474] Frequency dependence is also one of the layers of complexity behind ceramic capacitor behaviour, alongside voltage dependency.[626]

## Measuring frequency

A digital oscilloscope measures frequency automatically alongside peak-to-peak voltage, average value and rise and fall time, and can hold a stopped waveform for analysis after the signal has been disconnected.[926] These live in the horizontal measurement group, together with period, rise and fall time, width and duty cycle.[1751]

A frequency counter works by gating: the time between a reset pulse and the following clock-disable pulse sets a multiplier applied to the counted value, so a one-second gate yields a direct reading in hertz.[NvIv-0-R6qQ] Multimeters commonly include a frequency function, in some cases alongside simultaneous voltage and current display.[712][Iwy8UVVQNkA] A simple AC-coupled comparator front end with a logic output can extend such measurements to signals of up to 50 V RMS and frequencies up to 80 MHz.[809]

Aliasing is the characteristic frequency-measurement failure. A digital scope without anti-alias protection, fed a 10 MHz signal and run at a slow time base, will display and even measure an entirely fictitious low frequency such as 1 Hz or 8.16 Hz.[F0HQJIPcDYs] The same behaviour shows up when a scope's own generator is swept to its 5 MHz maximum.[474] An analog scope in XY mode gives a frequency comparison instead: two 1 kHz sine waves produce a stationary circle, and shifting one source by 1 Hz makes the circle rotate once per second in a direction set by which is higher.[502]

## Frequency as a diagnostic signature

The frequency of an unwanted signal usually identifies its source. A studio monitor amplifier oscillating at 61.7 Hz and 40 V peak to peak is destroying its own driver; after partial repair the same fault reappeared at 350 Hz with a visibly drifting period, showing the oscillation was not resonant but condition-dependent.[1072] Piezoelectric singing in a 10 uF multilayer ceramic capacitor is not at a fixed frequency either — the interval between successive peaks visibly varies — but the electrical frequency correlates with the audible sound, which is what identifies the mechanism.[855]

Harmonic relationships confirm identifications. A peak at 36.85 MHz found near a 12.28 MHz crystal is the third harmonic of the fundamental, itself measured at 12.23 MHz.[694] A signal on a vacuum fluorescent display controller that a scope refused to read directly became a clean 12 MHz once the input was AC coupled, and that number identified the node.[717] The beep of an electronic safe lock was captured by spectrum analysis at 4.072 kHz, allowing the buzzer tone to be compared against a suspected duplicate.[762]

Mechanical resonance obeys the same logic. Sweeping a shaker table across a mounted PCB found violent response around 95 to 98 Hz and a second node at about 111 Hz within a couple of hertz, with nothing happening at all at 120 Hz.[1442]

## High-frequency content and interference

Repetition rate and edge rate are separate things, and the edge is what causes trouble. Digital signals at only 6 MHz still contain high frequency content in their transitions, and this remains true even for a 1 Hz signal — the long ground lead of a probe is an inductor that rings on the edge regardless of how slow the repetition is.[1081] A sine wave is the exception, because it contains no fast transition.[1081]

Susceptibility follows harmonic content. A multimeter disturbed by an injected square wave at 5 MHz was reacting to harmonics extending up into the RF region; reducing the fundamental frequency progressively reduced the effect, while at 10 MHz and 10 V peak to peak the disturbance was severe.[933] Coupling was loose enough that moving a hand near the leads changed the result.[933]

Frequency also sets physical dimensions and behaviour. On a satellite phone, the shorter helical antenna is the receiver and the longer one the transmitter, because the transmit frequency is lower and therefore the wavelength longer.[721] In a terminated coaxial run, sweeping upwards brings the reflected signal out of phase with the incident one, with a distinct minimum at the input at about 47 MHz.[652] At around 1 MHz and 40,000 volts, a handheld Tesla coil's current largely travels across the skin rather than through the body, and it will punch through insulators such as wood over two or three centimetres.[yQ7_A4Cr9ak] 5G operates typically at 25 GHz and above against roughly 5 GHz or lower for 4G, but transmission and reception power levels are not correspondingly higher, and microwatt-level energy produces negligible heating.[4vHx-UyIM9M]

Frequency-selective faults point at the analog front end: an oscilloscope channel that reproduces a 1 kHz sine wave's amplitude and low frequency shape correctly while mangling its high frequency content has a bandwidth-limited defect, not a gain defect.[565] Front-end multilayer ceramic capacitors are also microphonic, coupling both a relatively high-frequency tap and lower-frequency thumps from the bench into the trace.[983]

## Noise and frequency

Op-amp input noise voltage is specified as a density, in nanovolts per root hertz, and plotted against frequency on dual logarithmic axes because the relationship is not linear.[528] Measured on a spectrum analyser, a bench instrument's noise floor came out at about 31 nV per root hertz at 1 kHz.[528] Low-frequency spans are slow to acquire: a 1 kHz span takes about a quarter of a second per record length before RMS averaging even begins.[528]

## Generated and mains frequencies

Mains equipment is normally specified over a range rather than at a point — a vintage instrument rated for 45 to 62 hertz handles both 50 Hz and 60 Hz supplies without issue.[553] A variable frequency converter can synthesise mains from below 50 Hz up to 440 Hz, and its output voltage regulation degrades noticeably as frequency is raised, with the internal switching frequency audible from outside the case.[449] Mains ripple injection signalling uses tones from 167 hertz up to 2 kilohertz, selected on a DIP switch.[1283] An AC voltage standard set to 5.00000 V at 60 Hz sits in the middle of its most accurate range.[852] A tuning-fork wristwatch achieves its smooth sweeping second hand from a fork driven by two coils in an oscillating circuit at around 50 hertz.[911]

Where frequency genuinely does not matter, it should not be chased. A 555-based LED dimmer wanders between about 310 Hz and 733 Hz as its duty cycle is adjusted, which is irrelevant because both extremes are far above any frequency at which flicker would be visible.[392] Duty cycle control from 0.3% to over 99% was achieved despite that drift.[392]

## Frequency in pseudoscience

Frequency is a favoured word in unfounded product claims, used without any defined quantity. Wellness marketing has asserted that unprocessed vegetables and fruit carry a beneficial frequency entering the body while canned food registers zero hertz.[1290] A supposedly anomalous sphere was presented as emitting strange frequencies of around one to two hertz on unexplained measuring gear, where readings drifted and were selectively accepted or rejected.[uI62sAN5JzU] Free-energy crowdfunding campaigns similarly wrap conventional mains figures — 50 to 60 hertz at 110 to 380 volts — around claims of perpetual motion.[HfqpuhYiR3o]
