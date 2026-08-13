---
video_id: EJ6KCpHc--4
title: Strange Brymen BM869 Resistance Quirk
url: https://www.youtube.com/watch?v=EJ6KCpHc--4
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 43, "3": 57, "4": 76, "5": 92, "6": 110, "7": 130, "8": 150, "9": 183, "10": 215, "11": 233, "12": 254, "13": 279, "14": 304, "15": 327, "16": 344, "17": 371, "18": 392}
---

**Dave Jones:** Hi, somebody on the EEVblog forum mentioned that there's an issue with the Breiman BM869. I've got the BM869, not the new S model. I've got the original. They said there's an issue around about 560, when measuring 560k resistors, if you have it anywhere near mains cabers, it'll cause a problem.

**Dave Jones:** And Joe looked at this in his video, but he didn't measure 560k. Joe Smith, that is. In his video, this is on the electrical meter robustness testing thread on the EEVblog forum. So I thought I'd try it. Here you go, 560k, nothing special, just got some leads here.

**Dave Jones:** And at first I didn't, like, I could, you know, move the leads around and it's, you know, it's changing, stuff like that. Which is not uncommon because when you're measuring high resistances like this, once you get into the hundreds of k's, the megs especially,

**Dave Jones:** then the currents we're talking about, test currents flowing through these cables are incredibly minute. So you can get, you know, triboelectric effects and you can get, you know, all sorts of pickup. And, you know, that's generally acceptable. But in this case, let's actually try, well, I didn't.

**Dave Jones:** At first, I got this to actually fail with no mains cable near it at all. This was on the floor, I've got no other, my instruments still aren't connected back here. So I've basically got no mains hanging around here at all. So let me put this away down on the floor, okay?

**Dave Jones:** And I'll get these cables and I'll just, sorry about this, but I'll just rub it against my shirt. Look, I'm able to get it to do that, but once again, that could be like triboelectric, you know, static effects, stuff like that. I was able to get it to continuously cycle.

**Dave Jones:** I was able to get it, trust me, to continuously cycle. Anyway, mains cable, let's put it near this mains cable, there you go. There you go. It's just, and if I turn on the light, this is going to my studio light. If I don't move anything else and I turn on the studio light, no, no.

**Dave Jones:** No, but certainly I can get it to just like cycle through like that. Okay, so let's see if I can, can I get it to, yeah, okay, it's permanently doing it. I won't breathe. Somebody said it was within a certain range. Yep, 660K, 560 definitely does it.

**Dave Jones:** 460, there you go. So it's within a certain range. 570, oh, I think somebody has lucked upon an exact figure where this BM869 goes Berco. 510, yeah, there you go. So it's like, let's just say 500K. In the range of like 500K, it doesn't, of course, 560 is an E12 preferred value.

**Dave Jones:** So there you go. Yeah, there's definitely something at play here. Now, let me actually try the brand new Breiman BM786. Will be available shortly. They're just having a few last minute issues. Let's try this. So BM786, can you see that? Alright. Once again, you know, you move the leads around like that, you expect some sort of change in that.

**Dave Jones:** No problem at all. I'll do the shirt thing. I'll do the mains cable thing. Oh, 560, no, no, I'm not, not seeing that. The problem is I can't put it up like that. The stand, the tilt stand on this is actually quite far back.

**Dave Jones:** So to prevent the lights. Um, no, I'm not, I'm not seeing it. I'm not seeing it on the BM786. So, no problems. Looks like it is to do with the BM869. Not unusual, like we're seeing like, you know, weird stuff like this before.

**Dave Jones:** Like famously the Fluke 87, of course, had that GSM fault. So that, you know, only with GSM mobile phones did it actually upset the firmware and brick them. But, yeah, I can get that to do that just on my shirt. Like that. So, anyway, yeah, but, look, I'll go to 460K.

**Dave Jones:** 460K, it definitely won't happen. So it's not, it is specifically within that range. That is very, very interesting. So there's some sweet spot there. Um, I wonder if it's a sweet spot on the range. So let's go up, actually, let's go up to 4 point, actually, yeah, 56.

**Dave Jones:** Let's go up to 450, okay? Let's go up to 4.5 meg. Does it do it on 4.5 meg? Now, once again, you know, I expect as you go up in the range, I'd expect it to cause more issues. But no, no, it seems to be only the 560K range.

**Dave Jones:** So that is really fascinating. Let us know, um, if you've got one of these, can you replicate this? And I'm certainly not in a noisy environment here, as I said, nothing's really running. Oh, I've got my overhead lights on, my studio lights on, I guess.

**Dave Jones:** Let me, I don't know, I could switch my studio lights off. And, right, so there's no, like, you know, inverters or whatever up there running. And let's go 560, there we go, 560K. Okay, yep, and, yep, yep, I can get it to, should be able to get it to do that.

**Dave Jones:** Apparently, like, if you wrap it around, you know, you've got to do a wrap, something like that. Anyway, can eventually get it to happen. Anyway, let us know in the comments if you've got an 869, that is very interesting. I'm sure Brian will get to the bottom of it, they're very good at investigating issues like that.

**Dave Jones:** So, yeah, catch you next time.
