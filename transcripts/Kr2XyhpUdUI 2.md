---
video_id: Kr2XyhpUdUI
title: EEVblog 1493 - MacGyver Project - Part 2
url: https://www.youtube.com/watch?v=Kr2XyhpUdUI
source: youtube-asr
timestamps: {"0": 0, "1": 26, "2": 44, "3": 63, "4": 97, "5": 112, "6": 138, "7": 154, "8": 172, "9": 190, "10": 213, "11": 233, "12": 252, "13": 270, "14": 308, "15": 326, "16": 340, "17": 358, "18": 379, "19": 408, "20": 428, "21": 457, "22": 472, "23": 486, "24": 504, "25": 523, "26": 546, "27": 561, "28": 579, "29": 595, "30": 632, "31": 651, "32": 669, "33": 688, "34": 706, "35": 723, "36": 742, "37": 761, "38": 790, "39": 808, "40": 830, "41": 861, "42": 890, "43": 917, "44": 939, "45": 979, "46": 992, "47": 1012, "48": 1026, "49": 1043, "50": 1076, "51": 1096, "52": 1114, "53": 1148, "54": 1163, "55": 1194, "56": 1217, "57": 1251, "58": 1281, "59": 1300, "60": 1313, "61": 1328, "62": 1362, "63": 1379, "64": 1404, "65": 1424, "66": 1457, "67": 1484, "68": 1513, "69": 1546, "70": 1569, "71": 1595, "72": 1621, "73": 1649, "74": 1662, "75": 1689, "76": 1718, "77": 1746, "78": 1771}
---

**Dave Jones:** Hi, this is part two in the MacGyver project because nobody can come up with a better name for the project. So, I'm going to stick with the MacGyver project. Um, and I thought we'd actually uh power up this uh board, the display board that we reverse engineered in part one, linked in up here and down below if you haven't seen it. Um, and there are a few questions regarding like actually driving this thing, but I thought like does it actually work? Like so we don't want to go through the whole effort of

**Dave Jones:** actually designing a circuit to drive this thing, building it up, and then finding uh there's something wrong with this. Um, that would really ruin your day. So, I thought we'd take the existing board out of here and just hook it up. I mean, we shouldn't need anything else. I mean, presumably if we power it on, then we're going to get something on here. Um, shouldn't we, Mr.

**Dave Jones:** Assistant? Say hi. Well, I'm Mr. Assistant. You're Mr. Assistant. Hooray! Yay! Sagan's here with me. Hello. There he is. Um, yeah, so we're going to power this thing up. So, let's have a look at this interface here, Sagan. Let's have a look. What can you see there?

**Dave Jones:** We've got 0 V, 24 24 V? Volts? And I don't have no what mA uh that'll be uh uh that's the milliamp interface. That's the um 4 to 20 milliamp current interface, I think. And 485 is RS485. That's a really old um serial protocol, still used though. Um, and 12 V I don't think 12 V is going to be an input. I think that might be an output. Anyway, so we've got the uh got the cable here from the uh casing, and you can see that

**Dave Jones:** yeah, the 12 V is this white wire here, but basically yeah, we've got the uh 24 V positive and negative, yeah? So, I think for a safe bet is just to connect up the 24 V. Volts. And see what happens.

**Dave Jones:** what happens. See if the magic smoke escapes. What do you think, Sagan? So, um up here is the So, that's the interface board there and uh yeah, we've got 0 24 V and there's no 12 V here. I don't see it. I'm not blind, am I, Sagan? There's no 12 V there. There's the uh 4 to 20 mA output, but so yeah, I reckon that 12 V is an output. So, that thing and that I reckon it's an output for something else. Um I don't know. Goes somewhere

**Dave Jones:** else internally, maybe. Um so, let's hook up 0 and 24 V and see what's what. So, is our power supply turned off on channel two? No, it's not. There we go. Okay, I'm just going to step back cuz I don't want to get blown up.

**Dave Jones:** You're going to step back? I don't want to get blown up. You think the magic smoke's going to escape? Maybe. Sagan's not confident. No. He's not confident. All right. Confidence is not high. Okay. So, 24 V So, we want to program that.

**Dave Jones:** So, Sagan, can you program that for me? He's never used it before. He's never used the Rohde & Schwarz power supply jobbie. Okay. So, well, there's different channels. So, this is channel two. So, this Yeah, oh yeah, yeah, it's channel two up there. So, it is touchy-feely screen.

