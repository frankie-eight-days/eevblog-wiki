# electrical contact

An electrical contact is the separable metal-to-metal interface through which current passes between two parts that are not permanently joined: switch wipers, connector pins, battery springs, card-edge fingers, pogo pins, relay and contactor tips. Because the joint depends on force, plating and cleanliness rather than on a metallurgical bond, it is one of the least reliable elements in a piece of equipment, and a large share of intermittent, pressure-sensitive and temperature-sensitive faults trace back to one.[808][1091][h9V0qJ4p3Aw][406] A contact that should measure close to zero ohms can instead sit anywhere from a couple of ohms to many hundreds of ohms, and the circuit around it rarely tolerates that range.[1361]

## Construction and materials

Contacts are generally formed sheet metal, folded or stamped into a curved or cantilevered spring that bears against a mating pad or pin.[135][99] Brass is common in low-cost consumer hardware, sometimes plated and sometimes painted over as a cosmetic finish.[135] Precious and semi-precious platings are used where reliability matters: gold on pogo pins and on quality banana plugs, and silver plating on the moving contact of tactile switches.[MqECOT5j-cE][1052][1361] Plating quality is not guaranteed by its presence — the gold on some connectors is bad enough that it should not be relied upon at all.[1052]

Multiple contact points per connection are a deliberate reliability measure. A tactile switch may split its central contact into two, giving two independent paths through the dome.[1361] Wafer switches in instrumentation can carry two contacts on the top surface of the board and one on the lower surface, wiping the same track from both sides.[693] Card-edge and connector arrangements vary from single-sided fingers on one face of the card only, to dual contact schemes on battery and terminal pads.[1404][1263][ZlDf1d18Kag]

Contact force comes from a spring, and the amount of it sets the quality of the joint. Heavy spring tension gives low resistance and reliable contact on wires with metal-on-metal engagement throughout.[749] Deep-travel contacts with a long spring stroke are a sign of a generous design.[1083] At the other extreme, mains plug contacts are held by comparatively little force, which is why the bulk of the resistance in a chain of plugs and sockets sits in the contacts rather than the wire: 283 double adapters in series with a 2 kW load measured about 9.5 milliohms in total for both the wiring and every contact in the chain.[1526]

## Contact resistance and its consequences

Where the contact resistance appears in a circuit determines how much damage it does. A resistive keypad that reads many buttons through a ladder divider into a single ADC pin is fully dependent on the contact resistance being negligible; a switch that drifts up into the tens or hundreds of ohms shifts the divider output and the microcontroller reads the wrong key or none at all.[1361][1360] The same physical fault in a power path shows up instead as a voltage drop, or as an appliance that simply does not start — a mini PC that used its standoffs as the main power rail failed to power on until thumb pressure on the board restored the contact.[1739]

Contact position also matters for bulk-resistance measurements. Sheet resistance figures assume the connection is made across an entire edge of the material, side to side; probing at a point or at an angle on the top surface does not measure the same thing, though on thin PCB copper of around 35 microns the approximation of an edge contact holds well enough.[732]

## Wear

Switch contacts wear by sliding, and the concern with that wear is twofold: loss of the plating and metal debris migrating between adjacent pads and shorting them.[u2-ot2vWLxI] Cycle testing of a multimeter rotary range switch found the contacts in good condition after 10,000 and 25,000 cycles with contact resistance still a couple of ohms, and still clean at 50,000 and 51,000 cycles with hardly any metal wear and no evidence of debris shorting.[u2-ot2vWLxI] The visible damage was largely dust caked under the wiper and a track between two contacts where the solder mask had worn through — the wear looks far worse than it measures.[u2-ot2vWLxI] Failure, when it came, was judged not on resistance but on function: the switch was deemed failed once a particular position misbehaved in diode mode.[u2-ot2vWLxI]

Well-made contacts have very long lives. The wafer switch contacts in a 52-year-old transistor analyser remain reliable, and a retro multimeter's range switch contacts show little or no wear despite an otherwise crude construction.[693][482]

