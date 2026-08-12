---
video_id: NiPJr1XNuPI
title: EEVblog #593 - HP35670A DSA Repair Part 4 - Thermal Testing
url: https://www.youtube.com/watch?v=NiPJr1XNuPI
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 24, "3": 39, "4": 50, "5": 65, "6": 80, "7": 96, "8": 108, "9": 123, "10": 148, "11": 164, "12": 176, "13": 200, "14": 211, "15": 221, "16": 236, "17": 248, "18": 258, "19": 274, "20": 291, "21": 300, "22": 311, "23": 326, "24": 337, "25": 350, "26": 360, "27": 374, "28": 382, "29": 395, "30": 404, "31": 419, "32": 426, "33": 438, "34": 449, "35": 458, "36": 470, "37": 480, "38": 490, "39": 499, "40": 508, "41": 529, "42": 541, "43": 559, "44": 568, "45": 576, "46": 586, "47": 600, "48": 621, "49": 630, "50": 652, "51": 672, "52": 685, "53": 698, "54": 711, "55": 723, "56": 750, "57": 764, "58": 778, "59": 791, "60": 805, "61": 816, "62": 833, "63": 842, "64": 855, "65": 870, "66": 878, "67": 890, "68": 901, "69": 914, "70": 924, "71": 938, "72": 956, "73": 969, "74": 983, "75": 993, "76": 1006, "77": 1026, "78": 1041, "79": 1057, "80": 1071, "81": 1085, "82": 1107, "83": 1117, "84": 1129, "85": 1147, "86": 1161, "87": 1175, "88": 1196, "89": 1208, "90": 1224}
---

**Dave Jones:** Hi. Welcome to part four of the HP 35670A dynamic signal analyzer repair video. And if you haven't seen the three previous videos, I'll link them in down below. Otherwise, hey, you're not following the story, may not make much sense.

**Dave Jones:** But anyway, this has been a real pain in the ass. There's been lots of red herrings on this one. And but we found a few faults on the way.

**Dave Jones:** And a brief recap is that the power supply on this looks like it failed on the I think the negative rail and -15 V rail and it took out at least one op amp plus three voltage regulators.

**Dave Jones:** That's what we found in the previous videos. And we've fixed the voltage regulators so the voltage rails are just fine now in this thing. But we did find a faulty op amp on the plus minus 15 V rail.

**Dave Jones:** And of course, if you find one faulty component on a rail which is a voltage rail which has gone over voltage in this case by the looks of it cuz that's the usual failure mode.

**Dave Jones:** You're not going to failure mode on under voltage unless it there's SCR latch up or something some bizarre thing like that happening. Then well, if one op amp can fail, well, this thing's got about 30 op amps or something 20 or something op amps on the same voltage rail.

**Dave Jones:** So, that was my guess last time is that possibly a whole bunch of op amps on this analog card which we pretty much nailed well, have narrowed down to at least the fault on this analog card in the thing.

**Dave Jones:** And also the error messages and stuff are basically telling us the same thing something wrong with this card in it. And well, that was my guess that maybe some other op amps have failed, but I couldn't get in there because it was all tucked away in the chassis.

**Dave Jones:** But thankfully, um some viewers have sent in some extender cards Uh DIN 41612 connector extender cards. Fantastic. So, I'm now able to get the board extended out so I can actually probe it and do the thing.

**Dave Jones:** And one thing we didn't have before ever, apart from the extender cards, was tada, my Flir thermal camera. So, we're going to use this as one of our main tools of attack this time on this sucker because if these op amps have failed, generally they're going to I think we found it uh failed short inside, but I couldn't measure the temperature using, you know, bit of spit on the back of a finger, go

**Dave Jones:** around, and you can test the chips. Well, only for the uh temperature. Well, only if you got access to them. So, we now have the card and yeah, I could go around and test them with my finger to make sure uh that none of the chips are overheating because that's a typical failure mode with uh chips like this that fail.

