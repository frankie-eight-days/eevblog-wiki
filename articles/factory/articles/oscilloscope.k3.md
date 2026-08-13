# oscilloscope

An oscilloscope is an instrument that measures voltage with respect to time, displaying voltage on the vertical axis against time on the horizontal axis.[926][UJjMt2-k99c] Its essential advantage over a multimeter is speed: it can display signals changing in microseconds or nanoseconds, which is where all modern digital electronics operates, giving a visual window into circuit behaviour that no other instrument provides.[UJjMt2-k99c][926] Amplitude is read against a screen grid called the graticule, scaled in volts per division, while the horizontal time base spans seconds down to nanoseconds per division.[926]

## Analogue and digital

The fundamental distinction between analogue (CRT) and digital oscilloscopes is that a digital instrument can store the waveform: single-shot capture freezes a one-time event for later analysis, and captured data can be zoomed, measured, and processed after the probe is disconnected.[926][UJjMt2-k99c] Digital scopes also add automated measurements, math functions, and intensity-graded persistence displays.[926][662][601]

Second-hand analogue CRT scopes remain a valid low-cost entry point: a working 20 MHz dual-channel unit typically sells for under US$100 and often for around US$50, with Tektronix, HP, Hitachi, Philips, and Kikusui among the usual brands.[168][498][1022] When buying second-hand, a listing should at minimum show a trace on screen or state the unit is tested, since a beginner is poorly placed to repair a dead channel; scopes sold explicitly as parts or non-working cannot usually be returned.[498][1450] A quick functionality check consists of confirming waveforms on both channels, confirming they trigger, and spot-checking a high and a low volts-per-division range against a known signal source, which establishes correct operation with high confidence.[1492]

## Triggering

Triggering stabilises the display by starting each acquisition at a defined signal level; if the trigger level is set above the signal's excursion, the display stops updating entirely.[UJjMt2-k99c] Beyond basic edge triggering, several subtleties matter in practice.

- **Trigger holdoff** is a dedicated control, present on most higher-end analogue scopes and as an option on digital scopes, that inhibits retriggering for a set interval; it is widely misunderstood and rarely used.[159]
- **Trigger jitter on bursts** arises because an edge trigger presented with a burst of identical cycles cannot distinguish which edge to use, producing jitter as wide as the burst packet itself.[387]
- **Separate trigger path**: the trigger system is a separate analogue system from the ADC and display path, and the external trigger input is physically a different channel, so the scope can genuinely trigger on a signal that the acquisition system never captures and the screen shows nothing.[1320]
- **Arming delay**: on a slow timebase in single-shot mode, a scope may fail to capture an event because it had not finished arming; with the trigger point centred, acquisition memory is split into "50% pre-trigger data and 50% post-trigger data", and the full pre-trigger record must be collected before the trigger is armed.[1678]
- **Persistence for intermittent faults**: leaving a scope running overnight with infinite persistence captures rare runt pulses, glitches, or missed clocks that would otherwise be missed.[3jDRH-6IvZc]
- Some instruments drop their waveform update rate dramatically when not triggering — in one observed case to roughly 20 Hz — rather than maintaining the continuous update users expect.[617]

## Bandwidth, sample rate, and memory

Sample rate matters more than headline bandwidth for single-shot work: a scope without roughly ten times its bandwidth in sample rate has limited usable single-shot performance — a 500 MS/s instrument has a usable single-shot bandwidth of only about 50 MHz.[107] The minimum practical rule is four times oversampling; a 1 GS/s scope meets this at 200 MHz on one channel, but interleaving that rate across two channels halves it to 500 MS/s and limits usable bandwidth to about 125 MHz.[800]

Deep acquisition memory is a defining feature of modern digital scopes and is the reason they have displaced logic analysers for serial-protocol debugging of SPI, I²C, and RS-232, the scope's two-to-four-channel count being its main limitation.[44] Memory architectures vary by manufacturer in how much record is available outside the visible window: one design may offer only the 20K points on screen despite 200M points of installed memory, requiring the time base to be changed to access deeper records, while others dedicate full memory to a single-shot capture by abandoning ping-pong buffering.[1311]

