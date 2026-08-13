# spectrum analyzer

A spectrum analyzer is an RF test instrument that displays signal amplitude against frequency, operating in the frequency domain where an oscilloscope operates in the time domain.[1661] Functionally it is a specialized radio receiver: "a spectrum analyzer is really just a radio receiver" in which "the last detector stage is a logarithmic amplifier instead of a linear voice detector", giving the instrument its wide decibel-scaled dynamic range.[575] It is the standard tool for measuring carrier frequencies, harmonics, spurious emissions, modulation, noise floors, and filter responses, and is central to EMC pre-compliance work.[343][548]

## Operating principle

The classic swept-tuned architecture follows a superheterodyne signal flow: a 50-ohm RF input feeds an input attenuator, then filtering, then a mixer driven by a swept local oscillator, producing an intermediate frequency that is filtered by the resolution bandwidth (RBW) filter, detected, and displayed.[391][207] Modern instruments are "all digital IF": the IF output is digitized by an ADC rather than detected in analog circuitry, in contrast to older fully analog designs.[1101] In one representative low-cost design, a 40 MSa/s ADC constrains the IF baseband to below 20 MHz by the Nyquist criterion.[892]

Because relative magnitudes span many decades, the vertical scale must be logarithmic; a linear voltage scale is unusable for typical signals.[845] Resolution bandwidth trades directly against sweep speed: a narrow RBW such as 300 Hz sharply slows sweep and even front-panel cursor response, while widening to 10 kHz restores near-real-time behavior.[645] The same trade-off applies in RF-scanner instruments modeled on spectrum analyzers, where a wider bandwidth setting yields faster scans.[795]

## Internal construction

Spectrum analyzer main boards are laid out as identifiable functional blocks, typically with distributed-element filters and machined shielding between stages.[1109] Common construction elements include:

- A 50-ohm input section with relay or solid-state switching (e.g. SOT23-6 switch packages with internal 50-ohm termination) to insert or bypass a preamplifier.[1109][892]
- Input protection ratings that vary by instrument; one low-cost model specifies a maximum input of +20 dBm and 50 V DC, unusually tolerant, while others are easily damaged and require care when connecting a device under test that may carry DC or transient energy.[323][548]
- Machined aluminum shielding enclosures in which each circuit block sits in its own milled cavity, with gold-plated contact surfaces and RFI gasketing, so that signals pass between blocks only through machined slots — a technique found in virtually all gigahertz-range RF equipment.[892][1101][470]
- A physically separate tracking generator board, since crosstalk between the sweep generator and the measurement path must be eliminated.[892][470]
- A local oscillator/VCO, for example a Hittite HMC429 covering 4.45–5 GHz in one design.[587]

## Swept, real-time, and direct-sampling designs

A traditional analyzer sweeps a resolution bandwidth filter across the span sequentially. A real-time spectrum analyzer instead captures contiguous chunks of spectrum — 85 MHz or 110 MHz wide in one product line — performing up to 50,000 discrete Fourier transforms per second and overlaying the results in a persistence display where color indicates spectral intensity, allowing transient signals to be seen.[207] Real-time instruments exist up to at least 20 GHz bandwidth with roughly 292,000 captures per second.[358]

Advancing ADC sample rates have pushed direct RF sampling into the single-digit gigahertz range, eliminating the mixer/LO chain below that frequency.[1032] The Tektronix MDO3000 exploits this by feeding its RF front end straight into the oscilloscope's existing high-sample-rate ADC: high oversampling yields roughly 57 dB of signal-to-noise improvement and a 107 dB noise floor from an 8-bit converter, where a conventional analyzer sampling at 20 MSa/s would need a 12.5-bit ADC for equivalent performance. The incremental parts cost of the 3 GHz spectrum analyzer function was estimated at US$25–30, though the shared ADC means the RF channel and analog channels cannot be captured simultaneously.[587][701]

## Tracking generators and network analysis

A tracking generator is a swept source locked to the analyzer's sweep, allowing direct measurement of a filter's frequency response — effectively a scalar network analyzer.[343][396] This is the easy way to obtain a Bode-style amplitude-versus-frequency plot of an RF filter; equivalent measurements without a tracking generator are possible but considerably harder.[343][396] Because the tracking generator in a low-cost instrument costs only a couple of hundred dollars, its output is not ruler-flat across the range — a measured low-pass filter response may show stopband recovery of 10 dB or more at wide spans that is an artifact of the generator rather than the device under test.[343] The tracking generator option is cheap enough relative to its utility that omitting it when buying an analyzer is poor economy.[323][891]

The Siglent SVA1015X extends this idea into a two-port vector network analyzer by multiplexing the existing spectrum analyzer measurement hardware to measure power reflected back from the tracking generator output, adding only directional couplers, switches, and extra coax plus software — a low-cost way to obtain S11 magnitude and phase in a conventional analyzer form factor.[1101]

## Oscilloscope FFT versus dedicated instruments

An oscilloscope's FFT math function converts it into a rudimentary spectrum analyzer, with usefulness determined by the number of FFT points and the quality of the implementation; a 128k-point FFT can give excellent resolution, while small-point-count implementations are little more than toys that show a signal exists but cannot characterize it.[845] As engineering judgment, "there's really no substitute for a proper spectrum analyzer" among scope FFT functions.[143] Nonetheless, a fast, high-point-count FFT combined with a US$10 DIY near-field probe is adequate for basic EMC sniffing without a dedicated analyzer, and an SDR USB dongle can serve as a "poor man's spectrum analyzer".[1188]

