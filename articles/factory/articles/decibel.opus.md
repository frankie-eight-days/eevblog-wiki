# decibel

The decibel (dB) is one tenth of a bel, an older unit that has fallen out of practical use.[49] It is not a unit in the sense that volts, ohms and amps are units: a dB expresses a ratio of two numbers, on a logarithmic rather than a linear scale.[49] Its value to engineering is that it makes very large and very small ratios tractable — a signal that is 0.5 times another can equally be described as −6 dB, and quantities spanning millionths to millions collapse into a range of two- and three-digit numbers that can be added instead of multiplied.[49][100]

## The two formulas

There are two dB formulas, and which one applies depends on the quantity being compared.[49] For power, expressed in watts, the ratio in dB is ten times the log of one power divided by another.[49] For magnitudes — voltage and current — the ratio is twenty times the log of one voltage or current divided by another.[49] In both cases the denominator is normally a reference value that the measured quantity is being compared against, such as 1 V or 1 mW.[49] In electronics the magnitude form is the one encountered most often, because voltages and signal levels dominate.[49]

The factor-of-two difference between the two formulas is a persistent trap. A conversion facility that implements only the 20 log definition gives a voltage answer that must be halved to obtain the corresponding power figure; an exam problem asking for the correction factor when a channel is terminated in 150 ohms resolves to 6.02 dB by exactly that route.[1571]

## Rules of thumb

Working in dB in the head, without a calculator, rests on a handful of memorised ratios.[49] For magnitudes:

- −3 dB is 0.707, one over the square root of two — conventionally called the half-power point even though it is a voltage figure.[49]
- −6 dB is 0.5, and +6 dB is a factor of two.[49]
- −20 dB is 0.1, and +20 dB is a factor of ten, one order of magnitude.[49]

Because each order of magnitude is another 20 dB, larger ratios are reached by adding: 1,000 times is 60 dB, times 100 is 40 dB, and 1 mV referred to 1 V is −60 dB.[49][1521] Applied to gain, a times-100 amplifier is 40 dB on a Bode plot's vertical scale.[692] Applied in reverse, an op-amp data sheet that states a large DC voltage gain in dB unwinds through the 20 log formula to roughly 100,000.[600]

For power or intensity, including sound intensity, the increments are different: −3 dB is half the power and +3 dB double it, while −10 dB is one tenth and +10 dB ten times.[49] A 3 dB difference between two instrument cooling fans was accordingly treated as a factor of two in acoustic terms.[704]

The substitution of addition for multiplication is the central practical advantage: a chain of cascaded amplifier stages is summed in dB rather than multiplied out.[100][49]

## Logarithmic axes and decades

A frequency response plotted on a linear axis hides detail at the extremes — a roll-off starting at 10 Hz is unreadable when the same axis must also show megahertz.[49] Compressing the frequency axis into decades — 1 Hz, 10 Hz, 100 Hz, 1 kHz, 10 kHz and so on — restores detail at both ends of the span.[49] The same six decades of data that were illegible on a linear plot show the response beginning to roll off at about 100 Hz and reaching 25 dB down further along.[49] A second consequence is that the roll-off traces become straight lines.[49] A decade logarithmic X axis with magnitude in dB on the Y axis converts a logarithmic response into a linear slope and fits wide frequency spans onto one graph, with 0 dB attenuation meaning the filter passes exactly what is fed into it.[225] Roll-off rates are quoted in the same terms, for instance 20 dB per decade.[49]

## Bandwidth and the −3 dB point

Instrument bandwidth is specified at the −3 dB point.[49] A 100 MHz oscilloscope fed a 1 V peak-to-peak 100 MHz sine wave should in theory read down by 3 dB, or 0.707; a measured 880 mV peak is close to that expectation and indicates the front end is performing reasonably.[977] Amplifier bandwidth is stated the same way, as the frequency at which the response is 3 dB down from its flat region.[692]

## Ratios expressed in dB on data sheets

Common mode rejection ratio is normally published as a dB figure, though it need not be, since it is only a ratio of differential gain to common mode gain.[1521] The sign convention is not standardised: the ratio computed as differential over common mode gain comes out positive, yet data sheets frequently print a negative number, and where negatives are used −60 dB represents better rejection than −40 dB.[1521] Some manufacturers simply omit the minus sign.[1631]

