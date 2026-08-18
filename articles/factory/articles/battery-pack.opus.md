# battery pack

A battery pack is an assembly of two or more cells wired in series, in parallel, or in both, so that a product sees one terminal pair with a voltage and capacity that no single cell could provide.[176] The pack, not the cell, is what an engineer actually designs around: it sets the supply rail, it usually carries the protection and management electronics, and in large systems it is the single most expensive item in the product.[8P8Af5SR57U][3EgRMEc8R_I] Because the pack multiplies cell voltage, every calculation done from a single-cell characteristic curve has to be scaled by the number of cells in series before it means anything at the pack terminals.[204]

## Topology

The simplest packs are pure series strings: a UPS pack of six 6 V blocks gives 36 V at 9 Ah,[1168] a network tester pack is six NiCad cells,[XpZVIWdXliY] and a multimeter can use three AAA cells stacked vertically in a custom carrier.[1520] Alkaline strings are often built as sub-packs of two cells each, so a thirteen-pack string sits near 26 V once the cells are down to about a volt apiece.[XDjyY48u0PU]

Larger packs are built as parallel strings that are then put in series. A 12.8 V lithium pack uses four parallel strings in series, with the battery management system tapping each string to keep the series groups balanced.[8P8Af5SR57U] The same pattern scales up: a battery-electric train uses a battery system made of two parallel packs, each pack carrying its own battery management system and each containing twelve modules, with a common thermal conditioning unit serving both.[1570] Where a string is tapped at its midpoint rather than only at its ends, the result is a bipolar pack with sense wires brought out at the taps.[1258]

Series count is a design constraint in its own right. Two packs in series at an absolute maximum of roughly 8 V each means the downstream switching device only ever sees 17 or 18 V, so a 30 V MOSFET in that position is heavily over-specified.[1461] A bar-graph driver that works from 3 V to about 15 V can be run directly from the pack it is measuring, with no intermediate rail.[204]

## Capacity and how it is rated

Pack capacity marked in milliamp-hours is close to meaningless because the figure is referred to the internal cell voltage rather than the output. A pack sold as 20,000 mAh is rated against a nominal internal battery voltage of 3.85 V held constant, which is "this is not how you rate battery capacity" territory: the honest unit is the watt-hour, and packs are only comparable to each other in watt-hours.[1649] Products that do label in watt-hours make the comparison immediate — 6,000 mAh at 22 Wh in a portable speaker,[1605] 72 Wh in a larger one,[1672] 427 Wh nominal from a 10.8 V, 40 Ah portable power station pack,[1707] 400 Wh enough to run a camping fridge for a couple of days.[t9o1xhAHREE]

Capacity is also the main product tier in battery-powered appliances: a pool-cleaning robot is sold in a 5,000 mAh version and a 10,000 mAh version, the larger pack being what buys the extra runtime.[S5JPr_XQcCc]

## Protection and management

Beyond balancing, the pack's protection circuit is what keeps an over-discharged system recoverable — an undervoltage lockout mounted directly on the battery is credible as the reason a deeply discharged portable power station survived at all.[8P8Af5SR57U] Small consumer packs carry their own protection board even at 1,500 mAh.[f_SdM6sXHD4] Instrument packs may be fused at the pack itself.[808]

Thermal instrumentation is a serious sub-problem in high-energy packs. One purpose-built 3.6 V, 20 Ah, 427 g module contains a four-point analog temperature sensor acting as a hot-spot detector, reporting only the highest temperature of its eight cells — a deliberate reduction of eight measurements to the one that matters.[917] The commercial motivation for such modules is that student and small-team electric vehicle projects are limited chiefly by pack size, weight and construction safety.[917]

Self-discharge sets a floor on standby designs. At a maximum of about 5% per month, a lithium-ion pack left armed for years has nothing useful left in it — "There's not going to be enough juice left in that pack." — and a design that must sit dormant for that long belongs on lithium primary cells instead.[1136]

## Construction quality

Packs are frequently custom, welded or bonded shut, and therefore not serviceable: portable power banks are typically welded closed and cannot be opened,[1649] and small accessory packs are ultrasonically welded.[1034] Custom cell arrangements are common even where the cells themselves are ordinary — standard Panasonic AA cells welded together into a custom pack, potted in styrofoam for thermal protection in a high-altitude payload.[1207] Where a pack is a custom size with no connector, replacement depends entirely on whether the original part remains available.[1605] A replaceable pack that is not externally accessible is a missed opportunity rather than a fault.[1672]

Bad pack construction is conspicuous. A tablet found to contain a hand-assembled pack drew the assessment "Unbelievable, they've bodge soldered a pack together. That is the worst I have ever seen." — the extension section of the pack being the same cells wrapped in paper and soldered on the end rather than an off-the-shelf assembly.[822] Poorly designed packs are the mechanism behind the self-igniting hoverboards of the mid-2010s, a bell-curve statistics problem in which some fraction of any large production run will fail.[833] Modular construction is the counterexample: a 3.6 kWh portable power station is fully modular, so a failed pack module can be removed and replaced rather than condemning the unit.[1499]

## Diagnosis

The pack is the first suspect and often the wrong one, so it is worth measuring before opening anything further. A portable soldering station that would not run measured 10.77 V against a 10.8 V nominal pack, proving the battery was charged and moving the fault onto the board.[1646] Conversely a UPS pack measuring 0.6 V is unambiguously dead.[1168]

