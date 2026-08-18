# parallel connection

A parallel connection joins two or more components or subsystems across the same pair of nodes, so that they share a common voltage and their currents add. It is the standard way to increase current capacity, capacitance, or power handling without changing the operating voltage, and it appears at every scale of electronics from two capacitors on a board to two solar arrays feeding the same mains.[1402][510][1426] Its characteristic weakness is that paralleled elements do not automatically share equally: whatever current-hogging, mismatch, or fault occurs in one element is hidden behind the common terminals, which makes both design and fault-finding harder.[1343][1722]

## What paralleling buys

The clearest case is a bench supply with two isolated outputs. A unit rated 0 to 100 V at 2 A per channel can be wired in series for 0 to 200 V at 2 A, or in parallel for 0 to 100 V at 4 A -- the same silicon reconfigured for either voltage or current headroom.[1402] The same trade appears in power stages: an H-bridge inverter built from four MOSFETs may use several devices in parallel in each leg, spreading the dissipation across more packages rather than relying on one.[504] Discrete transistors of the same type are commonly found paralleled on a board for exactly this reason.[1415]

Paralleling is also how capacitance is accumulated. A decade capacitance box is normally wired as a parallel configuration, so a coarse value such as 10 microfarads can be set on one box and trimmed with a smaller value paralleled across it; decade resistance boxes are wired in series and trimmed the same way with small series increments.[510] Bulk storage capacitors on the input and output rails of a supply can end up effectively in parallel through the interconnecting wiring, which means a stress event that damages one bank has to be assumed to have stressed the other.[814] Two large electrolytics in parallel at 100 V give roughly 2,000 microfarads of combined storage.[809]

Digital design has used the same trick structurally. Memory expansion was once done by stacking RAM chips physically on top of one another and soldering them together, because only one address line differed between them; everything else, data and address alike, was simply paralleled up. It was an efficient way to get a lot of RAM without resorting to a complex double-sided board.[142]

## Current sharing and its failure modes

Parallel elements share a voltage, not a current, and that is where the difficulty lies. LED luminaires are frequently built as parallel strings of series-connected dies -- twelve LEDs in series per strip, with many such strips paralleled onto a common metal strip -- and often with no current-sharing resistors at all.[1343][773] Such an array must be driven from a constant-current source rather than a constant-voltage one; driving it from a fixed voltage would be poor practice. Even with constant-current drive, the sharing between strings relies on the dynamic resistance of the LEDs themselves, which is a hopeful arrangement rather than a controlled one.[1343]

Wiring choice can push a design away from paralleling entirely. In a backlight assembly, very fine wires indicate a high-voltage series string rather than a low-voltage parallel arrangement: paralleling the LEDs would demand much thicker wire for the same power, and it is harder to lay out physically. Series is the easier construction.[pKV_JiauAE4] The same current-capacity logic drives connector design. Flat flex cables and their connectors carry little current per pin, so several pins are ganged in parallel wherever a substantial supply rail has to pass through.[631]

Fault isolation is the second casualty. In a towed hydrophone array, two hydrophones sat inside each protective shell simply wired in parallel; when one failed there was no way to tell from the terminals which one it was.[1722] Field repair required purpose-built test jigs -- acoustic clamps fitted over the assembly so each hydrophone could be excited individually and measured.[1722] A related creep effect shows up in analogue switch matrices: a specification such as 10 to the power of 11 ohms of DC isolation per module sounds ample, but paralleling many modules onto one bus divides that figure down and the leakage becomes real.[655]

Paralleling live sources can also be actively destructive. Connecting two electronic loads in parallel across the same supply output shorted the input of one of them and disabled its overcurrent protection, killing the instrument.[1691]

## Batteries and cells

Battery packs use both connection types at once. A 12.8 volt lithium pack is built as four parallel strings placed in series, giving the nominal four-cell series voltage while multiplying capacity; the battery management system taps each of those strings to balance the series elements.[8P8Af5SR57U] The same arithmetic applies to primary cells: extending a meter's already long battery endurance -- 34,000 hours, or about 3.88 years of continuous operation -- past the point where it can simply be left switched on indefinitely would mean filling it with multiple D cells in parallel.[WWMXJLhPVdA]

Paralleling does not rescue every energy source. Indoor light levels reduce a solar cell's output by roughly a factor of a thousand against full sun, taking 10 milliamps down to 10 microamps; no realistic number of cells paralleled within a product's area recovers that shortfall, and the arithmetic rules the approach out before any prototype is built.[48]

## Grid-connected solar

Multiple generating systems on one site combine in parallel whether or not that is intended. Microinverters are 240 volt inverters in their own right, and a string of them is effectively all in parallel on a single pair of conductors, with a controller handling up to 600 units over a 100 kHz control-over-power link.[1385] Adding a second array has electrical consequences beyond generation: an extra 5 kW system wired in parallel on the same house, in a street where most houses also have solar, raises the local mains voltage -- a serious matter where the supply already sits near 250 V.[1426]

Monitoring hardware inherits the problem. Where two production systems feed one site, a single current transformer cannot see both, and the industry-standard fix is to parallel the current transformers so their outputs combine into one measurement.[1390][k2_mJtAeaog] Clamps paralleled this way sum their currents entirely in the analogue domain, with no software involvement.[1390] The cost is a loss of granularity: once the transformers are combined, the individual circuits can no longer be measured independently, which is why monitoring software offers a specific setting for where the current transformer has been placed.[1390] One useful property of a paralleled current transformer is that it contributes nothing unless a conductor passes through its core, so an unwanted transformer in a parallel pair can simply be left with no wire through it rather than being physically removed.[k2_mJtAeaog]

## Instruments and bench practice

Meters are routinely paralleled onto one point for comparison. Two multimeters connected in parallel cannot meaningfully measure resistance against each other, but measuring zero ohms this way is valid and exposes differences in autoranging and update rate between firmware versions.[q4gXnpFPFzQ] With several meters paralleled, each is trying to drive its own test current through the network, so readings become inconsistent and depend partly on residual charge in the input sockets.[uUCQuIp_hzU]

Other bench connections follow the same pattern. A breakout adapter with a bank of negative terminals has them all connected in parallel, with the positive on a separate side.[606] Two serial buses sharing one physical connector are handled by paralleling them onto the same pins, with an inline joiner used where a double adapter will not physically fit.[RjfStZa4Si8] Transformer windings in an instrument's mains input are switched between series and parallel by jumper links on the board, so one product covers both mains voltages.[1189]

When adding a second LED to an existing indicator circuit, the correct practice is to give the new device its own dropper resistor rather than connecting it directly across the original LED. A 1K dropper with 4.5 volts across it sets about 4.5 milliamps through the LED.[182]

## In wireless power claims

Paralleling is often invoked to make an inadequate power source look scalable. A rectenna array collecting RF energy connects its individual patch-plus-rectifier modules in parallel, on the argument that combining at DC avoids the phase-variation problem that plagues RF-level combining.[MCyLO-1grEk] The arithmetic still binds: a patch measured at 5 volts and 5 milliamps yields 25 milliwatts, and connecting such elements in parallel to increase delivered power does not overcome the fact that six or nine of them together produced only 2.5 milliwatts.[1408]

## As a teaching approach

Parallel resistance is a standard early example of the gap between calculating and measuring. The practical route -- connect the resistors in parallel and measure the result -- takes a fraction of a second on a meter, where working the value out on paper takes ten minutes. Introducing heavy mathematics before that point slows a beginner down rather than helping.[280]
