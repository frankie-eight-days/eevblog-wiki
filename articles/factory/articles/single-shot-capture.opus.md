# single shot capture

Single shot capture is the oscilloscope acquisition mode in which the instrument arms itself, waits for one qualifying trigger, records a single acquisition into memory, and then stops. It is the defining capability of the digital storage oscilloscope: it allows the capture of events that only happen once, which an analog oscilloscope cannot do at all.[926] Because the waveform is frozen in memory rather than painted on a phosphor, it can be zoomed, scrolled, measured and analysed after the fact.[926][13]

The capability is valuable enough on its own to outweigh most other specifications. A low-end digital scope that can do single shot capture is more useful on the bench than a top-of-the-line analog instrument with dual time bases and high bandwidth, because the digital storage is the thing that matters.[1536] An analog scope remains an excellent learning tool, but single shot capture is precisely what it cannot offer.[722]

## Setting up a single shot acquisition

A single shot acquisition is a trigger problem before it is anything else. The vertical scale, horizontal time base and trigger level are all set in advance, memory depth is often set to maximum so the record can be zoomed into afterwards, and only then is the single button pressed.[1311] The trigger must be in normal mode rather than auto: in auto mode the scope free-runs and produces sweeps whether or not the event occurred, which defeats the purpose of arming for one event.[1228][1183] Normal mode is in effect the continuous equivalent of the same behaviour — "normal mode is basically a single shot capture" repeated on every trigger.[1042]

Once armed, the scope sits and waits. A glitch that arrives minutes later is still captured, so the instrument can be set up and left unattended while the fault is provoked.[HN_eeI12qZw] Slow phenomena are handled the same way: a 100 ms/div time base with the trigger set just above the baseline is enough to catch a transmitter's output burst on a single press of the device under test.[368]

## Single versus run/stop

Pressing stop during a running acquisition and pressing single are not equivalent operations. Stop freezes the acquisition wherever it happens to be in the sweep and displays whatever was already sitting in the buffer, which may be a partial record.[1311] Single waits for the next trigger point and then delivers an entire acquisition in memory.[1311]

This difference extends to how much data is actually acquired. Some capture architectures record more in single shot mode than in run mode at identical settings — on one Keysight platform with automatic memory selection, the single shot record covered twice the time span of the run-mode record at the same time base, a consequence of the MegaZoom ASIC and the acquisition architecture rather than a universal rule.[1311] The same distinction governs how much of the nominal memory is real: with one megapoint set and 3.2 GSa/s selected, a running acquisition only delivers the roughly 32 K points shown on screen, and measurements and saved binary data reflect only that screen data. The full record length is only obtained by performing a single shot capture.[1638]

## Interaction with acquisition modes

Averaging and single shot capture are fundamentally incompatible. Mathematical averaging works by combining many complete waveform captures of a periodic signal — 8,192 of them in one configuration — so with only one acquisition there is nothing to average and the captured waveform remains as noisy as the raw signal.[878]

High-resolution mode does work in single shot, because it averages differently. It performs boxcar averaging on adjacent samples within the one real-time acquisition, running at a higher sample rate and combining ten or twelve samples into each output sample period, all in hardware on the fly.[878] The result is a visibly cleaner single shot trace.[878] It also creates a trap: a slow signal carrying high-frequency noise can be single-shot captured in high-res mode and look smooth as displayed at 100 ms/div, with the noise only becoming visible on zooming in — and reappearing entirely when high-res is switched off for normal mode.[223]

A second display trap is interpolation. On a deep-memory scope, a single shot capture at 50 ms/div zoomed in afterwards can show apparent pulses with ringing that are artefacts of the reconstruction rather than the signal.[1213] Single-shot capturing and then examining the raw samples is what exposes the truth: at 2.5 GSa/s the rise being measured is built from only a handful of dots, and the dot count changes only when a new acquisition is taken.[1220]

## Working practice

Single shot capture underpins most digital debugging on the bench. Contact bounce is caught by arming on the input and closing the contacts once, revealing the single clean pulse followed by a burst of spurious edges.[961] A serial line is found and its baud rate measured by capturing one boot-time burst and cursoring the bit periods.[977][CK5nbC_dBWk] Current drawn by a solenoid-driven lock through a 10 ohm shunt is captured in one press, yielding roughly 250 mV of data packet detail at 100 mV/div.[762] Slowing the time base and re-capturing allows the record to be scrolled and compared against an earlier attempt.[771] Power supply behaviour — the ramp of a 30 V output with no overshoot on turn-on — and fast transients on a 5 V rail are both single shot measurements.[512][1733]

Advanced trigger types exist largely to make single shot capture selective. Runt, glitch, pulse-width and zone triggers let the scope arm on exactly the anomaly of interest and capture it every time, and are now available on sub-$400 instruments.[1583][1220] Without such a qualifier the event is effectively unreachable: repeatedly pressing single and hoping to land on an intermittent feature is not a workable method.[383] Zone triggering applied to an unsynchronised glitch is similarly unreliable, since successive single shot captures place the glitch at random positions relative to the waveform edges.[1583]

A single shot record of one channel carries no time relationship to a separately captured record of another channel, because each was triggered from its own signal under test. Probing points one at a time and capturing each in turn gives the waveforms but destroys the time correlation; triggering every capture from a common reference such as a power rail edge, and storing earlier captures as reference waveforms, restores it.[1324] A multi-channel scope solves the problem directly by capturing several time-correlated waveforms in one acquisition.[1324]

## Instrument-specific behaviour

Implementations vary enough to cause confusion. Single shot capture is disabled entirely in dual time base mode on some scopes, so pressing single reports the function as disabled even though run/stop still captures both time bases simultaneously.[1235] Alternate trigger mode likewise cannot be single-shot captured, though run/stop works.[1235]

Segmented memory changes what single means: with an N-single count of 500 configured, pressing single acquires five hundred waveforms into history rather than one, and only setting that count back to one restores single-acquisition behaviour.[HN_eeI12qZw][1529][1744] History mode may also switch itself back on automatically when single is pressed.[HN_eeI12qZw]

Other quirks are display artefacts. A high-update-rate scope in normal mode can leave multiple waveforms on screen after a single triggering event where a single capture is expected.[1042] Stopping on some instruments swaps the displayed multi-waveform image for the true single-shot record only at the moment of stopping.[617] The single button may not be a button at all — on one handheld the hold key serves as the single shot trigger.[1540] Deep-memory single shot records have also been observed to vanish from the display when the horizontal position is adjusted at slow time bases.[EVRdTY4LNhg]

Voice control has been demonstrated as an alternative to reaching for the front panel, on the reasoning that probing a fine-pitch pin with one hand while operating the scope with the other is awkward, so speaking a command to place the scope in single shot capture mode solves a real ergonomic problem.[1221]
