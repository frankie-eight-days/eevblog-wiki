# operational amplifier

An operational amplifier, universally shortened to op-amp, is a DC-coupled differential amplifier with enormous internal gain, used as a general-purpose analog building block.[600] It is one of the essential circuit elements of analog design, and appears in almost every instrument, power supply and signal chain that handles a continuous voltage.[600] Its behaviour in a practical circuit is set almost entirely by the external components wrapped around it rather than by the device itself, which is why a handful of cheap generic parts can serve an enormous range of applications.[600][1436]

## Origin of the name

The name comes from the earliest application of the devices: they were developed to perform mathematical operations.[600] Before digital computers existed, these amplifiers were the active elements of analog computers, performing addition, subtraction, multiplication, integration and differentiation directly in hardware.[600][854] Those functions survive as standard configurations — an op-amp can be wired as an integrator or as a summer, which is simply an adder — but the dominant modern use is as an amplifier proper.[600] Analog computation was not exclusively electronic; the alternative was a purely mechanical analog computer, containing essentially no electronics at all.[854]

## Symbol, terminals and supplies

The op-amp is drawn as a triangle with two inputs on one side and a single output on the other, and the symbol is sometimes flipped to suit the direction of signal flow without any change in meaning.[600] The positive input is the non-inverting input and the negative input is the inverting input; using the correct names is part of speaking about the parts accurately.[600] Besides the output there are two power supply pins, a positive and a negative.[600]

There is no ground pin on an op-amp — only the positive and negative supply connections — and this is a common source of confusion.[600] The voltage reference the circuit works against is part of the external circuitry, not of the amplifier.[600] Where a design needs a negative rail purely to supply its op-amps, a switched-capacitor converter is a standard way of generating one, with operational amplifier power listed among the intended applications of such parts.[1115]

## The closed-loop rules

The open-loop gain is designed to be enormous, effectively infinite, so an op-amp is essentially never used without external circuitry providing negative feedback.[600] With feedback in place, the amplifier drives its output to whatever voltage is required, within the limits the circuit allows, to make the two input voltages equal.[600][HbMnQdRzD8A] This single rule, combined with the ideal assumption that no current flows into the input pins, is enough to analyse most configurations.[600][479]

The simplest configuration has no external components at all: the output is tied straight back to the inverting input and the signal is fed into the non-inverting input, giving a buffer.[600] The same principle explains the virtual ground of the inverting configuration, which is the point most often misunderstood. With the non-inverting input tied to ground, the inverting node sits at zero volts not because nothing is present there but because the output continuously moves to cancel whatever the input does to that node.[HbMnQdRzD8A] A small input change forces a large output change to hold the junction of the two feedback resistors at the same place, and with equal resistors a rise on the input is matched by an equal fall on the output.[HbMnQdRzD8A]

The same op-amp action is exploited deliberately in supply design. A series resistor placed at the output of a buffer — there to protect the output — can be enclosed inside the feedback loop, at which point the amplifier compensates for the drop across it and the resistor effectively disappears from the output while still doing its protective job.[222]

## Departures from the ideal

### Input offset voltage

A real op-amp has an input offset voltage, VOS. A general-purpose part might exhibit 10 mV, 1 mV, or 0.1 mV for a good one.[24] That offset is amplified by the closed-loop gain along with the signal, so a device specified at 1 µV of offset running at a gain of 100 should produce about 100 µV, or 0.1 mV, at the output.[476]

Offset sets a hard floor on how small a sensed signal can usefully be. In a current-sensing front end, the shunt resistor cannot be made arbitrarily small, because the voltage developed across it would be swamped by the input offset voltage of the amplifier that follows.[232] A workable rule of thumb is that the error should not exceed one bit of resolution on the analog-to-digital converter behind it.[232] Measurement of offset at the microvolt level is itself difficult: a gain-of-101 test jig built around an AD8628 in an SO8 package, using 1 kΩ and 100 kΩ resistors, produced as much as 5 µV of apparent offset against a 1 µV typical specification.[476]

### Input bias current

