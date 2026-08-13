# solar power system

A home solar power system is a grid-connected rooftop photovoltaic installation: an array of panels on the roof, one or more inverters converting DC to mains AC, isolation and metering hardware in the switchboard, and increasingly a battery and a monitoring layer on top of it all.[484][724][1651] It matters because it is the one piece of generating plant an ordinary household actually owns and can measure, and because almost every interesting engineering question about it — sizing, clipping, shading, payback, self-consumption — only becomes visible once long-run data is logged.[724][1086][1386] Rooftop photovoltaics are a mature, simple and reliable technology whose economics are nonetheless borderline, requiring a long service life to pay back at all.[743][1234]

## Anatomy of a representative installation

A 3 kW system installed in Sydney in June 2013 consisted of 12 LG Mono X panels of 250 W each feeding an SMA Sunny Boy TL3000-21 inverter.[484][724][938][1086] The panels were rated 250 W with a peak voltage of 30.77 V and 8.13 A; the connectors carried a do-not-disconnect-under-load warning.[484] The property was single phase with a 60 A main incoming fuse and underground service wiring.[484] Physical installation of the 12 panels took roughly four hours and was contracted out rather than done by the owner.[484]

Placement of the inverter matters as much as placement of the panels. The inverter was deliberately mounted on the shaded side of the house, screened by a large tree, so that it receives no direct sunlight — direct sun is precisely what an inverter should not be installed in.[724] The consequences of the opposite choice were visible on the hardware itself: an isolator box exposed to sun had yellowed noticeably compared with the shaded one, while the roof penetrator's rubber showed no deterioration.[724]

A later expansion added a 5 kW Enphase microinverter system using 14 LG 370 W panels. To make roof space, the original 3 kW array was moved from the eastern roof to the western roof, with all racking, wiring and the original Sunny Boy inverter reused, giving a nominal 8 kW total.[1426] A western array is less efficient than an eastern one but still contributes morning output, so retaining it was worthwhile.[1426] Because the two arrays run as two entirely independent systems feeding back into the same house, monitoring and metering became substantially more complicated.[k2_mJtAeaog][1386][1390]

Subsequent rounds of work — a third installation after roof changes — replaced the non-hybrid Sunny Boy with a hybrid inverter, added a two-string inverter reaching a combined peak of about 5.8 kW, and added further panels on a pergola driven by Hoymiles microinverters, so that three separate PV systems coexist on one property.[1628][I7wMkLJgnko][1516][BXVgk-uoxn8][3hHG_WcJtQo]

## Power versus energy

A system's kilowatt figure is a power rating, not an energy figure: a 3 kW system can generate 3 kW in ideal sun, which is what it is rated at.[1009] Describing a home as having a 3 kilowatt hour solar system is a units error, since energy is what is billed and what accumulates over time.[1009] The distinction is easy to slip on even when the difference is understood, and getting the terminology right is a precondition for any sizing or payback calculation.[1009][1086]

## Output shape and seasonal behaviour

Ideal daily output rises from around 7 a.m., peaks near midday or early afternoon, and tapers off; the shape is what matters for energy calculations, because usable energy is the area under that curve rather than the peak.[632] The shape is independent of the particular panels or system size, which makes a single measured day generalisable.[632] In the southern hemisphere the annual curve is inverted relative to northern expectations: a system commissioned in July 2013 shows monthly output climbing to a December peak and falling away again.[724]

Winter output is not trivial. A nominal 8 kW installation peaks around 4 to 4.5 kW in midwinter.[WtGlolw-BxA] On a clear late-winter day such a system delivered a textbook curve, dropping off rapidly from about 4:40 p.m., and was still able to take a battery from 30% to 98% while running a pool heat pump on maximum for most of the day.[iztOfT0CX1k] Even on a heavily overcast, raining day, roughly a kilowatt remains available from an 8 kW nominal system — enough that a heat pump hot water cycle need not draw on the grid or on stored energy.[iavM2IqueM8] The counterexample is a severe storm, which cut output on an otherwise perfect summer day to 150 W.[WtGlolw-BxA]

## Inverter clipping and DC-to-AC ratio

Pairing 295 W microinverters with 370 W panels caps per-panel output at 295 W regardless of irradiance.[WtGlolw-BxA] Across 14 panels this clips the array at 4.13 kW, and the measured limit came in at 4.172 kW, consistent within measurement error.[1386] The system therefore cannot exceed roughly 4.12 kW despite being a nominal 5.1 kW array.[1386]

