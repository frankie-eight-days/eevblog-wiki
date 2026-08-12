---
video_id: BpfmvU8mWsU
title: EEVblog 1522 - BM786 Multimeter Repair PART 2
url: https://www.youtube.com/watch?v=BpfmvU8mWsU
source: youtube-asr
timestamps: {"0": 0, "1": 21, "2": 34, "3": 53, "4": 74, "5": 87, "6": 101, "7": 112, "8": 133, "9": 144, "10": 156, "11": 175, "12": 186, "13": 199, "14": 213, "15": 228, "16": 241, "17": 251, "18": 263, "19": 275, "20": 286, "21": 295, "22": 306, "23": 320, "24": 331, "25": 339, "26": 349, "27": 359, "28": 375, "29": 389, "30": 402, "31": 416, "32": 428, "33": 437, "34": 446, "35": 453, "36": 468, "37": 484, "38": 494, "39": 517, "40": 533, "41": 547, "42": 559, "43": 571, "44": 599, "45": 609, "46": 626, "47": 639, "48": 651, "49": 669, "50": 679, "51": 691, "52": 700, "53": 712, "54": 725, "55": 737, "56": 751, "57": 761, "58": 776, "59": 786, "60": 799, "61": 814, "62": 828, "63": 842, "64": 857, "65": 869, "66": 883, "67": 909, "68": 929, "69": 947, "70": 962, "71": 979, "72": 1003, "73": 1015, "74": 1029, "75": 1045, "76": 1061, "77": 1071, "78": 1081, "79": 1096, "80": 1109, "81": 1123, "82": 1136, "83": 1148, "84": 1159, "85": 1176, "86": 1191, "87": 1210, "88": 1219, "89": 1240, "90": 1253, "91": 1270, "92": 1283, "93": 1297, "94": 1310, "95": 1329, "96": 1346, "97": 1363, "98": 1374, "99": 1386, "100": 1396, "101": 1405, "102": 1416}
---

**Dave Jones:** Hi, just a follow-up to the BM 786 troubleshooting video I did where we came to the conclusion that it's most likely looks like the main processor here has failed because we can't program it from the header which is this one over here like we can't program it directly from the header even though the voltages around here look okay.

**Dave Jones:** But a few people have had some comments. So I thought I'd have a look at that. Yes, I did actually measure all the decoupling caps to make sure like none of them were shorted and stuff like that.

**Dave Jones:** The bypass caps. Sorry, I forget who mentioned this but somebody in the comments mentioned this resistor down here. Now clearly this resistor and this cap here these have been hand soldered as have some other parts that we'll have a look at.

**Dave Jones:** Now why have they hand soldered parts like this? Is it like a mod or something like that? No, almost certainly I think it's just that the pick and place machine when they assembled this these parts fell off cuz they you know parts fall off the heads all the time and so the board goes from the pick and place machine through the reflow oven and then it usually goes into an optical image

**Dave Jones:** inspection system which compares it against a golden reference board and then it can pick up that components have fell fell off they've been misplaced or they're tombstoned or whatever.

**Dave Jones:** So yeah, they're probably parts that have fallen off and rather than they don't put it back in the pick and place machine and they're not going to scrap the board so you know they have somebody do manual rework and obviously someone at Brymen's not very good at doing manual rework cuz this is pretty piss poor.

**Dave Jones:** Now this is the LCD driver chip and maybe this resistor here is to do with the contrast or setting the contrast or something like that. I don't know. But yeah, that's the LCD driver so that really shouldn't have anything to do with it.

**Dave Jones:** But I did find something interesting in here. Look at that. It's .2 ohms. That doesn't seem to make sense. Like it could be like a as part of a low-pass filter for the power supply, but at .2 ohms, that does not sound right to me.

**Dave Jones:** So, I got my reference board. Let's have a look at that one. That it is 9.4 K. We can flip it around. Yeah, 9.4 K. It's a good tip just to measure resistance in both directions.

**Dave Jones:** Just make sure you got no active components in there. You still got other components. You'll notice that this one actually has the resistor in the middle. Whereas the faulty board has has that resistor completely missing.

**Dave Jones:** I don't know what the issue is there. Joe Smith, who you should be familiar with his channel, does multimeter destruction testing. He noticed U2 over here. Like some people said, "Oh, this cap." I think Defpom, who does repair videos as well.

**Dave Jones:** If you want If you like your repair videos, he does multi-part series repair videos. So, check out Defpom's channel. And no, that is actually part of the trace. So, it's not like shorted out to that via.

