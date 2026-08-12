---
video_id: 07VkEUUd0eo
title: EEVblog #845 - Oscilloscope FFT Comparison
url: https://www.youtube.com/watch?v=07VkEUUd0eo
source: youtube-asr
timestamps: {"0": 2, "1": 9, "2": 29, "3": 41, "4": 50, "5": 64, "6": 88, "7": 106, "8": 116, "9": 123, "10": 137, "11": 161, "12": 170, "13": 179, "14": 192, "15": 203, "16": 223, "17": 237, "18": 253, "19": 264, "20": 275, "21": 288, "22": 300, "23": 312, "24": 336, "25": 349, "26": 360, "27": 376, "28": 390, "29": 401, "30": 413, "31": 426, "32": 443, "33": 458, "34": 469, "35": 479, "36": 492, "37": 505, "38": 524, "39": 534, "40": 550, "41": 560, "42": 572, "43": 589, "44": 605, "45": 616, "46": 644, "47": 657, "48": 678, "49": 693, "50": 709, "51": 723, "52": 732, "53": 750, "54": 762, "55": 782, "56": 798, "57": 815, "58": 828, "59": 836, "60": 851, "61": 872, "62": 883, "63": 900, "64": 917, "65": 926, "66": 937, "67": 952, "68": 965, "69": 982, "70": 1002, "71": 1015, "72": 1024, "73": 1042, "74": 1055, "75": 1065, "76": 1081, "77": 1099, "78": 1110, "79": 1128, "80": 1144, "81": 1159, "82": 1170, "83": 1183, "84": 1197, "85": 1209, "86": 1222, "87": 1241, "88": 1249, "89": 1273, "90": 1283, "91": 1297, "92": 1308, "93": 1318, "94": 1335, "95": 1345, "96": 1361, "97": 1378, "98": 1394, "99": 1406, "100": 1418, "101": 1427, "102": 1441, "103": 1456, "104": 1463, "105": 1479, "106": 1488, "107": 1499, "108": 1517, "109": 1527, "110": 1539, "111": 1551, "112": 1565, "113": 1578, "114": 1597, "115": 1607, "116": 1623, "117": 1633, "118": 1654, "119": 1670, "120": 1683, "121": 1706, "122": 1717, "123": 1738, "124": 1749, "125": 1764, "126": 1775, "127": 1794, "128": 1802, "129": 1816, "130": 1831, "131": 1851, "132": 1866, "133": 1878, "134": 1892, "135": 1908, "136": 1920, "137": 1940, "138": 1960, "139": 1976, "140": 1990, "141": 2001, "142": 2011, "143": 2025, "144": 2041, "145": 2057, "146": 2069, "147": 2081, "148": 2090, "149": 2104, "150": 2117, "151": 2132, "152": 2142, "153": 2153, "154": 2168, "155": 2178, "156": 2193, "157": 2202}
---

**Dave Jones:** Hi, it's just an ordinary day in the EVblog lab here. I've got five oscilloscopes, a spectrum analyzer, and a function generator. What are we going to do with these?

**Dave Jones:** Well, have some fun, of course. Let's go. Now, I recently took a look at this Rohde & Schwarz HMO 1202 series scope, and I noted that it had a really good FFT mode, and actually a quite large number of FFT points as well, 128K points, which is a a little bit on the unusual.

**Dave Jones:** Yeah, it's well, it's on the high end side for these scopes, and somebody asked, "Well, can I compare it with some other scopes and see what it's like?" So, that's what I've done here.

**Dave Jones:** I've set it up, and what we're comparing what we're going to have a look at is the Rohde & Schwarz compared to the Rigol DS 1000Z, which everyone's familiar with.

**Dave Jones:** I'll put in the 2000Z as well, but I believe there's actually no difference. Oh, sorry, the 2000 DS2000. I believe there's no difference. We've got the Teledyne LeCroy WaveJet Touch here.

**Dave Jones:** We've got the GW Instek GDS1104B. We've got the Keysight MSO-X 3000 series touch, the new touch model. So, let's have a look at the different FFT modes and see which one has the best FFT mode, and we'll just compare it to spectrum analyzer here, the good old Rigol DSA815, bottom of the range spectrum analyzer, but gives us a baseline.

