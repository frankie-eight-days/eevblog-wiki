# probe compensation

Probe compensation is the adjustment of a passive oscilloscope probe's trimmer capacitor so that the probe's divider stays flat across frequency when connected to a particular oscilloscope input. It is performed by hooking the probe to the scope's compensation output — a square wave, conventionally 1 kHz — and trimming until the displayed edge is square rather than rounded or overshooting.[1367][1709] An uncompensated probe misreports edges, and on a scope or probe with no adjustment available at all the instrument becomes unusable for high-frequency detail.[359]

## The adjustment

Compensation applies to the times 10 setting only: the trimmer works against the 9 megaohm series resistor that forms the divider in times 10 mode, so nothing happens in times 1.[1367] The probe is hooked to the compensation output and trimmed with a small adjustment tool until the 1 kHz square wave is square.[707][1367]

The trimmer's range is a specified quantity. One 10:1 probe specifies a compensation range of 10 to 35 pF, whose midpoint of 22.5 pF is the value used to represent the compensated probe in simulation; a series resistor of around 68 ohms is also typical in that network, though its exact value has very little effect on the response.[1445] Because the range is finite, unusually high scope input capacitance is a real concern: a 1 megaohm input at 24 pF, against the 14 pF of an earlier generation of the same family, raises the question of whether the probes supplied with it can still be brought into range.[1638]

Compensation is specific to the scope input, not to the probe alone. Different oscilloscopes have different input capacitance, so each probe must be re-compensated on each scope it is moved to.[707]

## Where the trimmer lives

Passive probes come in two styles: the compensation adjustment sits at the probe head, or it sits at the connector end where the cable plugs into the BNC.[1367][1119] Both do the same job.[1367] Higher-bandwidth probes are most commonly compensated at the connector end rather than at the tip.[707][1367] Within a single vendor's range the two conventions can sit side by side — of two Rigol probes with essentially the same input capacitance, the RP2200 is compensated at the probe tip and the RP3300 at the end of the cable.[707] The 500 MHz probes shipped with a 1 GHz scope are likewise end-compensated, times 10 only, which is what a passive probe at that bandwidth is expected to be.[1220]

Some probes carry both a low-frequency adjustment on the probe body and a separate high-frequency compensation at the cable's connector end, adjusted in sequence.[842][1367]

Moving all the compensation to the termination end rather than the probe head is what allows some hands-free probe systems to be usable at times 1: with the adjustment made at the termination, there is nothing left to trim at the tip.[GS0WqUKZ-3c][1362]

## Automatic compensation

Probes with an identification interface — a one-wire chip in the head that reports a serial number — dispense with trimmer caps entirely. There are no compensation adjustments at either the tip or the scope end; the probe is hooked to the calibration port and an auto-calibration routine is run, and the scope stores the resulting compensation against that probe's serial number.[1081][1367] The result is that the same probe moved to another channel is recognised as not yet compensated for that channel, because the stored setting is per channel as well as per probe.[1367]

Active probes are not exempt. They still have to be compensated; the correction is simply stored internally against the probe's serial number rather than dialled in by hand.[1368][1718]

A scope may also report whether a connected probe needs alignment at all, and allow the adjustment to be made live with the waveform on screen while a screwdriver turns the trimmer.[842]

## Symptoms of poor compensation

The visible signature of a mis-set trimmer is a square wave that is not square: rounded corners when undercompensated, overshoot and ringing when overcompensated.[GS0WqUKZ-3c][1185] Overshoot on a step is the expected consequence of using a probe on a scope it has not been compensated for.[1185] Compensation state can also plausibly explain triggering trouble on a badly shaped edge, though a poorly compensated probe on one instrument may still trigger reliably where a properly working setup on another does not.[879]

Probes with no adjustment at all cannot be corrected. A pocket scope supplied with a probe having no compensation adjustment on either the probe or the instrument shows severe overshoot and undershoot on a 1 MHz square wave, making it useless for high-frequency detail regardless of the claimed 40 MHz analog bandwidth.[359] Shipping an otherwise proper scope probe uncompensated and unadjustable counts as a design failure in itself.[359]

Stray hand capacitance acts as an uncontrolled compensation change: touching an active probe's tip structure with the fingers alters its characteristic response directly.[1715]

## The compensation output

The compensation signal is a low-frequency square wave, typically 1 kHz, brought out to a pin or pad on the front panel.[1367][1709][1723] Its presence is treated as a basic expectation of a bench oscilloscope, including in tablet-format and very low-cost instruments.[1317][1492] On some designs it is generated by dedicated chips rather than by a general-purpose output.[1477] Its absence is a defect, though not a fatal one on an otherwise working secondhand instrument.[559] Conversely, seeing a clean square wave on the compensation output through a channel is a quick confirmation that a repaired or salvaged scope's front end is alive.[690]

## Distinct from the attenuation setting

Compensating a probe is separate from telling the scope what attenuation the probe is set to. The volts-per-division reading is only correct if the scope's probe setting matches the switch position on the probe itself: switching the probe to times 10 requires switching the channel's probe factor to times 10 as well.[778][441] Scopes with probe identification handle this automatically, detecting the times 10 probe and setting the vertical scale to match.[1367] On scopes without it, a front-panel or menu probe-attenuation control that is quick to reach is a usability point in its own right.[797][ByUiOk00K0U]
