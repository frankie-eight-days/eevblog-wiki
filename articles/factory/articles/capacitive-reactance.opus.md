# capacitive reactance

Capacitive reactance is the opposition a capacitor presents to alternating current at a given frequency, measured in ohms and usefully thought of as an AC resistance.[1367][1715][1660] Its magnitude is X<sub>C</sub> = 1 / (2πfC), with frequency in hertz and capacitance in farads, so the opposition falls as either frequency or capacitance rises.[1718][1367][859] It matters because any stray or parasitic capacitance in a circuit — probe tip capacitance, coax capacitance, the capacitance of a load — stops being negligible once the frequency is high enough, and the DC picture of the circuit ceases to describe it.[1718][1367]

## Formula and complex form

The magnitude form 1 / (2πfC) is equivalently written 1 / ωC, where ω is the angular frequency in radians per second.[1660][1473] In complex notation the reactance of a capacitor is 1 / (jωC), which on extracting the imaginary part becomes −j(1 / ωC).[1660][1470] The negative sign is the substantive part: inductive reactance is positive j, capacitive reactance is negative j, and the sign is what distinguishes the two when they are added into a single impedance.[1728][1660]

A worked case: a 20 µF capacitor at ω = 500 rad/s has a reactance of −j100 ohms, and that complex value stands in for the capacitor at that one frequency in an otherwise resistive analysis.[1661] Resistors are unaffected by frequency and carry through unchanged, so a 10 ohm resistor remains 10 ohms in the frequency-domain version of the same circuit.[1661]

## Relation to impedance

Reactance is not the same thing as impedance.[1660] Impedance Z is the total equivalent AC resistance, formed by adding the real resistance in ohms to the reactance in ohms as a complex sum: Z = R + jX for an inductive branch, Z = R − jX<sub>C</sub> for a capacitive one.[1728][1730] Once the resistive and reactive parts are combined, the L and C subscripts are dropped and the result is written simply as Z = R + jX.[1728]

The sign of the imaginary part therefore identifies the character of a network at a frequency: an impedance such as 15 − j20 ohms is primarily capacitive, while one with a positive imaginary component is primarily inductive.[1729][7v-WfiFrFMM] The same distinction appears in the time domain through the mnemonic CIVIL — current leading voltage indicates a predominantly capacitive reactance, current lagging voltage a predominantly inductive one.[1730] For a pure capacitor the current leads the voltage by 90 degrees.[1660] The distinction also shows up graphically: on a Smith chart, a capacitive input impedance plots on the lower half, the inductive side being the upper half.[1715]

Susceptance is the reciprocal of reactance, in siemens; capacitive susceptance B<sub>C</sub> is 1 / X<sub>C</sub>.[1728] AC Ohm's law applies unchanged, with impedance in ohms equal to AC voltage divided by AC current.[1728][1660]

## Probe and instrument loading

The most direct consequence of capacitive reactance in bench work is oscilloscope probe loading. A probe's 10 megohm input impedance is a DC figure only; above DC, the tip capacitance must be run through the reactance formula to find what the circuit actually sees.[1718][1367] A probe with 13 pF of input capacitance presents 24.5 ohms at 500 MHz rather than 10 megohms.[1718] A 500 MHz passive probe specified at 11 pF of total system capacitance — the capacitance seen with the probe plugged into the scope — loads the circuit with about 29 ohms at 500 MHz.[1367]

The same arithmetic explains the bandwidth of a ×1 probe. The 15 pF of scope input and probe capacitance works out to roughly 1 kilohm at 10 MHz, and the 100 pF of coax capacitance to about 159 ohms at the same frequency, so the nominal 1 megohm input is shunted by those far lower values.[453] The series resistance of the probe working against that input capacitance is what sets the upper frequency limit, with the −3 dB point falling around the 0.707 crossing near 10 MHz.[453]

Capacitive loading degrades amplifier response for the same reason: a nanofarad of load capacitance is enough to destroy the response of a low-current front end at a few hundred kilohertz, because the reactance at that frequency is small.[l2LBkXxN81Y] An LCR meter can be misled the same way, reading a component as dominantly resistive when it is measuring a capacitance at a high test frequency where 1 / jωC has become small.[1473]

## Capacitors as frequency-dependent impedances

A real capacitor is not a pure reactance. Its model is ESR in series with the capacitive reactance and with the equivalent series inductance — effectively an RLC network capable of resonance.[33][859] Capacitive reactance falls with frequency while inductive reactance rises with it, so the impedance-versus-frequency curve is dominated by the capacitive term at low frequencies and by the inductive term at high frequencies, with total impedance being the sum of ESR and both reactive contributions.[33][859]

## Capacitive dropper circuits

Because an ideal capacitor dissipates no power, a capacitor can replace a dropping resistor in a mains-powered supply and drop voltage without the heat.[1482] A capacitor whose equivalent resistance is 14.5 kilohms dissipates effectively zero, against 3.7 watts that would be wasted in a resistor doing the same job — the only loss being the very small contribution of the equivalent series resistance.[1482]

The design depends on the capacitor holding its value, since X<sub>C</sub> is evaluated at the mains frequency: 50 Hz in Australia.[1482][1481] If the capacitance drifts low, the reactance rises and the voltage delivered downstream falls, which is the failure mechanism behind a mains capacitor–zener regulator producing roughly half its expected output when a 220 nF capacitor has degraded.[1482] The arrangement is not strictly a capacitive divider, but it requires the capacitor to hold a specific value to present a specific AC resistance.[1481]

Reactance and impedance are often used interchangeably in casual usage, but capacitive reactance refers to the contribution of the capacitor alone.[1482]
