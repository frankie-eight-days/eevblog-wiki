---
video_id: ezr3CzGUVeQ
title: EEVblog #663 - Compucorp 322G Calculator Teardown
url: https://www.youtube.com/watch?v=ezr3CzGUVeQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 26, "2": 41, "3": 61, "4": 81, "5": 96, "6": 116, "7": 136, "8": 151, "9": 166, "10": 181, "11": 191, "12": 206, "13": 226, "14": 241, "15": 261, "16": 286, "17": 311, "18": 326, "19": 346, "20": 361, "21": 376, "22": 386, "23": 406, "24": 426, "25": 446, "26": 471, "27": 491, "28": 506, "29": 521, "30": 541, "31": 561, "32": 586, "33": 601, "34": 626, "35": 641, "36": 656, "37": 671, "38": 686, "39": 706, "40": 726, "41": 741, "42": 756, "43": 776, "44": 786, "45": 801, "46": 816, "47": 831, "48": 856, "49": 876, "50": 891, "51": 916, "52": 941, "53": 956, "54": 976, "55": 991, "56": 1011, "57": 1021, "58": 1046, "59": 1061, "60": 1076, "61": 1096, "62": 1116, "63": 1131, "64": 1151, "65": 1171, "66": 1196, "67": 1231, "68": 1250, "69": 1265, "70": 1285, "71": 1305, "72": 1325, "73": 1335, "74": 1355, "75": 1380, "76": 1395, "77": 1420, "78": 1435, "79": 1470, "80": 1510, "81": 1535, "82": 1555, "83": 1575, "84": 1590, "85": 1605, "86": 1635, "87": 1650, "88": 1670, "89": 1690, "90": 1710, "91": 1730, "92": 1745}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We've got the CompuCorp 322G Scientist, well, programmable scientific calculator dating from 1973. So yes, that makes it more than 40 years old. Fantastic. Thank you very much James from Sydney who saved it from the Sydney University dumpster. And you've seen

**Dave Jones:** this in a previous mailbag, he sent it in. And it's just a beautiful looking device. There's something sexy about it. It's keys on it are absolutely horrible. Some of the worst spongy keys I've ever found in my life. But I don't know, it just looks really quite neat.

**Dave Jones:** I like it. And it works on four D cell batteries as we saw. And I tried to power it up in the mailbag video, but yeah, it drew like much more than it's rated. Current of 1.3 amps when I tried to power it.

**Dave Jones:** 7 volts through the jack there. But anyway, it is a beautiful machine. 1973 vintage. It's got a gas plasma display manufactured by Burroughs, I believe. So anyway, it should be a real interesting sight. Let's take a look. There's going to be lots of discreet stuff in here I suspect.

**Dave Jones:** And I can see inside the battery compartment, moldy board construction. So let's get into it. And here we go, it already came with these screws undone. There were just two more in the battery compartment there, so let's crack it open. And hey, we're in like Flynn.

**Dave Jones:** There we go. Oh look, you can see the nipple there on the gas plasma display. Doesn't that look? Doesn't that look nice? There we go, that instantly dates it. There we go, the 48th week. 72, that display was manufactured. Got a couple of, oh no, no, they're nuts.

**Dave Jones:** I thought they were trimmers there for a second. No. A couple of nuts, so it's hey, yep, the whole thing just lifts out. Look at that. There we go. Hey, not as, not as discreet-y as I imagined. I expected like a whole bunch of dense TTL stuff, but it

**Dave Jones:** looks like it's just, looks like we're going to have some LSIs in there that do all the magic. So presumably I've got to take, I might have to, yeah, I've got to take out little spring washers there off the, off those and the boards will just lift out.

**Dave Jones:** Now what's interesting at first glance is, look, they've got like the plug-in card edge connectors over here, and they're not actually connected up. There's nothing in the case or anything like that that joins them together. There's no bus on the end of it,

**Dave Jones:** or no backplane on the end of it that joins these boards together over here. So that must be for production testing, I would presume, that they can you know, like plug those boards into a test jig in the production factory and test them.

