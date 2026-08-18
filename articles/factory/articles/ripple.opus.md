# ripple

Ripple is the residual AC component riding on a nominally DC supply rail, left over from rectification or from the switching action of a converter.[594][512] It is distinct from, though usually measured alongside, high-frequency noise: on a captured waveform the low-frequency content is the ripple and the fast spikes on top are noise.[594] Because ripple is an AC quantity sitting on a DC average, a rail can measure correct on a meter's DC average and still be badly wrong — the DC number stays put while the AC component changes.[379][512]

## Measurement

Ripple is measured AC-coupled, since the whole point is to strip the DC average and expand the small AC residue.[594][1203] Triggering on it is awkward at low amplitudes; noise reject helps, and the mains AC line makes a usable trigger source for rectifier-derived ripple.[594] Where the variation is small compared to the rail, window triggering set just outside the normal operating band will catch excursions that ordinary edge triggering cannot.[512] On high-voltage rails such as a bulk capacitor at several hundred volts, a differential probe at 100:1 keeps the measurement inside the scope's input range.[630] Instrument power-analysis packages fold ripple measurement in alongside power modulation, safe operating area and switching loss.[199]

A dual-display meter showing AC and DC simultaneously is enough for a quick survey of many rails: a rail reading 5.3 V with 10 mV of AC, or 12.8 V with 26 mV, or 46 mV on another, is healthy and not worth pursuing.[780] Sub-volt logic core rails on a working board typically show no measurable ripple at all.[780]

Manufacturer specifications give the threshold that matters. The 5 V digital rail of a Tektronix 2465B is specified at 150 mV peak-to-peak; a measured 350 mV is out of spec and a legitimate suspect for misbehaviour elsewhere in the instrument.[1203]

## Ripple as a diagnostic

Excess ripple on a rail points either to a degraded reservoir capacitor or to something drawing more current than the supply can deliver, and the two are distinguishable. A failed capacitor produces a large amount of ripple; if a rail has sagged badly — 4 V where 5 V is expected — but shows hardly any ripple, the capacitor is not the fault and the rail is being dragged down by excess load that the output winding cannot support.[804] The converse case, a rail carrying far more ripple than it should even after a much larger capacitor is fitted, indicates something loading it down rather than a filtering deficiency.[1301]

This is why blanket capacitor replacement on a board whose rails all measure clean is unwarranted: with no measurable ripple and correct voltages, the fault lies elsewhere, in a dry BGA joint or the digital section.[780] Confirming a suspect capacitor directly is a matter of ESR, measured at 100 kHz.[1714]

One important limitation: a board powered from a bench DC supply rather than from its own mains front end has no ripple to observe, so ripple-based reasoning about input bypass and reservoir capacitors does not apply in that configuration.[1243]

The consequence of ripple depends entirely on what the rail feeds. A rail feeding 5 V logic, or feeding a local 3.3 V regulator downstream, will generally tolerate tens of millivolts without trouble; failures traced to modest ripple usually involve some more subtle sensitivity in one particular part of the circuitry.[512]

## Sources of ripple

In a rectifier-and-capacitor supply the ripple frequency and shape carry information about the topology. A 4.5 V rail showing 22 kHz ripple identifies the converter's switching frequency directly, and a second rise within each cycle betrays full-wave rectification from a second coil.[284] Where the ripple is at mains frequency, it originates in the rectified line.[594]

In a switching converter, ripple amplitude tracks both load and operating mode: the ripple waveform visibly changes character as the converter shifts modes with load, and peak-to-peak amplitude varies with it.[110] A converter measuring almost 200 mV peak-to-peak is high against a calculated target but not necessarily out of the ballpark; adding the intended output inductor and capacitor cleans the no-load ripple to the point where a 20 mV/div scale is needed to see it.[110]

Charge pumps and voltage doublers ripple as a direct function of switching frequency, because the frequency sets how far the capacitors discharge between pumps. Raising the frequency makes the ripple disappear; lowering it brings back both ripple and droop, visible from around 4 kHz down, and 1 kHz is unusable. Around 10 kHz serves as a working rule of thumb for these circuits.[473] Where the resulting DC feeds analog circuitry, a linear regulator downstream is the usual remedy.[473]

Inadequate output capacitance for the claimed output power leaves a supply unable to hold ripple down under load.[893] At the opposite extreme, more output capacitance is not simply better: the design target is the lowest output capacitance that still keeps ripple low, because stored charge in a large output capacitor is dumped into the load when the supply transitions into constant-current mode, before the control loop can respond.[1691] Bulk capacitor voltage must also be chosen with the ripple trough in mind — a rail whose minimum sits at 46 V leaves plenty of margin.[512]

## Filtering and attenuation

Filtering ripple out is a chain, and the weakest link dominates. In a PWM-derived control voltage, removing output capacitance and reducing a filter capacitor allowed the full switching ripple to pass straight through to the output; adding a second RC stage of 10 kΩ and 100 nF dropped it very significantly even with almost no output filtering.[225] The cost is bandwidth: a 10 Hz filter cutoff means the output voltage cannot be changed quickly, which is acceptable for a manually adjusted knob but not for fast programming.[225] As a design target for a control rail, 1 mV of ripple transferred to the output may be acceptable, but better than that is the sensible goal.[225]

A capacitance multiplier — a pass transistor with an RC on its base — multiplies the effective filter capacitance by the transistor's current gain. With a 470 mV peak-to-peak input ripple at 1.59 kHz, the output came out around 310 mV, close to the −3 dB value of roughly 330 mV, so the achieved cutoff sat far above the 15.9 Hz predicted from the multiplied capacitance.[1116] At 100 Hz the residual is small but still visible at 2 mV/div.[1116] The governing trade-off is the series resistor: raising it from 1 kΩ to 10 kΩ starves the transistor of base current and increases the voltage drop across the pass device, but improves ripple attenuation by the RC ratio, to the point where the ripple disappears into the noise floor.[1116] Replacing the single transistor with a Darlington pair raises the gain, permitting a larger resistor for a given capacitance and better low-frequency attenuation.[1116]

## Ripple and light output

In LED lighting, supply ripple appears directly as flicker, because LED current follows the rail. A driver using secondary-side constant-current regulation with substantial filter capacitance is not entirely ripple free but has little enough that it will not visibly flicker.[1252] Linear LED drivers with no ripple on their output cannot produce strobing at all; where flicker is present in such an installation, PWM dimming rather than supply ripple is the mechanism.[361]

## Simulation

Ripple is visible in simulation as the steady-state condition that follows the initial ramp: the differential voltage across a pass element is higher during ramp-up than after settling, and what remains at steady state is the ripple.[260]
