---
video_id: 07VkEUUd0eo
title: EEVblog #845 - Oscilloscope FFT Comparison
url: https://www.youtube.com/watch?v=07VkEUUd0eo
source: youtube-asr
timestamps: {"0": 2, "1": 32, "2": 58, "3": 96, "4": 113, "5": 135, "6": 166, "7": 195, "8": 227, "9": 258, "10": 287, "11": 312, "12": 346, "13": 360, "14": 392, "15": 418, "16": 451, "17": 468, "18": 487, "19": 505, "20": 534, "21": 560, "22": 596, "23": 630, "24": 663, "25": 693, "26": 709, "27": 723, "28": 737, "29": 770, "30": 803, "31": 831, "32": 854, "33": 881, "34": 917, "35": 947, "36": 982, "37": 1002, "38": 1015, "39": 1036, "40": 1055, "41": 1088, "42": 1121, "43": 1147, "44": 1170, "45": 1190, "46": 1205, "47": 1232, "48": 1258, "49": 1283, "50": 1308, "51": 1335, "52": 1366, "53": 1386, "54": 1420, "55": 1447, "56": 1477, "57": 1503, "58": 1535, "59": 1565, "60": 1597, "61": 1633, "62": 1657, "63": 1673, "64": 1710, "65": 1731, "66": 1760, "67": 1786, "68": 1799, "69": 1816, "70": 1843, "71": 1875, "72": 1896, "73": 1937, "74": 1956, "75": 1973, "76": 2005, "77": 2038, "78": 2072, "79": 2093, "80": 2104, "81": 2135, "82": 2164, "83": 2180, "84": 2196}
---

**Dave Jones:** Hi, it's just an ordinary day in the EVblog lab here. I've got five oscilloscopes, a spectrum analyzer, and a function generator. What are we going to do with these? Well, have some fun, of course. Let's go. Now, I recently took a look at this Rohde & Schwarz HMO 1202 series scope, and I noted that it had a really good FFT mode, and actually a quite large number of FFT points as well, 128K points, which is a a little bit on the unusual. Yeah, it's well, it's on the

**Dave Jones:** high end side for these scopes, and somebody asked, "Well, can I compare it with some other scopes and see what it's like?" So, that's what I've done here. I've set it up, and what we're comparing what we're going to have a look at is the Rohde & Schwarz compared to the Rigol DS 1000Z, which everyone's familiar with. I'll put in the 2000Z as well, but I believe there's actually no difference. Oh, sorry, the 2000 DS2000.

**Dave Jones:** I believe there's no difference. We've got the Teledyne LeCroy WaveJet Touch here. We've got the GW Instek GDS1104B. We've got the Keysight MSO-X 3000 series touch, the new touch model. So, let's have a look at the different FFT modes and see which one has the best FFT mode, and we'll just compare it to spectrum analyzer here, the good old Rigol DSA815, bottom of the range spectrum analyzer, but gives us a baseline. So, I've got my Siglent True Arb function gen here, and I've got it set up for an

**Dave Jones:** FM signal. So, with a carrier frequency of 1 MHz here, with an FM frequency of 5 kHz, and a frequency deviation of 500 Hz. And if we have a look at that on our Rigol DSA815, it's a bottom of the range spectrum analyzer, but it does the job.

**Dave Jones:** So, this is a real RS spectrum analyzer. It it gets in there and sweeps the frequency across, none of this digital FFT rubbish. And we're getting exactly what we expect here. Here's our carrier frequency bang on 1 MHz. We've got a span of uh 50 kHz there, so that's 5 kHz uh per division. So, you can see our um frequency modulation there and there.

**Dave Jones:** And we're getting tiny little ones over here, as well. Uh they're just uh some harmonics of our 5 kHz there. And let's have a look at what the same signal we get on the various scopes. Now, how the FFT mode or fast Fourier transform mode on a typical uh scope works is that it takes your regular input signal here, and here's our signal like this, and we can see uh if we uh whoop, go in here, and that not used to all these different scopes that I've got. Anyway, we can see

**Dave Jones:** there's our waveform in there. It's a little bit crusty, isn't it? Hm, bit of distortion. Anyway, doesn't matter. Um it's real See, and you can slightly see the little modulation on there. Maybe you can see it a little bit of little bit of shimmy in there. So, that's our modulation. So, uh what it's doing is when we turn on FFT mode, it'll actually uh compute the fast Fourier transform of this, and then we can uh just go in there and zoom in. But, the FFT depends

