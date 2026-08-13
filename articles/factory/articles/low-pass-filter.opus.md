# low pass filter

A low-pass filter passes signal content below a corner frequency and attenuates everything above it. In its simplest form it is a resistor in series with a capacitor to ground — a first-order RC filter whose corner frequency is set by nothing more than the value of that resistor and that capacitor.[611][225] It is one of the most widely deployed blocks in electronics, appearing as a two-component afterthought on an ADC input, as a distributed copper structure in a microwave front end, and as a dedicated eighth-order instrument costing more than the equipment it is patched into.[232][892][620]

## Corner frequency, order and roll-off

The corner or cutoff frequency of a first-order RC section is fixed by the product of resistance and capacitance, and moving either value moves the corner directly: doubling the resistance halves the corner frequency.[611] Time constants translate to frequencies the same way — a 50 ms charge time constant, the figure microphone manufacturers conventionally use, corresponds to an electrical roll-off pole with a −3 dB point in the region of 3 Hz.[609]

Order determines how steeply the response falls beyond the corner. A first-order section rolls off at 6 dB per octave; a second-order section at 12 dB per octave.[169] High-order filters approach a brick wall — an eighth-order low-pass set to 50 kHz stays flat across the passband and then drops away almost vertically at the corner.[620] Order costs components and complexity, so the choice is a trade between transition-band sharpness and part count.

Beyond first order, the usual construction is an LC ladder: a shunt capacitor to ground, a series inductor, another shunt capacitor. A pi-section arrangement of two capacitors around one inductor is the canonical form, and Butterworth pi designs are standard enough to be generated from online filter calculators.[823][343][353] Op-amp based active low-pass filters cover the audio and instrumentation range where inductors are impractical.[836] Switched-capacitor devices offer another route: an eighth-order low-pass switched-capacitor filter can be bought as a single part, as in the MAX7400 used in the Agilent U1733C LCR meter.[234]

## Non-ideal behaviour

A real low-pass filter does not attenuate indefinitely. Above a certain frequency the response bottoms out and recovers, producing a notch shape rather than continuous roll-off — so a filter should be designed to place its deepest attenuation at the frequency actually being suppressed, since everything above that point comes back.[343] Much of this degradation is physical rather than topological: parasitics in the response come from the construction of the filter, and the same schematic built with different layout and component choices behaves differently.[353] Dead-bug or free-air construction, which minimises distributed capacitance, improves matters over a compromised layout.[353]

## Converting PWM to DC

Passing a PWM waveform through a first-order RC low-pass filter averages the duty cycle into a proportional DC voltage — a 5 V microcontroller output switching between 0 V and 5 V yields a linearly proportional 0–5 V analogue level, provided the filter values are chosen correctly.[225] A 10 kΩ resistor with a 100 nF capacitor is a workable combination for a 100 kHz PWM carrier.[225] The resulting node is high impedance, so it is normally followed by a voltage-follower op amp, which draws no input current and therefore does not disturb the filter it is buffering.[600]

## Signal conditioning ahead of an ADC

Low-pass filtering is standard practice on the analogue path into a converter. In an energy meter the chain runs current transformer, burden resistor, low-pass filter, ADC.[409] Multiplexed cell-voltage measurement in a battery charger routes divided taps through a 4051 analogue multiplexer and a low-pass filter before the main ADC.[397] Around a current shunt, a low-pass filter removes switching noise and load transients before amplification.[259]

Source impedance matters here, because converter sample-and-hold inputs need a low-impedance drive. A series resistance of 330 Ω in the filter is low enough not to cause a problem when driven from an op-amp output; higher values may need a buffer between the filter and the converter.[232] Feedback-based current measurement uses the same idea, with low-pass filtering capacitors placed across the transimpedance feedback resistor.[406]

Filtering also solves architecture-level problems. Zero-drift amplifiers chop at a specific frequency, and if that frequency falls inside the measurement band it corrupts the result — the original µCurrent chopped at roughly 13 to 15 kHz, squarely in the range of interest. A device chopping above 200 kHz allows an output low-pass filter to place the chopper artefacts entirely outside the operational bandwidth.[1328]

