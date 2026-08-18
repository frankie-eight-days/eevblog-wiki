# rc filter

An RC filter is a resistor and a capacitor arranged to attenuate signals above (or below) a chosen frequency, and in its low-pass form it is the simplest way to strip ripple or switching noise off a node.[1116] It is a first-order, single-pole filter: one resistor, one capacitor, and a cutoff frequency given by 1/2πRC.[225][1116] Its ubiquity comes from that simplicity — it is a building block that appears on its own, in cascades, and embedded inside larger topologies such as the capacitance multiplier.[1116]

## Cutoff frequency and roll-off

The −3 dB point of an RC filter is 1/2πRC, and the same formula holds whether the filter stands alone or is buried inside a more elaborate circuit.[225][1116] A 10 kΩ resistor with a 100 nF capacitor gives a nominal cutoff of 159 Hz; 1 kΩ with 100 nF gives 1.59 kHz.[225][1116] Component tolerance sets how closely a measured response matches the calculation.[1116]

The cutoff is not a brick wall.[225] Above it, attenuation increases gradually, which is why a single pole placed at 159 Hz does a poor job of removing a 10 kHz interferer — the separation looks large but the first-order roll-off is too shallow to be effective.[225] Response is conventionally examined on a logarithmic frequency axis in decades rather than a linear one.[225] Adding poles steepens the roll-off: beyond the single-pole RC there are two-, three-, and four-pole configurations, and active arrangements such as Sallen-Key when an op-amp is available.[225]

## Converting PWM to a DC voltage

A pulse-width modulated output from a microcontroller carries no useful DC information on its own — it is a digital signal swinging between the rails.[225] Passed through a low-pass RC filter, it averages to a DC voltage linearly proportional to the duty cycle: a 5 V microcontroller at 10% duty produces 0.5 V, and the full 0–100% duty range maps to 0–5 V.[225] The same principle scales to other rails; a 10% duty cycle on a 1 V peak-to-peak signal settles at exactly 100 mV average.[225] This makes an RC filter a substitute for a DAC in circuits that need only a slowly varying setpoint, feeding an op-amp wired as a voltage follower.[1701]

The averaged output is never pure DC.[225] Residual ripple depends on the filter values relative to the PWM frequency, and a useful design target is to keep it below one LSB of the controlling resolution — for a 12-bit system, under 1.22 mV.[225] A buffer is required between the filter and the load: an RC-filtered PWM output is not adequate to drive a control input directly.[221] Where the filtered PWM sets a supply's output, any noise not removed by the filter passes through the control loop and appears on the output, so filtering of the modulated signal becomes the dominant noise limit — more so than driving the same pin from a quiet voltage reference and a pot.[222]

## Cascading stages and the response-time trade-off

Increasing R and C to buy more attenuation lengthens the settling time, since the RC time constant also governs how fast the output tracks a change in duty cycle.[225] A first-order 10 kΩ / 100 nF filter fed with a 10 kHz PWM signal leaves roughly 100 mV of ripple on the setpoint and about 10 mV on the supply output — inadequate for a supply asked to deliver 100 mV.[225]

Cascading two identical RC sections in series is the cheap way out.[225] A second 10 kΩ / 100 nF stage drops the ripple to the order of 0.1–0.2 mV — hundreds of microvolts — while keeping the response time near 10 ms, which raising the values of a single stage could not do.[225] Cascading is preferable to simply enlarging one stage precisely because it improves attenuation without the corresponding sluggishness.[225]

## Ripple rejection on power rails

For removing supply ripple, the larger the capacitance for a given resistor, the greater the attenuation.[1116] The limit is current: a resistor large enough to filter well drops too much voltage, and a plain RC network is only workable at very low currents — on the order of 10 mA — after which the required capacitance climbs to absurd values.[1116] Adding a second RC stage improves rejection but doubles the voltage drop for the same load current, so a multi-stage RC is still ineffective for anything but small currents.[1116] The case where it works cleanly is precisely the low-current one, such as smoothing a PWM-derived control voltage.[1116]

The capacitance multiplier addresses the current limit by combining an RC filter with a series pass emitter follower.[1116] The transistor's current gain means the resistor and capacitor handle roughly 1/β of the load current — a couple of hundred microamps instead of tens of milliamps for a β of 100 — giving an effective capacitance of C times beta.[1116] The name is contested because the cutoff frequency still follows 1/2πRC exactly as for a bare RC filter; what is multiplied is not the filtering capacitance but the current the stage can pass.[1116] Post-regulation of a noisy converter output can likewise be done with RC or LC filtering as an alternative to a low-dropout regulator or a Zener.[1115]

## Other roles

An RC network on a MOSFET gate slows the edge enough to swamp mechanical switch bounce, which is a practical fix in power-supply sequencing when a physical switch would otherwise make the FET turn on and off rapidly.[995] Series resistance ahead of a filter capacitor also limits input current into a chip, so an RC at an input serves as filtering and protection at once.[759] An RC network lets a microcontroller's on-chip ADC sample a slowly varying quantity such as battery voltage during charging, even where that converter is only 4 bits.[284] Simple tone controls have been implemented as nothing more than an RC filter.[752] Fed a square wave, an RC filter produces an approximation of a sine wave, with fidelity improving as the filter improves.[1417] At cryogenic temperatures, boxes of RC and LC filters both thermalise the wiring and strip high-frequency radiation, whose photons carry energy proportional to frequency via the Planck-Einstein relation.[1594]

Because the topology is so recognisable, an unidentified part sitting behind a series resistor and a capacitor can be read as part of an RC filter configuration during board reverse engineering, narrowing the candidates to something on a filtered rail.[1541] Conversely, RC snubbing networks omitted from a low-cost design are a visible sign of cost-cutting on drive circuitry.[1172]

## Measurement

An RC filter is the standard first test case for frequency-response instrumentation, being trivial to build and having a response that can be predicted exactly and cross-checked against a simulator.[396] A 2.2 nF capacitor with a decade resistance box set to 10 kΩ is enough to characterise a Bode plotting setup.[396] Gain-phase analysis on a network analyser treats such a filter as the device under test, measuring input on one channel and output on another.[1103] On instruments whose own response is flat to within thousandths of a decibel, inserting an RC filter is what makes any response visible at all.[1056]
