# current shunt

A current shunt is a low-value resistor placed in series with a current path so that the current can be inferred from the voltage developed across it, by Ohm's law.[1533] It is the dominant method of current measurement in bench and handheld instruments: a multimeter switched to amps is essentially nothing more than a current shunt connected from the input jack to ground.[731] Because the shunt sits in the circuit under test, every design decision about it is a trade between measurement resolution, the voltage it steals from the load, and the power it has to dissipate.

## Construction

The classic shunt in a handheld meter is not a packaged resistor at all but a length of resistance wire, usually nichrome, formed into a loop or a zigzag and soldered directly to the board.[344][931] The wavy or zigzag pattern sets the resistance by path length.[634] Wire-wound-on-former construction also appears, with nichrome wound around a ceramic core.[1189] Because a formed-wire shunt is a large, low-resistance piece of metal, it is effectively a short circuit that will never blow, which is why it is not the fusing element in an amps path.[931]

Solder joints on these shunts habitually look poor. The characteristic dull, lumpy fillet where nichrome wire meets the board is normal for the material rather than evidence of a bad joint, and can appear on instruments whose soldering is otherwise first class.[344]

Shunt quality is one of the fastest visual reads on a meter's class. Cheap instruments use a bent bit of copper wire; better ones still use a bent bit of wire, but a large, substantial, shiny one.[75] Notably wimpy 10 A shunts turn up in low-cost meters,[853][1096] and comparisons between meters at different price points often come down to one having a physically beefier shunt with more capacity than the other.[1447] Surface-mount shunt resistors are used where the currents are modest, in instrument front ends,[875] soldering stations,[1106] and LED driver boards where 0.1 Ω parts sense each string.[1460] Some designs abandon formed wire entirely for packaged precision parts, which is unusual enough to be conspicuous against the expected nichrome loop.[1382]

## Four-terminal connection

At milliohm values, the resistance of the connecting tracks and solder joints is a significant fraction of the shunt itself, so precision shunts are sensed with separate voltage-sense connections tapped onto the shunt body — a four-terminal, or Kelvin, arrangement.[373] Well-made examples include tapped 10 A shunts with dual sense terminals,[373] four-wire 0.1 Ω 0.1% parts in bench instruments,[658] and four-terminal shunts from established resistor makers mounted on the underside of the board.[485] On hand-formed shunts the sense wire is tapped off at a precisely chosen point along the wire and trimmed to trim the effective value.[634][775]

The benefit is easily thrown away in layout. Running a large copper pour and heavy via stitching between the high-current side and the sense side of a four-terminal shunt largely defeats the purpose of having one.[731]

## Burden voltage

Any shunt in the current path develops a voltage drop, and that drop is subtracted from the supply reaching the device under test.[1533] The magnitude depends on which range is selected, because each range switches in a different shunt value.[1533] A 10 mΩ shunt on a 5 A range gives 50 mV full scale; the same shunt used for a 50 mA range gives only 500 µV full scale, which is why low ranges conventionally use much larger shunt values and therefore incur much larger burden voltages.[929] In practice the high-current range has very low burden voltage, and switching down to the milliamp range for better resolution costs a substantially higher drop.[957] This is the central difficulty in measuring the current consumption of a product from a fixed supply voltage: the shunt drop means the device is not actually seeing the voltage the supply is set to.[1533]

## Ranging and switching

Multi-range instruments switch between shunt values, sometimes with relays and sometimes with MOSFETs — for instance a 10 mΩ shunt for the 10 A range and a 500 mΩ shunt for the milliamp range, selected by paralleled MOSFETs.[1761] An alternative is to short out part of a shunt chain with a MOSFET rather than switch between separate resistors; this puts the MOSFET's on-resistance in series with the sense resistor, an error that can be removed in software but which a cleaner topology would avoid.[1331] Simpler meters dispense with switching altogether and use a single fixed shunt.[417] Panel meters are frequently sold with no internal shunt at all, a 100 µA or similar full-scale movement or input being scaled to amps by an external shunt chosen by the user.[769][9lIC3ZzIht4]

## Power dissipation

Above a few amps the limit is thermal. Where a single part cannot handle the dissipation, shunts are paralleled: four in parallel for the main input shunt of an electronic load,[862] three in parallel in a 50 A supply.[1298] In an electronic load the shunt is bolted to the same heat sink as the pass transistors, and the airflow has to remove the shunt's dissipation as well as the load's.[862] The same design at lower current rating uses a different shunt with roughly half the power capability.[1298] Paralleling is also used to hit an awkward value: ten 10 Ω resistors in parallel give a 1 Ω shunt, which over a 2 A output range with a 10-bit converter works out to 2 mA per step, or 4 mA per step if only 8 bits are available.[259]

