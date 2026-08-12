---
video_id: Sf0RyRZAuqk
title: EEVblog 1751 - Oscilloscope Phase Measurement Masterclass
url: https://www.youtube.com/watch?v=Sf0RyRZAuqk
source: youtube-asr
timestamps: {"0": 0, "1": 22, "2": 34, "3": 50, "4": 63, "5": 81, "6": 105, "7": 119, "8": 129, "9": 143, "10": 154, "11": 169, "12": 183, "13": 192, "14": 206, "15": 223, "16": 234, "17": 253, "18": 263, "19": 277, "20": 289, "21": 303, "22": 320, "23": 335, "24": 350, "25": 366, "26": 376, "27": 394, "28": 406, "29": 417, "30": 430, "31": 448, "32": 459, "33": 471, "34": 488, "35": 498, "36": 511, "37": 524, "38": 535, "39": 547, "40": 565, "41": 576, "42": 595, "43": 607, "44": 616, "45": 629, "46": 646, "47": 664, "48": 681, "49": 696, "50": 708, "51": 722, "52": 732, "53": 747, "54": 758, "55": 768, "56": 794, "57": 804, "58": 816, "59": 827, "60": 838, "61": 851, "62": 873, "63": 885, "64": 905, "65": 915, "66": 923, "67": 937, "68": 949, "69": 959, "70": 970, "71": 990, "72": 1006, "73": 1018, "74": 1034, "75": 1050, "76": 1069, "77": 1078, "78": 1094, "79": 1107, "80": 1120, "81": 1132, "82": 1150, "83": 1171, "84": 1184, "85": 1198, "86": 1223, "87": 1233, "88": 1254, "89": 1269, "90": 1287, "91": 1298, "92": 1314, "93": 1323, "94": 1339, "95": 1348, "96": 1369, "97": 1382, "98": 1395, "99": 1405, "100": 1420}
---

**Dave Jones:** Hi, we've got another viewer question. Thank you very much Phase 303 on X or /Twitter, whichever you want to call it, who asked the question, "Can I show him how to actually measure the phase difference between two sine waves using a Rigol DHO 800 series oscilloscope?" We certainly can do that.

**Dave Jones:** It's rather interesting. There's several ways to do it, so let's take a look at it. So, you can see here we've got two sine waves. The yellow is channel one, blue is channel two here, and you can see that there is a phase difference between them.

**Dave Jones:** The phase difference is defined as the difference in degrees. A 360° will be one full cycle. So, the difference in degrees between the two waveforms at the same reference location.

**Dave Jones:** So, it could be the zero crossing point like here, for example, because our zero point is literally right there. So, that's our zero crossing point, or it could be the top or the bottom, the falling edge, rising edge.

**Dave Jones:** It doesn't have to be a sine wave, could be a square wave, for example, or triangle wave, whatever waveform it is. So, let's take that full cycle there. So, just by eyeballing this with your mark one eyeball, you'll go, "Okay, well, you know, if that's 360°, then that's about, I don't know, 1/10 of that, maybe." But anyway, let's get the exact figure from our generator.

**Dave Jones:** I've got a generator over here. Channel one is our reference here. It's at 0° because you have to have a reference somewhere, but it's all relative, and I've set it to 33°, and yeah, it seems to be about, you know, that 30°ish, but we want to measure it precisely because we've got the measurement tool for doing this, an oscilloscope.

**Dave Jones:** So, let's get to it. Now, there's several ways to do this, either manually or automatic. Automatic is going to be the easiest way to do it, and most modern digital scopes will have the ability for you to automatically measure phase difference between channels.

**Dave Jones:** So, what we have to do is we have to go up into measurements up here and then where in vertical measurements it's got nothing to do with the vertical the voltage of the measurement.

**Dave Jones:** So, we want to go into horizontal over here and we want to have a look at the features for the horizontal and really you know, we can measure the frequency the period the rise fall time the width and the duty cycle and all that sort of stuff.

**Dave Jones:** But there's no relative measurements between two waveforms over there. So, what we want to do is we want to go over to other and aha and here's where we could do it.

**Dave Jones:** It's got four different types of delay measurements and four different types of phase measurements here and the phase measurement is the one that we want cuz it'll give us a number in degrees out of the 360 as we said before over the full cycle.

