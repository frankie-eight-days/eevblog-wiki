---
video_id: uBYMePUFinQ
title: EEVblog #311 - Jim Williams Pulser Followup
url: https://www.youtube.com/watch?v=uBYMePUFinQ
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 27, "3": 41, "4": 66, "5": 85, "6": 96, "7": 111, "8": 128, "9": 149, "10": 162, "11": 183, "12": 200, "13": 214, "14": 234, "15": 249, "16": 265, "17": 276, "18": 296, "19": 316, "20": 340, "21": 361, "22": 371, "23": 392, "24": 403, "25": 416, "26": 429, "27": 443, "28": 454, "29": 475, "30": 489, "31": 507, "32": 522, "33": 541, "34": 555, "35": 574, "36": 593, "37": 612, "38": 630, "39": 657, "40": 672, "41": 687, "42": 694, "43": 711, "44": 729, "45": 753, "46": 788, "47": 814, "48": 830, "49": 846, "50": 858, "51": 869, "52": 885, "53": 908, "54": 922, "55": 938, "56": 949, "57": 957, "58": 970, "59": 982, "60": 997, "61": 1007, "62": 1025, "63": 1049, "64": 1068, "65": 1084, "66": 1098, "67": 1110, "68": 1124, "69": 1135, "70": 1152, "71": 1161, "72": 1175, "73": 1192, "74": 1212, "75": 1228, "76": 1243, "77": 1259, "78": 1272, "79": 1287, "80": 1299, "81": 1319, "82": 1344, "83": 1363, "84": 1372, "85": 1392, "86": 1411}
---

**Dave Jones:** Hi, I've got a follow-up video on the Jim Williams pulse generator. And if you remember last time we tried to measure the performance of Sylvan's little board here based on the Jim Williams circuit that he sent me for the mailbag again.

**Dave Jones:** Well, the $10,000 1 GHz Agilent 3000X series just wasn't quite up to the task of measuring the rise time of this thing. So, I thought we need to maybe step it up by say an order of magnitude.

**Dave Jones:** So, unfortunately, out it goes. Oh, well. Turns out that I had something lying around the lab here gathering dust and we can step it up by an order of magnitude.

**Dave Jones:** Here it is. Agilent Infiniium 13 GHz 40 gig sample per second DSA 91304A oscilloscope. Worth approximately uh about 140,000 Australian dollars. No worries. I think we might be able to finally measure the rise time of this thing.

**Dave Jones:** Let's give it a try. Now, if we take a look at the horizontal down here, it goes all the way down to that's we're into picosecond region now. 150 20 10 5 picoseconds per division.

**Dave Jones:** That's pico, folks, not nano. But that's what you get with a 13 GHz 40 gig sample per second scope. So, you might think oh like we expect like 300 odd picosecond rise time.

**Dave Jones:** So, you might think this thing would balls it in. Just plug it in and measure it. Turns out it ain't that easy. And by virtue of their incredibly high bandwidth, these scopes are all 50 ohm input impedance, which is great, which is what we need.

**Dave Jones:** But tada, the trap, check it out. Plus minus 5 volts maximum cat one. You used to, you know, 300 volts maximum like on a regular scope, but these things incredibly easy to blow the ass out of the front end.

**Dave Jones:** And as much as I'd like to smell what a $140,000 worth of magic smoke smells like, uh I don't think we're going to do it today. So, what we need is an attenuator because this little pulse gen outputs you know, too high a voltage to measure directly on this oscilloscope.

**Dave Jones:** So, what we need here is a wide bandwidth attenuator. And thanks to Charles at Trio Smart Cal, I was able to get one. It's not something I ordinarily I have in the lab.

**Dave Jones:** And it's a Mecca 650-21F4, and that's 20 dB, and it's it's got a 4 GHz rated bandwidth. go higher than that, but that's all it's actually rated to. So, really, even though we've got this $140,000 13 GHz oscilloscope, we're limited by our attenuator here.

