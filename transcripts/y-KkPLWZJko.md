---
video_id: y-KkPLWZJko
title: EEVblog #512 - Rigol DP832 Bad Design Investigation
url: https://www.youtube.com/watch?v=y-KkPLWZJko
source: youtube-asr
timestamps: {"0": 1, "1": 11, "2": 22, "3": 33, "4": 45, "5": 55, "6": 67, "7": 75, "8": 89, "9": 106, "10": 120, "11": 140, "12": 149, "13": 162, "14": 177, "15": 197, "16": 215, "17": 230, "18": 241, "19": 253, "20": 264, "21": 281, "22": 295, "23": 305, "24": 316, "25": 326, "26": 343, "27": 358, "28": 375, "29": 387, "30": 404, "31": 429, "32": 446, "33": 465, "34": 478, "35": 494, "36": 504, "37": 521, "38": 541, "39": 550, "40": 572, "41": 585, "42": 599, "43": 606, "44": 625, "45": 641, "46": 660, "47": 671, "48": 679, "49": 690, "50": 703, "51": 714, "52": 738, "53": 747, "54": 758, "55": 767, "56": 780, "57": 796, "58": 812, "59": 833, "60": 846, "61": 855, "62": 868, "63": 882, "64": 899, "65": 926, "66": 937, "67": 951, "68": 967, "69": 985, "70": 999, "71": 1017, "72": 1030, "73": 1041, "74": 1049, "75": 1065, "76": 1076, "77": 1094, "78": 1110, "79": 1120, "80": 1136, "81": 1146, "82": 1160, "83": 1172, "84": 1187, "85": 1199, "86": 1217, "87": 1231, "88": 1258, "89": 1270, "90": 1280, "91": 1293, "92": 1310, "93": 1323, "94": 1346, "95": 1360, "96": 1377, "97": 1393, "98": 1403, "99": 1415, "100": 1429, "101": 1440, "102": 1451, "103": 1467, "104": 1493, "105": 1505, "106": 1518, "107": 1539, "108": 1552, "109": 1562, "110": 1585, "111": 1600, "112": 1608, "113": 1620, "114": 1630, "115": 1644, "116": 1658, "117": 1676, "118": 1686, "119": 1697, "120": 1714, "121": 1726, "122": 1739, "123": 1747, "124": 1771, "125": 1788, "126": 1796, "127": 1811, "128": 1835, "129": 1847, "130": 1856, "131": 1868, "132": 1879, "133": 1889, "134": 1906, "135": 1918, "136": 1941, "137": 1951, "138": 1962, "139": 1974, "140": 1985, "141": 1994, "142": 2013, "143": 2025, "144": 2036, "145": 2050, "146": 2064, "147": 2072, "148": 2091, "149": 2101, "150": 2120, "151": 2133, "152": 2140, "153": 2151, "154": 2163, "155": 2175, "156": 2189, "157": 2198, "158": 2210, "159": 2222, "160": 2231, "161": 2247, "162": 2259, "163": 2272, "164": 2282, "165": 2302, "166": 2317, "167": 2334, "168": 2345, "169": 2363, "170": 2371, "171": 2382, "172": 2397, "173": 2411, "174": 2426, "175": 2435, "176": 2445, "177": 2462, "178": 2472, "179": 2489, "180": 2502, "181": 2514, "182": 2528, "183": 2541, "184": 2548, "185": 2559, "186": 2570, "187": 2587, "188": 2598, "189": 2609}
---

**Dave Jones:** Hi, uh I was just going to have a quick play around with this Rigol DP832 power supply. This is just a uh trace out the output circuit and uh probe a couple of waveforms and uh stuff like that.

**Dave Jones:** Maybe uh see if I could possibly find out uh uh what's going on, investigate that uh power on uh spike a bit further, but got the guts hanging out.

**Dave Jones:** And one of the first things I noticed was that um suddenly like I couldn't see the display, but the fan would suddenly start revving up and then uh going crazy.

**Dave Jones:** And I found out what was happening without even probing the thing is that the power supply would actually reset after a little bit of time. And I'm going to leave it here and uh just see if it resets.

**Dave Jones:** So, I switched on all the outputs there and uh hopefully if I won't touch it cuz I think maybe, you know, the reset might have something to do with, you know, there might be an EMI issue.

**Dave Jones:** The board's all hanging out here, all the wires, the you know, the some of the digital stuff going here is all loosey-goosey hanging out in the breeze. And uh maybe that has something to do with it.

**Dave Jones:** But anyway, um I'm just going to leave it here. There's no load on it, of course. And I found that the damn thing reset. So, I'll just leave the video running and see if we can capture that.

**Dave Jones:** Usually it doesn't take too long. It only takes like a minute or two. No, as Murphy would have it, it's not going to reproduce the problem. The old white coat syndrome strikes again.

**Dave Jones:** I've left it for a couple of minutes and uh annoying. Anyway, what I was doing is I was adjusting the output voltage in steps just as a first uh thing just to see where it um you know, it got the uh transformer taps and uh stuff like that.

