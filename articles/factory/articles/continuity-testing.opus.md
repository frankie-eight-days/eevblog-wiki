# continuity testing

Continuity testing is the practice of confirming that two points in a circuit are electrically connected, normally using the dedicated continuity function of a multimeter, which sounds a buzzer when the resistance between the probes falls below a threshold.[75][1636] Virtually every multimeter carries the function, marked with a buzzer or sound symbol on the range switch.[75][1636] It is the one function almost every user reaches for regardless of field, and it is the primary tool for finding breaks in cables, cracked PCB traces, and connections that are not where a drawing says they should be.[75][1636]

Beyond fault finding, the beep is a navigation aid: dragging one probe across a board while the other sits on a known net reveals where that net travels, which makes the function central to both repair and reverse engineering.[1636][675]

## Threshold and test current

A continuity tester is an ohmmeter with a comparator on its output, and where the comparator trips matters. Firmware development on the BM786 illustrates the range of choice available: the shipping firmware switched the buzzer on at roughly 270 ohms and required hysteresis out to about 300 ohms to release, while revised firmware moved the turn-on point to approximately 40 ohms with turn-off at exactly 100 ohms, a change requested by users who wanted the buzzer to indicate a genuinely low resistance rather than any conduction path.[PSdF0KNsiaY]

Threshold changes are not free. The revised BM786 firmware traded detection rate for the lower threshold, stretching what should have been a response on the order of 100 microseconds into an effective 100 millisecond pulse, and degrading the latching behaviour in the process.[PSdF0KNsiaY]

Production test equipment uses far heavier stimulus than a handheld meter. Bare-board flying probe testers pass on the order of 150 milliamps through each net during the continuity portion of the test, then run a separate isolation test at a specified voltage such as 64 volts to check that nets which should not connect do not.[939]

## Response speed and latching

The single most important quality metric for the function is how reliably it catches a brief contact. A good tester responds instantly on a fast swipe and latches the beep so the indication survives the moment of contact.[1636] A 500 microsecond response time is enough to pick up essentially everything.[60] Response speed is worth checking before buying a meter at all, because performance varies widely across otherwise similar instruments.[6][1636]

Failures cluster at the slow end. A meter that only registers eventually, with no latching and no buzzer at all, cannot compete with any serious instrument.[1238] A wrist-worn multimeter proved useless as a continuity tester.[1706] A pocket meter missed contact completely on a bench swipe.[6] The Hioki handheld was "slow as a wet week" in continuity mode.[973] Even a bench multimeter can disappoint, with autoranging too slow for everyday continuity work in its normal measurement mode.[1382] Middling performers register but drop enough events to be irritating: a Gossen unit was reasonably quick yet missed a noticeable fraction of contacts,[46] and an ANENG unit missed contacts even with gold-plated probes, rating as barely adequate despite being loud and having a visual indicator.[1704] A retro Fluke was not the fastest available but was loud enough to be usable.[1393]

Good implementations latch and respond instantly together.[973][1597][1540][1608][D2PANd9Hu3U] Even a highly regarded meter such as the Fluke 87V, generally very quick, can be made to miss occasionally.[10]

Latching is itself a design trade-off rather than an unambiguous good, since latching and pulse stretching interact with what is being probed, and large capacitor values can fool a latched tester.[1671] Non-latching behaviour produces the characteristic "itchy and scratchy" beeping on a dragged probe.[1083][PSdF0KNsiaY] Loudness matters alongside speed, and it depends on mechanical packaging: one pocket meter's buzzer was muffled by the thick TPU rubber case surrounding it and became noticeably louder with the case removed.[1083] A visual alert alongside the buzzer is useful, though it is often left unlatched even when the audible indication latches.[973][1424]

Placing continuity on its own switch position rather than behind a soft button on a shared ohms position is a meaningful ergonomic gain, since it removes a button press from an operation performed constantly.[60][973][1083]

## Probes and contact resistance

The tester is only as good as the metal touching the board. Gold-plated probe tips make measurably better contact than the nickel-alloy plating used on cheaper leads: a gold-plated probe resting under nothing but its own weight will hold continuous contact, while the industry-standard non-gold-plated leads may fail to register even when pressed with considerable force.[uV9mW0rpRxg] The difference shows up in ordinary probing as well as in continuity testing.[uV9mW0rpRxg] Swapping to gold probes visibly improves the apparent continuity performance of a meter that seemed poor with its supplied leads.[1272]

Tip geometry matters independently of plating. Round, blunt tips are a persistent annoyance where sharp points are needed to reach small pads.[46][1244] Gold plating does not rescue a slow comparator, however: a sufficiently poor tester will still miss contacts made with good probes.[1704]

A meter should be verified as working before it is trusted for a result, by shorting the probes and confirming the buzzer sounds.[1493]

## Fault finding and repair

