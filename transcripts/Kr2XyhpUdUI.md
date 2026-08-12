---
video_id: Kr2XyhpUdUI
title: EEVblog 1493 - MacGyver Project - Part 2
url: https://www.youtube.com/watch?v=Kr2XyhpUdUI
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 24, "3": 34, "4": 47, "5": 61, "6": 81, "7": 94, "8": 111, "9": 123, "10": 135, "11": 150, "12": 161, "13": 179, "14": 194, "15": 209, "16": 226, "17": 240, "18": 253, "19": 264, "20": 284, "21": 301, "22": 313, "23": 326, "24": 340, "25": 353, "26": 369, "27": 382, "28": 405, "29": 419, "30": 435, "31": 450, "32": 464, "33": 477, "34": 487, "35": 504, "36": 516, "37": 535, "38": 549, "39": 566, "40": 582, "41": 600, "42": 616, "43": 632, "44": 648, "45": 660, "46": 683, "47": 699, "48": 712, "49": 724, "50": 738, "51": 759, "52": 777, "53": 786, "54": 799, "55": 815, "56": 830, "57": 843, "58": 858, "59": 876, "60": 894, "61": 908, "62": 924, "63": 946, "64": 969, "65": 985, "66": 996, "67": 1012, "68": 1026, "69": 1043, "70": 1060, "71": 1073, "72": 1086, "73": 1104, "74": 1116, "75": 1132, "76": 1149, "77": 1167, "78": 1185, "79": 1195, "80": 1214, "81": 1236, "82": 1249, "83": 1261, "84": 1277, "85": 1298, "86": 1309, "87": 1320, "88": 1335, "89": 1352, "90": 1366, "91": 1383, "92": 1403, "93": 1422, "94": 1436, "95": 1455, "96": 1476, "97": 1491, "98": 1505, "99": 1523, "100": 1534, "101": 1550, "102": 1570, "103": 1581, "104": 1595, "105": 1611, "106": 1624, "107": 1639, "108": 1649, "109": 1662, "110": 1675, "111": 1688, "112": 1701, "113": 1713, "114": 1729, "115": 1740, "116": 1751, "117": 1764, "118": 1777}
---

**Dave Jones:** Hi, this is part two in the MacGyver project because nobody can come up with a better name for the project. So, I'm going to stick with the MacGyver project. Um, and I thought we'd actually uh power up this uh board, the display

**Dave Jones:** board that we reverse engineered in part one, linked in up here and down below if you haven't seen it. Um, and there are a few questions regarding like actually driving this thing, but I thought like does it actually work? Like so we don't

**Dave Jones:** want to go through the whole effort of actually designing a circuit to drive this thing, building it up, and then finding uh there's something wrong with this. Um, that would really ruin your day. So, I thought we'd take the

**Dave Jones:** existing board out of here and just hook it up. I mean, we shouldn't need anything else. I mean, presumably if we power it on, then we're going to get something on here. Um, shouldn't we, Mr. Assistant? Say hi.

**Dave Jones:** Well, I'm Mr. Assistant. You're Mr. Assistant. Hooray! Yay! Sagan's here with me. Hello. There he is. Um, yeah, so we're going to power this thing up. So, let's have a look at this interface here, Sagan. Let's have a

**Dave Jones:** look. What can you see there? We've got 0 V, 24 24 V? Volts? And I don't have no what mA uh that'll be uh uh that's the milliamp interface. That's the um 4 to 20 milliamp current interface, I think. And 485 is RS485.

**Dave Jones:** That's a really old um serial protocol, still used though. Um, and 12 V I don't think 12 V is going to be an input. I think that might be an output. Anyway, so we've got the uh got the cable here from

**Dave Jones:** the uh casing, and you can see that yeah, the 12 V is this white wire here, but basically yeah, we've got the uh 24 V positive and negative, yeah? So, I think for a safe bet is just to connect up the 24 V. Volts.

