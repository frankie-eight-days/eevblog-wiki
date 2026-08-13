---
video_id: EWR4RQPzB6U
title: x1 Oscilloscope Probe SHOOTOUT - Rigol vs Siglent
url: https://www.youtube.com/watch?v=EWR4RQPzB6U
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 25, "2": 43, "3": 63, "4": 79, "5": 96, "6": 120, "7": 139, "8": 151, "9": 167}
---

**Dave Jones:** Now, I almost missed this. The x1, x10 switchable passive probes. You usually don't think anything of them. Well, these ones are actually rather special, I think. It's the PVP 3150. And, you know, it's a nice, decent, you know, x1, x10 switchable probe. But the thing with x1 probes, and I've done a video on this, I'll link it in up here and down below

**Dave Jones:** if you haven't seen it, are the secrets of x1 oscilloscope probes. They usually have a really poor bandwidth, like 6 MHz or something like that. This one, DC to 20 MHz. Now, that's handy because you often want to use one of the applications

**Dave Jones:** for using the x1 position, for example, is measuring noise. And noise is typically measured over a standard bandwidth, just an industry standard, because you have to pick something, of 20 MHz. And that's why oscilloscopes have 20 MHz bandwidth limits. Well, if you've got your standard x1 probe, eh, you're actually not getting the noise over the full bandwidth.

**Dave Jones:** This one's DC to 20 MHz. So, let's test it. So I've got the Rodin-Schwarz MXO here, and I've got it connected up using the frequency response analyzer in x1 probe mode. And sure enough, I've got it going from 100 kHz to 100 MHz up here.

**Dave Jones:** And sure enough, the blue one here, the red one's phase, and the blue one here is the bandwidth. And 10 MHz there, it starts peaking up at, you know, like at a couple of meg, it starts going up. We're only talking like, you know, point, not even half a dB there or something.

**Dave Jones:** And it peaks at around about that 25 MHz mark, or thereabouts. We'll call it 20. So, like, it's actual minus 3 dB bandwidth is something over in the order of like 50, 60 MHz, something like that. So, really, well, you wouldn't use it that high, but the fact is, yeah, you would certainly use it right up to 20 MHz.

**Dave Jones:** So that's really handy. Now I have to measure, like, over 6 MHz one and see what we get. Alright, so I've got this Siglent PP5 1000 MHz switchable jobby. And its data sheet value is a very typical, almost universal standard 6 MHz bandwidth in the x1 position.

**Dave Jones:** And there you go, I've just done the sweep. It is significantly different. It's a, you know, nice roll-off here. There's no, like, little peak before it rolls off like we saw on the Rigol one. But, yeah, it's about 3 dB down at just over 10 MHz there.

**Dave Jones:** You know, call it rounded to 10 MHz or something like that. So it's a bit better than the spec of 6 MHz there. But it's a good 5.5 dB down at 20 MHz there. And its phase response is a little bit different as well.

**Dave Jones:** So I don't know, which one do you prefer? Do you prefer, like, the higher bandwidth with a little bit of a peaky on it? Or do you like your nice, boring, slow, roll-off 6 MHz jobby? Leave it in the comments.
