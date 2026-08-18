# current sense resistor

A current sense resistor is a low-value resistor placed in series with a current path so that the voltage developed across it can be measured and converted back into a current reading.[861][Lk2KRc6Bm4I] It is the element that closes the loop in almost every constant-current circuit — switchmode converters, LED drivers, battery chargers, electronic loads, bench power supplies and multimeter current ranges all depend on one.[110][855][176][1381][221][829] Because the resistance is deliberately small, everything about its use is a fight against the small signal it produces: the tapping arrangement, the tolerance, the temperature coefficient and the voltage it steals from the rail.

## Sizing and value

Values in real hardware span four orders of magnitude, set by how much current flows and how much voltage drop the design can afford. A 5 mΩ four-terminal part thermally mounted onto a heat sink handles the output of an 800 W supply;[1293] a defibrillator's transformer primary is sensed with 68 mΩ;[909] a scope meter uses 0.1 Ω 5% in series with its battery pack;[430] an LED headlamp's high range is set by a 0.33 Ω 0805;[67] a charger's dummy-load leg uses 0.5 Ω;[397] a benchtop lab supply design uses 1 Ω purely because it makes the arithmetic trivial;[221] and a 10 kW laser supply gives each paralleled pass transistor its own 2 Ω power resistor as the sense element.[1381]

Where a controller specifies the resistor, the value follows directly from a datasheet formula rather than from judgement. One switchmode controller sets its sense resistor as 0.3 divided by the calculated peak current, which for a worked example yields 0.4 Ω.[110] That figure is then rounded to a purchasable preferred value — 0.39 Ω from the E24 series — since 0.4 Ω is not a stock part and the value is not hugely critical.[110]

On a board, the sense resistor is often identifiable by physical size alone: it is conspicuously larger than the surrounding resistors because it has to dissipate real power.[67] The other identification route is to follow the current path and look for two thin traces leaving a fat resistor and heading for an amplifier — the tell-tale of a differential amp measuring across a shunt.[861][720]

## Four-terminal connection

The measurement is only as good as the connection to it. A two-terminal resistor's own solder joints and pad resistance sit inside the measured drop, so the correct construction is a four-terminal part: two terminals carry the load current and two carry only the sense voltage, tapped directly off the resistor's own terminals or pads.[173][1293] One energy multimeter uses a proper surface-mount four-terminal current sense resistor rather than "the bent piece of metal basically that almost every other meter uses", with the voltage sense terminals tapping straight off the pads.[173] The equivalent practice on a general PCB is a Kelvin connection to an ordinary shunt.[1174] Where a design offers no four-terminal part and no visible sense tap, that is a recognised shortcoming of the instrument.[Xg_niU86bhI]

The same principle appears inside components. Some MOSFETs are sold with a Kelvin sense pin and a dedicated current-sense pin that tap the die directly, specifically so that an external sense resistor in the source leg can be read without the package's own parasitics corrupting the measurement.[1180]

## Accuracy, tolerance and tempco

Tolerance matters less than stability, because a fixed error can be removed in calibration but a drifting one cannot. A battery emulator uses a pair of 10 Ω Dale resistors in parallel that are only 1% rated, on the reasoning that the gain error is calibrated out later; what they are chosen for is a very low temperature coefficient.[1550] The same requirement drives shunt selection in electronic loads, where the resistor runs hot by design and a poor tempco would make the measured current wander with dissipation.[1023]

## Burden voltage and headroom

The drop across the sense resistor is subtracted from the supply's available headroom. With a 1 Ω sense resistor at 1 A, a full volt appears across it, and that volt adds to the dropout budget of everything downstream — it stacks with the pass element's own minimum drop and must be accounted for at design time.[221] This is the main reason production designs push the value as low as the sense amplifier's input range allows rather than choosing a convenient round number.

The resistor also needs protecting. In one 600 V, 5.1 kW supply a large bridge rectifier is placed across the current sense resistor specifically to clamp it against fault conditions.[814]

## Where it sits in the circuit

In a linear supply the sense resistor sits in the output path in series with the series pass transistor, with its drop tapped off to an amplifier that feeds the current-limit loop.[861][804][272] Regulator ICs of the LM723 generation take that sensed voltage directly on a current limit pin.[804] The same arrangement in reverse defines the constant-current lab supply: converting 0 to 1 V from a microcontroller or pot into 0 to 1 A of limit current is exactly what a 1 Ω sense resistor buys.[221] Output voltage sensing is kept separate and taken right at the output connectors or binding posts so the sense resistor's drop does not appear in the regulated voltage.[814][314]

Switchmode controllers carry a dedicated current sense input pin, and the resistor's placement is identical across step-down and inverting topologies even when the inductor and diode swap places.[110] Fully integrated linear battery-charger chips move the whole arrangement on-die: a built-in shunt, a differential amplifier across it, and a series pass transistor or MOSFET driven by an op amp, with an external programming resistor setting the constant-current value from a datasheet formula.[176] Charge-pump LED drivers use an external sense resistor to hold LED current constant.[855] Motor driver ICs expose the sense resistors as explicit pins — RS1 and RS2 on a dual H-bridge.[326]

An electronic load is the most reduced form of the idea: an op amp, a transistor and a current sense resistor, with the resistor's drop used as the feedback signal.[1381] Source measure units and multi-range loads extend this by switching between several sense resistors with MOSFETs — one design offers a 1 Ω plus two separate 1.0 Ω resistors and parallels four such sections, each with its own shunt and its own pass MOSFET.[607] The same range-switching trick sets the current levels in a multi-mode LED headlamp.[67]

Dedicated high-side current monitor ICs sense across an external resistor and output a current, which a single load resistor converts back to a voltage — a two-external-component solution, though the part's 2.5 V minimum supply rules out low-voltage rails.[87]

## Other uses

Beyond regulation, sense resistors serve as fault detectors and as measurement access points. A soldering station places one in the tip drive so it can flag over-current errors if the tip shorts.[1106] USB output ports in a mains-powered pack each get their own sense resistor.[1483] Multimeters place them in the current ranges behind the diode-bridge clamp and the fuse.[829][1578][173] Chargers use one to measure discharge current where cells are stacked in series by a DC-DC converter.[812]

A sense resistor is also the standard way to get a current waveform onto an oscilloscope. Inserting one in a transistor's emitter leg shows the emitter current directly, which need not match the current in the load it drives.[1409] For side-channel power analysis, breaking a 10 Ω resistor into the ground line of a USB connection makes the supply current visible — done with a 10-bit ADC scope in high-resolution average mode at maximum memory depth, and with care over where the ground clip goes.[1006]
