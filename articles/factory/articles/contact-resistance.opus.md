# contact resistance

Contact resistance is the unwanted resistance appearing at any mechanical junction in a circuit — a switch contact, a relay contact, a connector, a banana plug, a battery spring terminal, a probe tip pressed against a pad. It is normally small, in the milliohm to sub-ohm range, but it is never zero, it is rarely stable, and it sits in series with whatever is being measured or powered.[72][210][929] It matters wherever the quantity of interest is itself small: a low-value current shunt, a precision resistance standard, a voltage measured across a high-current path, or a switch read as an analogue value rather than a logic level.[72][489][141][1361]

## Typical magnitudes

A good mechanical switch contact is on the order of milliohms.[72][929] A fresh tactile dome measures down in the tens of milliohms.[1361] A well-made flanged banana jack repeats to within a couple of hundred microohms as the plug is rotated, pulled part way out, and reinserted — around 500 microohms of movement in total.[1052] Gold pogo pin probe tips measure a gold pad at 0.238 ohms and shift by only a couple of milliohms as the pins are worked up and down.[407] A pair of ordinary test leads contributes roughly 55 to 56 milliohms.[413]

At the other extreme, cheap banana plugs have been measured at 0.243 ohms, rising to 0.7 ohms and beyond 2 ohms under nothing more than a light wiggle, with the solder joint itself demonstrably sound — a resistance far worse than would normally be expected of such a plug.[1052] A degraded tactile switch dome can vary from a couple of ohms under hard pressure up to many hundreds of ohms.[1361]

## Instability, not magnitude, is the real problem

A contact resistance that is high but constant can be calibrated or nulled out. One that moves cannot. The diagnostic technique is mechanical: wiggle the probes while watching the reading. If the display holds steady, the contact is sound; if it climbs or jumps, the measurement is not trustworthy.[398][215][1052] Firm, consistent pressure on the probe tips is essential, and very sharp high-quality tips are needed to pierce the oxidation on solder joints and reach metal underneath.[398]

This matters most when tracing a small differential. Locating a short on a power rail by measuring voltage-drop-style resistance across a board means chasing a delta — starting from 0.11 ohms at the connector and hunting for the point where it falls toward 0.06 ohms — so repeatability of the contact dominates the whole exercise.[398] Measuring through a plug-in memory module rather than directly on the board raises the reading to 0.17 ohms purely through the connector contacts.[398]

Contact instability also masquerades as bad data. A single 500-ohm reading among values that should all be near 100 ohms is far more likely to be a contact artefact than a real result.[1658] Even in a precision bench setup, brushing a 1 kΩ resistor under test with a hand adds enough contact resistance to shift a reading from 999.991 ohms to 1.000008 kΩ and push the result into a different histogram bin.[489]

## Cancelling it out

Four-wire (Kelvin) measurement removes the resistance of the leads and the contacts from the result entirely: the same PCB trace reads 212 milliohms in two-wire mode and 51 milliohms in four-wire.[317] Where four-wire is unavailable, the constant part can be nulled — subtracting a measured 0.15 ohms of combined lead and contact resistance from every reading in a batch to recover the true resistor values.[215] Neither trick removes the varying part.

The same principle applies to sensing voltage on a live circuit: the sense connection must be taken at the point of interest, not upstream of the contacts. Moving a voltmeter terminal from a battery's end cap back to the instrument's input jack introduces enough drop through a short lead and a spring terminal contact to change the reading measurably at 250 mA; with the current turned down, the discrepancy vanishes because there is no current to develop a drop.[141] For the same reason, battery cutoff testing should measure at the battery terminal rather than trusting the supply's own display, though at low power the contact contribution is small enough to ignore.[779] Contacts and wiring in a discharge rig also mean a nominal cutoff voltage is reached earlier than the cell's true state warrants, leaving real capacity — potentially a couple of hundred milliamp-hours — unextracted.[XDjyY48u0PU]

## Swamping low-value shunts

In current measurement the shunt resistor is deliberately made tiny, which puts contact resistance directly in competition with it. A 10 milliohm milliamp-range shunt is the same order of magnitude as the contact resistance of a typical switch, plus the connectors and other joints in the path, so the parasitic resistance swamps the intended value and destroys the accuracy of the range.[72][929] The remedy is to tap the sense connection at the shunt itself, so the amplifier sees only the shunt and not the switch in series with it; the switch still adds to total burden voltage, but burden voltage is a far more forgiving budget.[72] On higher ranges using 10 ohm and 10 kΩ shunts, switch contact resistance is negligible and can be ignored.[72]

Breadboard contacts are poor enough to matter in precision analogue work: unexplained residual error in a 1 A current source built from 0.02 percent resistors was attributable to breadboard contact resistance rather than the components.[577]

## Heat and high current

