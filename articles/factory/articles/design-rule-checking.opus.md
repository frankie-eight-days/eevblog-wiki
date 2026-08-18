# design rule checking

Design rule checking, universally abbreviated DRC, is the automated verification of a PCB layout against a set of geometric and electrical constraints — clearances, trace widths, hole sizes, pad-to-track spacing — before the board is committed to manufacture.[1327][990] It is the last gate between a finished layout and the Gerber files that go to the fabricator, and running it is the immediate prerequisite to generating those outputs.[1193][990] The same term is used at the semiconductor level, where the DRC stack encodes the patterning limitations of a given process node and has grown so complex that the tools to run it cost millions of dollars.[o2NxHu5Bsnk]

## Setting the constraints first

The constraints are not a post-routing afterthought. One of the first actions after importing footprints and the netlist, and before any track is placed, is to set up clearances, trace widths, track-to-via spacing and via hole sizes, and to base every one of those numbers on the capability of the fabricator actually building the board.[1327] This matters most with cheap prototyping services, where fine traces and clearances run up against a house minimum; a track that sits a smidgen inside the minimum pad-to-track distance is flagged by software, and software does not exercise judgment about how close is close enough.[1327]

Typical constraint categories include copper-to-copper and pad-to-pad clearance, minimum track width, same-net route length limits, and net-class-specific minimum trace widths, and a constraint set can be stored as a reusable configuration.[968][254] Larger organisations often carry standardised company footprints, approved spacings and DRC requirements forward for years, and a layout may be shaped as much by those inherited constraints as by the electrical need.[1512] Where checks concern safety spacings, transmission lines and current-carrying capacity of tracks, the constraint set expresses the whole design's manufacturing and electrical envelope in one place.[1032]

## What a check catches

A batch DRC on a routed board typically returns clearance violations — a track too close to a pad, two track ends too close together, a track near a via — alongside unconnected nets.[1193][974][245] Ten-thou clearance is a common threshold to fail against on a densely routed supply board.[245] Isolated fragments of copper left behind by editing show up as floating or unconnected copper, an error that is trivial to fix in the tool and expensive to miss: a board that reaches assembly with an unconnected copper pour needs a bodge wire to work at all.[Ep4r-wD7PPs][nkLQ-Co_cXI]

Checking is not limited to the copper layers. Footprint courtyard overlap catches two components physically colliding on the board — a mechanical DRC error rather than an electrical one.[1193] Silkscreen over pads and component spacing clearances belong to the more detailed check performed as a final professional pass, together with hole-size rationalisation, since consolidating a handful of odd drill sizes into the dominant one reduces tool changes and can make the board cheaper.[244] Solder mask expansion — whether mask actually exists between adjacent pins — can be captured by DRC rules as well.[990]

The check extends beyond the bare board when 3D models of the enclosure, connectors, ribbon cables and adjoining boards are imported. The software can then flag mechanical interference at the design stage, confirming that a capacitor will not foul an adjacent assembly when the board is inserted, which removes a whole class of re-spins.[1405][ag-MjKAfATw]

## Online versus batch

Most tools offer the check in two modes. Online DRC runs live while traces are placed, refusing to route through an obstacle and flagging a violation the moment it is created.[974] Disabling obstacle avoidance, or switching online checking off entirely, lets the router place anything — a trace straight through two pads and their holes — with the violation surfacing only when a batch check is run afterwards.[974][254] Online checking is commonly turned off on very complex boards because it slows the editor down badly.[974]

Some tools separate connectivity reporting from the rule check proper, listing unconnected nets as a distinct operation from DRC on the grounds that the two answer different questions.[Ep4r-wD7PPs] Batch mode also carries its own options: reporting all errors rather than only the first is essential, since the default of stopping at the first violation can make a board riddled with problems look nearly clean.[1193]

A practical workflow is to run the DRC with a report open on a second screen, work down the list of twenty or so items until the error count reaches zero, then verify the result in 3D, lock the board down and generate outputs.[Ep4r-wD7PPs][1193] Refilling copper zones immediately before the check is a trap: a changed clearance or tolerance in the zone settings can silently break a pour that was intact when it was last inspected, so refilling before DRC is not recommended without a specific reason.[1193]

## DRC versus ERC

DRC applies to PCBs; the schematic equivalent is the electrical rules check, or ERC.[1193][953] In a tool such as Altium Designer the two appear as separate validation outputs, with the design rules check offered only against a PCB document and the electrical rules check only against a schematic.[953] Schematic-level rules cover pin electrical types — power, input, output, passive — so that the checker can reason about what is legally connected to what.[255] A no-connect flag marks a pin deliberately left floating so the checker excludes it from analysis rather than reporting it as an error.[253] Hidden power and ground pins, invisible by default on many symbols, are a standard source of confusion when a schematic passes checking.[952]

Schematic checking is upstream of everything else: if snap grids are set wrongly, a wire can sit a fraction of a millimetre off a pin, make no electrical connection, and produce an incorrect netlist that propagates into the PCB, where design rule checking then operates on the wrong connectivity.[1129] A check performed between schematic and PCB confirms that the board matches the schematic it was drawn from.[240]

## Limits of a clean report

A zero-error DRC report is only as meaningful as the constraints behind it. Any board can be driven to zero errors by loosening or disabling rules, so a report showing no errors from a third party is worth little without sight of the constraint set that produced it — a board riddled with problems can still produce a clean report.[1193] This makes the constraints, rather than the report, the object of scrutiny.

A clean check is also not a substitute for looking at the board. The 3D view is treated as an inspection tool in its own right, valuable precisely because it shows what the physical board will look like rather than what the rules say about it.[1193][990][111] Independently, opening the generated Gerbers in a viewer catches errors that survived a clean check, because a Gerber viewer presents one layer at a time and the fresh, single-layer view exposes what weeks of staring at the CAD database concealed.[349]

The checker also cannot know intent. A layout that satisfies every rule may still be poor: an autorouted board meets the design rules, clearances and trace widths and joins every net, yet the result is generally unpleasant to look at and the router can back itself into a corner.[975] Conversely, some flagged conditions are acceptable — a minimum pad-to-track violation on a deliberately routed escape may be tolerated, and a repeated known error can be masked out of automated optical inspection since it appears identically on every board.[1353] Extra copper is sometimes placed purely for the checker's benefit, joining two pads that are already common on the parent board so that connectivity checking is satisfied and soldering is redundant.[1262]

Practice scales with stakes. A one-off personal board can skip fussing over silkscreen detail once the DRC passes and everything is connected, while a client or production board warrants the full pass.[990][Ep4r-wD7PPs] A simple assembly panel with little circuitry on it may not be worth checking at all, though doing so properly requires an associated schematic — individual board schematics plus a panel-level schematic.[552]

## At the fabricator

Design rule checking happens a second time at the manufacturer. On receipt of a design, the fabricator runs its own design rule checks before manufacture begins, and any questions arising from those checks must be answered by the customer before the board enters the process.[358] That review is budgeted into the engineering lead time deliberately, because an eight-layer board discovered to be wrong after fabrication is simply scrap.[358] Fabricators run the incoming data through dedicated CAM software rather than the customer's EDA package.[990]