**Dave Jones:** Crazy. But anyway, this should be more than good enough to measure the performance of the Jim Williams pulse generator. And of course, we had to fit various adapters cuz it's got an N connector on here.

**Dave Jones:** So, we had to fit N to BNC, and then a BNC uh six adapter there. And you know, crazy, but that's the shortest path I can possibly get directly from the BNC output of the pulse generator.

**Dave Jones:** So, let's give it a go. So, there's our pulse generator hooked up through our attenuator, and let's check out the signal. Ta-da! And if we have a look at the rise time here, we're talking about 254 picoseconds average, and a fall time of 420 picoseconds average.

**Dave Jones:** So, that's uh you know, that that will be somehow limited uh by our by our attenuator, of course, um because we're not essentially limited by the uh bandwidth of the oscilloscope here, but there you go.

**Dave Jones:** That's a really nice clean pulse. Maybe if we turn some average on on, uh we'll get a cleaner waveform. And there we go. With 16 averages on there, we're getting in about 253 picoseconds rise time and 420 picoseconds fall time on average.

**Dave Jones:** But as quite a few people uh pointed out in various uh comments that um because this uh waveform doesn't have time to settle up here, it is just a pulse.

**Dave Jones:** It falls as quickly as it rises, it's uh really uh no good for measuring the bandwidth. You really need it to rise and then flatten off and then fall for um those uh formulas we used last time to be valid, the uh you know, 0.3 or 0.4 on the uh bandwidth.

**Dave Jones:** So, on the rise time. So, um really uh we're going to have to modify the circuit and see if we can flatten that out a bit. And also, as a few people pointed out, one way to do this is to solder on a length of coax across uh the main uh two picofarad capacitor, I think it was.

**Dave Jones:** Actually, well, I replaced it with a bit of coax. So, I just wired that uh in parallel. I've got some RG-174 uh Belden, uh 35 cm worth. Of course, the uh longer it uh goes, the more you can um stretch that pulse out, but anyway, let's have a look what 35 cm soldered across the existing uh couple of picofarad capacitor in there can do.

**Dave Jones:** Let's give it a try. And bingo, that's actually worked a treat. Check that out. It's uh extended the pulse by What are we? 2 ns per division. So, it's extended it to 4 ns that pulse, and you can see the ringing up the top there, and it eventually flattens out and then drops back down.

**Dave Jones:** So, let's go in and measure the rise time of this baby. We're still got our averaging on in there, and what are we getting What do we know? About 288 ps rise time.

**Dave Jones:** Beautiful. And of course, we can zoom all the way in and go down to 5 ps per division just because we can. But, that's beautiful. So, still got the averaging on there, and that is a little That's a nice useful addition to extend the length of that pulse.

**Dave Jones:** So, let's get the official figure here. We've got to have the full pulse on the screen there so it knows the level where at. It measures 10 to 90% and 296 odd ps.

**Dave Jones:** So, let's call it pretty close to an even 300 ps. Now, if you're wondering what happens when I remove the capacitor and just have the coax there, look at this.

**Dave Jones:** We don't get a nice There's no more ringing at the top there, but we don't no longer get a nice stepped waveform. We sort of get this and then this little kink in here and then slowly rising up.

**Dave Jones:** So, it looks to be better to at least have the the old the the original cap in there, the original Jim Williams circuit. And of course, this is the Jim Williams recommended add-on.

**Dave Jones:** I can't remember offhand if he recommended leaving the original cap in there, whether or not he said to replace the capacitor or to with coax or to just add the coax in parallel.

**Dave Jones:** But, yeah, that is not a nice, you know, rise time input at all. It's, um, you know, it's pretty darn horrible. And you know, the rise time of course is going to be way out of whack, you know, 800 picoseconds or 1.4 nanoseconds four times still cuz that has all that down there.

**Dave Jones:** It's, you know, it's yeah, it's no good as a pulse generator for measuring bandwidth. And we'll step it up just a little bit by putting on what will the reel says 100 m of coax, but I don't think there's 100 m still left on there.

