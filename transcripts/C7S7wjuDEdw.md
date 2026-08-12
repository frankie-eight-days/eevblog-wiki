---
video_id: C7S7wjuDEdw
title: EEVblog #1138 - Systron Donner Counter Teardown
url: https://www.youtube.com/watch?v=C7S7wjuDEdw
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 26, "3": 37, "4": 50, "5": 61, "6": 74, "7": 85, "8": 99, "9": 110, "10": 125, "11": 142, "12": 150, "13": 161, "14": 168, "15": 185, "16": 201, "17": 225, "18": 248, "19": 274, "20": 288, "21": 315, "22": 341, "23": 347, "24": 361, "25": 375, "26": 389, "27": 398, "28": 414, "29": 429, "30": 451, "31": 463, "32": 472, "33": 486, "34": 498, "35": 505, "36": 515, "37": 527, "38": 547, "39": 571, "40": 584, "41": 596, "42": 606, "43": 621, "44": 630, "45": 646, "46": 654, "47": 662, "48": 677, "49": 687, "50": 703, "51": 714, "52": 728, "53": 747, "54": 767, "55": 781, "56": 791, "57": 810, "58": 819, "59": 831, "60": 849, "61": 861, "62": 883, "63": 901, "64": 914, "65": 932, "66": 941, "67": 960, "68": 971, "69": 979, "70": 994, "71": 1009, "72": 1027, "73": 1046, "74": 1067, "75": 1077, "76": 1088, "77": 1103, "78": 1128, "79": 1144, "80": 1167, "81": 1175, "82": 1195, "83": 1205, "84": 1215, "85": 1228, "86": 1241, "87": 1254, "88": 1266, "89": 1281, "90": 1289, "91": 1300, "92": 1309, "93": 1325, "94": 1340, "95": 1364, "96": 1380, "97": 1408, "98": 1421, "99": 1435, "100": 1447, "101": 1460, "102": 1475, "103": 1493, "104": 1507, "105": 1517, "106": 1538, "107": 1551}
---

**Dave Jones:** Hi, welcome to a teardown Tuesday. We've got a random bit of old test instrument kit here. Look at this, Systron-Donner. Hands up if you remember Systron-Donner. They're actually still around, but they don't make test instruments.

**Dave Jones:** They're like a defense company who make like uh radar-y type things or something like that these days, I think. Anyway, it's a 6051 for those playing along at home, counter-timer.

**Dave Jones:** And look at this, all these manual range buttons, beautiful. And yes, it's not just a frequency counter, it is, as the name says, it's a counter-timer. So, you'll see start-stop here.

**Dave Jones:** I don't know what these start-stop thumbwheel switches are. Love thumbwheel switches. I could play with those all day. Um and they're probably like some start delay or stop delay or something like that, perhaps.

**Dave Jones:** I don't know. I don't have the manual for this to hand. And it's got AC/DC coupling on all the channels, attenuator, of course, your thresholds, and your various functions.

**Dave Jones:** You've got You can do count would be not frequency counter, but physically counting your inputs. So, you know, this is very handy for counting events and stuff like that.

**Dave Jones:** If you don't have a proper time counter in your lab, highly recommend you get one if you want to count how many events happen, transitions happen in a certain time period or something like that.

**Dave Jones:** Counter-timer is absolutely invaluable for doing something like that. And of course, it's frequency counter, and you can get period and frequency display as well. And this is actually a Nixie tube display, as we'll see.

**Dave Jones:** Hang around for the end. We'll power this baby up, and sure we can get some Nixie tube goodness out of this thing. Hopefully, that's the plan anyway. This one has seen better days.

**Dave Jones:** Look at the top on that. I'm sure it didn't come factory fitted with that uh type camouflage. I'm sure it's uh you know, hasn't aged well. This probably dates from uh you know, sometime in the uh '70s.

