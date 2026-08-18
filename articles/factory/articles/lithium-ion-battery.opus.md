# lithium ion battery

The lithium ion battery is the dominant rechargeable cell chemistry in modern electronics, offering high energy density in packages that range from sub-millimetre flexible pouches to multi-megawatt-hour grid installations.[176][1568] Its arrival is a large part of why mobile equipment shrank: replacing a NiCad pack with a lithium ion one, alongside increased digital integration, was a key driver in the rapid collapse of mobile phone size.[243] The chemistry was first commercialised by Asahi Kasei in cooperation with Sony.[1090]

For a product that needs a built-in recharging solution, lithium ion is the default engineering choice: the cells are extremely versatile in shape and size, they are low cost, and the charger chips are cheap, readily available and easy to use.[176]

## Chemistry and naming

The terms *lithium ion* and *lithium polymer* name the same chemistry and are not two different battery types; the genuine distinction lies in the anode material, of which two types are in use.[176][919] From a charging point of view LiPo cells and 18650 lithium ion cells behave identically.[919] The chemistry is distinct from lithium *primary* cells, which are not rechargeable and must never be put on a lithium ion charging regime.[919]

Lithium iron phosphate (LFP) is a related but separate technology, regarded as substantially safer than conventional lithium ion, and has been adopted in home storage products and in later Tesla Megapack units.[gAu8CvMjDrU][1568] Nickel-manganese-cobalt (NMC) oxide is another cathode formulation used in lithium cells.[1633]

## Cell parameters

A single cell has a nominal voltage of 3.7 V and a maximum charge voltage of 4.2 V.[Cn3DVQGmF9A][KTr-44n0bbU][809] The low end of a usable single-cell range is around 2.7 V.[329] A two-cell series pack therefore spans roughly 6 V to 8.4 V, and a six-cell pack gives a nominal 22.2 V.[204][259][Cn3DVQGmF9A]

The discharge curve is comparatively flat, which makes it far easier to design a low-voltage cutoff that extracts most of the stored energy — in contrast to alkaline cells, whose sloping curve leaves a significant fraction of capacity stranded.[772] Round-trip storage efficiency of a complete lithium ion battery pack is around 90% end to end.[1086]

Because the voltages matter so much on a chemistry this sensitive, any serious battery analyser uses four-wire sensing at the cell, feeding the sense connection back so that cable drop at high current does not corrupt the measurement.[1434]

## Charging

Lithium ion charging follows a constant-current then constant-voltage profile. Applying 4.2 V directly to a low-charge cell would drive an enormous current into it and damage it, so the charger holds a fixed current until the cell voltage reaches 4.2 V, then switches automatically to constant-voltage mode as the cell's effective internal resistance rises.[1688]

The current in the constant-current phase is expressed as a multiple of capacity: 1 C on a 50 mAh cell is 50 mA. Most lithium ion cells are charged at around 0.5 C, though the cell datasheet is the authority.[176] Charge terminates when the tapering current falls below roughly 5% to 10% of the set rate; past that point it is heavily diminishing returns.[919]

A cell that has been run completely flat — no low-voltage cutout in the product, left switched on — can often be rejuvenated, but jumping straight to full charge current will finish it off. Dedicated charger ICs handle this with a pre-charge phase at typically 20% of the full rate.[176]

Charging can also be done with a bench supply by setting the voltage limit to 4.2 V and the current limit to half C, then letting the supply's own CC/CV behaviour execute the profile; the voltage limit means the cell cannot be pushed past 4.2 V and cannot explode from overvoltage.[919][KTr-44n0bbU] A supply timer set to about four hours provides the missing termination logic, since bench supplies have no taper-current cutoff and are not designed for float charging — leaving a cell on charge overnight is to be avoided.[919] The same technique will kickstart a deeply discharged pack sitting behind an undervoltage lockout, bringing it back to a state where its own charger will accept it again.[KTr-44n0bbU]

Dedicated charger ICs span a wide range of sophistication, from three-terminal parts to fully programmable devices whose resistors set every phase of the cycle.[176] Named examples include the LTC4057 single-cell charger, the Consonance CN3702 two-cell charge controller, and the Linear Technology LT1512, a SEPIC constant-current constant-voltage charger able to work from an input either above or below the battery voltage.[930][1460][259] Charger cost is not always negligible: at 100-off the LT1512 came in at $3.85, making it the most expensive semiconductor in a bench power supply design and ultimately disqualifying it.[259] At the low end, USB charger modules for a single cell reduce to a five-pin SOT-23 part and a two-way connector.[353] Because charging is now active silicon rather than passive circuitry, and costs cents to implement, essentially every modern consumer product uses a centre-positive DC jack.[1015]

## Protection circuitry

Consumer cells of any appreciable capacity carry built-in protection circuitry, and tape over the end of a cell is a reliable indicator that it is present.[189] Protected 18650s carry the circuit in the end cap and are sometimes slightly longer than unprotected cells.[919]

Protection parts are commodity items in small packages. The DW01 is a single-cell protection IC; the ABRCL3130 integrates an advanced power MOSFET, high-accuracy voltage detection and delay circuits into a SOT23-5.[V0RWwSw96Sw][1541] Equivalent pinouts proliferate across vendors because they all target the same single-cell lithium ion application, the main variable being cell count and voltage.[V0RWwSw96Sw] Tearing down almost any battery product turns up a small MOSFET performing battery switching or protection duty.[1736]

