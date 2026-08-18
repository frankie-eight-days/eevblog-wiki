# usb power delivery

USB Power Delivery (USB PD) is the negotiation standard that lets a USB-C source and its load agree on a voltage and current far beyond the original 5 V bus, turning a single connector into a general-purpose DC supply for laptops, test instruments, and soldering irons.[1262][1749][1646] The negotiation happens over the CC1 and CC2 configuration pins of the USB-C connector, which run to a dedicated PD controller that settles how much power the host can deliver and how much the load needs.[1262][1561] It is not a set of fixed voltages in the way earlier charging schemes were: a compliant source can be programmed to essentially any voltage up to the compliant limit.[1749]

## The negotiated envelope

The specification's ceiling is 48 V, and a well-behaved programmable supply will accept a request for 48 but reject 49.[1749] At the bottom end it reaches down to 3.3 V, with 3.2 V refused and 2.5 V out of range, and the voltage increment is roughly 20 mV.[1749] The 3.1 revision added the high-voltage tiers — figures in the region of 24, 36 and 48 V — on top of the older fixed steps.[1558]

Current is negotiable too. As well as adjustable voltage, the standard allows the current limit to be set, in what appear to be 50 mA steps, although in practice power banks and bricks that actually expose that capability are essentially absent from the market.[1749] The top of the range is a 240 W cable and supply combination at 5 A and 48 V, carried alongside 80 Gbit/s data on the same cable.[1725]

Below that, the familiar fixed modes dominate real hardware. 100 W is reached as 20 V at 5 A.[1646] A 30 W soldering iron gets there on the 12 V mode at 2.5 A.[1319] Devices routinely negotiate 9 V, 12 V, 15 V, 20 V and 21 V depending on what the sink asks for and what the brick can supply.[1319][1563][1646][1717] An oscilloscope powered over USB-C would light its front-panel LED on 5 V but could not actually run until it had negotiated 15 V.[1563]

## Sink and source silicon

A PD sink is normally built around a dedicated negotiation chip. The RT1716 is a Richtek PD controller in a small BGA whose CC1 and CC2 lines run to the USB-C connector; it does the hardware negotiation, is programmable, and presents an I²C interface.[1262][1561] The CH224 is a USB power delivery fast charging protocol sink controller supporting PD 3.0 and 2.0 plus BC 1.2 negotiation, and can negotiate up to the full 100 W.[1606] Increasingly the function is absorbed into general-purpose parts: the STM32G0 value-line microcontroller integrates USB PD, which removes not just the separate controller but its pull-up resistors and decoupling caps from the bill of materials.[1262][1741]

Negotiation only sets the rails; the downstream converter still constrains what the product can output. A 100 W USB-C bench supply built on a plain buck converter can only produce about 400 mV below whatever PD has negotiated, and cannot exceed the input at all — reaching 30 V out from a 12 V input would require a SEPIC or another buck-boost topology.[1606]

## Implementing it is hard

The engineering judgment that emerges consistently from designing with PD is that the standard is far more work than vendor marketing suggests. A promotional claim that a PD sink can be created in less than ten minutes does not survive contact with the actual silicon.[1262] Searching a microcontroller data sheet for "USB" can return no mention of it at all despite USB PD being a headline feature, and the correct data sheet's dead battery section reads "The content of this section will be provided later."[1262] The reference libraries may have to be requested from the vendor directly, possibly for money.[1262] Manufacturer PD stacks are also large — a 32 KB flash part chosen as ample for PD configuration plus serial and HID comms proved marginal once the vendor library was included.[1262] Vendor libraries can carry undocumented registers, requiring separate spreadsheets from the manufacturer just to document them.[1262]

Dave Jones's summary of the µSupply experience is that PD "implementing it correctly and thoroughly is pretty horrific experience", and that the negotiation swallowed an outsized share of that project's development effort alongside the processor isolation.[1262][1561] The µSupply ended up with two microcontrollers: one on the isolated USB side handling PD negotiation, USB HID and serial comms, and a second running the LCD, keypad and DAC-based supply functions.[1561][1264] Part of the PD code was bit-banged because the controller's I²C pins were shared with the programming interface.[1264] Jones's blunt verdict on the whole family of fast-charge schemes is "Bloody temperamental charge and voltage standards."[1319] He has also noted that PD negotiation is considerably easier now than when that design was started, with better solutions available.[1561]

## Interoperability failures

PD in the field is less uniform than the specification implies. Sources may be rated well below the standard's maximum, so a PD port is no guarantee of high power, and implementations are often buggy and not fully compatible.[1375] Sinks fail in the other direction: an 18 W-only power bank will not deliver more, and there are a lot of 18 W-only packs in circulation, so an iron capable of 30 W on PD silently drops to 18 W and loses thermal recovery performance.[1319] A device may fall back to Quick Charge 2.0 instead of Type-C PD, and refuse to negotiate the higher voltage from a given pack at all.[1319]

A sink that omits the CC pull-down resistors advertises nothing about its capability and will therefore not charge from a USB-C power bank, even though the same device charges happily from a dumb USB-A wall wart.[1704] Cables are a further failure point: a charge-only USB-C cable will pass current but neither data nor PD negotiation.[1558]

## Why it is worth the trouble

Dedicated USB PD test hardware exists to make the negotiation visible — inline meters that display volts, amps and watts, automatically detect which protocols a source supports, and offer trigger modes to force a particular PD contract.[1549][1319] These are how a design's negotiated rail is verified in practice: confirming a soldering station has taken the 21 V mode and is drawing 82 W, or that a scope has settled on 20 V and 56 W.[1646][1717]

The payoff is conversion efficiency and convenience. Powering a laptop directly from a battery station's USB-C output, rather than going out through a 240 V AC inverter and back in through the laptop's own mains brick, eliminates a full stage of conversion loss.[1499] The same reasoning underlies programmable PD adapters that take a single PD brick and derive arbitrary voltages for barrel-jack and terminal-block loads, with keyed connectors so polarity cannot be reversed.[1749]
