# shift register

A shift register is a chain of flip-flops that accepts data one bit at a time on a serial input and moves that bit along the chain on each clock edge, so that a long parallel word can be delivered over two or three wires instead of one wire per bit.[1611][1531] Its dominant practical use is line saving: a controller drives a clock and a data line, and the register expands them into eight, sixteen or forty outputs, which is why the part turns up wherever a board has more things to switch than the processor has pins.[824][948][589] The jellybean 74HC595 and the 4000-series 4094 are the versions most often encountered, and the 595 in particular has been in continuous bench use for decades.[952][1545]

## Operation

Data is presented on the serial input and clocked in. On a positive-going clock edge whatever is on the data pin is transferred to the first output stage, Q0; on the next edge that bit moves from Q0 to Q1, and so on down the chain.[1531][1611] Some devices clock on the negative-going edge instead, so the direction of the active edge has to be read off the timing diagram rather than assumed.[1249] A bit fed in at the input therefore takes as many clock pulses to reach the last output as there are stages: in an eight-bit part, a one placed on the input appears on Q7 only after the eighth clock.[1249]

The 74HC164 is the archetypal plain serial-in, parallel-out device. It has a clock, two data inputs combined through an AND gate, and a clear line, and nothing else.[1611][1531] The 4094 and the 74HC597 are the equivalent eight-bit parts from the 4000 and 74HC families.[824][589]

## The output latch

The defect of a plain shift register is that its outputs are live while the data is moving. Every intermediate state of the shift appears on the pins, so an eight-bit word intended to switch eight loads simultaneously instead ripples across them.[1611] With relays on the outputs and a slow enough clock the relays can be heard clunking on and off as the data walks through, and on a multiplexed display the effect is visible as the outputs change in sequence rather than together.[1611][948] Where the outputs drive a bank of transistors, the transitional states are also a supply problem: switching all the outputs on at once can draw hundreds of milliamps just to drive the output transistors.[1365]

The fix is a second, parallel register between the shift chain and the output pins. The 74HC595 carries this structure: the shift register part with its own shift clock, serial data input and clear, plus an output latch clocked separately by the R clock line.[1611] Data is shifted in with the outputs frozen at their previous state, then a single pulse on the latch clock transfers all eight bits to the pins at once.[1611][1365] Firmware for such a chain accordingly maintains two separate pulse routines, one for the data clock exercised on every bit and one for the latch clock pulsed once at the end of the frame.[VTAwzrKPjeE] Latched variants exist at wider widths as well, including parts combining a 16-bit shift register with a 16-bit latch, though the wide devices tend to arrive in awkward packages such as 0.5 mm pitch 32-lead QFN.[948]

## Cascading

Registers are daisy-chained by feeding the last stage of one device into the data input of the next, so that a string of chips behaves as one long register: five eight-bit devices form a 40-bit chain, and the first bit sent lands at the far end after 40 clock pulses.[1531] The chain is driven from the microcontroller into the first chip and passed chip to chip to the end, with no data read back.[952] On an oscilloscope the traffic appears as five packets of eight clock pulses, one packet per digit.[1531]

Not every part is designed for this. A device intended to be cascaded provides a buffered serial output pin dedicated to the purpose; the 74HC164 does not, and its Q outputs go straight to the output buffers, so a cascaded design has to tap the last output, Q7, and route it back as the data input of the following chip.[1491] Cascading also has an electrical cost at the board level, since a single driver on the source end may not be able to drive the accumulated capacitance of the clock and data lines across several daisy-chained boards.[1365]

## Driving displays

Display driving is the classic application. A digit-based display such as a Nixie needs ten or eleven separate lines per digit rather than the four of a BCD-to-seven-segment decoder, which rules out the traditional decoder and points instead to a latched shift register clocked in and then latched.[948] For high-voltage displays the register only carries the data; external high-voltage transistors and their resistors still have to be provided, which for ten lines per digit means a large number of discrete parts to assemble.[948]

Two arrangements are possible. In a static drive the data is shifted in once and stays on the outputs, sourcing current continuously through whatever is enabled.[1493] In a multiplexed drive the display is blanked, new data is shifted, and the display is unblanked, repeatedly — many devices provide an output-enable or blanking input intended for exactly this, so the shifting is invisible.[1491] Multiplexing is often forced by current budget rather than chosen: with eight segments in each of five digits, 40 segments at a per-output maximum of 25 mA cannot all be lit at once.[1491] A related pattern drives the digit-select transistors from the register itself, shifting a single active bit along so that exactly one FET, and therefore one display, is on at any instant.[689]

Serial addressable LED strips use the same principle at the module level, each LED passing data on to the next, which makes the strip length arbitrary and the driving code modular.[227] Character displays such as VFD modules can behave the same way, each latched byte pushing the character to the next position.[717]

## Elsewhere on the bench

Test equipment uses shift registers extensively for slow control paths where speed is irrelevant and pin count is not. Oscilloscopes carry 4094s per input channel to distribute channel control data without running a bundle of lines across the board, and the 595 recurs in scope designs of every generation.[824][1545] A power analyser's interface board can be little more than a stack of eight-bit shift registers, with the eight-bit parallel output of the ADC shifted through registers so that it can cross an optocoupler barrier on a single line.[589] In a logic analyser front end, mask and invert registers loaded serially from the host set the individual bits of the trigger mask and comparator arrays, which is a cheap way to make a wide configuration word settable.[747]

The structure also appears outside data distribution. A three-stage shift register with feedback clocked from a 14.318 MHz source acts as a divide-by-six, yielding 2.38 MHz along with a second output at a defined duty cycle.[32] Internally, processors may need extra clock cycles simply to move a word from one register to another, which can show up on a programming interface as a burst of clock pulses that does no visible external work.[1144]

## Practical notes

Level compatibility is the trap when a register drives something other than plain logic: the input threshold voltage of the driven stage has to be checked against what the register actually outputs.[952] When debugging a display chain, the fact that the data is visibly changing at the register input proves nothing on its own — the clock has to be confirmed as well, since a register receiving data but no clock produces no output at all while looking alive on the data line.[689]

Layout benefits from the topology. A serially driven display board reduces to a few common control lines plus data in and data out, which allows each display segment to have its own driver placed beside it with almost nothing crisscrossing the board.[1535]

Because the internal state is a visible, ordered thing, the shift register is also a natural teaching device: with LEDs on the outputs and a manual clock button, a bit can be pushed in and watched moving one position per press.[1720][1080]