**Dave Jones:** They they short or go low impedance internally, draw excess current, and they heat up more than they should. So, um that's what we're going to attack first. We may or may not find anything.

**Dave Jones:** We'll find out. Let's go. So, yes, some viewers very kindly sent in uh various solutions for extending these things out. And we've got a basic extender card from uh Roth Electronic here, and this one is actually quite neat in that you can have a DIP switch actually disable every single one of the lines cuz this is a DIN 41612 connector.

**Dave Jones:** It's got a whole crap load of data lines, and they're each wired individually across and go through a DIP switch. So, that's fantastic. Although, we won't really need that to isolate any signals.

**Dave Jones:** Although, if we got really, really desperate, deep down into the system architecture of this thing, yeah, something like that may come in handy. Someone else sent in uh these Sony extender cards.

**Dave Jones:** And these ones I could have, you know, cut down the middle, but unfortunately, um these ones have big power traces and shorted out multiple pins. So, So, ones are actually designed not like a universal type one, they're designed for some particular Sony products.

**Dave Jones:** So, I've no idea what that is, EX151, obviously designed for troubleshooting and repairing some particular Sony product that uses it. The other solution is, of course, a cable like this to extend out.

**Dave Jones:** There we go, an IDC ribbon cable to extend out like that. Just got a gender changer on here, that's just to protect the pins, but male to female, so we can use that one.

**Dave Jones:** Although, I really do like these cards. So, this is the one we're going to use today. Now, of course, a real trap for young players that you've got to watch out for, I can put this card in here, it extends out a couple of inches past here, no problems, I can plug my board in, prop it up off the bench, and Bob's your uncle, right?

**Dave Jones:** Well, what? No. Look at this, right? We've got through-hole components pins right about there. Look at all these exposed pins, you don't want those shorting onto your metal chassis down in here when this board inevitably bends and touches down.

**Dave Jones:** Oh, what just fell out there? A screw. Screw just fell out. What on earth is that? Goodness, I don't know. It's falling apart. Did it come out of Yeah, it came out of here.

**Dave Jones:** It was just one of those holding Yeah, it looks like one of those studs there. In fact, that one right there just fell out, no problem. Anyway, you don't want them shorting out to the metal chassis there.

**Dave Jones:** So, what I've got is I've just put a stiff cardboard envelope on there, just taped it under, so we can safely now just plug this sucker in, and then plug our board in here, and extend away.

**Dave Jones:** But, of course, I've got to prop that up. And that is absolutely perfect. Look, perfect height like that. We can stand it. Now, we've got to all our test points, our ground points, our probing points, everything.

**Dave Jones:** We can access the chips, we can check the temperatures on the chips, we can do everything. Access, fantastic. So, now we should have no problems at least seeing what's going on here and finding an overview.

**Dave Jones:** So, as I said before, first port of attack on this, I've basically I was able to get like the probe and meter and scope stuff in there before and measure things.

**Dave Jones:** I We know that the voltage regulators are now fine. We This is a chip which we repaired before. There it is down in its socket. That's one of the op amps that failed on the plus minus 15 V or 18 V rail or something like that.

**Dave Jones:** But, there's all these other op amps. Look at them. They're everywhere. I think there's like 20 total just on this board or something or like 12, 15, I don't know.

**Dave Jones:** There's a lot. So, if one of them can fail, I'm hoping that you know, the rest of them haven't failed. Or maybe that's a good thing. At least you know, finding a fault is good.

**Dave Jones:** If hey, worst comes to worst, I can actually replace all the op amps, but jeez, that'll be a hell of a job. So, there's only one way to find out that.

**Dave Jones:** Power this thing up and before you even probe it, just go around and look at the temperature of these things. And as I said, I can wet the back of my finger, go around, test all the op amps, but hey, the thermal camera's much better and much more fun.

**Dave Jones:** And as before, I'm powering it from my DC source cuz there was something wrong with the AC source here. So, I've got 15.4 V, which is the maximum voltage that's supplying.