**Dave Jones:** It's supposed to be. Now, Joe thought that this U2 here had a blow hole in it. So, I don't know what U2 does there. But that is that looks like for all the world not like a blow hole.

**Dave Jones:** It's just flux. So, it's all just flux. I believe that's just flux residue. So, yeah. If we clean that off, just wanted to show you that before. I can I can actually clean that.

**Dave Jones:** I'll just get the isopropyl. I do have flux cleaning stuff. But oh, yeah, there's also that black stuff in there as well. Yeah, gunk in there. But anyway, I think you'll find that'll actually clean up nicely.

**Dave Jones:** So, yeah, there's no there's no blow hole in that. Anyway, that resistor there is completely sus, so I'm going to get that out of there. Even though it's got nothing to do with the microcontroller circuit.

**Dave Jones:** So, the problem is is that we can't even identify the micro. So, you know, I I really need a better pair of tweezers. Do have I lost my set.

**Dave Jones:** I don't know where it is. There we go. Gone-ski. That is zero ohms. No wonder we're measuring point two that actually so there's nothing wrong with it. But once again, this meter was working.

**Dave Jones:** So, obviously I don't maybe they made a circuit change. Okay, so the other board I've got here is got on the bare PCB 20 33rd week 2020 whereas this one's got the 12th week 21.

**Dave Jones:** So, yeah, obviously they've made a they've made a more recent change there. I could open up and like a brand new stock unit or whatever, but it was obviously working.

**Dave Jones:** So, there's nothing wrong with it. I so I'll just put that back. I don't think that's an issue. Give that a bit of a clean, too. Okay, this is actually locked up my programmer.

**Dave Jones:** I can't cycle through. Got to actually re-power it. IDs the attempts to ID the chip. I'll stick it in the via there. So, much easier than the pin. Just the tip.

**Dave Jones:** Just slip the tip in. I'll just single shot capture that. Boom! There we go. We got something. So, oh, there we go. That's nice, isn't it? The uh National Instruments actually captures outside the window.

**Dave Jones:** That's the zoom out feature. I've done a video on that. Looks like the National Instruments does it. See where it comes in handy? I've zoomed in I otherwise I'd have to repeat this whole process.

**Dave Jones:** And no, I don't. Look. Boom boom boom. And you know, you don't worry about overshoot like that. In fact, I'll show you the other ones cuz they're on all the time.

**Dave Jones:** So, there you go. That's third from the second from the top. So, that one looks like data. Oh, there's an interesting level thing happening there. Like little bus contention or something.

**Dave Jones:** It's obviously we've got a decay there, so the bus has been disconnected somehow and it's glitching over there. That's interesting, isn't it? Let me look at the other one.

**Dave Jones:** It's not a continuous clock. So, there those two pins. Anyway, I'm going back to the second one. Oh, there There we go. So, we're getting two pulses, right? So, there That's all the data on the programming uh header.

**Dave Jones:** So, it's all there. It's not being loaded down except that other bus, but that's a bus. It's like a bus contention. Like it's a bus thing. It It's not like the entire line is shorted or anything like that, so it doesn't seem to be a big deal.

**Dave Jones:** Couple on the top. These ones here. These come out. These go around here. They go around here. They go to here. Oh, flippity doodah. Oh, it's getting close to being Oh, okay.

**Dave Jones:** They're 100 ohm resistors, are they? Those two high-speed signals. So, that pin and that pin. So, that's not an issue. Like, you know, and some people have said quite, you know, a few people said, "Oh, just reflow the main chip." Uh, not going to do that now.

**Dave Jones:** It's Larry. Uh, what's that? Yeah. Look for the reset pin. I agree. I adjusted my ATM switcher so you can now see these signals. So, there's those two main signals going in there.

**Dave Jones:** I think I'll get out the good board just as a matter of course and see if that's the same on the good one. Oh, okay. So, it only reads it once.

**Dave Jones:** Okay, so I have to I have to cycle through that on my programmer. The good thing is the standalone programmer, by the way, I don't have to have it hooked up to the PC.

**Dave Jones:** I've got the firmware actually programmed into it and then I can just hit the program. I can just hook it up, hit the program button. Boom. It's very nice, actually.

**Dave Jones:** Hmm. There you go. So, it's obviously like just continually for the other one, it's just continually cycling there. That doesn't actually help us, does it? Have a look. I'm not sure of the memory depth here.

