---
video_id: uBYMePUFinQ
title: EEVblog #311 - Jim Williams Pulser Followup
url: https://www.youtube.com/watch?v=uBYMePUFinQ
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 33, "3": 53, "4": 71, "5": 91, "6": 104, "7": 123, "8": 138, "9": 156, "10": 175, "11": 196, "12": 209, "13": 224, "14": 247, "15": 260, "16": 280, "17": 296, "18": 309, "19": 327, "20": 343, "21": 359, "22": 375, "23": 391, "24": 407, "25": 424, "26": 441, "27": 454, "28": 468, "29": 485, "30": 496, "31": 513, "32": 529, "33": 544, "34": 561, "35": 582, "36": 599, "37": 614, "38": 638, "39": 659, "40": 675, "41": 690, "42": 705, "43": 723, "44": 749, "45": 766, "46": 782, "47": 802, "48": 819, "49": 835, "50": 852, "51": 867, "52": 885, "53": 904, "54": 920, "55": 933, "56": 947, "57": 959, "58": 974, "59": 994, "60": 1007, "61": 1025, "62": 1049, "63": 1071, "64": 1086, "65": 1103, "66": 1119, "67": 1135, "68": 1152, "69": 1163, "70": 1182, "71": 1200, "72": 1217, "73": 1235, "74": 1253, "75": 1269, "76": 1287, "77": 1303, "78": 1319, "79": 1337, "80": 1358, "81": 1376, "82": 1394, "83": 1408}
---

**Dave Jones:** Hi, I've got a follow-up video on the Jim Williams pulse generator. And if you remember last time we tried to measure the performance of Sylvan's little board here based on the Jim Williams circuit that he sent me for the mailbag again.

**Dave Jones:** Well, the $10,000 1 GHz Agilent 3000X series just wasn't quite up to the task of measuring the rise time of this thing. So, I thought we need to maybe step it up by say an order of magnitude. So, unfortunately, out it goes.

**Dave Jones:** Oh, well. Turns out that I had something lying around the lab here gathering dust and we can step it up by an order of magnitude. Here it is. Agilent Infiniium 13 GHz 40 gig sample per second DSA 91304A

**Dave Jones:** oscilloscope. Worth approximately uh about 140,000 Australian dollars. No worries. I think we might be able to finally measure the rise time of this thing. Let's give it a try.

**Dave Jones:** Now, if we take a look at the horizontal down here, it goes all the way down to that's we're into picosecond region now. 150 20 10 5 picoseconds per division. That's pico, folks, not nano. But that's what you get with a 13 GHz 40 gig sample

**Dave Jones:** per second scope. So, you might think oh like we expect like 300 odd picosecond rise time. So, you might think this thing would balls it in. Just plug it in and measure it. Turns out it ain't that easy.

**Dave Jones:** And by virtue of their incredibly high bandwidth, these scopes are all 50 ohm input impedance, which is great, which is what we need. But tada, the trap, check it out. Plus minus 5 volts maximum cat one. You used to, you know, 300 volts maximum

**Dave Jones:** like on a regular scope, but these things incredibly easy to blow the ass out of the front end. And as much as I'd like to smell what a $140,000 worth of magic smoke smells like, uh I don't think we're going to do it

**Dave Jones:** today. So, what we need is an attenuator because this little pulse gen outputs you know, too high a voltage to measure directly on this oscilloscope. So, what we need here is a wide bandwidth attenuator. And thanks to Charles at

**Dave Jones:** Trio Smart Cal, I was able to get one. It's not something I ordinarily I have in the lab. And it's a Mecca 650-21F4, and that's 20 dB, and it's it's got a 4 GHz rated bandwidth. go higher than that,

**Dave Jones:** but that's all it's actually rated to. So, really, even though we've got this $140,000 13 GHz oscilloscope, we're limited by our attenuator here. Crazy. But anyway, this should be more than good enough to measure the performance of the Jim Williams pulse generator. And