**Dave Jones:** And see what happens. what happens. See if the magic smoke escapes. What do you think, Sagan? So, um up here is the So, that's the interface board there and uh yeah, we've got 0 24 V and there's no

**Dave Jones:** 12 V here. I don't see it. I'm not blind, am I, Sagan? There's no 12 V there. There's the uh 4 to 20 mA output, but so yeah, I reckon that 12 V is an output. So, that thing and that I

**Dave Jones:** reckon it's an output for something else. Um I don't know. Goes somewhere else internally, maybe. Um so, let's hook up 0 and 24 V and see what's what. So, is our power supply turned off on channel two? No, it's not.

**Dave Jones:** There we go. Okay, I'm just going to step back cuz I don't want to get blown up. You're going to step back? I don't want to get blown up. You think the magic smoke's going to escape? Maybe. Sagan's not confident.

**Dave Jones:** No. He's not confident. All right. Confidence is not high. Okay. So, 24 V So, we want to program that. So, Sagan, can you program that for me? He's never used it before. He's never used the Rohde & Schwarz power supply

**Dave Jones:** jobbie. Okay. So, well, there's different channels. So, this is channel two. So, this Yeah, oh yeah, yeah, it's channel two up there. So, it is touchy-feely screen. So, we want to set the voltage to 24 V. So, click here.

**Dave Jones:** Yeah? There you go. 24 V, not mV. Oh, oh, it did. Okay, it it defaulted to volts. Okay, cool. So, current-wise, I reckon this whole board is pretty you know, like I don't know, a couple hundred milliamps. It's already set to

**Dave Jones:** two .25 amps, 250 milliamps. Yeah. That sounds good. All right. Have we got the probes around the right way? Red goes to positive, blue is negative. That's a weird European thing. They use blue in Europe for some reason. I don't get it, but

**Dave Jones:** anyway, um all right, let's power it up and see see if it does anything. Okay. Please don't blow up. Please don't blow up. Well, the good thing is is that we've current limited the power supply, Sagan, so It won't blow up.

**Dave Jones:** It's It's not going to do much. There's There's not much power behind it there to actually do much. So, let's I I don't think there's any indicator leads on there. Can you see any, Sagan? Can you see any leads on that board,

**Dave Jones:** little surface mount leads or anything? I don't see any. I don't see any, either. No. So, you won't know if it's powered on or off. No. No. Well, no. We'll know by the current draw up here. So, you can read

**Dave Jones:** that out as we power it on. Okay. Uh switch it on. You want to press the channel two button? 0.250 amps. Yeah. Nothing. Zip. It's not drawing any current at all. Um Okay. Oh, maybe like it's got a fuse

**Dave Jones:** blown or something. Measure the fuse, Sagan. Let's see what we get. Yeah. That's intact. No worries. Squeeze that sucker. There we go. 0.1 ohms. Right. So, our fuse is intact. So, uh All right. It's not that. Why else would

**Dave Jones:** this not work? Uh Maybe the um connector's faulty. Maybe we didn't plug it in properly. That's all I can think of. Yeah. Or Did I I can't remember when I tore this down I put the board back in.

**Dave Jones:** Maybe I didn't connect it. Something dumb like that. Screw terminal. I remember they had screw terminals on the bottom. Okay. So, what we want to do, Sagan, is we want to buzz out So, put it on continuity mode.

**Dave Jones:** Yeah. There we go. Yep. Buzzer. Make sure that Make sure it buzzes. There we go. It buzzes. All right. Uh we want to probe. I'll take one and you take the other. I want to turn We're not in continuity mode.

**Dave Jones:** Uh yeah. We're measuring continuity to the black wire down here. Yep. Yep. Positive. Uh the red one. Do the same for the red one. Yeah, you probably have to get to this side. They're pesky, those connectors. Uh, there we go. All

**Dave Jones:** right, so we're getting 24 V. We will definitely be getting 24 V on our board. So, turn the power supply back on. We didn't click output. Daddy is so dumb. I'm so We didn't click output. Output. Press the output button, please.