**Dave Jones:** upon uh many different things. It depends on the sample memory of the scope, how deep a memory you've got. It depends on the sample rate uh you're using. It depends on your current uh horizontal time base setting. And uh most importantly, it uh depends upon the number of FFT points. And this Rohde & Schwarz one is unique in not only that it has a high number of FFT points, it has a 128 uh K points, but you can actually select it, as well. And that's really good, and we'll have a look at

**Dave Jones:** the effect of that uh in a minute. But, that effectively uh what that does, the number of points, is basically the frequency resolution for each individual pixel in there. It's got to calculate like a frequency bin, for want of a better term. It's got to calculate each individual point, and there's a lot of processing involved in this, and to do actually 128 K points FFT requires a lot of processing grunt. So, typically, it might be done in an FPGA or an ASIC.

**Dave Jones:** When you do it on like a regular Joe Blog's on processor or something, it's going to probably, you know, grind to a halt. But, yeah, we can actually select that. So, you can see that when we drop down in that, it just gets coarser and coarser, and of course it gets faster because it's able to calculate the fast Fourier transform faster. Now, it does the FFT using a DFT or a discrete Fourier transform, and depends and depending upon the manufacturer you get, they might implement that DFT in

**Dave Jones:** different ways. So, ultimately, what the oscilloscope is doing with the FFT function is it's converting the your time domain waveform here and doing a discrete Fourier transform on it and actually converting it into the frequency domain. So, now on the X axis, we've got frequency and amplitude on the Y, just like we had before, except we're at DB scale, of course. And we can actually show you that.

**Dave Jones:** There we go. If we just put voltage like that, no good. You've got to have it on DB because we're talking about quite large relative magnitudes there. So, of course, the FFT converts your oscilloscope into a rudimentary spectrum analyzer, but depending on how well they've implemented that FFT, how many FFT points has it got like this one, and how well it actually does everything, determines how useful it is. And as you can see, this Rohde & Schwarz one, excellent. It's got 128 K points FFT and

**Dave Jones:** it allows us to get excellent resolution. You can see our carrier in there. You can see our frequency modulation. And also, if your scope has got the high resolution mode as well, you can whack that on and you'll notice that the noise floor will drop a bit.

**Dave Jones:** It'll be a bit better. It has to recalculate that. Thinking, thinking, thinking, but there you go. It's a little It's a little bit better. Little bit better. And also, what the number of points does here is it actually effectively lowers your noise floor. So, it there could be like details hidden down in there that we can't actually see, for example. So, if I lower the number of points, we'll see that this side band component here might eventually vanish cuz the noise floor is effectively going to lift. And I should

**Dave Jones:** be able to show that if I scroll like a right down to a small center frequency just so that it's always going to be on the screen where it does the minimum 2048 points now. And just watch where this noise level is. And you'll see it slowly drop just each time I increment the number of points there. You'll notice that it slowly slowly drop. And you'll see all the way up. There we go.

**Dave Jones:** So, that is like a significant difference. And of course, if you do averaging and all sorts of other you know, stuff, you can really bring signals out of the noise. And here's a shot from an Infineon application note where it's showing the difference between like a a small number of FFT points and like millions of FFT points. You can see really how all the signals come right out of the noise. So, if we have our maximum number of points here, 130 128k, and then we go into our

**Dave Jones:** acquire menu. We're just in regular refresh mode at the moment. But if we actually go into average mode, for example, we can actually watch the noise floor drop. Here we go. There we go. It drops a little bit and brings out a bit more signal to noise there.

**Dave Jones:** So, there you go. It makes a difference. There we go. You can see it at two averages. And tweak it up. All right, let's go for broke. And then we can really go to town. We've got our average in on 512 averages. Thank you very much. But, then we can also turn on our high-resolution mode and wait for it. Oh, look at that.

**Dave Jones:** Beautiful. This is excellent. It's doing a really good job. And the other thing I like about it is when you turn FFT mode on, right? We're in our time base here. When you turn FFT mode on, you don't have to go around with the menus or the select button.

**Dave Jones:** What it does is it now enables your time per division to work like this on your FFT. Like this. Absolutely fantastic. So, you can do that and then the position the horizontal position control now works that and it just makes it incredibly, incredibly simple to use and intuitive to use. It's fantastic. Of course, but if you want to go back to and adjust the time base, you've got to actually switch the FFT off and then now we go back in and we work on our time

