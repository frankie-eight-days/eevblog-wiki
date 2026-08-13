# soldering

Soldering is the process of joining electrical components by melting a fusible alloy between a component lead and a conductive pad, forming both a mechanical and an electrical connection. Contrary to widespread belief it is not a difficult skill, and it does not take years of practice to do well: with the right tools and a small number of basic techniques, good quality results are achievable from the first attempt.[180][183] The same fundamentals — heat transfer, the right amount of solder, and flux — apply unchanged whether the work is a printed circuit board, a connector, a solder cup, or a wire splice.[183]

## The core technique

A joint is made by heating the pad and the component lead together, not by carrying molten solder to them. The chisel tip is placed so that it touches both the circular pad and the pin at the same time, held for about a second, and only then is solder fed in from the opposite side of the joint.[183] The single most common beginner error is loading solder onto the tip and bringing it over to the work; this produces a cold or otherwise poor joint because the flux has already burned off in transit.[183] The rule is that the tip comes in one side and the solder goes in the other: "Tip comes in one side, solder goes in the other."[183] Solder may be applied to the tip as an aid to initial thermal transfer on a high-mass joint, but never as the primary method, because fresh flux must still be carried into the joint by the solder itself.[183]

Kit instructions that direct the builder to place solder against the joint first and then apply the iron have the order backwards; the iron goes on first, then the solder.[555]

Timing is diagnostic. Small components should be done in a couple of seconds — apply, feed, move on. If a small joint requires more than a few seconds, something is wrong with the solder, the technique, or the preparation of the surface.[183]

## Tips and heat transfer

Fine conical tips are a poor default because they lack the surface area to transfer heat into the component. The general-purpose tip for both through-hole and surface mount work is a chisel tip, typically around 2 to 2.5 mm, with finer chisels available down to about 0.8 or 1 mm; a fine point should be reserved for the occasions where a chisel physically will not fit.[180] The chisel must be laid flat against the pad. Tilting it reduces contact area so that essentially no heat enters the joint.[aQ2AVLs8_7k]

Tip geometry dominates temperature. A large chisel at 300 °C will heat a bulky component tab without difficulty, while a much smaller tip at 400 °C will fail to bring the same device up to temperature at all.[183] High-thermal-mass joints — a large metal tab against a pad, a transformer, a device bolted to a heatsink — pull heat away faster than a small tip can supply it, and the joint will visibly wet at one end while the other end cools instantly.[183]

A common working temperature is around 350 °C.[131][h9V0qJ4p3Aw] Excessive temperature is counterproductive: it burns the flux off before the joint is made.[183][200] Flux is central to the process, and it is difficult to use too much of it.[200][688] Delicate operations demand less heat still — wiping excess solder off a fine-pitch footprint is done below 300 °C to avoid damaging the pads.[405]

## Solder diameter and consumables

The single largest lever on joint quality is solder diameter: the finest solder practical for the job gives the most control over how much alloy ends up on the pad.[200] Surface-mount work is commonly done with 0.35 to 0.38 mm wire, which allows far finer feed control than 0.8 mm and above.[KzC12xtHuXo][1400][1306] Carrying only one gauge is a limitation — a single 1 mm reel is unhelpfully coarse when solder must be fed sideways into a partly inaccessible pin.[1195] Flux-cored solder alone is normally sufficient, with separate liquid flux or a flux pen reserved for stubborn, oxidised, or old joints.[183][510][688]

Solder sleeves — short heat-shrink sleeves with a ring of solder moulded into the middle — join, solder, and insulate wires in one operation when heated, and are available in a range of sizes for wire-to-wire work.[780]

## Surface mount and rework

Surface mount hand soldering requires only basic tools and very little experience, and is done in seconds per joint.[186] Hand skills remain necessary even for those who stencil and reflow their own boards, because parts eventually need rework, and rework technique — particularly part removal — differs from initial assembly.[186]

The standard sequence for a fine-pitch package is to flux the pads, place the part, tack a single corner pin to fix its position, and then solder the remainder.[510][KzC12xtHuXo] The remaining pins can be drag soldered, with the solder mask between pads confining the alloy; once the technique is right, a single drag across should suffice.[510][997][1522] Excess is removed with wick or a well-type tip.[997] A useful preparatory step on a connector footprint with damaged or contaminated pads is to add fresh solder deliberately and then wick it all off, which cleans the pads for reuse.[1281][884]

Removal is a separate discipline. Low-melting-point alloy applied around all sides of a chip keeps the whole footprint molten simultaneously so the part lifts off in one piece; nearby passives must be protected from being dragged off or disturbed.[437] Flux is the recommended companion to this method, though the technique frequently works without it.[688] Very small parts, down to 0201, are removable under adequate magnification.[1125] Fine pitch is the practical limit on hand work — a 3 by 3 mm package with 0.4 mm pin pitch is genuinely difficult.[193]

