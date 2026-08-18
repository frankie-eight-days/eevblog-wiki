# junction temperature

Junction temperature is the temperature of the semiconductor die itself — the actual junction inside a transistor, diode, regulator or LED where power is dissipated.[105][222] It is the quantity thermal design exists to control: airflow, heat sink size, thermal compound, copper spreaders and vias are all only means to the end of holding the die at a safe value.[105] It is also the temperature that datasheet performance curves are plotted against, so it governs a device's electrical behaviour as well as its survival.[222][908]

## Why it cannot be measured directly

The junction is buried inside the package and cannot practically be probed.[105] Putting a probe on the case gets closer, but the case is still not the junction.[158] The working method is to measure what can be reached and calculate the rest: measure the case or heat sink temperature, take the junction-to-case thermal resistance from the datasheet, multiply it by the dissipated power, and add the resulting rise to the measured temperature.[105][158] Heat builds up in stages along the path — die to case, case to heat sink, heat sink to ambient — with each thermal resistance adding its own rise, so the junction always sits at the top of the ladder.[105][744]

A worked example on a power transistor: with 10 W dissipated and a junction-to-case resistance of 3.1 °C/W, the junction sits 31 °C above the case. A measured case temperature of 87 °C therefore implies a junction of roughly 118 °C.[105] Adding forced cooling to the same setup brought the case down to 47 °C, putting the junction at 78 °C — the same 31 °C differential, but a drastically lower die temperature.[105] In another version of the calculation, a heat sink at 70 °C with 3 °C/W and 10 W put the junction at 100 °C.[105]

Which thermal resistance to use depends on the mounting. Junction-to-ambient covers a device standing free on the board with no heat sink; one part with a junction-to-ambient figure of 62.5 °C/W reaches 82 °C at just 1 W in a 20 °C room, hot enough to burn a finger on contact.[105] Once a heat sink is attached, the junction-to-case figure is the one that feeds the calculation.[105]

Some devices report their own junction temperature through an on-chip PN junction used as a temperature sensor. Such sensors are crude but adequate, and respond visibly to something as simple as a finger placed on the package.[642]

## Choosing a target

There is no universal correct junction temperature; the target is usually a ballpark engineering choice, with something around 80 °C a common aim, on the reasoning that every 10 °C of margin below the limit buys reliability.[105] Absolute maximum ratings sit far higher — a semiconductor might be rated for 120 °C absolute maximum junction temperature, an LM317 for around 125 °C, a power MOSFET for 175 °C junction and storage — but designing to the absolute maximum defeats the point, particularly for equipment intended for long industrial service.[744][512][895][773]

Manufacturers also impose secondary limits that must be read alongside the junction rating. An 80 W LED module rated at 4.8 A maximum forward current and 115 °C maximum junction temperature also carried fine print requiring the aluminium PCB to stay below 85 °C, which in turn constrains how hot the heat sink behind it may run.[773]

The design lever is the number of thermal resistances in series. Going straight from case to heat sink, avoiding intermediate vias, sil-pads and heat transfer bars, keeps the whole system at a lower temperature and gets heat away from the junction efficiently.[744] Surface-mount parts in small handheld enclosures make this considerably harder, since the usual escape route of a fan is unavailable when only a few watts are involved.[744]

## Effect on electrical behaviour

Datasheet curves are frequently plotted against junction temperature, not ambient, and treating the two as the same is a standard trap.[222][158] A specification quoted at 25 °C refers to the die, not the room; a supply dissipating real power can easily push its junction to 100 °C or beyond while the lab stays at 25 °C.[222] Amplifier offset voltage is one casualty — a part specified at roughly 0.5 mV of offset at 1 A load drifts to about 0.75 mV once the junction reaches 125 °C, which matters in precision designs.[222] MOSFET gate-source threshold voltage is another, characterised in datasheets explicitly as a function of junction temperature; where a device runs cold and dissipates almost nothing, the junction stays near ambient and the curve can be ignored.[260][1461]

Zener diodes are a particularly direct case because they are typically used as power devices and heat themselves.[908] Their dynamic resistance varies with both current and junction temperature, so self-heating feeds back into the regulation.[908] Dissipating a quarter of a watt in a small package — 5.1 V at 50 mA — is enough to raise the junction and shift the dynamic resistance.[908] With the series resistor dropped to around 100 Ω and the input taken to 15 V, the output rose from 5.22 V to 5.47 V as the junction heated, against roughly 100 mV of movement with a 1 kΩ resistor.[908]

Passive components are exempt from this class of limit. An inductor dissipating power in the same converter has no maximum junction temperature to violate and is correspondingly more tolerant than the active semiconductors around it.[895]

## Design failures

Excessive junction temperature is a recurring finding in commercial equipment. A bench power supply using an ST LM317 rated to roughly 125 °C junction was measured with its heat sink already over 100 °C; with 5 °C/W and 5 W dissipated, the junction sat at least 25 °C above that, comfortably past the rating even with the intended airflow.[512] The same design used thin tabs offering little thermal mass.[512] An electronic load's linear regulators were too hot to touch at 80 °C on the case alone, placing the junction well above that figure and with the lid still off.[1023]

A model-aircraft BEC regulator measured 161 °C on its heat sink under nominal rated airflow, against a calculated rise consistent with that figure, and far above the maximum junction temperature of the semiconductors it fed.[895] Its MOSFET carried an absolute maximum junction and storage temperature of 175 °C, and the heat sinking sat on the opposite side of the board with only vias conducting heat through, adding further loss to the path.[895]