**Dave Jones:** So, I've got my Siglent True Arb function gen here, and I've got it set up for an FM signal. So, with a carrier frequency of 1 MHz here, with an FM frequency of 5 kHz, and a frequency deviation of 500 Hz.

**Dave Jones:** And if we have a look at that on our Rigol DSA815, it's a bottom of the range spectrum analyzer, but it does the job. So, this is a real RS spectrum analyzer.

**Dave Jones:** It it gets in there and sweeps the frequency across, none of this digital FFT rubbish. And we're getting exactly what we expect here. Here's our carrier frequency bang on 1 MHz.

**Dave Jones:** We've got a span of uh 50 kHz there, so that's 5 kHz uh per division. So, you can see our um frequency modulation there and there. And we're getting tiny little ones over here, as well.

**Dave Jones:** Uh they're just uh some harmonics of our 5 kHz there. And let's have a look at what the same signal we get on the various scopes. Now, how the FFT mode or fast Fourier transform mode on a typical uh scope works is that it takes your regular input signal here, and here's our signal like this, and we can see uh if we uh whoop, go in here,

**Dave Jones:** and that not used to all these different scopes that I've got. Anyway, we can see there's our waveform in there. It's a little bit crusty, isn't it? Hm, bit of distortion.

**Dave Jones:** Anyway, doesn't matter. Um it's real See, and you can slightly see the little modulation on there. Maybe you can see it a little bit of little bit of shimmy in there.

**Dave Jones:** So, that's our modulation. So, uh what it's doing is when we turn on FFT mode, it'll actually uh compute the fast Fourier transform of this, and then we can uh just go in there and zoom in.

**Dave Jones:** But, the FFT depends upon uh many different things. It depends on the sample memory of the scope, how deep a memory you've got. It depends on the sample rate uh you're using.

**Dave Jones:** It depends on your current uh horizontal time base setting. And uh most importantly, it uh depends upon the number of FFT points. And this Rohde & Schwarz one is unique in not only that it has a high number of FFT points, it has a 128 uh K points, but you can actually select it, as well.

**Dave Jones:** And that's really good, and we'll have a look at the effect of that uh in a minute. But, that effectively uh what that does, the number of points, is basically the frequency resolution for each individual pixel in there.

**Dave Jones:** It's got to calculate like a frequency bin, for want of a better term. It's got to calculate each individual point, and there's a lot of processing involved in this, and to do actually 128 K points FFT requires a lot of processing grunt.

**Dave Jones:** So, typically, it might be done in an FPGA or an ASIC. When you do it on like a regular Joe Blog's on processor or something, it's going to probably, you know, grind to a halt.

**Dave Jones:** But, yeah, we can actually select that. So, you can see that when we drop down in that, it just gets coarser and coarser, and of course it gets faster because it's able to calculate the fast Fourier transform faster.

**Dave Jones:** Now, it does the FFT using a DFT or a discrete Fourier transform, and depends and depending upon the manufacturer you get, they might implement that DFT in different ways.

**Dave Jones:** So, ultimately, what the oscilloscope is doing with the FFT function is it's converting the your time domain waveform here and doing a discrete Fourier transform on it and actually converting it into the frequency domain.

**Dave Jones:** So, now on the X axis, we've got frequency and amplitude on the Y, just like we had before, except we're at DB scale, of course. And we can actually show you that.

**Dave Jones:** There we go. If we just put voltage like that, no good. You've got to have it on DB because we're talking about quite large relative magnitudes there. So, of course, the FFT converts your oscilloscope into a rudimentary spectrum analyzer, but depending on how well they've implemented that FFT, how many FFT points has it got like this one, and how well it actually does everything, determines how useful it is.

**Dave Jones:** And as you can see, this Rohde & Schwarz one, excellent. It's got 128 K points FFT and it allows us to get excellent resolution. You can see our carrier in there.

**Dave Jones:** You can see our frequency modulation. And also, if your scope has got the high resolution mode as well, you can whack that on and you'll notice that the noise floor will drop a bit.

**Dave Jones:** It'll be a bit better. It has to recalculate that. Thinking, thinking, thinking, but there you go. It's a little It's a little bit better. Little bit better. And also, what the number of points does here is it actually effectively lowers your noise floor.

