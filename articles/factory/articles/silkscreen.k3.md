# silkscreen

Silkscreen, also called the component overlay or legend overlay, is the printed layer of text and graphics on a printed circuit board that carries component designators, values, polarity marks, logos, and assembly or service information. The term survives from the era when the markings were literally applied through a silk screen; modern boards use other processes, but the name persists: "It's not the process, but it's still called silkscreen."[zHpsA1RtQhw][990][1471] Its practical value is large relative to its cost: it makes boards buildable without a schematic, probe-able without a service manual, and cheaper to assemble correctly.[555][1394][1185]

## Fabrication processes

Two application processes dominate. Photoimageable overlay is a photo-lithographic process applied and exposed like solder mask, and it produces the sharpest result.[817][939] The cheaper alternative is dot-matrix (inkjet-style) printing, in which individual dots and line artefacts are visible under magnification; low-cost prototype services predominantly use it.[817][558][997][475] The difference between the two is plainly visible side by side, and photoimageable output is preferred when the silkscreen must look professional, for example on a board used as a front panel.[241][817]

A board received with blurred or smeared silkscreen is a manufacturing defect that a fabricator would ordinarily replace.[562] Silkscreen alignment and registration can be checked under a microscope along with the other layers.[Ep4r-wD7PPs]

## Colours and artwork

White is the default legend colour, but manufacturers typically offer a selection — half a dozen colours or more — and multi-colour legends are applied as multiple passes, one process per extra colour.[zHpsA1RtQhw][1471] Some low-cost services restrict the choice to white or black, and at least one fabricator sensibly refuses a black legend on matte black solder mask.[1259] Matte black solder mask with white silkscreen gives notably better contrast than gloss black.[555][460]

Arbitrary artwork on the silkscreen layer costs nothing extra, because the pattern makes no difference to the mask process; elaborate graphics, logos, and decorative imagery are effectively free as long as no additional production step is introduced.[1229][1254][266] Additional apparent "colours" can be produced by combining solder mask, silkscreen, and exposed copper or plating in the artwork.[zHpsA1RtQhw][1254]

## Layout practice

Silkscreen designators should be placed outside component outlines rather than under parts, so they remain readable after assembly — particularly important on single-sided kits.[244] Where density makes adjacent placement impossible, the accepted technique is to place the designator in open space with a silkscreen line pointing to the part.[720] Placing designators and markings on the bottom side of a board is a recognised serviceability measure: it lets every component be identified and measured from the accessible face when a board mounts component-side-down.[208][452][628][1322][8blgmbXfDEc]

Silkscreen over pads is a genuine defect, not a cosmetic one: a pad covered by legend ink cannot be wetted by solder, leaving the pin unconnected, and this has been observed as the actual fault in failed products.[1181] The standard final checks before release therefore include inspecting the board in the CAD 3D view — which renders the silkscreen exactly as it will appear — specifically to catch legend over pads or vias, supplemented by design-rule checks.[244][111][1193][990] On one-off or hobby boards, silk-to-silk clearance and minor overlaps are routinely waived as not worth the effort.[974][245]

Other established layout conventions:

- Silkscreen that extends past the board edge is simply chopped off by the fabricator; keeping a true-size outline of a heatsink or similar part on the overlay aids mechanical fit checking, though a mechanical layer is the more professional place for it.[244]
- The silkscreen component outline can serve as the component's size definition for spacing checks.[244]
- Fiducials must not be placed on the silkscreen layer, because the legend can be offset relative to the copper layers; fiducials belong in copper.[1512]
- Polarised and keyed parts depend on the legend: transistor flats are drawn on the silkscreen so the package can be oriented correctly, and a wrong silkscreen flat will cause backwards insertion — though a wrong footprint is worse.[aQ2AVLs8_7k][555]
- Pin-1 identifiers should be marked on connectors and board interconnects.[661]
- Component values printed directly on the legend let a kit be assembled with no reference to the schematic.[555]
- Decimal points are easily lost in small printed legends, so the convention of replacing the point with the unit letter — 6R2 for 6.2 Ω — is used.[1617]
- Regulatory markings such as the UL stamp should be added to the silkscreen by the designer rather than requested through a fabricator's checkout option.[1259]
- Fabricators that add their own batch codes or file numbers to the legend are a persistent annoyance, especially when the board serves as a front panel; some fabs provide a checkout option to suppress the markings after customers complain.[241][997][155][1471]
- Putting the designer's name or initials on the silkscreen is recommended practice even when an employer does not require it — there is always room somewhere on the board.[1313]

## The legend as documentation

A well-used silkscreen substitutes for documentation at the bench. Marked test points with labelled rail voltages allow a board to be diagnosed without a service manual or schematic.[1185][1394] Full pinouts printed beside connectors serve the same purpose, and their absence on boards that clearly had room for them is a recurring criticism.[1394][1420][1069] On vintage equipment, legends identifying functional blocks, chip identities, and high-voltage hazards ("danger 1,200 V") were standard practice and greatly ease repair.[788][863][261][628]

The legend also carries manufacturing intent. Assembly instructions such as cable colours have been printed directly on the board for production operators.[925] A large arrow indicating board travel direction through wave soldering is a recognised designer's marking, since component orientation relative to the wave affects solder quality.[431] Silkscreen lines marking the primary–secondary barrier and creepage paths on mains equipment delineate the safety isolation boundary.[388] When a board is known at design time to need wire links, printing the link path on the legend shows the intent even if production deviates from it.[1216]

Silkscreen also functions as evidence. The legend recording a designer's intent — for example a footprint marked for an RF bead later found stuffed with a zero-ohm resistor — reveals design history during troubleshooting.[987] Conversely, pin-function markings on the legend can expose that a published schematic does not match the shipped PCB revision.[XUyjRm1Upjs]

## Cost and ordering considerations

Silkscreen is included essentially for free on standard prototype panels — top and bottom overlays typically come as part of the base specification — so omitting it saves little, and a second side costs only cents.[155][1262][1306][237] Deliberately omitting the legend is a recognised cost-saving measure only at the extreme bottom end of manufacturing, measured in fractions of a cent per board; skipping it on an expensive instrument makes no sense.[813][536] Changes to silkscreen artwork late in a product's life are cheap compared to changes requiring new tooling.[e9cpKN69Avk] For boards that will never be seen, such as the underside of a densely loaded assembly, designers routinely decline the bottom overlay.[974][1193]

Because the legend is included anyway, a PCB ordered as an enclosure front panel gains fully labelled controls for the price of the board — a widely used alternative to machined and printed metal panels.[237][130][11][644] Gerber output for manufacture must explicitly include the top (and, if used, bottom) overlay layers alongside copper and solder mask, and the plotted Gerbers should be inspected before release.[990][1193]