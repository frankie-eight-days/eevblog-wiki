---
video_id: nImoQcoqkuQ
title: EEVblog #1188 - $10 DIY EMC Probe using Scope FFT
url: https://www.youtube.com/watch?v=nImoQcoqkuQ
source: youtube-asr
timestamps: {"0": 0, "1": 21, "2": 36, "3": 52, "4": 64, "5": 84, "6": 94, "7": 106, "8": 120, "9": 133, "10": 147, "11": 157, "12": 170, "13": 186, "14": 200, "15": 212, "16": 224, "17": 238, "18": 246, "19": 268, "20": 279, "21": 288, "22": 302, "23": 314, "24": 327, "25": 338, "26": 350, "27": 361, "28": 374, "29": 389, "30": 404, "31": 421, "32": 432, "33": 445, "34": 457, "35": 473, "36": 491, "37": 507, "38": 519, "39": 538, "40": 553, "41": 563, "42": 575, "43": 592, "44": 601, "45": 611, "46": 624, "47": 634, "48": 649, "49": 662, "50": 674, "51": 690, "52": 705, "53": 718, "54": 733, "55": 748, "56": 764, "57": 776, "58": 788, "59": 798, "60": 810, "61": 829, "62": 843, "63": 857, "64": 866, "65": 877, "66": 893, "67": 910, "68": 924, "69": 936, "70": 948, "71": 960, "72": 971, "73": 985, "74": 997, "75": 1011, "76": 1024, "77": 1036, "78": 1060, "79": 1075, "80": 1089, "81": 1099, "82": 1118, "83": 1137}
---

**Dave Jones:** Hi, just a quick follow-up to the previous video where I showed how you can make your own do-it-yourself EMI probe for 10 bucks including the little amplifier. And a lot of people pointed out the irony of making a $10 probe and then using it on like a $1,000 or $1,500 spectrum analyzer to make it work.

**Dave Jones:** And yeah, well, fair enough. But a lot of people ask, can you actually use this $10 EMI probe or any EMI probe on a regular oscilloscope? I use the FFT function to turn your oscilloscope into a spectrum analyzer.

**Dave Jones:** And yes, you can. So, let's take a quick look at that. And also, there's other ways to do a cheap spectrum analyzer as well. And I've got on order a one of those USB SDR software-defined radio spectrum analyzer.

**Dave Jones:** So, I hope to do yet another follow-up video on that. Okay, so what I'll do first is just get a base line right across the crystal on this Gigatron board here just so that we can compare it with various scopes.

**Dave Jones:** Here we go. I've got a 100 MHz span. Reasonably low frequency. If you're looking at the far field emissions in like a regular EMC compliance test, if you took your product to an EMC test house, then depending on the type of product, a typical frequency range might be from 30 MHz to 1 gig.

**Dave Jones:** But you can definitely get a decent look at things with just like a 100 MHz span and stuff like that. Depends on the product that you're working with. Let's get that.

**Dave Jones:** I'll put that right over the crystal like that. And we can freeze that. So, there you go. Let's see if we can get a similar response with a similar peaks and noise floor and whatnot.

**Dave Jones:** But really, when you're doing these sort of near field H or E field magnetic or electric field probing, you're not really doing a quantitative measurement as so like an absolute quantitative value.

**Dave Jones:** You're really looking at the spectrum and just seeing if any peaks actually pop out here. And it's something, you know, you move this over your board and you have a look in real time and see if any anything just pops out like that.

**Dave Jones:** And then you go, "Aha, what frequency?" You go in there, you measure the frequency, determine what frequency that is, and if that's going to be an issue. That's why it doesn't uh really matter what size uh loop you use here, whether or not it's calibrated in {quote} marks.

**Dave Jones:** I mean, the uh professional probes, yes, I had to dip the end in yellow cuz I peeled it back. It didn't stick very well, by the way. I need a couple of more coats on that.

**Dave Jones:** I need to get the uh the liquid dip one instead of the spray one, anyway. So, although these uh professional ones might come with uh characteristic uh plots like this, it shows you the uh coupling loss performance over frequency.

**Dave Jones:** In this case, it's a 3 GHz uh span here, but really the calibration in {quote} marks doesn't really matter for these things. You're just looking at a sort of like a relative signal just jumping out of uh the noise floor, basically.

**Dave Jones:** Okay, so let's just try a typical scope here. I've got the brand-spanking new uh Keysight four-channel 1000 X series uh 200 MHz analog bandwidth uh four channels. It's got a reasonably nice FFT function.

