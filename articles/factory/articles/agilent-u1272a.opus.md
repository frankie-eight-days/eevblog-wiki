# agilent u1272a

The Agilent U1272A is a 4.5-digit handheld true-RMS digital multimeter, later sold under the Keysight name, built as Agilent's direct attack on the Fluke 87 segment of the industrial handheld market.[171][1564] It is a clean-sheet Agilent design rather than a rebadge of the Escort design group's existing products, and it carries an unusually dense feature set for a handheld — AC+DC true RMS, 1,000,000-count ohms resolution, a 50 mV range resolving to 1 µV, dual display, onboard data logging, smart ohms and smart diode modes, and a bundled thermocouple probe.[171][211][406][249] Its measured performance is strong on the fundamentals — DC volts, resistance, current, burden voltage — and weak in two specific places: capacitance below roughly 8 nF, and recovery after an ohms-range overload.[249][252]

## Construction and physical design

The meter weighs just over half a kilogram, making it lighter than the 600 g Fluke 87.[249] It is slightly taller than a Fluke 87 V and essentially the same width at top and bottom, with curved sides that make it look slimmer than its actual footprint.[249] It survives a hard twist test with only slight flex, and is built to take the drops and knocks of industrial use.[249]

One design decision works against that. If the meter falls flat on its face, the impact lands on the range switch, because nothing else stands proud enough to absorb it. The Fluke 87 is shaped so the same fall is taken by the rubber holster and the range switch is never touched.[249]

Internally the construction is tight. The LCD hinges into place on retention hooks with alignment tabs seating into cutouts in the board, so the display cannot shift; the PCB itself is held by a single screw, yet is rigid once the retaining hooks engage.[171] Additional support posts press the board and sandwich it in the case to suppress the vibration modes set up by a drop or by transport.[171] There are apparently O-rings around the input sockets, consistent with the splash- and dust-proofing the design claims over the Fluke 87, and high-voltage isolation is handled with extruded plastic passing through the board.[171] Fusing is two HRC fuses, 440 mA and 11 A.[171] The one point of criticism inside is the flying lead running to the piezo buzzer, when the battery and backlight connections were done properly with spring terminals.[171] Overall the build quality is judged to be roughly on par with Fluke, with the caveat that a completely new design has yet to prove its long-term reliability.[171]

## The power-on firmware fault

Shortly after release the meter exhibited an intermittent fault in which it would lock up on switch-on, and if the range switch was moved slowly between positions it would return nonsense readings and hang.[170][178] The fault was intermittent enough to resist deliberate reproduction for minutes at a time, and initially looked like it might be damage from disassembly.[170] It was not: the same behaviour was widespread in already-shipped units, meaning the defect had been inherent in the product for some time without being isolated and reported.[178]

Agilent traced it to firmware, acknowledged it, and issued a downloadable firmware update within about three weeks, along with a free USB cable — needed to perform the update — offered to owners of the U1272A and the lower model sharing the same defect.[178] The affected units shipped with firmware version 2.0, which the meter reports through a power-on key combination.[249]

## Voltage, resistance and accuracy

Against a precision DC voltage standard the meter reads spot on to the least significant digit at both 10 V and 1 V.[249] Resistance spot checks are similarly good: a 10 kΩ 0.005 % 50 ppm reference reads essentially exactly, and a 1 kΩ 0.01 % 100 ppm reference reads almost to the last digit.[249] A voltage standard paired with a 5.5-digit bench meter is sufficient to verify a meter of this class without a certified cal lab.[374] In later work the U1272A itself serves as the known-good reference against which a drifting sibling meter's 1.8 % error is confirmed.[1564]

The 1,000,000-count ohms resolution is the reason it gets picked for checking decade resistance boxes, where lead resistance is first nulled out and the box is read up to 99.9 MΩ.[211] The 50 mV DC range with 1 µV resolution makes it usable for offset-level work — verifying that a picoammeter input sits at 110 µV rather than the 200 µV limit, or resolving the few-microvolt thermoelectric EMF generated across a wire loop with a temperature differential between its ends.[406][419]

Smart ohms compensates for a DC voltage sitting in series with the resistance under test. With roughly 0.365 V injected in series with a 10 kΩ standard, the ordinary ohms range collapses and reads 6.5 MΩ; smart ohms recovers the correct 10 kΩ while simultaneously displaying the 366 mV it has measured and offset.[249]

## Ohms-range open-circuit voltage

The ohms range presents about 3.2 V open circuit, and it does so even on the kilohms range.[675] That is high enough to forward-bias semiconductor junctions, which matters when tracing circuits in-situ: a meter whose ohms ranges stay under about 0.5 V can probe a live board without turning on the parts around the node, and this one cannot.[675]

## Ohms overload recovery

Applying 240 V mains to the ohms range — a standard input-protection check — does not destroy the meter, which is the primary requirement.[252] But it does not come back cleanly either. After a 10-second application, the reading on a known 10 kΩ resistor is no longer accurate: it climbs steadily away from the true value, reaches a peak, and only then starts heading back down, with full recovery taking possibly many minutes.[252][249] The residual error persists long enough to disturb later measurements in the same session.[249] This behaviour is the single strongest reservation about the meter: surviving the overload is not the same as being trustworthy immediately afterwards.[252][249]

## Capacitance