**Dave Jones:** base again like that. But, yeah, it's just so intuitive. Let me show you one that's not intuitive. And here we have the GW Instek GDS 1104B. Now, this thing actually claims to be the duck's guts in terms of FFT. It claims one claims it can do a one meg point FFT. And well, I it's doing a lot because look, check it out.

**Dave Jones:** I think it it probably is doing it. So, it must have some real grunty hardware in there doing a one meg point FFT. It's absolutely incredible. But, as you can see, we've got our carrier, we've got our FM modulation and of course that component down there as well. So, it's just as good if not better, than the Rohde & Schwarz one, but uh just try and use this thing. Right, the horizontal time base still works on the um time domain up here, okay? So, it's like that, right? So, my horizontal

**Dave Jones:** time base is still there. Where's the Let's go back to here, okay? But now well, this is fairly typical of scopes, but look how we have to dick around, okay? I've got to use the uh the variable knob here, okay? I've got to select which one I want, right? Either my uh horizontal per division or uh my center point, okay? So, now I can actually vary my center point, but when that varies depending upon the setting of the horizontal per division, so if you want to go all the way in

**Dave Jones:** well, uh all the way out, sorry, and then scroll across, you've got to dick around with that, and then you can maybe move this across, and it's just a lot lot of around, and trust me, when you're trying to set the damn thing up for the first time, and it's jerky, of course, because it's got to do all the FFT uh processing in the background, and it's just it it is really horrible to use, absolutely awful, but it ultimately can do the business. And by the way, both uh scopes have been set to

**Dave Jones:** uh the Hanning window here. You've got various different rectangular, Hamming, don't get confused between two, and good old Blackman or Blackman-Harris, and uh so, we've got that set to the uh same I've got it set to Hanning, as I did on the Rohde & Schwarz one, cuz that actually will make a difference. You'll see it. There we go, rectangular. Let's I won't go into details of how all these various modes work and things like that, but um but it's just when you're comparing them, it's just important to use the

**Dave Jones:** same window in technique. And And I've also got both scopes set to what 1 meg point sample memory and they're both working at 50 meg samples per second here 1 meg points as you can see same time base setting so it just allows us to get you know do decent comparisons.

**Dave Jones:** And the third cab off the rank here is the Keysight MSOX 3000 and this one I really like it works really well. It's got a dedicated FFT button goes straight in and you can actually do FFT and another math function at the same time.

**Dave Jones:** And by the way, it's the only one that allowed me to actually turn off visually the actual channel cuz like it's hard to see it when you you know when you've got your time signal on there. So you know it just that's just a nice touch.

**Dave Jones:** Anyway, once again, I can't set the memory depth with the Keysight because it it's purely automatic but you know, it's doing it's doing its deep memory of business and as you can see it's doing it perfectly well. The Keysight has a rated 64k FFT points. So not quite as good as the Rohde & Schwarz not nearly as good as the GW Instek but as you can see does a pretty damn good job of it. But unlike the Rohde & Schwarz this one is also requires you to dick around with the

**Dave Jones:** menus down here to actually set your your center and your span. But the good news is is that you can actually because this is the new touchscreen scope you can actually type in exactly what you want. So you know, but it's not nearly as fiddly as the GW Instek. So it works you know, it works fairly well. And the Keysight also has much better velocity control here and it doesn't slow down based on the FFT or anything like that. So we can keep our span at a low value and then we can

**Dave Jones:** actually go look we can go away. We just jumped right up to 24.5 gig. Right, it has a hell of a hell of a velocity control, but it it really is implemented beautifully. So, the what we had to dick around was so painful, you want to rip your hair out on the GW Instek, we can easily come to 1 MHz. It's almost as quick to use the knob as it is to type it in really. I'm not I'm trying to talk at the same time. I'm not really

**Dave Jones:** concentrating, but yeah, you know, you can really zoom you know, narrow in straight on that. It is very nice. So, yeah, thumbs up to that. Now, the Teledyne LeCroy WaveJet Touch 354, well, just like the Keysight, this one also allows us to turn off the time domain waveform as well. Excellent.

**Dave Jones:** But, this thing has a rated 8K points FFT. So, but look, I mean, this is it is horrendously bad. It is awful. This is the absolute best I can get it around trying to get all the settings right and everything else. This is the best I can get like I can't even I don't even know what's going on with the noise floor down here. I can't I do anything.

