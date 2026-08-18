# output ripple

Output ripple is the periodic AC component that rides on the DC output of a switching converter, charge pump, or regulated supply. A DC-to-DC converter does not produce a flat line at its nominal voltage; connecting an oscilloscope to the output shows a repeating charge-and-discharge waveform at the switching rate rather than a steady level.[110][483] Because ripple is a designed-in quantity rather than an accident, it is chosen as a specification at the start of a converter design and then used to size the output components.[110]

## Where it comes from

In a switching converter the output capacitor is charged during the switch-on interval and discharged into the load between pulses, and the resulting sawtooth is the ripple.[483] The same mechanism is visible directly on a microcontroller-driven charge-pump inverter, where the capacitor charging and then discharging can be watched on the output waveform.[483] Ripple amplitude therefore depends on the switching frequency and on the capacitor values: raising the frequency, raising the capacitance, or both produces a smoother output.[483] Driving such an inverter at 10 kHz can remove visible ripple entirely, while dropping to 1 kHz into the same load makes it severe.[483]

Because switching frequency is what sets the component values, converter chips that look interchangeable are not. Substituting a different brand of switcher generally still functions, but the inductor and capacitor values chosen for one part may give more ripple on the output with another, along with operation at a different point on the efficiency curve.[1475]

## Sizing the output capacitor

Ripple enters the design as a target. In a 5 V to 15 V, 100 mA boost design the accepted figure was 100 mV.[110] The output filter capacitor follows from nine times the output current multiplied by the on-time, divided by the allowed ripple; with 100 mA, an on-time of 7.3 µs and 0.1 V of ripple, the result is 66 µF.[110] The measured result at no load was roughly 200 mV peak against a 100 mV target, and the ripple changed as load was dialled in.[110]

Where the calculated capacitor is not enough, an additional LC section on the output is the standard remedy: in the same design a second 33 µH inductor and a further 100 µF capacitor were added as an optional output filter.[110] On a bench supply, bolting a larger capacitor across the output likewise cut the low-frequency ripple from a couple of hundred millivolts peak-to-peak toward the 50 mV specification, though the higher-frequency switching content survived the treatment.[1298] High-frequency spikes are a separate problem from low-frequency ripple and respond to different measures; on an isolated USB supply, an RFI suppression capacitor of 1 nF between primary and secondary knocked down part of the switching noise.[324]

## The ESR floor

Capacitance cannot be increased without limit. Beyond a certain point the equivalent series resistance of the capacitor dominates, and since a higher capacitance in a given package size implies a higher ESR, adding capacitance stops reducing ripple and eventually becomes counterproductive.[1115] There is consequently a minimum ripple that filtering alone can reach, and fitting a thousand microfarads does not drive ripple to zero.[1115] Where a lower figure is genuinely required, the answer is post-regulation — a low-dropout regulator on the output, a Zener, or an RC or LC filter stage.[1115]

The ESR relationship also runs in the other direction as a diagnostic. Aged output capacitors that have gone high-ESR produce excess ripple on the output even under light load, and that excess ripple can be enough to trigger hiccup mode in the supply's controller.[1726]

## Load, temperature and mode dependence

Ripple is not a single number. It scales with output current, so a quoted figure is meaningful only against a stated load, usually full load.[1265][1298] Datasheet curves carry the same caveat: a graph showing output ripple versus input voltage may omit the output current it was taken at, and the plotted figures assume particular capacitor values — for charge pumps typically a nominal 10 µF output capacitor and 10 µF switching capacitor — so the ESR of the actual capacitor used changes the result.[1115] Reading a peak-to-peak figure off such a graph and assuming the chip will deliver it is a trap.[1115]

Curve families plotted against ambient temperature show the ripple at a fixed load current climbing steeply as temperature moves, so a design verified at one temperature and one operating current can behave very differently at another — a particular hazard for circuits with two distinct current modes.[1115]

The sharpest discontinuities come from converters that change operating mode. A traditional 7660-style charge pump has a single mode of operation and its ripple rises roughly linearly with output current.[1115] Parts with a light-load pulse-frequency-modulation mode do not: the LM2776 allows the charge pump to switch less below 40 mA of output current to cut quiescent draw, and at that mode boundary the output ripple can rise by a factor of four or five, from around 20 mV to 80 or 100 mV peak-to-peak.[1115] A step from 80 mV to 120 mV may be tolerable in a design that post-regulates the rail, but the transition is abrupt and appears exactly where light-load operation is expected to be benign.[1115]

Frequency boost options work the other way. Running a 7660-class inverter at a boosted switching frequency can give around 50 mV peak-to-peak at 10 mA output where the plain ICL7660 gives about 200 mV; a 2 MHz switching frequency in this family implies low output ripple.[1115] At the low end of the range, capacitive inverters can reach figures an external LDO would struggle to match: under 1 millivolt in one case, and 4 mV peak-to-peak for a small negative-bias generator running from a 3 to 5 V supply and delivering perhaps 10 mA.[1115]

## Measurement and specification

Ripple is measured AC-coupled at the output, typically at 100 mV or 50 mV per division.[110][324] Both peak-to-peak and RMS figures are used and they are not interchangeable: one bench supply showed 78 mV peak-to-peak alongside 6 mV RMS, still half its specified figure.[1691] Manufacturers usually bound the measurement bandwidth, a variable-frequency converter specifying less than 500 mV RMS over a 20 Hz to 20 MHz bandwidth.[449] On a well-behaved switching supply the low-frequency ripple can be essentially absent, leaving only content at the switching frequency itself, 120 kHz in one 360 W bench supply.[1691] Quoted figures span a wide range by class: less than 50 mV at full load on a 2000 W supply,[1298] 100 mV on a low-cost 360 W bench unit,[1265] less than 75 mV peak-to-peak of ripple and noise at a rated 400 mA on a small isolated DC-DC module,[324] and just under 500 µV AC RMS on a 100 W USB-C supply.[1606] Oscilloscope power-analysis packages treat output ripple as one of a standard set of converter measurements alongside efficiency, inrush current, switching loss, transient response and PSRR,[209] and a full characterisation of a converter brick means sweeping ripple across the whole input-voltage and output-current envelope rather than measuring it at one operating point.[895]

Ripple also rises sharply when a converter is pushed past its rating: a 2 W isolated module run at 3 W kept regulating and restarted cleanly, but its output ripple increased drastically.[324]

## Ripple as a symptom

A low ripple figure is not on its own evidence of a healthy output. Adding output capacitance to a linear regulator whose error amplifier was oscillating reduced the visible variation to roughly half a millivolt, from about 370 mV to 368 mV, while the op-amp continued to oscillate underneath — the capacitance hid the symptom rather than fixing the instability.[95] Similarly, an offline LED driver with a 330 µF output capacitor showed clean output ripple while drawing 24 W at a power factor of 0.58, a defect the ripple measurement gave no hint of.[1253]
