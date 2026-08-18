# trigger level

Trigger level is the voltage threshold an input signal must cross before an oscilloscope begins an acquisition. Combined with a slope selection, it defines the instant that anchors the displayed waveform: on a positive-going edge trigger, the signal must transition above the set level before the scope will trigger at all.[1320] Because it is the single control that decides whether a waveform stands still on screen or refuses to appear, it is the first thing to check when a scope will not display a stable trace.[UJjMt2-k99c]

## Role in the acquisition sweep

On an analog oscilloscope the trigger starts the horizontal sweep. Once the trigger is received at the set Y value on the chosen edge, the sawtooth ramp applied to the horizontal deflection plates begins to rise and the beam sweeps across the display, drawing the waveform, before retracing rapidly back to the start.[159] The consequence is that on an analog instrument the trigger point sits at the very start of the trace, whereas on a digital scope it is placed in the middle of the record.[685]

Raising the level above the peak of the waveform removes the trigger condition entirely: the display stops updating and the trace freezes or, on a digital scope, the instrument falls back into auto trigger mode and free-runs.[UJjMt2-k99c][617] Dropping it below the negative excursion has the same effect from the other direction.[685] A serviceable analog front end should trigger reliably as the level knob is swept close to both the positive and negative extremes of the signal, on either slope — a check worth running after any internal calibration.[196]

## Setting the level

The level control is normally a rotary encoder, and on many instruments it is also the mechanism used to enter threshold values for other trigger types.[797] A dedicated 50% function, either a separate button or a push action on the level knob, lets the scope locate the waveform and place the trigger level in the centre of it automatically.[685][199][824] This is a one-button alternative to hunting for a threshold by hand on an unknown signal.[685] Its usefulness depends on the implementation: a knob-push 50% that takes long enough to display an hourglass is a poor substitute for a fast dedicated key,[199] and a scope that resets the level to zero rather than to the waveform centre defeats the purpose on any signal with an offset.[685]

Some instruments tie the level control to the trigger mode. On several low-cost scopes the level springs back to an automatic 50% position and cannot be dragged in auto mode; normal trigger mode must be selected before the level can be set manually at all.[1317][1260] Touchscreen instruments generally allow the trigger level to be dragged directly.[nO09bc5ozng][1540]

## Interaction with trigger coupling

Trigger level is only meaningful relative to the coupling of the trigger path. Under DC trigger coupling the threshold is absolute, so every time a new and unknown node is probed and the DC offset differs, the level control has to be tweaked again by hand.[685] With AC trigger coupling the offset is stripped from the trigger path, so a single level set near zero will trigger a good proportion of input signals, and switching between several sources with different DC offsets keeps triggering reliably without intervention.[685] AC trigger coupling is the default on analog oscilloscopes for exactly this reason, and the advantage carries over unchanged to modern digital scopes even though users accustomed to seeing a trigger line on screen tend not to use it.[685]

Selecting AC trigger coupling removes the on-screen trigger level bar on some scopes, which has caused confusion; the level no longer has a defined position relative to the displayed input channel, so printing it on the graticule would be misleading even though the instrument still reports a numeric value.[685]

## Practical placement

Deliberate placement of the level is the standard technique for catching an infrequent or transient event. Setting the threshold just above the amplitude of the normal waveform, in single-shot mode, captures over-voltage spikes on a sense winding,[330] the RF burst from a device under test whose output amplitude is unknown in advance,[368] or mechanical shock artefacts that would otherwise be buried — with the level set just above the noise, a barely perceptible tap on a scope's own front end shows up as a trigger event.[983] A negative level set below the resting line captures a falling event such as a beep pulse.[771] For a logic-level signal the usual choice is the middle of the swing, around 1.5 V on a 3.3 V rail.[p-eLu1z7-cs][1320]

Noise measurement is the awkward case. Ripple and noise are not clean edges, and with normal mode and manual triggering the level can be walked up until the scope barely triggers at all; the working approach is to place the threshold on a noise peak rather than expecting a stable lock, and to avoid auto trigger mode.[594] High-frequency reject and noise reject filters in the trigger path help, though their contribution can be modest.[594][l-fuyHCs2Sw]

Level placement also perturbs measurements of transient behaviour. When probing a power supply's turn-on characteristic, an apparent feature in the response may simply coincide with where the trigger level happens to sit, and moving the level above it re-frames what is captured.[1402] Adjusting the level while a capture is running loses the trigger, which is unavoidable but worth recognising rather than mistaking for an instrument fault.[699][387]

## Advanced trigger types

Trigger level does not fully determine the trigger condition once the scope moves beyond edge triggering. Glitches that wander randomly in the trigger sequence are captured regardless of where the level is set, because the trigger type rather than the threshold selects them.[1583] Edge triggering can be pressed into service by raising the level so it can never fire on the glitch and waiting for the event to arrive, but this is a slow substitute for a dedicated glitch trigger.[1583]

Runt triggering uses two thresholds, a high and a low signal level, plus qualifiers, so the display shows more than one trigger marker at once.[1583][1220] Interval triggering combines a single level with a width criterion, for example triggering on any pulse shorter than 80 ns.[1583] Terminology varies between manufacturers while the underlying mechanisms are the same.[1583]

## Beyond oscilloscopes

Timer-counters use the same concept in analog form. In the Philips PM6672 the front-end comparator takes the incoming signal on one input and the trigger level sensitivity potentiometer on the other; setting that level is essentially all that is required to sense the input.[265]

## Instrument shortcomings

Trigger level is a common site of implementation defects. A visible offset between the displayed trigger line and the actual trigger point — the line sitting above a triangle wave that it is supposedly intersecting — survives the instrument's own calibration routine on at least one budget scope-meter.[1540] Alternate trigger level on the Owon SDS series positions the trigger marker away from the centre where it should be, though moving the level does at least shift the waveform as expected.[480] Trigger level handling has appeared on firmware fix lists for current instruments.[1638]

Interface decisions matter as much as accuracy. Placing the trigger level indicator on the same side of the screen as the pop-up menus causes it to be hidden the moment a menu is opened.[474] Controls that adjust the trigger level without being labelled as such are a source of confusion.[1582] Conversely, permanently displaying the trigger level alongside sweep speed and vertical scale in a dedicated status area is a good use of screen real estate.[480]

Genuine acquisition bugs can masquerade as level problems. An R&S HMO1202 with the trigger level squarely in the middle of the waveform and everything else set correctly triggers in auto mode but, in normal mode, registers a trigger without capturing or displaying any data — behaviour that a comparable Keysight scope does not exhibit with identical probe placement.[879] An RTB2004 with AC coupling, high-frequency reject and a valid level fails to trigger at low frequencies, with the fault turning out to depend on acquisition memory length.[l-fuyHCs2Sw] A trigger level accidentally left down in the noise floor is a more mundane cause of the same symptom, and one worth eliminating first.[1612]

Where the trigger source is external, the level applies to the external input rather than the displayed channel, so the same threshold adjustment will destabilise the display even though the trace being viewed has not changed.[387]
