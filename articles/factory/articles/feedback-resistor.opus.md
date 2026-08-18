# feedback resistor

A feedback resistor is the component that returns a portion of a circuit's output to one of its inputs, and in doing so sets the circuit's behaviour rather than merely trimming it. In an operational amplifier it converts an enormous, temperature-dependent, essentially unusable open-loop gain into a precise closed-loop gain fixed by a resistor ratio.[600] In a regulator or DC-to-DC converter the same idea sets the output voltage: the feedback divider is what the control loop compares against its internal reference.[110][158] Because the feedback element sits inside the loop, its value influences not only gain but offset error, leakage, noise, and stability, which is why its choice is rarely arbitrary.[479][24][95]

## Setting gain in an op-amp

Negative feedback tames the raw differential gain of an op-amp so it can be used as a practical single-ended amplifier.[600] In the non-inverting configuration the feedback resistor RF returns to the inverting input, with a second resistor R1 from that node to ground, forming a divider that feeds back a fraction of the output.[600] The gain is RF divided by R1, plus one — the plus one being the term beginners drop.[600] With a 9K feedback resistor and a 1K resistor to ground, the ratio is nine and the gain is ten, so 1 V in gives 10 V out.[600]

The inverting configuration uses the same feedback resistor but drives the signal in through a series input resistor to the inverting pin.[600] Here the ratio alone sets the gain: a 10K input resistor with a 100K feedback resistor gives a gain of ten, so a 2 V peak-to-peak input produces 20 V peak-to-peak at the output.[600] Making the main feedback resistor larger than the input resistor is what produces gain greater than unity in this topology.[HbMnQdRzD8A]

The feedback resistor is also the physical path that makes the virtual ground work. The op-amp drives its output to whatever voltage is required to hold the inverting pin equal to the non-inverting pin, and the only route it has for doing so is through the feedback resistor.[600] Current cannot flow into the high-impedance input pin, so the current established by the input resistor must flow up through the feedback resistor and be sourced or sunk by the op-amp's output stage.[600] With a 1 V drop across a 1K input resistor and a 10K feedback resistor, that current develops ten times the voltage across the feedback element, which is where the gain physically comes from.[600]

## Value selection: offset, bias current and stability

Input bias current has to flow somewhere, and in an inverting stage it cannot flow through the input resistor, because the virtual ground puts zero volts across it regardless of its value.[479] All of the input bias current therefore flows through RF.[479] Since useful gains of ×5, ×10, ×50, ×100 or even ×1000 demand a large RF, even a very small bias current across a large resistance produces an offset error stacked on top of the specified input offset voltage.[479]

The standard remedy is a compensating resistor in the other input's path, chosen so the equal and opposite bias currents at the two inputs cancel.[479] Its value is RF in parallel with R1 — the reason an otherwise unexplained resistor so often appears in series with the non-inverting input in published circuits.[479] The same compensating trick applies to the non-inverting configuration by inserting a resistor of matching value in the feedback path.[479]

High-impedance feedback resistors bring two penalties at once: bias-current-induced offset, and stability problems.[xUKf-4rv_sQ] Much of the time modest ordinary resistor values are perfectly adequate.[xUKf-4rv_sQ] Where a closed-loop regulator refuses to settle, the feedback resistor values are a legitimate place to intervene, since lowering them changes the pole response of the loop — though that alone is not always enough to stabilise a marginal design.[95] A simulated linear regulator loop running a gain of 3.7 set by 10K and 27K feedback resistors, into a 10K nominal load with 100 nF of output capacitance, is representative of the scale of values involved in such experiments.[95]

Chopper amplifiers impose their own constraint. The switching that gives them their very low DC offset also injects charge, and that charge injection is reduced by lowering the input impedance and the feedback resistors.[24] For maximum performance from a chopper amp these should be made as low as practical.[24] Chopper amps also recover slowly from overload, on the order of five to ten milliseconds.[24]

## Transimpedance and current measurement

In a transimpedance amplifier the feedback resistor is the gain element itself, converting input current into output voltage; a photodiode front end is the classic case, needing little more than the op-amp and its feedback resistor.[1755]

In a picoammeter the feedback resistor also sets the range, and it interacts badly with input offset voltage. The amplifier's offset VOS is multiplied by the term RFB plus RS, divided by RS, where RS is the source resistance.[406] On a 100 microamp range with a 10k feedback resistor and a 10k source resistance, that term evaluates to two, doubling a 100 microvolt offset.[406] Switching to the 100 nanoamp range replaces RFB with a 1 meg resistor, and the multiplier grows accordingly.[406] Because the range switch is carrying these feedback resistors, its contacts sit directly in the feedback path and must be extremely reliable and extremely low noise — gold leaf spring contacts, in the case of instruments of that class.[406]