**Dave Jones:** It's definitely not '80s because it's a Nixie tube-based thing. None of that uh LED display rubbish. So, let's have a look. On the back here, we've got uh external reset, uh IEC mains power input, uh BCD out, a remote control interface, and it looks like we've got an ovenized oscillator here.

**Dave Jones:** If we take that cover off, I'm sure we can get into and adjust our oscillator there. Fantastic. It's got all your uh external uh time base and stuff like that.

**Dave Jones:** But, the most interesting thing, assembled and tested in Australia. No wuckers. Well, you know what we say here on the EV blog, don't turn it on, take it apart.

**Dave Jones:** Okay, this one's going to be way too easy. Two screws in the top. Let's pull it off. And oops, sorry. I'm going to have to move the camera back.

**Dave Jones:** Wow, we're in. Oh, isn't that beautiful? Oh, look at the daughter board, vertical uh you know, motherboard construction with all the individual cards popping out. Oh, that is gorgeous.

**Dave Jones:** Oh, wow. Oh, there's some system design engineering gone into this puppy. I just love it. And look at the gold plated PCBs down there. Oh, yes siree Bob. Oh, none of that tin plate rubbish.

**Dave Jones:** Japanese fan. All this stuff's made in Japan and Australia. Oh, there's our ovenized oscillator down there. Check out the uh the back of that. They've got like, you know, an old-fashioned uh tube socket, tube socket, and uh just discrete wiring just bundled out coming of course to the rear because you want to That was like the external uh frequency input and stuff like that.

**Dave Jones:** So, you want to be able to switch between those. So, they've got one big uh folded metal like cage at the back that holds all the uh power supply fan oven iced oscillator some of the big ass filter caps here and it looks like some more big ass filter caps in there and these are probably all your powers look little test sockets.

**Dave Jones:** Little test sockets on your power supply beautiful and then the rest of it is just one huge board and that looks like really thick as gold plating on that like you know gold was well I don't know was cheap in 73 anyway goes through cycles really but yeah like the old school stuff they just applied it thick as back in the day and even like the gold plate that you got on

**Dave Jones:** the card edge connectors you know they don't make them like they used to. Anyway this is fantastic oh that's actually an extender card. Wow look at that. We get a free extender card wow I wonder how much gold's on there.

**Dave Jones:** That's sweet and of course these extender cards absolutely vital when you're uh testing and let's get one out testing and repairing these cuz it means that you can just whack it in like that stick your board on top there and you can access the front and the back side to probe and troubleshoot this whole thing so repairability on this brilliant now I'll just go through each board

**Dave Jones:** briefly one by one this one's a bit how you doing got a that's out of trenny there just bolted onto its own little heat sink only single sided this one so this one doesn't look the least bit impressive and we got tin plate on the bottom here so they would have masked off during the the wave soldering these masked that all off and just rolled unfortunately is that hand done?

**Dave Jones:** By the looks of it anyway that one's a little bit how you doing but let's go on to the next one this looks more like it. Look at this.

**Dave Jones:** A little custom-made transformer in there. Look at that. I love it. And by the way, yes, we do have our date codes here. 1973, but some of them have got 72, but at least it's at least 73.

**Dave Jones:** So, there you go. Look at this. We've got a big ass 10-turn trimmer there. And another that would be an adjustable capacitor frequency trimmer. So, I'm not sure what that is.

**Dave Jones:** It's obviously, you know, it's not the main oscillator. So, anyway, I love the test points on there. Really old school. And once again, it's all tin plate on the back with real thick ass gold plating.

**Dave Jones:** Gorgeous. So, it would have been really nice if these were all labeled. Anyway, this one's the next one in the series there. You can see we've got some inductors there.

**Dave Jones:** Just, you know, air-cored jobs. And not much else doing there. Couple of trimmer caps. Little Old school package. Beautiful. And look at that. That one's actually got selective um tin on it.

**Dave Jones:** So, yeah, I'm not sure what happened there. That one didn't need much layout time, did it? Little resistor packages. Well, you know, why not? Hey, when you got a bus system like this, the A7 board, ITT.

