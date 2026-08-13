# standby power

Standby power is the power a product continues to draw when it is nominally off or idle — the residual consumption of a soft-switched mains device waiting for a button press, or the sleep current of a battery-powered instrument.[164][790][60] Because it is drawn continuously rather than in bursts, a figure of a few watts dominates a product's lifetime energy use far more than its operating consumption does, and in battery products the standby figure is usually what sets shelf life.[1313][320][1287] It is a routine measurement on any product with a soft power switch, and one where measured values across otherwise comparable equipment span more than three orders of magnitude.[790][1659][842]

## Where it comes from

A device with a real mechanical mains switch — a clunking switch, often with a plastic actuating rod running back to the mains board at the rear of the chassis — genuinely disconnects and draws nothing when off.[164][187][475] A soft power button cannot do this: something must stay alive to sense the press, so a small auxiliary supply runs continuously.[378][1032] The same architecture appears in televisions, where a small always-on rail keeps just enough circuitry powered for the infrared receiver to detect a remote command.[1032]

The presence of a mechanical switch is not by itself proof of zero standby. The Agilent InfiniiVision 2000 series had a full mechanical lever-arm switch running back to the mains board and still drew about 6.5 watts with the switch off.[164] The failure was noticed because the instrument stayed warm after being switched off.[164]

Auxiliary loads that are not part of the switching logic inflate the figure further. A frequency counter fitted with an ovenised oscillator draws 17 watts on standby, because the oven and its cooling fan are held powered whenever the instrument is plugged in — behaviour that is intentional, since an oscillator kept at temperature is the point of the option.[647] At the other extreme, one oscilloscope's eight watts of standby went largely to running a heartbeat LED.[800]

## Measured figures in test equipment

Standby consumption in bench instruments varies enormously and correlates poorly with price or brand:

- Agilent InfiniiVision 2000/3000X: about 6.5 watts, at 247 V mains and roughly 256 mA.[164][187]
- Siglent SDS1000X: 8.8 watts, 17.4 VA apparent.[797]
- Siglent 1000X: around eight watts.[800]
- Siglent SDS2000X: almost 7 watts standby, about 40 watts operating.[864]
- Tektronix MDO4000: 4.8 watts, power factor around 0.2 and nearly 24 VA.[199]
- Tektronix TDS2024C: zero, by way of a mechanical mains switch.[187]
- Uni-T UPO2104CS: 2.13 watts, against 26 watts operating.[1038]
- LeCroy WaveJet 354: 1.6 watts, about 7 VA.[790]
- Keysight HD3 with the Megazoom V ASIC: 1.1 watts.[1638]
- Rohde & Schwarz HMO1202: half a watt, 6.3 VA, against 18 watts operating.[842]
- Fluke 45: just over 1 watt, 8 VA, with the transformer and output rectifier and filter capacitors left energised.[791]

Figures in the 5-to-9 watt range are treated as design failures rather than acceptable trade-offs: a six-and-a-half watt standby is the kind of number expected from a 1970s or 1980s VCR, not from modern instrumentation.[164] Sub-watt standby in a mains-powered instrument is achievable and is the benchmark against which the rest are judged.[842][1659]

## Power factor and apparent power

Standby power factor is almost always poor, because the small auxiliary supply is lightly loaded and non-linear. A scope drawing half a watt real still presents 6.3 VA; one drawing 1.6 watts presents about 7 VA at a power factor of 0.23; one drawing 4.8 watts presents nearly 24 VA.[842][790][199] A hot air station measured 0.07 watts in soft-button standby yet still drew significant apparent power.[1659] The same instruments show much better power factor once operating — 0.64 to 0.86 is typical — because the supply is then properly loaded.[790][164][864]

Domestic consumers are generally billed on real power and not on apparent power, while commercial customers often are.[971] The generation and distribution system, however, must still be sized for the apparent power, so a poor standby power factor imposes a system cost even where nobody is billed for it.[971]

## Battery-powered standby

In battery products the relevant quantity is sleep current, and the design target is that standby consumption should be negligible against the cell's self-discharge — that is, the product should last its battery's shelf life.[320][1287]

A handheld multimeter drawing 75 microamps in sleep mode gives more than a year of standby from an alkaline 9 V cell, making auto-off nearly as good as switching the instrument off.[60] A handheld LCR meter specified at 2 microamps powered off measured 0.5 microamps, comfortably inside spec.[137] Another instrument settling at 55 microamps standby, against a nominal 800 mAh alkaline 9 V battery, works out to roughly 14,000 hours — effectively the shelf life of the cell.[320] Around 10 microamps is a reasonable figure to assume as typical standby consumption when designing a representative load.[hSkaZEgrZkY]

