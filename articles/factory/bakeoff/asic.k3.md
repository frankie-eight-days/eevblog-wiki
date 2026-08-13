# asic

An application-specific integrated circuit (ASIC) is a chip designed from the outset to perform one fixed function — waveform acquisition, serial protocol decoding, DSP, power integration — rather than a general-purpose function defined later by software or configuration.[496][969] Its engineering significance lies in the trade it forces: enormous up-front development cost and multi-year effort, exchanged for real-time performance and per-unit cost that off-the-shelf parts cannot match.[1639][1032][148]

## Economics and development cost

The central economic fact of an ASIC is its non-recurring engineering cost. Once that NRE has been paid for and absorbed, the ASIC becomes cheaper than the alternative of buying equivalent ADCs from Texas Instruments or Analog Devices and FPGAs from Xilinx.[1639] Development timescales are long: the Keysight MegaZoom 4 chipset took over five years to develop and was a complete ground-up redesign with all-new ASICs, even though MegaZoom 3 already existed.[1032]

The payoff is amortization. Once the hard design work is done, the capability can be pushed down into low-end products: a waveform update capability that previously cost $10,000–$20,000 became available in scopes costing little over $1,000 because the same ASIC technology filtered down the range.[148][143] Manufacturers recovering NRE on a new chipset tend to debut it in higher-priced models first before releasing cheaper derivatives.[1146][1566]

Volume is the gating factor. A logic analyser expected to sell in the hundreds or low thousands does not justify rolling a custom ASIC; an FPGA is the correct choice at that volume, and an ASIC only makes sense at genuinely high volume.[1018] Between full custom silicon and off-the-shelf parts sits the semi-custom path: a sufficiently large customer can commission a variant of a silicon vendor's existing chip — features added or removed to suit the application — provided the order quantity justifies it.[1229] Regulated products extend the timeline further: an implantable medical device requires not only the ASIC design but qualification of every single part, stretching conception-to-market to roughly five to eight years, and such devices use ASICs rather than any general-purpose microcontroller.[1027]

## Oscilloscope acquisition ASICs

Oscilloscopes are the corpus's dominant ASIC case study. In a traditional architecture, the ADC feeds an FPGA or custom chip, data is funnelled into external memory, and the CPU reads that memory and updates the display — making the CPU the bottleneck. An acquisition ASIC such as MegaZoom 4 eliminates this by coupling a display plotter directly onto the LCD, relegating the CPU to secondary functions: math, measurement and search acceleration, Ethernet, USB, and file handling.[148] The result is one million waveform updates per second directly onto the display, a rate unachievable with a traditional CPU-driven approach.[148] Because serial decoding, math functions, FFTs, cursors, and measurements are all executed in hardware on the ASIC in real time, enabling them carries no update-rate penalty.[149][594][1478]

The architecture is not magic, however. Enabling extra processing functions can still collapse the update rate — on the Rohde & Schwarz MXO4, switching on peak processing dropped the rate from 47,000 to 60 waveform updates per second.[1529] Conversely, scopes without dedicated acquisition ASICs, such as the Tektronix MDO3000, see their update rate collapse when digital channels, FFT, or serial decoding are switched on.[701]

ASIC ownership has become a marker of a first-tier oscilloscope manufacturer. Rigol developed its Phoenix chipset — a custom front-end ASIC plus an acquisition chip — placing it among the major players, and later pushed the same front-end ASIC into the $299 DHO800 series.[1218][1146][1566] The Rohde & Schwarz MXO4's ASIC is responsible for 4.5 million waveform updates per second as well as the digital triggering system.[1545] Later designs integrate further still, combining the acquisition ASIC and dual 14-bit ADCs into a single device approaching an "oscilloscope in one chip."[1639]

A practical consequence of per-pair ASIC architecture is a channel-selection trick: where one ASIC serves each pair of channels, using channels 1 and 3 (or 2 and 4) preserves full sample rate and memory depth, whereas enabling two channels on the same pair halves both.[792][149] Designs that spread a single ADC across all four channels allow no such escape.[704]

## ASIC versus FPGA and gate arrays

An FPGA is a universal programmable chip with no intended function at purchase, the closest thing available to designing a chip completely from scratch without doing so.[496] Gate arrays occupy the historical middle ground: customizable logic that avoids the cost of spinning a full ASIC, making them much cheaper and simpler for specialized low-volume equipment.[969] The 1973 Compucorp 322G calculator split its processor across four separate gate-array-type devices because the available logic capacity per chip was insufficient for a single device.[663] The Sinclair ZX81's "uncommitted logic array" (ULA) performed a similar integration role, collapsing the chip count by roughly an order of magnitude versus the ZX80 and enabling its low price.[872] A further modern consequence of mature ASIC chipsets is that what once demanded a board full of programmable logic — recovering a VGA clock, for instance — is now a single purchasable chip that lets anyone lay out a working board in a day.[694]

## Board-level identification

Vendor branding or removed markings are not proof of custom silicon. Chips with laser-etched markings are almost always commercial devices with the part numbers obscured to impede reverse engineering, not ASICs.[391] A company-branded chip is frequently an off-the-shelf microcontroller custom-branded by the manufacturer once order quantities are large enough.[330] The counter-test is structural: a daisy-chained JTAG header across several large devices identifies them as FPGAs, not in-house ASICs.[864]

## Thermal behaviour, power, and repair

High-performance ASICs run hot. The main ASIC die in a Tektronix TDS3054 reaches roughly 100 °C in operation;[565] around 55 °C is unremarkable for an instrument ASIC;[593] and forced airflow over the acquisition ASIC is mandatory in at least one design, which shuts itself down within minutes if fan cooling fails.[622] High-density modern ASICs run on very low core rails — 1.1–1.2 V for advanced logic, 1.8 V for other custom ASIC cores.[1145][780] Power integrity around them is a real design problem: switching supplies feeding high-power ASICs in a high-end function generator created spurs that coupled into the 120 MHz output, requiring a low-noise power supply redesign.[1032] At the low end, a typical processor ASIC node begins to fail as its supply falls below roughly 0.8 V.[1383]

For repair, a dead ASIC is usually the end of the line. In one oscilloscope, a shorted 3.3 V rail traced to four ASICs all at a uniform temperature — dissipating the excess power evenly with no localisable hot spot — led to the conclusion of four identically dead devices and an unrepairable board.[401] Constant-current fault-finding is also confounded on such boards because the ASICs' own large operating current produces voltage drops across the plane regardless of the fault.[401]

## Historical and niche examples

- The HP-41CV calculator integrated its extra registers by re-spinning the ASIC itself relative to the standard 41C, rather than adding external memory chips.[582]
- Sony routinely rolled its own silicon, from the transistor-array ASIC in the original TPS-L2 Walkman to custom video-effects chips in broadcast equipment.[752][598]
- Yamaha's YSS910 devices, claimed as the world's first 44-bit DSPs, were deployed ten to a mixer in the DME32, each with local memory.[738]
- The classic Fluke 27 multimeter ASIC remained in manufacture until at least 2005 because the design continued to use it.[372]
- Cryptocurrency mining made ASICs a volume commodity: one scrypt/SHA-256 mining blade carried 40 ASICs at 140 W total draw.[993]