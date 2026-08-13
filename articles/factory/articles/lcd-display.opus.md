# lcd display

A liquid crystal display modulates light that is already present rather than emitting its own, which is why it dominates every application where power budget, cost or daylight readability matters: wristwatches, calculators, handheld multimeters, panel meters, and flat-panel televisions.[1044][1636][413] The technology spans an enormous range, from a single-common static segment display costing a dollar or two to a 4K television panel driven by chip-on-flex drivers across its entire edge.[1044][248][915] LCDs displaced plasma in the television market outright, and plasma's poor reliability record helped.[446]

## Operating principle

The basic stack is a front polarizer, a back plane electrode acting as the common terminal, and the liquid crystal fluid itself.[1044] Drive is by electric field between the positive and negative plates, not by current, and that field changes the orientation of the crystals.[1044] With no field applied to a twisted nematic cell, light passes through, reflects off the rear reflector and comes straight back out, so the segment is invisible against the silver background; applying a field lines the crystals up and blocks the light, turning the segment on.[1044] Microchip application note AN658 covers the chemistry and physics in depth.[1044]

Because the cell is capacitive rather than resistive, its current draw is minute, and a monochrome reflective display needs no backlight at all in ordinary room light.[413][1699]

## Static and segment displays

A traditional low-cost reflective static LCD is the simplest form.[1044] A typical three-digit part is a 24-pin device where pin 1 is the common and every remaining pin is a single segment, so one common terminal serves all segments.[248] Not all displays are wired this way — many carry two, three or four commons, and the number of commons is the critical parameter when selecting a driver chip or a microcontroller with a built-in LCD module.[248][298] Segment LCDs also arrive in odd configurations: three-and-a-half digits with a plus/minus indicator and an arrow annunciator, or alphanumeric variants that can display letters and symbols as well as numbers.[248]

Driving these segments requires dedicated LCD driving circuitry; they cannot simply be strobed like an LED display.[248] A design needing one common and 23 segments narrows the microcontroller field considerably, and an ATtiny48-AU meets that requirement at 86 cents in hundreds — cheap enough that once the display and the DC-to-DC converter are excluded, the microcontroller becomes the most expensive part on the board.[298] Some microcontrollers add core-independent LCD animation, so blinking and alternating displays continue autonomously while the core stays in low-power mode.[1539] At the opposite extreme, a level meter built entirely from 74- and 4000-series CMOS logic can drive an LCD with no processor at all.[1258]

## Voltage doubling across an inverter

A five-volt logic supply can produce ten volts peak to peak across an LCD segment without any charge pump. Connecting the display across the input and the output of an inverting gate — an XOR gate and a buffer fed from ordinary 5 V logic, or even an Arduino pin — presents the panel with two square waves in opposite phase, and the difference between them, A minus B, swings 10 V peak to peak.[1046] This is not a theoretical artefact: measured differentially on an oscilloscope at 5 volts per division, the result matches the mathematical A-minus-B function exactly.[1046] The effect is simply a change of reference: nothing is stepped up, but the segment sees double the supply voltage.[1046]

## Character modules

Character modules with a standard chipset and a standard footprint are among the most reusable parts in hobby and small-volume design. A 53 by 20 mm two-line by 16-character module is an industry standard size available from four, five or six manufacturers with identical mounting holes and dimensions, and it uses a standard LCD chipset so existing code works unchanged.[4] An 8 by 2 module of roughly 40 by 35 mm with the standard Hitachi pinout is similarly generic, and the non-backlit version is very thin.[313]

Such a part can function as the seed of an entire product. The MicroWatch calculator watch was built around that 53 by 20 mm module; without it, the project would have been a non-starter, because a custom LCD, custom keypad, custom case and custom band attachment all cost serious money to develop.[11] Hooking an LCD to a microcontroller and a keypad is a couple of hours' work — the hard problem was making the result fit on a wrist.[11]

