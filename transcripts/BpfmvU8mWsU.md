---
video_id: BpfmvU8mWsU
title: EEVblog 1522 - BM786 Multimeter Repair PART 2
url: https://www.youtube.com/watch?v=BpfmvU8mWsU
source: youtube-asr
---

**Dave Jones:** Hi, just a follow-up to the BM 786 troubleshooting video I did where we came to the conclusion that it's most likely looks like the main processor here has failed because we can't program it from the header which is this one

**Dave Jones:** over here like we can't program it directly from the header even though the voltages around here look okay. But a few people have had some comments. So I thought I'd have a look at that. Yes, I did actually measure all the decoupling

**Dave Jones:** caps to make sure like none of them were shorted and stuff like that. The bypass caps. Sorry, I forget who mentioned this but somebody in the comments mentioned this resistor down here. Now clearly this resistor and this cap here these

**Dave Jones:** have been hand soldered as have some other parts that we'll have a look at. Now why have they hand soldered parts like this? Is it like a mod or something like that? No, almost certainly I think it's just that the pick and place

**Dave Jones:** machine when they assembled this these parts fell off cuz they you know parts fall off the heads all the time and so the board goes from the pick and place machine through the reflow oven and then it usually goes into an optical image

**Dave Jones:** inspection system which compares it against a golden reference board and then it can pick up that components have fell fell off they've been misplaced or they're tombstoned or whatever. So yeah, they're probably parts that have fallen off and rather than they

**Dave Jones:** don't put it back in the pick and place machine and they're not going to scrap the board so you know they have somebody do manual rework and obviously someone at Brymen's not very good at doing manual rework cuz this is pretty piss

**Dave Jones:** poor. Now this is the LCD driver chip and maybe this resistor here is to do with the contrast or setting the contrast or something like that. I don't know. But yeah, that's the LCD driver so that really shouldn't have anything to

**Dave Jones:** do with it. But I did find something interesting in here. Look at that. It's .2 ohms. That doesn't seem to make sense. Like it could be like a as part of a low-pass filter for the power supply, but at .2 ohms, that does not sound

**Dave Jones:** right to me. So, I got my reference board. Let's have a look at that one. That it is 9.4 K. We can flip it around. Yeah, 9.4 K. It's a good tip just to measure resistance in both directions. Just make

**Dave Jones:** sure you got no active components in there. You still got other components. You'll notice that this one actually has the resistor in the middle. Whereas the faulty board has has that resistor completely missing. I don't know what the issue is there. Joe Smith,

**Dave Jones:** who you should be familiar with his channel, does multimeter destruction testing. He noticed U2 over here. Like some people said, "Oh, this cap." I think Defpom, who does repair videos as well. If you want If you like your repair

**Dave Jones:** videos, he does multi-part series repair videos. So, check out Defpom's channel. And no, that is actually part of the trace. So, it's not like shorted out to that via. It's supposed to be. Now, Joe thought that this U2 here had a blow hole in it.

**Dave Jones:** So, I don't know what U2 does there. But that is that looks like for all the world not like a blow hole. It's just flux. So, it's all just flux. I believe that's just flux residue. So, yeah. If

**Dave Jones:** we clean that off, just wanted to show you that before. I can I can actually clean that. I'll just get the isopropyl. I do have flux cleaning stuff. But oh, yeah, there's also that black stuff in there as well. Yeah, gunk

**Dave Jones:** in there. But anyway, I think you'll find that'll actually clean up nicely. So, yeah, there's no there's no blow hole in that. Anyway, that resistor there is completely sus, so I'm going to get that out of there. Even though it's

**Dave Jones:** got nothing to do with the microcontroller circuit. So, the problem is is that we can't even identify the micro. So, you know, I I really need a better pair of tweezers. Do have I lost my set. I don't

**Dave Jones:** know where it is. There we go. Gone-ski. That is zero ohms. No wonder we're measuring point two that actually so there's nothing wrong with it. But once again, this meter was working. So, obviously I don't maybe they made a circuit change. Okay, so the

