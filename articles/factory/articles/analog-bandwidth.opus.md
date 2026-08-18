# analog bandwidth

Analog bandwidth is the frequency at which an instrument's front end falls 3 dB down in its frequency response, and it is the single most important headline specification of an oscilloscope.[13] It describes what the analog signal path — connector, attenuator, amplifier — can pass before the ADC ever sees the waveform, which is why it is quoted separately from sample rate and memory depth.[13][610] It is not, however, a specification that can be read on its own: a scope's usable performance depends on how bandwidth, sample rate, memory depth, update rate and display processing interact.[149][610]

## Definition and the 3 dB point

The number quoted on the front panel is the −3 dB corner of the front-end response, equivalent to the amplitude falling to 0.707 of its low-frequency value.[13][797] The corner is not a brick wall. A 200 MHz front end does not stop passing signal at 200 MHz; it begins rolling off there, and content beyond the corner is attenuated rather than removed.[1213] The practical consequence is that a 200 MHz square wave applied to a 200 MHz input does not reach the ADC as a square wave — the sharp rise and fall times depend on harmonics well above the corner, and those are filtered out by the front end before digitisation.[1213]

The shape of the roll-off matters as much as its corner frequency. Traditional analog CRT scopes have a Gaussian response, for which rise time relates to bandwidth by the classic rise time equals 0.35 divided by bandwidth.[306] Because the relationship between displayed rise time and true bandwidth is direct, a fast-edge pulse generator can be used to derive a scope's real bandwidth from the rise time it displays, assuming the input pulse is effectively perfect.[306] Front ends with a different response shape produce a different resultant waveform for the same input, and the response type also changes how reconstruction filters such as sin(x)/x interpolation behave.[1213]

## Measuring it

The direct method is to sweep the analog input with an RF signal generator at a fixed input amplitude and find the frequency at which the displayed amplitude drops to 0.707, rather than inferring it from a pulse and the 0.35 formula.[797] Measured results can exceed the datasheet: a Siglent SDS1000X specified at 200 MHz was found to be 3 dB down at 300 MHz.[797] Bandwidth that is honest in the analog domain can still be undermined by an inadequate sample rate, and by sample rate that halves when a second channel is turned on.[797]

Claimed figures at the low end of the market are often unsupported. A pocket instrument advertising 40 MHz analog bandwidth showed jitter severe enough to be unusable at 20 MHz and could not reproduce a 1 MHz square wave with any high-frequency detail.[359]

## Relationship to sample rate

Nyquist sets the floor: sample rate must be at least twice the analog bandwidth for interpolation to be mathematically valid.[1213] The working rule of thumb is ten times, not two.[13][107] A scope that does not carry ten times its bandwidth in sample rate is limited in single-shot use, and dividing the sample rate by ten gives the usable single-shot bandwidth — a 500 MS/s instrument nominally rated at 300 MHz delivers roughly 50 MHz for single-shot work.[107] Genuine ten-times ratios have been available since the Tektronix TDS 200 series, which paired 1 GS/s with 100 MHz of analog bandwidth.[1317][747] Modern bench instruments meet or exceed the ratio; a Rigol with 1 GS/s and 50 MHz analog bandwidth yields about twenty points per cycle of a waveform at the corner frequency, in real time.[13]

The ratio breaks down at the top of the range, where sample rates cannot keep pace. A probe and front end offering 2 GHz of analog bandwidth backed by 3.2 GS/s cannot deliver that bandwidth in real time; two units can be synchronised to raise the effective sample rate.[1709] Equivalent-time sampling is sometimes presented as a substitute for real-time sample rate, but an instrument relying on it is not a real-time scope and is of little use above roughly 20 to 30 MHz.[1317]

Sample rate and analog bandwidth serve different purposes, and both are needed. High analog bandwidth is what makes measurements such as eye diagrams possible, while sample rate governs single-shot capture.[107]

## Typical values

Two or three decades ago a good entry-level scope offered 20 MHz of analog bandwidth; the figure for a general-purpose instrument has since risen to a recommended minimum of about 50 MHz, driven by high-speed digital and microcontroller work.[13] Bench instruments now span a wide range: 300 MHz at 2 GS/s in a four-channel Siglent SDS2000X,[864] 350 MHz at 4 GS/s with 12-bit resolution in a Rigol positioned under $1000,[1717] 500 MHz and 1 GHz options in the Tektronix MDO4000 at 5 GS/s,[199] 1 GHz at 5 GS/s in the Rigol DS6104,[114] and 1 GHz at up to 4 GS/s in the older LeCroy 9384C.[217] Platforms have been announced with up to 16 GHz of analog bandwidth at 40 GS/s with channel interleaving.[5YjS4DHKlQU]

LeCroy historically led on large sample memories, fast acquisition rates and high analog bandwidths, and its instruments remain less sought-after second-hand than comparable Agilent and Tektronix models.[217]

Portable and PC-connected instruments sit lower. A ruggedised IP54 handheld with isolated BNCs offers a full 200 MHz;[358] a Fluke 91 Scopemeter, 50 MHz;[430] a Moku:Go, dual 30 MHz inputs at 125 MS/s alongside dual 20 MHz analog outputs;[1701] an Analog Discovery 3, around 9 MHz with no real front end at all;[1552] and a handheld Zotek instrument, 5 MHz at 48 MS/s with no equivalent-time sampling.[D2PANd9Hu3U] An OWON XDS3202A pairs 200 MHz with a 14-bit converter, at the cost of only 1 GS/s.[ByUiOk00K0U]

Analog bandwidth is not exclusive to oscilloscopes. A Sony data recorder scaled its analog bandwidth with channel count, giving 20 kHz in two-channel mode and only 5 kHz with all sixteen channels sampling at once.[1090] Catalogue ICs exist at 25 GHz analog bandwidth for a broadband AND/OR logic gate, and a spectrometer ASIC processing at 5.5 GHz bandwidth.[1435] A Red Pitaya-class instrument with roughly 50 to 60 MHz of analog bandwidth is sufficient to plot capacitor impedance against frequency into the tens of MHz.[859]

## Bandwidth as a purchasing and licensing variable

Within a model family the analog bandwidth is frequently the same hardware at every price point, with the difference sold as a software option — a 70 MHz Siglent SDS2000X and its 300 MHz sibling ran from $1285 to $2800 on hardware believed to be identical.[864] The same pattern holds in the entry-level Rigol DS2000 class, where the purchase is essentially software options rather than analog performance.[360] Where a lower-bandwidth model has been unlocked, the analog front end is generally judged capable of the higher figure, since the bandwidth is present in the hardware for a reason.[978]

Bandwidth is not the only axis worth paying for. Sustained waveform update rate that does not collapse when serial decode and mask testing are enabled can be worth more, for some requirements, than additional analog bandwidth or sample memory.[149] Comparisons between scopes must be made on matched terms; a noise-floor comparison is only meaningful if memory depth, analog bandwidth, intensity-graded display setting, update rate and sample rate are all equal.[610]

On analog scopes, a third channel is often the external trigger input pressed into service as a trace, typically with reduced analog bandwidth compared with the main channels.[1022]

## Probes and the delivered bandwidth

The specification at the BNC is only achievable if the probe and its connection can reach it. Among passive probes, 700 MHz represents about the practical ceiling, with 1 GHz passive probes existing at the extreme.[1715] Mechanical design can defeat the specification entirely: an instrument with a nominally good 60 MHz analog bandwidth was rendered unusable with any ×10 probe because the BNC spacing prevented the probe bodies from seating, leaving it serviceable only with plain BNC cables.[1127]
