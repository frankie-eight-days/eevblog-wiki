---
video_id: wWymcaiaQXM
title: What happened to my Rohde & Schwarz HMO1202?
url: https://www.youtube.com/watch?v=wWymcaiaQXM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 39, "3": 51, "4": 67, "5": 83, "6": 99, "7": 111, "8": 131, "9": 147, "10": 163, "11": 179, "12": 191, "13": 211, "14": 231, "15": 251, "16": 267, "17": 287, "18": 303, "19": 319, "20": 331, "21": 351, "22": 371, "23": 387}
---

**Dave Jones:** Hi, you might remember this Roden Schwarz HMO 1202 series scope that I did a teardown and play around with quite a few years ago. And I actually got this out and I was playing around with it yesterday and I forgot how much I really liked this thing.

**Dave Jones:** It's small, it's compact, it's light, it boots up quick, the fan noise is virtually practically zero, and it's got some really nice features. And my one here is a 300 MHz jobby, it's got mixed signal, it's got pattern gen, and it's got a function gen built in, and I think component tester, and all sorts of stuff.

**Dave Jones:** And it's got really good FFT, and I love the quick view mode on it, I'll show you that in a second. And I've forgotten how much I love this thing, so I might actually use this as my daily driver, but there is one problem.

**Dave Jones:** And sometimes I just completely forget that I've done a video in the past. No, it's not old age, it's just I don't know, some videos stick in my mind and some don't. And I had completely forgotten that I did a teardown, well I knew I did a teardown

**Dave Jones:** of this, but I had completely forgotten that I did like a hacking video of this actually looking at the SPI signals that are controlling the front end gain chip in here, and that's how they actually get the bandwidth. Because this is software bandwidth,

**Dave Jones:** the base unit is 50 MHz, and it goes up to 300 MHz and that's all in software. And they do that by sending SPI commands through to the front chip amplifier on here, I forget the part number, but yeah, that's how they do the software bandwidth.

**Dave Jones:** I'd completely forgotten that I'd done that video. Anyway, I'll link it in up here if you haven't seen that hacking video, it was rather interesting. But anyway, I was playing around with this thing again, and I noticed something that, well, is not right.

**Dave Jones:** You'll notice I've got channel 1, channel 2 here, but channel 1's 1 millivolt per division, it's got a low noise front end, it's looking pretty schmick. But channel 2 is 50 millivolts, let's actually turn that down here. Um, uh, Bueller? Bueller? What's going on here?

**Dave Jones:** Now, here's this feature I told you about the quick view feature. This is one of the things I really like about this. Look at that, you just press the quick view, and it just pops up. Unfortunately it does get rid of channel 1, it gets rid of the channel that you're

**Dave Jones:** not currently engaged in, it actually disables it. So I'm not sure whether, I assume the trigger would still work, I guess. But anyway, yeah, I don't know if they've done that for like a screen clarity reason, or whether that's a process in bottleneck thing, I don't know.

**Dave Jones:** Anyway, yeah, I love how it just automatically puts up like everything you need to know and how they do it on screen. It'd be nicer if I could actually get that bigger, but I can't, unfortunately. So, and the other thing I don't like is that you can't

**Dave Jones:** push to go center here, but you know, eh, can't have everything. But yeah, anyway, nice, but why? Why am I getting this? This is obviously 50 hertz, just look at the time base there, and well, it tells you here, doesn't it? Yeah, 50 hertz, there you go.

**Dave Jones:** So I'm getting all this 50 hertz noise, so I think I've completely come a gutser and I've forgotten to put the shield, when I reassembled it, the shield back on channel 2. It's gotta be. There's no other reason why we'd be picking up 50 hertz

**Dave Jones:** like that. Yeah, I reckon, so let's tear this thing down, and I think we'll find that the shield is missing. Oops. So let's have a squiz, I've got these six screws out of this puppy, and yeah, if memory serves me correctly that just pops off there, and

**Dave Jones:** no, both cans are in position. What's on the bottom? No, no, that's the trigger. That's the trigger channel. Yeah, because one of the things I don't one of the things that annoys me on this is that they're putting the external trigger here and channel, like, the external trigger should be like all the way over

**Dave Jones:** this side physically. It's just, I always plug in the channel 1 into the wrong one. I plug it into the external trigger. Yeah, so look, yep, yep, yep, yep, there it is. Yep. Yeah, you can see where that was soldered in there. I

**Dave Jones:** have not put the can back on, so wah, wah, wah, wah. Yeah. There's, I don't think there's any chance of me finding that shield now because this was like four, five years ago or something. This is quite a long time ago. They've since updated this model, by the way.

**Dave Jones:** It's now the RCM or something. There's a C in there or something. 1000 model, which looks to be, looks and feels almost identical, but it doesn't have the 50 ohm input. One of the things I like about this thing is that it does have actually a

**Dave Jones:** switchable 50 ohm input, which not even my RTB2000 model has, which is, I don't know, three times the price of this thing. Yeah, so this is like a really great little scope. I love it. So yeah, I'm going to have to manufacture some sort of

**Dave Jones:** can. I don't know, does anyone know? Are there any like prototype services out there? I mean, I guess I could take, I've got to desolder this. I don't know why they soldered them in there. I guess from vibration they want to stop them falling out or something, but they did solder it in one corner.

**Dave Jones:** I guess I could take that out, get all the measurements and whatnot, and then I could probably do it without that. But yeah, anyway. Yeah, if anyone knows, can you get like, is there a really cheap and simple prototype service out there? I think one of the manufacturers does it.

**Dave Jones:** So I think that's not new metal. I don't think this is magnetically shielded. But in either case, it doesn't matter because we're not dealing with a magnetic interference here, we're dealing with electric. So yeah, just a regular shielding can. So I don't know, maybe I can

**Dave Jones:** get some, you know, I could bodge something, but I don't know. Let us know in the comments down below what you think the best way to replace a missing shield like this, because I want to try this as my daily driver scope, and well, yeah, I don't

**Dave Jones:** want that much crap on my second channel. Thank you very much. So yeah, leave it in the comments. Anyway, catch you next time.
