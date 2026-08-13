# time base

The time base is the horizontal-axis scaling of an oscilloscope, set in time per division, which determines how much time the screen width represents and hence how rapidly the trace moves across the display. It is the control that lets fast-changing signals be slowed down into a visible window of voltage versus time.[926][UJjMt2-k99c] Because acquisition sample rate, memory-depth usage, waveform update rate, aliasing behaviour, and trigger arming are all functions of the time base setting, it is one of the primary setup controls alongside vertical scale and trigger level.[1311]

## Sweep behaviour and display modes

On an analog oscilloscope the trace always starts at the left-hand side of the screen, sweeps to the right at the rate set by the time base, and then retraces; a digital oscilloscope presents the same left-to-right time progression.[UJjMt2-k99c] The control is often labelled the main time base, abbreviated "M" (for example, M = 2 µs/div), with a separate zoom window time base where fitted.[480] At very slow settings the swept display becomes impractical, and roll mode is used instead: the trace scrolls continuously rather than sweeping, which suits signals such as an electrocardiogram at roughly one event per second.[660] In X-Y mode there is no time base at all; the X-input voltage positions the dot horizontally and the Y-input voltage positions it vertically, giving a direct correlation between the two signals.[153]

An auto-set function configures the time base, vertical attenuators, and triggering automatically to produce a stable display, though it is not foolproof.[86]

## Ranges and step sequences

Fast time-base limits track bandwidth class: the 50 MHz Rigol DS1054Z bottoms out at 5 ns/div, with an extra step available on the 100 MHz variant,[699] while the hacked Rigol DS1052E/DS1102E conversion extends the minimum from 5 ns/div to 2 ns/div.[70] Higher-end instruments go below 1 ns/div — the Rigol MSO7000 reaches 500 ps/div at 10 GSa/s.[CMoBGGqojqs] At the slow end, 50 s/div is available on low-cost hardware,[1260] and the Rigol MSO5000 offers an extreme 100 kiloseconds per division.[1146]

The conventional step sequence is 1-2-5, but deviations exist. One low-cost scope follows 1-2-5 until the bottom of the range, where it steps 25, 12, and 6 ns/div — a consequence of sample rate and memory depth limits.[1260] The Tekway DST1102B uses a 2-4-8 sequence,[487] and the Rigol HDO1000 steps 1-2-4-5.[p-eLu1z7-cs]

Where a main time base cannot go fast enough, a magnifier mode is the traditional workaround: the Tektronix 2225's standard time base is too slow to examine a 20 MHz signal closely, forcing use of the ×10 magnifier.[196] Analog time bases also drift and require calibration; on an uncalibrated unit, both the 1 kHz probe-adjust reference and a ×10-magnified 100 kHz signal read slightly off their expected graticule positions until the main time base is calibrated.[196]

## Interaction with sample rate, memory depth, and update rate

Reducing the time base (more time per division) reduces the acquisition sample rate once the record length is fixed; changing the time base on the Keysight 1000X directly changes the reported sample rate.[978] Some instruments, such as the Keysight 3000T, offer no memory-depth control at all and always allocate the maximum memory possible for the current mode and time base.[701] The number of sample points per history or segmented frame likewise depends on the time base — 100,000 points per frame at one setting.[1312]

Waveform update rate is jointly dependent on time base and memory depth.[1529] Measured behaviour illustrates the pattern:

- A Tektronix 2 Series reaches its best rate of 18.8k waveforms/s only at a fast time base (10 ns/div) with minimum memory (250 points) in normal trigger mode; slowing the time base drops it to 7.5k at 100 ns/div, 3.8k, 1.9k at 400 ns/div, and 760 Hz at 1 µs/div.[1478]
- An Agilent scope approaches its theoretical 1M waveforms/s only at fast time bases.[617]
- The Siglent SDS1000X has a distinct sweet spot near a 50 ns/div time base, where it reaches 446k waveforms/s in normal mode and 1.357M waveforms/s in segmented mode, falling off on either side.[797]
- The vintage Agilent 54622D manages about 520 Hz at its fastest 5 ns/div, decaying to roughly 120 Hz at 500 µs/div.[591]

The practical rule is to select the lowest memory depth that suffices for a given time base, since that maximises update rate and therefore the statistical chance of catching infrequent anomalies.[1478] Slow time bases also multiply dead time: at 50–250 ms/div the dead time between acquisitions on one scope reaches a quarter of a second.[797]