**Dave Jones:** So, it there could be like details hidden down in there that we can't actually see, for example. So, if I lower the number of points, we'll see that this side band component here might eventually vanish cuz the noise floor is effectively going to lift.

**Dave Jones:** And I should be able to show that if I scroll like a right down to a small center frequency just so that it's always going to be on the screen where it does the minimum 2048 points now.

**Dave Jones:** And just watch where this noise level is. And you'll see it slowly drop just each time I increment the number of points there. You'll notice that it slowly slowly drop.

**Dave Jones:** And you'll see all the way up. There we go. So, that is like a significant difference. And of course, if you do averaging and all sorts of other you know, stuff, you can really bring signals out of the noise.

**Dave Jones:** And here's a shot from an Infineon application note where it's showing the difference between like a a small number of FFT points and like millions of FFT points. You can see really how all the signals come right out of the noise.

**Dave Jones:** So, if we have our maximum number of points here, 130 128k, and then we go into our acquire menu. We're just in regular refresh mode at the moment. But if we actually go into average mode, for example, we can actually watch the noise floor drop.

**Dave Jones:** Here we go. There we go. It drops a little bit and brings out a bit more signal to noise there. So, there you go. It makes a difference. There we go.

**Dave Jones:** You can see it at two averages. And tweak it up. All right, let's go for broke. And then we can really go to town. We've got our average in on 512 averages.

**Dave Jones:** Thank you very much. But, then we can also turn on our high-resolution mode and wait for it. Oh, look at that. Beautiful. This is excellent. It's doing a really good job.

**Dave Jones:** And the other thing I like about it is when you turn FFT mode on, right? We're in our time base here. When you turn FFT mode on, you don't have to go around with the menus or the select button.

**Dave Jones:** What it does is it now enables your time per division to work like this on your FFT. Like this. Absolutely fantastic. So, you can do that and then the position the horizontal position control now works that and it just makes it incredibly, incredibly simple to use and intuitive to use.

**Dave Jones:** It's fantastic. Of course, but if you want to go back to and adjust the time base, you've got to actually switch the FFT off and then now we go back in and we work on our time base again like that.

**Dave Jones:** But, yeah, it's just so intuitive. Let me show you one that's not intuitive. And here we have the GW Instek GDS 1104B. Now, this thing actually claims to be the duck's guts in terms of FFT.

**Dave Jones:** It claims one claims it can do a one meg point FFT. And well, I it's doing a lot because look, check it out. I think it it probably is doing it.

**Dave Jones:** So, it must have some real grunty hardware in there doing a one meg point FFT. It's absolutely incredible. But, as you can see, we've got our carrier, we've got our FM modulation and of course that component down there as well.

**Dave Jones:** So, it's just as good if not better, than the Rohde & Schwarz one, but uh just try and use this thing. Right, the horizontal time base still works on the um time domain up here, okay?

**Dave Jones:** So, it's like that, right? So, my horizontal time base is still there. Where's the Let's go back to here, okay? But now well, this is fairly typical of scopes, but look how we have to dick around, okay?

**Dave Jones:** I've got to use the uh the variable knob here, okay? I've got to select which one I want, right? Either my uh horizontal per division or uh my center point, okay?

**Dave Jones:** So, now I can actually vary my center point, but when that varies depending upon the setting of the horizontal per division, so if you want to go all the way in well, uh all the way out, sorry, and then scroll across, you've got to dick around with that, and then you can maybe move this across, and it's just a lot lot of around, and trust me, when you're trying to set the damn thing

**Dave Jones:** up for the first time, and it's jerky, of course, because it's got to do all the FFT uh processing in the background, and it's just it it is really horrible to use, absolutely awful, but it ultimately can do the business.

**Dave Jones:** And by the way, both uh scopes have been set to uh the Hanning window here. You've got various different rectangular, Hamming, don't get confused between two, and good old Blackman or Blackman-Harris, and uh so, we've got that set to the uh same I've got it set to Hanning, as I did on the Rohde & Schwarz one, cuz that actually will make a difference.

**Dave Jones:** You'll see it. There we go, rectangular. Let's I won't go into details of how all these various modes work and things like that, but um but it's just when you're comparing them, it's just important to use the same window in technique.

