# pcb manufacturing

PCB manufacturing is the set of industrial processes that turn a set of design output files into bare fibreglass-and-copper boards: imaging, etching, lamination, drilling, plating, solder mask, silkscreen, surface finish, routing or scoring, and electrical test.[939][407] Boards are normally fabricated many-up on a panel — a single panel might carry ten individual PCBs — and separated afterwards.[939] Bare board fabrication is a distinct trade from assembly: a fabricator makes the empty board, and an assembly house populates it, and the two are frequently different companies in different countries.[533][1701][1447]

The economics of the industry have collapsed the cost of prototypes to the point that home fabrication has little purpose. Prototype boards from low-cost services arrive for a few dollars delivered, and Chinese fabricators can turn a board around in about seven days for under a hundred dollars.[1374][1759][939] Home-made boards give up plated through holes, solder mask, silkscreen overlay, gold-flash pads, V-scoring and routing — everything a professional board is taken for granted to have — so the only remaining reason to etch at home is needing a board within the hour.[939][1197] Even hobbyists therefore generate Gerbers and send them out; a CAD package that cannot export Gerbers is unusable for that reason alone.[255]

## The design output package

What is sent to the fabricator is a zip of Gerber files plus NC drill files, and in practice it is simplest to include everything the CAD tool generates and let the fabricator ignore what it does not need.[990] Additional non-copper information rides along in the same package: the mechanical layer carrying the board outline, the V-groove lines and the routing paths, so that the fabricator knows the finished board size and how the panel is to be scored and milled.[239] Slot features must be accounted for in the drill data as well.[990]

The Gerber format's role as the transfer medium is itself a source of loss. IPC-2581 was promoted as an open, industry-owned alternative intended to carry design, fabrication and assembly data accurately in one file, removing the assumptions and misinterpretation that arise when, for example, an aperture list goes missing, and lowering cost as a result.[349] Export bugs in CAD tools are a practical hazard in their own right — polygon segment-count settings affect fidelity, and at least one package failed to export circles on planes.[Ep4r-wD7PPs]

Automated panelization features are of limited use if they stop short of the fabrication requirements: a panel generated without fiducials in the corners and without tooling holes will cause trouble at the manufacturer, and knowing that this material has to be present is part of laying the board out.[255]

## Design rules and tolerances

The manufacturer's capability sets the minimum feature sizes a design may use. Minimum trace width is typically of the order of 4 to 6 thou, or 0.1 mm, and traces cannot go below that because the fabricator cannot guarantee that its etching process will not over-etch the copper and break them; boards are electrically tested, but fabricators will not test so aggressively that they scrap panels, since that cost either falls on them or is passed on.[1559] Package choice drives these rules directly: a board of large through-hole parts can be routed comfortably at 20 thou track and 20 thou space, while a single 0.4 mm pitch BGA forces the whole board down to at least 4 thou rules and, if vias must escape to inner or bottom layers, to very small drill sizes.[193]

Rounding is a real trap. A design set to exactly the advertised minimum — 3.5 thou, say — can be rejected because of rounding differences between imperial and metric units and the resolution chosen when generating the Gerbers, and how strictly the limit is enforced varies by manufacturer.[1327] On a cheap shared-panel service the check is automated: if a feature comes out fractionally under the stated limit, the board is rejected without discussion, because the customer is one of a hundred sharing that panel and there is no margin to negotiate.[1353] Higher prices buy tolerance; a five-dollar board does not.[1327][1353]

Not every parameter is specified. Fabricators often state a minimum copper-to-copper spacing but no minimum solder mask sliver width, from which an acceptable value can sometimes be inferred; some houses will simply attempt whatever is submitted, and if the mask does not work, that is the customer's problem.[1353] Copper weight behaves the same way: 1 oz is the standard outer-layer thickness, inner layers of a multilayer board are often half or quarter ounce, and if the designer does not specify it the result is pot luck — never more than 1 oz, because copper is expensive.[1559]

Plating thickness is similarly loose. A typical via barrel is about 1 thou — roughly 0.025 mm — of plating, but this varies substantially with the manufacturer and process, which is why via current capacity is treated as a rule of thumb rather than a specification.[543]

## Stack-up and layer construction

A four-layer board is not built as four equal layers. Fabricators buy prepreg and core material from specialist suppliers, laminate two very thin double-sided boards, and glue them to a core; in a 1.6 mm finished board that core is typically about 40 thou, or 1 mm, thick.[1117] The consequence is a large separation between the internal copper layers, which makes the power-plane capacitance of a cheap stock four-layer stack-up poor — and on a low-cost order there is no choice in the matter.[1117]

Blind and buried vias exist because of that construction sequence. An inner pair is fabricated as its own thin double-sided board with its blind vias, on thin prepreg FR4 or Rogers material, and the sub-boards are then stacked and pressed.[1259] Vias therefore cannot be placed between arbitrary layer pairs; there must be a manufacturing route to produce them, and requests outside the normal sequence are either refused or priced heavily.[1259] This level of construction is only warranted by genuinely dense designs such as mobile phones, which do not use holes running all the way through.[1259]

