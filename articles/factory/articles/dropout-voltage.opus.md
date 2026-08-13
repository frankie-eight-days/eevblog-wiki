# dropout voltage

Dropout voltage is the minimum differential a voltage regulator requires between its input and its output before it can no longer hold its output constant. Every linear voltage regulator carries a dropout voltage specification, and the input must sit at least that far above the output or the part falls out of regulation entirely.[158][90] The figure is not a footnote in a datasheet: it sets the minimum supply rail a design can run from, and in battery-powered equipment it directly determines how much of the cell's stored energy is reachable.[1331][722]

## Definition and measurement

The specification is the input-to-output differential voltage, so a regulator producing 5 V from a part quoted at 2 V minimum drop needs at least 7 V at its input.[158] Below that differential the internal control loop no longer has the headroom to function — the circuitry that drives the pass element must itself be biased above the regulated output.[221] The consequence is exactly what the name says: it drops out of regulation.[1147]

Measured in practice, dropout is defined at the point where the output falls by 100 mV from its regulated value.[158] The bench procedure follows from that definition: hold the load current fixed, wind the input voltage down while watching the output, and record the input-output difference at the moment the output starts to sag.[224][158] A 3.3 V rail from an LM317 at 20 mA load and 25 °C measured 4.803 V in against 3.26 V out, giving 1.54 V of dropout and matching the datasheet curve.[158] Watched on an oscilloscope, the approach to dropout is visible as more than a DC sag — the output stays roughly present but becomes unstable as the loop loses control.[1147]

## Dependence on current and temperature

Dropout is not a single number. It rises with load current and varies with temperature, which is why datasheets present it as a family of load lines on a differential-voltage-versus-temperature graph rather than a single entry.[158] An LM317 characterised this way shows separate curves for 20 mA, 200 mA, 500 mA, 1 A and the maximum 1.5 A output, with the highest-current curve sitting well above the rest.[158] At 25 °C the 20 mA line gives about 1.5 V while the 500 mA line gives roughly 1.75 to 1.8 V.[158] The temperature dependence matters mainly at industrial extremes; for room-temperature bench work the middle of the curve is representative.[158]

The current dependence is what turns a comfortable margin into a marginal one. A 3.3 V output at 1.5 V dropout needs 4.8 V in, which USB nominally supplies, but the same regulator at 500 mA needs 5.1 V — technically above what a 5 V USB rail provides, and USB is specified at ±5 %, so the supply could legitimately be as low as 4.75 V.[158] An LDO with 0.2 V dropout in that same application would have left ample margin and delivered the full 500 mA.[158]

Failing to meet a part's minimum load current specification can also degrade dropout, among other unpredictable behaviours; a part quoting 500 µA minimum load must be given that load across the entire output voltage range.[222]

## Standard linear regulators versus LDOs

A conventional linear regulator uses an NPN Darlington pass element, so the input-output drop must cover two base-emitter drops plus the pass transistor's saturation voltage — which is why a 7805 typically shows around 1.5 to 2 V, and sometimes more.[90][722] The precise figure depends on the specific variant and the load current.[722] The LM317 is likewise not a low-dropout part; its datasheet quotes a 3 V minimum input-to-output differential typically, more than the 7805, though a 2 V minimum drop at full current is the usual working rule of thumb.[1438][158] Several volts of mandatory headroom makes such parts unsuitable wherever the available input sits close to the desired output.[221]

A low dropout regulator is simply one with a smaller tolerated input-output difference.[90] Special low dropout types reach several hundred millivolts,[158] and modern jellybean parts do better still: a SOT-23 regulator rated 250 mA specifies 0.2 V dropout at 90 mA rising to 0.4 V at 150 mA, and measured 300 mV at its maximum recommended 250 mA — a figure its datasheet omits entirely, along with any performance graphs.[1147] For a 3.3 V output, an LDO of this class needs only about 3.4 V in.[1147] Sub-100 mV dropout is available where it is needed; 50 mV parts inform where a low-battery detector threshold can be set relative to the highest-voltage part in a design.[1331][972]

The low differential is bought at a cost. LDOs use a PNP or P-channel pass element that is inherently less stable, so the loop is more sensitive to the value and ESR of the output capacitor, and their ground current can scale with output current and waste power.[1147][90] Standard linear regulators are simpler and more stable but demand the larger voltage drop.[90]

Dropout also interacts with ripple rejection. The attenuation an LDO provides from input to output depends on the actual input-output differential, and gets worse as that differential falls, so a regulator running with very little headroom passes most of the input noise straight through.[1116][1115] Higher output current degrades the rejection further.[1116] This makes an LDO a poor choice for cleaning up tens or hundreds of millivolts of ripple unless it is given real headroom.[1116]

## Parts with a separate control pin

Some regulators specify dropout in two ways, giving distinct figures for the control pin and for the input pin.[222] On the LT3080 these pins are normally tied together, in which case the worst-case combined figure applies — 1.2 V at 100 mA, and as bad as 1.6 V at full current, so a 5 V output needs at least 6.6 V in.[222][260] Measured on the bench with the pins tied, the part showed about 1.25 V at no load and 1.35 to 1.4 V at 1 A, agreeing with the datasheet curve once junction temperature above 25 °C is allowed for.[224]

