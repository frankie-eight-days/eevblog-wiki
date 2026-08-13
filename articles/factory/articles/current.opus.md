# current

Current is the flow of electrical charge past a point in a circuit, measured in amps, and it is one of the three quantities — with voltage and resistance — on which the whole of practical electronics rests.[27aG9xhfk6s] Current flows only when there is a voltage difference between two points and a conductive path exists for charge to move along; connecting the two points with a wire creates such a path.[27aG9xhfk6s] Because power is the product of voltage and current, current is also the quantity that decides whether any energy is actually delivered: a circuit can sit at high voltage indefinitely and dissipate nothing at all until current begins to flow.[1009]

## Relationship to voltage and resistance

Ohm's law binds the three quantities together in both directions. Multiplying current by resistance gives the voltage across a component; dividing voltage by resistance gives the current through it; dividing voltage by current gives the resistance.[27aG9xhfk6s] Increasing either the current through a resistor or the resistor's value raises the voltage across it, and increasing the voltage across a resistor increases the force pushing charge through it and therefore raises the current.[27aG9xhfk6s]

Power follows directly: P equals V times I, in watts.[1009] Power in circuit theory is instantaneous, and the corollary of the P = V·I relationship is that current is the necessary ingredient — no current, no power, whatever the voltage.[1009] A reservoir analogy makes the separation concrete: the height of a dam corresponds to voltage, the rate of water flowing out to power, the setting of the gate that controls how much water escapes to current, and the volume of water held behind the wall to energy. Closing the gate leaves the stored energy untouched while flow, power and current all go to zero.[1009] Confusing current with a unit of accumulated charge or energy — amp hours, for instance — is a category error, not a rounding error.[1633]

## Current in AC circuits

In AC circuits capacitors and inductors introduce a phase difference between the voltage and current waveforms.[1469] For a capacitor the current leads the voltage; for an inductor the current lags it.[1469] The consequence is that current can no longer be described by a magnitude alone — it carries a phase angle, and so do voltage and reactance.[1470]

Ohm's law itself does not change. AC analysis uses the same law and the same techniques as DC, with voltages, currents and impedances expressed as complex numbers having a real and an imaginary part, in either rectangular or polar form.[1729][1470] The imaginary part of an impedance represents the phase difference between the voltage across it and the current through it.[1729] Everything else carries over unchanged: Kirchhoff's laws, nodal analysis, mesh analysis, Thevenin and Norton equivalents and superposition all work in AC once impedance Z replaces resistance.[1729]

For an inductor, because voltage leads current, the ratio V/I sits at an angle of 90 degrees, which in complex notation is jωL — the reactance in ohms, dependent on frequency.[1470] For a capacitor the reactance is 1/ωC at an angle of minus 90 degrees, anti-phase to the inductor and assuming ideal components.[1470]

Solving for current means dividing voltage by total impedance.[7v-WfiFrFMM] The arithmetic favours different forms at different stages: complex numbers add and subtract most easily in rectangular form, so impedances are summed there, but division requires polar form.[7v-WfiFrFMM] In a worked case, an impedance of 10 − j75 converts to a magnitude of 75.66 at a phase of −82.4 degrees; dividing 100 by 75.66 gives 1.32 amps, and subtracting the phases gives +82.4 degrees, so the steady-state current is 1.32 amps at 82.4 degrees, plotted as a single phasor.[1661] This is a frequency-domain result: the current through a network cannot be found without first converting each capacitor and inductor into an impedance or reactance and computing the total.[1661]

Phase also splits AC power into components. In a purely resistive load the cosine term is one and power is simply voltage times current.[1730] Introduce a reactance and a phase difference appears, giving reactive power Q — again the product of voltage and current, but scaled by the sine of the phase angle rather than the cosine.[1730]

## Current through a capacitor

Whether current flows through a capacitor is a question with two defensible answers depending on the level of description, and it is a recurring point of dispute.[486] At the level of the wires and plates, current unambiguously flows: charge arrives at one plate and leaves the other.[486] Inside the dielectric, no electrons cross — what exists there is displacement current, a consequence of the changing electric field between the plates creating a changing magnetic field, and part of Maxwell's account of electromagnetism.[486]

For circuit work the practical answer is that current does flow through the capacitor, because the ordinary design equations assume current in the series loop even though the capacitor is effectively an open circuit at DC.[486] The governing relations are Q = CV and I = dQ/dt: current equals the rate of change of charge with time.[486]

Energy storage follows from the same relation. Because the voltage ramp across a charging capacitor is linear, the average voltage is half the final value, so energy — power times time — becomes half the voltage times the current times time.[1618]

## Transients and inductive current

An inductor resists a change in current. At the instant a switch is closed no current flows at all, because the magnetic field has yet to build; the current then rises exponentially from zero, reaching 63.2% of its final value in one time constant and settling within about 1% after five.[1406] While the inductor behaves as an open circuit and no current flows through the series resistor, there is no voltage drop across that resistor, so the full supply voltage appears across the inductor.[1406]