## Feedback resistors used to defeat leakage

In a peak detector the feedback resistor can be repurposed to eliminate a leakage path rather than to set gain. Taking feedback from the capacitor side of the storage diode forces the voltage across that diode to zero while the peak is held, and a diode with zero volts across it passes no leakage current.[490] The residual leakage that does exist flows harmlessly through the feedback resistor and is negligible.[490] With the diode leakage removed, op-amp input bias current becomes the dominant error, and modern parts can bring that down to the femtoamp region.[490]

## Regulators and switching converters

For a DC-to-DC converter the output voltage is set by a feedback divider into the internal comparator or error amplifier. A common form is Vout equal to the internal 1.25 V reference times one plus R2 over R1, which rearranges to R2 equals Vout over 1.25, minus one, times R1, letting any convenient R1 be picked first.[110] Choosing R1 as 10k and R2 as 110k gives 15 V at 100 mA maximum from the worked example; a related data sheet configuration produces 28 V at 175 mA.[110] The same two feedback resistors reappear unchanged in the step-down configuration, where only the inductor and diode swap positions.[110] Other controllers use a different reference — 0.8 V rather than 0.6 V, for example — which makes otherwise similar parts non-substitutable because the divider equation no longer works out.[1475]

The LM317 works the same way, with two resistors setting the output; series combinations of E12 values are a normal way to hit an awkward target, such as 330 ohms plus 33 ohms to reach 363 ohms against a calculated 360.[158] The adjust-pin current term in the LM317 equation is customarily left out of the calculation because it is insignificant unless the feedback resistors are high in value.[158] In a simulated tracking pre-regulator a 1 meg upper feedback resistor and a 10k lower one place the ceiling of the converter's range very high, and deliberately lowering the upper resistor turns the divider into a safety limit that prevents the converter exceeding a chosen voltage.[260]

Feedback resistors around a switching supply also serve as monitors rather than setters. In an electric fence controller the feedback resistors after the step-up transformer's output diode allow the charge voltage on the capacitor bank to be monitored, so the bank can be fully charged to its eight joules within the cycle period.[1292] Adjusting a boost converter's feedback resistor is a plausible mechanism for producing a user-adjustable supply rail from a fixed-topology converter.[1596]

Feedback divider topology can also create dependencies between rails. In one instrument's supply the feedback resistors for the negative 15 V rail are referenced to the positive 15 V rail rather than to ground, so the negative rail is not independent and cannot be correct unless the positive rail is set correctly first.[804]

## Positive feedback

Returning the resistor to the non-inverting input instead produces hysteresis rather than controlled gain. Adding a 15K resistor from the output back to the non-inverting input of a comparator built with 1K and 1K around it introduces hysteresis, turning a plain comparator into a Schmitt trigger.[941] The exact calculation becomes awkward once the divider, an LED, and an open-collector output are all in play, but the order-of-magnitude choice of feedback resistor relative to the divider resistors is what matters in practice.[941] This resistive positive feedback is the discrete analogue of the Schmitt action built into logic parts such as the 74HC14.[941]

## As a diagnostic in reverse engineering

Recognising standard building blocks makes the feedback resistor a useful landmark when tracing an unknown board. An op-amp with no visible feedback signals a tracing error, and identifying the likely feedback resistor — R49, in one differential probe — quickly resolves ambiguous traces disappearing under a component.[1415] The absence of feedback resistors is equally informative: a suspected op-amp circuit that shows only an RC filter and no feedback network is almost certainly not an op-amp circuit at all, which saves pursuing candidate part numbers down a dead end.[1541]

Feedback resistors also reveal internal architecture in integrated parts. In a multimeter chip set, on-chip feedback resistors around an internal op-amp implement a non-inverting ×10 gain stage, sometimes alongside a selectable chopper amp reached through the internal multiplexer for the low-offset precision needed at higher resolutions.[853]

## In composite and control loops

A composite amplifier places a buffer inside the feedback loop of a precision front-end amplifier by moving the feedback resistor's far end from the front-end's own output to the buffer's output.[1609] The output voltage is then determined by the precision input amplifier rather than the buffer, so the buffer's offset voltage is compensated away by the front-end's gain and collapses to zero.[1609]

In a PWM-based supply control loop, the feedback resistor is often chosen simply to make the arithmetic convenient — changing it to 10K to give a gain of two in an amplifier fed from a 3.3 V PWM signal, for instance.[225]
