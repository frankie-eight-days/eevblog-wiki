# dynamic range

Dynamic range is the ratio between the largest and the smallest signal a system can handle at once, usually expressed in decibels. It matters wherever a single instrument or sensor has to cope with signals of wildly different magnitude without either clipping the large one or burying the small one in noise — a current that swings between microamps in sleep and milliamps during a radio transmission[1325], a spectrum in which a wanted tone sits far below a carrier[587], or an acoustic field spanning a whisper and a screamer[629]. It is distinct from resolution: a converter's bit count sets how finely it divides its span, but the noise floor sets how much of that span carries real information[107].

## Resolution is not dynamic range

Bits and usable dynamic range diverge because of noise. A converter can offer 24-bit resolution without delivering anything like 24 bits of true dynamic range, because the noise floor swamps the lowest bits and makes them unusable[107]. Working the other way, an 8-bit converter is only good for something around 50 dB, which is why a general-purpose oscilloscope FFT cannot substitute for a spectrum analyzer with roughly 100 dB of range[587]. The same 8-bit limit shows up directly on screen: pushed down to 500 microvolts per division while measuring supply ripple, the individual quantisation steps of the math result become visible, a disadvantage of the digital scope that the analog scope did not have when large differences and dynamic range were involved[594]. Bode plotting on an 8-bit instrument is constrained for the same reason, and the high-resolution boxcar averaging modes intended to recover range do not sit well with the measurement[396].

The trade also runs in the opposite direction. A dynamic signal analyzer can have enormous dynamic range in the sense of accepting inputs of very different magnitudes, and still be limited by the bit count of its ADC when those signals occur at the same time — a 14-bit converter is what stops it from resolving vanishingly small distortion products[vwAhHz7Zpzk].

## Oscilloscope front ends and 12-bit converters

In a 12-bit oscilloscope, the converter is not the whole story: the front end ahead of it is not itself 12-bit, but it must supply the low-noise dynamic range that lets the 12-bit conversion mean anything[1503]. Front-end design has advanced to the point that an 800 MHz, low-noise, 500 microvolt per division front end with 12-bit dynamic range performance is buildable at consumer price points, and the same board can be shared across products separated by thousands of dollars without changing that front end[1510].

Unusual vertical range sequences appear to be a consequence of the same optimisation. Where scopes conventionally step 1-2-5, some 12-bit instruments step 1-2-4-5, which is most plausibly explained as maximising the dynamic range performance of the 12-bit converter[1529][p-eLu1z7-cs].

## Measuring a scope's ADC range

The nominal full-scale span of a scope front end is not what the converter actually digitises. At 1 volt per division across eight divisions the nominal span is 8 volts peak-to-peak, yet a signal that appears clipped on screen proves, when the acquisition is stopped and shifted, to have been sampled outside the visible window — there is extra range beyond the display[6qjqhnQiQXQ]. The measurement procedure is to feed a triangle wave, which makes clipping easier to see than a sine, establish that the signal survives at one setting and clips at the next, then walk the generator amplitude down until clipping just disappears; the true range lies between those bounds[6qjqhnQiQXQ]. Not every instrument has much to give: on one 12-bit scope the overrange amounts to a little extra before it clips, and effectively nothing worth exploiting[1501].

## Preserving the range you have

Since dynamic range is finite, most bench technique is about not wasting it.

Attenuation throws range away, so an active probe is built with the lowest attenuation ratio that the design permits — around 1.3 to 1, almost but not quite unity — specifically to maximise the dynamic range of the signal reaching the scope[1733]. A large DC offset wastes range in the same way, by consuming span that carries no information. A power rail probe removes the DC offset before the signal reaches the scope input, so the full 14 bits are available to the AC content riding on the rail; an ordinary active probe without AC coupling cannot do this, and the burden falls on the scope front end's own offset capability instead[1733].

Automatic ranging is the instrument doing this housekeeping itself. A built-in DVM rescales to maximise the dynamic range of an 8-bit converter[701], and a frequency response analyser auto-ranges on every sample point — and adjusts its bandwidth as it sweeps — for the same reason[1521]. In audio transmission the equivalent is the compander, a combined compressor and expander that squeezes the source into the channel's available range and restores it afterwards, standard practice in wireless microphones; the art is in lifting low-level material without also lifting the noise[571].

## Current measurement

Dynamic range is the central specification for a current shunt amplifier, because the current being measured may swing between a sleep-mode trickle and an active burst when a device wakes up and transmits[1325]. Supply voltage sets the ceiling directly: an amplifier running on 2.7 to 5.5 volts has at most 5.5 volts of dynamic range, and if that is insufficient the design is pushed into range switching[1325]. Range switching carries its own penalty — driving an op amp into saturation costs milliseconds of recovery time unless clamping circuitry is added, which means extra parts and extra design work, and the artefact lands squarely in the measurement[1325].