**Dave Jones:** Hmm. Anyway, no idea what they are. Yeah, what do we got? A8 board. Every board's a winner. They are labeled. It'd be really, you know, I'm sure the manual for this thing is absolutely first rate, and it would list all the different, you know, boards, and it'd have block diagrams, and probably, you know, almost certainly schematics in it and stuff like that.

**Dave Jones:** But, what do we got? It's got Once again, ITT stuff. Oh, 936. Yes, that's old RTL stuff, isn't it? Some of the really early stuff. Anyway, some Motorola stuff.

**Dave Jones:** So, we're talking, you know, '73, probably late '73 this was manufactured, thereabouts. This one's just got logic. Oh, they're upside down, so all the electrons are going to fall out.

**Dave Jones:** And you'll notice that there's you know not for bypassing on each individual chip, none of that rubbish, just some bulk decoupling for the card. And you know, that's fine, gets the job done.

**Dave Jones:** And the A10 board is blue cuz well, blue makes it go faster. Once again, we're just got all logic. We've got a few more bypass caps. I love the little SE.

**Dave Jones:** Um they would be No, are they? I was going to say No, they're not power cuz you know, you can see the uh see the power up the top.

**Dave Jones:** They're just snaking one into the other. So, that looks like probably a ripple counter or something. Not even looking at those part numbers. Can't see them from here. And here's the A11 board.

**Dave Jones:** We've got some more analog stuff. So, maybe we could be talking some of the input type stuff. Maybe we've got some We've got some AC coupling and stuff like that.

**Dave Jones:** I don't know. So, looks like we've got got a relay there, little reed relay job going across. A12, once again, we've got Motorola parts. We're probably going to see classic Motorola Motorola just owned the market back then.

**Dave Jones:** What is it? The 13 09, is it? That was the was basically the input prescaler in every I probably got the number wrong. Anyway, in every frequency counter do-it-yourself design back in the '70s and right through the '80s and probably even into the '90s.

**Dave Jones:** Okay, so we just went through in sequence on all of those. So, let's pull out a couple of other random cards here. Power supply first. Hey, check out the the penetrators going through there.

**Dave Jones:** They're going through from the That's very nice. They're called penetrators cuz they penetrate a chassis from when you solder on one side to the other. And they're just going through from the folded metalwork up here down to the main board.

**Dave Jones:** That's just your power coming over. It's the A13 power supply board. So, yeah, what do we got? Just the you know, some classic what 73 regulators. I don't know.

**Dave Jones:** Not reading the part numbers. And we've got of course 5 volts for all your TTL stuff, plus 12, minus 12, and minus 5.2 for your What's that ECL stuff?

**Dave Jones:** Oh, look at this. We have our first budge. Check it out. And you can see the still see the flux residue on those joints. So, someone's had a crack at that.

**Dave Jones:** Someone's had a repair of the old power supply. Not sure what that board's doing, but it's got pre and balance there. So, I don't know. Beulah. None of this wasting you know, gold if you don't have to.

**Dave Jones:** Just love the attention to detail on the links here. Look at this. So, they you know, person laying out the board went oh, bugger this. I can't get this trace over to here.

**Dave Jones:** Why not? I don't know. They could have snuck it around there and went to there. But anyway, well, maybe they didn't want to break the ground in there. But is that that big a deal?

**Dave Jones:** It's going around there. Anyway, is that a layout fail? They could have bought that around there. Anyway, decided to use a link. And then of course, you don't want to short out, you know, someone's handling the cards, squishes it down, and it makes contact with the gold down there.

**Dave Jones:** There's none of this newfangled solder mask rubbish. So, they they put the plastic sleeve on there. Beautiful. Oh, that one's getting a bit interesting. Look at the reed relays down there.

**Dave Jones:** Fantastic. And I don't know what the rest is doing. But when you see sort of like a symmetrical layout like that put a line through the middle there. Can see it's completely symmetrical.

