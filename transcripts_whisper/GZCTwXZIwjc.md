---
video_id: GZCTwXZIwjc
title: EEVblog #1177 - Ericsson PABX Teardown
url: https://www.youtube.com/watch?v=GZCTwXZIwjc
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 25, "2": 54, "3": 78, "4": 96, "5": 112, "6": 132, "7": 149, "8": 168, "9": 183, "10": 199, "11": 218, "12": 243, "13": 262, "14": 284, "15": 307, "16": 314, "17": 337, "18": 356, "19": 381, "20": 400, "21": 416, "22": 440, "23": 461, "24": 477, "25": 500, "26": 522, "27": 534, "28": 554, "29": 582, "30": 603, "31": 617, "32": 633, "33": 648, "34": 665, "35": 685, "36": 702, "37": 715, "38": 735, "39": 752, "40": 770, "41": 787, "42": 806, "43": 818, "44": 843, "45": 858, "46": 880, "47": 896, "48": 918, "49": 936, "50": 952, "51": 966, "52": 981, "53": 1001, "54": 1017, "55": 1037}
---

**Dave Jones:** Whoa, unfortunately the magic smoke has escaped. Whoa, something went snap, crackle and pop. Damn it. Hi, we've got a quick teardown today because the more interesting teardown I was going to do actually blew up on me and released the magic smoke. And if you can hear some fan drone in the background, that's my filter in the lab furiously trying to get all the crap fumes out of here.

**Dave Jones:** So anyway, I thought I'd, this is my emergency backup teardown. It's one of these IPEX LG Ericsson, like phone call, telecom centers, all this stuff was left over in this office when I moved in here. If you saw the tour of that, it's the IPEX system and they've got a whole bunch of these, you know, these phony things and the switchy telecoms.

**Dave Jones:** The control thing with all the outputs and whatnot. I thought we'd give this a teardown, see what's what. So what we've got with this system is the IPEX and Ericsson, LG brand, IPEX EMG 80. So it's like a PABX call center, telephone, you know, integrated system for, you know, you have a big call center with, you know, 50 or 100 people.

**Dave Jones:** And they all have their individual phones or even like small teams of like, you know, five or something like that. That can all, you know, transfer calls and stuff internally. Then we've got a bunch of headsets and I posted, back when I posted that video, a lot of the, a lot of people said these are actually a really good brand.

**Dave Jones:** A Jabra Bluetooth, you can probably look, it's still charging there. Even though nothing's plugged in, so I don't know what the deal is there. Anyway, a Bluetooth wireless headset. So this is obviously the charging station, so at the end of the day, you put your,

**Dave Jones:** put your wireless headset back on the charging system and then you, at the start of the day when you come in, bingo. You've got this high quality Bluetooth-y, comfortable headset thing with no wires to dangle around. And so this is the telephone here and it's got, you know, your usual buttons, but it's got a trans-PGM, no idea what that is.

**Dave Jones:** Speed and do not disturb, oh okay. Callback, mute, and I did, you know, I'm sure it's got tons of features that you have to figure out how to use. Also all sorts of programmable buttons. Hi Paula and Joanne and Mark and Tony and Kath and Robert, thank you very much.

**Dave Jones:** Voicemail, you know, and all that sort of jazz. But it's got this Jabra, like a receiver, transceiver actually hooked over the, over the thing. Now the speaker's behind there and it looks like, it's, it's really weird. I don't, don't really know how that works.

**Dave Jones:** It looks like that comes up somehow. But I'm not sure, not sure what the deal is. I've never used one of these, I have no idea. But it's like, it, like, it looks like it's a, like, designed to clip over the existing unit.

**Dave Jones:** So that's, it's rather fascinating. Anyway, it's got a wire that just buggers off to the back of here. It's got a mains plug pack, it's got auxiliary and then you plug the headset and whatnot in there so it can presumably tap into that.

**Dave Jones:** And that looks like a channel selector perhaps. Now these phones here are not designed for your regular, you know, switched phone line. Even though it's got like, you know, line in here and the, like the handset going off to here and the headset going off to here.

**Dave Jones:** You can't just plug this into your standard phone line 'cause watch what happens if I do. It's funny. Here we go, watch this. . . I don't know if you can hear that, but snap, crackle, pop. . That's great. . That's brilliant. .

**Dave Jones:** That's not a happy camper. Yeah, so it looks like this puppy was not happy with the 40, 48 volts on the telephone line. So let's, let's crack this open. Here we go. Have I missed something? What's that little, some sort of little programming?

**Dave Jones:** Ah, forgot a screw. There we go. Whip that out. We should be in like Flynn. There you go. So we've got two board solution here. So that's your line isolation, but as I said, not designed for the public switched telephone network. Designed to, you know, a proprietary thing designed to go over to the specific PABX.

**Dave Jones:** So. And a custom bit of silicon. What is that? No idea, but it'd be a custom ASIC, that's for sure. The whole bunch of memory next to it and not much else, really. There's our, there's our off hook switch. That's a nice, that's a nice solution.