**Dave Jones:** Hey, look. Look. Look. Here it is. It showed all eights. It showed I think you captured that on camera. It showed all eights and then it showed all decimal points. Turn it off and on again, Sayid. And shows all eights. Geez, that's

**Dave Jones:** pretty bright. And 40 dB. 40 dB. 40.db, yeah. 40 dB. I assume 40 dB is the like power setting for the measurement of the ultrasonic sensor. Um, they've they've got it in dB. I don't know why else you'd have dB. And we've got a flashy

**Dave Jones:** LED there, but that's pretty bright. That display is pretty bright. So, they're running those segments at a uh, you know, fairly juicy current. And by the way, um, in the previous video, we came to the conclusion that they're

**Dave Jones:** probably multiplexing this and they're probably multiplexing each individual segment. Cuz you can see, turn it off and on again, Sayid. Hang on. Uh, Okay. Yeah, go. Hang on. You can see that's a consistent brightness between having all eights on and not

**Dave Jones:** having all of them on. So, it looks like I reckon that they're actually multiplexing every single segment. So, not just an individual display. So, they're multiplexing, you know, so then you would have a set amount of current in

**Dave Jones:** each segment, but then you've got to multiplex, um, 40 different segments, which is a lot. Um, but that's how they're That's how they're doing it. And as we said, they didn't have a dropper resistor, but meh, you know.

**Dave Jones:** So there there you go. So it works. It's sending It's basically sending the same signal strength across each one of the segments. Yes. From the one edgy source. The same current. Splits it and puts it into each segment.

**Dave Jones:** Yep. Well, it multiplexes it. Multiplexes it. Yeah. So it turns on one segment at a time, but it's doing it so fast It's doing it so fast that you can't see it. But each one of those segments is

**Dave Jones:** turning on at least 40 times per second, at least. Let's just probe some stuff for fun. Let me find a ground point. There we go. That's a ground point. It's very convenient, so I'll hook that up to there.

**Dave Jones:** And we can approve around cuz you don't want to hook your crocodile clip up to the pin headers cuz it can short out the other pins. Trap for young players. Okay, so we've got our pin out here and

**Dave Jones:** uh let's have a look at the clock and uh well, the clock. Let's have a look how fast that's going. 1 2 3 4 and let's have a look here, Sagan. What do we have here? We've got five

**Dave Jones:** packets here. Why do you think we've got five packets? Because there's um five digits and each and each line going up and down would mean that one digit's turning on and off. Correct. of course there'd be different even

**Dave Jones:** smaller segments inside those lines. Yeah. Which would be each one of the little um Count how many how many pulses we got in one of those. Um One of those packets. Just maybe the bottom one's easy. 1 2 3 4 5 6 7 8.

**Dave Jones:** Eight? Eight pulses. What a convenience. Um what a coincidence. How many digits have we got in each Oh, how many segments have we got in each digit? That's so coincidental. a coincidence, Sagan. That's exactly what expect to see. And you can see

**Dave Jones:** um they don't update this often. So well, hang on. Well, there we go. Every two divisions, we're at 10 milliseconds per division. So, how much time between each one, Sayid? 10 milliseconds. Sorry, 20 milliseconds. 20 milliseconds total. So, 20

**Dave Jones:** milliseconds they turn on um they update um or they clock the information into the LED display there. No worries. And these are Yeah, we just got ringing on the bottom. The reason we got horrible ringing down there is because of my uh

**Dave Jones:** in inductive um lead here. It's not great. So, yeah, it's a bit how you doing, but you can see the signal. So, no worries. So, that's our clock. And then our data is the pin next to it. And it's more

**Dave Jones:** randomy. Ooh, that's Oh, hang on. That's the trigger level. That's the trigger level. That's all over the shop, isn't it? That's everywhere. Yeah. Wow, so they're really So, we can single shot capture that. If we just single shot capture it a

