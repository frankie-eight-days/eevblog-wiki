---
video_id: jUvSP3BQpvs
title: EEVblog #85 - High Voltage Oscilloscope Probe Design
url: https://www.youtube.com/watch?v=jUvSP3BQpvs
source: youtube-asr
timestamps: {"0": 0, "1": 26, "2": 46, "3": 74, "4": 88, "5": 104, "6": 116, "7": 137, "8": 161, "9": 180, "10": 200, "11": 215, "12": 231, "13": 251}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. All right, go for your life. Okay, um the probe I was after had to measure voltages up to about 5 kV and I didn't want to buy a Tektronix uh high voltage probe for half a quadrillion dollars, so I decided to roll my own.

**Dave Jones:** I wasn't too worried about ultra high input impedance because I'm measuring uh quite high uh energy sources with low source impedance. So, I figured I'd kick off with something with five high voltage 10 meg resistors in series.

**Dave Jones:** So, I've got five by 10 meg resistors. Each of those is rated at 3.5 kV handling. And over here, since we've got 50 meg uh total load impedance over here of 50k comprising 56k fixed resistor, 1 meg worth of uh uh oscilloscope input resistance, and another uh 1 meg resistor hung off it.

**Dave Jones:** We've got some capacitive loading over here on the the oscilloscope side of things. Yeah, it's going to be about 12 puff. Yeah, but uh what I need to do is put I'm shaking the uh camera there.

**Dave Jones:** That's all right. Put a whole stack of uh caps across these little babies here. Mhm. Strictly speaking, I didn't need particularly high capacitance, but the smallest high voltage caps I could get were 10 puff rated at 3 kV.

**Dave Jones:** That goes off the probe. Mhm. Okay, so our total capacitance from there to there is two puff. And it's table shaking again uh because I've we've a 1001 divide ratio there.

**Dave Jones:** I need across here around about 2 nF. Yep, which was duly assembled and when tested in free air indicated pretty good results. Mhm, but there's a problem. All of these points in here are relatively high impedance and become a beautiful point of noise pickup.

**Dave Jones:** It's very easy to capacitive couple any any stray fields into those areas, so you need to encase the whole thing in a copper tube. Which was duly done and it was all nicely potted up and looks a little bit like that.

**Dave Jones:** Yep. Now, having done all of that, I discovered that my actual frequency response looks like that. Relatively close to unity down at the bottom, drops to a scale factor of .4 up the top.

**Dave Jones:** Why? All of these little stray capacitances here, yep, which were not present when I measured it in free air, Yep. and which were well and truly exaggerated by the fact that having potted it, the resin has a dielectric dielectric effect.

**Dave Jones:** Yeah, around about 4, 4 and 1/2, 5. So I wound up with this huge high frequency capacitive ladder divider in there, which spoils the high frequency response. So, okay, back to the drawing board.

**Dave Jones:** Next time I make another one of these, I will not put that capacitor in. I'll fit it externally after I've done all of the potting and fiddle it to trim for good high frequency response.

**Dave Jones:** Yep. The good news is the particular construction technique that I used indicate that up here at least it's flat out to well beyond 3 MHz, which is about as high as my crappy little oscillator will go, and rise time indicates that it's probably got a bandwidth of about 30 MHz.

**Dave Jones:** So, na na na na na Tektronix. Awesome. Thanks, Don.
