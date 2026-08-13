# power factor

Power factor is the ratio of real power to apparent power in an AC circuit — the fraction of the volt-amps drawn from the mains that actually does work in the load.[1730] It runs from zero to one and can never exceed one, and for a linear load it equals the cosine of the phase angle between voltage and current.[1730] It matters because a load with a poor power factor draws far more current from the supply than its wattage suggests, and that current has to be carried, fused and generated whether or not anybody is billed for it.[1730][1413]

## The power triangle

Apparent power, symbol S, is simply voltage times current, which is why its unit is the volt-amp rather than the watt.[1730] It is not the true power a product consumes: an oscilloscope reading 67 VA at the mains inlet was drawing 30 W of real power.[1730] Real power P and reactive power Q form the two legs of a right triangle whose hypotenuse is S, so S equals the square root of P squared plus Q squared, with Q the imaginary component.[1730] Power factor is P divided by S, and equals cos θ.[1730] Any reactance introduced into a circuit or load produces the voltage-current phase difference that brings the cos θ term into play.[1730]

Reactive power is not dissipated anywhere in the load — it is shuttled back and forth — but it still manifests as real losses upstream, because the conductors carrying the extra current are not superconductors.[1730] The same argument appears in current-probe terms: a load without correction draws large positive and negative current spikes rather than a clean sinusoid, and those spikes cause I²R losses in the cable, flow through the product's fuse, and therefore drive the fusing design, component ratings and distribution system design.[1413] This is why transformers and similar equipment are rated in VA rather than watts, and why any well-specified product states its mains draw in VA.[1730]

## Who pays for it

Domestic metering in Australia bills only true power in kilowatt-hours, so the power factor of a household load does not affect the bill.[1446] Large industrial consumers are a different case: they are charged for VA, so the closer a factory's power factor is to one, the lower its electricity bill.[1730] The design target is a power factor of one — a purely resistive load with no reactive component at all — and the further it falls toward zero, the more current is taken from the entire upstream delivery system and the more the utility charges.[1730]

## Correction

Passive correction works by adding the opposite reactance to whatever the load presents: power stations and factories use large capacitor banks, while a capacitive load such as a switch-mode power supply needs added inductance to compensate.[1730]

Active correction addresses the real culprit in mains-powered electronics. A bridge rectifier feeding a bulk capacitor charges only near the positive and negative peaks of the mains waveform, producing line sag and short current pulses at each peak; this configuration commonly yields a power factor of 0.5 to 0.7.[273] The fix is a power-factor-correction pre-converter inserted between the bridge rectifier and the bulk capacitor, such as a current-mode controller like the MC34262.[273]

The economics of PFC have shifted decisively. Active correction was once reserved for supplies of 600 W and up; PFC controllers are now available for well under 100 W, a 45 W brick may carry one, and above a certain power level PFC is actually cheaper to include than to omit.[1032] The consequence is that almost any modern product achieves a power factor of 0.98 or 0.99.[1032] Specified equipment reflects this: a variable frequency converter guarantees a minimum of 0.97 at full load across a 95–264 V, 47–410 Hz input range,[449] and a broadcast modulator specifies an operational power factor greater than 90%.[574] Solid-state transformers proposed for large installations offer unity power factor, or a power factor the utility can vary on demand, in place of conventional transformers whose power factor variation the supply system dislikes.[1753]

Applying reactive compensation to a load whose distortion is harmonic rather than phase-shifted does not help. Harmonic power factor is a separate problem from simple phase lead and lag, and is the more serious of the two.[1285] Attempting to passively correct a cheap LED driver with inductors was judged not worth doing, in part because the effect of such mods on efficiency is unknown.[1253]

## Measured values on the bench

Test equipment is a consistently poor performer. Measured operating figures include 0.45 for one oscilloscope,[1730] about 0.5 for a Tektronix TDS220 at 9 W and 18 VA,[690] about 0.55 for a Rigol DS1054Z drawing 22 W and 40.5 VA,[674] 26 W against 44 VA for a Uni-T UPO2104CS,[1038] 0.64 for a LeCroy Wavejet 354 running at 42 W and 68 VA,[790] 0.86 and 0.863 for an Agilent unit and a Prema 6047 respectively,[164][613] and 0.95 for a Tektronix MDO4000 at 143 W and 151 VA.[199] Two generations of the same Keysight scope differed little: the 3000A drew about 67 W at 0.91, the 3000T 67 W at 0.86.[701] A Rohde & Schwarz HMO1202 drawing 18 W operating had a power factor described as not great, consistent with having no active PFC.[842]

Other measured loads: a dual-Xeon workstation idling at 177 W and 192 VA gave about 0.92,[726] an LG plasma TV 230 W against 250 VA gave 0.82,[725] a salvaged LCD panel drew 63 W at 65.3 VA for 0.969 while a 50-inch LG TV drew 40 W at 50.92 VA for 0.8,[915] and a mini PC drawing 10.5 W showed 23 VA.[1649] A pair of powered monitor speakers idling at 8 W drew almost 24 VA, a power factor of 0.33.[169] Purely resistive loads sit at the other extreme: a 1 kW heater measured a power factor of precisely one,[uxm3qeKcg3w] as did an immersion-electrode water heater drawing 1.1 kW.[873]

