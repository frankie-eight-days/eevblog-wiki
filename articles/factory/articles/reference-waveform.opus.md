# reference waveform

A reference waveform is a captured trace stored in an oscilloscope's memory and displayed permanently on screen so that later acquisitions can be overlaid against it and compared.[704][1324] Because the stored trace persists through subsequent single-shot captures, it turns a single-channel instrument into a comparison instrument: signals that cannot be probed simultaneously can still be measured against one another, and a circuit's behaviour before a modification can be held on screen while the modification is made.[1324][1081] The same term has an unrelated but equally fundamental meaning in AC theory, where the reference waveform is the arbitrarily chosen signal against which all phase angles are measured.[1469][1470]

## Storage and display on an oscilloscope

The stored trace is written to a dedicated reference memory rather than to a file, and it can be toggled on and off independently of the live channels.[1081] Reference memory is separate from channel count, so scopes vary widely in how many references they provide: two on the Keysight 1000 X series, four on the Siglent SDS5000X, and ten on the Rigol DS1054Z.[1324][1220][704] Ten is more than enough for ordinary comparison work.[704]

The controls are not always where they might be expected. On some instruments the reference button does not store a reference at all; storing is done through the save/recall menu, where a source channel is selected and a destination reference slot chosen.[1081] On the Keysight 1000 X series the function lives under the analyze menu, where references are enabled, saved, and cleared.[1324] Ancillary details can also be poorly handled: one Rigol implementation offers up to ten reference channels but only five display colours to assign among them, and does not indicate which colour is currently selected.[771]

A stored reference is a fixed set of screen coordinates, not a rescalable record. Changing the time base after storage does not rescale the reference along with the live trace, so the comparison is only valid as long as the horizontal and vertical settings are left untouched.[704][1324]

## Sequential probing of multiple signals

The characteristic technique is to use references to escape the limits of both channel count and the number of available hands.[1324] Dense surface-mount assemblies often leave no room for probe holders, and soldering flying leads to test points may require disassembling the product.[1324] The alternative is to find a readily available, always-present signal — a power rail such as 3.3 V is a good candidate — and trigger channel one from it.[1324] Because that channel always triggers at the same point, it establishes a stable time origin.[1324] A second channel is then walked from test point to test point, each acquisition being stored to a reference slot; the accumulated references show the true time correlation between signals that were never on screen together.[1324] With one probe in one hand, the remaining hand is free and the risk of accidentally shorting adjacent pins is reduced.[1324]

Where a trace is being stored specifically for comparison, cleaning it up first is worthwhile: averaging gives a better result than high-resolution mode's boxcar averaging for this purpose, and the averaged trace is what gets stored.[1081]

## Comparison applications

Storing a known-good or known-state trace and re-acquiring against it is the general pattern behind a wide range of bench work.

- **Before-and-after circuit modification.** With all bypass capacitors fitted, both traces are stored as references; capacitors are then removed and the live traces compared directly against the stored ones to see whether the waveform changes at all.[1081]
- **Probe and probing-technique comparison.** A switching waveform captured with an optical fibre probe was stored as a reference so that the same node measured with a high-voltage differential probe could be judged against it.[1557] The same method shows the effect of shortening the ground path on a high-frequency active FET probe, the stored reference and the newly probed trace appearing in different colours.[Y7t6BIhBZhc]
- **Digitiser resolution comparison.** A reference captured with an 8-bit converter provides the baseline against which a 16-bit acquisition of the same signal is assessed.[5YjS4DHKlQU]
- **Protocol repeatability.** Capturing an infrared remote transmission as a reference and then pressing the key again reveals whether the code is identical each time or whether a toggle bit changes, as in the Philips RC5 protocol.[506]
- **Repeated-event verification.** In power-line analysis of an electronic safe lock, the current-draw signature of the correct entry sequence was stored as a reference and the capture repeated so that differences could be seen visually on screen.[762][771] The same approach confirms that two channels of an audio product produce identical output.[1605]

## Production mask testing

In an automated production environment the reference waveform becomes the basis of a pass/fail test. A reference is loaded from a known-good product, a mask is drawn around it defining the acceptable limits, and the oscilloscope then simply reports pass or fail on each acquisition and counts the failures.[1218] Throughput matters here: mask test rates reach 270,000 tests per second.[1218] The capability is close to essential for production engineering test work.[1218]

## Feeding an arbitrary waveform generator

On instruments combining a scope and a waveform generator, a stored waveform can be sent directly to the arbitrary generator without an intermediate file — the source may be a live channel, a math trace, or one of the reference waveforms.[209] The generator scales the imported waveform to full scale and picks up its parameters automatically; a capture of 640 mV peak to peak produced an amplitude setting of 635 mV peak to peak at 200 Hz.[209] Holding the original capture in a reference slot while the generator reproduces it allows the regenerated signal to be checked against the original on the same screen.[209]

## Phase reference in AC analysis

In AC circuit analysis the reference waveform is the signal against which phase difference is defined. Phase has no absolute meaning, so one waveform must be nominated as the reference before any other can be described as leading or lagging; the phase angle phi is the difference of the second waveform from that first one.[1469][1470] Which waveform is chosen is technically arbitrary.[1469] The angle is conventionally read at the zero crossing purely for convenience, though any corresponding point on the two waveforms serves equally well.[1469]

On a phasor diagram the reference is drawn at time zero and the whole diagram rotates at the angular frequency omega as time advances.[1469] Two waveforms crossing at the same points and peaking with the same polarity are in phase, a zero phase difference that puts both phasors in the same direction regardless of their amplitudes.[1469] A waveform crossing at the same instants but moving in the opposite direction, reaching an opposite peak, is in anti-phase — 180° out of phase.[1469] Once phase enters the picture, Ohm's law in its simple scalar form no longer applies and quantities must be treated as vectors.[1470]

## Reference waveform in LCR measurement

Inside an LCR meter, the reference waveform is one of the terms determining what the instrument actually measures. Along with the test frequency and the range resistor, it governs which parasitic contributions dominate the calculated result.[1473] This matters most for in-circuit measurement, where components in parallel with the part of interest contribute to what the meter sees.[1473]
