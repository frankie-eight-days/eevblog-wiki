# open collector output

An open collector output is a device output in which the collector pin of the internal output transistor is brought out to the pin with nothing else connected to it inside the chip.[950] The transistor can only pull the pin toward the negative rail; there is no upper device to drive the pin high, so an external pull-up resistor to the desired positive rail is required to establish the high level.[1208][368] This asymmetry is the whole point: the pin's high voltage is set by whatever the pull-up is tied to rather than by the chip's own supply, and several outputs can share one node without contention.

## Contrast with a totem pole output

The alternative is a totem pole output, which has transistors both top and bottom and can actively drive the pin in both directions.[950][1208] An open collector output has no active device that can pull an input quickly up to the positive rail, so the rising edge is left to the pull-up charging the line capacitance.[1208] A comparator such as the LM311 illustrates the practical consequence: with an open collector output it cannot drive an LED directly on the high-going transition, because the output pin can only pull low.[471] Wiring an LED so that it lights on the low state solves the problem, though the saturated output transistor leaves a small drop rather than a true ground, which complicates any calculation that assumes the output goes to zero volts.[941]

## Why designers choose it

### Voltage translation
Because the pull-up need not return to the chip's own supply, an open collector output interfaces directly to a higher-voltage system.[294] The output rating is often specified well above the part's rated supply voltage — 50 V at up to 50 mA drive on a common jellybean comparator, with the output voltage capability standing well above the chip's supply rating.[1464] The same property makes open collector the only workable choice for driving a Nixie tube anode string from a 170 V rail, where the driver must withstand roughly 200 V and a totem pole output is ruled out; an open drain MOSFET output serves the same role.[948] Selecting such a part is a matter of filtering a parametric search on output type, rejecting push-pull and complementary differential entries in favour of open collector or open drain.[948]

### Driving loads that logic outputs cannot
The large open collector driver on a comparator exists so the part can do more than feed digital logic — it can drive a relay coil, a solenoid, or a high-current LED or LED string directly.[1464] Darlington transistor arrays such as the ULN2803 apply the same idea as a dedicated part: a logic-level input, commonly fed from the phototransistor of an optocoupler, driving a beefy open collector transistor rated for hundreds of milliamps, with variants specified around 500 mA and 50 V output, and an integral reverse-protection diode for inductive loads.[1365]

### Wired-OR
Tying several open collector outputs together produces a wired-OR function on the shared node, with any one output able to pull the common line low.[471] This is what allows two comparators to be combined into a window comparator simply by connecting their outputs together, which is why the open collector output is treated as essential in a comparator and why an op-amp — lacking one — is the wrong part for the job.[1464] Combined with a wired-OR output that produces a low-going pulse, the pull-up also sets the recovery behaviour of any timing network hung on the node: the output shorts out a capacitor, which then recharges through the pull-up, in one case a 10 meg resistor, and that RC sets the pulse stretch.[471]

## Pull-up sizing and speed

The pull-up resistor is the dominant design variable. Its value trades static current against rise time, since the resistor and the line capacitance form the charging time constant.[1365][1307] On an I²C bus — an open collector arrangement by definition — a lower pull-up value gives a faster slew rate and therefore more attainable bus speed.[1307] Too high a pull-up leaves the line charging slowly, and if the resulting rise or fall time exceeds a receiver's specification, the consequences are real rather than cosmetic: an input clock that is too slow can drive the receiving chip into a metastable state, producing multiple clock pulses where one was intended and voiding any guarantee about the output.[1365][1208] A 500 ns maximum edge specification against a source already typically producing 500 ns leaves no margin at all; an open collector output feeding such an input is borderline slow by default.[1208][1365]

An optocoupler output is a common instance of this, its phototransistor collector brought out to a pin and pulled up to VCC through a resistor of a few kilohms.[1208]

## Grounding consequence

Because the load current in an open collector arrangement flows into the output transistor and out through ground rather than being sourced from the driving chip's VCC pin, the return current path is on the ground side.[1365] This matters in a multi-board system: current sourced from a supply on one board must return through the ground connection back to the other, which puts the burden on the ground path rather than the power path.[1365]

## Emulating it with a microcontroller

A microcontroller pin can be made to behave as an open collector output without any external part, by either driving the output low or switching the pin to a high-impedance input to release the line.[294] Microcontroller outputs used this way are common enough that an existing LED driven from one can be forced on by shorting out its series resistor, pulling the node low from outside the chip exactly as the internal transistor would.[liWWY5cSs4Q] Where a discrete part is still fitted in preference to the micro's own pins, the reason is usually to gain higher-voltage operation for interfacing to an external system.[294]

The technique has limits. It only works where the load is ground-referenced; a matrix of keypad switches that are not referenced to ground cannot be driven by an open collector output, whether that is a MOSFET inside a typical microcontroller or an external driver transistor, without tying two circuits to a common ground that they may not share.[505]

## Occurrences

Open collector outputs recur wherever a signal must cross a voltage or ownership boundary. The 555 timer's discharge pin is an open collector transistor driven from the inverted output of the internal flip-flop through a resistor.[555] Bus interfaces use a single open collector switching transistor to pull a shared line low, as on the Canon LANC control bus.[297] Diagnostic ports on older Renault vehicles present an open collector output, requiring an adapter to connect a TTL-level FTDI cable.[276] RF detection circuits use a threshold transistor with a pull-up so that the line switches low once signal amplitude crosses a level, which a microcontroller then reads.[368] Instrumentation exposes them as auxiliary signals, such as a go/no-go open collector output on a bench oscilloscope.[474] Small interface boards commonly pair opto-isolated digital inputs with open collector digital outputs.[353][294] A Hakko FX-888 iron drives its indicator from an open collector chip output, and probing that pin reveals a PWM signal rather than a static low, which can be smoothed by adding a 220 µF capacitor across the output.[242]

## Schematic convention

Open collector and open drain outputs have a distinct pin symbol, and marking it on a schematic conveys the output structure to anyone reading the drawing.[952] Its absence from a schematic editor's pin type list is a real omission, since no other graphic style carries the same information.[254]

## Limitations

The open collector jellybean parts share a family of restrictions beyond the output structure itself: inputs whose common mode includes ground but which are not rail-to-rail, and limited speed.[1464] Where those constraints bind, the remedy is to move away from the open collector jellybean class entirely toward a modern push-pull comparator family such as the TLV370x.[1464]
