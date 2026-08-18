# capacitive coupling

Capacitive coupling is the transfer of signal energy between two conductors through the stray capacitance that exists between them, with no galvanic connection required.[548][1003] It is a near-field effect, alongside inductive coupling, and it is the mechanism behind a large fraction of the unexplained noise, crosstalk and apparent action-at-a-distance misbehaviour encountered on the bench.[548][1306] The same mechanism is exploited deliberately wherever a signal must cross a barrier without a wire: AC coupling between amplifier stages, mains-frequency trigger pickup, non-contact voltage detection, and isolated digital links.[609][564][1003][1264]

## The human body as a coupling source

A finger or hand brought near a circuit forms one plate of a capacitor, and the body itself acts as an antenna carrying the mains frequency — 50 Hz in Australia.[689][306] Bringing a hand close to an unshielded input jack raises the 50 Hz amplitude on a scope trace, and withdrawing it drops the signal back down into the noise floor, purely as a function of distance.[1755] The coupling is strongly geometry-dependent: approaching a contact from the side, so that a length of finger runs parallel to the conductor, gives far more capacitance than approaching it end-on from directly above.[510]

The effect is enough to disturb working circuits without any physical contact. On an avalanche-transistor pulse generator, a finger placed near the transistor's can widens the jitter on the output before contact is even made, and touching the can kills the signal entirely as body-borne 50 Hz swamps the oscillator.[306] On a multiplexed display driver, approaching the chip closely — without touching any pin — coupled enough mains pickup into it to light segments, a fault that resets itself each time and is therefore electronic rather than a mechanical solder-joint defect.[689] A microcontroller board running only an internal oscillator and no input could be made to misbehave and then die outright as a hand approached, the coupling arriving through the air into the pins of a floating input.[1306] Even the act of touching a trimmer while adjusting an oscillator adds enough body capacitance to shift the frequency in the opposite direction from the adjustment being made.[457]

The remedy on a high-impedance node is to drive it rather than leave it floating. Tri-stating LCD segment drivers should in theory leave segments off, since there is no voltage difference across them, but floating pins accumulate charge from ambient fields and drift on; the pins should always be driven.[1045]

## Coupling on boards, wiring and construction media

Where signal traces run parallel with no ground shield between them, capacitance between them couples signals across, and on a wide bus routed as long parallel runs the resulting crosstalk can be serious.[1247] Traces that merely cross at right angles have little mutual capacitance and produce little crosstalk.[1247]

Prototyping media are worse than PCBs. Stripboard and perfboard introduce substantial crosstalk between traces, with capacitance between adjacent strips on the order of tens of picofarads — enough that point-to-point wiring can be the better technique, and enough that a switching supply is a poor candidate for such construction.[97] Breadboard coupling is measurable directly: with a glass delay line physically removed from the breadboard, the expected echoes vanished but a residual burst remained, produced by capacitive coupling through the breadboard alone at that frequency.[386]

Adjacent connector pins couple as well. On a pin-header instrument input, a 100 kHz sine on one channel appears as visible crosstalk on the neighbouring channel; grounding the second input reduces the pickup substantially but does not eliminate it.[692] In filters, coupling between input and output connectors bypasses the filter entirely, so avoiding it is part of achieving good VHF/UHF response.[353]

Stray coupling can also masquerade as a real signal in reverse engineering. A trace showing 12 MHz was carrying nothing of its own: it ran near the crystal and picked up a few hundred millivolts of stray coupling, which was itself evidence the pin was a high-impedance input rather than a low-impedance output, since a driven output could not have been perturbed that far.[717]

## Measurement and instrumentation

Any high-impedance node in a measurement circuit is a good noise-pickup point, and stray fields couple into it easily; the fix in a high-voltage probe design was to encase the assembly in a copper tube and pot it.[85] Removing a shield can is enough to ruin a measurement: with the can off an oscilloscope's front end and wires run into it, one channel picked up 50 Hz hum because everything was coupling capacitively.[879] An ESD mat left floating couples 50 Hz effectively into a scope front end; grounding the mat to the instrument reduces but does not entirely remove it.[e4wvxWWMla0] Even a bench that is non-conductive is not neutral — laying a board and an optical fibre probe flat on the bench increases capacitive coupling, which is why such probes are supplied with a stand.[1557]

