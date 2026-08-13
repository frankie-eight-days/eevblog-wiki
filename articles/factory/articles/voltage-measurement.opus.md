# voltage measurement

Voltage measurement is the most basic operation in electronics test, and the one on which nearly every other measurement is built. A multimeter has three fundamental functions — voltage, current and resistance — and voltage is the one no instrument omits.[75] An oscilloscope is no different in kind: it is also a voltage measurement device, distinguished only by displaying voltage with respect to time.[UJjMt2-k99c] Wattmeters, power analysers, LCR meters and electronic loads are all voltage measurements with something else layered on top.[705][589][922][1023]

## The golden rule of troubleshooting

The first rule of fault-finding is to measure the voltages, and it is stated so often that it functions as a rule of the bench rather than as advice. It appears in several wordings — "thou shall measure voltages",[831] "Thou shalt measure voltages",[804] "thou shalt check voltages",[147] "thou shall test voltages"[966] — but always as rule number one, ahead of any theorising about which chip has failed.[1475][536][507][CK5nbC_dBWk]

The reasoning is a probability argument. A dead-screen, dead-everything failure is far more likely to be a supply problem than a microcontroller fault, so the rails are where the search starts.[1726][58] The rule extends to ground and power pins specifically, because a chip missing its VCC pin or its ground pin can still appear to work through its ESD protection diodes, producing a fault that looks like anything but a missing supply.[831]

The rule is most often cited retrospectively, after a repair took longer than it should have. An Onkyo receiver's fault was a dead −35 V rail feeding a vacuum fluorescent display, caused by an open carbon film resistor — and it was the last supply measured.[1395] A JBL monitor repair would have reached its conclusion faster had every pin been measured early, though the fine pin pitch made probing genuinely risky.[1322] On a Data I/O programmer, the voltages were simply forgotten in the excitement of the repair; measured afterwards, all the test points were fine, which at least eliminated the supplies.[1061] The corollary rules that accumulate around it are of the same character: never assume something is overloaded, actually measure it,[804] and understand how the equipment works before trusting what it tells you.[966]

Where measurement is awkward, the practical form of the rule is to measure the easy things first — the points that can be reached without disassembly — and only then work toward the hard ones.[1433]

## Where the probe goes

A voltage reading is only meaningful at the point it was taken, and most measurement errors are errors of location rather than of instrument.

Probing a regulator means probing right on the input and output terminals, with the ground lead on the ground pin, because anything further away includes the drop caused by load current in the wires or PCB traces.[158] The magnitude is not academic: a model-aircraft regulator reading 6.18 V at the load terminals was still holding 6.55 V measured directly on the brick's own output, the difference being loss in the connecting leads.[895] The extreme form of this principle is the four-wire technique, where a separate pair of sense wires carries no current and the voltmeter reads directly across the component itself, nulling out the test lead resistance entirely.[133]

The same logic governs battery testing. Cells that measure adequately out of circuit may not deliver at the load, so the voltage must be probed at the contacts where the load actually sees it — a device that runs from a bench supply all the way down to 0.9 V may still refuse to run from two cells totalling 2.5 V.[789] Measured properly at the right point, a bench supply and a battery are equivalent sources.[789]

## Ground reference

Every voltage is a difference, so a wrong ground reference produces a wrong reading with no outward sign of error. Tracing a supposed ground back to a connector that was not actually ground has sent a measurement session down a long dead end, resolved only when the schematic's ground pins turned out not to match the physical board.[XUyjRm1Upjs] A prototype that read a healthy 5 V directly on its own pins was nonetheless failing from a classic system ground problem, invisible until the ground connection itself was changed.[155]

The practical response is to establish a known reference first: identify the ground point, verify it by continuity, and if necessary solder on a dedicated ground test point so the probe can move freely around the board.[135][663][297] For the same reason, node voltages in a network are only defined once a reference node has been chosen — in a resistor cube, symmetric nodes measured against a common reference read identically.[1472]