**Dave Jones:** And And I've also got both scopes set to what 1 meg point sample memory and they're both working at 50 meg samples per second here 1 meg points as you can see same time base setting so it just allows us to get you know do decent comparisons.

**Dave Jones:** And the third cab off the rank here is the Keysight MSOX 3000 and this one I really like it works really well. It's got a dedicated FFT button goes straight in and you can actually do FFT and another math function at the same time.

**Dave Jones:** And by the way, it's the only one that allowed me to actually turn off visually the actual channel cuz like it's hard to see it when you you know when you've got your time signal on there.

**Dave Jones:** So you know it just that's just a nice touch. Anyway, once again, I can't set the memory depth with the Keysight because it it's purely automatic but you know, it's doing it's doing its deep memory of business and as you can see it's doing it perfectly well.

**Dave Jones:** The Keysight has a rated 64k FFT points. So not quite as good as the Rohde & Schwarz not nearly as good as the GW Instek but as you can see does a pretty damn good job of it.

**Dave Jones:** But unlike the Rohde & Schwarz this one is also requires you to dick around with the menus down here to actually set your your center and your span. But the good news is is that you can actually because this is the new touchscreen scope you can actually type in exactly what you want.

**Dave Jones:** So you know, but it's not nearly as fiddly as the GW Instek. So it works you know, it works fairly well. And the Keysight also has much better velocity control here and it doesn't slow down based on the FFT or anything like that.

**Dave Jones:** So we can keep our span at a low value and then we can actually go look we can go away. We just jumped right up to 24.5 gig. Right, it has a hell of a hell of a velocity control, but it it really is implemented beautifully.

**Dave Jones:** So, the what we had to dick around was so painful, you want to rip your hair out on the GW Instek, we can easily come to 1 MHz. It's almost as quick to use the knob as it is to type it in really.

**Dave Jones:** I'm not I'm trying to talk at the same time. I'm not really concentrating, but yeah, you know, you can really zoom you know, narrow in straight on that. It is very nice.

**Dave Jones:** So, yeah, thumbs up to that. Now, the Teledyne LeCroy WaveJet Touch 354, well, just like the Keysight, this one also allows us to turn off the time domain waveform as well.

**Dave Jones:** Excellent. But, this thing has a rated 8K points FFT. So, but look, I mean, this is it is horrendously bad. It is awful. This is the absolute best I can get it around trying to get all the settings right and everything else.

**Dave Jones:** This is the best I can get like I can't even I don't even know what's going on with the noise floor down here. I can't I do anything. Look, it looks like dick and balls.

**Dave Jones:** That's what it looks like. And there's only a small selection of FFT windows here. Very confusingly, Von Hann, that's actually another name for Hannan. So, it does have it, but yeah, like I I don't I don't think I've ever seen it called Von Hannan on any other scope.

**Dave Jones:** Anyway, yeah, that's all you get, but jeez, like it's just hopeless. But, it kind of sort of there, but but it does have a dedicated math control here and allows us to change the offset there.

**Dave Jones:** And the other good thing is is that the horizontal control does actually become the span for the thing. So, just like it did on the Rigol Schwarz, so thumbs up there.

**Dave Jones:** But, apart from that, it is useless. I mean, this is I mean, around this I got 1 meg point memory on this thing and like this is the best I can get.

**Dave Jones:** It's just it's so rudimentary it almost doesn't work. But, anyway, I'll show you one that's even worse. And sorry to all you Rigol DS1054Z fanboys out there. Um yeah, these low-end scopes just do not cut it.

**Dave Jones:** This is the absolute best you can get with one of these low-end Rigols. It's so how low is it? Well, it doesn't even tell you how many points it can do in FFT mode.

**Dave Jones:** It's It's not many, clearly. So, this is the most optimum setting I can get, 20 microseconds per division and you know, it's like that is by tweaking this thing, getting the optimum settings for everything, that's the best it can do.

**Dave Jones:** It's just it's no good at all. I mean, yeah, you can see a carrier, but nothing else. Now, I'll just show you how here how the horizontal time base, which is up here, 20 microseconds per division, affects our ability to set a center frequency and our span as well.

**Dave Jones:** So, right, I've got let's say center frequency, right? That's as high as it high as it goes, okay? Absolute maximum, our span is as high as it goes. There we go, go down to 25 kHz up to 250 kHz.

