# frequency sweep

A frequency sweep is the systematic variation of a stimulus signal's frequency across a defined range while the response of a system under test is recorded, producing a response-versus-frequency curve rather than a single-point measurement.[343][859] It is the fundamental method behind Bode plots, impedance-versus-frequency graphs, filter characterisation, EMC scans and mechanical vibration qualification, and the swept stimulus is what makes the frequency response obtainable at all.[343][859][1442] The technique is instrument-agnostic: the same result can be had from a dedicated network analyser, a spectrum analyser with a tracking generator, or a bare function generator, a sine source and a multimeter working through the range by hand.[620]

## Sweep parameters

A sweep is defined by a start frequency, a stop frequency, a number of points, and a sweep time. The range is chosen from what is already known or suspected about the device: a probe circuit expected to roll off around 6.5 MHz is swept from 1 Hz to 20 MHz so the corner sits comfortably inside the span, with 1,000 points being ample resolution.[1445] An amplifier expected to reach about 300 kHz of bandwidth is swept from 10 Hz to 1 MHz, giving margin on both sides of the roll-off.[692] The axis is normally logarithmic when the span covers several decades, as in an impedance plot running from 100 kHz to 60 MHz.[859]

Common spans follow the physics of the domain rather than the instrument. Bypass capacitor impedance work runs to 60 MHz.[859] A programmable filter with a 100 kHz upper limit is swept to exactly that ceiling.[620] Acoustic measurement uses the audio band, 20 Hz to 20 kHz.[IVWhoGFJQAY] CMRR measurement of an amplifier front end runs 50 Hz to 10 MHz.[1521] A spectrum analyser with a tracking generator can sweep the instrument's full span, for example zero to 1.5 GHz about a 750 MHz centre.[343]

## Sweep time and the low-frequency penalty

Sweep time is not free, and the cost concentrates at the bottom of the range. Low frequencies require long dwell per point, so extending a start frequency downward disproportionately lengthens the run: dropping a network analyser's start to 1 Hz can push a sweep into the minutes, and the slowdown is visible as the sweep crawls through the first part of the span.[1103] For this reason a practical lower bound is chosen deliberately rather than set to the instrument's minimum.[1103]

The same tradeoff governs receiver bandwidth. Narrowing the receiver bandwidth — for instance from 300 Hz down to 30 Hz — cleans up a measurement that is down in the noise and improves accuracy, at the direct cost of a slower sweep.[1103] In EMC conducted emissions work the recommended sweep speed for a full scan can imply roughly 16 minutes of acquisition; restricting the frequency range, in one case to 0 Hz to 1 MHz, brings the automatic sweep time down to around 200 seconds, which is far more workable for iterative pre-compliance testing.[548]

## Establishing the response curve

Interpreting a swept response requires knowing that the fixture itself is flat. The standard procedure is to run the sweep first with a known component in place of the device under test — replacing a capacitor with a plain resistor alongside the existing 10 ohm shunt — and confirm the measured response is flat before trusting any structure seen with the real part fitted.[859] Cabling, BNC connectors and adapters all contribute at high frequency, and without this reference run their artefacts are indistinguishable from device behaviour.[859]

Where a swept sine source is unavailable, broadband random noise substitutes: driving a filter with 1 V RMS of random noise into a dynamic signal analyser yields the same transfer function without a sweeping generator.[620]

## Instruments

**Spectrum analyser with tracking generator.** The tracking generator output follows the analyser's own sweep across its entire span, and it is that synchronised sweep which produces the frequency response of the circuit under test.[343] A swept superheterodyne analyser also differs in kind from an FFT-based measurement, physically sweeping across frequency rather than transforming a captured record.[845]

**Vector network analyser.** Gain-phase and impedance measurements, including reflected S11, are configured as a start-stop pair with a chosen receiver bandwidth — 10 Hz to 20 MHz, or 100 Hz to 50 MHz over the full range.[1103] Impedance analysers extend the same swept approach to material properties, including dielectric constant and permeability, and to DC bias characterisation of capacitors.[wjMIsM4sDw8]

**Function generator plus oscilloscope.** A Bode plot can be obtained without a network analyser by driving a sine sweep and tricking the oscilloscope into displaying frequency on its horizontal axis: a generator in sine sweep mode set to a 1 second sweep from 1 Hz to 100 kHz makes the horizontal time axis a proxy for frequency.[396] Modern oscilloscopes integrate this directly, pairing a built-in function generator with a Bode plot function, in one case a dual-channel 100 MHz generator.[1717] Sweep is a near-universal mode on signal sources, appearing alongside modulation and burst on RF signal generators, bench function generators, and scope-integrated generators.[823][CMoBGGqojqs][cziiWo6Uh5M][351] The sweep parameter need not be frequency alone; amplitude, offset, symmetry and phase can each be swept over time.[692]

The value of the feature is measured by its controls. An instrument that cannot sweep or modulate its generator, and therefore cannot produce a Bode plot, is functionally rudimentary regardless of price — a criticism levelled at a six-thousand-dollar integrated instrument.[876] Sweep implementations that expose only a centre frequency and span, with no settable start frequency, are similarly limited.[LbqnHtNPt9Y]

**Simulation.** SPICE AC analysis is a frequency sweep in software, specified identically by sweep type (linear or logarithmic), point count, start frequency and stop frequency.[1445]

## Sweeps outside the electrical domain

**Mechanical vibration.** Electrodynamic shakers sweep a PCB or product over a frequency span, typically from a few hertz up to around 10 kHz, in each of three orthogonal axes in turn, to identify vibrational modes.[1442][1443] A reference accelerometer stays on the shaker plate to characterise the system itself, and additional accelerometers are then mounted on the product; the resulting sweeps are compared against a military or in-house vibration standard.[1443] Dips in the response are candidate mechanical resonances, though the setup must be validated before such features are attributed to the product.[1443]

**Acoustics.** Room and monitor measurement sweeps 20 Hz to 20 kHz, and repeating the sweep — eight passes averaged, at roughly 43 seconds total — yields a better result than a single pass.[IVWhoGFJQAY]

**EMC.** Both emissions and immunity work are swept. A wide conducted-emissions sweep localises where a design is marginal, in one case identifying problems below roughly 2.5 MHz with the spectrum above that dropping off acceptably.[548] Near-field magnetic loop probes are reciprocal: the same loops used to pick up fields can be driven with a swept signal to generate a field and inject it into a product, testing immunity across frequency rather than at a single point.[694]

## Sweeping as a servo mechanism

Sweeping is also used as a dither for locking rather than as a measurement in itself. In a rubidium frequency standard the RF interrogation signal is swept by a couple of hundred hertz around the 6.834 GHz hyperfine transition of rubidium; at resonance the atoms absorb light, the photocell behind the resonance cell sees less of it, and the transimpedance amplifier's output becomes an error voltage the loop servos on to hold lock.[235]
