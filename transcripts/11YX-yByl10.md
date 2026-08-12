---
video_id: 11YX-yByl10
title: EEVblog #1061 - Data IO Programmer REPAIR - Part 1
url: https://www.youtube.com/watch?v=11YX-yByl10
source: youtube-asr
timestamps: {"0": 1, "1": 21, "2": 34, "3": 48, "4": 61, "5": 74, "6": 88, "7": 103, "8": 114, "9": 130, "10": 149, "11": 164, "12": 175, "13": 189, "14": 202, "15": 224, "16": 237, "17": 251, "18": 265, "19": 288, "20": 308, "21": 329, "22": 348, "23": 367, "24": 386, "25": 403, "26": 416, "27": 437, "28": 452, "29": 470, "30": 482, "31": 497, "32": 517, "33": 528, "34": 544, "35": 555, "36": 569, "37": 583, "38": 599, "39": 613, "40": 624, "41": 638, "42": 648, "43": 664, "44": 680, "45": 695, "46": 706, "47": 719, "48": 736, "49": 759, "50": 776, "51": 788, "52": 804, "53": 824, "54": 837, "55": 859, "56": 876, "57": 893, "58": 907, "59": 923, "60": 934, "61": 949, "62": 966, "63": 987, "64": 1000, "65": 1012, "66": 1029, "67": 1043, "68": 1059, "69": 1075, "70": 1085, "71": 1098, "72": 1114, "73": 1128, "74": 1144, "75": 1160, "76": 1178, "77": 1191, "78": 1208, "79": 1226, "80": 1243, "81": 1258, "82": 1277, "83": 1290, "84": 1303, "85": 1315, "86": 1326, "87": 1341, "88": 1355, "89": 1370, "90": 1382, "91": 1396, "92": 1409}
---

**Dave Jones:** Hi, in a previous video we took a look at this Data I/O Unisite programmer. It was originally about like well, a typical configuration unit apparently was about $30,000 back in the day with all the extra, you know, cards and everything else. That's

**Dave Jones:** 1986 money. So, this is one hideously expensive thing. Anyway, link in the previous video if you haven't seen the teardown of it. We're going to have a go at repairing this. And now if you remember the previous video,

**Dave Jones:** well, I'll just show you. We've got the LEDs over here. So, just watch those LEDs there. And we'll power it on. And I did a teardown. The power supply is under here. The power supply visually looked in good condition and everything else.

**Dave Jones:** That was fine. So, let me switch it on. And I've got all the cards taken out just to minimize the load. So, we switch it on. The power LED comes on. I think that one came up on and then just switched off.

**Dave Jones:** And basically, we measured it last time. There's test points here and there is no voltage on the test points. So, it's like there's either something wrong with the power supply or what I think is more likely is the power supply is possibly

**Dave Jones:** shutting down cuz this is a ridiculously well-engineered unit. So, I'd expect a similar sort of well good engineering in the power supply in that there's no fuses blowing in there and it obviously tries to power up. There's a LED coming on. It's doing

**Dave Jones:** something, but it's probably got detecting some sort of overload and shutting down. So, that's the more likely scenario. So, there's basically two scenarios here. One is that the power supply, big power supply under here, big beefy one is there's something wrong

**Dave Jones:** with that or B, there's something wrong with this board here. Or could even be this board over here cuz it's powered from the same rail ultimately. But if there's something wrong with the circuitry on here which is maybe

**Dave Jones:** shorting out a rail or doing something like that. So, the first thing I'm going to do is, well, disconnect it and I'm going to So, I think it's more likely that there's actually something shutting it down. I think

**Dave Jones:** there's more likely than not. So, what I'm going to do is measure the uh measure the rails. Here we go. Let's give it a burl. We've got uh 5-V rail, we've got a 12-V rail, a 48-V rail, -5 and my and 2.1.

**Dave Jones:** So, let's go ground and let's go 5 V first cuz that's the biggie cuz all the chips on this board, hundreds of them, I don't know if there's hundreds, it's probably like I don't know, 50 or something. Um

**Dave Jones:** uh 5 V. So, if one of those is shorted or one of the caps, I mean, you know, there's each one of these chips is going to have one of these little axial bypass caps. These caps here actually look in

