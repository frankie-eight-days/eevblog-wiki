# quiescent current

Quiescent current is the current a circuit or device consumes to perform its own function, independent of whatever it delivers to a load.[1285] In a three-terminal linear regulator it is the small current that flows in the input pin and out the ground pin rather than to the output, so by Kirchhoff's current law the input current equals the quiescent current plus the output current.[1285] It matters because it is the floor on consumption: a load can be switched off or reduced to nothing, but quiescent current is paid continuously, which makes it the dominant term in battery life, standby power and micropower design.[1533][971]

## Definition and the current-law view

A regulator has only three legs, so any current entering it must leave either through the output pin or through the ground pin; the ground-pin share is the little bit the regulator itself needs to do its job.[1285] With a capacitive load only, the output capacitor is an open circuit at DC, so the output current equals the load current and nothing flows into the cap.[1285] That gives the arithmetic directly: with a 50 microamp load and a 7.5 microamp quiescent current, the input draw is 57.5 microamps, with a worst case of perhaps 70 microamps.[1285]

The same idea extends to whole products. A circuit's quiescent current is what it draws with no load or with its output disabled, and it appears as a fixed baseline on top of which the load current sits.[259][577] In pulsed systems the baseline is literal: a GSM handset shows a quiescent level with bursts of transmit current superimposed on it at a fixed repetition rate of 217 Hz.[23]

## Reading it from a data sheet

Quiescent current is voltage- and temperature-dependent in ways the headline number hides. A regulator specified at 7.5 microamps typical may be as high as 14 microamps maximum, that maximum being the figure over the full temperature range.[1285] Parameters can also vary with the selected output voltage, so the correct table must be used: the same part reads 7.5 microamps in the 3.3 V table but 18 microamps typical and 22 microamps maximum in the 15 V table.[1285] Where an internal constant current source sets the bias, quiescent current stays essentially flat across the input voltage range rather than rising with input voltage.[1285]

Some manufacturers split the specification in two. Quiescent current is then quoted for an output current of precisely zero — a no-load figure only — while a separate ground current parameter covers the loaded case, for instance 25 microamps for output currents up to 10 milliamps.[1285] Technically the loaded ground current is the number a designer should use.[1285] Notes attached to these tables carry real content and should be read: they cover heat sinking, safe operating area, and the fact that line and load regulation figures may exclude self-heating, which matters when a part with meaningful quiescent current runs from a 40 V input.[1285][500]

Data sheets are not static documents. A revision of the NE5532 removed a long list of parameters from the spec table while lowering the supply current from 8 milliamps to 6 milliamps.[1752]

## When it can be ignored

The practical test is orders of magnitude. A linear regulator's quiescent current sits in the microamp region while a multimeter's load sits in the milliamp region, and as a rule of thumb anything more than two orders of magnitude below the quantity of interest can be ruled out — that is a 1% error, which does not matter, and anything lower is simply insignificant.[1533] This tolerance is what makes back-of-envelope design by inspection robust: a data-sheet figure that turns out to be double the assumed value changes nothing when it is still three orders of magnitude below the competing term.[1285] In engineering terms 100 microamps against an assumed 500 microamps is near enough, because the comparison is being made in decades, not percentages.[1285]

## Zener shunt regulation versus linear regulators

The classic demonstration of quiescent current as a design driver is the Zener shunt regulator. Even with no load current at all, a Zener regulating 5.1 V can be throwing away 50 to 70 milliamps purely to hold the rail, which makes it very inefficient at low currents and hopeless as a general voltage regulator driving no load.[908] A 7805 regulates the same 5 V while taking a negligible quiescent current by comparison.[908] Against a micropower linear regulator the gap is a factor of a thousand: 80 milliamps for the Zener circuit against 80 microamps for the regulator.[1285] Experienced practice has long held Zener shunt circuits to be wasteful, and designers moved to linear regulators as soon as they became available; the remaining reason to use a Zener is that it is cheap.[1285]

## Minimum load current: the related trap

Quiescent current has a counterpart that catches designers of low-power circuits. The LM317 requires a minimum load current of 3.5 milliamps to maintain regulation, which is its entire job.[1438] The 78xx series has no minimum load current requirement but a higher quiescent current instead, so the two families end up in the same place for low-power work — neither is suitable for micropower circuits.[1438] Minimum load current specifications themselves carry conditions: half a milliamp may be specified only at an input range of 10 V, rising to 1 milliamp above that, with the detail buried in a note.[222] Among jellybean regulators, quiescent currents around 4 milliamps typical with a 6 milliamp maximum are common, which rules them out for low-power applications.[1438]

Modern parts do far better. A sub-cent SOT-23 LDO specifies 25 microamps of quiescent current — tens of microamps in practice — while still supplying 250 milliamps with 0.2 V of dropout at 90 mA output, so at a 100 mA load the input current effectively equals the output current.[1147] Energy-harvesting parts go lower still: 950 nanoamps quiescent with no load on the output, and 450 nanoamps input quiescent current in ultra-low-voltage lockout mode, over a 2.7 to 20 V input range with up to 100 milliamps of output.[534]

