---
video_id: DVXPGj0Pjyc
title: EEVblog #933 - Keysight U1272A EMC Issue
url: https://www.youtube.com/watch?v=DVXPGj0Pjyc
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 36, "3": 53, "4": 72, "5": 86, "6": 102, "7": 120, "8": 140, "9": 156, "10": 176, "11": 197, "12": 215, "13": 231, "14": 248, "15": 263, "16": 292, "17": 308, "18": 323, "19": 343, "20": 361, "21": 380, "22": 396, "23": 408, "24": 424, "25": 439, "26": 454, "27": 470, "28": 487, "29": 503, "30": 514, "31": 530, "32": 554, "33": 571, "34": 592, "35": 609, "36": 625, "37": 641, "38": 665, "39": 677, "40": 693, "41": 711, "42": 727, "43": 742, "44": 757, "45": 776, "46": 788, "47": 805, "48": 823, "49": 840}
---

**Dave Jones:** Hi, just a quick blab video with a potential issue with the Keysight U1272A multimeter here. One of my viewers, Bernard Ruff, was measuring using this meter to measure the current on his power supply like a project or whatever and

**Dave Jones:** getting some strange readings on the display and it turns out that it was near to the leads that were used to measure the current we need to an RFID reader and you know, he played around finally narrowed it down using a function

**Dave Jones:** generator to a noise pickup and I'll show you this right now. It's some sort of you know, conducted common mode thing. I anyway, let's have a go see if we can recreate it. So what I've got is the

**Dave Jones:** U1272A connected to my function gen here and I've got a 5 megahertz of frequency does matter as we'll see in a minute 10 volts peak to peak square wave okay, touchy-feely and I'm just going to take just the positive

**Dave Jones:** uh terminal here. Here we go and I'm going to plug this in on the amps range. Okay, so well, it's milliamps it'll switch down so when we plug it into here and look what we get. The ground's just flapping around in the

**Dave Jones:** breeze. We're getting -5 amps a huge reading like that and you take it out and it goes away. You plug in the negative one. Let's try that and it's not as high but you still get a reading on there. Now

**Dave Jones:** there's obviously some sort of conducted noise which is referenced to because this output here is mains earth referenced. So that you know, is there is a the system here there's capacitance everywhere going on. Anyway, we won't go into RFI and EMI and

**Dave Jones:** all that sort of stuff, but there is some sort of conducted issue there with that meter. And if you plug it into the ground terminal, not nearly as much, okay? So, there is something relative to the common measurement of the U1272A. So, there's

**Dave Jones:** obviously some sort of conducted common mode issue going on with this meter. So, I thought I'd actually just first of all recreate it with exactly the same settings, try out a whole bunch of different meters that we've got here, and give it a whirl. So,

**Dave Jones:** the first one is the Keysight U1273 AX. This is their waterproof low-temperature version. The screen is flickering cuz it has that OLED display. Let's plug it in and see what we get. Yep. You betcha. Look at that. 12.1

**Dave Jones:** amps. Exactly the same thing going on there with that one. Not surprising cuz it's basically an almost practically identical meter to the U1272A, except it has the OLED display on the thing. Now, let's try the Keysight U1282A. You've seen this before. This is the

**Dave Jones:** rugged meter, and all right, not nearly as high, but it's still there, okay? So, we're getting -0.1 amps. So, it still seems to be an issue with that one, but not nearly as bad as what we're seeing here. Let's try the

**Dave Jones:** Gossen Metrawatt. It just switched off. Thank you. Gossen Metrawatt Energy. Here we go. No worries whatsoever. We're down on the microamp range because this has a single jack to do everything. Not Not a Not an issue. Not an issue whatsoever.

**Dave Jones:** Fluke 87. uh the venerable old uh Fluke 87. Sorry, I'm not getting the best angles and stuff here. Anyway, it's reading bugger all. Let's go old school with a Fluke 27. Here we go. Nope. Bugger all on that one, too.

**Dave Jones:** And it doesn't matter if I do the negative one, of course. And the Brymen uh BM869, a lot of fans of this meter out there. And nope. And once again, it automatically detected that there's a thing plugged in, the amps jack, and

**Dave Jones:** everything's hunky-dory. So, let's go over to the Fluke 17B, shall we? Let's give that a whirl. No, absolutely nothing. The EEVblog BM235, nope, nothing. And the Uni-T cheap Uni-T UT61E, absolutely nothing. And just for kicks, the Keysight 34461A.

**Dave Jones:** Yep, that one actually shows something there. So, there you go. Minus 84, but it's microamps, right? So, if we manually switch that to the amps range, it'd be naff all, really. But no, technically, um that one has an issue as well. And you plug in

**Dave Jones:** the negative one, so obviously reference to to mains earth in some way, shape, or form. They're plugged into the 10-amp jack. Yep, similar sort of thing. But, you know, it's not a huge amount. So, as you can see,

**Dave Jones:** um it basically only seems to be the Keysight these particular ones, these ones in particular, the U 1270 series meters. There's something going on there. Whether or not it's a huge deal, uh you could say maybe not. But hey,

**Dave Jones:** uh Bernhardt did actually get this problem in a real-world scenario, measuring uh current you know, project current from from a power supply. So, yeah, there's some sort of conducted uh mode vulnerability there, but I'll show you something interesting. Let's

**Dave Jones:** now try see what happens instead of just plugging it in, okay? Bingo. Oh, there it is. 4 amps or whatever. If we just hold it near it, bang, we can get that to happen as well. So, it's not just conducted,

**Dave Jones:** it's radiated pick up as well. Some so so, what have they not designed the RFI im- immunity good enough inside this thing? Um seems to be that way. It's certainly picking up. A lot of other meters out there don't have it. So, let's just

