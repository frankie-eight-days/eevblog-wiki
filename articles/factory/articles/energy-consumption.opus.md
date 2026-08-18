# energy consumption

Energy consumption is the quantity of energy drawn by a device, a vehicle, a building or a society over a span of time, as distinct from power, which is the instantaneous rate at which that energy is drawn.[1009][1401] The distinction is the foundation of nearly every practical judgement about efficiency: a figure in watts describes a moment, while a figure in watt-hours or kilowatt-hours describes what actually accumulates on a meter or drains from a battery.[1009][1401] Aggregate energy consumption is treated as one of the defining engineering problems of the era, and the responsibility that follows is to build systems — particularly renewable generation — that are as efficient as possible for the resources they consume.[935][1001][sJS2paVW-kc]

## Energy versus power

Power dissipated in a resistance follows directly from Ohm's law: current through a resistance produces a voltage drop and dissipates power in watts, which is joules per second — a rate, not a quantity.[1401] That resistance can be almost anything in a circuit: the internal resistance of a battery or power supply, a PCB trace, wiring, or transformer winding resistance.[1401] Confusing the rate with the accumulated total is the common error, and it matters well beyond circuit analysis, because discussion of solar generation, energy production and energy consumption in the wider world depends on keeping voltage, power and energy separate.[1009][1401]

## Measuring consumption on the bench

At the small end, an inline energy meter accumulates elapsed time and total energy: a linear power supply left idle and powering nothing registered 0.044 kWh over 27.1 hours — a quantity too small to register any cost at all.[337]

For loads that draw current in short bursts rather than continuously, an oscilloscope's integration function gives the total charge or energy consumed over the event. A microcontroller that wakes once a second to update a display produces a current pulse that can be single-shot captured and integrated to find the energy per wake-up.[662] Because the integral accumulates noise along with signal, the acquisition should first be cleaned up with boxcar averaging or high-resolution mode to obtain the highest-fidelity waveform before integrating.[662]

## Household consumption

Domestic consumption is measured in kilowatt-hours per day or per billing quarter. A Sydney household recorded a total of 725 kWh across an 85-day quarter, roughly 8.5 kWh per day.[724] A single logged day showed 14 kWh of total consumption, with evening peaks around 4 kW while cooking.[1454] The refrigerator is generally the most power-consuming appliance in a house.[sJS2paVW-kc]

Solar monitoring systems plot generation and consumption together, typically with production and consumption on separate traces plus the overlap between them, so that self-consumed solar can be separated from what was exported and what was imported from the grid.[877] Such monitoring drives behavioural change as much as hardware change: shifting the washing machine and dishwasher from overnight operation to daytime raises the proportion of generated energy that is actually self-consumed.[724] A household present during the day — as with a young family at home — self-consumes a larger share than one where both parents work and the children are at school.[724]

Consumption level also determines whether battery storage makes economic sense. For a Sydney household with its particular consumption profile, no payback period existed at all for a battery system given the finite life of the pack; installing one would be a choice made for interest or for grid independence, not on financial grounds.[1086]

Standby energy is worth separating from energy used doing work. A heat pump hot water system consumed between 2.2 and 3 kWh per day, comfortably under the 3 kWh the manufacturer claimed for a family of four, and the penalty for actually drawing and reheating water amounted to roughly 20% above the baseline.[5HikvxaQ_Z8]

## Vehicle consumption metrics

The meaningful figure of merit for an electric vehicle is energy per unit distance, expressed in Australia as kilowatt-hours per 100 kilometres.[1480][QkFioBbH5aM][7nUgmEuyKIU] A Hyundai Ioniq driven around Sydney typically returns about 10 to 12 kWh/100 km, rising to 13 or 14 on a bad trip in hilly terrain, and as low as 10 in ordinary driving.[7nUgmEuyKIU] Measured trips produced 10.6 kWh/100 km overall, with sustained stretches at 8.8 and as low as 7.0 kWh/100 km on relatively flat suburban motorway driving.[7nUgmEuyKIU]

The instantaneous figure is nearly meaningless. At any given moment consumption swings between effectively zero and 25 or 30 kWh/100 km under acceleration; only the average over the entire trip is the number that matters.[7nUgmEuyKIU] Measurement error in the trip average also falls as trip length increases.[7nUgmEuyKIU]