**Dave Jones:** other board I've got here is got on the bare PCB 20 33rd week 2020 whereas this one's got the 12th week 21. So, yeah, obviously they've made a they've made a more recent change there. I could open up and like a brand new stock unit or

**Dave Jones:** whatever, but it was obviously working. So, there's nothing wrong with it. I so I'll just put that back. I don't think that's an issue. Give that a bit of a clean, too. Okay, this is actually locked up my

**Dave Jones:** programmer. I can't cycle through. Got to actually re-power it. IDs the attempts to ID the chip. I'll stick it in the via there. So, much easier than the pin. Just the tip. Just slip the tip in. I'll just single shot

**Dave Jones:** capture that. Boom! There we go. We got something. So, oh, there we go. That's nice, isn't it? The uh National Instruments actually captures outside the window. That's the zoom out feature. I've done a video on that. Looks like the National Instruments does

**Dave Jones:** it. See where it comes in handy? I've zoomed in I otherwise I'd have to repeat this whole process. And no, I don't. Look. Boom boom boom. And you know, you don't worry about overshoot like that. In fact, I'll show you the

**Dave Jones:** other ones cuz they're on all the time. So, there you go. That's third from the second from the top. So, that one looks like data. Oh, there's an interesting level thing happening there. Like little bus contention or something. It's obviously

**Dave Jones:** we've got a decay there, so the bus has been disconnected somehow and it's glitching over there. That's interesting, isn't it? Let me look at the other one. It's not a continuous clock. So, there those two pins. Anyway, I'm going back to the

**Dave Jones:** second one. Oh, there There we go. So, we're getting two pulses, right? So, there That's all the data on the programming uh header. So, it's all there. It's not being loaded down except that other bus, but that's a bus.

**Dave Jones:** It's like a bus contention. Like it's a bus thing. It It's not like the entire line is shorted or anything like that, so it doesn't seem to be a big deal. Couple on the top. These ones here. These come out.

**Dave Jones:** These go around here. They go around here. They go to here. Oh, flippity doodah. Oh, it's getting close to being Oh, okay. They're 100 ohm resistors, are they? Those two high-speed signals. So, that pin and that pin. So, that's not an issue. Like,

**Dave Jones:** you know, and some people have said quite, you know, a few people said, "Oh, just reflow the main chip." Uh, not going to do that now. It's Larry. Uh, what's that? Yeah. Look for the reset pin. I agree. I

**Dave Jones:** adjusted my ATM switcher so you can now see these signals. So, there's those two main signals going in there. I think I'll get out the good board just as a matter of course and see if that's the same on the good one. Oh, okay. So, it

**Dave Jones:** only reads it once. Okay, so I have to I have to cycle through that on my programmer. The good thing is the standalone programmer, by the way, I don't have to have it hooked up to the PC. I've got the firmware actually

**Dave Jones:** programmed into it and then I can just hit the program. I can just hook it up, hit the program button. Boom. It's very nice, actually. Hmm. There you go. So, it's obviously like just continually for the other one, it's just

**Dave Jones:** continually cycling there. That doesn't actually help us, does it? Have a look. I'm not sure of the memory depth here. No, we're reaching the reaching the limits, and I don't want to have to set up complex triggers and capture and all

**Dave Jones:** that sort of, you know, like Yeah, cuz then we'd just be getting into quirks of the programmer and and the chip and how it's programmed and, you know, how it's, you know, the IDs detecting and all that sort of stuff.

**Dave Jones:** So, as I said, I don't have the pinout for this because it's a like a sort of semi-custom device for Brymen, or it's at least a custom variant, I believe. So, for a reset pin, you'd probably be looking for

**Dave Jones:** like an RC power-up or something like that. I mean, there was that switch thing. We saw that on the bottom of the switch before that it had that contact, and that could be like a power-on reset contact, but that's that's different

**Dave Jones:** because that's when you rotate the switch. This is with the switch in the off position. That that's the data in, and data and the other one's got to be the data out. I just noticed something embarrassingly dumb, which nobody absolutely nobody picked me

**Dave Jones:** up on. Nobody. Not a single viewer picked me up on this. Well, I don't think so. Sorry if somebody did. This is not the processor. This is the multimeter chipset. So, there was no point changing that crystal. Makes absolutely no difference