**Dave Jones:** These are little transistors either side. When you got a symmetrical layout like that, you can tell that that's a some sort of differential you know, line differential amp, things like that.

**Dave Jones:** Anyway, it's when you see symmetry you know it's differential. And then of course the resistors at the end are going to be across the differential line. And then so it's probably you know, like single ended differential uh converter maybe.

**Dave Jones:** There's a lot of in there for that though. And another identical board. So given that there's two of them and also given their placement near the front panel physical placement near the input connectors here for like so this is basically so this board that we looked at here is a 16 one.

**Dave Jones:** The input amp for the like the frequency counter input, the channel A input. And then these two boards here which are absolutely identical no doubt the input amps with the selectable AC coupling and the trigger threshold and the attenuation and stuff like that.

**Dave Jones:** So there you go. Little trimmer pot. Oh, I just noticed that. On the back side there I don't don't know if it's an after thought but there's our they they wanted to ground the input to the chassis here.

**Dave Jones:** So when you plug that in that just makes contact with the chassis. So there you go. That just makes sense. And of course these three long boards over here with all the digital stuff.

**Dave Jones:** That's just all the different modes and stuff like that. So that it contain the gating logic and all that sort of jazz. And last but not least, well second last, let's have a look at this board which handles these thumbwheel switches here and this is this is pretty how you doing.

**Dave Jones:** I mean, look, you know, like everything else is quite neat and tidy. This just looks a bit messy with the ribbon cables and just the dicky little turret connectors up there.

**Dave Jones:** Yeah, they sort of let it down a bit there, but anyway. Unfortunately, this board doesn't come with the ejectors and they these boards do require, by the way, a lot of force to get these in and out.

**Dave Jones:** if I'm I'm trying to like sort of rock it out, but jeez, it's really really stuck in there good. So, forgive me for not taking that one apart. Anyway, that just handles the that's just decoding for the thumbwheel switches.

**Dave Jones:** Now is the time for all you Nixie tube fanboys to get excited. What we've got here is these are just latches that latch all the data 7475 four-bit latches there, but what we're really interested in is down here.

**Dave Jones:** Let me flip this around. There we go. Nixie tube goodness 74141 drivers the absolute classic Nixie tube driver and they've put those in sockets because presumably, you know, they could blow and look at these National Instruments Nixie tubes 7328 date code.

**Dave Jones:** So, yep, late 70s late '73 this would have been manufactured. Look at that. That's the money shot in 4K. And then that little board there is just the indicator board for the various you know, segments like you know, microseconds and milliseconds and stuff like that.

**Dave Jones:** So, you know, gating and all that sort of stuff just lights them up. So, it's interesting that all this comes in via these dipped cable tied sockets here. You know, it's not the best choice.

**Dave Jones:** It's not quite how you're doing, but it's getting there. And the Sprague passive fanboys go wild. Look at that. And it's none of that silk screen rubbish. Oh, wish this was Philco Vision there etched in the They're actually like etched punched in there.

**Dave Jones:** Brilliant. You didn't think I wasn't going to show you the bottom side, did you? Let's Oh, it just No, it just lifts off. Beautiful. Oh, look at that. Wow.

**Dave Jones:** What a Bobby-Dazzler. Lots of point-to-point stuff there. They didn't You know, they went to the effort to do the to do the main motherboard in here, but yeah, they sort of went, "Well, we can't do everything, so let's just uh let's just wire everything over, you know?

**Dave Jones:** Labor's cheap. No worries. Everything's still wired." Cost really wasn't a huge issue here. So, there you go. There's the big big capacitors down there, the huge lugs on them.

**Dave Jones:** Look at that. Fantastic. What have we got up the front here? Oh, is that a new switch? That looks like a new switch. I reckon someone's bodged in a new switch still there.