## Failure modes

The recurring causes of contact failure are contamination, corrosion, insufficient force and mechanical damage.

Contamination need not be conductive to cause trouble. Resistors pulled from bandoliers carry glue on their leads that stops them making good contact with the springs inside a breadboard; trimming the lead ends is the fix.[471] Corrosion and general crud accumulate on plug contacts held with light force, and discolouration of one terminal relative to its neighbours in a connector is a good indicator of which one is dodgy.[1526][h9V0qJ4p3Aw] Alkaline battery leakage attacks contacts and pins directly, and where it has eaten through them the repair stops being worth the effort.[ZlDf1d18Kag]

Insufficient force is often mechanical damage in disguise. In a rotary pulse encoder, a bent arm never had enough force to make contact against its mating surface as the mechanism flipped it over, while every other contact in the same part measured fine.[1573] A pushbutton contact pressed in further than its neighbours and failing to spring back produced an intermittent sensor fault in a printer.[p5-p8Iu7E1c] Assembly tolerances count too: a jack screw not tightened down enough by the assembler made contact only intermittently and failed on the milliamps range during production testing.[588] Enclosure screws often supply the contact pressure themselves, so a meter reassembled loosely will read differently from one done up properly.[uZ1vXaBPLTY]

Design can eliminate a contact entirely. A mains filter earthed only by a screw pressing into a threaded hole surrounded by plastic makes no reliable connection to the chassis at all, and over-moulding a little more plastic would remove the contact altogether — a crimped wire run directly to the front panel is the correct approach.[449] Similarly, contacts made by steel nuts held against magnets are expected to be worse than spring terminals and to grow grubby, and troubleshooting a bad contact in such a system is very hard.[27aG9xhfk6s]

## Diagnosis and repair

A contact fault announces itself by responding to pressure. Pressing on a suspect hot-bar-soldered display connector makes segments of a scope trace line up, which is close to proof that the contacts under it are bad.[808] Wiggling probes, holding plugs together by hand, and having a reading change as the joint is disturbed all point the same way.[1052][KTr-44n0bbU][XpZVIWdXliY]

Continuity testing isolates the fault: buzzing a contact straight through to its pin distinguishes a broken conductor from a contact that simply is not mating.[1573] Where a fault persists with the contacts demonstrably working every time the device does run, contacts can be ruled out and the search moved to the silicon.[f-LTv1GqCMw] With ribbon cables, reseating both ends first is the standard opening move, and shiny contacts at one end direct attention to the other connector.[1376]

Cleaning is usually the repair. Most switches are self-wiping, so working a suspect switch through several rotations will shift the gunk on its own — this is what makes a fault occasionally clear itself after a couple of operations.[m3sQHx5aMmU][406] Where that is not enough, the recommended procedure is to open the instrument, clean the contacts with isopropyl alcohol and a cleaning brush, and scrub them.[m3sQHx5aMmU] Contact cleaner and lubricant applied into an inaccessible automotive switch serves the same purpose.[h9V0qJ4p3Aw] For pressure contacts against a PCB pad, a dollop of solder added to the pad restores engagement, though this is a stopgap rather than a long-term repair and the board underneath can still corrode.[1756]

## Contacts as an interface

Beyond carrying power, contacts frequently form the data and sensing interface of a product. Four sprung contacts in an e-reader case cover carry a serial interface — transmit, receive, ground and a fourth pin — while doubling as the mechanical retention clips that lock the device in place.[135] A waste toner box uses a pair of wiper contacts that are shorted when the box is good and are mechanically unmated by a spring-flipped lever when it fills, so the presence or absence of a short is the sensor output.[p5-p8Iu7E1c] Not every visible contact is used: a wireless multimeter's flexible current clamp interface presents three connections of which one is a dummy.[417]

At the high-current extreme, a contactor is a solenoid-driven pair of large contacts that simply bridge the load circuit, and the return spring holding them can look distinctly underspecified for the job.[1457]