**Dave Jones:** of course, we had to fit various adapters cuz it's got an N connector on here. So, we had to fit N to BNC, and then a BNC uh six adapter there. And you know, crazy, but that's the shortest

**Dave Jones:** path I can possibly get directly from the BNC output of the pulse generator. So, let's give it a go. So, there's our pulse generator hooked up through our attenuator, and let's check out the signal. Ta-da! And if we have a look at the rise time

**Dave Jones:** here, we're talking about 254 picoseconds average, and a fall time of 420 picoseconds average. So, that's uh you know, that that will be somehow limited uh by our by our attenuator, of course, um because we're not essentially limited by

**Dave Jones:** the uh bandwidth of the oscilloscope here, but there you go. That's a really nice clean pulse. Maybe if we turn some average on on, uh we'll get a cleaner waveform. And there we go. With 16 averages on there, we're getting in

**Dave Jones:** about 253 picoseconds rise time and 420 picoseconds fall time on average. But as quite a few people uh pointed out in various uh comments that um because this uh waveform doesn't have time to settle up here, it is just a pulse. It falls as

**Dave Jones:** quickly as it rises, it's uh really uh no good for measuring the bandwidth. You really need it to rise and then flatten off and then fall for um those uh formulas we used last time to be valid, the uh you know, 0.3 or 0.4 on the uh

**Dave Jones:** bandwidth. So, on the rise time. So, um really uh we're going to have to modify the circuit and see if we can flatten that out a bit. And also, as a few people pointed out, one way to do this is to solder on a

**Dave Jones:** length of coax across uh the main uh two picofarad capacitor, I think it was. Actually, well, I replaced it with a bit of coax. So, I just wired that uh in parallel. I've got some RG-174 uh Belden, uh 35 cm worth. Of course,

**Dave Jones:** the uh longer it uh goes, the more you can um stretch that pulse out, but anyway, let's have a look what 35 cm soldered across the existing uh couple of picofarad capacitor in there can do. Let's give it a try.

**Dave Jones:** And bingo, that's actually worked a treat. Check that out. It's uh extended the pulse by What are we? 2 ns per division. So, it's extended it to 4 ns that pulse, and you can see the ringing up the top there, and it eventually

**Dave Jones:** flattens out and then drops back down. So, let's go in and measure the rise time of this baby. We're still got our averaging on in there, and what are we getting What do we know? About 288 ps rise time. Beautiful. And of course,

**Dave Jones:** we can zoom all the way in and go down to 5 ps per division just because we can. But, that's beautiful. So, still got the averaging on there, and that is a little That's a nice useful addition to extend the length of that

**Dave Jones:** pulse. So, let's get the official figure here. We've got to have the full pulse on the screen there so it knows the level where at. It measures 10 to 90% and 296 odd ps. So, let's call it pretty close

**Dave Jones:** to an even 300 ps. Now, if you're wondering what happens when I remove the capacitor and just have the coax there, look at this. We don't get a nice There's no more ringing at the top there, but we don't no longer get a nice

**Dave Jones:** stepped waveform. We sort of get this and then this little kink in here and then slowly rising up. So, it looks to be better to at least have the the old the the original cap in there, the original Jim Williams circuit. And of

**Dave Jones:** course, this is the Jim Williams recommended add-on. I can't remember offhand if he recommended leaving the original cap in there, whether or not he said to replace the capacitor or to with coax or to just add the coax in

**Dave Jones:** parallel. But, yeah, that is not a nice, you know, rise time input at all. It's, um, you know, it's pretty darn horrible. And you know, the rise time of course is going to be way out of whack, you know,

**Dave Jones:** 800 picoseconds or 1.4 nanoseconds four times still cuz that has all that down there. It's, you know, it's yeah, it's no good as a pulse generator for measuring bandwidth. And we'll step it up just a little bit by putting on

