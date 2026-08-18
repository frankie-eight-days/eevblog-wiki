# 555 timer

The 555 is an eight-pin bipolar timer integrated circuit, arguably the most famous chip in electronics, built from a handful of general-purpose analogue blocks that can be wired into a very large number of timing and oscillator circuits.[555][1054] It was developed in 1971 by Hans Camenzind, then working as a contractor at Signetics, and has remained essentially unchanged in function since.[1746] An early-2000s figure put annual sales at around a billion parts a year, and it is still produced in enormous volume.[555][1746]

## Origin and naming

Camenzind's timer grew out of a circuit he had been using as the timing source for phase-locked loops.[1746] Management at Signetics questioned why a standalone timer chip was needed at all; the marketing department disagreed, and the project went ahead.[1746] The first version was taped out in mid-1971, hand-cut in rubylith because no CAD tools existed, and it worked — but it required nine pins.[1746] A redesign in October 1971 produced the eight-pin DIP part that became the standard.[1746]

Signetics did not patent the design.[1746] By 1972 there were already a dozen different suppliers, and the part was being shipped and cloned from early that year.[1746] It reached Australia quickly: an advertisement in *Electronics Australia* of November 1972 already promoted it as an industry standard and as "the timer of a thousand and one uses".[1746] It became the de facto standard timer almost immediately.[1746]

The name was assigned by Signetics marketing manager Art Fury.[1746] Camenzind consistently stated publicly that 555 was an arbitrary number, next in a sequence, and unrelated to the internal circuit.[160][555] The internal divider nevertheless contains three nominally 5K resistors, which is the basis of the persistent claim that the number was not a coincidence.[160][555][1746] The CMOS variant does not use the same values.[160]

Camenzind, who remained involved in the electronics community until his death, is credited as the inventor of a part still selling in the millions decades later.[336]

## Internal architecture

The chip divides cleanly into functional blocks: a threshold comparator, a trigger comparator (sometimes called the upper and lower comparators), a flip-flop, an output driver, an open-collector discharge output, and a reset input tied into the flip-flop.[555] A resistor divider of three nominally 5K resistors generates the comparator reference voltages, setting the threshold at two-thirds of the supply and the trigger at one-third.[555] With a 9 V supply, the threshold sits at 6 V.[555]

The control voltage pin, pin 5, is connected directly to one of the divider taps, which is why it can be used as a modulation input — driving it moves the comparator thresholds and shifts the timing.[161][555][NvIv-0-R6qQ] The recommended configuration places a bypass capacitor of around 10 nF from pin 5 to ground; the application note calls for it, and omitting it leaves the reference nodes exposed to noise and coupling.[160]

In normal operation the threshold pin (pin 6) follows the exponential charging waveform of the timing capacitor, the discharge pin (pin 7) sinks that capacitor when the flip-flop resets, and the output (pin 3) toggles between rails.[555][392] The internal design leans heavily on constant-current sources, an arrangement common in comparator-style bipolar chips, which is what permits some of the direct transistor connections in the output stage.[555]

The transistor-level schematic reproduced in the original Signetics data sheet remains the canonical reference for the internal circuit.[555] A transistor-level 555 model also ships as one of the bundled examples with the LTspice circuit simulator, allowing the internal nodes to be probed in simulation.[555]

Discrete transistor-level replica kits exist that break the die out into physically separated blocks — threshold comparator, trigger comparator, flip-flop, output — so each node can be probed with clip leads.[555] Such a replica is only functionally similar rather than identical: process differences between discrete transistors and the monolithic part are unavoidable, and preferred-value substitutions are common, since 5K is not an E12 value and kits typically use 4K7 instead.[555] Two 10K resistors in parallel give an exact 5K if authenticity matters.[555]

## Timing configurations

**Monostable (one-shot).** A resistor to the supply, a capacitor to ground, and the discharge and threshold pins tied together form the classic one-shot.[1054] A negative-going pulse on the trigger pin starts the timer, which emits a single output pulse whose width is set by the RC time constant.[1054] The standard formula is 1.1 × RC.[1406]

**Astable.** With pins 8 and 4 to the supply and pin 1 to ground, the timing capacitor charges through the timing resistors toward the threshold voltage and is then discharged, giving continuous oscillation.[160][555] The frequency is readily made adjustable by putting a pot in the charging network.[160] The 555 is not an especially stable oscillator, and measured frequency benefits from averaging.[160]

**PWM.** The classic pulse-width-modulation configuration uses an adjustment pot and two steering diodes so that the charge and discharge paths are separated, with the pot setting the split between them.[392] In practice this gives close to the full range without quite reaching the endpoints: one such circuit swept from 8.8% to 99.6% duty cycle.[392] The pot sets both the frequency and the duty cycle in this arrangement.[392] Because the drive stage may be a PNP output transistor, the duty cycle presented to the load can be inverted relative to pin 3.[392]

