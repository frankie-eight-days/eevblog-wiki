# input offset voltage

Input offset voltage, usually written V<sub>OS</sub>, is the small differential error voltage that exists between the two inputs of a real operational amplifier or comparator when its output should be at zero. It is generated internally by mismatches in the input circuitry and is inherent in the design of every op amp, including the ultra-low offset parts.[476] Because it appears at the input, it is multiplied by whatever closed-loop gain the stage has, which is what makes a few microvolts of offset a first-order design problem in precision measurement circuits.[476][479][232]

Offset voltage cannot be measured by putting a multimeter across the input pins, not even a 6½-digit one — the error is generated inside the silicon, so the pins could be shorted together with a blob of solder and the offset would still be there.[476] The practical measurement is indirect: short the input, run the amplifier at a known non-inverting gain, and divide the resulting output voltage by that gain. A gain of 101 built from 1 kΩ and 100 kΩ, treated as 100, is close enough for the arithmetic.[476][479]

## Effect at the output

The offset is referred to the input, so the error appearing at the output is V<sub>OS</sub> multiplied by the stage gain.[232][476] In a times-100 stage, 1 µV of offset becomes roughly 100 µV at the output, and an output reading of 300 µV corresponds to about 3 µV of offset.[479][476] The same multiplication is what makes offset the limiting term in shunt-based current measurement: the shunt resistor cannot be made arbitrarily small, because the voltage developed across it will eventually be swamped by the amplifier's offset.[232]

## Budgeting offset in a design

Offset is normally specified against a resolution target rather than judged in isolation. A common rule of thumb is that the offset-induced error should not exceed one bit of the analog-to-digital converter reading the result.[232] For a 12-bit converter with a 2.048 V full scale, one bit is 500 µV at the output; behind a gain of 200 that translates to 2.5 µV allowed at the input, which in practice means a chopper or auto-zeroing amplifier — the MAX4238, at 0.1 µV, exceeds that requirement by more than an order of magnitude.[232]

The same method sizes the µCurrent front end: with a 0.1 mV display resolution and a gain of 100, the offset must be 100 times smaller than the least significant digit, giving a 1 µV requirement, which can then be entered directly into a distributor's parametric search to find candidate parts.[72] One microvolt of input offset is an extreme specification, and few parts on the market meet it.[72]

Where offset does not enter the signal path — a rail splitter built from two resistors and a spare amplifier, for example — the offset specification is irrelevant and a 10- or 20-cent jellybean part does the job, against roughly a dollar for a dedicated splitter chip.[72]

A well-matched example is a high-side current sense amplifier whose 100 µV typical offset happens to equal the 100 µV developed across a 0.2 Ω shunt at the 500 µA minimum current, giving exactly one bit of error at the bottom of the range.[232]

## Typical, maximum, and production spread

The banner figure on the front page of a datasheet is a typical value, not a guarantee, and the maximum column is the number a design must survive.[476] A part quoted at 1 µV typical may be specified at 5 µV maximum at 25 °C, and as bad as 10 µV once the full temperature range is included.[476] Comparators show the same pattern more starkly: 250 µV typical can become 5 mV or 7 mV over temperature.[1464]

Manufacturers often publish the production distribution as a bell curve. For a high-precision part specified at 500 µV, the measured spread runs to about ±400 µV, with the bulk of parts clustered slightly off zero — around 150 µV to 200 µV on the positive side — and very few landing out at the spec window edges.[238] A part guaranteed at ±4 µV may measure closer to ±1 µV in production, because the process is tuned to keep the distribution centred.[1325] Designing around that tightness is unwise, since production processes drift over time.[1325]

Two further datasheet traps: the offset specification often applies only at the highest supply voltage, leaving the low-supply behaviour undocumented and something the designer has to measure;[1325] and the dual or quad version of a part can carry a higher offset than the single.[1325] Grade suffixes matter as well — a device family may be sold in A, B, and C grades with different offset limits, with the best grade of one part number around 230 µV typical.[238] Nominally identical parts from different manufacturers can differ wildly: one second-source device measured about 190 mV of offset, roughly half an order of magnitude worse than another sample of the same part number, while a third measured a benign 0.2 mV.[1057]

