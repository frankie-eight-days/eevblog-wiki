# multilayer ceramic capacitor

The multilayer ceramic capacitor, universally abbreviated MLCC, is the dominant capacitor type in modern electronics, built from many interleaved layers of metal electrode separated by a ceramic dielectric and terminated at two end caps.[162][33] The multilayer construction is what the name describes and what gives the part its volumetric efficiency: a single chip may contain dozens of layers, or a hundred.[1037] Ceramic capacitors are used in enormous quantity for general-purpose duties such as bypassing and filtering, across a whole graded range of dielectrics suited to different purposes.[33] The same construction that makes them cheap and dense also gives them three characteristic weaknesses — capacitance that moves with applied voltage, a piezoelectric response to mechanical shock, and a brittle body that cracks under board stress.

## Construction and manufacture

An MLCC is made by milling ceramic to a controlled particle size and suspending it in a binder until it resembles paint, pouring that onto a stacking mechanism, drying it, applying a liquid metal electrode, then repeating with the next dielectric layer and the opposing electrode until the required capacitance and thickness are reached.[9V99J22aiLE] Modern high-CV ceramic parts work at extreme dimensions: particle sizes on the order of 0.4 micron and dielectric thicknesses around two micron.[9V99J22aiLE] Development work was once far cruder — early single-layer parts were produced by taking MLCC scrap from the edges of wafer starts, grinding it down by hand and metallizing it.[9V99J22aiLE]

The layers being that thin is precisely why high-capacitance parts carry low voltage ratings. A 100 microfarad chip ceramic was once out of reach entirely; when it became available it arrived as an X5R rated at only 6.3 volts, with 10 microfarad parts typically at 10 volts and higher ratings stepping up from 16 volts.[510]

## Miniaturization

Case sizes have shrunk far past the familiar 0603 and 0402.[855][1037] Parts in 0201, 01005 and 008004 are in production, the smallest measuring 0.25 by 0.125 millimetres — roughly the size of a full stop printed on a sheet of paper — with the board mounting area ratio collapsing accordingly, which is the entire point: more capacitance per unit volume of PCB.[1525][349] Handling and placement of parts this small is a genuine manufacturing problem, and inspection effectively requires a microscope.[1525][349]

## Capacitance versus voltage and temperature

Nominal capacitance on an MLCC is a starting point, not a specification of what the part will deliver in circuit. Class 2 dielectrics such as X5R and X7R carry tolerance and temperature-coefficient codes whose lower grades are severe: capacitance change figures of minus 82 percent and minus 56 percent appear in the standard code tables for the V and U characteristics.[33] Applied DC bias makes it worse. Capacitance may rise slightly at small bias and then fall away drastically, with 80 or 90 percent or more of the nominal value lost on general-purpose parts under bias.[626] AC drive level moves it in the other direction, capacitance increasing by 50-odd percent depending on the applied AC voltage.[626] Murata and AVX are notable for characterising and documenting these effects, including publishing capacitance-change-versus-bias-voltage curves in their data.[626]

An MLCC also has a series resonant frequency, visible as a dip in its impedance response and readily measured with a network analyser; it is this resonance that governs the part's usefulness as a bypass element.[1103] Before high-capacitance ceramics existed, the standard technique was to parallel several capacitors of different values so their individual response peaks combined into a broader low-impedance band.[wjMIsM4sDw8]

Where voltage stability and temperature stability matter more than volumetric efficiency, a tantalum polymer is the alternative to a large-value MLCC.[9V99J22aiLE]

## High-voltage parts

Ceramic dielectrics do not scale gracefully to high working voltage. For a supply with a 0 to 50 V output, the rating must clear 50 V with margin — 63 V, 80 V, 100 V or another preferred value.[1035] At those voltages the practical capacitance ceiling drops to something under 10 microfarads and realistically nearer 1 microfarad in a 1206 or slightly larger package; above that the parts become specially manufactured, physically unusual in size, or supplied as stacked arrays in a lead frame.[1035]

## Piezoelectric and microphonic behaviour

The ceramic dielectric is piezoelectric, so an MLCC generates a voltage across its terminals when the board it is mounted on flexes or vibrates.[1743][162] The part functions, in effect, as a piezoelectric microphone: ordinary speech in a room produces measurable, if microvolt-level, signals across small chip ceramics.[1743][855] The effect is bidirectional — driven at a frequency that matches a mechanical mode of the part and its attachment to the PCB, the capacitor vibrates and radiates sound.[1743] This is why a switching converter running at 5 kHz can be audible where the same design at 20 or 30 kHz would not be.[855]