**Dave Jones:** That's at 20 microseconds per division and yes, you can see like it's now got the full range, okay? Over there, so our our span is 250 kHz per division.

**Dave Jones:** So, 500 1 meg, so there's our 1 meg carrier, which we want to measure, so we can actually go in there and see it, okay? But, now I'll change my horizontal time base to 50 microseconds and you can see that it's dropped down.

**Dave Jones:** Once again, this is the absolute maximum we can do here. We can only do 100 kHz per division. Can't do anything more. You'll notice that we're set to 1.2 meg points here.

**Dave Jones:** It just cannot It's got a very low number of FFT points. So it can't use all of that sample data. And that's one of the keys with having a high number of FFT points.

**Dave Jones:** No point having 150 million gigabytes of sample memory if your FFT algorithm it just can't use it. So yeah, so our signal is way outside the range here. So we can obviously can't select that time base setting, okay?

**Dave Jones:** And if we go worse, we can only go to 800 kHz, okay? So we've got it So the absolute best range that we can get where we're going to get the most resolution out of this thing is at 20 microseconds per division because anything uh faster let me go to 10, okay?

**Dave Jones:** Or you know, let's let's go down to one for example. You know, look Right, we're at 5 MHz per division, okay? We're going to get no resolution in there at all.

**Dave Jones:** So the absolute best when you're mucking around trying to get the best FFT possible on your scope, you've got to do this. Find where your I'm tweak, sorry, the horizontal I'm not showing on the screen here, but So that is the absolute best we can do.

**Dave Jones:** So we want to go center. We want to go 1 MHz. And boop boop boop boop Right, and then we want to change our span like that and bingo, that is the absolute best we can do on this thing.

**Dave Jones:** The absolute best. So as you can see it's best ain't good enough. So while these modern low-end digital scopes are absolutely thoroughly impressive value for money, it's got more bells and whistles you can poke a stick at.

**Dave Jones:** It's got a ton of memory. This thing has like 14 mega standard. I think it has when you if you buy the option at Oh, I've got a dicky.

**Dave Jones:** I think I've got a dicky T piece there. I think I do. Uh anyway, you get these things impressive amount of memory. It works great in the time domain, everything else, but the FFT on it is almost like a toy.

**Dave Jones:** And we'll see if the Rigol DS 2200 is any different. We're at 50 microseconds per division, which wouldn't work before, and sure enough, it doesn't work here either. Look, we'll change it down to 20 microseconds per division.

**Dave Jones:** Bingo, we've now got our FFT, and we can maybe zoom in on that and have a squeeze. But the good thing about the Rigols is that yes, once you're in math mode, the horizontal actually does that.

**Dave Jones:** And if you just press channel one, bingo, you can go back, and that changes your time domain, and you press math again, and bingo, you're in you can actually adjust that, and then your time base can be used to zoom in.

**Dave Jones:** So, jazzy jazzy, okay, but What what what what? Thanks for playing. That is no good at all. Woo! Jumping around like a jackrabbit. There we go, center one meg, we're at uh 10 dB uh per division.

**Dave Jones:** Maybe we can change that. Hang on. No, how do we uh How do we adjust? Oh, that's right, we've got to go in here, and we've got to go like that, and then select.

**Dave Jones:** Now we're at 20 dB per division like we were on the other ones. Oh, goodness. around, around. There we go. Yep. No good at all. Not actually sure why it's jumping around like a jack rabbit on that 20 microseconds like we're triggering smack in the middle there.

**Dave Jones:** Nothing wrong there. And then there if we go to 10 microseconds per division on our time domain, then it doesn't jump around anymore and we got similar to what we saw on the Rigol 1000Z.

**Dave Jones:** But yeah, see it's it's pretty much just a toy. You can see that something's there and that might be good enough for a lot of uses, but to analyze something like this FM modulator signal you know like use it more like a real spectrum analyzer, it's no good at all.

**Dave Jones:** Now, if we go back to our Rigol and Schwarz here, it's a good example because it allows us to change the number of FFT points, which is absolutely beautiful.

**Dave Jones:** And you'll notice that if we change Okay, we're at our maximum 128K points, change it to 64K points and you'll notice that it's halved. Like that look at the it it has stopped here.