**Dave Jones:** So, maybe if I turn the voltage back up or something like that. Anyway, I'll leave it for another couple of minutes. I don't remember moving it or touching. I didn't move my multimeter it here out of the shot to to here, but I don't know.

**Dave Jones:** Better hold my tongue at the right angle. Hang on. Woohoo! Did I get it? Did I get it? I got it. See, it reset. It took bloody what, a 9 minutes on the camera here, but I got it.

**Dave Jones:** So, I was just in the other cubicle and heard the fan rev up. Bastard. So, the thing just resets itself. Let's turn that back on see if we can get it to reproduce even faster.

**Dave Jones:** I don't know why. I have no idea. I'm not probing anything, not touching anything. The outputs still seem to work, but I've got it under no load and the thing just reset itself.

**Dave Jones:** There we go. There we go. Got it. Bingo. What was that like a minute? There we go. It just switched off and reset. Why? I have no idea. My only guess is because it's, you know, it's hanging out here.

**Dave Jones:** It's not in the system. So, it may be an EMI issue getting in somewhere that's resetting this sucker. I don't know. All I can do really is fold this back in, screw it back in place, and run it as a bench supply for, you know, an hour and see if it see if it resets.

**Dave Jones:** Now, there's one thing I found is that this regulator in here, this tiny little that's an LM317, that's actually delivering the that isolated 5 volts for the main logic that we saw in the teardown, and I noticed that was getting really, really hot.

**Dave Jones:** And look at that. I mean, we're talking, you know, this isn't going to be super accurate, but look. I mean, it's not going to read over though. So, you know, I was getting close to 90 or something at one point.

**Dave Jones:** There we go. 95. It's crazy. That thing is getting super hot and I'm not sure if that's normal or not. Surely it can't be running that hot. Unbelievable. Have no idea why.

**Dave Jones:** Now, I've actually measured this thing and there's the 5 V that it's actually supplying and the input voltage, if I can actually get in there, correct ground. Yeah, there we go.

**Dave Jones:** 12 V. Now, I'm reading well over 100° on that now and I can should be able to get in there with a thermocouple and even confirm that. Look at that.

**Dave Jones:** That is ridiculous. 110° on the heat sink and this thing's only been on for like 10 minutes 115, 120. Unbelievable. No wonder something that regulator is just going to shut down and no wonder the thing's going to reset.

**Dave Jones:** So, clearly something is drastically wrong there because, you know, like an LM317 is only got an operational temperature range to like 120 125° or thereabouts and it's got built-in thermal overload protection.

**Dave Jones:** So, I think that's why this thing's resetting. Actually, as I think that even though I haven't measured it, I think the regulator is just getting too hot and it's shutting down for some reason.

**Dave Jones:** And of course, you can't have it operating at that temperature. It's just ridiculous. Let alone the like I was measuring what 110° plus on the case after a minute or two, let alone the actual die temperature itself.

**Dave Jones:** So, yeah, it's going to thermally protect itself and shut down and I think what's happening there cuz this supplies the main 5 V rail, which powers all of the logic board, of course.

**Dave Jones:** So, you know, it'll just shut off the output and it'll reset like that. And of course, you can't run this thing at too hot a temperature anyway being right next to these two large filter caps here, even though they're 105° C rated, they're just going to die, you know, in very short order.

**Dave Jones:** So, there is something wrong here. Surely, this cannot be normal. So, I'm just wondering if there's anything that I've done in the teardown to cause increased power consumption. I mean, my supply seems to work just fine.

**Dave Jones:** So, I don't know. I'm I'm at a loss here. I wasn't I you know, I wasn't expecting to troubleshoot this thing. I thought I'd um you know, just be able to probe some waveforms and and you know, do a little bit of reverse engineering and stuff like that, but no.

**Dave Jones:** Now, I've got this bloody problem to contend with. What the And there's also a software bug in this thing which people on the forum have actually reported and confirmed, and I'll just confirm it here.

**Dave Jones:** What it is is if you set the current limit here below 10 milliamps, then it actually shows, even with no load, nothing connected at all, no trickery going on here whatsoever, um it will actually show 30 milliamps reading current.

**Dave Jones:** So, let's try that. Let's lower it. 14, 13, 12, 10. Here we go. Bang. Look at that. It jumps up and reads 30 milliamps. Crazy. Why? Unbelievable. Of course, when it goes down to zero, it's it reads zero, but anywhere from 1 to 10 to 9 milliamps, Look at that.

**Dave Jones:** 30. And then it just goes back to zero over that. Ah. What's going on there? Now, what I've done is put the lid back on here, and it well, it's not actually resetting now, presumably because it's got more airflow actually, you know, it's sucking in the air through here and out the back.

**Dave Jones:** So, we're getting some forced airflow there where we didn't have that before. It was just still in the air, and I can still get in here and and probe the uh heat sink in here and yeah, it it rises.

**Dave Jones:** It takes some time to get the correct contact on the thing, but it's still running incredibly hot. Check this out. Look at that. We're already up to 90 and remember that heat sink is right next to those caps as well.