Microphonics are a practical nuisance in oscilloscope front ends, which are filled with MLCCs.[983] A tap on the case, or on the touchscreen, couples mechanically through the chassis into the PCB and appears on the trace; tapping one input channel couples through the BNC and shows up on another.[983] The probe itself contributes, since compensation capacitors sit either in the probe body or in its BNC connector, and tapping a probe can produce an impulse on the order of tens of millivolts per division.[162][983][1743] The high-value, low-voltage parts — a 10 microfarad 10 V ceramic, for instance — use the worst dielectrics and are the most microphonic; manufacturers including Murata offer grades that are more immune.[983]

The effect is a high-impedance phenomenon. The offending capacitor is normally on the input side of the input buffer, where the source impedance is high; place it after a JFET amplifier stage and the low output impedance swamps it out entirely.[983] Loading the input with any significant impedance suppresses it, and with 50 ohm input termination selected the impulse is not observable at all.[983] It matters in real work when probing high-impedance sources with a times-one probe, or when hunting low-level signals near the noise floor in high-resolution mode.[983]

Vibration coupling into MLCCs is not confined to instrumentation. Nearby ceramics in a switching supply have physically destroyed a MEMS oscillator in a compute module, a fault that took considerable effort to trace.[1607] Vibration in switching components — capacitors and inductors alike — measurably affects their behaviour, and there is a long-standing suggestion that switching noise can be reduced by exciting a particular mechanical vibration or subharmonic.[1607]

## Cracking and failure

Ceramic is brittle, and a high-layer-count MLCC depends on tight manufacturing tolerances across all those plates.[1037] Board flex transmits stress into the end caps and cracks the dielectric; the amount required is small, and stress at one end or both is enough.[1037] Cracked parts generally fail short circuit, though open-circuit failure also occurs.[1037][1743] A short across a high-energy source is destructive: dumping even 10 watts into a capacitor makes it smoke and catch fire, which is exactly what happened to a ceramic mounted directly between two screw-terminal pins on a bench supply module, where torquing the terminals imparted the cracking stress.[1036][1037] The manufacturer's interim advice for affected units was simply to remove the capacitor, which served only as extra output filtering; the board was subsequently redesigned, and a later revision of the product used leaded capacitors in that position specifically to avoid stress fracture.[1036][1265]

Thermal stress is the second failure route. A part with one end on a large ground plane and the other not sees an imbalance during reflow, because the copper retains heat and one termination reaches temperature differently from the other.[1037] Hand soldering carries the same risk from the opposite direction: a small chip has almost no thermal mass, so the iron's temperature goes straight into the component, and excess heat can lift the end caps off.[186] Working quickly and at the lowest usable iron temperature is the mitigation.[186]

Board flex in handheld instruments has produced the same class of fault, with MLCCs the prime suspects when components in a flex-prone area of a multimeter fail.[1449]

## Design and layout mitigation

Layout is the first line of defence: keep ceramics away from mechanically stressed regions of the board, including screw terminals and mounting holes where fastener torque couples torsional force into the PCB.[1036] Orientation and placement relative to the flex axis matter as much as the part choice.

Soft-termination parts address the failure directly. A conductive resin layer between the ceramic body and the metal end cap decouples mechanical stress from the dielectric while still conducting, allowing board flex up to 10 mm without damage.[1037] Such parts can still crack, but the crack no longer runs through the ceramic dielectric — the termination may peel slightly while the conductive epoxy maintains the connection — whereas a conventional MLCC under the same flex shows a stress crack straight through the body.[1037] The cost penalty is modest: a 1 microfarad 0402 TDK part with soft termination runs around 2.8 cents in 10,000 quantity.[1037] Parts carrying safety certification equivalent to X1 and Y1 film capacitors for direct mains connection command a much larger premium — volumetric efficiency plus guaranteed reliability and certification is what is being paid for.[1037] All the major manufacturers offer solutions to this problem, which is treated as a significant one across the industry.[1037]

## Related parts

The MLCC construction underlies some parts that are not conventional capacitors. Rechargeable ceramic cells built on the same multilayer process behave as capacitors but, because of the very tight internal tolerances, carry a finite cycle life — around 1,000 recharge cycles — and a working voltage of only 1.6 volts, enough to keep a real-time clock chip alive.[1242] A conventional MLCC has no such cycle limit.[1242]
