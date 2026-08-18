# slew rate

Slew rate is the maximum rate at which a circuit's output can change, expressed in volts per microsecond for amplifiers and logic, or amps per microsecond for current sources and loads.[1464][862] It is distinct from bandwidth: bandwidth describes small-signal frequency response, while slew rate is a large-signal limit on how fast an output can traverse its range, and a part can have adequate bandwidth yet still be unable to move a signal from rail to rail in the required time.[1464][1325] Slew rate governs whether a comparator-style output arrives on time, whether a peak detector catches its peak, whether a logic input crosses its threshold cleanly, and how much high-frequency energy a nominally slow signal actually contains.[1464][490][1611][316]

## Slew rate in operational amplifiers

Jellybean op-amps are slow. The LM358 specifies 0.5 V per microsecond, so a 0 to 5 V swing — the kind of transition wanted from a 5 V comparator — takes about 10 microseconds.[1464] This is the standard trap in pressing an op-amp into service as a comparator feeding a gate or flip-flop; the slew limit is compounded by overload recovery time, since an op-amp is not designed to have its inputs and outputs slammed non-linearly.[1464] The TL071 family sits somewhat above the LM358, with a reasonably high slew rate alongside 1 mV offset voltage and 2 µV/°C offset drift.[1436]

The spread across the market is enormous. A datasheet comparison between two shunt-amplifier candidates put one at 20 V per microsecond against the other's 1.6 V per microsecond, more than an order of magnitude apart, tracking the bandwidth difference between them.[1325] At the extreme, the BUF634 buffer specifies 2,000 V per microsecond along with 250 mA of drive.[1609] Wideband parts buy that speed with design compromises elsewhere: a fast op-amp's input architecture is optimised for bandwidth and slew rate rather than input current, which is why its input bias current can be a couple of microamps where a precision instrumentation-grade part is in the tens of femtoamps.[479]

Slew rate is also a specification that can move under a design's feet. A revision of the NE5532 improved gain bandwidth product while reducing the typical slew rate from 9 V per microsecond to 5, with no change to the part number — the same silicon revision also dropped the maximum output swing versus bandwidth figure, the output impedance spec, and the crosstalk attenuation spec from the datasheet.[1752]

## Charging capacitance: the peak detector case

A peak detector makes the consequence of finite slew rate visible. When a new peak arrives, the op-amp must charge the hold capacitor, and it cannot do so instantly; the output ramps rather than stepping, so the captured value lags the true peak.[490] Increasing the hold capacitor to reduce droop makes this worse — a very large capacitance cannot be charged quickly by a slow amplifier, so droop and acquisition speed are in direct conflict and the capacitor value is a compromise, not a free choice.[490]

Pushed hard enough, the circuit drops peaks entirely: the amplifier begins to slew back up towards a peak, the input has already moved on before the capacitor is charged, and pulses go missing from the output.[490] At low input frequencies the same circuit tracks fine, chopping up and following the input waveform, because the signal is far slower than the amplifier.[490]

## Digital logic and metastability

Any digital input without a Schmitt trigger — microcontroller inputs, FPGA inputs, ordinary logic gates — is susceptible to input slew rate.[1611] An input that changes too slowly can drive a flip-flop or counter into a metastable state, in which the output is indeterminate and the device may register multiple clock pulses, skip pulses, or produce none, appearing as erratic counting.[1611][1208] A representative failure: an open-collector optocoupler output pulled up to VCC, where the passive rising edge is not sharp but a slew that can be in the order of microseconds, set by the pull-up value against the total load capacitance — the driven chip's input capacitance, the breadboard or PCB trace capacitance, and any other components on the bus.[1208] The same node driven from a proper CMOS or TTL output presents no such problem.[1208]

Load capacitance accumulates faster than expected. A typical logic input is about 3 pF, so driving several gates from one output triples or quadruples the load and directly degrades the output's transition rate.[sr1DOHnJi8I] The effect scales up across a board: daisy-chained boards driven from a single Raspberry Pi output can present more line capacitance than the driver can handle, slowing the edges, eroding voltage-level margin, and causing boards progressively further along the chain to fail to clock data in reliably — the fix being a buffer chip on each board to redrive the outbound signals.[1365]

Pull-up selection on an open-collector bus is therefore a speed decision, not just a power one. Lower pull-up values give faster edges and more achievable I²C bus speed, at the cost of higher current, which is a trade-off worth spending a BOM line on rather than accepting whatever value a design tool suggests.[1307] Some microcontrollers expose the same trade-off directly as a selectable output drive or slew capability.[1140]

## Slew rate, rise time and bandwidth

A signal's frequency is a poor guide to the bandwidth needed to handle it; what matters is the rising edge.[316] A 1 kHz pulse train with a fast enough edge is a high-speed signal in every sense that counts for transmission-line matching, output impedance, and attenuator behaviour.[316] A square wave or step contains high-frequency components in proportion to its slew rate, which is why step response reveals overshoot, ringing and termination effects that a ramp waveform never shows.[6XpyOGw6RFM] Fast-rise-time pulse generators exist precisely to exercise this property in a system under test.[311]

The conversion is direct: an edge of rise time tr has an equivalent bandwidth of roughly 1/(π·tr), so 8 ns slew rates correspond to about 40 MHz.[1119] This is the figure that matters for common-mode rejection — differential probes with excellent CMRR at 50 Hz are useless by 10 MHz, so a fast common-mode edge appears in the measurement even though its repetition rate is low.[1119]

The same reasoning applies to power rails. Ringing and transients on a rail run to hundreds of megahertz, set by the slew rate of the circuit drawing current, and even ordinary microcontroller switching produces such content — which is why rail fidelity measurements demand high bandwidth and are taken at timebases in the tens of nanoseconds per division.[1735]

## Measurement and instrument control

Oscilloscopes expose slew rate as a direct automatic measurement — a rate-of-change parameter alongside rise time, duty cycle and voltage extremes.[704] Power-analysis application packages list slew rate among their measurements together with switching loss, power quality, transient response, turn-on and turn-off time, output ripple and PSRR.[209][1309] Mask and limit-test engines can be set to alarm on slow rising edges, catching a slew rate that drifts over a run of minutes, hours or days, alongside runt-pulse and glitch tests.[1638]

Programmable sources and loads increasingly make slew rate a settable parameter rather than a fixed characteristic. A DC electronic load in constant-current mode allows the rising and falling slope to be set — 5 A per microsecond at the high end, and rates as low as 0.01 A per millisecond at the low end.[862] On some loads slew rate is a licensed option, bundled with high resolution and frequency measurement as the difference between model variants.[1023] Programmable supplies expose slew rate in volts per second, which is what battery emulation requires in order to reproduce a source's real dynamic behaviour.[Y2rcx4vKxlc]

## Slew rate outside electronics

The concept carries into electromechanical output stages. A studio monitor's woofer amplifier can be specified at 9 volts per millisecond, and for a given cone and a given power the slew rate sets whether the cone can physically be accelerated fast enough — the cone's inertia is the limit being fought.[1156] Slew rate is one contributor among bandwidth and general amplifier performance, not the sole determinant of one loudspeaker over another.[1156]