**Dave Jones:** Okay, and the center is at 833 kHz. That's why there's no signal anymore cuz our 1 MHz is out here like this. Okay? So, using this particular time base of 5 ms here, sorry for the big fat finger in the way.

**Dave Jones:** I should use my poker. 5 ms per division and at 65K points, we can't get that. So, we're going to have to go basically turn this is where it becomes a bit annoying.

**Dave Jones:** Let's go down back to 2 ms per division here and turn the FFT back on and you'll notice that we will hopefully get it. There we go. Now with our 65K points, we can actually go in there and see that.

**Dave Jones:** But it all depends on the upon the time base. So, yep, we're at the center now and bingo, we can go in like that and see it. But of course, if we change our if we don't have enough data there, let's go down to say an order magnitude lower, 200 microseconds per division.

**Dave Jones:** Turn our FFT back on and look, we can't get See, the resolution in there is no good, okay? Cuz we're calculating even though we're still calculating a massive 65 thousand um FFT points in there, i.e.

**Dave Jones:** frequency bins, it still isn't enough. We cannot zoom in any further on that, and you'll notice that it has now given us a much greater frequency range. Our Our span is now 100 Look at this.

**Dave Jones:** Yeah, it's like 25 MHz span there. It's absolutely enormous. Good thing about this is that if you want to see a bit more, I can just turn that menu off there.

**Dave Jones:** That's quite jazzy. But, you can see how it's all a big trade-off in terms of, you know, getting the right uh A, you've got to have the right memory depth set.

**Dave Jones:** That's not going to work. You've got to have the right time base setting. You've got to have Well, you know, generally if your scope can do, um you know, allows you to change the number of points like this, then you set it to, you know, maximum unless you want really fast updating.

**Dave Jones:** So, if I now set it to 8K points FFT, same as what we had on that crappy Teledyne LeCroy, look, you can see that it's giving us, you know, like that is a similar sort of result at that particular time base.

**Dave Jones:** Let's see if we can tweak that. So, if we turn off FFT, let's give us a bit more. Let's go up to 1 ms. Can we get 1 ms worth?

**Dave Jones:** Nope, because it only gives us our um Sorry, our span 500 kHz, not good enough. So, the best time base we can do is 500 microseconds. There we go, 500 microseconds per division, and now we can zoom in.

**Dave Jones:** But, you know, at least it is doing a better job than that Teledyne LeCroy. You can actually see the separate signal components there. You know, it it's fairly clean.

**Dave Jones:** And, of course, as I said, you know, if we go into the acquire menu, high high resolution maybe maybe we can clean that up a little bit there. but we can certainly go in there and see these things.

**Dave Jones:** And with this Rohde & Schwarz, the measurements on the Rohde & Schwarz are really quite nice. I've showed the quick view thing, but if you go into which uh and auto measure, which doesn't work in FFT mode sadly, but if you go like if you turn the cursors on, next peak, previous peak works an absolute treat.

**Dave Jones:** Look at that. So, I hope you can start to appreciate the huge trade-offs in terms of sample rate, time base, setting number of FFT points, the higher the better.

**Dave Jones:** You know, it's worth paying for if FFT functionality is something that you want in a scope because, you know, you could end up with a toy like those Rigol scopes, and you know, it's really no good.

**Dave Jones:** So, there you have it. There's a little look at the FFT modes on five different scopes here. No, I didn't I deliberately didn't use the Tektronix MDO 3000 scope cuz it's got a built-in hardware spectrum analyzer.

**Dave Jones:** So, you know, I I guess I could get the FFT mode out and try that just for kicks, shall we? Yeah, yeah, why not? Anyway, I'll do that after this, but as you can see, I love this Rohde & Schwarz.

**Dave Jones:** Works really, really well. It's got a large number of FFT points, and it's functional, it's usability, functionality, the auto setup on the FFT gets you in the ballpark, and it just really is quite a nice scope.

**Dave Jones:** Of course, the the Keysight, which which is advertised as having a specific Well, this new touch model, specific FFT functionality, can do gated FFT. It's extremely powerful, which the Rohde & Schwarz can't do any of that.

**Dave Jones:** So, it's in terms of FFT, the best is the Keysight MSOX 3000 in this bunch by far, but you know, the Rohde & Schwarz does a really good job.

