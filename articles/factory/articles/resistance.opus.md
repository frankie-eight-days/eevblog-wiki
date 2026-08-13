# resistance

Resistance is the property of a conductor or component that opposes the flow of electrons, measured in ohms and denoted by the Greek letter omega.[27aG9xhfk6s][1636] Together with voltage and current it forms the set of quantities that everything else in electronics is built on, and it is the first thing taught alongside them.[1397][27aG9xhfk6s] Its practical importance is that resistance is never confined to resistors: it exists inside a battery, inside a power supply, in any voltage source as internal resistance, in a PCB trace, in wiring, in transformer windings — almost anywhere current flows.[1401] Wherever current passes through resistance there is a voltage drop set by Ohm's law and power dissipated in watts.[1401]

## Ohm's law and the three quantities

The relationship between voltage, current, and resistance is Ohm's law, named after George Ohm.[27aG9xhfk6s] Knowing current and resistance gives voltage by multiplication; knowing resistance and voltage gives current by division; knowing current and voltage gives resistance by dividing voltage by current.[27aG9xhfk6s] Raising either the current through a resistor or the resistor's value raises the voltage across it.[27aG9xhfk6s]

Resistance is bidirectional in its consequences: a fixed resistance in a circuit determines how much current a given source can push, and the current the source must supply determines how much of the source's own internal resistance matters. A source resistance in series with a variable load resistance is the standard arrangement used to explore maximum power transfer, with the current at each step computed as source voltage divided by the sum of load resistance and fixed source resistance.[1401]

## Resistivity, geometry, and sheet resistance

Resistance is not an intrinsic property of a material but of a piece of material. It depends on cross-sectional area and length as well as on the material itself, through the quantity rho.[1163] For a conductor the resistance is the material resistivity multiplied by length and divided by area, where the area is width times thickness; each material carries its own resistivity figure.[732] For copper PCB foil the thickness is effectively fixed by the plating weight — one ounce copper is about 35 microns, treated as a universal thickness — which is what allows the formula to be rearranged into a sheet-resistance form where only the length-to-width ratio matters.[732]

The same geometric dependence shows up in semiconductors as a design variable. In a bipolar transistor, a lightly doped region is effectively higher resistance than a heavily doped one, so the die stacks a low-resistance layer against a thin, high-resistance layer, and most of the collector-base voltage is dropped across the high-resistance side.[748]

## Resistance in AC circuits

In alternating-current work resistance becomes the real part of a larger quantity. Impedance is the real resistance plus the complex reactance; its inverse, admittance, is the conductance plus the complex susceptance.[1728] Reactance is measured in ohms just as resistance is, but carries a plus or minus sign in the j term depending on whether it is capacitive or inductive.[1730] A device under test that is a pure resistance shows no phase difference between voltage and current at all — a phase angle of zero.[81] On a Smith chart the circles represent pure resistances, 50 ohms among them, while the radiating lines represent complex impedances at different phase angles.[1101]

Conductance G is the inverse of resistance, expressing how easily current flows rather than how much opposition is presented.[1728] Some meters measure conductance directly and read out in nanosiemens, which is useful for very high resistance work and for material science; converting back to ohms requires inverting the reading.[1728] The series and parallel rules swap over: conductances in series follow the parallel-resistor form, one over the total equalling the sum of the reciprocals, so it is generally easier to convert them back to resistances first.[1728]

No real component is purely one thing. Every practical inductor, capacitor, and resistor has all three of inductance, resistance, and capacitance in it — an inductor has capacitance between its windings, a resistor has some inductance — so a purely inductive circuit does not exist.[1728]

## Real power and I-squared-R loss

Real power is only ever dissipated in resistances.[1730] It is never dissipated in capacitances or in inductors; where a capacitor or inductor does dissipate, it is through its equivalent series resistance.[1730] This is why every current-carrying conductor is a heat source: wires, transmission lines, power cords, house wiring, street wires and 500 kV transmission lines all contain resistance and dissipate real power as I-squared-R or copper losses.[1730] In transformers the same losses accumulate across windings, connections, crimps, and the copper or weight-saving aluminium used in the conductors.[1730]

