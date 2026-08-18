# volts per division

Volts per division is the vertical scale factor of an oscilloscope: the voltage represented by one square of the graticule, the grid ruled across the display.[926] Measurement on a scope is fundamentally a matter of counting divisions and multiplying, so the vertical amplifier is calibrated in volts per division rather than in absolute screen units — at a setting of 1 V per division, each division a trace rises corresponds to one volt.[926] The available range of settings, the granularity of the steps between them, and the smallest setting the front end can honestly support are among the defining specifications of any scope.[792][1501][1317]

## The step sequence and fine adjustment

The volts per division control normally moves in a 1-2-5 sequence, though the exact progression varies between manufacturers.[1226] A typical ladder runs 1 mV, 2 mV, 5 mV, 10, 20, 50, 100, 200, 500 and onward through the volt ranges.[1226] Departures from the convention exist: the Zotek ZT-702S steps 10 V, 5, 2.5, 2, 1, then 500 mV, with an audible relay click between the 200 mV and 500 mV ranges.[1540]

Because those steps are coarse, a waveform can easily end up too large or too small for the screen at every available setting.[1226] Most modern instruments therefore make the volts per division encoder pushable, switching the channel into a fine mode in which the scale can be adjusted in much smaller increments.[1226] Implementation is uneven — the Rohde & Schwarz HMO1002 makes the volts per division control pushable for fine mode but provides no equivalent push on the vertical position control.[793] On the Owon SDS the volts per division knob at least has detents, unlike some of the other controls on the front panel.[480]

Autoset routines choose a setting by the same logic: the algorithm picks a scale that leaves roughly a division of clearance above and below the waveform, then refines it with a fine volts per division value, which can be overridden manually.[6XpyOGw6RFM]

## Effect on measurement accuracy

Scale selection is not cosmetic. Automatic measurements can fail outright when the range is wrong, and reducing the range — for instance down to 1 V per division — is what allows the instrument to begin measuring at all.[1226] After any change of range or time base, measurement statistics should be restarted, since accumulated error from the previous settings can otherwise contaminate the result.[1226]

For calibration work the smallest volts per division setting, typically 1 mV, is the one that matters: applying around 1 mV to 1.5 mV on that range reveals how much noise the instrument contributes, which directly limits low-level measurements.[422]

## Minimum range and the honesty of the smallest settings

The lowest attainable setting separates instruments sharply. The LeCroy WaveJet Touch 354 bottoms out at 2 mV per division and will not reach 1 mV, against modern instruments offering a 500 µV per division range.[792] The 12-bit Rigol HDO4000 continues down through 500, 200 and 100 µV per division, with the 20 MHz bandwidth limit already engaged at those settings; the full 12 bits are not available at 100 µV per division.[1501]

Nominal ranges below the true front-end sensitivity are common. The Rigol MSO5000 pixel-doubles its display at 1 mV and 2 mV per division, only reaching a genuine front-end signal level at 5 mV per division.[1146] The Rigol DHO800 permits selection all the way down to 500 µV per division, well past its calibrated range, which is not a true representation of the signal — the limit simply has not been implemented in firmware.[1566]

At the other extreme, a limited range makes an instrument unsuitable for small signals altogether: the Fnirsi tablet scope cannot usefully resolve better than a 1 V peak-to-peak input at its lowest setting.[1317] The Moku:Go dispenses with the concept entirely, offering no input amplifier, no low voltage ranges and no traditional volts per division control, only autoscaling.[1701]

## Front-end hardware behind the setting

The setting selects a tap on a resistive attenuator ladder in the input path, and this has consequences beyond amplitude. Pulse response can differ from one volts per division setting to another depending on where in the divider ladder the signal is taken: a tap at the top of the divider can give a better response than one further down, since each tap involves compensating its own resistive divider.[6XpyOGw6RFM] A scope showing excellent pulse response at one scale may behave quite differently at another — the Rohde & Schwarz RTB2000 was examined at both 20 mV and 10 mV per division on this basis.[6XpyOGw6RFM]

The dependency is visible in firmware as well. On the R&S HMO1202, the attenuation ladder field written to the front-end LMH chip changes when the channel's volts per division setting changes, which identifies that chip as the one performing the 20 MHz bandwidth limiting without any further inspection of the front-end circuitry.[879]

In older instruments the function was mechanical and shared: the Tektronix 213 uses one complex custom switch to handle volts per division together with ohms and range selection.[628] Ergonomics vary too — the LeCroy 9384C provides no separate vertical attenuation control per channel, requiring a channel to be selected before its volts per division and time per division can be set.[217]

## Probes, offset and annunciation

Probe attenuation folds into the displayed scale. With a ×10 probe the instrument must be told so, after which a 0.1 V per division indication corresponds to the attenuated input.[196] Auto-probe interfaces do this automatically, jumping a 2 mV per division range to 20 mV when a ×10 probe is attached.[792] Where no annunciator indicates the probe setting, a displayed 1 V per division leaves genuine ambiguity about what the channel is actually set to.[CK5nbC_dBWk]

Vertical offset range is not independent of the scale. On active probes used for power rail work, the available offset changes with the volts per division setting, a trap when trying to view small noise riding on a large DC level.[s6lVvIWWNBw] On instruments with generous offset, 100 mV per division can still be paired with offset up to 10 V.[1735]

## In practice on the bench

Typical working settings follow the signal under examination: 500 mV per division to see a roughly 3 V level across a boost converter's 10 µF output filter capacitor,[855] 2 V per division on both channels to compare skew between two 6.25 MHz clocks on a board,[1081] 50 V per division while chasing a supply fault in an arcade machine,[1301] and 0.5 V per division to capture the ringing impulse from a deliberately poor probe ground, which measures around 140 MHz.[21]

Sweeping the volts per division control is also a diagnostic in itself. Spot-checking one high and one low volts per division range, confirming that both channels trigger and that the displayed amplitude matches the signal generator, gives high confidence that a scope's core functionality is intact — a gain fault large enough to matter would not go unnoticed by such a check.[1492] Stepping through the ranges likewise confirms that the displayed data is genuinely tracking the input.[1228]

Unconventional implementations break the expected relationship. The Haasoscope Pro leaves its displayed voltage scale fixed while gain is changed, so the reading must be multiplied by a separate 10 mV per division factor to obtain the real amplitude.[1709] Software-driven instruments vary in how the control is reached at all, from keyboard and mouse-wheel bindings[1056] to menu buttons on handheld units[D2PANd9Hu3U][f_SdM6sXHD4] to panels where the vertical scale is not visible unless a particular pane is open.[876]
