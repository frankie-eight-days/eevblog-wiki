# electrical current

Electrical current is the flow of charge — in a conductor, the motion of electrons — and it is one of the two quantities, alongside voltage, that every practical electrical measurement and calculation reduces to.[486][yQ7_A4Cr9ak] It is measured in amperes, with milliamps and microamps used for the small signals that dominate ordinary electronics.[1636] Current is what actually does the work and the damage: it is what heats a resistor, melts a wire, kills a person, and sets the copper cross-section of every cable in a system.[191][1219][yQ7_A4Cr9ak][472]

## Definition and scale

The conventional description of current is the flow of charge and electrons, and electrons cannot pass through an insulator such as the dielectric of a capacitor.[486] The numbers involved are enormous: one amp corresponds to roughly 6 × 10^18 electrons per second, which is why energy-harvesting claims quoted in thousands of electrons per second amount to nothing usable.[1333]

Introductory treatments almost universally reach for the water analogy — current as flow through a pipe, resistance as a restriction — before introducing charge and electrons at all.[WXJP_CNYt3o][yQ7_A4Cr9ak] Voltage and current are not alternatives to one another: it is the current that kills, but voltage is required to push that current through the body in the first place.[yQ7_A4Cr9ak] Electronics as a discipline is conventionally defined as the study of the motion of electric current in a circuit and the means of controlling it.[1179][WXJP_CNYt3o] The transistor is the archetype of that control, since a voltage or current applied to one pair of terminals controls the current through another pair.[hZnlDIvdabQ]

## Conduction current and displacement current

There are two distinct types of current under the single word. The first is electric current proper, the flow of charge and electrons through a conductor.[486] The second is displacement current, the concept Maxwell introduced to make the equations work through a capacitor, where no electrons cross the dielectric yet current enters one terminal and leaves the other.[486] In practical electronics the term current is used as an umbrella covering both.[486]

The boundary between the two is the conductor surface. On the wire and the capacitor plate, ordinary electric current is the correct description and the arithmetic behaves. Once inside the insulating dielectric, the description must switch to changing electric fields producing changing magnetic fields, with energy stored and transferred in those fields.[486]

## Kirchhoff's current law

The sum of the currents into a junction equals the sum of the currents out of it: "Current in must equal current out."[819] That is the entirety of the law, and it is a statement of conservation of charge in the same sense that conservation of energy is a fundamental law of physics — charge put into a loop must come out.[819]

In use, currents flowing into a junction are defined as positive and currents flowing out as negative, which lets any junction be written as a single summed equation regardless of how many branches meet there.[819] A junction with one current in and two paths out gives I1 = I2 + I3.[819] The law holds even in the trivial case of one current in and one out.[819]

The principle is directly measurable. With 283 double adapters chained in series feeding a 2 kW load, the current entering the chain measured 7.31 amps and the current leaving it measured 7.319 amps — the same figure within measurement error, despite the substantial voltage drop accumulated across the adapters.[1526]

## Current, power and heat

Power is voltage times current, which is what converts a transmission-line specification into an ampere figure: 1.21 gigawatts delivered at 500 kilovolts requires about 2420 amps, and that current then sets the required conductor cross-section against the cable's resistance.[AWYuyf3ILLk]

Power dissipated in a load is I²R, and the squared term is what makes maximum power transfer counterintuitive.[1401] Maximum *current* into a load is obtained by shorting the load — resistance to zero — but that condition dissipates all the power in the source's own internal resistance, heating and potentially destroying the source unless it is protected.[1401] Maximum *power* in the load occurs instead at a sweet spot where load resistance matches source resistance.[1401]

Heating by current is the mechanism behind several practical effects. A resistor carrying enough current will melt fishing line wrapped around it; the same result is obtainable at lower current, simply taking longer to generate the heat.[191] A battery pack shorted by chafed wiring inside a toy delivered enough current to melt the wiring insulation and the body of the switch itself.[1219] Conversely, the absence of heating is diagnostic: thermal imaging of a connector showed two wires at around 40 °C while an adjacent wire carrying little or no current showed no hot spot at all.[401]

Current-carrying capacity drives layout. A soldering station handling the output of a 150-watt iron uses heavy via stitching from the transformer taps and a flat flex cable with unusually thick copper, specified for high current rather than ordinary signal use.[472]

## Typical magnitudes

Indicator LEDs sit in the single-digit milliamp range: a 4.5-volt drop across a 1 k dropper resistor gives 4.5 milliamps, considered high for a circuit running from a 9-volt battery, and raising the resistor to 2k2 brings it down to about 2 milliamps.[182] Three matched LEDs sharing a supply through one resistor drew roughly 10 milliamps each for around 30 milliamps total.[1427] A battery-powered LED strap light drew about 25 milliamps on its low setting and 1.37 amps at full brightness, 7 watts.[1010]

Instruments and appliances occupy the hundreds-of-milliamps to low-amps range: an oscilloscope drawing 54.3 watts at 247 volts mains pulled about 256 milliamps at a power factor near 0.86,[164] a domestic air conditioner unit around one amp,[XD5Emhqd5Ks] and a vintage calculator's supply about 2.4 amps, of which 1.1 amps went to the gas plasma display alone at a nominal 6 volts.[663]

High-current rails inside equipment can reach eight to ten amps on a single supply shared across four ASICs; measuring the drop from about 10 amps to 8.8 amps after removing one device confirmed that the fault current was distributed roughly equally between them rather than concentrated in one.[405] Domestic high-power loads are larger still: 7 kW at 240 volts is about 32 amps, the same order as an electric vehicle charger drawing up to 29 amps through 6 mm² copper.[pXtSybs9QRs][1437]

At the other extreme, a non-contact voltage detector works on a genuinely minute current, capacitively coupled through perhaps 0.1 picofarads between the wire under test and the user's hand, and thence to ground — enough to be detected only because the sensing input is high impedance.[1003]

## Frequency and safety

Current magnitude alone does not determine hazard; frequency and path matter. A handheld Tesla coil operating at about 40,000 volts and roughly one megahertz produces only a small current, and at that frequency the current tends to travel across the skin rather than through the body, so it stings without being lethal.[yQ7_A4Cr9ak] Air and other insulators break down at roughly 20,000 volts per centimetre depending on humidity, which is why such a coil arcs several centimetres.[yQ7_A4Cr9ak]

Mains distribution presents the real danger. Australian power points supply about 10 amps at a voltage high enough to be lethal on contact unless a residual current safety switch is fitted; lower-voltage, higher-current distribution shifts the dominant failure mode from electrocution toward fires.[yQ7_A4Cr9ak]

## Current in pseudoscience

Current is a frequent vehicle for electrical pseudoscience, typically by asserting that some treatment makes electron flow "smoother" so that appliances no longer draw additional current to compensate for losses.[870] Such claims lean on the garden hose analogy — losses as holes in a leaking hose — and pad themselves with a list of real-sounding loss mechanisms such as heat loss, resistance, harmonic distortion, reactive power and electromagnetic interference, none of which the product acts on.[870] A related genre reconstructs physics wholesale, asserting that every atom and particle is a small electric current and that the material universe is made only of electric current.[78JC_p9DiJM] These are not competing theories but word salad wrapped around correct-sounding vocabulary.[870][78JC_p9DiJM]
