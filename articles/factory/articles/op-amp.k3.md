# op amp

The operational amplifier (op amp) is a DC-coupled differential amplifier with extremely high open-loop gain, designed to be operated inside an external negative-feedback network that defines the actual closed-loop behaviour of the circuit.[600][932] The name reflects the original application in electronic analog computers, where such amplifiers performed mathematical operations — addition, subtraction, multiplication, and the like.[854] Because the bare gain is enormous, poorly controlled, and temperature-dependent, it is unusable on its own; negative feedback converts that unwieldy gain into accurate, stable amplification set by a few passive components.[600]

## Idealised behaviour

Two rules of thumb make closed-loop op amp circuits analysable by inspection. With negative feedback present, the op amp drives its output to whatever voltage is required to force its two inputs to the same potential, and its high-impedance inputs draw negligible current from the source.[600][1116][221] The output is low-impedance and can source a reasonable current — milliamps to tens of milliamps for ordinary parts, and a couple of hundred milliamps for power op amps.[600]

A consequence that confuses beginners is the virtual ground: in the inverting configuration the summing node is held at the non-inverting input's potential, so a signal probed on one side of the input resistor appears to vanish at the node and reappear at the output.[600]

## Standard configurations

- **Buffer / voltage follower:** output tied directly to the inverting input, giving unity gain with high input impedance and a low-impedance output capable of driving loads from a sensitive source.[600]
- **Non-inverting amplifier:** a feedback divider from output to inverting input to ground sets a precise, stable gain from the raw open-loop gain.[600]
- **Integrator:** a capacitor in the feedback path with the input referenced to ground produces an integrator, the core of dual-slope ADCs used in digital multimeters.[485]
- **Difference amplifier:** a single op amp with a four-resistor network forms the standard differential stage, used in everything from current-shunt measurement to high-voltage differential probes; a three-op-amp instrumentation version appears in thermocouple cold-junction compensation ICs with a trimmed internal temperature sensor.[1415][1688][419]
- **Comparator:** an open-loop op amp works as a comparator — e.g. as a zero-crossing detector or a supply current-limit latch — although a purpose-built comparator such as the LM311 is usually the better choice.[941][221][471]
- **Howland current pump:** five resistors and a voltage reference around one op amp generate a constant current in the few-to-tens-of-milliamps range for driving LEDs or sensors where efficiency is unimportant.[xUKf-4rv_sQ]

Unused sections of dual and quad packages should be properly terminated rather than left floating.[600] Switching gain by breaking the feedback path turns a stage into a unity-gain follower, but inserting switches into the feedback path carries traps for the unwary.[931]

## Key parameters

### Input offset voltage

Input offset voltage (V<sub>OS</sub>) is an internally generated error inherent in all op amps, including ultra-low-offset parts; it cannot be measured by simply placing even a 6½-digit multimeter across the input pins.[476] A general-purpose part exhibits millivolts — the LM358 runs to several millivolts — while a precision bipolar part such as the OPA227 holds 10 µV worst case.[259][579] Chopper (auto-zero) amplifiers reach about 1 µV, and the best parts on the market approach 0.1 µV.[72][476] Offset is multiplied by the closed-loop gain: 1 mV of offset in a ×100 amplifier produces 100 mV of output error, which is why a ×100 current-shunt amplifier resolving microvolt-level signals essentially forces the choice of a chopper part such as the MAX4238/4239.[72][1318] Even a 5 µV-offset part becomes significant when trip thresholds sit below a millivolt.[584] Where residual offset must be eliminated entirely, a chopper amplifier is the standard remedy.[579]

### Input bias current

Small currents flow into or out of the input pins. They generate offset across source resistances, set the droop rate of peak-hold capacitors once diode leakage is eliminated, and can reverse direction over the supply-voltage range, making compensation impractical — the realistic options are to accept the error, fix the operating point, or choose another part.[479][490] Femtoamp-input parts exist, and picoamp-input precision parts such as the LT1012 are used where leakage dominates the error budget.[490][1334] Bias current also drifts with temperature.[101]

### Noise

Input noise is specified as a voltage density in nV/√Hz and splits into two regimes: inescapable flicker (1/f) noise dominating below roughly 10–100 Hz, and flat Gaussian white noise above it — so op amps are noisier toward DC, not quieter.[528] Datasheets quote spot noise at 10 Hz, 100 Hz, and 1 kHz precisely to allow comparison across the 1/f corner, but headline banner specs are chosen to flatter and the graphs must be compared directly.[528] Representative figures span from about 40 nV/√Hz for a TL072, through 4 nV/√Hz for an NE5534, down to 0.88 nV/√Hz for an LME49990.[528][541] Verifying state-of-the-art low-noise parts requires a measurement preamplifier quieter than the device under test.[528]

### Gain-bandwidth and cascading

