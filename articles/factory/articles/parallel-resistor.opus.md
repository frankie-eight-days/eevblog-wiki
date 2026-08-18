# parallel resistor

A parallel resistor is a resistor connected across another resistor so that both share the same two nodes, producing a combined resistance lower than either one alone.[1399] The configuration is fundamental enough that voltage divider and loading calculations cannot be done without it, since any real divider has a load across its lower leg and no source is ever truly unloaded.[1399] In practice it serves two distinct purposes: arriving at a resistance value that no preferred series offers, and spreading current or power across several parts.[1399][661]

## Formulas

For resistors in parallel the total resistance is the reciprocal of the sum of reciprocals: 1/(1/R1 + 1/R2 + 1/R3 ...).[1399] For the two-resistor case there is a shortcut, R1 × R2 / (R1 + R2), which many prefer.[1399] Series combination is the trivial case by comparison, being simply R1 + R2 + R3.[1399] The convention for indicating a parallel combination in written work is a pair of parallel lines, usually drawn sloping, and the operator appears on some calculators.[1399]

The current divider formula is restricted in a way the resistance formula is not: it applies only to the two-resistor case and cannot be extended by summing terms. Dividing current among three or more parallel resistors requires Kirchhoff's current law.[1399]

## Rules of thumb for trimming

Because putting anything in parallel can only lower a resistance, trimming with a parallel part is a one-directional operation.[1399] To reduce a value by roughly 10%, put a resistor ten times larger across it — a 100K across a 10K.[1399] The same scaling holds down the decades: 1% needs a hundred times the value, 0.1% a thousand times.[1399] To halve a resistance, use two equal values in parallel; to divide by three, use three equal values.[1399] The inverse operation, raising a value, is done in series with one-tenth of the value for a 10% increase.[1399]

The reason this matters is that E12, E24, E48 and E96 preferred ranges rarely contain the number a design actually calls for.[1399] A 555 timer's internal divider is nominally three 5K resistors, but 5K is not a preferred value; two 10K resistors in parallel produce it.[555] An LM3914 battery gauge design needing 10.909K for its lower divider leg obtained that value exactly from a 12K and a 120K in parallel.[204] Two resistors in parallel on an unknown board are themselves a diagnostic clue, being the usual signature of a trimmed window comparator threshold or similar exact-value requirement.[966]

Trimming is also applied to shunts. In one multimeter's milliamp range the shunt is a 1 ohm resistor plus a 10 milliohm element in series with it, and a 1K resistor sits in parallel with the 1 ohm to pull the combination down toward the 0.99 ohms the design actually needs.[853] Laser-trimmed thin film networks use the same principle internally: a ladder structure amounts to many small resistances stacked in parallel, providing coarse and medium trim values that can be cut open to move the total.[730]

## Sharing current and power

Paralleling identical resistors is a cheap way to get a low-value, high-dissipation element from ordinary parts. A constant-current load built from ten 1 ohm resistors in parallel yields 100 milliohms, and this is standard practice for sense resistors of that order.[661] A fast NiMH charger uses roughly six 1 ohm resistors in parallel per cell holder — three on each side — with the voltage sense tapped off them.[811] Elsewhere on the same charger, two 6R2 resistors in parallel sit under a SOT-23 MOSFET forming a discharge path back to ground.[812]

The technique extends to precision instruments: a battery emulator's current sense element is two 10 ohm Dale resistors in parallel, specified at only 1% tolerance because the value is calibrated out later, but chosen for very low temperature coefficient.[1550] Sense resistors of this class are expensive individually, on the order of a few dollars apiece for a 10 milliohm shunt.[1550]

Paralleling is also used purely for the resistance an RF design needs. A 50 ohm microstrip on standard FR4, 5 mm wide over roughly 1.6 mm of dielectric, was terminated in two 100 ohm resistors in parallel to make the 50 ohms.[1085] Not every parallel pair is there for its resistance at all — two large 150 ohm resistors on an isolated board cutout, which would give 75 ohms if paralleled, are sized as heaters forming a small oven for temperature-controlled circuitry.[823] Repair work leans on the same freedom: a 2K2 high-wattage resistor that had fallen out of a studio monitor was replaced with three 6K8 resistors mounted in parallel on the back of the board.[1072]

## Tolerance averaging and its limits

Series and parallel combinations behave differently with respect to tolerance. Ten 1% resistors in series retain the tolerance of a single resistor, but ten 10K resistors in parallel should in principle give a 1K resistor better than 1%, because the individual errors average out.[215] This holds only if the manufacturing distribution is a true Gaussian centred on the nominal value.[215] It frequently is not. A measured population of nominally 1K, 1% resistors sat well inside tolerance but with a mean displaced about 0.35% low, so paralleling ten of them averages toward that shifted mean rather than toward 1K.[216] Averaging by parallelling therefore improves random spread, not systematic offset.[215][216]

## Failure modes and loading effects

A parallel trim is a soft failure and a series combination is a hard one, which has consequences for how a fault presents. If two resistors are paralleled to tweak a value and the higher-value one loses contact — a real risk on breadboards where glue residue on a lead prevents contact — the remaining lower-value resistor is only slightly out of specification and the fault is easy to miss.[204] Putting resistors in series instead produces a gross, obvious failure when one connection is bad.[204]

Because a parallel resistor loads whatever it is placed across, it also functions as a deliberate test tool. A meter's 10 megohm input impedance is high enough to pick up ambient noise, and putting a 1K resistor in parallel with it collapses that susceptibility; measuring a genuinely low-impedance source such as a battery, whose source impedance is in the milliohms, has the same effect and leaves noise confined to a couple of least significant digits.[1379] A counter-surveillance monitor that would not detect its own probe was forced to detect it by connecting a load of around 100 to 190 ohms in parallel with the probe.[966] A misbehaving LED that could not be lit by any physical means came on when a second 1K resistor was placed in parallel with the existing 1K.[1087]

## Related applications

The parallel-resistance relationship governs quantities other than resistance. Electrolytic capacitors placed in parallel combine their ESR exactly as parallel resistors combine, so two capacitors of 0.2 ohm ESR in parallel present 0.1 ohms, and the standard parallel resistor formula is the one to use.[742] This is why several smaller, higher-ESR capacitors can substitute for one large low-ESR part.[742]

Recognising parallel pairs is also the main tool for reducing symmetric resistor networks by inspection. In the resistor cube problem, symmetry allows nodes to be shorted together, after which pairs of resistors become parallel and can be redrawn as R/2 while the remaining branches stay at R, collapsing the network to something solvable by series and parallel arithmetic alone.[1472]
