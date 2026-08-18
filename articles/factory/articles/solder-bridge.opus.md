# solder bridge

A solder bridge is a continuous path of solder spanning two adjacent pads or pins that should remain electrically separate.[499][186] On a fine-pitch package it is the dominant hand-assembly defect, and it is also the dominant defect the board designer is expected to design against, since the fix for most bridging is in the layout rather than in the operator's technique.[255][1353] The same physical thing, made deliberately, is a standard configuration and repair element: a blob of solder placed across two pads to close a link, select an address, or reroute a track.[755][1580][860]

## Why bridges form

Bridging is fundamentally a question of whether molten solder has anywhere better to go than the gap between two pins. Excess solder paste is the simplest cause -- too much deposited on the pads and adjacent pads short together on reflow.[346] In hand soldering, dragging a loaded tip along a row of pins leaves shorts wherever the tip carried more solder than a single joint needed, and this happens even to experienced operators.[186][434]

The structural cause is a missing or inadequate solder mask dam between pins. Where a manufacturer omits mask between the individual pads of a fine-pitch part, there is nothing to stop paste from two pads merging, and a bridge across the row is the expected outcome rather than an accident.[1306][1322] A dam that is present but too thin fails in two ways: it may not adhere to the fiberglass and simply peel away, and on close pin pitches it is too small to arrest the solder even when it survives -- some solder mask is better than none, but not by much once it is thin enough.[1353] Design tools can produce the same condition without the fabricator being at fault: an incorrect solder mask expansion on a quad flat pack's pads yields one solid mask opening over the whole row instead of a gap per pin, and soldering such a board bridges the pins together.[255]

Wave soldering adds a directional cause. As the wave crosses a package it drags solder across the pins much as a chisel tip does, and at the trailing end of the row -- the last two pins to leave the wave -- the accumulated solder has nowhere to shed and shorts across.[431] Components must be glued down for the process to work at all, and the pad geometry is what prevents solder dags forming between pads as the wave passes.[430][431]

## Design countermeasures

Correct solder mask between pins is the primary defence, and on a properly masked board a stencil-and-reflow cycle can produce a full fine-pitch row with no bridges and every pin wetted.[415] A bridge that does form in paste will often pull itself apart as the solder reflows and surface tension draws it onto the pads.[415]

For wave soldering, the countermeasure is a solder thieving pad: an oversized pad placed past the end of the pin row, so that solder preferentially flows to and stays on the larger pad rather than shorting the last two pins.[431][430] Because the effect is directional, thieves are only strictly needed at the trailing end for a known travel direction through the machine, but they are conventionally placed at both ends so the panel can be run either way.[431] Slightly enlarged pads at the end of a chip serve the same function in reflow, catching the solder so it does not form vortices and short out adjacent pins, and peeling it away from the pin before it.[856] The resulting asymmetry is diagnostic after the fact: extra solder on the pins at one end of a package indicates which way the board travelled through the wave.[431]

Carrier substrates can address the problem mechanically. A grooved or well-based pad system confines the solder to each pin's channel, so drag soldering along a 0.4 mm pitch row produces no bridges and a consistent solder volume per pin.[408]

## Technique and rework

Where drag soldering along a row risks shorts, dragging outward from the pins instead of along them helps prevent individual shorts between adjacent pins.[434] A bridge that does occur is not a serious defect, since it is removable: solder wick lifts it away, with fine-gauge wick appropriate to fine pitch, and a wicking tip does the same job.[186] Reheating between the two shorted pins and drawing the iron out through the middle will also collect the excess.[EjpUYGRXzRQ] On packages with no mask between pads, a bridge formed during reflow is anticipated and simply cleaned up afterwards.[1322] Rework under a camera is materially harder than at the bench, and a practice run before committing to an important board is worthwhile regardless of experience.[186]

## Detection

Small bridges are found visually, often as an incidental observation while inspecting an assembled board.[1511] Under high magnification on a hot air rework job, bridged solder balls between adjacent pads are directly visible.[1659] In diagnosis of a dead board, a stray solder blob is one of the standard suspects for an unexplained short, alongside failed devices and shorted bypass capacitors.[230]

Electrical detection at production scale is what JTAG boundary scan is for. Writing a one to a pin and reading it back detects a short to ground -- a pin that always reads zero is grounded -- and driving one pin while reading another detects a bridge between them, with the combinations chosen according to the board layout.[499]

## Deliberate bridges

Solder bridges are routinely used as a zero-component configuration link. Rows of paired pads on an instrument board, marked with abbreviations for the function they select, are bridged to set a board's address so identical boards can be stacked in a system -- a crude technique, but not an uncommon one.[755] A prototyping arrangement can bring a microcontroller pin to a pad set where it is bridged either high or low, with an optional series resistor and a 0.1 inch header on the same node.[1580] A supply rail run as a loop around the edge of a breakout board with bridge pads along it lets any I/O pin be tied to 3.3 V at will.[1410]

Matrix prototyping boards invert the stripboard convention: pads default to disconnected rather than connected, and any two points are joined with a small solder blob across a gap of a few thousandths of an inch, with traces running vertically, horizontally and diagonally so connections can be made in any direction.[860][922] The result behaves like routing cells in an FPGA fabric.[860][922]

In modification and repair work, pads placed on the top or bottom of a small mod PCB are simply bridged onto the target with solder, a technique on equal footing with castellated edge holes.[1158] Where a track is damaged, scraping back the solder mask and bridging across the break is a legitimate repair, ideally reinforced with adhesive to make the joint mechanically robust.[1727] Bridging individually to each conductor of a damaged flexible connector's traces is possible after scraping the coating off, though only worth attempting when getting the unit running again is essential.[o4S-TkTuHZs]

The deliberate and accidental cases are close enough in appearance that a bridge across a track can be presented, straight-faced, as a manufacturing feature added to increase current handling capacity.[686]
