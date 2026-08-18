# solder paste

Solder paste is a suspension of fine solder alloy powder in flux, deposited onto printed circuit board pads before components are placed and the assembly is heated until the alloy melts and wets the joint — the process called reflow soldering.[346][239] Because the flux is already carried inside the paste, no separate flux application is needed: the paste is put down on the board first, the part is laid on top, and heat does the rest.[346] It is the foundation of essentially all modern surface-mount assembly, and it is also the only practical way to solder packages whose contacts are hidden beneath the body, such as QFN and MLF devices with a central thermal pad.[346][1322]

Paste is not a universal replacement for wire solder. Ordinary leaded solder is easier to work with and adequate for most bench tasks; paste is worth adopting specifically for advanced surface-mount work, where it can be very useful.[180]

## Composition and grades

Paste is sold in alloys matching conventional wire solder. A typical leaded formulation is SN63 — 63% tin, 37% lead — close to ordinary 60/40 and explicitly not lead-free.[415][180] Lead-free tin-based pastes are standard for production boards, and a stencil printer loaded for a lead-free board is running lead-free paste.[264][558]

Pastes are graded by the size of the solder powder. The finest commonly available is type 6, whose individual solder balls measure 5 to 15 microns.[163] Finer powder is what makes very small apertures print cleanly.

The flux system matters as much as the alloy. No-clean paste is the preferred choice because it leaves behind no residue requiring a post-reflow cleaning step.[558] Where cleaning is unavoidable, paste selection and the matching cleaning agent have to be treated as a single decision: on boards built from low dielectric absorption laminates such as Rogers material, an assembly house washing with its usual general-purpose cleaner can leave residue that ruins the board's performance, and datasheets for such designs specify both the paste and what to clean it with.[1755] Residue from paste flux is visible on finished joints as a film around the pins.[115]

## Storage and shelf life

Paste must be refrigerated and kept airtight, with the nozzle replaced on the syringe before it goes back in the fridge; left out, it goes off.[415][180] Before use it has to be brought back to room temperature over a couple of hours.[415] It also carries a printed shelf life, beyond which performance is no longer guaranteed.[415] Paste already dispensed onto a stencil printer can be scraped back and reused for perhaps two or three days.[264]

These handling demands, together with the cost, make paste a poor fit for very occasional work: for one or two boards a year it may not be worth the trouble.[415] For QFN rework the quantities involved are trivial — a ten-dollar tube goes a long way — and a 15 g syringe is enough for many stencil prints of a typical board.[346][415]

Working time is also a constraint. Hand-placing several hundred parts on a pasted panel can take long enough that the paste begins to dry out before the last component is set, which is one of the arguments for a pick-and-place machine on larger boards.[740]

## Stencil printing

The standard way to deposit paste is through a stencil cut from the paste mask layer of the PCB design, so that paste is applied only to the pads and nowhere else on the board.[239] Production stencils are stainless steel, but these are expensive for one-off use; Mylar, Kapton or polyamide stencils can be laser cut directly from the CAD file cheaply enough that they are effectively given away with small board orders.[415][658][795]

Manual printing technique:

- Surround the board with scrap boards of the same thickness so the stencil sits level — 1.6 mm offcuts for a 1.6 mm board, thin ones for a 0.8 mm board.[407]
- Inspect the stencil first to confirm every aperture is actually cut.[415]
- Tape only one edge, forming a hinge, so the stencil can be lifted straight up as a flap without dragging across the printed deposits.[558]
- Spread with a squeegee or putty knife at a controlled angle of attack; a plastic credit card works well and is better for the job than a rigid metal spreader.[407][658][1003]
- Lift the stencil cleanly and do not touch the result.[415]

Small amounts of paste smeared between adjacent pads after lifting are normal and not a cause for concern.[415] Placement afterwards need not be precise, since surface-mount parts self-centre on their pads as the paste reflows, though the strength of that effect varies by component.[558]

Production stencil printers automate the same sequence: the board is aligned by a fiducial camera, raised hydraulically to compress it against the stencil, and the squeegee wipes across.[264] The result is described in industry terms as silk-screening the paste onto a bare board, and it feeds directly into pick-and-place and then the reflow oven.[684][239]

## Syringe and dispenser application

Paste is also supplied in syringes for hand application, either before the part is laid down or afterwards, with the quantity being the whole difficulty — too much and it has to be cleaned off.[186] For a fine-pitch package with no accessible pins, a bead or line of paste is laid along each row of pads plus the thermal pad, the part is held down, and a hot air gun at roughly 250 to 260 °C brings the whole area up to a uniform temperature.[346]

