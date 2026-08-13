---
video_id: _GThm9RX_YM
title: Just soldering a DIP header onto a Raspberry Pi Compute Module
url: https://www.youtube.com/watch?v=_GThm9RX_YM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 37, "3": 53, "4": 69, "5": 85, "6": 105, "7": 125, "8": 141, "9": 157, "10": 173, "11": 189, "12": 209, "13": 225, "14": 241, "15": 273, "16": 294, "17": 310, "18": 338, "19": 376, "20": 401, "21": 417, "22": 449, "23": 469, "24": 494, "25": 514, "26": 550, "27": 579, "28": 599, "29": 624, "30": 648, "31": 668, "32": 692}
---

**Dave Jones:** Hi, just a quick video. Not much to see here, just a Raspberry Pi. I've got this Raspberry Pi 4 compute module, which I've had left over, and I just got a heatsink, top heatsink for it, and this little add-on board here, so if you haven't seen the new Raspberry

**Dave Jones:** 5, well, it's not new, isn't it? It's the 5 now, but anyway it's one of the newer ones that I've got. So it's the Raspberry because I've got lots of 3 Raspberry Pi 3s. So I've got this 4 compute module. I'm potentially going to run home assistant

**Dave Jones:** on this. I'm going to have a play around with it. Anyway, uses technology licensed from ProAnt AB. Okay, is that the antenna thing? Because the antenna's actually in there. That's why they have the, there you go, you can see it on the top there, that's why they have

**Dave Jones:** the cutout in the heatsink there. They've got a little coax as well if you want to use that for an external antenna, but there you go. Anyway, Raspberry 5 4 compute module. So they put the, so they've got the heatsink, I won't take it off, but there's

**Dave Jones:** thermal pads on the processor itself and on the DC to DC converter chip down here. Yeah, under there. So you can tell by the big Vs there that that's regularly quite grunty thermally. So that's a dead giveaway. I like the big test points on here, nice.

**Dave Jones:** So they must have a nice big production bed of nails. Tester? Sorry, there's a bit of smoke around here. Sort of smoke. I do have my well, a fume extractor on. Anyway, so I got this little adapter board, because the Raspberry, the compute module can't do much on its own.

**Dave Jones:** It's just got these high density PCB interconnects here. And we've got this little adapter board which has a USB or a C or a DC, is that a DC power jack or is that audio? I don't actually know. Anyway, it's got a micro SD slot and

**Dave Jones:** it's got a ethernet connector as well and a USB A and a HDMI, mini HDMI out. What does that switch do? I don't know. Boot. Okay, so it's some sort of boot switch. I don't know what happens now to this. I guess I'll find out.

**Dave Jones:** What else? Oh, we've got a little key. Push button, key. I guess I'll find out what that does. Anyway, what I'm going to do is just solder this connector in here, because it was supplied with this. And it's nicely color coded, so that's pretty groovy.

**Dave Jones:** I've got no instructions, so I've got to figure out which way around it goes, because it's not symmetrical here. So obviously the black ones are all your grounds, green is like I.O., blue is, I don't know, red is power, for example. So does it go in that way?

**Dave Jones:** It looks like it might, because you can see, don't have my yellow poker, you can see that those two pads there are joined, and that looks like it is power. So yep, I'd be happy to confirm that those two are power over there.

**Dave Jones:** So I think it goes that way around, and that one there is ground. So you can see that that's going through some ground fill stitching there, so that was absolutely correct. If you whack it around in this direction here, wah, black and green, that's not going to line up.

**Dave Jones:** Nothing lines up, and this is obviously going to your ground plane. So no, it obviously goes in like that. I don't plan on using this header for this application, but why not? Solder it in. Before I plug it in onto my heatsink board, it came

**Dave Jones:** with a fancy supply with it, so might as well use it, just in case. So I'm just going to solder this sucker, and that's all this video's about. So there you go, nothing more to see here. So let's get in there. They are annoyingly close

**Dave Jones:** actually. So, very annoyingly close there. But anyway, so what we'll do is we'll just solder. So the board's pretty flat, just put some extra weight on that. And boom! There we go. Oh, hello, hello. Why aren't you melting? It took a while. And the thing is, you will burn your metal a little bit,