Interface choice matters at the pin-count level. An I2C module needs only SCL, SDA and a reset line, freeing microcontroller pins that a parallel interface would consume.[232] Graphical modules often offer both: a Newhaven 128 by 64 pixel display supports SPI and a traditional 8-bit parallel interface, the parallel path chosen where transfer speed matters.[8] A 20 by 2 line module was specified over the more common 16 by 2 because the extra characters were needed for status display, and at eight or ten dollars it was the most expensive component in an entire bench power supply — a cost accepted on the principle that a decent display is not optional.[232][240] Where a module carries an RGB backlight, the LEDs should be driven from the microcontroller's own PWM peripheral rather than through the I2C port.[238][232]

## Power consumption

The power case against LED seven-segment displays is decisive. LED segments need at least a couple of milliamps each for usable brightness in a lab or office, and a good grunty 5 mA per segment across a multi-digit display reaches roughly 40 mA, a substantial share of a 3.3 V power budget.[298] A Sharp memory LCD updating at 1 Hz draws about 6 microwatts, roughly 2 microamps at 3 V, and in one battery-powered design the display rather than the Giant Gecko processor dominated total consumption at that level.[413]

Datasheet figures should be verified on the bench: a display specified at 180 microamps measured 600 microamps because the contrast setting left many pixels partially on.[1699] Where a reflective display is specified, a backlight is worth designing in but not worth using in normal operation.[1699] LCD current also matters at the layout level, since the display's own draw adds voltage drop along shared supply traces and eats into an already narrow margin.[1216]

## Selecting and sourcing

Parametric search by digit count and price is the practical selection method, filtering distributor catalogues down from thousands of parts — one search returned 38 candidates in the three to four-and-a-half digit range, sorted by price, with the cheapest a Lumex part at $1.61 each in hundreds against roughly $2 for the next tier.[248][298] Datasheet configuration, particularly the pin table and the common arrangement, must then be checked individually.[248]

For a project centred on its display, the display is chosen first and the product envelope, battery and feature set designed around it.[1703] E-paper is a tempting substitute but is specified for update cycles from tens of seconds to minutes, which rules it out for a timer or stopwatch updating once a second or faster.[1703] The related memory LCD is not e-ink at all: it is essentially an LCD with an individual memory per pixel.[761]

Second sourcing is worth designing for. One eBook reader carried two alternative connector footprints on the same board so that whichever TFT panel was available could be fitted by loading the appropriate connector and moving the ribbon cable.[295] At the panel level, several sizes have become de facto standards — the 070-family 7-inch 800 by 480 panel with a 50-pin flat flex, used widely in Raspberry Pi conversions, appears in low-cost instruments and can be replaced with a generic equivalent right down to the asymmetric bezel.[g2kCBfUa9H0][1492]

## Panels, backlights and diffusion

A modern flat-panel television contains no high-voltage drive circuitry: the panel with its chip-on-flex drivers, a single-sided power supply, and an LED backlight driver.[915] Power draw is correspondingly modest — around 100 W for a 50-inch LCD against roughly 500 W for a plasma of similar size.[915]

The backlight assembly is where much of the technology sits. An LED-backlit panel replaces the cold cathode fluorescent lamp with LED strips plus a stack of diffusion and prism layers that improve brightness, contrast, uniformity and energy efficiency by redirecting off-axis light back into the stack rather than losing it.[465] Earlier notebook screens exhibited visible hot spots and uneven illumination that these layers eliminate.[465] The LCD panel itself forms the entire front surface of a modern set, with no separate protective film over it — a fact that becomes relevant the moment the set is dropped, and one that packaging designers address with foam lattice on the front face only.[465][FUjRmecLGzw]

Above the panel sits the timing control board, which splits and times the video signal coming from the main processor board and feeds the panel over multiway flat flex.[631][781] Some designs place an additional buffer board in the ribbon run to the panel.[630]

## Failure modes and diagnosis

A blank display is a power problem until proven otherwise; the first rule is "thou shalt measure voltages" before suspecting the screen or the microcontroller.[1726] LCD bias supplies are frequently negative or unusual — an Amstrad notepad generates minus 15 V purely for its display — and a failed electrolytic capacitor in that bias rail is a common and easily repaired cause of a dead screen, far more likely from the outset than a failed LCD driver or a failed panel.[385][918]

