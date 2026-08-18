# peak to peak voltage

Peak-to-peak voltage is the value measured from the bottom of a waveform's negative excursion to the top of its positive excursion — the full vertical span of the signal, rather than its displacement from a reference.[1417] It is one of four ways an AC waveform is commonly quantified, alongside peak, average, and RMS.[1417] It is the easiest of the four to read off an instrument and the one most bench measurements are quoted in, but it is also the least informative: it captures the extremes and discards everything in between.[1417]

## Definition and relation to peak and RMS

Peak voltage is the maximum excursion in one direction relative to the waveform's reference point, which is usually but not necessarily zero, and is abbreviated PK or simply P.[1417] Peak-to-peak spans both directions at once, so for a symmetrical waveform it is exactly twice the peak value.[1417]

The conversion to RMS runs through the peak value: RMS equals peak divided by the square root of two, or equivalently 0.707 times the peak.[1417] Using the square root of two rather than the rounded 0.707 gives a more precise answer.[1417] Rearranging that relation recovers peak from RMS, and the peak-to-peak figure follows from the peak; the various direct RMS-to-peak-to-peak conversions are all derivable from the one formula, so only one need be memorised.[1417]

## What the figure does not tell you

Peak-to-peak carries no information about waveform shape whatsoever.[1417] A signal that reaches plus one volt and minus one volt has a 2 V peak-to-peak amplitude whether it is a perfect sine, a triangle, a square wave, or a pair of narrow spikes with a very poor power factor.[1417] Average and RMS values differ precisely because they take the shape of the waveform into account; peak-to-peak is only the instantaneous extreme.[1417]

The practical consequence is that peak-to-peak and average figures are useless for computing power dissipated into a resistor — they give the wrong answer, and in the average case zero.[1417] For power, RMS is the only correct measure.[1417]

## Ripple and noise specification

The output of a switchmode converter is not a flat line but a rail with ripple riding on it, and the quantity of interest is the peak-to-peak excursion of that ripple.[110] For a 15 V supply, 100 mV of ripple is a reasonable design target.[110]

Supply manufacturers lump ripple and noise together into a single specification and, on good supplies, quote both a peak-to-peak figure — absolute maximum peak to absolute minimum — and an RMS figure.[594] The RMS value is always the lower of the two, so a supply that quotes only RMS is quoting the more flattering number.[594] The gap can be large: one 360 W bench supply specified 12 mV RMS at low load with no peak-to-peak figure given at all, and measured 137 mV peak-to-peak against 5 mV RMS at a 5 V output.[1691]

Peak-to-peak ripple measurements are also the most vulnerable to probing error. A measurement of roughly half a volt peak-to-peak of noise on a bench supply at 6 amps — just over 500 mV — turned out to be a probing mistake rather than a fault in the supply, with the genuine low-frequency ripple only about two divisions, or 40 mV.[1266] Common-mode pickup from lab lighting is a similar trap, capable of turning an expected figure into roughly 4 mV peak-to-peak of apparent supply noise that disappears when the lights are switched off.[509] Because noise couples in as spikes, peak-to-peak is the aspect of a noise measurement most affected by external disturbance, while the RMS figure moves far less.[1607]

## Measurement on an oscilloscope

Automated peak-to-peak measurement is a standard entry in the measure menu of essentially every digital oscilloscope, usually alongside period, frequency, mean, cycle RMS, rise and fall time, and overshoot.[480][1501][199] Instruments differ in how they label it; a display reading VP for peak-to-peak invites confusion with peak, where VPP would be unambiguous.[480] Scopes will track the value live and update it as the signal changes.[143]

The measurement fails if the waveform does not fit on screen. With only eight vertical divisions available, a 4 V peak-to-peak sine wave scaled to fill the display can push a couple of samples outside the window, at which point the scope simply refuses to calculate a peak-to-peak value.[1226] Backing off the vertical sensitivity restores the reading.[1226]

