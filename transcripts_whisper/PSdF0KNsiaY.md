---
video_id: PSdF0KNsiaY
title: BM786 Continuity Firmware Testing
url: https://www.youtube.com/watch?v=PSdF0KNsiaY
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 45, "3": 70, "4": 90, "5": 110, "6": 130, "7": 151, "8": 166, "9": 181, "10": 206, "11": 227}
---

**Dave Jones:** Hi, just a quick test on new firmware I've got for the BM786 for the continuity issue brought up on the forum. And this is the new 78612 firmware, hopefully you can see that. Current release 09 version, there we go, 609 version. So let's put them on ohms here.

**Dave Jones:** Now the current firmware will switch on at about 270, 280 ohms, or something like that. There you go, switches on at 270 and it actually requires a bit of hysteresis, 300, to get back. Now the new firmware, 90 ohms, 80, 70, 60, 50, 40, and it turns out

**Dave Jones:** it's just under 40. So let's go to 39, oh yeah, just on 39. And it won't switch off until actually 99, it'll actually switch off at exactly 100 there. So yeah, it's now basically, you know, say 40 ohms and 100 ohms there. So that should keep a lot of people

**Dave Jones:** happy who want a lower resistance reading. Now, interestingly, they did say there will be some compromise on the continuity test rate. So what I've got here is a pulse going in that's normally high and then just pulses low briefly. It's currently set for 200 millivolts peak-to-peak at 1

**Dave Jones:** hertz there, right? So 1 hertz reference at 200 millivolts peak-to-peak just gives us like a value that's sort of like, you know, in the 300 ohm region, something like that. So at 99%, right? That's a pretty, well, slow, because this is supposed to have a response time of like, you know, like microseconds, 100 microseconds

**Dave Jones:** or something. So if we go 99.999% there you go, it still does it at 99.999%. What is that? 10 microseconds or something? We can go down to 99.99999 we can go down to 5 nines in percentage there, and it's still doing, well, nope, nope, it's just starting to miss it there.

**Dave Jones:** So what's that? 1 microsecond or something? And it's missing the occasional, yep, it misses the occasional one there, but right? It is really, right? It's really very quick. So let's just go back to 99.999% there, it's consistently doing that. So the new firmware over here

**Dave Jones:** doesn't, well, it kind of does. You're not hearing that, but trust me, there is a brief I can hear a little tick, a tiny tick in there each second, but it's obviously not triggering the visual continuity there. So it's not actually triggering that

**Dave Jones:** at 99.999. So let's go 99.9% still doesn't do it. You can still hear it, but it's not triggering it. So let's go 99.9%. Still doesn't do it. You can see a slight on the screen there, you can see that it is actually flashing.

**Dave Jones:** So, yeah, that's actually very slow. Yet, yet, it's really not a problem in terms of the actual probes there. But that is, you know, several orders of magnitude slower than the current firmware here. So if we go to just 99%. Right, so that's effectively

**Dave Jones:** 100 millisecond pulse now. And it's not really latching, so the latching is kind of different, like the pulse stretching seems to be different than the older firmware over here. It can do it, but yeah, you're still not getting that. But as an actual continuity tester, it

**Dave Jones:** it works, but it's more itchy and scratchy. Original firmware, yeah, that's way more latched. So it's basically gone from a latched to an itchy and scratchy. So let me know what you think down below. Is that acceptable or not? Catch you next time.
