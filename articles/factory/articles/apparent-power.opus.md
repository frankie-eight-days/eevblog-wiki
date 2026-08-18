# apparent power

Apparent power, designated *S*, is simply the voltage multiplied by the current in an AC circuit, expressed in volt-amps (VA) rather than watts.[1730] It diverges from real power the moment a load contains reactance, because the resulting phase difference between voltage and current means the product of the two no longer equals the heat actually dissipated.[1730] The distinction matters everywhere in AC power distribution, power supply design, and mains-powered equipment, and it governs how transformers and supply infrastructure are sized and how industrial customers are billed.[1730]

## Definition and the power triangle

Apparent power is voltage times current, both AC RMS, and its units are VA precisely because that is literally what the quantity is.[1730] Where real power is computed as I²R, apparent power is I²Z or V²/Z — the total impedance, including both the actual resistance and the imaginary reactive component, rather than the resistance alone.[1730]

The relationship between the three powers is a right triangle. Real power *P* lies along the horizontal axis; the phase angle theta between voltage and current opens up from it; and the hypotenuse is the apparent power vector *S*, which is V times I and is a quantity that can actually be measured.[1730] The vertical leg joining them is reactive power *Q*, in VAR.[1730] By inspection, S equals the square root of P² plus Q².[1730] Reactive power uses the same V times I product as apparent power but carries a sine theta term, where real power carries cos theta.[1730] Power factor follows directly: it is real power divided by apparent power.[1730]

As phase angle increases, the apparent power vector extends upward and apparent power increases, whether the reactance is inductive or capacitive — the sign of the angle makes no difference to the magnitude.[1730]

## Apparent power is not dissipated

In AC circuits, loads, transmission lines, generators, and transformers, real power is only ever dissipated in resistances — never in capacitances, never in inductors.[1730] Apparent power therefore has no physical reality in the load itself and is not dissipated there.[1730] The reactive component is imaginary: it is not dissipated anywhere in the circuit or product.[1730]

An oscilloscope demonstrates the gap concretely. At 240 V RMS and roughly 280 mA RMS, the product of voltage and current is about 67, but that reading is 67 VA, not 67 W; the true power drawn is 30 W.[1730] The back label rates the instrument at a maximum power of 50 W, so a naive voltage-times-current calculation appears to exceed the rating — the discrepancy is entirely the difference between apparent and real power.[1730] The cause is that the instrument uses a switching power supply with no power factor correction circuit, which introduces the voltage-current phase difference.[1730]

## Upstream consequences

Although reactive power does not exist as dissipated energy in the load, it manifests upstream in the power delivery system as apparent power in volt-amps, and that has flow-on effects as real I²R copper losses in the rest of the system.[1730] The current has to be supplied from the power station regardless, and every conductor along the way — the mains wiring in a house, and even the power cord connecting to the product — has resistance and therefore real copper losses measured in watts, not in VA.[1730] In an industrial setting the high circulating current forces larger copper conductors to be specified.[o2NxHu5Bsnk]

This is why transformers and similar components are rated in VA rather than watts: the rating must account for the phase difference and the apparent power the device has to pass.[1730] Non-sinusoidal current waveforms compound the problem. Peak current spikes drawn by switching supplies are real and must come from the mains and from the entire distribution system back to the generator, they push apparent power above real power, and they bear directly on the fusing design for a product.[1413] Phase lead and lag are not the whole story either — harmonic power factor is the more serious contributor.[1285]

## Billing

Residential customers in most countries, including Australia, do not pay for apparent power; they are billed for true power in kilowatt-hours only, and the domestic energy meter is designed to measure that real component.[1446][1505] The meter installed even at a commercial office rate may be a real-power watt meter rather than an apparent power meter.[1191] Industrial and some commercial supplies are the exception: where the provider must build out extra capacity to carry the current, the charge is levied in VA, kVA, or MVA.[1730][1413][o2NxHu5Bsnk][971] The energy distribution and generation system still has to be sized to deliver the apparent power whether or not the customer is charged for it.[971]

Because reactive currents flow into the grid on one half cycle and back out on the next, and because domestic inductive and capacitive loads tend to cancel one another and pull the supply closer to a resistive load, the residential situation largely evens itself out and providers generally do not meter power factor at all.[o2NxHu5Bsnk][1191]

This billing arrangement is what defeats plug-in energy saver devices, which are typically nothing more than a 3 µF power factor correction capacitor connected across the mains.[1191] Correcting power factor has legitimate purpose for an inductive load, but with real-power metering it saves nothing, and one such device measured under test made matters worse: power factor dropped to 0.22 and the apparent power drawn rose substantially.[1191]

## Measured examples

Typical figures show how far the two quantities separate in practice:

- An oscilloscope acquiring data drew 54.3 W at 247 V and about 256 mA, giving 63.3 VA and a power factor of about 0.86; switched off, it still drew 6.5 W, and with power factor now down to 0.32 the apparent power rose to 20.5 VA.[164]
- An energy saver device measured about 9.1 W real against about 32 VA apparent, a power factor of roughly 0.57.[1191]
- A whole-house audit late at night, with everything switched off, showed 109.4 W of real power against 642 VA — some 2.7 A of current that has to come from somewhere, though only the 109.4 W is billed.[1505]
- A washing machine on standby drew 0.4 W of true power, with the reactive component at 16 VAR.[1505]
- A monitor's DC plug pack consumed 300 mW with no load, but 4 VA apparent.[971]
- A clamp current probe measurement gave 175 mA at 241.5 V for 42.26 VA, against 23.8 W of real power being paid for.[1413]

## Instrumentation

Measuring apparent power requires only a voltmeter and an ammeter on the load and a multiplication of the two readings, but separating real from apparent power requires an instrument that multiplies voltage and current in phase.[1730][1446] Bench power analysers handle the full set, measuring voltage, current, phase angle, real power, and apparent power across multiple ranges, along with inrush current.[589] Some mains-connected products carry the necessary sensing hardware — a current transformer or Hall effect sensor plus voltage sensing — which makes real and apparent power measurement possible even when the user interface exposes only voltage and current.[1507]
