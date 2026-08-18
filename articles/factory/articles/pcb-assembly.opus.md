# pcb assembly

PCB assembly is the stage that turns a bare fabricated board into a populated one: applying solder paste, placing components, reflowing or wave soldering the joints, then cleaning and testing the result.[163][431][1755] It is a separate industry from bare-board fabrication — trade shows for the sector list assemblers and bare-board manufacturers as distinct categories of exhibitor.[Ns0i3PEfOag][1754][1686] The distinction matters in design because several things that look like board features are actually assembly-stage operations: solder-filled vias, for instance, are not produced at the PCB manufacturing stage but at assembly, by leaving the vias untented and letting a wave or a paste aperture fill them.[500]

Assembly is also a real line item in product cost, alongside the bare board, the enclosure, the display and the connectors — for a smartwatch-class product the bare board alone might run around $30–33 in thousand-off quantities, with assembly counted on top of that.[761] For a large board carrying big BGAs, fine-pitch parts and a great many passives, assembly is not cheap, and is costed roughly as a nominal amount per component placed.[1679]

## Pick and place versus hand assembly

Above a modest parts count, machine assembly is the only sensible route. A board carrying 161 distinct components is not something to hand-assemble; it is designed from the outset for pick-and-place.[1307] The economics of a self-owned pick-and-place machine are narrow: the machine only pays off for the right type of board, with the right number of parts, at the right volume. For a single board with something like thirty parts, hand assembly wins outright.[740] Even at fifty boards the setup dominates — days spent setting up and fiddling with a pick-and-place machine to make fifty boards, against roughly four days to assemble the same fifty by hand.[a4Xpsenpd6E]

Hand assembly at any quantity benefits from being organised like a production run rather than a one-off: tapes of components taped down to the bench so parts can be picked in sequence, rather than extracting single parts from individual distributor packets or off full reels, which is very time-inefficient.[562] A common bench habit for long hand-assembly sessions is to put a familiar movie on at the other end of the workshop, unwatched, purely as background.[a4Xpsenpd6E]

## Design for assembly

Assembly constraints propagate backwards into layout and part selection.

**Panelization.** Small boards must be presented to the assembler in panels, with break-off tabs or V-scoring so they can be separated afterwards. Handing a contract assembler a tiny individual board and asking them to "Assemble that board, please." invites an inflated quote, and they will probably hand-solder it anyway.[1158]

**Board size.** Very large boards are awkward to fabricate and awkward to assemble. Rather than one metre-long PCB, a plasma display's column drivers were split into three separate boards precisely because it is easier to get smaller boards bare-board manufactured and easier to get them assembled.[725] A 1.2 metre LED board is bigger than a standard panel and requires a manufacturer capable of both fabricating and assembling at that size.[1343] An 800–900 mm strip PCB for a mixing console is poor from an assembly point of view, favouring modular per-strip boards instead.[840] Panel-width limits at the bare-board manufacturer or the assembler can constrain board outline shape.[840]

**Board partitioning.** The counter-pressure is that integrating everything onto a single board is cheaper to assemble and test than splitting a design into a display board plus interconnect plus separate qualification of each module — a genuine trade-off decided early in a design.[430]

**Component sizes and feeder count.** Choosing smaller passives can cost money: boards can be more expensive to assemble because they use 0402s, and small sizes limit which manufacturers, especially local ones, can take the job. 0201 capacitors are half the size of an already-small 0402 and are rarely justified.[1307] Feeder capacity is a hard limit too — a typical pick-and-place machine might have on the order of fifty reel feeders, and running out of feeder slots for the number of distinct part types is one reason a board ends up with unusual component choices.[335] Reducing distinct part count is therefore a manufacturing concern, not just a BOM-tidiness one.[1307] Extra support components, even cheap ones, carry cost in assembly time, in bill-of-materials lines and in board area.[1074]

**Process-specific artwork.** Wave-soldered boards need solder thieving pads — larger pads on the trailing edge that capture excess solder as the wave passes, preventing solder dags bridging between pads.[431] Through-hole-style axial parts mounted end-on must be spaced so bodies and leads cannot touch and short.[634]

## Preparing parts for the assembler

Components are supplied to the assembler on reels, and reel quantities interact directly with line time. Buying a custom short reel of 250 parts when the run is a thousand boards means the machine must be stopped and the reel changed four times; stopping the line costs time and the assembler charges for it. If a thousand boards are planned, buying a thousand parts on one reel beats four small reels, even against the alternative of a full 3,000-piece manufacturer's reel.[239] Custom-counted reels are non-returnable, since they were made up specifically for the customer.[239]