**Dave Jones:** Let me switch this puppy on and it's drawing 5 amps. So, there we go. I'll just let that warm up a bit because if the chips are faulty, you need to bring them up to temperature.

**Dave Jones:** Don't measure it straight away. Otherwise, you may not find the culprit. So, I'll give that 5 minutes. We'll come back. The screen, yep, is booting up just like it did last time.

**Dave Jones:** Now, just while that's booting up, some of you may be thinking, well, what are the effects of putting these extender cards in here cuz they are very long. You know, it's like a foot long or something like that, 30, 40 cm long.

**Dave Jones:** And well, yes, they can have an effect. If you've got a system which is, you know, running at relatively high speeds, you know, this can make a huge difference.

**Dave Jones:** Although, any well-designed product like this will pretty much have local voltage regulation on here, so it's not like they're being powered from somewhere else. So, all the voltages on this board should be just fine.

**Dave Jones:** So, the board should just operate fine and this is all 5-V TTL logic in this particular case, not operating very quick, you know, it might be operating I think 10 MHz maximum, something like that.

**Dave Jones:** That's really not much to worry about going over an extender board like this, but if you had, you know, a system at a higher frequency, well, you could be in deep trouble.

**Dave Jones:** But, generally, if you're using old-school uh DIN 41612 connectors like this, these aren't high-speed connectors. You're not going to be operating at, you know, hundreds of MHz across that bus, typically.

**Dave Jones:** So, yeah, in this case, it's pretty safe. I'm fairly confident that this board will operate and function correctly uh with that board in place, but even if it didn't, even if we're getting data issues and like that, uh what we're going to test for first is just to make sure that nothing is heating up on this board and we might test a few clocks and voltage rails and things like that.

**Dave Jones:** Um but, as I said, I've done that before and they look to be just fine. But, we'll do it again with the extender board. But, I'm curious to know if any of the other op-amps on that plus-minus rail have failed.

**Dave Jones:** So, first thing, get the FLIR meter out and see if there's any temperature difference. So, if they are if there is a fault in them that has caused low impedance or a short across the rail or, you know, some sort of latch-up fault or something like that, we should be able to see uh thermal differences in these chips.

**Dave Jones:** Let's see what we can find. So, yes, I've got my new FLIR E8 and it really is a fantastic tool. It's booting up at the moment. I I can actually capture video with this.

**Dave Jones:** I can hook it up to the USB port on the top, I believe, and and actually get, you know, nine frames per second streaming video out of it, but I won't go to that trouble today.

**Dave Jones:** I'll just point the camera at the screen. So, excuse the crudity of this thing. It's still booting up and oh, no. There we go. I've got to turn the shutter off and this thing is really, really nice.

**Dave Jones:** Oh, there we go. We're starting to see some stuff. So, let's Oh, yeah, look at that. Few chips. What Oh. Hello. Okay, let me set up the camera and the angles properly and let's have a look.

**Dave Jones:** Now, of course, one of the issues with this camera is that it's not designed for close-up work. And of course, you can actually hack on an external lens on this thing and you can actually get a tool which is on Thingiverse that allows you to tweak the lens in there so it can focus at a closer distance, but it's basically 30 cm.

**Dave Jones:** That's basically it. So, if we go into the menu here, we can actually settings. Yep, there it is. We can I've already got the alignment distance set for the lowest setting of 0.3 m.

**Dave Jones:** So, there we go. We should be able to focus on items if we're 30 cm away and the built-in camera with the MSX technology that that does all that neat overlaying of the real image and the thermal image as my hand, then it will align at if you're at least 30 cm or 0.3 m away from this thing.

**Dave Jones:** But jeez, look at all that stuff over there. That part of the board is heating up like a like a torch. Look at that. Wow, that doesn't that doesn't look good and a couple of other hot spots as well, which is rather interesting.

**Dave Jones:** So, yeah, let me set the camera and give you a good view of this. Now, what we're looking at here is the temperature on the screen here is telling us that is the maximum temperature across every pixel on that screen.