The consistent bench judgement is that too little paste is safer than too much: a joint short of solder can be touched up with an iron afterwards, whereas excess has to be removed.[346] In practice this errs far enough that reflowed joints sometimes come out visibly starved.[346]

Manual syringe dispensers with a lever mechanism need a delicate touch — where twenty full lever strokes drive the plunger to the bottom of the barrel, a single full depression dispenses far more than one pad's worth and simply oozes paste over the board.[556]

Automated paste dispensers occupy a middle ground between hand syringes and stencil printing. Such a machine places paste only and is not a pick-and-place; a representative unit holds the board on magnetic clamps that allow arbitrary positioning on the platen, references itself to the board's fiducials, and drives a paste syringe through interchangeable nozzles.[163][1686] The output is a board with paste on the individual pads ready to go to a pick-and-place machine.[200] Dispensing is inherently slower than stencil printing.[1686]

## Reflow profile

Reflow proceeds in phases: a slow, even preheat that avoids cracking components through thermal shock; a soak that activates the flux inside the paste and drives off its volatile chemicals; the reflow spike itself, which melts the solder; and a controlled decay.[558] The correct profile comes from the paste manufacturer's datasheet, and that profile is what gets programmed into a reflow oven or a converted toaster oven.[415]

A profile is specified as a band rather than a line — an upper and lower curve the board temperature must stay between — typically peaking around 180 seconds before tapering off.[415] A no-clean lead-free paste supplied with a reflow oven kit specified a peak of 250 °C and a ramp rate of 2 °C per second, with the board expected to pass at least 220 to 230 °C for the joints to form.[558] The right profile varies with the paste and also with the board itself: heavy ground planes without adequate thermal relief change how pads heat and can pull parts into tombstoning.[415] Surface-mount parts are designed to survive this, tolerating a couple of hundred degrees for a sustained period.[346]

Where a board fails to reflow, high local thermal mass is the usual cause — a large pad with a heavy trace running off it reaching insufficient temperature, or the flux embedded in the paste failing to clean the joint properly.[588]

## Failure modes and layout interactions

**Solder balls.** Paste volume is never perfectly repeatable from board to board, and a deposit slightly over target can leave a stray solder ball loose on the assembly, which then becomes an unpredictable source of shorts.[884]

**Bridging.** Where the board has no solder mask between adjacent pads, reflowed paste can bridge across, though such shorts are straightforward to clean up.[1322]

**Wicking down vias.** Vias in pads — including thermal via arrays under a power package — let molten solder wick down through the board, which is a genuine drawback of the technique.[744] Bare-board fabricators do not care about vias in pads, but they offer a via-plugging option specifically so the paste is not wicked away during reflow; unplugged vias are acceptable if the solder loss is tolerable.[1259] Where solder does leech through, the amount left on the top side becomes uncontrolled, and if the loss is not accounted for the device may end up with insufficient solder holding it down.[607]

**Joint geometry.** A paste-and-reflow joint wets the underside of the terminal and forms only a small fillet at the side; it does not climb over the top of the lead the way a hand-soldered joint does, so the hand joint is mechanically more robust.[1137] The same signature distinguishes reflow from wave soldering, where a molten bath plates the legs of the parts right up their length.[431]

**Thermal pads.** A package with a bottom-side thermal pad cannot be soldered by pre-tinning the pad and reflowing, because tinning leaves a lumpy surface before it melts; paste solves this chicken-and-egg problem by going down flat first.[1322] The thermal pad can also dominate the joint mechanically, preventing the part from self-aligning as the perimeter pads pull it in.[346]

At the extreme of miniaturisation, some large processor packages carry no balls at all: paste is simply applied to the land pattern and reflowed, and with pad widths of the order of 180 microns the resulting quantity of solder is so small that modest shear force can strip every pad at once.[1341]

## Related uses

Paste-based deposition is used to fill vias with solder, which is done at the assembly stage rather than by the bare-board fabricator: the vias are left untented and solder is placed via the paste mask, raising the current-carrying capability of the via.[500] The alternative is wave soldering, where the wave bubbles up and fills the holes.[500]

Paste can also be applied to the underside of a board so that a part with a bottom die pad protruding through a cut-out is soldered from the reverse side.[677] Hot-bar attachment of flat flex to a board relies on a conductive paste under the joint which melts as the bar passes across, forming the connection.[808]

Where a design is released with full manufacturing data, the paste layer accompanies the assembly drawing and pick-and-place files as one of the standard outputs.[1581]
