---
video_id: DizSMQSLuJc
title: EEVblog #987 - Keysight U1272A Multimeter EMC Followup
url: https://www.youtube.com/watch?v=DizSMQSLuJc
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 31, "3": 47, "4": 62, "5": 82, "6": 101, "7": 124, "8": 139, "9": 152, "10": 174, "11": 192, "12": 209, "13": 226, "14": 251, "15": 277, "16": 298, "17": 316, "18": 333, "19": 350, "20": 369, "21": 384, "22": 404, "23": 426, "24": 447, "25": 484, "26": 506, "27": 526, "28": 554, "29": 579, "30": 599, "31": 613, "32": 627, "33": 642, "34": 671, "35": 694, "36": 714, "37": 733, "38": 752, "39": 771, "40": 787, "41": 806, "42": 832, "43": 851, "44": 866, "45": 884, "46": 896, "47": 907, "48": 927, "49": 946, "50": 960, "51": 971, "52": 991, "53": 1009, "54": 1025, "55": 1040, "56": 1060, "57": 1079, "58": 1098, "59": 1116, "60": 1134, "61": 1153, "62": 1169, "63": 1183, "64": 1204, "65": 1220, "66": 1249, "67": 1265, "68": 1285, "69": 1306, "70": 1320, "71": 1337, "72": 1360, "73": 1375, "74": 1394, "75": 1413, "76": 1432, "77": 1458}
---

**Dave Jones:** Hi, back in October last year we took a look at the Keysight U1272A multimeter and a big issue it had with both conducted and coupled RFI emissions into it. And click up here if you, this little card up here if you haven't seen that video,

**Dave Jones:** it goes into all the details, compares a lot of other different meters. And it was a serious issue and Keysight took it seriously. They didn't quite recall the thing, but they basically said, yep, anyone who's got one of these, we will fix the problem and we'll replace it for you.

**Dave Jones:** And sure enough, they did. I believe, I think like everyone's like actually received a replacement now or whatever. And there's massive, you know, dozens and dozens of pages on the EEVblog forum talking about the issue. But they came to the party, they owned up to it and they fixed the issue

**Dave Jones:** and we've got a new multimeter to check out. Just a quick recap here, if you take a function gen like this and do a 10 MHz sine wave, square waves, worse, you know, like a few volts peak-to-peak, it starts to happen, 10 volts peak-to-peak, it goes off the scale

**Dave Jones:** and you've got your banana plugs like this, nothing else plugged in here, nothing up my sleeve and I just plug this in to the amps jack and it detects that it's on amps and boom, look at this. I mean negative 4 amps and look at this, it has some spooky action at a distance.

**Dave Jones:** Look at that, if I put my hand around that, put my hand on top, it's gone-ski. So that's conducted mode coupling into the multimeter. It's flooding the ADC with crap and it just cannot handle it. And that does exactly the same thing coupling into the common mode jack as well.

**Dave Jones:** So we'll wind that wick up to 10 volts peak-to-peak and also if you just drape the wire around it like that, it's also susceptible to just a coupled, a capacitively coupled issue like that, not just the conducted mode issue. Anyway, they've sent a brand spanking new one which has the fix.

**Dave Jones:** So let's first test that they've fixed the problem. It won't be entirely eliminated, I wouldn't expect, because this happens to various degrees on various multimeters. It's just that this meter was like orders of magnitude worse than any other meter that I actually tested.

**Dave Jones:** So it might, you know, we just want it to be sort of like low, not just extreme like we saw there, amps and amps. So let's try it out and then we'll crack it open and compare the two and see what their fix is.

**Dave Jones:** And here's the brand spanking new one with Keysight, none of that Agilent rubbish on there. Oh, come on, we get to peel. Jeez, that's the stickiest thing I've ever seen. Hey, have they changed the LCD? I think there's... I, it, like the background is, it, they have changed,

