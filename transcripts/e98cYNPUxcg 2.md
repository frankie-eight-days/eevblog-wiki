---
video_id: e98cYNPUxcg
title: Fluke PM3370B Solder Joint Inspection
url: https://www.youtube.com/watch?v=e98cYNPUxcg
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 47, "3": 72, "4": 91, "5": 123, "6": 156, "7": 175, "8": 208, "9": 241, "10": 262, "11": 289, "12": 307, "13": 335, "14": 358, "15": 390, "16": 421, "17": 451, "18": 486, "19": 497, "20": 523, "21": 546, "22": 583, "23": 610, "24": 637, "25": 667, "26": 682, "27": 700, "28": 720, "29": 747, "30": 771}
---

**Dave Jones:** Hi, just a quick follow-up video on the Fluke PM3370B scope. I It has not failed. I've had this like running for like a day and a bit continuously except when I go home. I don't want to leave it overnight just in case. And this thing just does not fail.

**Dave Jones:** I've just switched it off now or a few minutes ago and whoa. That's That's hot. I can barely keep my hand on there. So, I've had it running with the lid on, of course, to contain the heat inside so we're only relying on the fan, which is all the way up here, to sort of like, you know, circulate and stuff. So, you know, it gets hotter inside. So, it's effectively like heating up all the components to try and make it fail. But, unfortunately, it hasn't failed. Now, I

**Dave Jones:** want to take out the board and actually have a look at what solder joint and one of the components cuz here's a comment from the previous video from John Bonham. Thank you very much. Who noticed in one of my lingering nut shots, which I'll show here, that it looks like I believe it's the PTC in there, is it? On the input side over here that was It looked like the solder joint on that was dry as a dead dingo's donger. And somebody emailed me about another

**Dave Jones:** surface mount capacitor on the bottom that they think they noticed a like the solder was missing or a dodgy joint or something like that. And I Well, I'm going to take it out and visually check and show you because he thought like the PTC when I actually wobble it when I moved it or something it moved too far or something like that.

**Dave Jones:** Anyway, it could be, but if the DC We measured the DC rail and the DC rail was fine. So, if the if there was a crack in the solder joint in there that was causing that, then you wouldn't still get your DC rail. So, anyway, you never know with intermittent things. But, anyway, I get these comments quite a lot, especially in these repair videos because people are looking actively looking at my videos in high resolution, of course. Sometimes they do them in 4K resolution, but this one was 1070. And

**Dave Jones:** they go, "Aha! I can see that solder joint." And they give me the timestamp and everything. Fantastic. Thank you. Please keep doing that. But I find that in almost every case, uh that what you're seeing is a quirk of the lighting. And it's really hard to actually get good lighting on solder joints when you're inspecting this. It's why you have to really inspect them up close under a good optical magnification and different angles and with different lighting or up to, you know, lighting that you've set up optimized for the

**Dave Jones:** task. It's very difficult. So, we'll take the board out and we'll just recheck that joint to see if it is actually dodgy or whether or not it's just the light. So, I don't know. Let's go. Okay, there's the part there. And the first thing to notice, you know how I mentioned PTC before? This is actually NTC or negative temperature coefficient.

**Dave Jones:** PTC is positive temperature coefficient. I just assumed it was a PTC. I couldn't see the writing on it from the top because it's in series, of course, with the diode bridge. Here's your 240-V mains input here. Here's your X-class capacitor across the input. And then you've got a what I thought was a PTC in series with your diode bridge rectifier here, which is a full-wave bridge rectifies your AC mains. And that's why you've got to have a 400-V Nippon Chemi-Con caps here. So, what a PTC does, positive

**Dave Jones:** temperature coefficient, if the temperature of this part increases, which it will do if you pass more current through it, it will heat up. And when it heats up, a PTC will actually increase in value. So, what that does, if, you know, there's some short in your circuit somewhere, there's some fault that's drawing excess current, then this will actually, a PTC, will heat up and it will limit the current flow. So, it's an overcurrent protection device. Um but, why they've got an NTC in here in series with the

**Dave Jones:** bridge rectifier, what that's doing is it operates negative. So, if the temperature of this increases, the resistance goes down. So, and of course, the temperature of this will increase because there's the more current flows, the resistance goes down. Well, why would you do that? That just sounds like it's dumb, right? Well, no, it's not.

**Dave Jones:** What that's used for in this particular case, if you see an NTC in series with something like this, you know that's used for inrush current limiting. The surge when you first turn it on, these capacitors, of course, are going to act as a basically a short circuit. Um so, you want to limit the inrush current to charge these capacitors up. The way you do that is with an NTC, not a PTC. So, there you go. Um I nothing to do with this, but I just We're talking about

**Dave Jones:** this parts, so there you have it. So, apparently, in the previous video when I gave this a wiggle wiggle wiggle yeah, um it moved. They said it moved too far, but um no, that's just the nature of those um thin leads and the way it's mounted um with uh you know, off the board with only two of them like that.

**Dave Jones:** So, I don't see anything wrong there. Okay, so I've got my times 10 macro lens. Just This is a similar shot to how I had it set up before. My studio lights are here, and well, it's hard for me to see on the camcorder screen. So, I may have to um you know, annotate this in the um edit. Uh that that does look dry as a dingo's dung, doesn't it? You can see Oh, jeez, it's hard to get focus, you bastard. If I wiggle the top

**Dave Jones:** I'm wiggling the top now, but I'm not seeing the bottom wiggle. Now, I got my studio lights in the same position that I had them before. Okay, so I'm putting my studio lights like behind or to the right-hand side of the thing now. I can't once again, I can't see this on the camcorder screen.