Where a higher voltage already exists elsewhere in the circuit, powering the control pin from it — for example from the far side of a current shunt resistor — yields a substantially lower input-to-output dropout than tying the two pins together.[222][260] The technique is not universally available: some smaller pin-count packages bond the two pins internally, leaving no separate control connection.[222][260] The part's headline 350 mV dropout at full load applies only under the favourable pin arrangement, not the tied-together case.[222]

## Switching converters and buck regulators

Switching converters have a dropout condition too. A buck topology cannot produce an output above its input, so the input must exceed the desired output by whatever the converter's dropout amounts to.[1298][1030][1031] A module rated 6 to 40 V in and 0 to 32 V out therefore requires the input range to sit at least one dropout above the intended output range; a 0 to 12 V bench supply built from it could be fed from 13 to 15 V.[1031][1030] Measured with no load, one such module fed 32 V produced a maximum of 31 V out, giving 1 V of dropout.[1031] Dropout can be far larger in high-power designs: a 2000 W buck supply specified for a 96 V output accepts 20 V minimum and 110 V maximum input, implying at least 14 V of dropout.[1298]

A switching design can also enter dropout through component sizing rather than input voltage. A converter designed for 100 mA held regulation to about 170 mA before the output began to fall, the limit set by the chosen component values; substituting a 47 µH inductor for a 33 µH one moved the dropout point down to about 120 mA.[110]

Because switchers tolerate a much smaller input-output difference, they are the standard remedy where a linear regulator wastes usable range: a 5 V regulator running from a six-cell alkaline 9 V battery drops out around 6 V — roughly 1.15 V per cell — while at least 1 V per cell and ideally 0.8 V per cell is needed to extract most of the battery's capacity.[722] Any competent switch-mode converter reaches that easily.[722] The same reasoning appears in battery-life optimisation generally: moving from a linear regulator to a switching converter to obtain lower dropout is one of the standard what-if changes when a design's runtime is being re-optimised.[1331]

## Consequences for battery-powered design

Dropout sets the effective cutoff voltage of a battery-powered product, and that cutoff determines how much capacity is usable. A single-cell lithium polymer battery discharging to a 3 V cutoff feeding a 3.3 V LDO with 50 mV of dropout cannot run below about 3.35 V, which moves the cutoff point far up the discharge curve and wastes something like 45 to 50 percent of a 1000 mAh cell's capacity.[1331] Powering a 3.3 V rail directly from a single lithium polymer cell through a linear regulator is therefore poor practice unless a switching converter is used.[1331] The same arithmetic applies to alkaline cells: a 4.8 V minimum supply implies a 1.2 V per cell cutoff before the regulator's own dropout is even counted, discarding roughly half the batteries' capacity.[972] Where a chip's true operating limit is well below its specified minimum — one meter's highest-voltage internal part functioning down to 3.6 V against a datasheet figure of 4.8 V — the low-battery threshold can be set only slightly above that limit, provided the regulator's dropout is small.[972]

Equipment that fails this test fails visibly. A multimeter whose display brightness collapsed as its supply was wound down, going dark by about 2.5 V, cannot work across the 1.25 V per cell range at which a meter should still function.[1095]

Claims of extracting extra energy from cells by boosting their voltage have to be evaluated against this backdrop: whatever gain a booster offers by working below a product's own dropout voltage is offset by the converter's efficiency, which falls off sharply at higher currents, and the product's current draw is unknown to a general-purpose part.[751]

## Dropout in service and diagnosis

Dropout voltage is a diagnostic tool during repair. If a 5 V rail is derived from a pass transistor with an assumed 2 V maximum dropout, its raw input must sit at least 7 V above ground — so a rail measuring near 9 V is healthy, and one significantly lower points to the primary side failing to deliver enough power on that winding, and probably on the others too.[804] The same check applied to a repaired instrument means verifying that the ripple troughs on the raw rails stay well above the regulators' minimum dropout requirement, which some designs cut uncomfortably fine.[621]

Dropout can be inferred in reverse from a known regulator. A board using 7815 and 7805 parts to generate ±15 V and ±5 V rails must have at least 2 V of dropout on the 15 V regulators, implying an unregulated supply of roughly ±18 V rather than ±12 V.[1431] Keeping that raw rail no higher than necessary limits dissipation in the regulators.[1431]

The requirement persists in instruments with linear output stages. A bench source running its outputs in linear mode cannot swing to the maximum of its own input supply because some dropout is always consumed by the pass element — and at low output voltages and high current the resulting drop across that element becomes the dominant dissipation.[1701]

Because dropout behaviour is a function of the specific silicon, a regulator carrying a new suffix on its part number is not interchangeable with the old one on faith: it may drop out differently or oscillate with a different combination of load and bypass capacitors, and requires re-qualification.[1752]

## Terminology boundaries

The term belongs to voltage regulators and does not transfer cleanly. Voltage references have an equivalent requirement — typically 2 V above the output for all variants, so 5.3 V in for a 3.3 V reference, 6 V for a 4.096 V part, and 7 V for a 5 V part, below which output regulation is lost — but reference datasheets generally do not use the phrase "dropout voltage", which is a trap when searching for it.[500]

The phrase also appears with a different meaning on DC electronic loads, where a settable dropout voltage is the cutoff at which the load stops discharging the cell under test — 2.6 V, for instance, on a coin cell discharge.[862]
