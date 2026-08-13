---
video_id: I-9dGvk3BW8
title: TP-Link AX6000 Router Teardown
url: https://www.youtube.com/watch?v=I-9dGvk3BW8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 26, "2": 43, "3": 59, "4": 73, "5": 99, "6": 115, "7": 134, "8": 147, "9": 162, "10": 174, "11": 189, "12": 206, "13": 225, "14": 247, "15": 267, "16": 284, "17": 300, "18": 314, "19": 332, "20": 352, "21": 373, "22": 391, "23": 403, "24": 418, "25": 433, "26": 449, "27": 465, "28": 482}
---

**Dave Jones:** Hi, I've got this wanky-looking second-hand TP-Link AX6000 router. It's got 8 ports on it. It's pretty beasty. Let's have a look. It's got 8 gigabit Ethernet ports. It's got a 2.5 gig. It's got USB 3 and USB-C as well. Very handy. It's got a wanky LED light-up thing that spins around on the top.

**Dave Jones:** It's actually connected to the interwebs at the moment, so it's solid. Anyway, I got this cheap. This will be an upgrade to get some extra range. Look at all these wanky antennas on it. Jeez, look at this. So, apparently it's got, I don't know, all new super-whiz-bang-speed technology.

**Dave Jones:** All the gamer kiddies will know all about it. I know Jack all about it. But apparently it can do beamforming and stuff, so wherever your device is that's physically connected, it'll sort of, like, kinda-sorta beamform in that direction or something like that. Anyway, it's got all these whiz-bang antennas.

**Dave Jones:** So, we'll do a very quick teardown. One of the interesting things is that it didn't actually come with a plug pack, and I had trouble finding a 12-volt 4-amp minimum plug pack on here. So that's 48 watts. Why does a Wi-Fi router need 48 watts?

**Dave Jones:** That just seems, like, insane. So I thought I'd do a quick power consumption measurement, and I'm getting 12 watts there, near enough. Just at idle, when it's actually connected. You know, I've got my shoe phone actually connected to it. When I was running speedtest.net, that went up to just a smidge under 15 watts there.

**Dave Jones:** And I think maybe I briefed... Oh, there we go. It just jumped to 15. I don't know if you saw that. So, it has these little spikes, and I think I saw... Yeah, 13. There you go. I think I saw it actually go up to 19 at one point, but I don't know how this would draw 48 watts.

**Dave Jones:** So, I don't know. They need it for peak current or something? I don't know. Anyway, I did eventually find one, but yeah, it took some effort. So anyway, let's do a quick teardown. Well, there's the first teardown. There's the wanky LED. Some under the little light pipe-y thing here, the logo.

**Dave Jones:** So they've just got that as a translucent brick there. Sort of acts as kind of like a light spreader, light pipe-y. Not quite a light pipe-y, but just as a spreader. So it gives you a nice big even, even though there's not many LEDs in there.

**Dave Jones:** There's only like four a side. It does give you like a really good like solid sort of like flow-around effect. So that's pretty neat. They've just got a LED driver. I can't read that, but there you go. Got a couple of SO jobbies on the bottom side as well.

**Dave Jones:** And a little ribbon cable. Looks like we're going to have to get that out, because I think the whole front cover lifts off. And it's a real dog to get in there on these corners, but you're supposed to get in there. I think you're supposed to lift the four corners off,

**Dave Jones:** and this top cover's going to lift off, I think. And here we go. I think I got it. Sorry about the camera exposure, but when you have black... Oh, thing popped back in. Bastard. There we go. Got it. Yeah, black causes havoc with the cameras.

**Dave Jones:** Oh, there you go. Wow. Yeah, this is a power hog, alright. Look at the size of those heatsinks. There's no fan in the thing, so it requires, you know, this is relying on just the vents on the side, really. But unless you've got like air flow, you know,