**Dave Jones:** 92, 93. We're still rising. That's just crazy and you know, I'm not making the best contact there with the heat sink, of course, so you know, it it it is basically you know, round it to at least 100°.

**Dave Jones:** You got to be kidding me. And just to make sure I wasn't hallucinating this thing or that I there was some bizarre fault that happened in the teardown or something like that.

**Dave Jones:** I decided just to make sure I'd put this to the forum and I've left it overnight and sure enough there's a whole bunch of responses from other people. I asked if they could test their units and they have and they have absolutely 100% confirmed exactly what I'm getting.

**Dave Jones:** This heat sink some people are even getting 110° in the case like this poking their thermal couple through. Somebody showed a floor IR thermal image of the heat sink up to 130° C.

**Dave Jones:** Of course, to do that they have to take the case off and then there's no air flow and all that sort of stuff. So, you know, much higher temperatures than what you get in the case here, but it's absolutely confirmed it.

**Dave Jones:** The this thing the design of this Rigol DP832A is totally flawed. I have no idea how it even made it past the first design review meeting with a bloody 5-V sorry yeah, 5-V regulator for the main digital logic operating at a nominal around about 100° C.

**Dave Jones:** You got to be kidding me. You got to be me. It's It's one of the worst design oversights I've ever seen. It is absolutely bread and awful. This is bread and butter stuff for a power supply.

**Dave Jones:** One of the first things you're going to look at is the bloody thermal design of this thing. Verify the thermal design when you're designing this product. Unbelievable. Anyway, it definitely confirmed, but what I'm going to do is I'm just going to I've left this overnight.

**Dave Jones:** I haven't powered it up today, so I'm going to switch it on and see if I can get the heat sink through here. So, it's got the proper airflow coming out the back.

**Dave Jones:** Of course, the fan's on a minimum when you first start turn it on cuz it's not It's not loaded. So, potentially the heat sink could actually cool down even further when I ironically when the outputs are loaded because then it will turn the fan on greater at a greater speed.

**Dave Jones:** You'll get greater airflow over that heat sink and potentially could actually cool that heat sink down ironically. But anyway, I'll switch it on, see what I can get. As you can see, my ambient temperature's around about 23° C, which is, you know, a typical office ambient temperature.

**Dave Jones:** Now, I've only had it on for a couple of minutes and it's difficult to probe. I've got it going straight through there. I've actually took out some of the silastic between the the two filter capacitors there so I could actually get through and I am probing the heat sink, but you know, it's it's not ideal contact at all.

**Dave Jones:** But as you can see, I mean, you can never actually read too high on this thing. So, it's not like, you know, I can get bad contact and accidentally read high.

**Dave Jones:** So, I'm getting 75° C on that heat sink. I've got to put a bit of pressure on the thermal couple just to get, you know, I'm I'm right on the side of the heat sink.

**Dave Jones:** Trust me, it is That's not making good contact at all. So, I think the true temperature of the heat sink is greater than that, but we're up to 77 and at the moment and still climbing.

**Dave Jones:** 78. This is not looking good, folks. Here we go. Look at this. 91°. That is just insane, really. I mean, I you know, a lot of people might think, "Okay, what's the problem?" Right?

**Dave Jones:** But, it's all about design margin. And you saw what happened when we'll verify this again when we open it back up, but I'm sure that this is causing that 5-V reset problem.

**Dave Jones:** Now, the to run something at 90 to 100° uh to run a you know, an a 317 regulator or any heat sink at that sort of temperature for something dumb ass like a nominal, you know, 5-V rail to power uh you know, the digital circuitry in this thing is absolutely insane because there is no design margin in there.

**Dave Jones:** Um yeah, okay. Maybe this thing might work and might continue to work for most people for a couple of years or something until those caps dry out, of course.

**Dave Jones:** I hadn't not even mentioning the caps yet. Okay? Without resetting at all, right? There might just be adequate airflow in there. But, what happens if you stick this damn thing in a rack?

**Dave Jones:** You know, they I think they even sell a rack mount kit for it. If you've got uh you know, a rack can easily get 40 or 50° ambient in there, something like that.

**Dave Jones:** Raises Even if you raise the ambient temperature here in the lab by an extra 5°, that could be enough to actually reset uh to trip the thermal overload in the die in that LM317.

**Dave Jones:** And uh who knows what we'll check which try and check which LM317 they're using, but that'll vary based on batch. It'll vary They might have um you know, they might declare that they can source that from any manufacturer, so it's not going to be consistent across your entire production run of these units.

**Dave Jones:** All sorts of stuff. It's just It's just crazy. There is no way in hell that anyone could sensibly make a decision that says to run that heat sink at 90° would be a good idea for anything, let alone a production unit like this.

**Dave Jones:** It's disgusting. It's ah And I've managed to get almost 110°. Look at that, 108. Depends where I wiggle it. Disgusting. Who the hell designs 5-V regulator that runs quiescent at 109° C?

**Dave Jones:** What a Now, I'm going to see if I can actually verify that the reset problem I'm seeing on the on the unit is actually the 5-V regulator going into thermal overload and dropping out, so to speak.

