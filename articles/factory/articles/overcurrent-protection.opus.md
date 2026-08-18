# overcurrent protection

Overcurrent protection (OCP) is the set of mechanisms that detect current above a defined threshold and act on it — by limiting, shutting down, retrying, or physically opening the path — before the excess current destroys the source, the wiring, or the load. It appears at nearly every level of an electronic system: inside regulator and battery-management silicon, as discrete sense resistors and comparators on a board, as a settable trip point on a bench instrument, and as a passive device such as a PTC thermistor in a mains input.[90][e98cYNPUxcg][1541][1691] The stakes are direct: short the load of a voltage source and the source itself heats up and blows up unless something protects it.[1401]

## Overcurrent protection versus current limiting

The two are commonly confused because both respond to the same event. A conventional bench supply that hits its current setting enters constant-current mode and stays there, continuously regulating current down while holding the output alive.[439] Overcurrent protection is the alternative behaviour: instead of dropping into current limiting when the current limit is reached, it switches the output off entirely.[439] On supplies that expose OCP as a separate enable, turning it on converts the current setting from a limit into a trip point — the channel shuts down the moment it goes overcurrent, and shuts down again on any attempt to switch it back on into the same fault.[439]

The trip threshold is also distinct from the ordinary output voltage and current settings, and that separation is the point of it: the protection limits stand above the working setpoints so that someone else adjusting the panel cannot take the output past what the load can survive.[1293] Trip resolution on a mid-range supply can be fine — 1 mA steps on the overcurrent setting of one 3-channel supply.[509]

## Why it is set on the bench

The usual justification is the first power-up of a prototype. Setting overvoltage and overcurrent protection just above the expected operating point means that a bumped knob, a mis-entered value, or another person at the bench trips the supply instead of destroying the board — the difference between a protection event and a dead assembly on a board that may be worth tens of thousands of dollars and carry the entire project schedule.[509][1293] In practice the supply simply switches the output off when the set point is exceeded, and the board survives.[509]

Instruments other than supplies carry the same protection for the same reason. Electronic loads allow a maximum power, maximum current and maximum time to be configured so the device under test cannot be damaged.[862] One programmable load exposes overcurrent protection as an operating mode of its own, running a stepped sequence for testing supplies against power and current.[1023]

A cruder version of the same idea is a resettable trip in place of a fuse: a supply fitted with a red button that pops on excess current and is simply pushed back in once the fault is found, adopted specifically to stop the constant replacement of fuses.[874]

## Hardware versus software implementation

Whether the protection is real hardware or a firmware comparison matters, and on inexpensive equipment it is usually the latter. Overvoltage and overcurrent limits on low-cost bench supplies are typically software protections with no independent hardware crowbar behind them, so a firmware lockup or crash removes the protection entirely — the very failure mode the protection exists to cover.[1265][1030][1606][1691] Higher-end instruments do it in silicon: a precision battery emulator carries hardware overvoltage and overcurrent protection trip and DAC-set threshold circuitry alongside its current monitors, arranged so the protection is done in hardware rather than software.[1550]

Even where the protection is analog, a local processor often owns the loop. In one battery emulator the main applications processor is deliberately kept out of it; a dedicated local processor handles overcurrent and overvoltage protection along with ESR emulation and the constant-power and constant-current modes, for speed, consistency, and separation from the rest of the design.[1550] A high-voltage inverter controller adds microprocessor H-bridge overcurrent protection on top of the protection inherent in the analog design of the bridge, monitoring the current through the switching devices and reducing the commanded output magnitude on detecting an overload to bring the transient currents down.[1170]

## Hiccup mode

A well-behaved switching supply that detects an overcurrent does not simply latch off or blow a fuse — it shuts down, waits, and retries, repeatedly, producing the characteristic hiccup.[1203] A reversed electrolytic capacitor loading a rail beyond its protection current produced exactly that behaviour on a scope repair: the supply hiccupped rather than dying.[1203] The same signature appears in fault diagnosis, where a switching controller that is producing gate drive and seeing input voltage but restarting on a roughly one-second cadence is entering an overvoltage or overcurrent protection hiccup mode — a common behaviour for switching controllers, and one usually documented in the controller data sheet.[1726]

## Protection devices and integrated protection

A PTC thermistor is a self-acting overcurrent protection device. Passing more current through it heats it, and because its resistance rises with temperature, a short or fault drawing excess current downstream causes the PTC to heat and limit the current flow.[e98cYNPUxcg]

Overcurrent protection is also routinely built into the silicon. Linear regulators, LDOs and switching regulators alike carry internal overcurrent, overvoltage and overtemperature protection circuitry — additions that do not change the basic operation of the regulator but make the parts more useful.[90] Lithium cell protection boards implement overvoltage, overcurrent and low-voltage protection together; with all three present, a well-designed protection circuit should make the cell effectively impossible to kill, though it will certainly switch the cell off.[1613] Battery-management and charge-control parts combine overvoltage and overcurrent detection with charge detection and on-die overtemperature protection using an integrated silicon temperature sensor.[1541] Integrated power stages followed the same path: a monolithic half-bridge gained driver, level-shift and protection circuitry in a later generation.[1737]

USB power paths use dedicated hot-swap controllers for the job. One instrument's USB input uses a hot-swap controller with a settable current threshold, a series current shunt and a 12-bit ADC, giving both overcurrent protection and current measurement on the port.[692] Properly designed USB power products negotiate the bus rather than feeding 5 V straight through a buck converter, and provide overcurrent protection in the path as well.[827]

## Other applications

Device programmers use overcurrent detection as a diagnostic rather than only a safety feature: an overcurrent trip on the VPP or VCC rail is reported as an external short circuit, a reversed IC, or a damaged device, and the programmer can self-test the function by deliberately shorting the rail through a transistor to confirm the current limit works.[411] A soldering station's tip current-sense resistor exists to raise an overcurrent error if the tip shorts out.[1106] Automotive body-controller I/O nodes carry overcurrent protection, overvoltage protection and automotive transient protection on every input and output.[1627] An insulation resistance tester driving 2,500 V shut itself down on what appeared to be an overcurrent event during arcing.[468]

Overcurrent protection also bounds measurements. Sweeping a 9 V DC-DC brick rated at 100 mA output, the efficiency curve could be extended only to about 320 mA before the converter's own overcurrent protection kicked in and ended the sweep.[957]

## Interaction with electronic loads

Testing a supply with an electronic load can trip protection on either side, and the two can fight. An electronic load takes time to respond, and when it steps in it sets its output transistors to a very low impedance — effectively a short across the supply's output capacitor. The stored charge dumps into the load and trips the supply's input overcurrent protection.[1298] The load's own overcurrent and overvoltage protections are what make such loads hard to kill under that abuse.[1298]

The reverse coupling produces oscillation. If a load switch-on transient drives the supply briefly into constant-current mode, the load detects the mode change and switches its own mode in response, and the two chase each other until the operating point settles.[1298] The consequence is not confined to the bench: the same current dump that trips the protection is available to be delivered into whatever real product the supply is powering.[1298]