Waveform update rate is a major differentiator. Rates of one million waveforms per second were industry-leading when introduced in 2011 and previously cost US$10,000–20,000 to obtain; mid-range instruments more typically deliver 120,000–140,000 updates per second, and entry-level instruments a few thousand.[701][149][1309][114] High update rates, achieved through custom acquisition ASICs that bypass the CPU, are also why such instruments can appear visually "noisy": more overlapping acquisitions are displayed per unit time, so for valid noise-floor comparisons between scopes the memory depth, analogue bandwidth, intensity grading, update rate, and sample rate must all be matched.[148][610]

## ADC resolution and noise

ADC resolution has moved upward across the market: 12-bit converters are now standard even at entry level, and 14-bit instruments exist, which directly improves the ability to zoom into small signals riding on large DC levels.[1735][1004] Comparing 12-bit scopes meaningfully requires measuring the actual full-scale ADC range and noise floor to ensure an apples-to-apples comparison.[6qjqhnQiQXQ]

Practical noise figures at a 20 MHz bandwidth limit are in the tens of microvolts: measured mean noise floors of 38 µV and 65 µV were recorded on comparable instruments under matched conditions.[1223] Front ends designed for higher bandwidth are inherently noisier, because the amplifier ASICs must be built for the full 1.5 GHz-class bandwidth even when the user bandwidth-limits to 20 MHz.[1529] A 500 µV/division genuine vertical range is uncommon and valuable for low-level work such as power-supply measurement.[369][594] The 20 MHz bandwidth-limit setting exists specifically for noise measurement and is a long-standing standard method, though full bandwidth should be used when assessing signal fidelity and transients.[1735]

Oscilloscopes are not precision instruments for absolute voltage: absolute accuracy is typically on the order of half a percent to a couple of percent, so their strength lies in relative and time-domain measurement, where fine vernier control of the vertical gain can be used to maximise usable resolution.[1226]

## Probes and probing

The standard passive probe is a ×10 compensated design. Switchable ×1/×10 probes are a common source of error, because the switch is easily bumped and no passive means exists for the scope to detect its position; the resulting readings are an order of magnitude out. Professional probes omit the switch for this reason.[778] The probe-attenuation setting in the scope's menu is purely a software multiplier — the hardware input ranges from 1 mV to 10 V per division are fixed by physical amplifiers and attenuators — so a mismatch between probe and setting corrupts every vertical reading, and can make a scope appear unable to reach its lowest ranges.[778] Some probes carry a detection pin that sets the attenuation automatically.[778]

Other probe types covered:

- **Active FET probes** place amplifier electronics in the probe head rather than the scope, require power (usually drawn from a proprietary scope interface), and are used for high-frequency work; units with standard 50 Ω outputs can connect to any scope with a 50 Ω input or an inline terminator.[Y7t6BIhBZhc][1715]
- **DIY resistive probes**: a 1 kΩ series resistor into a 50 Ω-terminated input forms a 21:1 divider presenting 1 kΩ DC impedance, a cheap way to exploit a 1 GHz front end.[1718]
- **High-voltage differential probes** are essential for mains and power-supply work, allowing connections at arbitrary points without the ground-loop hazard of an earth-referenced probe.[932][1744]
- **Optically isolated fibre probes** are the only practical option for high-frequency, high-voltage switching measurements (such as GaN gate drive) where channel-to-channel time correlation must be maintained and differential probes cannot be used.[1557]
- **Current probes** output a volts-per-amp signal that scopes can display directly as amps per division.[812]

At high frequencies, channel-to-channel probe delay differences matter: oscilloscopes include a probe-skew (delay) calibration function, and a centimetre-scale cable-length difference required a 262 ps correction in one demonstration at 160 MHz.[652] Unterminated transmission lines produce reflections that can make a signal at the scope input effectively vanish at certain frequencies.[652]

## Grounding and safety

The BNC shells and probe ground clips of a bench oscilloscope are connected to protective mains earth, a safety requirement for the instrument itself.[Xg_niU86bhI][131] Connecting the ground clip to any point in a device under test that is not at earth potential creates a low-impedance short through the probe shield, the scope chassis, the mains earth wiring, and back into the device, destroying the clip lead and potentially the circuit.[279][131] This is the single most common way beginners damage equipment, and high-voltage differential probes or properly isolated instruments are the standard remedy.[932][1744] Handheld scope-meters achieve isolated, floating channels precisely because they are not earth-referenced.[807][1723]

## Common pitfalls and artefacts

