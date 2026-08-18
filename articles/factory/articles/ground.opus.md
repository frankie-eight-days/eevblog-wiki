# ground

Ground is the reference point from which every other voltage in a circuit is measured. It is zero volts by definition rather than by physics: the node becomes ground because it has been designated as the reference, and every other potential in the circuit is then expressed relative to it.[HbMnQdRzD8A][820] In practice the same word covers several distinct things — the analytical reference node, the negative rail or return path of a supply, a copper plane on a board, and the earthed metalwork of a chassis or connector shell — and confusion between them is a common source of error.[820][GoKbPDADG0c][202]

## Ground as a reference, not a place

Where a voltage reading lands depends entirely on where the reference lead sits. Moving the black lead of a voltmeter along a stack of batteries changes every measured voltage in the circuit without changing the circuit at all.[HbMnQdRzD8A] Placing the reference in the middle of the stack gives voltages both above and below ground, so that "zero volts is not the absence of voltage" — a node ten volts above the lowest potential and ten volts below the highest is nonetheless zero by definition.[HbMnQdRzD8A] Ground is therefore not necessarily the lowest potential in a system: in a circuit run from a negative rail, ground sits at a higher potential than the −15 V rail, which is what determines the correct polarity for an indicator LED referred to it.[1087]

Choosing the reference badly makes analysis harder without making it wrong. Referencing an op-amp circuit to the bottom of a split supply leaves both inputs sitting at some large positive offset, which is why the reference is conventionally placed in the middle of the supply stack where positive and negative signal excursions fall naturally either side of zero.[HbMnQdRzD8A]

In nodal analysis the choice is explicit: one node is nominated as the reference, marked with the ground symbol, and removed from the set of unknowns, leaving the remaining node voltages to be solved relative to it.[820] A branch that returns directly to the reference node simplifies immediately, since its voltage difference is just the unknown node voltage itself.[820]

## Virtual ground

An op-amp in the inverting configuration has its non-inverting input tied to ground, fixing that input at zero volts regardless of what the circuit does.[HbMnQdRzD8A][600] The amplifier then drives its output to whatever value forces the inverting input to the same potential, so that node also sits at zero volts without being connected to ground at all — a virtual ground.[HbMnQdRzD8A] This explains the result that surprises people probing an inverting stage for the first time: the signal is present on the input side of the input resistor and has apparently vanished on the op-amp side, because that node is being actively held at ground.[600]

A related construction is the rail splitter, which manufactures a mid-supply reference so that a single supply can be treated as a split one, with the created node serving as ground for the signal circuitry.[476]

## Ground in schematics

Ground and VCC are conventionally drawn at fixed positions on a symbol — supply at the top, ground at the bottom — so that pins which are simply tied to one rail or the other can be terminated with a symbol placed right at the pin.[DNlA4X5_S30][952] Placing a ground pin on the wrong side of a symbol forces an extra ground symbol and a wire run across the drawing to reach it, for no benefit.[DNlA4X5_S30] Symbols should also be drawn the right way up and duplicated ground symbols on a single net removed; upside-down ground symbols and redundant duplicates are among the marks of a schematic that has not been laid out with care.[1129]

Many library symbols hide their power and ground pins entirely, so a schematic can pass electrical rules checking with no visible ground or VCC connection anywhere on the sheet; the hidden pins can be revealed by enabling display of all pins.[952] Ground is a power net, and connecting an output pin to it is a hard error that electrical rules checking exists to catch, alongside shorted outputs and floating inputs — the sort of mistake that releases the magic smoke if it reaches hardware.[953][5eJorvyA708]

## Ground planes and PCB layout

On a multilayer board, ground and power planes are treated as equivalent at signal frequencies: "Ground and VCC are effectively the same. The bypass capacitors ensure that."[1193] The consequence for stackup is that signal layers should be pressed as close as possible to their nearest plane, with thin prepregs between the outer signal layers and the planes and the bulk of the thickness put into the inner core.[1193]

Ground routing sometimes drives mechanical decisions. Where a trace cannot be brought around the outside of a board, the shielded metal case of a component can be pressed into service as the ground connection between two points.[GoKbPDADG0c] The exposed thermal pad under a QFN package is normally ground, which means post-reflow inspection includes checking that no signal pin has been bridged to it.[346] Similarly, the tab of a TO-220 regulator is connected to its centre pin, so on a 7805 the tab is at ground and can be screwed directly to a grounded case with no insulating washer; the majority of other cases require the tab to be isolated with a mica washer or sil pad.[744]

