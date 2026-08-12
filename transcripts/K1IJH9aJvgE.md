---
video_id: K1IJH9aJvgE
title: EEVblog #699 - Rigol DS1054Z Oscilloscope Jitter Fix Testing
url: https://www.youtube.com/watch?v=K1IJH9aJvgE
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 28, "3": 39, "4": 57, "5": 67, "6": 91, "7": 120, "8": 138, "9": 154, "10": 165, "11": 181, "12": 206, "13": 221, "14": 240, "15": 252, "16": 274, "17": 285, "18": 300, "19": 317, "20": 341, "21": 355, "22": 374, "23": 388, "24": 399, "25": 411, "26": 424, "27": 440, "28": 451, "29": 465, "30": 483, "31": 495, "32": 505, "33": 521, "34": 531, "35": 548, "36": 569, "37": 583, "38": 593, "39": 605, "40": 621, "41": 637, "42": 654, "43": 667, "44": 678, "45": 693, "46": 706, "47": 720, "48": 736, "49": 755, "50": 768, "51": 784, "52": 792, "53": 806, "54": 816, "55": 842, "56": 854, "57": 865, "58": 891, "59": 906, "60": 918, "61": 934, "62": 952, "63": 975, "64": 987, "65": 1003, "66": 1020, "67": 1035, "68": 1044, "69": 1063, "70": 1073, "71": 1087, "72": 1106, "73": 1120, "74": 1130, "75": 1152, "76": 1165, "77": 1175, "78": 1187, "79": 1204, "80": 1221, "81": 1237, "82": 1249, "83": 1261, "84": 1274, "85": 1288, "86": 1303, "87": 1318, "88": 1334, "89": 1344, "90": 1368, "91": 1395, "92": 1408, "93": 1421, "94": 1439, "95": 1449, "96": 1459, "97": 1472, "98": 1490, "99": 1512, "100": 1545, "101": 1569}
---

**Dave Jones:** Hi, this is a follow-up video to the Rigol DS 1054Z firmware issues that were found in a previous video. If you haven't seen it, click here or link down below and watch that first cuz otherwise it may not make too much sense.

**Dave Jones:** Anyway, Rigol have finally released some new firmware that they claim fixes not only the 5 microsecond jitter issue, which we can see here, but also the AC trigger coupling jitter as well.

**Dave Jones:** So, I haven't installed the new firmware yet. So, we'll try it. Now, they have actually released a beta trial firmware fix for it before they put it on the EEVblog forum.

**Dave Jones:** So, huge thumbs up to Rigol for actually engaging directly on the EEVblog forum and and actually releasing it there so people could trial it, but unfortunately that one didn't work and I didn't get around to trying it myself, but a lot of people on the forum tried it and they said not didn't fix it and had other issues.

**Dave Jones:** It was locking up the keyboard and doing all sorts of weird and wonderful stuff. So, Rigol pulled that before I got a chance to try it, but they're finally in the new year now.

**Dave Jones:** So, happy new year to everyone by the way, and Rigol have released the new firmware. So, let's give it a whirl. But, before we do that, a few users on the EEVblog forum actually went to a lot of trouble to try and figure out exactly what was causing this 5 microsecond jitter issue and they pretty much came to the conclusion and I think they're right that it was

**Dave Jones:** something to do with the PLL, the phase lock loop inside the 1054Z that generates the main sample and FPGA clock. Now, this is a lower frequency crystal and there's nothing wrong with the crystal itself, but it's the PLL chip itself and the loop components around that and this is a programmable chip and they discovered that it looks like it's not locking properly and it's getting jitter and doing all sorts of weird

**Dave Jones:** things. So, that would explain it if your main clock for your ADC and sampling system and, you know, everything else, your main FPGA is jittering badly due to a poor PLL lock or something or, you know, some sort of issue to do with the PLL, then, well, that's going to upset the whole apple cart.

