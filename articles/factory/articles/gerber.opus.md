# gerber

Gerber is the file format in which a finished printed circuit board layout is handed to the board manufacturer. It is a proprietary format, and deliberately the least common denominator among PCB data formats: it exists to drive a plotting machine, and its entire vocabulary amounts to instructions to "turn the light on, drag it over here, shut the light off", which draws one line onto a piece of film.[349] Everything a fabricator does to a bare board — imaging the copper, the solder mask, the silkscreen — derives from that set of plotted films, and everything the format cannot express has to be carried by companion files or by a separate written note.[349][990][127]

## What a Gerber set contains

Gerbers are generated one file per layer, and the set is the deliverable rather than any single file.[127][239] A typical two-layer job produces top overlay, top solder mask, top layer, bottom layer, bottom solder mask, bottom overlay, and top and bottom paste.[127] The paste layers are for the assembler and the stencil, not for the bare-board fabricator, who has no interest in them.[127] Layer naming is by extension — GBL for the bottom layer, and so on — and a Gerber set may include layers that generate empty: a board with no components on one side still produces a paste file, just a blank one.[239]

Gerbers carry no drilling information at all. Holes are specified in a separate NC drill file, which is why a via visible in the finished board is invisible in the copper Gerber, and why pads in the Gerber appear as solid copper with no hole in them.[155][990][127] The NC drill file is industry standard and supplies drill sizes, drill counts and drill positions.[127] Plated and non-plated holes can be output as separate drill files; manufacturers handle that without difficulty.[1193]

Gerbers also do not carry fonts. Text on the silkscreen is rendered out as a mass of individual tracks, which is why overlay layers are slow to load in a viewer compared with copper layers.[239]

## The board outline and other mechanical information

The board outline is conveyed on a mechanical layer, and no accompanying explanation is required — a fabricator loading the Gerber set into their CAM software recognises which layer defines the outline and cuts the board to it.[974][1262] The same mechanical layer is the natural place for fabrication notes and tooling instructions: material and thickness callouts, V-scoring lines, routing paths.[974][127] A V-groove drawn as a line on a fab-notes layer is not part of the board layout, but it appears in the Gerber output and gives the manufacturer everything needed to score the panel.[127]

Panelisation works the same way. In a CAD tool that supports it, placing the individual board repeatedly into an array lays down only placement information, and the full panel materialises when the Gerbers are generated.[239] Alternatively, only the single-board Gerbers, bill of materials and other files are supplied to the assembly house, which does the panelisation, fiducials and tooling itself as part of a turnkey service.[127]

Process options that are not geometry — immersion gold, edge plating, specific laminates and tolerances — are not in the Gerbers and must be stated in drawings, in an email, or through the options on the manufacturer's ordering page.[1193]

## Resolution and the coordinate format

Every Gerber export offers what the software calls a coordinate format, which is really an output resolution: how many digits of precision are written into the file.[1327] Imperial formats run 2:3 for 1 mil resolution, 2:4 for 0.1 mil, and 2:5 finer still; metric formats run 4:2 for 0.01 mm and 4:3 for one micron.[1327][990] KiCad exposes only two metric options, 4.5 and 4.6 in millimetres, while Altium can be set in either system.[1327]

Choosing too coarse a format silently rounds the design. At 2:3, a trace set to 10.5 thou renders as either 10 or 11 thou, because the output cannot represent the half.[1327] The practical consequence is a design that passed its own rules being rejected by the fabricator's incoming check — a nominal 3.5 thou minimum that rounds the wrong way becomes a re-route of large parts of the board.[1327] There is no cost to picking the highest resolution available, and 2:5 or its metric equivalent is the sensible default; units themselves make no difference, since manufacturers handle either.[990]

## Generating and packaging the output