Not every part must be in hand before assembly starts. Parts fitted later in the process — connectors, for example — can be absent without holding up the pick-and-place run, and can sit waiting while the boards are machine-assembled, because it is a separate process.[m9tza_c4sxc]

The solder paste stencil is normally left to the assembler, but a customer-supplied stainless steel stencil in a welded aluminium frame can be had from a local company for around $98 and shipped along with the boards; the assembler loads it into their automated paste machine.[m9tza_c4sxc]

## Paste, placement and reflow

Paste application is either stencil-printed — squeegeed through a stencil, which may be polyamide for prototype work — or dispensed pad-by-pad by a machine that works from reference points set on the board.[795][163] Fiducial marks are the normal references, though ordinary pads can serve.[163] Dispensing works on BGA pads as well as discretes.[163] Once pasted, components are placed and the board goes to the reflow oven.[163] For a small panel the whole hand cycle from starting placement to going into the oven can run a little over an hour.[Ux7WdK6oym4]

Wave soldering is the older alternative and produces visibly messier joints — molten solder passing right across the board — and it requires every surface-mount component to be individually glued down first.[431] The process is regarded as horrid and largely obsolete.[431]

## Cleaning and post-assembly handling

Cleaning is a genuine process step with real constraints. High-impedance and low-dielectric-absorption boards cannot simply go through the assembler's standard wash phase, because residue left behind can ruin the properties of a material such as Rogers; contamination on such a board can form a weak parasitic battery.[1755] Older precision instrument documentation specified elaborate sequences — "freon clean the PCB flow and touch up using rosin flux", followed by local flux removal and a thorough methanol clean.[1017]

## Test and inspection

Assembly is followed by test, and test capability is designed in. A dense board with gold test pads implies either a dedicated bed-of-nails fixture or a flying probe tester after the PCB assembly stage, used to power up, program and fully exercise the board.[334] X-ray inspection after assembly checks BGA balls for correct soldering, and an x-ray sticker on the board records that it was done.[864] Production testing is commonly contracted to the same assembler that populated the boards, rather than kept in-house — testing 1,800 boards personally does not scale even when each test is quick.[588]

Incoming inspection of bare boards matters too: an unnoticed track break and excessive pad clearance on a cheap prototype board went undetected because the boards were only glanced at rather than thoroughly inspected before assembly, a fault capable of wrecking a design.[155] Faults found later in the field may be attributable to the board, the soldering or the assembly rather than to a component as such.[1164]

## Assembly quality as an indicator

Assembly workmanship is one of the clearest readable signals of how a product was built. First-class assembly is characterised by quality components, superb soldering and excellent PCB material together.[144] Small mechanical details betray assembly-line thinking: an alignment post added purely to guide a daughterboard in so its pins are not crushed, on the reasoning that assembling a thousand units without it would crush the pins on some fraction of them.[1717] Conversely, retaining clips left unsoldered have caused field failures by popping off and shorting.[360]

Assembly location and sourcing are frequently mixed: a US-assembled instrument built from Taiwanese display components,[460] a Japanese ALPS keyboard module shipped complete to a US assembler,[645] or a US-made meter whose bare board, assembly and plastics are all domestic while a competitor's come from Taiwan.[1447] Board-to-board interconnects and multi-board construction are themselves assembly decisions, sometimes replaced by cable harnesses where a single larger board was not possible.[840][1246][1500]

## Data and documentation

Assembly consumes design data, and the fragmentation of that data is a long-standing problem: design, prototype fabrication, in-circuit test and assembly each historically use their own formats, some paper and some electronic, where a single two-way data path would serve everyone. The IPC-2581 effort explicitly segments information by who provides and who uses it across design, fabrication, assembly and test, validating against Gerber, ODB++ and NC drill outputs.[349] CAD output jobs group assembly outputs, fabrication outputs, Gerbers and design-rule reports into one systematic release process.[953] At the documentation end, a schematic finished with a full board overlay lets a single PDF serve both as schematic and as assembly drawing.[294] For kits and open hardware, PCB assembly instructions alongside basic soldering instruction are part of good documentation.[872]

## Turnkey and prototype routes

Assembly services attached to board houses close the loop for small projects: parts linked to supplier part numbers in an EDA library, marked as available through the house's own assembly service, offer a turnkey path from design to assembled board.[1306] At the fast-prototype extreme, an in-house printed-board process has produced a working board from idea to assembled hardware inside an hour — roughly 15–20 minutes of layout, 30 minutes to print and another 15 to assemble.[614] For an open-source project, the full sequence is ordering the parts, ordering the board, assembling it, then testing, debugging and getting the firmware working — a chain that routinely turns out less trivial than expected.[1306]