Mixed-domain oscilloscopes occupy a middle position. The Tektronix MDO4000 contains a true spectrum analyzer RF front end with an N-connector input — "It is not just an FFT function and that can't be stressed enough" — integrated with the time-domain acquisition so the RF spectrum can be correlated with individual time points and used as a trigger source.[199] The later MDO3000 achieves a 3 GHz analyzer almost for free in hardware by reusing the scope ADC, with performance comparable to entry-level standalone analyzers, but sacrifices simultaneous RF/analog capture.[587]

## EMC pre-compliance testing

A major application of low-cost spectrum analyzers is in-house EMC pre-compliance testing, avoiding repeated multi-thousand-dollar laboratory sessions by allowing before-and-after comparison of design changes.[891][548] For conducted emissions, a line impedance stabilization network (LISN) is inserted in series with the supply cable, presenting a standardized 50-ohm impedance as specified by CISPR and coupling the noise to the analyzer's RF input through a BNC port, with gas discharge tube and MOV protection for the analyzer front end; the setup sits on a single large ground plane, since trailing cables off the plane corrupt the measurement.[548][546][993] For radiated troubleshooting, near-field probes — H-field loops for magnetic and E-field tips for electric measurements, typically through a 20 dB, 3 MHz–3 GHz preamplifier — locate offending traces and components; H-field probes are orientation-dependent, picking up fields in the loop plane, which can be exploited to isolate sources.[694][1176][1273] An industry-standard 120 kHz RBW EMI filter option and quasi-peak detection give ballpark agreement with laboratory measurements.[1176]

A cheap general-purpose analyzer will not reproduce the results of a US$50,000 EMC measurement receiver, but gives a reasonable indication sufficient for pre-compliance iteration.[548] True EMC test receivers span extremely wide ranges (one example covers 20 Hz to 40 GHz) and implement standard-specific detectors — quasi-peak, averaging, and RMS.[202] Related knowledge: spread-spectrum clocking deliberately dithers a system clock to smear a spectral peak — a flat line at, say, 100 MHz becomes a broad hump — lowering peak emitted energy to pass EMC limits.[111]

## Operation and measurement practice

- Unlike on oscilloscopes, where auto-set is disdained, the auto button on a spectrum analyzer is a reasonable way to get a first look at an unknown signal.[368]
- Zero-span mode stops the sweep at a fixed center frequency so amplitude versus time can be observed, allowing modulation to be examined.[368]
- Burst or intermittent transmitters are captured with single-shot trigger sweep modes; carrier harmonics can be found simply by re-centering on multiples of the fundamental.[368]
- Noise-density measurements require selecting a power spectral density measurement type, not merely changing vertical units, to obtain volts-per-root-hertz scaling.[1328]
- Low-cost portable spectrum analyzers have historically been used with simple antennas — even a dangled wire — to verify transmitter carriers, e.g. a 27.15 MHz CB carrier or a 121.5 MHz EPIRB burst.[839][368]
- Sensitivity of a simple homebrew design is modest: roughly 10–20 microvolts, compared with microvolt-level ham receivers.[575]

## Frequency coverage

General-purpose benchtop spectrum analyzers are RF instruments; a typical low-cost unit covers 9 kHz to 1.5 GHz and is of no use at audio or other low frequencies, where oscilloscope-based methods or a frequency response analyzer are needed instead.[396] Dynamic signal analyzers — often called FFT analyzers — fill the low-frequency gap, operating down to DC for vibration and acoustic measurement.[1443] At the upper end, handheld field instruments reach 20 GHz (the Agilent N9344C covers 1 MHz–20 GHz), and real-time and calibration-lab analyzers extend to 26.5, 40, or 50 GHz.[470][202][1041]

## Historical and homebrew instruments

In the late 1970s a capable Hewlett-Packard spectrum analyzer was unaffordable to individuals, prompting homebrew construction: one surviving example is a dead-bug/Manhattan-style receiver design with a 10.7 MHz IF and logarithmic detector, roughly 70 dB of display range, and a top frequency near 200 MHz, used successfully for repeater cavity tuning and for tracking a 160 MHz microprocessor leakage failure in a commercial traffic-light controller down to the offending board.[575] Later kit designs repurposed electronically tuned TV tuners as the front end, with the builder supplying the back end.[575] A low-cost commercial alternative of the kit era was the Dick Smith VHF/UHF spectrum analyzer, used with an oscilloscope for radio alignment.[KKEYAdXEW-M]

## Representative instruments

| Instrument | Range | Notes |
|---|---|---|
| Rigol DSA815 | 9 kHz–1.5 GHz | Tracking generator option; +20 dBm / 50 V DC max input; ~US$1,200–1,500 with TG [323][891] |
| Siglent SSA3021X | 9 kHz–2.1 GHz (software-upgradeable to 3 GHz) | US$1,600 base; US$169 TG option [891] |
| Siglent SVA1015X | 9 kHz–1.5 GHz | US$1,395; optional software-licensed two-port VNA [1101] |
| TTI PSA1301 | to 1.3 GHz (2.7 GHz model also) | Handheld, Palm-platform-based field analyzer [358] |
| Agilent N9344C | 1 MHz–20 GHz | Handheld field unit, ~A$18,000 [470] |
| Rigol RSA5000 | to 6.5 GHz | Real-time class [1686] |
| Rigol N series | — | Real-time with single-port VNA, two S-parameters and Smith chart, built-in return-loss bridge [1468] |
| Uni-T 3000 series | to 3.6 GHz | 1.5 GHz 1000 series below it; 26 GHz model in development [1625] |