# input bias current

Input bias current is the small DC current that flows into or out of the input pins of an operational amplifier or comparator, in violation of the ideal-op-amp rule that no current flows in or out of the inputs.[600] It is one of the real practical limitations that separates the first-pass ideal analysis — still the method professionals use as a first approximation — from measured behaviour on the bench.[600] Because the current has to flow through whatever resistance is connected to the pin, it develops a voltage that the amplifier then treats as signal, and in a high-gain stage that error is multiplied by the gain.[479]

## Magnitude by input technology

The size of the bias current is set almost entirely by the input stage technology, and the spread between technologies is enormous.[1436] A bipolar input design draws nanoamps to tens of nanoamps.[1436] A FET input stage is around three orders of magnitude lower, typically ±1 pA with a maximum spread out to ±120 pA on a jellybean part, with input offset current down around 500 fA.[1436] A CMOS input can be as low as 10 pA typical.[1436] The precision bipolar OP07 family, chosen as a step up from the LM358 or LM324 on offset voltage grounds, still draws nanoamps rather than picoamps, and that is one of its major downsides.[1436]

CMOS leakage is so small that it is impractical to test and guarantee in production; parts are screened on a go/no-go basis for input bias current rather than measured, and a device with every unit individually tested carries a price premium.[1325] At the one-picoamp level the parameter is normally irrelevant unless the design is genuinely ultra-critical.[1325]

The same ordering applies to comparators. A bipolar LM311 has 300 nA input bias and 70 nA offset current — acceptable unless the source impedance is high.[1464] The 301/391A sits at 25 nA bias and 5 nA offset.[1464] A dual bipolar part runs 3.5 nA.[1464] A CMOS comparator moves the whole specification into the picoamp region, typically under 100 pA, with the maximum only barely reaching the nanoamp range over the full temperature span.[1464]

At the extreme, the ADA4530 is a FET input amplifier with femtoamp input bias current, and it carries an on-chip guard amplifier that actively drives a guard trace to match the input voltage, so that PCB surface leakage from contamination or moisture never sees a potential difference to leak across.[1755]

## How bias current becomes output error

The mechanism is direct. If the input bias current is 30 pA flowing into the inverting pin, and there is no voltage drop budget elsewhere, that whole 30 pA flows through the 100 kΩ feedback resistor: 30 pA × 100 kΩ = 3 µV of error at the input.[479] With a stage gain of 100, that appears as 300 µV at the output — which matched a measured output offset of just over 300 µV on an AD8628 circuit whose input offset voltage specification was only about 1 µV.[479] The AD8628 is specified at typically 30 pA input bias current with a maximum of 100 pA, and the figure is higher in the quad package because of the process technology used to put four amplifiers on one die.[479]

This is why an unexplained output offset should not be attributed to VOS alone. Any observed input offset issue is typically a combination of the true input offset voltage — an entirely separate datasheet parameter — and the input bias currents flowing in the surrounding resistors.[479] The two can be comparable, and either can swamp the other depending on the part and the impedances chosen.[479]

The complementary case is a low-impedance design, where bias current simply does not matter. With 25 nA input bias current, an amplifier takes effectively nothing from the input, and 100 kΩ source resistors can be used without concern.[471]

## Input offset current

Input bias current is not one number but two, because IB+ and IB− differ. The input offset current, IOS, is the difference between them, and it must be read alongside IB.[479] A part can have a very low input bias current — 10 pA, say — and still be unusable if IOS is 100 pA, because there is then no bias resistor value that will cancel the error.[479] An individual chip in an individual circuit might be trimmed to work, but no generic resistor value will do it across parts.[479]

Datasheet reading has to be careful about the sign as well as the magnitude. When Texas Instruments revised the NE5532 datasheet, a plus-minus was added to the typical input bias current specification, meaning a parameter that had previously been implicitly one polarity could now be either — a change with real consequences for a design that relied on the original behaviour.[1752]

## The balance resistor and its limits

The standard fix for the inverting configuration is to return the non-inverting input to ground through a resistor RB rather than connecting it directly to ground, so that the bias currents in the two inputs develop matching voltages and cancel.[479] The value is RF in parallel with R1.[479] Where the gain is 10 or more and RF is ten times R1, RB ≈ R1 is close enough.[479] The same matching resistor appears in production inverting front ends, though it is not mandatory — the non-inverting input can simply be grounded.[1415]

