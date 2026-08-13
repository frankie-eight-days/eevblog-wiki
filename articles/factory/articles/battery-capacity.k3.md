# battery capacity

Battery capacity is the ability of a battery to supply a constant current or a constant amount of energy into a load for a given amount of time.[140] It is not a single fixed property of a cell: the figure obtained depends on the discharge current, the cutoff voltage chosen, the temperature, and the age and history of the cell, so the number printed on a battery label is only a nominal value valid under particular test conditions.[140][708][9FCzAgJhRdc]

## Amp-hours versus watt-hours

Capacity can be specified in two ways: amp-hours (or milliamp-hours) and watt-hours.[140][141] The amp-hour figure is a measure of charge, not energy; it is obtained by assuming a constant nominal voltage across the discharge and so does not account for the fact that cell voltage tapers off rather than staying flat and then dying suddenly.[1009][1648][140] The true measure of a battery's energy capacity is the watt-hour figure, which is the total area under the voltage-versus-time discharge curve.[140][1009][789] A 25 Wh battery can in principle deliver 25 watts for one hour or 1 watt for 25 hours.[1009]

Because milliamp-hours are only meaningful at a stated voltage, quoting them without a voltage is a common marketing device. USB power banks rated at, for example, "20,000 mAh" use input-referred capacity taken at the internal cell voltage (around 3.85 V), corresponding to 77 Wh; the energy actually deliverable at the USB output is lower once converter efficiency is accounted for.[1648][1649] The same distinction applies to larger storage products: a unit advertised as 3.6 kWh holds that energy in its internal cells, while the output-referred figure measured at the AC socket was about 3.285 kWh at a 1 kW load, varying with the inverter's efficiency curve.[uxm3qeKcg3w]

## Dependence on discharge conditions

### Discharge rate

Delivered capacity falls as discharge current rises, because internal equivalent series resistance (ESR) dissipates energy as I²R loss inside the cell.[lYKjScnkeq0][1732][hSkaZEgrZkY] A typical AA alkaline cell delivers a nominal ~2,800 mAh at a 25 mA drain but only about 1,200 mAh at 500 mA; at 100 mA the figure is roughly 2,200–2,500 mAh depending on brand.[140][708][j_eaXfmRB8Q] AA cells should generally not be loaded beyond about 1 A because ESR losses dominate.[hSkaZEgrZkY] The relationship is not strictly monotonic in all chemistries: one heavily aged lithium-ion cell returned slightly more capacity at 500 mA than at 250 mA, an effect attributed to the cell's electrochemistry rather than its (still low) ESR.[1732]

Charge and discharge rates are conventionally expressed as a C-rate, a multiple of the rated capacity: for a 2,100 mAh cell, 1C is 2.1 A.[35] Lithium-ion cells are typically charged at around 0.5C, with some permitting 1C or faster.[176]

### Temperature

Low temperature severely reduces alkaline capacity: cells that deliver their full rated capacity at 21 °C lose more than half of it at 0 °C, with the loss greatest at high discharge currents, because the cell's internal series resistance rises as temperature falls.[140] Lithium chemistries outperform alkaline markedly across the same range.[140]

### Shelf life and ageing

An alkaline cell retained at 21 °C retains roughly 80% of its initial capacity after seven years, though actual figures depend on manufacturing quality and cannot always be relied on.[140] Lithium coin cells self-discharge at very low rates — a CR2032 is quoted at 0.12% per month.[900] Cycle life and calendar age erode rechargeable capacity gradually; a Panasonic lithium-ion cell tested after roughly 20 years and over a thousand cycles still delivered 280–286 mAh against its 680 mAh rating, just under half its original capacity, and remained usable.[1732] Fresh, in-date branded cells can also fail to meet their own datasheet: a Duracell Procell AA with four years of shelf life remaining delivered just over 2 Wh at 250 mA, falling short of its specified nine hours to 0.8 V.[141]

## Discharge curves and cutoff voltage

The standard characterisation of a cell is its discharge curve: terminal voltage plotted against time or against extracted capacity at a given load.[176][140] Alkaline cells have a sloping, non-flat curve that falls off a cliff near 0.8 V per cell; by 0.8 V roughly 95% of the capacity is gone, and below 0.5 V essentially nothing usable remains.[140][1296][1331] Lithium-ion cells have a much flatter curve, and a 3.0 V cutoff captures 95–99% of their capacity; graphite-anode cells are treated as dead around 3.0 V, older coke-anode types around 2.5–2.7 V.[393][176][lYKjScnkeq0] Coin cells such as the CR2032 (nominal 225–245 mAh) fall off sharply at 2 V with nothing left under the curve beyond it.[900][1680][1383]