Symptoms distinguish the display from what drives it. A meter showing all segments lit indicates the processor never booted far enough to send the clear command, not a display fault.[JI4b-7vpIDc] A wrong reading that persists across voltage, millivolt, milliamp and amp ranges is a processor problem rather than an LCD problem.[9s9LXOBknck]

Panel faults are usually terminal. Persistent vertical or horizontal lines that survive a change of input, appear on both halves of a split drive arrangement, and remain after both the T-con and processor boards have been reflowed and every rail measured clean, point to the panel or to its chip-on-flex drivers, and repairing those gives Buckley's chance of success.[781][794][780] A replacement T-con board runs 80 to 100 dollars before shipping, and a replacement panel is generally beyond economical repair.[794][915]

Physical damage is the dominant reason large panels reach the dumpster, and a crack often shows only as a faint impact mark until the set is powered up.[fxEFnCpq_m4][Ia4xB9wk80o][1261] Blunt force with no visible external mark can still destroy a panel.[Ia4xB9wk80o] Connector damage is another route: on one laptop design, liquid ingress carbonized the LCD connector between the pins, with the largest pin carrying about 50 volts of backlight supply — the highest voltage in the machine.[1222]

Old displays fail in ways unrelated to their electronics. A 33-year-old colour laptop panel still boots with every pixel working while the image is ruined by degradation of the polarizing filters, the vinegar syndrome familiar to Macintosh collectors.[W91qP8GpgjM][afwqRu7W8V0] The original Sharp LM64C06P panel, a 640 by 400 passive matrix part, remains available new-old-stock or refurbished at around 220 Australian dollars, with no modern replacement made.[afwqRu7W8V0][W91qP8GpgjM]

## Retrofit and salvage

Replacing a failed CRT with an LCD is a routine upgrade for older test equipment. A commercial retrofit kit for a Tektronix TDS-series scope costs around 350 dollars, against 20 or 30 dollars for a generic 640 by 480 VGA colour LCD complete with driver board — leaving only the mechanical problem of mounting it behind the original bezel.[WHwf26JCUec] The payoff is lighter weight, lower power and better reliability, at the cost of brightness: a retrofitted panel washes out as the brightness control is advanced and is noticeably dimmer than the original tube.[1185][1515]

Salvaged panels are of limited value on their own, since a project will generally call for a specific display rather than whatever came out of the last teardown.[1302] A cracked television is more useful for its LED backlight assembly, which can be stripped of the broken glass and repurposed as a large diffuse light panel — useful, among other things, as a light box for viewing through printed circuit boards.[915][1700]

## Displays in test equipment

Handheld meters are built around their displays: four digits at the low end, five at the higher end, quoted as counts, where the count is the maximum value the reading can reach before the meter must change range and lose a digit.[1636] Ruggedness follows from the panel. A meter rated for a 3 metre drop kept its LCD intact through a 25 metre drop; the failures came from corner-first landings that put the impact directly beside the screen.[868]

OLED alternatives read beautifully indoors but are power hungry and close to useless outdoors, which is why manufacturers continue to offer LCD versions of the same meters — sometimes with reduced functionality.[WDYOSddZwto][894][1564]

Oscilloscope screens are typically 320 by 240 quarter-VGA in the budget bracket with an LED backlight, and 800 by 600 in larger instruments.[kdjpbWLi7UI][480] Vertical viewing angle is a common weakness: graticule visibility can be lost at around 45 degrees from below, a limitation shared across Rigol, Agilent X-series and Tektronix 3000-series instruments alike.[480][704] Panel quality is sometimes explicitly derated in the datasheet — one bench scope's display is specified to permit up to five dead or stuck pixels without being considered a failure, a consumer-grade clause absent from the same manufacturer's higher series.[976]

Safety architecture can also be dictated by the display. In an isolated instrument, isolating a flat panel display is harder than isolating a vacuum fluorescent one, because the LCD must connect directly to the processor over a bus of some 24 lines; moving that processing to ground potential required a new, much narrower protocol to the measurement engine.[1032]