**Dave Jones:** So, we want to set the voltage to 24 V. So, click here. Yeah? There you go. 24 V, not mV. Oh, oh, it did. Okay, it it defaulted to volts. Okay, cool. So, current-wise, I reckon this whole board is pretty you know, like I don't know, a couple hundred milliamps. It's already set to two .25 amps, 250 milliamps.

**Dave Jones:** Yeah. That sounds good. All right. Have we got the probes around the right way? Red goes to positive, blue is negative. That's a weird European thing. They use blue in Europe for some reason. I don't get it, but anyway, um all right, let's power it up and see see if it does anything. Okay.

**Dave Jones:** Please don't blow up. Please don't blow up. Well, the good thing is is that we've current limited the power supply, Sagan, so It won't blow up. It's It's not going to do much. There's There's not much power behind it there to actually do much. So, let's I I don't think there's any indicator leads on there. Can you see any, Sagan?

**Dave Jones:** Can you see any leads on that board, little surface mount leads or anything? I don't see any. I don't see any, either. No. So, you won't know if it's powered on or off. No. No. Well, no. We'll know by the current draw up here. So, you can read that out as we power it on. Okay. Uh switch it on. You want to press the channel two button?

**Dave Jones:** 0.250 amps. Yeah. Nothing. Zip. It's not drawing any current at all. Um Okay. Oh, maybe like it's got a fuse blown or something. Measure the fuse, Sagan. Let's see what we get. Yeah. That's intact. No worries. Squeeze that sucker. There we go. 0.1 ohms. Right. So, our fuse is intact. So, uh All right. It's not that. Why else would this not work? Uh Maybe the um connector's faulty. Maybe we didn't plug it in properly. That's all I can think of.

**Dave Jones:** Yeah. Or Did I I can't remember when I tore this down I put the board back in. Maybe I didn't connect it. Something dumb like that. Screw terminal. I remember they had screw terminals on the bottom. Okay. So, what we want to do, Sagan, is we want to buzz out So, put it on continuity mode.

**Dave Jones:** Yeah. There we go. Yep. Buzzer. Make sure that Make sure it buzzes. There we go. It buzzes. All right. Uh we want to probe. I'll take one and you take the other. I want to turn We're not in continuity mode.

**Dave Jones:** Uh yeah. We're measuring continuity to the black wire down here. Yep. Yep. Positive. Uh the red one. Do the same for the red one. Yeah, you probably have to get to this side. They're pesky, those connectors. Uh, there we go. All right, so we're getting 24 V. We will definitely be getting 24 V on our board.

**Dave Jones:** So, turn the power supply back on. We didn't click output. Daddy is so dumb. I'm so We didn't click output. Output. Press the output button, please. Hey, look. Look. Look. Here it is. It showed all eights. It showed I think you captured that on camera. It showed all eights and then it showed all decimal points. Turn it off and on again, Sayid.

**Dave Jones:** And shows all eights. Geez, that's pretty bright. And 40 dB. 40 dB. 40.db, yeah. 40 dB. I assume 40 dB is the like power setting for the measurement of the ultrasonic sensor. Um, they've they've got it in dB. I don't know why else you'd have dB. And we've got a flashy LED there, but that's pretty bright.

**Dave Jones:** That display is pretty bright. So, they're running those segments at a uh, you know, fairly juicy current. And by the way, um, in the previous video, we came to the conclusion that they're probably multiplexing this and they're probably multiplexing each individual segment. Cuz you can see, turn it off and on again, Sayid. Hang on.

**Dave Jones:** Uh, Okay. Yeah, go. Hang on. You can see that's a consistent brightness between having all eights on and not having all of them on. So, it looks like I reckon that they're actually multiplexing every single segment. So, not just an individual display. So, they're multiplexing, you know, so then you would have a set amount of current in each segment, but then you've got to multiplex, um, 40 different segments, which is a lot.

**Dave Jones:** Um, but that's how they're That's how they're doing it. And as we said, they didn't have a dropper resistor, but meh, you know. So there there you go. So it works. It's sending It's basically sending the same signal strength across each one of the segments.

**Dave Jones:** Yes. From the one edgy source. The same current. Splits it and puts it into each segment. Yep. Well, it multiplexes it. Multiplexes it. Yeah. So it turns on one segment at a time, but it's doing it so fast It's doing it so fast that you can't see it.

