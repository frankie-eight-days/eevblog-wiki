---
video_id: gEDs0OtOkGE
title: EEVblog #835 - Wekomm Resistance Standard Part 2
url: https://www.youtube.com/watch?v=gEDs0OtOkGE
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 24, "3": 32, "4": 48, "5": 74, "6": 90, "7": 114, "8": 135, "9": 150, "10": 170, "11": 183, "12": 190, "13": 200, "14": 210, "15": 223, "16": 232, "17": 242, "18": 255, "19": 263, "20": 279, "21": 296, "22": 304, "23": 316, "24": 325, "25": 341, "26": 354, "27": 365, "28": 385, "29": 397, "30": 416, "31": 432, "32": 442, "33": 462, "34": 474, "35": 490, "36": 498, "37": 518, "38": 534, "39": 545, "40": 556, "41": 564, "42": 574, "43": 585, "44": 610, "45": 630, "46": 639, "47": 660, "48": 673, "49": 695, "50": 704, "51": 718, "52": 729, "53": 740, "54": 758, "55": 769, "56": 786, "57": 797, "58": 812, "59": 825, "60": 842, "61": 854, "62": 862, "63": 878, "64": 899, "65": 907, "66": 928, "67": 934, "68": 945, "69": 961, "70": 979, "71": 991, "72": 1003, "73": 1013, "74": 1036, "75": 1044, "76": 1057, "77": 1069, "78": 1087, "79": 1102, "80": 1123, "81": 1142, "82": 1152, "83": 1168, "84": 1176}
---

**Dave Jones:** Hi, in a previous video, you saw me have a little play around with a Weinschel 10K laboratory resistance transfer standard that I've got hooked up to my Keithley DMM 7510 multimeter here.

**Dave Jones:** I was just having a play around and we noticed some drift in the reading up here and I said I'd do a second video where I'd actually put the resistance standard inside my thermal chamber here and that's what I've done overnight.

**Dave Jones:** So, let's take a look at what I got when I came in this morning. Now, if you haven't watched the previous videos, I won't go through the data again, so this won't might not make much sense.

**Dave Jones:** So, click here and watch that one first before we continue. Let's go. Okay, so basically nothing has changed in the setup here except I've put my Weinschel resistance standard inside my thermal chamber here.

**Dave Jones:** I've set it to 20°. It shows 19° up there, but I've actually got my thermometer here. It's currently at well, 19.8, 19.6, something like that. So, it's been like that overnight and I've basically just been continuously recording here, although there was a where I disconnected the thing so I could put it through the port on the side here and yes, as is standard industry practice for thermal chambers,

**Dave Jones:** I've plugged it up with a rag. Beauty, works every time, no worries. So, yeah, it's there was a little glitch in there when I disconnected, but I've continued the data cuz I thought that might be valuable rather than just start it again and look for stability because we've already got that you know, a previous history.

**Dave Jones:** I wanted to carry on from the previous video. So, let's take a look at the data. Now, the data we got previously showed a 0.0000600 difference between what the resistor data sheet here tells us or what the resistor calibration sheet told us and what we actually measured on the meter here.

**Dave Jones:** And my guess was that that point 0000600k discrepancy was coming from the actual Keithley multimeter itself up here. And we had a look at the specs for that and it seemed the temperature coefficient for this meter on its resistance range and that you know, it seemed to be accountable.

**Dave Jones:** In fact, the data sheet value of 2.5 ppm per degree C for a 4 degree C difference we're looking at actually seemed to be larger. So, it seemed you know, it just as a rough order seemed to be better than the spec.

**Dave Jones:** But the spec of this meter could certainly account for that. Hence why today I've actually got the resistance standard in the thermal chamber so that we can ensure that the resistance standard stays at a constant temperature and the only thing I'm going to change now is the temperature of this meter by changing my air con here in the lab.

**Dave Jones:** So, at the moment I'll show you what we did last night. This is where I started last night basically and see that big dip in there, that was when I actually disconnected the contact.

**Dave Jones:** So, it's good that it didn't actually give a reading outside of that. I really like that and like mess up your data. Although it does show a little tiny red dot in there.

**Dave Jones:** I'm not sure if you can see that but it that indicates that I guess there was an error condition. Like it actually went open because we're using four terminal resistance measurement here.

**Dave Jones:** Anyway, look, the first thing you notice is you get we get a hell of a lot more noise on here. Look at that to what we got previously and that's not surprising.

**Dave Jones:** We've got this thermal chamber which uses a DC to DC converter in it to drive the Peltier device to you know, keep it stable temperature and we've got unshielded shouldn't touch them unshielded test leads on here.