A more consequential ambiguity is whether the figure is input referred or output referred. A CMRR quoted at the input of the amplifier inside a probe, ahead of the probe's own gain, must have that gain accounted for in the dB figure — for a 10:1 division ratio, 20 dB — and a specification of −66 dB becomes −46 dB once the correction is applied.[1521] Quoting the input-referred number without saying so makes the rejection sound considerably better than it is.[1521]

Measurement against these specifications is arithmetic in dB. A mean of 9.2 mV divided by 1.78 V, logged and multiplied by 20, gives −45 dB against a 10 MHz specification of −30 dB, comfortably in spec.[1631] Elsewhere a probe read −50 dB where the data sheet promised −60 dB at 20 kHz, missing its specification by 10 dB, though insufficient signal level was a candidate explanation.[Dez9KG6whb0] Probe attenuation itself is checkable the same way: a 20 times attenuator should measure −26 dB through the 20 log formula.[1744]

Power supply rejection degrades sharply with frequency, and the dB figure makes the consequence direct: rejection falling from 75 dB at 120 Hz to only 20 dB at 1 MHz means that at the high end, with 0.5 V of input ripple, the output noise is one tenth of the input noise.[222]

## Referenced units

Where an absolute level rather than a bare ratio is wanted, the reference is named in the unit itself. Spectrum and signal analysers work in dB volts RMS — the lowest range on one such instrument is −51 dBV RMS, equivalent to about 4 mV peak — with noise floors down around −131 dBV RMS.[528][529] Spectrum analysers are also commonly operated in dB microvolts, particularly for EMC work.[1188] The convention extends to acoustics as dB SPL, and to the A-weighted dBA used by sound level meters.[n4NBUruLyoo][1616]

## Dynamic range

Expressing dynamic range in dB compresses ratios that would otherwise be awkward. The human eye covers roughly 90 dB, which corresponds to a little over 30,000 to 1, which is why it copes with full sunlight and with moonlight after adapting.[48] Instrument dynamic range is described identically: a spectrum analyser whose detector output is logarithmically proportional to its input has about 70 dB of range mapped to the height of the display, so signals sitting 40 dB below the top of the screen are read directly off the graticule and the noise floor sits at about −70.[575]

## Acoustic measurement

Sound level meters report in dBA, and small mechanical details of the measurement matter less than they appear to: the correction response curve published for a meter's windscreen foam is under half a dB across the whole frequency range.[1745] Repeatability sets the floor on what can be claimed. Comparing two firmware revisions of a buzzer across several orientations produced readings such as 65.3 and 67.3, with a difference of one and a half to two dB appearing at only one angle — not enough, across all the other measurements, to support a general claim that one was louder.[1745] Bench equipment is characterised the same way, a fume extractor measuring about 70 dBA at maximum and 65 and a half in its quietest mode.[1616]

Calibrating a room measurement system involves adjusting its software reading until it matches an SPL meter set to an appropriate range with A weighting; the calibrated setup then has a defined maximum SPL, in one case 111 dB.[IVWhoGFJQAY] Nuisance noise is quantified the same way — a phone whose boot animation peaks at about 70 dB while displaying the word "quietly".[156]

Ultrasonic power transmission is where SPL figures become load-bearing. Power in air falls off approximately with the square of distance, about 3 dB per metre, so at one metre half the power is lost to the air alone before any other loss is counted.[n4NBUruLyoo] Transmit specifications of 145 dB to 155 dB SPL at 60 kHz were claimed for one such system,[n4NBUruLyoo] and regulatory limits on maximum ultrasound energy make the original 145 dB claim unachievable in a shipping product.[1224]

## Broadband and EMC figures

Attenuation across wide bandwidths is naturally quoted in dB. A low-Q filter formed by transforming a capacitor's parallel inductance into series inductance is broadband and cheap, capable of holding 30 dB of attenuation across perhaps a gigahertz, with the response starting around 20 MHz and, depending on the part chosen, 30 dB endpoints as high as 10 GHz.[9V99J22aiLE]

Near-field probe measurements produce dB differences that are real but not transferable. Broadband noise measured about 15 dB lower on a four-layer board than on a two-layer equivalent, and that is a large difference, but a 15 dB improvement seen with near-field E and H probes does not translate into a 15 dB improvement in a compliance test at an EMC test house.[1273]

## Idiom

The dB has passed into everyday engineering speech to the point of being a marker of fluency, alongside talking in orders of magnitude.[286] Asked whether a glass is half full or half empty, Dave Jones answers: "Well, I'm an engineer, so it's 6 dB down."[49]
