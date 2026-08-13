# brymen bm786

The Brymen BM786 is a handheld digital multimeter, an EEVblog-exclusive variant within Brymen's BM780 series, sold from 2020 onward.[PfzgOuBHJFM][TkmMitYnHUA] Its significance is positional: it is the handheld that a mid-range Fluke — specifically the 77 IV — is most directly measured against, matching that meter in shape, form factor and overmolded case while costing between a half and a third as much.[ay9wFQAW19Y][1447] The models across the 780 series are functionally the same instrument with different feature sets; the 786 is the branded configuration.[TkmMitYnHUA]

## DC current performance

The 780 series specification for DC current is tighter than that of Brymen's own flagship BM869, an inversion of the usual assumption that the top-of-the-line model wins on every parameter.[PfzgOuBHJFM] The BM786 specifies roughly 0.075% plus 20 digits on DC current.[PfzgOuBHJFM] The 869's corresponding figure is 0.15%, with a best case of 0.1% plus 20 digits on its 6 mA and 6,000 µA ranges, and it degrades to plus 30 digits on the 600 mA range where the 786 holds plus 20 digits at the same percentage spec.[PfzgOuBHJFM] The 869's 500,000-count resolution applies to voltage, not to current, so it confers no advantage here.[PfzgOuBHJFM]

Burden voltage follows the same pattern. The BM786 is specified at 0.15 mV per microamp against 0.2 for the 869, and it is lower on the two principal milliamp ranges as well.[PfzgOuBHJFM] Better accuracy and lower burden voltage together make the cheaper meter the correct choice where absolute DC current measurement matters.[PfzgOuBHJFM] Verified against a calibrator at test points up to 100 mA, both meters read accurately, which is the expected outcome and does not discriminate between them — the difference lives in the specification, not in a spot check.[PfzgOuBHJFM]

## Non-contact voltage detection

The BM786 carries non-contact voltage detection with two sensitivity ranges, defaulting to the high range, actuated by a tab on the side of the case.[1378] Its detection performance is at the top of what handheld meters achieve: it will pick up a light switch, a target that weaker implementations miss entirely.[1378] Sensitivity of this order is the practical dividing line between a usable NCV function and a decorative one.

## Resistance behaviour

Certain BM869 units exhibit an anomaly in the region of 500 kΩ, where moving the leads produces reading instability at particular values.[EJ6KCpHc--4] The BM786 does not reproduce this behaviour under the same conditions.[EJ6KCpHc--4]

## Auto power-off

The BM786 uses a plain auto power-off timer that is not reset by taking a measurement, so the meter shuts down after its timeout — around 30 minutes — regardless of activity.[BuFoA-qt1PY] It also powers off while in min-max recording mode, which defeats the purpose of leaving a meter logging.[BuFoA-qt1PY] The later BM2257 implements Intelligent Auto Power Off, which resets the timer on measurement and suppresses shutdown in capture and recording modes.[BuFoA-qt1PY] The much older BM235 already behaved this way, so the omission on the comparatively recent 786 is not a generational limitation.[BuFoA-qt1PY] Firmware headroom is a plausible constraint on Brymen designs of this class — the BM235's microcontroller has extremely limited memory space, and feature requests have been declined on those grounds.[BuFoA-qt1PY]

## Construction

The fuses sit inside the main case rather than behind a separate access hatch, the same arrangement used by the Fluke 70 and 80 series.[1351] Case assembly uses proper plastic self-tappers of the type Fluke and Brymen both employ.[1351] Power-on is not a mechanical switch but an electronically switched arrangement using a MOSFET.[f-LTv1GqCMw] The 780-series board carries provisions for Bluetooth in the back of the unit — the series was originally promised with a Bluetooth option — but that option did not ship until the BM787BT appeared roughly five years later.[TkmMitYnHUA]

## Field failures

The BM786 does not have a zero failure rate.[f-LTv1GqCMw] Three distinct fault patterns are documented in returned units.

**Intermittent power-on.** A unit would come on only at certain switch positions, or not at all, with the behaviour changing after the meter had been left off for a period.[f-LTv1GqCMw] Running the meter from a bench supply set to 4.5 V with a 100 mA limit, the fault reproduced: the unit drew about 1 mA when it started correctly, and in the failed state settled at a consistent 0.3 mA, later shifting to a consistent 1.2 mA — a supply current that is repeatable but wrong, and that changed value over the course of the investigation.[f-LTv1GqCMw] Pressing on the battery compartment restored reliable starting for ten consecutive attempts, pointing at mechanical rather than purely electrical causation.[f-LTv1GqCMw] The original owner had already tried a bench supply and cleaned the spring contacts and the pads beneath them without effect.[f-LTv1GqCMw]

**Rotary switch misbehaviour.** Two returned units, out of three faulty over the first three or four months of sales, showed a switch-related fault in which the meter appeared to jump between adjacent positions such as diode and resistance.[IoRks5bJw8Y] The fault is reproducible on some units far more readily than others, and forcing it requires deliberate mechanical loading of the switch.[IoRks5bJw8Y] Root-causing it properly would require dimensional measurement of the plastic parts against the manufacturer's tolerance data — many days of work, and realistically the manufacturer's job rather than the seller's.[IoRks5bJw8Y]

**Insertion error.** Separate returns exhibited a persistent input jack alert, with the meter reporting an insertion error on every range including milliamps and microamps, refusing to take a measurement until switched off.[1663]

## Relationship to other meters

The teardown comparison of the Fluke 77 IV against the BM786 produced an unrelated finding about the Fluke: an average-responding 77 IV can be converted to true-RMS operation, matching a Fluke 177, for roughly ten cents in parts.[1448] Within Brymen's own line, the 786 was under development at a point when it already outclassed contemporaneous models by a wide margin.[SKuZ4_cZjDU]