**Dave Jones:** So, it ranges from room temperature, 23.8, to almost 70° there. And then we can see the components. You can see the advantage of the MSX technology here. You can see the outline of those chips.

**Dave Jones:** Sorry about the reflection of the uh lights on the roof. That's a pain in the ass. Look at that. Ah. But anyway, what we can see, we can clearly see a couple of the chips there light like that one there.

**Dave Jones:** It's cal- I have to wait for it to calibrate. Look. Look at that. And then we can see the temperature in the top left there, 46° for that little puppy there, 45°.

**Dave Jones:** There's our three voltage regulators up there, 70°. That one's red hot. Yeah. 50, something like that. But that poor little what looks like a a uh DIP 8 package is already at 40°, and a couple of the others are lighting up, whereas the ones next to them, look, are not lighting up at all, and they look to be the ones that are lighting up look to be

**Dave Jones:** the op amps, the 8-pin op amps that are powered on the rail, the plus minus 15-V rail that we know has failed. So, that's just on this left-hand side of the board, let alone all the way over there on the right-hand side.

**Dave Jones:** Ah, this looks awful. So, that one there, if I take my finger away, tada, there it is. That one is an op amp, and yes, it's an AD 845.

**Dave Jones:** It should not be getting No op amp should be getting that hot. 45°? Are you kidding me? But oh, what I'm forgetting here is that these things are plus minus 15-V rails.

**Dave Jones:** Hey, that's a 30-V supply. That's a lot. And well, hey, if this has got a quiescent current of, you know, even a milliamp, then, you know, it's a reasonable amount of power dissipation in this device.

**Dave Jones:** So, let me check the data sheet for that. So, let's do the proper engineering check on this by looking at the data sheet. Aha, this thing has a quiescent current of around about 10 milliamps.

**Dave Jones:** That's actually quite large and when you operate this thing at 30 volts, well, V * I, what's the power dissipation in that chip just for the quiescent current? Well, you're looking at 0.3 watts and that's actually quite significant for a DIP 8 package.

**Dave Jones:** And if you look further down in the data sheets, down in the all the weird stuff hidden away down in there, you'll find the thermal resistance of this DIP package.

**Dave Jones:** It's different between the DIP package and the ceramic package, but this one, the plastic DIP package, is 100°C per watt. So, 100°C per watt times our 0.3 watts, we'd expect this thing to be 30°C above ambient.

**Dave Jones:** So, what am I measuring? Yeah, there it is. Look, around about 50°C for that chip there. And well, bingo, that is roughly third that 30°C above our ambient temperature.

**Dave Jones:** So, you know, you might look around your board and go, "Aha, an op amp, look at that. It's you know, it stands out like a dog's hind leg. Look at that.

**Dave Jones:** Awful. That must be the culprit." No, it's not. Do your engineering, check the data sheet every time. So, there's actually nothing wrong with that. It's operating exactly to spec.

**Dave Jones:** But aha, wasn't this side of the board lit up like a Christmas tree? Yes, I need to go back and check the other side, but hey, this one was really looked a red hot before and a quick check.

**Dave Jones:** Let's go over here again and yep, a lot of the chips are Look at that, 60. That one's up to 60 seven 66 67. That one's That's pretty disturbing.

**Dave Jones:** There's a metal can. Got to make sure I've got the alignment uh properly on this. No, I don't. I'm not 30 cm away, so that's a trap. Let me get it more accurate.

**Dave Jones:** There we go. Yeah, basically up to 68 odd degrees, but it's pretty much the same. I mean, that one chip is a little bit hotter than the others, but the others are still probably you know, they're I don't know.

**Dave Jones:** It's Yeah, there we go. 63, 65. I don't know. It's hard to get this, especially when I'm doing it on camera, but uh yeah, they all look all those op-amps look to be displaying the same same amount of power, so they're all faulty or they've actually just got a high quiescent current operating on that 30-V rail.

