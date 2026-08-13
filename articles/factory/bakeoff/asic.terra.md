# asic

An application-specific integrated circuit (ASIC) is an integrated circuit designed for a defined application or set of functions rather than as a general-purpose programmable device.[1019][1150] ASICs concentrate functions such as acquisition, signal processing, display generation, communications, control, and power measurement into dedicated hardware, allowing a product to achieve high performance, lower component count, or both.[149][1693][514]

## Development economics and integration

ASIC development carries substantial non-recurring engineering (NRE) cost and can require years of work before production begins.[1639][148][1032] Once that cost has been absorbed, an ASIC can become relatively cheaper per unit than assembling the equivalent function from purchased ADCs, FPGAs, processors, and supporting components, particularly at high volume.[1639][1018]

The economic case is therefore strongest where volumes are sufficiently large or where the required function is specialized enough to justify dedicated silicon.[1018][1229] A customer may also request a modified version of an existing chip, adding or removing functions to meet requirements such as reduced power consumption, where expected quantities justify the customization.[1229]

ASIC integration can greatly reduce a product’s visible component count: low-cost phones may consist principally of a main ASIC, memory, and an RF chipset, while calculators, keyboards, and portable electronics may centre their operation on one or a few custom devices.[514][1727][633] Older designs were sometimes partitioned across several ASICs when the available gate-array capacity could not accommodate a complete processor or display processor in one device.[663]

## ASICs and programmable logic

An FPGA is a programmable universal device whose digital logic can be configured after manufacture, whereas an ASIC implements a fixed, purpose-designed hardware function.[496][1311] FPGAs are consequently appropriate for lower-volume or changing designs, since implementing custom logic in a gate array avoids the cost and effort of producing a full ASIC.[969][1018]

ASICs trade that flexibility for specialization. An FPGA-based instrument architecture can potentially be altered by firmware or FPGA reconfiguration, while an ASIC-based architecture is constrained by the functions designed into the silicon.[1311][383] Logic minimization remains important within ASICs because unnecessary gates consume silicon area and add propagation delay, reducing the maximum attainable clock frequency.[None]

## Oscilloscope acquisition and display engines

Oscilloscopes are a prominent application of ASICs because acquisition, triggering, waveform processing, measurements, and display updates require sustained high-speed data movement.[148][1545] A conventional architecture can move ADC data through memory to a CPU for processing and screen rendering, making the CPU a bottleneck for waveform-update rate and interface responsiveness.[148]

A dedicated acquisition ASIC can instead process and plot waveform data in hardware and couple the display plotter directly to the LCD, leaving the CPU to perform secondary tasks such as operating-system, file, USB, Ethernet, and control functions.[148] Hardware implementation can permit serial decoding, mathematical functions, FFT processing, search, measurements, and display activity to operate with less performance loss than equivalent CPU-based software processing.[149][594][845]

The MegaZoom 4 oscilloscope ASIC architecture demonstrated waveform-update rates of up to 1 million waveforms per second directly to the display, a capability previously associated with much more expensive instruments.[148] Its architecture allowed hardware serial decoding and other processing functions without the normal software-processing penalty, although the available sample rate, memory depth, and channel pairing still depended on the particular acquisition implementation.[149][704]

ASIC channel organization has practical consequences. Where one acquisition ASIC serves each pair of channels, selecting channels from separate pairs can preserve greater sample rate and memory than selecting both channels within one pair.[792][149] Conversely, a four-channel design sharing a single acquisition resource must divide performance across active channels regardless of which channel numbers are selected.[704]

Dedicated ASICs do not eliminate all processing limits. Enabling computationally intensive functions such as peak processing can reduce waveform-update rate drastically even in a high-performance instrument.[1529] Acquisition architectures also differ in their balance of dead time, display responsiveness, and processing workload; moving common functions into ASIC hardware reduces CPU involvement but does not make all operations cost-free.[1478][1529]

Modern oscilloscope ASICs may integrate analogue front-end and acquisition functions, allowing a high-bandwidth front end to approach a single-chip solution.[1218][1566][1582] The R&S MXO4’s IXP ASIC, for example, is responsible for 4.5 million waveform updates per second and digital triggering.[1545] Tektronix also used an ADC hybrid or ASIC with more than 5 GHz input bandwidth to directly sample RF signals for a 3 GHz spectrum-analysis input.[587]

## Other specialized applications

ASICs are used where continuous, deterministic hardware processing is useful. A power meter can integrate voltage and current at 1 megasample per second in hardware, retaining narrow transient events while the main processor handles the interface and other functions.[1693] A Bluetooth audio processor can combine a DSP core and associated application functions in a purpose-designed ASIC operating at approximately 80 MHz.[1150]

Dedicated ASICs have also been used for video effects, motion-JPEG compression, communications processing, display processing, beamforming, and high-channel-count mining hardware.[598][969][1019][1314][993] Yamaha’s YSS910 devices are custom LSI or ASIC DSPs, each with local memory, and were specified as 44-bit DSPs.[738] Ultrasound equipment combines dedicated ASICs, discrete logic, coprocessors, processors, and memory because beamforming and image processing require extensive parallel processing hardware.[1314]

ASICs can incorporate peripheral and display-control functions that would otherwise need separate chips. In the Amstrad NC100, the principal ASIC operated from a 12.2 MHz resonator and integrated the LCD controller, while the separate CPU performed comparatively little according to the system block diagram.[385] A revised HP-41CV calculator ASIC integrated additional register storage rather than adding separate external memory devices.[582]

## Power, thermal behaviour, and repairability

High-density ASICs commonly require low-voltage core rails, including 1.8 V, 1.2 V, and 1.1 V supplies in digital equipment.[780][1145] Low core voltage is characteristic of modern silicon-process nodes; operation around 0.8 V may be marginal for some processor ASICs.[1383] ASICs may dissipate enough power to require forced airflow, heatsinks, thermal interface material, or substantial power-distribution design.[622][1185][1032]

Thermal inspection can help locate a failed ASIC or abnormal power consumption, but reflective metal surfaces can create misleading apparent hot spots in infrared images.[401] A shorted supply rail shared by multiple ASICs may be difficult to localize because all affected devices can draw substantial current and reach similar temperatures.[401][405] Failure of proprietary ASICs can make repair impractical when replacements, documentation, or compatible donor parts are unavailable.[401][710]

Branded or unidentified chips should not automatically be assumed to be ASICs: manufacturers may relabel standard microcontrollers or other commercial devices, and a chip-on-board assembly can conceal a processor, memory, or other conventional component rather than dedicated custom silicon.[330][None][391]