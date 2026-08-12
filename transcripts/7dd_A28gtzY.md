---
video_id: 7dd_A28gtzY
title: EEVblog #538 - HP35670A DSA Repair - Part 2
url: https://www.youtube.com/watch?v=7dd_A28gtzY
source: youtube-asr
---

**Dave Jones:** Hi. Welcome to another repair video for this classic HP 35670A dynamic signal analyzer. And if you haven't seen part one of this video, I'll link it in down below. Yes, this is part two in a series, maybe. Depends how

**Dave Jones:** long it takes me to fix this thing. Repairing this unit or attempting to repair to attempting to repair because we don't know if it's you know, whether or not it's beyond economical repair or whether not it's going to just require another 5-minute

**Dave Jones:** video to fix. I have no idea. But I had a lot of people comment on it, can I do extra videos fixing this thing? And yes, that was my intention to do videos until it's repaired or until I decide

**Dave Jones:** it's just not worth the effort. So, here we go. I'm going to have another look at it, another crack at it. Now, to recap what happened last time, we have a known faulty power supply, which presumably took out best guess

**Dave Jones:** took out a 7912 -12 V regulator on the digital board, and that stopped the oscillator working. So, we have got to the point where the unit does actually power up and runs through the software. So, all the digital part of it's working fine. But

**Dave Jones:** we're getting error messages on there saying that the ADC ASIC has failed. And a lot of people said, "Well, let's go push the ADC ASIC back in the socket and all that sort of thing." No, I don't think that's going

**Dave Jones:** to be the case. Or it could be, but I think the most probable scenario of what else is wrong with this thing is, well, more power supply stuff because we've had a known fault in the power supply and at

**Dave Jones:** least one failed voltage regulator. Usually, they're pretty reliable, and usually the failure mode is a you know, a high voltage on the input, which could be caused by a failed mains power supply, which we know we have. These are known faults.

**Dave Jones:** So, rather than chase our tail, chase red herrings, and follow the service manual for the rest of this thing, that whole 70-page troubleshooting guide for this thing, you're going to take a step back, think about this, and go, "Well, what's most

**Dave Jones:** likely to be wrong with this thing? Is it actually the software tells us there's a fault with the ADC ASIC, but hey, you know, if there's no power going to the ADC ASIC, then you're probably going to get exactly the same error message."

**Dave Jones:** So, it's I reckon I would Well, where I would put my money on is that we have more failed voltage regulators on here somewhere because apart from the 5-V rail on this thing, which we know is good, and all of our

**Dave Jones:** digital logic is working, so it's unlikely that the failed switch-mode power supply has taken out anything on the 5-V rail on any of the boards. So, that's the only one which is powered directly from the mains power supply.

**Dave Jones:** The others are the This has plus minus 18-V rails and an 8-V rail, and I think and a 12-V. Yeah, and a 12-V rail as well. Now, the take the plus minus 18-V rails, for example, they aren't powering

**Dave Jones:** the op amps on all of these analog boards directly because a design of a unit like this needs to have low noise on the power supply, so it's going to locally regulate those on the other cards, like this one, for example,

**Dave Jones:** which I've just taken out. And sure enough, tada! I'll show you this in closer detail, but we have some local on-card regulation. I'm not even looking at the service manual, but first port of call is to measure those

**Dave Jones:** regulators and see if it's failed, cuz if we've taken out one voltage regulator, there's a very good chance that we've taken out some others as well. So, forget the service manual. I smell some faulty regulators. Let's go. Now, of course, the absolute first thing

**Dave Jones:** I do, golden rule of troubleshooting, thou shalt test voltages. So, what I've done is to access all of the voltages coming out of the power supply here via this ribbon cable. I've just taken the ribbon cable out because it's not Once

**Dave Jones:** it's on this motherboard, gone over this cable on the motherboard, yeah, it's not real easy to probe. I can probe the 5 V going under here, but how do I probe the other voltages? So, I just disconnected that. I have powered

**Dave Jones:** it up and I have measured the voltages and uh here they are. Thankfully, the service manual provides a chart telling you what pins are what, but basically we've got the uh plus 18 V supply here, measured 18.3, minus 18 V supply, minus

**Dave Jones:** 19.3. Uh you know, it's a bit high, but it's neither here nor there really because this 18 V rail, as I said, is probably not powering anything directly. It's just going into local uh say 15 V regulator or uh something like that to

**Dave Jones:** power the uh local op-amps. So, really 19.3, I'm not going to lose any sleep over that at all. It's not worth chasing that. There's nothing doing there. Plus 12 V rail is uh 12.3 V. The plus 8 V