**Dave Jones:** I really like that. That looks like that'll last a long time. Wow. Yep. I'm impressed by that. looks like they got a Mylar cone. Oh, there it is. Yeah, like some sort of Mylar-y cone. Speaker, it's got a seal, and that's really quite nice.

**Dave Jones:** That's a really nice professional solution. I like that. But you know, as you'd expect, these things aren't cheap. They're not built down to a price. In fact, you can see the rubber seal all the way around there, and that would mate up with the back of that.

**Dave Jones:** There you go, the back port. So that's a completely sealed enclosure. They've paid attention to the audio to get decent quality out of that, so that's really nice. I like that. That feels like there's a fair bit of travel in that, baby. I like that.

**Dave Jones:** I wonder who makes it. And they've even thought about how... How to get the cable through to penetrate down like that. They've left a little cutout in the black plastic, and they've put little notches in there that those wires can go in like that, and still form a great seal around there.

**Dave Jones:** Wow. Somebody took pride in that. We've just got a whole bunch of trennies around there, and some resistors, and a 74574, is it? 74 series. So that's just doing all the matrix switching for the keypad. And whatnot. So, that's it. Nothing else in there.

**Dave Jones:** It's pretty simple. Except for the ASIC, of course, which I'm sure is quite complex. Okay, we'll have a quick look inside this Jabra headset. The outer thing just plugs on there, because you can just get replacements for that, because they wear out and get all yucky.

**Dave Jones:** And that's about all I expected. Big single-chip solution up there. We've got the Bluetooth receiver here. You can see that buggering off there. Dual antenna there, buggering off along the sides. And I can't read that one from here. What's that? And that's a Dialog semiconductor part, which is actually formerly a Cytel.

**Dave Jones:** And here's the datasheet. Confidential. None of that NDA rubbish. We've got the good stuff here. And it's designed single-chip solution exactly for these decked applications. So, yeah, that's all she wrote. And, as I said, the transceiver. You can see a little itty-bitty tactile switch down there.

**Dave Jones:** That turns your power off and on. And that comes from that little bump there, which did have this little red cap on it. Yeah, not a huge amount in that, but, you know, some nice engineering's gone into that. So this transceiver thing seems to do absolutely nothing.

**Dave Jones:** It's just stuck on with double-sided tape. Well, it doesn't do nothing. Stuck on with double-sided tape. There's nothing in there. Yeah, I don't know what that slider is supposed to do. Got no clue. Like, what? Why? And I don't know what this arm here is.

**Dave Jones:** Does that detect, like, the pickup when you're off-hook? And what does that positive and negative thing do? There's different little indents in there. I guess I'd have to RTFM. Oh, there you go. It's a motorized flipper. Flippy doodad for, that's the technical term, for lifting the handset off the hook up here.

**Dave Jones:** So it's compatible with any phone on the market. So if you want to, like, it's got a button on the front so you can maybe do it manually. Or if you want to, I presume, maybe you can push the side of your headset or whatever,

**Dave Jones:** and that will instruct this to then, it'll just spin around and that'll lift that up. So it lifts the handset up and goes off-hook like that. So. And then, like, answers the call. Like, so it's compatible with any unit on the market. Isn't that neat?

**Dave Jones:** Hmm. Ooh, designed and engineered in Denmark. Manufactured in China, of course. I had all my Danish viewers. And there you go. There's the matching transceiver with the matching dialog Cytel chipset. Not much doing. Got some line interface stuff. There's a little PCB. Mount encoder there for the, that's for the channel select knob on the back.

**Dave Jones:** Got our dual diversity antenna there. And that's a, that's a nice bit of engineering. It all just, like, clips together in one piece of plastic. It's actually, it's very impressive envelope design. I love that. And that looks like it has some, like, sort of light pipes there, integrated.

**Dave Jones:** And it looks like we've got a little extension. It's got a little extender bars down there from the buttons on the front. And that's the matching channel select. And that all just comes apart in, like, those pieces like that. It really is pretty terrific.

**Dave Jones:** I'm impressed by that. A couple of relays for switching over there. And Bob's your uncle. See, something like that is, like, really quite complex and difficult to design without, you know, modern CAD tools that you can actually do mechanical DRC on that sort of stuff.

**Dave Jones:** Because it's all got the side clips on the side and everything else. And everything has to fit in just hunky-dory like that. But that's, yeah, that's pretty nice. It just goes together like that. It's beautiful. Access to our external test pads down here.

**Dave Jones:** Fantastic. And then that just clips in there like that. And it all goes together. Absolutely terrific. Okay, let's have a look inside this thing. And AC input, external battery, of course, for when the power fails. You still want to keep up and running for a little bit.

**Dave Jones:** At least. And on the other side, anything? Oh, yeah. Look, HDMI. But they're not HDMI. They just use the HDMI connectors. Left and right. I don't know what they're for. I don't think they're external monitors. Little RS-232. You've got your LAN interface as well.