**Dave Jones:** I mean mine's a really old, my original one's one of the original models and they've like completely changed that, but yeah, I, oh, this one's probably a bit better, maybe the new one. Anyway, this ain't a review, let's check it out. Serial numbers for those playing along at home,

**Dave Jones:** I'm not sure what serial number it started at or I have no idea what, this is the old one, no idea what MSSB means or whatever, but anyway, any new one you buy, I'm pretty sure will have this fix in it. Anything in stock should be fixed.

**Dave Jones:** Okay, let's just turn that to a square wave, make it pretty extreme, 10 megahertz, 10 volts peak to peak, here's the original one, wah, wah, wah, wah, it's just gonna overflow like that. Let's try the new one, oh, why do we have, how do you have

**Dave Jones:** a low pass filter in DC mode? What? Okay, they've enabled, I mean, it does have a low pass filter built in, but they've enabled that, can we disable that? What the, look, that vanishes on AC, no low pass filter, no low pass filter on AC plus DC,

**Dave Jones:** and just DC percent, no, they're forcing, they're forcing the low pass filter on, is that an extra software trick in there to actually get rid of the noise? Anyway, here we go. Let's plug it in. Ta-da! Completely gone. Completely gone. Plug it into the common jack,

**Dave Jones:** completely gone. Okay, they have absolutely, thoroughly nailed that. But can we disable the low pass filter? Maybe not. And it's fine on milliamps as well, no wackers, and microamps, yep. And of course you dangle it around the outside, there's absolutely nothing, there's no more spooky action to the difference,

**Dave Jones:** and that's on the microamp range, so yeah, that's, yep, that's basically nailed, no worries. So if we go into the filter option here, we can actually switch the filter off. Hopefully, that's the plan. It's got a reset. Ta-da! Now we're in like Flynn,

**Dave Jones:** and it's showing up. I think they did that by default, so that, oh no, hang on, no, no, it's all good. Why they're enabling that by default, I don't know. Maybe they just wanted it to be absolute, we've got a little residual thing there,

**Dave Jones:** doesn't matter, but maybe they just wanted to absolutely kill the issue, they didn't want anyone to complain, so they just whacked in a bit of the optional low pass filter in there by default. So, anyway, either way, it wouldn't have mattered. It's fixed.

**Dave Jones:** And for those wondering, no, they haven't changed anything with the internal shielding at all, so obviously the external coupling problem was not a shielding, it was not solved by a shielding issue, it would have been solved by ferrite beads on the board and on the supply

**Dave Jones:** and on the inputs and stuff like that. Alright, let's have a look under the Tigano microscope here. On the right-hand side is the new model that's fixed. You'll notice it doesn't have the populated programming header here, whereas the old one does. I'm not exactly sure why,

**Dave Jones:** but if we compare the two, I get... off the bat, I can't see a thing, except for down here, obviously they've changed the board from revision 4 to revision 6. I'm not sure if there was ever a revision 5, but it looks like somebody didn't get the memo,

**Dave Jones:** just a pro tip here, Keysight, if you're going to change the revision of your board, update your branding. How many years has it been since they changed to Keysight now? Oops, somebody didn't get the memo. Anyway, look, I cannot see a track difference, I cannot see

**Dave Jones:** a component difference, I can't see anything at all, like all the vias are in the same spot. Wow, obviously, you know, I mean, I'm shooting this live, in quote marks, so it's hard to, you know, it's hard to really tell, unless I like do a photo comparison.

**Dave Jones:** I've got some high res photos over on evblog.com, so I might do a edit here where I actually merge the two photos or something like that and see the difference. I can't see anything. I mean, I'd probably expect something around here, which is all the current

**Dave Jones:** measurement stuff, whereas all this is all your high voltage input stuff. So that, I can't see a thing. Can you spot anything? Where's Wally? Beulah, Beulah, Beulah. And if you're wondering about all the various, like, missing components and things like that, that is very common

