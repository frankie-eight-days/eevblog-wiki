# resolution bandwidth

Resolution bandwidth (RBW) is the width of the filter a spectrum analyser sweeps across the frequency span, and it sets how much detail can be resolved on the displayed trace.[891] It is the single control that most determines whether closely spaced signals appear as distinct features or merge into one blur, and it simultaneously governs the instrument's noise floor and its sweep speed.[891] On a swept analyser it lives in the bandwidth menu alongside video bandwidth, averaging type and detector selection.[891]

## What narrowing the filter buys

A narrower filter passes less noise power, so reducing RBW drops the displayed noise floor.[891] It also exposes structure that a wider filter integrates away: on a −70 dBm 1 GHz carrier, a 10 Hz setting shows sideband detail that is entirely absent at 1 kHz, where no signal detail is visible at all.[891] Comparing an instrument with a 10 Hz minimum against one limited to 100 Hz, the narrower filter resolves close-in detail the wider one cannot, and zooming the span in instead is not an equivalent substitute.[891] The same effect appears at the coarse end of the scale: dropping to a 100 Hz filter is enough to see the individual peaks of a hand-tuned LC-oscillator transmitter spread across a broad band.[767]

Where the difference is an order of magnitude — 10 Hz versus 100 Hz — it is a substantial reason to prefer one instrument over another, and by itself can justify the price difference.[891] A 10 Hz RBW "could be worth the price of admission on its own".[891]

## The cost: sweep time

The penalty for a narrow filter is time. Update rate falls sharply as RBW is reduced, and a full sweep on an entry-level analyser with a low RBW set can take on the order of 50 seconds.[845][891] Raising RBW restores responsiveness immediately: on one instrument the front panel effectively locked up while cursors were moved at a low setting, and changing to 10 kHz returned near real-time cursor movement.[645] Sluggishness at low RBW settings is an implementation defect rather than an inherent one — an instrument that becomes practically unusable at its narrow settings has a processing-architecture problem, not a physics problem.[645]

Because of this trade-off, RBW is normally coupled to span. Many instruments select it automatically, narrowing the filter as the span is reduced.[95jpp3txM0o] The minimum available RBW may itself depend on the span in use.[1529] Setting a wide span forecloses the narrow filters that would be needed to see low-level coupling artefacts, so such artefacts only become visible when zoomed right in.[891] Other settings can also constrain the range: on one analyser the minimum RBW rises to 30 kHz whenever the tracking generator is switched on, producing an "RBW out of range" error at narrower settings.[891]

## Typical values in practice

- Conducted EMC pre-compliance over the 150 kHz to 30 MHz range uses a 9 kHz RBW, with the analyser's dedicated EMI filter type selected in preference to the Gaussian filter.[548]
- Radiated near-field probing uses the industry-standard 120 kHz EMI-filter RBW to approximate what a compliance lab would measure.[1176]
- Broad survey work — an 8 GHz microwave amplifier checked over a 4 to 8 GHz span — runs at 1 MHz.[XqakD0dXdjM]
- General emissions hunting on a 0 to 10 MHz span uses 300 Hz, giving a baseline below −105 dBm with nothing connected.[645] The same 300 Hz setting over a 4 MHz span serves for comparing oscilloscope jitter spectra before and after a firmware change.[699]
- Noise-floor characterisation on a 1.5 GHz span is conventionally done at several settings at once — 1 MHz, 100 kHz and 10 kHz — using trace mode to hold all three.[891]

## Instrument limits

Minimum RBW is a headline specification. Entry-level analysers of the DSA815 class bottom out at 100 Hz; contemporaries in the same price bracket reach 10 Hz, and a 30 Hz intermediate setting unavailable on the former resolves detail the 100 Hz filter loses.[891] Higher-end models reach 10 Hz at around the $5,000 mark for 2 to 3 GHz coverage.[207] A VNA-capable analyser goes down to 1 Hz and offers EMI filtering as an option; unterminated with the preamp on it sits a little above −115 dBm at 10 kHz RBW.[1101] Increasing RBW to 1 MHz on that instrument gives the expected much faster update rate.[1101]

## Oscilloscope FFTs

Scope FFT implementations vary in whether RBW is exposed at all. Where the FFT is built on traditional scope maths functions, centre frequency and Hz per division can be set but resolution bandwidth cannot, so the instrument does not behave like a spectrum analyser.[1220] Better implementations present RBW directly, either as a value that can be typed in alongside the span[1188] or as an auto/manual RBW control displayed in kilohertz.[1529] An FFT resolution of 122 kHz is close enough to the 120 kHz EMI filter of a real analyser for near-field probe comparisons, though averaging helps.[1188] Where the minimum achievable RBW is too coarse — an instrument unable to resolve below roughly the scale of a 100 kHz sine wave — the FFT is of no use for frequency-domain analysis.[1701]
