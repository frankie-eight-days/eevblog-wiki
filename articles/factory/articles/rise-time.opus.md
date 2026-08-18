# rise time

Rise time is the interval a signal takes to climb through a transition, conventionally measured between the 10% and 90% points of the edge.[1133] It matters for two reasons: it is the direct measure of how fast a circuit or instrument can actually respond, and through a simple formula it stands in for analog bandwidth, so an edge fast enough to outrun the equipment under test becomes a bandwidth measurement.[306][70] In digital systems it is equally a constraint rather than a figure of merit — logic parts specify how slowly an input edge may transition before the part misbehaves, and an edge that is too slow is a real failure mode.[1208][sr1DOHnJi8I]

## Relationship to bandwidth

There is a direct relationship between the rise time observed on an oscilloscope, assuming a perfect input pulse, and the instrument's actual analog bandwidth.[306] For traditional Gaussian-response instruments — the older analog CRT types — bandwidth equals 0.35 divided by the rise time.[306][196] The same relation run the other way turns a fast square wave into a bandwidth check: feed in a very fast edge, measure the rise or fall time, and divide 0.35 by it.[70][433] The technique works on analog instruments that have no function generator fast enough to sweep them to their corner.[196] It was also the basis for characterising a home-built high-voltage probe, whose measured edge implied roughly 30 MHz of bandwidth even though the available oscillator only reached 3 MHz.[85]

Modern digital oscilloscopes generally do not have a Gaussian rolloff, and a coefficient of 0.4 is used instead; for a 500 MHz instrument this predicts a rise time of 0.4 divided by 500 MHz.[306] Applying the Gaussian 0.35 factor to such a scope overestimates the bandwidth substantially — on one instrument by tens of megahertz at minimum, which is a significant error.[311] Which coefficient is correct depends on the particular instrument and the method it implements, and using the wrong one silently corrupts the result.[311]

## The pulse source and its contribution

A pulse generator never produces a perfect edge, so its own rise time contributes to what the oscilloscope displays.[306] The practical rule of thumb is that if the source is five times better than the rise time being measured, its contribution can be neglected.[306] Classic avalanche-transistor pulsers of the Jim Williams type produce edges in the region of a few hundred picoseconds — 300 to 400 picoseconds is typical.[306][304] Commercial parts go considerably faster: a compact pulse head specified at 40 picoseconds for 10 to 90% rise time, with 1 volt amplitude, is available at modest cost.[1133]

Layout dominates at these speeds. Any lead has inductance, so the generator has to plug straight into the instrument input, and the board traces themselves must be laid out properly or the edge is degraded and the waveform acquires overshoot and undershoot.[304] Designing a very sharp edge is described as something of an art, and the avalanche transistor — a 2N2369 in the standard circuit — is not interchangeable between samples; parts are selected on test to find a good one.[304]

Degrading the source demonstrates the point directly. Rebuilding one pulser with 35 cm of coax in place of the original capacitor gave 270 picoseconds rise and 1 nanosecond fall, good enough to serve as the reference for measuring every other instrument in the lab.[311] With only the original 5 picofarad capacitor the same circuit gave about 295 picoseconds rise and roughly 600 picoseconds fall.[311] A much longer coax run produced an edge in the region of 800 picoseconds to 1.4 nanoseconds and was useless for bandwidth work.[311] Fed through an attenuator, the reference pulser measured 254 picoseconds rise against 420 picoseconds fall.[311]

## Measured values across instruments

A 13 GHz, 40 GSa/s sampling oscilloscope was needed to see the reference pulser at all, and read about 288 picoseconds.[311] A mid-range instrument measuring the same source landed between 610 and 630 picoseconds, mostly around 630 — a figure that, punched into the 0.4 relation, gave a bandwidth estimate somewhat above the rated number.[311] Amplitude that runs off the screen corrupts the reading: with the waveform partly off-screen the same edge read 590 picoseconds, and the whole waveform must be on screen for the measurement to be accurate.[311]

Other measured edges: a 1 GHz instrument read 440 picoseconds when driven by the 40 picosecond pulse head.[1220] A 350 MHz instrument read 360 picoseconds on a single channel, but the reading degraded once a second or third channel was enabled and the sample rate dropped to 2 GSa/s.[1717] A hand-built handheld pulser generated 1.4 nanosecond rise and 1.9 nanosecond fall, sufficient to verify a probing system up to about 250 MHz.[433] Built-in function generators are much slower — 18 nanoseconds rise and fall with 500 picoseconds of square-wave jitter is typical of a 20 MHz generator embedded in a scope.[143] A multimeter's square-wave output managed 500 nanoseconds.[56] Where a retro instrument's function generator output degenerates at the top of its frequency range, its separate TTL output supplies the sharp edge instead.[1724]