**Dave Jones:** couple of times Oh, hang on. I got to put it back in the middle. There we go. There we go. It change It'll change a few times cuz we got different displays. So, depending on which one we actually um just happen

**Dave Jones:** to trigger off it displays that. So, there you have it. That That is random. Wow. Okay, so our data's going in every 100 microseconds cuz we're 50 microseconds per division. So, every 100 microseconds we're getting data. What did we say it before on the clock?

**Dave Jones:** Uh 10 10 20 milliseconds, wasn't it? Every 20 It was milli or micro? It was milli. Milli. It was milli, wasn't it? Yeah. So, our data is updating like way more frequently. 20 times, 100 times as fast? Wow.

**Dave Jones:** Something like that. That's It's almost constant. The data is almost constant, but the clock is not. is not. The clock If If you're feeding the data, it's not going to do anything unless you clock it through. Here it is

**Dave Jones:** down here. You can feed in all the data you want until the cows come home, but if you don't clock it through, then it doesn't go through the uh shift register to drive the display. Exactly what I said.

**Dave Jones:** So, that's interesting. put as much data in as you want, but you don't get out until until you clock it. Until you clock it. That is interesting. Why are they bothering to update the information like that? So, there is the

**Dave Jones:** clock and there is your data. There it is there. So, wow. Big difference. They're just wasting their time. Literally. Okay, so again, I'm going to probe this sucker. All right, there's our data. There's our clock. I need you to press

**Dave Jones:** Oh, hang on. Whoa. Single? Uh run stop. Yep, cool. We captured it. There we go. So, we now have a time correlated signal between there. There you go. So, they're feeding in They're doing the data-y thing there. So,

**Dave Jones:** Data is down the bottom, clock up the Data is down the bottom, clock's up the top. You can tell it's clock because it's all periodic. There you go. And you can see that they're feeding in uh well, we can

**Dave Jones:** actually We We can actually have a look here. So, now let's try and decode these displays, Sagan. One of the displays here only has looks like one of the bits turned on. Is that correct? One of the seg- Oh, no. Hang on.

**Dave Jones:** One of the one. It's only got one of the segments turned on. Which display has one of the segments turned on? Surprise, surprise, that one. So, that maps over to there like that. Sagan's probably not following this cuz he

**Dave Jones:** hasn't watched my previous video. Well, actually I was going to this morning because I do check your subscriber. You do? Oh, he's one You're one of my subscribers. One of my valued subscribers. Thank you. I But, you're not on the forum though.

**Dave Jones:** No. No, no. school laptop and like they don't allow that sort of stuff. Right, yeah. Anyway, I'll have to talk to him about that. Okay, let's see if we can correlate this. You remember in the previous video how our data

**Dave Jones:** shifted in over here on this chip here, okay? So, that would actually So, it's got to shift in first, but it is basically the last to come out. This one with our single digit there, we just so happen to capture it when that

**Dave Jones:** little flashing decimal point is turned on, okay? So, that one is actually where that controlled by this chip, which is where our data is first shifted in. So, what happens is is the first one to shift in over here has to be the last

**Dave Jones:** digit over here, okay? So, it the first data that goes in here has to be shifted all the way over to here so that data there ends up in this chip here. It's even correlated. U1, U2, U2, U3, U4, U5.

**Dave Jones:** U1, U2, U2, U4, U5, U6. It It It directly maps over like that. And here, have we got two segments turned on or is it more? It depends on You'd have to go in here. No? So, a second one, it

**Dave Jones:** looks like we've got one, two, three, four digits on. So, our second display, has it got four digits? One, two, three, that's digits. I keep getting the terminology confused. Segments. Segments. It's got four segments turned on and that correlates

**Dave Jones:** perfectly with that over there, doesn't it, Sagan? Yep. Surprise, surprise. What a coincidence. Coincidence. Engineering's always amazing coincidences like that. Wow. Well done, dude. All right. learned nothing is a coincidence. Nothing is a coincidence in engineering, that's right. Everything happens for a

