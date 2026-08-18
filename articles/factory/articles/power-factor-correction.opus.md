# power factor correction

Power factor correction (PFC) is circuitry added to a mains-powered product to make the current it draws follow the shape and phase of the mains voltage, so that the apparent power in volt-amps approaches the real power in watts.[1730][1191] Without it, a switch-mode supply presents a badly non-sinusoidal load: the rectifier conducts only at the peaks of the mains waveform and refills the bulk capacitor in short, tall current spikes.[1413] Those spikes carry no extra useful power but do produce real I²R losses in the cabling and in the entire distribution system upstream, right back to the generator.[1413][1730]

## Real, apparent and reactive power

A product whose voltage and current are out of phase, or whose current is distorted, dissipates less real power than the product of RMS volts and RMS amps suggests.[1730] A typical modern oscilloscope with a non-corrected switching supply illustrates the gap directly: measured on a power analyser it drew about 9.1 W of real power against roughly 32 VA apparent.[1191] The same class of measurement on another instrument gave a power factor of 0.55, and elsewhere 0.45 — figures that are entirely normal for an uncorrected product and are not a fault of the instrument.[1413][1730][1191]

The closer power factor falls toward zero, the more current the product takes from the whole upstream delivery chain.[1730] Well-specified equipment therefore states its input rating in VA rather than watts; a mains rating given in watts is a reasonable hint that there is no PFC stage inside.[1730]

## Who actually pays for poor power factor

Residential and most commercial tariffs meter real power in kilowatt-hours, so a domestic user is billed for watts and not for apparent power.[1191][o2NxHu5Bsnk] Correcting the power factor of household loads therefore does not reduce the bill, because no apparent-power meter has been installed.[1191] Industrial supply is different: large sites with heavy motor loads can be billed on apparent power, and the high circulating current forces heavier copper, so power factor correction there is a genuine economic concern.[1191][870][o2NxHu5Bsnk][847]

The cost does not vanish for domestic users, it is simply socialised. If every television had its PFC stage removed, the utility would need greater transmission capacity, larger conductors and more generation to carry the extra current.[1388] Bad power factor is an environmental and infrastructure cost even where it is not a line item on the bill.[1388]

## Passive correction

The classic passive fix is to place reactance of the opposite sign in parallel with the load. A factory full of motors is almost entirely inductive, so capacitance is added in parallel to cancel the phase shift and bring power factor as close to unity as possible.[1730] Power stations and factories accordingly run large capacitor banks for this purpose.[1730][1191] The converse case — a switch-mode supply that looks capacitive — calls for added inductance instead.[1730]

Some correction is inherent rather than added. A supply with only a small amount of input capacitance conducts over more of the mains cycle and therefore has a naturally good power factor; one LED driver of this type measured 0.95 at just over 24 W output.[1253] Controller vendors advertise this as inherent PFC, which achieves the result through the converter topology rather than a dedicated stage, at a cost elsewhere in the design.[1253] A UPS inverter-charger design obtained the same effect by drawing a sinusoidal, undistorted current from the line without any additional control circuitry, using the leakage reactances of the main power transformer together with the H-bridge switching devices.[504]

## Active correction

An active PFC stage sits between the bridge rectifier and the bulk filter capacitor, and is recognisable as a switching element with a choke and a small controller chip in that position.[1388] It is a boost converter in operation: the switch chops current through the inductor, which feeds the main filter capacitor through a diode, shaping the input current to track the mains sinusoid.[1388]

Dedicated controllers for this have existed for decades. A 40 A bench switch-mode supply used a Motorola MC34262 in an eight-pin DIP together with a transformer and a handful of surrounding parts, feeding through a diode into series filter caps with voltage-sharing resistors, behind 3.3 µF 400 V bulk capacitors.[272] Modern LED driver controllers such as the TI TPS92314 fold PFC into an offline primary-side sensing part whose typical application schematic is otherwise near identical to a non-corrected equivalent.[1253]

Because the stage runs at rectified mains potential, its switch is a high-voltage device. In one 100 W-class product the PFC MOSFET was an N-channel part rated 18 A at 500 V with 0.27 Ω nominal on-resistance — arguably over-specified on current for the power involved, though 500 V is about the minimum sane rating on a 240 V mains.[1387] Substituting such a part is comparatively forgiving: matching voltage, current and roughly similar RDS(on) is generally sufficient in a PFC application, whereas the long tail of MOSFET datasheet parameters matters far more in other roles.[1387]

Removing the stage does not stop the product working. Taking the transistor out of a television supply and leaving the inductor and diode as a plain DC path let the set run normally — less efficiently, and with no power factor correction at all.[1388] With the new transistor fitted, standby consumption actually rose to 3.2 W and the corrected standby power factor was still only 0.16, which is typical for low-power products in standby.[1388]

## Where it appears

Active PFC is standard on professional and high-power equipment: a 5100 W, 600 V laboratory supply carried a dedicated PFC board on the primary side behind three bridge rectifiers and a three-phase common-mode choke arrangement,[814] and a variable-frequency AC source was specified with electronic power factor correction alongside its true sinusoidal output.[449] Television and monitor supplies commonly include an active stage behind the common-mode chokes and ahead of the high-voltage DC caps.[eCKRl_Txa18][1657] Lower-cost consumer instruments frequently omit it entirely — one oscilloscope had a common-mode choke at the IEC inlet and no other suppression or power factor correction at all.[384]

The economic threshold has moved sharply. PFC was once used only at 600 W and above; it is now found in 45 W adapters, because controller silicon has become cheap enough that above a certain power level a PFC front end costs less overall than omitting it, the savings in losses paying for the extra parts.[1032] A complete PFC function is available as a single small hybrid for around fifty cents, though a choke and a somewhat larger input filter are still required.[1032] The practical consequence is that almost any current product achieves a power factor of 0.98 or 0.99.[1032] Wide-bandgap devices push this further still: a gallium-nitride PFC board of 2.5 kW fits in a very small form factor at better than 99 % efficiency.[1557]

There are countervailing design reasons to avoid a PFC front end. Distributing 48 V DC internally instead of running a 400 V-plus PFC rail simplifies safety qualification substantially, shortening development time and compliance testing.[1032] Bidirectional supplies for electric-vehicle test can go the other way and regulate power factor digitally to unity while returning energy to the line,[1032] and solid-state transformers can be made unity power factor, or variable if the utility asks for it.[1753]

Regulation is often the driver rather than economics. A good power factor is a plausible requirement for public-sector lighting supply contracts, and LED driver silicon is marketed on high power factor for that reason.[1253][1252] Measured drivers in that class returned power factors of 0.9 and better.[GbADsyp9wM8]

## Mains capacitor boxes

Consumer energy-saving boxes sold as electricity savers are, internally, a single power factor correction capacitor connected straight across active and neutral — in one dissected example a 3 µF part with nothing else of consequence in the enclosure.[1191][847] Parallel capacitance is a real technique against inductive load, and the marketing copy correctly describes energy being interchanged between capacitive and inductive elements.[1191] The kernel of truth is what makes the product saleable.[1191]

It does not follow that the box saves money. On a domestic tariff billed in watts there is nothing to recover, and the device costs money rather than saving it.[1191] Against a load that is already capacitive — which describes most modern switch-mode electronics — adding parallel capacitance makes the power factor worse, not better.[1191] Correction of this kind belongs at industrial scale, where the customer is billed for apparent power and where the capacitor banks are sized to the motor loads they offset.[1191][870][847] Products claiming the same benefit through non-electrical means, such as substances applied to cabling, have no mechanism at all.[870]