## Standby is the worst case

Power factor degrades sharply at low load, and standby is where it collapses. A 4K television drawing 327 mW in standby had a power factor of 0.02 and was pulling 17.5 VA from the mains, of which only 0.3 W would be billed; switched on, it rose to 0.5 as expected.[1388] The same set drew more real power in standby with its power factor correction working, and even then reached only 0.16, described as typical of low-power products.[1388] A heat pump water heater drawing under 3 W in standby presented 40 VA at a power factor of 0.07.[1517] A HEPA air filter drawing 0.2 W measured 0.02 power factor and 11 VA, current that still has to come from somewhere.[1505] An Agilent instrument at 0.86 running fell to 0.32 when switched off, its apparent power rising to 20.5 VA on 6.5 W of standby draw.[164] A Rohde & Schwarz scope drawing half a watt in standby still presented 6.3 VA,[842] and a Fluke 45 with only its transformer, rectifier and filter caps energised drew just over 1 W and 8 VA.[791]

## LED lighting

LED drivers are where power factor trades directly against another defect. Increasing the input capacitance of a cheap driver cures its output flicker but drops the power factor — one such fix took it to 0.58, roughly doubling the current drawn through the network copper even though the user is not charged for it.[1253] The alternatives are close to a choice between near-100% flicker and poor power factor, and simply reducing the input cap to recover power factor reintroduces ripple and hence flicker.[dLlhoUHlnjE] Doing both at once requires a better topology: proper secondary-side current regulation gave a flicker-free driver a power factor of 0.974,[1253] and a primary-side-only design achieved 0.94 at about 30 W with almost non-existent ripple.[dLlhoUHlnjE] As a working threshold, anything over 0.95 is fine.[dLlhoUHlnjE]

Measured lighting products include an 80 W flood at 82 W with a power factor around 0.95 to 0.97 against a claimed 0.95,[773] and an 18 W tricolour panel at 0.9.[QxMmEAb2JME] Driver ICs intended for retrofit LED tubes advertise high power factor alongside 95% efficiency, low BOM cost, buck-boost and flyback modes and 5% output current accuracy, driving LED strings directly from rectified mains.[533]

## Capacitive droppers

A mains capacitive dropper feeding a zener regulator dissipates effectively nothing in the capacitor itself, aside from a very small loss in its ESR, which is exactly why the topology is used.[1482] There is no free lunch: the generating station still has to supply the 3.7 W, and because the circuit is mostly capacitive the power factor is extremely poor.[1482]

## Energy-saver devices

Plug-in devices claiming to reduce household energy consumption are typically a capacitor in a box.[1446] Against a predominantly inductive fan drawing 93 W real at a power factor of about 0.90, such a device improved the reading slightly, to 0.914.[1191] Against a modern electronic load drawing 9.1 W against about 32 VA — a power factor near 0.57 — the device made the power factor worse and increased the apparent power substantially, so a consumer billed on apparent power would pay more for having plugged it in.[1191] Since domestic billing is on real power in the first place, the correction cannot reduce a household bill at all.[1446]

## Measurement

Power factor is derived from simultaneous voltage and current measurement, and instruments that report it must multiply the two in phase.[1446] The electromechanical watt-hour meter solves this mechanically: at a power factor of one the voltage and current fluxes are in phase, which produces no circulating eddy currents and no torque, so the voltage coil is made inductive to introduce a deliberate 90° flux delay.[1446] Maximum disc torque then occurs at unity power factor, and torque falls as the load's power factor drops below one, which is precisely the behaviour needed to integrate true power.[1446]

Bench and panel instruments that report power factor directly include the Gossen Metrahit Energy multimeter, which displays power, watts, VA and power factor with simultaneous voltage and current on a triple display;[173] industrial panel analysers;[936] a programmable AC source with built-in power-factor and crest-factor readout;[1698] and utility smart meters performing four-quadrant real and reactive energy measurement per phase along with frequency, phase angle, power factor and total harmonic distortion, at a burden of under 0.5 VA per phase.[409] Three-phase oscilloscope options extend the same measurements to a scope, at typical scope accuracies of 1 to 4%.[VTHcxTst_RA] A current clamp around the active conductor of a mains lead shows the current waveform directly, making a poor power factor visible as peaked rather than sinusoidal current.[1368][1413] Simulation can predict power factor, but building the circuit and measuring it in the real world remains the practical check.[1285]

The distorted, peaky current waveform of an uncorrected supply is also the standard illustration of why RMS cannot be computed from peak values: the area under such a curve must be obtained graphically or by calculus.[1417]

## Boundary cases

Not every waveform defect is a power factor problem. Clipping of a solar array's power curve does not upset the power factor of a grid-tied microinverter, because the inverter still produces a continuous sine-wave output into the mains regardless of what the panel is doing.[BtQUuD6QRMw]
