# flux

Flux is the chemical agent that strips the oxide layer off metal surfaces so that molten solder can wet them and form a joint.[183] Every metal surface involved in a solder joint — pad, pin, wire, lead — rusts or oxidises in air, and the flux cleans that coating away just long enough for the solder to flow and bond.[183][1205] Without it, soldering does not work at all: metals oxidise too easily for solder to take on its own.[183] It is the single component of the process that cannot be substituted or skipped, whether it arrives inside the solder or is applied separately.[183]

## What flux does at the joint

The flux must reach both mating surfaces — the pad and the pin — not just one, because both carry oxide.[183] Where it does its job, the solder flows through the hole and wets around the top side of a through-hole joint; where there is not enough flux present, the solder fails to flow through and does not wet the far side, and the fix is to resolder the joint with flux applied on top.[183] Oxidised component leads make this visible: the solder has a hard time wetting, and the joint takes more flux or longer dwell time to come good.[183] The same effect shows on aged or contaminated SMD pins — flux gets straight through that contamination and lets the solder take.[997]

Flux also carries a joint where the iron cannot physically reach. On fine-pitch and no-lead packages the tip never touches the pin itself; the technique relies on flux plus molten solder creeping under the package to reflow the pin.[408] For a QFN placed without paste or hot air, the whole assembly is fluxed, solder is put on the pad, and the chip is pressed into place so the solder reflows underneath.[346] Some pad geometries are designed so that flux alone is enough — solder already present on the pad is pushed back into the connection with no new solder added.[353]

Flux takes a moment to activate once heat is applied, and a joint that seems sticky or reluctant may simply not have had that moment yet.[1110][1064]

## Forms and delivery

Most everyday soldering gets its flux from the solder itself. Cored solder carries flux down the middle of the wire — multicore types run five separate cores of flux through a strand as thin as 0.38 mm — and that flux cleans the joint as the solder melts.[1205][997][1433] For general work a good quality multicore solder, a temperature-controlled iron and tip, and fine solder are the whole requirement; separate per-joint fluxing is a level of trouble most work does not need.[183]

Where extra flux is wanted it comes as a pen, as a brush-on liquid, or as a gel.[180][1305] The flux pen is the convenient form and the one to have on the bench; branded pens cost around ten dollars and last a very long time.[180][688] Cheap flux pens are worth buying even on a minimal starter budget, because they make surface-mount and general soldering markedly easier.[954] Rosin is the standard chemistry for electronics — rosin is a tree sap — and the broader family also includes no-clean and water-soluble types.[1305][874][407] Solder paste for reflow carries its own flux.[558] Solder wick is supplied impregnated with flux, and the quality of that flux is a real differentiator between good wick and cheap wick.[688]

## Through-hole versus surface mount

For through-hole work no external flux is required; the flux inside the solder is sufficient.[183] The same applies to ordinary discrete SMD components — the flux in the solder will do, with no separate application needed.[1306][186]

Fine-pitch surface mount is the opposite case. Flux is the key to good surface-mount soldering: on a 0.5 mm pitch quad flat pack the pads are fluxed before the chip goes down, and more is added along the pins before drag soldering.[186] A side-by-side comparison of the same 0.65 mm pitch device soldered with and without added flux showed the fluxed side reflowing distinctly better and coming out cleaner.[186] Gold-flashed pads reduce, but do not eliminate, the need: everything takes better, less flux is required, the surface does not corrode as much, and it is flatter, which matters as pitches get finer and for BGAs.[186] A brand-new board with a brand-new unoxidised component can be soldered without added flux, but flux still helps.[186]

Connectors are a standing case for extra flux. USB connectors are awkward enough that fluxing the pads — and the pins as well — is worth doing before attempting them.[1306] Solder cups on gold-plated contacts still depend on the flux to clean both the cup and the wire, since neither surface has been properly prepared.[183] Tinned wire is re-fluxed, cleaned and freshly tinned before use in dead-bug work so that the joint really takes.[181]

The prevailing bench judgement is that flux is cheap insurance and erring on the generous side costs nothing: "you can never have too much flux".[688][186] The engineering advice given for beginners is the same — "apply flux generously".[1646]

## Temperature and burning the flux off

Flux is consumed by heat, and excess temperature destroys it before it can work. Too high a temperature simply burns the flux off in smoke, and this is one of the standard causes of poor results.[183][200] A badly regulated high-temperature iron makes the effect obvious — the flux vanishes in smoke rather than going into the joint.[1113]

The related error is loading solder onto the tip and carrying it to the joint. The flux goes up in flames on the way across, and what lands on the joint is fluxless solder, producing a terrible or cold joint.[183] Carrying a small lump of solder on the tip is legitimate purely as a thermal-transfer aid, since molten solder heats the joint faster than a dry tip, but it can never be the only solder applied — fresh cored solder must still be fed in to bring flux to the joint.[183]

## Rework, desoldering and repair

Flux is applied before hot-air work as a matter of routine, to help a package release and to let both sides melt together so the chip can be lifted with tweezers.[1322][E1IqcGcZKHE] It is applied before wicking, before reflowing a suspect processor, and before removing a chip from a donor board.[1353][9s9LXOBknck][1522]

Solder wick is a specific weak point. The flux in wick dries out and ages, so there is never enough of it in old wick, and adding flux is what makes it lift solder properly.[1353][688] Flux also helps when the metal on the board is a mixed and awkward alloy — for instance ChipQuik low-temperature alloy left mingled with the original lead-free solder.[688] The ChipQuik process nominally calls for flux along all the pins before the alloy is applied, though the removal will often succeed without it; the cases where the extra flux earns its place are stubborn chips and very old joints.[688]

On repair work, applying fresh solder to a tired joint is partly a way of introducing new flux to it.[1091] Old boards may need mechanical preparation first — scraping through conformal coating to expose gold before flux and a fine-pitch iron can do anything.[1433][1353]

## Reflow and production

In a reflow profile the soak phase that follows preheat exists to activate the flux inside the solder paste and drive off its volatile chemicals, before the profile peaks into the reflow phase proper.[558] When a production board comes out with an unreflowed joint, the two candidate causes are that the joint never reached reflow temperature — a large thermal mass with a heavy trace attached will lag the rest of the board — or that the flux embedded in the paste failed to clean the joint.[588]

## Residue, fumes and cleaning

Flux leaves residue, and boards are cleaned afterwards with a cleaner and an anti-static conductive brush to remove it.[183] The visible gunk left around a drag-soldered chip is largely flux residue.[997] Residue is also a diagnostic hazard in reverse: old flux from original hand assembly can look like contamination worth chasing, and distinguishing it from genuine damage such as leaked electrolyte depends on whether the deposit is localised to the joints or spread across the board.[h9V0qJ4p3Aw][1527]

Solder smoke is flux smoke. It comes from the rosin flux, whether from the cores in the solder or from separately applied gel or liquid flux, and it is produced identically with leaded and lead-free solder — it is not lead fume.[1305] It should not be inhaled.[688][183]

## Limits

Flux is not a universal remedy. A QFN with corroded pins failed to take despite a large dollop of flux and ample solder at 350 °C, the corrosion on the package having defeated the process rather than any shortage of flux.[408] Excess flux on a fine-pitch job is untidy rather than helpful.[590] And flux quality is not guaranteed by the presence of flux: cheap low-melting-point solder can behave as though it contains no proper flux capable of cleaning the wires, making joints slow and ugly to form.[780]