**Dave Jones:** What do you think? That looks like a new C&K jobbie. I reckon someone's had a go at that. Hmm. Anyway, you notice look at the attention to detail. They put the the heat shrink over the big strap going over to the BNC on the front.

**Dave Jones:** Jeez, they're serious there, aren't they? Jeez, that could carry some amps. And this is a double-sided load. We've got two reed relays on the bottom. This is fantastic, though.

**Dave Jones:** Wow. There's the rest of it. Oh, there's our uh There's our power on the heat sinks down in there. There you go. Straight into those. Okay. So, they're they're using the those penetrators were actually sockets.

**Dave Jones:** Yeah, they're actually not so much penetrators. They're actually like transistor sockets that are designed to mount into you know chassis with bottom point to point wiring like this. I'm sure that heatsink compound is dry as a dead dingo's donger.

**Dave Jones:** Uh yeah, I think I'm right. It's drier than a dead dingo's donger. Well, they certainly don't make them like this anymore, do they? And also, this is the first time I've probably ever seen supplying a an extender card cuz obviously like it they actually went to the effort to put like a little metal thing to retain it so it doesn't flap around in the breeze and fall out cuz

**Dave Jones:** it's got no socket to go into. So, I think, you know, it deliberately comes with that although you don't get one for these bigger ones which is a bit of a bummer, but geez, anyway.

**Dave Jones:** That's fantastic. Yeah, not exactly cost conscious on the design of this thing, but yeah, it did the business. There's only one thing left to do. Let's power it up.

**Dave Jones:** See if it still works. 1973. Confidence is high. I repeat, confidence is high. All right. See if this thing works. Woah. Hey, hey. Uh look at the beautiful Nixies.

**Dave Jones:** Uh what a Bobby dazzler. Oh, the power switch has seen better days. It rotates. Fantastic. Uh look at that. Uh thing of beauty is a joy forever. And I just love how you can see the six poking out further than the zero because the zero is physically towards the back on the Nixie tube.

**Dave Jones:** So, you can really see the difference there. Fantastic. Check out the update rate on this baby. Look at that. They're going so fast you can't see them. Woo. That's counter mode.

**Dave Jones:** WOW. THAT'S FANTASTIC. THIS thing looks like it works a treat. Well, she works. Check this out. I've set it to uh rate A here and I've set to 1 kHz range, so 1 Hz resolution here, generating just a 1 kHz uh square wave here and it's bang on.

**Dave Jones:** But look, you've got to press the manual reset button. It doesn't work. Like if I just suddenly, you know, take that up to 10 kHz or something, it doesn't work.

**Dave Jones:** We have to actually reset the counter each time. Uh fantastic, old school, but it's bang on. Oh, look at this. Look at how fast that counts. That's beautiful. Oh, this is so satisfying to use.

**Dave Jones:** Oh, you just want to press that reset button all day. Really, that's just beautiful. But it's out. But which one is out? The Sistrunk Donna or the Siglent, this newfangled Siglent?

**Dave Jones:** Ah, it's time to bring out the big guns. So, we've got the SRS SRO frequency reference standard. Let's take a look at this. Rubidium locked. Ah, there you go.

**Dave Jones:** She's out by uh uh 82 Hz. Oh, bummer. And we can actually uh extract an extra digit from this if you want to go over scale. I love the fact the manual reset just lets you show.

**Dave Jones:** It's a it's a really good visual way of showing the gating period. In this case, it's going to be uh 10-second gating period and how it actually counts those 10 MHz pulses in that counting period.

**Dave Jones:** There we go. Counts the input pulses, sorry. If we're in reciprocal counting mode, then it would count the input uh it would count the reference clock pulses. But there you go.

**Dave Jones:** Um 826, oh, that's slightly different, isn't it? 2 What do we have? Oh, no, 82. There you go. So, it was actually 826. But yeah, beautiful. This one I use this all day.

