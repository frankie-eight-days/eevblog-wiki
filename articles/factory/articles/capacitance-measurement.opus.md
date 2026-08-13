# capacitance measurement

Capacitance measurement is the determination of a capacitor's value in farads, and it is the function that separates an electronics-grade multimeter from an electrician's one.[973] It has become effectively a fourth core multimeter function alongside volts, ohms and current, present on almost every modern meter either as its own dial position or multiplexed onto the ohms range.[1465][1636][75] The measurement is cheap to implement and enormously useful for troubleshooting — but the range, resolution and accuracy on offer vary so widely between instruments that the presence of a capacitance symbol on the dial says almost nothing on its own.[249][75]

## How a multimeter measures capacitance

The standard digital multimeter technique is a timed constant-current charge. The meter's front-end chipset drives a constant current into the capacitor under test and times how long it takes the voltage to rise to a threshold; from current and time the capacitance follows directly.[853] The same analogue front end that generates the constant current for the ohms range is reused, with sense lines tapped off to read the voltage back.[853] Because the technique is a charge-and-time process rather than a continuous conversion, capacitance readings update slowly compared with volts or ohms, and large values take a visible time to settle.[1649][1574]

The same physics can be observed in reverse anywhere a constant current charges a capacitance: a bench supply set to a low current limit ramps its output slowly while the output capacitor charges, and the capacitance can be derived from the ramp time and the current.[549]

Dedicated LCR meters work differently, driving the part with an AC test signal at a selectable frequency and resolving the complex impedance, which yields ESR, quality factor and dissipation factor in addition to capacitance.[1465] They also require the user to choose a series or parallel equivalent model, and the accuracy specification depends on the range, the test frequency and the model selected — a single headline figure such as 0.5% is meaningless without them.[137]

## Range, resolution and residual

For electronics work the useful span runs from picofarads up to a few thousand microfarads; values above that are rarely encountered on the bench, so a meter's maximum range matters far less than its minimum.[75] A lowest range of 2 nF is good, 20 or 40 nF is about the practical limit of usefulness, and a meter whose lowest range is 200 nF is of little value.[75] One picofarad of resolution is the mark of a properly specified electronics meter and appears on instruments across the price spectrum, from Keysight handhelds through the Uni-T UT71E to sub-$40 units.[832][712][1095][249][1007]

The absence of a low range is the concrete reason a meter is classed as electrical rather than electronics-grade: a lowest range of 1 µF, adequate for motor run and start capacitors, cannot measure a 10 nF reference at all.[973] A 1 nF minimum resolution is likewise near-useless for electronics even on an otherwise capable meter.[60]

Residual capacitance — the reading shown with the probes open — is the dominant practical error at the low end. Values of a few tens of picofarads are normal, but meters have been observed sitting at 230 pF, 300 pF and 130 pF with nothing connected.[1083][1576][1649] A relative or delta mode nulls this out and is therefore more important on the capacitance range than anywhere else; meters that show a true zero on open probes need it less, and meters with a large residual and no way to null it are effectively crippled at low values.[1007][1083][1649] Lead and probe capacitance forms part of the same problem, and a body's own capacitance is easily large enough to shift a low-range reading — touching a device under test raises the reading measurably.[477][1723]

## Accuracy

Multimeter capacitance ranges are traditionally neither good nor accurate, and a proper LCR meter is required to do the job well.[75] A couple of percent is typical at best; 1% is very good for a handheld cap range and is what the top-tier Fluke handhelds achieve.[1465][75][10][15] Poor performance is common and often falls outside the manufacturer's own specification: mid-range handhelds have been measured 5 to 7% out at low values while meeting spec nearer the top of a range.[249] Budget instruments specify 4% and worse, and some capacitance ranges are simply flaky, reading tens of nanofarads into an open socket.[MarjYxiudYE][1257] Even within a single product family the cap range is frequently the weakest function and the standing criticism of an otherwise solid meter.[1692][1731]

Verification on the bench is done against a known reference capacitor — a 10 nF standard is the usual working check, sometimes cross-referenced against a bench LCR meter or a decade capacitance box whose individually measured versus target values are documented.[1465][1084][99][510] Discrepancies of a few percent against such a standard are frequently within the capacitor's own tolerance rather than the meter's error.[1471][1378]

## Test frequency and in-circuit measurement