**Dave Jones:** quickly experiment with some uh settings here. We're on a square wave, of course. Let's actually change it to a sine wave, and I think the harmonics of the square wave are going to be an issue. We're at 10 volts peak to peak. So, 5 MHz,

**Dave Jones:** there's tons of harmonics right up into the RF region. So, let's put it on sine wave, and hey, it's still there though, okay? So, obviously, um higher harmonics are causing more of an issue here. So, I would presume, so

**Dave Jones:** let's go back to um square wave. So, let's go down in frequency, and we should actually I I think this is going to drop as we go down in frequency. At a certain point, yep, it's going down, down. Well, I have to go across

**Dave Jones:** there. Okay, 9 900k, 400k, it's going down. There we go. It's starting to become a Whoop. Did it go back up there a little bit? Maybe. It's going to be all sorts of things, but 9 kHz, you know, that's not particularly

**Dave Jones:** high. And once again, if we switch to sign, I reckon, yep, that would go away. Yep. But so, obviously, the uh square waves are calling causing much higher harmonic theft. So, that can really jump up. We can actually get it

**Dave Jones:** even higher than that. Here we go. Yeah, there there seems to be some points, but look, we can go out to like 32 amps. Wow, -32 amps. Thank you very much. And if we actually that's plugged into the positive jack,

**Dave Jones:** if I plug that in into the milliamp jack, there we go. If I plug that into the common terminal, there you go. Same thing. But yeah, you plug that into the amps jack, and wow. Look at that. Thank you very much. And

**Dave Jones:** if we just dangle that over there, be better if we got a coil or something we could really couple it in, but once again, we're you know, we can we're able to couple in well, it what it thinks is a couple of

**Dave Jones:** milliamps. But yeah. And of course, we're going to see this change with amplitude as well. So, if we go over to our amplitude, and then we drop our amplitude, there you go. 1 volt peak to peak. Okay, it's it's

**Dave Jones:** becoming much less of an issue. 500 millivolts, you know, but still, yeah. That is interesting. That has definitely confirmed Bernard's results that this thing is susceptible, certainly, to direct conducted RFI onto the positive amps lead like this, but Bernard

**Dave Jones:** originally saw it when it wasn't being conducted in, it was being radiated in from a nearby RFI reader. Watch this. I'm measuring 1 amp coming from my Rigol power supply here, floating power supply. No worries whatsoever. And if I

**Dave Jones:** go to plug this in, look, it's already changing. Just this coupling between from this coax into that meter. Enough to you know, throw it way out of spec. Wow. So, I haven't even connected the damn thing up yet. So, now if I hook it on,

**Dave Jones:** that's going to completely screw that up. Yep, and the Rigol power supply is still measuring 1 amp there. But, yeah, this thing is completely knackered. Look, and even 1 volt peak to peak here, more than enough to throw that completely out. And

**Dave Jones:** I try that on other meters, and it's simply not an issue. It's only on the Keysight ones. Strange. And as far as the bench meter, that was a little bit susceptible. Nah, nothing. Because as we saw before, it was like microamps. And check it out,

**Dave Jones:** if we fill up this meter, okay, let's put it down here, couple it into this lead. Yep, causes it. Causes an issue down there, but let's uh let's fill her up, and look, as we go higher, the current is decreasing.

**Dave Jones:** Wow. Wow. Look at that, .2. This is shocking. Yeah, 10 volts peak to peak, it's pretty severe at 10 megahertz, you know. That's but jeez, don't get this on any other meter. See, absolutely nothing. And you'll notice it can change with

**Dave Jones:** just coupling of my hand as well. Watch this. Spooky action at a distance. Look at that.

**Dave Jones:** Um it's nothing to do with my ESD um mat, either. Look, if I um actually, if I ground myself, I've disconnected my mat from uh mains earth, okay? Look. So, I may I and I've connected this through to uh the mains earth on my

**Dave Jones:** Rigol here, so it's actually connected through and woo. So, just still mains earth coupling and if I connect myself to the mat as well, so I've got my finger actually under the conductive bottom of that mat, properties change a little bit. Maybe if

**Dave Jones:** here we go, I'll lift my fingers. Nah. Now, nah, it's all the same. Anyway, spooky. So, it's not picking something up, uh you know, from my ESD mat or anything like that. I've had issues like that before actually with like a floating ESD

**Dave Jones:** uh mat when it's not grounded and stuff like that, but I love it. The thing that actually concerns me the most here is uh not really the conducted mode uh stuff when we uh plug that in. Okay, it's an issue they need to look into,

**Dave Jones:** but the fact that you're just using this meter on the bench, you've got it sitting next to your uh you know, your arb gen like this and you switch it on and look, I it's the cable. It's just flapping around in

**Dave Jones:** the breeze and of course, if you take it anywhere near it, you're goneski. I mean, that's just That is nuts. Absolutely nuts. So, there you have it. The U1270 series has an RFI vulnerability. You remember the uh good old Fluke 87 GSM phone thing

**Dave Jones:** where you used to put a GSM phone next to it and would cause it to lock up and reset. It's not as bad as that, but well, actually I'd rather have my meter lock up and reset than um it just give

**Dave Jones:** you dodgy readings like that. So, there's some RFI vulnerability there, both uh conducted and coupled. So, um I haven't read the uh spec sheet offhand for this thing, but they they most likely have an electromagnetic conformity spec for this thing, but

**Dave Jones:** yeah, um Keysight, Please explain. Catch you next time. Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, why do I have the lab coat on today?

**Dave Jones:** Well, it's myth-busting time. Got his mobile phone and he put it next to his Fluke 87V and it killed it. It bricked it. So, yeah, I thought I'd sacrifice my 87V and try it out cuz this is really

**Dave Jones:** interesting. Let's see what happens.