Every op-amp has an input bias current. The ideal-op-amp rule that no current flows into the input pins does not hold in practice; some current always flows into or out of the input pins.[479] The effect is significant enough that microcontrollers with integrated analog blocks provide a calibration mode which stores the bias current values of the on-chip operational amplifier so the error in a following gain stage can be compensated.[900]

### Bandwidth

The ideal op-amp has infinite bandwidth. A practical part might have 1 MHz or 100 kHz, and this finite bandwidth changes the bandwidth of the surrounding circuit.[600] Bandwidth is also what distinguishes broad classes of parts: high-bandwidth op-amps are specified for switching and video paths,[1127] video op-amps such as the AD818 turn up in instrument front ends,[1005] and 1 GHz devices exist but are correspondingly power hungry — a real thermal consideration in a densely packed, fanless instrument.[1753]

### Supply rejection and power-down behaviour

Noise on the supply rails reaches the output only to the extent allowed by the power supply rejection ratio, and in a well-arranged circuit the contribution of the amplifier and its resistors to total noise can be small compared with other paths.[1328] Datasheet behaviour cannot be assumed for unusual operating states: a design using analog-devices op-amps specified as capable of being powered down was found to drag its input to −5 V when powered down, contrary both to the datasheet and to the expectation of the part's own designer until the effect was checked.[1119]

## Noise and precision

For precision DC and low-frequency work, a millivolt of offset is far too large, and ordinary op-amps are additionally noisy at DC where 1/f noise dominates.[24] The answer is the chopper amplifier, also called an auto-zero amplifier — a standard op-amp with an offset voltage that is continuously nulled.[24]

The internal arrangement uses two amplifiers, a main amplifier A and a nulling amplifier, together with four switches and two storage capacitors.[24] In one phase the nulling amplifier measures the offset of one amplifier and stores the result on a capacitor; the switches then change over, the nulling amplifier measures the offset of the main amplifier and stores that value on the second capacitor, and that stored value is fed back to offset the main amplifier's own VOS.[24] The result is offsets of the order of 1 µV or even 0.1 µV in place of a millivolt, and because the technique nulls DC offsets and very low-frequency content, the 1/f noise is cancelled along with them.[24]

Chopper parts are the natural choice for microvolt-level instrumentation. The AD8628 is among the best zero-drift, low-offset devices available, using a chopper configuration to reach roughly 1 µV of offset.[476] The MAX4238 forms the gain-of-200 stage of a precision current adapter, where 1 mV across the shunt produces 0.2 V at the output.[232] The OPA189 measures significantly lower in noise than the MAX4239 for essentially the same power, and is a drop-in replacement in that application — although an accompanying LMV321 has to be swapped for a part that tolerates the higher rail voltage.[1328]

Where noise rather than offset dominates, the limit is usually the front end as a whole. In a dynamic signal analyser input stage, input noise is set by the combination of the FETs and the op-amp, and by both the input current noise and the input voltage noise together.[529] Audio-oriented low-noise parts are specified in these terms — the LME49990 quotes 0.9 nV/√Hz nominal and 1.3 nV/√Hz maximum input voltage noise density, though its noise curves are not dramatically better than those of the LM797.[541] Audio parts are also characterised by distortion; the OPA134 is a high-performance audio operational amplifier specified at vanishingly small THD.[1752]

## Stability

An op-amp inside a control loop is a stability problem as much as a gain problem. In a linear supply, substituting an LP2902 quad — almost identical to the LM324, sharing much of the same datasheet, but with an extra internal current source — for the original amplifier produced a marked improvement in stability, alongside a little more output capacitance and the removal of a times-four gain stage from the control loop that was contributing to the instability.[95] Loop stability is not always where it appears to be: in a precision current source, it is ultimately determined by the phase margin of the output op-amp inside the voltage reference, so adjusting input capacitance elsewhere addresses the wrong part of the circuit.[577]

Loop behaviour is directly observable in load-transient testing. Watching the control op-amp output alongside the supply output shows the switch-on transient, roughly 100 mV with a 1 µF output capacitor, followed by visible recovery and settling; on load removal the output shows a burst of high-frequency content, ramps back down and settles as the amplifier takes control again, jumping about 50 mV for a quarter-amp step.[224] Increasing the output capacitance to 47 µF reduces the transient amplitude but brings in considerably more noise.[224]

