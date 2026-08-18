# watt hour

The watt hour (Wh) is the unit of electrical energy formed by multiplying power in watts by time in hours.[1009] Energy is the usage of power over time, so its derived units can equally be expressed as kilowatt-hours, watt-hours or watt-seconds, all following from energy equals power times time.[1009] Power is instantaneous and cannot be stored; energy can be, and the watt hour is how a stored quantity of it is stated.[1009] For batteries the watt hour is the only measure that captures the true capacity, because it accounts for both current and voltage rather than assuming one of them.[140][789]

The rating is directly usable: a 1 Wh battery can deliver 1 W for one hour or 0.1 W for ten hours.[140] A 25 Wh cell could potentially deliver 25 W for an hour or 1 W for 25 hours.[1009] A 5,000 mAh lithium polymer pack at a nominal 3.7 V works out to 18.5 Wh, which corresponds to roughly 1 W continuous for eighteen and a half hours.[393]

## Why watt hours and not amp hours

Amp hours and milliamp hours measure charge, not energy, and take no account of voltage.[1648][789] They are a more simplistic figure that only becomes a capacity number once a nominal voltage is assumed across the discharge.[141][140] Battery voltage is not constant — it sags through the discharge and then tapers off before dying — so the watt hour figure is the correct energy capacity precisely because it takes that drop into account.[1009] Quoting energy capacity in milliamp hours is not defensible engineering practice; capacity should always be specified in watt hours.[1371][1732][1649]

The true capacity is the area under the discharge curve — the integral of the power curve over time — not a point on it.[140][1732][789] For a graph of voltage versus time, that integral is what the milliamp hour or watt hour capacity actually represents.[1732]

In practice the two figures often land close together, which is why many batteries are specified in amp hours with a constant current discharge assumed.[140] Under a constant current load the errors introduced by the nominal-voltage assumption tend to cancel in terms of area, so the amp hour capacity at a given constant current can be similar to the watt hour capacity.[140]

Where they diverge is with loads that are not constant current. Most real circuits are neither constant resistance nor constant current but constant power, since a DC-to-DC converter driving a circuit draws essentially constant power from the battery.[140][393] For such a design the constant power discharge graph, and with it the watt hour capacity, is the more relevant characteristic.[140][393] Constant resistance testing — literally a 10 ohm or 100 ohm resistor across the battery — matches almost nothing that gets designed.[140] With a constant power discharge, remaining capacity can be read directly as a percentage off the x-axis of the discharge curve.[789]

## Measuring watt hours

The traditional method is to discharge the battery at a defined load while logging voltage and current at regular intervals, then computing the total watt hour capacity from that data.[140] Each interval yields its own watt hour increment, and the increments are accumulated to a running total.[141][772] Doing this properly requires two differential amplifiers and a means of logging — a data acquisition card into a PC, or a pair of logging multimeters.[141] Amp hour measurement by contrast needs only a battery, a dumb constant current load built from a FET and an op amp, a multimeter and a stopwatch.[141]

A watt hour total can also be reconstructed after the fact. Multiplying average voltage by capacity in milliamp hours gives around 2.6 Wh for an AA alkaline.[708] A CR2032 coin cell at 235 mAh over an average of roughly 2.8 V gives its energy capacity closely enough without integrating the whole curve.[1383] A lithium thionyl chloride cell at 2.6 Ah and 3.6 V nominal comes to 9.36 Wh.[1371] Elapsed time against a known constant load works the same way: 68,625 seconds at a continuous 20 W converts to about 381 Wh.[IXVTMUQGN5U]

Measurement setup matters at the connector. A test taken through a barrel-jack-to-barrel-jack connection with lead and contact losses returns a true minimum figure rather than the highest accurate one; a proper four-terminal measurement at the load would only increase the watt hour result.[IXVTMUQGN5U]

## Instrument support

Watt hour capability is not universal on test gear, and its absence is a real limitation for battery work. Electronic loads that offer only amp hours in their battery test mode force the watt hour calculation to be done manually.[862][lYKjScnkeq0] The Rigol DL3021 displays voltage, current, milliamp hours, watt hours and a timer in battery mode, but while stop conditions can be set on voltage, current and time, no stop value can be set on watt hours.[1023] The Rohde & Schwarz NGP800 performs energy calculation and reads out in watt hours or milliwatt hours.[1293] The Uni-T UTE310 provides an integrate mode that integrates power to produce a watt hour figure over an arbitrary logging period.[1693] Bench meters may offer a dedicated energy mode where the units switch from watts to watt hours or milliwatt hours once a timer starts accumulating.[1009] The µSupply adds a watt hour display alongside a joules readout.[1561]

Recorded test results illustrate the resolution involved: 2.06 Wh for an AA alkaline discharged at 250 mA[141]; 10.38 Wh alongside 8,333 mAh over 8 hours 21 minutes for an NiMH cell[9FCzAgJhRdc]; and 0.024 Wh after 24 seconds at the start of a long alkaline leakage run.[RFb3TwWzza0]

## Input-referred versus output-referred ratings

USB battery banks expose the sharpest consequence of unit choice. A pack labelled 20,000 mAh also carries a watt hour figure — 77 Wh, derived from that charge at the internal cell voltage of 3.85 V — and that watt hour figure is the one intended for comparing packs.[1648] A constant current test at a 5 W load, taking twelve hours, returned 61.8 Wh, well under the 77 Wh spec.[1648]

The discrepancy is a referencing problem. The 20,000 mAh figure is input-referred, or battery-referred: it describes the cell inside, before the DC-to-DC converter that drives the output.[1648] The internal battery may genuinely hold 77 Wh and meet its spec, but the input-referred number excludes converter efficiency.[1648] Measured output-referred energy of 61.8 Wh against 77 Wh input-referred implies an 80% efficient DC-to-DC converter, and the same referencing trick appears across many products where efficiency is left out.[1648]

## Beyond batteries

Domestic electricity is metered in kilowatt hours, the same power-times-time construction.[1009] Solar production is reported the same way: 511 Wh from an eastern-roof panel over a full solar production day, with western-roof panels yielding about 2.5 times more.[5x8UVZnwyL8] For solar surface-area analysis, a peak irradiance figure converts to daily energy through the area under the daily curve — a best-case multiplier of seven turning 90 W per square metre peak into 630 Wh per square metre per day.[632]

Portable power stations are named for their energy: the Goal Zero Yeti 400 is a 400 Wh battery.[1707] Capacity tests on one returned figures close to that nameplate — roughly 400 Wh on one run and 381 Wh on another, and 305.6 Wh over 7 hours 4 minutes before a fault forced a power cycle and lost the accumulated total.[IXVTMUQGN5U][lYKjScnkeq0] At household scale the same arithmetic sizes a grid outage: 41% remaining on a 3,600 Wh reserve.[JSahPkUjDYA]
