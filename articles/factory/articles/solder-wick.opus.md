# solder wick

Solder wick is a flux-impregnated copper braid used to draw molten solder away from a joint, a pad, or a plated through-hole.[180][183] Held against the work and heated with a soldering iron, the braid pulls the solder up into itself by capillary action, leaving the pad clean and tinned rather than blobbed or bridged — "It goes up the wick, hence the name solder wick."[183] It is treated as a non-negotiable bench item rather than an optional accessory: a basic soldering kit is not complete without it, and a $300 starter lab budget allocates for it alongside flux and a tip cleaner.[168][180][365][954]

## What it does

The primary job is removing excess solder. A joint that has been overfed becomes a ball with dags of solder trailing off the iron; laying wick over it and heating recovers a normal fillet without the joint having to be redone from scratch.[183] Applying too much solder is therefore not a fault that has to be avoided at all costs, because it can simply be wicked back off.[183]

The same action clears through-holes. Once a component has been pulled, the hole is usually still plugged with solder and will not accept a new lead; wick laid over the pad and heated opens it up, which is the standard way of preparing a board for replacement electrolytics.[365][538] For component removal generally it competes with a solder sucker or a dedicated desoldering station, and either can be used on through-hole capacitors.[763][861]

In surface-mount work it does two distinct jobs. It removes solder bridges between adjacent pins — a drag-soldered fine-pitch package that comes out with two pins shorted is cleaned up in one pass, including at 0.65 mm pitch.[186][434][1322][977] And it cleans up pads after a chip has been lifted with hot air, with ChipQuik, or by cutting and dragging the pins off, leaving a flat tinned footprint ready for the replacement part.[167][405][437][1322][1351] Where a chip has been removed by cutting each pin individually, wick then takes off the stubs left behind.[689] Cleaning pads down to bare metal matters most when a new device is going back on; if the board is only being tested and the chip is scrap, the pads can be left as-is.[405]

## Technique

The dominant failure mode is lifting pads. Placing the iron on the wick and dragging the assembly across a row of pins applies lateral force to pads whose adhesive has been softened by heat, and on a mediocre PCB the pads come off with it.[437][1322] The correct motion is to dab: press down on one pad, let the solder transfer, lift, move along, repeat.[437][688] This is slower but does not tear the footprint off the laminate.[437] Scraping should be reserved for cases where nothing else will work.[688]

Where the wick must be stroked, it is stroked longitudinally — along the axis of the pad, in the direction the pin runs — never sideways across the row.[688][405] A feather-light touch is required regardless of direction.[688]

Iron temperature is the other half of the equation. A low tip temperature protects the pads, and dropping from 370 °C to 330 °C is a reasonable response to a board that has already shown it will lift pads.[688][1281][437] Excessive heat combined with lateral force is what destroys footprints, so the two precautions are applied together.[688][1322]

## Flux

The braid is sold with flux already impregnated in it, and that built-in flux is what makes it work.[180] It is also the first thing to fail: flux dries out and ages in storage, so old stock underperforms, and the practical remedy is to add liquid flux from a pen before wicking.[1353][688] On corroded or 20-year-old joints, on conformally coated boards, and on mixed alloys — regular lead-free solder contaminated with a low-melting-point removal alloy — supplementary flux is what makes the difference between the wick grabbing the solder and merely smearing it.[1353][688] On ordinary joints in good condition the built-in flux alone is generally sufficient.[688]

Burning flux produces visible smoke and a distinct sizzle during fine-pitch cleanup; the fumes should not be inhaled.[186][688]

## Choosing and stocking

Brand quality is not cosmetic. Cheap braid has poor or insufficient flux and works badly; a good professional-grade multicore braid is the recommended default, and the cheapies are to be avoided.[180][688]

Width should be matched to the work, which means keeping more than one roll. A general-purpose braid of around 2.2 mm covers most tasks, with a narrow roll of roughly 1 mm for fine-pitch pins and a wide roll for bulk removal and for use with a wide chisel tip.[168][954][688] Very thick braid on a 0.65 mm pitch package is the wrong tool, and this is precisely where the superfine stock earns its place.[186] A roll of each width is regarded as the minimum sensible holding.[688]

## Limits and alternatives

Wick is not universally superior to suction. A desoldering station clears multi-lead through-hole parts far faster, though its nozzles block frequently and need continuous cleaning; wick plus a cheap manual sucker and a wide iron tip is a workable substitute for occasional repair work.[111][542] Dave Jones ranks a second soldering iron above a desoldering station in purchasing priority, on the grounds that a desoldering station is of no help with surface-mount parts, where heat must be applied to both ends of the component at once.[111]

The reverse also holds: a round desoldering nozzle cannot seal against irregularly shaped pads or oddly formed legs, and cannot reach solder close to a board edge, so wick — or simply heating and wiggling the lead free — is the better option there.[542] Some parts resist wick entirely and have to be removed by heating all leads simultaneously and lifting the package off.[230]

Used braid is worth keeping rather than discarding. Solder-loaded offcuts make excellent very low impedance straps and grounding links, a use Dave Jones keeps a parts-drawer stash for.[1017]
