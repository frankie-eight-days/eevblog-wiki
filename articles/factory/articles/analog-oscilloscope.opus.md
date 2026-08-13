# analog oscilloscope

An analog oscilloscope, or cathode ray oscilloscope, displays voltage against time by sweeping an electron beam across a phosphor-coated CRT in real time, with no digitisation and no memory anywhere in the signal path.[UJjMt2-k99c][159][86] It remains a genuinely useful bench instrument decades after digital storage scopes displaced it, both because a second-hand one costs almost nothing and because the way it works is the way every oscilloscope works underneath.[86][168] Its one structural limitation is that it cannot store a waveform, which is precisely the capability a digital storage oscilloscope adds.[1022][926]

## How the display works

The instrument measures voltage with respect to time: voltage on the vertical axis, time on the horizontal, with the vertical scale set by a volts-per-division control and a division being one square of the graticule.[UJjMt2-k99c] The sweep always begins at the left-hand edge of the screen, travels to the right, and then retraces back to the start; the image exists only because that sweep is repeated continuously.[UJjMt2-k99c][153]

Brightness is not a display setting so much as a physical consequence: the intensity of any point on the screen is determined by how long the beam spends in that position.[601] A waveform that repeats identically every sweep is written over the same path each time and appears bright and fine; a runt pulse that occurs one sweep in a million is written once and is effectively invisible.[601] The phosphor supplies a natural persistence, holding the illuminated point for a period before it decays, which is what gives the analog display its intensity-graded appearance.[3jDRH-6IvZc][601] Turning the intensity up increases the effective persistence and thickens the trace, but there is a hard limit to how far that can be pushed.[3jDRH-6IvZc][601]

Traditional analog front ends have a Gaussian frequency response, for which the classic relationship holds: rise time equals 0.35 divided by the bandwidth of the scope.[306] Modern digital scopes do not necessarily follow it, since their analog input channels often use a maximally flat response instead.[306]

The CRT itself is an electromagnetic device with large deflection coils that radiate a substantial magnetic field, commonly at a switching frequency around 25 kHz.[1329]

## Triggering

Because the concept originates with the sweep of a CRT beam, analog scopes are the natural place to understand triggering, and the behaviour carries directly over to digital scopes, which work the same way.[159] Trigger holdoff is a dedicated knob on most higher-end older analog instruments.[159] Adding holdoff has a visible side effect unique to the analog display: the screen is no longer re-traced as often, so the trace dims noticeably.[159]

AC trigger coupling sits at the top of the trigger coupling selector on essentially all analog scopes, positioned as the de facto default, because it makes probing an unknown circuit easier by removing the DC content and giving an easier trigger point to work from.[685] Trigger coupling is independent of input channel coupling; the input coupling setting makes no difference to triggering.[685] A digital scope offering AC and DC trigger coupling should behave identically to an old-school analog scope regardless of whether the selection is implemented with a real capacitor and relay or entirely in the digital domain.[685]

Alternate trigger, which jumps between two channels fast enough that both appear on screen simultaneously, was an analog feature that modern digital scopes have largely dropped, replaced by pattern or OR triggering.[1235] Some analog scopes also offered trigger view, which displayed the trigger signal itself as an extra trace; a four-channel Kikusui COS 6200 could be made to show twelve or fourteen waveforms this way, counting trigger views and displayed sweep waveforms.[1418]

## The noise myth

A persistent claim holds that analog oscilloscopes are lower noise than digital ones. This is not true.[601][878][442] Digital scopes are not noisier; their sampling behaviour and update rate simply make them capable of displaying more of the noise that is genuinely present.[442][610] An analog scope averages the signal out across its screen, so uncorrelated high-frequency content is written too dimly and too infrequently to be seen.[601][610]

This can be demonstrated directly. A 30% noise component added to a sine wave is barely visible on an analog scope because the noise is uncorrelated to the sweep and each excursion is written only briefly.[601] Photographing the screen with a long exposure reveals the dim phosphor the eye cannot resolve, and the noise appears superimposed on the waveform exactly as the digital scope showed it.[601] The ridges around the bezel of analog scopes exist for this purpose: they accepted a hood so a film camera could be mounted for long exposures.[601] A direct amplitude comparison at 5 mV per division shows common-mode switching noise of exactly the same amplitude on analog and digital.[442] Turning the analog intensity all the way down produces an apparently clean flat line while that common-mode noise is still present on the signal.[442]