**Dave Jones:** rail, it's a little bit low, 7.7 V, but once again, that plus 8 V is probably doing doing some local 5 V regulation. So, plenty of margin there, you know, 2 V drop on a standard 7805, something like that. And we've already measured

**Dave Jones:** the 5 V in the previous video, and it's just hunky-dory. So, everything coming out of the main power supply here is just fine, but of course, this is the repaired power supply. So, the original one likely could have well, we can think

**Dave Jones:** it's taken out that uh 7912 voltage regulator we had in the previous video, and my guess is it's probably taken out some others as well. I'd probably surprised if it hasn't. Now, here's the um analog uh processor uh board here and I haven't

**Dave Jones:** checked the service manual, but presumably that is the ADC ASIC that they're talking about there, the Actel um FPGA there. So, I believe that's what they're talking about and you can see that we have three on-card voltage regulators there.

**Dave Jones:** And if we have a look here, we've got uh some test points, minus 15 V here. So, as I said, the minus 18 V it's just regulating that down to minus 15 V. We have plus 15 V here. We have

**Dave Jones:** minus 5 V here. And we have well, plus 5, we don't need to measure cuz it'll be coming from the same point. There's no So, we've got three regulators there um powering uh those particular rails. So, first thing we need to do is measure

**Dave Jones:** those, but unfortunately, the really annoying thing is is that because this is a plug-in card, I can't just uh you know, once we slide that in there, we can't access those anymore. So, uh but thankfully, it's got these nice test

**Dave Jones:** posts. I'll just whack some alligator clips on there, have those coming out uh just laying on top of the board. They'll be able to poke out through the side here and we'll be able to plug these in those into our meters,

**Dave Jones:** no problem at all. Let's measure them, see if they're any good. Actually, I just realized that I missed one there. That's actually plus 5 V A. So, A stands for analog. The other plus 5 V is here and that would be

**Dave Jones:** coming, as I said, directly from the main power supply there, but this one's a plus 5 V and there is the tiny 78L05 to go along with that puppy. So, I need another probe on there. So, I'm going to

**Dave Jones:** be probing four different voltages. All right, here we go. Let's power this sucker on. I've got the ribbon cable back in. Uh ground is coming from it's uh going to be one common ground for all of them. Now, what I've got here is uh

**Dave Jones:** plus 5 V analog, minus 15 V, plus 15 volts, and minus 5 volts here. So, let's do I don't know. Let's do that plus 5 volts analog first. So, we'll plug that in. And yeah, we're getting plus five. So,

**Dave Jones:** our analog, that little uh TO-92 package um low power regulator is just fine. So, our analog now we've got our negative 15 volts. Hello. Yep. Oops, it looks like we have a shorted pass transistor um in that uh puppy. So, it's feeding

**Dave Jones:** that minus 19. 19.2 volts straight through to the output of the regulator. Uh classic fire mode shorted There you go. So, you know, it it wasn't hard at all. Um my guess was correct. My hunch was correct. There we go, plus 15 volts.

**Dave Jones:** No problems at all. So, that one hasn't been taken out. So, we have an example of two negative voltage regulators being taken out on this thing. So, it looks like that one rail. So, um I think this one here this

**Dave Jones:** uh minus five uh no, the minus five should be okay. But no. Hello. Minus five is minus 1 volt. So, it looks like we have now three failed negative voltage regulators. And of course, one other thing I'm going to be

**Dave Jones:** looking at here these dip tantalum caps. Um these can fail quite easily in um over voltage uh situations. So, you've just got to be uh careful visually check those. They can be really nasty. But they you know, visually they look just

**Dave Jones:** fine. So, um I think no problems there with the tantalums. But you just got to keep that sort of thing in mind. And if we have a probe with this negative uh 15 volt regulator here in and out, as

**Dave Jones:** I said, shorted pass transistor. So, yep, there we go, 0.3 ohms between inputs and out. And before I rush down to Jaycar and pick up some regulators cuz I don't have any 7915s in stock here, well, let's just take a look

**Dave Jones:** at the main analog input board and bingo, look, we've got some more regulators as well. Minus 15 volts. These aren't the same though. These are LMR337 and LM317. Whereas the other ones aren't the adjustable type. They're just the fixed

**Dave Jones:** 7800 series and there's a plus 5 volt one here as well. So, I'll whack some probes on there and we'll put this card back in and just measure this board here. And we've got two other TO220 packages here and here but they're