**Dave Jones:** You know, so it's not the best setup. So, maybe we should actually turn the filter on for this one because we didn't need it before but now that noise is getting massive.

**Dave Jones:** But anyway, you can see it dropped up here when I um left uh last night. I actually had the air con on. This is when we ramped the air con back up, and we could actually see the difference.

**Dave Jones:** Yeah, we could actually I believed that we could actually see the oscillation of my air con in there. You can see that. Like that. And basically, what I did is I turned the air con off.

**Dave Jones:** I probably Maybe I turned off uh Well, no, probably kept going. Anyway, I turned it off before I went home, okay? So, there's no longer any air con cycling, okay?

**Dave Jones:** But we are getting Look, we are getting some noise. So, you know, that's like periodic noise on there. So, that's rather interesting. So, I don't think that's the Peltier uh device in the chamber switching off and on.

**Dave Jones:** The thermal uh response of the resistance standard wouldn't be anything like that, you know? It wouldn't be anything near that quick. So, uh Yeah, that's probably just, you know, maybe switching crap from the DC to DC converter in the uh thermal chamber.

**Dave Jones:** So, when I went home last night, it was I had the air con on to ramp up like that, and then uh it got to it was about uh 22°.

**Dave Jones:** Uh or thereabouts. Then I went home, turned the air con off, and you can see that we've got a negative temperature coefficient. As the temperature increased, uh we can see the change there.

**Dave Jones:** And it's currently uh 26 uh and 1/2 degrees in here. Let's just call it 26. So, we've got that 4° differential uh that we had before, which is handy.

**Dave Jones:** And uh and once again, the temperature in in the uh resistance standard has been constant, although there might have been a little bit of thermal lag in there um just to bring that up to uh temperature, but you know, still it stayed stable all overnight.

**Dave Jones:** So, uh really, the only change would be due to the meter here, the Keithley meter. So, we're because we in the previous video, we suspected this meter had a negative temperature coefficient.

**Dave Jones:** The data sheet doesn't tell you that, it just says plus minus, right? It doesn't tell you what the actual temperature coefficient is. So, but we realized it must have been negative.

**Dave Jones:** That was our theory anyway. So, that was our hypothesis. And so, it's going negative like this, exactly what we expected. So, let's get the difference there and there and see get the values and see if it's equal to that point double O double O 600 K discrepancy that we got last time.

**Dave Jones:** And we can do that by going into our reading table here. So, I'll read off that figure point 10.000 say 40 and then we'll get this value at the end here.

**Dave Jones:** And right at the end there, we're getting basically point 9.99998. Oh, you know, 81, something like that, 82. So, last time we had that discrepancy, as I said, of the meter minus what we got from the resistor cal sheet here.

**Dave Jones:** And we had a point double O double O 600 basically difference there. So, we had that discrepancy, which our hypothesis was that it was caused by the temperature coefficient of the Keithley multimeter.

**Dave Jones:** And what did we get when we only change the temperature of the Keithley multimeter? Ta-da! A difference, a delta of point double O double O 59. Let's call it 60.

**Dave Jones:** We see the exact almost practically the exact difference there. And we're not even using a really you know, decent, you know, like really controlled proper setup here. Yet, we were able to can basically confirm the difference between these two.

**Dave Jones:** Neat. Beauty, huh? So, what we're going to try and do now is I'll turn the air con back on, okay? Of course, our temperature chamber is going to stay exactly the same temperature.

**Dave Jones:** It's not, you know, it can easily uh you know, cater for external slow external temperature changes caused by the air con. No worries. So, our resistance standard is going to stay at our constant temperature, which is uh currently Come on.

**Dave Jones:** You can do it. You know, 20 odd degrees. It you know, it's going to cycle, you know, maybe half a degree around that or something like that. So, there's not much in that.

**Dave Jones:** And I'll put turn the air con back on. It is currently uh 26 odd degrees. And I'll I think I'll turn some filtering on just so that we get a filtered uh signal there cuz that's too much noise anyway because we now um have confirmed that this thing has a negative temperature coefficient.

**Dave Jones:** If we drop the temperature back down to 22, then we expect this to rise up. Let's see if we get it. Actually, I could have sworn I had the filter turned off, but I actually have the filter turned on with the 10 power line cycles.

**Dave Jones:** Oh, jeez. Anyway, so it looks like we're not going to filter that any better, and I don't want to go touching the uh setup and you know, shielding the leads and doing everything else.