There are at least six mechanisms besides the noise floor of the ADC that affect how noisy a digital scope appears: memory depth, analog bandwidth, boxcar averaging, the intensity-graded display, the update rate, and the sample rate.[610] Boxcar averaging in high-resolution mode thins the trace in almost exactly the way an analog scope's phosphor persistence does.[601][610]

Two genuine advantages do remain on the analog side. A digital scope can radiate its own switching noise into a low-level measurement, which an analog scope does not do.[441] And at high dynamic range with small vertical settings, a digital scope is limited by its 8-bit converter — at 500 µV per division the individual quantisation steps become visible in the trace, where the analog display stays continuous.[594][1716]

## What an analog scope is still good for

The absence of storage is the whole of the deficit; apart from that the instrument is highly useful.[1022] A good lab is still worth equipping with one for its higher update rate, its lower apparent noise, and its ability to show signals a low-end digital scope cannot capture.[51][200][196] It is a strong choice for measuring power supply ripple and noise, where high-frequency detail matters and the vertical range is small.[594] Analog subtraction for differential measurements is immediate, where a digital scope's math function may be sluggish because the processing is done in software.[565]

It is also good at slow signals: wound out to seconds per division, the beam crawls visibly across the screen.[UJjMt2-k99c] Bode plotting works on an analog scope with nothing more than a sweep generator.[396] Oscillator calibration by watching a waveform drift against a reference trigger is fundamentally an analog technique that works identically on either instrument.[457] Entry-level 20 MHz analog scopes frequently included a built-in curve tracer, which measured component parameters using the XY mode.[1137] A few analog scopes offered measurement functions, but these were cursor-based rather than the automatic parametric measurements a digital scope provides.[1226]

The intensity-graded displays on modern digital scopes exist specifically to replicate the analog look.[601][143] The value of that emulation is judged against a real CRT: 64 shading levels with fast update is close, 256 levels closer still, and colour grading of the waveform is a separate matter.[703][704][1146][591] A display advertised as fast but showing hard vertical lines and no true persistence does not achieve it.[474]

## Where an analog scope loses

Single-shot capture is impossible.[926][13] An event that happens once cannot be held on a phosphor screen, and a rare glitch that appears one sweep in a thousand and lasts a millisecond will not build enough brightness to be seen.[3jDRH-6IvZc][601] A digital scope can be stopped and the captured waveform then zoomed, measured, and analysed at leisure with the probe disconnected, which is the single most valuable thing it does.[926] Faster waveform update rates improve the statistical probability of catching an infrequent event — 100,000 waveforms per second gives far better odds than 100.[3jDRH-6IvZc][143]

The engineering judgment that follows is unambiguous: a low-end digital scope capable of single-shot capture is more useful than a top-of-the-line analog one with dual time bases and high bandwidth.[1536][3jDRH-6IvZc][400] Someone with a limited budget and no scope at all should buy a cheap DSO first.[722][400]

The complaint that analog scopes are harder to use does not hold up. A digital scope does the same things and differs only in storing the waveform rather than tracing it continuously on a CRT; used manually, there is no difference at all, and a well-laid-out analog front panel can be easier than a menu-driven digital one.[86] The counterargument is that a beginner who learns only to press the auto-set button has learned nothing about operating an oscilloscope, which is the basis for recommending an analog scope as a learning instrument.[86][722]

## Buying second-hand

A working dual-channel 20 MHz analog scope can reliably be found for $50 or less, and they are given away free by universities, labs, and individuals on forums.[498][1022][168][86] Twenty megahertz dual channel is the baseline; 50 MHz is nicer and 100 MHz better still.[86][168] Paying more than about $50 is poor value — the money is better saved toward a $300 to $400 modern digital storage scope.[1022]

Practical search tactics matter more than the money. Many sellers do not put the word analog in the title or listing category, so filtering on it is a good first pass but misses bargains, and browsing categories catches items listed by people who do not know what they have.[498][1022] Watch lists across several brands, familiarity with completed listings, and patience are what actually produce the result.[498][1022] Surplus auction houses carry high-end analog scopes including 2465Bs, though often only in pallet lots rather than singles.[1184][1536]

