# oscillator

An oscillator is the circuit element that generates a periodic signal from a DC supply, and in practice almost every active chip needs one to run at all — either from a bare crystal or from a packaged external crystal oscillator module.[1614] Structurally it is an amplifier with feedback: a common-emitter, common-base or common-collector stage becomes an oscillator once positive feedback is applied around it.[280] Because the clock is the one signal without which nothing else in a digital system happens, the oscillator is also the first thing checked when a board is completely dead.[97][710]

## Clock sources for digital systems

FPGAs contain no internal clock of any use to a design, so a working system requires an externally supplied clock, typically a standard packaged 3.3 V oscillator with its own bypass capacitor, fed into a global clock pin — around 20 MHz for a general-purpose FPGA system.[193] Using a global clock pin for the oscillator costs the I/O function that pin would otherwise have provided.[193] Development boards ship with an oscillator on board for exactly this reason; a basic FPGA trainer might carry a 50 MHz part alongside its memory and converters.[494]

Microcontrollers usually offer a choice between an internal RC oscillator and an external source, and the configuration of those options is a recognised trap for beginners setting up registers on a PIC or Atmel part.[45] The internal oscillator is often not accurate enough over temperature for asynchronous serial communication, which is a standard reason to fit an external 8 MHz resonator instead.[238] Ceramic resonators appear widely in this role — an Amstrad NC100 clocks at 12.363 MHz from a resonator rather than a crystal.[385][827] Some evaluation boards expose several oscillator options, for example 32 kHz and 4 MHz selectable by jumpers, plus a variable-frequency input.[341]

Where a clock is generated internally by a processor and distributed to legacy bus devices, a failed distribution path can in principle be worked around with a mod board carrying its own 25 MHz oscillator to clock the affected ROMs and bus devices — at the risk of losing synchronisation with the rest of the system.[1288]

## Frequencies encountered in practice

The main oscillator frequency is a reliable clue to what a board is doing. A 32.768 kHz watch crystal indicates a real-time clock or a deliberately slow, low-power chipset; a multimeter drawing single-digit microamps runs its processor from one.[973][413][1416] A handheld multimeter's main oscillator may be only 4 MHz,[853] a thermal imager's only 8 MHz, which is adequate when the processor merely reads a serial interface from the sensor and drives an LCD.[669] Instrument main clocks of 10 MHz,[521][1256] 20 MHz,[810][625] 50 MHz[377] and 100 MHz[359] are common, and RF receivers run far higher — 230 MHz for a wireless microphone receiver paired directly with its RF chip.[1416] A 54 MHz oscillator inside a camera lens is high enough to be surprising for the application.[849] Ultra-low-power microcontrollers may limit their built-in oscillator range deliberately: one single-chip toothbrush controller runs from 32 kHz to 800 kHz and draws 4 µA in active mode.[284]

Where two oscillators sit together on a board, or an oscillator sits inside a shielded can beside a chip, it usually signals a PLL or clock generator synthesising the sampling clocks rather than two independent references.[1545][I-9dGvk3BW8][1701][1679]

## Accuracy, jitter and reference quality

Instruments that measure frequency are only as good as their timebase, so frequency counters are sold with a range of oscillator options — the base option being an ordinary temperature-compensated quartz oscillator, with better references available at extra cost.[235] The same tiering appears in oscilloscopes and spectrum analysers: a $599 instrument may carry a 20 ppm oscillator while a $50,000 version of the same architecture carries a far better one with much lower jitter.[1701] In the 1 GHz oscilloscope class a 1 or 2 ppm temperature-compensated oscillator ought to be standard equipment, and manufacturers that fit poor ones are cutting a corner that matters.[1218] Specifications also need reading over the full period: a part specified at 1 ppm for 12 months may only be guaranteed to 3.5 ppm over ten years.[1218]

A high-grade oscillator is what buys low phase noise in a spectrum analyser, together with good mixers in the RF block.[470] Non-standard oscillator packaging on a scope board — alongside a 10 MHz reference input and output — is a sign the designers specified a better-than-standard reference.[384][892]

A counter can be made to read exactly its nominal frequency by feeding its own internal oscillator into both its signal input and its external reference input, which measures the oscillator against itself and therefore proves nothing about absolute accuracy.[459]

## Oscillators built into ICs

Many parts hide their oscillator inside the package. The CD4060 combines an oscillator usable with either an RC network or an external crystal with a binary ripple counter, so a single chip and a few passives produce a chosen frequency and a set of divided outputs.[831] The LM567, best known as a tone decoder, is equally usable as a precision oscillator and can be tuned to a chosen frequency such as 50 kHz.[354] Switch-mode PWM controllers integrate a switching oscillator alongside the voltage reference, error amplifiers, dead-band control and steering flip-flop.[272] Chopper-stabilised op-amps run their chopping oscillator entirely internally with no external components.[476] Frequency-standard and calibrator designs may use a chip with a built-in oscillator and a digitally programmable divider, with diode gating used purely to select among the available output frequencies.[709]

