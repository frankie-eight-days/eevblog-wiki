# amplitude modulation

Amplitude modulation (AM) carries information by varying the amplitude of a higher-frequency carrier in step with a modulating signal, leaving the carrier frequency itself untouched.[5][368] In its simplest hardware form it needs almost nothing: a transistor switched on and off across a resonant circuit is enough to impress one and zero onto a carrier.[539] The scheme survives in analog television visual carriers, RFID and NFC cards, distress beacons, utility control receivers, and — in a different guise entirely — as the bench signal used to stress oscilloscope displays.[569][539][889][368][1457]

## Depth, sidebands, and the modulation index

Modulation depth is expressed as a percentage. At 100% the envelope swings fully to zero between peaks, and drives beyond 100% — 110% or 120% — push the signal into overmodulation.[502][474] In the frequency domain the modulating tone appears as sidebands flanking the carrier. Their visibility is a resolution-bandwidth problem: a 1 GHz carrier at −100 dBm modulated 10% at 1 kHz shows its sidebands clearly on an analyser with a 10 Hz resolution bandwidth and a low noise floor, while an instrument limited to a 100 Hz resolution bandwidth and a worse noise floor resolves the same signal only faintly.[891] Depth also sets the floor for what a digitiser can see at all: a 10 MHz sine with 50 kHz AM at a modulation factor of 0.02% sits below the threshold an 8-bit front end can resolve in an FFT.[1566]

## The standard oscilloscope test signal

A 1 MHz sine carrier modulated 100% by a 1 kHz sine is Dave Jones's standard test signal for evaluating intensity-graded, or so-called digital-phosphor, oscilloscope displays.[792][795][876][1220] The signal works because its envelope produces a dense range of trace densities on screen, exposing whether a scope renders true intensity grading or merely draws a flat trace.[795][591] The same waveform is applied across generations and price points, from a $19 analog scope to modern super-phosphor and 12-bit models.[502][1146][1582][1260]

Two instrument limitations show up immediately. First, most scopes cannot trigger stably on the waveform, because the trigger circuit sees many qualifying edges per modulation cycle; the fix is trigger hold-off set to roughly the modulation period.[480][1260][1582] Second, the display result is strongly dependent on acquisition memory depth — at 50k points there is simply not enough data to build up the intensity artifacts, and in a fast-acquisition mode that sacrifices memory the modulation is only barely discernible.[792][617] An amplitude-modulated pulse waveform is harder still, testing trigger capability and memory depth at once; a scope set to only 1,000 samples cannot represent it.[617]

## Generating AM on the bench

Function generators have offered AM alongside FM for a long time, historically as a front-panel switch selecting between the two with a separate level control for depth.[5] Setting the standard test signal on a modern generator means selecting AM modulation, an internal source, an AM depth of 100%, and an AM frequency of 1 kHz.[797] Built-in generators on oscilloscopes typically expose AM, FM and FSK, with a choice of sine, square or ramp as the modulating waveform plus depth and frequency.[1146][1529][383] Coverage is uneven: some instruments provide AM and FM but omit FSK, and internal modulation without an external modulation input is common.[1638][383] Rudimentary implementations that offer sweep, burst, PWM, FM and AM but little control over the surrounding output configuration are still shipped on otherwise capable hardware.[1701] Older bench equipment could be more generous, exposing an external amplitude modulation input feeding a discrete amplitude modulator ahead of the output amplifier.[1724] At the high end, an amplitude-modulated sine on one channel can be merged with a quadrature-amplitude-modulated signal on another and routed to a single output.[cziiWo6Uh5M]

On the receiving side, spectrum analysers and VNAs with modulation-analysis modes can demodulate an AM carrier directly, though AM and FM demodulation are frequently sold as separate paid options.[1101] A generator feeding a receiver makes the effect audible: a 27 MHz carrier amplitude modulated at 1 kHz produces a clear tone, and increasing depth from 10% through 20%, 30% and 40% increases the recovered tone's level correspondingly.[839]

## Analog television transmission

In analog TV the video and audio paths remain separate through essentially the entire transmitter chain and are modulated by different schemes: audio by frequency modulation, video by amplitude modulation.[569] Because the tube modulating the visual carrier uses AM, its high-voltage supply must be DC rather than AC — any supply hum would otherwise be superimposed directly onto the picture as an amplitude variation indistinguishable from the video signal.[569] The three-phase supply feeding such a tube is rectified for exactly this reason, while the filament runs at roughly 6 V at 130 A.[569]

## Load modulation in RFID and NFC

Passive RFID and NFC tags have no transmitter. They reply by amplitude modulating the reader's own field, a technique often described as backscatter or load modulation. A modulation transistor sits directly across the tag coil; switching it does not short the coil out but changes whether the coil is damped or undamped, and the chip simply turns that transistor on and off to send ones and zeros.[539] At 125 kHz the tag modulates the carrier directly, and the reader demodulates and decodes the returned data.[539]

At 13.56 MHz the same principle is formalised. Under the ISO 14443 protocol used by contactless credit cards, the card loads its coil to amplitude modulate the field at a subcarrier frequency of 847.5 kHz; cursor measurement of a captured return gives 847.46 kHz, matching the standard.[889] The coupling here is magnetic, not radiative — the coils form a transformer rather than a pair of antennas.[889]

## Re-radiation and passive surveillance devices

The same passive principle underlies certain surveillance hardware. A countersurveillance monitor uses a pulse-position-modulated square wave at an undisclosed preset frequency to switch a FET; when the unit is illuminated by a CW signal from a nearby radar, it amplitude modulates that incoming signal with the square wave, making the device a re-radiator in the manner of an RFID tag.[956] The historical antecedent is a Soviet device containing no active electronics and no power supply at all: a capacitive membrane acting as a microphone modulated a quarter-wavelength antenna at around 330 MHz, so that a radar illuminating it received a tiny reflection carrying room audio.[956]

## Other applications

An emergency position-indicating radio beacon generates its homing modulation in the microcontroller, AC-couples it into the oscillator which amplitude modulates the carrier, and passes the result to the RF transmitter; a detection circuit taps the transmitted signal and feeds it back so the microcontroller can confirm the correct data is actually going out.[368]

Ripple-control and load-management receivers in electricity meters use an amplitude-modulated signal on the mains distribution network, recovered by a conventional AM receiver chip that hands a data stream to a microcontroller for decoding.[1457]

Amplitude modulation also appears as an explanatory frame well outside communications. In a spin-qubit system, the amplitude of an applied oscillating magnetic field sets the rate at which the spin rotates between states, so that a 1 microtesla field at 39 GHz yields a 28 kHz rotation rate — a relationship characterised as amplitude modulation, with an observed rate near 200 kHz implying a field somewhat under 10 microtesla.[1594]