**Dave Jones:** And we're pretty much and we're pretty sure, I think most people are pretty sure that's actually what's at fault here. And Rigol have they haven't admitted that, but they have said that they have updated the coefficients which get programmed into the PLL chip when the unit boots up.

**Dave Jones:** And well, that's, you know, most likely to be the issue or it could be that plus a combination of some stuff in the in the sampling FPGA as well.

**Dave Jones:** We don't know unless Rigol actually come clean and admit exactly what the issue is and what they did to fix it, but I thought we'd not only reproduce the problem here before we update the firmware, see if it works, but this thing open, have a quick sniff around with an EMC probe, see if we can get that signal.

**Dave Jones:** Let's give it a try. So, consider this our before shot for the 5 microsecond jitter. Here it is, we've got a 20 MHz square wave going in. We've got our 5 microsecond precisely offset and I've got infinite persistence on there and you can see pretty much it's doing just maybe a division maybe, you know, 1 and 1/2 little graticule positions there.

**Dave Jones:** So, it's 5 nanoseconds per division. You know, it looks like it's maybe 1.5 almost 2 nanoseconds jitter on there. Not a huge amount, but as I said in the previous video, my unit is not a particularly bad one.

**Dave Jones:** Some people have it really horrifically. So, and if I push the horizontal to go back to no offset at all, bingo, you'll see it vanish. All right, so we crack this open and what we're going to use here to measure the PLL clock in this thing, I'll show you a close-up in a minute.

**Dave Jones:** We're going to use this you've seen in a previous mailbag. This is the Tech Box EMC probe set and we've got the three H field probes here, the magnetic field probes and the one we're going to use is the E field probe here.

**Dave Jones:** The magnetic field probes will will work especially the smaller loop one here, but in this particular case we really want to get down, isolate components right there. So the E field probe is better with its tiny tip and really we're not talking about large magnetic you know loop currents and things like that.

**Dave Jones:** So the E field probe is a better choice for this and we've got our wideband amp here. So that goes from 3 meg up to 3 gig. So that should be pretty good.

**Dave Jones:** We've got our Rigol DSA815 spectrum analyzer here and we can now sniff around. What I'm going to do though is I think I'm going to have to set up a second camera so that I can show you probing around here at the same time as the result we get on the screen here.

**Dave Jones:** Now here's the main culprit right here, the Analog Devices ADF4360-7 here and this is an integrated synthesizer and voltage controlled oscillator. It's basically a PLL which multiplies the main crystal here, 25 megahertz.

**Dave Jones:** You can see that oscillator. Now this oscillator is going to have bugger all jitter. That's not going to be the issue. It's going to be this phase lock loop and you can see it sort of multiplies that frequency based on these loop filter components around here and the internal coefficients that have been programmed into it by the firmware at startup and then you can see it's a differential output here and that

**Dave Jones:** is the main clock which goes into your ADC over here. I'm not sure if it actually goes anywhere else, whether it's goes into the FPGA or such, but it looks like it might just be for the ADC here.

**Dave Jones:** So, let's give it a burl, see if we can sniff around here and get the signal out of this thing. Now, this is certainly not a tutorial, so I won't bother explaining how PLLs work and how the loop filter components and coefficients and all that sort of jazz works, but these these components here, they will be our loop filter uh components.

**Dave Jones:** These are looks like we've just got some output AC coupling here, and that's about it. So, what we can do is use our probe to sniff around here and see if we can get that output clock signal.

**Dave Jones:** All right, let's have a probe around with our E-field probe here, and you can see how I said it's got a tiny little tip on there, so it really allows us to get in here and look at our components.

**Dave Jones:** Now, I've set up the DSA 815 spectrum analyzer. Well, I haven't set it up. It's just like power on default. It's just full span like this. So, we just want to have a look to see if we can find the signal.

**Dave Jones:** Now, if we get our probe in here like this, and we go very close to our the output pin here, it's a single-ended output on our clock, our 25 MHz clock.