**Dave Jones:** So, you know, uh let's just go back to the uh graph and uh just simply turn the air con on. Anyway, we can see even though we've got a lot of noise there now, we can see we should be able to see that change.

**Dave Jones:** So, I expect that now to start ramping back up. I'll give it an hour and or two and we'll come back. And I think as we saw in the previous video, I've just started.

**Dave Jones:** It's been like 5 10 minutes or something. Just started turning on the air con. And it's Of course, you'd expect it to go immediately up in value because the temperature's coming down, right?

**Dave Jones:** The air con's I've measured the temperature, you know, at the vent it's pumping out like, you know, 13-14°C air, right? So, you'd expect it to go immediately up, but it doesn't.

**Dave Jones:** It looks like it it just like it's not the correct term, but it's sort of like undershoots like that, and then it's going to go back. Now, I suspect that's because of the uh control loop for the uh reference inside the Keithley meter actually trying to, you know, either the thermal uh response of the uh you know, the the the heater in there for the uh reference or, you know,

**Dave Jones:** however they've got that uh control loop set up. So, that's probably a response from that, and you know, it'd be nice if we had a nice noise-free, you know, you could do it better if we actually uh put had the meter in a thermal chamber, everything else, and we're just measuring a fixed resistor with no noise or whatever, you know, you'd be able to see that, but you can actually see that

**Dave Jones:** dip go down, and now it'll you can actually see it it's starting to head back up, and I believe over the next hour or so it'll shoot right back up.

**Dave Jones:** So, that's rather interesting that we can actually see that. And it's another 5 minutes later or something, and you can see it is actually uh heading up there, and of course, we've already hit uh you know, near our 22 uh degrees there, so because the ambient air is just circulating around, but it hasn't immediately uh shot back up because there is going to be some thermal lag

**Dave Jones:** for the uh for the air to actually get in through, you know, the vent holes, and this thing's, you know, hot inside, and and it's got its own thermal characteristics inside, so it's going to take some time for this thing to actually ramp back up.

**Dave Jones:** Okay, it's been an hour or so, and yep, you can see that we're getting basically the same ramp we got here, not quite as big or uh instant because well, we're you know, we've got that extra noise on there now, and I guess the uh uh, resistor wasn't uh adding on because it is a quarter of the value that we had uh, before.

**Dave Jones:** So, now we haven't got that. So, but it's slowly ramping up as you can see and it'll most likely get back to that average value that we saw there.

**Dave Jones:** Absolutely no doubt. And yes, I have been monitoring the uh, temperature inside this thing and inside the thermal chamber and uh, it has been, you know, stuck around 20 plus minus uh, 0.5.

**Dave Jones:** So, the thermal chamber was doing the business and keeping that uh, even though the air kind of ramped down by 4° cuz it's 22° in here now. Uh, the resistance standard stayed at that temperature.

**Dave Jones:** So, what we're seeing there is just the Keithley meter. And here you go, you can see that we've actually uh, flattened out and we haven't quite come back to the peak there.

**Dave Jones:** If we have a look, we've come back to uh, is that is that straight? There we go. We've come almost almost pretty darn close to it. But of course, as I said, um, there would have been some uh, settling there of the uh, resistor in the thermal chamber as well.

**Dave Jones:** So, you know, maybe that that sort of exact in quote marks figure we got of 0.0000 uh, 600 that difference we measured. It might be, you know, it's going to be slightly out perhaps.

**Dave Jones:** But anyway, you can see that it has recovered there. So, no problems whatsoever. Look at that. So, this uh, Keithley um, DMM 7510 on the resistance uh, range has a negative temperature coefficient and it matters.

**Dave Jones:** You can actually see it in the data, which is really really interesting. But look at that. Look at that cycling there. There is definitely definitely cycling in that. Wow.

**Dave Jones:** Have to get a time period on that. You can see that's uh, actually 200 seconds or thereabouts uh, per division. So, it's nice that it actually tells you that.

**Dave Jones:** And we're looking at basically one cycle, you know, around about uh just over two divisions there. May a bit more like it. I think it actually varies. It's going to vary a bit.

**Dave Jones:** But that's you know, let's say you know, 400 to 500 seconds per cycle. So, it might be tempting to think that this is that this is the cycle of the air con cuz it does seem to match the time period of the air con cycling off and on.

**Dave Jones:** But it's not. I've actually switched the air con off at the moment. So, there is no that you know, cycle of plus minus half degree air actually you know, doing anything.

**Dave Jones:** So, what I'm going to do now is just last thing is just turn the thermal chamber off and I won't open it. I'll just turn it off and see what happens.