**Dave Jones:** good nick. There's uh the vent holes, there's no bulging. The vent holes look good. Um I don't think there's any tantalums on this board. Uh by the way, um simple repair thing, yes, I've done the visual like I've looked around,

**Dave Jones:** everything's fine. You do the smell test, everything's fine. Um so, there's no visual signs of any problems. Um so, maybe we've got a uh a cap shorted out or something. So, let's have a look at the rails. Well,

**Dave Jones:** hello. Hello. Point two and it's not charging up. Point one, if anything is dropping. So, what you do here is swap the probes, see if there's some No. Our 5-V our 5-V rail is shorted. Wow, that's it. Ha.

**Dave Jones:** Yep, that was the most likely scenario. It looks like it's paid off. So, our 5-V rail is shorted. Great. We've got A, we've got something to work from. B, it explains the uh symptoms of the power supply shutting down. So, I think the

**Dave Jones:** power supply is probably fine and it's just detecting that short and shutting the thing and shutting down all the rails just to protect the whole instrument. So, that's great. But, as I said, yeah, we've got like bypass caps

**Dave Jones:** on every single chip. So, what we need is a high resistance high resistance high resolution multimeter that can go down to 1 mΩ or thereabouts and we start tracing down a short. Actually, let me let me measure the other rails don't to

**Dave Jones:** go off half-cocked. And well, you know, we've found a definite problem. Okay, so there you go. 12-V rail's fine. The other rail's fine. Whatever that is, 48 V. -5 V. Yep. 2.1 V. Yep. And yep, so all the others are good. 5-V

**Dave Jones:** rail is cactus. All right. Let's chase this one down the rabbit hole. A meter with 1 mΩ resolution and let's measure that again. Okay, 228 or 22 6 225, whatever you want to call it. It's like going down slightly.

**Dave Jones:** Um and let's go somewhere else on the board. Let's go all the way over here. Measure another cap. Oh. Oh. That's no good. So much for narrowing this sucker down. That big ground plane in there is going to ruin our day. What if I keep one

**Dave Jones:** probe on there? One over here. Uh okay. Yeah, here's the problem. We're going to have to get better resolution than this and or like yeah, we can like short out the probes, you know, you can do your relative thing. If you've only

**Dave Jones:** got this, where where is that null like that, you know, and you can go This is where you need good sharp probes. Okay, there you go. 186 187 to the short.

**Dave Jones:** Oh. 176 to the short. Uh where else? I don't know. There's another cap all the way over here. You need uh good sharp probes. So, I'm using my uh probe master ones with the ridiculously sharp tips on them so I can penetrate

**Dave Jones:** the oxide and uh really get in there. And well, uh this is not great. We're going to actually Maybe I need more uh higher resolution bench meter to try and uh tackle this one. So, wouldn't be the first time that I've had to resort to a

**Dave Jones:** uh bench meter, like a 6 and 1/2 digit bench meter, to uh get the resolution required to trace down a short on a board. Check this out. I thought I'd take the board out just so it's, you know, easier to work on and maybe

**Dave Jones:** isolate one of the other uh sections. And look at this. 5-V rail. 56 ohms. Now, not the same in the other direction. Give me auto ranging.

**Dave Jones:** 79 ohms. There you go. So, the short is not actually on this board. Now, that's, you know, that wouldn't be uncommon. I wouldn't uh quibble about that for a um five you know, a 5-V rail with a huge

**Dave Jones:** number of uh TTL Well, you know, CMOS TTL type chips um for this sort of thing. So, I deem that to be okay. So, I reckon the short somewhere else. Hmm, narrowing it down. I'm actually glad it's not on here.

**Dave Jones:** So, uh process of elimination, we'll plug in the uh memory expansion board there. Let's have a look. Turn it the right angle.

**Dave Jones:** Hey, no. It ain't there. All right. Floppy drives. Let's plug in the floppies. Is it the poor old floppy drive?

**Dave Jones:** No. It's got to be the backboard. That's the only one left. So, just probe the I don't know what pins are down there. I'll just probe pin 10 and 20 on a chip here. That'll be the 5-V rail.

**Dave Jones:** Bingo. Found it. Definitely short on the backboard. So, I need to unscrew that, get it out, and then we can work on that separately. Don't want to work on it when it's in the back there. That's horrid. Tell you

