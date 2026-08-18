# square wave

A square wave is a two-state periodic waveform that spends its time at one of two levels and transitions between them as fast as the generating circuit allows. Its defining electrical property is that it is not a single frequency: a square wave is a fundamental plus all of the odd harmonics at diminishing amplitudes, and adding up those sine waves is what produces the flat tops and steep edges.[652][1439] That harmonic content is the reason the square wave is simultaneously the most useful signal on a test bench and the one most likely to expose a weakness in whatever is carrying or measuring it.

## Harmonic content and bandwidth

Because the edges of a square wave are built from high-order harmonics, the frequency content of the signal extends far above its repetition rate. A 50 MHz crystal oscillator output has frequency components reaching into the gigahertz range purely because it is a square wave rather than a sinusoid.[1715] A step change is, for the same reason, a multi-frequency event, which is why a square wave rather than a sine wave is the correct stimulus for demonstrating transmission-line behaviour — reflections and improper termination alter the edge in ways a single-frequency test hides.[652][1439]

The corollary is that any bandwidth limit in the signal path kills the high-frequency content and visibly rounds the waveform. A 10 MHz square wave viewed through a probe rated at 350 MHz in ×10 mode looks like a square wave; switching the same probe to ×1, where the bandwidth is far lower, degrades it immediately.[453] This is also the basis of the standard rise-time measurement: feeding in a very fast rise time square wave and applying 0.35 divided by the measured rise or fall time gives the bandwidth of the instrument under test.[70]

Steep edges also excite behaviour that slower waveforms never reveal. Low-frequency pulse-response anomalies in an oscilloscope front end show up on a plain 1 kHz square wave and do not appear on a ramp, because a ramp is simply moving too slowly to provoke them.[6XpyOGw6RFM]

## Generating and squaring up

Square waves are commonly produced by squaring up something else rather than by synthesis. A slow, varying input passed through a Schmitt trigger squares up as it crosses the upper and lower threshold levels, so a sine wave in yields a square wave out provided the input actually reaches both thresholds.[267] Mains-derived clocks exploit this directly: the 50 Hz mains is filtered, divided down and converted to a square wave to serve as a timebase.[131] A comparator does the same job for arbitrary input magnitudes, cleaning a signal into something a microcontroller can accept, typically with a little hysteresis so the output does not flap around the threshold.[809] An op-amp can be pressed into service as a crude comparator where the result need only be good enough — the output will not be a perfect square wave — though op-amps are poor comparators and this is a compromise rather than a design choice.[713]

Digital sources give square waves for free. A crystal oscillator module contains the oscillator circuit and an output buffer and puts out a square wave on its output pin.[1089] A binary counter clocked from an oscillator produces a series of square waves, each bit at half the frequency of the one above it, so a 100 MHz input divides down through 50 MHz, 25 MHz, 12.5 MHz and onward to a few hertz.[8OaZ89TN0fo] A microcontroller timer toggling a pin produces a square wave of chosen frequency without any delay routines.[1140]

Function generators approach the problem from the other direction. Traditional instruments generated the square wave first and derived the other shapes from it, converting square to triangle and then shaping the triangle into a sine.[1724] DDS-based generators, by contrast, handle square waves badly: jitter on square wave output is a well-known weakness of the technique, severe enough that some designs avoided generating square waves from the DAC at all and instead ran a triangle wave into a comparator, at the cost of only two or three selectable slew rates and a 10% minimum duty cycle.[1032] Built-in generators on scopes and handheld instruments generally offer sine, square, ramp, pulse, DC and noise as fixed shapes.[522][149] Some multimeters include a square wave output as a stimulus source; one such instrument emits a 3 V square wave at a selectable frequency from 0.5 Hz upward on the milliamp jack.[56]

## As a bench test signal

The probe compensation output on an oscilloscope is a 1 kHz square wave, and compensating a ×10 passive probe consists of trimming its adjustment until the displayed square wave is flat and even.[1367] The compensation cap serves the 9 MΩ resistor of the ×10 path, so the adjustment does nothing in ×1 mode.[1367] A badly compensated probe is immediately visible as a sloped or overshooting square wave.[779][879]

Square waves are the standard stimulus for characterising acquisition behaviour. Waveform update rate is measured by feeding in a square wave — 1 MHz on one instrument, a 2 MHz signal on another — and counting pulses on the scope's trigger output with a second instrument or counter; measured results of 1.9 k and roughly 23.5 k waveforms per second have fallen well short of headline specifications of up to 280,000 per second.[1478][617][1220] Trigger jitter problems likewise surface with a clean square wave input, for example 5 V peak to peak at 20 MHz, with infinite persistence turned on to accumulate the spread.[683][699]