## Accuracy, tempco and calibration

Shunt accuracy sets instrument accuracy. In a high-precision instrument specified at 0.05% class voltage and 0.1% class current, the main input shunts are expected to be a very low tempco alloy, either trimmed to value physically or characterised and corrected in software.[281] Similar reasoning governs meter front ends, where the shunt's temperature coefficient is the dominant concern and the value itself is calibrated out.[1592] When the shunt is off value or inconsistent between batches, the error shows up directly in the reading — a batch problem in a 10 mΩ shunt accounting for a 0.23% error where the rest of the signal chain was good to 0.01%.[1328] Precision shunts are themselves calibration artifacts, forming part of the equipment set in an automated calibration rack.[422] At the utility scale, shunt error is one plausible source of small residual energy readings, on the order of a couple of hundred watt-hours, in revenue metering.[lndRXed2ylk]

## Where shunts appear

Bench power supplies use an output current shunt in the main power path between the power board and the output binding posts, for current readback and current limiting.[30][314][755] The same is true of the small DC-DC converter modules sold as cheap adjustable supplies, some of which carry dual shunts.[1030][1375] Electronic loads use large shunts on the input side.[281][862] Power analysers use internal shunts on each channel, with provision to program in an external shunt where the internal one is unsuitable, though the internal ones are the recommended configuration.[589] Soldering stations,[OvGdE5hC1Ro][472] computer motherboards,[882] and telecoms line cards[1177] all use them for local current monitoring.

Instruments themselves are often built for shunt access during service. Rail-to-rail links on a board, labelled with the rail voltage, can double as current measurement points, letting a technician cut the link and measure the current on that particular rail during troubleshooting.[208]

Shunts also make a good diagnostic target. A production test failure confined to the amps range, with all other ranges passing, points at the current shunt, since a passing volts range proves the amplifiers, gains and supply generation are all working.[588]

Not everything that looks like a shunt is one. Large low-resistance-looking parts can turn out to be jumper links added purely to raise current-carrying capacity where the copper on the PCB is inadequate — cheaper than specifying 12 oz copper.[1610] Similar parts measured too high in value to be shunts turn out to be something else entirely.[1639]

## Layout and safety

Because the amps path carries the full input current to the common jack, layout around the shunt matters. A screw hole placed in the middle of a 10 A trace, leaving very little copper on either side, is a construction defect regardless of what the shunt itself is.[712] Good front ends put high-voltage isolation slots around the shunt and the input jacks and route the current path cleanly.[432][1592] The shunt sits downstream of the high rupture capacity fuse in a properly designed amps path,[853] and in practice the 10 A shunt is not the part that fails — something else blows first.[1447]

## Alternatives

The shunt's defining drawback is that it must be inserted into the circuit. Where that is impractical, current transformers or clamp probes are used instead. Revenue meters use current transformers rather than a traditional shunt on each phase, a choice driven by the IEC 62053-21 standard and its relatives.[409] Hall-effect clamp probes measure current by clamping over a wire without breaking into the circuit, avoiding the need to install a shunt or cut traces, though they cannot be clamped over a PCB track.[1413][812]

The difficulty is sharpest with mains current. Measuring the mains consumption of a product with a shunt means getting inside the power supply, fitting the shunt, and reading it with an isolated high-voltage amplifier; a clamp probe simply goes around the active conductor.[1368] Ordinary oscilloscope probes across a shunt bring grounding problems, and differential probes, designed for high voltages, are poorly suited to the small voltages a shunt produces.[1368]

## Designing for measurement

Where current consumption is a design parameter, the shunt is best planned in rather than retrofitted. Evaluation boards built to compare candidate microcontrollers can be laid out with dedicated current-consumption shunts and jumpers so that in-circuit consumption can be measured directly on each part.[1539] The same thinking applies to test fixtures, where a small current sense shunt lets the fixture read the test current drawn as each board under test is switched on and compare it against an expected figure.[552] Multi-output products require a shunt per output to measure delivered power rather than input power; measuring only on the input side gives total consumption including converter losses, which can be approximated by subtracting a nominal efficiency figure in software.[1137]

Polarity and connection order matter in use. A shunt inserted the wrong way round simply produces negative readings, and the sense terminals must be taken from the shunt itself rather than from further along the wiring.[1693]