## Special processes and their cost

Anything beyond the standard flow is an additional step and an additional charge. Side contacts on a board edge are an extra bare-board process that normally costs more, though at volumes around a hundred thousand units the premium may not matter.[514] Gold edge plating on a small region of a board is quoted as a separate process for extra money.[1336] Rigid-flex — a rigid PCB with an integrated flex section — is more expensive to fabricate, but can be cheaper overall in volume by eliminating a connector, and may be the only option when there is no internal volume for one.[1210]

Castellated edges are the cheap exception. They require nothing special from the fabricator: a normal plated through hole is placed half on the board outline and the routing path is specified through it, so the mill cuts through the existing barrel — at the cost of small burrs.[1649]

Copper thieving, the small isolated copper pads scattered across otherwise empty areas, exists for the plating bath: balancing the copper area across the board gives a more even electroplated and immersion-finish coverage.[1639]

Silkscreen is a design surface rather than just a label layer, and boards are cheap enough that using one as a product front panel is practical, with a choice of solder mask colours and high enough silkscreen resolution to print button legends.[644] The corresponding hazard is fabricator-added markings — order numbers and similar identifiers sprayed onto the board — which ruin a front panel; some suppliers offer an option to suppress them and others do not, making the outcome a matter of luck.[555]

## Board size and panel limits

Panel size is a hard constraint that catches large designs. A board over a metre long is beyond what many fabricators can panelize at all, and it then also has to find an assembler capable of handling it.[533] For pick-and-place, length is usually the least of the problems — machines can take long boards in one pass or in halves — while height and width inside the machine are the real limits.[533][465] Where a single board of the required length is impractical, the design is split for manufacturing reasons and the sections joined electrically, as with LCD driver strips feeding a T-con board.[eCKRl_Txa18] A large fully routed board with no breakout tabs or V-grooving implies a custom assembly jig rather than a conventional panel.[465]

Board size also drives price at the prototype end, which is why dirt-cheap quotes do not survive contact with a physically large design.[990]

## Checking before release

The amount of checking is scaled to the consequences. A simple four-layer board that passes DRC, with sound ground planes and only electrical function at stake, does not warrant fussing over details.[1193] A dense eight- or ten-layer board carrying thousand-pin BGAs represents weeks or months of layout, is expensive to fabricate and expensive to assemble, and attracts a formal design review — with a day or two spent double- and triple-checking before release.[1193] The 3D view is useful at this stage not for the component models but for inspecting features such as solder mask expansion and whether mask exists between all pins.[990] Locking placed components guards against the critical part being nudged during layout, which will otherwise surface at manufacture.[974]

Solder mask expansion is one of the checks that matters most on cheap services. Copper and solder mask layers are never perfectly registered, and low-cost fabrication takes less care over that alignment; without expansion, mask creeps onto the pad, paste is then printed partly onto mask, and solder balls result.[1353]

Errors that survive review can sometimes be worked around rather than respun: a narrow-body footprint used for a part that only exists in a wide-body package can be salvaged by bending the leads back under the chip into a J-lead arrangement and soldering them down.[990]

## Working with the fabricator

Gerbers are to be manufactured exactly as submitted. A fabricator that silently edits the design data — expanding pads and cutting back ground fill — is doing something no professional manufacturer does, and the practice destroyed a deliberate current path when an eighth-thou trace between pads was reduced to an open circuit; such changes also create subtle grounding problems when current no longer flows where the designer intended.[500][155]

Published open-source hardware is only as manufacturable as the data released with it. A project distributed without Gerbers and with a source file lacking solder mask between pins cannot simply be imported and sent out; regenerating usable outputs takes real work.[1374]

Assembly-adjacent inspection completes the line: automated optical inspection sits at the end of a production line, checking placement or solder paste, and is distinct from the pick-and-place equipment itself.[1686]

## Fabrication as a business decision

Board fabrication has consistently moved out of product companies and into specialists. One instrument manufacturer exited board manufacturing at the transition to surface mount, judging that keeping up with evolving equipment and doing it to quality standards — with RoHS arriving as well — was not worth the investment when the service could be bought, while retaining final product assembly in house.[1032] Domestic bare-board capacity can be extremely thin as a result: Australia has only about two bare-board fabricators, one high-end military supplier and one lower-end house.[1701]

At the product level, fabrication cost is a large share of total cost, particularly for multilayer, high-density boards — which is why adding a process step such as printing carbon resistors directly onto the board is not done today, given that placing a physical resistor with a modern pick-and-place machine is cheaper.[335] Design-for-manufacture decisions of this kind are old: the 1960s and 70s practice of sandwiching components between two circuit boards to save space became less useful as component sizes shrank and integration advanced.[612]
