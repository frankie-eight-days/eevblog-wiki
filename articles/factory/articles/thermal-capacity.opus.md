# thermal capacity

Thermal capacity is the ability of a soldering iron, a tip, or a workpiece to store heat and keep delivering it into a joint while the joint draws that heat away.[180][596] It is the single property that separates an iron which melts a joint on contact from one that stalls against a ground plane, and it is largely independent of the temperature the display shows: two irons set to the same number will behave completely differently once the tip touches metal.[596][1063] It applies in both directions — the same physics that lets a big tip drive a joint also lets a large component keep sucking heat out of the iron, and keeps that component dangerously hot long after the joint is finished.[183][186]

## Why irons run far above the melting point of solder

Standard solder melts at somewhere under 200 °C, yet soldering irons are set to 350 °C or so — around 680 to 700 °F — and their dials commonly run to 480 °C.[180][596] The reason is thermal capacity rather than metallurgy. A tip sitting in free air will regulate very close to its setpoint, but the moment it contacts metal the work transfers heat out of the tip faster than the heater can replace it, and the tip temperature drops.[180] The setpoint is therefore chosen as headroom against that drop, not as the temperature the joint is expected to see.

This makes the setpoint a compensation mechanism for a deficiency. An iron with low thermal capacity has to be run hotter to do the same work, which is exactly the trade a cheap station forces on its user.[596] Measuring what actually happens at the joint is not straightforward: getting a proper temperature reading of a solder joint as it collapses is an involved exercise, and readings taken on the opposite side of the joint from the tip are one practical approach.[596]

## Tip geometry and mass

Thermal capacity is dominated by the physical bulk of the tip. A large chisel or wedge tip stores and moves far more heat than a fine conical one at the same temperature and the same station.[1645][1646] The difference is stark enough that a single station will pass and fail the same task depending only on which tip is fitted: with the smallest conical tip available, a Pace station struggles on a TO-220, and with a higher-capacity chisel tip on the same iron at 370 °C the joint melts without difficulty.[1645] There is a hard ceiling on what a tiny tip can do, regardless of the station behind it.[1645]

The constriction matters as much as the mass. A large tip lets a station push essentially all of its available power into the tip and keep it there, while a thin tip forms a bottleneck that limits transfer no matter how much power the base can supply.[1646] Tip range is consequently part of what an iron is: a system offering only small tips suited to mobile phone work cannot serve as a bench iron, whatever its rated wattage.[5vbg8QEZXfY]

Tip construction introduces a deliberate trade-off. Pace tips carry a thicker iron plating, which lengthens tip life at the cost of heat transfer; JBC tips use a thinner iron plating and deliver better thermal performance for the same power input.[1106]

## Power, technology and rated wattage

Direct-heat irons, in which the heater sits at the tip, have inherently better thermal capacity than older designs with the heating element set back from the tip.[1064] Power ratings give a rough ordering — a JBC CD-2BB is nominally 130 W and other bench irons peak around 135 W — but the rating is a claim about the heater, not a guarantee of delivery.[5vbg8QEZXfY][1064] Irons rated at 80 W and 100 W have failed to meet their claimed thermal capacity under test, and the discrepancy is large enough to be the deciding factor in whether an iron is fit for bench use.[5vbg8QEZXfY]

Portable USB-PD irons are additionally limited by their supply. A TS80P has better thermal capacity than its predecessor on paper, but fed from an 18 W pack that cannot deliver, it performs no better than the original TS80.[1319]

## Testing

The standard bench test is to submerge the tip in water and watch what happens. An iron with adequate capacity keeps the water boiling and sizzling with the tip fully immersed; one without it cannot hold the tip above 100 °C.[1646][1650][5vbg8QEZXfY] An 80 W iron tested this way peaked at around 55 to 57 °C, reaching only about 60 °C with the whole tip submerged — far short of boiling, and consistent with its failure on real joints.[5vbg8QEZXfY] Desoldering tweezers driven to maximum power settled at 58 °C, which is poor on this measure though still usable in practice.[1650] Where a station reports power as a percentage, a large-capacity tip will show it accepting 100% of available power.[1646]