Gain-bandwidth product varies between individual units of the same part, with supply voltage, and with test frequency, so a design needs margin — pushed to the limit, the op amp begins to distort.[572] Cascading two lower-gain stages yields more total bandwidth than a single high-gain stage; total noise is dominated by the first stage, so maximum gain belongs at the front end.[572] This is the technique used to extract bandwidth from cascaded chopper amplifiers in precision current measurement.[1318]

### Common-mode rejection

An op amp's own CMRR commonly exceeds 100 dB and is rarely the limiting factor: in practical differential amplifiers and probes, resistor-divider matching dominates and can drag the system CMRR down to 40 dB or less.[1521]

### Supply rails and output swing

±15 V is about the upper supply limit for ordinary op amps; rails of ±21 V or more exceed what jellybean parts tolerate.[168][731] Classic parts such as the LM741 cannot swing near either rail, so outputs clip well short of the supplies.[600] Single-supply parts accept inputs at — and slightly below — the negative rail and drive the output to ground, which is essential when the signal source is a 0–2 V DAC referenced to ground.[238] Rail-to-rail CMOS parts handle low-voltage designs but many are limited to 5.5–6 V total supply.[dv0B_WqL7w4][660][661] Where the output must swing both polarities about ground, a split supply is required; a part run from ±1.5 V simply perceives a 3 V single supply.[72]

## Stability and capacitive loads

Op amps generally do not tolerate large capacitance on their outputs, which can push the feedback loop into oscillation.[577] A series resistor between the output and a capacitive load such as a MOSFET gate is the standard isolation measure, but it does not magically decouple the load — the capacitance still shifts a loop pole.[304][l2LBkXxN81Y] Substituting a different manufacturer's LMV321 into an existing design has caused outright oscillation, cured more cleanly by bypassing the virtual-ground divider on the input side than by hanging capacitors on the output.[1697][n7XX75S98e8] Loops that enclose pass transistors — current sources, regulator error amplifiers — likewise oscillate if not stabilised, particularly at high load current.[577]

## Failure modes

Applying an input voltage beyond the supply rails destroys the input stage: feeding 10 V into a part powered from a 6 V rail kills the input op amp, and unruggedised inputs are the usual enabler.[727] Failed op amps typically go short or low-impedance internally, draw excess current, and run hot, making a thermal camera — or a finger — a first-line diagnostic.[593] Because everything shares the rail, one supply overvoltage event can kill dozens of op amps spread across a board.[540][593]

## Applications

- **Regulator error amplifier:** the op amp drives a series-pass transistor so the divided-down output equals the reference, which is the regulation mechanism of linear supplies.[861][90][221]
- **Constant-current sources and loads:** op amp, pass transistor, and shunt give I = V<sub>REF</sub>/R<sub>SHUNT</sub>; a bench dummy load needs little more than an op amp, a MOSFET, and a few resistors, with op-amp output offset setting the minimum achievable current.[1688][772][102] A precision reference such as the REF102 plus a precision resistor and an OPA227 yields a microamp-class current source.[579]
- **Precision rectifier:** placing the diode inside the feedback loop makes the op amp absorb the diode drop in real time, compensating for temperature and diode quality.[490]
- **Peak detector:** a precision rectifier charges a storage capacitor; a smaller capacitor tracks faster but droops more, the op amp spends the inter-peak time slammed against the negative rail and must recover, and a following buffer presents a low-impedance source to an ADC.[490]
- **Negative-rail generation:** a diode charge pump can produce a low-current negative supply for op amps from a single rail.[483]
- **Audio:** the JRC 4580 is the classic dual audio op amp at 0.05 % typical distortion; the OP275 uses a Butler front end combining JFETs and bipolars with 9 MHz bandwidth; in a large mixing console, thousands of op amps at 5–10 mA each make quiescent current a supply-design issue in its own right.[ag-MjKAfATw][738][840]
- **High-speed and high-current output:** current-feedback parts such as the THS3095 (210 MHz, high-voltage, high-current) serve as function-generator output stages, and some current-feedback amplifiers have remained available only in DIP packages.[497][1005]
- **Composite amplifiers:** enclosing one amplifier inside another's feedback loop combines their strengths — a chopper front end for microvolt offset wrapped around a high-current output buffer, or a power audio amplifier enclosed in an op-amp loop for extremely low distortion — a technique largely absent from textbooks.[1609][vwAhHz7Zpzk]
- **Capacitance multiplier:** an op-amp variant of the transistor capacitance multiplier works, but is constrained by the op amp's limited output current and gain-bandwidth.[1116]

## Choosing parts

If any specification genuinely matters to a design, the correct approach is a purpose-selected part rather than a jellybean; thousands of op-amp types exist precisely because requirements differ.[1697] High-end instruments reflect this, using many different op amps each chosen for a specific role rather than one type throughout.[718] Jellybean parts — the LM358 with its ground-sensing inputs, or the TL071/072/074 JFET family common in oscilloscope front ends — are acceptable where millivolts of offset are irrelevant, but even a jellybean-adjacent part like the LMV321 has caused failure when swapped across vendors.[259][824][511][1697] There is no single go-to op amp in professional practice, because each new design optimises around different constraints.[97]