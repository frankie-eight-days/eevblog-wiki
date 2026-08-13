# auto ranging

Auto ranging is the ability of a measuring instrument — most commonly a digital multimeter — to select its own measurement range automatically, choosing the attenuation or gain setting that gives maximum resolution for the applied signal. It matters because manual ranging, in which the user pre-selects a range on the dial, is slower to use, and manual-ranging meters carry no price advantage over auto-ranging equivalents, so there is no reason to buy one.[75] Nearly all modern digital multimeters are auto-ranging, whereas analog meters are inherently manual-ranging.[1067]

## Implementation

Auto ranging is implemented at several levels of an instrument's architecture. At the chip level, dedicated multimeter chipsets incorporate the range-switching logic directly: the Fluke 27's proprietary AP25 chip combines the ADC, active filter, buffer integrator, and input network selection that performs the auto ranging[372], the Hycon HY3131 chipset is shared by the 121GW, the Keysight U1282A, and the Gossen Metrahit Ultra[uUCQuIp_hzU][1272], and parts such as the SDIC SD7500 are sold as complete auto-ranging multimeter systems-on-chip including LCD drivers.[1598]

Range switching is done either with relays or with analog switches. Meters that have no manual range switch at all must contain relays, which are audible as a clunk when the range changes.[1457][1704] Oscilloscope front ends similarly use per-channel relays that click on power-up and on every auto-range change.[217] Hardware auto ranging can also be built from comparators that set the thresholds at which range changes occur.[1190] A cheaper alternative avoids switching altogether: the Voltech PM300 power analyser runs several op-amp gain stages in parallel, lets the higher-gain stages overload and saturate, and simply selects the appropriate output.[589]

## Ranging speed

Ranging speed is a primary differentiator between meters and a standard evaluation test. The quick in-shop check is to select ohms and short the probes: if the meter takes much more than about a second to cycle down through its ranges to zero, it is slow.[75] Measured examples span roughly an order of magnitude. The Brymen BM235 ranges in under a second, close to human reaction time.[izCDWjK_pV4] The 121GW takes around three seconds, with the exact time varying depending on where the continuously running measurement cycle happens to be when the input is applied.[izCDWjK_pV4] At the slow end, meters in budget shootouts have been described as "slow as a wet week".[99][1734]

Speed is largely a property of how the manufacturer implements ranging on a given chipset rather than of the chipset itself: the 121GW, Keysight U1282A, and Gossen Metrahit Ultra share the HY3131 yet range at different speeds, while Brymen's fast meters use a custom chipset.[uUCQuIp_hzU] Firmware also matters — 121GW ohms auto-ranging was improved in firmware 1.04, again in 1.05, and again in 2.00, and a community-produced hacked firmware targeted the same slow ranging.[uUCQuIp_hzU][q4gXnpFPFzQ][3MD88EYLdQQ] Update rate and ranging speed are independent: the Agilent U1253A updates its ohms display 14 times per second yet has notably slow auto ranging on that same range.[56]

In automated test systems, avoiding range changes entirely is a throughput advantage: an 8.5-digit voltmeter can be locked on its 100 V range and still read any incoming signal accurately, whereas a 6.5-digit meter may have to change ranges, and each change takes time.[1032]

## Why ranging is needed: dynamic range

Ranging exists because no single shunt and converter can cover the full span of real signals. Measuring microamp-level sleep current in the presence of amp-level bursts with one shunt would require something like a 32-bit ADC, which is impractical, so current-measurement instruments switch shunts.[1190] A device drawing tens of microamps in sleep cannot be resolved on a 180 mA range with a 14-bit converter.[1190]

Auto ranging is not a complete solution to this problem. A true auto-ranging current instrument needs hysteresis so the ranging does not oscillate back and forth on small dips in current, and switching the shunt fast enough not to brown out the device under test is difficult; for some products the only workable approach is a fixed manual range with the device forced into one mode at a time.[1190]

## Failure modes

- **Inductive inputs.** Measuring the primary of a transformer confuses auto ranging — the large inductance makes the meter skip erratically between ranges.[406]
- **Mains-frequency noise.** With too short an integration time (a low number of power line cycles), picked-up 50/60 Hz noise makes meters range chaotically between, for example, the 1 V and 10 V ranges, with relays flicking continuously; a smoothing filter does not fix it, but setting the integration to one or more power line cycles does.[1379][1382]
- **Stuck ranges.** A faulty BM235 measured correctly on a manual range but its auto ranging stuck at a wrong reading (e.g. showing 16 MΩ for a 100 Ω input) — a fault that manifests only in the auto-ranging path.[0z5dGXlRibA]
- **Overshoot.** Some meters overshoot badly while ranging up; in one test a 10 V step produced an 18 V reading on an Extech meter.[91]
- **Mode interactions.** On some meters, engaging min-max or record mode forces the instrument onto a fixed manual range, so an overrange during recording is possible; others stay in auto range during recording.[1692][1731]
- **Auto-scan hazards.** Auto function-selection modes that must identify the input before measuring can mishandle high voltage; one meter in auto-scan mode failed destructively when connected to 240 V mains.[94]

## When to force a manual range

As bench practice, auto ranging is frequently overridden to save time or to get a valid measurement at all. Fixing the range manually avoids waiting for the ranging cycle when probing around a circuit.[1433] Low-level noise measurements on a dynamic signal analyser require a fixed input range rather than auto ranging.[528] In frequency-response measurements, letting the input auto range can clip the channel and corrupt the coherence trace, producing a spurious response that disappears once the range is set correctly.[1443] When measuring capacitors in circuit, the function should be set manually so the auto-selection algorithm is not confused by parallel active elements.[1474] Some meters do not auto range down to the millivolt range on AC volts, so low-level AC signals require manual ranging regardless.[91] Conversely, auto mode can be faster than manual: the Agilent 34461A produces an intermediate unsettled reading on a fixed range that it suppresses in auto mode.[489]

## Related automatic functions

Auto ranging is distinct from, but often bundled with, *auto function selection*, in which the meter identifies what it is connected to — DC volts, AC volts, resistance, or continuity — and switches function as well as range.[1706][1238] Such auto-detection requires firmware thresholds, which introduce arbitrary cut-outs: the Brymen BM2257's auto-sensing LowZ mode stops detecting below about 0.93 V even though there is no electrical reason it could not read to zero.[1667] Auto modes may also search only a subset of functions — volts, ohms, and continuity but not capacitance.[1420] Auto ranging interacts with other features in meter-specific ways: some relative/null modes continue to auto range after the offset is taken, which is the more useful behaviour, while others freeze onto one range.[137][216][249]

Beyond multimeters, the same concept appears as auto set or auto scale on oscilloscopes — where implementations can fail even on a basic 1 kHz sine wave[359] — as per-sample auto ranging in audio and CMRR measurement routines that maximise dynamic range on each acquisition[1521], and in LCR meters, which scan ranges to decide whether a device under test is dominantly capacitive, inductive, or resistive, a decision that depends on the chosen test frequency.[1473]