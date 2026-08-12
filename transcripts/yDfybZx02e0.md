---
video_id: yDfybZx02e0
title: The Art of Custom PCB Test Jigs
url: https://www.youtube.com/watch?v=yDfybZx02e0
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 44, "3": 66, "4": 86, "5": 107, "6": 114, "7": 129, "8": 139, "9": 149, "10": 161, "11": 172, "12": 187, "13": 199, "14": 207, "15": 217, "16": 225, "17": 236, "18": 251, "19": 265, "20": 274, "21": 288, "22": 297, "23": 315, "24": 326, "25": 339, "26": 348, "27": 359, "28": 373, "29": 382, "30": 393, "31": 408, "32": 415, "33": 424, "34": 433, "35": 441, "36": 453, "37": 467, "38": 475, "39": 487, "40": 506, "41": 513, "42": 524, "43": 532, "44": 541, "45": 551, "46": 562}
---

**Dave Jones:** Here at Redback Test Services, and interesting bit of nails, custom bit of nails thing, and uh it's not much to see here at all. Um yeah, I No, there's nothing to see.

**Dave Jones:** Nothing to see here. So, we check out some of these uh custom bit of nails test solutions, and this one is really brilliant. I'll get him to take you through this at the moment, but got some really like awesome ones here that have a a top board solution with multi-contact down there, and like custom little cutouts for all your boards going in, individual pass fail on the bottom board, and then

**Dave Jones:** you can it's got all the diagrams and stuff on the top, just absolutely brilliant. This is the uh kind of stuff I didn't make this elaborate stuff, but this is the kind of stuff I'd make complete like I'd make these in house, like these bit of nails testers, and yeah, nothing this fancy, of course, but cuz there's a lot of engineering that goes into lot of design

**Dave Jones:** and engineering that goes into the in-lock systems, cuz when you're talking about a board, if you've got like, you know, some of them can have like a hundred plus like pins on there, pogo pins on them, and each one has, you know, X grams of force, X you know, a hundred grams of force or whatever, and it's a lot of force when you push these down, and then

**Dave Jones:** you can get like micro cracking on the boards if you don't actually reinforce them in certain places, so you might do finite element analysis on like the bending stress on the boards and stuff like that, cuz if you get micro cracks in, you know, any of your components, they can fail down the track, like it might pass on this machine, like you put it down, you put

**Dave Jones:** the force on, it passes the test and everything, and then you lift it up, but the act of doing that, you've done some micro cracking in there, and then that'll fail later.

**Dave Jones:** So, you know, there's a lot of art and uh engineering that goes into uh custom uh solutions like these, custom test solutions. I mean, this is you know, this is like a complete uh test stand thing.

**Dave Jones:** And this one's, you know, it looks like it might be simple to test that board, but you know, there's a lot of uh custom stuff in there. You have 470 on the bottom.

**Dave Jones:** We've got about 16 light pipes on the top for LED detection. Oh, okay. So, this is in I was wondering, these didn't look like um uh you know, these look like weird wires.

**Dave Jones:** These are actually fiber optic light pipes, which go over the LEDs down on the board to actually um indicate. And so, fiber optic over to here, and then you've got uh photo receivers in here.

**Dave Jones:** So, this is a photo receiver uh board, which would go into your uh test um system. And and it reads all your indicators to make sure all your LED indicator boards.

**Dave Jones:** And how many test pins on the bottom? Uh 470. 470. Can we see those? Is that 400 Oh. Oh, wow. Look at that. That's insane, right? That is crazy.

**Dave Jones:** Every single aspect of this board is tested. Thorough. That's just nuts. You've also got a part presence detection there. Yep. a board marker there. And here we've got holes so that the board locates properly.

**Dave Jones:** So, that when the operator pops it in, Yep. it drops in the place every single time. Every single Oh, that's nice. Because cuz you don't want to like damage the screen.

**Dave Jones:** You don't want to have a offset like that because Yep. Been there, done that. Wow. boards like you wouldn't believe. So, this is uh for a uh customer board, or is this like a just a demo?

**Dave Jones:** this is a demo board that I I built. I designed this about 3 years ago for another customer. It's a power uh measurement device. So, you've got all your current transformers here.

**Dave Jones:** So, you want to current loop through there. I've got basically you've got voltage coming in here. So, you do voltage and power modifications for eight channels. Nice. And it's capable of three phase as well.

**Dave Jones:** But it we never we never got to to launch it. Um so we decided, "Why don't we use it in our ICT machine?" And we And this board actually tests everything This is an ICT which tests all the single components and it does everything in about 3 seconds.

**Dave Jones:** Three Test that entire board in Does all the electrical test the Can it do Is there a micro on there that needs to be programmed? Cuz you integrate You can integrate micro programming and integrate programming, but that obviously add additional time.

**Dave Jones:** Right. Got it. And what have you written that in? That's All right. So this is your studio? Yep. Yes, it's Visual Studio. So this is This code here is Visual Basic.