**Dave Jones:** in multimeter designs like this, to put in extra components for various things and then not populate them, you know, ones in there like that. So nothing doing there, and because Keysight have had, and Slash Agilent have had problems with the soldering before on this, they had a real batch problem

**Dave Jones:** on this series meter, the 1270 series of soldering, of course, now looks spot-on. Is that a little bit, is that a little bit of how you're doing? Let me... Hang on. Ah, that value there's changed. Look, 3300, 2401, that has changed. That's interesting.

**Dave Jones:** Is that like hand-soldered? Look, you can see some flux residue on there. Somebody's had a go at that. Somebody's had a go at that puppy. So... Ah, R55 there. So I've actually measured that in circuit, and that one is 330 ohms, sure enough, and this one over here

**Dave Jones:** is its marked value of 2.4k, 240, and then the one on the end means 10, so 2400 ohms, 2.4k. And they are bang on those values, so they've significantly increased that value, and they've done it after the production stage, after that board's been assembled.

**Dave Jones:** So if they just take an existing stock, and they've done a rework on that, I mean, you know, it's as plain as day. That's been redone. Look at all the beautiful fillets, solder fillets everywhere else. Absolutely gorgeous. And then you've got this little hack in

**Dave Jones:** there. So I'm going to have a look around for more hacks, but maybe that's the only one. But I expect them to redesign this board, re-layout, to put in some ferrite beads at least, in series, to, you know, that's the most common technique to stop

**Dave Jones:** RFI getting into conducted mode. Stuff getting into chips. You put them on the power lines and other stuff. So, you know, ADC inputs maybe, and stuff like that. But not seeing it on the top side of the board anyway. And if we go to

**Dave Jones:** the bottom side of the board here, once again, I can't see anything at all. That looks absolutely identical. Every trace, every via, every component. Wow. Nothing. They've added no extra components. Nothing down in the bottom side protection. I wouldn't have expected to see anything down there anyway.

**Dave Jones:** You were probably screaming at me. Look at this. This is the new board. There we go. BD4, BD5 beads. There are ferrite RF beads there. And, note, they're beautiful fillets on all the other parts around here. Reflow soldered. These, somebody's actually taken to these and hacked them.

**Dave Jones:** So, by hack them, I mean resolder them. And here they are, but here's the original REV4. Okay? So we've got the three RF beads. So it's not like they've added these. They have not added these at all. And it looks like they're, so, well,

**Dave Jones:** they've changed them. They've probably changed the value and type, but you'll notice that the beads are between grounds here. So they're between, like there's the little spring which buggers off to the shielding on the top, but then that separates the two grounds there and

**Dave Jones:** there. And once again, that is coming from the 11 amp fuse input there. So that's interesting. So that's, you know, that's where you'd expect to find them, but they have obviously thought about this before in the original design, and they put them in there, but maybe they

**Dave Jones:** were the wrong value. And they were resonating at that 13 megahertz or whatever, combined with the ground plane and the capacitance of the planes, and you know, like a complex system thing which we won't go into because, well, without knowing all that, without having

**Dave Jones:** all the details, you wouldn't be able to do that. And likewise, we've got ferrite beads on the voltage input over here, and they're still there as well. So they haven't changed those, but of course we're only talking about the current ranges here. So they've obviously just

**Dave Jones:** taken the existing Rev6 design, I would say, unless there's some other minor change we can't see somewhere. But it's certainly not like they've added in any ferrite beads. They've just changed them. So I would say possibly that's all there is to it. They've simply chosen the wrong

**Dave Jones:** value there of RF ferrite bead in the ground, separating the main current input ground with the system ground. And that was enough to cause both conducted and coupling mode problems. Wow, let that be a lesson to you when you, you know, you try and do the right

**Dave Jones:** thing by designing in these ferrite beads, but hey, you can get it wrong. It's the same with bypass capacitors too. For example, I won't go into details, I've done a video on why and how to select bypass, why you put multiple bypass capacitors, but in theory and also in