The accounting is exact and unforgiving. A load drawing 67 VA at the wall while dissipating 30 watts of real power internally implies another 37 watts dissipated elsewhere in the system, because the current is real current and must be lost in resistances somewhere upstream.[1730] Any analysis of power delivery that assumes ideal wires and neglects I-squared-R losses discards the only mechanism by which the delivery system loses energy.[ItoRt1buLkM] The same term underlies the derivation of RMS: DC power is I-squared-R, and the AC equivalent is the average of the squared value times the load resistance, with the resistance cancelling from both sides of the equation.[1417]

Conductor losses are real but should not be overstated. The losses in ordinary conductors are actually pretty small — if they were not, everyone would be paying enormously more for electricity — which is the flaw in marketing claims that a household product can save money by reducing wiring resistance.[870]

## Transmission lines

A transmission line is modelled as a chain of lumped elements, each unit length carrying series resistance, series inductance, and shunt capacitance between the conductors.[1439] The unit length is arbitrary — a centimetre, an inch, a metre — and the model is built by duplicating the element outward, in both directions, effectively to infinity.[1439] For an idealised analysis the series resistance may be set to zero, but real cable is lossy: an oscilloscope probe coax is specified with a resistance in ohms per unit length, and simulating it accurately requires that figure rather than a lossless coax model.[1439][1445] A representative lossy-coax SPICE directive uses 210 ohms of resistance, 83 pF of capacitance, 208 of inductance, and a length of 1.2 metres.[1445]

## Measuring resistance

Resistance measurement is one of the three core functions of a multimeter, alongside voltage and current, provided by a built-in ohmmeter reading in ohms.[1636] Even a decades-old instrument covers it — the Fluke 73 dates from the early 1980s and measures resistance from the ohm symbol on its dial.[847] An LCR meter extends the set: multimeters measure resistance and usually capacitance, but few measure inductance, and an LCR meter adds accurate inductance and capacitance plus quality factor, dissipation factor, and ESR.[115] Auto-ranging LCR instruments can misidentify what they are looking at, reporting a shorted probe pair as an inductor with 0.02 of series resistance rather than as the resistor it primarily is.[1375] Cheap component testers show similar limits, tracking resistance and inductance reasonably at 1 kHz for a 1 mH part but running out of resolution at 10 µH and failing entirely at 1 µH, where the reading collapses to a resistor.[1020]

Impedance analysers reach resistance indirectly. Placing a shunt resistor in series with the device under test and measuring both the generator voltage and the voltage across the device yields impedance, and from that capacitance, inductance, and resistance together with a full frequency response.[858][2] Resistance can also be derived from a voltage-versus-current sweep and plotted: PCB via measurements taken this way are linear from 0.1 A to 2 A, with a slight tailing-up non-linearity at the low end.[543]

## Decade boxes and substitution

A decade resistance box provides a switch-selected resistance for substitution work and is among the most useful pieces of bench test gear.[211] A nine-decade box has nine switches, each numbered zero to nine; the IET Labs RS201W spans 0.1 ohms to 100 megohms at 0.1 percent basic tolerance, using thumbwheel switches instead of the traditional rotaries, at a price of 539 US dollars.[211] Power rating is a practical constraint on such boxes — a 0.5 W rating may be per step or overall, and a lower-value box designed for 10 milliohm steps will take more power per step.[966]

The tolerance arithmetic of series-built substitution boxes is reassuring: four nominally 100-ohm resistors that are each actually 101 ohms total 404 ohms against a 400-ohm nominal, an error of 4 in 400, or 1 percent — the same 1 percent that would result from a hundred such resistors in series.[212]

A decade box is also a measurement instrument in its own right, used to find the value a circuit actually wants. Dialling resistance into a marginal LCD contrast circuit showed operation at 10 and 20 ohms, failure at 30 to 40 ohms, and thus bracketed the fault to a reset pin pulling the rail down.[710] The same substitution approach on an LCD V0 line identified 4.3 k as the working value, to be replaced by a fixed 4.7 k part.[1202]

## Resistance in fault-finding