**Dave Jones:** So, let's call it, you know, maybe 75 m or something like that. It's Philips branded. I I Googled that part number, nothing comes up. Um, so, you know, it's once again, it's thin coax like the RG 174, but anyway, let's give this a try and see what we get.

**Dave Jones:** And here we go. This is with no original capacitor in there. So, it's just like the 75 m of coax or whatever. We're talking 184 picoseconds according to this, but that increases if we get the whole pulse on there.

**Dave Jones:** The whole pulse, we're talking 50 nanoseconds per division, 150 like we're talking 170 nanosecond pulse or thereabouts now. And but we get a a nice clean edge there, but then it sort of we get a little bit of ringing and then it starts still starts to rise up there.

**Dave Jones:** So, I really don't like that. And then we've almost got a linear fall back at the top of the waveform there. So, yeah, I think I might put the original cap back and see what we get.

**Dave Jones:** No, we get pretty much exactly the same with that linear ramp going down at the pulse. It's the same pulse length of course. And but we get this massive overshoot here at the first edge, the rising edge.

**Dave Jones:** But anyway, if we let the scope call that in terms of rise time, we're talking 180 picoseconds there. So, yeah, I don't know. You know, you could you could take it at any point you deem you know, to be worthy of being the 90% point.

**Dave Jones:** And as it turns out, I just killed my two picofarad capacitor and the end cap just uh fell off. Um so, I've put in a five picofarad the nearest one I had to hand quickly and it's slightly increased amplitude, I believe, but there we go.

**Dave Jones:** We're back to our original cap with no um uh coax on there, just the five picofarad capacitor and we're talking 295 odd picoseconds rise time and 598 or say even 600 picoseconds fall time.

**Dave Jones:** And I resoldered my coax back on the 35 cm of coax cuz I really like that. That seems uh like an ideal thing to use. A bit of overshoot there, but we can get the rise time nicely and we are talking 270 picoseconds rise time and 1 nanosecond fall time.

**Dave Jones:** So, I'm going to use that as the reference. I'm going to leave the circuit alone now. I'm not going to play with it anymore. Um and now we'll do some bandwidth measurements on our other scopes based on that reference rise time of 270 picoseconds.

**Dave Jones:** So, let's go back to our Agilent 3000 series the 3054 X-series oscilloscope. 500 MHz. I'm using the exact same attenuator, exactly the same as we just did. Wanted to keep it all the same.

**Dave Jones:** Didn't want to put it directly in there. We'll do that uh I just wanted to see what we get, keeping the conditions the same. Let's check out the rise time.

**Dave Jones:** And as you can see, the wave shape is, I believe, almost identical to what we were getting on our $140,000 uh dollar 13 GHz Agilent. But, of course, our rise time is greater, and it's basically uh jumping between 610 and 630.

**Dave Jones:** It's mostly been about 630 picoseconds there. So, I'm going to take that as the value. And if we punch that into our calculator, 0.4 divided by uh 630 picoseconds, what do we get?

**Dave Jones:** We get Ta-da! 635 MHz. So, we were definitely overestimating uh before because we didn't um because we only had the pulse which didn't settle out. But now we've got the pulse which settles out there, the scope is able to take the average of the top, get the 90, and get the true 90%, and give us the rise time.

**Dave Jones:** So, 635 MHz, but that doesn't take into account the uh absolute rise time of our unit, which we uh saw was 270 picoseconds. So, we haven't taken that into the calculation yet, but even so, that value, 635, if you go back and look at my uh Marconi uh 2023 video, which I'll uh have to link in here, um we measured the bandwidth of this thing, the minus 3 dB bandwidth of

**Dave Jones:** this at, guess what? It was actually 637 MHz. So, you tell me, is that just a uh coincidence, or is this actually good enough to, you know, measure to a reasonable degree of accuracy the minus 3 dB bandwidth using that formula, that maximally flat formula in quote marks of 0.4 on the rise time.