Low-power programmable logic makes similar numbers available in more complex designs: the Lattice iCE40 LP1K used in a smartwatch, with 1280 logic cells, 64K of RAM and a PLL, has a 21 microamp standby figure.[761] At the extreme, an Amstrad NC100 notepad measured on the order of 10 nanoamps — effectively nothing.[385]

Where standby is the dominant load, the arithmetic is unforgiving in the other direction too. A battery-powered shredder mechanism has roughly a month of standby per 50 mW of consumption before the cell is exhausted, leaving nothing for the motor; multi-year receiver standby is achievable, but only by deliberately reducing consumption.[1136] A shopping trolley lock running a very low-power microcontroller from a large lithium primary should manage 5 to 10 years, since only the lock and unlock motor drive takes significant current.[1287]

Software can wreck an otherwise sound standby design. A navigation utility running on a Nokia E71 kept a process alive with the phone in standby, producing a repeating square-wave current pulse of several seconds high and several seconds low, which raised average standby consumption to about 0.18 watts and cut endurance to roughly two days against an advertised 480 hours.[80]

## Consumer products and aggregate load

Consumer equipment measurements cluster around the one-watt mark. Mini PCs measure 1 W and 1.5 W in standby; a desktop video-editing machine measured about 0.4 watts; an 86-inch LCD television measured 1.3 watts before its backlight came on; an inkjet printer measured 100 milliwatt standby.[1656][1649][462][Ia4xB9wk80o][1421] A Yamaha receiver achieved 0.1 watts using a novel and convoluted low-power supply topology built around a half-wave rectified tap with a feedback path through Q1.[379] Another product measured 0.12 watts against a manual figure of about 0.1 watts, which confirmed the mains input and fuse were intact and pointed the fault at the soft power switch circuitry instead.[378] Half a watt is a fair expectation for a well-designed television standby supply.[915]

Individually small figures aggregate badly. A household audit put whole-house standby at around 100 watts with everything switched off, possibly as low as 90, reducible to 80 or 90 by removing the Wi-Fi and NBN modem.[1505] The contributors are the usual soft-sense devices — printer, games console, DVD player, network hub, television, sound bar, streaming stick — each drawing a watt or so and jumping around too much to read a stable figure.[1505] A well-equipped laboratory was found to be throwing away about a kilowatt in standby alone, much of it in bench supplies and in RF equipment holding oven-controlled crystals at temperature.[s2KkgI-kyK0] A whole-house energy monitor with sufficient resolution can be used at night, with everything nominally off, to attribute the residual draw device by device by unplugging plug packs one at a time.[877]

## Regulation and design practice

Energy efficiency legislation — Energy Star, and the MEPS regulations — makes it illegal in some countries to sell chargers and similar products that fail to meet a specified standby power figure and efficiency, which can rule out a product concept outright at the proposal stage.[n4NBUruLyoo] Consumer-grade brick switching supplies are designed against these rules and are commonly specified below one watt in standby.[1032]

Test and measurement has historically had an easier time of it, and instruments built around a mains transformer face a hard floor: with the transformer energised and the supplies on its output engaged, there is a limit to how low standby can go.[1032] The consumer architecture — a small always-on supply feeding only the wake-up circuitry, with the power button wired separately from all other front-panel buttons — is migrating into instrumentation and can bring standby down to around 100 milliwatts.[1032] The commercial pressure that drives this is partly ergonomic rather than environmental: large mechanical power switches take up panel space and require a plastic rod running fore and aft, so manufacturers prefer soft switches and must then engineer the standby figure down.[1032]

A standby indicator LED is a design choice in its own right and can be badly judged. An instrument whose standby LED is bright enough to glare across a darkened lab is behaving like a consumer product rather than professional equipment.[199]

## Zero-standby claims

Claims of eliminating standby power entirely warrant scrutiny about where the loss actually sits. A sensor-driven voltage detector IC — a five-pin SOT-23 part designated UBM20, requiring no supply of its own and drawing its operating power from the sensor signal — was demonstrated waking a television from the infrared signal of a standard remote control at a distance, giving a set with no continuous standby draw.[971] The demonstration is misleading as a product case, because the television's own standby consumption sits alongside the quiescent draw of the plug pack feeding the arrangement; the chip removes the former while the latter, at around 4 VA for a plug pack under no load, remains.[971] Conventional standby supplies in this application already reach the order of five to ten milliwatts, so energy harvesting is not solving the loss that dominates in mains-powered products.[971]

The same reasoning applies to folk beliefs about mains outlets themselves consuming power when switched on with nothing plugged into them, which they do not.[CYm-4gbl1Zc]