The cutoff voltage designed into a product directly determines how much of the stored capacity is actually used. A product cutting out at 1.2 V per alkaline cell throws away roughly half the battery's capacity; even a 1.1 V cutoff wastes a visible slice of the area under the curve.[140][772][972] Recommended design targets are operation down to 0.8 V for a single alkaline cell, 1.6 V for a two-cell product, 3.2 V for three- or four-cell products, and 4.8 V for a 9 V battery.[140] Equipment that cuts out high — 9 V multimeters dying at 6.5–7 V are a cited example — discards a substantial fraction of the capacity paid for.[140][200] Products designed around rechargeable cells typically cut out near 1.1 V and thereby use 80–90% or more of the cell's capacity; low-self-discharge NiMH cells such as Eneloops reach 90–99%.[751] One bench-review practice consequently includes measuring a product's actual battery cutout voltage as part of assessing its design quality.[140] The engineering conclusion is that claims of "80% wasted energy" recoverable by add-on boost devices presuppose pathologically bad product designs with cutoffs near 1.35–1.4 V; against real products the recoverable excess is at best 10–20%.[751][772][963]

Datasheets specify capacity against one of three load types — constant current, constant resistance, or constant power — and all three may appear on the same sheet.[140] Constant current is the most common and underlies amp-hour ratings.[140]

## Measuring capacity

The standard measurement discharges the cell at a controlled load into a defined cutoff voltage while integrating current (for mAh) or power (for Wh) over time; programmable electronic loads with a battery mode automate this, accumulating both figures with selectable stop conditions on voltage, capacity, or time.[1023][393][9FCzAgJhRdc] Some battery chargers expose the same function, computing accumulated capacity during a discharge-recharge cycle.[811] Commercial analysers such as the Cadex C7000 measure capacity alongside internal resistance and perform chemistry-specific reconditioning on in-service cells.[1434] For estimating the capacity a given product design will waste, the remaining energy is read off the discharge curve as the area between the product's cutoff voltage and end of discharge.[772] Pack-level state-of-charge displays are often non-linear — one large unit sat at "1%" while delivering a further ~800 Wh — a problem avoided by coulomb counting, which logs charge in and charge out directly; smart batteries such as Sony's InfoLithium implement this internally.[uxm3qeKcg3w][625]

## Verification of rated figures

Independent discharge testing routinely checks label claims:

- An RS Components D-size NiMH cell rated 8,000 mAh delivered 8,333 mAh (10.38 Wh) over 8 h 21 min at a 1 A load, exceeding its rating.[9FCzAgJhRdc]
- A years-old Goal Zero Yeti 400 delivered essentially its full 400 Wh nameplate at a 4 A load, and again at a gentler 20 W constant-power load.[lYKjScnkeq0][IXVTMUQGN5U]
- An AllPowers R1500 station rated 1,150 Wh delivered 924.8 Wh at a punishing 1,100 W load, with the shortfall attributed to the extreme discharge rate.[WFhk1aRqLD8]
- Branded D-size NiMH cells from Energizer (2,500 mAh) and Duracell (2,200 mAh) were found on disassembly to contain cells far smaller than the can — with the remaining volume empty — versus the 8,000 mAh that size can hold; the cells do meet their printed ratings at the stated discharge rate, so the practice is legal but relies on buyers not comparing figures across brands.[1200]

## Recovery, pulsed discharge, and misuse effects

A rested, apparently exhausted cell recovers open-circuit voltage — a drained alkaline may sit back up at 1.3 V or more — but this reflects electrochemical relaxation, not regained capacity; only a small additional amount of charge can be extracted.[865][pa8j-Lje_2o][1023] Discharging intermittently rather than continuously does recover measurably more total energy, however: a cell rated at 1,400 mAh on a continuous 100 mA discharge yielded 1,630 mAh when drained in separated sessions with recovery periods.[789] Mechanically compressing a drained alkaline AAA cell in a vice before a second discharge increased the additionally extractable capacity from 140 mAh to 261 mAh, about a 19% improvement in overall capacity in that test.[865]

When cells of unequal capacity are discharged in series, the weakest cell empties first and is then reverse-charged by the others, driving its terminal voltage negative; this occurs readily with mixed brands or partially drained cells and is a reason not to series-connect mismatched batteries.[hSkaZEgrZkY][1274]