**Dave Jones:** So, I've set up the scope. Nominally, it's There it is. We've got our 5-V output there. It's all pretty clean. Triggering it about 4 and 1/2 V on negative going.

**Dave Jones:** So, we'll just leave it there and I've got my outputs switched on, so I'll definitely be able to do uh tell when it's done that and well, let's see if it correlates.

**Dave Jones:** See if we trigger anything on the scope a drop out in that 5-V rail when this thing resets. Could take a while though. And look at the temperature that thing's running at, 141 and climbing when there's no airflow over it.

**Dave Jones:** Unbelievable. It's even got some additional little heat sinking on it due to the oscilloscope probe. Oh. And I only had to wait a minute or so and it's it has reset here, but I didn't get anything triggering on the scope over here.

**Dave Jones:** So, it looks like it didn't drop below that 4.5-V value. I mean, I you know, maybe I've got to tweak that up a bit. Maybe there's a voltage supervisor or something on the 5-V rail inside the main chip that or even could be a function inside the main processor or something a that's you know, is actually detecting a smaller drop out than what's there.

**Dave Jones:** Let me tweak it. No, it still couldn't get it to do it. I'm triggering at 4.8 volts and the thing just reset itself, but I still couldn't detect drop in that 5 volt rail.

**Dave Jones:** So maybe my theory is wrong there, but jeez, I don't see what else it could be. I mean, you know, just as a rough indication as what temperature those caps are running that just by sitting near that heat sink it you know, 130° or whatever it is.

**Dave Jones:** There you go. They're almost up to 70° just the cans on there. Of course, there's no airflow it's going to help when there's airflow over these things of course, but that's how you can get with just you know, just the coupling over to those capacitors.

**Dave Jones:** Well, I'm at a loss now as to explain exactly what the mechanism is for resetting this unit. I could have sworn it must have been the drop out of that regulator, but I cannot seem to capture any drop out AC or DC coupled at any time base of this regulator.

**Dave Jones:** So I I don't know. But anyway, what I've done is this board it when it was sitting here before it was resetting every 1 minute or 2 minutes absolute tops with monotonous regularity.

**Dave Jones:** Then I just put this paste fume exhaust I've got air blowing over it like this. It's been probably more than I'm pretty sure it's more than what was getting inside the case and all of a sudden bam, I've left for 10 minutes and it's not resetting at all.

**Dave Jones:** So it definitely looks like it has something to do with that the heat of that regulator, but the exact mechanism still eludes me. Now I've even got to the trouble to set up a window trigger here.

**Dave Jones:** Oh, oh, hang on. Yeah, I just saw that. I just saw it switch off. I don't know if you saw there was some dip in the waveform there. There was something.

**Dave Jones:** There was something there. I hadn't Damn it, I hadn't had the trigger on. I was too busy shooting this video. But anyway, looks like we may have finally got it.

**Dave Jones:** Let me switch this back on. Anyway, I've set up a window trigger here so that it can trigger anything outside of that those two windows there. So, I'm going to put it into single mode again and see if I can capture that.

**Dave Jones:** I've got it back on, but let's let's see what happens. Let's just leave it running. Well, no, it's switched off and reset, but we didn't capture anything even with that tiny trigger window there.

**Dave Jones:** But no, I still couldn't get anything there. So, I've gone back to AC mode and there it is. There's our AC coupled mode 50 ms time base there and I set up a window trigger mode just around that.

**Dave Jones:** So, let's up. There we go. Look at that. Did you see that? Look at that. There we go. So, we've got some sub Yeah. Yeah. I think we're we're getting very close to getting this.

**Dave Jones:** Anyway, you can see that right there. Looks like that's normal, you know, in quote marks, right? That's normal 5 V AC coupled output. We're only at 100 mV per division there.

**Dave Jones:** Now, let's trigger off that and see and watch it and see what happens. See if we can trigger anything when these switch off and it resets. Bingo. There we go.

**Dave Jones:** We finally got it. Yes, it triggered. You saw it. There you go. This waveform started I don't know, maybe a second before this thing reset itself. So, there you go.

**Dave Jones:** My theory was right. Well, you know, it could not be wrong, really. It had to be that voltage regulator. In this case, just doing, you know, just some subtle drop out there.

**Dave Jones:** It's, as you saw, we couldn't trigger on the 5-V any significant variation on the 5-V rail itself, but when you get down, you know, we're only talking like 100 mV per division.

**Dave Jones:** So, just that sort of noise or ripple that regulator is doing something, and it's not regulating as it should anymore. It's, yeah, it's still regulating at 5 V, but the AC component of it has actually changed.

**Dave Jones:** So, that is causing something on the digital board. I don't know what. I'm not going to go into the digital board and try and, you know, dissect why, you know, it doesn't matter.

**Dave Jones:** The fact is that regulator is overheating and is causing reset on the digital board somehow. So, that's what we captured there, and whoop. That is normally. So, you can see that it was, you know, double or triple in amplitude before when it actually fails.

**Dave Jones:** And we can no doubt capture that again. It'll be fully repeatable. You watch. Bingo. Too easy. There it goes. Switched off. Barely even had to turn around for, you know, 10 seconds, and we captured it.

