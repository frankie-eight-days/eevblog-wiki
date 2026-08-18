# solder

Solder is the fusible alloy that joins electronic components to a printed circuit board, and it does two jobs at once: it forms the electrical connection, and it provides the mechanical rigidity that holds the component to the board.[1281] It is common to hear that solder is not meant to act as mechanical strain relief, but mechanical retention is in practice one of its two principal purposes, and joints that lose it fail.[1281] Of everything on the bench, the solder itself — the right type, in the right diameter — is the single largest determinant of joint quality, ahead of the iron.[180][168]

## Diameter

Fine solder is the default recommendation: the smallest diameter that will do the job, and certainly under 0.5 mm.[180][200] A fine wire gives control over exactly how much metal enters the joint, which is the whole point, because too much solder is itself a defect.[183] Typical working sizes are 0.46 mm for general through-hole and pad tinning,[180][181] 0.38 mm for surface mount,[1306][KzC12xtHuXo] and 0.35 mm down to 0.3 mm for the finest work such as soldering directly to a hard drive's micro-actuator flex.[1400][1205] At 0.38 mm the wire is about as small as commonly available, and it is fine enough that it is not really intended for through-hole work — feeding a through-hole joint with it takes a great deal of wire.[1205] For surface mount the fine wire is preferred precisely because feeding 0.8 mm stock gives far coarser control.[1306]

Thick solder still has a place. Soldering a component down to a ground plane, where the board acts as a heat sink, is done with a large chisel tip and 1 mm wire, because in that situation controlling the quantity of solder matters much less than getting metal and heat into a thermally massive joint.[183] Carrying only one diameter in a field kit is a limitation: a 1 mm roll is awkward when the task is feeding solder sideways into a broken connector pin.[1195] A minimal lab stocks both a fine roll and a coarse one, in both leaded and lead-free.[954][1319]

## Alloy

Standard 60/40 tin-lead, optionally with a small silver load, is the recommended general-purpose alloy; lead-free is explicitly not the first choice for hand work.[168] Leaded solder reflows at a lower temperature, which is the practical reason to prefer it even on processes that tolerate both.[614] Lead-free tin-copper is used where the process demands it.[1306] Lead-free joints are also implicated in cracking failures: a Garmin GPS whose connector joints had every single one broken is the characteristic presentation.[1281]

Alloys far from the eutectic behave very differently. A 97/3 solder, used at 180 micron pad width in an IBM multi-chip module, is brittle enough that chips can be pushed off their pads at room temperature with no heat applied at all, and the solder smears rather than deforming like familiar 60/40.[1341][2G7Z9IIQoIs] Only the smallest parts resist this: chip capacitors and the large chips with many hundreds of balls under them have too many joints to shift by force and must be heated off.[2G7Z9IIQoIs] Bulk solder for wave machines is supplied as bars, dipped into the molten wave.[2vJ0c0ioAXY]

## Flux

"Without flux, nothing works."[183] Metals oxidize too readily for a joint to wet without it, so flux is non-negotiable, whether it comes from the core of the wire or from a separate liquid or gel.[183] Multicore flux-cored wire — a five-core flux formulation, for instance — means no additional flux is needed for ordinary component soldering, surface mount included.[1306][186]

Two failure modes destroy the flux before it can act. Loading solder onto the tip and carrying it across to the joint burns the flux off in transit — visible as smoke as the wire touches the tip — and produces a cold or otherwise poor joint.[183] Running the iron too hot does the same thing, burning the flux away in smoke.[200] The correct sequence is to place the chisel point so it touches both the pad and the pin simultaneously, then feed solder to the far side of the joint.[183]

## Technique

The core rules are a temperature-controlled iron, the right solder diameter, flux, a tip that couples heat into both pad and lead at once, and application of solder to the opposite side of the joint from the iron.[183] A working temperature of around 350 °C is a reasonable standard for leaded work.[131] A joint that is slow to wet may need three or four seconds, and a small amount of solder fed toward the iron itself to establish thermal contact.[183] Well-wetted solder flows through a plated through-hole to the far side of the board on its own; where it does not, the joint may have wet only the side the iron was on.[183] A finished joint is a shiny fillet.[1205] Freshly soldered thermally massive components stay hot long after the iron is removed.[183]

