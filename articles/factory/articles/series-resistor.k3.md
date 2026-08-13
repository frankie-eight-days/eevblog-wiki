# series resistor

A series resistor is a resistor placed directly in a current path so that the full circuit current flows through it, where it drops voltage, limits current, or shapes the behaviour of whatever lies downstream. It is one of the most heavily used roles a resistor can take: protecting inputs, biasing LEDs, modelling the internal resistance of real sources, and extending the voltage rating of a circuit by stacking several resistors in series.[1397][908][1491][1620]

## Series combination: value, tolerance, and power

Resistors in series add directly: the total is R1 + R2 + R3, however many are in the chain.[1399] A common beginner mistake is assuming the tolerances add as well — that four ±1% resistors in series yield a ±4% part. They do not; the combination retains the same percentage tolerance as the individual parts, so ten 1% resistors in series still give a 1% result.[212][215] Parallel combinations behave differently: with a true Gaussian distribution of values around the nominal mean, paralleling (for example, ten 10k resistors to make 1k) can produce a tolerance better than that of the individual parts.[215]

Power handling also improves in series. In a decade resistance box built from 0.5W resistors, dialling in more sections raises the total dissipation capability to a maximum of 2.5W because the heat is spread across the series chain.[211]

For hand-tweaking values, series combinations are arguably safer than parallel ones: a poorly contacting resistor in a parallel pair can silently leave the lower value slightly out, whereas a failed resistor in a series chain produces a gross, obvious failure.[204]

## The series resistor inside every real source

A real voltage source cannot be modelled as an ideal voltage source alone; in practice it must include a series resistor, which is the essence of the Thévenin equivalent.[1397] This shows up concretely on the bench:

- An arbitrary waveform generator used as a high-resolution DC source has a fixed 50Ω output impedance — equivalent to a precision adjustable supply with a 50Ω resistor in series — and this is unaffected by the high-impedance load setting.[1560]
- Battery ESR can be simulated with a series resistor: a vintage portable computer booted fine at 1Ω and 5Ω of simulated ESR but refused to boot at 10Ω.[1662]
- A microcontroller parasitically powered through a reset pin tolerates series resistance up to a point — still running with several kΩ dimming its LEDs, but dead by 10kΩ.[831]

Series resistance also appears inside measurement setups, where it creates burden: a picoammeter front end with a 10k series resistor into its feedback amplifier exhibits an offset (burden) voltage of around 100µV that must be accounted for in the measurement.[406]

## Current limiting and LED droppers

The classic series-resistor job is setting LED current. When LEDs are paralleled, they do not share current evenly unless matched at the semiconductor level, so a series ballast resistor per string is the general rule; even a single dropper resistor in series with a whole multi-segment display is better than none, though the current is then shared between however many segments are lit.[1491] A worked dropper example: a 7.2V battery driving a 5.6V LED string at 250mA leaves 1.6V across the resistor, giving 6.4Ω by Ohm's law — 6.8Ω as the nearest E12 value — and I²R gives 0.25W dissipation, so a quarter-watt part suffices.[RT3godBXkOg] LED strips use the same scheme, e.g. a 360Ω drop resistor in series with each six-element section.[1617] A series dropper also enables a bidirectional LED indicator across a logic inverter: the LED pair wired between input and output via one series resistor lights one way for a high input and the other way for a low.[242]

A series resistor is equally effective for simply throttling a load: inserting 100Ω in series with a cooling fan both quieted the acoustic whine and dropped the operating voltage substantially.[zoyaHOqp9gI]

## Protection and clamping

Series resistance is the standard first line of input protection because it limits the current that can flow into a device under fault conditions. A logic analyser front end routes each input through a 510Ω series resistor and then through low-capacitance diode clamps to the supply rails; the resistor limits current so the clamps can absorb overloads without damage.[436][759] The same principle protects a programmer/debugger when a line is pulled low externally — the series resistor ensures the tool cannot be harmed.[liWWY5cSs4Q] At the design stage, a series resistor in a supply line to a switch can prevent a shorted external case from destroying the circuit, though it costs an extra part.[GoKbPDADG0c]

Zener-based protection is impossible without a series resistor: the resistor must limit the current into the Zener or the Zener itself blows on overvoltage.[104] The Zener additionally has its own internal dynamic resistance that varies and must be taken into account alongside the external series resistor in a practical circuit.[908] The transistor–Zener clamp (a BJT whose base-emitter junction acts as a roughly 6V Zener in reverse and a 0.6V diode in forward) clamps at about ±6.6V, and only works as a complete protector when a series resistor sits on the input to take up the clamped energy.[1157][1000]