Loaded and unloaded measurements can disagree spectacularly. An alkaline string that read 25 V open-circuit collapsed to essentially zero volts while 44 to 50 mA was still flowing through it, a result that points at contact integrity — weak spring contacts in the holders — rather than at true cell depletion.[XDjyY48u0PU] The same class of complaint appears in charging: an intermittent DC jack that only passes current when physical pressure is applied will draw about 73 mA at 12 V and still charge nothing useful.[XpZVIWdXliY] A pack-plus-temperature-controller assembly that draws only quiescent current and refuses to charge at all is simply failed, even though it powers up correctly from an external pack.[h9V0qJ4p3Aw]

Under fault conditions the pack itself reports the problem: a shorting compute module drives the supplying pack into overload.[E1IqcGcZKHE] Thermal imaging of a working LED strap light shows the pack running around 30 °C, comfortably below the surrounding heatsink temperatures.[1010]

## Packs in test equipment

Battery operation in bench instruments is almost always an option rather than a fitting. Scopes and analysers ship with a slot or slider on the bottom or rear for a pack that is bought separately,[480][1503][207] and the moldings for that slot survive into models where the connection is deleted, because the case is reused.[1510] A frequency counter of the same lineage had its optional pack fitted internally, making the instrument fully portable.[265]

The Tektronix 2 Series treats the pack as a structural part: it is an option that ships with a single battery, the kickstand mounts on the pack rather than on the instrument, the pack has its own alignment protrusion, and the same pack works with the main stand.[nO09bc5ozng][PcxEO3fA_Ls][1477] Batteries are hot-swappable and a separate external charger is offered, so a user can keep charged spares in rotation.[nO09bc5ozng] Shipping constraints bound the design — at about 97 Wh the battery is close enough to the air-freight limit that the product ships with only one.[nO09bc5ozng]

Where no factory option exists, external packs fill the gap. A 35 W scope can be run from a pack mounted on its VESA points with a cable run to the input,[1563][1566] and the fuel-gauge and mounting problem is one the user community solves on its own.[1566]

## Bench use as a clean supply

A pack is a supply with no mains-referred path, which makes it a diagnostic instrument in itself. Running a circuit from a battery pack while disconnecting all external supply inputs isolates whether an observed modulation originates in the supply or in the circuit — in one case a 55.5 Hz modulation persisted unchanged on battery, exonerating the supply entirely.[160] A power supply fed from an external 12 V battery instead of a lab supply shows significantly cleaner output noise.[1606]

Products with both an internal pack and a DC input handle the changeover mechanically rather than electronically. A three-pin DC barrel jack with a normally-closed switch contact carries the battery positive through pins 2 and 3; inserting the plug breaks that contact so the battery positive is completely disconnected from everything, and the external supply takes over.[1015] The battery ground stays permanently tied to common, so only the positive needs switching.[1015]

## Electric vehicles and grid storage

In an electric car the pack dominates cost. The premium for the fully electric version of a car also sold as a hybrid runs to about $20,000, and that premium is the pack.[1337] Stated more bluntly, the pack for a Tesla costs more than a whole new internal-combustion car, which is why electric cars would have a serious hard time competing without subsidy — and battery technology improves at single-digit percentages per year, not in steps large enough to change that quickly.[3EgRMEc8R_I]

Pack size is not the same as range. A 37.5 kWh pack delivers more range than a 40 kWh one in a competing car because the higher-performance car consumes 20 to 25% more energy per unit distance, on the order of 15 to 20% worse efficiency per range.[XmBW_MV-TBU][1337] Trading punchy performance for range in this way is a defensible choice, and the smaller pack makes the car three or four thousand cheaper as well.[1337] Efficiency figures anchor the comparison: 10.5 kWh per 100 km for a solar-assisted production car with a 60 kWh pack and 625 km nominal range,[1480] against 6.25 kWh per 100 km implied by a 100 kWh pack claiming 1,000 miles.[1480] Working backwards from claimed solar range gains — 20 km added in two hours on a car needing 10.5 kWh per 100 km — gives 2.1 kWh into the pack, 1.05 kWh per hour, and over 5 m² of panel, 210 W/m².[1480]

Pack architecture in a production EV is many modest cells in a long series string: 50 Ah cells, about 82 of them, totalling roughly a 320 V pack.[179] Mounting the whole pack under the floor puts the centre of gravity very low, so a narrow car handles like a much wider one.[179] Larger-format cells attack the mass problem from the other direction — for the same kilowatt-hour pack size, fewer and larger cells mean far less steel casing and therefore less weight, along with fewer cells to handle on the production line.[1340] Market pressure runs toward larger packs regardless, because range anxiety is real for new owners and manufacturers build what buyers want.[1584]

At grid scale the modular pack is also the fire compartment: in a large battery installation a fire that starts in one cell engulfs the pack containing it, and spreads from there unit to unit, with toxic smoke as a primary hazard.[1411] Residential storage is sold in the same modular way — nominal 5.1 kWh packs at around A$2,900 street price each, with a 15 kWh installation expandable to six packs, so capacity is purely a spending decision.[vNKcRs3zDBI]

## Miscellaneous applications

Packs turn up wherever mains cannot go. Autonomous ocean-bottom seismic recorders carry a huge pack to run a data logger, hydrophone and tilt sensor for the duration of a deployment on the sea floor.[61] A CubeSat-class satellite kit ships the pack alongside the solar cells, power management controller and microcomputer as part of a complete kit.[shSoVLSPbaQ] A shredding mechanism concealed in a picture frame needed a pack with enough energy in reserve for a couple of test shreds before the real one, because a mechanism you cannot test after final assembly is a reliability gamble.[1131] In benchtop projects the pack is often two 18650 cells on a connector, with a switching pre-regulator taking the place of a heatsink.[258] Custom high-capacity pack assembly is a trade in its own right, extending to home-storage-sized packs of 15 kWh and above.[UJ6JG4eV0nY]