**Dave Jones:** No, we're reaching the reaching the limits, and I don't want to have to set up complex triggers and capture and all that sort of, you know, like Yeah, cuz then we'd just be getting into quirks of the programmer and and the chip and how it's programmed and, you know, how it's, you know, the IDs detecting and all that sort of stuff.

**Dave Jones:** So, as I said, I don't have the pinout for this because it's a like a sort of semi-custom device for Brymen, or it's at least a custom variant, I believe.

**Dave Jones:** So, for a reset pin, you'd probably be looking for like an RC power-up or something like that. I mean, there was that switch thing. We saw that on the bottom of the switch before that it had that contact, and that could be like a power-on reset contact, but that's that's different because that's when you rotate the switch.

**Dave Jones:** This is with the switch in the off position. That that's the data in, and data and the other one's got to be the data out. I just noticed something embarrassingly dumb, which nobody absolutely nobody picked me up on.

**Dave Jones:** Nobody. Not a single viewer picked me up on this. Well, I don't think so. Sorry if somebody did. This is not the processor. This is the multimeter chipset. So, there was no point changing that crystal.

**Dave Jones:** Makes absolutely no difference whatsoever. This is the main processor. How is it the main processor? Because you've you've seen me. I've been probing these clocks around here. It just dawned on me.

**Dave Jones:** This is the damn processor. That the previous video, for some reason, I was I was fixating on that other chip, which is the multimeter chipset. Dolt. Well, that's embarrassing.

**Dave Jones:** See, yeah, I can't believe nobody picked me up on that. I expected more from my audience. Anyway, that's water under the bridge. Okay, since discovering that this is actually the processor here, um yeah, I've actually gone back to the data sheet and it turns out that the pinout seems to be correct because this is now a 64-pin chip and that does match the data sheet for not the full part

**Dave Jones:** number, the one I've that my programmer reads out is a four-digit part number, but the data sheet's only three-digit. got an extra one tacked on the end. Um but I can't find any information on that one.

**Dave Jones:** Now, just as an aside and a trap for young players, one of the annoying things about this particular uh micro is that it's available Not only is it available in a LQFP like this, uh low-profile quad flat pack, but it's also also available in a 64-pin QFN.

**Dave Jones:** Now, the pinout for the QFN is slightly different to this one. So, I do actually have the pinout for this one and it matches up. Um this is the uh clock going in here and this is the data for the debug interface.

**Dave Jones:** So, clock and data. I've discovered that this one here is uh VSS or ground and this one here, or pin uh three here, is actually uh positive. So, ground and positive rail here.

**Dave Jones:** But the QFN pinout is like shifted one pin around so that pin 64 here is the ground and then this one's the clock. This one's the data and I've uh in and in this particular case, pin two is actually the reset pin.

**Dave Jones:** So, aha, we've found the re- reset pin. It buggers off under here. Does it go over to there? I don't know. I can buzz that out. VCC goes through that zero-ohm resistor to there.

**Dave Jones:** So, what I can do now, powering it through the debug interface, we can measure the voltage rail there. There you go. So, 3.5 V. We can look at pin two, which I have verified is the reset pin.

**Dave Jones:** Got to be careful when you probe here. Don't want to short anything out and it I know it's an active low reset. And there you go. We're actually getting 3.

**Dave Jones:** 3 volts there. Yeah, it's not being processor not being pulled in a constant state of reset, but that doesn't mean that there's not like a failed capacitor. I'm going to actually follow that reset trace.

**Dave Jones:** In fact, I'll just probe, make sure that it is going to where I suspect it is. Yep. And I know it's that via going out there. So, I just whack a light under that.

**Dave Jones:** Jeez, need to turn that down a tad. There we go. That one. So, that's going out there. Aha. There's your reset cap going down to ground. Could that cap be failed?

**Dave Jones:** Hang on. I think I traced the wrong pin. So, that's another tip. Just be double-check whether or not the trace that you tracing is the one you're tracing. If that makes sense.

**Dave Jones:** Yeah. I goofed that. It's this one here. I Yeah. I was way off as the reference. I took those four pads as the reference, not those four pads as duh.

**Dave Jones:** Yep. You're probably screaming that at home. Right. So, this is the reset line here. Aha. A diodey. So, let's actually measure that. Yeah, diode's okay. No wackers. Turned around the other way.

**Dave Jones:** Yeah. Okay. Easy to test and rule out actives like that easy to Usually diodes will test in circuit like that. And then there's something going off over to here as well.

