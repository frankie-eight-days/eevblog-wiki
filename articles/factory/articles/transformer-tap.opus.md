# transformer tap

A transformer tap is a connection brought out from an intermediate point on a transformer winding, so that one transformer can supply several different voltages rather than a single fixed one.[1301][440] Taps appear on both sides of the magnetics: primary taps let one design be wired for different mains voltages, while secondary taps let a downstream circuit select the lowest usable input voltage for the job.[569][512] In linear equipment the secondary tap is the single most important thermal design element, because everything above the tap voltage is burned as heat in the pass element.[828][440]

## Primary taps and mains voltage selection

Multiple primary taps are the standard way of making one product worldwide-compatible: the tapping is changed for the local mains, and only the transformer itself differs between 50 Hz and 60 Hz markets.[569] Consumer gear often exposes this as a slide-type voltage selector on the case, which is mechanically a three-pin tap selector on the transformer primary.[1756] Where no external selector exists, the tap change may be an internal jumper, or may not be provided at all.[314]

The HP/Agilent E3610A illustrates the alternative approach. The mains wiring runs from the IEC input through the front-panel switch and straight into the transformer with no solder tabs, no internal jumpers, and no accessible taps, so there is no way to convert the standard unit to 240 V operation.[166] A separate transformer is used for each market, with the 240 V version sold as an option rather than a tap change.[166] Building one tapped transformer instead of two part numbers is the better engineering choice, and its absence here is a design failing rather than a necessity.[166]

## Secondary taps in linear power supplies

A linear regulator drops the difference between its rectified input and its output across the pass transistor, so a single high-voltage secondary would dissipate enormous power at low output settings. Tapped secondaries solve this: the supply switches to a lower tap as the set voltage falls, keeping the headroom — and the dissipation — bounded.[512][440] A linear bench supply of any range therefore needs taps as a matter of course.[314]

Tap switching is normally done with relays, audible as a click as the output voltage crosses a boundary.[439][gqzZHbEfWDU] The Rigol DP832 instead switches its secondary taps with triacs and triac drivers, an unusual substitution for the conventional relay.[512] A toroidal-transformer supply with three relays visible inside can be expected to carry three taps.[TQcV3ftPLgA]

Measured tap structures are modest in number. The Siglent SPD3303X has three taps, switching at roughly 8 V, 16 V and 24 V, and will only change tap with the output enabled.[828] The Atten PPS3205T-3S transformer is labelled with 0 V, 7.6 V, 19 V and 34 V windings, each rated 5 A, corresponding to the tap transitions observable from the front panel.[440]

## Worst-case dissipation and tap boundaries

Because dissipation is set by the gap between the tap voltage and the output, the hottest operating point of a tapped linear supply is just *above* a tap transition, where the supply has selected a higher tap but is delivering only slightly more voltage than the tap below.[828][440] Testing therefore targets those boundaries rather than the extremes of the range. On the Atten, 24 V at 5 A was chosen precisely because it sits near the bottom of the highest tap, giving maximum drop across the pass transistor; dropping to 23 V moved the unit one tap down onto the high side of that tap and reduced the heat sink load.[440] The full test point was 24 V at 5 A plus 6 V at 3 A, about 138 W total.[440]

The other worst case is a short applied while the supply is set low, so the pass element drops nearly the whole tap voltage into a near-zero output.[828] Driving the SPD3303X this way with an electronic load in constant-resistance mode at 1 Ω made the supply oscillate between constant voltage and constant current and hunt across its tap boundaries at the same time, taking the power transistor to 100 °C — within margin, but not a condition to leave running indefinitely.[828]

Tap coverage also sets real current limits that specifications may not state. The Atten delivered 5 A at 20 V, where the relay had selected a lower tap, but could not do so at 30 V on the top tap.[439] Stepping from 5 V to 30 V under a 10 Ω load, a 90 W step, took the supply through two tap changes before it settled.[439]

Tap voltage is also a fixed constraint on modification. Extra current might be obtainable from an Agilent 6643A by changing a jumper, but the voltage range is determined by transformer tap ratios, and with no spare or alternative taps on the transformer the supply is tailored to the magnetics fitted.[667] Similarly, the thermal problems of the Rigol DP832's LM317 were not addressed by re-tapping: the transformer and its tap were left unchanged in the revised design, so the voltage reaching the regulator after the bridge rectifier stayed as it was.[549] Mains that sits high — 248 V is common in some locations, and over 245 V nominal most of the time — pushes that rectified rail higher still.[549] Out of the box the DP832 was set to its 230 V tap.[509]

## Auxiliary and multiple-output taps

Beyond the main power path, separate low-current taps commonly feed housekeeping rails so that logic and analogue supplies do not share the main rectifier. The Atten has a dedicated tap for the DAC/ADC board's ±15 V regulators and another for the front-panel logic board, each with its own bridge rectifier, filtering and on-board regulation.[440] The SPD3303X's third channel is fed from its own yellow-wire tap and its own discrete-diode bridge, which does not need to be heat-sunk because that channel's power output is lower.[828] An Onkyo receiver derives its negative VP rail from a separate tap measuring 39 V AC on a dedicated transformer tap board.[1394]

Taps also carry heavy current in non-supply equipment: the JBC CD-2BB soldering station routes its transformer taps through heavy via stitching and thick copper to handle the current of a roughly 150 W iron.[472]

## Other tapped configurations

A centre or extra tap is what converts a half-wave arrangement into a full-wave one. A Cockcroft-Walton multiplier can be made full-wave by mirroring and duplicating the ladder and taking the extra tap from the transformer exactly as a conventional linear supply does, which doubles the ripple frequency and reduces capacitor sag.[469]

In inverters, an H-bridge on each side of the transformer tap allows that side to be pulled to ground or driven high, so either side of the winding can be switched, alternated, or disconnected — the same topology used for motor drives.[1620]

Constant-voltage 100 V line audio systems use the same tapping idea on the speaker transformers rather than the source: individual 4-inch speakers tapped for half a watt or one watt allow roughly 300 units to be reticulated onto a single 150 W amplifier.[354]

## Taps in fault diagnosis

Because taps are the boundary between the mains side and the rectified rails, they are a natural probe point. Measuring AC on a tap distinguishes a dead transformer or open winding from a downstream fault: on one repair the tap was confirmed live once the mains relay was forced on, drawing 42 W, which localised the fault to the processor failing to recognise the powered-on state rather than to the supply.[378] Where a rail shows excess ripple, a failing tap is possible but ranks well below a degraded reservoir capacitor or an interconnect problem in likelihood; a 35-year-old 5300 µF capacitor going bad would produce a large amount of excess ripple, which is the more expected signature.[804] Tap wiring is also useful for orientation when reverse engineering an unfamiliar board, identifying which rails enter the secondary side and where the current shunts sit.[1423]

Taps are visible in teardowns as the incoming secondary wiring. An electrophoresis supply's primary tap is a six-wire bundle of three brown and three black wires arranged as three separate pairs, and its 250 V tap measured 258 V RMS with the output ramping — the tap voltage itself fixed and low-impedance, with the rising output being the DC produced by the downstream converter.[530] Poorly executed tap connections are a workmanship flag in their own right.[922]