**Dave Jones:** Doesn't have a huge number of uh points on this thing. What is it? 64 K point FFT, I think. But it's going to do the business. Now, this isn't the best scope if you're looking at uh low amplitude signals.

**Dave Jones:** It does have a 500 microvolt uh per division range, but that's not true 500 microvolts per division. It's just software magnified. You might be able to see that um in that the pixels are actually uh doubled.

**Dave Jones:** But fortunately, you don't need a uh like a really good low signal level front-end scope because that's what our amplifier's for. This is a 20 dB amplifier, one the cheap $7 one from eBay.

**Dave Jones:** This one happens to be 30 dB. You can get 40 dB ones. If you're worried about the noise floor of your scope impacting it, just get a higher gain preamp.

**Dave Jones:** That's it. So, if you want to get these on eBay, just search for RF preamplifier and there's like dozens of different models. Do a set our probe just one-to-one cuz we haven't got our times 10 probe here and we'll just set it to a like 200 mV per division and I'll put the probe over that crystal again in exactly the same location that we had for the spectrum analyzer and

**Dave Jones:** look at that. Let's go down to 100 mV per division. This is not low amplitude stuff even with a 20 dB gain amplifier. If you get a higher gain amplifier, it's going to be higher again.

**Dave Jones:** But, you know, if I put it elsewhere on the board like directly over the ROM for example, 200 mV per division is some really high-level stuff. That's over the RAM.

**Dave Jones:** I'll just show you that on the board here. See? That's over the ROM. Address decoder, you can see that signal really changing in real time. It's great. That's what you can do probing.

**Dave Jones:** But, of course, we can't see much in the time domain. So, we have to turn on our FFT. You can switch it to the frequency domain exactly like we get over on the spectrum analyzer so we can see the frequency peaks cuz that's what we're really interested in.

**Dave Jones:** All right. Now, we can actually leave the analog signal on if we want. This and generally switch that off cuz it just adds clutter. And if we put it over the crystal like this, then we can start to see some spikes in here.

**Dave Jones:** So, we use our controls here. Let's have a look at the FFT. We're at 100 MHz span. So, there's 10 divisions on there. So, it's 10 MHz per division.

**Dave Jones:** Doesn't actually tell you that down here that's 10 MHz per division. You just got to use your noggin. And our center frequency is 50 MHz. We're just using a Hann in window and vertical units in DBs.

**Dave Jones:** Doesn't matter. You might have seen me use DB microvolts on the spectrum analyzer. I just prefer to work in that for this sort of thing. It doesn't really matter.

**Dave Jones:** We don't really care about absolute values on this near field type measurements really. It's more of a comparative thing and trying to find peaks in the value here. Anyway, move this up and we can change our scale here.

**Dave Jones:** Let's move that up. There we go. And of course we can change our horizontal to get more resolution. You can see the resolution FFT resolution there 122 kHz. So that would be equivalent to our spectrum analyzer there.

**Dave Jones:** It's which we were using a 120 kHz resolution bandwidth filter there. So maybe some averaging or something like that. Get it a little bit better. And then we can go in there with our cursors and then we can measure our frequency.

**Dave Jones:** Bingo, 6 MHz. That's our fundamental clock. Of course 12 MHz and so on. Now because it's hard to actually show these two side by side, what I've done is actually screen captured the spectrum analyzer and in my video editing software here I can overlay it.

**Dave Jones:** That's kind of cool. It's got a similar sort of shape. You can see that the peaks are the same and if you have a look at like this one here for example, it's sort of like you can see that that's a lower amplitude to all the others.

**Dave Jones:** Some of them are a bit higher but and stuff like that. This one is correspondingly low like the spectrum analyzer one. So it's doing the business. And as I said, all you care about is those peaks popping out.

**Dave Jones:** As you go over the board, you might compare board PCB revisions for example. So you might go, "Aha! Like I've got this big spike here for example." might come out.

**Dave Jones:** So you might realize that you goofed up the PCB layout. So you might respin your board, tighten up the loop area to actually get that down, or do whatever measure you want to do, and then you retest it, and you should be able to then see that particular spike drop by X amount of dBs, or whatever.

**Dave Jones:** So, it you don't need a quantitative value. It doesn't really matter to get a comparative difference when you make changes on your design. That's what it's all about. So, you can see how even a low-end scope like this, with its FFT functionality, is more than good enough for the job of doing this.

**Dave Jones:** You don't need an expensive spectrum analyzer. You can just do make your own probe for like five bucks, buy another $10 preamplifier, Bob's your uncle. Let's actually add a 50 ohm terminator to that, and see what difference that makes.