**Dave Jones:** That would be my guess anyway, but this is how that they're, this is how they're joining the boards together using this stack arrangement here, and they plug in. So this is like a backplane connector, you can see the cards just slide into there like that.

**Dave Jones:** Oops, sorry, I've had my camera white balance switch to auto, so the colours may not have been perfect in the previous things. That was from the trade show that I went to. When I go to trade shows on site I just whack automatic white balance on.

**Dave Jones:** Anyway, it's fixed now. So here we go. There's the 16 digit gas plasma display, that looks really quite nice. And of course this whole thing just lifts out like that. We've got a flat flex going over there, it's multiplexed of course. And well

**Dave Jones:** let's try and get all these boards out of here and see what we can get. And here you go, we're in. There's the two main custom LSIs, and I'm not sure why I sort of expected this to be chock full of like a, you know, TTL

**Dave Jones:** or other, not necessarily TTL, but like chock full of logic, I don't know. Anyway, that's the back of the keyboard there, keypad. So that's got Teledyne Kinetics Series K patent pending. Thank you very much. I think your patent's expired by now. But yeah, these are manufactured by

**Dave Jones:** Texas Instruments and they're, you know, clearly, and there we go, clearly custom LSI chips. There we go, dated 29th and 34th week 1972. So all the magic happens in there and not much else. We've got some UMP480s, they're obviously driving, I don't know what they are off hand, but and a whole bunch of transistors, they're obviously driving

**Dave Jones:** the gas plasma display up here. And we've got some funky looking old school foil caps in there, and well that's about it. Double, all double sided board, just all tin plate, nothing fancy going on there at all. A few diodes, a few resistors, and nothing obvious

**Dave Jones:** blown yet that I can see that's causing the issue. By the way, boards are tied together with just these, so there's only a couple of like a, apart from the big parallel connections on the back, they've obviously got I don't know, some sort of power or something going over there.

**Dave Jones:** Why they didn't put it all on the card edge connectors at the back, I don't know, why they still need to do that. Not a bit disappointed, not as dense and impressive as I thought. It takes all the shine off it when all the logic's inside a couple of custom LSI's you'll never

**Dave Jones:** get the data on. And they've obviously got a compression fit on these card edge connectors over here, because they wouldn't budge until I loosened all that. And there we go, they all come apart. I'll show you that in a second, but obviously that has got, you know,

**Dave Jones:** they're using all the contacts in there to get power through. They've got some logic on there. But apart from that, the bottom side here, woohoo! And if you're wondering why they've shorted out all these contacts here, because this slides into the, and there'd be pins on

**Dave Jones:** the bottom there shorting out. Well this is just one big heat sink. You can see the screws there, they've got some Loctite on those, and they're just these little power transistors there. And they're just heat sinking those. So this is the power supply board.

**Dave Jones:** And you know, not a huge amount doing here. Looks like we've got an inverter for the gas plasma display. Hence, you know, that separate cable we saw jumping off to the main one. And here's our power input here. So maybe there's something wrong around here.

**Dave Jones:** That could be possibly why it's not working, or when you power it from the batteries, or it's drawing too much current when I power it from the plug pack. So, well apparently. So there's got to be something wrong on there. And of course this is a battery-powered calculator, even if it is D-cells.

**Dave Jones:** So they've sprung for the 74L series here, the low power TTL stuff. Beautiful. And here's our memory board. Take a look at this, we've got ourselves ROM and some RAM here, and obviously some sort of memory controller ASIC, once again all designed by, well manufactured by TI.

**Dave Jones:** Yep, 39th week 1972. And these are obviously our program ROMs here. No, they're not EPROMs, because there's no window on there. They've definitely got those soldered shut. So they're definitely write once ROMs. And check it out, we have an Intel P2102. We've got four of those, and

**Dave Jones:** that's going to be the RAM for this thing. I couldn't immediately, I know it's an Intel SRAM, but I don't know what size. So this thing has 80 program words of memory, so obviously it's got to have some, unless something built into the process in ASIC, which we'll