**Dave Jones:** reason. Call it fate. Call it luck. Call it karma. I believe that everything happens for a reason. It's just data going in. Data going in willy-nilly and there's a dead period here and they've got a little flurry of data here. What Why? I mean, this

**Dave Jones:** data's useless to even generate it if you're not clocking it through. So, that's I don't know. Um that's just an artifact of this state machine that they're using inside. I'm sure it's the actual uh PLD here that makes

**Dave Jones:** Would it be? I don't know. I'd have to trace it out, actually. We're in the right I assume it's coming from the Xilinx uh CPLD here. Um that was I think most people's theory was that it was that and not the

**Dave Jones:** microcontroller. So, can you come up with any other reason, Sagan? Any theory why they're bothering to clock the data in here other than that I just think it's a just a artifact of the state machine. It just keeps doing its thing and I don't know.

**Dave Jones:** Think of any other reason? No, I've only got two sides. Okay, two sides. What side what? The technical technical side of my brain says I've got absolutely no idea. Yeah. Side two of my brain says it's data running free.

**Dave Jones:** Oh, data running It's just free-running data. Free-range data. Yeah. Free-range data. Okay, it's free-range data. That's That's a Yep. Yep. Free-range data. There you go. It's probably organic. I think it's organic free range data. We'll call that. Yeah. Okay. There you go.

**Dave Jones:** Got past security. New terminology invented by Sagan. Free range data. Oh god. Getting free range data. Data. That's good. Terrific. So there you go. The segment current. I'm not going to tap in there and try and gen- get the No, no, yeah, we didn't

**Dave Jones:** even have a series resistor, did we? So like I'd have to like budge in a series resistor somewhere if you wanted to actually see the current consumption. I mean the entire board if you're interested is taking 100 milliamps at 24

**Dave Jones:** volts. Fair amount, you know, 2.4 watts. Geez, that's you know. But yeah, we we don't care about the segment current. So yeah, we do know that they're uh shifting in the data like that. Although we No, we haven't

**Dave Jones:** correlated the blanking line as well. We've got to We need three hands to probe this thing to get the blanking line. Should we go to the effort, Sagan? Yeah. Mhm. Probe. What? Is it probe's already up? Oh. You have to close that up.

**Dave Jones:** jeez. Okay, so all we've got really is the LED um drive like that. So let's probe that. See if we can see anything. I'm going to have to do this three hands. Okay. There's our clock. There you go. I can

**Dave Jones:** do this. I can do this. And pin eight. Yeah? Yeah. Okay. Press stop. Okay, so what we've got here is all this stuff in here is just noise. It's just because we're not probing, you know, it's just picking up

**Dave Jones:** just rubbish from here. So we ignore that. But it is you can see that it's it's grounded down here. So this is the display period. So it's on. So it's on during this period. And then when it goes high like this,

**Dave Jones:** this This 500 millivolts per division. There you go. And then during this period it's actually blanking. So, let's go to a wide We're going to have to re- do this, Segan. Let's go out. Like that. And Hold the tongue at the right angle and

**Dave Jones:** go. There we go. Okay, hopefully we've got enough memory depth to see that. There are Yep. Okay. So, yeah, only during So, it blanks it It blanks it during the period that it's updating the display. Otherwise, you'd see all the data turning off and on

**Dave Jones:** well, real quick. You probably wouldn't see it, but you'd get flicker on the display. So, they're effectively turning that off there. So, it stays on for 20 milliseconds. So, it updates the display almost every 20 milliseconds. I think

**Dave Jones:** it's a smidge over 21 milliseconds. Round it to 20 milliseconds, which it keeps the information on and then updates it. So, it just updates the display every 20 milliseconds. No, if they're leaving it on all the time then they're not multiplexing

**Dave Jones:** the individual segments. That would mean that they're not doing that. But just changes the whole perspective of this. It does, doesn't it, Segan? It changes everything. Not multiplexing Because yeah, so that common collector output is low which means that, you know, if you're getting

