# bandwidth limit

A bandwidth limit is a selectable low-pass filter in the front end of an oscilloscope or probe that deliberately restricts the input bandwidth below the instrument's full specification.[704][601] Its purpose is almost entirely noise reduction: the higher the bandwidth, the greater the inherent noise of the amplifier and other front-end circuitry, so cutting bandwidth cuts the noise the instrument adds to the measurement.[601] A 20 MHz limit is the near-universal implementation, present on practically every oscilloscope, and it doubles as the standard measurement condition for power supply ripple and noise.[879][1735][704]

## The 20 MHz convention

Twenty megahertz is the standard value, and on lower-end instruments it is often the only one offered.[704][1566] It persists for historical reasons, but it is also the conventional bandwidth over which noise is specified and measured, which is why it appears on essentially every instrument regardless of price or class.[1735][1266]

Because ripple and noise specifications are written against a defined bandwidth, the measurement is only valid if the scope is restricted to that bandwidth.[594] Switching between 20 MHz and full bandwidth on a supply rail produces two very different numbers, and only the limited one corresponds to the specification.[594] Where an instrument provides no such limit, a series filter must be added ahead of the input to create one.[594] The distinction matters in the other direction as well: the 20 MHz limit is specific to noise measurement, and when the goal is the actual signal fidelity of a rail, the limit must come off so that transients remain visible.[1735]

The convention is also useful as a levelling condition when instruments are compared. Noise comparisons across several oscilloscopes are run with every unit set to a 20 MHz bandwidth limit and the same memory depth, with averaging off, so that front-end noise is the only variable.[1000][n4NBUruLyoo]

## Available settings

Beyond the standard 20 MHz value, higher-end front ends offer intermediate steps. One instrument provides full 100 MHz plus 20 MHz and 200 MHz settings per channel, an unusual range for its class.[792] Software-defined bandwidth limiting appears on some scopes as a set of selectable filter options rather than a single switch.[1521] Working settings in practice range from 20 MHz for low-level noise work up to 50 MHz for common-mode rejection measurements and 200 MHz in high-resolution acquisition modes.[1521][1557][1328]

Differential probes carry their own limits. A high-voltage differential probe with an internal microcontroller, ADC and DAC provides a 5 MHz bandwidth limit alongside offset nulling, and the same 5 MHz limit carries across the related model range.[1631][1744] Engaging it on a 10 MHz test signal produces the expected attenuation.[1744] An older probe generation lacking the feature leaves no option but an external filter, or accepting the noise.[1631]

Some low-level ranges force the limit on automatically. On one instrument the datasheet carries an asterisk noting that at 1 mV per division the bandwidth limit is set to 20 MHz automatically; on another, selecting 2 mV per division engages the limit and annotates the display accordingly, so the full 300 MHz bandwidth is not available at the most sensitive setting.[474][480]

## Implementation

In modern digital oscilloscopes the limit is usually a function of the programmable gain amplifier that drives the ADC rather than a discrete filter. The LMH6518 is a 900 MHz programmable gain amplifier with SPI-controlled gain and internal bandwidth limits on its output at roughly 60, 100, 200 and 350 MHz, and it is the recommended front-end device for the associated ADC.[475] A single SPI command sets the 20 MHz limit, and the same mechanism is the most likely means by which software-licensed bandwidth upgrades are delivered.[879] Programmable gain amplifiers with integrated bandwidth-limiting filters appear in high-end front ends alongside relay-switched attenuator stages.[1639]

The alternative is fixed component selection. A manufacturer whose model is not software upgradeable may instead fit different resistor or capacitor values to set the bandwidth elsewhere in the signal path, though doing so forecloses any later bandwidth-upgradeable variant.[475] In one entirely discrete transistor-based front end, where the 50, 70 and 100 MHz model bandwidths are purely software-configurable, determining how the bandwidth limiting was implemented required reverse engineering the board.[675][675] The limiting in these designs is genuinely analogue and ahead of the converter: feeding in a 100 MHz signal shows real attenuation before it reaches the ADC.[37]

Where the SPI traffic is accessible, the bandwidth-limit control bits can be identified by watching which data bits toggle as the front-panel button is pressed. In one investigation of a 24-bit frame carrying 8 command bits and 16 data bits, the expected bits did not change on the write operations at all, indicating a problem with the capture rather than the theory.[879]

## Practical use

Turning the limit off is the direct way to see what it was hiding. On a step response, removing the limit reveals overshoot, ringing, transmission-line effects and termination effects that the filter had smoothed away — the point at which the difference between an in-line 50 ohm terminator and an alternative arrangement becomes visible.[6XpyOGw6RFM] Conversely, engaging it visibly cleans up a noisy trace.[876][601]

Matching the limit to the probe is sound practice. Where the probe's own bandwidth is the binding constraint, setting the channel limit to the probe bandwidth costs nothing, since going higher only admits additional noise.[1557] The same reasoning applies to instruments whose bandwidth is itself the limitation: a 5 MHz positional current probe cannot resolve the harmonics of a 1 MHz switching supply, which easily exceed 5 MHz.[296] Bandwidth constraints are one reason to select a purpose-built instrument rather than improvise — a power rail probe exists because AC coupling an active probe discards low-frequency fluctuations and introduces bandwidth limitations of its own.[1733]

A limit left engaged is a standing measurement trap: an amplitude reading taken with the 20 MHz limit still on will be attenuated, and the discrepancy is easy to chase in the wrong direction before the setting is noticed.[1492][1492]

Since the setting materially changes what a circuit does, it belongs on the schematic. Annotating an input filter with its design intent — a 20 MHz bandwidth limit, for example — and placing the note beside the relevant side of the switch tells a reader what the RC network is for, rather than leaving them to infer it from component values.[1129][1129]

## Interface and defect notes

Access to the limit is a recurring point of instrument criticism. Burying bandwidth selection inside a dedicated bandwidth menu is poor grouping for a control used this often.[1529] A channel-menu button that highlights the bandwidth limit before it can be toggled wastes a button press where a direct toggle would do.[1231] The absence of the control altogether marks an instrument as not yet behaving like a regular oscilloscope; the 20 MHz limit is treated as an industry-standard expectation.[1709]

Defects appear here too. On one instrument, the full-bandwidth selection worked on channel one but could not be restored on channel two, leaving that channel stuck at the limited setting.[ByUiOk00K0U][ByUiOk00K0U] On another, a low-frequency acquisition with the 20 MHz limit engaged produced anomalous behaviour consistent with an acquisition bug.[l-fuyHCs2Sw] Analogue and combination instruments carry the control as well, alongside peak detect and envelope modes.[1450]