## RF front ends

Superheterodyne receivers place a low-pass filter between the input attenuator and the first mixer, so that only content below the intended input range reaches the mixer and generates the intermediate frequency.[1109][892] At these frequencies the filter is often built from copper rather than parts: a distributed element filter, in which the pads are capacitors to ground and the meandering traces are series inductors, forming a multi-stage LC low-pass in the layout itself.[823] Bowtie low-pass filters, named for their shape, appear at several points in a spectrum analyser signal chain to take the upper edge off a band.[892][1101] The trade is cost against performance — a distributed element filter is cheaper than discrete parts, and a redesign may swap a distributed structure for discrete capacitors and inductors, or the reverse.[1101]

## Instrument functions

Many bench multimeters include a low-pass filter mode for work on motor drives and other electrically noisy equipment, removing high-frequency content that would otherwise corrupt an AC reading.[75][10] The Agilent U1272A provides a 1 kHz low-pass mode on both millivolt and volt ranges specifically to reject switching noise.[249] Meter VFD modes are the same idea packaged for variable frequency drive work.[CYm-4gbl1Zc][1602] A filter can be forced on rather than offered: some firmware enables the low-pass filter by default even in DC mode, which suppresses coupled RF but limits what the instrument will show.[987]

Universal counters carry switchable input filters — a 100 kHz low-pass keeps noise above that frequency from producing false counts, though it cannot help with noise inside the passband.[961] Oscilloscopes implement low-pass filtering in maths and DSP: an adjustable-bandwidth low-pass on a maths channel visibly smooths high-frequency components and reduces amplitude as the bandwidth is lowered.[209][310][662][CMoBGGqojqs][792] Absence of any such function is a real limitation on an otherwise capable instrument.[703] Power-measurement modes apply a selectable cutoff — up to 100 kHz — so that a switching-noise-laden current waveform can be measured cleanly at line frequency.[VTHcxTst_RA] Field-measurement instruments do the same, using a low cutoff such as 2 Hz to strip high-frequency content from a magnetic field reading.[UJ6JG4eV0nY]

Standalone programmable filters, such as the Stanford Research SR650, provide independent high-pass and low-pass channels; cascading a 10 kHz high-pass into a 20 kHz low-pass produces a band-pass response between those frequencies.[620]

## Audio

Loudspeaker crossovers are the archetypal audio application, splitting the band between drivers with a low-pass to the woofer and a high-pass to the tweeter — for instance a 1400 Hz Linkwitz-Riley low-pass at 12 dB per octave paired with a 4 kHz high-pass at 6 dB per octave.[169] A powered subwoofer carries its own low-pass filter on its amplifier board.[1519] Digital audio devices with user-settable filter coefficients allow the same shaping in software, in real time.[1569] Mixing consoles and PA equipment stack high-pass and low-pass sections around each channel for equalisation and for extracting specific tones from a line.[840][354][738]

## Measuring the response

The response of a filter is found by sweeping a source through it and plotting output amplitude against frequency. A spectrum analyser with a tracking generator does this directly, feeding the source through the filter under test and displaying the resulting curve.[343] The same measurement can be made with a scope driving a function generator over USB, with the filter input on one channel and its output on another.[LbqnHtNPt9Y] A flat reference sweep taken with the source connected straight to the input establishes the baseline before the filter is inserted in series.[620] Instruments with built-in frequency response analysis produce the plot on screen in real time rather than requiring the sweep to be tabulated into a spreadsheet.[396][N63dJHbCdbk]

## Diagnostic use

A low-pass filter is also an investigative tool. Filtering the output of a 555 oscillator strips the 55.5 kHz carrier and leaves a 55.5 Hz modulation component that is otherwise invisible on the raw waveform — the filter separating two superimposed phenomena that share a single node.[160]
