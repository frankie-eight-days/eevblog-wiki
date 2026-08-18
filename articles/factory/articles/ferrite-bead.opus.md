# ferrite bead

A ferrite bead is a small block of ferrite placed around a conductor so that the conductor becomes a lossy inductor at high frequency. A wire with a bead threaded onto it is "essentially an inductor"; the ferrite contains the magnetic field that surrounds any current-carrying conductor and makes that inductance more effective than the bare wire alone.[1406] Its purpose in a product is almost always electromagnetic compatibility — knocking the sharp edges off fast switching waveforms and stopping high-frequency energy from travelling along power rails, signal lines and cables where it would be radiated or conducted out of the box.[1021][347][725]

## Impedance rather than inductance

Beads are specified by an impedance at a stated frequency rather than by an inductance value, and packages are sometimes marked with that figure — a bead may carry a number such as 200 ohms which is its impedance in quotes at frequency, not a DC resistance.[987] Values in the low hundreds of ohms are typical; a bead in a consumer audio product's power-key line is a 220 ohm part.[1672] Because the DC path through a bead is essentially a short, a bead sitting in a signal line is transparent to the function of the circuit until something makes it open.[1672][884]

Where more attenuation than a single bead can give is needed, the usual escalation is more turns: winding the conductor through the ferrite several times, or moving to a wound coil, is the standard way of making the same core more effective.[1406] Cable assemblies take the opposite approach and simply use many discrete beads along the run.[202]

## Where they get fitted

Power entry is the most common location. Beads appear on IEC mains inputs alongside the filter can and the voltage selector,[281][308] on external DC input jacks for noise suppression to help a product pass CE compliance,[234] and on the wiring leaving a switch-mode supply.[261][875] A DC-DC converter module quoting less than 75 mV of ripple and noise is not quiet by bench standards; a ferrite bead on the output, followed by a linear regulator, is the way to bring that down.[324]

They are equally common on individual leads and traces: on the cathode of a rectifier diode to take the edge off the waveform,[360] on the lead of a regulator or diode inside a laptop,[639] on the negative sense line of a bench supply but pointedly not the positive one,[755] on a BNC input where DC is also being fed up the coax to a masthead amplifier,[956] and around the ground input jack wiring of a handheld meter.[1393]

Cabling and flexible interconnect attract the largest ferrites — across an LCD ribbon cable,[985][1261] on the ribbon cables of a front panel,[1513] on every channel of an ultrasound probe's cable bundle,[1315] on the cables of a plasma television so the product meets its EMI limits,[725] and on flat-flex, where a purpose-made flat-flex ferrite is an uncommon and worth-keeping salvage part.[488]

The practice is old. A 1980s home computer used ferrite beads to take the edge off 5 V TTL running around a double-sided PCB with no ground plane,[1021] a contemporary 16-bit machine carried beads and ceramic capacitors on all its external ports,[438] and one minicomputer-era board carried what appear to be beads on the leads of every single ceramic capacitor on it.[1404]

## Layout and integration

On a board, the bead is normally placed immediately adjacent to the decoupling capacitor it works with; crowding a bead and a capacitor together where space is tight is ordinary PCB layout practice, even when the board in question had room to spread them out.[1602] Beads are also placed in the ground path, deliberately separating one ground region from another — for example a current-input ground from the system ground.[987]

Mechanical integration can go much further. One projector power supply had mounting posts and bead cradles moulded into the fan assembly, sized around a known number of turns, so the wiring loom and its ferrites were designed as one piece — a level of integration design effort that is unusual.[1546]

## Choosing the wrong value

A bead is not a free component. Because it is an inductance, it can resonate with the capacitance around it, and getting the value wrong can create the emissions problem it was fitted to prevent. In one bench multimeter, beads placed between the current-input ground and the system ground were the wrong value and resonated near 13 MHz against the ground planes' capacitance, causing both conducted and coupling-mode failures.[987] The fix was not extra shielding and not extra components: the internal shielding was unchanged, the beads on the voltage inputs were untouched, and the correction amounted to changing bead values — and a resistor — on existing production boards.[987] Diagnosing this kind of interaction takes substantial engineering effort, and the same mechanism is known to occur when bypass capacitors resonate with trace inductance at a particular clock frequency.[987]

The general lesson is that beads are a mitigation to be verified, not a talisman. Two beads sitting loose inside a rechargeable toothbrush around a drive coil made no measurable difference to the waveform at all.[284]

## Failure and diagnosis

Because a bead is normally a near-short at DC, an open bead reads as a broken connection and can take out a whole function. A production multimeter was repaired by tracing a fault down to a single failed RFI bead; the soldering was sound and the component itself was bad, and the isolated nature of the failure argued for a one-off part defect rather than a bad batch.[884] Continuity checking a bead in a signal path is a standard step when hunting a break: beads in oscilloscope channel circuitry were checked and found not open,[565] and a power-key line was traced through a bead to the switch when the path measured open elsewhere.[1672]

## Substitution and rework

When EMI requirements do not apply to the immediate task, a bead can be bridged. A zero ohm resistor is the correct substitute; a mod wire is worse, because a length of wire can act as an inductor in its own right unless it is genuinely low impedance, so proper surface-mount zero ohm parts are preferred.[884][987] A board whose silkscreen designates a bead position but which is populated with zero ohm resistors reveals the designer's original intent and a later change of mind.[987]

## Analogue and RF uses

Beads are not only an emissions tool. Isolating an amplifier input with a ferrite bead raises the source impedance at high frequencies, which is one countermeasure against the negative-impedance oscillation that emitter-follower output stages exhibit into a capacitive load; beads work up in the hundreds of megahertz, well above the transistor bandwidths involved.[629] Beads have also been proposed across switching components such as a MOSFET to damp ringing in a power supply, as one of several possible mitigation strategies.[1266]

Used as ordinary inductors in an RF context, salvaged beads are unpredictable. An unmarked SMD bead substituted into a tuned circuit shifted the resonance to around 125 MHz and behaved poorly at the top end, compared with a 500 nH salvaged inductor that gave about 70 MHz.[343]

## EMC workflow

The bead's role in development is as a cheap, late variable. In-house pre-compliance conducted emissions testing lets a design be changed — adding a few ferrite beads, adding shielding — and then re-run on the identical setup to see what each change did to conducted and radiated emissions.[548] The 121GW multimeter's development went through EMC issues that required a redesign, with RF beads added at various points in the circuit across several prototype rounds.[e9cpKN69Avk] Conversely, a large ferrite appearing across a ribbon cable in an otherwise tidy instrument reads as a late EMI fix.[985] Well-executed instrument power supplies are recognised in part by their attention to EMC with beads and related parts.[790]
