---
video_id: UrS5ezesA9s
title: EEVblog 1465 - Your Multimeter Can Measure Inductors
url: https://www.youtube.com/watch?v=UrS5ezesA9s
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 26, "3": 41, "4": 54, "5": 71, "6": 86, "7": 99, "8": 111, "9": 127, "10": 140, "11": 157, "12": 174, "13": 184, "14": 202, "15": 216, "16": 232, "17": 246, "18": 262, "19": 278, "20": 292, "21": 306, "22": 320, "23": 336, "24": 351, "25": 365, "26": 382, "27": 400, "28": 419, "29": 437, "30": 452, "31": 466, "32": 485, "33": 504, "34": 523, "35": 536, "36": 548, "37": 561, "38": 577}
---

**Dave Jones:** Hi, I'm going to show you a neat little feature in multimeters you probably weren't aware of. Now, most multimeters these days have a capacitance mode either single on the dial like that or switch through typically on the ohms range like

**Dave Jones:** this and you can measure your cap like that. No worries, okay, we've got our 10 nanofarad standard capacitor here and it measures that. No worries except for this one. I don't know why this fluke is out, but anyway, they have reasonable

**Dave Jones:** capacitance measurement in them. It's not great. It's usually only like a couple of percent accuracy at best, but it's quite handy. Not as good of course as a proper LCR meter where you can select the different test frequencies,

**Dave Jones:** but you can also measure not only capacitance but inductance as well and resistance and ESR and quality factor and dissipation factor and all sorts of stuff that you get with a nice LCR meter. Now, there's only a few

**Dave Jones:** multimeters on the market that will actually have inductance measurement built into them and they're and they're pretty rare, but a little known feature of multimeters is that they actually test at well, not specific fixed frequencies like a good LCR meter does.

**Dave Jones:** This one can measure 100 hertz, 120, 1 kilohertz, 10 kilohertz, and 100 kilohertz, but multimeters also test at frequency as well, which means you might be able to press them into service for measuring inductors as well. Let me show

**Dave Jones:** you. So, we'll have a look at the actual waveform the test signal that's actually being used. Now, of course for an LCR meter, we're getting of course a perfect sine wave like this at the perfect 1 kilohertz that we select and of course

**Dave Jones:** at 10 kilohertz and we can go to 100 kilohertz and we can test down at 100 hertz if we want to. There you go. So, a perfect sine wave at specific set frequency is what you get with proper

**Dave Jones:** LCR meters, but if we swap that over to a multimeter, in this case got the 121G W, you can see that it's actually got a triangular-shaped waveform here. And that is at 100 you know, just a little bit over 100 hertz

**Dave Jones:** here. And if we change the capacitance, it's actually the test frequency is going to vary with the capacitance, but not all meters work identically like this. And then if we try the Fluke here, you can see that that's once again the

**Dave Jones:** same 1 nanofarad, but it's higher frequency again. It's testing at 4.3 kilohertz. It's not quite a triangle wave there. Then if we change the capacitance, you can see that the test frequency changes with the capacitance there. And then if we try the Uni-T 61E+

**Dave Jones:** here, you can see that that's 142 hertz, but it doesn't really change frequency at all with the capacitance that we're actually testing. So, you know, every multimeter uses its own little secret sauce. Every multimeter chip set's different, everything like that. So, you

**Dave Jones:** can probe your multimeter and have a look for yourself, and they'll have different test signal levels, and they'll have different biases, and everything else. But anyway, I'm just showing you that they all work differently. Now, you should know your

**Dave Jones:** capacitive impedance formula, XC, is 1 on 2 * pi * F * C. And then they can calculate the capacitance. You can rearrange that to calculate the capacitance. Well, you should also know that the impedance formula for an inductor is exactly the

**Dave Jones:** same as that, except it's not the reciprocal. It's just 2 * pi * F * L. So, what you can actually do, because there is actually a frequency component in there, you can actually press your multimeter into service to measure

**Dave Jones:** inductors. It's not perfect, but you can actually do it. And this one over, or reciprocal measurement mode as it's called, is used on some multimeters like the Fluke 87V here for measuring large-value resistors. It's actually got a nanosiemens mode. So, I'm measuring a

**Dave Jones:** 10 megaohm resistor at the moment, but it we can actually go into nano-Siemens mode here, and if we hook on, this is a 10 gigaohm resistor. It's a bit touchy cuz it's really high value. We can actually measure that. And it's 0.11 or

**Dave Jones:** point So, it's 0.1 nano-Siemens. And if you get the reciprocal of that, 1 on 0.1 nano gives you the 10 gigaohms. And that's how the nano-Siemens mode works. Well, you can kind of sort of do a similar thing with inductors on your

