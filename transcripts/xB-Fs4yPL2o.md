---
video_id: xB-Fs4yPL2o
title: EEVblog #1096 - ANENG Q1 Multimeter Teardown (Now in 4K!)
url: https://www.youtube.com/watch?v=xB-Fs4yPL2o
source: youtube-asr
timestamps: {"0": 8, "1": 16, "2": 31, "3": 44, "4": 54, "5": 68, "6": 81, "7": 100, "8": 109, "9": 119, "10": 130, "11": 145, "12": 154, "13": 168, "14": 180, "15": 193, "16": 203, "17": 220, "18": 231, "19": 241, "20": 256, "21": 270, "22": 280, "23": 293, "24": 306, "25": 319, "26": 331, "27": 344, "28": 357, "29": 375, "30": 388, "31": 400, "32": 417, "33": 426, "34": 441, "35": 459, "36": 470, "37": 481, "38": 490, "39": 505, "40": 514, "41": 526, "42": 537, "43": 550, "44": 562}
---

**Dave Jones:** Anyway, let's take a look inside this thing. I don't particularly like the children bail. It just like comes out every time you got to dick it around to put back in.

**Dave Jones:** They do have metal threaded insert though, but the screw comes out just flies out so it's easily lost. The two double a batteries you need your bloody double a batteries to at least get your pissant 50, you know, 60 70 hour battery life or whatever it is you might get out of this thing.

**Dave Jones:** Anyway, let's crack it open. There's no fuse access of course, you wouldn't expect it. And here's where you might want to switch to 4K mode down here in the corner so you can see all the detail.

**Dave Jones:** Let's have a look. I don't mind that little riser board there for the uh current. That's pretty good. You can see how it's got the split jack and it's actually sensing those off so I can do that auto detection there.

**Dave Jones:** No worries. Two little M205 HAC fuses there. Not branded at all so okay, well they're better than a little pissant glass fuse. There's our little 10 amp current shunt.

**Dave Jones:** Isn't it little piss weak? Look at that. Couple of MELs in there. I jeez, I tell you what. They filled in the ground plane. Look at that. That's pretty close to your voltage input jack.

**Dave Jones:** That's like you want to peel back the ground plane. Why have that close? I don't I don't understand that at all. I think that's probably too close, but this thing yeah, I I forgot to mention it's only like just like the 8008 is 600 volt CAT III, but it's not independently tested or rated or anything like that.

**Dave Jones:** Okay, we've got a couple of more MELs. You know, I'm a bit of a MEL fanboy, but apart from that, where are the where's the PTC protection? Where are the MELs on there?

**Dave Jones:** We've got ourselves a diode. Yeah, good on you. And here's the interesting thing. We've got ourselves a relay. Look, it's a big proper ass relay in there, and it goes clunk when you power it on.

**Dave Jones:** Wait, no. Is that our PTC? That could be our one and only PTC, is it? Uh, okay, it's better than nothing. Anyway, we've got ourselves the black blob there.

**Dave Jones:** What else? Look at this beastie. There, yes, they have rubbed the numbers off that. Look at that, they have completely erased from existence. Got ourselves an e-squared prom there with some pretty crusty soldering.

**Dave Jones:** I'll get the macro lens out and show you. And there's our ICL voltage reference. What's that one? I could use my new 4K zoom. I'll zoom into that and see what we get.

**Dave Jones:** Cuz that's one of the advantages of having a 4K camera, not necessarily that, you know, people are going to watch in 4K, but at that the editing stage, it allows me to like zoom in on teardowns and stuff like that in the editing process if I see something interesting.

**Dave Jones:** Cuz once again, I do all this on the camcorder screen, right? So, even though this is a really excellent camcorder screen, it's 1440 by 1080, like, you know, I I really can't It's small, and I can't see it.

**Dave Jones:** 3 and 1/2 inch, I can't see really good detail on that. So, often in teardowns, when I go to editing stage, I'll notice something and go, "Aha, I want to zoom in." So, with 4K, it allows me to, you know, zoom in really well.

**Dave Jones:** Just gives me the extra resolution. And well, what else is there? Like, the jacks, they're just mere par for the course on these things. Um, as I said, the ones down in there are split.

**Dave Jones:** You can see that, hopefully. Um, yeah, but that's all she wrote. You know, mysterious micro here. Um, we've got our chipset here, our fake bar graph, and uh Do those solder joints look a bit pasty, or what?

**Dave Jones:** What's the deal there? And if we get the board out, there you go. That was a struggle, but you can see the uh split jacks down in there. Check out these joints here.

**Dave Jones:** Look at those ones. Dry as a dead dingo's donger. Unbelievable. Wow, Frosty the Snowman. Check out the joint in there. Let's just put a lid on the other side.