**Dave Jones:** what will the reel says 100 m of coax, but I don't think there's 100 m still left on there. So, let's call it, you know, maybe 75 m or something like that. It's Philips branded. I I Googled that

**Dave Jones:** part number, nothing comes up. Um, so, you know, it's once again, it's thin coax like the RG 174, but anyway, let's give this a try and see what we get. And here we go. This is with no original capacitor in there. So, it's

**Dave Jones:** just like the 75 m of coax or whatever. We're talking 184 picoseconds according to this, but that increases if we get the whole pulse on there. The whole pulse, we're talking 50 nanoseconds per division, 150 like we're talking 170

**Dave Jones:** nanosecond pulse or thereabouts now. And but we get a a nice clean edge there, but then it sort of we get a little bit of ringing and then it starts still starts to rise up there. So, I really

**Dave Jones:** don't like that. And then we've almost got a linear fall back at the top of the waveform there. So, yeah, I think I might put the original cap back and see what we get. No, we get pretty much exactly the same with that

**Dave Jones:** linear ramp going down at the pulse. It's the same pulse length of course. And but we get this massive overshoot here at the first edge, the rising edge. But anyway, if we let the scope call that in terms of rise

**Dave Jones:** time, we're talking 180 picoseconds there. So, yeah, I don't know. You know, you could you could take it at any point you deem you know, to be worthy of being the 90% point. And as it turns out, I just killed my two

**Dave Jones:** picofarad capacitor and the end cap just uh fell off. Um so, I've put in a five picofarad the nearest one I had to hand quickly and it's slightly increased amplitude, I believe, but there we go. We're back to our original

**Dave Jones:** cap with no um uh coax on there, just the five picofarad capacitor and we're talking 295 odd picoseconds rise time and 598 or say even 600 picoseconds fall time. And I resoldered my coax back on the 35 cm of coax cuz I really like

**Dave Jones:** that. That seems uh like an ideal thing to use. A bit of overshoot there, but we can get the rise time nicely and we are talking 270 picoseconds rise time and 1 nanosecond fall time. So, I'm going to use that as

**Dave Jones:** the reference. I'm going to leave the circuit alone now. I'm not going to play with it anymore. Um and now we'll do some bandwidth measurements on our other scopes based on that reference rise time of 270 picoseconds. So, let's go back to our

**Dave Jones:** Agilent 3000 series the 3054 X-series oscilloscope. 500 MHz. I'm using the exact same attenuator, exactly the same as we just did. Wanted to keep it all the same. Didn't want to put it directly in there. We'll do that uh I

**Dave Jones:** just wanted to see what we get, keeping the conditions the same. Let's check out the rise time. And as you can see, the wave shape is, I believe, almost identical to what we were getting on our $140,000 uh dollar

**Dave Jones:** 13 GHz Agilent. But, of course, our rise time is greater, and it's basically uh jumping between 610 and 630. It's mostly been about 630 picoseconds there. So, I'm going to take that as the value. And if we punch that into our calculator,

**Dave Jones:** 0.4 divided by uh 630 picoseconds, what do we get? We get Ta-da! 635 MHz. So, we were definitely overestimating uh before because we didn't um because we only had the pulse which didn't settle out. But now we've got the pulse which settles out there,

**Dave Jones:** the scope is able to take the average of the top, get the 90, and get the true 90%, and give us the rise time. So, 635 MHz, but that doesn't take into account the uh absolute rise time of our unit,

**Dave Jones:** which we uh saw was 270 picoseconds. So, we haven't taken that into the calculation yet, but even so, that value, 635, if you go back and look at my uh Marconi uh 2023 video, which I'll uh have to link in

**Dave Jones:** here, um we measured the bandwidth of this thing, the minus 3 dB bandwidth of this at, guess what? It was actually 637 MHz. So, you tell me, is that just a uh coincidence, or is this actually good enough to, you

**Dave Jones:** know, measure to a reasonable degree of accuracy the minus 3 dB bandwidth using that formula, that maximally flat formula in quote marks of 0.4 on the rise time. It gave it It gave us within a couple of megahertz the exact

