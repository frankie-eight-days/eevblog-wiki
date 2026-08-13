# voltage

Voltage is electrical potential difference: the difference in electrical potential between two points in a circuit.[1009] It is the quantity that pushes charge through a conductor, and together with current and resistance it forms the small set of relationships on which practically all circuit analysis rests.[27aG9xhfk6s] It is also one of the most misused terms in engineering, routinely confused with power and with energy by people who should know better.[1009]

Sources of voltage are varied and need not involve chemistry or rotating machinery: a battery, a solar cell, a junction device such as a thermocouple or a Peltier element, or a generator consisting of a wire moving through a magnetic field.[1009]

## Voltage, power and energy are three different things

Voltage can be expressed — and arguably more correctly is expressed — as the difference in electrical potential energy between two points.[1009] That phrasing invites the mistake of treating voltage as energy. A physicist will say voltage is energy per unit charge, volts equal joules per coulomb, and that is correct as far as it goes.[1009] It does not make voltage into energy, because voltage can exist with practically no energy behind it. Static electricity is the standard demonstration: rubbing feet on carpet generates tens of thousands of volts, and discharging that will not hurt anyone, because there is essentially no energy in it.[1009]

Power is the product of voltage and current.[1009] Five volts into a constant-current one-amp load is five watts, an instantaneous figure with no time component in it at all.[1009] Energy is power accumulated over time, and the rate of accumulation depends on the instantaneous power: at three volts into the same load the accumulator climbs more slowly, at two volts slower still.[1009] Claims that a cell has "1.5 volts of energy" or 1.5 volts of power are simply category errors.[1009]

The distinction has a practical consequence in battery ratings. A milliamp-hour figure ignores the fact that cell voltage is not constant but tapers as the cell discharges, so the watt-hour figure is the correct statement of energy capacity: a 25 watt-hour battery could deliver 25 watts for an hour or one watt for 25 hours.[1009] A 20,000 mAh USB battery bank carries a 77 watt-hour rating derived from an internal cell voltage of 3.85 volts, but a constant five-watt load measured only 61.8 watt-hours out of it, because the mAh figure is input-referred to the cell rather than to the boosted output.[1648]

The same reasoning disposes of energy-harvesting claims that report only a voltage. Producing a voltage is nothing in itself; what matters is the power produced.[1633] One wireless-power demonstrator reported an output of 0.0037 volts, and a later test of the same system showed a phone receiving two and a half milliwatts while a screenshot of a detected 5.2 volts was presented as evidence of charging.[1408]

## Voltage is always a difference

Because voltage is defined between two points, no point in a circuit has a voltage on its own — only relative to whatever node has been designated zero. Zero volts is therefore not an absence of anything: "zero volts is not the absence of voltage", it is merely the point where the black lead of the voltmeter has been placed.[HbMnQdRzD8A] Four five-volt batteries in series give twenty volts end to end; the same stack measured from its midpoint gives plus ten and minus ten.[HbMnQdRzD8A] In an inverting amplifier this produces the apparent paradox of five volts at the input resistor and minus five volts at the output while the op-amp inputs themselves sit at nothing, the amplifier driving its output to whatever voltage holds the inverting input at zero.[HbMnQdRzD8A]

Symmetry can establish equal voltages without any calculation. In a resistor cube driven between two opposite corners, inspection of the top-bottom and left-right symmetry shows that the voltage at one intermediate node must be identical to the voltage at another, which collapses the network into something solvable.[1472]

The conventional definition also has an edge. Under classical electronics, voltage is created only from electric fields — the integral of E dl along a path — and on that definition there is no voltage across a coil at all, because there is no electric field through the coil.[UStV3zyhgnQ]

## Ohm's law and DC analysis

The relationship between voltage, current and resistance is direct: knowing current and resistance gives the voltage across a component by multiplication, knowing resistance and voltage gives the current by division, and knowing current and voltage gives the resistance.[27aG9xhfk6s] Physically, a higher voltage across a resistor forces more electrons through it than a lower voltage across the same resistor.[27aG9xhfk6s] The common informal description of voltage as the pressure behind the electrons pushing them through a wire or component captures this.[27aG9xhfk6s]

The water analogy makes the pressure interpretation concrete: the height of a dam corresponds to voltage, while the rate of flow out of it corresponds to power and the gate opening controls the current.[1009] Pouring water from a greater height is the equivalent of a higher potential difference, and pouring it fast as well gives high current at high voltage.[yQ7_A4Cr9ak]

The same circuit algebra transfers wholesale to thermal design, where voltage becomes temperature, current becomes power and resistance becomes thermal resistance measured in degrees per watt.[105]