**Dave Jones:** what, that's not bad design. There's only one screw top and bottom there, and then this entire piece comes out with these um little bracket little hooks in there to hook into the bottom. Wow, that's nice. What the hell is Wow. Look at all the

**Dave Jones:** heat sink devices on there. I was going to say that it had nothing to do with the power supply, but that's the waveform generator board. Um so, that's the external heat sink. It's all passive, of course. There's no fan in

**Dave Jones:** that. Uh it's all the passive heat sinking for the uh drive. There's all the drive transistors down in there for the driving the VCC of the pin and and the programming uh pin. So, this is the waveform generation

**Dave Jones:** board as we went um through in the previous video. But, wow, that's a it's a beast of a heat sink. I think these things are a bloody huge power amplifier or something. It's a program a little piddly chip.

**Dave Jones:** Wow, talk about over engineered. Now, the first thing I see, I'm not sure if they're across the rails or not. But all these old school tag tantalums and yeah, they're one of the first culprits that you'd suspect, but I don't

**Dave Jones:** know if they're just across the 5-volt rail or not. But once again, you know, you give this thing a visual uh check, make sure nothing is uh dodgy there, but no, it all looks okay. But you know, it could be a chip

**Dave Jones:** shorted, could be a cap. Um you know, it's unlikely to be like a PCB fault or something like that in a bit of gear that made it into production, you know, like a short on um internal layer or

**Dave Jones:** something like that. So, yeah, it's got to be some sort of cap or or uh component. Uh I'll tell you what, we may not need our high-resolution uh meter after all. We might be able to do this. Um I've nulled this out. I'll just null

**Dave Jones:** uh near enough. Yep, good enough for Australia. Um the first thing I did is I don't have Well, I do have the schematic for this board, so I could look it up, but I'm going to try and do it without it. So, I went

**Dave Jones:** through and measured all across all the tantalum caps, and the only one that was across the rail was this one here. And well, uh that was across the 5-volt rail. So, all the others, there we go. It's 55 mΩ, right? And then if we go up

**Dave Jones:** here and measure that same chip I was measuring before. No, sorry. That's the Analog Devices part. That's not the correct pins. There you go, 211 mΩ. So, you can see that's higher resistance over here, and we we can measure a much

**Dave Jones:** lower value here. So, it's got to be closer to this area than it is to this, because it's got if Let's assume that that cap is shorted, for example. Let's assume that's the culprit. It could very well be. Then, uh you know, if you

**Dave Jones:** measure any two points on opposite sides of the board, they should be uh higher resistance over here. And that's how you can narrow it down. You can sort of, you know, measure resistance on points and and things. And

**Dave Jones:** this one actually doesn't have too many 5-V digital chips actually, cuz this is the waveform board. It's got just tons of other um stuff. So, but that one is like that's as low as you get. I don't see anything

**Dave Jones:** else digitally around there. So, really, I'm you know, I I would almost uh suspect that I would um suck that one out, really. Maybe I'll find another digital chip over here somewhere. Yep, sure enough. Check this out, right? This one over

**Dave Jones:** here is 208 milli ohms. And this one over here, which is a HC373, it's kind of further uh I don't know, kind of well, you could say similar. Similar distance. And bingo, that's 221. So, that's slightly higher. So, you know, if the short was

**Dave Jones:** here, of course, then it it just doesn't make sense. The short has to be within this area down here. So, I reckon that little tantalum that little tag tantalum evil little suckers they are. Um they can develop our shorts and they can

**Dave Jones:** catch a light and explode with pulse input. Um uh you know, excessive pulse currents and things like that. Anyway, I'm going to suspect that sucker and uh desolder that one, I think. Um cuz I can't really find anything else around

**Dave Jones:** there. 5 V. I I don't want to go consult the manual and I don't I don't have the board overlay, but I've got the schematic, but yeah, that's good enough evidence. And as further confirmation, this puppy up here, there we go, 300

**Dave Jones:** milli ohms. So, that is further away than there. So, yep, that makes sense. And I've sucked it out. Straight across that cap again. Bob's your uncle. Look at that. No wackers.