Capacitance is the meter's weakest function. Resolution is 1 pF, which on paper suggests low-value capacitors are within reach, and the reading is stable when probing.[249] In practice a 39 pF capacitor — measured as 38.5 pF on an LCR meter — produces nothing at all, and a 100 pF capacitor is equally hopeless even with the null disabled.[249]

The failures continue into the region the specification covers. The quoted accuracy is 1 % plus five digits on the 10 nF range; a 1 nF capacitor measured on that range comes out 5 to 7 % out with no offset null applied.[249] Nearer the top of the range the error closes up, and an 8.23 nF capacitor reads within spec.[249] Higher values are mixed: 82.9 nF reads 84.1 nF, a 10 µF ceramic reads about 9.9 µF against 9.27 µF from a 120 Hz LCR meter — far outside the claimed ±1 % plus a few digits on all ranges — while a 6300 µF electrolytic auto-ranges quickly and reads in the right neighbourhood, the residual error being expected given the different test frequency used at that magnitude.[249] The suggestion that these capacitance errors came from probing across an anti-static mat surface does not hold; measuring a capacitor in free air and against the mat gives the same result.[250]

## Current and burden voltage

Low-end current is accurate: a 999.9 nA input reads close to nominal.[249] Burden voltage beats the specification at every point checked — under 30 mV against a claimed 40 mV on the 300 µA range, 0.3 V against a claimed 0.4 V on the 3 mA range, comfortably under the claimed 80 mV on the 30 mA range, and a worst case of 0.66 V at 300 mA against a 1 V claim.[249] An input jack alert warns audibly when leads are plugged into the current jacks in the wrong mode, on both the microamp and amp inputs.[249]

## Frequency, bandwidth and dual display

AC voltage is specified only to 20 kHz at 2 % plus around 20 counts, but the front end goes considerably further: with 1 V RMS applied the response is still usable at 100 kHz and only begins to drop off in the several-hundred-kilohertz region, still showing something at 1 MHz.[249] At a 50 mV RMS level the response holds through 32, 50, 76 and 100 kHz and starts to fall away just past 100 kHz.[249]

The frequency counter works in AC mode, DC mode and current mode, a consequence of the AC+DC true-RMS front end, and is reached from any of those with a single Hz button.[249] Beyond frequency in Hz and kHz it displays pulse width in milliseconds and duty cycle, with an annunciator showing which polarity of pulse is being timed.[249] Against a 1 kHz square wave with a 2.5 V offset and 20 % duty cycle it reports 1 kHz, negative-going pulse width of 0.8 ms, positive of 0.2 ms, and duty cycle tracking correctly from 20 % up to 80 %.[249] Pulse width is not reliable in the presence of a large DC offset: at low offsets it is fine, but at 2.5 V the reading jumps and is inaccurate.[249] The counter claims sensitivity to 1 MHz at 40 mV peak-to-peak and meets it, losing lock only when the input is reduced to just over 25 mV; with 1 V in, it holds to about 1.7 MHz.[249]

The dual display can show frequency alongside AC voltage, or dBm referenced to a value set in the setup menu.[249] A 1 kHz low-pass filter is available on both the millivolt and volt ranges to strip switching noise from a reading.[249] The range of dual-display combinations across the meter's functions is extensive enough to occupy its own section of the manual.[249]

## Other functions

Auto diode mode identifies a working junction, annunciates it as good on the display and shows the forward voltage; reversed leads still produce a reading, flagged negative on the upper display. The good/no-good thresholds are 0.3 V and 0.8 V.[249] A white LED is within the meter's diode-test capability.[249]

The bundled temperature probe resolves to 0.1 °C, though absolute accuracy is only about ±1 °C; delta temperature against a nulled reference is supported.[249] Thermocouple type is one of many setup-menu items, alongside backlight timeout in 1-second increments, the input alert, 4–20 mA current mode, serial communications settings, and reading smoothing.[249]

Trigger hold is the equivalent of Fluke's touch hold, and is one of few implementations of that capability on the market; several trigger modes are provided, with manual and auto triggering also available inside the data logger.[249]

## Data logging

Onboard memory holds 10,000 samples, enough to characterise a large batch of components without a PC in the loop.[216] Three logging modes are selectable from the DLOG entry in the setup menu: triggered, hand, and auto.[216] Hand mode — press a button to store each reading — is the obvious choice for manual component sorting, but the manual reveals it is capped at 100 readings, far short of the meter's total memory.[216] For automated capture the meter connects to a PC over its serial link, and the workflow is essentially the same as with a GPIB bench meter, with the advantage that the interface is one modern computers still have.[216]

## Assessment and service history

The meter's design and construction rank among the best in its class, and no fault can be found with the mechanical execution.[171] The functional criticism is that a great many features were packed in, several of them arrived with problems, and the problems were being worked through after release rather than before it.[249] Where a meter's reading must be trusted absolutely — a life-safety measurement — Dave Jones's position is that the Fluke 87 remains the pick, on the strength of two decades of accumulated confidence and the simple fact that it does not have the U1272A's overload-recovery behaviour.[249] Set against that, the U1272A is fast, accurate and unusually feature-dense for the money.[1564]

The LCD-equipped U1272A is the sibling of the OLED-equipped U1273AX, and the two share a platform.[1564] The family also shares failure modes with the earlier U1253B: at least one U1272A fault turned out to be a known, recurring pattern in these meters rather than a one-off, already documented publicly before the repair was undertaken.[a4Xpsenpd6E]
