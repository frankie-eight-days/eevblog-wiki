# microinverter

A microinverter is a small grid-tie inverter installed one-per-panel, typically mounted on the racking directly beneath each solar panel, that converts that panel's low-voltage DC (nominally around 40 V) straight into mains AC (240 V) rather than feeding DC into a shared string inverter.[1385][BtQUuD6QRMw] Functionally, microinverters and string inverters are the same kind of device — "Inverters and microinverters are identical, effectively identical" — the distinction being one inverter per panel instead of one per entire series string.[BtQUuD6QRMw] The architecture trades higher hardware cost for per-panel maximum power point tracking, per-panel monitoring, fault isolation, and the elimination of high-voltage DC cabling.[1386][1426][1385]

## Electrical characteristics

A representative unit, the Enphase IQ7+, accepts a maximum input voltage of 60 V DC, suiting panels that produce around 40 V in normal operation and up to about 41 V open circuit, leaving comfortable headroom against the 60 V absolute maximum.[1385][BtQUuD6QRMw] Continuous AC output of the IQ7+ is 295 W, which is why the rating matters when matching to higher-wattage panels.[1386][WtGlolw-BxA] Multi-channel variants condense several microinverters into one enclosure: the Hoymiles HMS-800T is a two-channel 800 W unit, and four-channel units exist with a 16–60 V MPPT window, 22 V startup, and 400 VA per channel.[BXVgk-uoxn8][1516][puGooNKVE74] Typical conversion loss is around 5% before cabling; measured Enphase IQ7+ efficiency data shows about 93% at the 10% power point.[632][1386]

A defining grid-tie behaviour is anti-islanding: a microinverter that is fully powered on the solar side will not energise its output unless it detects the grid, a compliance and safety requirement.[1626]

## Advantages over string inverters

- **Shading and fault isolation.** In a series string, shading or failure of one panel degrades the whole string; a thin shadow covering only a couple of cells has been observed to cut a 12-panel string's output by 10–20%.[1426][NoIjTK249D0] With microinverters, a dirty, shaded, faulty, or bird-soiled panel trips its bypass diodes and drops out alone — 13 of 14 panels could fail and the remaining one still produces full power.[1385][1426][1386]
- **Per-panel MPPT.** Maximum power point tracking operates on each panel individually rather than across an entire string, extracting more energy under mismatched conditions.[1426]
- **Safety.** Output is 240 V AC per panel instead of a 450–500 V (or higher) DC string. High-voltage DC sustains a plasma arc that does not self-extinguish the way AC does at zero crossings, and DC isolator switches are a known rooftop fire source — a hazard the microinverter architecture removes.[1385][WzpXyNNZg38]
- **Monitoring.** Because each unit is individually serial-numbered and addressed, systems can be mapped to a photograph of the roof, yielding per-panel power, energy, AC voltage, DC panel voltage, frequency, and microinverter temperature, and making a failed or underperforming unit immediately identifiable by location.[1628][M4IiR4vW0aY][1390]

## Cost and trade-offs

Microinverter systems cost more than an equivalent string-inverter system simply because there is one inverter per panel; individual units run around US$150, which can exceed the value of an older 250 W panel and makes retrofitting them onto an existing small string system uneconomic.[1386][1426][M4IiR4vW0aY] String arrays remain the cheaper solution where shading is not a concern.[1426]

## Panel oversizing and output clipping

It is common and legitimate practice to pair a panel with a microinverter rated below the panel's nameplate power — for example, 370 W or 415 W panels on 295 W IQ7+ units.[1386][1628] The consequence is clipping: the panel can never deliver more than the inverter's limit, so a 14-unit system built from 5.1 kW of panels peaks at about 4.13 kW even on the best day of summer.[1386][WtGlolw-BxA] For a 295 W / 370 W pairing in a high-insolation location, clipping occurs on roughly 38% of days nominally, but the energy lost is only a single-digit percentage of the annual total.[1386] Counterarguments favour deliberate oversizing: per-panel MPPT and shading immunity recover energy across the year, and an underrated inverter may run more efficiently at the power extremes.[1386] Manufacturer availability constrains the choice — Enphase did not offer a 370 W-output unit, and higher-rated microinverters from any vendor carry a significant price premium, which feeds directly into the payback calculation.[1386]

## System architecture and communications

Microinverters are AC-coupled in parallel onto a shared mains bus, with each unit individually addressed by serial number; in the Enphase system, Q relays each support up to 11 microinverters per branch.[1682][1626] A separate mains-powered gateway (the Envoy) aggregates data and is supposed to report at roughly 15-minute intervals around the clock, even with no solar production.[uE0x8YR7nMg][1385] Communication travels over the mains cabling itself and is slow — a backlog of around 100 days of buffered per-unit data can take days to upload after an installation is first connected.[1626]

## Reliability

Because they live outdoors under panels, microinverters are hermetically sealed, and their thermal design must account for the full rooftop environment; reliability expectations are high enough that Enphase backs its units with a 10-year warranty.[1385][isnXYy9vCag] Failures do occur and are observable precisely because of the per-unit monitoring: a single unit among 14 stopped reporting after roughly four years, triggering an email alert, with the faulty unit identified by its status LED and replaced under warranty.[1682][isnXYy9vCag] A Hoymiles two-channel unit has also been observed failing with mains present at its input but no output.[puGooNKVE74][GFlckdPzYQQ]

## Integration with hybrid inverters

Some hybrid inverters — the Deye 5 kW unit being a noted example — provide a generator port that accepts not only a diesel generator but also microinverter input, selected via a software checkbox; this AC-couples the microinverter array through the hybrid and keeps the microinverters producing when the grid fails.[1610][1620][BXVgk-uoxn8][T2yNMQM_TEA] A quirk observed on the Deye is a persistent, physically unaccounted-for 84 W reading on the generator port whenever microinverter mode is enabled, which measurement against battery current shows is not real power flow.[kCtGoymiShU]

## Suitability limits

Commodity microinverters are designed for efficient rooftop panels generating substantial power; they are a poor match for very low-output sources. Solar roadway and pavement tile proposals suffer specifically because off-the-shelf microinverters assume far more power per panel than a tile produces, because microinverter-plus-cabling losses of around 10% must be budgeted into already marginal output, and because dedicating a microinverter to each small tile multiplies embodied energy far beyond that of a conventional panel per watt delivered.[1363][632][1389]