**Dave Jones:** Yep. And haven't measured this yet. Could have that third hand, but I'm sure if I do that come on. Little turd.

**Dave Jones:** Bingo. Tag tantalum. Classic. Absolutely classic. Culprits these things. Pain in the ass. Look at that. 10 mic 50 volt job. STC. And for those playing along at home who want to run the numbers, let's go between Is this the ground?

**Dave Jones:** Yep, the ground there. There you go. So, that's 67 milliohms. And the positive over to our reference Oh, do I use that one or that one? Doesn't matter. Over to our reference chip 163. And you can probably see if we

**Dave Jones:** go over to this one over here. See, it's higher. And that's just the resistance going across the board, across the ground plane, plus the you know, the uh thermal relief uh small traces going into there and the joints and everything

**Dave Jones:** else. So, here you go. Beautiful. And it's time to get out that gorgeous AVX sample kit that I got. This was one of many I got in the mailbag. Thank you very much AVX. Tantalum sample kit. Of course, they

**Dave Jones:** don't have any of that newfangled uh tag tantalum crap these days. Um but there's a 10 mic 50 volts even though we don't need it. Like there's no reason that like it's just impossible that you could possibly get 50 volts across that cap

**Dave Jones:** cuz it's directly across measured across the 5-V rail. I don't even have to check the schematic. So, you know, anyway, I'll go with the same one. So, there you go. We'll use one of those. Have to hold my tongue

**Dave Jones:** at the right angle. All right. There we go. Um even though it's a surface mount jobby, so the pin pitch of that looks very similar. I'll just barge in an SMD one. Yeah, she'll be right. No worries. Look at that. Looks like I bought one.

**Dave Jones:** Let's go. All right, let's power this puppy back up. I measured the 5-V rail. It's 11 ohms in both directions. So, that sounds pretty good. Let's give her a bell. And here we go.

**Dave Jones:** Green LED. Four LEDs. If I hear the floppy drive go, I might might wet my pants. Sweet. Not often do I get one that uh basically um was well still like we've fixed that fault. Whether or not there's other faults, I

**Dave Jones:** don't know. Um but we're certainly getting progress. It's not very often that I get a repair like this that pretty much comes down to exactly what I thought it would be. I thought it was, you know, most likely to be

**Dave Jones:** not the power supply but actually a short on the board shutting down the power supply cuz that all made sense from an engineering perspective and it turns out yep, it was a short on the board and then I been

**Dave Jones:** narrowed it down, got down to that board and then hey, tantalum's. Yeah, let's check those and sure enough one of those babies confirmed confirmed with multi-point measurement on there pretty much, you know, triangulated kind of thing and that was it. Bob's your uncle. That's a

**Dave Jones:** Bobby dazzler. Look at that. So, we've got some LEDs happening here. I need to make boot floppies and everything like that. All right, so I put all the cards back in and we power it up and uh this LED over here, it's not very

**Dave Jones:** bright. Jeez, you can't see it, but anyway, power and self-test there are on. I believe the self-tester takes quite some time, so I'm going to leave that uh running, consult the manual how to use this thing and uh go find a uh

**Dave Jones:** D25 serial cable to hook up to this thing. Um and you may not I can't remember, but you may not need the floppies to actually uh you know, at least get something out of the serial port to begin with. Uh the ROM may actually do

**Dave Jones:** that, you know, it may not uh it may tell you, you know, no, load the boot put in the boot disk or something like that. Um so, if we can get that far, if we can get something out of the serial

**Dave Jones:** port, well, it's been over half an hour now and the self-test LED is still lit. So, um which is like it's supposed to do this. When you power it on, power and the self-test LED is supposed to be uh

**Dave Jones:** lit and then it doesn't say how long the self-test uh uh takes, but uh Secret Squirrel told me it was like yeah, 20 minutes or something like that. So, it hasn't gone off. So, this is not good. Hmm. And you know,

**Dave Jones:** they're supposed to be like blink once it's finished its self-test, it'll like blink and tell you any errors or anything like that. So, yeah. Uh it's not great. By the way, I found out what this was on the ROMs here, property of uh copyright

**Dave Jones:** 1983 H&I Inc. H&I actually stands for uh Hunter and Ready. Um my mate Steve Leibson actually commented on the video and he uh knew all about this back in the day and uh apparently Hunter and Ready they developed uh basically the