Gerber generation belongs at the end of a checked sequence, not before it. A design rule check comes first, so errors are caught while they are still cheap to fix.[1193] Refilling copper zones immediately before plotting is a hazard rather than a precaution: a clearance changed inside the zone settings can quietly remove copper that the earlier inspection showed present.[1193] Altium's outjob mechanism formalises the whole sequence — DRC, Gerber generation, NC drill generation, bill of materials — into a repeatable board release process, which is the rigorous approach for professional work, if heavier than a one-off hobby board warrants.[990][953]

Two export settings deserve attention beyond the resolution. The film size defines the plotted area and simply needs to exceed any board being made; the reference position determines where the board sits on that film, and referencing it to the design's own origin marker is reliable.[990] Getting absolute origin confused with a relative reference is a way to produce a set of layers that do not line up.[Ep4r-wD7PPs]

For delivery, the whole set is zipped. Aperture files and report files such as the DRR are probably unnecessary for modern fabricators but cost nothing to include, and extras are simply ignored; simulation netlists can be left out.[990] Some manufacturers offer a subdirectory variant with no silkscreen overlay for boards ordered without silk.[1306] Upload sites accept the zip directly, resolve the layer assignments from standard Altium, Eagle or KiCad output names, and let the user assign layers manually where the naming is non-standard.[785][1306]

## Gerbers versus native CAD files

Most PCB houses will accept native design files directly — Altium PCB files, Eagle board files, KiCad files — and will make the board from them without question.[990][1193] This is not the controlled way to do it. Generating Gerbers means the designer can inspect exactly what the manufacturer will receive, so that what is seen is what will be made.[990] For anything beyond a genuine one-off, and certainly for anything semi-professional, Gerbers plus NC drill files are the correct deliverable, and are how professionals release boards.[990][1193]

The requirement runs the other way too. A PCB CAD package that cannot export Gerbers cannot get a board manufactured, which makes Gerber export in a freeware edition close to a showstopper rather than a premium feature.[255] Historically the function was sometimes a separate program entirely: Protel's Autotrax shipped as Tracks Edit for layout and Tracks Plot for Gerber generation, and the plotting half did not come as standard.[747]

## Checking Gerbers

A Gerber viewer is the last inspection stage before manufacture, and it catches what the CAD system hides. Looking at the plotted output after weeks of staring at a clean design and a passing rules check is precisely when an obvious error becomes visible.[349] Viewers are widely available: Altium contains one built on Camtastic, which produces a composite view of all layers superimposed with individual layers selectable, though it is crude;[990][1327] KiCad ships one; and most online fabricators provide a browser-based preview of the uploaded set before ordering.[1327][1306][1193] Dedicated CAM tools such as CAM350 occupy the same role at the professional end.[349] Circuit Maker, by contrast, removed Gerber viewing from the Altium feature set it otherwise inherited.[754]

Online viewers have real limits. At least one commonly used fabricator preview displays only top and bottom copper, giving no view of inner layers on a four-layer board — exactly where a mistake is most expensive to discover after the fact.[1193] Viewer measurement accuracy is also limited, so a rendered trace width read off screen is approximate.[1327]

Generation can fail outright rather than degrade. A KiCad error reading that the board outline cannot be determined stops plotting entirely: no files appear in the output directory, for any layer.[1193] Some artefacts in the output are harmless — a plotted sheet frame, for instance, is simply ignored by the manufacturer.[1193]

## Fabricator-side processing

The manufacturer's first step is to process the supplied Gerber and drill files, by methods that vary with their CAM software and machinery.[939] Incoming checks are automated: the fabricator's software examines the Gerbers against the ordered capability class, and traces narrower than the purchased minimum — 5 mil routing submitted against a 6/6 order, for example — come back rejected.[1259] Bare-board electrical test is also derived from the Gerbers: the tester extracts a netlist from the copper layers, reconciles it against the supplied IPC-D-356 test file, and then probes every trace, pad to pad, which is what 100% electrical testing means.[349][939]