**Dave Jones:** see. Obviously the process is going to have some registers and stuff like that, so I'm not sure if this is just storage memory or whether or not it's actually used for intermediate calculations and stuff like that as well. But yeah, 80 program steps.

**Dave Jones:** So it's got to at least store that most likely battery back there. Or I don't see any sort of diode kind of thing happening for the power on that, but that would be, I mean they've got to keep the contents of that when you turn the thing off.

**Dave Jones:** Otherwise, well I believe it's got non-volatile, actually I'm only assuming. I don't actually know whether or not it keeps the contents when you turn it off. Kind of be stupid to have to reprogram in your 80 step program every time you powered it on, but I don't know.

**Dave Jones:** Could be. And this is actually our main processor board. So those two Texas Instruments ASICs we saw on the display board, they're probably like, you know, a display controller. It could be additional processing as well. But yeah, here we go. I mean I've got 07, 06,

**Dave Jones:** 05, 04. Let me check. Has the other one got 03? I don't remember. Yeah, 02. There we go. 02 and 08. So this one, there we go. 03. Where's 01? So they've got at least four chips to do this, and the processing architecture, I don't know.

**Dave Jones:** You know, whether it's a 4-bit, 8-bit, or whatever, or 64-bit processor, I have no idea whatsoever. If you do, please let us know. If you've got any specially internal block diagrams, you know, architecture information on this sort of stuff, please let us know.

**Dave Jones:** So this top display board here, they actually call that the D-scan board. All these boards are labeled, but yeah, I guess that's display scan, right? So obviously they are the two display multiplexer, you know, processors. They probably of course would contain registers to handle the display data.

**Dave Jones:** So the processor would just offload the data, and then this would handle updating the display and keeping it multiplexed. So that's, you know, that's that entire board. I think it's just dedicated to that display stuff. So it really is quite a nice modular design here.

**Dave Jones:** I mean, you know, they made it easy to service, to test. As I said, you know, they've got these test card connectors on the side, so they can probably test all this jazz. So we've got our display, and then we've got our main

**Dave Jones:** processor board. I mean, look, there's bugger all on there. Look at that. I mean, there's no, even well, they've got some, I presume that's bypassing on the one input there, but there's like, they don't even bother. The thing's probably so slow, it's probably running at, you know,

**Dave Jones:** hundreds of kilohertz or something like that. They're probably, you know, not worrying about bypassing. That's why you won't find them on any of the other chips. So that's the processor. And then the memory board over here. Look, you know, there's no decoupling here, it's just

**Dave Jones:** not fast enough. It just doesn't need it. And then a power supply board. So very nicely modular, and they can plug it in and test the damn thing. So that is really quite a nice modular bit of kit. And then there is our press-together.

**Dave Jones:** Check that out. There we go. Our press-together card edge connector. So presumably, like, the contacts are just shorted from one side to the other. I'm, don't know, I'll have to measure that. So let's test that theory. That the top of here goes to the bottom of this one, and yep, it

**Dave Jones:** does. Check it out. Yeah, that's just not coincidence there. Yep, there you go. So that's how it's designed. So the, like, the top of, sorry, the bottom of this top board here goes to the top of the board below it, and then so on.

**Dave Jones:** So you'd have to design your board architecture and your pin-outs to match that sort of stuff, but that's how they get the data between boards. And it's all sandwiched together, and once you screw that on, it actually becomes quite a rigid structure that holds the board in place.

**Dave Jones:** I don't mind that at all, that's quite novel. So I'm a little bit surprised at the sort of lack of density in this thing. Like, you know, I expected, like, all dip technology, of course, back then, but I expected it to be, you know, like, chock full of dip chips on each one.

**Dave Jones:** I expected sort of, you know, this total number to be sort of crammed onto one board, and I don't know, maybe they used a, you know, a four-layer board or something really fancy like that. But no, you don't have to when you go for all these ASICs.