The distinction matters when specifying transducers: a buzzer is a piezoceramic transducer with a built-in oscillator, so applying 3 V makes it sound at its own internal frequency, whereas a bare piezoceramic transducer needs external drive and its pitch is then set in firmware.[1745]

## Discrete and analogue oscillators

Discrete transistor oscillators remain common where cost or RF performance dominates. A metal detector's transmit oscillator is built from a discrete transistor and coil, with start-up base current supplied through a 15 kΩ resistor and the sense coil so that oscillation can build; drive and sense coil inductances of 1.7 mH and 18 µH respectively set the operating point.[714] Loading such an oscillator heavily enough removes the feedback needed to sustain it and stops oscillation completely.[714] Old bit-rate generators used Colpitts-variation oscillators with a separate crystal per rate, occupying an entire board.[1237] A three-transistor covert transmitter allocates one transistor each to microphone gain, the tone oscillator and the RF output stage.[956] Older laboratory and instrument designs put the oscillator in its own shielded case — a 1 kHz oscillator in a transistor analyser, for example.[693]

Oscillators also serve as the energy source for voltage conversion. Condenser microphone polarising supplies historically used an oscillator driving a step-up transformer; a simple CMOS RC oscillator gives a well-determined frequency of oscillation that can then be fed through further stages.[609] Isolated DC-DC converter modules likewise contain their own oscillator and magnetics.[680] A switching converter's primary side may be powered from a rail derived downstream, with the oscillator sitting on the primary;[791] where no separate primary-side oscillator exists at all, the supply is bootstrapped instead.[1301]

In a switch-mode regulator the oscillator is what distinguishes the topology from a linear one: the same series pass transistor, reference, error amplifier and feedback divider are present, but the error amplifier gates an oscillator on and off to drive the pass transistor in bursts rather than driving it continuously.[90]

## Layout and shielding

Placement matters. An oscillator serving a specific chip belongs close to it; a 100 MHz oscillator placed at a distance from the device it clocks is poor practice even if the board works.[359] The same applies to schematic placement, where signal flow should run left to right and finding an oscillator and a JTAG header where the input connectors ought to be is a sign of a badly organised drawing.[1129]

Shielding is a functional requirement, not cosmetic. A super-regenerative receiver contains an LC tank oscillator with positive feedback, which genuinely oscillates and, if unshielded, transmits on essentially the frequency the receiver is trying to receive — so two such receivers placed close together will swamp each other.[767] Oscillators are correspondingly found inside metallised cans and machined RF enclosures in commercial designs.[907][1416][492]

## Fault finding

The oscillator is one of the small set of checks made before anything else on a non-functional board: verify power, verify the oscillator is running, then look for activity on the data and display lines.[710] On a microprocessor system the specific question is whether the oscillator starts at all.[97] A loss of supply elsewhere can present as a stopped oscillator — a failed −12 V regulator taken out by a bad power supply stopped an analyser's oscillator working,[538] and a crystal that appeared faulty in a multimeter turned out to be fine, having simply not been receiving power; re-checking the oscillator immediately after force-feeding power to the chip would have found this sooner.[1520] Conversely, oscillation where none is wanted is also diagnostic: a comparator without hysteresis will oscillate around its threshold.[714]

Because the oscillator is a defined, observable node, its presence or absence partitions the fault. If power and clock are both confirmed good and there is still no data anywhere, the remaining suspect is the processor or ASIC itself.[710]

## Oscillators as signal sources

Beyond clocking, oscillators supply the excitation for measurement and modulation. An EPIRB's microcontroller feeds its modulation signal through AC coupling into the transmitter's oscillator, amplitude-modulating it, with a detector tapping the output and feeding it back so the microcontroller can confirm it is transmitting.[368] A PA amplifier uses a local 25 kHz oscillator gated onto the audio path as a signalling tone summed with speech.[354] A bench oscillator's own upper frequency limit can become the limit of a measurement: a high-voltage probe was verified flat only to about 3 MHz because that was as high as the available oscillator would go, with rise time indicating an actual bandwidth near 30 MHz.[85]

Signal generators and function generators are, in specification terms, judged as oscillators, and a mid-priced instrument can carry very good numbers for any oscillator regardless of price class.[497] A separate oscillator is also what makes certain demonstrations possible: the 555 timer April Fools hoax worked by generating a sine wave at 55.5 Hz and about half a volt from a waveform generator, AC coupling it through a concealed switch and wires run under the ESD mat, and soldering it directly to pin 5 of the breadboarded timer — the frequency modulation input.[161]
