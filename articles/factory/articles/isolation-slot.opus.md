# isolation slot

An isolation slot is a slot routed clean through a printed circuit board to separate two regions of copper that must not be bridged by a surface discharge.[8blgmbXfDEc][373] Removing the board material removes the creepage path: a high-voltage arc can no longer track across the laminate surface from one side to the other, and instead must jump an air gap or travel the long way around the end of the slot.[468] Slots are one of the small handful of features — alongside HRC fuses, MOVs and PTCs — that separate a properly designed high-energy input protection scheme from a cheap one.[373]

## What the slot does

Solder mask is not an insulator you can rely on at high voltage. A surface discharge will track across mask-covered laminate, then punch through the thin mask to reach copper underneath, so the mask contributes nothing useful to the creepage figure.[1734] A slot removes the surface entirely, which is why it works where extra spacing under mask does not.

Where two slots are placed in a staggered arrangement, creepage between two points has to snake around both of them before it can reach the far side, multiplying the effective path length far beyond the straight-line distance.[468] Slot length is chosen against the clearance standards: a 10 mm slot corresponds under the IEC standard to roughly 8,000 V of real isolation, which is what allows a design to be certified at 1,000 V CAT III with margin in hand.[1119]

## Where slots are used

The most common placements are all boundaries between galvanically separate domains:

- **Under optocouplers**, splitting primary from secondary in a switching supply, with the slot continuing under the feedback path back to the primary side.[360][985][800][612]
- **Under the main switching transformer**, so that the transformer footprint itself does not become the weak point in the primary-to-secondary barrier.[1355][1309]
- **Between the individual pins of a bridge rectifier**, an unusually fine-grained treatment that indicates a layout engineer who understood the requirement.[764][1161]
- **Around opto-isolated digital links**, separating a digital section — DSP, control FPGA — from the analog measurement section it drives.[478]
- **Between multimeter input protection components**, around MOVs, gas discharge tubes, high-voltage input resistors and the input jacks themselves.[1592][1382][1667]
- **Around relays and range switches**, both between coil and contacts and between individual throws of a switch.[1382][731][1083][1723]
- **Between channels** on multi-input instruments, and between a scopemeter's multimeter section and its oscilloscope section.[810][808]

## High-voltage versus leakage slots

Not every slot is there for voltage. A short slot routed under a single component in a precision measurement path serves to block leakage current from one side to the other rather than to prevent arc-over, and can be distinguished from a high-voltage slot by its size and by the voltages involved.[607] The same reasoning applies in an electronic load operating at only 150 V, where slots are present as insurance against transient overvoltage rather than because the working voltage demands them.[1023] Conversely, in a low-impedance power-measurement front end where leakage and creepage are simply not concerns, a large slot may be present without any obvious justification.[1693]

## Mechanical stress isolation

A slot routed around a component serves a second, unrelated purpose: mechanically decoupling the part from board flexure. High-precision voltage references, often in an SO8 package, are frequently surrounded by a slot on all sides so that bending of the board does not couple mechanical stress into the die, where it causes drift and other subtle errors.[1037] The same slot also isolates the reference from thermal expansion of the board.[1037]

## Combination with the enclosure

A slot on its own leaves an air gap that an arc can still cross. The stronger construction moulds a plastic rib into the case that protrudes up through the slot, so the discharge cannot jump straight across but has to climb over the plastic wall and back down, over a much longer path.[1734] The same idea appears in fuse compartment design, where an extended section of the moulded compartment mates with the isolation slot in the board beneath it, giving blast containment as well as arc-over protection between the input side and ground.[173] A Fluke 27 shows the enclosure profile matching the slot shape exactly, physically separating the sections with both the air gap and the moulded plastic barrier.[373]

## Slots versus other approaches

Creepage across the input can also be handled without a slot. Stacking multiple MOVs in series steps the creepage distance up a few millimetres at each device and spreads the surge energy across several parts, which is better than relying on one MOV for both jobs; cutting a slot beneath a single MOV is a workable alternative, but the series arrangement buys additional safety margin without the routing.[373] In the Fluke 27, four 430 V devices in series put the clamping threshold at roughly 1,700 V, well above the rated 1,000 V input range.[373]

Slots are also cheaper to fit than to retrofit. A pocket meter with only a voltage input has few enough constraints that full creepage, clearance and isolation slotting can be accommodated in a small form factor without inflating cost.[1574]

## Absence as a defect

Missing slots are a specific, locatable failure mode rather than a general quality complaint. A 2000 V-rated multimeter built without slots between its high-voltage input paths was driven to 5,000 V and arced over exactly at the predicted weakest gap, breaking through solder mask after tracking across the surface; a slot at that point would have prevented it.[1734] The instrument was engineered adequately for 2,500 V in a one-off test, but with no slots there is no guarantee of consistency across units or in the presence of internal moisture.[1734]

Other observed omissions include a fake USB charger with no isolation slots anywhere and a ruined primary-secondary gap at the optocoupler[388]; a bodged instrument with no slots at all[556]; and three-phase inputs on a solar monitor where the clearance is probably technically sufficient but slots between the phases would be the correct layout choice.[WFVfbu1Xz3A] A 1980s Fluke 37 has slots cut throughout for creepage but not around the input, evidently judged unnecessary there.[1393]

Slotting can also be done inconsistently within one product. A Keysight bench meter places slots around a double-pole double-throw input relay but then routes a trace underneath, relying on the dielectric thickness of the inner layers rather than continuing the slot between the contact pairs.[1382]

## As a quality indicator

Because a slot costs a routing operation and some board area, its presence is read as evidence that the layout was done by someone who understood the safety requirement. Slots between every pin of a bridge rectifier, under every optocoupler, and even around mounting nuts are treated as attention to detail beyond what is strictly required.[764][1161][1309] Their systematic presence across a power supply — under the transformer, under the optos, between earth and the active and neutral sides — is taken as a sign that the supply will be reliable.[360][985] Conversely, a manufacturer known for poor input protection putting a single slot on an otherwise inadequate front end is an anomaly rather than a redesign.[712]
