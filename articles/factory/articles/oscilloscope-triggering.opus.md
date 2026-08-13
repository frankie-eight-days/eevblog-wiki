# oscilloscope triggering

Triggering is the mechanism that decides when an oscilloscope starts a sweep, and it is what turns a stream of samples into a stable, readable picture of a repetitive signal.[159] Together with the time base and the vertical attenuator it forms the core of how an oscilloscope works, and the concept is identical on digital instruments and on the analog CRT scopes where it originated.[86][159] Without a correct trigger setup a perfectly good signal is either invisible, jumping around the screen, or captured at the wrong moment — and a scope whose triggering is poorly implemented is of limited use no matter how good its front end is.[86][1260]

## What the trigger system does

The trigger compares the incoming signal against a user-set level and slope, and starts an acquisition when the condition is met.[983][512] A typical low-level setup is edge trigger, sourced from channel 1, rising slope, DC coupling, no high-frequency reject.[983] The trigger point can be placed anywhere in the record — commonly in the centre of the screen, so that pre-trigger and post-trigger data are captured in equal measure.[UDGsZcAWgL8][1678]

In hardware the comparison is done by a fast analog comparator; a GW Instek GDS-2000A uses an Analog Devices AD CMP 567 ultrafast comparator as part of its trigger circuitry.[475] On digital scopes the trigger also gates memory allocation and the sample rate the acquisition will run at.[1312]

The trigger level is a genuine threshold, not a suggestion: setting it above or below where the signal actually goes simply produces no trigger at all, and on an otherwise periodic-looking waveform that failure to trigger is itself diagnostic information about the signal's true structure.[1360]

## Trigger modes

Three acquisition modes are near-universal: auto, normal, and single.[1716][359][D2PANd9Hu3U][1701] Auto mode free-runs the sweep when no valid trigger arrives, so something is always displayed; normal mode updates only on a valid trigger; single shot arms once, captures one record, and stops.[1183][1716] Auto is forgiving but is not a substitute for a correct setup — the display it produces on a marginal signal can be unstable and misleading.[553]

A common working sequence for capturing a one-off event is to set the trigger level while free-running in auto so the signal can be seen, then switch to normal mode, then arm a single-shot capture.[1183]

## Trigger types

Beyond basic edge triggering, mid-range digital scopes carry a substantial menu of trigger types: pulse width, slope (triggering on the rate of an edge), video, pattern, duration, timeout, runt, rise/fall, bus, and logic.[704][474] Slope polarity is normally selectable as positive, negative, or bidirectional, and the bidirectional option is what makes eye-diagram-style displays possible.[704] Serial-protocol triggering — arming on decoded bus data rather than on a raw edge — is available on scopes with decode options, and is found under the trigger type menu rather than under the source menu.[704][1566]

Cheaper and software-defined instruments are frequently cut down here. The Moku:Go offers only edge and pulse triggering plus holdoff, with no advanced trigger types, and cannot trigger from a math function at all despite the platform's extensive software processing capability.[1701] The NI VirtualBench offers edge, pattern and pulse width only, though its source list is unusually flexible — any analog or digital input, the trigger BNC, the line frequency, or the function generator start.[876] Some very cheap handheld instruments cannot select an "either edge" slope, or omit triggering entirely.[D2PANd9Hu3U][1190]

## Source and coupling

The trigger source is selected independently of what is displayed, which is a frequent source of confusion: a channel-2 waveform will not trigger while the source is still set to channel 1.[196] Beyond the input channels, most scopes offer AC line as a trigger source, which synchronises the sweep to the mains frequency.[704][1716] Line triggering is a useful fallback for getting a usable display out of an instrument with a fault elsewhere in its signal path.[1418]

Trigger coupling and conditioning options — DC, AC, HF reject, LF reject and noise reject — sit in the trigger mode/coupling menu and exist specifically to stop the trigger circuit responding to content that is not the feature of interest.[983][876][1716][1566] When switching noise rides on a supply rail, the trigger will sometimes fire on the real edge and sometimes on the noise, which makes the waveform jump around on screen; noise reject is the direct remedy.[324]

## Holdoff

Trigger holdoff sets a dead time after each trigger during which the trigger system will not re-arm.[159][1360] It is a control many users have never touched and do not understand, and it is available as a dedicated knob on most higher-end older analog scopes as well as a menu item on digital ones.[159]

Its value is on signals with internal structure that would otherwise satisfy the trigger condition many times per cycle. On a packet-based serial signal repeating roughly every 500 ms, setting the holdoff to something like 400 ms causes the trigger system to re-arm inside the quiet period between packets and therefore to catch the start of the next packet every time, producing a stable display.[1360] The same technique — deliberately arming in a dead period — stabilises an otherwise jittery capture of a bus like Canon's LANC.[297]

## Armed and ready: the slow-time-base trap

