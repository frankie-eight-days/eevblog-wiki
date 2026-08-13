---
video_id: _hUrp6wZgbk
title: What's up with my Siglent Calibration?
url: https://www.youtube.com/watch?v=_hUrp6wZgbk
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 36, "3": 68, "4": 84, "5": 104, "6": 120, "7": 144, "8": 172}
---

**Dave Jones:** Hi, I was just doing some peak-to-peak jitter analysis for another video, and I was using a Siglent scope here. This is the 1 gig jobby, the SDS5000 and I had a bit of an issue with it. So I got out the SDS2000 here.

**Dave Jones:** Both of these, by the way, are the only scopes I have in the lab that actually do peak-to-peak jitter measurement. None of the other scopes do it. The MXO4 doesn't. It needs the MXO6 to do that. The Keysight 3000 doesn't do it. You need the Keysight 6000 to do that.

**Dave Jones:** My tech MDO3000 doesn't do that, so anyway. Check this out, right? I'm feeding in a 500 millivolt RMS signal. Sine wave, right? 10 megahertz, 500 millivolts. And no, we've got like 600 and something here. I can clear sweeps at 650 millivolts. Right? This is 200 millivolts per division,

**Dave Jones:** full bandwidth, times one probe, AC coupling 50 ohms, okay? And then I do the exact same signal over here on the exact same scale, vertical scale, and I get precisely my 500 there. Go away. How do you get rid of that? I can clear sweeps here.

**Dave Jones:** I get precisely my 500 millivolts. This is 625. What the hell's going on? I just shot this before I do the internal self-calibration, but I've never known a scope to be that far out. And I tried the second, look, you can see it's off the scale there, right?

**Dave Jones:** And then I tried the second channel. It's off the scale. So there's nothing wrong with channel one. So like, well, channels one and two are the same, so what the hell? Okay, I'm going to run self-cal now and see if that fixes it.

**Dave Jones:** Because this is just ridiculous. Anyway, continue, yes. Okay, doing self-cal. I'll get back to you. See if that fixes it. But 150 millivolts out? Crazy! Well wow, what do you know? There you go. Calibration finished. Clear sweeps. 503 millivolts. The 3 millivolts is neither here nor there.

**Dave Jones:** So there you go. The gain of this thing, not the offset, because usually you know, front ends will, the offset, DC offset will drift. But in this particular case, the actual gain was out by what? 20%? Or something? Ridiculous. That's really weird. Anyone got any clue why?

**Dave Jones:** Leave it in the comments down below. Anyway, that's it. Catch you next time.