**Dave Jones:** Okay, how does that look? Does that look any different now? Hmm. Now the ultimate optical tool I have here in the lab is my Mantis Elite microscope and I've mentioned this before that the internal camera in this thing sucks ass. It's just Oh, it's hopeless. I hate it. Um it's really an optical visual inspection bit of kit and so I've got my camcorder up into the hood of the you know, the actual viewing hood of this thing. So it's it's not the best, but there it is looking from the top and

**Dave Jones:** as you can see it actually looks pretty schmick. And there's another view of it there and you can see that there is like a really sharp angle on like the right-hand side here. It was left hand side before when we're viewing it from the other direction. Um and so yeah, but the one but on the left of the joint there, it is actually very smooth. So it's really hard to keep and get this in focus on camera.

**Dave Jones:** But yeah, it is actually completely smooth on one side and it doesn't move when I wiggle it on the top. All right, so how does it look under the Tagarno microscope? The Tagarno is just not as good as you can't beat the optical Mantis microscope, but I I actually got the camera working in the Mantis, but it's just it's garbage. It is so underexposed. It just looks black as the ace of spades. It's just absolutely terrible. Anyway, here's the joint under the Tagarno. So there it is. That's the

**Dave Jones:** one we're interested in and once again, if I wiggle the bottom, I am wiggling that. Okay? There is nothing transferring through to that other side. okay? But, so if I turn that light and that's the internal light. So, now if I get another external light and turn this down a bit and I take it around take it around like there there is a sharp contrast. But, unfortunately, to tilt it and get the same zoom, I'm going to have to lift my Takgano up. That might do it.

**Dave Jones:** There you go. Because it's all a function of distance. It's tricky cuz I've got my ATM on there. Hang on.

**Dave Jones:** You're better off having it higher up and then bringing the object up to it than not. Okay, so now my Takgano's high. All right, there we go. Yeah, see it's overexposed there, but hopefully you can see but that is shiny. I can actually under expose that. There you go. Can under expose that. There you go. Now you can actually see. Let me zoom in a bit more.

**Dave Jones:** Uh sorry, I've got a hand hold this just at like I'm at maximum zoom. It's 30 cm working distance. Now, you can see down in there you can see why you know, like under certain lights this would this would show up really bad. Um but as I said, there is no like if I wiggle that, it's doing absolutely nothing. So, that's at that angle.

**Dave Jones:** It's all about the angles. There you go. Look, on that side of it the joint actually looks I'll try and keep it a bit steadier. Trying to hold it in free air here. See? On that side it actually looks pretty good. So, yeah, I like there's there's nothing inherently wrong with that joint. I don't think. But, of course, I will just to be sure, I will actually reflow um that joint. But, yeah, you can see how hopefully that gives you an idea. And look, and it

**Dave Jones:** looks perfect from the top. If you were looking around with your digital, you know, microscope, even if you've got a kick-ass one like this uh Tagarno one, then like you would think that would be, you know, great. Like you might give it a little bit of an angle, but I can see this incredibly clearly and detailed under the Mantis microscope here. And um yeah, I'm sorry I can't It doesn't show up on camera. It just looks go- You have to look through these things in real

**Dave Jones:** life to actually like it just It's so bright and clear and crisp. And and I can tilt my head around and I can like it's a 3D microscope, so I can like move my head and look at the angles and stuff like that. And it looks okay. It does actually look okay. But, yeah, that is actually, believe it or not, that is I I believe that's a that's a good joint. Like you would you would certainly certainly I'd say resolder that as a matter of course. So,

**Dave Jones:** let's do that just to keep everyone happy. But, anyway, I hope you found that as an interesting um example of how light can potentially fool you into the Oh, that's definitely a dry joint when it's actually in most of in almost every case every repair almost every repair video actually I get somebody email me uh cuz they've watched it on their high-def telly and they go, "Oh, that joint's definitely dry." Um and it it's not. It's just a trick of shadows and lights and stuff like that. In this

**Dave Jones:** particular case, yeah, it doesn't look terrific at certain angles. And um but, certainly when I wiggle it, so it's got nothing to do with the wiggle wiggle wiggle, yeah. Um and so, I will just uh clean that and resolder it.

**Dave Jones:** Oh, we'll just heat that up a bit there. And now, I'll actually wick I'm just putting that on so I then I can wick it off. Let's just some of that away, shall we? And it's still not wiggle wiggle wiggle year in.

**Dave Jones:** And we will resolder that. Nice and fresh. There you go. That's a freshy. Look at that. Beautiful. Yeah, it's that lead-free rubbish. But anyway, thanks for those who pointed it out. I just wanted to show you that it's most likely wasn't that.

**Dave Jones:** So, yeah, there's a couple of other theories and stuff, but yeah, if it ain't busted, it's hard to fix it. And by putting the case on, it is actually getting very warm inside this thing. So, yeah, like I can put it inside like if you don't have a thermal chamber, if you just want stuff to heat up, you can stick it inside say a Styrofoam container or something. I have it You see me score those from the dumpster, the big Styrofoam containers. That's what I have those for. You can stick

**Dave Jones:** them in there. They do a pretty good job once you heat it, you know. Put a little port in the side for the cable, power it up, and it'll heat up inside cuz it's an insulator. The heat can't radiate out. So, yeah, of course you put a temperature probe in there to make sure you're not going to fry the thing, but yeah, you can stress products that way or something, but yeah, I don't know. At this stage, I'm just running it for like a few days to see how it goes

**Dave Jones:** and stuff, but I I just cannot fail it. It's just not failing. So, anyway, hope you found it interesting. Catch you next time.
