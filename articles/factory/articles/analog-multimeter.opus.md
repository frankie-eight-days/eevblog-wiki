# analog multimeter

An analog multimeter, also called a VOM (volt-ohm-milliammeter), is a general-purpose test instrument in which a moving-coil meter movement and a needle indicate voltage, current and resistance against printed scales.[1067][1013] It was the standard bench and field meter for most of the twentieth century, and remains in limited production today, though digital multimeters outperform it in nearly every measurable respect.[1067][1580] Its defining characteristic — and the source of both its main weakness and its few remaining advantages — is that the needle is deflected by current drawn out of the circuit under test.[1067]

## Operating principle

The meter movement takes its energy from the circuit being measured, so no battery is required to read DC volts or current.[1013][633] A battery is needed only for the resistance ranges, and for the capacitance ranges where those exist — typically a single AA or C cell, sometimes a 9 V battery alongside it.[1013][633][1362] This makes the instrument self-sufficient in a way a digital meter is not: a vintage 30 V battery can be measured on the 60 V DC range of the very meter it would otherwise be powering, with no external supply involved.[634]

Everything between the input jacks and the movement is passive: a range switch, a bank of precision series and shunt resistors, and the movement itself.[1013][686] There is very little else inside.[686]

## Sensitivity and ohms per volt

Analog meter sensitivity is specified in ohms per volt, and it is the reciprocal of the full-scale current of the movement.[1067][1580] A 50 µA movement gives 20,000 ohms per volt: one volt divided by 20 kΩ is 50 µA, so 50 µA must be pulled from the circuit to drive the needle to full scale.[1067] Twenty thousand ohms per volt is the typical figure; 50 kΩ/V is a good meter and 100 kΩ/V a superb one, and instruments above 100 kΩ/V are essentially unknown — beyond that point the only route to higher input impedance was a FET-input or vacuum-tube instrument.[1067][633] Cheaper meters ran far lower: 10 kΩ/V was a technician's budget specification, and older instruments went down to figures like 4 ohms per volt.[416]

Because the series resistance scales with the range, the input impedance is not a fixed number but the sensitivity multiplied by the range in volts.[1013] A Triplett 630-NA at 10,000 ohms per volt presents 120 kΩ on the 12 V range, not the 10 MΩ a digital meter would offer.[1747] The loading error this produces can be severe: measuring across a 100 kΩ leg of a divider, a 200 kΩ meter impedance parallels it down to 66.67 kΩ and drags the reading to 0.4 V.[1067]

The relationship inverts at the top of the range set. A 20 kΩ/V meter on its 1,000 V range presents 20 MΩ — twice the input impedance of a standard 10 MΩ digital meter — and the highest-sensitivity instruments do better still.[1067] There are measurements where the low impedance itself is the point: probing a reverse-biased Schottky diode with a 10 MΩ digital meter reads almost the full supply voltage, while the loading of an analog meter reveals what is actually happening.[1747]

## Reading the scale

Accuracy depends on the operator's eye position. Better meters carry a mirrored strip along the scale; the reading is valid only when the needle is lined up directly over its own reflection, and viewing at an angle introduces parallax error.[1067] Meters without a mirrored scale offer no such correction.[673] The zero must also be adjusted, and re-adjusted whenever the instrument's orientation changes.[633][1067]

Resolution is limited by the width of the needle. A skilled reader can resolve a fraction of a needle width, but no amount of technique gets past the second decimal place — the instrument is adequate for establishing that a value is in the right ballpark, not for the last digit.[1067]

## Resistance measurement

The ohms scale is non-linear, crowding high resistances into the top end of the arc.[1013] On a Simpson 260 the maximum scale factor is 10 k, so a 100 kΩ measurement sits well up the compressed part of the scale and 1 MΩ sits at the extreme end, where half a needle width of misreading is a 10 % error.[1067] Resistance measurement is where the analog meter is least defensible against a digital one.[1067]

Negative voltages drive the needle hard against the backstop, which can damage the movement or bend the needle; better instruments provide a polarity reversing switch instead.[1067] Some, such as the Triplett 630-NA, add a range doubler that multiplies the effective range rather than adding switch positions.[1067]

## Protection and failure modes