**Dave Jones:** There we There we go. You can see the clock and all its harmonics right down there. No problems whatsoever. So, if we can now go over our PLL chip, we can't see anything on the PLL chip.

**Dave Jones:** You can see how discriminatory this probe is. We've hardly moved it, and it's vanished. Now, let's move the probe over these loop components up here. Bingo! Look at that.

**Dave Jones:** There is our PLL output frequency right there. Massive spike. And look, I moved that away just a little bit from those components, and or back over the chip and it vanishes vanishes.

**Dave Jones:** So this is how useful these damn probes can be. You can get right in there and of course we can go to the output traces here not nearly as the differential output here not nearly as uh high amplitude as what we get with those loop components.

**Dave Jones:** So really uh anyway we're getting it quite a decent signal on there. So now we can center our spectrum analyzer here and just have a look for any side components on there.

**Dave Jones:** See how clean that is. But as I said before we can use this tiny H field probe here. So let this is the smallest one out of the three I've got so it's got smallest loop area.

**Dave Jones:** So you'll get the most the best discrimination there. So let's put it over here and look we can put it over the ADC here for example and you can see like various components on the ADC there which we couldn't actually see with the E field probe.

**Dave Jones:** So this is going to pick up more but it depends on the loop area and the current flowing. So here we go. What? Hey there we go. There's our spike.

**Dave Jones:** That's actually I think bigger. That yeah. Oh yeah look at that. It's really gone to town there. Check that out. We're really picking that up but we're also picking up so we're picking up much higher amplitude than we're getting before but we're also picking up lots of other crap down here as well.

**Dave Jones:** So for the for the purposes of measurement I think the E field probe is probably going to be the better choice here. We can really get localized in but yeah as far as amplitude goes we are actually getting a higher amplitude there with that uh with that tiny H field probe.

**Dave Jones:** But yeah look you can pick up a lot of crap at the same time if you're not careful. Whoa look at that. And if we turn our marker on there look, we can see that is bang on 1 gig because, hey, this is a 1 gig sample per second scope, is it not?

**Dave Jones:** That's exactly what you'd expect, and it is bang on according to the Rigol. Now, I've got my probe over the uh loop components there. I've got some auto scale happening.

**Dave Jones:** We've got 1 gig center, and it looks pretty clean like that with a span of uh 10 MHz, but aha, our bandwidth Here we go. Our resolution bandwidth is by is the default uh 300 kHz here.

**Dave Jones:** So, we need to really knock that down before we can start seeing some components in there. So, let's have a burl at that and see what we get. And here we go.

**Dave Jones:** If we get a 4 MHz uh span on here with a resolution bandwidth of 300 Hz, takes a while to build up there, but look at that. That doesn't look too crash hot, does it?

**Dave Jones:** And here it is. That'll do. Now, I don't really care about the particular details of what's actually going on here. All we want to do really uh for the purposes of this video is to see if this stays the same after our firmware change with the with the same setting, same probe position, everything else.

**Dave Jones:** I think we're going to see a fairly dramatic change. Now, here's the interesting bit. I've changed the span here to 1 MHz total, um and look, we can see these peaks here.

**Dave Jones:** Here's our fundamental here, okay? And look at the deviation from here to here. The delta I've set up a delta of those two markers, 100 kHz. Why is that significant?

**Dave Jones:** Well, our issue is a 5 microsecond multiple jitter problem. That means at um every 10 microseconds it goes away, multiples of 10 microseconds It goes away and comes back, etc., etc.

**Dave Jones:** Well, what is 10 microseconds? Invert that, it's bang on 100 kHz. Aha! Please excuse the crudity of the model. Didn't have time to build it to scale or to paint it.

**Dave Jones:** Now, I'll try and explain kind of what's going on here. Now, with our little DaveCad droid, now, if we've got our trigger point here, okay? This is our I know it doesn't kind of make sense the way I've drawn it, but stick with me.