**Dave Jones:** but, I should have mounted it on something, but I just want to whack in a couple of two opposite ends. No whackers. Alright. There we go, that's better. Maybe the tip wasn't at the right angle before. What have I got? Like a 2mm, 2.5mm chisel, or something like that?

**Dave Jones:** So that will hold it in place nicely. I'll get my vice stick, if I can this lab is in a constant state of flux. Ah, there it is. That's right in front of me, buried under a couple of boards. So, I'll get my

**Dave Jones:** vice stick in here, and just hold that in place. Unfortunately, it's not the best thing for this, but... Hello? That'll actually keep that ah, it doesn't really keep that in place, but eh, it's good enough. Keeps it off the mat, she'll be right.

**Dave Jones:** Alright. So, let's go solder, shall we? Oh, oh, oh, not happy with it. Not happy Jan. So I might actually get in this orientation like that. So, let's go, shall we? There we go, that's tacked in place. Take me a couple of joints to get into the

**Dave Jones:** swinger things. And I'm not looking at the board, I'm looking at my screen here. So, the eyes ain't what they used to be, but this is trivial of course. But the problem is, is that with the shiny light I've got from my, by

**Dave Jones:** filming this, I get, if I look, if I stare down at the joints, I actually get glare on the joints, and it's not good. So ideal, this is not the light, if I was hand soldering this without using the screen, yeah, if I wasn't recording it, I would not

**Dave Jones:** be using this, I'd have different lighting. So, it's all about, jeez, I'm not doing this very quick, am I? Ooh, hello, the flux was a bit funny there. There you go, oh, ooh, hello. Don't leave that there. What did I do there? Could have picked a smaller tip, but this was on here

**Dave Jones:** and it's good enough for Australia, so no wuckers. That tip is, I think it's worn out on one side. It's fine on the other side, but on this side it's not good. I've tried to tin it and it ain't taking. I've tried to scrape it, I don't know.

**Dave Jones:** It looks like it's just totally dead-ski, so might have to get a new tip. There you go. Alright. Yeah, I could like drag solder, try and drag solder this or something, but I enjoy doing it onesies, twosies, because it's quite therapeutic. Thank you very much.

**Dave Jones:** Yeah, the stick vise doesn't really hold it down terrifically. Because the pin header is protruding from the bottom, so it's not the best thing there. Oh, I copped a bit of Oh, fumes didn't go up. Didn't get sucked up by the weller there.

**Dave Jones:** I've got it on low-ish so it doesn't, so hopefully you don't hear it that much. That's the plan. Beautiful. Big ground one there. Hello. That's what your problem with your two-dimensional, soldering stuff under a two-dimensional screen, you don't get a feel for the 3D nature of it.

**Dave Jones:** Like going over pads, going over like pins and high components and things. So yeah, it's a disadvantage. I can't have that ball hanging off the side of the tip there. It's annoying. Again, that was the that was filming on the screen. Leave it in the comments if you're a

**Dave Jones:** screen user, or you do it under a microscope, or whether or not you do this by eye. Normally I'd do this by eye, but I thought I would just record it. I have to put up with the glaring light. I mean I could turn that off.

**Dave Jones:** There you go. That's a bit better. So, well, from my eyes anyway. I guess it may not look as nice. So there you go, that's pretty terrible murial. It'll do. It's good enough for Australia. And that's it. There you go. We have a

**Dave Jones:** one complete Raspberry Pi Compute Module Adaptery Board. I just got it on eBay. Cheap. There are quite a few sellers on eBay of this thing. So yeah, really cheap. So no problem. There you go. And the board-to-board interconnect. It's just going to mate on there like

**Dave Jones:** that. And it should go in like that. There you go. Whoa, look at that. Bob's your uncle. There you go. That's sweet. Now I'm going to power this thing up and try and install Home Assistant on it. I don't know what I'm going to do with Home Assistant, but I just want to have a fiddle with it.

**Dave Jones:** Maybe consolidate my solar into there. And because apparently you can get an external power supply and apparently you can get an Enphase plug-in for Home Assistant, or Solar Assistant, and then, no, you can get an Enphase plug-in for Solar Assistant, which I have to run on another Raspberry Pi 3

**Dave Jones:** and then I can use Home Assistant to combine the two solar assistants from my two different solar systems. So yeah, that's something like that. That's the plan. There you go. Simple. Catch you next time.
