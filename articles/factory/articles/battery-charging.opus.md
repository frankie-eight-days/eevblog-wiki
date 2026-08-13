# battery charging

Battery charging is the controlled delivery of energy into a secondary cell, governed by a profile that the cell chemistry dictates rather than by whatever the source happens to supply. For lithium-ion and lithium-polymer cells the profile is a two-stage constant-current then constant-voltage sequence, and getting the terminal voltage wrong is dangerous rather than merely inefficient.[919][176] Almost every portable instrument, tool, camera, and e-reader carries the charger inside it, which makes charging circuitry one of the most common blocks encountered in teardown and repair work, and one of the most common places for a product to fail.[1672][1370][1433]

## The constant-current / constant-voltage profile

Two numbers are needed to charge a lithium cell: its nominal charging voltage, which is critical, and its charge current.[919] The overwhelming majority of cells terminate at 4.2 V, though the figure shifts slightly with chemistry and manufacturing.[919] The characteristic curve plotted for such a cell is cell voltage against time or against capacity, the x-axis running from zero to 100% of capacity — the quantity called C — or equivalently from zero to some number of hours.[176]

Charging begins in constant current. As the cell fills, its effective electrochemistry and internal resistance change until the terminal voltage reaches the set point, at which the charger crosses over into constant voltage and the current begins to fall away.[1688][357] Termination is typically at a current threshold rather than a time: around 10% of the charge current, so a cell charged at roughly 1.7 A might cut off near 170 mA.[919] The crossover is directly observable — a cell sitting below the set voltage is still in constant current, while a cell pinned exactly at 4.2 V with falling current has already switched to constant voltage.[357] A partly charged cell, for example one resting at 3.81 V, may skip the constant-current phase almost entirely and drop straight into constant voltage.[357]

Charge current is conventionally expressed relative to capacity. A 2600 mAh cell charged at 1 A is not even at 1C, and could take a couple of amps if wanted.[1613] At a 1 A rate, cells of around 2700 mAh charge in roughly three hours.[259]

## Charging from a bench supply

Because a lab power supply provides independent constant-voltage and constant-current limits, it implements the lithium charging profile directly: set the maximum output voltage to 4.200 V and the current limit to the desired charge rate.[919] Supply accuracy is not the limiting factor — a 0.05% instrument such as the Rigol DP835 is an order of magnitude better than the application requires.[919] The same procedure applies unchanged to 18650 cells and to LiPo pouch cells of the kind found in remote-control equipment.[919] Done incorrectly, charging lithium cells this way can be quite dangerous.[919]

The technique generalises to other chemistries by changing the compliance voltage. A nickel pack is charged by setting maximum compliance at 1.4 V per cell — 8.4 V for a six-cell pack — with a current limit of around half an amp.[XpZVIWdXliY] A single small rechargeable cell can be nursed at 1.5 V compliance and 1 mA of constant current.[0018phUFjuQ] A 30 V, 500 mA tool pack accepting charge shows constant current at 500 mA with the compliance voltage sitting at 28.98 V and climbing, which is the signature of a pack that is genuinely taking a charge.[1760]

Nickel chemistries are less forgiving of a dumb profile than the two-step lithium sequence. Nickel-metal-hydride charging is exothermic, and charging such cells properly calls for temperature sensing.[176] Modern integrated lithium chargers fold the same idea in: a battery running too hot is charged at a slower rate in accordance with the JEDEC standards.[1694]

One hazard specific to bench charging is what happens at the supply rather than the battery. Disconnecting the input voltage from a linear supply while a charged battery remains connected to its output feeds voltage backwards into the regulator, a scenario common enough with traditional linear supplies to warrant deliberate testing.[233]

## Charger silicon

Dedicated charger ICs are jellybean parts, and a premium one is a defensible choice rather than an extravagance in a product whose failure mode is thermal.[1694] Identified charge controllers include the BQ24773 in a portable speaker,[1672] a Microchip part paired with battery reverse-polarity protection,[1619] and a Linear Technology charging circuit sited immediately next to the charge connector.[571] Charging is also frequently absorbed into a power management unit: the MC13892 companion to an ARM Cortex processor carries built-in battery charging plus coulomb counting for state-of-charge estimation, a real-time clock, and the DC-to-DC converters and regulators for the processor cores.[189]

