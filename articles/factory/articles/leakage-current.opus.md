# leakage current

Leakage current is the small unwanted current that flows through a component or along an insulating path that is nominally blocking — a reverse-biased diode, an off MOSFET, a capacitor dielectric, or the surface of a printed circuit board between two adjacent pins.[1747][1736][33][485] It is never zero, and whether it matters depends entirely on what it is being compared against: a few microamps is negligible next to an amp, and fatal next to a picoamp.[286][1747] Most of the design effort spent on leakage is therefore not about eliminating it but about pushing it an order of magnitude or more below the smallest current the circuit is meant to resolve.[286]

## Reverse leakage in diodes

A reverse-biased diode passes a non-zero reverse current, and that current rises with applied reverse voltage rather than staying flat.[1747] Schottky diodes are markedly worse than PN junctions in this respect: the extra metal layer of the Schottky barrier construction buys a low forward drop at the cost of roughly three orders of magnitude more reverse leakage than an ordinary jellybean PN junction part.[1747] A representative small-signal Schottky measured 2.4 µA of reverse current at 5 V, while the equivalent PN junction device sits in the nanoamp region under the same conditions.[1747] A 1N4148 leaks on the order of tens of nanoamps.[1242]

This makes the choice application-dependent rather than absolute. A Schottky is the right part for reverse-polarity or reverse-clamp protection, where the low forward drop is the point and the leakage is irrelevant, because a PN junction's 0.6 V drop can be enough to forward-bias junctions in the circuit being protected.[1747] It is the wrong part wherever the blocked node is high impedance.[1747]

## How leakage becomes a visible error

The classic symptom is a voltage that should not be there. A reverse-biased diode feeding a node loaded only by a multimeter's 10 MΩ input forms a divider: 10 nA of leakage across 10 MΩ produces 0.1 V, which is why such a measurement reads close to zero rather than exactly zero.[1747] With microamps of Schottky leakage instead of nanoamps, the same arrangement can read the full rail voltage on a node whose supply is disconnected, and the effect is entirely the leakage combined with the meter's internal resistance rather than a fault.[1747] Bench multimeters with gigaohm input impedance on their lower ranges make the problem worse, not better, because they load the leaking node even less.[1747]

The same mechanism appears in precision analog circuits. In a peak detector, when the output drops low the storage diode is reverse biased into what is effectively a path to ground, and its leakage can exceed the input bias current of a FET-input op amp — the diode, not the amplifier, sets the droop.[490] The standard fix is a two-diode arrangement that feeds the peak output back so that the voltage across the offending diode becomes zero; with zero volts across it there is no leakage current through it at all.[490]

In a battery gauge built around an LM3914, the leakage current of the voltage reference itself has to be carried explicitly as an error term in the resistor calculation, and the value comes from the data sheet — 120 µA maximum from the adjust terminal.[204]

## Guarding and PCB construction

Where currents of interest fall below the microamp level, the dominant leakage path is the board itself, and the countermeasure is guarding: a trace or ring held at the same potential as the sensitive node, placed so that it surrounds and intercepts every path leading away from it.[1755] Because there is no voltage differential between the node and the guard, Ohm's law leaves no current to flow — the leakage that does exist flows from the guard driver rather than from the measurement node.[1755] Guard rings appear routinely around individual pins of analog multiplexers and high-impedance amplifier inputs in precision instruments.[485][1334][607][1382] Supporting details include vias arranged to block cross-contamination through the board, guard traces routed underneath the sensitive resistors and capacitors, and solder mask deliberately removed around the guarded pins.[1755][1334] Isolation slots are cut under the FET switches that reset the integrating capacitors of a multi-slope converter, where any leakage would corrupt the charge and discharge timing the conversion depends on.[731]

