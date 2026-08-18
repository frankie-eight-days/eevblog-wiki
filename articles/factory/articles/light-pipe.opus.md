# light pipe

A light pipe is a moulded transparent plastic part that carries light from an LED soldered to a circuit board out to wherever it needs to be seen on the outside of a product.[182][454] It works by trapping light inside the plastic, bending it around corners, and focusing it out an end face, so an LED sitting flat on a board can appear as an indicator on a front panel or case edge.[182][860] Its purpose is economic as much as optical: the LED stays a cheap surface-mount part placed by machine on the main board, and the light is routed to the user rather than the LED being routed to the user.[454][547]

## What it replaces

Without a light pipe, an indicator visible on a panel has to be built one of the harder ways: an LED bent up off the board on leads, an LED mounted on the back panel and wired across, or a separate flat-flex assembly running out to the indicator position.[182][454] Any of these adds wiring, hand assembly, or an extra sub-board. A light pipe collapses all of it into one injection-moulded part and lets the LED be placed at the same time as every other component.[454][547]

The saving is specifically in assembly-line time. If an LED must emit from the top face of a board whose components are all loaded on one side, the board has to make a second pass through the pick-and-place machine purely to fit those LEDs, which costs line time and money.[547] A light pipe over a bottom- or side-loaded emitter avoids that pass entirely.[547]

The counterweight is that a light pipe is still a part on the bill of materials, and one that has to be engineered and manufactured rather than bought as a standard component, so it adds cost.[1552]

## Optical behaviour

The commonest job is a right-angle turn. Vertical-emitter LEDs throw their light out of the top of the board, and a light pipe takes that vertical output, bends it, and brings it out the front or side of the case.[860][1552][9VVTGE7ABIk] The alternative — a right-angle-leaded or side-firing LED — is available but generally the nastier option, particularly in surface-mount form.[1552] Where the mechanical envelope is extremely tight, as in compact camera bodies, a right-angled emitter on the board mating into a light pipe is efficient use of the space that remains.[672]

Light pipes are also used in the other direction, as area illuminators rather than point indicators. In an edge-lit LCD backlight the light enters along one edge of a flat pipe, curves through it, and is emitted across the face; reflective strips along the outside contain the light in the middle so the spread is even.[417] Two or three LEDs fired into the side of a diffuser plate produce an even backlight the same way,[898] and a single LED into a well-designed pipe can light a whole display evenly.[571] Larger flat panels, including laptop screens, use the same principle of edge injection plus scattering across the back of the screen.[afwqRu7W8V0] Angled plastic channels fed by a row of LEDs are used to flood-fill light onto a scan line in document scanners.[1589]

The technique also scales down to segments: an array of individual LEDs can be made to imitate a segmented display by using the moulded plastic over each LED as a light pipe to light one segment.[1155][1669]

## Mechanical integration

A light pipe has to be held in position relative to both the board and the case, and the retention scheme is part of the design. Cheap approaches include a slot cut in the edge of the PCB that captures the pipe,[1552] and clips that engage two holes in the board.[182] At the more considered end, the pipe can be moulded permanently into the front panel so it cannot move or fall out at all.[1701] Where retention is poor, the pipe simply drops out when a unit is opened.[525][1552]

Because the pipe belongs to the case as much as to the board, its geometry constrains PCB layout. An LED mounted at a deliberate ten to fifteen degrees off vertical is the visible trace of that negotiation, and the person laying out the board has to work with the industrial designer responsible for the pipe and the case.[454]

Compliant materials can serve the same function without a dedicated part: a rubber keypad membrane over a reverse-mount LED acts as a light pipe of sorts.[330]

## Quality and failure

Light pipes vary widely in how well they do the job. A poorly executed one is visible as hot spots where the LED sits, rather than an even glow, and produces a backlight noticeably worse than better-built instruments achieve.[417] Worse cases are directional to the point of uselessness: a pipe that shows nothing when viewed straight on and only lights up when viewed from the edge is a hopeless light pipe.[1335]

Light pipes are also a mechanical liability. In one field failure, drop-induced tolerance stack-up between the plastic housing and the PCB was tight enough that impact popped the LEDs off the board, leaving holes punched in the light pipe; the fault escaped testing because only a handful of prototypes existed and nobody was willing to destroy one.[1759] Building enough prototypes to test to destruction is the corrective.[1759]

A light pipe can also complicate repair and modification, since it physically covers the LED and prevents soldering directly to it. The workaround is to trace the LED's connection back to an accessible point elsewhere — a driver transistor package or the top of the dropper resistor — and solder there instead.[182]

## Alternatives

The main alternative for a panel indicator is a reverse-mount, or bottom-emitter, LED: a standard SMD part placed with everything else, firing down through a hole or slot cut in the board and straight out the other side.[330][1292] Where the case front is already clear or has a moulded-in clear feature, no separate light pipe part is needed at all, and the light-guiding geometry becomes free with the case moulding.[1292][409] Bottom emitters are worth using specifically to avoid having to deal with light pipes.[1292]

## Sensing and test applications

Light pipes are not restricted to indicators. They are used to carry light to or from optical sensors, for example feeding an edge-detection signal back to a photodiode in a banknote acceptor,[525] and distributing light along the length of a laser printer drum from a single emitter.[1302]

In production test, fibre-optic light pipes are positioned over each LED on a board under test and routed back to a bank of photoreceivers, so an automated test system can confirm every indicator on the board actually lights.[yDfybZx02e0] A single jig may carry sixteen or more such pipes.[yDfybZx02e0]

## Sourcing

Off-the-shelf light pipes are a standard catalogue item available in a wide range of shapes and sizes, and are widely used.[182] Products in low volume may instead use custom pipes,[1669] and 3D-printed transparent pipes are viable for small runs and prototypes.[1690] Because they are generic, salvaged light pipes are worth keeping: a parts drawer of them is handy for hacking into later projects.[547]