**Dave Jones:** But once again, like our reset line isn't being held low. So, the processor isn't isn't not being actively reset. The data sheet definitely says active low. Yeah, it ain't that.

**Dave Jones:** Anyway, might be chasing a red herring with the reset line, but you know, you just want to make sure because if there's a cap that's pulling it low, and that cap is, you know, it's it's open, then which is a fine mode for caps, they can fail short and open, multi-layer ceramic caps.

**Dave Jones:** And if it fails open, it doesn't get its power-on reset, that could cause a problem. Okay, I just discovered that when I I can switch the power off from the programmer when it goes into that programming mode.

**Dave Jones:** So, what I can do is I can adjust the time base here, make it short, 20 milliseconds and there's 50 milliseconds per division, something like that. I can single shot capture that, then force the programmer, there we go, two reset pulses.

**Dave Jones:** That's interesting. Let's compare that with a good one. One reset pulse. Isn't that interesting? There there is no reset line from the programmer. Um that's according to the pinout on the programmer.

**Dave Jones:** So, that's very interesting, but in any case, that is not an RC like power-on pull-up reset pin on the micro. This is the direct reset pin. There you go.

**Dave Jones:** So, yeah, there's there's something active. Hmm, there's not like a reset chip or anything on here, I don't think. Aha, that's interesting. The reset line is connected to there.

**Dave Jones:** The plot thickens. According to the programmer pinout, that is actually VPP. Okay, so VPP go is the reset line on the programmer. Okay. Right, that makes sense. Um I didn't think there was like an active reset circuit, cuz like a lot of times you can get, you know, from TI and a whole bunch of other makers, you can get like active reset circuits, which cleanly give you a reset pulse when you

**Dave Jones:** power on, as opposed to relying on a RC power-on. So, obviously, um yeah, it's it's getting the pulse. So, that's probably why there's two pulses there is, cuz that's the programmer just going and it's it's trying to reset and then it doesn't get anything and then it resets again and it's just trying itself over and over, as we've seen with the clock and data.

**Dave Jones:** Whereas the good unit, when we hook the programmer up, it only it it does its thing, reads the chip ID and then stops talking. Right, so at this point, I know that the processor is getting clock, data and getting reset as well, which is the programmer's VPP.

**Dave Jones:** I don't know if it actually does a VPP function and actually like pulls a VPP is a programming power. So it's, you know, old school is like 12 volts, even 24 volts, something like that, you know, but it pulses it to a higher voltage.

**Dave Jones:** I don't know if it actually does that. I don't care. It's not reading out the chip data. So the the the debug interface is getting everything. So the chip's getting its power and it's getting clock, data and reset from the debug interface and it's not talking.

**Dave Jones:** So, once again, the only conclusion I can come to, like I did in the first video, is that that processor is bunk. Possibly, I'm going to have to find a uh donor unit and try and remove that and then um solder on another one from a known donor unit that actually talks to the programmer.

**Dave Jones:** If it can't talk to the programmer, that's the whole fault. Yeah, obviously, I'm not going to debug the multimeter in any other operational regard. There's just no point um when it doesn't go directly from the debug interface like that.

**Dave Jones:** And that's basically it's bypassing all the power on, any sort of like power on reset or anything like that. It's it's being controlled from the debug um interface and it's just it's not doing it.

**Dave Jones:** All right, I have actually found a donor unit. Let's actually remove this. Put some flux on here. All right, let's see if I can remove this. Bingo. Didn't damage anything there.

**Dave Jones:** Nice. Do the same thing for the dead chip. So, we won't be able to do any more debugging on this, I'm afraid. I am pretty done on that. Sorry, my Tiguan is not going to be able to view this.

**Dave Jones:** Tada! There we go. So, that's the faulty one. No pads were harmed in the filming of this video. If you're wondering what flux I'm using, it's an Edsyn FL 911.

**Dave Jones:** Seems to work for me. Your mileage may vary. Now, I've got to make sure I put the right chip in, and I've got to make sure I get pin one over here.

**Dave Jones:** Put that on. I might just uh wick off some of the solder on those pins. Oh, why you could see that wick straight off there. That was nice. Seems to be a couple of shorted out pins on there.

**Dave Jones:** But, I'm not going to Oh, that one pin over there has been a bit bent. And I'll tack pin 64 over there. Decided not to reflow this. Just do some drag soldering.

**Dave Jones:** And we go. Just give those a little dab dab. And they should be soldered nicely. It's not pretty. Um in fact, there are a couple of pads over here which I don't think they go anywhere.

