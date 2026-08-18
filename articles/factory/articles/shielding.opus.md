# shielding

Shielding is the use of conductive material -- cans, plates, cases, foil, braid, ground planes, plated case interiors -- to block electromagnetic coupling between a circuit and everything around it. It serves two separate purposes that are frequently confused: keeping outside interference out of a sensitive circuit, and keeping a noisy circuit's own emissions in so the product passes EMC requirements.[1679][735] Both jobs can appear in one instrument, and a shield fitted for one reason does not automatically do the other well.[1602][1679]

## Two directions, two problems

A shield placed to protect a circuit is solving a susceptibility problem; a shield placed to contain radiation is solving an emissions problem, and the design decisions differ.[1679] In an amplifier, a shield over the switching supply exists mainly to keep switching noise out of the analog section, with EMI compliance as a secondary motive -- which is why the unit can be powered up safely on the bench with that shield removed.[1602] A small can over a modem chip with nothing but copper on its underside is doing little for the circuit itself and is most plausibly there to satisfy an EMC requirement.[735]

Whether a circuit needs shielding for immunity at all depends on its impedance. A low-impedance node -- a 50 ohm driven output, for instance -- is hard to disturb, because the interfering sources coupling into it are high impedance and cannot force meaningful signal onto it.[1679] Such a circuit may still need shielding to stop it radiating, but that is the other problem.[1679] Conversely, high-impedance and low-current front ends are where shielding becomes decisive: down at nanoamp levels, an LED stuck into the middle of an input connector produced 1.1 nA of generated current, and simply bringing a hand near the input increased the pickup.[1755]

## Internal shielding and crosstalk

Much shielding inside instruments is not aimed at the outside world at all but at channel-to-channel and section-to-section coupling.[1679][1101] In a multi-channel arbitrary waveform generator, the shielded channels are shielded because they swing large square waves at high voltage into a low impedance and would otherwise couple into the physically adjacent channel; the coupling works in both directions, so the neighbour on the other side needs treatment too.[1679] Leaving the remaining channels unshielded is a deliberate cost-cutting decision justified by their low-impedance nature.[1679]

RF instruments carry this furthest. Critical RF blocks -- preamps, mixers -- are physically separated and enclosed in machined aluminium blockwork, and the same reasoning that demands physical shielding also demands local regulation per section, because crosstalk can travel by way of a shared supply rail as easily as through the air.[1101] Wireless microphone hardware separates and shields each section individually.[571] One signal generator goes as far as shielding inside the shield, with an additional tag bonding the inner enclosure to the upper plate beyond what the screw holes already provide.[261] A high-voltage differential probe is shielded almost throughout, with separate cans for the input and output sections that must be desoldered to reach the front end.[932] A modular test set built around RF cans was partitioned from the outset so that modules could be shielded and still be accessed, serviced, tweaked in production, and recalibrated.[1256]

Where internal shielding is absent, the failure is concrete: unshielded superregenerative receivers interfere with each other badly enough that the standard workaround is to physically separate them, a problem of system design rather than anything inherent to the regenerative circuit.[767] Not all internal shields are equally effective -- a small can mounted to the board over a level-control section containing a couple of trimmer pots and a trimmer capacitor is of doubtful benefit.[265] In one bench multimeter the shield is a mains-earth-referenced trace routed to snake around the board, isolating the mains-referenced portion from the measurement circuitry, rather than a can over the digital section.[427]

## Ground planes and the PCB as a shield

Copper planes inside the board are themselves shielding. A solid ground plane and power plane provide shielding against magnetic and electric fields, on top of the lower inductance and smaller loop area they give the return path -- a measurable EMC difference between a two-layer and a four-layer version of the same circuit.[1176] Even where no metal can is fitted, inner-layer ground plane under the main circuitry provides some protection.[344] Signal traces sandwiched between top and bottom ground planes are shielded by them, and via stitching around the board perimeter closes the edges.[1315] Taken to its conclusion, plating the board edges and connecting them to the ground plane forms a shielded box with all signal layers enclosed inside, so signals cannot radiate out of the sides.[1193]

At extreme sensitivity the PCB itself becomes part of the shielding problem alongside guarding, dielectric material selection, and via fencing.[1755]

## Cables and connectors