**Dave Jones:** Woo. So, actually, this is a really good example of a little bit of a tricky real real-world troubleshooting scenario where I had a theory, okay, this regulator is overheating, it was dropping out, causing resets on the on the processor inside this thing in some manner, but you know, I my theory was almost blown blown out of the water.

**Dave Jones:** I expected the 5-V rail to just, you know, plummet down to zero or drop down to 3 V, or I don't know, do something stupid and allow, you know, a couple of volts or ripple to come through or something horrible like that.

**Dave Jones:** And I couldn't capture it even with a tight couple hundred millivolt window triggering around the 5-V rail that I had there before. I couldn't do it on that 5-V scale.

**Dave Jones:** So, I had to switch to AC and I originally couldn't even find it on AC as well. I'd done that before, but it turns out I wasn't setting my trigger point narrow enough.

**Dave Jones:** And in this case, I switched to the window trigger. And you can see it's probably just, you know, going over that top one. So, I had to set that I had had to use window triggering to go outside of the normal operational window to capture a really what is quite a small variation.

**Dave Jones:** And most circuits would tolerate that quite well, you know, if you've got an additional 3.3-V local regulator on your rail or you're just powering some 5-V logic, it's going to tolerate this sort of ripple generally no problem whatsoever.

**Dave Jones:** But there is something subtle on the particular processor inside processing circuitry inside this Rigol that is causing that thing to reset. So, if I wasn't absolutely confident that that regulator was dropping out, then I, you know, I could have thought, "Okay, well, I've checked that and that's not the problem." You know, not an issue at all.

**Dave Jones:** It must be something else. You go away go away. You chase red herrings until the cows come home. But no, we nailed it because I finally got down to a point where I could trigger off something that was causing this to drop out.

**Dave Jones:** Now, a couple of people have already been a little bit confused by this issue. So, I'll make it very clear. This 5-V regulator that we're looking at here, it has absolutely nothing to do at all with powering these outputs or what load you put on the output, whether you have a load or not.

**Dave Jones:** It's a completely isolated circuit with its own tap on the transformer and its sole purpose is to power all the digital circuitry in the front here. So, that applications processor, the LCD, some of the IO stuff here at the back.

**Dave Jones:** That's all there is to it. You can load down this all the outputs to the 495 watts and the dissipation on that heatsink is going to remain exactly the same.

**Dave Jones:** Although, as I mentioned before, when you do load down the outputs, the firmware knows that or it's measuring the temperature of the main heatsink, but I can't see any thermometer on thermistor on there at all measuring the temperature of that.

**Dave Jones:** It does increase the flow rate of the fan. And as I said, the increased flow rate of the fan could actually have the effect of actually cooling down a little bit that 5-V heatsink, but it's got nothing to do at all with loading the outputs.

**Dave Jones:** Now, the question is how much load does this thing actually take? How much does all this digital stuff in here take? Well, let's have a look at it. Let's measure our power.

**Dave Jones:** Let's switch it on, shall we? Let me put my probe in here and we'll switch that on. Here we go. And it's powering up. It's powering up. It's not much at all.

**Dave Jones:** Aha, silly me. I figured out what's going on. Well, not silly me, silly Rigol. This connector here, which obviously carrying all of that 5-V over to the board, they've actually got the colors of the wires back to front.

**Dave Jones:** I assumed, huh, silly me, that the positive wire would actually be positive. It's not. It's actually negative relative to that regulator. So, ah, now I've pulled out the black wire there because the reason why we're only measuring like, you know, 20-30 milliamps before is because this ribbon cable here was taking that return current.

**Dave Jones:** So, here we go. Now, we should be able to get it. Measure the actual current. Here we go. If we break into the positive wire here, which is actually black.

**Dave Jones:** Bingo, there we go. We're getting 300 it's booting now. Probably can't see the screen. There we go, it's just booted up. There we go. And now after it's booted, we're getting, you know, let's call it say 700 milliamps, something like that.

**Dave Jones:** Let's switch the outputs on. Doesn't make any difference, of course, but yeah, you know, it's jumping around as you'd expect, but let's call that 700 milliamps. And the input voltage, about 11.8 volts, which will of course vary with the line voltage because it is bridge rectified with just some filter caps coming from the transformer.

**Dave Jones:** So, you know, that could vary, but let's just call it 12 volts. Now, if we're getting 12 volts in and 5 volts out, well, we've got a delta or a voltage drop across this regulator of 7 volts.

**Dave Jones:** And because it's a linear regulator, it's got to drop seven the power is going to be 7 volts times the current flowing through it, which is of course the output current, which is .7 amps.

**Dave Jones:** 7 volts times .7 amps, 4.9, let's round it to 5 watts. This thing is dissipating five freaking watts. Now, anyone with any electronics design experience knows that no way in hell you're going to use a heat sink of that size for 5 watts, even if you've got a fairly high air flow.

**Dave Jones:** Uh you know, go going through your design and good thermal management. It's just ridiculous. 5 watts? Did no one even stick their bloody finger on this or even think about it?