**Dave Jones:** value cuz there's error in this, of course, and there was a slight error in the measurement of our Marconi 2023 minus 3dB bandwidth as well, but you know, it it's pretty darn close. But we haven't taken into account that 270

**Dave Jones:** picoseconds. So, I'm not sure if we have to, but hey, it is basically spot on. And if we take a look at it here, this is directly connected straight into the scope. There it is. So, it's really it's really bang on, as good as we can

**Dave Jones:** get it. No coax in No No coaxial connection, just direct BNC connection in there. And the amplitude's a little bit over. It's off the screen. It'll give us 590 picoseconds there when it's off, but really you need to get the

**Dave Jones:** whole thing on the screen for that to be an accurate measurement. And it is jumping between that 630 and that 610 picoseconds like we had before. So, if anything, it's slightly lower, and hence overestimating our um uh bandwidth again like we did uh

**Dave Jones:** last time. So, um in this case, we might have to take into account the uh 270 picoseconds absolute rise time, but still I think this probably demonstrates that you can um probably just measure the bandwidth of a 500 megahertz scope using

**Dave Jones:** this basic Jim Williams pulse generator with the coax mod on there as well. I've got 35 cm of coax with the original cap in there. And that that works. That works a treat. And a few people have asked to see the

**Dave Jones:** trusty old Rigol to see what it gives. So, there's the fabulous boot screen. All Rigols now come shipped with this boot screen. And we'll give it a go. Um I'm using a 50 ohm uh termina- 50 ohm in in-line

**Dave Jones:** terminator because of course the Rigol doesn't have uh 50 ohm termination on it. So, let's have a look. I've got the 75 m of coax set up here. And of course we've got our downward uh slope on the waveform here. So, once

**Dave Jones:** again, where do you take the 90% uh point from? I'm not sure where the Rigol's taking it. It's telling us the rise time is less than 2.4 nanoseconds, but really, you know, it's not that accurate less than four. Depends where

**Dave Jones:** you want to take it. If we want to um say uh zoom into the position here and take that as the value. Um then we're talking, you know, 2 nanoseconds. So, what I'm going to do now is measure the

**Dave Jones:** uh real bandwidth, the actual minus 3dB bandwidth of this uh scope using my Marconi uh 2023 RF signal generator. So, what I've done here, I'm feeding in a 1 MHz sine wave at 1 V peak-to-peak. So, we want to uh increase

**Dave Jones:** the input frequency um until it drops to 0.707. And that'll give us our real bandwidth. So, let's give it a go, shall we? Okay, let's wind the wick up. And you can see that lovely effect there is due

**Dave Jones:** to the averaging. I got 16 averages turned on. We're at 50 MHz now, so let's go up, increase the time base. So, we want 0. 70 or 770 mV. So, let's keep going.

**Dave Jones:** We're at 123 MHz now. It's 0.707. Once again, this is 50 ohm terminated of course, and it's jumping around. It's hard, but let's call that um at is that's let's call that as the minus 3 dB point and we're talking 136

**Dave Jones:** MHz. So, that is our the real bandwidth of our 100 MHz modified, of course, 100 MHz Rigol scope. Beautiful. That's our reference point. So, clearly the two nanoseconds that we're uh reading here for the rise time, that's 200 MHz. That's way

**Dave Jones:** overestimating. So, that's with our 75 m of coax. So, let's Well, you know, if we get 4 nanoseconds, once again, it's not very accurate down there. So, you know, there's uh it jumps up to 2.4 maybe. You know, it's not that

**Dave Jones:** great. And to get our figure of 136 MHz, we need a smidgen under uh to measure a smidgen under 3 nanoseconds rise time. So, it's clearly not going to give us that. Doesn't have the resolution to do that, I'm afraid. So, let's That's