**Dave Jones:** Look, it looks like dick and balls. That's what it looks like. And there's only a small selection of FFT windows here. Very confusingly, Von Hann, that's actually another name for Hannan. So, it does have it, but yeah, like I I don't I don't think I've ever seen it called Von Hannan on any other scope. Anyway, yeah, that's all you get, but jeez, like it's just hopeless. But, it kind of sort of there, but but it does have a dedicated math control here and allows us to change the

**Dave Jones:** offset there. And the other good thing is is that the horizontal control does actually become the span for the thing. So, just like it did on the Rigol Schwarz, so thumbs up there. But, apart from that, it is useless. I mean, this is I mean, around this I got 1 meg point memory on this thing and like this is the best I can get. It's just it's so rudimentary it almost doesn't work. But, anyway, I'll show you one that's even worse. And sorry to all you

**Dave Jones:** Rigol DS1054Z fanboys out there. Um yeah, these low-end scopes just do not cut it. This is the absolute best you can get with one of these low-end Rigols. It's so how low is it? Well, it doesn't even tell you how many points it can do in FFT mode. It's It's not many, clearly. So, this is the most optimum setting I can get, 20 microseconds per division and you know, it's like that is by tweaking this thing, getting the optimum settings for everything, that's the best it can do.

**Dave Jones:** It's just it's no good at all. I mean, yeah, you can see a carrier, but nothing else. Now, I'll just show you how here how the horizontal time base, which is up here, 20 microseconds per division, affects our ability to set a center frequency and our span as well.

**Dave Jones:** So, right, I've got let's say center frequency, right? That's as high as it high as it goes, okay? Absolute maximum, our span is as high as it goes. There we go, go down to 25 kHz up to 250 kHz.

**Dave Jones:** That's at 20 microseconds per division and yes, you can see like it's now got the full range, okay? Over there, so our our span is 250 kHz per division. So, 500 1 meg, so there's our 1 meg carrier, which we want to measure, so we can actually go in there and see it, okay?

**Dave Jones:** But, now I'll change my horizontal time base to 50 microseconds and you can see that it's dropped down. Once again, this is the absolute maximum we can do here. We can only do 100 kHz per division. Can't do anything more. You'll notice that we're set to 1.2 meg points here.

**Dave Jones:** It just cannot It's got a very low number of FFT points. So it can't use all of that sample data. And that's one of the keys with having a high number of FFT points. No point having 150 million gigabytes of sample memory if your FFT algorithm it just can't use it. So yeah, so our signal is way outside the range here. So we can obviously can't select that time base setting, okay? And if we go worse, we can only go to 800 kHz, okay? So we've got it So the absolute

**Dave Jones:** best range that we can get where we're going to get the most resolution out of this thing is at 20 microseconds per division because anything uh faster let me go to 10, okay? Or you know, let's let's go down to one for example. You know, look Right, we're at 5 MHz per division, okay? We're going to get no resolution in there at all. So the absolute best when you're mucking around trying to get the best FFT possible on your scope, you've got to do this. Find where your

**Dave Jones:** I'm tweak, sorry, the horizontal I'm not showing on the screen here, but So that is the absolute best we can do. So we want to go center. We want to go 1 MHz. And boop boop boop boop Right, and then we want to change our span like that and bingo, that is the absolute best we can do on this thing. The absolute best.

**Dave Jones:** So as you can see it's best ain't good enough. So while these modern low-end digital scopes are absolutely thoroughly impressive value for money, it's got more bells and whistles you can poke a stick at. It's got a ton of memory. This thing has like 14 mega standard. I think it has when you if you buy the option at Oh, I've got a dicky.

**Dave Jones:** I think I've got a dicky T piece there. I think I do. Uh anyway, you get these things impressive amount of memory. It works great in the time domain, everything else, but the FFT on it is almost like a toy. And we'll see if the Rigol DS 2200 is any different.

**Dave Jones:** We're at 50 microseconds per division, which wouldn't work before, and sure enough, it doesn't work here either. Look, we'll change it down to 20 microseconds per division. Bingo, we've now got our FFT, and we can maybe zoom in on that and have a squeeze.

**Dave Jones:** But the good thing about the Rigols is that yes, once you're in math mode, the horizontal actually does that. And if you just press channel one, bingo, you can go back, and that changes your time domain, and you press math again, and bingo, you're in you can actually adjust that, and then your time base can be used to zoom in. So, jazzy jazzy, okay, but What what what what? Thanks for playing.