- **Aliasing**: a scope without effective anti-aliasing can display a 10 MHz input as an apparent 1 Hz waveform at slow time bases, complete with a confident (and wrong) automatic measurement.[F0HQJIPcDYs]
- **Microphonics**: multilayer ceramic capacitors in scope front ends are piezoelectric, so tapping the case injects a visible signal; the effect is present in almost every scope on the market. The same effect lets a ×10 probe double as a crude vibration or acoustic sensor.[983][1743]
- **Electrostatic pickup**: standing up from a chair can inject a roughly 100–120 MHz impulse into a shorted probe, reproducible across many scopes, bandwidths, and probe types, independent of the ground-lead loop.[14][20][21]
- **Probe-setting mismatch** producing an apparent inability to reach 1 mV/div (see Probes above).[778]
- **Interpolation traps** when zooming deep-memory captures, where a sparsely sampled record is sin(x)/x-interpolated for display.[1213]

## Analysis features and techniques

Modern digital scopes apply math operators — add, subtract, multiply, divide, differentiate, integrate — to captured data in real time as well as on stopped acquisitions.[662] Integration has direct application in power measurement, since true power in a pulsed load is the area under the current waveform.[708] Other established techniques include:

- **Frequency response (Bode) plotting** by sweeping a function generator and recording amplitude at spot frequencies, or with a built-in frequency-response analyser; the scope's FFT is generally unsuitable for this because a scope does not natively display against frequency.[396][LbqnHtNPt9Y]
- **FFT spectral display**, where best resolution requires deliberately tuning centre frequency, span, and time base.[845]
- **Phase measurement** between channels by automatic measurement, cursors, or arcsine of voltage levels, with roughly half a dozen distinct methods available.[1751]
- **XY mode** for curve-tracer-style component characterisation, historically built into some 20 MHz analogue scopes as a component tester.[1137]
- **Serial triggering and decode** (e.g. SPI), allowing data-level correlation between captured waveforms and firmware.[240]
- **Power-supply ripple and noise** measurement with AC coupling, a 20 MHz bandwidth limit, and the lowest-noise front end available, ideally with a genuine 500 µV–1 mV/div range; the DC-offset control is used to null the rail voltage and zoom onto the ripple.[594][1735][765]
- **Reference waveforms**, stored captures displayed alongside live channels for comparison, complementing the four-channel capability now available even in sub-US$400 instruments.[1324]
- **Roll mode** for very slow signals such as heart rate, typically entered automatically at slow time bases.[665][660]

## Market tiers and architecture

Entry-level digital scopes were redefined by the Rigol DS1052E, which established the roughly US$400 price point in the compact form factor pioneered by the Tektronix TDS220, the industry's first small real-time digital storage scope; its four-channel successor, the 50 MHz DS1054Z at US$399, became the benchmark entry instrument.[1566][703] Below that tier, USB scopes and pocket "nano" scopes are regarded as poor value relative to a US$400 bench instrument or a US$50 used analogue scope.[168] Above it, spending beyond roughly US$1,000 is generally more than a hobbyist or general-purpose lab needs, covering serial decode, mixed-signal analysis, and a few hundred megahertz of bandwidth well before that figure.[ln_XJDPKJlc]

The high-end market — Tektronix, Keysight, Rohde & Schwarz, and LeCroy — prices differently for structural reasons: high-end manufacturers may keep the same model in production for 10–20 years with managed last-time buys, because military, industrial, and government customers write procedures and test environments around a specific instrument and require consistent availability, something lower-tier manufacturers replacing models every couple of years do not provide.[3t9G80wk0pk] Within a product line, two-channel models exist mainly as a cost saving; on a 350 MHz MDO4000-class instrument the saving was roughly US$3,000 on a US$16,500 instrument, and multi-channel system requirements beyond eight channels are more often met by synchronising multiple scopes or modular acquisition systems.[1632]

Internally, the classic digital scope architecture funnels ADC data through an FPGA or ASIC into dual-port memory that the CPU reads to update the display, making the CPU the bottleneck; the performance generation of the early 2010s solved this with custom ASICs handling acquisition, memory, and display plotting directly, relegating the CPU to a secondary role and enabling million-waveform-per-second update rates.[148][701] That class of ASIC has since appeared in instruments starting around US$450.[976] A further generation shift has brought 12-bit resolution and 350 MHz four-channel instruments with 4 GS/s and 500M-point memory below US$1,000.[1735][1717]