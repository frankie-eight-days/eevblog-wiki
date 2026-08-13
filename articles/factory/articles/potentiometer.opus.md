# potentiometer

A potentiometer is a three-terminal resistive component in which a wiper contact slides along a continuous resistance track, tapping off a fraction of the end-to-end resistance according to its mechanical position.[706] Wired across a supply it forms an adjustable voltage divider; wired to only two terminals it becomes a plain variable resistor, or rheostat, and both usages are ordinary practice.[1054][1720] It is the standard interface between a human hand and an analog quantity — a volume, a threshold, a set point, a shaft angle — and it remains the cheapest way to inject an adjustable voltage into a circuit that would otherwise need a DAC.[837][471][218][232]

## Construction and taper

The track carries a controlled resistance across its whole length, so the tap voltage varies with wiper position; in a typical arc-shaped element the resistance is evenly distributed and the response is close to linear, with an end-to-end value measuring around 3.6 k in one joystick example.[706] Track materials vary. Carbon and graphite compositions dominate cheap and mid-range parts, including sliders.[706][1054][1244] Wire-wound elements appear in precision instrument work, sometimes as two separate pots ganged on a single shaft, and in vintage meters the wiper can be seen scraping directly along exposed nichrome wire.[693][930]

Track law matters as much as value. A part marked 10KA is a 10 k logarithmic pot, the A suffix denoting the log taper used for audio-style controls.[256] Taper is a first-class parameter of the component alongside resistance, and belongs in any competent treatment of the subject.[1304]

Where the divider tap must be sealed against contamination or vibration, sealed-body pots are used, and re-enterable potting compound permits a screwdriver to reach a buried adjustment and then heals behind it.[587][384][1516]

## Single-turn versus multi-turn

Resolution is set by mechanical travel. A single-turn pot spreads the entire range over roughly 300 degrees of rotation, which makes fine setting on a wide-range control genuinely difficult — enough that adjusting a lab supply's output to a round number by hand becomes an exercise in patience, and the setting drifts under the lightest disturbance.[224][471] The engineering answer is a multi-turn part, and Dave Jones treats a 10-turn control as a baseline requirement, holding that any good lab power supply should have 10 turn pot.[224] A 10-turn part spanning a 50 k range lets a constant-current dummy load be set anywhere from about 1 mA to 1 A with usable resolution across the whole span.[102][749]

The alternative to more turns is two controls: a coarse and a fine potentiometer whose outputs are mixed, an arrangement worth adopting when the design was never built around a 10-turn part.[304] Even a 10-turn control is not proof against a dead element — a 10-turn adjustment on an OCXO that can be driven hard against both mechanical stops without shifting the output frequency indicates a failed pot rather than an exhausted adjustment range.[1139]

## Circuit roles

The classic use is setting a timing element. Substituting a pot for a fixed timing resistor in an astable 555 makes the oscillator frequency directly adjustable,[160] and a 10 k pot in a 555 PWM dimmer produces brightness that tracks the knob roughly linearly and switches fully off at the bottom of travel.[392] A pot on a triac gate circuit sets the turn-on point within each mains half-cycle.[1172]

In a linear power supply the pot generates the reference that the error amplifier servos the output to, either directly or through a buffer.[861] Because the set pin is inside a direct feedback loop, whatever noise rides on that node appears on the output within loop bandwidth; a pot fed from a quiet voltage reference is therefore a low-noise way to derive a set point, while a PWM-and-RC-filter substitute passes through whatever ripple the filter fails to remove.[222] The same node is what a DAC replaces in a digitally controlled supply, generating Vset and Iset exactly as a pot would.[232][102] Deriving the control voltage from an LM317-style regulator carries the penalty that the set value is offset by the regulator's 1.25 V reference and cannot reach 0 V at all.[221]

Threshold setting is the other staple: a pot sets the trip point of a light detector,[27aG9xhfk6s] supplies the swept input to an overload comparator that must fire above +1.25 V and below −1.25 V,[471] exercises a Schmitt trigger's hysteresis,[941] and adjusts LCD contrast on the VO pin where a fixed divider is inadequate.[274][1202][1664] A single external resistor sets the output current of a constant-current LED driver, so replacing it with a pot yields a brightness control.[513]

Nulling an op-amp offset with a trimmer is possible but is not a proper fix for a production circuit; the better route is to redesign the resistor values so input bias current stops dominating in the first place.[479]