**Dave Jones:** But each one of those segments is turning on at least 40 times per second, at least. Let's just probe some stuff for fun. Let me find a ground point. There we go. That's a ground point. It's very convenient, so I'll hook that up to there.

**Dave Jones:** And we can approve around cuz you don't want to hook your crocodile clip up to the pin headers cuz it can short out the other pins. Trap for young players. Okay, so we've got our pin out here and uh let's have a look at the clock and uh well, the clock. Let's have a look how fast that's going.

**Dave Jones:** 1 2 3 4 and let's have a look here, Sagan. What do we have here? We've got five packets here. Why do you think we've got five packets? Because there's um five digits and each and each line going up and down would mean that one digit's turning on and off.

**Dave Jones:** Correct. of course there'd be different even smaller segments inside those lines. Yeah. Which would be each one of the little um Count how many how many pulses we got in one of those. Um One of those packets. Just maybe the bottom one's easy.

**Dave Jones:** 1 2 3 4 5 6 7 8. Eight? Eight pulses. What a convenience. Um what a coincidence. How many digits have we got in each Oh, how many segments have we got in each digit? That's so coincidental. a coincidence, Sagan.

**Dave Jones:** That's exactly what expect to see. And you can see um they don't update this often. So well, hang on. Well, there we go. Every two divisions, we're at 10 milliseconds per division. So, how much time between each one, Sayid?

**Dave Jones:** 10 milliseconds. Sorry, 20 milliseconds. 20 milliseconds total. So, 20 milliseconds they turn on um they update um or they clock the information into the LED display there. No worries. And these are Yeah, we just got ringing on the bottom. The reason we got horrible ringing down there is because of my uh in inductive um lead here. It's not great. So, yeah, it's a bit how you doing, but you can see the signal. So, no worries. So, that's our clock. And then our data is the pin next to it. And it's more

**Dave Jones:** randomy. Ooh, that's Oh, hang on. That's the trigger level. That's the trigger level. That's all over the shop, isn't it? That's everywhere. Yeah. Wow, so they're really So, we can single shot capture that. If we just single shot capture it a couple of times Oh, hang on. I got to put it back in the middle.

**Dave Jones:** There we go. There we go. It change It'll change a few times cuz we got different displays. So, depending on which one we actually um just happen to trigger off it displays that. So, there you have it. That That is random.

**Dave Jones:** Wow. Okay, so our data's going in every 100 microseconds cuz we're 50 microseconds per division. So, every 100 microseconds we're getting data. What did we say it before on the clock? Uh 10 10 20 milliseconds, wasn't it? Every 20 It was milli or micro?

**Dave Jones:** It was milli. Milli. It was milli, wasn't it? Yeah. So, our data is updating like way more frequently. 20 times, 100 times as fast? Wow. Something like that. That's It's almost constant. The data is almost constant, but the clock is not.

**Dave Jones:** is not. The clock If If you're feeding the data, it's not going to do anything unless you clock it through. Here it is down here. You can feed in all the data you want until the cows come home, but if you don't clock it through, then it doesn't go through the uh shift register to drive the display.

**Dave Jones:** Exactly what I said. So, that's interesting. put as much data in as you want, but you don't get out until until you clock it. Until you clock it. That is interesting. Why are they bothering to update the information like that? So, there is the clock and there is your data.

**Dave Jones:** There it is there. So, wow. Big difference. They're just wasting their time. Literally. Okay, so again, I'm going to probe this sucker. All right, there's our data. There's our clock. I need you to press Oh, hang on. Whoa.

**Dave Jones:** Single? Uh run stop. Yep, cool. We captured it. There we go. So, we now have a time correlated signal between there. There you go. So, they're feeding in They're doing the data-y thing there. So, Data is down the bottom, clock up the Data is down the bottom, clock's up the top. You can tell it's clock because it's all periodic. There you go. And you can see that they're feeding in uh well, we can actually We We can actually have a look here. So, now let's try and decode these

**Dave Jones:** displays, Sagan. One of the displays here only has looks like one of the bits turned on. Is that correct? One of the seg- Oh, no. Hang on. One of the one. It's only got one of the segments turned on. Which display has one of the segments turned on?