**Dave Jones:** The delay will give us essentially the same value but in a different units of time i.e. seconds microseconds milliseconds nanoseconds whatever it is. But usually when you're talking about phase you're talking about in degrees.

**Dave Jones:** So, what are these four different measurements? What does R to R R to F and F to R and F to F mean? Well, R and F mean rising and falling.

**Dave Jones:** So, it's the rising and falling edge of the waveforms. So, it just gives you different options there between different points on the waveform. So, whoop a bit tricky to get rid of that.

**Dave Jones:** So, this is considered a rising edge like this because it's going upwards. So, these are both rising edges. So, if we wanted to measure that difference in there which is what we do want to happen do want to measure here then we want rising edge to rising edge or R to R of those two waveforms.

**Dave Jones:** But if you wanted the rising edge of this one to the falling edge of the yellow one then you could do that as well. but that depends on the circumstances that you want to measure.

**Dave Jones:** So, let's go back in there and we'll go into other and we will if the bloody touchscreen works. There we go. It's touchy. I'm here all week. So, we want phase R to R like that and bingo, it's going to add a measurement over here on the side.

**Dave Jones:** So, you notice that it's not showing any value over there. That's because we didn't set it up properly before we hit it. A source A is chat So, they're both channel two.

**Dave Jones:** So, we want the source to be channel one and that to be channel two. So, we add that there and boom, there's our 33 degrees. We'll just get rid of the other one we had before.

**Dave Jones:** That's dodgy. We can remove that and bingo, we've got our automatic measurement and sure enough, there it is, 32 33 degrees. It's updating like crazy, but we can actually expand that and get statistics in here.

**Dave Jones:** And you'll notice that how many counts it's actually getting these um average values over. So, 33.1 degrees. There you go, fantastic. And you'll notice if I change the time base, that count will reset like that.

**Dave Jones:** There you go. Or if I change the vertical scale, for example, it will reset those statistics there. So, that's easy peasy lemon squeezy, but Dave, what happens if your oscilloscope doesn't have this fancy pantsy new um phase measurement capability like this?

**Dave Jones:** Well, there's ways to do it manually. Old school. And just so there's no confusion over which two points it's measuring, we can actually go in there and we can actually turn on the indicator and that will actually track uh these particular measurements.

**Dave Jones:** So, if I change it on my function generator, for example, you'll see it, it'll change in real time like that. Beauty. But uh if you want the a proper average value, you see that the average value is lagging behind, we'll have to just reset those uh stats there.

**Dave Jones:** And if you've got a tricky waveform or something, you can actually go into the settings here, and you can actually uh like fiddle around with the uh threshold uh values here and stuff like that, but we won't go into that uh for this video.

**Dave Jones:** So, but if you've got a more complex waveform you're looking to get, and it can't quite do the automated uh measurement, then you might have to play around with uh uh amplitude thresholds.

**Dave Jones:** But basically, you should just be able to uh have that on auto for, you know, most general waveforms. And you can even get fancier by saying, "Oh, okay, I want to actually do manual measurements into the zoomed-in uh version of the waveform and things like that." But, you know, most of the time you won't have to do that.

**Dave Jones:** Well, that uh zoom thing might come in handy soon. So, there's other ways we can do this. We can go older school, not quite old old school. We'll show you that at the end.

**Dave Jones:** But, uh the next way you can do this is with uh cursors. So, you can turn cursors on, and you can see that we've got horizontal cursors like this, and we've got vertical cursors like this.

**Dave Jones:** Well, we don't need to dick around with the vertical cursors. Now, this oscilloscope, unfortunately, doesn't have uh give us the ability to actually measure a uh a cursor delta, it's called, the difference between the two cursors in a uh in actual degrees.

**Dave Jones:** So, we can't get a direct phase reading. So, we're going to have to work out the time for the full cycle. So, we're going to have to go back to measurements over here, and then we're going to have to go back into horizontal, and then we're going to have to do the period here, and we're going to add a period there.

**Dave Jones:** And because it's a 1 kHz waveform we're talking about here, it's basically bang on 1 ms there. But, you need to know that before you can actually do the calculations with these cursors.

**Dave Jones:** But, just be aware that some scopes might have more advanced cursor capabilities. You might be able to set a reference and then get a phase difference and different units and things like that.