**Dave Jones:** So, there you go. It does get a little bit closer, perhaps, to our response over here. And you can actually see the general trend. So, really, the averaging is probably the best.

**Dave Jones:** Just love the averaging effect. And if I just dial that back to a similar sort of like amplitude, relatively speaking to what we've got on the two screens here, you can see Yeah, it's it's doing quite a reasonable job.

**Dave Jones:** And if we try a scope with a sort of notoriously poor FFT functionality, the venerable Rigol DS1054Z, which is otherwise still an excellent bang for buck scope, let's see what we can do with that.

**Dave Jones:** As you can see, we can actually get that to do the business as well, even though it's, you know, update rate and its number of FFT points isn't great.

**Dave Jones:** But, yeah, let's have a closer look. 18.8 kilo dB volts. just got serious. And as you can see there, it kind of works where it the same 10 MHz uh per division here.

**Dave Jones:** You can see some spikes in there, but it's not terrific. But, the trick with this is is that you'll notice over here it's got trace. Now, the latest firmware the original firmware only um did FFT based on the the trace data, i.e., the display data.

**Dave Jones:** But, if we actually change that, that's why the resolution isn't that great. But, if we change that to memory, there you go. Bingo. That does it on the entire memory.

**Dave Jones:** And you'll notice that we get the expanded uh frequency range now as well. And that's much better, but it's a it is 16K points, but it still does the business.

**Dave Jones:** Yes, the updating is slow on this thing, but like it is still actually usable. It's just not as great. 16K points versus 64K points, there's a big difference, but the information is there.

**Dave Jones:** So, that's the main thing. One of the annoying things about the Rigol though is that you can't turn off channel one, for example, because then your data just vanishes.

**Dave Jones:** So, you've got to actually have channel one on the screen. And if you go into the math function here, and you and it's like half display, which is the split display, and if you go into the full display, it like So, there we go.

**Dave Jones:** We can actually get rid of it like that because it's uh the displayed window moving that out. So, it's still actually capturing the data in there. It's possible to do the business with the Rigol.

**Dave Jones:** It's just a bit slow and clunky, that's all. Like, just trying to change the offset in on this is just an exercise in in frustration. It'll eventually come good, but hey, there it is.

**Dave Jones:** So, we can actually go into the cursors here, and we can actually change our units to hertz. 6 MHz and our 12, etc., etc. Does a reasonable job, but the 16K points isn't great and the slowness of it.

**Dave Jones:** But, apart from that, you can coax it into working, no problems. Now, let's have a look at the Siglent SDS 1202 XE. This is a 200 MHz bandwidth scope, and it gives a pretty darn good account for itself as I'm in exclusive mode at the moment.

**Dave Jones:** I really like the split screen mode is really nice, super fast updating, of course. The FFT is is faster than the Rigol, but you know, not super quick. And I like how you can overlay them on top.

**Dave Jones:** It really like the contrasting colors with the white and the yellow, they really works. Or you can just go exclusive like that. We can actually improve that cuz we're normal display at the moment, but if we go in and do some averages, that is pretty jazzy.

**Dave Jones:** That's doing the business very nicely. I like that. But there are some scopes that are just absolutely useless. This 01 XDS 3202, which actually has a 12 and 14-bit converter in it.

**Dave Jones:** So, in terms of like, you know, like resolution, it's actually quite a good scope, but it its FFT functionality is absolutely useless. I can't even get it to match the parameters of the other scopes with 10 MHz per division.

**Dave Jones:** It's just You can't do anything with it. And the Rohde & Schwarz HMO 1200 series, very cute little scope. It's giving an excellent account for itself. Look at this.

**Dave Jones:** It's a little bit slow cuz I've got all the averaging turned on. I've got 131 K points here, 128 K Oakley Henning window, and that is a superb result.

**Dave Jones:** Look at that. Wow. It does take a slight little bit more fiddling on this to actually get what you want on the FFT window, but that is That is beautiful.

**Dave Jones:** We can actually lower the points. There's our 65 K points. 32 K points. Anyway, that's 16 K points. That's the same as the Rigol, for example, and we're getting a much better response on the Road & Schwarz here.

**Dave Jones:** Not only is it faster, but look at the the noise floor is much better. It's those signals are really popping out of that. So, I'm I'm loving that. And we have a quick look at the GW Instek GDS-1104B because this thing has 1 meg points FFT.