**Dave Jones:** Surprise, surprise, that one. So, that maps over to there like that. Sagan's probably not following this cuz he hasn't watched my previous video. Well, actually I was going to this morning because I do check your subscriber. You do? Oh, he's one You're one of my subscribers. One of my valued subscribers. Thank you. I But, you're not on the forum though.

**Dave Jones:** No. No, no. school laptop and like they don't allow that sort of stuff. Right, yeah. Anyway, I'll have to talk to him about that. Okay, let's see if we can correlate this. You remember in the previous video how our data shifted in over here on this chip here, okay? So, that would actually So, it's got to shift in first, but it is basically the last to come out. This one with our single digit there, we just so happen to capture it when that little flashing decimal point is turned

**Dave Jones:** on, okay? So, that one is actually where that controlled by this chip, which is where our data is first shifted in. So, what happens is is the first one to shift in over here has to be the last digit over here, okay? So, it the first data that goes in here has to be shifted all the way over to here so that data there ends up in this chip here.

**Dave Jones:** It's even correlated. U1, U2, U2, U3, U4, U5. U1, U2, U2, U4, U5, U6. It It It directly maps over like that. And here, have we got two segments turned on or is it more? It depends on You'd have to go in here. No? So, a second one, it looks like we've got one, two, three, four digits on. So, our second display, has it got four digits? One, two, three, that's digits.

**Dave Jones:** I keep getting the terminology confused. Segments. Segments. It's got four segments turned on and that correlates perfectly with that over there, doesn't it, Sagan? Yep. Surprise, surprise. What a coincidence. Coincidence. Engineering's always amazing coincidences like that. Wow. Well done, dude.

**Dave Jones:** All right. learned nothing is a coincidence. Nothing is a coincidence in engineering, that's right. Everything happens for a reason. Call it fate. Call it luck. Call it karma. I believe that everything happens for a reason. It's just data going in. Data going in willy-nilly and there's a dead period here and they've got a little flurry of data here. What Why? I mean, this data's useless to even generate it if you're not clocking it through. So, that's I don't know. Um that's just an artifact of this state machine that

**Dave Jones:** they're using inside. I'm sure it's the actual uh PLD here that makes Would it be? I don't know. I'd have to trace it out, actually. We're in the right I assume it's coming from the Xilinx uh CPLD here.

**Dave Jones:** Um that was I think most people's theory was that it was that and not the microcontroller. So, can you come up with any other reason, Sagan? Any theory why they're bothering to clock the data in here other than that I just think it's a just a artifact of the state machine. It just keeps doing its thing and I don't know.

**Dave Jones:** Think of any other reason? No, I've only got two sides. Okay, two sides. What side what? The technical technical side of my brain says I've got absolutely no idea. Yeah. Side two of my brain says it's data running free.

**Dave Jones:** Oh, data running It's just free-running data. Free-range data. Yeah. Free-range data. Okay, it's free-range data. That's That's a Yep. Yep. Free-range data. There you go. It's probably organic. I think it's organic free range data. We'll call that. Yeah. Okay. There you go.

**Dave Jones:** Got past security. New terminology invented by Sagan. Free range data. Oh god. Getting free range data. Data. That's good. Terrific. So there you go. The segment current. I'm not going to tap in there and try and gen- get the No, no, yeah, we didn't even have a series resistor, did we? So like I'd have to like budge in a series resistor somewhere if you wanted to actually see the current consumption. I mean the entire board if you're interested is taking 100 milliamps at 24 volts. Fair amount, you know, 2.4 watts.

**Dave Jones:** Geez, that's you know. But yeah, we we don't care about the segment current. So yeah, we do know that they're uh shifting in the data like that. Although we No, we haven't correlated the blanking line as well. We've got to We need three hands to probe this thing to get the blanking line. Should we go to the effort, Sagan?

**Dave Jones:** Yeah. Mhm. Probe. What? Is it probe's already up? Oh. You have to close that up. jeez. Okay, so all we've got really is the LED um drive like that. So let's probe that. See if we can see anything. I'm going to have to do this three hands. Okay.

**Dave Jones:** There's our clock. There you go. I can do this. I can do this. And pin eight. Yeah? Yeah. Okay. Press stop. Okay, so what we've got here is all this stuff in here is just noise. It's just because we're not probing, you know, it's just picking up just rubbish from here. So we ignore that. But it is you can see that it's it's grounded down here. So this is the display period. So it's on. So it's on during this period.