## Jellybean parts

A small set of generic op-amps is used by default, on the basis that the part number is known to do the job. The LM358 is a dual bipolar device, explicitly described by its manufacturers as an industry standard, and is the sensible default for ordinary work; since it contains two independent amplifiers in one package, there is little reason to choose a single-amplifier jellybean instead.[1436] The LM324 is the corresponding quad and is valued particularly for its wide supply range — low-cost quads from other vendors may be limited to around 6 V, which rules them out of many designs.[400] Variants such as the LMV324 appear in mains metering hardware,[409] and LF-series and LF347 quads are common in older instruments.[217][1258]

The NE5532 is the classic dual audio op-amp and has been in production for decades, which makes any change to it consequential: a manufacturer alteration to a long-standing jellybean part, even when nominally notified, can damage a product or a company if a design relies on the previously published specification, including such basic details as the pinout.[1752] Other parts that recur across teardowns include the MCP6002 and other Microchip devices,[Yk_T-uCbg10][400] the TLC2252 dual,[1248] Burr-Brown devices in broadcast video distribution,[456] general-purpose quads in probe front ends,[1744] and the NJM2100 dual, a low-voltage part operating from ±1 V to ±3.5 V or a single supply.[271]

At the precision end, ultra-precision parts such as the OP177 are scattered throughout a battery-simulator instrument, alongside an AD620 instrumentation amplifier and jellybean comparators like the LM393.[1005]

## Power op-amps

Monolithic power op-amps extend the same closed-loop behaviour to load currents that would normally require a discrete output stage. The OPA541 is a high-power monolithic operational amplifier rated for a 60 V supply and 9 A of continuous output current, with a 1.6 MHz gain-bandwidth product, and is unity-gain stable — enough to build a programmable-gain, programmable power supply around.[500] A comparable linear pass element used in a benchtop instrument is technically an operational amplifier: a single supply range from 8 V to 60 V, splittable into a dual supply, with 500 mA of continuous output current, giving a supply output with no switching noise at the cost of dissipation.[1701]

## Typical uses

The op-amp is what makes many small pieces of bench equipment trivial to build. A constant-current electronic load is essentially a FET, an op-amp, and not much else, which is enough to run a battery capacity test with a multimeter and a stopwatch.[141][393] Adding a DAC, whether a card or an on-board converter, turns the same arrangement into a programmable load.[393] Building a non-standard voltage reference follows the same pattern: since band-gap physics stops around 1.2 V, a lower reference is made by dividing down with 0.1% precision resistors, or with ordinary resistors and a trimpot, and then buffering the result with an op-amp follower.[400] A single-supply amplifier constrains what is possible here, since dividing down a higher reference in that way would require a non-inverting configuration with a gain of less than one.[400]

Adding a nonlinear element to the feedback path changes the operation performed: a transistor in the feedback loop of an op-amp, exploiting the diode equation, yields a logarithmic amplifier.[818] The same building block also acts simply as the output gain stage of a larger analog chain — amplifying a phase-detector output ahead of low-pass filtering in a modulator,[574] providing DAC offset trimming in a scope's analog channels,[217] driving muxed filter banks in a network analyser,[1104] or buffering a scope's programmable-gain front end.[360][1717]

Op-amps are increasingly integrated rather than discrete. Microcontrollers ship with on-chip amplifiers — two op-amps together with a 12-bit ADC and DAC on one ARM part,[900] or four op-amps and two low-power comparators that run independently of the core in sleep mode on a programmable-analog device.[722] Where op-amps are absent, the design is usually older or deliberately discrete: 1970s and 1980s consumer and instrument hardware often used transistor arrays and discrete differential pairs with only basic op-amps alongside 4000-series logic.[752][208] Conversely, an unexpectedly large amount of op-amp circuitry in a modern product is a sign that the designers did not simply drop in a single integrated chipset.[ag-MjKAfATw]
