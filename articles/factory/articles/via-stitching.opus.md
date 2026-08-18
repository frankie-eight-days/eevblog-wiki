# via stitching

Via stitching is the practice of placing many vias in an array or line to tie copper on different layers of a printed circuit board together — typically ground pours and planes, but also power planes and thermal paths.[1193][384][1216] The point is almost never connectivity for its own sake: a single via already makes the electrical connection. Vias are stitched in numbers because each one in parallel lowers the inductance, impedance and resistance of the path, and because current and heat both need more cross-section than one hole provides.[391][1475][397] It is one of the most visible signatures of a considered layout, and its absence — or its presence in the wrong places — is one of the first things a layout review looks for.[643]

## Lowering ground inductance

The dominant use is grounding. The more vias stitched between a top pour and the plane beneath it, the lower the inductance to ground and power.[1475] On RF and high-speed boards this is the difference between a plane that behaves like a plane and one that does not: heavily stitched ground around each circuit block keeps the ground inductance low enough everywhere that the plane is effectively at DC potential even at RF frequencies.[391] Inductance, not resistance, is the quantity that matters at these frequencies.[391]

The pattern shows up wherever signal integrity is paid for. Board-to-board coax transitions in a 20 GHz spectrum analyser are surrounded by dense via fields to drive the inductance down.[470] A single-ended RF path between filter and balun in a mixed-domain oscilloscope is stitched along its length for low impedance.[587] Multi-layer receiver boards use stitching around the RF sections purely to reduce the impedance of the internal ground layer, which is standard practice in RF systems.[571] Stitching a connector footprint around its full perimeter, top and bottom planes joined, is done for signal integrity and high-frequency performance.[304]

Stitching also buys isolation between adjacent pins. Where an RF part places its input pin, then two ground pins, then its output pin, the ground pins stitched down break the coupling path between input and output and let the whole part be laid out with minimal coupling.[1109] The same idea appears in extreme form on a femtoammeter, where a guard buffer drives guard traces that are themselves via-stitched, forming a guard ring that prevents leakage contamination through the PCB dielectric.[1755]

## Bypass capacitors and return paths

Stitching is the fallback when a bypass capacitor's ground return cannot be made physically short. The ground return of a bypass capacitor should sit as close as possible to the ground pin of the device it decouples; where the parts cannot be flipped or rearranged to achieve that, heavy via stitching can carry the return down instead.[1034] It is a remedy, not a first choice — on a small LDO layout with modest currents, rearranging the capacitors is enough and the stitching is unnecessary.[1034]

The failure case is a bypass capacitor grounded to a pour that is not stitched over to the pour its chip sits on. On a split-ground two-layer board this leaves the return current to find its way back by a long and indirect route, enlarging the loop area and producing substantially more radiated emission than a four-layer board, where the top and bottom copper under the chip flood the area with low-inductance ground and power loop paths.[1176]

## Two-layer boards and EMC

On two-layer designs, stitching is one of the few tools available for controlling emissions. Good practice is to keep ground and power directly on top of each other wherever possible, avoid splitting the ground, and add extra via stitching and flood fills to keep return paths tight.[1176] A well-laid-out two-layer board treated this way can radiate less than a poorly laid-out four-layer board, though four layers with dedicated ground and power planes makes the result much easier to achieve and much harder to get wrong.[1176]

When flood filling a two-layer board, the recommended approach is to pepper the copper with vias throughout.[1176] The caveat is that stitching can occasionally create a loop where none was wanted; in general, though, the more the planes are tied together the better the odds.[1176]

## Board-edge stitching and shielding

A ring of vias around the board perimeter, tying the top and bottom planes together along the edge, contains RF that would otherwise leak out the exposed edge of the stackup and improves EMC performance.[842] Taken to its conclusion this becomes a deliberate Faraday cage — stitching vias all the way around so that nothing escapes.[1193] The technique is used on a wide range of hardware, from six-plus-layer oscilloscope mainboards to interconnect PCBs inside ultrasound probes, where perimeter stitching turns the board into one large ground plane and shields the internal traces between the top and bottom pours.[842][1315] Where a copper tape shield is added over the top anyway, the marginal benefit of a full perimeter cage largely disappears.[1193][1315]

## Current carrying

Vias also serve as conductors. A widely used rule of thumb is roughly half an amp nominal per via.[397][643] A DC-to-DC converter output routed to a connector across a riser board might use a dozen vias on that basis.[397] Larger, heavier-duty vias raise the figure — on the output path of a laboratory power supply, heavy stitching between the negative terminal and the internal copper is reckoned at about an amp per via.[667] Heavy stitching for current appears in high-power hardware generally: plasma television driver boards where connector pins are all commoned through massive stitched fields, and soldering station boards carrying transformer secondary current for a 150 W iron.[446][472]

For a trace carrying serious current on a double-sided board, stitching the two copper layers together does not do much for resistance, since the trace width already sets that; the gain is extra copper and a modest improvement in thermal spreading.[1559] It is reasonable to stitch such a trace as a matter of course, but not to excess — every via displaces copper and reduces the effective surface area of the conductor.[1559]

## Thermal use

Stitching under a thermal pad conducts heat from a package into the ground plane or into copper on the far side of the board, where a heatsink or a large pour can take it.[1322][475] Amplifier ICs with a bottom-side thermal pad rely on the pad, the ground pour and the stitching under it as the primary heat path.[1322] Oscilloscope input amplifiers use the bottom-side ground plane as a heatsink, reached through stitching directly beneath the device's thermal pad.[475] Stitching on a modular controller board serves the same function, moving dissipation between layers and into the ground planes.[686]

Sparse stitching under a dissipating part is a legitimate criticism: four paralleled pass devices in a source measure unit carry less stitching than would be expected for a low thermal impedance path through to the heatsink, though the devices are sufficiently overspecified for it not to matter.[607] Conversely, the absence of any stitching around switching MOSFETs with only small PCB heatsink areas is a reliable indication that the parts are not dissipating much.[1434]

## Practical limits

Stitching costs money. Vias are a real per-hole expense, particularly in high-volume manufacture.[463] It is possible to overdo it: boards exist with solder mask stripped back over vast stitched fields where most of the current is already being handled by the top and bottom traces, so the stitching contributes little.[1298] Beyond a point, adding vias simply removes copper.[1559]

Stitching is also not a substitute for routing discipline. Vias should not be used casually to drop traces onto another layer where signals are length-matched or impedance-controlled — that is a last resort for when space has genuinely run out.[1323]

In layout review, the question asked of a flood-filled ground pour is whether it carries enough stitching to couple the ground across, since an unstitched pour may carry no current at all between two points and simply dead-end.[643] Where a ground path passes through a single via and jumps across to another, a half-amp-per-via budget determines whether that is acceptable; on a low-current design it usually is, though an extra via as a matter of course costs nothing.[643]
