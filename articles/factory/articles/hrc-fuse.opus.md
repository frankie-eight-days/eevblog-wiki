# hrc fuse

An HRC fuse — high rupture capacity fuse — is a fuse built to interrupt a very large fault current without the fuse body itself failing violently.[373] Instead of a wire in a glass tube, it uses a ceramic body packed with sand or a similar filler that absorbs the arc energy and stops the arc continuing after the element has parted.[373][75][1636] In test and measurement equipment it is the single clearest indicator of whether a design takes gross overload seriously: a multimeter intended for anything beyond low-voltage battery-powered circuits should have HRC fuses, and one without them is not safe for that work.[75]

## Why glass fuses are not equivalent

A glass fuse is essentially a length of fuse wire in a glass envelope.[373] Under a genuine mains fault the tube can blast open and the arc can continue across the gap, so current keeps flowing.[373] The consequence is not a quietly blown fuse but an instrument that vents, arcs and can catch fire.[373][75] The HRC construction is intended to contain that event entirely within the fuse body.[373][lgtooEtk9R4]

The threat model is specific. Connecting the amps jack of a meter across a mains supply puts the instrument across a source with enormous available energy — a 240 V outlet delivering a nominal 2,400 W is capable of far more than that instantaneously — and it is that instantaneous capability, not the steady-state rating, that the fuse has to survive.[373] Meters built for that duty carry fuses rated accordingly; interrupt ratings of 30 kA appear in high-end industrial handhelds.[986]

## Voltage rating

The rupture rating is only half of the specification, and the voltage rating is the half most often overlooked.[1351][MarjYxiudYE] A fuse being an HRC type says nothing on its own: a 250 V rated HRC fuse is materially inferior to a 600 V one, and the better instruments use 1,000 V rated parts.[1351][MarjYxiudYE] Pocket meters have been found carrying 600 mA 250 V fuses, which is not the 600 V or 1,000 V part the enclosure's safety claims would imply.[1351][MarjYxiudYE] The 1,000 V HRC fuses are the ones specified into high-quality multimeters.[929]

## Resistance and burden voltage

HRC fuses are not electrically transparent. They have appreciable resistance — often higher than the current shunt they sit in series with — and that resistance adds directly to the meter's burden voltage.[929] A typical 10 A or 11 A HRC fuse runs on the order of 10 mΩ cold, rising as it heats, which adds roughly another 50 mV on top of the 50 mV developed across a 10 mΩ shunt.[931][853]

The effect is far more pronounced on low-current ranges. In the 121GW the milliamp-jack fuse is about 2 Ω nominal against a shunt of about 1 Ω, so the fuse dominates burden voltage on the 50 mA range.[121] Routing the 500 mA range through the 11 A fuse instead of the milliamp fuse keeps burden voltage on that range very low.[121] Cheap substitutes behave differently for the wrong reason: a 500 mA fast-blow fuse rated at only 250 V measured about 0.3 Ω, roughly a third of the resistance of a properly rated part at a similar current rating.[929]

## Time-current behaviour

An 11 A fuse does not open at 11 A. It takes a considerable time to clear at its rating, which is why some multimeters specify a short-duration overload such as 20 A for around ten seconds without the fuse blowing or the shunt being damaged.[373] At a genuine fault current the clearing is fast — a 50 A fault through an 11 A fuse opens quickly.[373] Time-current curves matter when substituting a non-recommended replacement, though in practice HRC fuses of comparable rating fall in much the same ballpark on the average time versus current curve.[376]

## Scope of protection in a multimeter

The fuses in a multimeter protect only the amps and milliamp ranges.[373] They have nothing to do with protecting the voltage input jacks, which rely on their own protection network.[373] Removing the fuses leaves volts, ohms, capacitance and diode functions working normally; only current measurement stops.[373] Fusing is therefore one element of a front end that also includes input protection resistors and thermistors, MOVs, spark gaps, back-to-back protection diodes, high-voltage isolation slots and blast shields.[373][46][344][75][775]

## Sizes, fitment and access

HRC fuses appear in a full-size format and in smaller 3AG / M205-size ceramic bodies, and meters mix the two — a large HRC for the amps range and a smaller one for milliamps.[RDUn3CoVmuc][99][875] Fitting two full-size HRC fuses alongside four AA cells and an SD card in a compact meter is a real packaging constraint.[RDUn3CoVmuc][ILIO5b1BliE]

Fuse access is a design quality issue in its own right, since fuses are consumables. Good practice puts them behind a dedicated compartment — a sealed rubber boot compressed by the back cover, then an inner cover that pops off to expose the fuses — or behind external screw-in holders, one per range, as on bench meters that provide them.[64][731] The opposite pattern is common and criticised: fuses reachable only by removing the entire case, sometimes six self-tapping screws with O-ring grommets, on meters where a blown fuse is an expected event.[43][417][986][1457]

## Cost and retrofitting

The reason low-cost meters ship with glass fuses is price. Glass fuses are produced for cents each, while HRC fuses run from tens of cents for small sizes to dollars each for large parts from established manufacturers such as Bussmann.[lgtooEtk9R4] Retrofitting a cheap meter with HRC fuses of the same rating works and does deliver higher rupture capacity, so a gross overload is contained rather than blowing the fuse apart.[lgtooEtk9R4] The caveat is that the rest of a cheap meter is unlikely to be designed or tested for gross overloads to the same standard, so the upgrade helps without turning the instrument into a properly rated one.[lgtooEtk9R4]

## Beyond multimeters

HRC fuses are used wherever mains energy enters an instrument, not just at meter input jacks. They appear as dual mains input fuses on bench power supplies, oscilloscope mains input boards alongside MOVs and suppression capacitors, digital mixer power inlets, bench instrument supplies and even reflow oven controllers driving a solid-state relay.[268][790][738][1005][558][745] Television power boards use them in preference to glass parts as well.[725]

Their presence in a class of instrument that does not obviously need them is notable: an 11 A HRC fuse on a CAT II rated bench multimeter is unusual, since rack-mounted system instruments do not normally see the surge overload conditions a handheld meter encounters in the field.[485]

Their absence is equally diagnostic. Oscilloscopes with built-in multimeters have shipped with no fuse protection whatsoever, or with an automotive blade fuse in place of an HRC part, in instruments otherwise carefully isolated — a design that should not be used on mains or high-energy circuits.[1004][1761] Budget meters commonly pair an unfused 10 A input with a small glass fuse on the milliamp and microamp ranges.[75][880]

## Mechanical mounting

Because the fuses are physically large and heavy relative to the rest of a handheld meter, their retention matters under mechanical abuse. In drop testing a handheld industrial meter, one of the HRC fuses came completely out of its holder while the battery cells deformed against their supports and the back plate began to crack.[868]
