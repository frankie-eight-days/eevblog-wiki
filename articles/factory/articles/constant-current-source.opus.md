# constant current source

A constant current source is an active circuit that forces a fixed current through whatever load is connected to it, instead of presenting a fixed voltage and letting the load decide how much current it draws.[1688] It is the dual of the voltage source, and although textbook DC theory introduces it alongside Thevenin and Norton equivalents, that treatment is theoretical rather than practical.[1688] In real hardware it appears everywhere: biasing precision references, driving LEDs and laser diodes, measuring resistance and capacitance, and setting the operating points inside almost every analogue integrated circuit.[908][853][555]

## What it actually is

A current source cannot exist on its own. Drawn practically, it is a voltage source followed in series by active constant current circuitry, and the circuitry has to be active — no arrangement of passive components will do it.[1688] Adding external circuitry to an ordinary voltage source is precisely how one is built.[1688]

The behaviour is easiest to see at the extremes of load resistance. If a source is designed for 1 amp, then shorting its terminals gives 1 amp through 0 ohms; the current stays where it was set even as the load resistance changes.[1688] A short circuit is the best possible load for a constant current source, the exact opposite of a voltage source, where shorting the output is a very bad idea.[1688]

## Compliance voltage

The voltage source behind the current circuitry sets the limit on what the source can achieve, and that limit is called the compliance voltage.[1688] It can be thought of as the supply rail available to the circuit, and it is the maximum voltage the source will put across a load.[1688][908] The constant current circuit is not a voltage multiplier: with only 5 volts of compliance, no more than 5 volts can appear across the load, and beyond that point regulation is lost.[1688]

Compliance also has to be matched to the load, not merely to the current. A 1 microamp source on a 100 volt supply still cannot bring a Zener diode into conduction, because the current itself is insufficient regardless of how much compliance is available.[908] Conversely, an IEPE accelerometer needing a few milliamps also demands compliance somewhere between 18 and 30 volts.[1443] Instrument specifications state the figure as an open circuit compliance voltage — 180 volts in the case of one TENS-style stimulator.[1471]

## Current source and current limiter

The same circuit can be read two ways. A bench power supply is a constant current source as well as a voltage source; which behaviour is observed depends on the application and the load.[1688] The current knob is normally thought of as a limiter, and that view and the current-source view describe the same hardware.[1688] The LM317 makes this explicit: with a shunt resistor between output and adjust, and the adjust pin tied to the output, the classic adjustable voltage regulator becomes a constant current source, or a current limiter, depending on the point of view.[1688]

## Circuit implementations

The LM317 arrangement is the minimal discrete approach — the regulator, a couple of resistors and a capacitor, with the resistor tied between the output pin and the adjust pin — and it is good for around a watt.[992]

The LM334 is a purpose-built two-terminal part in a TO-92 package that programs its current with a single resistor. It runs from 1 volt to 40 volts, covers 1 microamp to 10 milliamps, and has 3 percent initial accuracy.[222] Temperature is the limiting factor: a crude two-transistor source built from jelly bean 2N3904s drifts about 15 percent over a 50 degree C rise, roughly 0.3 percent per degree C, and the LM334 has essentially the same temperature coefficient.[301]

Higher performance comes from op-amp feedback. The improved Howland current pump uses an op-amp, five resistors and a voltage reference to source a few milliamps up to tens of milliamps for driving an LED or a sensor, where efficiency is not a concern.[xUKf-4rv_sQ] Its principle is that a difference amplifier holds a constant voltage across a resistance, and a constant voltage across a resistor is a constant current — so the current through a series load stays at 1 mA regardless of the load value.[xUKf-4rv_sQ] The same idea scales up: holding a reference voltage of 1.25 V across a four-terminal current shunt yields 1 amp, with essentially all of it flowing through a high-gain Darlington NPN pass device that needs only a milliamp or two of base current.[567] A power FET in an op-amp feedback loop, with a DAC setting the current and an ADC monitoring the voltage, is the standard arrangement for a laser diode driver.[bg6QsTT0Plw] A 10 kW argon ion laser supply goes further and sets the current for each parallel pass transistor individually with its own op-amp, rather than paralleling the transistors behind a single sense resistor.[1381]

