# electronic load

An electronic load is a programmable constant current sink: a value is dialled in, and the instrument draws that current from whatever is connected to it regardless of the source voltage, whether that is 3 volts, 5 volts, 15 volts or 20 volts.[102] It exists to replace the alternative — a large stock of power resistors hung on a supply output to simulate different operating points, which is slow and awkward.[102] It is the standard companion instrument to a bench power supply, and the enabling tool for power supply testing, battery discharge testing and solar cell testing.[1023][281]

## Operating principle

The core is trivially simple: an op-amp, a current sense resistor and a pass transistor, with the voltage across the sense resistor fed back to the op-amp so that the loop forces a set current through the transistor.[1381] Scaled up to a commercial instrument, this becomes a bank of MOSFETs on a large heat sink with load and sense resistors, either under op-amp control or under digital control.[1550] Inside a commercial unit there is a microprocessor to control everything, a DAC to set the demanded value and an ADC to read it back, and a MOSFET or bank of MOSFETs with load resistors — the basic operation of any DC electronic load.[281] The difficulty is not the topology but the control loop: the magic is in the loop stability, making sure the thing does not oscillate.[1550]

Because the pass elements are purely linear, all the input power is turned into heat in the transistors, which is why the load section of an instrument carries the largest heat sinking.[1550] The same architecture shows up inside other equipment for the same reason — a battery analyser that dissipates its discharge current in power transistors on heat sinks is running an electronic load, distinguishable from a current-measurement arrangement by the absence of large sense resistors in that path.[1434]

A related distinction is that a four-quadrant source measure unit can both source and sink current, and so can be used as a load in its own right.[718]

## Operating modes

Instruments provide constant current, constant voltage, constant resistance and constant power modes.[-ir61ARd5T4] Constant current is the workhorse: set the amps, switch on, and the load holds them.[1301][320] Constant power is used where the specification under test is expressed in watts — a 10 W draw on a USB battery bank, for example, where the source voltage cannot be controlled and using a nominal 2 A would overshoot the intended power.[1649] Constant power accuracy is generally worse than constant current accuracy, because the instrument has to do arithmetic and additional errors are introduced.[774]

In constant current mode the terminal voltage is not fixed the way it would be with a resistor; it winds down to whatever compliance voltage the load requires to pass the demanded current.[1688]

Constant resistance mode is the mode most likely to cause trouble. Setting a resistance can drive a supply into oscillation between constant voltage and constant current mode.[828] It is also the only legitimate way an electronic load should ever present a short across its input — with the resistance set to zero and the output switched on.[-ir61ARd5T4]

## Effect on the device under test

An electronic load is an active, dynamic device and does not behave like a resistor. Startup transients cannot be captured into an electronic load for this reason; a resistive load must be substituted to get a representative switch-on waveform.[1298] Under constant power the interaction can be worse still: a supply that is clean into a resistor may simply oscillate against a constant power load.[1298]

The load also injects noise into the measurement. A load can couple mains hum back into the circuit under test — a case of roughly half a volt of 50 Hz appearing in a DC-DC converter measurement, present even with the load turned essentially to zero at around 1 mA, and vanishing the instant the load is disconnected.[324] Similarly, 142 Hz switching noise attributed to a power supply under test turned out to be coming from the load; swapping in a resistive dummy load of comparable current, 2.5 A instead of 2 A, made it disappear entirely.[594] The general lesson is that the noise floor of a ripple measurement belongs to the whole test setup, not to the device under test, and differential probing is what allows the culprit to be identified.[594]

Dave Jones refers to his BK Precision 8500 as his "power supply killer", having destroyed a production power supply with it.[828][320] A supply that dies while being played with by an electronic load is a failed supply: current limiting exists precisely so that a good design survives dead shorts on its output indefinitely.[315]

## Measurement limits