## Quiescent current as dissipation

Quiescent current is dissipated as heat inside the part, and at high supply voltages that dissipation is not trivial. A device with roughly 10 milliamps of quiescent current running from a 30 V supply dissipates 0.3 watts before it does any work at all, which is significant for a DIP-8 package.[593] Confirming that op-amps draw their data-sheet quiescent values is a standard step when hunting for an unexplained hot spot on a board.[593]

## Switching converters and light-load modes

Switching converters carry their own quiescent penalty, which becomes dominant at light loads because it is paid regardless of output and is then compounded by conversion efficiency. A typical boost converter might specify 300 microamps of active quiescent current, on top of which the efficiency — perhaps 70 to 80% in real use rather than the headline 90% — further erodes what reaches the load, a combination that makes such converters a poor fit for low-current products.[751] Device quiescent current is accordingly one of the first parameters checked when selecting a DC-DC converter.[139]

Charge pumps and switchers address this with light-load modes. The LM2776 uses PFM, or pulse-skipping, operation to minimise quiescent current at light load, allowing the charge pump to switch less when the output current is below 40 milliamps.[1115] The mode change is visible as a step in output ripple at the transition, since the device is changing switching frequency rather than merely reducing it.[1115] Older single-mode parts such as the 7660 have no such mode; output ripple simply tracks output current, and part-to-part variation between vendors shows up as differences in quiescent current and efficiency.[1115]

## Bench measurement

Quiescent current is measured with the load disconnected or the output disabled, and it is a fast diagnostic. On an unfamiliar or repaired supply the first check is for gross excess current faults: 90 milliamps for the standby draw of an old-school linear supply board is unremarkable, and the measurement is used to decide whether to proceed rather than to characterise anything.[663] The inverse case is a fault found by this method — a carbonised PCB that formed a low-impedance path across the output, measuring tens of kilohms before the failure and 47 ohms afterward, drew enough quiescent current to trip a current-limited source into hiccup.[1036] A functioning supply of the same type draws about 2 watts quiescent.[1036]

The no-load draw of a switching supply module can differ between output-off and output-on states even with nothing connected — 0.39 W with the output off against about 0.5 W with it on — so the output-on figure is the one that belongs in an efficiency calculation.[1031] The output-off figure represents the module's own electronics and does not change with the programmed output voltage.[1031] Larger bench supplies show the same fixed overhead: 940 milliwatts quiescent for a 360 W supply, and around 15 to 20 milliamps for a linear-plus-switching design including its LCD and microcontroller.[1265][259]

Typical measured values across instruments and modules span several decades: 2.8 microamps for a low-power handheld multimeter,[1704] 1.3 milliamps in normal operation and about 1 milliamp in DC volts for a Fluke 117, rising to 20 milliamps with the backlight on — currents low enough against a roughly 800 mAh alkaline cell to comfortably meet a 400-hour battery life claim.[60] A DIN-rail supply draws 2 mA at 9 V input including its indicator LED, falling to 1.1 mA at 48 V.[1656] An electropermanent magnet driver idles at about 27 mA even though its coil takes no power.[1656] A boost module shows 4.6 mA at 12 V input with no load,[1710] an electric fence controller 14 mA,[1277] a precision current source circuit about 4 mA,[577] and a 1980s boombox around 70 mA — though with a genuine mechanical power switch, off means off.[1756] A USB programmer that does nothing but flash an LED draws roughly 100 milliamps.[158]

## Standby power and battery life

Claims of zero standby power do not survive measurement, since the external supply that feeds the switched-off product still draws from the mains — a plug pack for a 24 V DC monitor measures 300 mW.[971] Products that keep a switching stage running while nominally idle can draw a substantial quiescent current for nothing: a portable power station's inverter consumes 11 W with the output disconnected.[1707] Excessive quiescent current is a plausible explanation for equipment found with a flat battery after long storage.[1720] Quiescent current drawn by mains products in standby has been the specific target of criticism where the alternative is a battery-powered solution.[1285]

Where the load is intermittent, the quiescent baseline sets the achievable runtime. An LM3914 battery gauge draws roughly 5 milliamps with no LEDs lit; in bar mode each lit LED adds at least 2 mA on top of the chip's operating current, so switching to dot mode by leaving pin nine floating is what makes the design practical.[204]

## Design practice

For a linear supply feeding a low-power circuit, the design method is to look up the regulator's quiescent current in the correct data-sheet table, add it to the measured or estimated load current, and check whether it changes the answer at all — usually it does not, and that conclusion is itself the useful result.[1285][1533] For electret microphones the equivalent step is to obtain the manufacturer's specification for the quiescent current, then size the bias resistor around that figure and the available supply rail.[611]