## Test points and service documentation

Marked, accessible voltage test points make the golden rule cheap to follow, and their absence makes it expensive. On an HP dynamic signal analyser, the lack of accessible marked test points on the top of the board meant time was spent suspecting the crystal and reset lines before the supplies were properly checked; the eventual measurement required soldering pins onto a 79L12 regulator to get at its input and output.[536][540] Reference voltages, supply rails and DC quiescent voltages are the correct first pass whenever they can be reached.[540]

The best service documentation annotates the schematic with the voltages themselves. The Sony D50 schematic carries voltage test points marked with their expected values — 2.8 V and 2.7 V DC bias among them — supporting a procedure of measuring supplies first and then working through the DC bias levels point by point.[863] Locating the voltage test points is the first move on an unfamiliar board even before the circuit is understood.[918]

## Reading the result

A measured voltage is usually interpreted against an expectation rather than an absolute standard. Standard rails identify themselves: 1.2 V across low-ESR output caps is the expected core rail for a high-density VLSI part, even on a board with no silkscreen marking.[TE3il-V6XCE] Finding 3.3 V and 5 V alongside a crystal identifies a microcontroller section.[1322] A +5 V and −5 V pair points at a 7660 capacitor voltage inverter.[918]

Deviations localise the fault. A protection MOSFET pair reading the full 3.5 V cell voltage across it is open — a good cell behind an open switch measures exactly as it would with the switch removed.[RasOXxxEhCk] A backup supply pin can be confirmed by measuring across the capacitor that sits on it, in one case 2.9 V present and therefore not the cause of a no-boot.[1433] A battery reading 4.15 V at the terminals eliminates a suspected bad spring contact in one measurement.[1428] A regulator whose input reads −19.2 V on nominal ±18 V rails but whose output reads −1.85 V has failed unambiguously.[536] Barely 0.4 V across a cap where a rail should be points at a dead supply rather than a dead processor.[1739]

Equally, a reading that is nearly right is still a fault. A 5 V interface reading 5.68 V is outside any plausible ±5% tolerance and warrants explanation.[297] A rail that has recovered from 4.5 V only as far as 4.83 V has not actually been fixed.[379]

## Instruments and resolution

Resolution and accuracy are chosen against the job. Bench and system-level voltmeters run from six-and-a-half digits — capable of seven-and-a-half with averaging in high-resolution mode, though only over GPIB rather than the front panel[426] — down to handheld meters where a 3.5-digit display with a manual ×10 multiplier makes 6 V read as .594.[930] Small-signal work needs the opposite end: a meter with 10 µV resolution and a 50 mV range is what makes thermoelectric generator output measurable at all.[664] The available span of laboratory equipment stretches from nanovolts to a thousand volts, but chasing the last digits is a separate discipline that most bench work does not require.[s2KkgI-kyK0]

Resolution should be spent where the dynamic range is. In a bench instrument measuring both voltage and current, an 8-bit or 10-bit converter is entirely adequate for the voltage channel, because the voltage is known and roughly constant; the current is what must be resolved across many decades and many ranges.[1190]

Verification is by comparison. Two meters on the bench is the working minimum for serious measurement, one on the input and one on the output,[158][954] and having more than one available is repeatedly what settles a doubtful reading.[804] Where two independent instruments agree — a scope and a meter both reading 10.01 V peak-to-peak — the accuracy spec can be trusted.[6qjqhnQiQXQ] Where a meter reads 5.07 V and the supply's own display reads 5.00 V, nothing has been established about which is correct without a third reference.[482] Against a proper standard the question is settled directly: a reference diode expected at 6.1730 V measured 6.173 V.[210] Instruments that display a measured rather than a set output value are more trustworthy for this reason — the number shown is the actual measured output voltage, not the programmed one.[655]