Buzzing out connections is the standard method for locating breaks in corroded or damaged boards, and on a badly corroded board every single suspect trace has to be checked individually because visible copper says nothing about whether the conductor is intact underneath.[Gbn_51IoJiM][1527][507] On an Acorn Archimedes with electrolyte damage, common pins on adjacent ROMs that were unambiguously supposed to be connected showed no continuity at all, and multiple breaks existed in the affected traces.[507] Repair of such a board requires buzzing out every connection and repairing the faulty ones.[507] Corrosion travels further than it appears to, reaching vias well away from the visible damage, which widens the set of nets that must be checked.[1527]

The test is also the quickest way to confirm or eliminate mechanical failures. A suspected micro-crack in a solder joint can be checked by buzzing from one side of the joint to the other, a fast enough test to run as a matter of course.[afErPINq8qc] Conversely, the test can exonerate a suspect: a crack apparently visible on a wide trace was shown to be intact, and a crack of that size on a trace of that width is implausible in the first place.[m3sQHx5aMmU] A track that looked black and rotted turned out on measurement to be exactly the fault.[1376]

Where the far side of a board is inaccessible, buzzing a pin out simply to establish whether it goes anywhere at all is a useful first move.[1702] The same probing can map the row-and-column structure of a contact array.[1702]

Distinguishing a short from a break is part of the same workflow. Probing across capacitors that sit on power rails finds shorted parts,[330] and a reading of 12K to ground on a suspect node establishes that the node is not shorted, redirecting the diagnosis.[710] A surface-mount inductor can be checked for continuity through itself and separately for a short to ground.[1299] In a mains filter with no internal fusing, an open between the input and output pins localises the fault to one side of the common-mode choke.[620]

Flexible circuits are a recurring offender: on a camera repair, neither the battery positive nor the battery negative path had continuity through the ribbon, and the ribbon had to be reinstalled and re-tested after each intervention to confirm a repair.[1433] Continuity checks also catch documentation errors: a service manual claiming a signal appeared on pin 12 was contradicted by a measurement showing continuity to nothing there.[1602]

## Reverse engineering and pinout determination

Tracing an unknown board is largely a continuity exercise, and it is where response speed pays off most directly, because the technique is to hold one probe on a known point and drag the other along IC pins and other candidate points looking for the beep.[675] Inner-layer vias that disappear from top and bottom layer photographs can only be resolved this way.[675] Deduction narrows the search first: a trace that vanishes under a package must emerge somewhere, so buzzing the candidate pins confirms it, as when an op-amp pin 3 was shown to connect to pin 6.[714] Where components obscure the copper, desoldering them to look underneath is often faster than randomly buzzing pins.[837]

Test points removed from a production board can still be reached at the bed-of-nails pads, and scraping a continuity tester along a suspected quadrant of pads identifies the one that connects to a known pin.[977] Failure to buzz out a connection that should exist is itself diagnostic — an unbuzzable ground pin traced back not to a broken link but to an incorrect pin-out in the schematic.[XUyjRm1Upjs]

Connector polarity on unlabelled equipment is determined the same way: buzzing a DC jack's pins to the grounded chassis identifies which is negative,[802] buzzing between the internal battery negative and the jack's centre tab revealed a centre-negative input on a device where centre-positive would have been assumed,[940] and the ground pin of an audio jack is identified by continuity to the chassis or an external metal part, which is usually common ground.[400]

The technique scales beyond the bench. Aircraft panels reused in a 747 simulator had to be continuity-tested from the rear before re-pinning their connectors, because wiring diagrams vary between aircraft, fleets, and panel numbers, and the panels installed were not the ones originally fitted.[1268] At the other extreme, a suspected connection between an FPGA and downstream hardware was verified by writing a dedicated project that drove data onto every pin.[58]

## Verification before power-up

Continuity checks belong before power is applied, not only after something fails. On a freshly hand-assembled board, buzzing out the power rails to confirm nothing is shorted is the last step before first power-up, with the input capacitor and each regulated rail checked in turn.[1306] The same discipline applies to construction: on a home-made EMC probe, the inner conductor must be confirmed shorted to the shield at the far end before the shield gap is cut.[1178] When identifying which screw terminal carries which supply rail, continuity from the terminal back to the known wire resolves it without guesswork.[1493]

Continuity is equally the go/no-go test for conductive-ink and other non-standard conductors, where an unbroken-looking line can still fail because the trace is not thick enough to carry a path end to end.[1244]

## Related instrument features

Continuity appears alongside diode test, resistance, and capacitance in the standard function set of general-purpose handheld meters,[91][Iwy8UVVQNkA][184] and it is included on specialist instruments such as SMD tweezer-format LCR meters.[81] Meters that break capacitance, frequency, and ohms onto separate switch positions but leave continuity multiplexed miss an opportunity, since continuity is the function most deserving of its own position.[1083]