**Dave Jones:** the one the one Z data out here, if you're getting the ones out of your chip, which turns the segment on, then it's going to switch those on. So, they're not actually multiplexing this thing. It's just nuts. And of course,

**Dave Jones:** they're they're shift registers. So, once you've shifted that data in, the data's going to stay on the output here. If you feed out the ones to this out of this chip, then they're going to stay on. And as long as

**Dave Jones:** that common collector is low, then it's going to source current through all of those. So, it looks like they're not multiplexing this thing at at all. They're not doing individual segments. They're actually turning on all of the displays. But, we didn't

**Dave Jones:** really see any brightness change, did we, Sagan? Although, the eye is incredibly good at compensating um for brightness changes, it's the eye's one of the most amazing high dynamic range things in the world. The eye is amazing. You can kind of stare at the sun, kind

**Dave Jones:** of sort of, not really. But, and then you can see right down in the dark, and it gains things up, and it's it's really amazing. So, yeah, um the eye is very adaptive. I think it's got 10 orders or something of dynamic

**Dave Jones:** range. It's got massive and massive dynamic range. It's got more than 40 dB. The eye has more than 40 dB of dynamic range. I can tell you that for nothing. Um so, yeah, I It doesn't look like it's

**Dave Jones:** multiplexing that. So, there you have it, Sagan. But, guess what? What? Multiplexing it from a certain point of view. From a certain point of view. Sagan's always throwing in Star Wars references. Yeah. It It wouldn't It wouldn't be me.

**Dave Jones:** So, what they're doing is Yeah, like I don't recommend you drive your displays like this. So, what they're relying on is the RDS on of the HC161 driver in here because there's no dropper resistors at all. So, well,

**Dave Jones:** there is effectively inside the chip the RDS on of the output MOSFET. They're relying on that to drop the current for each segment here. So, I think they have to be driving this at a really low voltage. So, let's actually have a

**Dave Jones:** squeeze at the at the voltage. So, we're looking at pin two here. It's got to be low. Um so, well, actually one RI TX That That's one of the VCC inputs. What's pin one? That's 12 V. Okay, they're definitely

**Dave Jones:** not the HC, it only goes up to six, so it's definitely got to be 3.3 or under, be my guess. Woah! 1.95. Um uh technically, that's actually under the minimum spec, isn't it? For a 74HC, it'll go down to 2 volts. It's actually

**Dave Jones:** 1.95. Oh my goodness, it's just oh, the poor the poor thing. Let's actually disconnect the display, right? So, it's drawing no So, it's drawing no current and see what that voltage rail goes to. Oh. See if it's actually a solid 2 volts or

**Dave Jones:** whether or not it's just dropped. Yeah, uh there it is. They're supplying a solid 2 volts, so they're they're as well, you know, so yeah, I think they've they've deliberately tried to set it for 2 volts, which is the absolute minimum

**Dave Jones:** required for the 74HC series logic to work, so they get That's how they're getting away with this without dropper resistors and the high brightness. So, and I know there's people in the comments that'll go, "Oh, yeah, that's pretty clever." Um

**Dave Jones:** Okay. Yeah, maybe. If you would like if you really couldn't afford those dropper resistors and you had to have a high brightness display and you were like and so you'd rely on the um RDS on of the HC output driver, the

**Dave Jones:** upper MOSFET in there driving it. Uh yeah, nah, but they're getting away with it and that's how they're doing it. They're driving it at a fixed 2 volts, so there's got to be a 2 volt rail on here somewhere. So, yeah, for this sort

**Dave Jones:** of like high certification environment where this thing's being used, like in potentially explosive atmospheres and stuff, they go to all the effort to like engineer cases with these O-rings and everything. And the extra penetration depth on the case and

**Dave Jones:** everything when they join together to stop the explosions coming out and igniting the atmosphere and all that and all the regulations that goes involved that's involved in getting that. And they drive the displays like that. Um yeah, okay.

