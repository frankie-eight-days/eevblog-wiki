---
video_id: jUvSP3BQpvs
title: EEVblog #85 - High Voltage Oscilloscope Probe Design
url: https://www.youtube.com/watch?v=jUvSP3BQpvs
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 35, "3": 57, "4": 78, "5": 92, "6": 111, "7": 132, "8": 152, "9": 174, "10": 191, "11": 211, "12": 230, "13": 247}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. All right, go for your life. Okay, um the probe I was after had to measure voltages up to about 5 kV and I didn't

**Dave Jones:** want to buy a Tektronix uh high voltage probe for half a quadrillion dollars, so I decided to roll my own. I wasn't too worried about ultra high input impedance because I'm measuring uh quite high uh energy sources with low

**Dave Jones:** source impedance. So, I figured I'd kick off with something with five high voltage 10 meg resistors in series. So, I've got five by 10 meg resistors. Each of those is rated at 3.5 kV handling. And over here, since we've got 50 meg uh

**Dave Jones:** total load impedance over here of 50k comprising 56k fixed resistor, 1 meg worth of uh uh oscilloscope input resistance, and another uh 1 meg resistor hung off it. We've got some capacitive loading over here on the the oscilloscope side of

**Dave Jones:** things. Yeah, it's going to be about 12 puff. Yeah, but uh what I need to do is put I'm shaking the uh camera there. That's all right. Put a whole stack of uh caps across these little babies here.

**Dave Jones:** Mhm. Strictly speaking, I didn't need particularly high capacitance, but the smallest high voltage caps I could get were 10 puff rated at 3 kV. That goes off the probe. Mhm. Okay, so our total capacitance from there to there is two puff.

**Dave Jones:** And it's table shaking again uh because I've we've a 1001 divide ratio there. I need across here around about 2 nF. Yep, which was duly assembled and when tested in free air indicated pretty good results. Mhm, but there's a problem.

**Dave Jones:** All of these points in here are relatively high impedance and become a beautiful point of noise pickup. It's very easy to capacitive couple any any stray fields into those areas, so you need to encase the whole thing in a

**Dave Jones:** copper tube. Which was duly done and it was all nicely potted up and looks a little bit like that. Yep. Now, having done all of that, I discovered that my actual frequency response looks like that.

**Dave Jones:** Relatively close to unity down at the bottom, drops to a scale factor of .4 up the top. Why? All of these little stray capacitances here, yep, which were not present when I measured it in free air, Yep. and which were well and truly

**Dave Jones:** exaggerated by the fact that having potted it, the resin has a dielectric dielectric effect. Yeah, around about 4, 4 and 1/2, 5. So I wound up with this huge high frequency capacitive ladder divider in there, which spoils the high frequency

**Dave Jones:** response. So, okay, back to the drawing board. Next time I make another one of these, I will not put that capacitor in. I'll fit it externally after I've done all of the potting and fiddle it to trim for good high

**Dave Jones:** frequency response. Yep. The good news is the particular construction technique that I used indicate that up here at least it's flat out to well beyond 3 MHz, which is about as high as my crappy little oscillator will go, and

**Dave Jones:** rise time indicates that it's probably got a bandwidth of about 30 MHz. So, na na na na na Tektronix. Awesome. Thanks, Don.