Over-discharge protection typically trips at around 2.4 V to 2.5 V. A cell sitting at 2.86 V is above the protection threshold but already below the operating voltage of the device it powers.[1370]

## Safety and failure

Lithium ion fires are exothermic and self-sustaining: once a cell of any size catches, it cannot be extinguished, and the only available response is containment — keeping the fire from spreading to adjacent packs and letting it burn out.[1422][1568] Cells are required to survive stringent abuse testing, including a nail test in which a nail is driven through the cell shorting all internal layers, without igniting; energy density in modern batteries is high enough that manufacturing tolerance problems have produced field fires despite this.[1204]

Working on relatively high-capacity lithium ion packs away from the lab, in a space with a fire extinguisher and nothing valuable to lose, is a sensible bench practice.[1707] For test gear, a clamp meter intended for battery work needs a 600 A range to cover short-circuit currents from lithium ion packs.[3kdYGneg9xI]

Ageing failures are ordinary rather than dramatic. Batteries lose capacity with time as a matter of course.[Ac1zZo7wLo8] A Panasonic cell around 20 years old and over 1000 cycles delivered 286 mAh against its 680 mAh rating when discharged at 500 mA — still a usable fraction, but far off nameplate.[1732] Packs also fail per-cell: a Dyson pack whose cells sat at about 3.5 V each simply hit the charge cutout and stopped.[Cn3DVQGmF9A] Pouch cells that have gone puffy are visibly failed.[1330] Cell quality varies, and off-brand replacements failing in quick succession is a recognised outcome.[1460]

## Physical formats

The 18650 cylindrical cell is the workhorse format, appearing in torches, laptops, test equipment, power banks and vehicle packs.[919][1540][964] Panasonic NCR 18650s have been used in competition solar electric vehicle packs.[923] At the other extreme are ultra-thin rechargeable pouch cells from 0.5 mm to 1 mm thick that can be bent, suited to products that cannot accommodate a rigid rectangular battery.[176][130]

Typical capacities in consumer products run from a 900 mAh, 3.4 Wh cell in a budget phone, through 1700–1800 mAh (about 6.7 Wh) in e-readers, to 54 Wh in a high-output work light.[514][189][108][1516] The presence of a lithium ion cell can date a product: batteries of this chemistry did not exist in 1985.[940]

## Packs and large-scale storage

Series-parallel construction scales the chemistry up. The Mitsubishi i-MiEV uses a 320 V pack built from roughly 82 or 83 cells of 50 Ah each, charged and cooled as part of an integrated water-cooled system covering charger, inverter and motor.[179] A converted 1990 Suzuki Carry van carried 450 16 Ah cells for a 23 kWh pack.[784] Grid-scale installations aggregate packs into Megapack units — one such site comprised 40 Megapack 2.0 units.[1568] Spent automotive and industrial lithium ion packs are recycled, retested and repurposed at industrial scale.[1403]

Bench instruments exist specifically to emulate these packs, spanning anything from a coin cell up to the large lithium ion battery found in an electric scooter or bike.[Y2rcx4vKxlc]

In spacecraft use the chemistry has to survive an unregulated thermal environment; one approach places the cells in the coldest part of the structure, exploiting the fact that lithium ion cells are exothermic and self-heat during operation.[896]

## Where lithium ion is the wrong choice

Rechargeable lithium ion is a poor fit for products that must sit unattended for years. Self-discharge of a few percent per month makes multi-year standby impractical, and a design that genuinely has to work after an indefinite dormancy calls for a lithium primary solution with a guaranteed ten-year-plus shelf life instead.[1136] The same reasoning drives instrument designs aiming at decade-scale battery life to reject lithium ion and lithium polymer outright in favour of lithium primary cells.[1371]

Energy density claims made against lithium ion warrant scrutiny. Nanodiamond betavoltaic batteries advertised as tens of thousands of times more energy dense than lithium ion deliver on the order of 100 microwatts, a power level with almost no product applications, which makes comparisons on density alone meaningless.[1333] Conversely, a device that harvests ambient 2.4 GHz Wi-Fi energy into an internal lithium ion cell and then charges a phone from it is simply discharging a pre-charged battery — the observed charge rate comes from the internal cell, not from harvesting.[55] A thermoelectric-generator smartwatch producing 500 microwatts under best-case conditions still contains a lithium ion battery of 200 mAh, or 740 mWh, that could run the watch for years on its own.[945]

For scale, the energy density of fossil fuel remains far higher: a 10-gram lump of coal holds enough energy to run a mobile phone, whose lithium ion battery it dwarfs, for more than a month.[sJS2paVW-kc]

## Measurement and instrumentation

Battery voltage can be turned into a usable state-of-charge indication with an expanded-scale voltmeter. An LM3914 configured as a two-cell lithium ion gauge covers 6 V to 8.4 V through an input divider, mapping the 3 V to 4.2 V per-cell window onto the display; the same circuit is adjustable for other chemistries, cell counts and voltages.[204]

Where a design must run from a single cell across its full discharge range, a boost converter handles the shortfall — from 2.7 V at the low end upward.[329] A two-cell pack topping out at 8.4 V pairs naturally with boost regulators specified for a 2.5 V to 10 V input.[259]
