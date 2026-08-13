# metal oxide varistor

A metal oxide varistor (MOV) is a voltage-dependent, nonlinear resistor used as a transient suppression device: it presents an open circuit at normal operating voltages and collapses to a low impedance when the voltage across it exceeds its nominal rating, shunting surge energy away from the circuitry it protects.[373] It matters because it is one of the primary devices by which multimeters, power supplies, and other mains-connected equipment absorb high-energy voltage transients — such as the 6–8 kV impulses a CAT III 1000 V meter is designed to survive — fast enough that slower protection elements like PTC thermistors cannot respond in time.[373]

## Operating principle

In its normal state an MOV is completely open circuit and has no effect on the circuit across which it is connected.[373] When the applied voltage exceeds the device's nominal rated voltage, the MOV clamps down very quickly to a low impedance and shunts the surge current through itself, so that only a low voltage appears across the protected downstream circuitry.[373] The response is fast — on the order of microseconds to nanoseconds — which is precisely why MOVs are used where a PTC, which requires time to heat up and rise in resistance, cannot act quickly enough to block a transient.[373][1378]

The schematic symbol is a standard resistor symbol with a small diagonal squiggly line through it, reflecting the hysteresis-like clamping behaviour.[373] Physically, MOVs in instruments are typically round radial disc devices, and they are often large and chunky because disc size relates directly to energy absorption capability.[373]

The clamping action is a threshold phenomenon, not a gradual one. A meter protected by MOVs with an aggregate clamp voltage above the applied voltage can sit on a continuous DC overvoltage indefinitely without the MOVs conducting: a Brymen-based 121GW meter sustained 1200 V DC continuously because the voltage was not enough to trigger its MOV chain into conduction.[YPUJipe8Loo] The same behaviour was measured directly on the BM2257, whose three-MOV string left the meter's 10 MΩ input impedance essentially unchanged (10.02 MΩ) even at 1100–1200 V applied.[rT0g1QmKE5E]

## Ratings and part numbering

MOV voltage ratings are commonly encoded in the part number. A Nippon Chemi-Con device marked 471K is a 470 V nominal part; CNR-brand parts marked 621 and 561 are 620 V and 560 V nominal devices respectively; devices marked 681 correspond to roughly 480 V RMS.[814][rT0g1QmKE5E][1667][1500] The same part carries an energy rating — the failed 471K MOV in a Keysight N8762A supply was a 30 joule device.[814]

## Series stacking

Placing several MOVs in series is standard practice rather than using a single higher-voltage part. Series stacking both increases total energy dissipation capability and increases creepage distance, since the physical gaps of a few millimetres between successive devices add up and prevent arc-over across the package during high-voltage transients.[373] Concrete examples:

- The Fluke 27 uses four 430 V MOVs in series, so it does not begin clamping until the input reaches roughly 1700 V — well above its 1000 V rated measurement range, on the basis that the rest of the input circuitry will survive 1700 V.[373]
- The Brymen BM2257 uses two 620 V devices plus one 560 V device in series, giving a nominal 1800 V clamp, theoretically conducting only above that figure.[rT0g1QmKE5E][1667]
- Multimeter input stages generally clamp below 2 kV; a typical arrangement might be two 900 V MOVs in series clamping at about 1800 V, after which the remaining input protection can handle the residual safely.[1016]
- An electric fence controller used strings of three or six MOVs in series across its output because individually higher-rated parts were not used.[1277]

By contrast, paralleling MOVs is not sensible practice, since matched current sharing cannot be assumed; an apparent second parallel device on one board turned out to be a Y5V ceramic capacitor.[1741]

## Role in multimeter input protection