Capacitance is not a frequency-independent quantity, and the test frequency is part of the measurement. An 855 µF capacitor measured out of circuit at 100 Hz reads 820 µF at 1 kHz and behaves as a short at 10 kHz.[1474] Handheld multimeters do not expose this choice; LCR meters do, and 100 Hz, 120 Hz and 1 kHz are the common settings.[137][757][1525]

In-circuit measurement is possible and is one of the more useful troubleshooting applications, particularly on power supplies where electrolytics dry out or vent.[1636] It is very often inaccurate but frequently gives a usable indication.[1649] The failure mode is surrounding circuitry: parallel components and other capacitors charging through the network give readings that swing wildly and vary with test frequency, with one in-circuit part reading 700 nF at 10 kHz, 1600 nF at 100 kHz and 1200 µF at 100 Hz.[1474][1649] Readings that come in somewhat under the nominal value — 27 µF for a 33 µF part, 19 µF for a 22 µF part, 8 µF for a 10 µF input capacitor — are typical of in-circuit conditions and do not by themselves condemn the component.[1ngqB4mxZOI][1299] Where accuracy matters, one lead is lifted; if the capacitor connects to a socketed IC, pulling the chip frees a leg without desoldering anything.[777]

Out of circuit the measurement is decisive. Film capacitors that had failed in service measured 103.5 nF and 19.2 nF at 1 kHz against a 220 nF nominal value — less than half, and more than an order of magnitude down, respectively.[1486]

## Safety

Meter leads must never be connected across a voltage source while the function switch is in the capacitance, resistance or diode position; the input protection on those ranges is not designed for it and the instrument can be damaged or destroyed.[94] This is a documented manual warning, and it is a warning worth taking seriously: an LCR tweezer instrument rated CAT III at its inputs exploded in the hand of its user when probed onto 240 V mains.[94] A professional meter should nonetheless survive the abuse, and 240 V applied to the ohms and capacitance ranges is a standard survival test that competent meters pass.[94][91]

A related safety argument applies to the dedicated two-pin capacitance sockets found on cheap meters. They are convenient — a capacitor plugs straight in without probes — but they are not found on top-quality instruments, for high-voltage and explosion-rating reasons, and are not considered an essential feature.[75]

## Special modes and applications

A low-impedance capacitance mode, entered on some Fluke handhelds by holding the range button during power-up, is intended for noisy measurements such as the capacitance of long cable runs in an industrial environment, where ordinary meters pick up interference.[60] Cable capacitance measurement is a significant enough application that its absence has been called out as a real limitation on bench instruments.[489]

Capacitance is otherwise a notable omission on high-end bench multimeters: some 6½-digit units ship without it while competing Fluke and Rigol models include it, and at least one vendor has added the function to a bench meter by firmware update.[489][829] The gap is conspicuous because a bench meter intended as a general-purpose lab instrument is otherwise well suited to the job.[489]

LCR tweezers automate the measurement for surface-mount work, auto-detecting whether the part under the tips is a resistor, capacitor or inductor and displaying the reading without a mode change.[81] Tweezer instruments trade range for convenience — 0.1 pF resolution up to a ceiling of 400 µF is typical — and their capacitance mode will also light and test LEDs, flashing them more slowly than diode mode does.[1335]

The measurement is also used to characterise stray capacitance in physical structures rather than components: solderless breadboard contact strips, quoted in circulating figures at anywhere from 2 to 25 pF per strip, were resolved by direct measurement rather than by reference to a datasheet.[568] Similarly, direct measurement of a 99.3 pF capacitor in free air and resting on an anti-static mat showed no difference between the two, disposing of the claim that mat conductivity corrupts capacitance readings.[250]

## Analogue instruments

Capacitance measurement on analogue meters was rare and is historically notable where it appears. The Metrawatt and a small number of other analogue movements carried a genuine capacitance range, complete with trimmers for the gain of the capacitance and high-resistance functions.[634][1097] Such ranges require the internal battery, unlike DC volts on the same instrument.[633] The alternative analogue technique — watching the needle kick and decay when a capacitor is connected on a resistance range and inferring the value from the movement's decay — is inferior to a dedicated capacitance mode in both convenience and accuracy, since it requires calculating from a needle decay factor.[1067]

Capacitance was not a standard multimeter function when many classic instruments were designed; late-1980s Fluke handhelds omit it entirely, and a 1981 instrument offering capacitance testing represented substantial functionality for its era.[1393][372][986]