**Dave Jones:** So, but this one, you know, it's an entry-level scope. It's already got ridiculous amount of measurement capability built in, but it's not that good. So, what we want to do is move these cursors to our reference point, which we'll just say is the zero line there cuz you've got to choose a reference.

**Dave Jones:** As I said, doesn't matter where you do it. So, we can use the cursors with the touch screen, or we can actually move them. And at the moment, they're actually tracking like that.

**Dave Jones:** But, we don't want them to track. So, we're just going to ignore these vertical cursors here, and we're going to move our horizontal cursors like this. And we could sort of like guesstimate it down in there like that.

**Dave Jones:** But, we'd like a bit more resolution. So, there's two methods you can do to get more vertical resolution. One is to increase your scale like this. Okay? So, we can see that they didn't track there.

**Dave Jones:** So, we can see, okay, that's about the point where it crosses that zero line. And that one's, you know, it's it's near enough, good enough for Australia. There it is about there.

**Dave Jones:** But, because the slope of this waveform is like it's a bit how you doing. When it goes across, it's really hard to see where it crosses that line. We can actually increase the vertical resolution here.

**Dave Jones:** We can actually use our vertical control to increase them like this. Just go way off like that. And bingo, we can actually get Look at that. We can actually now see much better where it actually crosses that zero point line.

**Dave Jones:** And you can see that we had it. We had it pretty close. Anyway, if I hold my tongue at the right angle, get the cursor set up, I think that's where it crosses the zero Oh, that one's a bit off.

**Dave Jones:** So, we can even expand that further and then we can use our horizontal position to bring it over here and then bring our cursors even finer like that. So, you can use your horizontal and your vertical main controls to get a bit more resolution out of this sucker.

**Dave Jones:** So, there you go. Right, what value have we got? So, what we're looking for is the delta or difference between those two X cursors. So, that would be delta X there.

**Dave Jones:** That's what that triangle symbol That's actually the symbol delta. So, 95 microseconds. So, you remember before how I told you that we needed that period down here. It's gone.

**Dave Jones:** It's vanished. It's less than one femtosecond. That's femtosecond, right? Because it's off the screen. We don't have the full waveform on there. But, you just remember from before it was 1 ms.

**Dave Jones:** So, now get our confuser out here. 95 microseconds, okay, divided by the 1 ms that we had for the entire period, okay? And that gives us 0.095, but we want to get that in degrees.

**Dave Jones:** So, we multiply that by 360° and that gives us uh 34.2. I still have it set to 33 on my generator, so it's not as precise as we'll get in with that automated measurement.

**Dave Jones:** Maybe I'm slightly off on my cursor. Yeah, I think we're down in the resolution of what we can do with our delta cursor measurement there. So, it's not going to be as accurate as our automated measurement, unfortunately, but you know, it's going to be close enough.

**Dave Jones:** Good enough for Australia. And now, is it positive 33° or negative 33°? Well, our channel two waveform, the blue waveform, is leading, what's called leading, the channel one waveform here because it comes before it.

**Dave Jones:** So, it's leading it and that's why if we have a look on our generator over here, we can see that we're positive 33° and that means I'm setting that for channel two here.

**Dave Jones:** Sorry, it's it's confusingly yellow, which actually goes into the blue over here. So, yeah, sorry about that. So, that's positive 33° on the channel two signal relative to the channel one.

**Dave Jones:** So, when you say it's positive, that means it's leading. It comes first. So, zero and then one degree and then 10 degrees and 20 degrees and 33° over here.

**Dave Jones:** If it was minus, then it'd be minus. It'd be lagging the channel one waveform. So, minus 33 would put it on the other side. But Dave, I'm running an old school analog oscilloscope.

**Dave Jones:** Couldn't be bothered getting my analog oscilloscope output. It doesn't have cursors. Some of the Some of the good analog oscilloscopes have cursors, but what happens if you didn't have a cursor?

**Dave Jones:** Well, you've got that's where your graticule, these grid lines on your scope for. Sorry, they're quite hard to see. Maybe I can turn off my lights. So, we look at our horizontal time base, 20 microseconds per division, okay?

**Dave Jones:** And then we just count the divisions. So, it's kind of like just before a smidge before that vertical graticule there. So, that's 20 40 60 80. Oh, then you got to fiddle around with it and yeah, maybe we're about that 95 microseconds that we'll get in before.