A pot is also an efficient reverse-engineering tool. When hardware configuration is set by fixed resistors, fitting a pot in place of the resistor — a 100 k part substituting for a 120 k original — lets the whole configuration space be swept without desoldering a new value for every trial.[977][978] Trimmers installed for this purpose should be mounted so that screwdriver force is decoupled from their solder joints.[977]

## Position sensing

Coupling the wiper shaft to a mechanism turns the pot into an absolute angle sensor. An antenna rotator uses a pot on the mast shaft to feed position back to the indicating needle,[218] and analog joysticks connect two rotating arms directly to carbon pots, a two-terminal connection being sufficient.[1054]

Reading those pots on early PCs avoided ADCs entirely, since converters were expensive around 1980 and four would have been needed. Instead the joystick pots set the pulse width of a 558 quad 555 timer, and a timer/counter measured the resulting pulse to recover position; finer polling of the port yielded finer position resolution.[1054][1053] The pots themselves were imprecise, one axis ranging to roughly 120 k at full deflection, which is why front-panel trimmers were provided to re-centre each axis.[1054]

Industrial joysticks are specified by operation count, with potentiometric versions rated at more than 5 million operations against up to 15 million for Hall-effect sensing — the trade being that the pot version needs no active electronics and can be supplied with dual outputs for failure detection in safety-critical applications.[706]

## Loading and precision

A pot loaded by an external impedance is no longer the divider it appears to be. Placing a 2 k pot across a 10 ohm resistor gives fine adjustment on top of a coarse divider and is chosen for stability; a 10 M multimeter input across the pot alone would introduce only about 0.02 % error, but the same 10 M path running from the wiper to ground, with a further 10 k in circuit, substantially upsets the divider.[584] Where the pot is used to set a precision value, the source impedance seen by the loading element — not the pot's nominal value — determines the error.

## Wear, contamination and failure

The wiper contact is the weak point, and the failure is progressive rather than sudden. Sliders and faders in mixing consoles collect dust and debris through their top slot, and once the pots have gone scratchy the labour to replace them all can exceed the price of a new console, which is why consoles are often scrapped before their power amplifiers fail.[840][354] A completely open-circuit slider gives no reading at all and must be replaced; on keyboards and consoles these are among the first parts to wear out.[256] Substituting a standard part is usually acceptable provided the taper is matched.[256]

Contact cleaner is the first intervention. The spray should reach the element rather than the exterior, so the part is best rotated during application and oriented so the fluid runs down the shaft rather than dripping off the surface.[502] Ordinary cleaning solvent poured into a pot is not advisable.[256] Not every symptom is electrical: a shaft pin that no longer engages its plastic drive gear leaves the pot electrically sound but mechanically disconnected, producing a control that simply does nothing.[502] Similarly, a control that adjusts in one direction only points to the pot rather than the circuit behind it.[1572] Intermittent contact in a single-turn trimmer is a live suspect when a factory-calibrated instrument's accuracy drifts over time, since each unit's calibration rests on those manual adjustments.[Yk_T-uCbg10]

Pots are also exposed to abnormal energy. In a multimeter fault where an input switch failed to disengage, 240 V passed through the variable pot and the on-board PTC, and the surrounding passive parts were the ones that visibly failed.[94]

## Calibration adjustments

Older analog instruments are dense with trimmers. A vintage oscilloscope can carry more than nineteen visible adjustment pots plus further ones on the underside of the main board — more adjustment pots than you can poke a stick at — before counting the trimmer capacitors used for compensation.[208] Some are ganged with the front-panel switch, a single control acting as both switch and rotary pot.[208] Once set, factory adjustments are commonly locked down with a coloured compound so vibration cannot move them, which also marks any subsequent tampering.[268][449]

Adjustment technique matters. A non-conductive, non-magnetic plastic alignment tool is required where the adjustment is not a pot at all but a slug-tuned inductor, since a steel screwdriver blade inside the coil detunes the circuit while it is in place.[523]

Modern digital instruments have largely displaced the trim pot: calibration constants are programmed into the meter in software at the factory, and current multimeters of this class contain no calibration pots at all.[852] Where a manufacturer does still fit off-the-shelf pots for calibration, it reflects a low-cost implementation taken essentially from the chipset's application note.[344]
