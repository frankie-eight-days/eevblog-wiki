# electric field

The electric field, usually abbreviated E-field, is the field set up by separated electric charge, and it is one of the two components — the other being the magnetic or H field — that together make up electromagnetic radiation.[694][1176] It matters in practical electronics far beyond physics classes: it is the mechanism by which a MOSFET switches, by which an LCD segment turns dark, by which a capacitor stores energy, and by which one half of a board's radiated emissions escapes.[748][1044][486][1273] Voltage itself is defined in terms of it — voltage is the integral of electric field intensity along a path, which is why the classical definition gives no voltage across a coil, where there is no electric field through the winding.[UStV3zyhgnQ]

## Field control inside semiconductors

The field effect transistor takes its name directly from the effect. With the device off, two depletion layers block conduction from source to drain; applying a positive gate voltage — not a large one, a couple of volts depending on the type — establishes an electric field strong enough to overcome the depletion region barrier, forming a channel between the two heavily doped n-type regions through which electrons flow.[748] The switch is turned on by the field alone, with no gate current required.[748]

Gallium nitride exploits a far more intense field. Because GaN is polar, mechanically straining the crystal generates charge; growing a thin GaN layer on silicon and capping it with a layer that squeezes the surface — aluminium gallium nitride — produces a heterojunction so intense that it generates a "6 megs per centimeter electric field" across a distance of only a few angstroms.[1737] That field pulls electrons to the surface and confines them so tightly that they behave quantum mechanically, forming a unified electron gas.[1737]

Cell geometry in power devices is a field-management problem. Hexagonal cells, with every internal angle at 120 degrees, let the depletion regions meet exactly in the middle, giving the lowest possible peak electric field.[1737] Aligned square cells leave a hole in the middle that becomes a high-field point and causes premature breakdown; offset squares retain 90-degree angles whose curvature lowers the breakdown voltage.[1737] Radiation hardness is a related concern: a device designed correctly does not respond to a charged particle passing through it with a spike in the electric field capable of destroying it.[1737]

## Capacitors and dielectrics

Charging a capacitor builds equal and opposite charges on its two plates and sets up an electric field in the dielectric between them.[486] No electrons cross the dielectric — as far as conduction goes it behaves like an open switch — yet current measurably enters one terminal and leaves the other.[486] The resolution is that the changing electric field between the plates creates a changing magnetic field, and that gives the displacement current its equivalent through the dielectric.[486] On the conductor side, ordinary current language works fine; once inside the insulator the correct description is changing electric fields creating changing magnetic fields, with energy stored and transferred in those fields, and it all falls out of Maxwell's equations.[486]

For everyday design work the useful abstraction is the simpler one: treating current as flowing through the capacitor is easier from a design point of view in every practical aspect, even though the physical reality is charge accumulating on the plates and a field between them.[ItoRt1buLkM]

Field strength distribution also sets a floor on how small a ceramic capacitor can shrink. The dielectric is barium titanate, a granular structure, and between the electrodes the grains stack up; the design goal is to have some number of grains in the stack so the electric field is divided across each grain, so that one grain failing does not fail the part.[9V99J22aiLE]

## Displays

Liquid crystal displays are electric-field devices, not current devices. In a twisted nematic LCD the liquid crystal fluid sits between top and bottom electrodes and is affected by the field between them — essentially not a current, just an electric field between the positive and negative plates — which changes the orientation of the crystals.[1044] Applying a field across an individual red, green or blue element turns the polarization of light through that element on or off, so the colour filter behind it either passes or blocks light; three such elements make one pixel.[465]

Because the drive is a field rather than a current, an LCD has essentially no static power consumption, with the switching capacitance accounting for nearly all of it.[1670] The corresponding side effect is that the extremely high impedance of the panel lets stray charge persist: rubbing a finger along a disconnected LCD raises segments that then stay lit, because the charge simply remains on the glass and the field holds them.[1670]