**Dave Jones:** So, once again, you know, we're only going to get, you know, 34°. So, we could be like a percent out there compared to our 33° that we'll get in over here.

**Dave Jones:** But so, anyway, that's how you do a phase measurement on an oscilloscope. Automated, if your scope's got that feature, is the best way to do it. You're just going to get the most accurate number, and it just puts it there for you.

**Dave Jones:** So, we just go into our measurements here, and and we can do I can show you like we can do rising to rising edge, and then falling to falling edge.

**Dave Jones:** It should make no difference. They're exactly the same because the rising and falling edge of these two waveforms bloody shut down. But, you'll notice one thing, which is a trap for young players.

**Dave Jones:** Once again, it's all relative. You'll notice that it's showing minus 33° because we're getting the yellow waveform minus the C2 waveform. So, it's giving us a minus value there.

**Dave Jones:** So, we would if you wanted that to be positive to match So, you'd have to swap if you want that the other way around, you'd have to choose channel two as your source A and channel one as your source B, and then rising edge to rising edge and falling edge to falling edge, and bingo, it's now positive.

**Dave Jones:** So, that's a trap for young players. You have to keep your brain engaged when you're actually doing these measurements to make sure you actually get the sign correct. You have to know which one is relative and which one is leading and lagging, etc.

**Dave Jones:** So, yeah, little trap for young players there. So, another way to use the graticule system without actually having to like count them is to use single shot sampling. So, let's let's go vertical again on these so that we get a nice vertical resolution on there.

**Dave Jones:** Let's go out like this, and we've got our trigger point right in smack in the middle there, and our horizontal so we actually can reset those. So, we reset our horizontal position.

**Dave Jones:** Like, we can move our position like that, but we want to reset it, and then we want to reset our trigger level smack in the middle like that. No worries.

**Dave Jones:** And then you can actually move your cursor position, and you'll notice that we're getting the figure up there that where we've moved it from, and that center point of the screen was our reference.

**Dave Jones:** So, we can just move that over there like that, and bingo, 94.4. But, you'll notice that the resolution jumps 0.2. That's the best resolution we've got at the moment.

**Dave Jones:** And of course, you can single shot capture this too if you have to. So, you can see how we're only getting a 0.2 microsecond resolution there when we shift that.

**Dave Jones:** So, to increase that resolution, what we can do is we can get it so that both of these are on screen. If no, that's not I'm going to have to go down to time base like that.

**Dave Jones:** Okay? And then we can single shot capture that. Okay? And then if we center it like that where it's zero there, and then we can just bring this over, and instead of just measuring it like that and get our point, you know, be happy with our 0.2 microseconds, we can increase our time base like that.

**Dave Jones:** And go in there, and you'll see that now it's finer. So, we've got 94. So, what's that jump in at 0.08? I think. Yeah, 0.08 microseconds there. So, we can actually get just a finer resolution there.

**Dave Jones:** But, you can see that we're kind of getting towards like the sampling uh limit here cuz we're only 10K points memory. So, we got the extra little resolution, but you know, it's it's good enough.

**Dave Jones:** But, if you really want to increase your chances, you can actually change your sample rate here. Let's go in there, and let's go to our full 10 meg of memory like that, and we can now single shot capture that again, and you can see that we've got more data in there.

**Dave Jones:** It's more better, huh? And we're now point 04 point Yeah, point 04. It's jumping in resolution there. So, that's just a way to get a slightly finer or greater resolution measurement there like that.

**Dave Jones:** And that's 94.32 microseconds. And we can take that figure and we get like 33.9. So, we can actually get a little bit more equal bit more resolution out of it there by single shot capturing expanding it and then shifting the waveform over and then choosing a reference point.

**Dave Jones:** It's easy just to get the you know, the center of the screen. And yeah, you can get a bit better that way, but but here you're saying, "Dave, those four or five ways isn't enough.

**Dave Jones:** I need another way to do it." Okay, there is another way to do it. Once again, a very old school stuff. Let's go in here and we can go into XY mode and we can get ourselves a listen what's called a Lissajous figure.

**Dave Jones:** Pronounce that three times quickly. So, what is XY mode? Well, it's a little bit deceiving because our channels channel one is actually also called the X channel and channel two is called the Y channel.