Poor instruments fail visibly on voltage. A meter that reports 10.19 V from a single cell, and holds that reading stably, is not merely inaccurate but unusable, since a battery is about the lowest-noise source available.[1238] Conversely, an insulation resistance tester's rudimentary DC and AC volt modes, with a single coarse range and no true RMS, do not make it a substitute for a multimeter.[468]

## Loading and input impedance

A voltmeter is part of the circuit it measures. Meter loading is irrelevant across a low-impedance source such as a thermoelectric module, where the difference between a 10 MΩ input and something lower changes nothing.[664] It matters greatly at the other extreme: with a high-voltage probe across an electrostatic speaker output, the unknown probe loading makes the 40–60 V observed at 20 V/div difficult to trust as the true open-circuit figure.[1150] Low-impedance measurement modes exist for the opposite purpose, deliberately loading the input below a threshold voltage to suppress ghost voltages in electrical work.[973]

## High voltage and indirect methods

Mains-level and higher measurements are ordinary work for a suitably rated meter — 248 V on a nominal 240 V supply is a normal lab reading[1095] — and range switching between volts and millivolts is done by relay inside the meter.[1095] Overvoltage behaviour is part of the specification: a meter presented with 600 V AC should read it and warn, not misbehave.[1704]

Some voltages are only accessible by measurement rather than by inference. The off-state pin voltages on a nixie tube driven from a 170 V supply through a 22 kΩ resistor vary enormously from pin to pin — 24, 43, 47, 49, 69, 118, 122 and 123 V were all present on a single tube — so the driver's required standoff voltage cannot be assumed from the supply rail.[RXk_wr0g8UM] A solar string of twelve panels in series nominally at 456 V is diagnosed by first confirming that any voltage at all arrives from the array, since one failed panel takes out the entire string.[1217] Even a battery can carries voltage: the outer can of a cell is connected to the positive terminal, so piercing the skin against a grounded chassis shorts the cell.[1350]

Non-contact measurement at a distance is possible in principle. Laser voltage probes exploit Faraday rotation through air, where the angle of rotation is proportional to the Verdet constant for air, the magnetic field and the path length in that field, allowing field strength and hence the conductor's voltage to be extracted optically.[263]

## Logging and instrumented measurement

Voltage is the easiest quantity to log over long periods, and battery and supply characterisation depend on it. A meter's CSV export gives a reading number and the voltage; fixing the meter to a single range — the 10 V range, for instance — prevents it switching to exponent notation partway through the log and complicating the data.[774] The resulting discharge curve shows what a spot reading cannot: an alkaline cell falling away in a near brick-wall response at 0.8 V, with little useful energy below 1 V.[774] Chart auto-scaling is frequently the wrong choice for mains logging, where manually fixing the axis to 235–245 V makes both the variation and any data dropouts obvious.[1684]

Purpose-built measurement hardware follows the same pattern at smaller scale: end-of-line test fixtures with ±10 V voltage measurement inputs alongside digital I/O and analog output,[1391] compact voltmeter modules monitoring ±36 V in real time,[1649] and dataloggers storing 0 to 15 V as 8-bit or 10-bit samples, the range extensible if the input protection diodes are removed and the firmware modified.[294]

## Voltage as half of every other measurement

Most derived electrical quantities are a voltage measurement paired with a current measurement. A wattmeter requires both, brought in on separate voltage and current terminals.[705] A power analyser carries two nearly identical signal paths, one for voltage and one for current, and from them derives phase angle, real power, apparent power and inrush current.[589] An LCR meter can be built on the voltage-and-current technique: excite the device under test at a fixed frequency, measure the voltage, the current and their phases, and calculate everything else from those basic measurements.[922] Modern power meters may split the work across separate processors, one handling voltage and current processing and another the real-time energy calculation.[1693]

The generality of the measurement is itself notable: any two coupled classical analog circuits will always have some voltage measurable at the output, which is precisely the property that quantum systems do not share.[1316]
