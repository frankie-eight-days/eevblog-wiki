---
video_id: nvgW5iWXbts
title: EEVblog #768 - Cordless Anti-Static Wristbands BUSTED!
url: https://www.youtube.com/watch?v=nvgW5iWXbts
source: youtube-asr
timestamps: {"0": 1, "1": 26, "2": 40, "3": 63, "4": 95, "5": 127, "6": 160, "7": 190, "8": 218, "9": 232, "10": 261, "11": 290, "12": 315, "13": 346, "14": 370, "15": 400, "16": 431, "17": 454, "18": 472, "19": 492, "20": 516, "21": 543, "22": 564, "23": 590, "24": 610, "25": 625, "26": 643, "27": 658, "28": 685, "29": 710}
---

**Dave Jones:** Hi. What time is it? It's myth-busting time. Yes, cordless antistatic wristbands. None of this rubbish. What do you want one of these annoying uh antistatic wristband cords for? Screw that. You can buy these on eBay for a buck. They're cordless. They're supposed to work.

**Dave Jones:** Can you smell what I smell? Yeah, [ __ ] Thank you to the anonymous mailbag person who spent a whole dollar and sent this into the mailbag cuz you can really buy these on eBay for a dollar delivered from China.

**Dave Jones:** And rather than just go, "Ah, they're obviously [ __ ] There's no way in hell these things can work without dissipating the charge down to ground just like your regular cord-based systems here plugged into your ESD uh point down here." They're obviously [ __ ] right? Anyone with any engineering knowledge knows this, but hey, let's do it the scientific way.

**Dave Jones:** Let's put it to the test, get some quantitative measurements here, and see whether or not these things are [ __ ] Behold the cordless antistatic wrist strap. Looks just like a real wrist strap like these uh two here, but it hasn't got the proper uh stud either the small one or the larger stud here to come along and press your uh cord into like this. Oh, no, sirree, Bob. It's got some wireless magic voodoo inside here.

**Dave Jones:** That dissipates all the static charge into the ether. So, unlike your regular antistatic wrist straps, which have no internal resistance, they just connect directly through to the stud on the uh top there, your 1 meg safety discharge resistor is done inside the lead here and also an extra one uh uh inside your uh the point that you're actually mounted to. But, this thing actually has it built in. Well, because you can't just have nothing built in, can you?

**Dave Jones:** There it is. It's got a 1 meg resistor built inside here plus all the voodoo magic. Now, I'll do a teardown at the end of this, but inside here you can see that looks like the leg of the resistor in there. So, that just makes contact and this just folds over like that. So, we'll see what's inside here later. But, yeah, this is just designed to be worn on the wrist like that. That's it. And it's supposed to be as effective as a regular antistatic wrist strap. And to get some

**Dave Jones:** quantitative measurements here, I've got the exact tool for the job. This is my Alpha Labs surface DC voltmeter. It's designed to measure surface charge, ESD charges on mats and things like that or other objects without actually touching it. So, we can actually use this stainless steel SMD stencil here. It's just a convenient conductive surface and we can measure the charge We can put a charge on this mat. We can watch it discharge and we can actually get a real quantitative value in kilovolts.

**Dave Jones:** This thing goes up to 20 kilovolts, I think it is or more and we can actually get a direct read out in voltage of any sort of charge that we either build up or we discharge from this supposed wrist strap. And just to show you my setup here, I've got the ground of the surface DC voltmeter going down to my ESD mat here. I'm just using that as a reference surface down here. I've got my Keithley 240 high voltage power supply. It can go up to 1200

**Dave Jones:** volts. I've also got the negative of that reference down to the mat here. So, by connecting this metal surface here to the output of the power supply, we can use this to actually calibrate our system and show that it's working. I'm just doing that for For of fun. We could just trust this, but hey, why trust it?

**Dave Jones:** Let's actually try and do a little bit of calibration first before we do it. But then we can use this lead to actually discharge. I can charge myself up, touch it, charge the sheet, and we can once again use this to just discharge to my earth mains earth reference ESD strap down ESD bonding point down here. Now, sorry, it's not particularly easy to get both of these in shot cuz this has to be exactly level with the surface down here, exactly 1 in above. That's where

**Dave Jones:** it's actually calibrated. It's got a little disc on the bottom. It's calibrated for that distance. Anyway, what we can do is we can take this, we can plug it into our output here, and I can reset this, so we're at 0 V there, and I can actually turn this on up to 100 V. Bingo. Look, 101 V, and we can go all the way up to 1,000 V. It's a little bit out. You know, if I actually move this up and down just the tiniest amount, it'll

**Dave Jones:** change, but you can see that that is perfect. And we can actually Look, we can go 500, and then we can go negative as well, and it shows negative charge, too. No problems whatsoever. Systems all calibrated, ready to go. All right, let's give this a go. Now, this isn't going to be the world's greatest test today because I don't have synthetic underwear or clothing on or anything like that. Do have a jumper on, but, you know, like we're not going to be able to generate tens of kilovolts, but it

**Dave Jones:** doesn't matter. If we can generate charge, static charge, build up a charge on that plate, we can check to see whether or not this cordless wrist strap dissipates any faster than your regular corded wrist strap. So, what I've got here is one of my real corded wrist straps, but I'm not going to connect it through to my earth bonding point. This is to actually connect via this alligator clip lead here through to the charge plate. So, that charge plate will be at the same value as me cuz it's not

