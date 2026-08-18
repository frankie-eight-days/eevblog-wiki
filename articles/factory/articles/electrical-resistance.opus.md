# electrical resistance

Electrical resistance is the property of any material or component to oppose the flow of electrons from one point to another.[27aG9xhfk6s] It is the quantity that turns a voltage difference into a finite current rather than an unbounded one: a wire of zero ohms would offer no opposition at all, and a battery connected across it would be drained almost instantaneously.[27aG9xhfk6s] Where current does flow against resistance, the energy is dissipated as heat — the mechanism by which a toaster element toasts bread.[1439]

In practice resistance is rarely a design parameter in isolation. It is the thing measured to decide whether a contact is good, whether a trace can carry the current, whether a supposed short is real, and whether a product claim is physically possible.

## Measurement

The direct method is a multimeter across the two points of interest, and for most bench questions that is sufficient: 4 megohms between the input and the output ground of a high-voltage differential probe, consistent on both inputs and unchanged when the connections are swapped, establishes that the path is a genuine resistance rather than active circuitry.[932] Confirming the same 4 megohms with a source capable of 500 V rules out any voltage dependence in the reading.[932]

For low values the meter's own leads and the resistance of the connection dominate, and the accurate approach is to force a known current and measure the resulting voltage drop, then apply Ohm's law.[543] This is the technique used to characterise a single PCB pad: hold the current constant, measure the voltage across the pad without disturbing the solder joint, and repeat over a range of currents from 0.1 A up to 2 A to build a curve.[543] The effectively infinite input impedance of the multimeter means the voltage measurement itself does not perturb the result.[543] Milliohm-scale work on copper strip uses the same method — just over 1 amp of constant current through bare 1 ounce copper produced 52.86 mV, read directly as 52.86 milliohms.[319] An LCR meter with its leads nulled out is the alternative for milliohm measurements on assembled hardware.[1526]

Two measurement errors recur. Gripping both probes while measuring puts the body across the terminals: a reported 2 megohms between two exposed contacts was the person's own hand resistance, and the correct reading was an open circuit.[135] And a continuity function that latches will hold a reading such as 1.7 k that is not a real resistance value at all but an artifact of the meter's own behaviour, reproduced as 1.8 k on a second instrument of the same design.[1671] Resolution matters as well; a resistance display offering a single digit of resolution is of little use for anything beyond a go/no-go check.[1238]

## Conductors, traces and tinning

The resistance of a PCB trace can be reduced substantially by tinning it with solder. Controlled measurements on Vero board strip, referenced against a confirmed 1 ounce bare copper baseline, put the improvement from 60/40 leaded solder anywhere from a 15% decrease for a very thin coat to a 50% decrease — effectively a halving of the trace resistance — for a thickness comparable to what accumulates during wave soldering.[317] Lead-free solder behaves similarly: a 99.3% tin, 0.7% copper alloy applied as a thin layer brought a 52.86 milliohm baseline down to around 46 milliohms, a 13% decrease against the 15% obtained with leaded solder at equivalent thickness.[319] The two alloys land in the same ballpark, with thickness rather than composition as the dominant variable.[319]

The effect is reversible. Wicking the solder back off the strip returned it to roughly 52 milliohms, close enough to baseline to confirm that the change is due to the added conductor cross-section and not to some alteration of the copper — though physically scraping along the strip risks removing or leaching a little copper and introducing error.[317] Since removing solder mask lets the wave soldering process do the tinning at no additional cost, the technique is close to free.[317]

Conductive inks and paints occupy a different regime entirely and are never shorts. Carbon ink on a membrane keypad measures a couple of hundred ohms across a track.[505] A carbon layer laid down on a single-sided board to route around traces gives 47 and 44 ohms on adjacent runs — not a controlled value, but low enough for its purpose.[1108] Silver paint applied to worn keypad contacts read 15 ohms on one pad and around 4 ohms on another, sufficient for a microcontroller to register the press; the resistance falls as the carrier evaporates, one pad dropping from 12 ohms to 6 ohms with additional drying time and thinner deposits reaching one or two ohms.[1702] Fifteen ohms in that application is, in Dave Jones's phrasing, "good enough for Australia".[1702] Printed conductive traces on paper suffer from the substrate's porosity; a single printed layer gives a working pad of 7.6 ohms but may break elsewhere in the loop, whereas roughly ten layers on paper approaches conductivity comparable to copper.[1244][614]

## Sheet resistance

