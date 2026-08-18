# current source

A current source is a circuit element that forces a fixed current into whatever load is connected to it, adjusting its terminal voltage as needed to do so — the dual of a voltage source, which holds a fixed voltage and lets the current fall where it may.[1397][1688] It is drawn as a circle with an arrow inside pointing in the direction of conventional current flow.[1688][105] Along with the voltage source it is one of the first abstractions worth learning after voltage, current and resistance, because it underpins Thevenin and Norton equivalents, circuit analysis, and a large amount of practical design.[1397]

Purely theoretical treatment of current sources is of limited use on its own; the concept earns its keep when applied to real hardware, where current sources appear as bench instruments, as biasing elements inside integrated circuits, and as the correct way to drive devices whose voltage is not a usable control variable.[1688]

## Behaviour and compliance

An ideal current source delivers its set current regardless of load, including into a short circuit, where the terminal voltage simply collapses to whatever the load demands — an amp into a short still produces an amp, at a few tens of millivolts.[1688] The bound on this behaviour is the compliance voltage: the maximum voltage the source will develop in its attempt to push the programmed current.[1397][908] Once the load requires more than the compliance voltage, regulation is lost and the set current is no longer delivered.

Compliance is not a cure-all. A 5.1 V Zener driven from a constant current source holds its rated voltage at 10 mA and at 1 mA, but by 100 µA it has sagged to 9.45 V, and at 10 µA and 1 µA it does not work at all — and raising the compliance from 10 V to 100 V does not rescue it, because the limitation is in the device, not the source.[908]

The source's own impedance is what distinguishes the two kinds of supply. A bench power supply presents an output impedance in the order of milliohms and therefore behaves as a voltage source, forcing its set voltage onto the node and leaving the load to sort out its own current.[1427] In network analysis this duality appears directly: when suppressing sources to find an equivalent, a voltage source is replaced by a short circuit and a current source by an open circuit.[820]

## Where the model is used

The current-divider relation is the counterpart of the voltage divider, describing how a total current from a source splits between two parallel resistive branches.[1399] Thermal design reuses the whole electrical model: heat flow in watts is represented as a current source, thermal resistances as resistors, and temperature as voltage.[105]

Driving a capacitor from a constant current source removes the time term from I = C dV/dt, so the capacitor voltage rises as a straight line rather than an exponential.[486] That linear ramp is the basis of the standard derivation of the energy stored in a capacitor as ½CV².[3MtK035qiT4][1618]

A solar panel behaves as a source rather than a load, with conventional current flowing out of its positive terminal — which is why current can flow up through and bypass the panel's bypass diodes in a way that would be impossible if the panel were merely a resistive load.[1426]

## Inside integrated circuits

Current sources are pervasive as internal bias elements. The input stage of a bipolar operational amplifier uses a pair of NPN transistors whose tails run into a current source in a current-mirror configuration.[479] One technique for reducing input bias current is the bias-cancelled input, in which additional current sources supply the base current that would otherwise be drawn through the input pins; the cancellation is good but never exact, and zero bias current is not achievable in practice.[479] A differential JFET front end likewise needs extra transistors forming a current source in the tail.[932]

The differential pair in a comparator is a fairly crude amplifier on its own; current sources in the bias network are what make it acceptable in that role.[555] Substituting an LP2902 for an LM324 in an unstable control loop produced a marked improvement in stability, the relevant difference between the two otherwise near-identical parts being an extra internal current source.[95]

Current sources also appear as small building blocks in discrete design. Loading a voltage-gain stage with a current source is standard practice in preamplifier design, and the implementation can range from a plain resistor to a proper active source depending on how much performance is required; an amplified-zener arrangement with a bias resistor gives a current source that is intrinsically short-circuit protected and very low noise.[629] Some Nixie tube driver chips integrate a current source with a bias pin, removing the need for an external dropper resistor.[950] Precision voltage-reference parts can be configured as floating current sources as well as references.[1438]

Instrument front ends contain them too: the Fluke 189/289 proprietary chip is limited to input switching, filtering, a comparator, a buffer and a current source.[15] The DataIO Unisite universal programmer carries a dedicated supply whose only job is to set a clamp voltage on the pin driver output while the fine current source is sinking current, with 12-bit DACs setting the levels.[1060]