**Dave Jones:** It gave it It gave us within a couple of megahertz the exact value cuz there's error in this, of course, and there was a slight error in the measurement of our Marconi 2023 minus 3dB bandwidth as well, but you know, it it's pretty darn close.

**Dave Jones:** But we haven't taken into account that 270 picoseconds. So, I'm not sure if we have to, but hey, it is basically spot on. And if we take a look at it here, this is directly connected straight into the scope.

**Dave Jones:** There it is. So, it's really it's really bang on, as good as we can get it. No coax in No No coaxial connection, just direct BNC connection in there.

**Dave Jones:** And the amplitude's a little bit over. It's off the screen. It'll give us 590 picoseconds there when it's off, but really you need to get the whole thing on the screen for that to be an accurate measurement.

**Dave Jones:** And it is jumping between that 630 and that 610 picoseconds like we had before. So, if anything, it's slightly lower, and hence overestimating our um uh bandwidth again like we did uh last time.

**Dave Jones:** So, um in this case, we might have to take into account the uh 270 picoseconds absolute rise time, but still I think this probably demonstrates that you can um probably just measure the bandwidth of a 500 megahertz scope using this basic Jim Williams pulse generator with the coax mod on there as well.

**Dave Jones:** I've got 35 cm of coax with the original cap in there. And that that works. That works a treat. And a few people have asked to see the trusty old Rigol to see what it gives.

**Dave Jones:** So, there's the fabulous boot screen. All Rigols now come shipped with this boot screen. And we'll give it a go. Um I'm using a 50 ohm uh termina- 50 ohm in in-line terminator because of course the Rigol doesn't have uh 50 ohm termination on it.

**Dave Jones:** So, let's have a look. I've got the 75 m of coax set up here. And of course we've got our downward uh slope on the waveform here. So, once again, where do you take the 90% uh point from?

**Dave Jones:** I'm not sure where the Rigol's taking it. It's telling us the rise time is less than 2.4 nanoseconds, but really, you know, it's not that accurate less than four.

**Dave Jones:** Depends where you want to take it. If we want to um say uh zoom into the position here and take that as the value. Um then we're talking, you know, 2 nanoseconds.

**Dave Jones:** So, what I'm going to do now is measure the uh real bandwidth, the actual minus 3dB bandwidth of this uh scope using my Marconi uh 2023 RF signal generator.

**Dave Jones:** So, what I've done here, I'm feeding in a 1 MHz sine wave at 1 V peak-to-peak. So, we want to uh increase the input frequency um until it drops to 0.707.

**Dave Jones:** And that'll give us our real bandwidth. So, let's give it a go, shall we? Okay, let's wind the wick up. And you can see that lovely effect there is due to the averaging.

**Dave Jones:** I got 16 averages turned on. We're at 50 MHz now, so let's go up, increase the time base. So, we want 0. 70 or 770 mV. So, let's keep going.

**Dave Jones:** We're at 123 MHz now. It's 0.707. Once again, this is 50 ohm terminated of course, and it's jumping around. It's hard, but let's call that um at is that's let's call that as the minus 3 dB point and we're talking 136 MHz.

**Dave Jones:** So, that is our the real bandwidth of our 100 MHz modified, of course, 100 MHz Rigol scope. Beautiful. That's our reference point. So, clearly the two nanoseconds that we're uh reading here for the rise time, that's 200 MHz.

**Dave Jones:** That's way overestimating. So, that's with our 75 m of coax. So, let's Well, you know, if we get 4 nanoseconds, once again, it's not very accurate down there. So, you know, there's uh it jumps up to 2.4 maybe.

**Dave Jones:** You know, it's not that great. And to get our figure of 136 MHz, we need a smidgen under uh to measure a smidgen under 3 nanoseconds rise time. So, it's clearly not going to give us that.

**Dave Jones:** Doesn't have the resolution to do that, I'm afraid. So, let's That's with the 75 m coax. Let's give the 35 cm coax a try. And here it is, 35 cm of coax.