**Variable-pulse-width sensing.** Replacing the monostable's timing resistor with a potentiometer converts shaft or lever position directly into pulse width.[1054] This was the basis of the analogue PC joystick: the joystick pots, ranging up to around 120K, fed the timing network, and the host measured the resulting pulse length in software — no ADC required, at a time when microcontrollers did not have converters built in.[1054] The scheme was cheap enough that it survived integration into motherboard chipsets, and software could not distinguish a 555-based game adapter from a later ramp-generator-and-comparator implementation as long as the read and write addresses matched.[1054]

## Supply range, variants, and limits

The bipolar part operates down to about 4.5 V.[1653] Below that the internal threshold voltages, which scale with the supply, fall far enough that oscillation stops.[1653] The CMOS variant operates from lower supplies, and also addresses the shoot-through current on the bipolar output stage and the quiescent current consumption of the original.[1653][1746]

Multi-timer packages exist: the 556 is the dual and the 558 the quad.[1053] A space-rated variant is available.[1746]

One practical trap appears when substituting parts or building replicas: where the reset pin would normally be tied directly to the supply pin, some equivalents require a series resistor of around 100K if VCC exceeds 6.5 V, so the substitution is not unconditionally drop-in.[555]

## Design practice

For pulse stretching — holding an indicator on after a very short input event — a 555 one-shot is one option, but it needs a fair number of external parts; a 74HC123 retriggerable monostable is the alternative, and simpler discrete solutions may beat both.[471] Where a circuit needs any switching source, such as the drive for a diode-and-capacitor charge-pump voltage inverter, a 555 serves as well as a microcontroller or a tapped DC-DC switching node.[483] The chip's slow edges and modest currents make it entirely suitable for breadboard construction, unlike fast switching-supply work.[500]

Dave Jones's first paid design job, at around 12 or 13 years old, was a multi-channel 24 V to 12 V converter box for a tow truck that used a 555 to flash the lights.[74-KI3DLdc4] Choosing a 555 over a more specialised timer chip attracts criticism, but the part's availability, low cost, and familiarity generally justify it.[74-KI3DLdc4] It is expected to remain in use for decades to come.[97]

A claimed hidden Easter egg — an astable running at 55.5 kHz with pin 5 left unbypassed, apparently self-modulating at 55.5 Hz — was a fabrication, staged with a concealed second oscillator injecting a 55.5 Hz sine wave through wires run under the bench mat.[161][200] No such behaviour exists in the part.[161]

## In production equipment

The 555 turns up throughout vintage computing and instrumentation. Old PCs of the 1970s and 1980s used it for one-shot and general timing duties.[1054] The IBM PCjr carried a 558 quad 555 for its joystick port.[1053] The Apple IIc used both a 555 and a 556.[788] The Amiga 500 contained one.[438] A retro Iskra multimeter includes a 555 alongside its Intersil converter and 4511 display driver, with date codes placing manufacture in 1980.[482] Aircraft autopilot hardware has been found with 555s date-coded to 1973 and 1974.[815]

It also persists in equipment built to avoid digital control entirely: an analogue ramp-and-temperature controller used a 555 together with 4000-series CMOS counters to perform all ramping and timing without a processor.[hVIo7vmIExw] Automotive tail-light assemblies have used a 555 alongside constant-current drivers.[1190] It is common in products that need a blinking LED purely to indicate activity, in one case a 555 running from a 7809 regulator driving an LED and nothing else of consequence.[1049] Touch-sensitive tools often implement a retriggerable monostable that the 555 could equally have provided.[1113]

Instrumentation for bench work is built around it too: an alkaline-battery leakage test rig required three 555s to generate its pulsed load, assembled from a scrounged single part plus a 556 dual.[1653] A decade capacitance box is useful for exactly this kind of work — setting 555 timing, laying clock edges, and one-shots.[510]

## As a teaching part

The 555 is one of the first chips a hobbyist encounters, and it remains a standard fixture of beginner kits: electronic dice built from a 555 and a 4017, LED flashers, and educational bundles built around a single timer and a handful of passives.[555][353][964] Forrest Mims's *Engineer's Mini-Notebook* series devoted a volume to 555 timer IC circuits, hand-drawn and still relevant.[733][1034] Magazine literature from the same era covered it exhaustively, including half a dozen different ways to drive a speaker from one.[142][1194] Oscilloscope education packages ship 555 lab exercises complete with schematic and formula.[MguJvnyX4fc]

Its pedagogical value is not sentimental: the RC time constant that governs it appears everywhere in electronics, and building an astable on a breadboard and having to troubleshoot it teaches the fundamentals that no amount of module-level assembly does.[1406][zyuRcsM0gjI] A well-stocked hobby bench is expected to have a few in the junk box alongside 4000- and 74-series logic and basic op-amps.[107][168]