Resistance measurement is the primary diagnostic in repair work, and low readings where high ones belong are the usual signal. A high-precision CMOS op-amp input that should present effectively infinite input impedance reading 60 ohms indicates the part is destroyed and is loading down whatever reference feeds it.[727] A power rail reading 0.21 ohms from pin 11 of an 8284 to the supply is a short, not a marginal reading.[1348] In an LED studio light, a node measuring 1 ohm against an expected 4.5 M identified the culprit.[1460] Conversely, a resistor measuring 925 ohms in circuit against a 1.025 k marking is not open and, once desoldered and confirmed at 1.025 k, is near enough to be exonerated.[1139]

Unstable resistance identifies mechanically failing parts. A switch measuring 190 ohms, then 170, then falling to three and two ohms only under hard finger pressure is failing, and reads 14.2 k open and zero closed once replaced.[1360] Contamination can create resistance where none should exist: conductive residue on a board carries current and changes its resistance as it does.[1072]

Resistance to mains earth is a safety measurement rather than a repair one. Equipment that measures 1 K to earth instead of a direct short is still low enough impedance to be dangerous to probe with a non-isolated oscilloscope, and a USB-powered board measuring 9 ohms from its ground pin to mains earth — through the host computer's grounding — is effectively earth-referenced and will destroy itself or the scope if probed anywhere other than at that ground terminal.[279]

## Resistance as a sensing mechanism

Because resistance responds to physical conditions, it serves as a transducer. A catalytic bead gas sensor behaves as a resistance whose value changes with the gas present: a heating element brings a sensing element to a few hundred degrees, burning the gas at the bead — which is why a flame arrestor is required.[603] Motor windings present resistance as load, and a marginal battery source collapses as soon as any resistance is applied to it.[789]

## Values, tolerance, and specialised parts

Trimming resistance without a trimmer pot is possible with snap-off networks: parallel elements of differing length, each snap raising the resistance by 20 percent, giving a five-fold increase once all nine parts are broken off, with an initial TCR of 100 ppm on a ceramic thick-film substrate.[1391] These exist because cermet trimmers are expensive.[1391] At the other extreme, transimpedance front ends for femtoampere measurement rely on a specialised hybrid feedback resistor: 10 gigohms against a 20 pA minimum full-scale range yields 0.2 volts, confirming a 200 mV full-scale design.[1755] A rheostat is the adjustable high-power form, an example being a 100 ohm part at plus or minus 5 percent.[1720]

In simulation, resistance must be entered in ohms with the correct unit interpretation — 1000 or 1 k both being accepted, in either case — alongside farads for capacitance and henries for inductance.[516] Electronic loads work in the same terms, offering resistance R as a selectable graph parameter beside voltage, current, and power.[1023]

## Network reduction

Resistance in networks is solved by repeated series and parallel reduction, aided by symmetry. In the resistor cube, symmetry lets pairs of resistors be collapsed to R/2 while others remain at R; a half-ohm in parallel with 1.5 ohms gives 0.375 R, and two such sections in series give 0.75 R as the resistance between diagonal-face nodes such as B and G, A and H, E and D, or C and F.[1472] The absolute value of R is irrelevant to the result — it can be 1 ohm or 10 k — since the answer is expressed as a multiple of R.[1472]

The same reduction logic governs op-amp feedback. In an inverting amplifier holding a virtual ground, unequal resistances scale the output's compensating swing: with twice the resistance in the feedback path, a one-volt rise at the input forces a two-volt fall at the output to hold the summing node at zero.[HbMnQdRzD8A]

## Teaching resistance

Introductory material conventionally presents voltage, current, and resistance as the foundational triad, sometimes styled the three pillars of electricity, and typically arrives at them through the water analogy of a pipe with resistance rather than through atoms and electron physics.[27aG9xhfk6s][WXJP_CNYt3o] Beginner curricula reasonably defer the rho-L-over-A treatment of resistivity, which belongs at university level, and reach resistance directly alongside charge, current, conductors, and mains safety.[1163][1304]

The term ohms-ky is used informally for a dead short.[1348]
