# solar array

A solar array is a set of photovoltaic panels wired together as a single generating source, either as series strings feeding a central inverter or as panels each carrying their own microinverter.[1426][1626] Array behaviour is dominated by two things that are easy to overlook: the electrical topology, which determines what a single shaded panel does to the rest of the system, and the projected collecting area and angle, which set the ceiling on energy yield regardless of how the panels are marketed.[1426][1544] Because a string of panels in series can reach several hundred volts of DC before it reaches the inverter, an array is also a high-voltage DC installation with failure modes that ordinary household wiring does not have.[GoKbPDADG0c][1734]

## Topology: strings versus microinverters

In a string array, panels are wired in series and the whole string presents a single operating point to one maximum power point tracker at the inverter.[1426] A string inverter may offer more than one string input, allowing separate sub-arrays with different orientations to be tracked independently; a hybrid inverter at the larger end of the residential range may provide four string inputs arranged as two strings per PV tracker, so that two distinct PV arrays can be run from one box.[dlOtqDPCO1o][kKfZgAyFu8Q]

The microinverter alternative puts a converter on each panel, so maximum power point tracking happens per panel rather than across the whole series string.[1426] A microinverter array is described by how many units sit in parallel on each relay rather than by series count: one residential installation runs two strings of microinverters on two relays, each relay rated to support up to eleven microinverters.[1626] Microinverters must also detect the presence of the grid before they will export, and will not switch on without it even when the sun is up and the unit is powered, which is a mandated anti-islanding safety behaviour rather than a fault.[1626]

Per-panel conversion is the better technical answer for shading and mismatch, but string arrays with a central inverter remain the cheaper solution, and the choice is a genuine trade-off rather than a settled question.[1426]

## Shading and mismatch

Shading loss in a series string is grossly non-linear with shaded area. A partial shadow falling on a single cell — not even covering the whole cell — is enough to cut roughly 20% off the output of an entire twelve-panel series string.[1426] The mechanism is that the series string is current-limited by its worst cell, so a small obstruction such as a mast or an antenna can ruin the yield of panels that are themselves in full sun.[1426] Per-panel microinverters limit the damage: shading on one panel does not drag down the rest of the array.[1426]

Shading also constrains siting. Early-morning shadowing from nearby structures or trees is often unavoidable, and trimming vegetation only partially recovers it.[dlOtqDPCO1o]

## Voltage, isolation and system-level effects

A rooftop PV string can reach 400 to 500 V, and large commercial arrays run at 1500 V.[GoKbPDADG0c][1734] Because this is DC, there is no current zero crossing to extinguish an arc: water ingress into a DC isolator can start an arc-over that then sustains itself and develops into a plasma event.[GoKbPDADG0c] The practical bench consequence is that a multimeter intended for PV work should not offer any easy way to land in current mode by accident while probing an array at these voltages.[1734]

An array is not purely a source. Because the panel structure sits on a grounded roof or, in utility installations, close to ground level, the array presents a large distributed capacitance to earth.[1620] That capacitance interacts with the inverter's high-frequency switching and drives common-mode behaviour, which becomes a design constraint as arrays get physically larger.[1620]

From the point of view of the house and the inverters downstream, the array is only one possible source among several. A hybrid inverter that can supply the same internal bus from a battery, from one PV array or from another makes the actual origin of the energy invisible to the load.[1620]

Wiring topology is also where large deployments of non-standard panel formats tend to be underspecified: how individual elements are interconnected, whether each carries its own microinverter, how the arrays are arranged, and how any of it is maintained are system-engineering questions that determine viability as much as cell efficiency does.[850]

## Yield, area and the per-square-metre figure

The honest way to compare arrays of different construction is energy per unit area over a matched period. A conventional rooftop installation of ten 385 W panels covering 17.8 square metres — not even angle-optimised — produced 42.9 kWh over seven days, or 2.41 kWh per square metre.[1544] A 400 square metre solar pavement measured over the same seven days produced 388 kWh, about 1 kWh per square metre, roughly two and a half times worse for the same footprint.[1544]

The same method applied to a solar roadway installation: an array of twelve 250 W panels, of comparable physical size to the roadway section and already seven years old, produced 3,200 kWh in a year against the roadway's projected 1,300 kWh — more than double, from panels that had been degrading for years.[1356]

