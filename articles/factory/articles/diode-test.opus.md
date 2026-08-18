# diode test

The diode test is a multimeter function that drives a small current through a semiconductor junction and displays the resulting forward voltage drop, typically 0.5 to 0.6 volts for an ordinary silicon diode.[1636] Almost every meter on the market carries it, marked with a diode symbol on the range switch.[75] Its value in troubleshooting is that a junction can usually be judged good or bad in seconds, often without unsoldering it, which makes it one of the first checks in any dead-equipment diagnosis.[1460]

## What the reading means

The function reads the forward drop of a diode in circuit, and the same reading taken with the probes reversed distinguishes a working junction from a failed one.[1636][565] A dead short inside a semiconductor is a more likely fault than a short inside a capacitor, and diodes fail both open and short.[1388] A junction that reads identically in both directions is either shorted or is being read through some other path in the circuit.[565] Beyond plain diodes, the function reads transistor base-emitter junctions and zeners: a supposed 8.2 V zener reading a normal diode drop one way and its rated voltage the other confirms the part.[1087][1394]

Because the drop of a light emitting diode is also just a forward voltage, the same range lights LEDs and reads their drop, which is what makes it useful for checking indicator and display parts.[1636] A meter with enough headroom and current can light an LED dot matrix display through the probes; one such display measured a 1.8 volt drop, read as 1.85 volts.[960]

## Compliance voltage

The single specification that separates one meter's diode range from another's is the open circuit, or compliance, voltage — the maximum the meter can put across the junction.[75] A meter limited to 2 volts cannot test a modern white LED at all, and this limit is common on otherwise excellent instruments: the Fluke 27's diode range stops at 2 volts, and the Fluke 28 Series II likewise reads only to 2 volts, so a Cree XPG LED that measures 2.477 volts on a Fluke 87 barely comes on and gives no reading on the 28-2.[372][64] The Fluke 17B Max shows the same behaviour, the LED barely lighting and the reading over range, while a companion meter read 2.38 volts.[1692]

Compliance figures across the field span an order of magnitude. A Hioki clamp meter designed for electrical rather than electronics work manages only 1.5 volts from four AA cells, not enough to light even a red LED.[973] A GVDA pocket meter offers 2 volts.[MarjYxiudYE] The Ziboo 17B Pro reaches 2.1 volts from three AA cells, below the 2.3 volts a two-cell Fluke achieves.[1731] The Fluke 101 gives 2.43 volts from two AAA cells, enough to light a white LED dimly.[1574] The retro Fluke 37 gives 2.5 volts despite a 9 V battery.[1393] The Uni-T UT71E reaches 2.8 volts, marginal for a white LED.[712] A $25 meter reached 3.28 volts on fresh AA cells, though that figure falls as the batteries age.[1007] The Zotek ZT-702S manages 3.2 volts, comfortably turning on a white LED.[1540] The Gossen Metrawatt Xtra reaches roughly 8 volts.[46] The Agilent 34461A raised its predecessor's 1 volt maximum to 5 volts specifically to allow testing of modern LEDs, at the cost that the higher open circuit voltage may disturb junctions in existing automated test systems that did not expect it.[489]

Compliance voltage is a direct consequence of the battery topology. A 9 V battery supplies a high diode and ohms test voltage without a DC-DC converter; running from two AA cells forces a converter, with its own efficiency penalty and shortened battery life, as the only route to a higher diode test voltage.[97]

## High-voltage diode ranges

A 15 V diode range, as fitted to the 121GW, extends what the function can do.[121] The extra headroom is not only about reaching higher forward drops — it also delivers more current capability, which is what allows LED displays to be driven visibly.[960] It permits reverse breakdown measurement: a transistor's emitter-base breakdown, specified at 6 volts but highly variable in practice, measured 7.7 volts.[1087] It reads zeners directly rather than by inference.[1394] And it reaches parts that lower-compliance meters simply report as open, such as a pair of unusual diodes in a Fluke combiscope that read open on a normal meter but 10.7 volts on a 15 V range.[1452]

## Test current

Test current is not standardised and differs between meters even where compliance voltages match.[1084] A $25 meter delivered roughly 1.6 milliamps, sufficient to light an LED.[1007] The DT71 LCR tweezers supply 2 milliamps, enough to light an LED and particularly useful for lighting LEDs already populated on a board.[1335] A meter drawing 1.7 milliamps on DC volts drew 5 milliamps on the diode range.[64] A user-selectable test current for the diode range, aimed at LED testing, is a feature worth buying a meter for, and none on the market offers it.[46]

## In-circuit measurement

Diodes are among the easiest parts to check in place, and in most cases can be measured without removal.[1460] The trap is parallel circuitry. A rectifier diode with a 68 ohm bleed resistor in series with a coil across it presents well under 100 ohms in parallel with the junction regardless of probe polarity, so the meter reads that path rather than the diode.[1364] A reading of about 50 ohms in both directions invites the conclusion that the part is shorted, when in fact the surrounding network must be accounted for before the measurement means anything.[1364] Where the in-circuit reading is ambiguous, pulling the part settles it.[1388]

## Use in fault-finding

On equipment drawing excess current, the diode test is an early step: something is shorted or heavily loaded, and the rectifiers are prime suspects.[663][1364] Blown rectifier diodes are a classic culprit in switch-mode supplies.[1364] A standard sequence after a visual inspection for dry joints is to measure every diode on the board before moving to other component classes.[1452] A short found this way inside a semiconductor is the more probable failure than one inside a capacitor.[1388]

## Implementation differences

Meters vary in how the function is presented as well as in its specification. Some give no audible or visual indication that a good junction has been found, and no indication of probe polarity, so the operator must track which lead is which.[1731][1649] The Agilent U1272A adds an automatic diode mode that displays a good or bad verdict alongside the voltage, using thresholds of 0.3 volts and 0.8 volts, and reports a reversed junction as a negative reading rather than refusing it.[249] The Smart Tweezers LCR meter shows a diode symbol on its display and flags a short across the probes.[81] On the Agilent U1253A the continuity beeper also sounds on the diode range, and responds about twice as fast there as on the ohms range.[56]

Implementation can also simply be broken: one meter in a $50 shootout could not measure a standard silicon diode at all on its diode range.[91] On another, the diode reading in circuit failed where a bare junction measured 0.4 volts.[1649] A meter with a poorly designed range switch flickers between the ohms and diode positions, a symptom that points at dirty or worn switch contacts rather than at the measurement circuitry.[IoRks5bJw8Y]

## Safety

Meter manuals prohibit connecting the test leads across a voltage source while the function switch is in the capacitance, resistance or diode position, on the grounds that doing so can damage the meter.[94] The countervailing engineering position is that a meter which cannot survive 240 V mains applied to those ranges should not be on the market, particularly a single-switch instrument whose own marketing shows people probing mains.[94] Robust meters do survive it: applying 240 volts to a Fluke 117 makes the diode and capacitance range misbehave visibly while the meter itself comes through undamaged, and other meters recover fully after the same treatment.[60][99]

## Beyond the handheld multimeter

The function is not confined to bench and field multimeters. It appears on LCR tweezers, where the small probe spacing suits surface mount parts.[81][1335] It appears on scopemeters and combined scope-meter instruments.[430][1540][1723] It appears on bench system multimeters alongside thermocouple and continuity functions.[478] It is fitted to clamp meters intended for industrial electrical work, where its usefulness is questionable given that little on a large site presents a junction worth testing.[3kdYGneg9xI][973] Even a wrist-worn meter carries the symbol on its case, in that instance for a function the meter cannot actually perform.[1706]
