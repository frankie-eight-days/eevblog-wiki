---
video_id: e98cYNPUxcg
title: Fluke PM3370B Solder Joint Inspection
url: https://www.youtube.com/watch?v=e98cYNPUxcg
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 21, "3": 36, "4": 53, "5": 60, "6": 80, "7": 91, "8": 104, "9": 118, "10": 127, "11": 142, "12": 156, "13": 164, "14": 175, "15": 186, "16": 199, "17": 214, "18": 233, "19": 247, "20": 260, "21": 268, "22": 279, "23": 289, "24": 307, "25": 315, "26": 325, "27": 339, "28": 353, "29": 372, "30": 386, "31": 400, "32": 410, "33": 426, "34": 439, "35": 458, "36": 475, "37": 487, "38": 504, "39": 517, "40": 525, "41": 535, "42": 550, "43": 562, "44": 577, "45": 593, "46": 606, "47": 621, "48": 634, "49": 660, "50": 670, "51": 682, "52": 696, "53": 710, "54": 726, "55": 740, "56": 750, "57": 767, "58": 775}
---

**Dave Jones:** Hi, just a quick follow-up video on the Fluke PM3370B scope. I It has not failed. I've had this like running for like a day and a bit continuously except when I go home.

**Dave Jones:** I don't want to leave it overnight just in case. And this thing just does not fail. I've just switched it off now or a few minutes ago and whoa.

**Dave Jones:** That's That's hot. I can barely keep my hand on there. So, I've had it running with the lid on, of course, to contain the heat inside so we're only relying on the fan, which is all the way up here, to sort of like, you know, circulate and stuff.

**Dave Jones:** So, you know, it gets hotter inside. So, it's effectively like heating up all the components to try and make it fail. But, unfortunately, it hasn't failed. Now, I want to take out the board and actually have a look at what solder joint and one of the components cuz here's a comment from the previous video from John Bonham.

**Dave Jones:** Thank you very much. Who noticed in one of my lingering nut shots, which I'll show here, that it looks like I believe it's the PTC in there, is it?

**Dave Jones:** On the input side over here that was It looked like the solder joint on that was dry as a dead dingo's donger. And somebody emailed me about another surface mount capacitor on the bottom that they think they noticed a like the solder was missing or a dodgy joint or something like that.

**Dave Jones:** And I Well, I'm going to take it out and visually check and show you because he thought like the PTC when I actually wobble it when I moved it or something it moved too far or something like that.

**Dave Jones:** Anyway, it could be, but if the DC We measured the DC rail and the DC rail was fine. So, if the if there was a crack in the solder joint in there that was causing that, then you wouldn't still get your DC rail.

**Dave Jones:** So, anyway, you never know with intermittent things. But, anyway, I get these comments quite a lot, especially in these repair videos because people are looking actively looking at my videos in high resolution, of course.

**Dave Jones:** Sometimes they do them in 4K resolution, but this one was 1070. And they go, "Aha! I can see that solder joint." And they give me the timestamp and everything.

**Dave Jones:** Fantastic. Thank you. Please keep doing that. But I find that in almost every case, uh that what you're seeing is a quirk of the lighting. And it's really hard to actually get good lighting on solder joints when you're inspecting this.

**Dave Jones:** It's why you have to really inspect them up close under a good optical magnification and different angles and with different lighting or up to, you know, lighting that you've set up optimized for the task.

**Dave Jones:** It's very difficult. So, we'll take the board out and we'll just recheck that joint to see if it is actually dodgy or whether or not it's just the light.

**Dave Jones:** So, I don't know. Let's go. Okay, there's the part there. And the first thing to notice, you know how I mentioned PTC before? This is actually NTC or negative temperature coefficient.

**Dave Jones:** PTC is positive temperature coefficient. I just assumed it was a PTC. I couldn't see the writing on it from the top because it's in series, of course, with the diode bridge.

**Dave Jones:** Here's your 240-V mains input here. Here's your X-class capacitor across the input. And then you've got a what I thought was a PTC in series with your diode bridge rectifier here, which is a full-wave bridge rectifies your AC mains.