## Aliasing at slow time bases

Because sample rate falls with slower time bases, most digital oscilloscopes will alias a fast input into a convincing low-frequency waveform, generally with no on-screen warning.[F0HQJIPcDYs][I3FhAhxet7s][j49T1E4UEv4] A 10 MHz input has been displayed as an apparent 1 Hz signal on one instrument and 8.16 Hz on another, while a Keysight 3000 series resisted aliasing even at 2 s/div through anti-alias processing.[F0HQJIPcDYs] The Rigol DHO800 aliases predictably at 200 ms/div without warning,[I3FhAhxet7s][1566] and a 101 MHz input on a low-cost tablet scope aliases once the time base is reduced from its 10 ns/div maximum.[1317] Stopped acquisitions can also differ by one time-base step in how the decimated display is rendered.[j49T1E4UEv4]

## Triggering at slow time bases

A subtle and practically important trap is trigger arming delay: a digital oscilloscope must pre-fill its acquisition buffer before it can trigger, so at slow time bases there is a dead period after pressing single-shot during which triggers are missed. At 1 s/div the arming delay is about 10 seconds, scaling with the time base; at fast time bases the buffer fills essentially instantly and the effect disappears.[1678] At 100 ms/div the same scope triggers immediately every time.[1678] Anomalous premature triggering has also been observed specifically at slow settings such as 500 ms/div.[1320]

## Interaction with measurements and analysis

Many scope features behave differently depending on the time base:

- FFT frequency span and resolution are set by the acquisition, so the time base and memory depth must be chosen together: 65K points at 200 µs/div yields unusable resolution where 2 ms/div resolves the signal, and at 5 ms/div with 65K points a 1 MHz carrier falls outside the computed span entirely.[845]
- Measurement statistics accumulate counts that reset whenever the time base or vertical scale is changed.[1751]
- Vertical-measurement standard deviation improves as more cycles are captured at a longer time base, while horizontal standard deviation worsens with few cycles on screen and improves when only one or two cycles are displayed.[1226]
- Per-probe deskew calibration can be disabled at some settings — on the Rigol DS1054Z it is unavailable at 10 µs/div and becomes available at 5 µs/div.[704]
- Averaging cannot be enabled at very slow time bases, nor in roll mode; high-resolution boxcar averaging remains available but may hide high-frequency noise superimposed on a slow signal — a capture at 100 ms/div can look perfectly smooth until high-res mode is turned off.[660][223]
- Stored reference waveforms do not rescale when the time base changes, so comparisons must be made at a fixed setting; a reference persists for single-shot recapture as long as the time base is left untouched.[704][1324]
- Integration measurements read out in volt-seconds and may require expanding the time base to capture the complete figure.[662]

## Implementation faults observed

Several documented firmware bugs are time-base-dependent. The Rohde & Schwarz RTB2004 displays acquisition artifacts at slow settings around 100 ms/div when channels are switched, and fails to flush and resize its sample buffer cleanly when memory depth is changed, producing a display that looks like a playback time-base compression.[Ott9syzNLuE][l-fuyHCs2Sw] The Rigol MSO5000 shifts the displayed waveform relative to an unchanged trigger point below a certain time base.[UDGsZcAWgL8] The Uni-T UPO3000 leaves a stray display line when the time base is changed in stop/replay mode.[1231] The GW Instek GDS-2000A silently overrides dot display mode with vectors when the time base is expanded toward 5 ns/div.[474] The Siglent SDS1000X exhibited a failure to recover from a very slow time-base setting, attributed to velocity-sensitive behaviour of the horizontal control.[797]

## Time bases as frequency references

Beyond the oscilloscope horizontal control, "time base" denotes the master frequency reference inside test instruments, typically a 10 MHz oscillator. Standard instrument time bases stabilise within about four hours of power-up, but calibration of a precision temperature-controlled crystal oscillator requires the reference to be powered and on site for 48 hours before measurement begins.[424] For residual phase-noise measurement at close-in offsets from the carrier, the time bases of the device under test and the reference oscillator must be locked together, because any DUT instability inside a phase-locked loop's bandwidth would otherwise be lost within the loop; this distinguishes residual from absolute phase noise.[1041]