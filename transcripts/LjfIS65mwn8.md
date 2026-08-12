---
video_id: LjfIS65mwn8
title: EEVblog #39 - Microchip PICkit 3 Programmer/Debugger Review
url: https://www.youtube.com/watch?v=LjfIS65mwn8
source: youtube-asr
timestamps: {"0": 10, "1": 21, "2": 32, "3": 48, "4": 57, "5": 73, "6": 92, "7": 100, "8": 116, "9": 128, "10": 139, "11": 154, "12": 163, "13": 176, "14": 189, "15": 201, "16": 216, "17": 230, "18": 237, "19": 248, "20": 266, "21": 276, "22": 284, "23": 298, "24": 311, "25": 327, "26": 338, "27": 355, "28": 375, "29": 386, "30": 411, "31": 424, "32": 438, "33": 455, "34": 466, "35": 476, "36": 487, "37": 498, "38": 524, "39": 540, "40": 548, "41": 571, "42": 585}
---

**Dave Jones:** Hi, welcome to the EEVblog. I'm your host, Dave Jones. It's equipment review time. Well, not so much equipment, but this week we've got the Microchip PICkit 3 uh debugger / programmer.

**Dave Jones:** Let's check it out. Uh it's $45 just on its own as opposed to $35 for the old PICkit 2, so it's gone up a bit. All right, let's check them out side by side.

**Dave Jones:** Here's the new PICkit 3 and there's the old one. And as you can see, they're an identical uh case, absolutely identical except this is a new funky translucent red and you can actually see the circuitry inside it.

**Dave Jones:** But they've actually changed the name of the LEDs, if you notice. Uh the old one was power, target, and busy. And the new one is power, active, and status.

**Dave Jones:** Why? Why change it? It's supposed to be an identical product, just a slight upgrade. Why change it? I don't know. It's nuts. Now, the reason this new one is more expensive than the old one by $10 is because they use a new uh 24F series 16-bit PIC in here.

**Dave Jones:** It's a much bigger and more powerful uh PIC controller as opposed to the old one which had an 18F series uh PIC in it. But they're both a standard USB interface and but it's just uh the new one's gruntier and more powerful, but only works at 3.3 V.

**Dave Jones:** It doesn't work at 5 like the old one did. So, it means they have to have some extra uh extra voltage regulator in there and they've actually put in some poly switches.

**Dave Jones:** I can see some protection poly switches inside there as well, which is a good uh fairly good addition, I think. Ever since this first came out, even slightly before it when the rumors started coming out, people were saying it's not nearly as good as the old one and it's supposed to be a direct replacement.

**Dave Jones:** Microchip are going to discontinue this uh fairly soon. In fact, they've dropped all new device support for the PICkit 2. You have If you want the new devices coming out, you have to get the PICkit 3.

**Dave Jones:** Which, okay, fair enough. If it's exactly the same capability, and you'd think so because it's the same target market. It's got exactly the same looks, the same interface, it all works the same.

**Dave Jones:** In fact, the circuitry inside's a bit different, but fundamentally, it's it's basically the same. It can power the circuit under test and at at different voltages, and it's got the program to go button on it, and it's it should be identical.

**Dave Jones:** But, it's not. Now, I was going to use this for a while before I did a blog on it so I could, you know, thoroughly evaluate and see how it goes.

**Dave Jones:** But, I've used it for like an hour or something today, and that was enough to tick me off. It's really annoying. They've made uh quite a few changes to the way it works with MPLAB, and I don't like it.

**Dave Jones:** It sucks. Now, the old PICkit 2, what it does is if it doesn't detect when you plug it in, if it doesn't detect that there's power on your user board, it will actually supply power to the thing.

**Dave Jones:** And this thing's going The new PICkit 3 has got that option as well, but it's not on by default. It won't automatically detect. They've done away with this automatic voltage detection feature, and that was fantastic.

**Dave Jones:** And they've killed it. Why, you idiots? Second thing I noticed is that when you hook it up, and okay, I figured out you've got to switch the power on manually now, it uh normally it tells you it's hooked up to the chip, it tells you what chip it is, and what device revision it is.

**Dave Jones:** Now, it tells you it's connected, okay. Once you turn the power on, it says, "I'm connected." But, it doesn't tell you what chip it is. I hooked it up to one and I thought, "I'll do a programming test." And uh I hooked it up.

**Dave Jones:** This has actually got a PIC uh 16F833 chip on it. And I I thought I'd time it to see how long it takes to program compared to the old one.

**Dave Jones:** Now, the old PICkit 2 took 5 seconds or thereabouts. The new PICkit 3 took about 7. I tried it multiple times and yeah, it seems slower. So, it's it's definitely not faster.

**Dave Jones:** And it's got this new faster 24F series PIC in it. You'd think it'd be quicker. But no, it's actually slower if anything. Another thing I noticed about it straight away is that the old PICkit 2, the tiny little status LEDs on here, they were they were they weren't too hard to see, but you could see them.

