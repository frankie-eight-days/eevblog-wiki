---
video_id: VtsE6xbwHcQ
title: EEVblog #223 - Agilent Oscilloscope High Res Mode
url: https://www.youtube.com/watch?v=VtsE6xbwHcQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 57, "4": 85, "5": 105, "6": 125, "7": 141, "8": 157, "9": 177, "10": 197}
---

**Dave Jones:** Hi, I thought I'd show you a quick little track for young players, really, with the high-resolution mode that you get in a lot of modern scopes like this. In this case, it's the Agilent InfiniiVision 3000X series. Now, the high-resolution mode, if you're actually

**Dave Jones:** going to acquire down here, it's got normal mode, peak detect, average and high resolution. Now, the high-resolution mode actually does some high-order averaging of the bits to actually give you a lower noise floor. And it can really work out quite well, and I might show an example of that.

**Dave Jones:** But I just thought that I'd show an example here of how it can be a little trap unless you're at, if you've got high-frequency noise superimposed on a low-frequency signal that you're looking at. Now, in this case, I've got a couple of signals here which I'm capturing.

**Dave Jones:** They're very slow, 100 milliseconds per division in there, right? So a relatively slow changing signal, which we're going to single-shot capture. So let me single-shot capture that, and bang! OK? And it looks, both of these curves look quite smooth and nice, OK? But when you zoom in, look at that, see?

**Dave Jones:** Only when you zoom in can you see that noise on the signals like that. But when you zoom out, like that, you don't actually see it. It looks smooth as a baby's butt. But if you turn off high-res mode and you go into normal mode,

**Dave Jones:** let's capture that same signal again, shall we? And bang! You can see the noise at the slowest time base like that, and it's exactly the same when you zoom in. So if you are using high-resolution mode, just be careful at these expanded time bases that it's not averaging

**Dave Jones:** some high-frequency noise like that. Now, I'll show you an example of where the high-res mode can be useful to clean up your signal, just measuring the DC output of a 5-volt sorry, a 1-volt power supply here. So we've got a volt output there,

**Dave Jones:** and the line is a bit thick and fuzzy regardless of what the time base, 10 nanoseconds per division, 10 microseconds per division, and that's because a wide bandwidth scope like this one, this one's a 500 megahertz bandwidth scope, so it's going to be relatively noisy like that.

**Dave Jones:** But if you go into the acquire menu and you choose the high-resolution mode, bang! Look, it's cleaned that up very significantly, and at the lower time bases. If you go up to the higher time bases, of course, it's still thick like that, but at the lower

**Dave Jones:** time bases, it really averages out that high-frequency noise, as opposed to average mode, which is a bit different. It works differently, and I won't explain that. But high-resolution mode can be quite neat, and you can get a much greater vertical resolution, or improve vertical resolution on your scope

**Dave Jones:** effectively, compared to normal mode. So, there you go. That's high-resolution mode, and it's available not only on this scope but a lot of modern scopes out there, so have a play around with it, but just be careful. ... ...