Seasonal variation is large and is routinely omitted from marketing claims. Output roughly halves in winter relative to summer at Sydney latitude, so any array sized on peak summer figures will be undersized for most of the year.[QkFioBbH5aM][1570] Sizing a battery-electric train from the solar array on a factory roof illustrates the margin: powering it might be possible from that roof on the best days of midsummer, but covering 60 trips and roughly 450 km per day year-round needs three to four times the array area.[1570]

## Residential systems in practice

A reference residential installation, commissioned in June 2013, is a 3 kW system of twelve LG Mono X panels on a domestic roof.[938][484] Roof undulation is visible as a wave along the panel run, and is normal — most roofs have some degree of it and little can be done about it.[484] That array was later joined by a 5 kW Enphase microinverter system on a different roof face, the older 3 kW string system being physically relocated to make room for the better-oriented new one.[1390] The combined 8 kW, roughly 40 square metres, runs as two fully independent generation sources with separate inverters and separate monitoring, which complicates measurement: capturing whole-house production requires combining current transformers from both systems.[1390][1480][M4IiR4vW0aY]

Household metering follows directly from the topology. Both systems feed the switchboard in parallel alongside the main breaker and the individual circuits, so net flow at the connection point reverses direction depending on whether combined array output exceeds household consumption — exporting when it does, importing at night or when it does not.[1390] A clamp on the 3 kW array's own wiring lets the monitoring system account for that string's contribution separately from the rest.[1390]

Typical performance for such a system: a peak of 3.8 kW and about 25 kWh on a good day from the Enphase array alone.[1467] Over a day the combined arrays more than cover household use with enough left over to charge an electric car, which a solar-tracking EV charger diverts by pushing only the excess that the house is not consuming — around 6.1 kW at peak.[1502][1480]

## Off-grid limits

Being able to run entirely from an array on most days is not the same as being able to disconnect. A week of bad weather in a row leaves the battery unable to recharge, so genuine grid independence requires both an enormous array and an enormous battery sized for the worst run of days rather than the average.[5C_IT9F4ZkA] In practice a well-sized residential array covers 80% to perhaps 90% of usage, with the remainder drawn from the grid after spells of poor weather during which an entire week may yield little usable energy.[1480]

Aggregate deployment produces the same problem at grid scale. Massed solar arrays over-generate in the middle of the day and collapse in the late afternoon as demand rises, producing the duck curve in the generation graph and making solar energy cheap during daylight hours.[1637]

## Vehicle-mounted arrays

Arrays integrated into vehicle bodies are limited by available area and by shape. A car carrying panels on bonnet, roof and boot self-shades: with the sun on one side, the bonnet is shadowed by the rest of the body, and with it on the other, the rear panels contribute practically nothing.[1480] Curved panels also cannot be angled toward the sun the way even a non-ideal residential roof is, and the cells themselves are no more efficient than ordinary residential ones — probably slightly less.[1480][QkFioBbH5aM]

The area arithmetic settles the question. One vehicle carries 5 square metres of double-curved array, another 3 square metres and 700 W.[1480][QkFioBbH5aM] Against a residential array eight times that surface area, even generously assuming the vehicle panels perform as well as a rooftop and ignoring shape losses entirely, the claimed 70 km per day of solar range does not survive.[1480] The constraint is not engineering effort: "You cannot beat the laws of physics."[QkFioBbH5aM] Vehicle solar remains a supplemental technology — useful for a driver covering 20 to 30 km a day in good conditions, not a substitute for charging.[1480]

## Spacecraft arrays

Deployable solar array wings are the standard power source for crewed and near-Earth spacecraft, unfolding over an extended period after launch rather than snapping open.[p5BjSoLgIoE] Their span makes them useful mounting points for cameras: the wide external views of a capsule in flight come from a camera at the end of an array wing.[p5BjSoLgIoE] Beyond the inner solar system the approach fails outright — at Pluto distances irradiance is too low for arrays to work at all, and the spacecraft must carry a plutonium-fuelled radioisotope generator instead.[tWW56LAnT1Y]

## Micrometeorite impacts

Scaling published micrometeorite flux to the Earth's surface area of about 510 million square kilometres gives an average of roughly 392 impacts per year on a 20 square metre rooftop array — more than one per day.[846] That the world's arrays are not routinely shattering is the point of the calculation: the arithmetic falsifies the premise rather than confirming it.[846]