A small series resistor also appears at op-amp outputs for stability and short-circuit protection. A 100Ω series output resistor keeps an op-amp stable into capacitive loads and protects it if the output is shorted; the error it introduces against a 10MΩ multimeter input is negligible, and only becomes a ~0.1% problem once the driven instrument's input impedance falls to about 100kΩ.[72] The caveat is that such a resistor does not truly isolate a capacitive load — it shifts the pole rather than eliminating the stability problem.[l2LBkXxN81Y]

In switch debouncing, the classic RC circuit can generate a large discharge current spike when the switch shorts the capacitor directly; adding a series resistor between switch and capacitor forces the discharge through that resistor instead, typically with a value smaller than the pull-up so the cap still discharges quickly.[961] Series resistors can be omitted entirely where the current is already constrained — for instance inside ICs, where internal constant-current generators limit transistor base current and no series resistor is needed.[555]

## Stacking resistors for high voltage

A single surface-mount resistor has a limited voltage rating, so high-voltage circuits routinely place several resistors in series purely to divide the voltage stress across the chain:

- A grid-tied solar hybrid inverter uses four series surface-mount resistors — each good for a couple of hundred volts — where one through-hole part could have done the job, for grid-voltage sensing.[1620]
- Multimeter high-voltage input strings use two or three series resistors (e.g. three 3MΩ parts) together with PTCs to stand off the input voltage.[1083][1704][3kdYGneg9xI]
- An oscilloscope front end with four large resistors in series indicates a high-voltage path; that is the only reason for the arrangement.[1639]
- An EVSE charger uses a bunch of series resistors to achieve a high-voltage-rated drop for its auxiliary supply.[1507]
- A mains appliance test circuit places three 1206 resistors in series across active and neutral with a relay coil, the series combination meeting the voltage requirement.[1164]
- A 1MΩ series resistor suffices for detecting the presence of mains AC on an alarm panel.[682]

Analog multimeters illustrate the flip side: the meter is essentially just series resistors plus the movement, so on the lowest ranges (e.g. 30µA) the movement is at the mercy of the input, saved only by back-to-back germanium diodes clamping the voltage across it.[634]

## Instrumentation and measurement applications

Decade resistance substitution boxes are built entirely from series chains: each decade has a string of equal-value resistors tapped by a multi-way switch, the decades themselves wired in series, so a six-decade box spanning 10Ω to 1MΩ can dial any value in 10Ω steps up to 10.1MΩ.[97] Lower-cost designs use a 1-2-3-4 arrangement where successive switch positions route through one, two, three, or four series resistors, with a further position shorting one out to reach five.[1586] Deliberately desoldering a series resistor on a board and fitting a two-pin header is a quick way to break into a supply rail for current-consumption measurement.[413]

Elsewhere in instruments:

- An LCR meter drives the device under test from a function generator through an output series resistor, tapping the resulting voltage for amplification and A/D conversion.[81]
- Current shunts in a multimeter can be cascaded in series so all ranges are read from a single tap at the top of the stack, eliminating multiplexer taps.[931]
- A multimeter's low-impedance (LoZ) mode inserts a 1k series resistor plus a PTC in series, which will safely discharge a charged capacitor through the meter itself.[1655]
- A diode-test function with only a couple of milliamps of drive — limited by roughly 2.2k of internal series resistance — may fail to light an LED at all.[1087]
- A transmission-line (Z0) passive oscilloscope probe is nothing more than coax with a 1k series resistor at the tip; the resistor isolates the cable and scope capacitance, which at 1GHz would otherwise present a reactance of only about 1.6Ω for 100pF. The 1k value is the conventional compromise — not so high as to limit bandwidth, not so low as to load the circuit.[1367]
- Series termination resistors on digital lines should be placed physically close to the driving device they belong with.[795]

## Signal-line and bus roles

On digital buses the series resistor defines whether a line can be driven at all: a CAN bus terminated in 120Ω cannot be driven through two 10k series resistors, which simply lack the drive capability to assert the bus.[1181] Series resistors on I²S clock and data lines provide convenient probing points — the signals can be identified by touching one side of each resistor without knowing the pinout.[1322] Capacitive touch sensing relies on a series resistor feeding the touch pad: finger capacitance to ground forms an RC time constant with the resistor, so a 16-key touch interface needs 16 series resistors, which can be embedded as carbon resistors directly on the flat-flex to save board space.[1166] A series resistor from the wiper of a trimmer can also be used to narrow the effective adjustment range of a calibration control.[647]