**Dave Jones:** I'm flipping the finger, that's for sure. Let's just go to a representative heat sink. You haven't wasn't able to find the exact one, but this is going to be fairly close.

**Dave Jones:** It's an Avid Thermalloy 1 TO-220 free free sink. well it's actually a PCB mount one. It's got a PCB mount tab. This one looks to have two PCB mount tabs.

**Dave Jones:** So um I'm not sure if there's any heat sink on the copper at the bottom side of this board. I haven't taken it out but anyway, we're going to be easily able to get some ball park stuff here.

**Dave Jones:** And if we have a look at it uh let's go in here. It's talk we're talking 24.4° uh C thermal resistance there uh per watt but this is what we're interested in down here.

**Dave Jones:** Let's have a look at the graph, shall we? And what we've got here is well we don't need to really worry about the thermal resistance. What we're talking about here because this is um power dissipated.

**Dave Jones:** We know we're dissipating 5 watts. Look, it's for heat sink of this size it's off the graph already. That should be ringing alarm bells, right? And this is the mounting surface temperature rise from 0 to 100° C above ambient and that's the key of course.

**Dave Jones:** And what were we measuring on this thing? Well with no air flow, you know, we were getting basically um you know, 100 you know, well over 100 130 or something like that.

**Dave Jones:** And this is the ball park that we're operating up here at 5 watts with this size heat sink. I mean it's going to be very similar. We're just talking ball park calculations here.

**Dave Jones:** We're looking at 100° C rise above ambient and that's exactly what we're getting. It's ridiculous. I could go into there, you know, draw the thermal uh graph of all the things in there and the heat sink compound and the bloody you know, everything the junction case and all that.

**Dave Jones:** And imagine what the if this is what the heat sink temperature is at, imagine what the junction's at. Well, we actually don't even need to guess what the junction's getting at because let's look at the data sheet for the LM 317.

**Dave Jones:** Just take a typical one from Fairchild for example. Let's go down here. Let's get the thermal characteristics. Well, here it is. Um, there we go. Thermal resistance junction to case.

**Dave Jones:** We already know that but let's assume that there's no loss between the case and the heat sink, right? Let's assume that it that's just fine. Well, the case, there it is.

**Dave Jones:** 5° C per watt. We're trying to dissipate 5 W in this thing. The junction is going to be 25° C at least above that's above the already measured and quantified uh temperature on that heat sink which even in the case with the proper air flow and everything else is over 100° C.

**Dave Jones:** You got to be kidding me. Ah, facepalm. Hang on, double facepalm. Well, enough of that fiasco. I may as well um do a little bit of poking around of what I originally did before I bloody discovered this ridiculous issue.

**Dave Jones:** Anyway, I was just going to have a look at the a little just a little bit at the output circuitry here and see exactly what we've got and it is very easy.

**Dave Jones:** You've probably already guessed it but I've drawn a simple Dave card here and this is basically what we've got on the output. We've got the 1000 mic output uh filter cap right on the front panel terminals as you saw.

**Dave Jones:** I haven't shown the sense wires going back out. They're obviously going back to a sense amp but yeah, there's nothing in this at all really. There's no output relay switching of course or any sort of electronic Well, there's electronic switching but it's done by the series pass MOSFET that we've got in here but we've basically got a big Schottky diode in there.

**Dave Jones:** There we go. We've got some Schottky diode protection across the output as you typically find. Then we've got a couple of MOVs here going to mains earth here. And remember, this output is not mains earth reference.

**Dave Jones:** It's actually floating. So, these things are going to uh chassis earth ground. And then, we've got a another couple of MOVs on our high side current sense resistor here.

**Dave Jones:** So, there's our high side current sense resistor. We saw that uh close up. The traces go off there to There's our high side current amp. They've rubbed the number off that, the bastards.

**Dave Jones:** But, and of course, the output of uh that will be tied into the constant current uh circuitry, which then controls the gate. So, that'll all be uh analog loop stuff going on in there.

**Dave Jones:** And then, we've got a bleeder resistor across here. That's that one down in there. There we go. It's a fairly uh large one. And then, we've got another bleeder resistor across the um filter caps.

**Dave Jones:** There our main three filter caps up here. There they all are. Boom boom boom. Uh they're 2,200 mic each. Uh 63 V. And we'll measure some uh We'll get the scope out, and we'll actually measure some things on here and have a look at the gate waveform there.

**Dave Jones:** But, uh and basically, the input here um as I mentioned in the uh teardown, that they actually Well, I mentioned that there were triacs in there, but I didn't mention that they're actually switching the secondary uh taps on the transformer here.

**Dave Jones:** The transformer taps coming in here. And there are two triacs in there. There are two triac uh drivers down in there as we saw in the teardown. But, that's what they're using instead of uh more traditional relays uh to select the secondary taps because uh yeah, because this is a linear supply, you want to you need uh some sort of tap on there.

**Dave Jones:** Imagine you're delivering only 3.3 V out of here, and you're getting, you know, 40 V out of your uh transformer. That's a lot of power to dissipate in your uh linear regulator like that.