**Dave Jones:** transistors. They aren't actually linear regulators. And our 5 volt rail there is just fine. And let's have a look at this should be negative 15 volts. Aha, -16.5. So, there you go. Yeah, that one I don't like the look of

**Dave Jones:** that at all. Well, the test point is labeled 15 so it is an LM317 of course which means that the resistors could be out or it could have been trimmed to that or you know, actually set to that but yeah, I don't like it.

**Dave Jones:** It should be minus 15. It's likely the regulator's gone and plus, well, there you go, 16. You could argue that that's 16.5. They're suspiciously close to each other so I'd say that's not a fault at all. I would say that's they've been

**Dave Jones:** deliberately set to 16.5 even though the test points are 15. That would be my guess and it turns out my hunch there was right on the money cuz if I flip the board over and have a look at the

**Dave Jones:** resistor values here and here, which set it, they're both the same 237 ohms and 2.87 K, and you whack that into the formula for the LM317, and you get about 16.4 volts. So, there you go. It's not set to 15 as it actually says on the

**Dave Jones:** test points there. So, yeah. Just got to watch out for stuff like that. That could leave lead you up the garden path, it wastes time and effort.

**Dave Jones:** And yes, we have got a couple of these wimpy thin tab ones. Cost-cutting bastards. And these ones actually have a solder tab on the underneath of the heat sink there, so the heat sink just it's a slide-on type,

**Dave Jones:** but then secures down with a single tab. And really the easiest way to get these out, if you know it's a dimension you don't want to use it again, just get in there and slice the pins off and then

**Dave Jones:** just heat up and pull the pins out one by one. Then you don't have to worry about heating up all three at once or doing the you know, the sideways dance, putting sideways pressure on it and then heating up the joint. Bugger that.

**Dave Jones:** And then of course, you just want to wick the holes out. Apply some more solder on there if you really want to, but there we go. Don't pull them don't wipe them across or anything like that. There we go.

**Dave Jones:** Uh almost. That one had a bit more solder on it than we anticipated, and uh bingo. Three nice holes. And just to check that shorted pass transistor in there. Here we go. Hello. 10 meg. LOOK AT THAT. HOLY

**Dave Jones:** CRAP, it's not the regulator. What do you know? Hmm, protection diode? Let's go to the board. There we go. We've got a crappy little, like, you know, 4148, uh, type signal diode there going between the input and output of that.

**Dave Jones:** So, let's, uh, let's measure that and see if that's the sucker that shorted out. Sorry, this doesn't show up very well on video, does it? No, input and output. There we go. We're still getting the 0.3 ohms we got

**Dave Jones:** before. So, almost certainly that diode. Well, let's hope it is. All right, I've lifted one end of that diode there. So, let's measure that again, and I can't see what else it would be. Yeah, bingo. Look at that. No problems

**Dave Jones:** whatsoever. So, it looks like, uh, our mains power supply, in this case, I don't know if it's taken out the regulator. It could have. So, you would have replaced them regulator as a matter of course, you know, considering that

**Dave Jones:** you've already got it out, and it's, you know, a dollar to whack another one in. You'd just put it back in. You wouldn't bother testing it. But, yeah, took out that little, uh, reverse protection diode there. Little piss ant thing. They put in a big 41,

**Dave Jones:** uh, big 4001 or something, probably would have survived. But, of course, you have to wonder whether or not, um, that bigger is, you know, we were getting, uh, that 19, -19 volts directly on that -15 volt rail, and it's been

**Dave Jones:** there for some time that we've had all this powered up, and presumably when it failed as well, went through. So, hopefully, uh, we haven't, uh, blown up anything on that 15 volt, -15 volt rail attached to there. Um, it looks like the other

**Dave Jones:** regulators have just gone pop, you know, the pass transistor, bang, and, you know, and it's they're reasonable at actually protecting the circuitry they're powered to. But, this one, because it's gone to the effort to short that, output diode as well, well, yeah,

**Dave Jones:** hopefully not too much abuse on that minus 15 volt rail. Well, only one way to find out, replace it all and power it up. And that is a National Semiconductor. It's got 10 050 505 on it. Eh, not your standard 1N9144148

**Dave Jones:** by the looks of it. Could be offhand I don't know that part number. Okay, they've all been replaced. Let's power it up. And that's the minus 5 volts. That's working just fine and dandy. Fixed. Minus plus 15 which we had no

**Dave Jones:** problems with before. And minus 15. Brilliant. All right, I replaced that diode with just a 1N4148. Should be good enough. Whatever it was, whether it you know, signal diode or zener diode, whatever. It's going to be good enough for a to