**Dave Jones:** That is no good at all. Woo! Jumping around like a jackrabbit. There we go, center one meg, we're at uh 10 dB uh per division. Maybe we can change that. Hang on. No, how do we uh How do we adjust? Oh, that's right, we've got to go in here, and we've got to go like that, and then select. Now we're at 20 dB per division like we were on the other ones.

**Dave Jones:** Oh, goodness. around, around. There we go. Yep. No good at all. Not actually sure why it's jumping around like a jack rabbit on that 20 microseconds like we're triggering smack in the middle there. Nothing wrong there. And then there if we go to 10 microseconds per division on our time domain, then it doesn't jump around anymore and we got similar to what we saw on the Rigol 1000Z.

**Dave Jones:** But yeah, see it's it's pretty much just a toy. You can see that something's there and that might be good enough for a lot of uses, but to analyze something like this FM modulator signal you know like use it more like a real spectrum analyzer, it's no good at all. Now, if we go back to our Rigol and Schwarz here, it's a good example because it allows us to change the number of FFT points, which is absolutely beautiful.

**Dave Jones:** And you'll notice that if we change Okay, we're at our maximum 128K points, change it to 64K points and you'll notice that it's halved. Like that look at the it it has stopped here. Okay, and the center is at 833 kHz. That's why there's no signal anymore cuz our 1 MHz is out here like this. Okay? So, using this particular time base of 5 ms here, sorry for the big fat finger in the way.

**Dave Jones:** I should use my poker. 5 ms per division and at 65K points, we can't get that. So, we're going to have to go basically turn this is where it becomes a bit annoying. Let's go down back to 2 ms per division here and turn the FFT back on and you'll notice that we will hopefully get it. There we go. Now with our 65K points, we can actually go in there and see that. But it all depends on the upon the time base. So, yep, we're at the center

**Dave Jones:** now and bingo, we can go in like that and see it. But of course, if we change our if we don't have enough data there, let's go down to say an order magnitude lower, 200 microseconds per division. Turn our FFT back on and look, we can't get See, the resolution in there is no good, okay?

**Dave Jones:** Cuz we're calculating even though we're still calculating a massive 65 thousand um FFT points in there, i.e. frequency bins, it still isn't enough. We cannot zoom in any further on that, and you'll notice that it has now given us a much greater frequency range. Our Our span is now 100 Look at this. Yeah, it's like 25 MHz span there. It's absolutely enormous. Good thing about this is that if you want to see a bit more, I can just turn that menu off there. That's quite jazzy. But, you can

**Dave Jones:** see how it's all a big trade-off in terms of, you know, getting the right uh A, you've got to have the right memory depth set. That's not going to work. You've got to have the right time base setting. You've got to have Well, you know, generally if your scope can do, um you know, allows you to change the number of points like this, then you set it to, you know, maximum unless you want really fast updating. So, if I now set it to 8K points FFT, same as what we had

**Dave Jones:** on that crappy Teledyne LeCroy, look, you can see that it's giving us, you know, like that is a similar sort of result at that particular time base. Let's see if we can tweak that. So, if we turn off FFT, let's give us a bit more. Let's go up to 1 ms. Can we get 1 ms worth? Nope, because it only gives us our um Sorry, our span 500 kHz, not good enough. So, the best time base we can do is 500 microseconds. There we go, 500

**Dave Jones:** microseconds per division, and now we can zoom in. But, you know, at least it is doing a better job than that Teledyne LeCroy. You can actually see the separate signal components there. You know, it it's fairly clean. And, of course, as I said, you know, if we go into the acquire menu, high high resolution maybe maybe we can clean that up a little bit there. but we can certainly go in there and see these things. And with this Rohde & Schwarz, the measurements on the Rohde & Schwarz

**Dave Jones:** are really quite nice. I've showed the quick view thing, but if you go into which uh and auto measure, which doesn't work in FFT mode sadly, but if you go like if you turn the cursors on, next peak, previous peak works an absolute treat. Look at that. So, I hope you can start to appreciate the huge trade-offs in terms of sample rate, time base, setting number of FFT points, the higher the better. You know, it's worth paying for if FFT functionality is something that you want in a scope because, you