**Dave Jones:** And look, this has to be the fastest updating of all of them. That is insane. Look at that. Unfortunately, um it's a bit inflexible in that you can't actually turn off the analog channel, otherwise it actually vanishes.

**Dave Jones:** And if you try and change the position of it, if you go up off the screen, it's not just the display, it's actually the um ADC window. So, you start to see your signal vanish like that.

**Dave Jones:** But one of the reasons it's so fast, we're we are only on 10 K points mode if we memory mode. If we go to 100 K points, wow, look at that.

**Dave Jones:** Now we're talking. 1 meg points. Takes time for its first, but but even at 1 meg points, which is different, this is the sample memory. This is not the FFT number of FFT points.

**Dave Jones:** This one actually takes a bit of fiddling around in terms of like selecting the correct thing here, but there we go. We've got it. And you can see the ridiculously fine resolution in there.

**Dave Jones:** It's just nuts. Unfortunately, it doesn't seem to have an FFT averaging function. I've got the I've got the channel averaging function turned on. If we go into acquire there, I've got that done, but it doesn't look like it has a well, separate average for the FFT.

**Dave Jones:** But yeah, it's just all kind of like really messy. I'm not not too taken by it. Let's have a look what a higher end scope can do, one with not only a true 1 mV front end, but also a 10-bit ADC as well.

**Dave Jones:** So, this is a Rohde & Schwarz RTB2204, very nice scope. And look at the ridiculously fast updating on this. I've got the resolution bandwidth. You can just go in there and set that.

**Dave Jones:** It's very nice. You can just like type it in and the span, it's beautiful. Anyway, like it is quick. It is superbly fast. Look at that. But, you might notice that there's a lot of crap in there.

**Dave Jones:** So, if you actually go into the waveform. So, we've got our handing waveform as per normal. That's our spectrum. We can actually go in there even though I've got averaging for the front end.

**Dave Jones:** Now, it's actually got both on that screen together. You can see that. So, that's a real nice feature. So, you can have both turned on. We can just turn the spectrum off and bingo, there's our average.

**Dave Jones:** And look at all that beautiful detail just popping out of the noise there. That's fantastic. You notice how it's like going up and down, up and down very slowly like that.

**Dave Jones:** I believe this is like beating between the averaging cuz this has got two different types of averages. One is the FFT processing average, which we've got down here. The other, if we go to the acquisition menu, I've actually got the input sampling in average mode.

**Dave Jones:** So, if we change that back to sample mode, you'll notice that it's it's kind of like it's different now. But, if we can do both, we can pull out extra detail.

**Dave Jones:** Now, I've got 10 averages on both and we just pull out the extra detail there. It's very nice. The other thing I really like about this scope, not only the FFT detail we're getting in here, but look, I can just draw stuff.

**Dave Jones:** Look at that. Like just little things like just popping out of the noise like that one in there, for example, like this little thing popping out in there. It's just it's absolutely terrific.

**Dave Jones:** Smiley face. There you go. But of course that's a much more expensive scope than the other uh bottom of the range ones we've looked at. But you can see that, you know, while the uh performance of this is brilliant cuz it's got a 10-bit analog-to-digital converter, a true 1 mV uh noise floor, and uh really super fast FFT uh processing with large number of points, we're really extracting the detail out

**Dave Jones:** of that. Actually, more you could argue more so than we were getting with the uh Rigol spectrum analyzer over here. But granted, this this scope is actually much more expensive than this Rigol spectrum analyzer, which is a bottom of the range thing, granted.

**Dave Jones:** Dave cat. So there you go. These are, you know, a reasonably low-end scope, a low-bandwidth one, can give a reasonable account of itself, and can be fairly useful for troubleshooting boards like this.

**Dave Jones:** We can just go over there. We can see various peaks. You can see that they vanish. You can manufacture different size uh probes to get different sensitivities. You can really do live probing with just your scope.

**Dave Jones:** Works a treat. No worries. But you've got to have a nice fast FFT mode, and if it's slow as a wet week, and it's got a crap uh resolution like the Rigol one, for example, you might be able to press it into doing the business, but it's not as nice as a high number of points FFT and, you know, real-time updating.

**Dave Jones:** So, and it works a treat. You don't need $1,000 or $1,500 spectrum analyzer. But as I said, I've ordered one of those SDR USB dongle things, and in theory you should be able to use this with a SDR dongle for a poor man's spectrum analyzer.

**Dave Jones:** But anyway, save that for another video. If you like this one, please give it a big thumbs up. As always, discuss down below. Catch you next time. Hey.