**Dave Jones:** And that's why you've got to have a 400-V Nippon Chemi-Con caps here. So, what a PTC does, positive temperature coefficient, if the temperature of this part increases, which it will do if you pass more current through it, it will heat up.

**Dave Jones:** And when it heats up, a PTC will actually increase in value. So, what that does, if, you know, there's some short in your circuit somewhere, there's some fault that's drawing excess current, then this will actually, a PTC, will heat up and it will limit the current flow.

**Dave Jones:** So, it's an overcurrent protection device. Um but, why they've got an NTC in here in series with the bridge rectifier, what that's doing is it operates negative. So, if the temperature of this increases, the resistance goes down.

**Dave Jones:** So, and of course, the temperature of this will increase because there's the more current flows, the resistance goes down. Well, why would you do that? That just sounds like it's dumb, right?

**Dave Jones:** Well, no, it's not. What that's used for in this particular case, if you see an NTC in series with something like this, you know that's used for inrush current limiting.

**Dave Jones:** The surge when you first turn it on, these capacitors, of course, are going to act as a basically a short circuit. Um so, you want to limit the inrush current to charge these capacitors up.

**Dave Jones:** The way you do that is with an NTC, not a PTC. So, there you go. Um I nothing to do with this, but I just We're talking about this parts, so there you have it.

**Dave Jones:** So, apparently, in the previous video when I gave this a wiggle wiggle wiggle yeah, um it moved. They said it moved too far, but um no, that's just the nature of those um thin leads and the way it's mounted um with uh you know, off the board with only two of them like that.

**Dave Jones:** So, I don't see anything wrong there. Okay, so I've got my times 10 macro lens. Just This is a similar shot to how I had it set up before.

**Dave Jones:** My studio lights are here, and well, it's hard for me to see on the camcorder screen. So, I may have to um you know, annotate this in the um edit.

**Dave Jones:** Uh that that does look dry as a dingo's dung, doesn't it? You can see Oh, jeez, it's hard to get focus, you bastard. If I wiggle the top I'm wiggling the top now, but I'm not seeing the bottom wiggle.

**Dave Jones:** Now, I got my studio lights in the same position that I had them before. Okay, so I'm putting my studio lights like behind or to the right-hand side of the thing now.

**Dave Jones:** I can't once again, I can't see this on the camcorder screen. Okay, how does that look? Does that look any different now? Hmm. Now the ultimate optical tool I have here in the lab is my Mantis Elite microscope and I've mentioned this before that the internal camera in this thing sucks ass.

**Dave Jones:** It's just Oh, it's hopeless. I hate it. Um it's really an optical visual inspection bit of kit and so I've got my camcorder up into the hood of the you know, the actual viewing hood of this thing.

**Dave Jones:** So it's it's not the best, but there it is looking from the top and as you can see it actually looks pretty schmick. And there's another view of it there and you can see that there is like a really sharp angle on like the right-hand side here.

**Dave Jones:** It was left hand side before when we're viewing it from the other direction. Um and so yeah, but the one but on the left of the joint there, it is actually very smooth.

**Dave Jones:** So it's really hard to keep and get this in focus on camera. But yeah, it is actually completely smooth on one side and it doesn't move when I wiggle it on the top.

**Dave Jones:** All right, so how does it look under the Tagarno microscope? The Tagarno is just not as good as you can't beat the optical Mantis microscope, but I I actually got the camera working in the Mantis, but it's just it's garbage.

**Dave Jones:** It is so underexposed. It just looks black as the ace of spades. It's just absolutely terrible. Anyway, here's the joint under the Tagarno. So there it is. That's the one we're interested in and once again, if I wiggle the bottom, I am wiggling that.

**Dave Jones:** Okay? There is nothing transferring through to that other side. okay? But, so if I turn that light and that's the internal light. So, now if I get another external light and turn this down a bit and I take it around take it around like there there is a sharp contrast.

**Dave Jones:** But, unfortunately, to tilt it and get the same zoom, I'm going to have to lift my Takgano up. That might do it. There you go. Because it's all a function of distance.

**Dave Jones:** It's tricky cuz I've got my ATM on there. Hang on. You're better off having it higher up and then bringing the object up to it than not. Okay, so now my Takgano's high.