A JFET above a certain drain voltage behaves as a constant current source in its own right, and that saturation region is where the device should be operated — below it, transconductance collapses.[611] Whatever generates a constant current across a resistor is a current source in effect: a 1.25 V bandgap reference across a 10 K resistor sets 125 microamps, and because base current contributes nothing, the same current flows in the downstream branch.[329]

## Inside integrated circuits

Constant current generators are ubiquitous inside analogue chips. A typical comparator may contain three or four of them.[555] In the 555 timer they bias the trigger comparator circuitry and feed the flip-flop, and the current limiting they provide removes the need for a series resistor in the cross-coupled latch.[555] Constant current generators are frequently arranged as current mirrors, with the current in one branch set equal to the current in another.[555] The LT3080 uses an internal 10 microamp constant current generator in place of the LM317's internal voltage reference; that current must flow out of the set pin into the programming resistor, and it contributes an offset error at low output settings.[222] A device whose quiescent current is held by an internal current source shows the same quiescent draw across a 25 V to 450 V input range — 7.5 microamps typical, up to 14 microamps worst case over temperature.[1285] Current mode logic biases its transistors from constant current sources to prevent saturation, giving extremely rapid switching and high noise immunity despite low logic levels.[867]

## Biasing voltage references

A high-stability Zener reference needs a known constant current through it to produce a stable voltage, which is why reference circuits so often power the Zener from a current source — it makes the design far simpler than the resistor-fed case, where supply voltage, resistance and temperature all interact.[908][210] A DC voltage standard sets 6.5 milliamps through its Zener via an adjustment pot, trimming the current until the desired voltage appears; with the diode held at constant temperature by an internal heater and a constant current flowing, stability is very high, even though the diode's initial tolerance may be 2 percent.[210]

## Measurement applications

Four-wire resistance measurement is done by passing a known constant current through the unknown resistance via drive leads and measuring the voltage drop with separate sense leads, so the drop along the drive leads does not appear in the result.[317] This can be done manually with a current source and a multimeter, or automatically by an instrument such as the HP 3478A.[317] A practical fixture is a low-value resistor with the current leads and the sense wires landed directly on the resistor's contacts.[133]

Inside a multimeter, the ohms ranges work by pushing a constant current out through the same switched range network used for DC and AC volts.[853] Capacitance measurement uses the same trick differently: a constant current output charges the capacitor and the chipset times how long it takes to reach a threshold, from which the capacitance follows.[853] The linear voltage ramp that a constant current produces across a capacitor is also the basis for deriving the half-CV-squared energy relationship.[1618]

Current sources also serve as calibration stimuli. Feeding a precision current adapter 99.9 nanoamps and reading 99.7 confirms the correct sense resistor is fitted, and repeating the check on each range verifies the rest.[133] Production test does the same against programmed pass-fail limits, so that tweaking the source current off nominal flags a failure.[Ux7WdK6oym4] A reference voltage on a test fixture can generate the constant current itself, removing the need for a separate bench current source.[552] One limitation of series-connecting boards under test to share a single current source is a common output ground, which prevents the current input from floating.[552]

## Driving loads

LED strings are the classic application.[1688] An LED strip salvaged from an LCD television can be driven directly from a laboratory current source at 10 milliamps with the compliance raised to cover several volts per LED in the series chain.[916] Many LED assemblies include their own current source behind the emitter.[338] A charge-pump LED driver achieves the same result by switching at some frequency with a current sense resistor setting the level.[855] A constant current feed can even be PWM-dimmed with a 555, although the usual approach is to PWM a voltage source and set the current with a dropper resistor.[392]

Battery charging exploits the source's indifference to load voltage. In a 15 minute charger, the current comes from a DC-DC converter operating as a current source into a MOSFET totem pole; when a body diode adds its 0.6 volt forward drop, the node rises to 2.2 volts and the charge current is unaffected.[811] The consequence is that the charge cannot be stopped by pulling the MOSFET gate low — the output of the constant current converter itself must be turned off.[811]