**Dave Jones:** know, you could end up with a toy like those Rigol scopes, and you know, it's really no good. So, there you have it. There's a little look at the FFT modes on five different scopes here. No, I didn't I deliberately didn't use the Tektronix MDO 3000 scope cuz it's got a built-in hardware spectrum analyzer. So, you know, I I guess I could get the FFT mode out and try that just for kicks, shall we? Yeah, yeah, why not? Anyway, I'll do that after this, but as you can see, I love this Rohde &

**Dave Jones:** Schwarz. Works really, really well. It's got a large number of FFT points, and it's functional, it's usability, functionality, the auto setup on the FFT gets you in the ballpark, and it just really is quite a nice scope. Of course, the the Keysight, which which is advertised as having a specific Well, this new touch model, specific FFT functionality, can do gated FFT. It's extremely powerful, which the Rohde & Schwarz can't do any of that.

**Dave Jones:** So, it's in terms of FFT, the best is the Keysight MSOX 3000 in this bunch by far, but you know, the Rohde & Schwarz does a really good job. The Rigol the Rigols are a toy, you know, as are most low-end scopes. The GW Instek, very nice, very impressive at 1 meg point FFT, but the usability on it is just pretty atrocious. But ultimately, it does the job. So, you know, hey, you got to give it a thumbs up for that. And the Teledyne LeCroy here is a is a joke, the

**Dave Jones:** Dick and Balls model. Yeah, don't like that at all. Hmm. Um that's not good. Pair on self-test failed. What? What? There are persistent power please qualified. Unbelievable. Um well, I've got my signals connected in, but surely that shouldn't make a difference. That is greatly disturbing.

**Dave Jones:** Hmm. Now, if we have a look at this on the Tektronix MDO 3000 scope here, this is not the FFT, this is using the analog RF front end because it's a mixed domain oscilloscope. Does actually have an RF spectrum analyzer built in.

**Dave Jones:** Albeit, it's a digital sampling-based system, so it does actually do an FFT approach, but it actually has, you know, specific hardware and software to actually do this. So, it's not a That's why it's it's faster updating, even though this slow scope is generally slow as a wet week, it is much faster updating because it's doing the discrete Fourier transform of the all the FFT of the signal instead of actually doing the sweep-based system, you know, generating a sweep and going across. Because the Rigol DSA815 to build up the image that

**Dave Jones:** we saw before actually takes like 50 seconds, I think, to do an entire sweep cuz I had a low-resolution bandwidth set in and everything else. But there you go. This gives an excellent result. Check it out. It's performance is better. As we've seen before, performance is better than the entry-level Rigol DSA 815.

**Dave Jones:** And as you actually saw before, we've got a modulation index set up here of 0.1. So, the modulation index is the frequency deviation is the frequency deviation divided by the FM frequency there. So, it's we've got 500 Hz deviation with a 5 kHz FM frequency. So, I'll just interestingly show you what happens if we take that above one, okay?

**Dave Jones:** If we take the modulation index above one, we'll see our carrier actually start to drop. And as we go up, say to 0.5 or something, we'll actually see more we'll see more tones down here getting smaller and smaller and smaller. So, it's 500 Hz at the moment, okay? This is 1 kHz. And do we see any? No, not really. Let's take it up to 2 kHz.

**Dave Jones:** There we go. Got another See? There we go. They're increasing amplitude, and then we start to see more of them. If we increase the modulation index, let's go up to five. So, we've got a modulation index of one.

**Dave Jones:** So, our frequency deviation is 5 kHz, our FM frequency is 5 kHz. And look at that. There we go. Beautiful. Now, if we take it above that, so we've got a module I've got now taken up to 10 kHz frequency deviation.

**Dave Jones:** So, we've got a modulation index of two. Bingo, our carrier here has dropped. And let's take it up to 20. So, now you can see the carrier's actually gone back up, and the side first sideband here has dipped back down, and then it goes up again. And this is all classic textbook stuff for FM frequency analysis theory. So, go look it up if you want, but it works.

**Dave Jones:** Excellent. But, if we actually try and do an FFT on our channel one signal here, look, it's got the same annoying thing as the GW Instek. You got to set, you know, your horizontal controls actually still work on your time domain signal. So, you've got to now dick around with these two multi-purpose controls. I hate having these two separate controls on the MDO 3000. It's just It's excruciating. Anyway, well, actually in this case it's a bit handier because um this is a good use of the

**Dave Jones:** dual knobs, I guess. You don't have to dick around with this. So, we can actually uh tweak that. You can see how slow this thing is. It's just whoa. You can easily overshoot with this. So, anyway, this thing does have a keypad. So, actually, we can type it in.