Charger parts differ in their termination features. A later-generation part replacing the LT1512 added end-of-charge control with a selectable minimum current ratio — that is, a programmable termination threshold.[259] At the crude end, the charger in a rectifying toothbrush base is a single SOT-23 switch with no series current limiting at all, connecting the rectified voltage from the power coupling coil straight through to the battery, with the microcontroller's ADC measuring battery voltage during charging to decide what to do.[284] Adjustable linear regulators are also pressed into service as chargers in their application notes, distinguished from the ordinary regulator configuration by an added series resistor in the output leg.[1438]

Where charging circuitry lives is a board-level design decision with thermal consequences. Charging two 18650 cells from a 12 V rail through a linear pass element throws the difference away as heat; moving the charging circuitry onto the main board and adding a switching pre-regulator removes the heat sink altogether.[258]

## Multi-cell and series-pack considerations

A single-cell product sidesteps the whole problem of multi-cell charging.[913] Where several packs are present, a charger may handle them one at a time: in principle packs could be paralleled and the charge split between them, but packs that are paralleled to charge cannot simultaneously be in series to power the product, so a device that charges while running must keep them in series.[1460] Separate charge circuits per battery are also used, as in a portable DAC with two independently charged cells.[1613]

In a large series pack, keeping all cells at roughly the same voltage matters, and cells are sourced matched from the same batch to that end.[923] Balancing is visible during recovery charging of a nickel pack, where individual cells converging toward the same voltage indicates the pack is coming back.[XpZVIWdXliY]

## Deeply discharged packs and under-voltage lockout

The most common charging failure in a dead device is not a dead cell but a protection circuit latched off. A pack that has been drawn down below its threshold trips under-voltage lockout, after which the product's own charger will not restart it — a device left on its charger for days will simply flash and refuse, which is a design oversight when the product is a standalone power bank.[1707][8P8Af5SR57U] The remedy is to bypass the internal charging circuitry and apply constant current directly across the cell terminals until the pack rises above lockout: a GPS unit sitting at 2.5 V and refusing external USB charge went straight into constant current at 400 mA from a bench supply and recovered.[KTr-44n0bbU][XpZVIWdXliY] The behaviour is then confirmed the ordinary way, by watching the pack transition into constant voltage with the charge current tapering.[KTr-44n0bbU]

Under-voltage lockout, in the cases where it acts before the cell is damaged, is what saves the pack rather than what breaks it.[8P8Af5SR57U] A pack that is merely flat, rather than latched, will still misbehave in circuit: an uncharged battery can load down the rail feeding the processor enough to cause repeated resets, which reads as a hiccuping power supply until the battery has taken on enough charge to stop being a burden on the rest of the circuit.[1662]

## Diagnosing charging from the outside

Charge state is readable from input current without opening anything. A camera drawing 150 to 180 mA on USB that collapses to about 1 mA within five seconds is not charging its battery; it has recognised a full or unreachable cell and dropped to standby, whereas a sustained draw of 150 to 160 mA is genuine charging.[1433] An e-reader drawing 460 mA is putting essentially all of it into the battery, since an e-ink display needs no power to hold an image and the device only wakes to scan the touchscreen.[1370] Where the product is supposed to charge only while switched off, a cell that recovers no faster with the charger plugged in localises the fault to the charging path rather than the battery.[1433]

Indicator behaviour is a second, weaker channel: an amber LED going green on completion,[205] a battery symbol flashing fast for charging and slow for discharging,[1719] or a state-of-charge readout that reports the battery as too low and shuts the product down even while current is demonstrably flowing into it — which points at a second fault in the charging chip alongside the failed cell.[1370] A charger that begins a charge cycle with no battery installed is unambiguously faulty.[1460]

Some designs expose the battery directly enough to be charged through an unexpected port. A portable power station whose nominal 12 V output is connected straight across a 12.8 V pack, with no 12 V regulator in between, will charge that pack when 12 V is applied to the output.[-ir61ARd5T4] Other designs invite disassembly instead, with the pack contacts sitting directly across the cells so the internal charging circuitry can be bypassed.[XpZVIWdXliY]

## Charging from the mains supply

