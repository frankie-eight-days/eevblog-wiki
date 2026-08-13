# led

A light-emitting diode (LED) is a semiconductor diode that emits light when forward current passes through it. It is a current-driven, non-linear device: brightness is controlled by the current through the junction, while the forward voltage drop is a consequence of that current, so an LED must never be connected directly across a low-impedance voltage source without current limiting.[1427][1688][1617] Light output is roughly linearly proportional to current over most of the operating range, even though the current–voltage characteristic is non-linear.[869][1427]

## Electrical characteristics

Forward voltage depends on the LED's material and on the operating current. A typical red LED drops about 2 V at its 20 mA rated point, falling to roughly 1.8 V at 10 mA and about 1.6 V at 1 mA.[1427][1491][708] White LEDs drop around 3 V each, with some high-voltage parts dropping 5 V per die.[661][1700][1423] Because the device is non-linear, the supply must exceed a minimum compliance voltage before any current flows at all: a 1 V, 100 A supply cannot light an LED, while a current source with adequate compliance voltage will.[1617][1455] A string of nine series LEDs measured 45–46 V total drop at 1 mA, and a six-LED architectural strip extinguished below about 15–16 V, a little over 2 V per LED.[1688][1617]

LEDs emit usable light at far below their nominal rating. A standard LED gives reasonable brightness at 1 mA (about 1.6 mW for a red part), and a high-efficiency LED can be visibly lit at 30 µA in room light; emission persists down to extremely small currents, which is the basis of photon-counting experiments probing the turn-on threshold.[708][1455][869] Conversely, the eye's logarithmic response means that halving current from 20 mA to 10 mA produces little apparent brightness change, so running indicator LEDs at full rated current is usually unnecessary.[1427]

## Current limiting and drive circuits

The standard drive is a series "dropper" resistor sized from the rail voltage minus the LED forward voltage, divided by the desired current — for example, 2 V across a 100 Ω resistor gives 20 mA, and a 7.2 V battery driving a 5.6 V LED string at 250 mA needs a resistor dropping 1.6 V.[1427][RT3godBXkOg] For order-of-magnitude work, a 10 V rail with a 1 kΩ to 10 kΩ resistor brackets the usable 1–10 mA range for a standard LED.[286] Where brightness stability matters, a constant-current circuit replaces the resistor; an LM317 with a 2.5 Ω sense resistor makes a 500 mA constant-current source, which shared across 24 LEDs gives about 20.8 mA each.[392][1688]

Placing LEDs directly in parallel is poor practice because they do not share current evenly unless matched at the semiconductor level; a series ballast resistor per branch forces sharing, although same-batch parts are often reasonably matched, and some designs rely on the output on-resistance of driver chips as an incidental ballast.[1491][708][1372] Apparent exceptions such as keychain flashers with an LED straight across a coin cell work only because the battery's internal resistance acts as the series element.[1427] Driving an LED from a low-impedance source with no limiting produces current spikes of hundreds of milliamps that can exceed both the continuous rating (commonly 20 mA) and any pulse rating, drastically shortening LED life.[708][135]

## Failure modes and reliability

Gross overvoltage is destructive: 15 V across a red LED with no current limiting heats the bond wire until it glows, smokes, and fuses.[857] Sustained operation within current ratings (20 mA is safe for virtually any LED; many are rated 30–60 mA) still fails when thermal design is poor — cheap LED products have burned from inadequate board copper and bad FR4 rather than overcurrent.[735] LEDs are also temperature-sensitive during assembly, being notorious for not surviving reflow temperatures, and moisture-sensitive parts ship in sealed bags with desiccant.[415][m9tza_c4sxc]

White LEDs are blue dies with a phosphor conversion coating; with age, heat, and time the phosphor degrades and the output shifts blue, which is why aged LCD backlights develop a blue tint.[OdovWOP7ik4]

## Thermal design and efficacy

High-power LED design is dominated by heat extraction. The thermal path is characterised as a series chain: junction-to-solder-point resistance from the datasheet, then solder-point-to-heatsink resistance measured with a thermocouple, allowing die temperature to be inferred from input power and sink temperature.[361] Metal-core PCBs exist specifically to pull heat out of the back of power LEDs, with thermal conductivity options around 1–2 W/m·K.[1259] A worked example at 35 % wall-plug efficiency puts 1.4 W of waste heat per 2.2 W LED into the sink, 11.2 W for an eight-LED strip.[50]