**Dave Jones:** with the 75 m coax. Let's give the 35 cm coax a try. And here it is, 35 cm of coax. And if it looks familiar, it's because it's like the standard pulse again, like the without the coax that we

**Dave Jones:** saw. And the reason for this is because this bandwidth of this scope is lower. So, it just you know, it hasn't got time for the thing to settle out. So, we really need to add maybe just a little more coax to it, so we can do

**Dave Jones:** that. We're getting 2.48 nanoseconds. So, you know, it's not the value of three that we require. We can't really turn that up a tad cuz it can't measure the rise time there, but yeah, it's uh 2.5, it's 2.6.

**Dave Jones:** Um it's not going to cut the mustard. Need more coax. And I've doubled that to 70 cm of coax. And as you can see, it does flatten out before it drops back down now. But, uh, we're still getting,

**Dave Jones:** you know, the resolution's not bad on the rise time, uh, measurement here. It's, um, but we're still only getting just over 2 ns, which is up near 200 MHz. So, clearly overestimating once again. And how about 105 cm of coax? I keep

**Dave Jones:** adding on these 30 35 cm, uh, segments. And, uh, nope, no good. At least with the automated, uh, rise time measurement, just over 2 ns still. Now, what I'm going to do is manually set up my cursor cursor measurements here to the 10 and

**Dave Jones:** 90% mark. I've used a my, uh, variable vertical, uh, attenuator to set it for five divisions peak to peak to that to the basically the top of the waveform there, ignoring the overshoot there. And then I've set my cursors to the 10% and

**Dave Jones:** 90% mark. And if we zoom in here, we can get, let's have a look. Let's smooth that to the where it just crosses that vertical graticule division there. And go across where 2 ns per division. And where it crosses that one, it looks like

**Dave Jones:** it's only one division. So, it's still 2 ns. Pretty much exactly what it was measuring automatically. So, it looks like we're entirely unsuccessful here of using this, uh, Jim Williams pulse generator, even with the coax, uh, mods to extend the pulse to,

**Dave Jones:** uh, accurately measure the, uh, or at least give us an a reasonably accurate ballpark measurement of the minus 3 dB bandwidth. We're way overestimating here at like, you know, in the order of, uh, 200 MHz, um, instead of the 136

**Dave Jones:** which we measured is the true analog minus 3 dB bandwidth. And that's using the formula of 0.4. Of course, it may or may not actually apply to this scope because it may not have a maximally flat response. Who knows what's going on

**Dave Jones:** here? But yeah, you know, it relies on a whole host of factors. You've got to get the correct waveform type with no over as little overshoot as possible. You've got to extend the pulse as much as possible. And you've

**Dave Jones:** got to, you know, make sure it's a suitable pulse length for the bandwidth of the oscilloscope you're using. And then you've got to know what the correct factor is, what the that correct formula is based on your particular scope and what method

**Dave Jones:** it's implementing to do that. So, yeah, it's it's not looking that great. It seemed to work for the Agilent 3500 MHz scope, but can't get this thing to work on the Rigol really. I mean, even taking our Gaussian formula

**Dave Jones:** of 0.35 on the rise time, we're still overestimating by quite, you know, tens of megahertz at at minimum. Quite a significant error. So, anyway, more food for thought. We might do some more tests on this later. But anyway, I hope you enjoyed that. That's

**Dave Jones:** the uh Jim Williams pulse generator with coax modification on it. And it does certainly seems to extend the pulse. So, if you got one of these, definitely give that extra Jim Williams mod with the coax a try and see what you can get. So,

**Dave Jones:** even that may not be fantastic for measuring the bandwidth of a scope with those formulas unless you get the waveform absolutely perfect. It could still be used for, you know, measuring the rise time of systems and things like that. The effect on the

**Dave Jones:** the slew rate. Have it just having a fast rise time pulse can be quite useful for quite a few different applications. So, if you enjoyed the video, please give it a thumbs up and if you want to discuss

**Dave Jones:** it, jump on over to the EEVblog forum. Catch you next time.