Backup power systems face the problem of pushing large amounts of energy into large packs without dedicated charging hardware. One line-interactive UPS solves it by running its inverter backwards: the H-bridge MOSFETs' substrate body diodes rectify power fed back through the transformer, energy is stored in the winding inductances, and large bulk capacitance filters the result to charge the batteries.[504] With the H-bridge devices as the only power semiconductors present, this is the only route by which enough power could reach the packs.[504] The approach is documented in US patent 5,302,858, "Method and apparatus for providing battery charging in a backup power system".[504]

At the other end of the scale, a NiMH fast charger routes current down through a ladder of MOSFETs and into the battery, and the same shunt reads current in one direction during charge and the opposite direction during discharge, since the pack's positive terminal sources current on discharge.[812]

## Grid-scale and vehicle charging

Domestic storage inverters make charge scheduling a tariff-arbitrage problem. A hybrid inverter can be configured for time-of-use offsets between grid, battery, and load, supports flexible dynamic battery charging across different chemistries, and accepts solar, wind, generator, and microinverter inputs.[1628] Where a network has excess solar and offers a free-power window — for instance three hours from 11:00 a.m. to 2:00 p.m. — charging the house battery inside that window is worth doing regardless of what the sun is doing.[HctGMxWPWRE] The binding constraint is charge power rather than storage: a 25 kWh battery limited to a 5 kW maximum charge rate can absorb at most 15 kWh in a three-hour window, which is roughly overnight supply.[HctGMxWPWRE] Raising the inverter from 5 kW to 8 kW exists specifically to fill more of that window, and the same window is used to charge an electric vehicle.[kKfZgAyFu8Q] Accounting across AC-coupled sources is not straightforward: 0.6 kW from one array plus 0.08 kW from a microinverter does not obviously produce 1.24 kW into the battery.[BXVgk-uoxn8]

Electric vehicles charge in the other direction as well. Regenerative braking returns energy to the pack whenever the driver lifts off the accelerator, which is the desired behaviour in about 95% of lift-off events; disabling regen restores true coasting, limited only by tyre rolling resistance and aerodynamic drag.[1432]

## Harvested energy and charging arithmetic

Claims that ambient energy can charge a phone collapse under a straightforward energy balance. A device that charges a phone from 30% to full in about 90 minutes is doing so from an internal lithium-ion battery that was charged conventionally beforehand — functionally no different from a pair of AA cells and a 5 V generator.[55] A thermoelectric watch harvesting on the order of 0.77 mWh per day would need 961 days, about 2.6 years, to fill a 740 mWh cell from flat, and that figure ignores losses in the DC-to-DC converter and the charging process entirely.[945] Phone-to-phone charging over NFC fails on a second ground beyond the power budget: no circuitry exists in NFC-equipped phones to route received energy back into the battery, so even the tens of milliwatts theoretically available cannot be stored.[1099]

Harvesting that is engineered rather than asserted works, and is specified accordingly: a solar-powered meter with a genuine rechargeable cell has its charge rate quoted for a given illuminance in lux.[1608]

## Charging interfaces

The charging connector is a frequent point of failure and of deliberate lock-in. Designing proper in-camera charging circuitry and then fitting a connector that resembles micro-USB closely enough to invite the mistake, while requiring the manufacturer's own cable, negates the benefit of the charging design entirely.[578] Proprietary multi-contact barrel jacks with an inner ring in addition to the outer ring and tip serve the same purpose.[Cn3DVQGmF9A] Worn or marginal DC jacks are a diagnostic hazard in their own right, requiring physical pressure before any current flows.[XpZVIWdXliY]

Alternatives exist. One handheld meter dispenses with a DC jack and charges through its ground and milliamp banana jacks, marked as such on the front panel, running a three-minute self-test on connection to determine whether the installed cell is an alkaline primary or a rechargeable before starting a charge and reporting a time to completion.[56] Docking contacts serve the same role in mobile robots, where returning to a charging station and charging unattended is the whole point of the product.[980][429]

Charging hardware is also treated carelessly in the field. A mains tool charger visibly melted and well past its test date, left permanently plugged in and in daily use to recharge tool packs, is the ordinary state of such equipment on a work site.[YaTldV7-uXo]
