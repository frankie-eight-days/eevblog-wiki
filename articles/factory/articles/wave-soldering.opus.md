# wave soldering

Wave soldering is a bulk soldering process in which a populated printed circuit board is conveyed over a standing wave of molten solder, so that every joint on the underside of the board is formed in a single pass.[12][431] It is the mass-production method for through-hole components, and for decades it was also the method for surface-mount parts, which were glued to the underside of the board and dragged through the bath.[907][1033] Its economics are unbeatable — one pass solders an entire board face — but it is a far less controlled process than reflow, and almost every characteristic feature of a wave-soldered layout exists to stop the wave from bridging pins.[431]

## The process

The board travels on a conveyor through a preheat stage and then over an open bath of molten solder, where a pumped wave rises up to meet the underside.[684][12] The bath is genuinely hazardous in operation, since the solder can splash.[12] Better machines use multiple waves rather than one: the extra waves prevent shadowing, where a tall through-hole lead or a can-style component blocks solder from reaching what sits behind it.[684] Machine temperature profiles are stored and selected to suit the board's thermal mass and component mix, and the machine tracks the board's progress through preheat and over the bath.[684] The bath is charged from solder bars, which in modern installations are lead-free.[2vJ0c0ioAXY]

On a mixed-technology board the sequence is two-step: the surface-mount side is reflowed first, then the board is passed through the wave to solder the remaining through-hole parts.[12][782][446] Because the wave heats only the individual pins from below rather than the whole component body, through-hole parts see a different thermal exposure from reflowed ones.[782]

## Glued-down surface mount

Surface-mount parts on the wave side cannot simply be placed; they must be bonded to the board first, or they float off into the solder bath.[811][745] Manufacturers dispense dots or lines of adhesive under each part, and this glue is one of the most reliable tells of a wave-soldered board — red or orange blobs visible oozing from beneath resistors, MELF diodes and small ICs.[907][1090][1562][378][1714] The glue pattern is laid down from a glue mask profile, so dots often appear under positions that were later depopulated.[1091][1ngqB4mxZOI] After gluing, the board is inverted and run over the wave.[651][1ngqB4mxZOI]

## Solder thieves and pad design

The dominant layout concern is preventing bridges between closely spaced pins as the wave sweeps across them. The standard countermeasure is a solder thieving pad — an oversized pad placed beyond the last pin of a package, which captures the excess solder peeling off the wave and stops it dagging across to the adjacent pin.[431][1033][811] These pads go by several names and are covered by established footprint standards for bottom-side wave soldering.[431][651] Since the thief only works on the trailing end, a designer who knows the direction of board travel needs them on one end only; putting them on both ends is insurance against the panel being run the other way round.[431]

Boards that predate solder mask between pins relied entirely on this kind of geometry, and it worked — wave-soldered vintage boards with enormous solder mask expansion and no mask webs between pins show no bridging at all.[1111][1243] Where mask between pins is absent, another defence is to rotate the package: mounting DIPs at 45° to the direction of travel prevents shorts between pins.[1243][1133]

## Orientation and direction of travel

Component orientation relative to the wave is a design decision, not an aesthetic one. ICs should be oriented so the solder drags along the row of pins rather than across it, which is why every chip on a properly laid-out wave-soldered board points the same way.[431] Passives should sit with their long axis vertical relative to travel; a passive lying the other way forms a cavity behind it as the last of the solder passes, and will not solder as consistently.[431]

Because all of this depends on which way the board goes through the machine, designers mark the direction on the silkscreen — commonly a large arrow, or the word DIP with an arrow.[431][446][598][1322][619] The marker survives on the finished board and makes the process direction readable long afterwards.[446][1322] Even boards that appear to be all surface mount carry the arrow, because their connectors still need the wave.[446] The convention is followed loosely enough that direction arrows sometimes appear on boards that are double-sided reflow and never see a wave at all.[1150]

Direction is also readable from the joints themselves: the pins at the trailing end of a package carry visibly more solder than those at the leading end, because the leading pins hit the solder first and it drags across.[431]

## Identifying wave-soldered work

Beyond the glue and the thieving pads, the signature is solder plated all the way up the legs of the parts — evidence a molten bath washed over the whole component, whereas reflow from paste leaves solder only on the pads.[431] Wave joints simply look different from reflow joints, carrying noticeably more solder.[619] Wave joints are also uniform across a board, which makes later rework obvious: a repaired chip stands out by its flux residue and mismatched joint appearance against the original wave soldering around it.[1111][815][1376][1203][1189] Parts that would not survive the bath — reed relays, temperature-sensitive supercapacitors, batteries, and anything physically awkward — are excluded from the wave and hand-soldered afterwards, as are ribbon cables and similar assemblies.[1189][207][256] After auto-insertion, through-hole leads are bent over on the underside before soldering, which makes them awkward to clear later with a solder sucker.[763][256]

Joint quality varies widely between manufacturers. Good wave soldering is clean and consistent even on large power transformers; poor operations produce crusty joints and messy, uneven results.[449][1278][1190][1091] Clearance problems coming out of the machine were historically a routine source of shorts between pins and ground planes on dense boards.[717ampROkvc]

## Deliberate tinning

Wave soldering is also exploited as a free way to increase trace current capacity. Leaving solder mask off a trace lets the wave deposit solder onto the bare copper, thickening the conductor at no extra cost, since the board has to go through the machine anyway.[314][317] Measured against thicker copper — 2 oz instead of 1 oz — which costs real money, the technique is effectively free.[314] Controlled measurement puts the improvement at roughly a halving of trace resistance for a heavy deposit, with lead-free solder giving a comparable result of around 72% reduction at maximum thickness on a 4.2 mm track.[317][319] The gain is real but not dependable: the spread is wide, and a thin coating does very little.[317] The same effect appears unintentionally on older tin-plated boards, where wave flowing over untinned, non-levelled plating leaves an uneven, globby surface.[557]

## Thermal limits and process choice

The wave imposes its own constraints on part selection. Through-hole connectors are frequently specified as wave solder capable with no reflow rating stated at all; running such a part through a reflow oven instead — paste-in-hole — melts the plastic body, while the surrounding surface-mount parts survive unharmed.[782] Connectors intended for paste-in-hole use high-temperature thermoplastics specifically so they can take the full reflow profile.[782] Layout rules interact with the process too: solder mask expansion between pads must leave four or five thou of mask, or solder will bridge during hand or wave soldering.[244] Where a section of board must be kept clear of solder entirely, peelable solder mask can be specified to protect it through wave and reflow, then removed afterwards.[1259]

For surface-mount work the process has been almost entirely displaced by reflow, which is far more controlled and produces much cleaner joints; passing a bath of molten solder across an entire populated board face, with every part individually glued, is a comparatively crude way to build.[431] Wave soldering persists where through-hole content remains, which on double-sided-loaded consumer and industrial boards is still routine.[913][856][651]