Contact resistance dissipates power, and at high current that shows up as heat. Alligator clips carrying 11 amps get noticeably warm for exactly this reason.[401] The effect is also self-reinforcing and time-dependent: pitted contacts in a mains switch can run slightly resistive, heat up, and degrade further until the switch can no longer deliver enough power to a transformer, causing every downstream rail to sag — a fault that appears only after the instrument has been running for a while.[804] In a twelve-panel solar string, a single joint developing higher resistance and heating under load is a plausible cause of a significant output drop, since a long string contains many connections and any one of them can be the culprit.[1426]

Where a low-resistance bond genuinely matters at high current, it is made explicitly rather than assumed. A 10 kW laser supply routes a dedicated bus bar between all the transistor cases rather than relying on the metal of the heat transfer block to carry the connection, purely to obtain lower contact resistance.[1381]

## Precision resistance standards and decade boxes

In decade resistance boxes and resistance calibrators, contact resistance is the dominant design problem, not the resistors. The resistors themselves are stable and do not age much; the reliability and repeatability of the switching is what the price buys.[211][461] Every mechanical switch in the chain has dirty contacts, bounce, and a certain minimum contact resistance, which sets a floor on how low the bottom decade can usefully go.[210]

Several countermeasures recur. High-quality thumbwheel switches are custom made with extra-thick gold plating specifically for low contact resistance maintained over age.[211] Precision calibrators use top-quality relays on the low ranges, sometimes with multiple contacts paralleled to drive the accumulated contact resistance and long-term error inside the target spec.[544][545] The requirement is range-dependent: on the kilohm ranges physically smaller relays with somewhat higher contact resistance are acceptable, and by the megohm ranges contact resistance ceases to matter at all — it is unmeasurably small relative to the value — at which point the critical parameter flips to the insulation resistance of the relay, which is why ultra-high-insulation reed relays appear at the top end.[544][545]

Switching topology also multiplies the problem. A decade built from normally-closed switches puts four contact resistances in the path per decade instead of one, which is why a home-built box of that design should start its lowest decade at 10 ohms rather than attempting a 1 ohm or 0.1 ohm decade — unless high-quality switches are used throughout.[212] Contact resistance is also the first suspect when a decade box gives nonsensical readings.[1586] Boxes that have sat in storage need their switches operated a number of times before they will meet their minimum contact resistance spec again.[461]

At the level of a dedicated resistance standard, contacts join temperature and lead resistance as one of the error terms that must be controlled, using low-noise materials such as tellurium copper for the contacts.[834]

## Switch matrices read as analogue values

A switch matrix decoded as pure logic is largely immune to contact resistance: whether a closed contact reads zero ohms, one ohm, five ohms, or a couple of hundred ohms, it either registers as pressed or it does not.[1360] The tolerance disappears when multiple switches are multiplexed onto a single microcontroller pin by having each switch insert a different resistance into a divider read by an ADC. In that arrangement a dodgy contact varying from a couple of ohms to many hundreds of ohms shifts the divider output and causes the wrong key to be decoded, or inconsistent behaviour with no clean failure.[1361][1360] The technique itself is a long-established way to get many switches onto one line; the vulnerability is that it converts a contact-resistance problem into a functional one.[1361]

The measured resistance of a tactile dome is not a property of the dome alone — it depends on the contact, the surface, and the materials it is mated to, which is why dome test equipment measures it in situ alongside trip force, return force, free height, displacement, and tactile slope.[1291]

## Plating and probe choice

Gold plating is the standard answer for a contact that must stay low over time, both in precision switchgear and at the probe tip.[211][uV9mW0rpRxg] Gold-plated multimeter probes make better contact than plain silver-type ones, giving faster continuity response and lower contact resistance, and the price premium is usually small; general purpose silver probes are better regarded as electrical-work probes, made to be shoved hard into contacts, and are a poor choice for electronics use.[uV9mW0rpRxg] Where sharpness is prioritised for fine-pitch work, there is a trade-off — fine pogo-pin probes can carry noticeably high contact resistance despite being mechanically ideal for the job.[1460]

## Wear and life testing

Because contact resistance degrades with mechanical cycling, it is the natural pass/fail metric for switch endurance testing. A rotary range switch can be instrumented by wiring out its off position and reading it through an ADC in a divider, with a parallel resistor included so an open contact still produces a finite, calculable value.[u2-ot2vWLxI] Such a switch measured a nominal 0.9 ohms rock steady at the start of life, still read 0.85 ohms after 11,000 cycles, and remained around a couple of ohms while visible wear accumulated — plating marks on the gold pads and fiberglass dust pushed in from an unplated hole edge — proving that visible wear and electrical degradation are not the same thing.[u2-ot2vWLxI] Failure at approximately 25,000 cycles came not as a resistance number out of spec but as intermittent misbehaviour in one mode, with the contact resistance still nominally acceptable.[u2-ot2vWLxI] Fixturing is itself a source of error in such tests: poor positioning of the unit in the jig corrupted a run's contact resistance data.[u2-ot2vWLxI]