Nodal analysis works directly in voltages: solving the nodal equation yields the voltage at a node, and once that node voltage is known the branch current follows from Ohm's law relative to earth.[820] Mesh analysis takes the complementary route through loop equations, with the known resistor and source voltage values substituted in.[820] For maximum power transfer studies the current is computed as the source voltage divided by the sum of a fixed source resistance and a stepped load resistance.[1401] Simulation makes the same information available without algebra: a SPICE DC operating point analysis produces no waveforms at all, only a text listing of every node voltage and branch current, and the voltage across a component is obtained by taking the difference of two net names.[516]

## Voltage in AC circuits

For an alternating waveform, a single number does not define the voltage, and there are four separate conventional ways to state it — a distinction that applies equally to current.[1417]

Everything learned about DC carries over to AC provided voltage, current and reactance are given phase components as well as magnitudes.[1470] Ohm's law itself is unchanged; the impedance is simply a complex number with a real part and an imaginary part, the imaginary part representing the phase difference between the voltage and the current across that impedance.[1729] Kirchhoff's laws, nodal and mesh analysis, Thévenin and Norton equivalents and superposition all behave identically with impedance substituted for resistance.[1729]

For an inductor, voltage leads current by 90 degrees, so the ratio of voltage to current is jωL.[1470] For a capacitor, current leads the voltage, giving a reactance of 1/ωC at an angle of minus 90 degrees — anti-phase relative to the inductor, assuming ideal components.[1470] Voltages in this form are usually stated in RMS with a phase angle, for example 5 V RMS at 20 degrees, and multiplication in polar form multiplies the magnitudes while adding the angles.[1470] Calculators aimed at engineers include rectangular-to-polar conversion for exactly this work, so that a source given as 100 volts at 0 degrees can be combined with impedances expressed in rectangular form.[7v-WfiFrFMM]

Power splits along the same lines. With a purely resistive load the phase angle is zero, the cosine term is one, and power is simply voltage times current.[1730] With reactance present, the reactive power Q is the same voltage-current product carrying a sine-of-theta term, theta being the phase difference in degrees between voltage and current.[1730]

## Inductive kick

An inductor whose current is interrupted does not permit the current to stop. When the magnetic field collapses and there is no path for the current, the voltage must rise — the formula must be obeyed.[1409] Switching off a relay coil generates a large reverse voltage that swings the node above the supply rail, which for a 1.2-volt battery source means a large positive excursion at that point, and it is the reverse-connected clamp diode across the coil that limits how far it goes.[708] This is why back-EMF diodes are not optional.[1409]

## Measuring voltage

A multimeter displays the input voltage fed into it, and adjusting a supply is tracked immediately on the display — it is fundamentally a voltage measurement device.[UJjMt2-k99c] An oscilloscope is no different in that respect except that it measures voltage with respect to time, with voltage on the vertical axis and a movable zero-volt reference trace.[UJjMt2-k99c] With no input the trace sits on the reference line; at one volt per division a five-volt input steps the trace up by five divisions, the same measurement a multimeter makes but at lower precision and resolution.[UJjMt2-k99c] In X-Y mode the time base disappears entirely and the voltage on the X input positions the dot horizontally while the voltage on the Y input positions it vertically.[153]

Voltage measurements can be turned into phase measurements. Using cursors on an X-Y ellipse, the intercept value divided by the maximum amplitude gives a ratio whose arcsine is the phase angle: 1.062 V divided by 2.046 V gives 0.51, and on the ordinary time display 1.055 V divided by 2.102 V yields 30.12 degrees.[1751] Voltage and current together also yield everything about a component under test — capacitance, inductance, series and parallel resistance, quality factor and dissipation factor all fall out of the voltage, the current and the phase between them.[81][100]

Because power requires both quantities, measuring voltage and current simultaneously requires either two instruments or one built for it. Owning at least two multimeters is a standing bench recommendation of Dave Jones for exactly this reason, with the secondary benefit that periodically measuring a common voltage and resistance source with both reveals if either has drifted.[75] Some meters merge the function: one handheld reads voltage and current at once and displays watts, along with VA and the phase angle on a triple display.[712] Others only appear to — a bench multimeter that audibly clicks a relay about once a second between voltage and current is time-multiplexing rather than measuring simultaneously.[829]

Low-level voltage work drops into the noise floor of the instrument: an op-amp input noise measurement read as minus 123 dBV RMS converts to a voltage by dividing by 20 and taking the inverse log, giving 708 nanovolts.[528] At the other extreme, injected voltage can corrupt a reading outright — one handheld meter's current measurement was thrown badly off by 10 volts peak to peak at 10 MHz coupled into the lead, and even one volt peak to peak was more than enough to disturb it, an effect not seen on other meters.[933]

## Voltage in fault finding