**Dave Jones:** And if it looks familiar, it's because it's like the standard pulse again, like the without the coax that we saw. And the reason for this is because this bandwidth of this scope is lower.

**Dave Jones:** So, it just you know, it hasn't got time for the thing to settle out. So, we really need to add maybe just a little more coax to it, so we can do that.

**Dave Jones:** We're getting 2.48 nanoseconds. So, you know, it's not the value of three that we require. We can't really turn that up a tad cuz it can't measure the rise time there, but yeah, it's uh 2.5, it's 2.6.

**Dave Jones:** Um it's not going to cut the mustard. Need more coax. And I've doubled that to 70 cm of coax. And as you can see, it does flatten out before it drops back down now.

**Dave Jones:** But, uh, we're still getting, you know, the resolution's not bad on the rise time, uh, measurement here. It's, um, but we're still only getting just over 2 ns, which is up near 200 MHz.

**Dave Jones:** So, clearly overestimating once again. And how about 105 cm of coax? I keep adding on these 30 35 cm, uh, segments. And, uh, nope, no good. At least with the automated, uh, rise time measurement, just over 2 ns still.

**Dave Jones:** Now, what I'm going to do is manually set up my cursor cursor measurements here to the 10 and 90% mark. I've used a my, uh, variable vertical, uh, attenuator to set it for five divisions peak to peak to that to the basically the top of the waveform there, ignoring the overshoot there.

**Dave Jones:** And then I've set my cursors to the 10% and 90% mark. And if we zoom in here, we can get, let's have a look. Let's smooth that to the where it just crosses that vertical graticule division there.

**Dave Jones:** And go across where 2 ns per division. And where it crosses that one, it looks like it's only one division. So, it's still 2 ns. Pretty much exactly what it was measuring automatically.

**Dave Jones:** So, it looks like we're entirely unsuccessful here of using this, uh, Jim Williams pulse generator, even with the coax, uh, mods to extend the pulse to, uh, accurately measure the, uh, or at least give us an a reasonably accurate ballpark measurement of the minus 3 dB bandwidth.

**Dave Jones:** We're way overestimating here at like, you know, in the order of, uh, 200 MHz, um, instead of the 136 which we measured is the true analog minus 3 dB bandwidth.

**Dave Jones:** And that's using the formula of 0.4. Of course, it may or may not actually apply to this scope because it may not have a maximally flat response. Who knows what's going on here?

**Dave Jones:** But yeah, you know, it relies on a whole host of factors. You've got to get the correct waveform type with no over as little overshoot as possible. You've got to extend the pulse as much as possible.

**Dave Jones:** And you've got to, you know, make sure it's a suitable pulse length for the bandwidth of the oscilloscope you're using. And then you've got to know what the correct factor is, what the that correct formula is based on your particular scope and what method it's implementing to do that.

**Dave Jones:** So, yeah, it's it's not looking that great. It seemed to work for the Agilent 3500 MHz scope, but can't get this thing to work on the Rigol really. I mean, even taking our Gaussian formula of 0.35 on the rise time, we're still overestimating by quite, you know, tens of megahertz at at minimum.

**Dave Jones:** Quite a significant error. So, anyway, more food for thought. We might do some more tests on this later. But anyway, I hope you enjoyed that. That's the uh Jim Williams pulse generator with coax modification on it.

**Dave Jones:** And it does certainly seems to extend the pulse. So, if you got one of these, definitely give that extra Jim Williams mod with the coax a try and see what you can get.

**Dave Jones:** So, even that may not be fantastic for measuring the bandwidth of a scope with those formulas unless you get the waveform absolutely perfect. It could still be used for, you know, measuring the rise time of systems and things like that.

**Dave Jones:** The effect on the the slew rate. Have it just having a fast rise time pulse can be quite useful for quite a few different applications. So, if you enjoyed the video, please give it a thumbs up and if you want to discuss it, jump on over to the EEVblog forum.

**Dave Jones:** Catch you next time.
