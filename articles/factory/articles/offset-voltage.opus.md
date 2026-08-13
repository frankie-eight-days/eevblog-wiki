# offset voltage

Offset voltage, usually written VOS, is the error voltage that appears at the input of a real operational amplifier where an ideal one would need none: a regular op amp behaves as though a small DC source were wired in series with its input terminals.[24] Because that error sits at the input, it is multiplied by whatever gain the stage has, which makes it the dominant limit on precision DC and low-frequency measurement long before noise or bandwidth become interesting.[24][929] A typical general-purpose part carries a millivolt or so, which is very large for precision DC work; specialised chopper parts get four orders of magnitude below that.[24]

## Magnitudes across the op-amp spectrum

A standard general-purpose op amp may have 10 mV of offset, 1 mV, or around 0.1 mV for a good one.[24] For jellybean parts this simply is not a specification anyone is buying: an LM358-class device is chosen for availability and longevity of production rather than for precision, and ten millivolts of offset is accepted without a second thought.[1697] Differences between the ST and Arts Chip versions of the same jellybean part number amount to slight variations in very average offset figures.[1697]

Precision parts occupy the middle ground. The LT1014 has a couple of hundred microvolts of offset and costs accordingly.[225] The TLC272 is specified at 500 µV maximum at VDD of 5 V.[238] The OPA335 has about 5 µV.[413] The OPA376 is a precision-trimmed part at 5 µV typical, which against a 1.25 V reference works out to 0.0004% error — negligible against the other terms in the budget.[577] The OPA227's worst case is only 10 µV, equivalent to 1 ppm of a 10 V reference; against a 1 V reference the same 10 µV would be 10 ppm, a much larger share of the error budget.[579]

Comparators are generally worse and are treated accordingly. The LM311 runs a couple of millivolts at ±15 V, and a device specified at ±3 mV minimum-to-maximum offset is unremarkable but entirely adequate where the threshold does not need to be tight.[1464][471]

Chopper and zero-drift parts sit at the bottom. The MAX4238/4239 is specified at 0.1 µV typical, that is 100 nV.[929][1057] The MCP6V01 has a maximum of ±2 µV.[476] Zero-drift architecture is characterised not just by ultra-low offset but by near-zero input offset voltage over temperature and over time.[1325]

## Gain multiplies the error

Offset voltage referred to the input is amplified by the stage gain, so the useful question is always what it becomes at the output. A ×100 amplifier turns the MAX4239's typical 0.1 µV into about 0.01 mV at the output.[1057][929] Run the arithmetic the other way and the offset sets the floor of a measurement system: a 500 µV full-scale shunt drop displayed to 0.01 µV resolution is an order of magnitude finer than the amplifier is actually capable of, so the least significant digits do nothing but wander, and what they are displaying is the offset voltage.[929]

The same logic applies to a digitiser's front end. A programmable-gain ADC specified at ±10 µV of offset at a gain of one sets the bottom-line system capability; across a 1 Ω current shunt that becomes ±10 µA of measurement capability, irrespective of how many bits the converter has.[259]

## Chopper and auto-zero amplifiers

The chopper or auto-zero amplifier is a standard op amp that additionally nulls its own offset, achieving figures such as 1 µV or 0.1 µV where a conventional part would give a millivolt.[24] Internally it consists of the main amplifier, a second nulling amplifier that has an offset of its own, four switches and two sampling capacitors.[24] In the first phase the nulling amplifier's inputs are shorted so that it measures its own input offset, stores that value on one capacitor and feeds it back to offset itself, while the main amplifier is held offset by the charge on the second capacitor.[24] Swapping the switches transfers the correction, and the main amplifier's offset is effectively cancelled.[24] The mechanism is nothing more exotic than storing charge on capacitors and alternating between them.[24]

Low offset is not free. Chopper parts trade against drift, noise and bandwidth: the Maxim device has lower offset than a comparable Analog Devices chopper but higher drift, higher noise and lower bandwidth.[476] Conventional op amps, meanwhile, are very noisy at DC, which is the other reason precision low-frequency designs reach for an auto-zero part.[24]

Offset in real parts is also a function of operating conditions. Measured across the supply range, one device's offset practically doubles over its operating supply voltage, and rearranging the bypassing — replacing split-rail 0.1 µF caps with a single capacitor directly across the positive and negative supplies at the chip — changes both the magnitude and the shape of that dependence.[476]

## Where it decides the design