**Dave Jones:** The Rigol the Rigols are a toy, you know, as are most low-end scopes. The GW Instek, very nice, very impressive at 1 meg point FFT, but the usability on it is just pretty atrocious.

**Dave Jones:** But ultimately, it does the job. So, you know, hey, you got to give it a thumbs up for that. And the Teledyne LeCroy here is a is a joke, the Dick and Balls model.

**Dave Jones:** Yeah, don't like that at all. Hmm. Um that's not good. Pair on self-test failed. What? What? There are persistent power please qualified. Unbelievable. Um well, I've got my signals connected in, but surely that shouldn't make a difference.

**Dave Jones:** That is greatly disturbing. Hmm. Now, if we have a look at this on the Tektronix MDO 3000 scope here, this is not the FFT, this is using the analog RF front end because it's a mixed domain oscilloscope.

**Dave Jones:** Does actually have an RF spectrum analyzer built in. Albeit, it's a digital sampling-based system, so it does actually do an FFT approach, but it actually has, you know, specific hardware and software to actually do this.

**Dave Jones:** So, it's not a That's why it's it's faster updating, even though this slow scope is generally slow as a wet week, it is much faster updating because it's doing the discrete Fourier transform of the all the FFT of the signal instead of actually doing the sweep-based system, you know, generating a sweep and going across.

**Dave Jones:** Because the Rigol DSA815 to build up the image that we saw before actually takes like 50 seconds, I think, to do an entire sweep cuz I had a low-resolution bandwidth set in and everything else.

**Dave Jones:** But there you go. This gives an excellent result. Check it out. It's performance is better. As we've seen before, performance is better than the entry-level Rigol DSA 815. And as you actually saw before, we've got a modulation index set up here of 0.1.

**Dave Jones:** So, the modulation index is the frequency deviation is the frequency deviation divided by the FM frequency there. So, it's we've got 500 Hz deviation with a 5 kHz FM frequency.

**Dave Jones:** So, I'll just interestingly show you what happens if we take that above one, okay? If we take the modulation index above one, we'll see our carrier actually start to drop.

**Dave Jones:** And as we go up, say to 0.5 or something, we'll actually see more we'll see more tones down here getting smaller and smaller and smaller. So, it's 500 Hz at the moment, okay?

**Dave Jones:** This is 1 kHz. And do we see any? No, not really. Let's take it up to 2 kHz. There we go. Got another See? There we go. They're increasing amplitude, and then we start to see more of them.

**Dave Jones:** If we increase the modulation index, let's go up to five. So, we've got a modulation index of one. So, our frequency deviation is 5 kHz, our FM frequency is 5 kHz.

**Dave Jones:** And look at that. There we go. Beautiful. Now, if we take it above that, so we've got a module I've got now taken up to 10 kHz frequency deviation.

**Dave Jones:** So, we've got a modulation index of two. Bingo, our carrier here has dropped. And let's take it up to 20. So, now you can see the carrier's actually gone back up, and the side first sideband here has dipped back down, and then it goes up again.

**Dave Jones:** And this is all classic textbook stuff for FM frequency analysis theory. So, go look it up if you want, but it works. Excellent. But, if we actually try and do an FFT on our channel one signal here, look, it's got the same annoying thing as the GW Instek.

**Dave Jones:** You got to set, you know, your horizontal controls actually still work on your time domain signal. So, you've got to now dick around with these two multi-purpose controls. I hate having these two separate controls on the MDO 3000.

**Dave Jones:** It's just It's excruciating. Anyway, well, actually in this case it's a bit handier because um this is a good use of the dual knobs, I guess. You don't have to dick around with this.

**Dave Jones:** So, we can actually uh tweak that. You can see how slow this thing is. It's just whoa. You can easily overshoot with this. So, anyway, this thing does have a keypad.

**Dave Jones:** So, actually, we can type it in. Beautiful. Yes, I love things with keypads. Ah. So wonderful. So wonderful. And we want 100 kHz. There we go. We're in like Flynn.

**Dave Jones:** Okay, now I set this to 1 meg point memory. I set it to Hann in window. Here we go, and 1 MHz center with a Well, 100 I sure I It's set It's changed that to 125.