The long leads of a differential probe pair are exposed to external capacitive or EMI coupling, which arrives on both wires alike; twisting the pair is what makes that interference genuinely common-mode so the amplifier's rejection can remove it.[1521] When an oscilloscope probe is used as a mechanical vibration pickup, the input must be shorted, otherwise it simply capacitively couples whatever electrical signal is present on the board.[1743] A high-impedance ammeter front end will show current from coupling paths through a thermocouple and the shielding around it, which can be mistaken for an effect under investigation.[1455]

## EMC and interference

Capacitive coupling and inductive coupling are treated separately from radiated and conducted emissions in EMC work, and because they are near-field effects they are only subject to a standard in specific product cases; most products are tested for radiated and conducted emissions only.[548] The ground planes used in conducted-emissions test setups exist in part to stop capacitive coupling to other equipment in the room.[548] Bench-level pre-compliance measurements are contaminated by whatever else is nearby — overhead LED lighting contributed broadband noise to one such measurement — so capacitive and inductive coupling into the test setup must be accounted for before believing a trace.[548]

Susceptibility, not just emission, follows the same path. A multimeter that failed under conducted injection also failed with the injecting wire merely draped around it, an entirely capacitively coupled path rather than a conducted one.[987]

Fast transients are easy to generate through the same physics: pass a current through an inductor, open-circuit it, and capacitively couple the resulting spike onto the supply rail under test.[354]

## Coupling as a design tool

Line-frequency triggering in oscilloscopes is commonly implemented by heat-shrinking two wires alongside the mains cable with no electrical contact at all; the mains capacitively couples across and the processor recovers the line frequency from it, which is cheaper and safer than tapping the signal electrically inside the supply.[564][587]

Non-contact voltage detectors work the same way: the probe tip is one plate of a capacitor, feeding through a high-value current-limiting resistor into a threshold gate such as a 74HC14 that drives the indicator.[1003] The coupling capacitance between the wire under test and the probe is on the order of 0.1 pF, which passes only a minute current — sufficient only because the input impedance is very high.[1003]

In audio circuits, the audio signal riding on a DC bias is capacitor-coupled out to the following amplifier stage, whose own bias conditions are then set independently by a resistor to the chosen bias voltage.[609] The same technique takes the balanced signal off a phantom-powered line into the differential amplifier while blocking the 48 V.[616]

Isolated digital links can be built on deliberate capacitive coupling. A capacitive digital isolator contains a modulator and demodulator that send the signal across an internal capacitance of a few picofarads, and such parts draw considerably less power than the alternatives.[1264]

The mechanism can also serve as a sensor. In an EPIRB, the proximity of a grounded bar to the antenna changes the capacitive coupling and hence the antenna's characteristics, so short test bursts from the transmitter return different amplitudes depending on whether the antenna is stowed flat against the bar or raised; the resulting switching of a transistor lets the microcontroller determine antenna position without a mechanical switch.[368]

## Suppressing unwanted coupling

The classic countermeasure in a mains transformer is an electrostatic shield: an earthed screen wound between primary and secondary, cutting the interwinding capacitance so that common-mode noise on the primary cannot cross to the secondary.[791] The shield is closely coupled to the primary side.[791] Good safety isolation transformers are built this way, and the technique appears in quality instrument supplies.[791] In switching supplies, an opto-isolator carries the feedback across the barrier while the transformer's residual interwinding capacitance remains the coupling path of concern.[1726]

On boards, the general remedies follow from the mechanism: ground shielding between parallel traces to break the mutual capacitance,[1247] enclosure of high-impedance nodes in shielding,[85] separation of filter inputs from outputs,[353] and grounded planes to intercept coupling to nearby equipment.[548]
