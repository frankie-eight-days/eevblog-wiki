# chopper amplifier

A chopper amplifier is an operational amplifier that continuously measures and nulls its own input offset voltage, and so behaves like an ordinary op amp except with a ridiculously low offset.[24] The same part is commonly called an auto-zero amplifier or a zero-drift amplifier; there is a real architectural distinction between true chopping and auto-zeroing, but in practice the terms are used interchangeably for the whole family.[24][1328][651] Where a general-purpose op amp might carry ten millivolts, one millivolt, or at best a tenth of a millivolt of offset, a chopper gets down to around one microvolt or a tenth of a microvolt — the difference between usable and useless in high-precision DC and low-frequency work.[24]

## How the nulling works

The mechanism is not magic: it amounts to storing charges on capacitors and swapping between them.[24] The part contains two amplifiers, a main amplifier A and a second amplifier B, each with its own offset voltage, plus four internal switches.[24] In one phase, the second amplifier measures the main amplifier's VOS and stores the result on a hold capacitor, which is fed back into the main amplifier to cancel that offset.[24] The switches alternate between two phases at a fixed frequency, alternating which of the two amplifiers is being nulled — so the correction loop also cancels the offset of the amplifier doing the correcting.[24] The end result is that the main amplifier's offset voltage is effectively canceled out entirely.[24]

The internal details are not always disclosed. Analog Devices parts of this type use a patented ping-pong architecture whose internal structure is not published, described only as auto-zeroing and chopping.[479]

## Offset, drift and bias current

Offset voltage is the whole point. A zero-drift architecture delivers not just ultra-low offset voltage but near-zero input offset voltage over temperature and over time, which is what separates it from a precision bipolar part whose trimmed offset then drifts.[1325][1693] Offset current is likewise extremely low, effectively negligible.[1318] The practical benchmark is roughly 0.1 microvolts of offset — practically zero.[1693]

The contrast shows up clearly in parts that are precise but not choppers: a converter-front-end op amp specified at 25 microvolts maximum offset voltage and 0.6 microvolts maximum drift with temperature is not low enough for microvolt-level work, and its offset will move with temperature rather than being zeroed out.[1693] Where a design senses a current shunt and the converter resolution is down in the microvolts, the absence of a chopper in the signal path is a design choice worth noticing.[1693]

Input bias current is less well behaved than offset voltage. On a chopper, VOS and input bias current are not consistent, and the bias currents can go in either direction on both inputs across the supply voltage range.[479]

## Noise

Choppers essentially eliminate 1/f noise, which is a major advantage: because the architecture nulls DC offsets and very low-frequency signals, the high-noise flicker content is canceled along with them.[24] Datasheets for zero-drift parts advertise zero flicker noise alongside ultra-low broadband noise, with the flicker behaviour understood as operating below the chopper frequency.[1325]

The trade is a noise spur at the chopping frequency. A chopper necessarily chops at a particular frequency, and that shows up as a spike in the noise spectrum — around 11 kHz in one MAX4239-based instrument, where the spike also varied considerably in amplitude.[1190] The MAX4239's chopping frequency is on the order of 15 kHz; measured on the bench the spur lands near 13.3 kHz, because the datasheet specifies not one fixed frequency but a spread-spectrum scheme with dither added.[1318][1328] Chop frequencies are not all in that band: the OPA189 chops up in the 200 to 300 kHz region, well beyond the 100 kHz span of a typical dynamic signal analyzer, so a 25 kHz spike observed in such a measurement cannot be attributed to its chopping.[1329]

## Bandwidth and other costs

The main disadvantage is bandwidth. Choppers do not have high bandwidth — a couple of kilohertz is typical, a direct consequence of a chop frequency of only 10 to 15 kHz.[24] There is also a pole in the response at the switching frequency, which can make the part troublesome in a signal chain that was not designed around it.[931][1318] In multimeter front ends, the limited bandwidth of these amplifiers is one of the reasons a mux amp built around them is a constraint as well as an expense.[931]

Where the low offset is needed but the drive or bandwidth is not there, the chopper can be embedded in a composite amplifier: a MAX4239, with only microvolts of offset, used in a non-inverting gain-of-10 stage ahead of an output stage that supplies the drive capability, giving a precision high-drive circuit that compensates for the output stage's shortcomings.[1609]

## Where they appear

Choppers are the standard answer wherever DC precision dominates. The MAX4239 is the part used in the µCurrent, and also turns up in isolated current-measurement front ends built around a precision ADC.[1190][1609] Analog Devices' AD8628 is a zero-drift single-supply rail-to-rail part of the same family, and a pair of AD8629 zero-drift choppers appears in the Siglent SDM3055 bench multimeter.[476][829] The OPA189 is a more recent zero-drift part evaluated directly against the MAX4239 on bandwidth, noise and offset voltage.[1325][1329]

Multimeter chipsets sometimes carry a chopper amp alongside their standard op amps, selectable through the internal mux; this is not uncommon on a higher-end four-and-a-half digit chipset, precisely because the chopper is very precise with almost no DC offset.[853] In a Krohn-Hite DC voltage standard, a negative-feedback zero-offset chopper amp sets the output with its gain determined by the feedback network, working against a passive Kelvin divider whose ranges are trimmed by small adjustable resistors; the surrounding circuitry is simple, an LM741 comparator driving an overload lamp and an emitter-follower output driver.[210]

Older precision instruments used considerably lower chop frequencies. The chopper amp in a Keithley 177 microvolt DMM runs at 390 Hz, and the service procedure for a faulty ohms source directs the technician to check that chopper amp first.[777]

## Before the chopper, and the mechanical original

The name is literal, and the original implementations were electromechanical: a vibrator that chops between two signals, packaged as a component in its own right.[847] Such mechanical choppers date from the same era as the early precision monolithics, with parts of this vintage carrying date codes around 1983.[651][847]

Historically the chopper was the only route to low offset voltage — before dedicated precision op amps existed, achieving it meant using a chopper amplifier.[1436] The OP07 changed that: a precision part with low offset voltage built in, requiring no external trimming, after which the chopper stopped being mandatory for merely precise work and became the tool for the extreme end.[1436]