**Dave Jones:** Anyway, if you've got the trigger point here, you've got your 1 GHz sample clock, okay? Now, because that is the trigger point of the oscilloscope, you're not actually going to see any jitter there, because the clock can be jittering like crazy.

**Dave Jones:** You're not going to see it because at at this point on on the screen and on your waveform, because it's the same sample point each time. You're only going to see it when you shift the waveform in this direction and then view this one in the center 5 microseconds later, okay?

**Dave Jones:** This is the problem. And let's say you view it 10 microseconds later, well, there's our 100 kHz, okay? If this uh main sample clock is jittering, effectively being modulated by 100 kHz, that's a period of 10 microseconds.

**Dave Jones:** So, once again, you're not going to see it there because it's going to match up precisely with the jitter time, but if you go halfway, i.e., half that value of 10 microseconds, 5 microseconds, bingo, you're going to see all your jitter in there.

**Dave Jones:** And then likewise at 15 and so on. So, I hope that's as clear as mud. Hmm, I think I could have come up with a better explanation than anyway.

**Dave Jones:** Right, so we've got that little baseline there. Now, let's upgrade our firmware. For the record, this is what I'm running now, 4.01 uh {dot} sp2 on uh 1.1 board revision.

**Dave Jones:** Okay, let's update the firmware here. I've installed the file on the stick that's what you're supposed to do. The .GEL there we go. Bang. Caution new uh software version detected.

**Dave Jones:** We're installing 4.02.04.07. Do you wish to continue? Please do not remove. Come on. You can do it. Could take a while. Should I twiddle my thumbs? I think it's worth it, isn't it?

**Dave Jones:** Come on. Come on. Anyway, what we really want to see is a change in that PLL. The PLL coefficients Rigol have said they have changed them. So, they have admitted that.

**Dave Jones:** So, we should expect to possibly see a uh a change in that spectrum there. Congratulations. Update was successful. Now, you can restart the oscilloscope and enjoy it. I will enjoy it.

**Dave Jones:** If it bloody well works. So, yeah. I guess we just depower and power back up. Remove the stick, of course. And as usual, the scope does take a little while to uh boot, which is a downside of modern scopes.

**Dave Jones:** But, oh with their all new modern whiz-bang operating systems, you know, what do you expect? Anyway, we're in. We're in like Flynn. So, the utility system system information. So, no problems at all.

**Dave Jones:** 4.02.SP4. I've no idea if this keeps the uh you know, any upgrades and things you've got or any any software upgrades or anything. Presumably, it would. All right, here's our test.

**Dave Jones:** I'm putting the probe basically where I had it before. And let's go in there and uh Okay, here's the test. I'm putting the probe pretty much where I had it before.

**Dave Jones:** So, let's uh do single shot and see what we get. Bingo! Significantly different 1 MHz span there. I haven't changed anything else on here. So, I what you the waveform you uh saw before was this is what it has changed to.

**Dave Jones:** There you go. So, they certainly have updated the coefficients of this uh down in here. They've uh they've changed that because it's got um a uh spy bus on there which uh interfaces to the main uh micro and then they it has to program in those coefficients based on the particular loop filter components they've got on there.

**Dave Jones:** And there's a lot of tricky theory which all goes behind this. And well, yeah, I won't go into it, but hopefully Rigol have done their homework. Now, let's repower it and uh see if there's any jitter.

**Dave Jones:** All right, there's our 20 MHz signal at uh no delay 0.00000 picoseconds. Got to be me. Anyway, that's just crazy. Um so, we'll change our horizontal here. Oops, sorry, we'll go this direction.

**Dave Jones:** So, we'll tweak that up. I'm holding my tongue at the right angle just in case. And 5 microseconds. And ta-da! Look at that. It that looks pretty good. You can't complain about that.

**Dave Jones:** Like I can't zoom in any faster than that cuz that's the lowest time base is 5 nanoseconds uh per division on this uh 1054 uh Z. You might uh get an extra um step there if you've got the 100 MHz model, but I've only got the 50 MHz model.