Current measurement is the clearest case. A power meter using a 25 µV maximum offset amplifier with 0.6 µV maximum drift over temperature is not using a chopper, and with a low-value shunt the offset lands squarely in the microvolt region where the converter is trying to resolve; a chopper configuration is the appropriate choice when the shunt drop is that small.[1693] In a femtoammeter the amplifier's 50 µV offset, together with an integrated guard buffer specified at 100 µV maximum, is precisely what sets the achievable burden voltage.[1755]

Offset also sets the low end of adjustable sources. A constant-current dummy load bottoms out at about 1.5 mA because of the op amp's output offset; the offset can be trimmed, and rescaling the divider resistors moves the whole range down if a finer span is wanted.[102] In a threshold detector working to four decimal places, a 5 µV amplifier offset is close to the point where it starts to matter — it may in practice be higher than 5 µV.[584] In a battery gauge built around the LM3914, the offset contributes a nominal 75 µA error term, with a maximum of 120 µA, which is significant only if the load current is itself small.[204] Offset appears in unexpectedly coarse forms too: 1% resistors rather than precision parts in a panel meter's input divider produced a 16 mV offset that had to be trimmed out.[102]

## Composite amplifiers

Cascading a precision amplifier into an output buffer destroys the precision if the buffer is outside the feedback loop. The BUF634 drives 250 mA at 2000 V/µs but its front-page specifications omit the offset voltage, which is 30 mV typical — measured on the bench as 30-odd millivolts at the output of a stage whose MAX4239 input amplifier contributes on the order of 100 µV.[1609] The fix is the composite configuration: closing the feedback loop around the buffer's output instead of the precision amplifier's output makes the buffer's offset a loop error to be corrected rather than an additive one, and the output offset drops to zero.[1609] The MAX4239's own output then sits at about −55 mV, the amount needed to compensate the buffer.[1609] The same technique lets a designer trade off noise, offset, input impedance and drive capability between the two stages.[1609]

## Trimming, testing and specification

Some parts expose the offset directly. The LM311's balance pins accept a pot so the threshold can be tweaked to be more precise than the raw device.[1464] Instruments frequently expose an offset-voltage setting in firmware for the same reason.[1410]

Offset is worth production testing when the product is sold on it. Every µCurrent is tested for offset voltage and for gain on all three ranges using a dedicated jig, with a go/no-go limit in the region of half a millivolt.[1057] A µCurrent test jig carries a power LED, an offset measurement and an in-spec LED driven by a trimmed window comparator, so testing the offset costs nothing beyond the act of powering the board up.[588]

Reported offsets far outside the datasheet deserve scepticism about the measurement rather than the part. Units reported as showing four or five millivolts of offset with no input current were more than an order of magnitude outside the absolute worst-case production spec over the full temperature range — and only two meters in the lab, the highest-specified ones, measured a high offset at all, and they disagreed with each other.[1057] With the output driven through a protection resistor from a low-impedance source and the output ground taken from the star reference point of the split rail, the circuit topology gave no route for a genuine offset error; the LMV321 that generates the split rail has an offset of its own, but it does not matter, because the output reference point and the gain are both set by that rail, which is free to sit anywhere within the 3 V range rather than at exactly ±1.5 V.[1057] The effect was a marginal instability provoked only by a sufficiently reactive load.[1057]

Direct bench comparison keeps this honest. On a sample of one, a MAX4239-based µCurrent set to the 10 mΩ shunt and effectively shorted measured about 61 µV, and an OPA189 in the same position measured 73 µV settling toward roughly 50 µV with filtering — "good enough for Australia", and no more than the binning data predicted, the OPA189 having slightly wider offset margins for equivalent typical performance.[1328]

A missing offset specification is itself a signal. A current probe datasheet that lists bandwidth, sensitivity, supply current, saturation field, nonlinearity, offset voltage, hysteresis and temperature coefficients as headings while declining to give the numbers is not being straightforward.[1413] Silicon changes matter as well: a revised part used in oscilloscope front ends developed an offset problem in which a sustained DC offset presented to the input can damage the chip.[1752]

## Deliberate offset

The term also describes an intentional DC shift rather than an error. In a single-supply amplifier the output cannot swing below the negative rail, so the input and output reference must be lifted by a deliberate offset voltage — typically half the supply, generated by an equal-value divider from the rail, to maximise headroom.[600] That offset shifts the whole waveform up, and it is a design choice rather than a device imperfection.[600]