At the connector, the same idea becomes the three-terminal triaxial cable: chassis or mains earth on the outside, a driven guard terminal inside it, and the signal at the centre, which eliminates leakage and interference paths into an electrometer front end.[1476][607] Instruments resolving down to 10 fA require this construction rather than ordinary coax.[607] Guarding, shielding, and wiring layout account for much of the internal complexity of classic high-resistance instruments, where measuring megohm, gigohm, and teraohm resistors was otherwise not practical.[1476]

Exposed traces with solder mask stripped away are not always a leakage measure, and the interpretation depends on where they sit in the circuit.[559]

## Leakage as a device parameter

Leakage is a specified characteristic across component families and is frequently the axis on which two otherwise similar parts differ:

- **MOSFETs** — drain-to-source leakage in a small jellybean part runs to a maximum of about 1 µA.[1736]
- **Logic families** — the 4000 series has better leakage behaviour than 74HC-class parts, which trade it away for lower on-resistance and higher bandwidth.[1611]
- **Tantalum capacitors** — very low leakage is one of their genuine advantages, alongside good reliability when operated inside their specifications.[33]
- **ESD protection networks** — leakage is a first-order design consideration when series resistors, avalanche diodes, and capacitors are added ahead of instrumentation amplifier inputs.[1619]

Diode curves showing leakage current alongside temperature stability and the breakdown region are standard textbook material for characterising the device.[1270]

## Mains-frequency and high-voltage leakage

At mains potentials, leakage is a safety and power-measurement issue rather than a precision one. A soldering iron whose start button measured 85 V AC to protective earth, accompanied by a tingling sensation when the knob was held, points to leakage through a filter capacitor.[1291] Distributed capacitance is enough to draw measurable current with no load connected at all: 283 double adapters chained in series drew 229 µA at 241.3 V in, amounting to 54 mW of leakage from the capacitance alone.[1526]

Input protection components can also leak in a way that degrades a meter's own specification. A multimeter using three MOVs in series across its 10 MΩ input has a leakage path through the varistors that, from the data sheet, was predicted to pull the effective input impedance down to about 9.5 MΩ and raise the current to roughly 105 µA at 1000 V.[rT0g1QmKE5E] Measurement showed better than predicted behaviour — the input stayed at effectively 10 MΩ, measured as 10.02 MΩ, all the way to 1200 V, so the MOV selection leaves leakage a non-issue across the meter's full range.[rT0g1QmKE5E]

Leakage is also used deliberately. Displays driven from high-voltage rails can pre-bias unselected outputs through discrete diodes to a chosen supply, preventing digits from faintly glowing on leakage currents alone.[950] Measuring that leakage directly on a Nixie tube — all unselected pins shorted together and clamped by a 30 V Zener, against 1.6 mA flowing in the selected segment through a 22 kΩ resistor — gave about 330 µA total, low enough not to disturb operation.[950] In alkaline battery discharge testing, a 100 kΩ resistor placed in parallel with each cell supplies a deliberate 10 µA to emulate the leakage current a real product would impose.[hSkaZEgrZkY]

## Measuring it

Very small leakage currents are often better expressed as conductance than resistance. Multimeters with a nanosiemens range, reached on some models by pressing the range button twice while on ohms, read high-resistance leakage paths directly; converting back to ohms requires inverting the reading.[372][1728] Conductance in siemens is the conventional unit for the very high resistances found in dielectrics and PCB materials, and in materials science generally.[1728]

Isolating a leaking node also matters when storing charge. A supercapacitor or battery backing a low-power circuit must be separated from the main supply rail by a blocking diode so that no reverse current flows back into the powered-down circuitry, and the diode's own leakage — tens of nanoamps for a 1N4148 — sets the floor on how well that isolation works.[1242]

Leakage is not confined to conduction through components. In an electrostatic system where the attractive force is electrostatic and no conduction current is intended in theory, leakage and capacitive charging currents are still present in practice.[1149] Keeping noise and leakage out of the analog section is a general construction requirement in precision resistance standards and calibrators, alongside the type and construction of the reference resistors themselves.[544]