**Dave Jones:** But they're certainly designed, and they had to split the processor up into four separate ASICs. So I'd love to know what the architecture is there that made them do that, and the display processor. They couldn't fit it in one, so they had to use two.

**Dave Jones:** Probably this is some sort of, like, gate array or something like that, so, you know, they only had a certain amount of logic and they had to design their processor using a custom gate array. So it's probably, like, a gate array chip. So it's not actually, probably not a custom ASIC as such.

**Dave Jones:** And what I've done here is I've powered it up. I know it draws, like, 2.4 amps or something, 2.3 I think, just irregular. So I've taken out the board. Taken out the power supply board here, so it's not powering anything. I've still left the

**Dave Jones:** gas plasma high-voltage display plugged in, and well, it's drawing 1.1 amps at the 6-volt, nominal 6-volt battery supply. Well, 6.8 watts just for a power supply sitting there doing naffle. Something's wrong. If I have a look at the output voltage from this inverter here, hey, there we go,

**Dave Jones:** 62 volts. There's another wire there. Minus 56 volts. Okay, now we're starting, now we're talking. So, yep. So you combine those, and yeah, that can be reasonably dangerous. So you don't want to go touchy-feely around there, that's for sure. So, you know, I don't know

**Dave Jones:** what it runs at, but hey, sounds, you know, it sounds reasonable anyway. It's a high-voltage inverter, so that works, but yeah, where that damn 1.1 amps is coming from, I've got no idea. Okay, I've disconnected that, let's see what we get now. And oh, bingo, look at that!

**Dave Jones:** So that display we're only getting, oh you can't see that, but only getting half a watt or 0.8, sorry, 80 milliamps. So, at 6 volts. So there you go, that display could be cactus. That, yeah, I don't know, is it supposed to take that sort of current?

**Dave Jones:** I don't think so. Because the rating on the back of the case here, it says 7 volts supply at 1.3 amps. So, you know, with everything, I'm almost getting that with just the plasma power supply hooked up. So, wah! Alright, now I've disconnected this display processor board over here from the display

**Dave Jones:** and we'll just power that on again and see what we get. Yeah, we're still getting an amp, so nothing to do with the gas plasma display itself. Something on that display processor board is chewing an amp. And I'll get my Breiman BM257 here.

**Dave Jones:** Very nice little meter by the way. Nice little compact meter if you're after a nice cheap one. And it's got a low impedance check function, so we can use that to drain the cap. I measured this cap here. It's got, during operation, the full 128 volts across it.

**Dave Jones:** So we can actually use that to discharge. Now cap on there, it's not going to hold a lot, it's only 0.5 mic, so you know, it's not much at all. So there we go, there's no voltage left on it, it's just going into

**Dave Jones:** auto mode like that. So yep, that's fine. Discharged, can safely work on it. So something has failed on here. What? Well, it's drawing excess current. So something is going to be shorted or loaded down severely. Diode test, there's a diode here. I mean, you know, here's our input over here.

**Dave Jones:** So there's no connections on the bottom, if you have a look at the bottom there. So it's easy to see all the traces going on top. I love tracing these, they're just, you know, so easy to do. And going over to the diode there.

**Dave Jones:** So first thing I'm going to check is that diode, that looks okay. No worries there at all, we're getting our diode drop. So that's fine. So yeah, we're getting a short somewhere else. The thing I'm going to test next, that main capacitor there.

**Dave Jones:** Although as I said, I measured the voltage on that, I was getting 128 volts. Switch that back to ohms, and give that a burl. As I said, we've discharged that, otherwise it's going to affect our resistance reading. No, there we go, 7 meg.

**Dave Jones:** And someone's calling me. Better go answer it. So that's exactly what you'd expect from a good cap, it's just going up and up and up. I mean, we can whack it into capacitance mode, but whether or not that's going to do any good in circuit, this is half a mic.

**Dave Jones:** So let's have a look. But it's not shorted. I mean, we're basically looking for shorts. So yeah, no, it doesn't like that. Maybe it's got some residual voltage on there or something like that. From the charge in from either from the original charge, it didn't discharge enough, or maybe from the resistance test function.