**Dave Jones:** capacitance range on your multimeters. It's not terrific, but you can get it to work. And you can see serious changes in frequency as I change the range on the meter here. Frequency and amplitudes and maybe offsets as well and stuff. So,

**Dave Jones:** yeah, each meter is going to be quite different, but there you go. Let's go to Dave calc here, and I'll show you how it's all going to work. It's not that intuitive, and it's all range-based as well because as I showed,

**Dave Jones:** the different ranges have different frequencies and whatnot. So, it depends on the range you're on. So, one 1 millihenry inductor is actually going to read 1 millifarad if you've got it on or it should in theory if you've got it on

**Dave Jones:** the millifarad range, but it gets weird for the other ones. Gets a bit non-intuitive. 2.2 milli, what you've got to do is you've got to take out the milli there. Okay, so assuming you're on the milli range on your meter that

**Dave Jones:** matches this range like this that the inductor you're trying to measure, then it's 2.2. You invert 2.2 on a calculator, and you get 0.55, and then you just keep the units the same. So, 2.2 millihenries should in theory read

**Dave Jones:** as 0.455 millifarads or 455 microfarads. And so on all the way down. And if you're on microhenries range, then uh need to be on micro Farads range over here. And you may have to use a thousand of uh

**Dave Jones:** multiple if you're on the wrong range and you get the reading here. Anyway, uh let's have a let's see if this actually works. But you I'll just uh auto range it here. Hopefully, we'll get the right range. I'm on 150 milli Henry's here.

**Dave Jones:** Will it actually will it actually work? Uh 150 milli Henry's uh we should be getting uh six 6.6 micro Farads. It's 6.1. So, the lower that is, the higher um it's going to be in the inductance. So, that's reading slightly over. We can

**Dave Jones:** get the confuser out. So, we want to convert this to milli Farads to match the range. So, 6182 like this and you invert that and we get 161 milli Henry's. Um there you go. That's not too far off. So, let's see what the

**Dave Jones:** Uni-T reads. 6.18 we were getting. Is it going to do the same range? 6.31. There you go. That's not too shabby at all. And well, let's choose say 47 milli Henry's. Uh what do we expect? Uh 21 mic. We're getting uh 23 mic. There

**Dave Jones:** you go. And we can swap that back. Come on, you can do it. 23.5. That's good enough for Australia. That gives you a pretty decent indication. Let's try 10 milli. 91.3 uh okay, we expected a hundred there. Well, our

**Dave Jones:** inductor might be a little bit out. 90.3. There you go. That's all right. And if we compare the actual uh values here with the proper LCR meter, I'm measuring it at 1 kilohertz here. The uh 6.8 milli Henry is actually uh 7.3

**Dave Jones:** and the 10 milli Henry is actually well, it it's pretty close to uh bang on 10 and 47 milli is uh 50.8. So, you know, there's some errors in there, but man there you go, 106. But, you know, it's

**Dave Jones:** nothing doing, really. All right, let's try a 220 micro Henry SMD inductor here. Let's give it a whirl with our LCR meter first. There you go, 233 micro Henry's. All right, let's try the same thing with our 121 GW.

**Dave Jones:** Get on there, you bastard. Ah, come on. Easier to probe on the bottom, I think. There we go, 4. Let's Let's call it 4.9 nano Farads. Get the confuser out here, 4.9. We leave the units off, so we invert

**Dave Jones:** that. That'd be 204 micro, cuz you got to shift it back that way. That's not too far off, is it? That's all right, not too shabby. Try the Uni-T, 4.84. Let's try the Fluke 87 here. 5.3. That puts it a bit lower. So, I'll

**Dave Jones:** leave it up to those playing along at home to you try it on your own meter and see how low you can get. Now, on the lower value, like really low in value inductors, of course, you know, you're getting pretty close to

**Dave Jones:** a short circuit. So, you don't expect this to work and sure enough, it doesn't work that well. But, I won't go through like all the whole ranges and everything. But, you can use this like to measure at least reasonably sized

**Dave Jones:** value inductors and get a like at least a usable indication. You've just got to have your noggin on when you use your confuser here to make sure you don't don't don't get your units mixed up. But, yeah, you can actually

**Dave Jones:** get reasonable indications of inductive values. Who knew? Multimeter for measuring inductors. Neat neat little trick. Doesn't work in all cases, but hey, give it a try at home. If you like that video, found it useful, please give it a big thumbs up and leave your

**Dave Jones:** results down in the comments down below to see how your meter fares on what different values and types of inductors and frequency hooking up the scope or that sort of jazz. Fascinating, huh? Catch you next time.