**Dave Jones:** It's almost like an afterthought. And aha, if you have a look at the data sheet for this Hongfa relay, then it's actually a latching type, which of course makes sense cuz you don't want to be pissing away the current on the coil when you power this thing up.

**Dave Jones:** So, you latch it on, it stays on, and then when you uh remove and then it doesn't consume any power to keep the coil energized. So, and aha, it starts to make a bit more sense if you actually get rid of the battery cover here, which was hiding some of the traces.

**Dave Jones:** I thought it was originally coming from here and this trace was going under to here to the relay, but it's not. If you follow the money directly, this is the voltage input here.

**Dave Jones:** There you go. Directly right over to the one contact of the relay there. So, there you go. It's definitely switching the volts input directly. So, I was actually a bit confused by this.

**Dave Jones:** I thought you know, where does the other side of the contacts go cuz this is the common pin of the relay here. Here's the input coming You can see that comes directly from the input there.

**Dave Jones:** So, there's nothing else connected. Look, nothing behind the curtain there. So, by default, there is no the PTC is on the switched side. Here's the PTC there between those two pins.

**Dave Jones:** There's absolutely nothing on the other contact. So, all they're doing with that relay, the latched relay, that's why it's got two coils there. You can switch it one way or the other then it just stays there to reduce your power consumption.

**Dave Jones:** So, we've got two distinct paths here. One goes via these mouth resistors here in series. These are high value resistors, so it really limits the current. That seems to go directly in here.

**Dave Jones:** Haven't followed that trace, but it completely bypasses the relay up here. Um and and the PTC here. Now, the other path is directly from the jack here, which snakes away its way around.

**Dave Jones:** That goes into uh one contact of the relay, and the only place it The only function of this relay is to switch that direct input in and out. And the out of that, when it is switched in, it goes directly to the PTC here, through the PTC, and that trace goes down into It looks like they've got uh back-to-back diode there.

**Dave Jones:** So, it seems that uh one looks like it's for the voltage range. They switch in uh the resistors here, and they switch in the relay and all that just for the voltage range.

**Dave Jones:** The other one, the direct input um with the PTC protection and the diode protection is for the millivolt range, obviously. Whereas, you know, on the old-school meter, you didn't need any of that relay rubbish or anything.

**Dave Jones:** All you needed was, you know, a different range switch position. So, this is why you can hear the relay switch if we go between volts and millivolts. So, if you compare the original 8008 on the right there to the uh this new, I guess, Q1.

**Dave Jones:** It's not really a replacement for the 8008. It's just uh designed to meet a different market, and they're very similar. They've uh the Q1 has the larger um M205 HSC fuses.

**Dave Jones:** The 8008 has those uh smaller squat ones, which are probably um harder to get, you know, technically not as good. The mouth input uh resistors are the same, the same uh diode uh protection.

**Dave Jones:** And it's probably got the same blob microcontroller. It's got the E squared prom there. Um but, it's got the uh that extra uh microcontroller chip. Um so, that must be Maybe that's like Is that like doing the extra bar graph stuff and doing like the Something's got to do the relay switching and things like that.

**Dave Jones:** So, maybe they might be uh dual-purpose in that cuz they've got to get those uh 100 extra LCD segments from somewhere. I'd be surprised if the chipset has all that.

**Dave Jones:** It uses the same buzzer and everything else. So, it's a bit bigger, uses AA batteries, but it's basically crippled by that ridiculous choice of that screen. And these soft buttons are going to put the relay in there.

**Dave Jones:** Like, why? I I just don't get it. It just seems to be a meter that didn't seem to need to be made. Really, I mean, the screen just spoils it.

**Dave Jones:** I can see that hey, having the extra non-contact voltage thing would be an additional feature on there. Some people might prefer the you know, the push buttons to the range switch, and that's fine, but nah, it's totally let down by the screen.

**Dave Jones:** Imagine if they just you know, put the original screen back in there and had the AA batteries. It'd last forever. It'd be a nice little up-step in the model there.

**Dave Jones:** And if they just put in those extra two current ranges, jeez, it might even be a bit of a killer. But, you know, construction of these things is as what you'd expect for a $25 and a $38 multimeter.

**Dave Jones:** It's you know, it's acceptable for the price. So, anyway, if you liked that video, please give it a big thumbs up. And as per the previous video, please tell me what you thought of the 4K video.

**Dave Jones:** And does it actually look any better and on 1080p? Cuz it should in theory, when you upload a 4K video to YouTube, YouTube processes it at a higher bit rate.

**Dave Jones:** They process the 1080p version at a higher bit rate, apparently. And so, they give you and deliver a higher quality 1080p than if you just if I just rendered a 1080p from this 4K content and uploaded it.

**Dave Jones:** Anyway, catch you next time. Mhm.
