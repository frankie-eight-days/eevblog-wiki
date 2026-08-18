# pin pitch

Pin pitch is the centre-to-centre spacing between adjacent leads on a component, and it is the single number that determines whether a part can be soldered by hand, probed on the bench, routed on an ordinary PCB, or substituted with something else from the shelf.[186][127][408] It sets the difficulty of nearly every physical operation an engineer performs on a chip, and it is quoted in the package drawing of a datasheet as a dimension in millimetres — the letter E in a typical mechanical drawing.[1074] Because pitch and package outline vary independently, two parts with the same die and the same function can differ entirely in pitch, and choosing between them is a real design decision rather than a formality.[1074]

## The through-hole standard and its limits

The reference point for through-hole parts is 0.1 inch, and departures from it are always described relative to that baseline.[186][592][1111] Once a package outgrows the density that 0.1 inch allows, designers either go finer or resort to geometry: older DIP variants used a staggered arrangement, with pins offset in two ranks so that a pitch finer than 0.1 inch could still be given large solder pads on the board.[256] The same trick reappears in miniature form in probe-card style assemblies, where a single row of contacts on a die is too closely spaced to drill individual holes for, so the contacts are split into two vertical levels to open the pitch back up to something mechanically workable.[532]

Early microcontrollers already broke the standard: a mask-programmable, one-time-programmable device from 1970 carries a visibly finer pitch than 0.1 inch when set beside a modern PIC.[1111] The same pressure applies to hobbyist-scale boards. Shrinking an Arduino-format design far enough forces the pin pitch off 0.1 inch, and past a certain size the standard spacing simply cannot be used at all.[592]

Non-standard pitch on a programming or debug header is a recurring nuisance rather than a technical necessity. The in-circuit serial programming header on a PICkit 3 is not 0.1 inch, which makes it incompatible with a target board expecting standard spacing — while inexpensive clones sold through eBay are reported to use the correct pitch.[841]

## Surface mount: what is solderable by hand

For surface-mount packages the practical hierarchy is well established. An eight-pin SO package at 0.05 inch — 1.27 mm — is half the pitch of a DIP and is still considered large; each pin can be soldered individually with an ordinary iron and fine solder, even by someone who has never done SMD work.[186][353] At 1.27 mm the difficulty is low enough that a prototyping aid designed around that pitch does not really demonstrate its own value.[408] A 1 mm LQFP is likewise trivial by hand.[1074]

Below that, individual-pin soldering falls away. At 0.65 mm, soldering each pin separately becomes hard enough that a microscope is effectively required for a good result, and drag soldering with a wicking tip or a chisel tip becomes the sensible method instead.[186] At 0.5 mm the part is about as small as parts get in normal work; drag soldering still works, aided by solder mask remaining between the pads.[186] A 3 mm by 3 mm MLF/QFN at 0.5 mm pitch is genuinely difficult and worth avoiding unless the required function is only available in that package.[346] An 0.8 mm pitch is comfortably large enough for dead-bug prototyping, where bond-out wires are soldered directly to the leads under magnification.[181][1074]

At 0.4 mm the process reaches its practical floor — "0.4 mm is about um as small as it gets in the industry in terms of pin pitch" — and hand-soldering an 88-lead QFN at that spacing on an ordinary board is a serious challenge — assuming solder mask can still be held between the individual pads at all.[408] Even a 0.4 mm QFN socket, supplied because that is the only package the part comes in, is regarded as fine for a mobile phone and awkward for anything else.[833] Stated as a rule: 0.5 mm is small, and "0.4 is starting to get, you know, really pain in the ass category."[1074] Pitches finer still exist — a 0.35 mm part appears in consumer audio electronics — and are described as simply annoying to work with.[1322]

## Design for manufacture

The manufacturing guidance follows the same thresholds. For designs headed to volume assembly, staying at 0.5 mm pitch or larger on SO packages and quad flat packs, alongside 0603 and larger passives, keeps yields and inspection straightforward; BGA and finer pitch bring more critical pad dimensions, harder inspection, and lower yield.[127]