How often that limit bites is an empirical question answerable from logged data. Over 1,980 days of five-minute-sampled output from the original array, the nominal 3 kW system reached a full 3 kW on only about seven days, though it came close on many more.[1386] Scaling the same irradiance history to the new array — justified because both use LG panels at the same location and orientation, rated at 1,000 W per square metre — predicts clipping on 796 of 1,980 days, close to 40%.[1386] Days clipped is not the same as energy lost, which is a harder analysis, since each individual peak within a day must be accounted for.[1386]

Deliberately under-sizing the inverter relative to the array, giving a DC-to-AC ratio above 100%, is common practice and especially so in lower-irradiance countries; the original 3 kW system sat exactly at 100%.[1386] The judgment is economic rather than technical: whether it is worth paying for a larger inverter to capture a peak that only appears on a few dozen days a year.[1386]

## Shading

Shading losses are disproportionate to the shadow that causes them. A very slight, diffuse shadow cast by an antenna cable across the panels produced a 20% drop in output from a home system — a magnitude that intuition does not predict from so subtle a shadow, and which follows from how bypass diodes partition a panel.[NoIjTK249D0][1426] Ordinary environmental shading is also significant: afternoon shading can shut a system off entirely, and trees at the end of the day pull down a whole string.[1356][dKOmNkVLUAA] Shading level is a standard input to sizing calculators for solar-coupled loads.[oWi6pgg1W1A]

## Grid interaction and voltage rise

Exporting into the mains raises local mains voltage, and where an entire street is fitted with solar the effect compounds. Adding a 5 kW array wired in parallel with an existing inverter inside the same house was the leading hypothesis for an unexplained output loss, investigated by logging mains voltage every 10 seconds at a nearby power point.[1426] Feeding energy back to the grid carries many practical constraints beyond the generation itself, and these apply to any distributed generation scheme.[632]

Under net metering, only exported energy is paid for, and the export rate is far below the import rate — as little as 8 cents per kilowatt hour against a much higher purchase price.[724][lndRXed2ylk] The practical consequence is that self-consumption dominates the economics: solar energy is use it or lose it, and household habits were rearranged to consume more generation directly.[724] A revenue meter flashing at 800 impressions per kilowatt hour gives a live indication of import.[724]

## Load shifting and self-consumption

Once export is worth little, the design problem becomes moving loads into daylight hours. An EV charger configured to follow surplus solar tracks the generation curve closely, with only slight deviation attributable to the control loop between car and charger; below about 1.2 kW of surplus the car stops charging altogether and will not go under that threshold.[EYx46kRv2Bw] A heat pump hot water system is a near-ideal solar load: heating the household's water consumes about one sixteenth — roughly 6% — of what an 8 kW system produces on a good summer day, and it can be timed to run during generation.[WtGlolw-BxA] A pool heat pump serves as a dump load for surplus, drawing about 2.5 kWh on maximum and around 2 kW on its lower setting.[iztOfT0CX1k]

By the same logic, instant electric hot water is the wrong choice for a solar or battery household: it consumes too much peak power, and the design goal in such a house is minimising peak current rather than maximising it.[pXtSybs9QRs] Thermal storage in an insulated tank is itself stored energy, useful when supply fails.[pXtSybs9QRs] Competing loads must be prioritised — an EV takes all available solar before any surplus reaches the battery.[vNKcRs3zDBI]

## Batteries and off-grid limits

Battery storage changes the arithmetic but does not remove the grid. A nominal 11 kW array fully charged a 15 kWh pack by around noon on three consecutive midwinter days, yet the pack barely lasted each night.[vNKcRs3zDBI] Expansion to six modules would double the pack, at roughly A$2,900 street price per 5.1 kWh unit.[vNKcRs3zDBI] Battery discharge is itself rate-limited: a 5 kW maximum output cannot cover an 8 kW household draw, and only brief periods actually reach that ceiling.[lndRXed2ylk] Even with more than 10 kW of panels and a 25 kWh battery, disconnecting from the grid is not viable outside good summer weather.[5C_IT9F4ZkA] A battery system would in principle eliminate the electricity bill, but not the battery's own maintenance cost or the amortised cost of the solar installation.[724] In practice, monthly bills fall to a small residual figure rather than zero.[b9K0YoPBGek]

Where multiple PV systems coexist, AC coupling is the mechanism that keeps a second array useful: a hybrid inverter that has no knowledge of a separate microinverter system would otherwise let that generation flow out to the grid, and AC coupling redirects it into the battery instead.[1719][BXVgk-uoxn8] Verifying that it is actually working requires reconciling the power figures, which do not always add up cleanly.[BXVgk-uoxn8] Larger LFP rack batteries with pre-wired high-current busbars and CAN interconnect target the upper end of home and light-industrial storage, such as a farm with a large array.[1634]