## Through-hole and mechanical assembly

Multi-pin through-hole parts should be mechanically constrained before heat is applied. Inserting the mating header or connector onto the pins first holds the alignment while soldering; without it, the plastic body can soften and the pins shift out of position.[974] Thin, long pins have play and wobble, which makes alignment on the board a problem in the first place.[974]

Access often dictates the approach. When a wire is fed through a cleared hole, it is soldered from the underside rather than the top.[1364] A discrete LED can be soldered on one leg only, then reheated while pressure is applied to the body, allowing each part to be individually centred before the remaining legs are committed.[353] A 1.6 mm PCB soldered on both sides of a straight pin header gives a rigid right-angle mount for a display without needing a right-angle header part at all.[644]

Not every mechanical connection should be soldered. Press-fit holes are specified with tighter tolerance precisely so that studs or component leads can be retained without solder.[1259] Test leads should be crimped as the primary connection, with solder used only as a backup — and a lead that shows essentially no wetting at the joint is defective regardless.[87E3wqfxHqg]

Some materials cannot be soldered at all: attempting to solder a membrane switch tail simply melts it, and adhesive or conductive alternatives are required.[1702] Enamelled magnet wire must have its insulation removed first, which can be done crudely by burning it off with the iron and solder until the end takes.[539]

## Defects and failure modes

**Solder balls and splashes.** Solder can spit during work, throwing balls and splashes that go unnoticed at the time. These remain loose inside the product, move around, and can short between pins later. Any board that has been hacked or reworked should be visually inspected for them before reassembly.[1418] Loose solder dags can bridge microcontroller pins in exactly this way.[1036]

**Dry and starved joints.** Joints carrying roughly half the solder they should, and connector shields left entirely unsoldered, are a classic mark of poor assembly and produce intermittent behaviour.[12] A component may be held on by little more than a sliver of alloy.[1191]

**Cracked joints.** Solder joints crack, characteristically on high-mass components such as power devices, transformers, and large connectors; the repair is to remove the old solder entirely and reflow with fresh alloy.[884][1243] Preventive resoldering of the major power components, the transformers, and heatsink-mounted switching devices is a reasonable first step on an intermittently faulty instrument.[1452]

**Lifted pads and traces.** Pads lift when heat and mechanical force are combined. Excess solder should be wiped along the length of a pad rather than across it, since a transverse wipe puts pressure on the pad and pulls it up.[405] Pads over a solid ground plane are better anchored; pads that are not can lift after only a second of iron contact.[1639] Poor laminate bonding makes this worse, and pads on some boards come away very easily.[1522] Years of flexing can peel copper away before any iron touches the board.[1281]

**Hairline opens.** A pin can sit a fraction of a millimetre proud of its pad, so that the signal is present when probing the pad but absent at the top of the pin. This kind of fault is only found by inspecting at a steep angle under magnification.[689]

**Reflow damage.** Component datasheets specify a recommended thermal profile with distinct phases, and exceeding it voids the guarantee — a connector family such as the Hirose DF13 is rated for a maximum of 230 °C for 60 seconds, beyond which behaviour is not guaranteed and connector bodies melt.[782] Melted connectors can sometimes be salvaged by desoldering and reinstalling the individual pins.[782] Getting the profile wrong at assembly causes tombstoned parts and joints that never properly solder, and thick boards compound the problem because they heat and hold heat differently.[104]

## Bench setup

Precision comes from stability. Hands should rest low on the bench so the wrist stays down and the hand acts as a pivot; soldering freehand up in the air introduces tremor and makes fine solder feed and iron placement imprecise.[680] The board itself must not move — a weighted holder prevents a small board being shuffled around by an incidental tug from the iron, particularly on a surface without good grip.[680] Long-armed articulated clamps wobble and are better suited to probing than to soldering.[787]

**Magnification.** Working distance is the governing specification. A stereo inspection microscope offering roughly 80 mm of working distance at 4x and about 50 mm at 10x allows an iron to be brought in at 45 to 60 degrees, and 4x is preferable for general work.[390] Conventional stereo microscopes force a hunched posture with a narrow head position, causing fatigue quickly over long sessions, whereas a head-up design permits ten or twelve hours of continuous work with minimal fatigue beyond the physical.[390] Magnification can also be excessive: a 25 mm field of view with 10x eyepieces is too restrictive for general soldering, with 10x better suited to fine repair and lower-power eyepieces preferred for routine work.[1209]