**Dave Jones:** Just why can't you just put the dropper resistors in? I mean, if I was like like analyzing this design for certification, I don't know if it's like part of the standard, maybe they're just not looking at that sort of thing, but

**Dave Jones:** I'd go, "How are you limiting your current in your LEDs?" Oh, you've got no current limiter? Uh fail. There you go, right on the chip. Yeah, 1.5, 1.95 right on the chip. So, that's how they're doing it. Technically, that's under spec. So,

**Dave Jones:** there you go. That was certainly uh unexpected. I expected to see a individual segment multiplex display, but I guess they've done I'd something better that allows them to have a more uh you know, a better clearer display. Cuz that is pretty bright, you know, I

**Dave Jones:** don't know the actual um you know, output of that. I got no real easy way to measure that, but it is, you know, pretty bright even with my lab lights on here. Um so, yeah, I'm sure that is, you

**Dave Jones:** know, reasonably outdoor readable, which is what you need this thing because it's used in outdoor environment. And that's how they're doing it. And that's how, of course, we can do this uh to drive this board. We can simply have a 2-V rail

**Dave Jones:** as well. Um why not? Let's duplicate what they do. Although, everyone will complain, "Oh, Dave, he's showing bad design practice." Well, you know, it's not me. Just copying Benchy. So, yeah, we have uh two options there. One is to to exactly the same as what

**Dave Jones:** they're doing. It's just like shifting the data uh like normal and you know just like have it displayed on just update it periodically like they're updating every 20 milliseconds whatever. Like you don't even have to update the display that quickly. You can just leave

**Dave Jones:** it on all the time. You can update it once per second or whatever. And and the free range data of course new industry term. There it is free range data. That's for when you sending data that can't possibly be used

**Dave Jones:** because you're not clocking it. So it's just free range. Or yep, we could just drive the sucker at 2 volts.

**Dave Jones:** This terrible Muriel but you know I can't say I haven't done it when I was a kid you know. Jeez, come on. Put your dropper resistors in. But anyway, yeah, we can certainly drive this sucker at 2 volts.

**Dave Jones:** But then if you want to drive it from other logic, yeah, you might need like level translator or something like that depending on what you're doing. Oh, and I just realized that yeah, 1 volt per division the data is only 2 volts. I

**Dave Jones:** didn't actually notice that before. So whatever chip on this board is driving that it's also running at 2 volts as well. Or is there a like a level translator on there? Now I have to inspect the board a bit more. This is

**Dave Jones:** just like this has nothing to do with the actual project. So sorry for taking you know another 30 minutes but this is just interesting. So that's the actual segment voltage that we're dropping 1.65. I assume it's going to be like you know

**Dave Jones:** they're going to be all reasonably matched you know kind of sort of. So there you have it. That's a rather interesting part two. So I think we'll leave it at that. Yeah, we can just drive this thing. We don't have to go

**Dave Jones:** cuz it's more complicated to drive this thing like multiplex each individual segment. It's much easier like from a software point of view to actually just drive this thing the way they did it there. Much simpler and then just yeah

**Dave Jones:** supply to volts and Bob's your uncle. Um, and it looks like you can get away with it and that's what they're doing here and we could get away with that as well. Anyway, well, it depends. Um, because you know, we want this thing to

**Dave Jones:** be battery powered. So, yeah, well, that's the thing. I don't know. I maybe in another video I'm going to have to measure how much uh, power consumption this all takes and I won't do it in this video, measure individual segment

**Dave Jones:** currents and uh, stuff like that. So, yeah, if we do want to reuse this, um, it's not the best thing because uh, yeah, it may just draw too much uh, battery power if we want to like have the display on all the time and power it

**Dave Jones:** from an internal battery. That might be troublesome. So, anyway, hope you enjoyed the video, found it interesting. If you did, give it a big thumbs up. As always, comments and suggestions down below for the MacGyver project here and

**Dave Jones:** I'll catch you next time.