Because peak-to-peak is a min-to-max statistic, it is sensitive to noise and sampling error, and statistics modes report a standard deviation alongside the mean to show the spread.[1226][878] A measurement showing a mean of 4.24 V with a 25 mV standard deviation is reporting a 25 mV spread across the individual measurements, not a 25 mV uncertainty in the signal itself.[1226] Averaging and high-resolution acquisition modes are compared by exactly this metric: resetting the statistics and running out to a thousand averages over two thousand waveforms gives a standard deviation on the peak-to-peak value of around 17 mV in normal mode.[878]

Two further traps recur. An engaged 20 MHz bandwidth limit will attenuate the signal and produce a peak-to-peak reading — 120 mV where the vertical scaling clearly implies more — that makes no sense against a times-one probe setting.[1492] And a value boxed on screen may not be the live peak-to-peak reading at all; on one instrument a figure taken for 120 mV peak-to-peak was a different quantity entirely, with the actual peak-to-peak lower.[1492]

Peak-to-peak is also the natural readout for checking an instrument against a known source. Setting a generator for 40 mV peak-to-peak and confirming exactly four divisions at 10 mV per division verifies vertical gain calibration directly.[208] The same comparison works in reverse: a generator nominally producing a small amplitude may be well off, with a signal marked 10 mV peak-to-peak actually measuring 4.7 mV peak-to-peak, an error to be expected at that level.[196]

## Typical bench figures

Peak-to-peak is the working unit for specifying test signals and for characterising what a circuit produces:

- Low-noise oscilloscope front ends are compared by their peak-to-peak noise floor: around 440 microvolts on one instrument, 536 microvolts on another set to 200 MHz bandwidth to match a comparison.[e4wvxWWMla0][1612]
- Power supply ripple and noise measured on a scope's statistics readout runs to almost 20 mV peak-to-peak against a 2.6 mV average on a typical supply.[594]
- Analog scopes resolve down to 10 mV peak-to-peak with visible undulation on the trace at 1 mV per division.[502]
- A high-voltage probe measurement sweeps peak-to-peak values in the hundreds of volts, with clipping becoming visible around 600 to 700 V.[1414]
- The coil drive in a small motor product measures just over 13 V peak-to-peak, with ringing on both rising and falling edges.[284]

## Amplitude as a design variable

Where a circuit's function depends on drive amplitude, peak-to-peak is the figure that matters. An LCD driven from a ground reference with 5 V logic gets 5 V of swing; strapping the backplane so the LCD's effective zero sits mid-supply gives plus and minus 5 V, or 10 V peak-to-peak total, from the same 5 V logic level.[1045] The same trick on 3.3 V logic yields 6.6 V peak-to-peak, enough to drive practically any LCD at high contrast.[1045] Where a display's contrast is inadequate, the fault may be DC offset rather than amplitude — the peak-to-peak drive level can be identical and still not work.[1045]

Peak-to-peak amplitude also defines the limits of a part or instrument. Clipping is identified by feeding a known peak-to-peak signal in and watching where the output stops following: 15 V peak-to-peak into a pair of 5.1 V Zeners produces clear clipping, clamped slightly above the nominal Zener voltage by the forward drop of the additional diode.[908] Oscilloscope ADC dynamic range is found the same way, by lowering the input amplitude in steps — 8.8 V peak-to-peak, somewhere between the 10 V that clips and the 8 V that does not — until clipping just disappears.[6qjqhnQiQXQ] A true-RMS meter's tolerance of high crest factor waveforms is tested by sweeping the generator amplitude in peak-to-peak terms, where a generator restricted to peak-to-peak output prevents setting the level in RMS at all.[972]

Signal generators are usually specified and set in peak-to-peak, and their capability falls off with frequency: an instrument delivering 20 V peak-to-peak at 1 MHz cannot sustain that output higher up the band.[323] Short-pulse work is quoted the same way — a 5 ms, 5 V peak-to-peak pulse into a 50 ohm source is a signal for an oscilloscope rather than a multimeter, which is not designed to capture events that brief.[cBNOxg8Px8M]