**Dave Jones:** It's obviously having a big issue with auto-ranging there, so we could... no, this one doesn't. We can't manual range our... oh, look at that! Auto-range only. Forgot about that. Oh, that's a bit annoying. Here, I was saying this is a decent meter. Well, it still is, but yeah, it doesn't let you manual range the

**Dave Jones:** capacitance. That's crazy. Anyway, next thing I'm going to check is the other caps. I mean, before we start mucking around with semiconductors, you know, these are... I don't even know the pin-outs. What is it, UHP 480? I don't know, and you don't know the pin-outs for the custom ASIC,

**Dave Jones:** so I don't really know where the rails are here as such. So let's start measuring some caps and see if any error... That's a pretty consistent 7 nanofarads there. There's probably nothing else in circuit there. Hey, there we go. There's 7 nanofarads a pop.

**Dave Jones:** And no, it doesn't like that one. That one's got something in circuit. We can go to our resistance range there, see if that's shorted out. Oh, 2k, you know, it could be something in circuit, so I'm not too concerned about that. I'm looking for gross

**Dave Jones:** shorts at the moment, so let's measure the other caps here. 7 nanofarads again, bingo. Alright, we should try and change the polarity on that one. That one is, again, looks like it's low impedance. 7 nanofarads, pretty close. So let's go back, measure this one again.

**Dave Jones:** Hello? Hello? Oh there's your problem! I'm dead short across that cap, so ouch! Ouch! There's, that could be an issue. We could have ourselves a dead cap there. 7 nanofarads. Yeah, it's 7. Doesn't like that one either. So, let's go back. No, that's

**Dave Jones:** 1.2k, but that one... Look at this, I originally thought, here's the cap, here are the three caps there, there and there, and it's the centre one that's shorted out, and I thought that track was at first glance going straight across to there, but it's not, it's cutting short, but look, that's pretty

**Dave Jones:** darn close down in there, isn't it? But it's not, but jeez. Yeah, there's no little bridge in there or anything, but maybe the top side, I don't know, we'll have to suck the cap out and see. Oh no, wait, look at the top side here.

**Dave Jones:** What's that little dag in there? Like that, that could potentially be shorting out, maybe. I'm going to get the knife in there and give that a little scrape. It doesn't look like it's touching, but jeez. Alright, so I've lifted that out, and there appears to be, I'll show you this

**Dave Jones:** close up in a minute, like a white residue or something on there, so. Yeah, that cap is definitely shorted, that ain't right, so yep, that, well, I don't know if it's going to solve the problem, but it definitely is a failure point. So check out that residue on that

**Dave Jones:** capacitor, and it's like, all the ones next to it have that residue on there, so yep, that cap is gone. Bleurgh. And you can see there's evidence of some of that on the bottom of this cap over here as well, so yeah, you'd just change that one as a matter of course

**Dave Jones:** too, even though it hasn't shorted like the other one. Alright, it didn't have any axial capacitors, but yeah, I had some radial ones, I'll just bend the leads. I've probably got some old axial ones somewhere, but probably not the right value anyway. 5600 puff, it's going to be near enough.

**Dave Jones:** I doubt that it makes a major difference. I changed the two that were leaking, I guess with that crap, white crap oozing out, so let's power it up. Hey, that's better. There you go, half an amp. Awesome! So that was definitely some of the current draw right there.

**Dave Jones:** So with all boards plugged in now, I'm getting you know, almost 2 amps, so that is higher than the rated current on the back there of 1.3. Hmm. And if I power up just the power supply board on its own with the display supply disconnected, we're getting

**Dave Jones:** 90 milliamps. So that's pretty much, you know, what you'd expect ballpark for the quiescent supply of something like this old school power supply. So you know, no problems at all. We're basically looking for gross excess current faults here. Let's check the power rail here.