**Dave Jones:** They weren't very bright. This new one, they you can't even see them. You have to look at straight on. You have to be directly above it staring at it like this to see that the damn LEDs are on.

**Dave Jones:** If you tilt it I have to be straight on. So, if you tilt it to the side a bit, you can't even tell if the LEDs are on. It's nuts.

**Dave Jones:** It's crap product design. With the old PICkit 2, you used to be able to program your project under test anywhere from 2.5 V up to 5 V. This one is limited to 3 to 5.5.

**Dave Jones:** So, they've changed the output range. And that's no good for say my microwatch project. And the changes don't stop there. There's another change they've made with this. They've changed the whole architecture of how the firmware works in this thing.

**Dave Jones:** Now, if you change your device in MPLAB, if you want to change from this part to some other part, then you have to download new firmware. It pops up and says, "Sorry, your current firmware has to be changed to support the new chip." And well, it it does it automatically.

**Dave Jones:** It sits there and it reprograms the damn thing, but you have to do it every time. It's annoying. What did they change the whole software architecture for? It's nuts.

**Dave Jones:** And if that change in direction isn't enough, well, they've completely changed the concept. It's own This is only designed to work with MPLAB. They have dropped that really cool utility you had for the PICkit 2 as a standalone programming environment.

**Dave Jones:** It was really small, it was really quick, it was simple, it's all you needed to program, and it also had the very cool logic analyzer feature. This was a actually a four-channel logic analyzer, and you can also use it the old PICkit 2 as a serial port decoder as well that was built in to that separate software.

**Dave Jones:** But the new PICkit 3 doesn't have that separate software, it's nothing. It's got nothing, it's only designed to work with MPLAB. They've had a complete paradigm change in the way they market and support this thing.

**Dave Jones:** Compared to the PICkit 2, they've absolutely screwed it, and I don't know why, and they're going to force people onto this. Now, the reason I reckon they've done it is because the PICkit 2, I think, I'm only guessing here, I've got no inside knowledge, but I reckon this was designed by, you know, one or maybe two engineers, you know, a really small team of of guys who wanted to produce a very

**Dave Jones:** low-cost tool that people would use and enjoy, and they designed it properly, and Microchip sort of didn't give them any resources or anything like that, and so they they finally came out with that that and they produced it and they released it, and what do you know?

**Dave Jones:** It was massively popular. It took the entire market by storm, this PICkit 2. There was nothing on the market like it for any other micro pro, and I think Microchip were massively surprised by it.

**Dave Jones:** So that's when I reckon management took over. They said, "Ah, the PICkit 2 was so darn successful, we should do a PICkit 3. People will buy it by the truckload." So they started to do what managers do, and they designed it by committee.

**Dave Jones:** They, you know, how can we do it different? They they said, "Ah, you know, these MP management types, that's what they're trained to do. They're trained to think that it's got to be different.

**Dave Jones:** You have to redesign it completely." And they got the software people involved, and they go, "Oh, we can't support that external programmer anymore. That's crap. People have MP Lab.

**Dave Jones:** Let's use MP Lab. That's our That's our solution, you know? People don't need this external programmer thing. What do they want that for? No, we'll force MP Lab upon them."

**Dave Jones:** And then, "Oh, we can have some new firmware paradigm we've been thinking of doing. Oh, that'll be fantastic. And download new firmware for each chip. It's really modular and elegant, and it fits in with all these new software paradigms.

**Dave Jones:** Woohoo!" So, they completely drop support for the really cool external programmer software they had for this thing. And I don't reckon we'll ever get it back. Why? Because some [ __ ] manager at at Microchip who actually, you know, who managed the project on this thing and made those decisions will never admit they're wrong, and never admit that MP Lab sucks if you just want to program a

**Dave Jones:** chip. So, really, we'll never see it. That [ __ ] is probably going to get promoted, too. I can just see the design engineers walking out of the design review meeting for this thing, going, "What the hell just happened?

**Dave Jones:** They're making us change everything? Why? They probably went back to their cubicles and just started bashing their head against the desk." And you know what the stupid thing is?

**Dave Jones:** It's entirely fixable. There's There are hardware differences between these, but they basically operate exactly the same. All this thing needs to make it as good and successful as the PICkit 2 is to fix the damn software, bring back the external programmer, and still, many, many months after this thing's been released, it still doesn't support the programmer to go feature.

**Dave Jones:** Now, I tried to find something good about this compared to the PICkit 2, but I can't really. It's worse in almost every respect, apart from the bigger memory it's got in it, but you could get that as a third-party add-on for the PICkit 2 anyway.

**Dave Jones:** So, there you have it, the PICkit 3. It wins the EE blog [ __ ] product of the week award. Crap.