**Dave Jones:** In your part series pass transistor to it's called. So, really, you want to choose the uh they've got a couple of selections on those uh taps there. So, that's basically um what they're doing.

**Dave Jones:** There's nothing in here at all. There's no output relay switching to switch when you press that on-off button on the front, all it's doing is just effectively grounding that gate and pulling the output down to zero.

**Dave Jones:** So, it's not actually isolating the um output at all. It's just switching off the output series pass transistor. So, we'll just see where those uh voltage taps actually occur.

**Dave Jones:** You can see I've got the full uh 31 V output voltage. I'm measuring the uh voltage and also looking at the waveform. Uh so, this is identical to that.

**Dave Jones:** You can see the voltage down there, 54. Um we're getting Yeah, basically uh 54 V out of those uh filter caps with 31 V output voltage. Now, I'll lower my uh voltage in 1 V uh output voltage in 1 V increments and see where the tap drops.

**Dave Jones:** And of course, in that you'd normally hear a relay clicking in a regular uh power supply, but this one uses a triac switching. And bingo, there it goes. It looks like it when it goes from 20 21 from 22.

**Dave Jones:** Once we get down to 21, it drops down to 35 V. So, we're getting, you know, a 15 V um uh delta there. So, it's got to dissipate uh 15 V uh best case there.

**Dave Jones:** 14 13 12 11 10. There we go. We've got to drop down to 10 V and then we drop down to our next tap, which is seven about 17 and 1/2 V.

**Dave Jones:** So, there you go. And they will be the two taps. We won't find any more than that because we've only got uh two triacs on these things. And as we saw in the teardown, there is only a single uh TO-220 uh MOSFET in there.

**Dave Jones:** And you know, a lot of people are probably going to argue, "Well, you know, they're 90 W is this particular channel." This is one of the uh 30 V uh 3 amp channel.

**Dave Jones:** So, 90 watts dissipation. Is this enough heat sink and air flow? I don't know. You can try and get the data sheet and stuff like that. But, what we should probably do is measure the temperature on that heat sink at a full 90 watt load and see what it gets to.

**Dave Jones:** Yeah, you know, some designs would actually parallel up the MOSFETs there just to so you're not actually stressing just the one individual MOSFET. You're spreading the power against a couple of them.

**Dave Jones:** But, Rigol, well, now I'm doubting their design decisions after that ridiculous LM317 fiasco. But, anyway, they've Assuming they've done it right, they've determined that, "Well, no, we can get away with a single MOSFET on there." So, anyway, let's let let load it down and see if we can measure temperature on this thing somehow.

**Dave Jones:** But, yeah, there's no real easy way for me to stick my thermocouple on that and get a really good connection, I'm afraid. And just as we saw in the review, it can't actually deliver the full 90 watts on that channel.

**Dave Jones:** But, I was able to just, you know, shut the voltage down. I was able to get, you know, 85. It can do a couple of watts more than that.

**Dave Jones:** But, let's just That'll do. 85 watts output. So, I'm drawing 85 watts. I've got the lid kind of sort of closed. So, we're getting an extra air flow over the top instead of through here.

**Dave Jones:** But, it's going to be, you know, it's going to be reasonably close. And I am probing the main filter cap as well. And as you can see there, we got 10 volts per division.

**Dave Jones:** 10, 20, 30, 40. So, you know, 46 volts minimum. Plenty of margin in there for the ripple. And some initial probing of the heat sink there, it's at least to 45 degrees.

**Dave Jones:** So, you know, as I said, it is quite difficult. I'm not going to get in there and actually, you know, I can't really probe the MOSFET itself. It's getting up there, but I wouldn't call that particularly hot.

**Dave Jones:** And of course, the you probably can't hear it, but the fan actually has turned on louder. And we have been able to hit 70 there, so there you go.

**Dave Jones:** I don't know. You know, I'm not going to go into the full thermal calculations, but that you know, that's not too bad. That's what you'd expect really, you know, that's a ballpark of what you'd expect for a full load on this thing.

**Dave Jones:** So, you know, not a problem. And I just took that back out and with no air flow, there you go, it's jumped up to 84. It's a bit hot, but you know, there's no air flow, so you'd expect it.

**Dave Jones:** Okay, I'll have a quick probe of the gate of the series pass MOSFET there. And as I said, that actually controls switches the output off and on and we'll actually see that here.

**Dave Jones:** What I've got dual channels here. Channel one, which is the yellow waveform, is the gate voltage there where it 5 volts per division on both channels. So, 5 10 15 20 25 30 30 volts output by the way, set 30 volts there.

**Dave Jones:** The output is actually switched on at the moment and as you can see, if you switch it off, up, run it. There we go. We can see our output and channel two is our output waveform.

**Dave Jones:** So, our output voltage. So, we're smack on 30 volts there. And if we just single shot capture that, bang, there we go. We can see the rise there. It's got some little something happening down there.

**Dave Jones:** I'm not sure what, but anyway, that's still there's no overshoot on that output at all. It's ramping up. The output ramps up to 30 volts and of course, directly controlled from the gate voltage.