The cancellation is never complete. The input transistors are not a matched pair, so the two bias currents are never precisely equal; some op-amps get very close, but the residual is not zero, just as the bias current itself is never zero regardless of input topology.[479] For ultra-precision work there is no easy solution: the circuit has to be trimmed to account for the actual bias currents, and on top of that the offset voltage still has to be dealt with.[479] The combination of IB, IOS, VOS, input topology and circuit impedances can get genuinely ugly, and it can bite circuits that do not look critical at first glance.[479]

The alternative to trimming is to design the sensitivity out. Dropping the surrounding resistor values by an order of magnitude makes the IB term small enough that the VOS term dominates; on the AD8628 circuit, reducing the resistors and using a 100 Ω bias resistor brought the output error down to an average of 50–60 µV, which is what the roughly 1 µV input offset voltage predicts at a gain of 100.[479]

## Supply and common-mode dependence

Nulling with a trimpot works, but only at one operating point. Substituting a 500 Ω trimpot for the fixed bias resistor allows the error to be tweaked out completely and held stable, but the setting is valid only for that particular supply voltage and common-mode input range.[479] Change the rail and the null is gone.[479] In a chopper-stabilised amplifier with an undisclosed internal ping-pong architecture, neither VOS nor the input bias currents stay consistent over the supply voltage range, and the currents can go in either direction on either input.[479] The options are to accept the variation over the supply range, to fix the supply at one voltage, or to choose a different amplifier.[479]

One further caution: if the bias resistor is large, its thermal noise becomes a problem, and it may need to be bypassed with a capacitor.[479]

## Measurement

Input bias current can be measured directly, though not easily. Using a Keithley picoammeter on its 1 nA range, the current into the non-inverting input of an AD8628 through a 100 Ω bias resistor measured about 1620 pA at a 5 V rail.[479] Lowering the supply changed it: by 3.5 V it had fallen almost to zero, and at 2.7 V it had reversed direction entirely.[479] The measurement is noise-sensitive and a casual bench setup will not give the lowest noise figure.[479]

## Selecting parts

Input bias current is a specification to weigh against the others rather than a veto. On a part where the competing device is far better on bias current, 70 pA is worth considering but probably not a show-stopper; a chip would not be discarded on that basis alone unless the application is ultra-critical, and bias current can reasonably be traded away for higher bandwidth and lower noise.[1325] In one datasheet comparison the OPA189 won in many categories and often by a wide margin, and input bias current was the single parameter where the competing 4239 won decisively.[1325] Where the parameter does drive the choice, it is because of the surrounding impedances: measuring across a 10 kΩ source impedance on a nanoamp range demands a low input current, and the parts in question specify around 1 pA typical with 2 pA maximum input offset current.[1325]

Instrument front ends reflect this. A precision thermocouple amplifier such as the LT6010 is chosen partly for its roughly 100 pA input bias current.[417] A chopper amplifier selected for a precision bench measurement was specified at 100 pA input bias current, which was good enough that the parameter was not a concern for the application at all — the offset voltage and its 2 nV/°C drift mattered far more.[476] The Agilent 34461A's design notes claim best-in-class input bias current alongside noise and injected current, compared against three unnamed competing instruments.[485] Where a divider is driven by precise FET input op-amps drawing only picoamps, the loading on a trim pot is irrelevant, and in any case a measured-and-compensated calibration absorbs whatever bias current loading exists.[584]

## Circuits where it dominates

Two circuit classes are especially exposed. A precision low current source built around two op-amps cannot deliver its nominal output current to the load, because the op-amp input bias currents divert a fraction of it — a precise 10 V across a precise 10 MΩ resistor gives a precise 1 µA in the resistor, but not 1 µA into the load.[579] The datasheet bias current figure, for an OPA2277 in that design, is the number needed to quantify the shortfall.[579]

A peak detector holding charge on a capacitor is the other case: for an ultra-precision application that can tolerate no droop at all, the op-amp input bias current discharges the hold capacitor.[490] That part of the problem is solvable by choosing an amplifier with femtoamp input bias current; the harder residual problem is the reverse leakage of the peak-detector diode once the output falls and the diode is effectively returned to ground.[490]
