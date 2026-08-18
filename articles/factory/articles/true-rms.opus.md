# true rms

True RMS is an AC measurement method in which the reading is correct for any waveform shape, not just a sine wave.[1223][1636] A true RMS meter measures the true power in the signal — the same heating effect the waveform would produce in a resistor — rather than inferring a value from an assumed wave shape.[75] It is one of the main dividing lines between a cheap multimeter and a professional one, and it applies only to AC voltage and AC current measurement; nothing else on the dial is affected by it.[75][1636]

## Average responding meters and where they fail

A meter without true RMS is called an average responding meter.[75][1636] Its AC ranges are tweaked and calibrated on the assumption that the input waveform is perfectly sinusoidal.[75] On a clean sine wave — mains at 110 V or 240 V, for instance — that assumption holds, and an average responding meter can in fact be more accurate than a true RMS one.[75][1636] On anything else it fails badly: most waveforms encountered in electronics are not perfectly sinusoidal, and an average responding meter fed a square or triangle wave reads visibly out, with errors running to tens of percent and as much as 50%.[99][75]

The distinction is a specified feature rather than something to be inferred: true RMS is almost always printed on the front of the meter, and its absence there is the tell.[1636]

True RMS should not be confused with DC-plus-AC coupled measurement. True RMS concerns validity across wave shapes; whether the DC offset is included in the result is a separate choice, and DC plus AC is what includes it.[1223] Which is the relevant figure depends on the application.[1223]

## Bandwidth is the real limitation

Buying a meter marked true RMS says nothing about the frequency range over which the claim holds, and this is where cheap meters give ground. Where the true RMS function is built into the main multimeter chipset rather than implemented with a dedicated converter, bandwidth is low — typically one or two kilohertz depending on the chipset.[1007][1083] Sub-$50 meters advertising true RMS commonly specify only 1 kHz.[1731][1351][MarjYxiudYE] The Brymen BM235 is specced to 440 Hz; it works beyond that, but somewhere around 1.5 kHz it degrades and behaves erratically.[912] The Uni-T UT61E+ reaches 10 kHz.[1378]

Extended bandwidth generally means a separate true RMS chip, and manufacturers use it to differentiate models within a family: the lower Brymen BM787 variants are true RMS but bandwidth-limited by the chipset, and the extended frequency range requires the highest-end model with the true RMS chip fitted, with the corresponding circuitry unpopulated on the cheaper boards.[Q_RYG_5cQk8] Meters without a proper true RMS chip are already several dB down by 4 kHz.[1731]

Accuracy also degrades across the band on instruments that do have wide bandwidth. The Agilent U1253A specifies 0.4% on AC over its limited bandwidth, blowing out to around 3.5% across the full 100 kHz.[56] Highly accurate true RMS measurement is expensive; a true RMS spec of 1% or so on an ordinary handheld is not a cause for concern.[75] The Fluke 8060 was notable for 100 kHz true RMS analog bandwidth.[802]

## Implementation

True RMS is done either inside the multimeter chipset or with a dedicated converter. The Fluke 287 uses an LTC1968 for the true RMS output, with the meter rated to 100 kHz bandwidth.[1592] Bench instruments have used whole boards for it: the HP 3457A carries a separate AC converter board handling the true RMS conversion.[426] In the Fluke CNX3000 the function sits inside a Fluke custom part that also handles input switching.[417] On the Fluke 8842A true RMS was a factory option rather than standard equipment — a unit without it reports error 30 and refuses AC volts entirely.[1012] The difference can be small enough to exploit: an average responding Fluke 77-4 can be converted into the true RMS equivalent, a Fluke 177, for roughly 10 cents in parts.[1448]

## Product segmentation

Because it is a headline feature, true RMS drives pricing and model lineups. On $100-class meters the true RMS version has typically cost $15 to $20 more than the average responding one, which is generally worth paying.[99]

The persistence of average responding meters at the top of the market is a documentation problem, not a technical one. The original Fluke 27 was average responding and sold in enormous numbers to the US military, which wrote tens of thousands of procedures and manuals around it.[64] The Fluke 28 Series II is true RMS and therefore not a drop-in replacement, so Fluke produced the 27 Series II specifically for customers who could not change their documentation; apart from that niche, and at essentially the same price, there is no reason to choose it over the 28 Series II.[64][ay9wFQAW19Y] The same logic keeps the 70 series alive: those were average responding, the 79 Series III was the true RMS exception, and the line was superseded by the true RMS 170 series while legacy customers continued to want average responding meters.[1448]

Low-cost and pocket meters remain mostly average responding. The Fluke 101 at $42 and the Fluke 17B MAX are both average responding, as were all five meters in a $50 shootout.[1574][1692][91] In pocket-meter comparisons only a couple of units in a large field were true RMS at all.[1083]

True RMS is old rather than new: the Tektronix 213 of 1975 combined a 1 MHz scope with a 3.5-digit, 0.1%-plus-one-count meter that did true RMS AC,[628] the Fluke 45 of 1989 had it as standard,[791] and 30,000 counts with true RMS was impressive in its day.[1525]

## Practical judgement

For general electronics work a true RMS meter is the recommendation, because the waveforms being measured are usually not sinusoidal.[75][99] For a beginner buying a first meter, however, it is "nice to have, but it's not really that important" — the common case of measuring mains and other clean sine waves is exactly the case an average responding meter handles well.[1636]

Where an RMS value is needed on a signal outside a handheld meter's bandwidth, an oscilloscope now covers it. Measuring power supply ripple and noise once called for a wide-bandwidth multimeter with a true RMS mode; modern scopes compute the RMS value directly.[594][926]