## Monitoring

Long-run data is what makes any of these questions answerable, and the logging chain is worth building deliberately. One approach extracts daily data stored inside the Sunny Boy inverter over Bluetooth using PV Bean Counter and uploads it to pvoutput.org, giving public daily, monthly and seasonal views.[724][1047] A dedicated consumption monitor added several years later supplied the missing half of the picture, since the inverter alone reports production and not household consumption.[877] Once two production sources exist, the monitor must see both — current clamps placed in parallel across the two production feeds plus one on the main incoming conductor let it compute household consumption by addition and subtraction.[1390][k2_mJtAeaog] Without that, consumption readings can go negative during the day.[1386][k2_mJtAeaog]

The instrumentation itself accumulates: a complex installation ends up with two independent solar systems, a monitoring system and an EV charger, requiring more than half a dozen current clamps in the switchboard.[X83SPqsf5kY] Separate import and export meters can be consolidated into a single 4G-connected smart meter.[X83SPqsf5kY] Monitoring hardware also fails, taking the combined view of both systems with it.[1511]

Automated underperformance alerts list plausible causes — incorrect system details, incorrect device wiring, an actual system fault, inverter fault, overvoltage, shading, seasonal change and design faults — while noting that dirty panels are typically not the cause.[uuLwmQ7oLo8] Such alerts are prone to false positives from ordinary cloud cover.[uuLwmQ7oLo8]

## Reliability and failure modes

The dominant experience of a quality installation is that nothing happens: zero maintenance cost over five years, no need to go on the roof, and no degradation visible in the panels or mounting hardware.[724][1086] Panels were never cleaned, though dirt and bird droppings do reduce output efficiency.[724]

Real failures are nonetheless documented. A panel shattered completely from an unidentified impact, an event LG characterises as extremely rare.[6enosoC9NsU][1086] A rooftop DC isolator failed outright; such isolators catching fire is a common enough occurrence that not doing so is worth remarking on, and the replacement was chosen as a proper unit.[vlKQ3TzGrX8] After about six years the system failed completely, producing nothing, flagged first by a monitoring alert that initially appeared to be a glitch and then recurred.[1217] On the microinverter side, an alert reported microinverters not responding roughly four years after installation, after a previously trouble-free run.[isnXYy9vCag][1682]

## Sizing

Sizing follows from measured consumption rather than from ambition. Over about 18 months a 3 kW system generated roughly 7.4 MWh against 6.7 MWh consumed, a surplus of some 700 kWh, making it adequate for a four-person household running normal appliances including air conditioning.[724][WtGlolw-BxA] Average daily grid usage fell from 19.1 kWh to 12.87 kWh after installation.[724] Where a residual import of 5.1 kWh per day remained, closing it implied an array of roughly 4.43 kW.[1086]

A concrete upgrade study illustrates the method: a string of ten 380 W panels gives 3.8 kW, and removing one panel from the existing 3 kW string leaves 2.75 kW, for about 6.5 kW total.[dKOmNkVLUAA] Measured household peaks of six to eight kilowatts occur only very briefly, so a 6 to 6.5 kW system covers essentially all consumption with a margin left over for the battery, even with someone working from home.[dKOmNkVLUAA]

## Cost and payback

A 3 kW system with premium components cost about A$5,000 after rebate, against roughly A$3,300 for a comparable budget system; the premium went to the Sunny Boy inverter and LG panels rather than generic parts.[500] Rebate levels vary enormously and have been large enough elsewhere to cover an installation entirely.[500]

After five years the premium system had not paid for itself, with payback projected at seven to eight years — improved to nearer seven by a change of plan giving a cheaper import rate and a feed-in tariff more than double the original.[1086] Under a jurisdiction offering a feed-in tariff equal to the import rate, the same system would already have paid back.[1086] A cheaper system at around A$3,500 would have a payback of just over three years, and a payback of two to three years is achievable in some states and many other countries; cheaper panels and inverters are still likely to last the five years needed.[1086] The system was expected to comfortably exceed ten years of service life, with no trouble anticipated from the inverter.[1086]

The general conclusion is that rooftop solar sits at the margin: it is a borderline marginal payback product that needs its full ten- or twenty-year lifetime to be worth installing, which is precisely why proposals that add cost and complexity to photovoltaics fail against roof-mounted panels that already exist and are far more profitable.[743][1234]
