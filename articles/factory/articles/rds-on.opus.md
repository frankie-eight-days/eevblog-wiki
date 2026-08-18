# rds on

RDS(on) is the resistance measured between the drain and source terminals of a MOSFET when the gate is driven hard enough to turn the device fully on.[1736][1461][931] The name comes from the two terminals it is measured across, with the gate acting as the control element.[1736][1461] It is the parameter that decides how much voltage a switching MOSFET drops and how much power it burns, and alongside drain-source voltage rating and current rating it is one of the three specifications that matter for a device used purely as a switch.[1461][1387]

A MOSFET switched on behaves as a resistor rather than as a saturated junction, and RDS(on) is the MOSFET counterpart of VCE(sat) in a bipolar transistor.[1736] The much lower on-resistance available from MOSFETs is a principal reason they displaced BJTs in switching roles: lower on-resistance means lower voltage drop, and therefore more current and more power handling from a given package size.[1736]

## Dependence on gate drive

RDS(on) is not a single number; it is always quoted at a specified gate-source voltage, and data sheets conventionally give two operating points, commonly 10 V and 4.5 V or 5 V.[1461] A part specified at 9 mΩ maximum with 10 V of gate drive typically degrades to something in the region of 15 mΩ when driven from 5 V logic.[1461] Manufacturers also print an RDS(on) versus VGS curve, which shows the resistance rising steeply as drive is reduced; by the time gate drive falls to around 2 V, a typical jellybean part has little left to give.[1736]

Data sheets list both typical and maximum values, and the distinction becomes important when a candidate part is marginal against the requirement rather than comfortably inside it.[1461] Logic-level parts that hold low resistance at reduced drive are the ones worth stocking for microcontroller-driven applications, since a 3.3 V output must be able to turn the gate on by itself.[1736]

## Temperature behaviour

RDS(on) rises as the device heats.[931] Live measurement of a MOSFET in operation shows the effect directly: a device sitting at roughly 3.1 mΩ drifts upward to 3.2 mΩ as it warms.[1753] Any burden-voltage or dissipation figure calculated from a cold data-sheet value therefore describes the best case, valid only at low currents before self-heating sets in.[931]

## Package, dissipation and typical values

For a given silicon technology, moving up in package size buys both lower RDS(on) and greater power dissipation capability, because there is more surface area to get the heat out; the step from SOT-23 to SO-8 is the routine example.[1736] Dissipation follows directly from the on-resistance and the drain current as an I²R loss.[1736]

The spread across ordinary parts is very wide:

- Small-signal jellybean N-channel devices in SOT-23 sit around 2.4 Ω at VGS of 10 V, advertised as 2.5 Ω, which is high for a MOSFET and rises further at lower gate voltages. Such a part is adequate for a couple of hundred milliamps and no more.[1736]
- The traditional P-channel counterpart is rated at 50 V with a comparatively wimpy 10 Ω at ±5 V of gate drive and around 130 mA.[1736]
- Better modern SOT-23 parts reach tens of milliohms rather than ohms — around 26 mΩ at 10 V drive and still roughly 48 mΩ at only 2.5 V.[1736] One such device carries 3 A at 2.5 V drive with 24 mΩ typical and 48 mΩ maximum, which works out to only about 0.2 W of dissipation at that current.[1736]
- Larger SMD parts reach roughly 18 mΩ at both 10 V and 4 V of gate drive, with double-digit amp ratings that are impractical to exploit in a SOT-23 outline.[1736]
- A TO-220 part specified at 35 mΩ at 4 V drive and 21 A handles 46 A continuous and 160 A pulsed, dissipating 3.8 W in free air and considerably more once bolted to a heatsink.[1736]

On-resistance is also a headline marketing parameter for high-voltage power devices, where best-in-class RDS(on) and ultra-low gate charge are the claims made for 650 V parts in TO-247 packages.[U_QoWa6qXeo]

RDS(on) is specified for integrated switches as well as discrete devices. Open-drain shift-register drivers, for example, are characterised at around 7 Ω typical with 250 mA of current capability,[952] and the on-resistance of the output MOSFETs inside a display driver forms part of the series-resistor calculation for the segments it drives.[1491]

## Contribution to measurement error

In current-measurement instruments the on-resistance of a range-switching MOSFET adds directly to the shunt and therefore to burden voltage.[931] A big N-channel MOSFET switching a 10 mΩ shunt must have an on-resistance well below that shunt value, otherwise the effective shunt resistance is more than doubled.[931] Because a MOSFET that is on behaves as a plain resistor, it conducts in both directions, which is what allows the same arrangement to measure AC current or to tolerate probes inserted the wrong way round.[931]

The arithmetic is straightforward. On a 5 A range with a 100 mΩ shunt giving 50 mV, a MOSFET of 5 mΩ adds a further 25 mV, and an HRC fuse of perhaps 10 to 20 mΩ cold contributes another 50 mV, for a true terminal burden voltage in the region of 125 mV.[931] The MOSFET's contribution scales with current, so on the 500 mA range the same device drops only 2.5 mV and ceases to matter, while the fixed fuse resistance dominates less and less as the ranges go up.[931]

The same effect appears in battery-profiling instruments where a MOSFET shorts out a high-value sense resistor: the MOSFET's RDS(on) ends up in series with the remaining 100 mΩ sense element and must be calibrated out in software.[1331] A separate sense line would avoid the problem but requires a multiplexer to switch it, which is why the simpler arrangement is common.[1331]

## Choosing a replacement part

For a device used as a switch, essentially every other specification on the data sheet can be ignored apart from voltage, current and RDS(on).[1461] Among parts of comparable voltage and current rating, on-resistance figures almost always land within a fraction of an order of magnitude of one another, and 10 to 20% is near enough for a repair; gate charge and drive capacitance need attention only if a part is unusually bad.[1387] For a 500 V, 18 A power-factor-correction device, matching the voltage rating, the current rating and an approximately similar RDS(on) is sufficient, though a ground-up design would warrant more care.[1387] Voltage rating is the one specification that should never be skimped on.[1387]

Where the original is heavily over-specified for its application, a substitute with somewhat higher on-resistance is acceptable: a MOSFET rated at 12 A but never seeing anything close to that will run slightly warmer without the difference being detectable by hand.[1460][1461] Replacing a 17 A part with a 30 V, 12 A device pulled from scrap is on this basis unremarkable.[1461]

The difficulty in parametric searching is rarely RDS(on) alone but the conjunction of constraints. Finding another MOSFET with integral ESD protection is easy; finding one in the same package, at the same voltage and current, and with comparable RDS(on) as well, can prove impossible.[1461] Parametric tables compound the problem, since an on-resistance column expressed in milliohms is easily misread as a current rating at a glance.[1461]