For a uniform film, sheet resistance is a constant of the material and its thickness, expressed in ohms per square, and it does not change with geometry.[732] An arbitrarily shaped region — however many cuts are made in it — has the same ohms-per-square figure; what the shape alters is the end-to-end electrical resistance for the particular practical purpose at hand, obtained by counting squares.[732]

## Contacts and connectors

Contact resistance is usually the dominant term in a connector assembly. A mains double adapter measured 9.5 milliohms total, covering both internal wires and all the contacts in each section, with most of that residing in the press-fit plug contacts rather than the conductors — those contacts are held by modest force and are exposed to corrosion and contamination.[1526] An LCR probe pushed into a single socket with significant force read 8.7 milliohms, doubling to about 20 for the pair, consistent with the total.[1526] At a 2 kW load this amounts to roughly 1 W of loss per adapter.[1526] Construction choices matter here: internal wiring with crimped terminations is expected to yield higher resistance per unit than a solid brass strip moulded into the plastic, despite the wiring being more expensive to assemble.[1526]

The same effect appears on the bench as voltage drop. A supply set to 1 V delivering 5 A showed 0.6 V lost in the connecting leads and terminals — a drop invisible at low current and unmissable at high.[gqzZHbEfWDU] Crosspoint switches in a solderless breadboard product contribute 85 ohms in the signal path, enough to disturb a circuit under test and disqualifying the instrument from precision work.[1608]

Resistance is equally a diagnostic for contacts that should be open or should be intact. An 18 megohm reading on a printer contact confirms something is connected to the pin rather than nothing at all.[p5-p8Iu7E1c] Anti-static bench mats measure in the gigohm range — tens of gigohms in some cases — which is why they do not affect a circuit resting on them outside of extraordinarily critical work.[250]

## Temperature dependence

Ordinary conductors and heating elements have different resistance values in the cold and hot states.[1186] This is not a subtlety confined to heaters. A 3.3 V rail measuring 0.11 ohms with a multimeter — at the milliamp test current the meter uses — drew 11 A rather than the ~30 A that figure would predict, because the shorted path heats up and its resistance rises with it.[401][405] A short with a temperature coefficient behaving this way is common and expected, and the low-current bench measurement should not be assumed to hold at operating current.[401] The rail in question was not supposed to be 0.1 ohms at all; the correct value was an order of magnitude greater.[401]

## Load and source resistance

In DC power analysis, plotting power dissipated in a load resistance against the value of that load resistance — with source voltage and source resistance both held fixed, for instance a 100 ohm source — produces the maximum power transfer relationship.[1401]

## Resistance in electrochemical cells

The internal resistance of a battery, also called IR or ESR, is not a single quantity but two resistances in series. The electrical resistance comes from the internal metal contacts and construction; the ionic resistance comes from the electrochemical reaction itself, and depends on the conductivity of the electrolyte, the electrode surface area and polarization.[140] The two are distinguishable in time. Under a current pulse, the battery voltage drops sharply and immediately — that steep initial step is the electrical resistance, which is always present and acts instantly.[140] The ionic component lags, showing up only after some delay and settling to a fixed value over time, which is why it is visible only under pulse conditions.[140] Electrode materials must themselves be low resistance; the positive electrode of a NiMH cell measures around 1 ohm depending on probe placement, with both surface area and bulk volume contributing.[1200]

## Resistance in false product claims

Resistance is a favoured ingredient in pseudo-technical marketing, mixed with heat loss, harmonic distortion, power quality, reactive power and electromagnetic interference to produce claims that sound plausible without meaning anything.[870] Wipes sold on the premise that cleaning a fuse box aligns the electrons and lowers resistance fall into this category and would require controlled experiments and proper engineering measurements to substantiate — measurements the vendor does not supply.[870]

A related claim is that a heating element's resistivity is identical in the cold and hot states, offered as an efficiency advantage.[1186] It is irrelevant: a resistive radiant heater converts everything into heat and is 100% efficient regardless of internal losses, so the figure of merit is the energy delivered, not the constancy of the element's resistance.[1186]

## The infinite resistor grid

A recurring puzzle asks for the resistance measured across one resistor in an infinite two-dimensional grid of identical resistors, conventionally 1 ohm each although the value does not matter.[25] The answer is 0.5·R.[25] The result is verifiable on a finite physical grid: with R = 10 k, the expected 5 k appears as measurements of 5.034 k, 5.017 k and 5.02 k at various points, all within the tolerance such a grid would be expected to show.[25] The harder variant asks for the resistance between diagonally opposite nodes, which resists intuitive solution and often drives people to write a program; the accepted answer is 2/π times R, about 0.636·R.[25]
