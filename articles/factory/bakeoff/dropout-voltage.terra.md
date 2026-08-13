# dropout voltage

Dropout voltage is the minimum voltage difference required between a regulator’s input and output for it to maintain output-voltage regulation; below that headroom, the output falls out of regulation rather than remaining at its set value.[158][1147] It determines the lowest usable input voltage for a required output and therefore affects supply-range design, battery-capacity utilisation, dissipation, and ripple rejection.[158][1331][1116]

## Input-output headroom

For a linear regulator, the required minimum input voltage is the desired output voltage plus the applicable dropout voltage.[158][222] A 5 V regulator with a 2 V dropout requirement, for example, needs at least 7 V at its input to regulate; a 5 V output with a 1.6 V worst-case dropout requirement needs 6.6 V at the regulator input.[158][722][222]

The term ordinarily describes an input-to-output differential, not the absolute input voltage.[158] It may also be specified operationally as the point at which the output has fallen by a defined amount; one LM317 characterization uses a 100 mV output reduction as the dropout criterion.[158] The output does not necessarily disappear immediately at dropout, but it no longer holds its specified regulated voltage and can become unstable.[1147]

Voltage references may impose the same practical requirement for input headroom even when their documentation does not label it dropout voltage.[500]

## Dependence on operating conditions

Dropout voltage is not a single fixed property independent of conditions: it varies with output current and temperature.[158][722] Regulator data commonly provide curves of input-to-output differential voltage against temperature, with separate curves for load currents ranging from light load to rated maximum current.[158] A design must use the applicable worst-case value at its maximum load and expected junction temperature rather than a typical or lightly loaded figure.[222][224]

For example, an LM317 operating at 25 °C may require approximately 1.5 V dropout at 20 mA and about 1.75–1.8 V at 500 mA.[158] A measured LM317 example produced 3.26 V from 4.803 V at 20 mA, corresponding to 1.54 V dropout.[158] A regulator specified at 0.2 V dropout at 90 mA and 0.4 V at 150 mA cannot safely be assumed to retain either figure at its 250 mA rated current when no corresponding specification or curve is supplied.[1147]

Minimum-load requirements also matter: if a regulator specifies a minimum load current for regulation, operation below that current can produce loss of regulation, instability, or a larger effective dropout requirement.[222][1438]

## Standard linear regulators and LDOs

Conventional linear regulators commonly require roughly 1.5–3 V of headroom, with familiar 7805 and LM317 examples often treated as approximately 2 V devices under relevant load conditions.[90][158][722][1438] This relatively large differential arises in common standard-regulator architectures from the pass element; an NPN Darlington arrangement incurs two base-emitter drops plus transistor saturation voltage.[90]

A low-dropout regulator (LDO) is a linear regulator designed to operate with a smaller input-output differential than a standard linear regulator.[90] LDO dropout can range from several hundred millivolts to much lower values in suitable low-current applications; examples include 0.2 V for a 3.3 V output at 90 mA, 0.35 V at full load for a specified regulator, and approximately 50–100 mV in a low-voltage battery-powered application.[158][1147][222][972] Thus a 3.3 V rail with 100 mV dropout can operate from about 3.4 V, whereas a standard regulator needing 1.5 V would require about 4.8 V.[1147][158]

Lower dropout is not the sole selection criterion. LDOs can be more sensitive to output-capacitor value and ESR because of loop-stability considerations, while ordinary linear regulators are generally simpler and more stable but need more voltage across input and output.[90]

## Battery-powered systems

Dropout directly raises the system’s effective battery cutoff voltage, because regulation ceases once the battery voltage falls below output voltage plus dropout.[1331][972] This can leave substantial battery energy unused when the discharge curve spends appreciable capacity below that threshold.[1331][972]

A one-cell lithium-polymer supply feeding a 3.3 V regulator with 50 mV dropout cannot regulate down to a 3.0 V cell cutoff; it reaches the regulator limit at about 3.35 V instead.[1331] In the illustrated discharge case, that higher cutoff discards roughly 45–50% of nominal battery capacity.[1331] Similarly, a 9 V battery made from six cells benefits when a 5 V regulator can operate near 0.8 V per cell; a regulator needing about 1.1–1.15 V per cell leaves more capacity inaccessible.[722]

A switch-mode converter can be preferable where lower operating input voltage or greater battery utilisation is needed, provided its conversion efficiency across the expected load range justifies the choice.[722][751] Buck converters still require input voltage above their desired output by their own dropout or conversion headroom; they cannot generate an output higher than their input.[1030][1031][1298]

## Circuit and layout allowances

The voltage budget must include voltage drops external to the regulator, such as current-sense resistors, wiring, connectors, and cable resistance.[222] A 1 Ω series sense resistor at 1 A loses an additional 1 V, turning a nominal 6.6 V regulator-input requirement for 5 V output into a 7.6 V upstream supply requirement.[222]

Some regulators provide separate input and control-supply pins. Supplying the control pin from a higher available voltage can reduce the effective input-to-output dropout, whereas packages that internally join those pins cannot use this arrangement.[222][260] An LT3080 arrangement with its control supply separated from the main input can therefore have lower effective dropout than one with the two pins tied together.[260]

Adequate margin must also be retained under input ripple. If ripple troughs fall below the regulator’s minimum input requirement, regulation is lost during those portions of the cycle.[621] Operating close to dropout can additionally worsen an LDO’s attenuation of input ripple, particularly at higher output current.[1116][1115]

## Dropout in converters and pass stages

The broader term is also used for the point at which a DC-to-DC converter or other regulated power stage can no longer sustain its output under excessive load or insufficient input headroom.[110][1031] In a 15 V converter designed for 100 mA, output voltage began dropping at about 170 mA because the component values were not optimized for the greater current.[110] A buck power-supply module supplied with 32 V and unloaded produced a maximum of 31 V, corresponding to about 1 V dropout at no load.[1031]

For linear pass elements, dropout also limits how near an output can approach its supply rail; an output cannot reach the maximum input voltage because some voltage must remain across the pass element.[1701] That remaining differential produces heat proportional to the voltage drop and load current, making excessive headroom a dissipation concern even though insufficient headroom causes dropout.[1701]