**Dave Jones:** So, if you actually bring that up, you'll find that those two waveforms are virtually perfectly superimposed there because there's you know, there's nothing else switching the output. It's just that actual gate series pass transistor via the gate there.

**Dave Jones:** And I'm afraid I'm no real closer to that uh, turn on uh, glitch when you actually power the thing on. So, I don't know. That was the aim of this when I started this uh, yesterday was maybe to get down into that detail, but who cares now?

**Dave Jones:** I mean, we've got that show stopper which is the bloody LM317. And here's another thing, the LM317 they're using, check out the ridiculously thin tab on that. That is just well, that is really piss ant thin tab ones.

**Dave Jones:** Absolutely horrible. And you can see the difference on these two devices over here. Whereas this has got like a normal thickness tab on it. That's what a, you know, a proper well-designed TO220.

**Dave Jones:** These ones are little piss ant thin tabs on them. Look hopeless. So, that LM317, I mean, you've just got less thermal mass right there. And for the record, that looks to be an ST brand 301 LM317T.

**Dave Jones:** And when I check the data sheet for the ST brand LM317, and just like all the others, you know, maximum junction operating temperature is, you know, around about that 125° C mark.

**Dave Jones:** And we found we've, you know, proven by measurement and based on the data sheet values, the junction to case and that sort of stuff that they're operating above that.

**Dave Jones:** They're operating above the recommended junction temperature. It's just It's just complete fail right there. So, there's something I wasn't expecting when I started probing this thing yesterday. I noticed an issue where it would reset.

**Dave Jones:** I tracked it down to a bloody overheating piss poor designed 5-V regulator for the main logic. Can you believe it? Bloody ridiculous. I'm pissed off. This is a huge serious design oversight.

**Dave Jones:** No one in their right mind would deliberately design a little LM317 with that piss ant heating to run at five bloody watts and think that you can get away with it right next to the output filter caps.

**Dave Jones:** These power supplies are going to fail in the field, no doubt about it. Probably even see the resetting feature I had or in a couple of years time those caps are going to dry out.

**Dave Jones:** It's just absolutely shocking how this thing even made it past the bloody design review meeting, let alone into production, let alone into people's hands. How many months has this thing been on uh sale for now?

**Dave Jones:** And well, yeah, okay, nobody's found it. Okay, maybe a few units, I don't know, it might have experienced issues that that we haven't heard of, but this is a huge, very serious design oversight and Rigol need to explain what the hell happened here.

**Dave Jones:** And I don't think they can explain this away. How? Like, you know, apart from we missed it or we swept it under the somebody found it and they'll told to "Oh, it's not a problem.

**Dave Jones:** Shut up. Go back to your bench." you know? And it's ridiculous. A hundred plus degrees C on a on a you know, on a regulator? And it's just quiescent static current driving the thing as measured by multiple people through the case with the proper airflow.

**Dave Jones:** Yeah, they'll probably do like a firmware upgrade. Oh, we can fix that firmware upgrade. Make the fan run all the time. God, man, unbelievable. And there's probably going to be some people who will say, "Well, what's the problem, right?

**Dave Jones:** Nobody's had an I Look, it just reset it again." Oh, bloody hell. Uh people are going to a few people say, "Oh, you know, Rigol might even say, 'Oh, had no problems in the field, no returned units.'" That's beside the point.

**Dave Jones:** The point is is that this is has no design margin in it whatsoever. You mount this thing in a bloody rack, right? Sits in a rack, your ambient goes up by 20 or 30 degrees Celsius, you're just going to be screwed.

**Dave Jones:** Those regulators are going to shut down. You you know, who knows what regulator, what the thermal cutout is in that particular type of regulator. You got variations in your junction to case.

**Dave Jones:** I don't even think Yeah, they put some heat sink in there. There's going to be variations in that. There's going to be variations in the airflow on the fan.

**Dave Jones:** Huge variations. Going to be variations in the life of those caps and all sorts of stuff. It's just it It's just bad engineering. It's not going to work. Needs to be fixed.

**Dave Jones:** Anyway, Rygo, explain because this power supply now gets a huge thumbs down until this problem is fixed. I think it needs to be fixed before you sell any more of these bloody things.

**Dave Jones:** Unbelievable. What can you do? Well, you know, it's tempting to sort of move that 5-V reg over to you know, an existing heat sink on here, but then you break your isolation stuff between your isolated 5-V power to digital and your output.

**Dave Jones:** So, that's not really going to work. Might You've got There's a couple of mounting holes in there. They probably could solve it by manufacturing some sort of custom heat sink or something which goes in there.

**Dave Jones:** And yeah, that'll probably be a fix. Maybe, you know, that Well, it probably would be a half reasonable fix if they up the size of that heat sink by you know, four or five times or something like that.

**Dave Jones:** But, it definitely involves something custom. Other than that, it probably have to relay out the board or something like that. This is clearly unacceptable. Anyway, let's see. I'll definitely let Rygo know about this and let's see we hear back from him cuz this is just complete utter Catch you next time.
