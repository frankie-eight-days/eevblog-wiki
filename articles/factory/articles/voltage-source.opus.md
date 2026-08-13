# voltage source

A voltage source is a circuit element that establishes a potential difference across its terminals, and along with the current source it forms one of the two primitive energy sources of DC circuit theory.[1397][1688] It sits immediately after voltage, current and resistance in the order in which electronics is usually learned, and it underpins Thevenin and Norton equivalents, mesh and nodal analysis, and the maximum power transfer theorem.[1397][1401] The single most consequential fact about it is negative: the ideal voltage source of the schematic symbol does not exist, and every real one carries an internal series resistance that must be accounted for.[1397][1401]

## Symbol and physical realisations

The conventional symbol is a circle enclosing the letter V, with the voltage value written alongside and the positive terminal marked at the top; the alternative is the battery symbol, whose stacked long and short bars denote a multi-cell battery.[1688] Either way the element represents a potential source of energy.[1688]

The category is defined by behaviour rather than construction, and the physical realisations are diverse: an electrochemical battery, a linear or switch-mode power supply, a lab supply, a solar cell, a Peltier device, a generator, or triboelectric effects.[1397] Generators push the discussion into AC, which is treated separately from the DC case.[1397]

## Non-ideality and source resistance

An ideal voltage source would hold its terminal voltage at any current draw. Because no such source exists, the correct model of a practical source is the ideal element in series with a resistor, and analysis that omits that resistor is analysis of something that cannot be built.[1397][1401] The series resistance is conventionally labelled RS for source resistance.[1401]

This internal resistance is what makes the maximum power transfer theorem non-trivial: with a source of fixed EMF and fixed RS driving a load resistance, there is a specific load value that extracts the greatest power from the source.[1401] The same quantity appears in simulation as an explicit parameter — a DC voltage source in LTspice exposes a series resistance field among its parametric entries, which is how a real cell is represented.[516] A CR2032 coin cell, for instance, may carry something on the order of 10 ohms of series resistance within the cell itself.[516]

## Behaviour in circuit analysis

In superposition and equivalent-circuit work, a voltage source is idealised to zero internal resistance and replaced by a short circuit while another source is considered; a current source in the same position is replaced by an open circuit instead.[820] Where a network contains more than two sources, every source other than the one under consideration must be replaced by its internal resistance in this way.[820]

Sign convention follows the assumed current direction rather than the physical identity of the part. Traversing a source in which the current flows from the negative terminal to the positive, the source is generating voltage in the circuit and enters the loop equation as positive.[820] The same battery traversed with current flowing from positive to negative acts as a voltage drop, purely as a consequence of the arbitrary current direction chosen at the start.[820] Kirchhoff's voltage law can therefore be stated either as the sum of applied voltages equalling the sum of the voltage drops, or as a loop sum equal to zero — a source is an applied voltage or a drop depending on which side of the equation it lands.[819]

A canonical worked network is two voltage sources labelled E1 and E2, at 10 V and 1 V, with three resistors of differing values, solved for the current through R2.[820]

## Converting to a constant current source

A voltage source is the starting point for a constant current source rather than its opposite: adding external regulating circuitry around a voltage source converts it into one.[1688] The voltage source behind the regulating circuitry sets the compliance voltage, the headroom within which the constant current circuit can maintain its programmed current.[1688][1397]

## Driving loads and bench practice

A low-impedance voltage source must not be connected directly across a non-linear element such as an LED.[1427] Impedance can be inferred from the operating point — a part driving 20 milliamps must be at least reasonably low impedance — and the prohibition follows from the load's non-linearity, not from any current rating.[1427]

Voltage sources are routinely embedded in test fixtures and instruments as stimulus. An automated PCB panel test jig can carry a selectable 3 V and 2.6 V source purely to exercise a low-battery detector, alongside a current sense shunt to read the test current of each board as it is switched on.[552] Electrometer-class instruments include a built-in voltage generator for powering the device under test and for extending resistance measurement, in one case up to 103 volts maximum.[1017] A femtoammeter similarly provides a voltage source able to drive its ADC input, which is what enables resistance measurement on the instrument.[1755]

In simulation the same technique isolates faults: substituting a voltage source directly on a control node such as a regulator's set pin, in place of the surrounding loop, reproduces what the real supply circuit does while removing the loop as a suspect.[260]

## Precision references

A voltage reference standard is a voltage source built for accuracy rather than power delivery, and the market divides sharply. Inexpensive imported units offer only fixed taps — typically 10 volts, 5 volts and 1 volt — with no adjustment and no communications port, whereas adjustable designs allow every digit to be set down to the sixth.[a4Xpsenpd6E]

Such references are also vulnerable to what is connected to them. A multimeter left in ohms mode sources its own voltage and current into whatever it is plugged into, and connecting one in that state to a metrology-grade 10 V standard shifted the standard's output to 10.470 volts.[ZYC763Vx9O8]