## Probes

The probe, not the oscilloscope, is usually the limiting element. A passive probe rated for 350 MHz in ×10 mode collapses to well under 10 MHz in ×1 mode, and the rise time specification shows the same collapse: 900 picoseconds at ×10 against 40 nanoseconds at ×1 on one probe,[453] and 1 nanosecond at ×10 against 58 nanoseconds at ×1, with the ×1 bandwidth given as DC to 6 MHz, on another.[1367] The specification is printed in the manual, so the difference is documented rather than hidden.[1367] Between two probes of the same family, near-identical input capacitance — 17 pF against 16 pF — nevertheless corresponds to a 150 MHz versus 350 MHz rating and correspondingly different rise times.[707]

## Rise time in digital design

Logic datasheets specify an input transition rise and fall time, expressed as ΔT/ΔV: how fast the input signal is permitted to ramp, measured between the relevant threshold voltages rather than rail to rail.[sr1DOHnJi8I] The switching specifications elsewhere in the datasheet are themselves conditioned on a fast test edge; one part's numbers are all measured with a 6 nanosecond rise and fall pulse applied.[1208] Violating the input transition specification does not merely slow the circuit — it can drive the part metastable.[1208]

Open-collector outputs are the common source of trouble because the rising edge is produced by a passive pull-up charging the bus capacitance, while only the falling edge is actively driven. An optocoupler used as a clock source illustrates the asymmetry: the output falls in 500 nanoseconds with the transistor pulling down, but the rise is far slower and is specified only for a nominal pull-up and load capacitance — 4.7 kΩ and 30 pF, roughly the input capacitance of a gate.[1208] Adding devices to an I²C bus adds capacitance and lengthens the rise time on the low-to-high transition, which is why the usual 2.2 kΩ pull-up is sometimes reduced to 1 kΩ for faster operation.[1208] These typical datasheet figures also shift with temperature and production spread, so a design that is already marginal on the nominal number has no margin at all.[1208]

Fast edges are also deliberately created for measurement. A 1 MHz HCMOS oscillator with about 2 nanoseconds of fall time — and a comparable rise time — provides the sharp transition needed to make bypass-capacitor behaviour visible on the power rail; the frequency is irrelevant, only the transition time matters.[1085] Conversely, a Schmitt trigger's tolerance of slow inputs is demonstrated by deliberately stretching the clock edge from around 45 nanoseconds out to 500 nanoseconds, 1 microsecond and beyond while the downstream counter continues to work.[941]

## Deliberately slowing edges

Fast edges generate emissions, so many modern parts include slew-rate control on their outputs specifically to reduce EMC problems: instead of a really fast edge the output is slewed, and the emitted energy falls.[111] This sits alongside the other standard mitigation, keeping current loops tight and short.[111]

Slew limiting is also a designed characteristic in some equipment. A DC electronic load programmed at 10 mA per millisecond takes 200 milliseconds to complete its rise and fall, matching the programmed slope.[862] A bench supply's output ramps up to 30 volts under gate control with no overshoot at all.[512] In a linear supply, an RC time constant in the control path shapes the output edge into a visible exponential, and shortening it produces a faster rise at the cost of the op-amp having to work harder to compensate.[224]

## Instrument measurement functions

Rise time is a standard automatic measurement on essentially every digital oscilloscope, sitting alongside period, frequency, width and duty cycle in the horizontal measurement group.[1751][143][480][487] Quick-analysis modes display rise time, fall time, mean and peak values at once, though on some instruments enabling that mode restricts the analysis to a single channel.[793][842] Some instruments include on-screen help that explains, with example waveforms, what the rise-time measurement function actually does.[703] Beyond simple measurement, rise and fall time variation can be used as a trigger and search criterion for hunting anomalies in a stored acquisition.[199]

Even at ordinary timebases the concept is visible: a 1 kHz probe-adjust square wave rising within a single microsecond division is an edge no multimeter would ever show.[UJjMt2-k99c] Logic-analyser front ends without proper termination display visibly degraded edges, which is precisely why viewing the analog waveform alongside the digital decode is worth having.[876]

## Terminology note

Picoseconds are sometimes rendered verbally as "puff" — the same shorthand normally reserved for picofarads — as a matter of long habit.[1133]