When assessing a listing, prefer one whose photographs show waveforms on both channels — a trace on screen means the EHT section works, and roughly 95% of the time a scope showing a trace will be functional.[196][1536] A tilted trace in a photograph is only trace rotation and is trivially adjusted.[1022] Very old instruments are best avoided; 1980s models are preferable to 1970s ones for general use.[1022][1536] Almost any analog oscilloscope will do the job, and there are essentially no bad ones.[1022]

Cheap pocket DSOs, FPGA scope kits, and AVR-based oscilloscope kits are not a substitute at the same price, lacking proper high-bandwidth vertical attenuators and proper triggering.[86][359]

## Notable instruments

The Tektronix 2465 and 2465B, 400 MHz, are regarded as about the best analog scopes Tektronix produced, excepting the micro-channel-plate CRT models with their storage capability.[695][1203] They are long in the tooth, last manufactured around the mid-1990s, and the 2465 and 300 series both have known long-term failure modes with active repair communities around them — a 2465B restored to specification after thirty years may need nothing more than a full recap.[695][1536][1203]

The Tektronix 2225 is a 50 MHz dual-channel scope of late-1980s vintage, notable for a 500 µV per division vertical range, one of only about three oscilloscopes offering it.[196][1000][1022] The Tektronix 475 is a 200 MHz instrument dating from 1972 and sold into the early 1980s.[jmb9ICnI8xI] The HP 1740A is a 100 MHz dual-channel scope with delayed time base, auto and sweep and intensified modes — about as advanced as an analog scope became in its day — and its vertical section includes a custom differential-output driver chip rather than being entirely discrete.[803] The HP 1700 series was available with a multimeter attachment on top.[756]

Hitachi and Goldstar, the latter being the original name of LG, both made good analog scopes.[416] Hameg produced high-quality German-made instruments, including combiscopes, at the cost of a confusing user interface.[104][502][153] Hung Cheng 20 MHz dual-channel units turn up cheaply and are serviceable.[1022] Prices in period were substantial: a Hitachi V5500 50 MHz was $1795 in 1980 and even a 15 MHz unit was $595, while a Goldstar 20 MHz with 1 mV per division sensitivity was around $650.[416] Dave Jones's first oscilloscope was a Kikusui COS5020, a 20 MHz dual-channel single-time-base unit bought new for about $800.[54][ln_XJDPKJlc]

## Combiscopes

A number of instruments are true analog scopes with a digital storage board added, rather than digital scopes emulating analog. Switching storage mode off returns them to normal analog operation.[502] Their digital performance is usually poor by modern standards — a Hameg 20 MHz example sampled at 20 MS/s with 2K per channel and had no sin(x)/x interpolation, so no meaningful storage bandwidth should be expected from it.[502] A 40 MHz Kikusui with a digital add-on managed 25 MS/s into 1,024 points of sample memory, enough for the display; switching from analog to storage mode makes the 8-bit ADC resolution steps visible in the waveform.[1716] On such a machine the storage board can be removed entirely and the instrument still works as a dual-channel analog scope.[502]

The Philips PM 3370B, later badged Fluke, is an analog scope with digitally controlled focus, intensity, and trace settings held in battery-backed memory; with the battery dead the settings must be reset at every power-up, so it is not purely analog in that respect even though it works as an analog scope.[1450] The Tektronix 213 is a 1 MHz portable combining a classic analog scope architecture — a matched JFET input pair on the front end — with switching that routes the probe through to multimeter circuitry.[628]

Some late analog scopes added digital readout and cursors without becoming digital scopes, which can make a listing photograph look misleadingly like a DSO.[1536]

## Supply

The population of surviving instruments was reduced deliberately. At least one major test equipment manufacturer ran a trade-in programme that accepted any scope, including old analog CROs and other brands, against a discount on a new instrument, and required its dealers to destroy the traded units and provide evidence they had done so — including perfectly functional and relatively high-end scopes.[a4Xpsenpd6E] Working instruments also continue to be dumped by shops and universities when they fail or when premises change hands.[803][jmb9ICnI8xI][1716]