Efficacy figures differ sharply between bare emitters and finished products: diffused flat ceiling panels deliver about 50 lm/W while the LEDs inside them are around 120 lm/W, the difference being lost in the light-guide and diffusion stack.[361] Retrofit LED tubes have cut consumption from 35–40 W per fluorescent tube to about 17 W, using series-parallel strings presenting roughly 60 V of forward drop.[362] For photography lighting, colour rendering index matters more than raw output; unbranded LEDs have garbage CRI, and name-brand high-CRI strips are required for accurate colour.[1372]

## Optical properties

Typical viewing angle is around 120°, but relative intensity falls by roughly an order of magnitude at the shallow angles at which a driver views a road surface, so daylight-visible marker LEDs need about half a watt each; a Philips Lumileds Rebel amber part is rated at 350 mA (1 W) and the comparable white part at 700 mA (2 W) for rated flux.[632] Even illumination from point sources requires engineered optics: edge-lit displays use a handful of LEDs firing into a diffusion film or light guide to produce shadow-free light across a whole screen, as in the four-LED Kindle frontlight, and compact products route light from right-angle board emitters through light pipes to the front panel.[370][672]

## LEDs as general-purpose circuit elements

The stable forward drop makes an LED useful as a crude voltage reference or offset. A red LED provides about 1.8 V at low current, used to generate the offset in a tracking pre-regulator (with the bonus of acting as a power indicator) and as the fixed-voltage element in a two-transistor constant-current source.[260][301] LEDs turn up as ordinary diodes in unexpected places, such as a calculator using one for its 1.6–1.85 V drop.[1209] An LED paired with a phototransistor forms an optocoupler; where no commercial part meets the isolation requirement, a discrete LED and phototransistor can be faced across a gap as a homebrew coupler.[660][1277] LEDs respond essentially instantly to current, so a microsecond overload pulse that would light an LED invisibly briefly needs a pulse-stretching stage to hold the indication for about a second for the human eye.[471]

## LEDs as light sensors

The effect is reversible: an LED illuminated by external light generates a photocurrent like a photodiode, usable as a crude light sensor or a source for femtoampere-level current measurements, and this photon interaction underlies low-current emission experiments.[1755][869]

## Testing and measurement

Multimeter diode-test mode will light an LED and show its forward drop, but only if the meter's open-circuit test voltage exceeds the LED's threshold; raising the test voltage from 1 V to 5 V is what allows modern white LEDs to be tested.[1636][489] Instruments with low test voltages fail entirely — one LCR tweezer cannot forward-bias even a 1.8 V green LED — while 2 mA of test current is enough to verify individual LEDs populated on a board.[81][1335] Component testers automatically identify anode and cathode on arbitrary pinouts.[f_SdM6sXHD4] SMD LED polarity markings are inconsistent between manufacturers — a notch marking the cathode on one part marks the anode on another — so parts should be physically verified before placement.[415]

## Displays and multiplexing

Seven-segment LED displays come in common-cathode and common-anode variants, which determines whether a logic one or a logic zero turns a segment on.[801][1531] Individual LEDs are cheap enough — about a cent each on a 3,000-piece reel — that discrete LEDs can replace manufactured seven-segment modules, a technique also used historically when 50 discrete LEDs cost less than one display.[298][142] Pin-limited microcontrollers use charlieplexing to drive disproportionately many LEDs, for example 20 individually addressable LEDs from five I/O pins.[556]

Driver-chip current limits dominate multiplexed designs. A shift register rated at 25 mA per output must split that current across every segment it feeds — 40 segments sharing 20 mA get half a milliamp each — so driving many segments simultaneously at outdoor brightness is impossible without per-segment drivers or resistors.[1491] Parts such as the 74HC595 can drive LEDs and small seven-segment displays directly only at modest currents.[1611] Omitting dropper resistors entirely and relying on chip output impedance both limits brightness and raises certification questions about how LED current is being limited at all.[1493]