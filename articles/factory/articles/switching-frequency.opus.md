# switching frequency

Switching frequency is the rate at which the active element of a switch-mode circuit — a MOSFET, a bipolar transistor, or a switch array inside a charge-pump chip — is turned on and off to transfer energy. It is the single parameter that sets the size of the magnetics and capacitors a converter needs, the switching losses it burns, and the frequency at which its noise appears in every other circuit nearby.[110][139][1294][548] Almost every design decision around a switcher is a trade against it: raising the frequency shrinks the passive components and worsens the losses, and the correct answer is a compromise rather than a maximum.[110]

## Frequency and component size

The higher the switching frequency, the smaller the inductor a converter requires, and inductors are physically bulky parts — a large inductance value means a large device.[110][139] In a space-constrained design this is often the deciding factor: a boost converter selected for a small board was chosen partly because its higher switching frequency permitted a smaller inductor, alongside its 800 mA output capability and 2.05 W maximum output.[139] The same logic applies to transformers, and explains why an offline or isolated stage that would need a large 50 Hz transformer can get away with a tiny one once it switches at high frequency.[yOJ7xPugsdc]

Inductor and capacitor values are computed for a particular switching frequency, so they are not portable between chips.[1475] Switching frequency can differ vastly from part to part, and substituting a pin-compatible regulator without matching the passives may still work but can produce more output ripple or lower efficiency than intended.[1475] Where two candidate parts share a formula and a nominal frequency — both around 1.5 MHz, for example — they can reasonably be treated as equivalents.[1475]

In classical switch-mode design the frequency enters the calculation directly: the sum of on-time and off-time is simply 1/F, so a device specified for a maximum of 100 kHz yields 10 µs for T on plus T off.[110]

## Losses and the efficiency trade-off

Switching losses rise with frequency. A conventional hard-switching topology drives the transistor essentially digitally, high-low-high-low, and the losses of that transition grow the faster it is repeated — which is awkward, because higher frequency is exactly what is wanted for smaller magnetics and better efficiency elsewhere.[1294][110] Resonant topologies such as LLC exist to break this deadlock by reshaping the switching waveform so that less is lost per transition.[1294] The trade-off is a standing design question rather than a solved one: for any given converter it is worth asking why a particular frequency was chosen and what changes if it goes higher.[1737]

Overall converter efficiency is a function of the magnetics, the MOSFET, the output capacitance and the switching frequency taken together, and a converter designed around a specific operating point can reach 90% or better.[895][321] Efficiency of that order matters directly as heat: at 100 W output and 90% efficiency, 10 W has to be dissipated by the active semiconductors.[895]

## Device limits on frequency

MOSFETs dominate switching applications because they are faster than bipolar transistors, and remain usable into the megahertz region where high-frequency DC-DC converters operate.[1736] The limit on bipolar transistors is storage time — the base charge is retained for a period on the order of microseconds after drive is removed, keeping the transistor on, and this is what caps their switching frequency.[1409] Small jellybean MOSFETs are commonly rated around 1 MHz switching frequency; at that level input capacitance is rarely the binding constraint for jellybean use, and package power dissipation is more likely to be — a SOT-23 part is limited to roughly 0.2 W absolute maximum at room temperature.[1736]

## Frequencies encountered in practice

Measured switching frequencies span more than four orders of magnitude depending on the era, topology and purpose of the equipment:

- Mains-derived and offline supplies sit at the low end: an arcade machine power supply at about 27 kHz,[1301] a switch-mode supply probed at 40 kHz,[296] a VIPER 22A primary-side offline switcher at 60 kHz,[1ngqB4mxZOI] a bench supply at around 66 kHz.[439]
- LED lighting gear clusters in the tens of kilohertz: an LED fluorescent tube replacement at 64 kHz,[533] one LED panel at 62.7 kHz and another at 47 kHz.[1252]
- Modern bench and USB power supplies run higher: 120 kHz,[1691] about 160 kHz for a USB DC-DC supply,[324] 246 kHz for two separate units,[1607][1606] and 300 kHz for a boost converter demo board running 19 V in to 24 V out.[oVkrc3gF7ns]
- Integrated converters and chopper-stabilised amplifiers reach the megahertz region: 1.5 MHz for a small buck regulator,[1475] 1 MHz or more for a tablet's DC-DC converters,[321] 2 MHz for a switched-capacitor inverter,[1115] and hundreds of kilohertz — reportedly around 250 kHz — for the internal chopping of an OPA189.[1328]

A period tool intended for power work needed only hundreds of kilohertz to several megahertz of bandwidth to cover the switching frequencies of its day, which is why 7.5 MHz was ample for its market.[1724]

## Frequency that varies

Switching frequency is not always a fixed number. Many converters deliberately vary it with output power to hold efficiency up at light loads, so a measured value is only valid for the load at which it was taken.[957] One PoE hat measured about 24.6 kHz under one condition, and running the load up from a light condition to 2 W doubled the frequency from 9 kHz to 19 kHz — behaviour the data sheet would be expected to describe.[1122] A supply operating at 120 kHz was seen to add a second, additional switching component once driven to 200 W, a genuine mode change rather than a capture artifact.[1691] In a data sheet, the switching frequency in the typical application circuit is governed by a complex equation with several dependencies, and taking the headline number at face value is a way to come unstuck.[1216]

