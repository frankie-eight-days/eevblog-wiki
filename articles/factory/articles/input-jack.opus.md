# input jack

An input jack is the front-panel banana socket through which a multimeter, LCR meter or other bench instrument receives its test leads. A typical handheld multimeter carries four of them — ground, 10 amp, milliamp/microamp, and volts/ohms/diode — each fed by a completely separate input protection circuit.[373] Because the jack is the first metal in the signal path and the last mechanical part a user touches, its construction is one of the most reliable single indicators of whether an instrument was engineered or merely assembled: cheap meters give themselves away at the jacks before anything on the board is visible.[75]

## Solid tube versus split jack

The central distinction is between a solid metal tube and a split jack. A solid tube is a full cylindrical barrel that grips the probe evenly around its circumference; a split jack has a slot cut down one side so the two halves act as a spring contact.[99] Solid tubes are the preferred construction, and the split type is treated as a defect to be tolerated rather than a design choice.[417][634] On analog classics such as the Triplett 630-NA the split jacks — press-fitted into the plastic surround rather than mechanically fastened — are the one part of the instrument that fails to impress.[634] A meter whose jacks are all split reads as a slapped-together design.[712]

The worst grade is stamped rather than tubular. In cheap meters the jacks are a bit of stamped metal that does not fit the plastic surround properly and lifts straight out of the front panel.[75] Stamped and folded jacks are simply expected at the bottom of the market.[1580] Even where stamped construction is acceptable, the jacks can sit visibly off-centre in their shrouds, relying on the shroud of the probe to self-centre them on insertion.[99]

Good construction is unambiguous in appearance: solid input tubes folded over and screwed down on top with a star washer and a self-locking nut,[99] or solid metal posts with shake-proof washers screwed directly into the PCB.[372] A generational upgrade from split stamped jacks to solid screw-in jacks is a substantial improvement in a meter's front end.[1378]

## Mechanical retention and board attachment

How the jack reaches the PCB matters as much as the barrel itself. Several distinct approaches appear across instruments:

- Solid metal posts screwed directly into the main PCB, with the fuse board on a vertical riser soldered to it.[372]
- A single solid piece with an integrated lead fed through a slot in the board and hand-soldered, the slot itself providing the rigid mechanical constraint.[173]
- Folded metal passed through the board, bent back up on the underside, and soldered at both points.[115]
- A dedicated secondary board carrying the jacks, connected to the main board by headers or by brass standoffs running top to bottom.[99][171]
- Solid metal threaded inserts moulded into the case body.[417]

Where jacks are held only by a shake-proof washer, the assembly can work loose in service.[1576] Jacks pressed into place with high-quality contact surfaces can also be effectively unserviceable — in some precision instruments they are not realistically replaceable and are best left undisturbed.[461]

## Split jacks and the input alert

Splitting a jack is not always a cost measure. Split contacts are two-sided by design, and the two halves are used to detect whether a probe is actually inserted — the basis of the input alert feature that warns when a lead has been plugged into the wrong terminal.[171][99] Detection is only needed on the current terminals, so the volts jack halves are joined together while the amps jacks are kept separate and tapped off to a sensor.[171]

The mechanical cost is real. Because the split halves must flex, the current jacks are noticeably softer than the volts and ground terminals, which are full metal tubes; probes sit almost loose and jiggly in them, and the plastic inserts in the amps jacks can come out entirely.[99] The alternative is optical detection: a sensor shines through a clear housing on the terminal jack, so a fully sealed solid jack can still support input alert.[64][99]

## Sealing and water ingress

Waterproofing is achieved by moulding the jacks fully into the front panel so no water enters through them at all,[99] or by fitting an O-ring seal around each jack.[171] The absence of O-ring or rubber sealing around the jacks, alongside a smaller current shunt and a lighter fuse, is a recognisable cost saving.[344] Where the whole jack assembly is embedded in one large plastic moulding, the instrument is waterproof through the terminals and the opto sensing has to pass through the clear housing instead.[64]