## Driving LEDs and other nonlinear loads

An LED's current is an extremely steep function of its forward voltage, so small variations in supply voltage or in forward voltage between nominally identical parts produce large changes in current. This is why every practical LED circuit uses either a series resistor or a current source.[1427] Feeding LEDs directly from a low-impedance bench supply set to their nominal forward voltage leaves the branch current uncontrolled, and mismatched devices in that configuration behave unpredictably.[1427]

A bench current source makes LED characterisation straightforward: a backlight strip in an LCD panel can be run from 0.1 mA up to 90 mA — the instrument's ceiling — with the operating point dialled in directly and a maximum voltage set alongside it.[465] The same approach serves for driving an unknown laptop backlight at a nominal 50 mA when the drive current is not documented,[pKV_JiauAE4] for driving a green LED behind a colour filter,[1690] and for driving an LED down into the picoamp region while counting individual photons at the other end with a single-photon counting module.[869]

The diode-test range of a multimeter is effectively a fixed 1 mA current source, which is just enough to light an LED; selectable test currents would make the function considerably more useful, but essentially no meter on the market offers them.[46]

Multimeters generate current in resistance mode as well, and this can have side effects. The ohms-range current source in a Keithley 177 is specified at a milliamp and drives the internal shunt being measured.[777] Connecting a meter that is inadvertently left in ohms mode across a precision voltage reference injects that current into the reference and can disturb it — a 10.0000 V standard read 10.470 V afterwards.[ZYC763Vx9O8]

## Bench instruments

The Keithley 225 is the general-purpose workhorse of this class, spanning 0.1 nA to 100 mA with a compliance voltage adjustable from 10 V to 100 V, in decade ranges from nanoamps through three microamp ranges to milliamps.[197][1688] Its resolution is limited — three digits of adjustment — which matters when setting an exact test current.[1427] It is used routinely for verifying multimeter current ranges,[372] for characterising Zener diodes,[908] and for exercising the low current ranges of a 6½-digit bench meter down to 1 nA.[489]

For the extreme low end, the Keithley 261 picoamp current source reaches down to 10 femtoamps, with a full-scale ceiling of 100 µA; the two instruments together cover picoammeter calibration across all ranges.[51][197][406] Instruments of this kind are special-purpose rather than general lab equipment, but there is no substitute when very small currents must be generated.[51]

Ordinary bench power supplies also operate as constant current sources in their current-limit mode, covering currents up to the order of amps — the region the low-current instruments cannot reach — though their current setting resolution is typically coarse, in some cases no finer than 10 mA.[197][1688] A resistance decade box driven from a voltage source is a workable improvised current source.[KKEYAdXEW-M] A source measure unit takes the concept further: in the Agilent B2912A a large N-channel power MOSFET both sinks and sources the current, with range-switched sense resistors in the return path, four such sections paralleled to share the dissipation.[607]

## Building a precision current source

A practical precision design consists of a voltage reference across a precision resistor, with an op-amp servo driving a pass element to hold that current in the load. A 1 A design used a 1.25 Ω four-terminal precision resistor with an N-channel MOSFET as the pass device, the reference ground returned separately to the sense terminal.[577]

The difficulties scale inversely with the current. At 1 mA an OPA277-based design is well behaved and essentially noise-free.[579] At 1 µA the same topology is dominated by op-amp input bias current, which subtracts from the output and introduces an error against a target accuracy budget of better than 0.05%.[579] Measured output at 1 µA came out at about 1.027 µA against a computed 0.991 µA from a 9.912 MΩ setting resistor — in the opposite direction from the bias-current error, indicating something other than the intended error mechanism dominating.[579] Apparent output noise at 1 µA reaching 50 mV per division across the sense shunt is dominated by external pickup on the long test leads rather than by instability in the reference itself.[579]

## Process control current loops

The 4–20 mA current loop applies the current source to signal transmission. A two-wire sensor is placed in series in the loop and acts as a current source, with a load resistor, typically 250 Ω, converting the loop current back to a voltage at the receiving end.[DX_f0Cg6pHo] Three-wire variants take a separate 12–30 V DC supply and produce an absolute current output referred to ground.[DX_f0Cg6pHo] Because the information is carried as current rather than voltage, series wiring resistance does not corrupt the reading.