**Dave Jones:** And the reason we use Visual Basic is because it's it's anything any engineer can pick up. Yep. Um young or old and it's very easy to read. As you see here, it's like, you know, 10 milliamps you've got a DC of 5 seconds integration time of 5 seconds.

**Dave Jones:** You've got a min max of 4 milliseconds. Delay time for the ramp up and you've got the tolerance there and the test point A and B what you're measuring across.

**Dave Jones:** Right. So That that is brilliant. How many man months are going into a a build like that? Cuz that is like, you know, that that's not quite as almost as complex as it gets in terms of, you know, number of test points and photo receivers and stuff like that.

**Dave Jones:** Okay. Um the the photo receiver board on the top there took me took me about uh 2 weeks to design Yep. and build and assemble and test and probably about a week of firmware.

**Dave Jones:** Right. Um whereas the whole fixture as you see here, barring obviously the the DUT components, I think this was done up in about 8 to 9 weeks. Nice. And That's that's pretty quick actually for something of this magnitude.

**Dave Jones:** Yeah. And the the beauty of the this particular test week, um it is written in Visual Studio, but the back it's got its own back end. So, it's got like the site is all in its own back end.

**Dave Jones:** So, it's got its own interpreter. Yep. And it interfaces with the MTS 30 in the back here. Oh, let's let's go have a look. Which is an ICT. Yep.

**Dave Jones:** So, you've got an analog measurement unit, and you've got 1 2 3 mux cards, which do switching. So, each one of these switch cards has 196 pins. Mhm. And I think the last one is a hybrid card, which is 96 pins.

**Dave Jones:** It's pretty noisy when it's running, but in this in this environment here, everything's noisy. So, you can't even hear it. Oh, really? Okay, so it's actively running now. It's actively running now, yeah.

**Dave Jones:** So, can we actually run a test on it? Yep. All right, go. All right, let's see if we got the errors. There you go. Pass. Winner winner chicken dinner.

**Dave Jones:** 2 seconds. 3 seconds to test 100 470 470 odd points, plus optical and everything else. Very impressive bit of kit. Let's open it up. This particular one has a neat feature.

**Dave Jones:** It's got a wireless probe interface. It's got a wireless probe interface? So, what you do is you take your own custom PCB, you pop it into here, and it mates with these these probes here.

**Dave Jones:** So, it's basically top and bottom the receptacles have got basically probes on the bottom side. Is that a No, that's I thought that was a uh PCB at first, but it's not.

**Dave Jones:** No, it's just a piece of FR4. Yeah. So, the receptacle goes through this plate here. This is ESD, as well as this part of the PCB. And and it pops into there, and basically keeps it rigid.

**Dave Jones:** Keeps it straight. So, when you pop pop your board on there, you can And this is really good because you can put your like your connection for your Sega, your digital IO, your DMM, your power.

**Dave Jones:** You can have it all on this board. Oh, on that custom board, and then yeah. and that minimizes the design down to things. So, you can have like your USB, your Ethernet, all separate.

**Dave Jones:** And it's got total interlock as well. Show us how the um interlock system works. So, the interlock is screws that lock in there. All right, so that closes up like that won't close, but that like that it'll just it'll just jam.

**Dave Jones:** Yep. So, you got to make sure she's sent all the way back. All right. And it closes there. There's you got the interlock key there. That's a Smerschal interlock.

**Dave Jones:** And in behind there is a Datalogic safety relay and that interacting with the You got the four It's a four-wire contact. Um and it goes back and it'll actuate a contactor.

**Dave Jones:** And you basically when it powers up you hear the contactor when you when you close the lid. Got it. And we've also got a second lock here. So, when operators they get a bit uh handsy with the thing and they open it up and they're like, "Oh, you've just stuffed a $4,000 board disabling well halfway through programming."

**Dave Jones:** The Smerschal switch will allow allow you a little bit of wiggle room, but it won't allow you to fully open it, whereas the lock bolt basically locks the handle in place.

**Dave Jones:** Now, the reason obviously for the two is this isn't a safety rated product, whereas this is a safety rated product. Yep. So, you can guarantee the safety of the operator.

**Dave Jones:** exactly right. Yes. By design. That's it. And then you've just got the major test buttons down the bottom. Yeah. Oh, these are just indicating lights. They're just indicating. Okay, I thought they were lights.

**Dave Jones:** You got your This one had a emergency stop feature on it as well. Um Not all products need the emergency stop feature, but some of the sometimes they do.

**Dave Jones:** Ball with pogo pin freebies. I mean, that's that's that's just great. OH, WHAT'S IT OH, that's a pogo pin brush. That's You can Oh, no, no, it's for the beard, surely.

**Dave Jones:** brush, man. It's It's for the beard. Come on. How much uh force on the pogo pins? Let's Let's Let's push those down. That's how much force is required for that many pogo pins.

**Dave Jones:** That's great. Ah. Freebie. I love it. Best freebie here. Yes. See you.
