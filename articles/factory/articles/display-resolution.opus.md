# display resolution

Display resolution is the pixel count of a screen, and on test equipment it sets a hard ceiling on how much waveform detail, annotation, and menu structure an instrument can present at once. Because an oscilloscope's screen is the only place its acquisition data becomes visible, screen resolution is treated as a first-order specification alongside bandwidth and sample memory.[1218][1032] It is also, in most instruments, not a display choice at all but a consequence of the acquisition ASIC that writes to the screen, which is why resolution tends to be frozen for the life of a product family.[383][1638]

## Resolution tiers in oscilloscopes

A rough hierarchy has emerged across instrument generations. Full HD at 1920 by 1080 sits at the top, reached by the Tektronix 3 and 4 series scopes.[1218] Below that is 1280 by 800, used by Rohde & Schwarz in the same class and by the Keysight HD3 with its Megazoom V ASIC.[1218][1638] A 1024 by 600 panel is common across several mid-range instruments,[1218][1501] and 800 by 480 widescreen is typical of budget models such as the Rigol DS1054Z, the Rigol DS1000Z series, and the Siglent SDS1000X.[703][522][797] The Agilent 2000 X series used 800 by 480, a resolution high enough that no pixel compression occurs in the waveform at all.[143]

At 800 by 600 the display is squarely at the bottom of the modern range: this was the Keysight limit across the 1 GHz class, including the 4000 series, which despite being the physically largest screen in its comparison group carried the lowest pixel count.[1218][1032] The OWON XDS3202A and the 300 MHz OWON SDS both use 800 by 600 panels, the latter with no apparent pixel doubling.[ByUiOk00K0U][480] Lower still, the LeCroy WaveJet Touch 354 shipped a 7.5 inch touchscreen at only 640 by 480, which limits how much vertical resolution can be given to more than one waveform.[792]

Higher vertical resolution buys more than waveform area. On the Agilent 4000X, the additional vertical pixels allowed a larger information strip along the top of the screen carrying extra readouts.[383]

## The ASIC as the limiting factor

Screen resolution on these instruments is bounded by the acquisition ASIC rather than by panel availability. The Agilent 7000 series ran an XGA display at 1024 by 768; the 4000 series dropped to 800 by 600 and lost visible waveform area as a direct result of the Megazoom 4 ASIC.[383] The same ASIC prevents the menu from being collapsed to enlarge the usable window, an inherent disadvantage and the price paid for one million waveform updates per second, because the ASIC must write to a designated area of the screen.[383] Keysight's own position acknowledged the constraint: the platform lagged on sample memory and on screen size, capped at 800 by 600, with no route to going bigger without new silicon.[1032]

The constraint persisted into the Megazoom V generation. That scope exposes a GUI scale factor, but scaling only changes font sizes; there is no increase in resolution, which remains a limitation of the ASIC.[1638] A 10.1 inch touchscreen paired with a 14-bit converter would reasonably have carried a full HD panel, and 1280 by 800 falls short of what the acquisition hardware could justify.[1638] Conversely, when Siglent moved the SDS2000X Plus to a 10.1 inch higher-resolution display with more mapping, the FPGA behind it was almost certainly enhanced to match.[1309]

Resolution also functions as a price-per-pixel comparison between competitors: the Siglent's 1024 by 600 screen against the Rigol HDO4000's 800-pixel-wide panel means better vertical resolution for less money.[1501]

## External display output

Instruments generally do not raise their internal rendering resolution when an external monitor is attached. Across an entire 1 GHz shootout, none of the scopes increased screen resolution on an external display, so hooking a monitor to a Rigol, Siglent, or Keysight yields the native panel resolution enlarged rather than full HD detail.[1218] Where a host program stretches the output to full screen, that is the program auto-scaling and not the scope, so no additional waveform detail or 14-bit data becomes visible.[1638] The Rigol DHO800 is an exception: its HDMI output scales to the screen resolution, driving a 4K display and genuinely rendering the output at higher resolution, with touch control also working over the link.[r_BYYgCqScE]

For bench viewing generally, a monitor need not be full HD to be useful; a 1440 by 900 19 inch panel is adequate as a microscope viewing display.[585]

## Software and usable screen area

Minimum resolution is a practical constraint on EDA software. KiCad's schematic editor requires more than 1024 by 768 to be used reliably, since some tools along the bottom fall off the screen at that size, which is a real limitation on a netbook-class machine.[253] The PCB editor is worse: a screen larger than 1280 by 720 is needed to see all the icons and toolbars.[254]

High resolution can also be misused. On a high-resolution e-reader panel, the page-number indicator was rendered as small as the pixel pitch allowed, to the point of being unreadable with good eyesight and invisible to anyone visually impaired; the temptation for a designer to spend the available resolution on shrinking elements is a genuine disadvantage of a denser display.[188]

Windows font scaling on a 3840 by 2160 monitor is a related problem. Windows recommends 150 percent scaling for such a panel, which conflicts with running every other monitor at 100 percent.[qjLXJl0kDjg]

## Pixel density and perceived quality

Pixel density, not pixel count alone, determines how a display reads. The Nexus 7 combined a 7 inch IPS panel with 1280 by 800 pixels for 216 pixels per inch, sitting between the contemporary iPad and the Kindle Fire, and that resolution allowed basic 1280 by 720 HD playback.[322] E-ink at 800 by 600 across a 6 inch panel works out to roughly 150 to 160 pixels per inch and reads convincingly like paper.[200][108] The Kindle 4 kept exactly the same 800 by 600 screen as its predecessor despite claims of improvement.[205]

Physical size is an independent axis. The Rigol DS1000Z uses the same 800 by 480 resolution as the 2000 series in a panel roughly an inch to an inch and a half smaller.[522] Two camcorder screens of identical physical size differed only in resolution, 1.2 megapixels against 920k, and the denser one was noticeably sharper.[650] Even a good camcorder screen at 1440 by 1080 is too small at 3.5 inches to resolve fine detail during a teardown, which is one argument for shooting in 4K and zooming in during editing instead.[1096]

## Historical and embedded displays

Low-resolution panels dominate older and embedded hardware. The original Apple Newton MessagePad of 1993 used a 336 by 240 screen, physically large but very low in resolution, driven by an ARM 610 at about 20 MHz.[418] The Amstrad NC100 notepad carried a 480 by 32 pixel display, presenting 8 lines by 80 characters.[385] The Cambridge Z88 appears to run roughly 80 characters by eight lines.[382] An industrial Norand handheld running Windows 3.1 had only a 320 by 240 screen.[686] Amiga-era game graphics ran at 320 by 200.[438] A 1985 trade magazine advertised Sharp LCDs at 640 by 200 as a notable capability.[1194]

Embedded projects face the same tradeoffs at smaller scale. The Gigatron TTL computer renders 160 by 120 with a 64-colour palette produced by two resistor-ladder bits each for red, green, and blue, giving four levels per channel and 4x4x4 combinations.[1080] Upgrading a project display from 192 by 64 to roughly 300 by 160 is a large resolution jump that also came in cheaper.[1703]

## Resolution of a measurement

The word carries a second, unrelated meaning in instrumentation: the smallest increment a reading can express. The Rigol DP832 power supply displays 10 mV and 10 mA increments in its base configuration, and a paid software option adds an extra digit to both.[509] On an HP 53131A counter set to 15 digit resolution rather than a fixed gate time, the instrument computes three digits beyond what its front panel can show; recovering them requires tapping the last physical digit, and rounding complicates any scheme to blank and shift the display, since a rounded-up reading yields fewer usable extra digits than an unrounded one.[6M-xXEn1_iI]