The first question about a dead board is whether the supply voltage is present at all. A microcontroller with no voltage reaching it cannot run and cannot produce a clock, so the failure says nothing about the microcontroller itself.[1520] The measured rail is also a direct check on mechanical integrity: eight D cells reading ten volts where twelve-point-something was expected pointed straight at a contact problem, and in that case a second fault as well.[1756] Corroded battery terminals can pass voltage at one end while still failing to power the unit.[1756]

Voltage that is correct in magnitude can still be wrong in every other respect. A scope fed its own 1 kHz calibration signal displayed the correct amplitude at 2 V per division while the trace was surrounded by garbage jumping all over the place.[564] A capacitor that had fallen from 22 nanofarads to around 500 picofarads still produced a nominal 0.3 volts at the point it drove, which is why component values measured at low voltage on an LCR meter do not necessarily describe behaviour at working voltage — testing under voltage is a different test.[379][1714] Supply rails also move on their own: a rail measured at 48 V one day read over 50 V the next, following the mains.[1714]

## Voltage as a bench control

Bench supplies are set and read in volts, and the interface for doing so is a recurring source of friction. On one triple-output supply the output changes live as the knob is turned even before entry is confirmed, the digit-skip button will not jump to the ten-volt digit — presumably because the step is large enough to destroy the circuit under test — and reaching knob-adjust mode at all requires selecting the channel, entering V set, and pressing again.[439] More capable supplies sequence voltage and current settings against time in a list function, cycling once or repeating indefinitely.[1691] Displaying voltage, current and power together is preferred to a segmented triple display, and the available resolution is a purchased option: 10 mV and 10 mA steps without the high-resolution licence installed.[509] A supply set to 57.6 volts with a 1.2-amp limit and drawing one amp delivers about 57 watts.[1375] Programmatically, the same settings are reached over a text interface, where a SCPI parser matches a voltage node spelled with a required VOLT and an optional AGE and returns the value on query.[GarToEo6ekQ]

Battery characterisation is voltage logging over time. A discharge curve can come from a data logger or a multimeter, or from writing down a reading every minute by hand; a cell starting at 1.65 volts against a nominated cut-off of 0.8 volts under a 0.1-amp constant-current load gives all the data needed once the numbers are in a spreadsheet.[772] Under load the terminal voltage drops immediately: a LiPo at 4.2 volts fell to 4.07 volts the instant a five-amp load was applied, purely from internal ESR, before beginning its gradual decline toward a 3-volt safety cut-off.[393] Distinguishing lead loss from cell behaviour requires checking the leads first — a supply set to two volts showed almost no drop across the test leads, against an open-circuit 2.59 volts from the cells themselves.[789]

## High voltage, low voltage and what actually hurts

Voltage and current cannot be considered separately where safety is concerned: current is what kills, but sufficient voltage is needed to push that current through the body.[yQ7_A4Cr9ak] Australian power points, rated around 10 amps, can kill on contact without a safety switch, while the lower distribution voltage and higher current typical of the United States shifts the dominant hazard toward house fires.[yQ7_A4Cr9ak] A handheld Tesla coil illustrates the other side of the trade: about 40,000 volts at relatively small current and around one megahertz, which passes across the skin rather than through the body, with air breaking down at roughly 20,000 volts per centimetre.[yQ7_A4Cr9ak]

Electrostatic voltages on the body are large but, as above, carry little energy. Walking across a lab floor with shoes on generates a substantial reading; the same walk barefoot does not even reach 100 volts.[768]

Very high voltage is also the entire basis of long-distance transmission. Since cable loss is I²R, moving a given power at higher voltage means lower current and lower loss, which is why HVDC links run at levels such as 500 kilovolts.[AWYuyf3ILLk]

## Orders of magnitude

Voltage is the usual vehicle for the order-of-magnitude shorthand. One order is ten times: a voltage dropping by an order of magnitude goes from 1 volt to 0.1 volts, and increasing by one takes it from 1 volt to 10 volts.[286] The reference point need not be one or any power of ten — a thousand volts raised by an order of magnitude is ten thousand volts, and 3.5 volts raised by an order of magnitude is roughly 35 volts.[286] The term is deliberately approximate, and being out by three orders of magnitude means being wrong by a factor of 1000 in an unspecified direction.[286]

## Voltage on a transmission line

On a line simulated with a pulse generator and a resistive load, the voltage and current waveforms propagate together and, with the load matched to the line, essentially no reflected signal comes back toward the generator.[lBycH31K-E8] Mismatching the load — raising it to 1000 ohms — is what produces reflections.[lBycH31K-E8]

## Teaching voltage

What voltage is, alongside what a resistor and a capacitor are and how a pull-up works, is genuinely introductory material, and there is enough of it to fill a 500-page book on the basics alone.[1270] University-level textbooks running to 1100 pages are designed as course companions and are not where a beginner should start looking for an answer to what a voltage in a battery is.[1270]