**Dave Jones:** Beautiful. Yes, I love things with keypads. Ah. So wonderful. So wonderful. And we want 100 kHz. There we go. We're in like Flynn. Okay, now I set this to 1 meg point memory. I set it to Hann in window. Here we go, and 1 MHz center with a Well, 100 I sure I It's set It's changed that to 125. I'm sure I set it to 100. Anyway, um it looks like it needs to It can't 100 kHz. There we go. No, doesn't like that. Anyway, so we need to uh

**Dave Jones:** Oh, sorry, but per division. Okay, so let's go in there and 10 kHz. Ah, it's changed our carrier. 1 MHz. Thank you very much.

**Dave Jones:** It didn't It didn't like that, did it? 10 kHz per division. Oh, no, there we go. 12.5. Okay, now we're in Lake Flynn. Here we go. It's doing the business now, but look, it's not updating. It's not updating.

**Dave Jones:** Like you'd expect to see the noise change. That way, we got one. We got one. Um yeah, this is the MDO 3000 in a nutshell. It is one of the slowest modern scopes I've ever used. I I Well, I think it is the slowest. It is just horrendous. Um every time you turn something on, it's got very limited processing power in this thing. So, I don't know how many points FFT uh this one actually does in math mode. I wonder if it's in the manual. Let me go read

**Dave Jones:** it. But, let me try and turn the channel off. Can we still do the FFT? I don't know, but anyway, look how sharp this is. It's absolutely incredible. It must have a massive number of frequency bins, i.e. a massive number of FFT points that it's calculating. This has got it. Yes, it still works, by the way, with the waveform off. Excellent. So, the Tektronix actually is has got to be the winner in the in this FFT shootout by far. That's got to be equivalent to the

**Dave Jones:** million points in the GW Instek, no doubt. So, no wonder it's as slow as a wet week. Um is that No, it doesn't tell us. We've got 1 meg point as our sample memory, but it doesn't tell us how many uh FFT points it's actually doing, and there's Yeah, there's no indication in there. All you can tell is by how slow it is. And yes, I just read the manual, and sure enough, this thing has up to 2 meg points FFT. So, absolutely brilliant. Um yeah, okay. Sorry,

**Dave Jones:** Tektronix. No wonder it's uh slow calculating 2 million meg points, but the GW Instek was faster doing a million. It was at more than twice as fast. So, it is This is still a very slow scope, right? Don't get me wrong, it's a dog, but uh hang on. Why is it now like it's now take Oh, there we go. Hey, we got one.

**Dave Jones:** Um, yeah, it it takes forever. It's still very slow, but it can give you the performance, not that you really need it, because you're going to use the real RS spectrum analyzer, but anyway, this is indicative This should be indicative.

**Dave Jones:** Uh don't quote me, but uh should be indicative of the other uh non-MDO scopes um in uh in Tek's range, cuz basically the MDO is one of their existing series with the RS spectrum analyzer hardware tacked on. That's basically what it is. Um, so yeah, its performance should be similar. So, absolutely, the MDO is the winner, although I'm not sure if it can do gated, but I think we can Can we do gated on the real RF like we can on the Key site? I don't know. Anyway, um

**Dave Jones:** it it is a winner. So, very, very happy with that. Oh, it can do advanced math. And there we go. That's zoomed in a bit. That's uh 2.5 kHz per division now. So, check that out. Beautiful result. Absolutely gorgeous. So, there you go. I hope you enjoyed that uh Well, it was supposed to be a quick look. I always say that, don't I? And then I just waffle on, and yeah, yeah, find extra things to do. Anyway, look at the difference between FFT modes on various

**Dave Jones:** scopes, and you can see how some of the entry-level ones are just toys pretty much. Yeah, you can detect that some carrier's there, but that's about it. You can't see some basic uh FM uh sidebands and things like that. So, um yeah, but I like that little Rohde & Schwarz. It's a very cute. Look at it.

**Dave Jones:** Um, but yeah, the winner um Tektronix, but the Key site one is really awesome as well. GW Instek, lot of points in it, million points, but yeah, it's a bit annoying to use, but ultimately, yes, it does do the business. So, there you go.

**Dave Jones:** Um it was not designed to be a tutorial on FFT tutorial or anything. It was just a comparison of uh all the different scopes, but I hope you liked it. If you did, please give it a big thumbs up and all that sort of jazz. Catch you next time.