**Dave Jones:** And you might be able to set that up you know, on your scope for which channels it's using, but let's just go with that. So, it's plotting the voltage on channel one on the X axis and the voltage on the Y axis is the voltage on channel two.

**Dave Jones:** And for two sine waves that are offset like this, we get an ellipse. So, I'll demonstrate this. I'll call my measurements back up here. So, let's Sorry, I can't actually float that measurement out.

**Dave Jones:** So, and I don't want to get rid of the sine wave screen over here. So, we're going to have to live with that. So, let me adjust the phase angle and you'll see that as I'm adjusting it, it gets once if I go down to a phase angle of zero Well, that is zero.

**Dave Jones:** We get a straight line like that. Both waveforms match perfectly like that, so we get a straight angled line. But, the more that we go out, and you guessed it, if we go up to all the way up to 90° 70, 80, and 90°, we get a perfect circle there.

**Dave Jones:** And as we increase at 100°, we go the opposite direction. And if we go 180 right up to 180°, and whoop whoop, there it is there. Perfect straight line like that.

**Dave Jones:** And then we can go beyond 180° of course, and it's just going to go backwards like that. Cool, huh? So, you can also technically use this display to actually measure your angle.

**Dave Jones:** Calculating the phase angle from this Lissajous figure is a little bit tricky, but we should be able to in theory do it. So, if we call up our cursors, at the moment our cursors are only working on the time display over here, but if we go in there and we go into the settings, we can actually set that to XY mode, and now our cursors are available on our XY

**Dave Jones:** display over here. So, I'll just get rid of that waveform so that we get our Lissajous figure full screen like this. All right, so let me just move those horizontal cursors out of there cuz we don't need those.

**Dave Jones:** We're going to focus on our vertical cursors. So, what we want to do is move our cursor here until the point where it intersects that Y axis there at that point, and then the other cursor we want to put at the maximum amplitude there of our the ellipse there.

**Dave Jones:** So, oval circle, whichever it happens to be. So, we can calculate out our angle with voltages here, and this is really cool. So, Um the Y value here is 1.062.

**Dave Jones:** So, 1.062 V and then we divide that by the maximum value up here, which is 2.046 V. That's the AY figure divided by 2.046 V and that gives us a value of .51 and then we want to do arc sine.

**Dave Jones:** So, it's that sine -1 there on your calculator. You might never have used it. But if we use that, boom, that is our phaser. That happens to be our phase angle.

**Dave Jones:** It's a little bit off because our resolution's not great, but it's there. And then if I wind this up to 90°, okay, and it's perfect like that, then the both values are the same, 2.046.

**Dave Jones:** Like it intersects at 2.046 and the maximum value is 2.046, which is you divide those two figures, it's just one. And then if you've got one and then you do your arc sine like that.

**Dave Jones:** You've got to be in degrees mode, of course. Bingo, there's our 90° and we're we have a 90° phase difference between these two. So, it works. Magic. And for those wondering, yes, I was just using XY mode for funsies there.

**Dave Jones:** You can actually do this on the regular time display as well. When you've got your waveform centered like this, you just take your the channel that you want to measure there.

**Dave Jones:** So, the Y cursor there is 1.055 V. You divide that by the maximum value up there, which is BY, which is 2.102 equals that. Shift arc sine and bingo, 30.12°.

**Dave Jones:** Not quite the 33°, but you know, good enough for Australia. And because like we don't have the actual the measurement resolution there, I'll leave it up to you experiment at home how you can get better resolution on that.

**Dave Jones:** But cool, huh? You can get arc sign of voltage levels to actually measure your phase angle. Neat. So, there you have it. There's just like half a dozen different ways to use your oscilloscope to measure phase between two waveforms.

**Dave Jones:** So, thank you very much for that question. Very interesting. If you want to send me questions, you can always tag me on X or {slash} Twitter, depends what you want to call it.

**Dave Jones:** Anyway, if you like that video, please give it a big thumbs up and as always discuss down below. And if you want to get yourself some top quality multimeter merch, head on over to evblog.store down below and that's the best way to support the channel as well as, you know, liking, subscribing.

**Dave Jones:** Oh, almost at a million subscribers. Maybe might get this year in there this year. Maybe. I don't know. Catch you next time. >> [music]