Protective structures are referred to ground and belong at the point of entry. A PCB spark gap is placed right at the input connector, running down to ground, so that the impulse energy is dissipated before it can travel down the trace toward the chip.[678] Inside CMOS devices, every I/O pin carries reverse-biased protection diodes to both VCC and the ground pin, conducting only when the input is overdriven beyond the rails.[831]

## Current return paths

Because ground is the return path, it carries real current and obeys Ohm's law like any other conductor, and unaccounted return paths show up as measurement error. A parasitic path to ground alongside the intended one diverts current away from the load: a 2 mA error current returning through such a path represents a 0.2 % error, which is fatal to a design aiming at 0.02 %.[577] Current-sense arrangements make the return explicit, with the low side of the sense resistors carried back to ground so the shunt develops its voltage across a defined path.[812]

Datasheets impose limits on the ground pin itself, not just on individual outputs. A logic device rated at 25 mA per output does not permit four outputs to draw 100 mA simultaneously, because the continuous current through VCC or ground is limited to ±50 mA for the package as a whole.[sr1DOHnJi8I] Output stages are not zero-ohm either: the transistor and resistance between the output pin and ground produce a measurable drop — 0.2 V at 5.2 mA in one case — from which the output resistance can be calculated.[sr1DOHnJi8I]

## Ground as a signal

Pulling a node to ground is itself a control action across many circuits. Digital logic is defined by a chip connected between ground and a supply rail of 5 V, 3.3 V, or lower, with every signal interpreted as one or zero relative to those two references.[7bVnsXHO6Uw] An external trigger input held high by a pull-up is asserted simply by grounding it.[947] A reset pin that is active low is at reset when it sits at ground and running when it is at the rail.[1144] Where a capacitor ties a reset line to ground only during power-on, a mod wire shorting the line permanently to ground holds the part in reset thereafter.[1322] Cutting a jumper on a pin with a pull-down resistor leaves that pin pulled to ground.[1246] In an open-collector driver arrangement, pulling the base node to ground cuts the transistor off entirely, removing it from the circuit.[242]

Ground also serves as the destination for deliberate shunts. The low-impedance mode of a multimeter that operates permanently is implemented by shunting the input path straight down to ground through a PTC element, bypassing the Zener clamping diodes altogether; the measurement is then read from a different path.[1667]

## Finding ground on an unknown board

Identifying ground is usually the first step in reverse engineering a board, and it is normally done by measurement rather than assumption. Pins that all read shorted together are likely ground, but the assumption is verified with a meter before anything is connected.[717] A pin that reads as connected to ground on both the board and the device under test confirms that the two share the same ground, establishing the sanity of the rest of the investigation.[1520] Package pinouts provide the starting hypothesis — VSS or ground and the positive rail located from a datasheet, then cross-checked against the physical part — but package variants shift the numbering, so a QFN version of the same die can have its ground on a different pin from the DIP.[1522][1541][1111][V0RWwSw96Sw][1306]

Assumptions about ground fail often enough to be worth checking every time. On one analog instrument chip, the pin that a conventional pinout would place at ground turned out to be the +15 V input for the internal reference, because the part does not follow the usual conventions.[777] On a multimeter chipset, a pin identified as ground on the basis of a misread silkscreen label proved not to be ground at all, but the common terminal of the chipset, which would have sent a parts search in the wrong direction.[kU7zSSuy9WQ] A pin that measures as floating — not connected to ground and not connected to any semiconductor like its neighbours — is itself diagnostic, in one instance revealing an unconnected LCD contrast pin.[1664]

Connector metalwork is a convenient and reliable ground access point. The shell of an HDMI connector is at ground, as are the outer pins of the socket, leaving the centre pin as the supply.[1279] The shield of a USB connector is connected through to the ground point of the board, which makes it usable as a soldering surface for a decoupling capacitor's ground end.[158] On coaxial connectors, everything outside the centre conductor is ground, and in RF test infrastructure that ground is bonded to mains earth for safety.[430][202] On DC jacks, the centre pin is the positive input and the remaining contacts return to ground.[278] Where a connector is unlabelled, the ground lead is identified by measurement and then marked before use.[1733][992]

## Grounding for measurement

Probe ground return matters as much as the probe tip. Ideally a ground pin and a supply pin sit adjacent on the header so the probe can be connected directly across them with minimal loop.[1733] Where no convenient ground point exists, a header pin soldered to a known ground pin creates one.[1376] Probing a 25 MHz signal calls for a low-inductance probe with a short ground connection to keep the displayed waveform representative of the signal rather than of the probe arrangement.[1288]

Ground connections inside instruments can themselves be shaped for the measurement. In one scopemeter input, the ground of the coaxial input is wrapped in a capacitor that AC-couples the negative input of the BNC through to the internal shielding and signal common.[430]
