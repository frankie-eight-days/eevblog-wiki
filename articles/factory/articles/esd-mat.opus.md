# esd mat

An ESD mat is a bench-surface covering that provides a static-dissipative working surface for electronics assembly and repair, and doubles as the primary work surface of the bench itself.[228][679] It is the blue rubber benchtop material visible across most EEVblog bench work.[228] The critical property is that a dissipative surface does not build up a charge, and that dissipative is not the same as conductive.[228][ddQF9U5CRNA]

## Construction and layers

A typical rubber mat is a laminate: a static-dissipative top surface with a conductive layer beneath it.[679][ddQF9U5CRNA] The distinction matters — the top is dissipative, the bottom conductive, and the mat as a whole is not a conductor.[228][679] Variants exist: an RS Components mat is static dissipative on both outer faces with a conductive inner layer, whereas an older mat is conductive on the bottom face directly.[ddQF9U5CRNA] The two faces of a laminated mat are not interchangeable; the underside is visibly shinier and a different surface, so a faded mat cannot simply be flipped to recover a fresh top.[ddQF9U5CRNA]

Mats ship with press studs — commonly four, one per corner — for snapping on earth leads and wrist straps.[ddQF9U5CRNA][679] A complete bench setup runs an ESD binding point down to mains earth, then out to the mat and to a wrist strap.[51] The path to earth is deliberately resistive rather than a short: a wrist strap reaches mains earth through a couple of megohms, and the mat spreads resistance across its area, so touching an earthed mat pulls a charged body low but not to zero.[1567]

Rubber is the material to buy; PVC mats are not worth having.[679] The rubber type is tear-resistant, heat-resistant, solder-proof, and dissipative all at once.[679]

## Sizes and cost

Mats are sold by the roll and cut to bench depth. Standard depths are 600 mm and 900 mm, with anything else effectively a custom order.[1391] A 10 m roll cost around 300 Australian dollars at the time of one bench build, and 300 to 400 dollars at a later one.[679][ti8mbPIAvbI] Off-cuts are worth keeping: a strip can be fitted with studs and straps to make a portable fieldwork surface, or laid over the main mat as a sacrificial second layer for heavy-duty work.[679]

## Ageing and UV degradation

The dominant failure mode in practice is not wear but colour change. Blue rubber matting installed in a lit lab shifts over a couple of years to a greenish cast, attributed to UV from the bench lighting.[oILC5TsG2_k][ti8mbPIAvbI] The change is in the material, not on it: the discolouration cannot be removed with Windex or other cleaning chemicals, and the affected area is the exposed area — anything left standing on the mat for years, such as a microscope base, leaves behind a patch of the original colour when moved.[oILC5TsG2_k][ti8mbPIAvbI][ddQF9U5CRNA] High-quality matting is not immune; the effect appears across mats generally, with some examples worse than others.[oILC5TsG2_k] Given that the degradation is driven by ambient light, repurchasing the same product is poor value for a lit lab.[ti8mbPIAvbI]

Mat colour also interacts with photography. Camera exposure metering is calibrated to an 18% grey card, so a grey mat rather than a blue one under an inspection microscope removes the exposure problem outright.[ddQF9U5CRNA] Colour varies between suppliers even within nominally the same product — a traditional deep blue against a much lighter blue from a later order.[585] The mat's large flat expanse has also been considered as a seamless photographic backdrop, curved up the wall behind a bench, though bench geometry made the camera placement impractical.[640]

## Grounding, floating mats and 50 Hz pickup

An ungrounded mat is not neutral: left floating, a large conductive-backed sheet under the bench becomes an efficient capacitive coupler and an effective 50 Hz antenna. Sensitive unshielded circuitry sitting on it picks up mains hum that grows as the circuit is brought closer to the mat surface, and connecting the mat to earth removes the pickup almost entirely.[e4wvxWWMla0] Floating mats have been the root cause of spurious measurement behaviour on the bench before, which makes an unplugged mat earth lead a standard suspect when unexplained mains-frequency signals appear.[933][e4wvxWWMla0] The same coupling shows up incidentally in other work — a mains voltage detector stick registers stray 50 Hz from the mat.[VZuebPVrzI8]

Because the mat couples to whatever rests on it, isolating a device under test from the mat is a legitimate diagnostic step: mounting sensitive input circuitry on a wooden frame so nothing touches the mat isolates its contribution.[660] Conversely, the mat serves as a defined reference surface for electrostatic measurement, with a surface DC voltmeter's ground taken to the mat and high-voltage supply references returned to it.[768][247]

Grounding discipline is easy to let slip. A microscope-supplied mat may carry a proper ESD stud and still sit unconnected in normal use.[1361] Equipment such as hot air rework stations ships with a grounding point and strap intended to be run over to the mat and thence to mains earth.[1058]

## In use

The mat is the default surface for whatever happens on the bench, which means it also becomes an uncontrolled variable in ad hoc experiments — dropping cells onto rubber matting to compare their rebound is surface-dependent and not a controlled test.[508] It is soft enough to run wires underneath and bring them up through a drilled hole to a breadboard beneath.[161] Rubber matting sits at the boundary of what counts as a hard surface for small mechanical toys.[541]

Nice matting belongs on the list of lab equipment worth funding ahead of over-specified test gear.[ln_XJDPKJlc] Australian supply has come through Oratec, an importer rather than the manufacturer, which also carries ESD trays and related consumables.[oILC5TsG2_k][1468]