**Dave Jones:** Time to check them, too. Well, they're all exactly the same AD 845. So, well, yeah, I'd expect them all to get quite warm, but they're a good 7 to 10° warmer than the other one on the other side of the board.

**Dave Jones:** So, either they're you know, they're that's just a quiescent power, of course, that's not the active power of it driving anything. So, although it does look suspicious on the thermal camera, that I I think this is probably right.

**Dave Jones:** We're probably getting cuz there's multiple ones here, we're probably getting some you know, heat spread between them, so the whole area is raising up by a bit more temperature.

**Dave Jones:** I mean, this thing's been running for you know, 15, 20 minutes or something now, and yeah, I you know, the whole board's probably warming up and just raising the whole temperature around the board, and they're probably driving something as well.

**Dave Jones:** So, although that did look bad on camera, no, I I don't suspect those at all anymore. Now, curiously though, this LM6321 here, which is a power buffer amplifier basically driving the 50-Ω source, I believe it is then, yeah, you'd expect that one to get pretty hot.

**Dave Jones:** Check the data sheet for that. Sure enough, 20 mA quiescent current. So, jeez, I'd expect that one to be significantly warmer than the others and well There you go.

**Dave Jones:** 46. No, it's very similar. So Yeah, 50. So I would have expected that to be much higher, but it ain't. So I've really had a good look around this board and well, nothing stands out at all.

**Dave Jones:** The op amps are as per their data sheet values for the quiescent current. The Raytheon uh chip down in there, I'd expect that to get a little bit warm and uh yeah, it is a bit toasty.

**Dave Jones:** I'm still using my finger even though I've got a Flir camera in front of me, crazy. And the ASIC gets as warm as you'd expect, 55° and that sort of stuff, but apart from that, nothing really scorching hot or out of the ordinary.

**Dave Jones:** So well yep Great tool, but didn't find anything in this case. Bummer. And I've had a probe around with the scope on all the various test points, cuz there are lots of nice test points in here even though I don't know what a lot of them do, but I'm getting, you know, the activity I expect, a clock line, you get clock line, you get clock data.

**Dave Jones:** They're all these system clocks are working. All the voltage regulators are still working. The supplies for all the op amps and everything, as I said, just fine. There's no noise on them.

**Dave Jones:** No issues whatsoever. So yeah, I don't like that. You know, gets back to we're looking at the uh source before the source wasn't working and trying to track that down.

**Dave Jones:** Well, I'm no closer to that, cuz I don't actually have a schematic for this analog board. Uh somebody did send me the schematic for the main processor board, but unfortunately, that doesn't help us with this board that uh I'm pretty sure is the culprit, cuz our source is not working and our source is generated from this board.

**Dave Jones:** So yeah, I'm uh going to have to call it quits, I'm afraid, for uh today. Once again, sorry. Um yeah, no more progress on this. Um well, there's progress.

**Dave Jones:** I mean, not finding an issue is progress, you know? We've looked at it thermally with the camera, and you know, nothing stands out. Although, I wouldn't rule out that the op amps could be faulty, but they're at least not overheating.

**Dave Jones:** So, that could still be an issue. And well, if it is, then you know, we might cuz tracking those down, if it's not a thermal issue, tracking them down is basically, you know, you've got to have the circuits, you've got to trace it all the way through, you've got to put test signals into this thing, know how it samples, and know how it does everything else, and you know, yeah,

**Dave Jones:** that's not easy. Uh Anyway, I hope you found that mildly interesting, if uneventful, just like the previous videos. Oh, well. If you want to discuss it, jump on over to the EVblog forum.

**Dave Jones:** Link is down below. And if you like these sorts of videos, please give them a big thumbs up. Although, yeah, the EVblog repair curse strikes. I never find anything that's either repair either it's trivial, or it's just, you know, unrepairable, or so difficult, or whatever, to track down.

**Dave Jones:** And this one, I think, is going to be a real dog, but I'm not done yet. If I can get the schematic for this uh analog board, then we will certainly be on our way again.