**Dave Jones:** So, there you go. That is that is gone. And I've got infinite persistence on there, of course. And let's just I'll hit the horizontal button, so we'll jump back.

**Dave Jones:** So, like we can turn off the infinite persistence there. There we go. But, it's certainly it's certainly changed. So, I I can certainly consider that fixed. Although, I would have to go in and check for any other multiples in there or anything like that.

**Dave Jones:** But, you can pretty much be sure if you can measure it on the uh spectrum analyzer, then well, you should be able to actually calculate where any of these issues should be.

**Dave Jones:** But, looks like they fixed it. But, that's fixed it for my scope. They had the same issue uh before when they released the beta version of this fix. It fixed some people's machines, and everyone said, "Yay!

**Dave Jones:** Problem fixed. Thank you very much, Rigol." And then, other people came out and said, "No, made it worse." All sorts of things. Because those loop components uh they're they're going to have very significant tolerance, like 5 10% tolerance on those things, let alone over temperature and and everything else that can be involved.

**Dave Jones:** So, uh you know, really, um yeah, it's okay. It's fixed mine. So, fantastic. I'm a happy little camper. Um let's see if it's fixed the AC trigger jitter. So, put that back to the start there.

**Dave Jones:** That's uh go into our trigger jitter menu. You've got to go down here to setting coupling, and this is trigger coupling. As I've done a video on, it is not input AC coupling.

**Dave Jones:** It's AC trigger coupling. Big, big difference. So, let's do that, and ta-da! We're a happy little happy little camper there. If I Oh, let's turn off our infinite persistence, cuz I was uh just varying the um offset uh level control there.

**Dave Jones:** So, let's go into display, change that back to minimum. Thank you very much. So, I can change our level there. And of course, it's going to lose it because I'm adjusting the adjusting the trigger level.

**Dave Jones:** So, it's obviously like going above the waveform and it just doesn't know what to do. There we go. Set it properly the times one scale factor on channel one here.

**Dave Jones:** So, yeah, you'd expect it to go off trigger at when it gets to about two and a half cuz we're talking 1 volt, 2 volts, you know, two and a half there and that's what we start to see and bang at about yeah, 2.7 or something.

**Dave Jones:** So, that's right down on the negative side. So, our AC trigger coupling is now coming back down. Whoop, let's go. Sorry. Let's go negative. And about the same, 2.6 about 2.5 volts or thereabouts.

**Dave Jones:** Yep. So, that's not too shabby at all. On first glance here, AC trigger coupling problem also fixed. Very nice. And if you're curious to know about the new PLL signal here, well, our delta there is about 68.334 kHz.

**Dave Jones:** So, we need to invert and then halve that and that gives us an offset round about 7.31 microseconds. And here we go. 7.31 microseconds. Well, I don't see any noticeable jitter in there at all.

**Dave Jones:** So, yeah, I think that's pretty well fixed. So, although the problem's fixed, I did actually if you probably watch this in HD, you can actually see a little bit of fuzziness to the line.

**Dave Jones:** There is a slight bit of jitter there compared to the regular one, but uh you're really, you know, you're really pixel peeping there, but anyway, I still really have I do really have a still have a problem with this.

**Dave Jones:** Although, hey, the jitter problem on my particular unit is fixed. Okay, fine. But, this is a pretty awful clock. I mean, you know, ordinate like I've zoomed in this a little bit.

**Dave Jones:** I've now got a 500 kHz span here. And and I've got our delta there's a delta on there that's 67.5 kHz there. And then we've got another little peak which is showing itself here.

**Dave Jones:** And really none of this should be there. And it's like only like 37 dB down from the carrier here. I mean, that's it's pretty piss-poor. So, the output from that PLL is still not great.

