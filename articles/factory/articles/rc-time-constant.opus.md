# rc time constant

The RC time constant, usually written as the Greek letter tau, is the product of a resistance in ohms and a capacitance in farads, and it sets how quickly a capacitor charges or discharges through that resistance.[626][1406][471] It is a basic building block of circuit analysis: knowing R and C gives a rough ballpark of how long a capacitor takes to charge, without solving the exponential.[626][1406] Its reach is broad — timers, reset circuits, filters, debouncers, sensor bandwidth and control loops all come back to the same product.[1406]

## Definition and the 63.2% figure

One time constant is the point at which the capacitor voltage has risen to roughly 63.2% of the final value.[626][1406] The number falls out of the exponential itself: substituting one into e to the power of minus one produces it.[626] It can also be derived geometrically — take the initial slope of the charging curve, extend it linearly, and the point where the real curve sits at that same time is 63.2% of maximum charge, defining 1T, with 2T, 3T and 4T following at equal intervals along the axis.[1406] The figure is diagnostic in itself; 63.2% appearing in a problem is a reliable sign that an RC or LC transient is involved.[1406]

The discharge curve is the mirror image. Starting from the fully charged value V, after one time constant the voltage has fallen to 36.8%, and that figure carries the same signature as its complement.[1406] The charging expression is one minus e to the power of minus t over RC, where the lowercase t is the elapsed time and the capital T in the denominator is the time constant itself — the two are distinct quantities that share a letter.[471][1406] The discharge expression is identical in form but without the leading one, because it starts at V rather than at zero.[1406]

For practical purposes a capacitor is treated as fully charged after about five time constants.[626] Pushed further, after roughly ten time constants — an order of magnitude — the voltage can be taken as equal to V; in theory it never arrives, but in the real world it does.[1406]

The same analysis holds when the transient does not run to completion. If the capacitor only charges partway before it begins to discharge again, the maximum value in the formula is simply substituted for the actual endpoint; the exponential shape is unchanged, it merely starts and ends elsewhere. This is the normal case in 555 timers and similar RC circuits.[1406]

The instantaneous current follows the inverse curve, starting at a maximum set by the supply and the inevitable series resistance and decaying toward zero.[1406]

## Timing circuits

Using an RC to charge toward a detection threshold is one of the most common applications of a capacitor, and it is the mechanism behind analogue timers generally.[626] In the 555 the timing period works out to 1.1 times RC.[1406] The internal resistor chain places the threshold comparator at two-thirds of the supply, so on a 9 V rail the threshold is 6 V.[555] A 555 kit charging a 3.3 µF capacitor through 200 kΩ produces exactly this waveform, with the output transition occurring as the ramp crosses the comparator threshold.[555] A one-shot built with a timing RC of around five seconds holds its output LED on for about that long after power is applied.[1746] Tying the discharge and supply pins together and placing the timing resistor elsewhere lets the RC charge immediately, but when the threshold is crossed the open-collector discharge transistor turns on into what is effectively a crowbar short to ground.[1746]

Timing precision is rarely the point. For an overload indicator whose only job is to light an LED for a noticeable interval, the exact exponential is irrelevant — half a second or a full second are equally acceptable, so the plain R times C figure is sufficient and a value of about one second is a sensible target.[471]

## Digital reset and logic inputs

RC time constants are used constantly in digital work, most visibly on a microcontroller reset pin, where the RC holds the processor in reset for some milliseconds while the supply rises so that the part gets a clean start rather than doing funny business at the edge of its operating range.[1406] The consequence is a very slowly ramping edge, and ordinary logic gates do not tolerate slow input transitions.[1611][1406] The remedy is a Schmitt trigger input to square up slow rise and fall times — the 74HC14 is preferred over a plain 7404 inverter for exactly this reason.[1611]

## Switch debouncing

Placing a capacitor directly across a switch converts the contact bounce into a clean exponential rise of the classic RC form.[961] With a 330 µF capacitor and a 5k6 pull-up the resulting edge shows no contact bounce at all, because the instant the switch closes it shorts out the capacitor.[961] That shorting is itself the problem: a second resistor in series with the capacitor limits the discharge current, but it must be small enough to discharge quickly while still being chosen against the timings of the specific switch, and it then appears in series with the pull-up for the charging path, which interacts with the Schmitt trigger thresholds downstream.[961]

## Sensor and detector bandwidth

Where a time constant defines a bandwidth rather than a delay, the same arithmetic sets the response. The pyroelectric element in a PIR sensor is itself a capacitor, and together with a gate resistor it forms a time constant of about one second in typical parts — deliberately slow, since the sensor should respond only to the gradual thermal changes produced by people moving, not to wide-bandwidth events.[275]

A peak detector's droop is governed by the same rule. With 100 nF across 10 kΩ the output decays back to zero in about 5 ms, which is the expected result from the rule of thumb of five times RC, and that decay period is the effective reset time of the detector.[490]

A condenser microphone capsule polarised at 60 V to 90 V charges through gigohm-scale resistance into a few picofarads.[609] Taking 10^9 ohms and 50 pF gives a 50 ms charge time constant, which in turn corresponds to a low-frequency electrical roll-off pole of a few hertz.[609] The value is unrealistically low as a physical resistance but is what microphone manufacturers use.[609]

## Time constants inside feedback loops and filters

An RC in a control path is not free. In a lab supply's output stage a 22 µF capacitor with about 2 kΩ of total series resistance forms the turn-on time constant that determines how the output ramps up.[224] Because that network sits inside an active feedback loop driven by an op-amp, the capacitor charges faster than the bare RC figure would predict — op-amp action drives the node rather than the source resistance alone.[224] Remove the RC from the feedback loop entirely and the output switches on instantly.[224]

The trade-off is sharpest in a PWM-to-analogue filter, where the same RC that smooths the ripple also sets the settling time. Increasing the time constant to reduce ripple pushes the settling out to roughly 50 ms before the output begins to level off toward its correct average.[225]

The behaviour also shows up in latching and indicator circuits. In a soft latching power switch a capacitor charges from zero at a rate set by the RC — plus whatever base current flows into the NPN transistor — holding the node high for something like half a second before the transistor switches on; holding the button down makes the circuit oscillate at the frequency set by that RC, and reducing the capacitor from 47 µF to 10 µF speeds the oscillation up correspondingly.[262] In a soldering iron modification, adding a 220 µF capacitor across the open-collector output and lowering the LED drop resistor to 1 kΩ both change the time constant, altering how long the indicator LED stays lit.[242]

## Component tolerance and the ceramic capacitor trap

RC timing is not accurate, because capacitors are not high-tolerance devices.[626] Beyond tolerance, ceramic capacitance is voltage-dependent, and not only with DC bias — applied AC voltage has an effect too, so the deviation is not confined to slow RC timing but extends to filtering, where it can be quite critical depending on signal level.[626] Picking a relatively stable dielectric such as X7R or X5R for a timing network is the obvious defensive move, but it does not eliminate the effect.[626]