Pitch also constrains routing. On a densely populated BGA, a wide enough ball spacing allows a via to be placed outside the footprint with a trace running to it; when the pitch is too small, that escape route disappears and via-in-pad or similar techniques become necessary.[1259] On flex PCBs the constraint is mechanical as well: castellations at 0.5 mm pin pitch on a flex are of doubtful manufacturability, which pushes the design toward small vias in the flex through which solder is flowed down onto the pads beneath.[1262]

Fine pitch magnifies footprint errors. A 0.6 mm pitch device on a board with a slightly incorrect footprint shows the first pin centred correctly while the error accumulates progressively along the row; on a package with a high pin count the accumulated offset becomes a real fault rather than a cosmetic one.[689]

## Working on assembled boards

Fine pitch makes fault-finding physically hazardous. Probing individual pins on a fine-pitch package risks shorting adjacent pins and destroying parts that were not already faulty, which is one argument for measuring at the external components — the capacitors and other passives around the chip — rather than at the leads themselves.[1322] Skipping voltage measurements at the pins because they are hard to reach lengthens diagnosis considerably.[1322] Fine-pitch probing at 0.5 mm is feasible on two adjacent pins with a handsfree probing fixture, avoiding the usual alternative of soldering wires on or finding a larger access point elsewhere in the circuit.[GS0WqUKZ-3c] Under magnification of around ten times, fine-pitch work becomes practical.[1322]

Rework carries the same penalty: removing a fine-pitch package that also has a thermal pad underneath is a job worth avoiding if the fault can be located elsewhere.[1322] Small pitch on a connector also invites misalignment — plugging a fine-pitch programming lead in one pin off is an easy mistake.[JI4b-7vpIDc]

## Connectors, displays and flex

Pitch governs connectors and display interfaces as much as ICs. A 1 mm pitch dual-row board connector rebuilt pin by pin after its plastic body was cut away is difficult precisely because every pin must be aligned before any of them will seat.[794] Display flex tails commonly run at 0.5 mm pitch.[1699][1703] Where a driver chip is bonded directly onto a flat flex, the pitch of the chip's connections and that of the flex tail differ markedly.[781] Hot-bar attachment of a dense flex array, as in an ultrasound transducer with on the order of 128 elements, involves pitches finer still.[1315] A fine pitch on a display's connection tail can be reflowed with hot air or an iron once the pads are tinned or pasted, though the pitch itself remains the objectionable part of the design.[1241]

Mechanical fit at a given pitch is sometimes a matter of luck: a 0.5 mm display flex that will not enter a connector in one orientation may fit perfectly in the other.[1699]

## Sourcing and substitution

Pitch is a specification that must be pinned down at order time, not assumed. Ordering a part by its base family number without specifying the exact configuration can yield a device with entirely the wrong pin pitch, which is a bill-of-materials failure with no recovery — particularly where the datasheet does not supply an unambiguous ordering part number.[1074]

The same applies to replacement passives. A radial electrolytic in a plasma TV supply at a standard 5 mm pin pitch is available in other pitches as well, and buying the wrong one wastes the repair; leads can be bent to fit, but matching the pitch is far preferable.[763] In a mains filter application the choice narrows further, since a stocked part with the correct pitch may be the wrong safety class — not properly self-healing and lacking the required ratings and markings — while the correctly rated X-class part may only be available in a different pitch and body size.[1481]

For programming and test fixtures, pitch is baked into the hardware. A universal programmer's adapter accepts any PLCC of one particular pitch; a different pitch, a different pin count, or a different package style requires buying a whole additional adapter.[1060]

## Pitch as an indicator

Because pitch scales with the density a manufacturer is willing to pay for, it serves as a quick read on a design's ambition. A 0.5 mm pitch FPGA in a signal generator is visually intimidating, though in that instance most of the pins are unconnected or tied together, so the effective interconnect density is far lower than the package suggests.[805] The same holds in reverse for compact instrument boards, where a tiny pin pitch on a custom shield signals that the designer accepted assembly difficulty in exchange for area.[1410]