A sponge-water variant discriminates between comparable bench stations. Holding a Hakko FX888D tip in sponge water dropped it to roughly 230 °C, while a Weller WE1010 fell much further and much faster, settling around 100 to 140 °C — a direct indication of lower thermal capacity despite otherwise decent tip temperature sensing.[1063]

Repeated soldering onto a ground plane is the corresponding functional test, and an iron can pass it within its intended scope even if it would lose an outright comparison.[5vbg8QEZXfY]

## Comparative behaviour

Side-by-side work makes the property visible without instrumentation. A JBC set to 270 °C heats a joint thoroughly, right through to the far side, while a cheap Yihua 936 set to 350 °C reaches only about 215 °C on the opposite side of the same joint and visibly struggles.[596] On a heat-sink joint, a Hakko 936 at 300 °C gets there only with difficulty where the JBC at 270 °C passes straight through.[596] Metcal irons are regarded as production tools — fixed temperature, fixed job, very high thermal capacity — while a JBC matches that capacity and adds adjustability.[500]

## The workpiece side

Thermal capacity belongs to the work as much as to the iron. Soldering a TO-220 tab down to a ground plane means driving a component and a plane that act together as a heat sink, and it demands a much bigger tip than the leads would.[183] A joint on a heavy copper pour takes noticeably longer to melt because it draws away far more heat than a small component; on a large tab, one end will wet while the other cools instantly until enough energy has gone in to bring both up together.[183] Large surface-mount devices such as a D-pack, with a big thermal pad connecting to a heat-sink ground plane, are the surface-mount equivalent.[186] For large ground planes the practical answer is a high-capacity iron such as a Metcal, a very large tip, or both.[183]

The same mass that resists heating retains heat afterwards. Large components trap heat and stay very hot well after the joint has solidified, which is a burn hazard rather than a soldering problem.[186][183]

## Desoldering and hot air

Desoldering stations are judged on thermal capacity alongside suction. A ZD985 handled a multi-layer motherboard with inner planes — requiring longer dwell, with a correspondingly greater chance of heating adjacent components than on a double-sided board — while showing little temperature droop on the display and working mostly at 300 °C against a 480 °C maximum.[542] Its combination of suction and thermal capacity was found equal to Hakko equivalents in use.[542] Hot air stations face the same requirement at larger scale: a Quick 861 Pro carries more than enough thermal capacity to lift a large BGA such as a GPU with a high ball count.[1659]

## As a purchasing criterion

Thermal capacity is one of several axes an iron must be judged on, alongside price, tip compatibility and user interface, and the correct weighting depends on the intended work.[5vbg8QEZXfY] An iron with modest capacity may be entirely adequate for small, low-thermal-mass work such as phone repair while failing outright as a bench iron, and the same iron can be acceptable as a portable and unacceptable for large cable connections in the field.[5vbg8QEZXfY] A plastic cutting tool needs only to heat up and cut, so a soldering iron's level of thermal capacity is simply not required of it.[880]

Capacity claims are also not always transferable between similar-looking products: the Hakko 936 was reportedly of better thermal capacity than the 926, and lesser-known brands are sometimes represented as matching JBC-class performance.[596][2vJ0c0ioAXY] Where capacity is deficient because of tip range rather than the station itself, a revised tip line-up can change the assessment.[5vbg8QEZXfY]

Dave Jones's own bench choice rests on this property: the JBC CD-2BB displaced a long-serving Hakko as his main iron specifically on thermal capacity and speed of heating, and an iFixit FixHub replaced a TS80 as his portable, on thermal performance together with construction and interface, despite not being a leader on capacity.[472][400][5vbg8QEZXfY][1646] Testing thermal capacity and cutting some joints is treated as the core of what a soldering iron review consists of.[111]
