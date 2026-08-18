# kirchhoff current law

Kirchhoff's current law, abbreviated KCL, states that the sum of the currents flowing into a junction equals the sum of the currents flowing out of it.[819] It ranks alongside Ohm's law as one of the most fundamental laws in electronics, and it is paired with Kirchhoff's voltage law, which governs the voltages around a loop.[819] Both are named after Gustav Kirchhoff, who formulated them in about 1845.[819]

The law is a statement of the conservation of charge: charge put into a circuit must come out again, and at a junction point this reduces to current in equals current out.[819] That single sentence is the entirety of the law — nothing more complicated is involved, and the concept matters more than any formula derived from it.[819]

## Statement and algebraic forms

For a junction with one current entering and two leaving, the relationship is written directly as I1 = I2 + I3.[819] The form extends to any number of branches: an additional current I0 entering simply appears on the input side of the equation, and the law can be written for any number of currents flowing in or out, even the trivial case of one in and one out.[819]

More powerful mathematically is the rearranged form in which the algebraic sum of all currents at a junction equals zero.[819][820] This requires a sign convention — currents entering the junction taken as positive and those leaving as negative, or the reverse.[819] Which polarity is assigned makes no difference provided the choice is applied consistently, and a negative result that falls out of the algebra is informative rather than an error, since it reveals something about the direction of current in the circuit being analysed.[819]

## Use in circuit analysis

Nodal analysis is built directly on KCL.[820] Choosing a reference point is arbitrary, and by convention all currents at the node under examination may be assumed to be leaving it, with none flowing in.[820] Each branch current is expressed by Ohm's law in terms of the unknown node voltage, and the resulting nodal equation — of the form I1 + I2 + I3 = 0 — is solved for that voltage.[820] Applied to a textbook circuit of three resistors and two voltage sources, this procedure yields a node voltage of 2.3636 V, from which the current through the target resistor follows as 0.11818 A by Ohm's law.[820] Mesh analysis, which rests on Kirchhoff's voltage law, produces the identical answer for the same circuit, as does superposition; agreement between the three methods is a check that both laws hold.[820]

KCL also marks the boundary of simpler shortcuts. The two-resistor current divider formula applies only to that specific case and cannot be extended by summing terms; for three or more resistors in parallel, the analysis must fall back on Kirchhoff's current law.[1399]

In highly symmetrical networks the law supports a shortcut of its own. In the resistor cube problem, recognising that equal resistances force equal branch currents identifies equipotential nodes, so the network collapses without writing out the full set of Ohm's law and KCL equations.[1472]

## Application on the bench

Design by inspection leans on KCL as a standard DC circuit theorem alongside knowledge of basic building blocks.[1285] For a linear regulator, the capacitor on the output is an open circuit at DC, so the output current equals the load — a measured 50 µA in one worked case — and the input current is fixed by I in = I Q + I out, with the quiescent current read from the data sheet.[1285]

The law also constrains an inverting op-amp node: the current up the feedback resistor plus the leakage current into the input must equal the current flowing in, and with a good enough practical op-amp that leakage can actually be measured.[819]

For a shunt regulator, the resistor must pass the zener test current and the load current together. With a 50 mA test current from the data sheet and a 50 mA load, the resistor carries 100 mA; across a differential of 12 V input minus a 5 V zener, that gives 69 Ω.[908]

Fault diagnosis is a natural fit, because KCL bounds where missing current can be. In an oscilloscope supply where excess current was dragging a rail down, the law reduced the possibilities to a short list: the current was not passing the current sense resistor, leaving only the base of a pass transistor into the LM723 regulator, or the regulator's current limit pin.[804] The same reasoning applies to return paths — current leaving a MOSFET into ground must complete a loop, and the ground plane is what carries it back.[812]

Multiplexed displays run into the law as a hard limit. A 75 Ω series resistor sized for a nominal 20 mA at 3.3 V delivers that current to a single segment, but turning on all 40 segments forces the same total current to be shared, dropping each segment to half a milliamp and leaving the display very dim.[1491] Driving segments in smaller groups rather than all at once is the way around it.[1491]

## Ideal assumptions and real parts

An exam question involving one LED feeding two parallel LEDs illustrates both the reliability of the law and the fragility of what is assembled around it. Given 2 V at 20 mA and matched devices, KCL forces the 20 mA in the lower branch to split evenly, so each parallel LED carries 10 mA.[1427] Of all the idealisations such a question demands, the assumption that Kirchhoff's current law holds is the one that must be granted above everything else.[1427]

The rest of the idealisation does not survive contact with real components. LED forward voltage is non-linear, so a device specified at 2 V and 20 mA sits nearer 1.8 V or 1.85 V at 10 mA, and rigidly holding VF constant while insisting each branch carries 20 mA implies 40 mA in the series LED — a current at which the forward voltage has moved again.[1427] The current split is nonetheless real and continuous: at any instant the two upper branch currents sum to the lower branch current, even as the division shifts with temperature and lead connections.[1427] It is not, however, visible by eye — a branch carrying twice the current of its neighbours can appear to have much the same brightness.[1427]

## Standing in the fundamentals

The law is generally already obvious to anyone who has thought about circuits, and is used daily in circuit theory without conscious effort.[819] The stated position is that if the only thing carried away is that current in equals current out, and that the voltages around a loop sum to zero or the applied voltages equal the voltages dropped, that is enough for everyday circuit analysis.[819] Deriving equations and solving circuits algebraically is optional; the concepts alone are powerful, and become more so the deeper the circuit theory goes.[819]

Together with Ohm's law and basic building block circuits, KCL is treated as part of the minimum foundation for troubleshooting hardware rather than merely assembling it.[zyuRcsM0gjI]