**Dave Jones:** So, we'll don't through and test all the functions on here, you know, you'd have to uh uh uh test the start, stop, and the start, stop, and whatever delay or whatever it is here, and you'd have to test, you know, all the various threshold levels and the coupling and all sorts of stuff, but it seems to do the business.

**Dave Jones:** This is, you know, it's not a big like 12-digit display like you get these days. It's only eight digits, but meh, you know, this would have been pretty schmick back in the day.

**Dave Jones:** So, I hope you like that teardown Tuesday. If you did, get a random number there, please give it a big thumbs up, and as always, you can discuss down below.

**Dave Jones:** Catch you next time. What will the random number be? Use this as your lotto pick. All right. I know people aren't going to be happy unless I tweak this thing to match my rubidium.

**Dave Jones:** So, here we go. All right. I think I got it. Tongue at the right angle, very important. So, Uh No light, none of this live updating rubbish. Wow. Geez, what is this?

**Dave Jones:** A 10-turn trimmer? Think I'm turning it. Uh hang on. Okay, smaller screwdriver this time. Geez, I'm No, that's go- that's gone all the way with LBJ. Let's turn it all the way the other way.

**Dave Jones:** Yeah, it's like a 10-turn, five or 10-turn. I got diddly squat. What? Oh, 69. No, I've gone all the way. I'm getting jacked. What the So, after watching the teardown, I realized that it did have an internal 10-MHz oscillator and adjustment pot on that board, if you remember that that we actually took out.

**Dave Jones:** So, I figured that the ovenized oscillator that we saw in the back of this thing is probably like a separate thing, and you had to connect it. So, what I've done is actually hooked up the external 10-MHz out to the and switched to the external frequency in, and that's what we get.

**Dave Jones:** And it makes no difference when I tweak that pot on the back for the ovenized oscillator. So, I'm going to have to damn well cheat and plug my external reference into my 10 MHz rubidium standard, and of course, it's going to be bang on because I'm feeding the same 10 MHz into the reference clock as I'm feeding into here.

**Dave Jones:** So, will it make a fool out of me, or will there be one least significant digit? No, there we go. And can we go all the way with LBJ up to with our 10-second gating time, and we should get all zeros.

**Dave Jones:** Maybe a least significant digit. Ah, yes, a least significant digit. There you go. Right, so I switch back to the internal oscillator, and here it is over here. So, let's let's tweak the internal oscillator.

**Dave Jones:** We've got 60 on there at the moment. Oh, no, it's 71. Oh, why has it changed? I'm going to tweak that a little bit. Yeah, 64. Okay, we're going down.

**Dave Jones:** Ah, bang on, look at that. All right, so we tweak Wait, I can't believe it's got like the ovenized oscillator in the back, and it's it's set to the internal osc- Ah, there we go.

**Dave Jones:** Ah, I can tweak it maybe a little bit more. Ah. Half a bee's dick. Ah, near enough. And if we actually go back and have a look at our ovenized oscillator here, you can see that it is actually all entirely separate.

**Dave Jones:** Look, I mean, the middle BNC down in there is the 10 MHz out. So, um yeah, I was doing the right thing by connecting the external frequency input up to there, like that, and then switching our reference to external.

**Dave Jones:** But if I do that and then do it again. So, yeah, I plug that in and like we're over, which is fine. Um you know, it might need a trim, but the trim does nothing.

**Dave Jones:** So, maybe there's a fault with the uh trimmer inside that ovenized oscillator. So, but it gets stranger. I'm not sure if I'm using this thing right. I've disconnected the external 10 MHz reference.

**Dave Jones:** I've got it switched over to the external frequency standard and it's still counts. What? And that's pretty close to bang on what I did with the And if I switch it to the internal back to the internal oscillator, that's what we were getting with the the internal that I just trimmed.

**Dave Jones:** And it's drifted a bit, you know, temperature. Meh, the internal oscillators aren't great. So, yeah, I don't understand this thing at all. Um it's very strange. I might have to RTFM if I can find the FM.

**Dave Jones:** Catch you next time.
