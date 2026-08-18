# led current

An LED is a current-driven device: its light output is set by the current through the junction, not by the voltage across it, and a design therefore specifies a target current and arranges a resistor, a regulator or a driver IC to deliver it.[286][1307][204] Over the ordinary operating range the relationship between current and luminous intensity is close to linear, so intensity can be traded against supply current almost proportionally.[708][1427] The practical consequence is that the conventional 20 mA figure attached to indicator LEDs is a maximum rather than an operating point, and most indicator functions are satisfied at a small fraction of it.[286][1427][708]

## Typical operating range

A bog-standard LED will turn on somewhere from about 1 mA and can be run up to roughly 20 mA before it is at risk, with 10 mA a comfortable middle value for calculation purposes.[286] Twenty milliamps is the point normally quoted as the maximum for a small indicator part.[708] At the other end, junk-bin LEDs twenty years old remain perfectly usable at a milliamp or two and even below 1 mA.[708] Backlight films recovered from LCD panels light up acceptably at 1 mA, and remain visible when the drive is reduced to 0.1 mA and lower.[915] A single edge-lit LCD backlight strip lights fully at 10 mA and is still producing light down at 1 mA.[465] Seven-segment and multi-emitter display packages are commonly exercised at 20 mA per segment, at which the individual emitters inside a single segment window are distinguishable.[561]

## The eye versus the meter

Apparent brightness is a poor guide to drive current because the eye compresses the difference. Two LEDs running at half the current of a third can appear equally bright, or even brighter, side by side, which is a property of vision rather than of the devices.[1427] Instrumented measurement of millicandelas or lumens recovers the underlying proportionality with current.[1427] The engineering judgement that follows is that there is no need to run indicator LEDs at 20 mA; the current can generally be halved with no perceptible loss.[1427] Comparison is only meaningful under fixed camera exposure or fixed instrumentation, and under those conditions an LED wound down from 20 mA through 15, 8 and 5 mA to about 1 mA shows far less change than the twenty-to-one current ratio suggests.[708]

The same compression underlies claims made for pulsed "overunity" circuits: LEDs driven at an average of half a milliamp each, out of 12 mA shared across a group, give a perfectly reasonable brightness that is not dramatically dimmer than the same part held at a fixed 20 mA.[708] Measured average current, not asserted current, is the figure that matters in such a comparison.[708]

## Setting the current

Where the LED forward drop is an order of magnitude smaller than the supply, it can be neglected and the series resistor found directly from the remaining voltage and the target current: 10 V across a resistor gives 1 kΩ for 10 mA and 10 kΩ for 1 mA.[286] The full calculation subtracts the LED string voltage from the supply first — a 5.6 V string on a nominal 7.2 V battery leaves 1.6 V across the dropper, from which the resistor follows at the chosen 250 mA.[RT3godBXkOg] Series strings are also used to drive many LEDs from one current: an illumination panel run at 500 mA sits at around 35.5 V across the string.[1373]

Resistor values chosen this way are prime candidates for BOM consolidation, since the exact brightness implied by a calculated 680 Ω for 10 mA is rarely a hard requirement.[1307] Indicator currents can be cut aggressively on the same reasoning: a 1 kΩ resistor with 4.5 V across it passes 4.5 mA, and raising it to 2.2 kΩ brings the current to about 2 mA, which is more than adequate for a 3 mm indicator.[182]

## Driver ICs with programmable current

Some drivers set LED current internally and dispense with dropper resistors altogether, saving component count. The LM3914 bar graph driver has a programmable LED current adjustable from 2 mA up to 30 mA, and operates from single supplies of roughly 3 V to 15 V, so it can run directly from a battery pack.[204] Its LED current is approximately 12.5 times the reference load current set by R1, so R1 is 12.5 divided by the desired LED current — 12.5 / 2 mA giving about 6,250 Ω for a 2 mA target chosen to keep battery drain low.[204] The multiplier of 12.5 is visible on the device's characteristic curve of LED current against reference load current, where 1 mA of reference current yields 12.5 mA of LED current; the relationship is fairly linear though not perfect.[204] With 1.25 V of internal reference across 6,250 Ω the reference current is 200 µA, landing at the bottom of the published curve and near enough to the 2 mA target.[204] In the built circuit other loads on the same node shifted the final value to around 13 kΩ for R1, still giving roughly 2 mA per LED.[204]

## Measuring it

The current through an LED can be inferred from the voltage measured directly across it, which tracks the current and reveals modulation such as the amplitude control of an infrared emitter.[980] A current probe reads the current directly, provided the scope probe is set to ×1 because the probe output is direct, and the probe's data sheet scaling is applied — at 1 V per amp, a 230 mV peak-to-peak trace is 230 mA.[915] A bench current source such as a Keithley 225 sets the current outright, which is the cleanest way to compare brightness at stated currents.[465] Current can also be plotted against time on a scope: in a pulsed inductive driver the LED current does not rise instantly, ramps down over the discharge, and is absent entirely while the inductor is charging.[708]

Where an LED shares a supply with other loads, the standing LED current forms the baseline of the total. In one battery test rig the quiescent reading of 17 mA is entirely LED current, rising to 88 mA once discharge mode engages and varying with how many LEDs are lit.[1653]

## Sharing and non-ideal behaviour

Reasonably matched LEDs in parallel share current roughly equally, so a branch carrying 10 mA against a total of up to about 30 mA is the expected result.[1427] Which pin the current enters and where it flows from determines the drop seen across internal protection structures — an asymmetry of 0.2 V on one path against 0.6 V on another comes down to how much current flows through the LED and its return path.[831] Some failures are current-dependent in a more pathological way: an LED with an internal defect can behave correctly at higher current and latch in that state for a while before switching back.[1087]

The linear intensity-versus-current relationship also does not hold indefinitely. Photon counting on an LED driven in the nanoamp region gives photons per second against LED current that is not linear at all — the output ramps up and then tapers off well below the milliamp range.[869]

## Illumination-level currents

Lighting applications work orders of magnitude above indicator currents. A DIY PCB photography light box is normally run at 500 mA, with 150 mA producing a usably illuminated but dimmer panel.[6ZH2KeplSrs][1373] A magnifying lamp converted to LED was set at 250 mA, about half the brightness of that photography box.[RT3godBXkOg] At these levels the current is limited by the LED rating rather than by visibility, and the drive current becomes the main determinant of dissipation in the series element.[RT3godBXkOg]

In portable equipment driven by a DC-DC converter the LED current may not be accessible for measurement at all, in which case converter efficiency and the actual LED operating point cannot be determined — only the input power, such as the roughly 1.2 W drawn on the high setting of a keychain flashlight.[78]