**Dave Jones:** And then when it goes high like this, this This 500 millivolts per division. There you go. And then during this period it's actually blanking. So, let's go to a wide We're going to have to re- do this, Segan. Let's go out.

**Dave Jones:** Like that. And Hold the tongue at the right angle and go. There we go. Okay, hopefully we've got enough memory depth to see that. There are Yep. Okay. So, yeah, only during So, it blanks it It blanks it during the period that it's updating the display. Otherwise, you'd see all the data turning off and on well, real quick. You probably wouldn't see it, but you'd get flicker on the display. So, they're effectively turning that off there. So, it stays on for 20 milliseconds. So, it updates the display

**Dave Jones:** almost every 20 milliseconds. I think it's a smidge over 21 milliseconds. Round it to 20 milliseconds, which it keeps the information on and then updates it. So, it just updates the display every 20 milliseconds. No, if they're leaving it on all the time then they're not multiplexing the individual segments.

**Dave Jones:** That would mean that they're not doing that. But just changes the whole perspective of this. It does, doesn't it, Segan? It changes everything. Not multiplexing Because yeah, so that common collector output is low which means that, you know, if you're getting the one the one Z data out here, if you're getting the ones out of your chip, which turns the segment on, then it's going to switch those on. So, they're not actually multiplexing this thing. It's just nuts. And of course, they're they're shift registers. So,

**Dave Jones:** once you've shifted that data in, the data's going to stay on the output here. If you feed out the ones to this out of this chip, then they're going to stay on. And as long as that common collector is low, then it's going to source current through all of those. So, it looks like they're not multiplexing this thing at at all. They're not doing individual segments. They're actually turning on all of the displays. But, we didn't really see any brightness change, did we, Sagan? Although, the eye is

**Dave Jones:** incredibly good at compensating um for brightness changes, it's the eye's one of the most amazing high dynamic range things in the world. The eye is amazing. You can kind of stare at the sun, kind of sort of, not really.

**Dave Jones:** But, and then you can see right down in the dark, and it gains things up, and it's it's really amazing. So, yeah, um the eye is very adaptive. I think it's got 10 orders or something of dynamic range. It's got massive and massive dynamic range. It's got more than 40 dB.

**Dave Jones:** The eye has more than 40 dB of dynamic range. I can tell you that for nothing. Um so, yeah, I It doesn't look like it's multiplexing that. So, there you have it, Sagan. But, guess what? What? Multiplexing it from a certain point of view.

**Dave Jones:** From a certain point of view. Sagan's always throwing in Star Wars references. Yeah. It It wouldn't It wouldn't be me. So, what they're doing is Yeah, like I don't recommend you drive your displays like this. So, what they're relying on is the RDS on of the HC161 driver in here because there's no dropper resistors at all. So, well, there is effectively inside the chip the RDS on of the output MOSFET. They're relying on that to drop the current for each segment here. So, I think they have

**Dave Jones:** to be driving this at a really low voltage. So, let's actually have a squeeze at the at the voltage. So, we're looking at pin two here. It's got to be low. Um so, well, actually one RI TX That That's one of the VCC inputs.

**Dave Jones:** What's pin one? That's 12 V. Okay, they're definitely not the HC, it only goes up to six, so it's definitely got to be 3.3 or under, be my guess. Woah! 1.95. Um uh technically, that's actually under the minimum spec, isn't it? For a 74HC, it'll go down to 2 volts. It's actually 1.95.

**Dave Jones:** Oh my goodness, it's just oh, the poor the poor thing. Let's actually disconnect the display, right? So, it's drawing no So, it's drawing no current and see what that voltage rail goes to. Oh. See if it's actually a solid 2 volts or whether or not it's just dropped.

**Dave Jones:** Yeah, uh there it is. They're supplying a solid 2 volts, so they're they're as well, you know, so yeah, I think they've they've deliberately tried to set it for 2 volts, which is the absolute minimum required for the 74HC series logic to work, so they get That's how they're getting away with this without dropper resistors and the high brightness. So, and I know there's people in the comments that'll go, "Oh, yeah, that's pretty clever." Um Okay.

**Dave Jones:** Yeah, maybe. If you would like if you really couldn't afford those dropper resistors and you had to have a high brightness display and you were like and so you'd rely on the um RDS on of the HC output driver, the upper MOSFET in there driving it. Uh yeah, nah, but they're getting away with it and that's how they're doing it.