## Interaction with input bias current

Offset error observed on the bench is usually a combination of the true V<sub>OS</sub> and the contribution of input bias currents flowing through the feedback and gain resistors — two entirely separate datasheet parameters.[479] A large feedback resistor turns even a small bias current into an offset error over and above V<sub>OS</sub>, which is why bias current is a persistent nuisance in precision applications.[479]

This explains a common bench discrepancy. An AD8628 with 1 µV typical offset in a times-100 non-inverting stage should give about 100 µV out, but measured over 300 µV, and replacing the chip repeatedly produced the same result — the part was within specification and the excess came from elsewhere in the circuit.[479][476] Dropping the resistor network by an order of magnitude, to 100 Ω and 10 kΩ, only recovered about 60 µV; adding a bias-compensation resistor, trimmed with a 500 Ω pot, brought the output down to 50–60 µV, equivalent to well under 1 µV of offset.[479] Once nulled, drift of roughly ±100 µV at the output over the supply range is acceptable for most purposes.[479]

The behaviour also varies with supply voltage in ways the datasheet does not predict. Measured offset drifted with the rail, at one point crossing through zero and going negative near the 2.7 V minimum supply; at 2.7 V on a single supply the same circuit produced about 73 µV out, or 0.7 µV of offset.[476] In a rail-to-rail part the input topology allows bias currents to flow in either direction, and that combines with a V<sub>OS</sub> that itself shifts across the supply range, so a null valid at every supply voltage is not achievable.[479] The remaining options are to tolerate the variation, trim it at one operating point, or choose a different amplifier.[479] A ±I<sub>B</sub> specification on a datasheet, given where a single-polarity figure would be expected, is a strong hint that the part is internally bias-compensated even if the text does not say so.[479]

## Auto-zero and chopper amplifiers

Chopper and auto-zero amplifiers contain an internal process that continuously nulls the input offset, giving offsets that are almost zero.[72] These are the parts that reach 0.1 µV, and essentially nothing else on the market matches that.[1325][232] The AD8628 is a zero-drift chopper part quoted at 1 µV with 0.5 µV peak-to-peak noise from DC to 10 Hz; lower-offset parts exist, but few match the combination of offset, noise, and drift.[476] The internal architecture is generally proprietary and undisclosed, which limits how far its supply-dependent behaviour can be reasoned about from first principles.[479]

## Composite amplifiers

No single amplifier provides ultra-low offset, high bandwidth, low noise, and large output drive simultaneously.[1609] Buffer amplifiers with high output drive typically carry offsets of tens of millivolts, so simply cascading a precision front end into a buffer adds that 10 mV or so directly to a 0.1 µV output and destroys the advantage entirely.[1609]

The composite amplifier avoids this by taking the feedback for the first amplifier from the output of the second, placing the buffer inside the precision amplifier's loop.[1609] The buffer's offset is not removed, but the precision amplifier drives its input to whatever value cancels it — roughly −10 mV for a 10 mV buffer offset — automatically, so the composite output offset returns to the 0.1 µV of the precision stage.[1609]

## Offset in other circuits

Offset appears wherever an amplifier defines a DC operating point. In the Howland current pump the op amp's input offset is one of the named sources of output current error, alongside current lost through the feedback network and bias-current effects in high-impedance feedback resistors.[xUKf-4rv_sQ] Comparators are specified the same way as op amps — parts range from 250 µV and 370 µV typical to ±2 mV maximum — and CMOS input stages push the associated bias and offset currents down into the picoamp range, where the offset voltage becomes the dominant input error.[1464]

Familiarity with the order of magnitude of the offset voltage of common jellybean parts is part of basic working knowledge, alongside features such as ground sensing and rail-to-rail output.[1436] The OP-07 sits at sub-100 µV, around 60 odd microvolts typical, and is the conventional step up from a general-purpose part when offset is the binding constraint.[1436] Other jellybeans carry a 3 mV guaranteed figure with a typical value near 300 µV — an order of magnitude better than the guarantee, and adequate for non-critical low-side shunt measurement, but with the guaranteed number often tied to a specific version suffix.[1436]