The canonical multimeter voltage-input protection scheme is a PTC thermistor in series plus MOVs shunting toward the input-jack common (not necessarily the meter's logic ground).[373] The division of labour is temporal: the MOV clamps the transient within microseconds and its resulting low impedance drives a large current that heats the PTC relatively quickly; the PTC then rises into the megaohm range and cuts off current flow, while the MOV has absorbed the pulse energy.[373] Certification testing of CAT-rated meters applies high-energy input transients of various waveforms to verify that the MOVs and the meter survive.[rT0g1QmKE5E] Gas discharge tubes serve the same clamping function as MOVs in some meters, such as Gossen and Hioki designs.[1016][973]

Practical design details observed across instruments include: physical barriers around the MOVs so they cannot arc to nearby components such as the range switch; high-voltage isolation slots coordinated with the clamp level (the Fluke 27's trimmer capacitors are rated 1700 V, matching its four-MOV string); and a direct, low-impedance return path from the MOVs back to the input jack ground for the impulse energy.[373] Multiple protection paths are common where extra taps feed the range switch or ADC, with additional MOVs guarding each path.[373][1667]

The presence, size, and count of MOVs is treated as a baseline indicator of multimeter safety engineering. A properly designed meter is expected to have a PTC, MOVs, a bridge rectifier, and HRC fuses; a meter lacking MOVs is judged not to meet its claimed CAT ratings regardless of labelling, because input resistors and PTCs alone cannot dissipate high-energy impulse energy.[373][712][1016] Larger MOVs absorb more energy before destruction, so physically bigger devices count as better protection, all else equal.[1447]

## Mains and other applications

Beyond multimeters, MOVs appear across mains inputs of power supplies, televisions, UPS units, alarm panels, and chargers, typically ahead of the common-mode choke and bridge rectifier, alongside X/Y-class capacitors and fuses.[790][504][682][764] Two distinct protection topologies are used because there are two distinct fault mechanisms: MOVs connected from each AC line down to mains earth clamp earth-referenced surges, while a separate device across the line pair clamps differential overvoltage; a large differential voltage can exist across the input without stressing the earth-referenced MOVs at all.[682]

MOVs are frequently combined with other devices:

- A gas discharge tube in series with an MOV, as found in a microinverter front end and in a Keysight bench multimeter's clamp-to-earth path (spark gap, MOV, and 100 Ω resistor in series to mains earth).[yOJ7xPugsdc][1382]
- A thermal fuse thermally coupled to the MOV body (heat-shrunk against it) so that if the MOV overheats under sustained conduction the fuse opens before the MOV explodes — used in UPS and appliance designs.[1168][1164]
- MOVs on floating outputs and sense inputs of bench power supplies, referenced to chassis earth rather than to the output common.[512][511]

Multilayer varistors (MLVs) are the surface-mount counterpart: zinc-oxide devices built like ceramic capacitors, available down to 0201 size, that become conductive in the presence of an excessive electric field. Early MLVs wore out because inconsistent grain sizes caused uneven field stress; the failed grains became resistive and then flamed. Modern devices with tight grain-size control do not wear out.[9V99J22aiLE]

## Failure modes

MOVs protect sacrificially. Under a high-energy overload they can blow apart violently — in one case the explosion of a meter's input MOV generated enough internal pressure to blow the range knob clean off — while leaving the rest of the instrument undamaged, which is exactly the intended behaviour.[84] A 400 V-per-phase input applied to a Keysight supply blasted one 470 V MOV apart and sprayed its contents against a heatsink while the fuses and remaining MOVs protected everything downstream.[814] Conversely, if the surge energy is low and fast enough, an MOV absorbs it internally with no external sign of damage and continues to work.[682]

Leakage current is a real but manageable characteristic: MOVs shunted across a meter's 10 MΩ input will leak at high applied voltage, but device selection can keep leakage negligible even at 1200 V, as verified on the BM2257.[rT0g1QmKE5E]

An intact MOV measures as a very high resistance — on the order of several megohms — in-circuit, and a blown one typically reads open after failing; confirming full functionality, however, requires an actual overload test, since a visually undamaged device may be degraded.[682][1424] On repair, a blown MOV should be replaced as a matter of course even though the equipment can function without it, and equipment may be powered under controlled conditions with the MOV removed since it exists purely for protection.[682][814]