**Dave Jones:** They're driving it at a fixed 2 volts, so there's got to be a 2 volt rail on here somewhere. So, yeah, for this sort of like high certification environment where this thing's being used, like in potentially explosive atmospheres and stuff, they go to all the effort to like engineer cases with these O-rings and everything. And the extra penetration depth on the case and everything when they join together to stop the explosions coming out and igniting the atmosphere and all that and all the regulations that goes involved

**Dave Jones:** that's involved in getting that. And they drive the displays like that. Um yeah, okay. Just why can't you just put the dropper resistors in? I mean, if I was like like analyzing this design for certification, I don't know if it's like part of the standard, maybe they're just not looking at that sort of thing, but I'd go, "How are you limiting your current in your LEDs?" Oh, you've got no current limiter? Uh fail. There you go, right on the chip. Yeah, 1.5, 1.95 right on the

**Dave Jones:** chip. So, that's how they're doing it. Technically, that's under spec. So, there you go. That was certainly uh unexpected. I expected to see a individual segment multiplex display, but I guess they've done I'd something better that allows them to have a more uh you know, a better clearer display.

**Dave Jones:** Cuz that is pretty bright, you know, I don't know the actual um you know, output of that. I got no real easy way to measure that, but it is, you know, pretty bright even with my lab lights on here. Um so, yeah, I'm sure that is, you know, reasonably outdoor readable, which is what you need this thing because it's used in outdoor environment. And that's how they're doing it. And that's how, of course, we can do this uh to drive this board. We can simply have a 2-V rail

**Dave Jones:** as well. Um why not? Let's duplicate what they do. Although, everyone will complain, "Oh, Dave, he's showing bad design practice." Well, you know, it's not me. Just copying Benchy. So, yeah, we have uh two options there. One is to to exactly the same as what they're doing. It's just like shifting the data uh like normal and you know just like have it displayed on just update it periodically like they're updating every 20 milliseconds whatever.

**Dave Jones:** Like you don't even have to update the display that quickly. You can just leave it on all the time. You can update it once per second or whatever. And and the free range data of course new industry term. There it is free range data. That's for when you sending data that can't possibly be used because you're not clocking it. So it's just free range. Or yep, we could just drive the sucker at 2 volts.

**Dave Jones:** This terrible Muriel but you know I can't say I haven't done it when I was a kid you know. Jeez, come on. Put your dropper resistors in. But anyway, yeah, we can certainly drive this sucker at 2 volts.

**Dave Jones:** But then if you want to drive it from other logic, yeah, you might need like level translator or something like that depending on what you're doing. Oh, and I just realized that yeah, 1 volt per division the data is only 2 volts. I didn't actually notice that before. So whatever chip on this board is driving that it's also running at 2 volts as well. Or is there a like a level translator on there? Now I have to inspect the board a bit more. This is just like this has nothing to do with

**Dave Jones:** the actual project. So sorry for taking you know another 30 minutes but this is just interesting. So that's the actual segment voltage that we're dropping 1.65. I assume it's going to be like you know they're going to be all reasonably matched you know kind of sort of. So there you have it. That's a rather interesting part two. So I think we'll leave it at that. Yeah, we can just drive this thing. We don't have to go cuz it's more complicated to drive this thing like multiplex each individual

**Dave Jones:** segment. It's much easier like from a software point of view to actually just drive this thing the way they did it there. Much simpler and then just yeah supply to volts and Bob's your uncle. Um, and it looks like you can get away with it and that's what they're doing here and we could get away with that as well. Anyway, well, it depends. Um, because you know, we want this thing to be battery powered. So, yeah, well, that's the thing. I don't know. I maybe in another video I'm going to have to

**Dave Jones:** measure how much uh, power consumption this all takes and I won't do it in this video, measure individual segment currents and uh, stuff like that. So, yeah, if we do want to reuse this, um, it's not the best thing because uh, yeah, it may just draw too much uh, battery power if we want to like have the display on all the time and power it from an internal battery. That might be troublesome. So, anyway, hope you enjoyed the video, found it interesting.

**Dave Jones:** If you did, give it a big thumbs up. As always, comments and suggestions down below for the MacGyver project here and I'll catch you next time.