**Dave Jones:** first RTOS, the first real-time operating system. I believe it was called VRTX and uh that's probably what's running inside here, hence the copyright. Thank you very much, Steve. Uh we've uh interviewed Steve on the uh Amp Hour, and that was very interesting. I'll have

**Dave Jones:** to link that one in down below. Check it out. Right, so I've repowered it uh with the extra memory board uh disconnected, and same thing. The LED is still on. So, um yeah. Hmm. Anyway, I I forgot in all the excitement of uh

**Dave Jones:** repairing this thing, forgot to measure the voltages. I've measured them all, and all the test points are uh fine. So, all the rails are up, so it's not that. All right, time to get the scope out and see if this thing does anything um using

**Dave Jones:** the terminal mode here. Uh pin two is the transmit in DTE mode, data terminal equipment, pin seven, and the ground. And if we switch it on here, we get our regular RS-232 uh levels. They were like minus um or you know, 5

**Dave Jones:** and 1/2 volts or something like that. And not a sausage, but check this out. So, well, obviously, it doesn't uh output anything until it's finished the self-test, and it's not finishing the self-test. But, if we switch it off,

**Dave Jones:** ta-da! Look at that. So, let's actually try and capture that, shall we? So, here we go. Bingo! We've actually got some data. There you go. So, it it is spitting something out when you switch it off. It's like, I don't know,

**Dave Jones:** shutting down or something like that. Hmm. Anyway, at least it's doing something. It shows that the processor is working and everything else. And sure enough, if we actually capture and decode that 9600 board, we can actually see what it says. It's uh carriage

**Dave Jones:** return and then line feed, line feed, line feed, and then you can see on the list here, power space down. Awesome. So, it's pairing down. Thanks for that, Uniside. And I managed to find an old school D25 to D9 adapter. I've got a cable run over

**Dave Jones:** to the PC, and we can simply use a terminal emulation program to check it out. Don't need the scope and the dodgy wires anymore. Sure enough, there it is. That's power up. We just get nothing. There's a whole

**Dave Jones:** bunch of line feeds in there, and we just get the message power down. Well, at least it's uh doing the right thing and actually gracefully shutting that down. It's not like a soft power switch, because I'm physically doing the

**Dave Jones:** hard mains power switch on the back. So, it's obviously detecting that it's powered down. It's got enough power reserves, and it's simply doing the right thing, shutting down the OS, doing whatever it needs to do, and outputting the serial command. So, it's obviously

**Dave Jones:** still got the power reserves to actually keep that process going and doing that. So, there's got to be some sort of power down watchdog interrupt type thing. And I'm sure if you check the schematic, it's in there. It interrupts the

**Dave Jones:** processor and goes, "Whoop, go to your power down routine before we actually lose power." Awesome. So, unfortunately, that's going to be it for this episode anyway. We have actually repaired the thing to the point where it's booting up, and it's doing it's, you know,

**Dave Jones:** giving us the proper data output. The rest maybe like, you know, some sort of software or configuration problem or something like that, which needs a different class of troubleshooting, I'm afraid. So, I'm going to have to leave that to a second video. But if you have

**Dave Jones:** any ideas, if you've seen this problem before, if you're familiar with it, where it just sticks continuously in the self-test mode, then let me know. I've As I said, I've tried with and without the memory card and stuff like that. And

**Dave Jones:** that I've put a like a blank floppy in the drives, and it doesn't, you know, seem to make a difference. And And it doesn't matter how long I leave this thing. It just sits in self-test mode there and never exits. it. It's the

**Dave Jones:** letter supposed to turn off when it's finished or given error code and start blinking LEDs and things like that and nothing comes out of the serial port after boot up. So, yeah. It's a bit disappointing, isn't it? Geez, I hope it

**Dave Jones:** would would have Yes, and I've plugged in the pods, too, by the way. And it doesn't make a difference there, either. So, very strange. So, anyway, I hope you found that repair interesting and useful. If you did, please give it a big

**Dave Jones:** thumbs up. As always, discuss down below. Links, subscribe, videos at the end here somewhere. Other ones to watch. Catch you next time.