**Dave Jones:** They were lifted off. Let's have a look. Yeah, those pads don't go anywhere. So, they lift off very easily. And just the glue on this PCB material is not that good.

**Dave Jones:** So, yeah, they lifted off, but the chip reads. The chip reads on the programmer. No wuckers. And I was able to successfully program it with the latest version as well.

**Dave Jones:** But, if I plug it in in the programmer mode, it I do get insertion error. That means the processor is now working and the LCD driver is working. Whoop.

**Dave Jones:** Whoop. Something Something's reset itself there. Whoop. Look at that. There you go. So, we're just insertion error there. Something else is going on. So, I'm going to uh put that transistor back in there because there was nothing wrong with that.

**Dave Jones:** Okay, I'm just don't going to do a quick and nasty reflow of that old chip onto the donor board. Sorry, you can't see this. Okay, so this board did work before.

**Dave Jones:** It's got those pins look absolutely correct. Let's plug the programmer in. Boom. Yep, no chip ID. So, there you go. And I can buzz out those and definitely those pins are getting over there.

**Dave Jones:** Yep, everything's Everything's hunky-dory. I can measure volts on there. The mantis was in the way. I was using that to inspect and I can actually measure Sorry, you got to have got the on-screen multimeter at 3.3 volts.

**Dave Jones:** Yeah. So, that's confirmed. I transferred the faulty chip onto the donor board, which was powering up, but it sort of had like some other issues or something. I can't remember exactly what, but yeah, that was from a junk uh bin multimeter, but it did power on and work and you know, it programmed and all that uh sort of jazz.

**Dave Jones:** So, yeah, that's confirmed. I'm silicon failed. What what what what? No idea why, you know? If you got any idea, leave it in comments down below. Let's power it on.

**Dave Jones:** There it is. I was able to program that with the uh latest firmware uh 609. Unfortunately, there's an insertion error. I don't know what the insertion error is, so whether or not that was a fault that I don't see how it could cause the That's really annoying.

**Dave Jones:** It does that in all ranges. So, I think I've had that error before. Yeah, I've had a 40 meter with that before and I had to replace it, at least one of them.

**Dave Jones:** So, I I don't think I ever got that meter back. I never investigated, but there it is. Um it is repaired in that it now powers up. So, yeah, we definitely had a faulty processor in that thing.

**Dave Jones:** But, now it looks like there's something else wrong and it Well, that's it for this video. I'm I'm done. I didn't actually want to repair this thing. I just wanted to troubleshoot down to find what the issue was and we definitely found a problem.

**Dave Jones:** Faulty processor and we uh replaced it. We We deduced that in the first video, but the second video, yeah, absolutely confirmed that and I put that chip back on the um back on the other board here and it buzzes through everything buzzes through fine uh from the programming header and it just doesn't does exactly the same fault as before.

**Dave Jones:** So, there's definitely a dead silicon there. So, there you go. Anyway, I've got myself a donor board now, which is kind of handy. And as I mentioned in a live show uh recently where I actually got people to guess and somebody did actually Well, a couple of people I think ended up guessing uh the goof up I made in that video.

**Dave Jones:** Now, a lesser YouTuber, of course, would have like hid that because they'd be too embarrassed to show that they made a goof like that. And well, you know, this kind of thing I I can't tell you the mindset I was in when I um started thinking that was the DMM chipset.

**Dave Jones:** It's obvious just from the topology, as I I explained in the live video, just the topology of the uh thing. It was It was really obvious, but no one in the comments picked it up.

**Dave Jones:** I'm absolutely surprised. That's one of probably my first video ever where I've made a major goof like that, major embarrassing goof, and nobody's actually picked it up until I prodded some people, "Hey, there's something wrong." And they started to put their thinking cap on it.

**Dave Jones:** Yeah, um there you go. So, I hope you enjoyed me leaving in the goose like that. It shows that these things happen. Probably wouldn't have done that um well, wouldn't have happened if I had a schematic.

**Dave Jones:** And it wouldn't have happened if I probably wasn't shooting a video. Shooting a video is like different level of stuff. Your mind gets all, you know, anyway. Anyway, whatever.

**Dave Jones:** Um there it is. It was confirmed 40 processor. So, yeah, that that insertion error, I don't know. I might leave that for another video if I've got the time and motivation.

**Dave Jones:** So, anyway, I hope you learned some valuable lessons from that video. If you did, please give it a big thumbs up. And as always, discuss down below. Catch you next time.