Video microscopes are viable provided latency is low enough that the iron can be driven while watching the monitor rather than the board; 60 frames per second gives negligible lag, and even 30 frames per second is workable, with 0.6 mm pitch parts soldered entirely by screen.[1125][590]

**Fume extraction.** Extractor effectiveness falls off sharply with distance. A good unit will capture smoke at roughly 100 mm at its lowest fan setting when positioned close to bench level, but a weaker one must be within about 10 cm to catch most of it.[yi5pb_l8U94][4oHUuXgK_i4] Noise sets the practical operating point: a mid setting is acceptable for a session of half an hour to an hour, while maximum is generally unusable.[1338]

**Portable irons.** USB power-delivery irons are for field and spot work, running from a power bank, and are not recommended as an everyday substitute for a proper temperature-controlled bench station.[1319][h9V0qJ4p3Aw]

## Repair and modification practice

Where a modification point is physically inaccessible — a lead under a light pipe, for instance — the track is traced to an electrically equivalent point that can be reached, such as a pin on a nearby small-outline package or the top of a series resistor.[182] Mod wires are soldered to pads prepared with fresh solder, and any modified part should be mechanically secured, for example glued down, so that stress is taken off the wires rather than the joints.[978]

Soldering is also a measurement technique: short pins tacked onto a board create insertion points for an ammeter in series with a supply rail.[330] Two pogo pins soldered side by side widen an effective test contact so that a small target is not missed.[216]

Before rework, cleaning the area with isopropyl and a brush removes crud and old flux so the retouched joints can be assessed properly.[h9V0qJ4p3Aw] Flux residue is cleaned off afterwards with a cleaner and an antistatic conductive brush.[183] Leaded solder is preferred when reworking lead-free joints.[1756]

Some construction choices make repair substantially harder: a shield plate soldered down across a front end must be desoldered in full to reach anything beneath it, at real risk to the circuitry.[1477] Shielding cans with a single solder point are far more tractable.[879]

## Solder quality as a design and process signal

The appearance of the solder work on a board is a direct readout of the assembly process behind it. First-class soldering with no residue indicates a properly controlled line.[171][200][417][470][91][56] Conversely, sloppy joints, heavy flux residue, hand-bodged components, and parts held by minimal alloy indicate assembly done cheaply.[440][633][211][12][295]

Component choice interacts with solderability. Sticking to larger small-outline packages and passives rather than 0402 parts or BGAs keeps parts cheap, available, easy to hand solder, easy to repair, and yields better in production.[171] At the other extreme, a board combining thousand-pin BGAs with dense connectors and sockets places the entire yield on getting the reflow process exactly right, since one bad joint condemns the whole assembly.[860]

Good mechanical design removes solder operations altogether. Engineering the underside of a heatsink to press down on shielding cans holds them in place by geometry alone and eliminates a hand-solder step from manufacture.[1717] Design decisions can also work against the builder: white solder mask on the underside of a through-hole kit board makes traces, pads, and joints very hard to see while soldering, and large pads deliberately provided beside a pin give a beginner somewhere to place the iron.[1483][aQ2AVLs8_7k]

Loose components that ought to be soldered are a defect in their own right. A watch crystal left unsecured when pads are provided for it, or retaining clips left unsoldered so that they pop off in service and short something out, are both avoidable.[1101][360]

## Learning to solder

Through-hole kits are the standard vehicle for acquiring the skill, and the better ones include resistor colour codes, component identification, and step-by-step soldering guidance alongside the parts.[1080][353] A kit that omits soldering instructions entirely is a missed opportunity when its target audience is beginners.[1483] The skill transfers quickly: a group of around fifty to sixty attendees, most of them software developers with no prior hardware experience, were taught to solder and completed working assembled boards in roughly an hour and a half.[203]

Even for an experienced practitioner, it always takes a few joints to get back up to speed after a break.[1205] Being able to construct and solder a circuit decently, alongside designing it, laying out a board, and debugging it, has long been part of the working definition of an electronics hobbyist.[9iXFhKUa1BU]

Age readiness is individual rather than fixed. Dave Jones held off teaching his elder son at six on the grounds that he was still wary of the heat, treating soldering as a means to an end rather than something to be pushed; the same child later completed a Z80 single-board computer kit without a single soldering error.[1069][1205]

## Summary of practice

The consolidated rules are: use a good quality temperature-controlled iron; use a solder diameter fine enough to control the quantity deposited; use a chisel tip large enough to transfer heat to both pad and pin simultaneously; heat the joint, not the solder; feed solder to the side of the joint opposite the tip; and keep the temperature low enough that the flux survives to do its job.[183][180][200] "Flux is everything."[200]