**Dave Jones:** USB. What else have we got? Relay, paging relay and stuff like that. So you can put it up to, you know, old-fashioned paging systems. And a whole bunch. A whole bunch of RJ-11s. That's it. I suspect there's going to be a huge amount of wasted space in here.

**Dave Jones:** It just flips up. That's it. Two screws on the back. Oh, Bob's your uncle. We're in. Got a light pipe that goes down to, through to the front. Just to light up the bar, wank, wank, under the, that no one's going to see it.

**Dave Jones:** Because it's installed in the, in the comms rack or whatever. That's just ridiculous, but there you go. Isn't that neat and tidy, though? It's a lot of engineering. Engineering that goes into one of these, though. I can see a lattice part, and I have a custom ASIC jobby down here, not huge, big, quite

**Dave Jones:** a flat pack over there. That's enormous. And of course your line interface board and expansion and a second, you could put a second one on here. That's why they've got that extender up there and daisy chain. So I come with a base number of channels and then you add, you know, an extra four, yeah,

**Dave Jones:** four channels or whatever for each one. Check out this board, there's actually a ton of stuff missing up the top. Well, they've got an extra two, yeah, looks like they've got only half the channels populated. You can see that they're all duplicated, and these ones are duplicated here.

**Dave Jones:** You can actually see the thermal pads under these. These must be switching regulators. You can tell by the big ass inductors and the caps around them. That's a, and you know, it looks like they've got some current measurement shunts and stuff or something like that.

**Dave Jones:** And yeah, so they're, they're big ass switching regulators. You've got your line interface transformers. Got some line protection down there. They look pretty chunky, look at the thickness of those. Whoa, neat. But why that's only half populated when it's, oh yeah, no, you can fit another four channels

**Dave Jones:** on there. Okay, that's why. But here you've only got your two, so it's interesting. And then a lattice semiconductor job up there. programmable. But yeah, there's not much doing on that. A couple of passives on the back. That's about all she wrote. LG, Nortel, there you go.

**Dave Jones:** They've rolled their own custom silicon for this, Rev B, on there. So, yeah. Wow. Look at all the tans. That's incredible. I haven't seen that many tantalums. Somebody had fun. That's just insane. Anyway, we've got some firmware down here. And by the way, that's actually

**Dave Jones:** that looks like a programmed part as well. Well, I don't know if that's, well, would it contain like internal flash or whether it'd be external? I'm not sure, but it's got a software sticker on it. But anyway, got some more flash down here.

**Dave Jones:** We've got a lattice programmable jobby down in there. What is that? A little FPGA. And that one looks like, that's a free scale, is it? M83. M83-61G. So I suspect that's going to be some sort of applications processor. Got some memory tied into that.

**Dave Jones:** So there's not a huge amount else. Of course, we had that, all the line interface stuff that we saw before also on this board. So it's got a set number of channels in the base unit. But I, like, is this like the voice processor or whatever?

**Dave Jones:** I don't know if this is like an analog or a digital. I presume it's like a digital system these days. Some miscellaneous housekeeping with the lattice there. And some sort of applications processor for all your Ethernet goodness and all that other internet or whatever

**Dave Jones:** LAN connectivity stuff. But that's about all she wrote. They're like little custom transformers. That goes up to the relay alarm output up there. That's fascinating. Anyway, battery backup. And not much else doing. Still don't know what this thing does with these HDMI outputs.

**Dave Jones:** I don't think they're actually video. They're just using the connector for something else. Like and look at that power supply. And this is all passive, of course. There's no fan in this thing. Hence all the lots of grills and slots all the way around.

**Dave Jones:** It's just getting the airflow. Generally, you're going to have like some sort of airflow in the cabinet from the comms cabinet from, you know, other gear and stuff like that. But yeah, generally, that looks really schmick, well laid out. And I love the

**Dave Jones:** big plastic cage that goes over the top of that. Beautiful. Nice big ferrite on there, too. So there you go. That's just a quick look at this Ericsson LG IPEX PABX things. Oh, little board. Don't know what that does. Some option you pay a fortune for, I'm sure.

**Dave Jones:** Why they couldn't include it, I don't know. Anyway, yeah, you've got to option these babies up. Cool. You know, purpose design specific bits of kit. They don't sell, you know, they're not really consumer type things. They're, you know, designed for professional office environments.

**Dave Jones:** Don't know how much they cost, but I'm sure they're not cheap. And they're designed and engineered very well. There doesn't seem to be any cost cutting at all inside these things. Engineered remarkably well. And, of course, they all roll their own custom ASICs, as a lot of these telecom

**Dave Jones:** companies do, which we've seen on similar sort of boards in the mailbag and stuff like that. Really remarkable. And a lot of effort's gone into designing and manufacturing these systems. So if you actually work at a company designing these sorts of telecoms, niche telecom stuff, please let us know in the

**Dave Jones:** comments down below. Anyway, hope you enjoyed it. Catch you next time. Captions by GetTranscribed.com