**Dave Jones:** And across this main... main filter cap up here. And bingo, 4.9 volts, presumably it's 5 volt logic, and well, I'm happy with 4.9, that's certainly well within spec. So yeah, like, you know, 5 volt logic, they've got 7.4 TTL stuff in there, so you know, they're going to have a

**Dave Jones:** 5 volt supply everywhere you've got to presume, so that's okay. So all the logic is powered up. And if we have a quick little probe around here, there's our 5 volt rail. So that's doing hunky-dory. No problems whatsoever, there's no ripple on that.

**Dave Jones:** And we've got all this bus stuff happening over here. So let's start probing some bus. Hello! Hello, Mr. Signal at 10.1 kilohertz. Okay, there we go. Yeah, 10.1, yep. Oh. Hello, so it's working. Hello. Bit of rounding there. Look at that, 200, it's almost bang on 200 kilohertz, 203 kilohertz there.

**Dave Jones:** So we're getting some activity, so... ooh. Yeah, that's reasonably warm. Yeah, they're actually getting warm to the touch. Oh, that's gone negative. Yeah, there we go. Got a bit of negative stuff happening down in there, yep. But yeah, we certainly have some clock stuff happening, there's that 10 kilohertz and 200, so

**Dave Jones:** yeah, it's doing something. It's powered up and she's trying to work. Actually I just thought of something. The back of this says 7 volts at 0.7 amps, but that might not, it may not be able to operate from that. That may just be to charge, if you've got internal rechargeable batteries in there, that may just

**Dave Jones:** be the charging current circuitry. So yeah, maybe this, you know, I mean, clearly we found a problem, it was drawing excess current. We fixed that with the shorted cap and stuff like that, but you know, the 800 milliamps that we're drawing with all these

**Dave Jones:** boards in, well 850 could actually be right. And there might actually be nothing wrong with this, it might be driving, it may be just the display board or the display itself, which is cactus. And by the way, if you want to know what good a good continuity, quick

**Dave Jones:** continuity buzzer is, this one's pretty darn quick. You can, you know, if you're scanning for ground pins to find, on this top board for example, yes it's powered down. We can swipe along there like that. Bingo, until we got one right on the end.

**Dave Jones:** We got ourselves a ground pin right there. And if we... so I just soldered myself on a little ground test point there. I've got a resistor just hanging off there. It's a bit bodgy, a bit how you're doing, but it just allows us to get in here and probe around.

**Dave Jones:** And look, we've got some activity there. So that's a win, that's 925 hertz there. That's 5 volts, 2 volts per division. That's going negative by the way, so that's negative going. So there's lots of negative going stuff happening in here. And that's 10 volts, 5 volts per division.

**Dave Jones:** 5, 10, 15, so like negative 15 volts and stuff like that. So yeah, like there's data getting to here. And I checked a few supplies on the other supply rail and yeah, we were getting like a negative 15 supply and there was a plus 9 somewhere and you know, other stuff.

**Dave Jones:** But you know, we're getting nothing on the display and I presume that I don't have to you know, do some sequence to power the damn thing up. So I don't know. Yeah, I would have expected the display just to come on, but certainly getting some activity there.

**Dave Jones:** And some of those pins on that chip there, negative 150 volts, that's 50 volts per division. So yeah, serious business. Well unfortunately I think I'm going to have to call it quits there for today. And we got some progress on the repair of this thing, but who knows?

**Dave Jones:** You know, maybe it's just not repairable. I don't know. If anyone certainly has schematics for it, that would be very nice. So anyway, I hope you enjoyed that teardown and a little bit of troubleshooting there 1973 vintage scientific desktop, scientific calculator with a whopping 80 words of program memory.

**Dave Jones:** And it's a bit of a beast and quite simple. And as I said, if you do have any info on the gate arrays or ASICs used in this thing, please leave it in the comments as well. So I hope you enjoyed that, and as always

**Dave Jones:** you can discuss it over on the EEVblog forum, links are down below, and also there's a link down below to the high res teardown photos of this. I mostly take photos as I go along, and they'll be on EEVblog.com. Catch you next time.

**Dave Jones:** See you next time.