In a screened twisted pair, the screen keeps out electrostatic noise -- interference capacitively coupled from nearby conductors such as a mains wire -- while the balanced twisted pair rejects magnetically coupled noise from transformers and current-carrying conductors.[616] The two mechanisms need different countermeasures, and the cable construction addresses both.

Good video cable is layered for the same reason: an outer braid, a foil beneath it encasing the whole bundle, and individually shielded inner pairs to stop crosstalk between the internal signals.[1028] For critical low-leakage, low-current measurement the connector of choice is triaxial coax, which adds a guard conductor between the inner and the outer shield.[607][1017] Ribbon cable and flat flex runs are shielded too, either with foil wrapped around the cable or with a dedicated shield plate covering the run.[648][384]

## Low-level measurement

Precision low-current and low-resistance work is where shielding becomes the dominant design constraint. Precision high-value resistors are mounted in double-shielded boxes, isolated with minimum capacitance to their surroundings.[406] In such a fixture the outer case is connected to mains earth while the instrument input is not earth-referenced; the internal ground can be shielded as a second layer if measurements go low enough to warrant it, though double shielding is not always necessary.[406] A resistance calibrator puts its mains transformer inside its own shielded box, and the precision reference resistors and relay switching are shielded several layers deep.[544]

The payoff is visible on a noise floor. A properly shielded analyser with a 50 ohm terminator on its front end shows no 50 Hz pickup whatsoever in a laboratory saturated with mains-frequency fields; connecting a practical circuit instead almost always brings some 50 Hz back.[528]

A precision low-frequency instrument built around a CRT illustrates the complete approach: the front panel that appears to be plastic is nickel-screened and conductive, bonded through a metal tab to the chassis, the CRT itself is shielded, and the front panel mesh exists to stop the CRT scan frequencies escaping.[524] The reason is specific -- the scan frequency of tens of kilohertz falls in the middle of the instrument's DC to 100 kHz measurement range, so any leakage lands directly in the measurement band.[524]

## Making the shield actually work

A shield is only as good as its connection. In a handheld meter the arrangement is typically a metal shield or foil insert in the case rear plus a spring contact that grounds it to the board; the absence of that spring and foil is a straightforward place to save cost.[344][171] Conductive sponges serve the same function of bonding a board-level shield to case-mounted screening.[295] A shield with no visible spring or contact point is suspect, and unbonded shielding is a plausible explanation for pickup observed on a sensitive ohms range.[1723] Nickel screening on interior plastics only works when it reaches a chassis connection.[524][8h-5cx-qiqo]

Transformer shielding is a similar matter of optimisation -- getting the shield placement right for common-mode noise performance is an iterative process, far easier with a supplier close enough to visit and adjust in person.[1032]

A simple bench test of an instrument's shielding is to place an active mobile phone call beside it and watch whether the reading moves at all; it applies to a wide range of instruments.[115]

## Where shielding is spent and where it is skipped

Shielding costs metalwork, mass, and assembly time, so its presence and absence both encode design decisions. Heft is a rough proxy: several kilograms of instrument implies significant shielding and possibly a die-cast RF front end, while a suspiciously light instrument has little shielding inside.[391][480]

Common economies include leaving can footprints on the PCB and populating none of them, having designed in the ability to shield and then deciding it is unnecessary.[1545][1596] A front end may be only partially shielded because heatsinks must protrude through the can.[1146] Two variants of the same oscilloscope family can differ in that the higher model encloses the power supply while the lower one leaves it open.[1042] The bottom of a board may be left unshielded because it already sits hard against a die-cast case.[875] A plastic cover over a voltage reference and ADC is not a shield at all -- it is there to keep fan-driven air currents off the parts, with the actual shielding on the base of the board.[731] Cheap meters omit internal shielding entirely.[1692]

At the other extreme, retro computers and consoles carry substantial soldered-down shield cans that must be desoldered to get inside.[491][438] Spectrum analysers carry additional shielding blocks over individual subsystems, and mechanical accommodations -- a cutout in the main cover for a tall inductor, then a plate over the cutout -- keep the enclosure intact.[470] Shielding also gets added after the fact: a bodged shield tacked down to a couple of pads over a chip is a retrofit for a problem found late.[1450] Gaffer tape holding a shield in place is not.[1278]

Sealed applications shield for safety rather than performance. A parachute automatic activation device is enclosed in a fully shielded case with a shielding wire, so that a nearby radio transmitter cannot set off the pyrotechnic charge.[339]