**Dave Jones:** And there we have it. I switched off completely and disconnected the mains power cord from our thermal chamber. I haven't opened it so the temperature hasn't changed. So, it looks like well, you know, you could say that that's a temperature cycle change with inside the thermal chamber.

**Dave Jones:** But I don't necessarily hear it actually you know, changing that quick. Although you know, it could be. But as I showed in the previous video inside the thermal resistance chamber it has a high you know, like it's going to have a very big thermal lag.

**Dave Jones:** So, I'd be very surprised if it could actually change that quickly. Although it it possibly could. So, we might be able to see a smaller term change I e.

**Dave Jones:** that one quarter which we're looking at before. I'm not going to go any further in this and uh muck around with it. But suffice it to say that that switching does certainly come from the thermal chamber.

**Dave Jones:** So, there you go. I hope you found that video rather interesting. It just started out as a quick thing. I wasn't even going to make a video on it.

**Dave Jones:** I just wanted to, you know, plug that reference in overnight and see what happened. But, it's turned into a two-part video. Getting a, you know, a fair bit of data here.

**Dave Jones:** But, it's interesting to note that that Keithley meter we've proven actually has a negative temperature coefficient, substantial one or one that's, you know, it's still within spec. Everything we're seeing here is still within spec of the instrument.

**Dave Jones:** But, because we're measuring right down in the noise, we can actually see the changes in the temperature coefficient. So, it's rather interesting. We can see the thermal lag in there as well, you know, so of the Keithley instrument and the reference heater and other things inside.

**Dave Jones:** We can see that little um undershoot there. And, it's, you know, thermal response of the reference. It's all It's all rather interesting stuff. And, this was pretty much a hacked-together test as I went along.

**Dave Jones:** I didn't, you know, really design it from the start to make, you know, to do a proper test. But, we were still able to get some real numbers out of that that actually matched up.

**Dave Jones:** Fascinating stuff. So, if you like that, please give it a big thumbs up. It's another 20 minutes of waffle. Anyway, I think some people might really find that rather fascinating.

**Dave Jones:** And, if you've got, you know, a decent meter with this sort of resolution, you can, you know, do and play around with that test like this. Of course, you know, like all you need to do is put like a resistor short, you know, straight in the input terminals, for example, or a battery voltage, you know, just to hook a battery straight up to it, you know, so you don't get noise

**Dave Jones:** and everything with the cables and test system and all that sort of jazz. So, you know, and you can eliminate noise and you can actually start seeing drift in your actual meter.

**Dave Jones:** So, you know, it's it's handy to know when you're doing precision measurements like this. You can't just magically take the meter and you know, oh, it's within spec, you know, plus minus 5°.

**Dave Jones:** Outside that, okay, but within plus minus 5° of the temperature was calibrated that it's spot-on. Well, no, the things drift all the time. So, there you go. Hope you enjoyed it.

**Dave Jones:** Catch you next time. Just a very quick follow-up. I left this running over Christmas time. It's now Boxing Day. I came back and inside the chamber I switched it off 25 and 1/2° and inside the lab here, I haven't been to the lab for like, you know, day and a half, 2 days or whatever.

**Dave Jones:** So, if 25 odd degrees and this is the response I got over that time. So, the air con is definitely off. Everything's switched off and there we go, but it's fascinating.

**Dave Jones:** You can see that's reached a new low down here where it's, you know, it hasn't really increased in temperature much since here, but yeah, like it's, you know, it's been tracking there because that's been the temperature here in like the building and, you know, the corridor it seeps in through the roof, the walls, everything else.

**Dave Jones:** So, I've had some slight temperature variations here, but looks like it's reaching a new low there and this brings up interesting things in, you know, long-term trend plotting. We could maybe, you know, plot this thing for 2 weeks in a temperature chamber and stable and everything else and we might see some drift and, you know, things like that.

**Dave Jones:** It might, you know, settle down and, you know, all that sort of jazz. When you're talking about the the precision, the resolution we're looking at here and, you know, all the little subtle things matter.

**Dave Jones:** And long-term aging and and drift and other, you know, there could even be some sort of, you know, quantum effects in the reference or whatever, you know, like weird, you know, physical phenomenon at play.

**Dave Jones:** And you know, it could be fascinating stuff if you leave it for weeks and months and you know, some people leave them for years to see the long-term drift in things.

**Dave Jones:** And it can be absolutely fascinating. So, there you go. I wonder where it's going to go, but yeah, I think I'm going to call it quits now.