## Radiated emissions and EMC

Which of the two fields dominates a given emission depends on the source impedance. Low-impedance, high-current sources — heavy switching currents in a trace, or fast switching dumping energy into bypass capacitors and interplane capacitance — generate predominantly magnetic field.[1273] High-impedance sources that pass little current generate electric fields; a static 5 V power supply rail is an example.[1273] The rule of thumb follows: at high voltage and low current the E-field dominates and an E-field probe is the right instrument, while high-current nodes call for H-field work.[694] In the near field the H field presents a very low source impedance and the E field a very high one, with the boundary between near and far field set by wavelength, at lambda over 2 pi.[1273]

In the far field the two are locked together. The standard picture shows the electric field oscillating along one axis and the H field at 90 degrees to it, the two propagating together; at a sufficient distance in wavelengths they combine into the electromagnetic radiation that a test house measures during EMC compliance testing.[1176][1193] Board layout determines the mix: large loop areas that cannot be avoided across a big multi-chip board radiate mostly magnetic field with an electric field component as well, and whether a given structure emits E, H, or combined field depends on source and load impedance, frequency, bypassing and capacitive loading.[1176]

## Electrostatics and ESD

Charge on a non-conductor produces a field, and that field induces charge on the nearest conductor — only on a conductor, since a non-conductor will not take an induced charge.[BUW6h88weXU] The chain runs from a charged shoe sole to the skin of the wearer to whatever conductive surface is next in line.[BUW6h88weXU]

That chain is measurable. Once a plate is charged, the electric field at a distance can be measured, and surface DC voltmeters that do exactly this are commonplace instruments, calibrated for a specific standoff such as 1 kV at one inch.[1567] Wireless body-voltage monitors work through the same sequence — electric field to charge density to total charge to voltage — which is how a body voltage reading is obtained without a wire to the wearer.[1567] The relationship breaks down in a few scenarios: standing next to a grounded workstation or wall makes the charge distribution on the body asymmetric, so the reported voltage runs slightly high or low.[1567]

## Sensing and unintended pickup

Non-contact voltage detection is E-field pickup. In a socket tester the sensing element is a bare strip of copper along the top edge of the board acting as an antenna for the electric field.[1598] The same coupling appears as an interference mechanism: 50 Hz pickup on relay contacts inside an oscilloscope is an electric field problem rather than a magnetic one, which is why magnetic shielding tape over the relays does not fix it and a metal can does.[e4wvxWWMla0]

Piezoelectric ceramic bender transducers work the field in both directions — they bend when acoustic pressure is applied and equally bend when an electric field is applied across them, behaving electrically as a capacitor.[1400] At the other end of the scale, beam position monitors and related pickups placed inside a synchrotron beamline detect the electric and magnetic fields produced by the electron beam itself.[836]

## Fields as the carrier of energy

Maxwell's realization was that light consists of oscillating electric and magnetic fields, perpendicular to each other and in phase, so that when one is at maximum so is the other.[1439] Poynting's vector, derived from conservation of energy, applies wherever electric and magnetic fields coincide, giving a flow of energy that can be calculated.[1439] A battery alone has an electric field but no magnetic field because no charges move, so it loses no energy; connected into a circuit, its electric field extends through the circuit at the speed of light.[1439] Surface charge on the conductors creates an electric field outside the wires while the current inside creates a magnetic field outside them, and the combination in the surrounding space carries the energy — the fields, not the electrons, which barely move at all.[1439]

None of this is new material for engineers, who are taught drift velocity, Maxwell's equations and the Poynting vector as a matter of course.[1439] The field-propagation description is not wrong, but it is of little use to a practising design engineer: no working engineer reasons about energy transport as the propagation of electric fields.[ItoRt1buLkM] The exception is at the PCB level, where dielectrics, transmission line behaviour and energy in the dielectric genuinely start to matter.[ItoRt1buLkM]