**Dave Jones:** All right, there we go. Yeah, see it's overexposed there, but hopefully you can see but that is shiny. I can actually under expose that. There you go. Can under expose that.

**Dave Jones:** There you go. Now you can actually see. Let me zoom in a bit more. Uh sorry, I've got a hand hold this just at like I'm at maximum zoom.

**Dave Jones:** It's 30 cm working distance. Now, you can see down in there you can see why you know, like under certain lights this would this would show up really bad.

**Dave Jones:** Um but as I said, there is no like if I wiggle that, it's doing absolutely nothing. So, that's at that angle. It's all about the angles. There you go.

**Dave Jones:** Look, on that side of it the joint actually looks I'll try and keep it a bit steadier. Trying to hold it in free air here. See? On that side it actually looks pretty good.

**Dave Jones:** So, yeah, I like there's there's nothing inherently wrong with that joint. I don't think. But, of course, I will just to be sure, I will actually reflow um that joint.

**Dave Jones:** But, yeah, you can see how hopefully that gives you an idea. And look, and it looks perfect from the top. If you were looking around with your digital, you know, microscope, even if you've got a kick-ass one like this uh Tagarno one, then like you would think that would be, you know, great.

**Dave Jones:** Like you might give it a little bit of an angle, but I can see this incredibly clearly and detailed under the Mantis microscope here. And um yeah, I'm sorry I can't It doesn't show up on camera.

**Dave Jones:** It just looks go- You have to look through these things in real life to actually like it just It's so bright and clear and crisp. And and I can tilt my head around and I can like it's a 3D microscope, so I can like move my head and look at the angles and stuff like that.

**Dave Jones:** And it looks okay. It does actually look okay. But, yeah, that is actually, believe it or not, that is I I believe that's a that's a good joint. Like you would you would certainly certainly I'd say resolder that as a matter of course.

**Dave Jones:** So, let's do that just to keep everyone happy. But, anyway, I hope you found that as an interesting um example of how light can potentially fool you into the Oh, that's definitely a dry joint when it's actually in most of in almost every case every repair almost every repair video actually I get somebody email me uh cuz they've watched it on their high-def telly and they go, "Oh, that

**Dave Jones:** joint's definitely dry." Um and it it's not. It's just a trick of shadows and lights and stuff like that. In this particular case, yeah, it doesn't look terrific at certain angles.

**Dave Jones:** And um but, certainly when I wiggle it, so it's got nothing to do with the wiggle wiggle wiggle, yeah. Um and so, I will just uh clean that and resolder it.

**Dave Jones:** Oh, we'll just heat that up a bit there. And now, I'll actually wick I'm just putting that on so I then I can wick it off. Let's just some of that away, shall we?

**Dave Jones:** And it's still not wiggle wiggle wiggle year in. And we will resolder that. Nice and fresh. There you go. That's a freshy. Look at that. Beautiful. Yeah, it's that lead-free rubbish.

**Dave Jones:** But anyway, thanks for those who pointed it out. I just wanted to show you that it's most likely wasn't that. So, yeah, there's a couple of other theories and stuff, but yeah, if it ain't busted, it's hard to fix it.

**Dave Jones:** And by putting the case on, it is actually getting very warm inside this thing. So, yeah, like I can put it inside like if you don't have a thermal chamber, if you just want stuff to heat up, you can stick it inside say a Styrofoam container or something.

**Dave Jones:** I have it You see me score those from the dumpster, the big Styrofoam containers. That's what I have those for. You can stick them in there. They do a pretty good job once you heat it, you know.

**Dave Jones:** Put a little port in the side for the cable, power it up, and it'll heat up inside cuz it's an insulator. The heat can't radiate out. So, yeah, of course you put a temperature probe in there to make sure you're not going to fry the thing, but yeah, you can stress products that way or something, but yeah, I don't know.

**Dave Jones:** At this stage, I'm just running it for like a few days to see how it goes and stuff, but I I just cannot fail it. It's just not failing.

**Dave Jones:** So, anyway, hope you found it interesting. Catch you next time.
