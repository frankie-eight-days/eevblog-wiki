# dropout voltage

Dropout voltage is the minimum differential a voltage regulator needs between its input and its output in order to keep regulating: the input must sit some number of volts above the output, or the regulator falls out of regulation and the output simply follows the input down.[158][221] Every linear regulator carries a dropout specification, and the figure is not a constant — it varies with load current and with temperature, so a part that looks comfortable at 20 mA can be marginal at half an amp.[158] Because the differential is wasted headroom, dropout voltage sets the floor on how much of a battery's discharge curve is usable, how hot a linear pass element runs, and how well a regulator rejects input ripple.[1331][1701][1116]

## Definition and measurement

The specification is a differential, not an absolute input voltage: for a 5 V output from a standard linear regulator with a 2 V dropout, the input must be at least 7 V.[158] Below that point the part stops holding its reference and "it drops out of regulation" — the output is still present, but it is no longer controlled and can become unstable.[1147]

Datasheets define the threshold operationally, as the input-to-output differential at which the output voltage has fallen by 100 mV.[158] That makes it directly measurable: wind the input down until the output sags by 100 mV, then subtract. On an LM317 loaded at 20 mA, an input of 4.803 V against an output of 3.26 V gives 1.54 V of dropout, matching the datasheet curve.[158] The same technique applied to an LT3080 gives roughly 1.25 V at no load and 1.35 to 1.4 V at 1 A, which agrees with the published minimum once junction temperature is allowed to rise above 25 °C.[224]

Manufacturers present the parameter as a family of load lines — input-to-output differential against temperature, one curve per output current, typically spanning 20 mA up to the part's 1.5 A maximum.[158] For an LM317 at room temperature, that is about 1.5 V at 20 mA rising to roughly 1.75 to 1.8 V at 500 mA.[158] Cheap parts sometimes truncate the data: one three-terminal LDO specifies 0.2 V at 90 mA and 0.4 V at 150 mA, then gives nothing at all at its 250 mA rating and provides no graphs, leaving the designer to measure it — about 300 mV in practice.[1147]

## Standard linear regulators versus LDOs

A conventional linear regulator uses an NPN Darlington pass element, so the minimum drop is two base-emitter voltages plus the saturation voltage of the driving transistor; that is why a 7805 shows a typical dropout of around 1.5 to 2 V or more.[90][722] The LM317 is in the same class, with a datasheet input-to-output differential typically quoted as a 3 V minimum, worse than the 7805.[1438] Two or three volts of mandatory headroom is a serious constraint in low-voltage systems.[90]

A low dropout regulator is simply one with a smaller minimum differential, achieved with a PNP or P-channel pass element.[90][1147] Special low dropout types reach several hundred millivolts,[158] and a 3.3 V LDO may need only about 3.4 V in.[1147] The cost is stability: the PNP or P-channel topology is inherently more prone to oscillation, so the value and ESR of the output capacitor matter far more than they do for a standard part, and LDO ground current can rise with output current and waste power.[90] Linear regulators of the old type are simpler and more stable but demand the larger drop; that is the basic trade.[90]

The margin matters in practice. Running a 3.3 V rail from a 5 V USB supply through an LM317 requires 4.8 V at 20 mA, which USB nominally provides, but 5.1 V at 500 mA — technically over budget before USB's ±5 % tolerance is even considered.[158] An LDO with 0.2 V of dropout in the same slot would have left ample margin and full output current.[158]

## Battery-powered design

Dropout voltage translates directly into wasted battery capacity, because the regulator's minimum input becomes the system's cutoff voltage. A single-cell lithium polymer battery feeding a 3.3 V LDO with 50 mV of dropout cuts off at about 3.35 V, high on the discharge curve: "you're pissing away, you're wasting half of your battery capacity".[1331] With a linear regulator's larger drop the effect is worse still, which is the argument for a switching converter wherever the cell voltage approaches the rail.[1331]

The same arithmetic applies to a 9 V alkaline pack feeding a 7805. A dropout of roughly 2 V makes the effective cutoff a nominal 7 V, about 1.15 V per cell across the six 4A cells inside.[722] A design should reach at least 1 V per cell and ideally 0.8 V per cell, since that is where most of the pack's capacity lies — a switch-mode converter gets there easily, whereas the linear part simply stops regulating with nothing to indicate it has done so.[722]