Comparisons between vehicles reduce to this same metric. A Nissan Leaf offers better acceleration performance precisely because it uses roughly 20 to 25% more energy per unit distance, which is why the Ioniq achieves greater range from a smaller 37.5 kWh pack.[XmBW_MV-TBU] The Aptera's claimed 1,600 km range from a 100 kWh pack works out to 6.25 kWh/100 km — less than 40% better than the Ioniq's real-world 10, despite the radically different vehicle concept.[1480][QkFioBbH5aM] A purpose-built solar racing car carried an energy consumption sticker rating of 115 Wh per kilometre.[923] Its zero-CO2 rating, like that of any electric vehicle, depends entirely on where the batteries are charged from.[923]

Aerodynamic drag dominates at speed even for very small vehicles: on a normal bicycle at 20 miles per hour, some 90% of the rider's energy goes into pushing air.[501]

Regenerative braking recovers energy that would otherwise be lost, and its effect appears directly in the trip consumption figure — braking visibly returns charge to the battery, though conversion losses mean recovery is never complete.[7nUgmEuyKIU] Coasting competes with regeneration on gentle downhill sections, where a coasting vehicle maintains speed against only tyre friction, wheel bearing losses and air resistance rather than harvesting.[7nUgmEuyKIU] Comparative testing between maximum regeneration and pure coasting on flat urban and motorway routes favoured light rather than aggressive regeneration.[7nUgmEuyKIU]

## Transport systems

At the systems level the comparable metric is specific energy consumption in watt-hours per seat-kilometre, which normalises for both distance and carrying capacity.[YyEMU_qu4PM] By that measure the Shanghai Transrapid maglev consumes fewer watt-hours per seat-kilometre than the ICE high-speed rail it is compared against, making maglev an efficient if expensive design.[YyEMU_qu4PM] Energy is nonetheless the dominant operating cost for such a system: published figures put energy consumption at 64% of the Shanghai maglev's operating costs.[YyEMU_qu4PM] Proposed evacuated-tube systems have advanced energy consumption and carbon neutrality as fundamental metrics, though the maglev component alone already delivers the efficiency without the vacuum envelope.[1588][YyEMU_qu4PM]

## Energy as a debunking tool

Because energy consumption is bounded by physics, a consumption calculation is often the fastest way to test an extraordinary claim. Atmospheric water generation is the standard case: extracting water from air is a dehumidification problem, governed by latent heat and the gas-to-liquid phase change, and the energy required per litre sets a hard floor.[WyPBIzJQB_o][1121][1454]

Applying roughly 2,300 kJ per kilogram to a claimed 37 litres per day gives about 85,000 kJ, or 23,600 watt-hours, which spread over 24 hours amounts to a continuous kilowatt that must be dissipated into the surrounding soil — the equivalent of a radiant bar heater running non-stop, in an arid region.[WyPBIzJQB_o] The same latent heat calculation applied to a desiccant dehumidifier product yields a minimum of about 250 Wh per litre.[1454] Real hardware confirms the order of magnitude: the most efficient dehumidifiers on the market extract about 1.85 litres of water per kilowatt-hour consumed.[WyPBIzJQB_o] For an earlier self-filling water bottle, the same back-of-the-envelope approach showed that a rooftop-sized solar panel would be needed, best case, to reach the claimed output.[1121]

A commercial atmospheric water generator consuming roughly 14 kWh per day to produce at best 10 litres therefore consumes as much energy in a day as an entire household, at a water cost of around 35 cents per litre — some 175 times, more than two orders of magnitude, above conventional supply.[1454] As an engineering judgement, spending that much energy to obtain drinking water is the worst available option by orders of magnitude, and the argument holds with particular force off-grid, where solar or wind capacity is finite and cannot be squandered.[1454]

The same method applies to generation schemes. Basic LED line marking for a solar roadway was calculated at 30 kW consumed per kilometre, which over 24 hours is 720 kWh per day against an ideal generation of 3,000 kWh per day from that same kilometre — about a quarter of the ideal maximum output consumed by the markings alone, before any other signage or safety features.[632]

## Efficiency as a regulated requirement

Efficiency is not left entirely to the market. Energy Star and MEPS-style legislation make it unlawful in some countries to sell products such as chargers and mobile phones that fall below defined efficiency and standby power limits.[1001] Against that backdrop, a wireless charging technology with the worst efficiency on the market by an order of magnitude fails at the concept stage rather than at the product stage.[1001]

Infrastructure consumption is easy to overlook because it is remote from the user. Streaming video is served by thousands of servers that consume large amounts of energy, to the extent that watching one hour of a popular channel per week consumes more energy than two refrigerators — a cost incurred regardless of how low-power the viewing device itself is.[sJS2paVW-kc] The underlying driver is the sheer scale of energy use, and the reliance on fossil fuels that release carbon dioxide and sulfur dioxide to meet it.[sJS2paVW-kc]