Two limits dominate practical accuracy. The first is lead and terminal resistance. At 1 A, even heavy cable and large binding posts drop enough voltage to matter: in a low-power battery discharge test a 0.15 V drop against 0.66 A accounted for the full 100 mW programmed into the load, producing about 40% apparent error in the external measurement while the load itself was regulating perfectly.[774] Good quality electronic loads therefore support four-terminal measurement and remote sensing, with sense terminals on the rear or front, and enabling remote sense brings the load's own reading into agreement with an external meter.[957]

The second is resolution at low current. Measurement precision on a bench electronic load runs out somewhere around 10 mA, below which a source measure unit is the appropriate instrument for setting and measuring sink current.[957] Compliance voltage is a hard ceiling of a different kind: loads rated at 120 V and 150 V cannot be used to load a 180 V supply at all.[1263] A load with a 60 V maximum compliance voltage sets the limit on how many cells can be strung in series for a batch discharge test.[1296]

## Battery testing

Battery work is the application that most exercises an instrument's programmability. A battery discharge mode discharges at a set current and stops on a programmed condition — a cutoff voltage, an accumulated capacity, or an elapsed time — and accumulates the milliamp-hour or watt-hour figure.[9FCzAgJhRdc][1274][RFb3TwWzza0] Typical setups: alkaline AA cells discharged at 0.5 A to a 0.8 V cutoff to produce a known partially-discharged state;[508] AAA cells drained at 500 mA to remove 500 mAh;[865] alkalines drained at 100 mA with an automatic stop at 1,250 mAh, half the roughly 2,500 mAh capacity available at that rate;[1274] a NiMH cell discharged at 1 A on the 4 A range with a 1 V cutoff and no timeout, using a Kelvin connection to sense directly at the battery terminals.[9FCzAgJhRdc]

The programmable cutoff is the specific advantage over logging a discharge with a multimeter, which cannot stop itself and requires the capacity and reading count to be worked out in advance.[774]

Two measurement points matter for battery capacity claims. Every battery data sheet specifies its cutoff voltage under load, because terminal voltage recovers when the load is removed; switching a load on drops the terminal voltage immediately by the amount lost across the cell's internal ESR.[772] And capacity figures for USB battery banks should be compared output-referred rather than input-referred, since an input-referred number excludes the efficiency of the internal DC-DC converter.[1648]

## Commercial instruments and DIY

There is not a huge amount inside a commercial electronic load, and the DIY route is well established — an op-amp, a FET, a DAC and little else, with microcontroller or PC control added at will.[281][393] Building one from junk box parts is a standard exercise, and the design has been rebuilt and extended by many people, including microcontroller-based versions.[102][393][1097]

Commercial units nonetheless buy precision. The BK Precision 8500 is a 120 V, 30 A, 300 W unit, one of a family covering different voltage, current and power ratings; it is designed and manufactured by ITech and sold as the IT8512, and its recommended price was around 1,100 US dollars.[281] It supports pulse loads and PC-controlled battery discharge testing.[281] The 8601 is its successor, offering extra resolution, more flexibility and faster operation, including programmable current slew — 10 mA per millisecond giving a 200 ms transition — though only in sequencing mode rather than on the on-off transition.[862] The Rigol DL3021, the bottom of the DL3000 series at 499 US dollars, sits mid-market.[1023] The Keysight E36731A combines a precision DC power supply, an electronic load and a battery emulator in one chassis from about 4,700 US dollars; internally the load is simply wired in parallel with the supply output and switched in when required, since a battery emulator does not need it.[1550]

Firmware quality is a real hazard. A DL3021 was observed to short its own input spontaneously during a battery capacity test, losing the accumulated time and watt-hour figures each time and requiring a power cycle to clear — behaviour confirmed by other users of the model rather than a fault in one unit, and apparently tied to a combination of micro firmware and FPGA revision.[-ir61ARd5T4][lYKjScnkeq0] A load shorting the thing it is measuring, mid-test, is the opposite of what the instrument is for.[lYKjScnkeq0]

Terminal design is a recurring practical annoyance across the category: large screw binding posts that accept lugs but have no cross-hole for a wire and no socket for a banana plug, to the point that adapter boards exist purely to convert them to female banana jacks.[1034][546]