**Dave Jones:** air cons on and there's movement going around, then yeah, nothing's going to happen. Yeah, two absolutely giant processors. There you go. There's a Broadcom jobbie over there. You can see flux around it. Has that had a little repair? Maybe? I can see some...

**Dave Jones:** I can see Rossmann loads of flux on there. Anyway, a couple of things that are completely unpopulated over here. And bloody black solder mask on the PCB as well. Anyway, so all the little coax is all running off to the antennas here. So yeah, little UFL connectors.

**Dave Jones:** Down on the board there. Nice. Can you read what that silver puppy down there is? I'm not sure, but anyway. Got a whole bunch of transformers along here. So they'd be handling two channels each. And that one there would be for the 2.5 gig internet input on the thing.

**Dave Jones:** But apart from that, jeez, I don't know. Do I have to get the board out? I'd love to show you under the heatsinks, but it is now currently, I think it's almost like 10 o'clock at night. And I've got to get home and take this home and plug it in.

**Dave Jones:** I thought we might be able to see something more interesting than that. A couple of little programming headers over there, have we? Or something. Anyway, I do really like the RFI cans they've got over the USB connectors there. They're really serious about this.

**Dave Jones:** And the little mini coax there. It's been held in with a little clip. I mean, this one's going through the heatsink there, so that's a bit how you're doing, but it keeps them in place. So, and that one there as well. So, nothing wrong with that.

**Dave Jones:** Not much in the way of power supply at all. Just got a couple of filter caps there. I thought that might have been a polyfuse for a second, but it's not. It looks like it's a Y-class cap, RFI cap in there, which is going over to the metal can.

**Dave Jones:** There you go, managed to undo a couple of coaxes. Aha, there is some switching converters. There you go, no worries, you can give away, of course. You've got your inductor there and a whole bunch of parallel caps there. Oh, I love how they've got the silk screen for all of these tiny little,

**Dave Jones:** oh my God, are they 0201s? They're absolutely tiny, Todd. Those bypass caps, oh, that's horrific. So I've obviously got two very dense BGAs under there. Looks like there's our oscillator down there. Yeah, you can tell that, that's a PLL in there. And we've got some memory, that'd be the flash, wouldn't it?

**Dave Jones:** And we've got a very nice shielded can, which looks to be soldered down, so I'm not getting that off. And then a whole bunch of miscellaneous power supply stuff there. And yeah, more over there for the USB stuff, and just through-hole stuff down the bottom.

**Dave Jones:** So there you go. And it's interesting to note that the heatsink is on top of the metal can, so it may not be, I don't know if that metal can's actually just a shield like around the outside of the die and the heatsink's directly on the die,

**Dave Jones:** because it'd be pretty poor to go through, you know, to have this sort of heatsink in with like a couple of extra, layers in there to get the heat through. So yeah, maybe it's just metal around the outside of that, but I won't know unless I got that heatsink off.

**Dave Jones:** Sorry, ain't going there. I wonder if this thing's expensive. There's a lot of, there's got to be lots of really expensive high-speed custom silicon inside this jobby, but anyway, if you do know the chips used in there, leave it in the comments down below.

**Dave Jones:** You know, I could like take off the heatsinks, but nah, I need to finish this up. So I'll put it back together, and there you go. Bob's your uncle. That's the TP-Link AX6000. Let us know in the comments down below. I know there's haters out there, and they'll go,

**Dave Jones:** oh, this is a piece of shit. Others will go, oh, it's fantastic. All the gamer kiddies will love it. And yeah, whatever. I got it for a nix. And it seems to work just fine. So yeah, catch you next time. Oh, and by the way,

**Dave Jones:** yeah, catch you next time. Oh, and they have designed the standoffs in the plastic so that it only goes on one direction. Nice attention to detail when you're doing your molding. Someone was thinking. The industrial designer who did the molding was talking to the PCB designer

**Dave Jones:** and the system designer. Nice.