**Dave Jones:** practice, you know, it does happen occasionally that you, you know, you throw in all these bypass capacitors and they just happen to resonate with the inductance of the traces you're doing and cause a problem at a specific, you know, clock frequency or something like

**Dave Jones:** that. You know, it's not very common at all, but it can happen. And likewise, something's happened with these beads, I reckon, combined with maybe there's a couple of capacitance values different somewhere along the line as well, they might have, you know, figured that out.

**Dave Jones:** There would have been a lot of engineering which went into figuring this out. It would not have been easy at all, trust me. If it was the value of those beads, I can picture, that's why it probably took them so long to, you know,

**Dave Jones:** to reply to the forum and do other things and get the fix in. That would have been a real pain in the butt. You would have followed lots of red herrings down rabbit holes there, let me tell you. Would have been absolutely hideous.

**Dave Jones:** But yeah, maybe just change the value of the beads, nothing changed. I mean, that one's, you know, reflowed. So they've obviously taken existing production boards and just changed a few values. That R55 that we saw before is changed up here. And well, they haven't changed, given that

**Dave Jones:** they only changed those after the fact. So there you go, something subtle was happening in this poor meter and they didn't, they didn't find it during testing or anything else. But that is interesting. I totally did not expect them just to change a couple of values

**Dave Jones:** there and use the existing design. At least that's what it seems to, whether or not they actually did upgrade to the Rev6 board here, and then they thought they had it fixed. And then they went, oh no, we still, you know, but we've made

**Dave Jones:** these boards, you know, we've made 10,000 of them or something. And then they thought, oh no, we need to tweak it a bit more. And they've changed a couple of extra values in there after the fact, maybe to improve it or make it better, or

**Dave Jones:** maybe they found another issue after testing. We just don't know until, unless Keysight actually come to the party and someone from engineering who investigated this come to the party and share the whole story. Because it'd be really interesting. I would love for Keysight, for, you know, the engineer or

**Dave Jones:** engineers who, you know, worked on finding this problem. You know, look, there's nothing embarrassing about it. Issues happen with multimeters. I'm designing my own multimeter. We've had no end of issues with it, and all sorts of stuff. And this U1270 series meter has

**Dave Jones:** had no shortage of issues either over the years. Firmware, production, soldering, EMI issue, and other stuff. And, you know, it happens. And we, the technical customer, understand that. You know, as long as you're honest. And we would love really for you to come.

**Dave Jones:** Oh, I thought I saw a difference. We would love for them to come out and let us know, do a video on it. You know, if you want to do a Skype interview or something, I'm always open to doing that. Because that would be

**Dave Jones:** fascinating, about what went into fixing that. Now if we look a bit closer at these, they actually appear to be like a thin film resistor. Just like up there. And that is, it looks more like a square than a zero. But, if you have a look over

**Dave Jones:** here, we've got the exact same part. Basically, so they're populated where R88 is supposed to be. So they're, I'm pretty sure they're identical parts. So that, for all the world, is a zero ohm resistor. It is not an RF bead. I mean, the beads look,

**Dave Jones:** they typically look different. They might, you know, like grey type one like that would be fairly typical. And they might have some markings on them indicating their, their resistance in quote marks at frequency. Like, you know, 200 ohms or something like that. Oh yeah, there's the

**Dave Jones:** one next to it. So, just zero ohm resistors. So, it's if, it's as if they've designed in those RF beads, because you can tell the intention of the designer with the silkscreen on there. It was definitely bead. They went, oh okay, it'll be a good

**Dave Jones:** idea if we just put an RF bead between, or in this case, two in series by the looks of it, between these two grounds here. But they've come a gutser. They've completely come a gutser. And they've went, oops, that's resonating with the ground

**Dave Jones:** capacitance or some other stray capacitance in the circuit or some other, you know, coupling capacitance or whatever. And they've gone, let's just take it out. So, they've just shorted out those two beads. Amazing. Ooh, I love the MELF resistor. Here you go. For all you