**Dave Jones:** dissipating anywhere. It's just connected via this direct connection here. So, if I Look, you can see I got a second camera here set up on this surface DC voltmeter. You can see I can build up a charge there, and it slowly dissipates because of natural dissipation and shoes and and natural dissipation of the system. That's no problems at all. So, I can Let's go. I can like give it a little charge, okay?

**Dave Jones:** So, I charged up the plate, and I can actually zero that out by boom, connecting uh the plate and hence my body through to directly onto the earth bonding point down there. And as you see, it went down to zero. Now, first we'll try my real antistatic wrist strap. Here we go. I've got it not connected to anything. So, once again, I can build up a charge on that plate, okay? And it stays there, and it just naturally dissipates a little bit. But here we go. I'll plug it in, and bam, it

**Dave Jones:** goes straight down to zero because it's it's a 1 meg resistor. It dissipates the charge really quickly from my body. No problems whatsoever. Now, let's do with the exact same thing again with our woo strap here, patent pending, okay? And I'll turn it around like that, so it's on the bare part of my skin like that, so people can't claim you got hairy skin and all that, you know, sort of stuff. And right, so here we go. We're going to do exactly the same thing we did before. And let's see.

**Dave Jones:** Mhm. It's just doing its natural dissipation. That's as part of the system. This thing is not accelerating that discharge at all. Now, I could, you know, get the stopwatch out and time it and everything, and I Who cares? Look, it's not doing anything. The charge remains on my body.

**Dave Jones:** It's remaining on that plate. And it doesn't matter whether it's, you know, 1,000 V, 500 V, or this or whether it's 10 or 20 kV, this thing does nothing. What? And let's do a side-by-side comparison test. I've got both the Woo strap and the real strap on my arm. Here we go.

**Dave Jones:** Let's Oh, sorry. I didn't put that uh back on properly. Here we go. Charge up our plate. No problems at all. It's pretty slow to dissipate, isn't it? There we go. But of course, we can go like that and wham. As soon as I plug in the real strap, it dissipates.

**Dave Jones:** I just realized you may not have been able to see much of what I was doing there with that uh real strap. There we go. I just had that uh hooked onto there, hooked onto the plate. That's it. So, that my body was definitely connected through to the plate and it wasn't dissipating anywhere else. All right. I know some people will complain or try and generate a bit more higher voltage, but I've been experimenting here. Haven't had much luck at all. I've actually got my uh

**Dave Jones:** synthetic uh walking pants on, synthetic polyester shirt, and I've tried all sorts of various shoes and my jumper taken off and on. And this is about the best I can get. Here we go. I can start it from zero there. And here we go. I've got no wrist strap at all. And, you know, I can get like 2 and 1/2 thousand or something like that and slowly dissipates. I've actually changed the mount on here. I had the Art of Electronics book before. I've actually just propped it up with some batteries.

**Dave Jones:** So, it it discharges slower now, but you know, that's pretty much the best I can get. Sorry. So, we'll just try that again. Here we go. Got the good antistatic wrist strap. And bam. There we go. Discharges. And I've got the Woo strap on. Here we go. Once again, we're down to zero there.

**Dave Jones:** Charge her up. Ta-da! And it's not doing anything. It's just the regular discharge rate. Ah, hopeless. So, this thing is an absolute crock. So, let's take a look what's inside this. My bet is it's just a 1 meg resistor flapping around in the breeze. Here we go. Let's have a look.

**Dave Jones:** Tada! Look at that. Look at that. There's our 1 meg resistor in there. And that's it. Wow! Unbelievable. It's actually broken off there. It's Yeah, that just fell off. So, I had to Did I have a faulty one? I doubt it.

**Dave Jones:** And that's it. All I've got is that nut there. There we go. I've got a captive nut to hold the plate in, and that's it. It's just a screw attached to a resistor flapping in the breeze. That's it.

**Dave Jones:** That's it. That's the whole thing. It's an absolute con. No real surprise. So, there you have it. There is the cordless antistatic wrist strap. It is a complete con. It is just a 1 meg resistor flapping around in the breeze, and as you saw, it didn't work.

**Dave Jones:** Of course it didn't work. Anyone with any clue whatsoever about how static charge and discharge works knows knew that this thing wasn't going to work, but Oh, you know, people go, "Oh, it's only a dollar. I'll just get it on eBay." It's not even worth the one freaking dollar.

**Dave Jones:** It is useless. So, there you have it. That is totally busted. You want to discuss it? EEVblog forum at link is down below. Catch you next time. Oh, by the way, yes, the rumor is true. I do actually work in the lab in bare feet pretty much all of the time. And well, here's one reason why. Not that I think it's the most comfortable thing, but hey, this is a nice side benefit. Check it out. Here we go.

**Dave Jones:** This is with This is with shoes on. There we go. Take the shoes off. Tada! Let's ground it in and look at that. Not even generating close. Not even getting to 100 V. Beauty. So, nothing wrong with bare feet in the lab unless you like step on an upturned IC and then ouch.

**Dave Jones:** Catch you next time.
