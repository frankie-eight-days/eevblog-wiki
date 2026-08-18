# high resolution mode

High resolution mode, commonly called hi-res or boxcar averaging, is an acquisition mode on digital storage oscilloscopes that averages consecutive real-time samples within a single acquisition to produce each displayed sample point.[878][610] Trading surplus sample rate for vertical bits, it turns an 8-bit front end into an effective 9, 10, 12 or even 14-bit converter and lowers the displayed noise floor.[878][223] It is the correct noise-reduction tool for single-shot, jittering or modulated signals, where conventional mathematical averaging fails outright.[878]

## Mechanism

The mode operates entirely inside one capture. It takes a single-shot acquisition in real time, collects a run of consecutive samples — ten or twelve, for instance — and averages them into one sample period.[878] Mathematical averaging mode works on a completely different axis: it takes multiple whole waveform captures, and with an average count of four takes the four data points at each position along the waveform and returns one averaged value per position.[878] The two are entirely different ways of averaging, and the distinction is subtle enough that it is routinely misunderstood.[878]

Because the averaging happens between samples rather than between acquisitions, the mode is effectively a moving-average low-pass filter applied to the acquisition record, which is what produces both its benefits and its principal trap.[601][797]

## Sample rate is the raw material

High resolution mode consumes samples that would otherwise be discarded, so it can only work where the scope is sampling far faster than the timebase requires. At the fastest sweep speeds it does almost nothing, because there are not enough samples in the record for the boxcar function to operate on.[610] As the timebase is slowed, the effect grows progressively stronger.[610]

This is why headroom well beyond the usual four-times-bandwidth rule is worth designing in. The Agilent 4000X uses its excess sample rate for a 12-bit high resolution mode on the analog front end, performing the boxcar averaging of those samples in real time; putting 5 GSa/s on a 200 MHz scope is a sound decision for exactly this reason.[383] The resolution gained also depends on the bandwidth left available: a 12-bit Rigol HDO4000 in high res mode with bandwidth limited to 50 MHz reaches 14 or 16 bits, short of the 18 bits an MXO4 can produce.[1529]

## Resolution gained

Most digital scopes carry only eight-bit converters, but with high resolution mode enabled the effective resolution can rise to nine, ten, twelve, or as much as fourteen bits depending on sampling conditions.[878] The Rohde & Schwarz HMO1202 annotates the display with the resolution actually achieved, showing 10 bits when high resolution is switched on, and up to 16 bits when combined with its smoothing mode — from an 8-bit converter.[842] Bits beyond about eight cannot be seen on an ordinary scope screen; they become useful only through FFT analysis, exported data, or on-screen math.[842][594] The improvement in a math result is visible as reduced blockiness, since the calculation has more than eight bits to work with.[594] Applied ahead of an FFT, the mode drops the displayed noise floor.[845]

## Versus mathematical averaging

On a well-triggered repetitive waveform carrying random noise, the two modes can be nearly indistinguishable — the difference bordering on zero for that particular application.[878] The gap becomes stark as soon as the trigger is not stable. Averaging mode relies on repeatable triggering; on a square wave with FM modulation, doubling the deviation from 10 kHz to 20 kHz changes the on-screen artifacts entirely, producing sampling and mathematical averaging artifacts that make the waveform look nothing like the real signal.[878] High resolution mode shows none of that.[878]

The resulting rule is straightforward. Averaging mode is for random noise on a stable trigger, where it works extremely well.[878] High resolution mode is the one to reach for with single-shot signals, or anything that is jittering, modulated, or otherwise not triggering repeatably.[878] High resolution mode is also the more forgiving of the two, lacking the gross failure mode of a forgotten averaging setting silently distorting a waveform.[878] A further practical constraint: averaging is unavailable at very slow timebases and does not function in roll mode at all, whereas high resolution mode remains available.[660]

## The trap at slow timebases

The mode's filtering is indiscriminate, and at expanded timebases it will quietly remove high-frequency noise superimposed on a low-frequency signal. A single-shot capture at 100 ms/div of two slow-changing signals appears entirely smooth with high res enabled, and only zooming in reveals the noise; on a 500 MHz scope the same capture in normal mode shows that noise plainly at the slowest timebase and identically when zoomed.[223] Anyone using high resolution mode at slow sweep speeds should confirm it is not averaging away content that matters.[223]

The same behaviour is what makes the mode useful in the opposite direction. On a wide-bandwidth instrument the trace is thick and fuzzy at every timebase simply because the scope is showing real high-frequency content an analog scope would have averaged out on its phosphor.[223][601] Switching to high resolution mode cleans that up markedly at the slower timebases, restoring an analog-like display of a power supply ripple waveform on a digital scope.[594][601] It is worth being aware of when the mode is on for exactly this reason: an apparently clean supply rail may reveal following noise once the mode is switched off.[224]

## Practical applications

The mode is standard equipment for low-level and low-noise measurements:

- Measuring power supply ripple and noise, AC-coupled and bandwidth-limited, where it reproduces the analog-scope view of the waveform.[594][315]
- Low-current measurement with a current probe, where a reading of 25.7 mA sits down in the noise and requires noise-reject triggering alongside the boxcar averaging.[1413]
- Integration and energy calculation on a microcontroller's power-up current waveform, where a cleaner, higher-fidelity record directly improves the accuracy of the computed result.[662]
- Capturing current-draw signatures for analysis, such as the packet structure in an electronic safe lock.[762]
- Long-record capture combined with a deep memory setting and a 20 MHz input bandwidth limit, so the data can be zoomed into afterwards.[665]
- Resolving small reflections on a transmission line against a background of mains-frequency interference.[386]
- High input sensitivity operation, such as 500 µV/div, where digitiser noise otherwise dominates and low-millivolt signals need to be resolved.[358]
- Observing op-amp waveforms on a 1 GHz instrument, where full bandwidth in sample mode gives a fuzzy trace that regular acquisition mode is simply the wrong choice for.[600]

## Nomenclature and availability

Vendors name the function inconsistently. Boxcar averaging, rolling average and moving average all describe the same operation.[878][792][797] Siglent labels it e-res, for enhanced resolution.[797] Rohde & Schwarz pairs it with a separate smoothing mode.[842] It is normally found in the acquire menu alongside normal, peak detect and average.[223][704]

Modern digital scopes are generally expected to have it, including inexpensive models — a $399 Rigol DS1054Z includes it.[704][1146] Its absence is treated as a genuine deficiency: the GW Instek GDS-2000A and GDS-1000B both lack it, leaving only conventional averaging, and the Rigol MSO5000 omits it as its predecessor 7000 series did.[474][824][1146]

Outside oscilloscopes, the same idea appears in bench multimeters. The HP 3457A, a six-and-a-half-digit meter, is technically capable of seven and a half digits with averaging in high resolution mode, but that resolution is reachable only over GPIB and not from the front panel.[426]