Analog meters have no MOVs or PTCs.[1067] Overload typically destroys the movement, the diode protection, or the range resistors outright, and connecting one to mains-level circuits is inadvisable.[1067] Current ranges are fused, often with HRC fuses, and many instruments include a mechanical thermal overload cutout that is simply reset after a mistake.[1067][633][634]

High-voltage ranges are a genuine capability of the class. Dedicated 2,500 V ranges are common, fed through a high-value series resistor — one instrument uses a 40 MΩ part for its 2.5 kV range — and some meters reach 5 kV.[1013][1362][1580] That range is directly useful where a digital meter cannot follow, such as measuring the roughly 2,400 V output of an electric fence controller.[1277]

## Construction

Point-to-point wiring is typical of the class and the era, with range resistors and a custom moulded plastic base rather than a motherboard.[686] Better examples use single-board construction with dual-contact wafer range switches, the movement tied directly to the input circuitry, and a well-implemented reset circuit.[634] Input jacks are a common weak point: split jacks press-fitted into a plastic surround are less satisfactory than solid ones.[634]

## Notable instruments

The Simpson 260 is the archetype of the American VOM and was produced in enormous numbers.[1067][559] Simpson also built the 269, an ultra-high-sensitivity volt-ohm-microammeter at 100 kΩ/V with a 16 µA full-scale movement and ranges to 1,600 and 4,000 volts.[899] The Triplett 630-NA is a 10,000 ohms per volt instrument regarded as the best of the classic American designs on construction grounds.[1747][634] From Germany, the Metrawatt Unigor A43 is a comparable classic.[633][634] AVO, dating from around 1923, produced the Universal AVO Meter; the Model 7 Mark II is the best-known variant, physically very large, with capacitance measurement and electromechanical cutout protection built in.[1097] Sanwa was the leading Japanese maker of the era and continues with digital instruments.[673]

The Chinese type 500 platform has been in production since the 1960s, and its current MF500 variant is externally near-identical to the original, retaining the same zero-ohms adjustment pot arrangement and the dedicated 2,500 V range, at 20 kΩ/V.[1362] Micronta, the Tandy/RadioShack house brand, sold multi-range 20 kΩ/V instruments such as the 22-201U at pocket-money prices.[Gq8ly6TQQu8][54][riBwRC_CaAA]

## Capacitance and dynamic measurements

Built-in capacitance ranges were rare and notable before the 1990s; a 100 kΩ/V Dick Smith instrument carrying a couple of capacitance ranges was considered groundbreaking, and the usual alternative was a dedicated capacitance meter or an LCR bridge.[951] The classic analog technique of judging capacitance from the needle's kick and decay requires calculating from the decay factor of the movement and has no advantage over a digital capacitance mode.[1067]

The needle is often claimed to be superior for observing changing signals. Tested against a fast-responding bar graph on a digital meter with a 250 mV peak-to-peak sine superimposed on 4 V DC, the digital bar graph tracks the variation better than the movement does.[1067] The movement's sensitivity to small currents does have demonstrative uses: a 60 µA full-scale analog meter in current mode registers a clear needle jump from a bare LED illuminated by a xenon flash, showing the photoelectric effect directly.[716]

## Higher-impedance variants

Vacuum-tube voltmeters were the contemporary alternative where the loading of a passive movement was unacceptable. Being active, a VTVM presents a high input impedance comparable to the 10 MΩ of a modern digital meter.[1013] As tubes were phased out through the 1970s and 1980s the same role passed to the FET VOM, a FET-input analog instrument.[1013][1067] These sat at the top of the market: in 1985 a precision FET analog multimeter listed at $49 against $10 for a 10 kΩ/V technician's meter and $59.50 for an entry-level digital.[416]

## Current status

Analog multimeters are still manufactured, both by established makers such as Triplett and by low-cost Asian producers.[1580] The cheap modern examples are functional but crude: one recent Chinese instrument at around US$17 provides a printed 20 kΩ/V scale and integrated protective caps over its current and high-voltage inputs, while its resistance function is effectively a go/no-go test despite carrying a proper scale.[1580] Digital meters beat analog ones in practically every aspect — resolution, resistance measurement, polarity handling, capacitance, and response to changing signals — leaving the low-impedance loading trick and the high-voltage ranges as the narrow cases where an analog instrument still earns its place.[1067][1747][1277]