**Dave Jones:** MELF fanboys. Oh, look at that. Beautiful. So, what happens if we take our old one here and simply short out both of these? You could physically remove them. You could actually short them out. But then, if you put in a long wire in there, for

**Dave Jones:** example, to just like a mod wire or something, unless it's like low impedance, because that can act as an inductor in its own right. So, probably better to put, you know, proper surface mount zero ohm resistors in there. Not that, you know, it

**Dave Jones:** would still probably work. But, you know, in theory, yeah, just be careful. You might add a little bit of inductance in there. But just changing that, changing these from a proper RF bead to, which is basically an inductor really, to just, you know, short it out should do the trick.

**Dave Jones:** And yes, we've got the other resistor value up here. Where is it? Up here somewhere. Changed, but that might be to do with something else. So, it may not have anything to do with this RFI problem at all. So, I'm going to rip those out,

**Dave Jones:** short them out. I bet you the problem goes away. When in doubt, whip it out. And we'll whack those in there. No worries. And, hello? Hang on, I haven't plugged in anything yet. We've got a residual. It's on DC. Yeah, it looks like we've got a

**Dave Jones:** little offset there. So, maybe the board might still be a bit warm, or I couldn't see how having some beads in there would be causing some sort of DC offset there. So, that may come down. Don't, nothing to see there. Anyway, what we want to see,

**Dave Jones:** we've got our 10 megahertz, we've got our square wave, 10 volts peak-to-peak. Let's whack it in. And, nah. Hey, but it's different. Hello? Ooh, still got the spooky action at a distance. Ooh, use the force, Luke. You can see that this has changed

**Dave Jones:** dramatically. It's still there, okay, but drastically, drastically reduced. I mean, we were getting like full-scale stuff before. So, that, that has really made a hell of a difference. So, there's definitely something huge to do with those ground beads that go into the system ground.

**Dave Jones:** Wow! Hey! And, that offset does seem to be changing, going down by the way. So, yeah, I would say that was just a, you know, the board is still warm thing. So, nothing to see there. And, we'll just pop that one out too.

**Dave Jones:** There we go. And, 2.4k, that'll do nicely. It's an 0603, she'll be right. By the way, you can pick up these resistor kits on eBay and Capacitor Kits and everything else for bugger all. Like, so definitely get some of these for your kit.

**Dave Jones:** They're very handy. Alright, we've got it with the 2.4k resistor in there now, and the zero-ohm resistors. So, let's give it a burl. Yeah, it's, nah, is it the same as before? I can still use the force. And, yeah, it's still there. So, obviously, there is something

**Dave Jones:** else going on there. Like, there's no coupling at all. So, it's drastically improved. You know, I would say that was fine. I mean, if that was the fix, then I think other meters are like that, you know, of that order as well. So, I wouldn't be

**Dave Jones:** too concerned with direct coupling like that. Like, because there's, so, you know, it's like, direct coupling is hard to stop. But, yeah, that's fixed. That, and I haven't even turned, like, the low-pass filter on. So, I would even call that a fix. But, obviously, they've tweaked

**Dave Jones:** something else, I think. Just a tad, perhaps. Alright, let's try it again with the low-pass filter on. Yeah, see, whereas the other one gave, you know, diddly-squat there. So, that's, yeah, so they've made some other little minor changes in there. Probably tweaks and capacitances or

**Dave Jones:** something like that. Unless there's some other mod on the board, some other change and maybe a track layout change that I haven't seen yet. But, there you have it. The main culprit was the RFI beads in there on the ground plane. Oops! Seemed

**Dave Jones:** like a good idea at the time. Anyway, that's it. I hope you found it interesting. If you did, please give it a big thumbs up. No, that's my magnified thumb. Anyway, one of those fun things. And discuss it down below. Catch you next time.

**Dave Jones:** you