A square wave also exposes the interpolation trap. With too few samples in memory, a square wave can be reconstructed into something bearing no resemblance to the input — a failure of memory depth, not of bandwidth, and reducing the analog bandwidth to 20 MHz makes no difference to it.[1213] The same signal is the natural test for aliasing and for basic auto-set competence.[430][1231]

For extreme linearity requirements the flat top of a square wave becomes the specification itself: an isolated oscilloscope design aiming for one part in 8,000 requires the top of a square wave to be linear to that degree, which ordinary probes — good to perhaps 1% — cannot deliver.[1119]

## Measurement error and instrument response

Average-responding AC multimeters are calibrated to give the correct answer for a sine wave, so any other shape introduces a known error. A symmetrical 50/50 duty cycle square wave reads approximately 11% high on an average-responding meter, against 0% error for an undistorted sine and −3.8% for a triangle wave; a true-RMS meter reads all of them correctly.[1448] The further the waveform departs from a sine, the larger the error, and square waves, triangle waves, noise, pulse waveforms and SCR switching waveforms all fall outside the calibration assumption.[1448][99]

Peak and peak-to-peak figures carry no shape information at all: a sine, triangle or square wave all reading plus one and minus one have identical peak-to-peak values despite entirely different energy content.[1417] Duty cycle matters as well — a pulse-width modulated square wave that is high 10% of the time has an average value quite unlike its peak.[1417] Meters with frequency and pulse-width functions read duty cycle directly; a 1 kHz square wave with a 2.5 V offset at 20% duty cycle displays as 1 kHz with 0.2 ms high and 0.8 ms low pulse widths.[249]

Fast edges are also an EMC hazard for measuring instruments. Feeding a multimeter's amps jack a 10 V peak-to-peak square wave at 10 MHz — with nothing else connected — produced large spurious current readings through conducted common-mode pickup, and square waves were worse than sine waves of the same amplitude.[933][987] Adding ground beads to the system ground drastically reduced the effect without eliminating it.[987]

## Applications

Square waves appear as the working signal in a broad range of circuits:

- **LCD drive.** An LCD segment must see zero average DC or it will eventually be destroyed, so it is driven with a continuous 100 Hz square wave with no DC offset.[1045] Driving a segment across the input and output of an inverter — whose two ends are in antiphase — yields double the supply's peak-to-peak swing across the panel: a 5 V peak-to-peak square wave into a 74HC04 or 74HC14 produces 10 V peak to peak measured differentially.[1046]
- **Charge pumps and multipliers.** A Dickson doubler fed a square wave from a microcontroller pin gives an output of twice VCC.[483] A Cockcroft-Walton multiplier does not require a sine wave input and in most cases is in fact driven with a square wave.[469]
- **Inverters.** Cheaper uninterruptible power supplies switch their H-bridge to produce a simple square wave output; because a MOSFET turned on hard has very low on-resistance, dissipation in the switches stays modest.[504]
- **Sensor excitation.** A fluxgate current probe drives its low-saturation core with a square wave that alternates polarity, pushing the core into saturation in each direction.[296]
- **Vacuum fluorescent displays.** The filament of a VFD is typically driven not with a sine wave but with a square wave, measured at around 6.8 V average in one instance.[717]
- **Vehicle charging.** The control pilot pin of an electric vehicle charger outputs a 1 kHz square wave whose duty cycle encodes the maximum current the car may draw.[1437]
- **Clamping and protection.** A 7 V square wave swinging between 1 V and 7 V into a 1 kΩ dropper and a 5.1 V Zener is clamped sharply at 5 V on the output.[908]

Square waves are also convenient for driving mechanical loads slowly enough to observe: an 8 V peak-to-peak, 1 Hz square wave was enough to step a camera iris mechanism open, and a 1 Hz square wave drives a hard drive actuator in abrupt steps where a triangle wave gives smooth linear motion.[937][395]

## Limitations and failure modes

The abruptness that makes a square wave useful also makes it destructive in the wrong place. A power amplifier fault that put a 40 V peak-to-peak square wave across a tweeter produced huge cone excursions and probable mechanical damage, since the driver was never designed for that.[1072] Square-wave excitation of a component also generates harmonics in unintended domains: a capacitor driven with a square wave emits acoustically at twice the drive frequency, the second harmonic rather than the fundamental.[1743]

Not every two-state signal is a square wave. A random telegraph signal switches between two current levels but has randomness in the interval between transitions, making it closer to a randomly pulse-width modulated waveform than a periodic square wave.[1594] Real square waves also carry imperfections worth capturing: a pseudo-random 1 Mbit/s square wave with deliberate positive and negative glitches of about 1.5 V occurring roughly every 15 ms is the standard exercise for a scope's glitch and pulse trigger modes.[1583] And a square wave that looks clean at a driver's output can be badly degraded by the time it has crossed a long, poorly controlled interconnect.[1365]
