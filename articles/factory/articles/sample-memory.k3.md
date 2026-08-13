# sample memory

Sample memory (also called acquisition memory or record length) is the high-speed buffer in a digital oscilloscope or logic analyzer that stores the digitized samples of each acquisition. Its depth, specified in samples or points per channel, is a defining specification alongside bandwidth and sample rate, because it determines how long an instrument can record at full sample rate and how far a captured waveform can be zoomed before the underlying data runs out.[44][149][1311][1260]

## Depth, time base, and sample rate

Capture duration is the product of memory depth and sample interval, so once memory is exhausted the instrument must drop its sample rate as the time base is slowed. A 4 meg point scope sampling at 5 GS/s falls to 2.5 GS/s and then 1.25 GS/s as the time base is wound out past 50 µs/div, because the memory cannot sustain 5 GS/s at 1 ms/div.[1311] Conversely, deep memory lets a user zoom from a wide capture down to fine detail such as individual SPI data bytes, with the zoom range limited by the chosen memory depth.[199] A scope that advertises 128k of storage depth but cannot zoom into a stopped waveform effectively wastes that memory.[1260]

Memory may be dedicated per channel or shared. The GW Instek GDS-1000B provides 10M per channel that is not shared[824], while the Siglent SDS1104X-U has 14M points total that effectively shrink as channels are enabled[1355]; the Rigol DS2000 captures 700 points across two channels at a fast time base and doubles to 1.4K when the second channel is turned off.[369] On the Tektronix MDO3000 one memory device serves two channels, so the sample rate halves when both are active.[587]

Instruments offer different memory management policies: automatic modes that maximize memory use for the current settings, fixed memory depth, or fixed sample rate; the Siglent SDS1000X HD drops the fixed-memory option entirely in favor of automatic management.[1311][1612] Acquisition modes can also trade memory for speed — selecting maximum waveform rate on the Rohde & Schwarz HMO1202 drops the depth to 480k points.[842]

## Waveform update rate

Deeper memory slows acquisition because more data must be processed and rendered per trigger. On the Tektronix MDO4000, measured update rate at one time base was roughly 3,000–4,000 waveforms per second at 1K through 100K points, fell to about 1,000 at 1M points, about 200 at 10M, and about 20 at 20M points; capturing a single event at 1M depth took on the order of 18 seconds.[199] High advertised update rates can likewise depend on sacrificing memory: the Tektronix 4-series' 500,000 waveforms per second figure applies only in a special fast acquisition mode with drastically reduced sample memory, versus roughly 100 per second in normal mode.[1218]

## Displayed noise and aliasing

At a given time base, deeper memory preserves more high-frequency content, so a scope with more memory can display more apparent noise on an open input: the 1M point Rigol DS1052E shows more noise than an equivalent Tektronix purely because it captures more of it, and increasing memory depth on a scope visibly increases apparent noise.[601][797] Too little memory at slow time bases also produces aliasing; a 20 MHz sine that aliases at a short depth displays correctly at 1M or 10M points.[199]

## FFT analysis

Oscilloscope FFT performance depends jointly on memory depth, sample rate, time base, and the number of FFT points; deep memory is of no use if the FFT engine cannot process that many points.[845] Memory depth and FFT point count are distinct settings — a scope can capture at 1M points while the FFT uses far fewer.[1188] For fair cross-instrument FFT comparisons, both memory depth and sample rate should be matched, for example 1M points at 50 MS/s.[845]

## Segmented and compression approaches

Segmented memory conserves depth by capturing only bursts of interest and skipping dead time, avoiding the need for hundreds of megabytes or gigabytes of continuous high-speed memory — a capability that otherwise commands $50,000–$100,000 instruments.[143]

In logic analyzers, two memory systems exist: traditional sequential sampling, which stores a sample on every clock, and compression (transitional) sampling, which stores a word only when an input channel changes, time-stamping each transition — the same waveform may take four words instead of a thousand or a million.[44] Compression maximizes memory use for widely spaced packets, but it is not magic: any single fast-toggling channel forces a sample across all channels and can consume the whole buffer before a slow packet arrives, and compression analyzers with only a few kilobytes of memory lose packets once their transition budget is spent.[44][876] The NI VirtualBench exposes this directly, letting the user specify a capture as 10,000 or one million transitions rather than a memory depth.[876]

Streaming USB analyzers take the opposite approach: with no on-board buffer, they sample in real time to the PC, giving effectively infinite memory limited only by disk, but sample rates capped around 10–24 MS/s by USB bandwidth.[44][436][1018] Analyzers with genuine on-board memory, such as the ZeroPlus range at 32K to 2M per channel with up to 8× sample compression, are not streamers.[1018] Low-cost hybrid devices can be very shallow — the Digilent Analog Discovery logic analyzer uses only 2,048 samples with no compression.[692]

## Hardware implementation

Sample memory is implemented as dedicated devices adjacent to the acquisition FPGA or ASIC, identifiable by matched-length traces.[1038][587] Fast synchronous SRAM is common in mid-range scopes — ISSI 9Mbit parts in the HMO1202 and GDS-2000A, where two devices provide the 2M sample memory and a third supports the variable-intensity display and segmented memory[842][475]; SRAM is preferred over DRAM for speed and ease of FPGA interfacing.[810][1018] Higher-end designs use DRAM: the Rigol DS2000 pairs two 512Mbit parts for 64M per channel[360], the Uni-T UPO2104CS uses a single MT41K64 for its 32M per channel[1038], and the Keysight HD3 uses a 512MB Micron device per channel to deliver 100M points.[1639] Agilent/Keysight MegaZoom ASICs integrate the sample memory on-die, leaving no external memory around the acquisition chips.[144][976]

Sample width matters: 8-bit scopes store one byte per sample[842][1038][1477], while a 12-bit converter such as the R&S MXO4's requires at least two bytes per sample from its 8Gbit memory devices.[1545] Installed memory can exceed the marketed depth — the Tektronix 2 Series carries four 512MB devices (two gigasamples of hardware) for a specified 10M point depth.[1477]

## Capacity in context

Expectations have shifted by orders of magnitude. Early digital scopes ran on kilobyte-scale buffers — 1K points on a 25 MS/s Kikusui[1716], 2K SRAMs in the Fluke Combiscope[1450], 2K per channel in the Hameg hybrid[502] — and the Tektronix TDS2024C shipped with the same 2.5K depth as its 1997 ancestor, barely a couple of screens' worth.[187] Eight megabytes was massive for a 1999 Tektronix TDS540D[1185], LeCroy built its reputation on huge memories with fast acquisition[217], and the Agilent 90000 series reached one gigabyte of high-speed sample memory.[342] Modern mid-range instruments run from 14M[1042] and 32M[1038] to 200M points[1309], with the Rigol 7000 expandable to 500M[CMoBGGqojqs]. Memory is also divided between pre- and post-trigger data, with the trigger point determining the split.[290][1716]

## Multimeter data logging

Handheld and bench multimeters use sample memory for data logging. The Agilent U1272A stores 10,000 points with auto and trigger-hold modes that append each probed reading, though its manual hand-logging mode is inexplicably limited to 100 samples.[216][249] The Keysight U1282A's trig hold similarly appends readings to sample memory on probe contact.[832]