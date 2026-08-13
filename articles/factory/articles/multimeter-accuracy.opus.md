# multimeter accuracy

Multimeter accuracy is the guaranteed bound on how far a meter's displayed reading may sit from the true value, published by the manufacturer as a percentage of reading plus a fixed number of least significant counts.[75] It is conventionally quoted for the DC volts function, because that is the range a meter is best at and the figure by which instruments are compared and classed.[75][72] Accuracy alone is a poor way to choose a meter: beyond about 0.5% on basic DC volts, most day-to-day electronics work is limited by other things entirely — battery life, stability, measurement confidence, build quality and safety — and additional digits are a bonus rather than a requirement.[75]

## How the specification is written

An accuracy figure is meaningless without the counts term that follows it, and a meter can advertise an attractive percentage while pairing it with a poor plus-counts number.[75] The two terms combine differently across the range: on the Uni-T UT71E a spot check came out roughly 0.04% out against an Agilent bench meter, apparently failing its 0.025% class claim, but the full specification is 0.025% plus five counts, and once the counts are included the reading is inside the limit.[712] The same arithmetic explains readings that look wrong at a glance — a meter 14 counts out on a 6 V mode was still within its published spec, even though a unit fresh from the factory at laboratory temperature would be expected to sit only a few counts off.[1731]

Accuracy is also only specified over a stated temperature band, typically a narrow window around room temperature such as 19 to 23 degrees, with a separate temperature coefficient governing behaviour outside it.[930] One older meter specified 0.2% of reading plus 0.1% of full scale, with a tempco of 0.2% per 10 K from 0 to 55 degrees.[481]

There is a direct relationship between basic DC volts accuracy and the number of counts or digits a meter displays, and the two are supposed to track each other.[75] A 6,000 count instrument specified at 0.3% is proportionate to its resolution; where such a meter carries a plus/minus 5 digit term, tighter models in the same family may drop to plus/minus 3 digits, so the individual model number matters more than the family.[973] Where the relationship breaks the other way it is a selling point: the Fluke 27 is only a 3,200 count, three-and-a-half digit instrument, yet specifies 0.1% plus one count on DC volts, against the 0.5%, 0.3% or at best 0.2% normally offered at that resolution.[372] The retro Fluke 37 shares essentially the same specification.[1393] The Meterman 37XR combined 0.1% DC volts with 10,000 counts, making it nearly the equal of a four-and-a-half digit meter for readings between 3,000 and 9,999.[6]

## Accuracy classes

Instruments fall into recognisable classes. Handheld meters of four-and-a-half or five-and-a-half digits, and low-end bench meters, occupy the 0.05% class; a six-and-a-half digit bench multimeter belongs to the 0.005% class, equivalent to 50 ppm, and high-end specifications are often quoted in ppm directly.[1184] Ordinary handheld meters cluster at 0.5% basic DC volts.[72][1420][813] Pocket meters are half a percent to one percent class instruments and are not the tool to reach for when absolute accuracy is the point.[1083][Iwy8UVVQNkA]

Adding money does not automatically buy accuracy. In a survey of $100 meters, the extra fifty dollars over the $50 class bought no increase in resolution or accuracy at all: still 6,000 or 4,000 counts, all at 0.5% basic DC volts.[99] Accuracy is likewise not the reason Fluke handhelds command their price — competing meters match or beat them on the specification sheet.[ay9wFQAW19Y]

At the upper end, the Fluke 45 specified 0.025% plus two counts across every range from 300 mV to 1,000 V for one year, with no relaxation on the millivolt range.[791] The Prema 6047 published 24-hour drift figures around half a ppm, 90-day accuracy of 0.004%, one-year nominal accuracy of 0.007% on DC volts and as low as 0.009% on resistance.[613]

Analogue meters occupy a different scale entirely, where 1% is a good result.[633] Among classic analogue instruments the Unigor Metrawatt held the tightest figure at 1% on ohms and DC volts, against 2% for the Simpson 260 and about 1.5% for the Triplett.[634]

## Accuracy by function

DC volts is always the best function on a multimeter, and on some designs the millivolt range is better still; it is more accurate than resistance, current or capacitance, and a decent meter will at least bring ohms close to the DC volts figure.[75] Typical handheld ratios show the pattern: 0.5% DC with 1% AC, 1% ohms and 4% capacitance on one budget unit,[1351] 0.5% DC with 0.8% current and 1% resistance on another.[1420] The Fluke 28 Series II specifies 0.05% plus one count on DC volts with 0.2% on both ohms and current.[64] Current ranges on mid- and low-end meters are generally the weakest, which is a recurring practical limitation.[72]

Where the ratio is badly out of proportion it is worth noting. The UT71E, claimed as a 0.025% class instrument, offers only 0.3% plus eight counts on its best resistance range, degrading to half a percent on the 400 k range and one percent at 1 meg.[712] AC accuracy is usually accompanied by a bandwidth limit, and a true RMS meter that runs out at 1 kHz is of limited use.[1351][1731]

## What sets the accuracy in hardware

The two components that determine both accuracy and long-term stability are the main voltage reference and the resistor network that divides it down for the various ranges.[171] In a quality handheld this is a laser-trimmed thick film network on a hybrid substrate, shielded and with multiple contacts.[171] Precision, very low aging resistors — half a percent parts including the high-value ones — are what make an accurate analogue meter possible.[634]

A 0.5% class meter does not need any of that. At that performance level standard parts give perfectly acceptable drift, and a precision low-drift divider network would be overkill; its absence from a meter in the $50 to $200 class is expected rather than a defect.[344] Cheap instruments can nonetheless behave better than their specification if the reference is decent: a $25 meter substantially exceeded its accuracy specification, though a single sample is no guarantee of the population.[1007]

## Verification and drift

Checking a meter means feeding it a known value from a calibrated source — a DC voltage standard, a low-voltage reference that has itself been compared at a standards laboratory, or a 0.1% decade resistance box for the ohms ranges.[341][1578][1351] A quick cross-check against a second, known-good meter of the same model can confirm agreement to within one least significant digit.[JI4b-7vpIDc] Applying exactly 30.00 V to a group of meters at once makes the spread visible: some spot on, some reading a little high or low, all still inside their specifications.[91]

A meter that reads consistently high or low by the same proportion on every range and every function points at the reference rather than at any one signal path. A 4,000 count Metrix reading 1.1% out on the millivolt range was equally 1.1% out on the 10 V range, on ohms and on current — the signature of a drifted main reference or a drifted overall calibration.[1578]

Good meters hold their calibration for a very long time. Original Fluke 70 series instruments almost always still work and are almost always still within specification decades on, with only a couple of digits of error on the current ranges.[1424] A Fluke subjected to water ingress still read 1 k spot on afterwards and so remained within specification.[66]
