---
video_id: LjfIS65mwn8
title: EEVblog #39 - Microchip PICkit 3 Programmer/Debugger Review
url: https://www.youtube.com/watch?v=LjfIS65mwn8
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the EEVblog. I'm your host, Dave Jones. It's equipment review time. Well, not so much equipment, but this week we've got the Microchip PICkit 3 uh debugger / programmer. Let's check it out. Uh it's $45 just on its own as

**Dave Jones:** opposed to $35 for the old PICkit 2, so it's gone up a bit. All right, let's check them out side by side. Here's the new PICkit 3 and there's the old one. And as you can see, they're an identical

**Dave Jones:** uh case, absolutely identical except this is a new funky translucent red and you can actually see the circuitry inside it. But they've actually changed the name of the LEDs, if you notice. Uh the old one was power, target, and busy.

**Dave Jones:** And the new one is power, active, and status. Why? Why change it? It's supposed to be an identical product, just a slight upgrade. Why change it? I don't know. It's nuts. Now, the reason this new one is more expensive than the old one by

**Dave Jones:** $10 is because they use a new uh 24F series 16-bit PIC in here. It's a much bigger and more powerful uh PIC controller as opposed to the old one which had an 18F series uh PIC in it. But they're both a standard USB

**Dave Jones:** interface and but it's just uh the new one's gruntier and more powerful, but only works at 3.3 V. It doesn't work at 5 like the old one did. So, it means they have to have some extra uh extra voltage regulator in

**Dave Jones:** there and they've actually put in some poly switches. I can see some protection poly switches inside there as well, which is a good uh fairly good addition, I think. Ever since this first came out, even slightly before it when the rumors

**Dave Jones:** started coming out, people were saying it's not nearly as good as the old one and it's supposed to be a direct replacement. Microchip are going to discontinue this uh fairly soon. In fact, they've dropped all new device support for the PICkit 2. You have If

**Dave Jones:** you want the new devices coming out, you have to get the PICkit 3. Which, okay, fair enough. If it's exactly the same capability, and you'd think so because it's the same target market. It's got exactly the same looks, the same

**Dave Jones:** interface, it all works the same. In fact, the circuitry inside's a bit different, but fundamentally, it's it's basically the same. It can power the circuit under test and at at different voltages, and it's got the program to go

**Dave Jones:** button on it, and it's it should be identical. But, it's not. Now, I was going to use this for a while before I did a blog on it so I could, you know, thoroughly evaluate and see how it goes.

**Dave Jones:** But, I've used it for like an hour or something today, and that was enough to tick me off. It's really annoying. They've made uh quite a few changes to the way it works with MPLAB, and I don't like it. It sucks. Now, the old PICkit

**Dave Jones:** 2, what it does is if it doesn't detect when you plug it in, if it doesn't detect that there's power on your user board, it will actually supply power to the thing. And this thing's going The new PICkit 3 has got that option as

**Dave Jones:** well, but it's not on by default. It won't automatically detect. They've done away with this automatic voltage detection feature, and that was fantastic. And they've killed it. Why, you idiots? Second thing I noticed is that when you hook it up, and okay, I figured out

**Dave Jones:** you've got to switch the power on manually now, it uh normally it tells you it's hooked up to the chip, it tells you what chip it is, and what device revision it is. Now, it tells you it's connected, okay. Once you turn the power

**Dave Jones:** on, it says, "I'm connected." But, it doesn't tell you what chip it is. I hooked it up to one and I thought, "I'll do a programming test." And uh I hooked it up. This has actually got a PIC uh

**Dave Jones:** 16F833 chip on it. And I I thought I'd time it to see how long it takes to program compared to the old one. Now, the old PICkit 2 took 5 seconds or thereabouts. The new PICkit 3 took about 7. I tried

**Dave Jones:** it multiple times and yeah, it seems slower. So, it's it's definitely not faster. And it's got this new faster 24F series PIC in it. You'd think it'd be quicker. But no, it's actually slower if anything. Another thing I noticed about

**Dave Jones:** it straight away is that the old PICkit 2, the tiny little status LEDs on here, they were they were they weren't too hard to see, but you could see them. They weren't very bright. This new one, they you can't

**Dave Jones:** even see them. You have to look at straight on. You have to be directly above it staring at it like this to see that the damn LEDs are on. If you tilt it I have to be straight on. So, if you