**Dave Jones:** whatsoever. This is the main processor. How is it the main processor? Because you've you've seen me. I've been probing these clocks around here. It just dawned on me. This is the damn processor. That the previous video, for some reason, I was I was

**Dave Jones:** fixating on that other chip, which is the multimeter chipset. Dolt. Well, that's embarrassing. See, yeah, I can't believe nobody picked me up on that. I expected more from my audience. Anyway, that's water under the bridge. Okay, since discovering that this is

**Dave Jones:** actually the processor here, um yeah, I've actually gone back to the data sheet and it turns out that the pinout seems to be correct because this is now a 64-pin chip and that does match the data sheet for not the full part

**Dave Jones:** number, the one I've that my programmer reads out is a four-digit part number, but the data sheet's only three-digit. got an extra one tacked on the end. Um but I can't find any information on that one. Now, just as an aside and a trap

**Dave Jones:** for young players, one of the annoying things about this particular uh micro is that it's available Not only is it available in a LQFP like this, uh low-profile quad flat pack, but it's also also available in a 64-pin QFN.

**Dave Jones:** Now, the pinout for the QFN is slightly different to this one. So, I do actually have the pinout for this one and it matches up. Um this is the uh clock going in here and this is the data for

**Dave Jones:** the debug interface. So, clock and data. I've discovered that this one here is uh VSS or ground and this one here, or pin uh three here, is actually uh positive. So, ground and positive rail here. But the QFN pinout is like shifted one pin

**Dave Jones:** around so that pin 64 here is the ground and then this one's the clock. This one's the data and I've uh in and in this particular case, pin two is actually the reset pin. So, aha, we've found the re- reset pin. It buggers off

**Dave Jones:** under here. Does it go over to there? I don't know. I can buzz that out. VCC goes through that zero-ohm resistor to there. So, what I can do now, powering it through the debug interface, we can measure the voltage rail there. There

**Dave Jones:** you go. So, 3.5 V. We can look at pin two, which I have verified is the reset pin. Got to be careful when you probe here. Don't want to short anything out and it I know it's an active low reset.

**Dave Jones:** And there you go. We're actually getting 3. 3 volts there. Yeah, it's not being processor not being pulled in a constant state of reset, but that doesn't mean that there's not like a failed capacitor. I'm going to actually follow

**Dave Jones:** that reset trace. In fact, I'll just probe, make sure that it is going to where I suspect it is. Yep. And I know it's that via going out there. So, I just whack a light under that. Jeez, need to turn that down a

**Dave Jones:** tad. There we go. That one. So, that's going out there. Aha. There's your reset cap going down to ground. Could that cap be failed? Hang on. I think I traced the wrong pin. So, that's another tip. Just be double-check

**Dave Jones:** whether or not the trace that you tracing is the one you're tracing. If that makes sense. Yeah. I goofed that. It's this one here. I Yeah. I was way off as the reference. I took those four pads as the reference, not

**Dave Jones:** those four pads as duh. Yep. You're probably screaming that at home. Right. So, this is the reset line here. Aha. A diodey. So, let's actually measure that. Yeah, diode's okay. No wackers. Turned around the other way. Yeah. Okay. Easy to test and rule out

**Dave Jones:** actives like that easy to Usually diodes will test in circuit like that. And then there's something going off over to here as well. But once again, like our reset line isn't being held low. So, the processor isn't isn't not

**Dave Jones:** being actively reset. The data sheet definitely says active low. Yeah, it ain't that. Anyway, might be chasing a red herring with the reset line, but you know, you just want to make sure because if there's a cap that's pulling it low,

**Dave Jones:** and that cap is, you know, it's it's open, then which is a fine mode for caps, they can fail short and open, multi-layer ceramic caps. And if it fails open, it doesn't get its power-on reset, that could cause a problem. Okay,

**Dave Jones:** I just discovered that when I I can switch the power off from the programmer when it goes into that programming mode. So, what I can do is I can adjust the time base here, make it short, 20 milliseconds and