A frequency that has moved without being asked to is a fault symptom. In a failed combiscope supply, the switching seen across a convenient diode had simply dropped in frequency, which pulled down every output rail derived from it, including the EHT — evidence against the tripler being at fault.[1452] Conversely, a healthy supply shows a consistent waveform at its nominal frequency with no cycle skipping.[1301]

## Measuring switching frequency

The usual probe point is the inductor, though the right node depends on the converter.[957] The primary of the main switching transformer works for offline supplies, probed with a high-voltage differential probe at settings such as 50 V or 100 V per division.[1301] A field-sensing current probe allows the switching waveform at the inductor output to be observed without breaking into the circuit, which is the traditional requirement for current probes.[296] Where automatic measurement is unavailable, the frequency can simply be read off the time base and division count.[1265]

Deep memory helps capture the whole waveform for later zooming, but it also causes trouble: with high-frequency content held in memory, a scope's automatic frequency measurement may lock onto the switching edges' ringing rather than the switching cycle itself. Offsetting the waveform vertically away from the screen centre makes the counter find the peaks elsewhere and track the intended frequency.[324]

Probe fidelity degrades with frequency, so the measurement setup must be qualified alongside the circuit. At 1 kHz switching, a high-voltage differential probe shows no visible change in waveform even at 300 V; as frequency rises, common-mode rejection falls off and the artifacts appear.[1557] At 1 MHz switching frequency, differences between probes were attributable to the probing arrangement itself rather than the probes' performance.[1631] Low-inductance probing — dispensing with the standard ground lead — is required to see the switching component honestly.[1122]

## Noise, EMC and resonance

Switching frequencies and the fast, sharp edges that accompany them are the primary source of broadband radiated emissions from an electronic product; short of a fully effective sealed metal enclosure, essentially any product containing them will radiate.[548] On the output side, the ripple that matters on a switching supply is at the switching frequency rather than at low frequency, and manufacturers frequently specify low-frequency ripple in millivolts while saying nothing about the switching noise.[1691][1265] A PoE hat exhibited 320 mV peak-to-peak of switching noise at a modest load,[1122] and an inexpensive supply module showed roughly 700 mV peak-to-peak.[1265] Switching noise also couples in from the environment: an instrument's low-level measurement picked up a component at around 64 kHz that came from studio LED lighting, not the circuit under test.[579]

Filtering a switching component out of a low-level output requires the filter corner to be well below the switching frequency; an RC filter with a 3 dB point at 159 Hz was still not low enough in value to remove the switching noise from a supply attempting to output 100 mV, leaving roughly 10 mV of ripple.[225]

Resonance makes the choice of frequency consequential in less obvious ways. Fitting many bypass capacitors of different values raises the risk of hitting a resonant point at some switching frequency, where the track inductance and the capacitors' resonances combine and the circuit misbehaves badly.[1117] Return current also depends on frequency: the higher the switching frequency, the more the return loop hugs the path directly beneath the power traces due to spreading inductance, rather than spreading out across the plane as it tends to at DC.[1216]

The mechanical consequences are real. In Tesla's Dojo hardware, MEMS oscillators cracked from out-of-plane mechanical resonance excited by capacitor vibration at the switching frequency combined with high currents; among the available fixes were anti-vibration mounting, relocating the oscillator to a separate board, and changing the switching frequency itself.[1504] Multi-layer ceramic capacitors are piezoelectric, and choosing a switching frequency of 5 kHz puts the resulting vibration squarely in the audible range — a chipset switching at 20 kHz or 30 kHz instead would have gone unnoticed, making an audible switcher a poor choice of frequency rather than an unavoidable defect.[855]

## Charge pumps and voltage multipliers

In switched-capacitor circuits the frequency interacts with capacitor value to determine output droop. Output ripple and sag depend jointly on the capacitor values and the switching frequency, since the capacitors must recharge between cycles and a loaded stage passes a lower peak voltage to the next.[483][469] In a Cockcroft-Walton multiplier the practical limit on chain length comes from the AC impedance of the components together with the switching frequency; a full-wave version doubles the effective frequency, reducing sag and increasing load capability, exactly as it does in a linear supply.[469]

A microcontroller-driven voltage doubler illustrates the trade directly. At 1 kHz the ripple and droop are severe; 10 kHz serves as a reasonable rule of thumb.[473] Frequency only starts to matter once the output begins to droop — with no ripple present, raising the frequency buys nothing.[473] Increasing the capacitors to 47 µF allows acceptable operation at frequencies as low as around 100 Hz, down to 81 Hz in testing, with enough DC left to run a load such as an LCD, particularly with a linear regulator following.[473]

The relationship between frequency and ripple in charge pumps is a trap in part selection. A 2 MHz switched-capacitor inverter appears, by analogy with the classic 7660, to promise low output ripple, but the 7660's near-100% efficiency depends on both the switching frequency and the output impedance of its internal switches, and the analogy does not carry over.[1115]