**Dave Jones:** So, I think Rigol need to fix that. I mean, they need to fix that solid whether or not that whether or not they can even tweak the coefficients even further, perhaps, and get a better or whether or not they have to actually change their loop component values in hardware.

**Dave Jones:** And it wouldn't surprise me if Rigol just didn't mention this and like all existing unit and this firmware fixes all existing units, but secretly in the background newer units might actually have different loop value components.

**Dave Jones:** That wouldn't surprise me at all cuz this is pretty bloody awful. I mean, you know, a proper one should be like it should look, you know, none of this stuff should be here.

**Dave Jones:** It should be like right down here like this. It should be very nice like that. So, we shouldn't have these components in here, but it it's doesn't seem to I mean, I've checked the multiple frequency of that and it seems to be okay, but yeah, that's that's a still a pretty bad clock, but I you know, I mean, Rigol are between a rock and a hard place here.

**Dave Jones:** They don't want to have to recall every unit that's already been sold to actually fix any hardware loop component values. That'd be, you know, that'd be absolutely horrendous. And they have to weigh it up against the actual performance of the scope and well, if it's proven, hasn't been proven yet, but if it's proven that every it fixes everyone's unit out there and there's no reports of it, you know,

**Dave Jones:** different spreads of units. We've already seen that issue. A lot of people have a huge spread of issues. So, if we can get all those same people and even more to report whether or not this is an issue, we'll know if it's a solid fix.

**Dave Jones:** And if it's a solid fix, well, it's a solid fix even if this clock is still pretty pretty crusty. Well, you know, I think Rygo do need to fix this though.

**Dave Jones:** I don't like it still. Gives me the heebie-jeebies. So, there you have it. I'm pretty happy with the fix on mine. It seems to work well, but yeah, the proof is going to be everyone else when we've got actually, you know, statistically significant numbers and spreads of units and component spreads and all that sort of stuff.

**Dave Jones:** So, if it if it works out to be a solid fix, great, you know, I'm happy, but yeah, I there's still a chance that it may not fix everyone's unit.

**Dave Jones:** So, that's going to be Rygo's problem. Oops, we've re-triggered there. It shouldn't have done that. Wonder why I did that. So, yes, Rygo still need to be vigilant on this issue.

**Dave Jones:** And as I said, I still think they need to fix that clock. That's pretty piss-poor, but you know, it's one of those arguments like is it good enough to do the job if the scope if there's no measurable difference on the scope, well, does that clock matter?

**Dave Jones:** Is it good enough? Yeah, you know, ultimately, yeah, it's a bit academic that okay, it's not the world's greatest clock, that's for sure. It's pretty piss-poor, but if it does the job on this particular hardware and nobody can measure the difference on the scope itself, then yeah, what does it matter?

**Dave Jones:** So, I hope it's a solid fix. If it is, fantastic, but yeah, wouldn't be surprised if they sneak in a little hardware fix. and they you know like this thing shouldn't have happened like the design engineer should have damn well measured the output of the ADC clock there but hey maybe that like maybe they did and and and it was fine because a lot of units out there show

**Dave Jones:** absolutely no problems whatsoever and the PLL locks and everything's you know everything's hunky-dory so but they just didn't test a statistically significant number so it slipped through oops it was pretty embarrassing but yeah big thumbs up to Rigol for engaging the EV blog community and ultimately fixing this relatively quickly so they're a bit premature on the initial beta firmware release but hey you know they did pull it back which was

**Dave Jones:** great and now they've well on my unit so everyone please if you got one of these try it out and well the review is still out but you know this is a pretty damn good scope as I said even with those issues a lot of people still give this scope a big thumbs up and on mine I could maybe test it across temperature or something like that but anyway keep reading the EV blog

**Dave Jones:** forum down below for updates on this cuz that's where all the action's going to happen so sorry about the length of this thing it was supposed to be quick as all my videos are but you know I get a bit carried away sometimes oops so there you have it if you like it please give it a big thumbs up on YouTube cuz that helps catch you next time