**Dave Jones:** there's 50 milliseconds per division, something like that. I can single shot capture that, then force the programmer, there we go, two reset pulses. That's interesting. Let's compare that with a good one. One reset pulse. Isn't that interesting? There there is no reset

**Dave Jones:** line from the programmer. Um that's according to the pinout on the programmer. So, that's very interesting, but in any case, that is not an RC like power-on pull-up reset pin on the micro. This is the direct reset pin.

**Dave Jones:** There you go. So, yeah, there's there's something active. Hmm, there's not like a reset chip or anything on here, I don't think. Aha, that's interesting. The reset line is connected to there. The plot thickens. According to the programmer pinout, that is actually VPP.

**Dave Jones:** Okay, so VPP go is the reset line on the programmer. Okay. Right, that makes sense. Um I didn't think there was like an active reset circuit, cuz like a lot of times you can get, you know, from TI and a

**Dave Jones:** whole bunch of other makers, you can get like active reset circuits, which cleanly give you a reset pulse when you power on, as opposed to relying on a RC power-on. So, obviously, um yeah, it's it's getting the pulse. So, that's

**Dave Jones:** probably why there's two pulses there is, cuz that's the programmer just going and it's it's trying to reset and then it doesn't get anything and then it resets again and it's just trying itself over and over, as we've seen with the

**Dave Jones:** clock and data. Whereas the good unit, when we hook the programmer up, it only it it does its thing, reads the chip ID and then stops talking. Right, so at this point, I know that the processor is getting clock, data and

**Dave Jones:** getting reset as well, which is the programmer's VPP. I don't know if it actually does a VPP function and actually like pulls a VPP is a programming power. So it's, you know, old school is like 12 volts, even 24 volts, something like

**Dave Jones:** that, you know, but it pulses it to a higher voltage. I don't know if it actually does that. I don't care. It's not reading out the chip data. So the the the debug interface is getting everything. So the chip's getting its

**Dave Jones:** power and it's getting clock, data and reset from the debug interface and it's not talking. So, once again, the only conclusion I can come to, like I did in the first video, is that that processor is bunk. Possibly, I'm

**Dave Jones:** going to have to find a uh donor unit and try and remove that and then um solder on another one from a known donor unit that actually talks to the programmer. If it can't talk to the programmer, that's the whole fault.

**Dave Jones:** Yeah, obviously, I'm not going to debug the multimeter in any other operational regard. There's just no point um when it doesn't go directly from the debug interface like that. And that's basically it's bypassing all the power on, any sort of like power on reset or

**Dave Jones:** anything like that. It's it's being controlled from the debug um interface and it's just it's not doing it. All right, I have actually found a donor unit. Let's actually remove this. Put some flux on here. All right, let's see if I can remove

**Dave Jones:** this. Bingo. Didn't damage anything there. Nice. Do the same thing for the dead chip. So, we won't be able to do any more debugging on this, I'm afraid. I am pretty done on that. Sorry, my Tiguan is not going to

**Dave Jones:** be able to view this. Tada! There we go. So, that's the faulty one. No pads were harmed in the filming of this video. If you're wondering what flux I'm using, it's an Edsyn FL 911. Seems to work for

**Dave Jones:** me. Your mileage may vary. Now, I've got to make sure I put the right chip in, and I've got to make sure I get pin one over here. Put that on. I might just uh wick off some of the solder on those

**Dave Jones:** pins. Oh, why you could see that wick straight off there. That was nice. Seems to be a couple of shorted out pins on there. But, I'm not going to Oh, that one pin over there has been a bit bent.

**Dave Jones:** And I'll tack pin 64 over there. Decided not to reflow this. Just do some drag soldering. And we go. Just give those a little dab dab. And they should be soldered nicely. It's not pretty. Um in fact, there are a couple

**Dave Jones:** of pads over here which I don't think they go anywhere. They were lifted off. Let's have a look. Yeah, those pads don't go anywhere. So, they lift off very easily. And just the glue on this PCB material is not that good. So, yeah,

**Dave Jones:** they lifted off, but the chip reads. The chip reads on the programmer. No wuckers. And I was able to successfully program it with the latest version as well. But, if I plug it in in the programmer mode, it I do get insertion