**Dave Jones:** tilt it to the side a bit, you can't even tell if the LEDs are on. It's nuts. It's crap product design. With the old PICkit 2, you used to be able to program your project under test anywhere from 2.5 V

**Dave Jones:** up to 5 V. This one is limited to 3 to 5.5. So, they've changed the output range. And that's no good for say my microwatch project. And the changes don't stop there. There's another change they've made with this. They've changed

**Dave Jones:** the whole architecture of how the firmware works in this thing. Now, if you change your device in MPLAB, if you want to change from this part to some other part, then you have to download new firmware. It pops up and says,

**Dave Jones:** "Sorry, your current firmware has to be changed to support the new chip." And well, it it does it automatically. It sits there and it reprograms the damn thing, but you have to do it every time. It's annoying. What did they change the

**Dave Jones:** whole software architecture for? It's nuts. And if that change in direction isn't enough, well, they've completely changed the concept. It's own This is only designed to work with MPLAB. They have dropped that really cool utility you had for the PICkit 2 as a

**Dave Jones:** standalone programming environment. It was really small, it was really quick, it was simple, it's all you needed to program, and it also had the very cool logic analyzer feature. This was a actually a four-channel logic analyzer, and you can also use it

**Dave Jones:** the old PICkit 2 as a serial port decoder as well that was built in to that separate software. But the new PICkit 3 doesn't have that separate software, it's nothing. It's got nothing, it's only designed to work with

**Dave Jones:** MPLAB. They've had a complete paradigm change in the way they market and support this thing. Compared to the PICkit 2, they've absolutely screwed it, and I don't know why, and they're going to force people onto this. Now, the

**Dave Jones:** reason I reckon they've done it is because the PICkit 2, I think, I'm only guessing here, I've got no inside knowledge, but I reckon this was designed by, you know, one or maybe two engineers, you know, a really small team

**Dave Jones:** of of guys who wanted to produce a very low-cost tool that people would use and enjoy, and they designed it properly, and Microchip sort of didn't give them any resources or anything like that, and so they they finally came out with that

**Dave Jones:** that and they produced it and they released it, and what do you know? It was massively popular. It took the entire market by storm, this PICkit 2. There was nothing on the market like it for any other micro pro, and I think

**Dave Jones:** Microchip were massively surprised by it. So that's when I reckon management took over. They said, "Ah, the PICkit 2 was so darn successful, we should do a PICkit 3. People will buy it by the truckload." So they started to do what managers do, and

**Dave Jones:** they designed it by committee. They, you know, how can we do it different? They they said, "Ah, you know, these MP management types, that's what they're trained to do. They're trained to think that it's got to be different. You have

**Dave Jones:** to redesign it completely." And they got the software people involved, and they go, "Oh, we can't support that external programmer anymore. That's crap. People have MP Lab. Let's use MP Lab. That's our That's our solution, you know? People don't need this external

**Dave Jones:** programmer thing. What do they want that for? No, we'll force MP Lab upon them." And then, "Oh, we can have some new firmware paradigm we've been thinking of doing. Oh, that'll be fantastic. And download new firmware for each chip.

**Dave Jones:** It's really modular and elegant, and it fits in with all these new software paradigms. Woohoo!" So, they completely drop support for the really cool external programmer software they had for this thing. And I don't reckon we'll ever get it back. Why?

**Dave Jones:** Because some [ __ ] manager at at Microchip who actually, you know, who managed the project on this thing and made those decisions will never admit they're wrong, and never admit that MP Lab sucks if you just want to program a

**Dave Jones:** chip. So, really, we'll never see it. That [ __ ] is probably going to get promoted, too. I can just see the design engineers walking out of the design review meeting for this thing, going, "What the hell just happened?

**Dave Jones:** They're making us change everything? Why? They probably went back to their cubicles and just started bashing their head against the desk." And you know what the stupid thing is? It's entirely fixable. There's There are hardware differences between these, but they

**Dave Jones:** basically operate exactly the same. All this thing needs to make it as good and successful as the PICkit 2 is to fix the damn software, bring back the external programmer, and still, many, many months after this thing's been released, it

**Dave Jones:** still doesn't support the programmer to go feature. Now, I tried to find something good about this compared to the PICkit 2, but I can't really. It's worse in almost every respect, apart from the bigger memory it's got in it,

**Dave Jones:** but you could get that as a third-party add-on for the PICkit 2 anyway. So, there you have it, the PICkit 3. It wins the EE blog [ __ ] product of the week award. Crap.