Manufacturing options offered in an ordering interface are frequently overridden by the file data, and correctly so. Via treatment is the clearest case: tented or untented vias are inferred from the solder mask expansion present in the Gerber, so setting all vias tented at export time is the whole of the instruction, and the shopping-cart option becomes irrelevant.[500][1259] The general principle is that a PCB house should build exactly what it is told, and a good one does not make such choices on its own initiative.[500]

## Unauthorised modification

Manufacturers modifying customer Gerbers is a recurring failure mode. One prototype supplier expanded the ground plane copper on a delivered board relative to the submitted files, eating away an eighth-thou trace, even though the design already met the 6 thou trace and 6 thou copper-to-copper clearance the supplier itself specified.[155] Another altered pad widths, with the result that tracks vanished and the ground plane was broken.[500][1193] The engineering position is that a manufacturer should not touch a customer's Gerbers without express written permission — "Don't touch my Gerbers"[1259] — because the submitted files are the specification and the customer cannot verify a board built to something else.[1193][500]

Leverage over this varies with what is being bought. Paying for a whole panel gives the ability to demand that the files be built as sent; on a shared prototype panel at a few dollars for five boards, a stated policy such as solder mask expansion being adjusted to meet a 0.2 mm bridge spacing may simply be non-negotiable.[1327] Suspected pullback or other silent edits on inner layers are difficult to confirm after the fact on a finished board.[ct9K-EutiIQ]

## Limitations of the format

Gerber's simplicity is its constraint. It has no way to express part polarity or orientation, blind and buried vias, back drilling, V-grooved slots, or milled content — none of that is in a Gerber file.[349] The result is a multi-format delivery: RS-274X for the copper, Excellon for the drill data, IPC-D-356 for electrical test, and drawings in ASCII, PDF, HPGL or JPEG for everything remaining, with a translator required at every boundary.[349] Machines downstream then perform conversions purely to reconcile these formats with each other, such as reworking a Gerber-extracted netlist to match the supplied 356 file before driving the bare-board tester.[349]

Attempts to fix this predate the modern industry. IPC assembled the D-350 format in 1970 as an intelligent version of Gerber, adding an aperture list and other data, but it did not take hold.[349] IPC-2581 is the later single-source approach: one file describing the entire PCB structure — CAD and CAM data, parts, models — with a rich defined schema covering the drilled and milled content, embedded and stacked components, and test support that Gerber cannot represent, plus viewing software as part of the deal.[349]

Gerbers are also a one-way transformation, which becomes a problem when old designs must be revived. Where the original CAD tool is gone, the fallback is a Gerber copy: load the Gerbers as a backdrop for the board layout and manually retrace every track in the new tool.[1032]

## Gerbers and open designs

Distributing Gerbers is how a design becomes physically reproducible by anyone: download the set, upload it to a low-cost fabricator, and receive boards for a few dollars.[1374][1649] Published Gerber sets appear for panel-integrated parts, instrument accessories, dummy loads, and even printed rulers.[1649][304][481][1471] A satellite kit supplying Gerbers for the internal boards rather than the boards themselves is the same arrangement.[shSoVLSPbaQ]

Gerbers alone, however, do not make hardware open source. A PDF schematic plus a Gerber set is insufficient; the original PCB and schematic source files must be released, along with firmware, any required PC software, the bill of materials and supporting documentation, so that the design can be modified and not merely rebuilt.[195] A project that publishes only source CAD files in a format requiring hours of import cleanup, without a ready Gerber set or a bill of materials, is technically open but not straightforwardly manufacturable by a third party.[1374]

## Adjacent uses

The paste Gerber feeds the assembly side rather than the fabricator. Stencil printers and pick-and-place systems ship with CAM software that loads the paste layer directly, working either on a single board or on the whole panel.[163] Gerber output also serves as an artwork format in its own right: open-source bitmap-to-Gerber converters exist for placing arbitrary raster graphics onto copper or silkscreen in Altium and KiCad, a task otherwise awkward in those tools.[1229]