**Dave Jones:** I'm sure I set it to 100. Anyway, um it looks like it needs to It can't 100 kHz. There we go. No, doesn't like that. Anyway, so we need to uh Oh, sorry, but per division.

**Dave Jones:** Okay, so let's go in there and 10 kHz. Ah, it's changed our carrier. 1 MHz. Thank you very much. It didn't It didn't like that, did it? 10 kHz per division.

**Dave Jones:** Oh, no, there we go. 12.5. Okay, now we're in Lake Flynn. Here we go. It's doing the business now, but look, it's not updating. It's not updating. Like you'd expect to see the noise change.

**Dave Jones:** That way, we got one. We got one. Um yeah, this is the MDO 3000 in a nutshell. It is one of the slowest modern scopes I've ever used. I I Well, I think it is the slowest.

**Dave Jones:** It is just horrendous. Um every time you turn something on, it's got very limited processing power in this thing. So, I don't know how many points FFT uh this one actually does in math mode.

**Dave Jones:** I wonder if it's in the manual. Let me go read it. But, let me try and turn the channel off. Can we still do the FFT? I don't know, but anyway, look how sharp this is.

**Dave Jones:** It's absolutely incredible. It must have a massive number of frequency bins, i.e. a massive number of FFT points that it's calculating. This has got it. Yes, it still works, by the way, with the waveform off.

**Dave Jones:** Excellent. So, the Tektronix actually is has got to be the winner in the in this FFT shootout by far. That's got to be equivalent to the million points in the GW Instek, no doubt.

**Dave Jones:** So, no wonder it's as slow as a wet week. Um is that No, it doesn't tell us. We've got 1 meg point as our sample memory, but it doesn't tell us how many uh FFT points it's actually doing, and there's Yeah, there's no indication in there.

**Dave Jones:** All you can tell is by how slow it is. And yes, I just read the manual, and sure enough, this thing has up to 2 meg points FFT. So, absolutely brilliant.

**Dave Jones:** Um yeah, okay. Sorry, Tektronix. No wonder it's uh slow calculating 2 million meg points, but the GW Instek was faster doing a million. It was at more than twice as fast.

**Dave Jones:** So, it is This is still a very slow scope, right? Don't get me wrong, it's a dog, but uh hang on. Why is it now like it's now take Oh, there we go.

**Dave Jones:** Hey, we got one. Um, yeah, it it takes forever. It's still very slow, but it can give you the performance, not that you really need it, because you're going to use the real RS spectrum analyzer, but anyway, this is indicative This should be indicative.

**Dave Jones:** Uh don't quote me, but uh should be indicative of the other uh non-MDO scopes um in uh in Tek's range, cuz basically the MDO is one of their existing series with the RS spectrum analyzer hardware tacked on.

**Dave Jones:** That's basically what it is. Um, so yeah, its performance should be similar. So, absolutely, the MDO is the winner, although I'm not sure if it can do gated, but I think we can Can we do gated on the real RF like we can on the Key site?

**Dave Jones:** I don't know. Anyway, um it it is a winner. So, very, very happy with that. Oh, it can do advanced math. And there we go. That's zoomed in a bit.

**Dave Jones:** That's uh 2.5 kHz per division now. So, check that out. Beautiful result. Absolutely gorgeous. So, there you go. I hope you enjoyed that uh Well, it was supposed to be a quick look.

**Dave Jones:** I always say that, don't I? And then I just waffle on, and yeah, yeah, find extra things to do. Anyway, look at the difference between FFT modes on various scopes, and you can see how some of the entry-level ones are just toys pretty much.

**Dave Jones:** Yeah, you can detect that some carrier's there, but that's about it. You can't see some basic uh FM uh sidebands and things like that. So, um yeah, but I like that little Rohde & Schwarz.

**Dave Jones:** It's a very cute. Look at it. Um, but yeah, the winner um Tektronix, but the Key site one is really awesome as well. GW Instek, lot of points in it, million points, but yeah, it's a bit annoying to use, but ultimately, yes, it does do the business.

**Dave Jones:** So, there you go. Um it was not designed to be a tutorial on FFT tutorial or anything. It was just a comparison of uh all the different scopes, but I hope you liked it.

**Dave Jones:** If you did, please give it a big thumbs up and all that sort of jazz. Catch you next time.