Surface mount uses the tack-and-reflow method: tin one pad with a small lump of solder — not flattened out, or there will not be enough metal left to hold anything — bring the component in with tweezers, tack that one pin down, then complete the remaining joints.[186] Working systematically matters, since it is easy to lose track of which ends have been soldered; doing all right-hand ends then all left-hand ends, or all top then all bottom, makes the omissions findable.[1306]

A well or wicking tip is filled with solder so that it bulges just above the surface and then dragged along a row of fine-pitch pins. It deposits only the quantity each pad requires and wicks the excess back into the well.[180] Excess left behind on a single pad is enough to ruin the result on a BGA-style part, where the chip then sits neither flat nor flush.[186]

Throughput depends on the interaction of solder type, tip, and the thermal sink capacity of the pad and part.[1064] Two seconds per joint is an achievable target only if the iron has the reserve for it; small tips intended for fine surface mount work barely melt solder on a large ground plane even at 370 °C, and a low-end iron with no real thermal capacity may fail to heat a pad at all after thirty seconds of contact, even with molten solder applied to improve coupling.[1645][913][183]

## Rework and removal

An SMD chip can be removed with nothing more than an iron by covering all the pins on both sides with large blobs of ordinary solder, then alternating the iron between the two sides until everything is molten simultaneously, at which point the part lifts off with tweezers or falls off when the board is tilted. Large surrounding ground planes that sink the heat away make this fail.[688] Low-melting-point rework alloy is applied the same way — solder added to every pin, with essentially no downward pressure on the iron, since the alloy is brittle and pads and pins lift easily.[437] A desoldering station sucks molten solder out of the hole against gravity, which works readily on a joint at 300 °C.[542] Solder wick removes what remains.[230][180]

Old solder is not to be reused when the joint is suspect: it is sucked out entirely and replaced with fresh.[1301] Corroded joints are the hardest case; applying fresh solder to a corroded joint in order to desolder it can still be a miserable operation.[1527]

## Reflow and wave

A reflow profile ramps up, peaks, and cools about as fast as possible.[782] The thick band drawn across the profile is the acceptable temperature range for that specific solder, and every solder type has its own profile; individual parts have their own limits too, and component datasheets often carry recommended profiles.[782] Even with a controller that ramps deliberately rather than simply switching the elements on, a converted oven does not necessarily deliver an even temperature across the board — solder on one side can be fully reflowed while the other side has not yet started.[558]

In wave soldering, solder thieving pads are placed on the board deliberately; they exist because of the dynamics of the molten wave and how solder bleeds off the board as it passes through.[745]

## Solder as a conductor

Solder measurably reduces resistance where it is added, contradicting the claim that only a wire through a via will help. Filling a pad and via with solder while measuring live drops the voltage across it from 1.312 mV by a significant margin.[543] Tinning a bare copper strip produces a resistance decrease on the order of 50%; wicking the solder back off returns the strip to roughly its original 52 milliohms, confirming the change is the added metal and not a measurement artifact.[317]

The metal has mass, and enough of it accumulates over a large board that the solder and lead weight must be included in any centre-of-mass calculation.[1278] It is also just wire when needed — a length of solder serves as an improvised antenna for a spectrum analyser sniff test.[1085]

## Related board and process defects

Solder mask between the pins is a layout requirement for hand-soldering fine-pitch parts, and getting solder mask expansion right is part of that.[186] Gold flash pads cost only cents per board more and improve the result.[186] Where the silkscreen has been printed over a pad, no solder reaches the pin at all and the connection simply does not exist — a defect that can leave half the pins on a package unconnected.[1181] Old adhesive stick-on jumper links rely on the underlying solder mask to avoid shorting.[541] Conversely, the presence of proper solder rather than conductive adhesive or hot-bar bonding is a sign of a rigid, reliable interconnect.[1564]

Molten solder is a hazard in production: splashing is a real risk on a surface mount line.[100] Solder and residual flux left in a fuse from manufacture are visible on high-speed footage as the element blows, with solder running along the wire as it cools.[857]
