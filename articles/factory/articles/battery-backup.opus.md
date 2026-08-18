# battery backup

Battery backup is the practice of holding a small secondary cell across a circuit's power rail so that a defined subset of the system — volatile memory, a real-time clock, calibration constants, or in larger installations the whole load — survives loss of primary power.[942][116][615][1177] In the era before cheap non-volatile storage it was not an optional refinement but the only mechanism by which a portable computer, an organiser, or a data logger retained anything at all when switched off.[418][1209][1662] The backup cell is therefore a load-bearing part, and because it has a finite life it is also one of the most common failure points in aged equipment.[615][639]

## Retaining volatile memory

Before EEPROM and flash were commonplace, user data lived in SRAM and stayed there only as long as the cell held up.[1662][1209] The Apple Newton used five Mitsubishi 128k x 8 SRAMs for a total of 640 KB of storage with nothing in flash, so the backup battery was the sole thing keeping a user's data alive; later Newtons moved to flash.[418] The Tandy Radio Shack Model 100 carried a backup battery for its CMOS memory, allowing the main cells to be removed and replaced with contents intact.[116] The Tandy 200 exposed the arrangement directly as a memory protect switch: with it on, the backup battery held the RAM; switched off, everything was lost, including a week's worth of typed BASIC or documents.[1662]

Parts intended for this duty are specified for retention well below their normal operating rail. The Samsung KM68-series SRAMs found in battery-backed designs run as 5 V parts in system but retain data down to 2 V, which is what makes a 3 V lithium cell a viable holdover source as it sags.[942]

A common consequence of SRAM-only storage is that the main and backup cells form an interlocked set. Pocket organisers of the period carried one or two operational batteries plus a backup battery, and removing all of them at once would lose the contents, leaving only the reserve charge on the main capacitor.[1209] The Casio FX730P made the dependency explicit in both directions: replacing the backup battery required the two operational cells to be fresh, and replacing the operational cells required the backup cell to be good, since there was no other storage.[1102] The reservoir capacitor amounted to a third tier of holdover worth perhaps a few tens of seconds.[1102] Large supercapacitors serve the same memory-retention role, sometimes alongside a battery, and 5 F 5 V parts in compact packages are well suited to it.[1043][214][619]

## Power switching

The standard method of bringing a backup cell onto a rail is diode steering: one diode from the battery, another from the main supply, so that when the main rail fails the battery diode takes over and powers the memory.[942] The switching is deliberately confined to the parts that need it — in the FX730P the diode steering feeds only the SRAM, not the whole machine.[1102] Where the backup cell is rechargeable, a series resistor sets the trickle charge from the main rail.[815] In energy-harvesting front ends that combine a piezoelectric source with a battery, a reverse protection diode is required because nothing internal prevents the harvesting element from reverse charging the battery on the input pin.[534]

## Real-time clocks and calibration data

The other dominant use is keeping a real-time clock running. Instruments and appliances that timestamp data almost universally carry a cell next to a 32.768 kHz watch crystal and an RTC chip: gas-detection data loggers,[603] source measure units,[607] bench multimeters,[485] oscilloscopes,[976] electric vehicle chargers,[1437] access control readers that log card swipes by time and date,[673] and even a heart defibrillator, whose clock exists so the unit can record when an incident occurred.[909] The absence of the feature is equally diagnostic — the earliest portable computers had no backup battery and no real-time clock, so they could not keep the time when switched off.[955]

Calibration constants are a distinct case. Older multimeters commonly held their calibration data in battery-backed storage, whereas a newer instrument with no backup battery is holding it elsewhere.[478] The Prema 6047 stored its constants in a Dallas non-volatile RAM whose internal cell has a nominal ten-year life and cannot be replaced; when it goes, the chip is scrap.[615] In practice such parts have been observed still working after nearly twenty years.[615] Where a modern instrument does carry a cell, it is generally for the clock alone and not for calibration.[485]

Losing the backup is not always catastrophic but is always visible. A Fluke Combiscope missing its rear backup battery no longer retains digitally controlled focus, intensity and trace settings, so they must be reset at every power-up.[1450] Metrology-grade equipment that cannot be turned off without losing its state needs full battery backup as a matter of course.[s2KkgI-kyK0]

## Ageing and failure

Checking the backup cell is a routine early step when diagnosing dead vintage gear, before the power supply is even measured.[620] A healthy cell reads close to its nominal voltage — 2.92 V in a Stanford Research SR650, 3.42 V in a Tandy 102, both with no corrosion on the contacts — though in equipment of that vintage replacement is prudent regardless.[620][1376] Anomalously high readings indicate a fault elsewhere: a Toshiba T1000LE's backup-battery SRAM rail measured 7 V against a datasheet value of 5 V.[1527]

Failed cells announce themselves through system errors and through leakage. An IBM L40SX reported error 161, a backup battery error, on a machine whose cell was either dead or had leaked onto the motherboard.[639] Corrosion and crustiness around the cell are typical of surviving 1980s and 1990s hardware.[438][1334][1587]

Serviceability varies. Some designs are built to be opened for cell replacement.[1102] Consumer products increasingly solder the backup cell directly to the board with no user access, as in a JVC camcorder and a GoPro Hero 4 Silver.[454][672] The non-replaceable case is the Dallas-style module, where cell and silicon are a single sealed part.[615]

## Security applications

Battery-backed SRAM is used deliberately as a tamper-erasable store. Payment pin pads are expected to combine tamper switches, potting, and battery backup wired through contacts so that opening the case breaks the connection and the memory is erased.[686][1110] The volatility is the security property.

## System-level and mains backup

At the equipment level, backup batteries keep telecommunications running through outages: a PABX takes an external battery so the system stays up for a period after the mains fails,[1177] and fibre network terminations offer an optional battery backup module so the telephone still works when local power goes out.[913] Alarm systems run from their backup battery when mains is absent, which shapes the design — PIR sensors use normally closed relay contacts specifically so that the quiescent state does not consume power while running on backup.[275][1505] Consumer surge-protection-plus-battery-backup units combine both functions in one heavy box.[463]

At the household level the sizing question is which loads actually need to ride through. A whole-house backup battery is unnecessary if the requirement is fridges, freezers, lights and emergency circuits.[JSahPkUjDYA] A 3.6 kWh backup battery was sized against three domestic fridges and freezers and verified by test to last, with an automatic transfer switch used to move those loads over on failure.[1500] Battery backup also pairs naturally with rooftop solar, giving an independent off-grid capability alongside the grid-tied system,[dlOtqDPCO1o] and electric vehicles capable of exporting energy back to the home can serve as a backup battery in the same role.[3EgRMEc8R_I]

Omitting backup is a defensible choice only when the consequence of a power interruption is trivial. A home-built digital clock with no backup simply stopped when the mains failed, which was tolerable given a stable supply.[801] A month-long thermal chamber cycling test run without battery backup on the data logging equipment is the opposite case: any power glitch would have reset everything and destroyed the run, and Dave Jones regards having half-done it that way as a mistake despite getting away with it.[s2KkgI-kyK0]