A digital scope with pre-trigger memory cannot honour a trigger until it has filled the pre-trigger portion of its buffer. At one second per division with the trigger point centred on a ten-division screen, that means five seconds of acquisition must elapse after pressing single before the instrument is actually armed.[1678] An event occurring inside that window is silently ignored. The failure mode is insidious: the setup is correct, the signal is present, and nothing appears — and the natural response is to start doubting trigger level, mode and holdoff settings that were never wrong.[1678]

Instruments differ widely in how, and whether, they communicate this state. Some Rohde & Schwarz models show only a small change from a pre-trig indication to waiting, with no explicit armed annunciator.[1678] The Rigol DHO800 shows a run indication that confirms sampling is happening but says nothing about whether the trigger is armed.[1678] Keysight models using the MegaZoom V ASIC behave inconsistently, sometimes showing a question-mark armed indication and sometimes not, and in at least one case a scope at one second per division took around 20 seconds before displaying a captured waveform — far longer than the time base and division count would suggest.[1678] Display latency after a successful trigger also varies: Rigol instruments tend to put the waveform up immediately, while others wait out the full post-trigger period first.[1678]

The best implementation in this respect is a dedicated hardware indicator: a Siglent instrument with a ready LED next to the trigger level control, which lights exactly at the expected five-second mark, so the user can see at a glance that the instrument is armed.[1678] Dave Jones's stated design preference is for unambiguous terminology and a prominent visual state — the words armed or ready, or a large red-to-green indicator, rather than a small pre-trig label.[1678]

## Signals that are hard to trigger on

Some waveforms defeat most trigger systems. A 100% amplitude-modulated sine wave, used as a standard test signal for variable-intensity displays, is notoriously difficult — essentially every scope tried has trouble triggering on it, and where a trigger can be found it is often a narrow sweet spot.[795][793][ByUiOk00K0U] Aliased signals and low-amplitude signals at high sensitivity are similarly awkward; at 100 µV per division a trigger becomes very touchy, and a failure to trigger properly will corrupt an averaged measurement because averaging depends on a consistent time alignment.[1501]

Scope-specific defects also appear as trigger problems. A Rigol MSO5000 running normal edge trigger with the trigger point in the middle of a 20 Mpts, 2 GSa/s acquisition of an SPI signal made the signals vanish and reappear at random, while the same signals fed to a Keysight 3000 displayed correctly.[UDGsZcAWgL8] Firmware bugs can leave a stopped acquisition looking furry and unstable rather than clean.[567] An Owon SDS misplaces the alternate trigger level marker, which does not sit in the centre where it should.[480] Low-cost instruments frequently show a bandwidth-dependent triggering ceiling: one kit scope would not trigger reliably at 50 kHz but triggered fine at 10 kHz.[1272]

## Practical uses

Triggering is not only about getting a stable display; it is a measurement technique.

**Establishing a time reference.** Triggering on the rising edge of a power rail gives a reference point against which any other signal on the board can be time-correlated.[1324]

**Cleaning up a swept measurement.** In scope-based Bode plotting, triggering off the raw channel-1 response signal gives an unstable result; moving the trigger to the clean gating pulse on channel 2, positive slope, produces a trace that triggers every time and yields a usable frequency response plot.[396]

**Catching intermittent faults.** A trigger set just above a live waveform, in normal mode, single shot, will capture a transient on the mains that would otherwise require sitting and waiting for it.[1183][1283] Setting the level at about 4.5 V on a negative-going edge captures a 5 V regulator dropping out of thermal overload; setting a trigger on a 58 V rail at 100 ms per division captures the rail failing.[512][1452] Glitches and infrequent high-frequency pulses in a common-mode noise measurement can themselves be used as the trigger source.[441]

**Verifying an instrument.** Confirming that both channels produce waveforms and that they trigger, plus a spot check at a high and a low volts-per-division range, gives high confidence that a repaired scope has full functionality.[1492] Conversely, a working trigger system alongside a working ADC narrows a fault down to something else, such as a DC offset problem common to both channels.[1418]

## Learning to trigger

Triggering is one of the skills the auto-set button erodes. Auto-set configures the time base, the vertical attenuators and the triggering and usually puts the waveform on screen, but a beginner who only learns to press it has learned nothing about operating an oscilloscope.[86] The recommendation for a beginner is an analog scope, precisely because it forces an understanding of time base and triggering that carries directly over to digital instruments.[86] Cheap USB and pocket instruments are a poor substitute in part because they lack proper triggering as well as proper input circuitry.[86]

Setting up a trigger for an elusive event is also hard to do under pressure. Built-in training signal generators — sine with glitch, RF burst, runt pulses, digital burst with infrequent glitch — exist so that the trigger can be configured and rehearsed against a synthesised version of the problem before probing the real circuit, which matters when the real event happens once a day or once a week and there is only one chance to catch it.[143][701]

A general caution applies to periodic-looking signals: apparent periodicity at one zoom level is not periodicity. If the waveform looks repetitive but will not trigger at the level it obviously should, the signal is not what it appears to be, and zooming out will usually reveal packet structure at a much lower repetition rate.[1360] This is a classic trap for young players.[1320]