Water that does reach the jacks produces a characteristic symptom rather than a failure: the meter reads amps error, or beeps continuously, because the wetted contacts make it think a probe is plugged in.[868][66] The condition can persist for hours after immersion and survive both blowing out the jacks and banging the meter on the bench, while the measurement accuracy itself stays bang on.[868]

## Circuitry immediately behind the jack

The jack is the entry point to the protection network. On a volts input the jack feeds a string of five series resistors, used in series specifically to obtain a high withstanding voltage more cheaply than a single high-voltage part.[853] Other front ends run the jack into a 1 meg high-voltage ceramic resistor and then into a bank of MOVs, with a tap off to the range switch,[373] or through a fusible resistor, a high-voltage resistor, a PTC and three MOVs.[1592] In a low-impedance mode the positive input jack is routed through a 1k resistor into a physically large PTC, chosen for its greater heat dissipation.[1667] On the amps side the jack feeds a current shunt resistor and its fuse, an entirely separate path from the volts circuitry.[373]

Thermocouple front ends impose a placement constraint on the jack itself: cold junction compensation needs the temperature sensor to see the temperature of the dissimilar metals at the terminals, so the layout note reads "place near the inputs".[853] Better implementations physically couple the sensor chip through to the metal of the input jacks; cheaper ones merely place it physically close, which is still preferable to siting it halfway up the meter.[853]

## Ratings, arrangement and count

The CAT rating marked at the jacks is not always the rating the instrument holds — jacks printed with CAT 1000 volts on a meter that is in fact CAT II 600 volt rated are a known form of overstatement.[341] Terminal count and arrangement vary with function: four-wire resistance measurement adds two sense terminals alongside the basic volts/ohms/diode pair,[489] and bench instruments provide both front and rear terminal sets, front for traditional bench use and rear for system measurements.[489] Some bench multimeters carry both a 3 amp and a 10 amp input jack, the 3 amp retained for backward compatibility with an earlier model while the 10 amp is the recommended terminal for better accuracy.[489][485]

## Failure modes

The input jack is a common point of failure, and its failures are intermittent rather than absolute. A dodgy jack may not open-circuit outright: it can present a high but finite impedance that forms a voltage divider against the meter's own nominal 10 or 11 megohm input impedance, producing a reading that is wrong rather than absent.[1576] The usual cause is tarnishing or oxidisation on the contacts combined with looseness; tightening the jacks lets the probe pierce through the oxide layer and restores the reading.[1576]

Mechanical abuse produces the same signature. After a meter was run over by a car, the positive socket required the probe to be physically depressed before it would measure, and wiggling the probe made the reading jump around — with the solder joint, lock nut and star washer all sound, the fault had to be internal to the jack, most likely dirt and grit driven inside.[151] An unreliable input jack is a functional failure of the instrument even when everything downstream is within specification.[151][1576] Consequently, wiggling the leads at the jacks is a standard first check when a meter misbehaves, and ruling the jacks out redirects the diagnosis elsewhere.[FgkD8K0Ssdc]

Jacks also wear out with ordinary use, gradually losing grip on the probe over the life of an otherwise excellent instrument.[107]

## As a design and layout concern

Crowding around the jacks is a layout defect in its own right: a resistor touching an input jack, or input components bunched and pushed over, undermines an otherwise sound front end.[99] Well-executed designs route high-voltage isolation slots into the board near the terminals.[99] On schematics, the inputs belong on the left, and a multimeter schematic drawing the input jack on the right departs from best practice.[1704]

Retrofitting quality is not a practical option — improving the jacks and safety of a cheap DMM by hand is not worth attempting.[89] In original design work the jacks are often not specified at all but inherited from the contract manufacturer's standard part used across multiple designs.[e9cpKN69Avk] The distinction between good and bad jacks remains visible without instrumentation: "Not the crap split type" is a complete assessment.[417]