The reverse case is the dangerous one. When the field collapses, the current must continue somewhere; if there is no path, the voltage rises without limit to force one.[1409] This is why flyback or back-EMF diodes are not optional across inductive loads.[1409] With the diode present, the collapse drives a large current spike around the loop through the diode, which clamps the node at roughly the diode's forward voltage; without it, the node can rise to tens of volts or far beyond.[708]

## Current in circuit analysis

Mesh analysis begins by assuming a current direction — conventionally clockwise around each loop — without knowing whether it is correct.[820] A negative result simply means the assumed direction was backwards, and the sign is trusted rather than corrected mid-solution.[820] Where two mesh currents share a branch and flow in opposite senses, the branch current is the difference of the two.[820]

Symmetry can remove work entirely. In the classic resistor-cube problem, nodes at equal potential can be shorted together, and branches carrying no current can simply be deleted from the network, collapsing the cube into a trivial series-parallel combination.[1472] The balanced-Wheatstone-bridge argument gives the same result: a balanced bridge has no current through its central branch, so that branch may be eliminated outright.[1472]

Simulation gives the same information numerically. A DC operating point analysis produces no waveforms — there is nothing to plot — only a text listing of every node voltage and branch current in the circuit, which is more useful than its plainness suggests.[516] Parameter sweeps show how small those currents move: over a temperature sweep, a current changed only from 6.508 mA to 6.51 mA, a shift of ten or twenty microamps.[301] Transient simulation plotted against time gives voltage and current graphs for a load directly.[1439]

## Measuring current

Voltage and current must often be measured simultaneously to obtain power, and since a single conventional multimeter cannot do both at once, two meters are the practical minimum for anyone serious about bench work.[75] Some instruments close the gap. A meter with power measurement capability reads voltage and current together and displays watts, and with a triple display can also show VA, the phase angle of the current, and frequency.[712] Bench multimeters may separate the current and voltage terminals with a common ground and switch between the two functions roughly once a second, updating the display alternately — a physical switch rather than genuine simultaneous acquisition.[829] From voltage and current together, a long list of derived quantities becomes measurable: series resistance, parallel resistance, quality factor, dissipation factor.[100]

Range matters as much as accuracy. Reverse leakage measured at 0.15 microamps requires a microamp range, while the switched-on state of the same circuit draws 15 milliamps — a range change of four orders of magnitude on the same measurement session.[357] Current measurement also settles claims quickly: producing a voltage means little without the current to go with it, and a short-circuit current of half a milliamp is decisive on its own.[1633]

Current readings diagnose faults by what they do not do. A supply rail behaving erratically while the current draw stays flat indicates a fault that is not an overload.[804] Susceptibility testing shows the opposite pattern, where injected RF at 10 volts peak to peak and 10 MHz drove a meter's current reading progressively downward as the interference level rose.[933] Thermal imaging localises current distribution directly — in a set of parallel conductors, the two carrying essentially all of the current run hot while the third shows only residual heat conducted from its neighbours.[401] The same principle applies at the extreme low end, where the drain current of a single MOSFET sensor is read out as a DC voltage from an amplifier chain, with the full bright-to-dark colour scale spanning roughly half a nanoamp down to zero.[1594]

Not every conductor in a circuit carries current. Remote-sense wiring on a precision supply may be any convenient gauge, because a sense line carries no current whatsoever and therefore develops no error-producing drop.[667]

## Current as a set quantity

On programmable bench equipment, current is a variable to be commanded rather than only observed. Power supplies expose a current setting alongside voltage, entered by knob or keypad.[439][1691] A list function sequences voltage and current settings over time, repeating for a chosen number of cycles or indefinitely.[1691] Displays typically present voltage, current and power together, with the available resolution — 10 mV and 10 mA in one instance — sometimes gated behind a paid high-resolution option.[509] Electronic loads select among current, voltage, resistance and power as the graphed variable, though plotting voltage and current on a shared time axis with a second Y axis is a common omission.[1023] Programmed load steps are exact enough to be useful: a commanded 5 amp step lands on 5 amps and immediately reveals the cell's internal ESR as a voltage drop.[393]

Remote control protocols mirror this structure. An SCPI parser distinguishes a voltage node from a current node by required and optional character segments — c-u-r-r required, e-n-t optional — and dispatches to separate query or command handlers accordingly.[GarToEo6ekQ]

## Pedagogy

Current sits in the irreducible core of introductory electronics, alongside voltage and resistance, and any teaching resource that presents circuits without explaining how current actually behaves in them — for example how a light-dependent resistor modulates the current into a transistor's base — has left out the part that matters.[27aG9xhfk6s] There is enough substance in the basics alone — what a resistor is, what a capacitor is, how a pull-up resistor works, what voltage and current actually are — to fill a 500-page book before any advanced material is reached.[1270] The controlling role of current is what makes the transistor a building block in the first place: a voltage or current applied to one pair of terminals controls the current through another pair, and because the controlled output power can exceed the controlling input power, the device amplifies.[I4tHtPwYQ_o]