**Dave Jones:** get this thing working again. And there we go. Let's plug in all the cables and power the thing up. See if we still get that error message. It's booting system. Recall state. We may have to uh run through it like clear the log and

**Dave Jones:** all that sort of stuff, but here's where it failed before with that ADC error. So, let's see if it uh still does. Calibration in progress. Oh, hardware error. See fault log. Okay. Well, yeah, calibration file change state. Yeah, blah blah blah. Calibration, we'll

**Dave Jones:** turn that off and system utility, more fault log. Uh ADC I2C no device acknowledge. Your calibration file. Okay, no more ADC file which we were getting before, I believe. Um so that could have fixed that. So, let's now run in let's go into the

**Dave Jones:** self-test. Self-test and quick conf Let's run the quick confidence test that we did last time and we've got a whole bunch of failures.

**Dave Jones:** Failed. What? There we go. All right, we still have ADC gate array. There we go. Looks like I think we're still going to Yeah, gate array failed. Bugger. Bugger. I thought that I was reasonably confident we we're going to fix that by

**Dave Jones:** fixing our power power rails, but what? Murphy gets us again. Well, the next thing I did is just take this board back out and just feel around the main chips to see if there's anything that's you know, overheated because it's

**Dave Jones:** been taken out by the that minus 15 volt rail because we don't have the schematics don't exactly know what things on here are powered, but now you know, there's nothing obvious. There's a whole ton of op-amps here which are presumably, you know, plus

**Dave Jones:** minus 15 volts a pop and uh No, nothing obvious. There's a Raytheon chip there. Woohoo, you don't see Raytheon chips that often. Other thing to do is check that we're getting SCL and SDA. There's some test points on the

**Dave Jones:** board and yeah, sure enough we get something there. Let me change to another test point. Should use multi-channel, but uh couldn't be bothered. There we go. That's looking like it's doing something and then we've got 10 MHz and uh 20 MHz

**Dave Jones:** test points for the ADC and stuff. So, yeah, look at that. Wait, there we go. It's dodgy because I've got um these ultra long leads coming out of here and it's just man it just and the ground's going over to the digital board

**Dave Jones:** and the loop in there is absolutely ridiculous but all we're checking here is that we're actually getting a signal there and sure enough 20 megahertz and 10 megahertz cuz sometimes you're not after the signal you don't care about the signal

**Dave Jones:** integrity you're and that's that looks like 10 yeah 10 megahertz so we're getting our data there um you know that's there's a few other test points on there I'm not sure what they do I would probably have to look up the

**Dave Jones:** manual and troubleshooting guide for that but it looks like it's doing stuff and I'm not particularly encouraged by the constant overload leads on the input there that indicates something something wrong I mean these things have a dedicated overload and

**Dave Jones:** half rail circuitry in there so to have and we've got that sort of flashing down there periodically for the half rail so they've got like dedicated you know op-amps and dedicated comparator circuitry in there to actually detect that stuff and well those leads are

**Dave Jones:** coming on you know that's not like the processor turning those on or something like that that's all analog stuff so that's not good and I'm getting nothing on the source output either I'm in the leads coming on for the source output I

**Dave Jones:** mean it looks like we're getting something there but trust me whether or not I turn that source off or on one volt peak sine wave or different types of output waveform not nothing so source ain't working well what can I say I

**Dave Jones:** tried yeah there's going to probably be some more videos run out of time yet again this is all I'm going to do for today but hey we found a couple more negative voltage regulators failed so clearly that power supply the original power

**Dave Jones:** supply fire on that negative 18-V rail has taken out at least three voltage regulators, but all the other rails look fine. So, we're now and we're getting the exact same ADC Gator array error now. So, I don't know. Now, I'm getting, you

**Dave Jones:** know, a bad feeling about that minus minus 15-V rail, which went to minus 19. Shouldn't be a huge deal, but you know, that diode was shorted out. So, all that power was going through there into the analog rail. So, hopefully it hasn't

**Dave Jones:** taken out too much, but maybe we have to go back now to the troubleshooting guide cuz once we check your power rails, then you'd go systematically back through to your troubleshooting guide. That's probably what we'll do next time and

**Dave Jones:** hopefully we'll find the sucker, but anyway, I was really hoping that would fix it. I was, you know, pretty confident, sort of, you know, 80% sure that fixing those regulators would would do the trick, but no, clearly not. I've tried to press

**Dave Jones:** that ADC ASIC back in the socket and and no, nothing. So, oh, well, the saga continues. Catch you next time.