The asymmetry between the two measured quantities is instructive. In a source-measure style instrument the voltage channel is undemanding, and an 8- or 10-bit converter suffices; the current channel is where the massive dynamic range lives, spread across eight ranges, and where converter quality is worth paying for[1190].

Elsewhere the requirement can be modest. A biopotential front end such as an ECG amplifier has enough dynamic range at 3 volts, and the practical constraint is the upper limit — going beyond about 5.5 to 6 volts risks damaging the op amp through its input protection diodes[660].

## Audio

Audio is where the largest numbers appear. A well-designed microphone preamplifier measured at 12 dB SPL equivalent input noise and 155 dB SPL at one percent distortion — not at clipping — yields 143 dB of dynamic range from a single circuit, which few semiconductor circuits achieve and which a tube circuit can match[629]. Converters sold into the audio market quote figures in the same territory: a 24-bit, 192 kHz codec specifies 114 dB of dynamic range for both its ADC and DAC paths, alongside about -100 dB THD[1405]. Competing audio interfaces built on such parts can differ by only a few decibels of dynamic range[1405].

Bench audio analysis is more constrained than the sources it measures. A 16-bit dynamic signal analyzer specifies 90 dB of dynamic range, rising to 130 dB in an optional swept sine mode[536], and an older analyzer tops out at 75 to 80 dB, which is not enough to characterise a low-distortion compound amplifier without an external notch filter ahead of it to suppress the fundamental[vwAhHz7Zpzk].

At the transmission end the requirement collapses. Digitising intelligible voice needs only about 30 dB of signal-to-distortion ratio held over roughly 40 dB of dynamic range, a specification that telephony codecs meet with companding rather than brute-force linear conversion[619].

High dynamic range in a transducer has a downside: powered studio monitors combining efficient drivers with wide dynamic range make the inherent noise floor of their own amplifiers audible as tweeter hiss[1322]. Speakers nonetheless offer considerably better dynamic range than headphones, though headphones seal out room noise and expose small details during editing[169]. Dedicated audio codec silicon is what buys improved dynamic range in a compact recorder, as in the generational step between action camera models[672].

## Sensing, imaging and RF

The human eye sets a benchmark that electronic sensors struggle to meet: roughly 90 dB, a bit over 30,000 to 1, adapting quickly enough that scenes from full sunlight to moonlight all appear broadly usable[48]. This is why a small photovoltaic panel that charges a phone in full sun does nothing indoors — the eye's adaptation disguises how far apart the two light levels actually are[48]. The same gap explains why camera-only autonomous vehicle perception is weaker than human vision at picking out low-light detail, glints and small movements, and why such systems are supplemented with radar and LIDAR[1066]. Camcorders address the problem with dedicated dynamic range modes, which on some models shift the image sensor and visibly alter the frame[2].

Physics instrumentation pushes the requirement further. A neutrino detector module must resolve anything from a single photon striking its photomultiplier up to thousands during a large event, and that wide dynamic range has to be achieved at a cost that permits building thousands of identical units[1gfM_9EdLSs].

In RF, dynamic range is a system-level result rather than a single component specification: the phase noise and noise figure of a radar receiver add up to determine the dynamic range of the whole system, which is why phase noise calibration matters so much to radar operators[1041]. Measurement systems built around FFT analysis rather than a conventional D-to-A converter achieve better dynamic range and a lower close-in noise floor[1041]. Spectrum analyzers are specified accordingly — a mixed-domain oscilloscope's RF input is quoted at -60 dBc, adequate to pull low-level content out from under an -18 dBm peak[199] — and dynamic range is one of the axes on which six-figure real-time analyzers compete[207]. A SAR test chamber achieves very wide dynamic range partly by using fiber optic links, which contribute little noise[201].

## Dynamic range as a headline specification

Instruments intended for precision work advertise dynamic range because it bounds what can be trusted. A 24-bit delta-sigma converter running at 4 megasamples per second specifies 103 dB of dynamic range, improving to 111 dB with -107 dB THD at lower sample rates, which is the kind of part that goes into a source measure unit[607]. A 16-bit precision instrumentation recorder handling 20-volt ranges devotes substantial effort to shielding and to generating clean rails from a single battery, precisely to protect that dynamic range from its own power conversion[1090]; the electrical specifications alone were rarely the whole argument for such a machine against a plug-in data acquisition card, but they were the entry requirement[1090]. The practice extends beyond instruments: dynamic range and digit accuracy were specified for a professional personal computer, an unusual disclosure that reflected a calculator heritage in which the numbers coming out were meant to be trustworthy[904].