**Dave Jones:** error. That means the processor is now working and the LCD driver is working. Whoop. Whoop. Something Something's reset itself there. Whoop. Look at that. There you go. So, we're just insertion error there. Something else is going on. So, I'm

**Dave Jones:** going to uh put that transistor back in there because there was nothing wrong with that. Okay, I'm just don't going to do a quick and nasty reflow of that old chip onto the donor board. Sorry, you can't see this.

**Dave Jones:** Okay, so this board did work before. It's got those pins look absolutely correct. Let's plug the programmer in. Boom. Yep, no chip ID. So, there you go. And I can buzz out those and definitely those pins are getting over there.

**Dave Jones:** Yep, everything's Everything's hunky-dory. I can measure volts on there. The mantis was in the way. I was using that to inspect and I can actually measure Sorry, you got to have got the on-screen multimeter at 3.3 volts. Yeah.

**Dave Jones:** So, that's confirmed. I transferred the faulty chip onto the donor board, which was powering up, but it sort of had like some other issues or something. I can't remember exactly what, but yeah, that was from a junk uh bin

**Dave Jones:** multimeter, but it did power on and work and you know, it programmed and all that uh sort of jazz. So, yeah, that's confirmed. I'm silicon failed. What what what what? No idea why, you know? If you got any idea, leave it in comments down

**Dave Jones:** below. Let's power it on. There it is. I was able to program that with the uh latest firmware uh 609. Unfortunately, there's an insertion error. I don't know what the insertion error is, so whether or not that was a fault

**Dave Jones:** that I don't see how it could cause the That's really annoying. It does that in all ranges. So, I think I've had that error before. Yeah, I've had a 40 meter with that before and I had to replace it, at least

**Dave Jones:** one of them. So, I I don't think I ever got that meter back. I never investigated, but there it is. Um it is repaired in that it now powers up. So, yeah, we definitely had a faulty processor in

**Dave Jones:** that thing. But, now it looks like there's something else wrong and it Well, that's it for this video. I'm I'm done. I didn't actually want to repair this thing. I just wanted to troubleshoot down to find what the issue

**Dave Jones:** was and we definitely found a problem. Faulty processor and we uh replaced it. We We deduced that in the first video, but the second video, yeah, absolutely confirmed that and I put that chip back on the um back on the other board here and it

**Dave Jones:** buzzes through everything buzzes through fine uh from the programming header and it just doesn't does exactly the same fault as before. So, there's definitely a dead silicon there. So, there you go. Anyway, I've got myself a donor board

**Dave Jones:** now, which is kind of handy. And as I mentioned in a live show uh recently where I actually got people to guess and somebody did actually Well, a couple of people I think ended up guessing uh the goof up I made in that video. Now, a

**Dave Jones:** lesser YouTuber, of course, would have like hid that because they'd be too embarrassed to show that they made a goof like that. And well, you know, this kind of thing I I can't tell you the mindset I was in when I

**Dave Jones:** um started thinking that was the DMM chipset. It's obvious just from the topology, as I I explained in the live video, just the topology of the uh thing. It was It was really obvious, but no one in the

**Dave Jones:** comments picked it up. I'm absolutely surprised. That's one of probably my first video ever where I've made a major goof like that, major embarrassing goof, and nobody's actually picked it up until I prodded some people, "Hey, there's something wrong." And they started to

**Dave Jones:** put their thinking cap on it. Yeah, um there you go. So, I hope you enjoyed me leaving in the goose like that. It shows that these things happen. Probably wouldn't have done that um well, wouldn't have happened if I had a

**Dave Jones:** schematic. And it wouldn't have happened if I probably wasn't shooting a video. Shooting a video is like different level of stuff. Your mind gets all, you know, anyway. Anyway, whatever. Um there it is. It was confirmed 40 processor. So, yeah, that that insertion

**Dave Jones:** error, I don't know. I might leave that for another video if I've got the time and motivation. So, anyway, I hope you learned some valuable lessons from that video. If you did, please give it a big thumbs up. And as always, discuss down

**Dave Jones:** below. Catch you next time.