Where the load chip is conservatively specified, the regulator's dropout becomes the binding constraint on the low-battery threshold: a meter whose highest-voltage internal part works down to 3.6 V can have its detector set only slightly above that, allowing perhaps 50 to 100 mV for the LDOs.[972] A high cutoff wastes capacity regardless of the cell chemistry: dropping out at 4.8 volts on a four-cell pack means 1.2 V per cell, before the regulator's own dropout is counted.[972] The failure is visible on badly designed instruments — one multimeter's display faded noticeably at 3 V and was gone by 2.5 V, against the 1.25 V per cell it should have tolerated.[1095]

Boost converters intended to extend cell life are subject to the same accounting from the other direction: whatever is gained by lowering the host product's dropout is offset by converter efficiency, which falls off steeply at higher output currents and is unknowable when the downstream load is unspecified.[751]

## Parts with a separate control pin

Some regulators specify dropout twice, once for the main input pin and once for a control pin that powers the internal circuitry.[222] Tying the two together is the usual arrangement and forces the worst-case figure — 1.2 V at 100 mA, and as bad as 1.6 V at full current — so a 5 V output needs at least 6.6 V in, or 7.6 V once a 1 Ω current-sense resistor is dropping another volt at 1 A.[222] Powering the control pin from a separate higher rail, or from the far side of the sense resistor, lowers the input-to-output differential substantially, though the input-side voltage drop must then be accounted for.[222][260] The option is not always available: smaller pin-count packages of the same die tie the two pins internally.[222][260] The headline specification for such a part can be as low as 350 mV at full load, which is why the distinction is worth reading carefully.[222]

Minimum load current is a related trap. A part specifying 0.5 mA minimum gives no defined behaviour below it, and among the plausible consequences are instability and a larger dropout voltage, so the minimum load must be guaranteed across the whole output range.[222] On the LM317, minimum load current is "a big trap for young players" in exactly the same way.[1438]

## Switching converters and other pass elements

A buck converter has an equivalent constraint: it cannot produce an output above its input, so the input range must clear the desired output range by the module's own dropout.[1031][1030] A bench module fed 32 V delivered a maximum of 31 V unloaded, giving 1 V of dropout,[1031] while a 2 kW supply rated 20 V minimum input for a 96 V output implies at least 14 V of required headroom.[1298] Dropout in a switcher also depends on component values rather than being fixed by the topology alone: a converter designed for 100 mA held regulation to about 170 mA, and swapping a 33 µH inductor for a 47 µH part moved the drop-out point down to around 120 mA.[110]

Discrete pass elements behave the same way and the figure is useful diagnostically. A series pass transistor assumed to have a 2 V maximum dropout needs at least 7 V on its input to hold a 5 V rail, so measuring significantly less than the expected 9 V there points at the supply feeding it rather than the regulator.[804] Fixed regulators reveal their supply rails by the same logic: 7815 and 7805 parts producing ±15 V and ±5 V require at least 2 V of dropout, so the raw rails must be well above ±15 V.[1431] When checking margins on a repaired instrument, the point to verify is that the ripple troughs on the unregulated input stay above the regulators' minimum dropout.[621] A programmable supply built around a linear output stage inherits the same limit — the output cannot reach the input rail — and the headroom is dissipated as heat, around 7 W when 10.5 V is dropped at 700 mA.[1701] A control loop built from op amps around a pass element likewise needs its input significantly above the regulated output for the circuitry to function at all, which is one reason an LM317-based topology with several volts of dropout is a poor basis for a wide-range lab supply.[221]

## Effect on ripple rejection

An LDO is often used to clean up a noisy rail, but its attenuation from input to output is not fixed: it depends on the input-to-output differential, and as the differential falls the rejection can get worse.[1116] Higher output current degrades it further.[1116] This makes a low dropout regulator a poor ripple filter precisely where it is most attractive. The trap appears when post-regulating a charge pump such as the 7660: with only a small voltage dropped across the regulator, most of the input noise passes straight through.[1115]

## Terminology elsewhere

The term is specific to voltage regulators and is generally absent from voltage reference datasheets, where the same requirement appears as a minimum input voltage — 2 V above the output for most types, so 7 V for a 5 V reference, 5.3 V for the 3.3 V version and 6 V for the 4.096 V part.[500] The intent is identical: below that differential the device will not maintain output regulation.[500]

The phrase is also used in a different sense on electronic loads, where a user-set dropout voltage is the cutoff at which a battery discharge test stops, for example 2.6 V on a coin cell.[862]

Because dropout behaviour is a function of the silicon and not just the part number, a die revision behind an unchanged or barely changed part number is grounds for re-qualification: the replacement may drop out differently, or oscillate with load and bypass capacitor combinations that were previously stable.[1752]
