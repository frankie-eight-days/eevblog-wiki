---
video_id: uus_cpZiqsU
title: EEVblog 1443 - They Don't Teach This in School! (Coherence)
url: https://www.youtube.com/watch?v=uus_cpZiqsU
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 28, "3": 41, "4": 57, "5": 71, "6": 87, "7": 105, "8": 118, "9": 134, "10": 150, "11": 165, "12": 180, "13": 193, "14": 205, "15": 215, "16": 229, "17": 246, "18": 262, "19": 277, "20": 289, "21": 300, "22": 317, "23": 329, "24": 341, "25": 353, "26": 367, "27": 382, "28": 396, "29": 411, "30": 425, "31": 440, "32": 453, "33": 468, "34": 485, "35": 501, "36": 516, "37": 529, "38": 546, "39": 559, "40": 575, "41": 593, "42": 609, "43": 622, "44": 639, "45": 652, "46": 672, "47": 685, "48": 698, "49": 712, "50": 730, "51": 746, "52": 759, "53": 773, "54": 785, "55": 800, "56": 812, "57": 828, "58": 843, "59": 860, "60": 874, "61": 890, "62": 908, "63": 924, "64": 936, "65": 952, "66": 971, "67": 988, "68": 1003, "69": 1018, "70": 1034, "71": 1050, "72": 1066, "73": 1081, "74": 1094, "75": 1110, "76": 1124, "77": 1138, "78": 1152, "79": 1167, "80": 1181, "81": 1195, "82": 1212, "83": 1227, "84": 1244, "85": 1259, "86": 1273, "87": 1285, "88": 1298, "89": 1312, "90": 1327, "91": 1341, "92": 1359, "93": 1371, "94": 1384, "95": 1404, "96": 1420, "97": 1431, "98": 1445, "99": 1464, "100": 1478, "101": 1495, "102": 1510, "103": 1522, "104": 1539, "105": 1557, "106": 1570, "107": 1585, "108": 1599, "109": 1613, "110": 1628, "111": 1643, "112": 1655, "113": 1668, "114": 1682, "115": 1696, "116": 1707, "117": 1719, "118": 1734, "119": 1747, "120": 1760, "121": 1775, "122": 1788}
---

**Dave Jones:** Hi, my previous video on this Ling electrodynamic shaker was very popular. So, I thought I'd do a follow-up video to this. I'll link it up here if you haven't seen it and down below. Highly recommend you watch it. It explains what

**Dave Jones:** electrodynamic shakers are, shows you inside this thing, and we have a play around with it. It's for testing. It's designed for to shake PCBs just like this. You shake them in this direction and change the orientation, this direction, and this direction. And not

**Dave Jones:** just shake like this, but actually over a whole frequency span. So, this one goes from a couple of hertz. I've got this at 5 hertz at the moment. You can count those if you really want to. And it can go up to like, you know, many

**Dave Jones:** kilohertz. They usually top out at around, you know, 10 kilohertz. So, these electrodynamic shakers are great for testing PCBs and products and assemblies. And you're basically testing them to see if they can survive transport. They might whack a satellite

**Dave Jones:** on here. And like a really big one. Cuz you can get ones the size of cars and trucks. And you can shake a whole satellite on there to simulate, you know, launch or, you know, your space probe to simulate re-entry or Now,

**Dave Jones:** I'm going to show you how to set up one of these. And it's all about a mathematical term called coherence. Now, hopefully I'm not going to lose a lot of people, but it involves using, once again, my very cool

**Dave Jones:** HP. None of this Agilent or even Keysight rubbish. HP 3566A dynamic signal analyzer or DSA. And this is the bread and butter tool for the industry I used to work in, the seismic industry, where everything was like low

**Dave Jones:** frequency stuff. I mean, this thing only goes up to 100 kilohertz, 50 kilohertz if you turn on two channels, right? So, these things are designed for really low frequency stuff, but they go right down to DC. They're low noise, and they're

**Dave Jones:** purpose designed. And as you'll see, they have the mathematical capabilities to actually measure coherence, which is a fundamental concept of setting up uh one of these. So, you can buy your $10,000 calibrated electrodynamic shaker, you can buy your

**Dave Jones:** $1,000 uh accelerometer here, and then you can pay another thousand bucks to get it uh NIST-traceable calibrated. Here's uh the little accelerometer here, and you might think, "Well, I've got all this calibrated gear. This is fantastic. I can just whack my accelerometer on here.

**Dave Jones:** I can have another one on my product uh PCB that I'm shaking, and Bob's your uncle. I can just get these beautifully calibrated measurements." What? Couldn't be further from the truth. If you don't set up your jig properly, and you

**Dave Jones:** and you have to do this before you take any serious measurement at all, then your measurements are absolutely useless. In the industry, if you hand in a test result uh report, and it doesn't have the coherence uh data that I'm

**Dave Jones:** going to show you uh setting up today, then they're just going to toss your report in the bin cuz it's absolutely all your data is absolutely worthless if you haven't proven that your uh shaker table, in this particular case, and your

**Dave Jones:** setup for the particular measurement that you're taking at the time, is set up correctly. So, that's what this video's about. I'm going to show you how to set this up and the importance of coherence. Now, of course, I also have

**Dave Jones:** to mention that you don't need to do any of this that I'm talking about in this video if your goal is just to put your product on a shaker and then just shake the crap out of it until something

**Dave Jones:** fails. If if that's your goal, and you're not doing any quantitative measurements at all using uh little accelerometers or bigger accelerometers like this one, then uh that's fine. You don't have to worry about any of this. But if you're doing

**Dave Jones:** any quantitative measurements, you have to do what I'm doing as a first step, absolutely essential. Now, you can think of a dynamic signal analyzer is just like a spectrum analyzer or like an FFT analyzer. In fact, that's what

**Dave Jones:** they're often called, FFT analyzers. But, this one is specifically designed, as I said, for low-frequency measurement. Goes right down to DC. That's where they come into their own in like physical measurements like this or your physical phenomenon that you're

**Dave Jones:** typically dealing with in vibration and sound and other, uh, you know, physical, uh, type things, they're all down in the DC to, you know, tens of kilohertz range. So, this is the bit of kit that you want, and it's got the mathematical

**Dave Jones:** functions, as we'll see. So, it works just like a spectrum analyzer. You have frequency on the x-axis. I'm actually starting from 0 hertz here, and I'm going to 200, uh, hertz, and that's what we're going to analyze today. And on the

**Dave Jones:** y-axis, uh, we've got, uh, dB volts, RMS here, and I'm actually feeding in a 100 hertz, um, sine wave, and there it is. You can just get the peak at 100 hertz. And if we feed in a sweep, you know,

**Dave Jones:** we'll we'll see a flat frequency response here because I've just got the source actually connected directly to the input, channel one here, and that's what we're seeing. Simple. But, the real advantage with a dynamic signal analyzer is all the mathematical stuff that you

**Dave Jones:** can actually do, and you can do it when you include a second channel like this. So, you'll notice that we have, uh, the options of just getting the frequency spectrum of channel one or channel two, uh, PSD. I've shown that in another

**Dave Jones:** video. That's the power spectral, uh, density, and, uh, you can get, uh, time as well. So, we can just work like an oscilloscope. But, and then, you can get Well, you can get frequency response, but you then you can get what's called

**Dave Jones:** coherence down here, and that's what this video is all about cuz it's so important. That's related to, our cross spectrum as well. And you'll notice that they're all grayed out because we don't have the second channel enabled. So, if

**Dave Jones:** we actually go into our two-channel measurement here, then we'll find that we'll actually get all of these and we can enable these. So, what we need to do is enable what's called coherence measurement here. Okay, before I freak

**Dave Jones:** you out with what coherence is, let me explain what we're actually trying to measure here. Now, we have a signal source here. Um so, we can generate a sine wave, we can generate a sine sweep, which is called a periodic chirp, or as

**Dave Jones:** we're going to use here, it's going to generate a random frequency over the frequency range of interest, 0 to 200 Hz. So, we're we've got our signal source. This is the input to our system. This is our system here. Our shaker

**Dave Jones:** table is a system. We have an input, which is our signal that we're feeding in via our big power amplifier over here. But, that's the input signal to this electrodynamic shaker here. And then, I'm feeding that input signal into

**Dave Jones:** channel one of our dynamic signal analyzer so that we can measure the input. And you guessed it, channel two is going to measure our output here. So, our output here, this comes from our accelerometer. Now, it can be this tiny

**Dave Jones:** little PCB piezotronics shear accelerometer. This is designed for really small systems. It's absolutely tiny. One of the smallest ones you get. This is actually designed to be glued onto here. This is an adhesive mount. So, we're going to put

**Dave Jones:** the accelerometer onto our shaker plate here. Or, we could use a bigger one in this particular case. This one's got a big ass magnet and it just boom, attaches to the plate like that, or you can screw them on. They're the three

**Dave Jones:** different types available. Jeez, that's powerful. So, the system we're trying to measure is the input to the shaker here and the output from the accelerometer. So, what we're going to try and measure with uh coherence here today is we're going to

**Dave Jones:** try and ensure that this setup that we've got, this crude pathetic uh setup here, is uh ready for measurement in that it's linear, it doesn't have any issues, it's got no noise associated with it, it's got no um other vibrational modes or

**Dave Jones:** anything like that. There's nothing in this system that is going to cause a problem. Then once we set it up, our accelerometer will actually go onto our product, onto our PCB under test. Uh for example, we want to get a quantitative

**Dave Jones:** measurement uh with the accelerometer in say the middle of the product, how much this board is uh flexing, for example, um over the vibrational frequency range. So, that will be our output. But, the values we get here won't be worth

**Dave Jones:** anything unless we know that our uh system itself is set up and it's coherent. So, what does coherence mean? Well, it's actually a mathematical concept. You know, if I put up the formula, I'm probably going to freak you

**Dave Jones:** out, but it doesn't matter. Don't worry about the formula whatsoever. It's a coherence is a mathematical concept that and the coherence has to do with uh complex mathematics, which has of course real and imaginary parts. That's why DSAs have uh real and imaginary uh

**Dave Jones:** measurement components. And the coherence is used in all sorts of other uh measurement internally um in the scope as well. Basically, if we've got an input to a system here and we've got an output to a system, how much does

**Dave Jones:** this output signal that we're getting correlate to the input signal? Like, if we're putting in a perfect sine wave into this thing, are we getting a perfect sine wave out? Basically, and it does that for every frequency element

**Dave Jones:** over the entire frequency range. So, basically think of it how much of the output is correlated to the input and you want, obviously, 100% correlation because if your output signal is not 100% correlated with your input signal, the shake that you're putting into this

**Dave Jones:** thing, then obviously, you've got some sort of non-linearity in your system. You've got noise in the system. You've got vibrational modes in your daggy stupid plate that I've got set up here. Um and I'll we'll hopefully be able to

**Dave Jones:** see the difference um in a minute with that. And you want to make sure that your system is set up because once you go to do your quantitative measurements, if you haven't done your coherence measurement and ensured that your system

**Dave Jones:** is completely linear and set up, then uh all bets are off. Your data's useless. So, here's actually a coherence uh plot here and this is once again over frequency 0 to 200 Hz. And what the coherence mathematical function gives

**Dave Jones:** you is a value between 0 and 1 here. This is not like 1 V or anything like that, right? This is basically this is a factor between 0 and 1. And if your factor is 1 up here, then you have

**Dave Jones:** perfect correlation. If you've got 1.00000 uh pops out for your coherence up here, that means at that particular frequency, we can move the cursor in the middle there at 100 Hz, we have a coherence of 0.99. And that's excellent. Basically, you

**Dave Jones:** know, anything above like It depends on what actually It depends on what type of measurements that you're uh trying to take, but you know, in a system like this, above 0.95 would be like considered like pretty schmick. So, this

**Dave Jones:** is ideally what we want is a coherence value that's completely flat over the entire frequency range, but of course, you can see like a 10 hertz here, it's starting to roll off and we're not worried about that. That's just a

**Dave Jones:** limitation of our system here. So, things in this particular system that might cause your coherence not to be a perfect one like you want it at a particular frequency, you could be getting noise in your measurement, you know, you could be getting like

**Dave Jones:** electrical noise pick up, you could be trunk getting triboelectric noise on your cables which is basically the vibration couples through to the cables. And then your output signal that you're getting from your accelerometer is then no longer correlated with the input

**Dave Jones:** signal. So, it's basically uncorrelated noise is one of the factors that will cause your coherence to drop. Now, if you've got a really crappy shaker, this one's a particularly good one, but it might be non-linear. And that non-linearity could be in the coil

**Dave Jones:** itself. It could be the fact that you're overdriving it. It could be that you know, you've got like a real dodgy plate sitting on it that's just hanging out flapping out in the breeze over here. And if you've got your accelerometer

**Dave Jones:** over here, then you might have a vibrational mode on this plate which causes non-linearity for example and that will screw up your measurements. Or you could have something that's loose on your plate and it's shaking around and things like that. That will cause

**Dave Jones:** uncorrelated noise that's not coming from your source. It's inherent in the system and that will cause you to drop in coherence. Another thing that will drop the coherence is any delay in the system. If you've got any phase delay,

**Dave Jones:** measurement delay, or anything like that, that will cause a drop in coherence as well. So, let's actually assume that this is our vibration test jig that we've assembled and we want to do quantitative measurements on it. So, let's set this up and test how linear

**Dave Jones:** this system is, see what the coherence performance is like before we take any measurements whatsoever. Because as I said, absolutely essential to do this before taking any measurements. So, what we're going to use is we're going to use

**Dave Jones:** our little ICP accelerometer here, and I'm going to just attach this to the plate. I'm going to be really dodgy. Okay, normally you glue these things with super glue, but I couldn't be bothered. And I think it's going to work fairly well with a

**Dave Jones:** bit of electrical tape. She'll be right. And I've got it right near the actual armature over here like this. Now, these accelerometers are touchy little beasties. They actually require a constant current source. This particular one, it's a couple of milliamps up to 10

**Dave Jones:** milliamps. So, I'm going to put it around 5 milliamps. So, I've got my constant constant current source here set up for 5 milliamps, and it requires a compliance voltage that is anywhere from 18 V up to 30 V. If I disconnect

**Dave Jones:** the accelerometer, ta-da! There we go. I've got it set up for a 20 V compliance voltage. And then, when we plug in the accelerometer, we're getting This is smack in the middle of its nominal range. So, 9 V. So, this gives

**Dave Jones:** it the DC bias point. So, we have our 5 milliamps coming in here, and this is powering our accelerometer. Now, I'm tapping off that with an AC coupling cap here. A 0.5 microfarad AC coupling cap, which goes into our input, cuz the

**Dave Jones:** inputs are not that robust. And you can actually blow them up. So, you don't want to be going like high voltage high compliance voltage sources. Even though this does have an AC coupling input option, and we're going to be using that, like it's yeah, I just

**Dave Jones:** want to be built and braces to ensure that no no DC is going to the input here. Okay, I've set it up for 0 to 200 Hz span here. Now, you can actually do a periodic chirp. Like, way. It's sweeping

**Dave Jones:** through the frequency range. It's called a chirp, but it's basically you might know it as a frequency sweep. And that's useful for some things, but we generally don't use that for this sort of test. So, we're going to

**Dave Jones:** choose actually a random noise. And you can might be able to hear that now. And that's inputting random noise over that frequency range from 0 to 200 hertz. So, then when we average our data, we take multiple samples, we average, average,

**Dave Jones:** average, you know that you're going to get energy input at each frequency over here, because it's random. And eventually, you will build up a waveform over frequency. Okay, so we've got our coherence measurement here. Our input, we can like auto range our inputs, so

**Dave Jones:** that it gets a suitable selects a suitable input range. And I've turned on averages as well. Let's just get an RMS average, and then we'll just start like this. So, it's going to now take a few seconds before it starts getting a

**Dave Jones:** couple of averages, and then it starts displaying it. Bingo. We now have This is our coherence response over frequency. And you'll see it slowly gets better as we take more samples, and then it gets more samples at each particular

**Dave Jones:** frequency. And you can see that this is actually a pretty schmick response. The coherence is pretty darn close to one over the entire frequency range. This is just for a bit of tape like this. And if we actually glued it down, we might get a

**Dave Jones:** smidge better, but that's not bad performance at all. So, what happens if we move our accelerometer right out to the edge here? Let's actually do that again. We've got to restart. Before we had it right on the armature here, now it's out here

**Dave Jones:** flapping around in the breeze over here. and Oh, that's not very good, is it? Look at that. Really have something happening here at 100 Hz, and it's like and it's all over the place at even at, you know, it's not just 100 Hz, but

**Dave Jones:** what's happening here is um our system has become non-linear because we've moved the accelerometer from right on the arm and you're here right out here. So, we now got it So, now this is taking into account the mechanical properties

**Dave Jones:** of this plate. And with this plate flapping around in the breeze over here going wiggle wiggle wiggle, yeah, right? It's it's causing all of this uncorrelated noise that's not coming from our signal source. It's coming from um the mechanical

**Dave Jones:** It might be the mechanical resonance. It might be, you know, just basically the non-linearity in the system. Bam! Look at that. So, this is horrible. So, if we put if we built this and we would want to do some

**Dave Jones:** uh quantifying measurements and our accelerometer's mounted over here like this, then if we didn't do this coherence measurement, we would have had no idea that this thing is horribly unlinear between like, you know, 80 Hz and like 140 or something. Okay, so

**Dave Jones:** let's run the same test again, but we'll use uh this accelerometer. This is a Vibra Metrics Inc. made in the United States of America Model 7000. It's really old, but it still works. It's got a magnetic mount. So, let's whoa, put it

**Dave Jones:** on there. But, this one is much heavier. I mean, this weighs practically nothing, um but this one is heavy as It's designed for much bigger systems. So, that extra weight's going to affect the uh magnitude here. It's going to uh

**Dave Jones:** possibly affect the uh mechanical mode of this plate hanging out in the breeze here. And let's start that again and see how this one performs. That's not too shabby at all. And it's going to get better and better

**Dave Jones:** as we build up more data there with the averages. But yep, that's a really schmick response, is it not? Now, what happens if we move this all the way out to the end here? So, that that wasn't there before, was

**Dave Jones:** it? So, if we slide that back, yeah, you can see, yeah, it is very different. So, that was causing, down at about 10 hertz there or something, um yeah, that was causing an issue, definitely, just by having it

**Dave Jones:** out there like that. And this is smart enough to know that if I try and measure coherence without turning averaging on, yeah, nah, you can't do that. And as I mentioned before, the coherence is actually related to the cross spectrum,

**Dave Jones:** and they're mathematically they are actually different, but we can actually do a cross spectrum measurement as well, and you'll notice that it's fairly linear, but we won't go into cross spectral analysis versus coherence, but suffice it to say, they

**Dave Jones:** are intimately related. Pop quiz, hot shot. We've got our nice response like this, it's all happening, exactly what we've seen before. Now, I'm going to change something, see if you can spot the difference. Check this out, there's something horrible happening at

**Dave Jones:** like what, 65 hertz there? Something like that, right? Pretty awful. You might think, "Oh, there's something wrong with my thing." Or, if you've actually got your a second accelerometer on your uh product, on your actual PCB, and you're getting your response, and

**Dave Jones:** this is what all this coherence is about. If you're getting this response, you might think that your product is doing that. But it's not, it's not your product, it's not the jig. What has changed? Well, it's the auto range. Your input values

**Dave Jones:** matter, cuz we're actually clipping. You might have seen there that we're getting an overload on channel two here, which was the accelerometer input. Now, if we put it back to auto range to range it properly, bingo, we go back to exactly

**Dave Jones:** where we were before. And this is the importance of coherence. There's all sorts of factors that can go into this. It's not just the physical jig um itself, the physical mounting and everything else. You have to ensure that

**Dave Jones:** your entire system is set up correctly because at the moment we're just testing the response of this uh plate and you would leave a reference accelerometer on the plate. But, this is just setting the system up. Then you'd add a second

**Dave Jones:** accelerometer onto your actual product or multiple accelerometers onto your product and you'll get your various frequency sweeps to see if they meet some uh you know, military uh performance vibration standard or whatever it is you're in-house company standards. Doesn't matter what it is.

**Dave Jones:** You'll get a response on here and you might see all these dips and everything else and you might think, "Ooh, I've got some mechanical resonance in my product. Oh, I better redesign it quick. Panic." And no, you just haven't set up your jig

**Dave Jones:** properly. And that's the importance of coherence here. This is why I was saying if you don't have your coherence data with your report of your test results of your product, then it's worthless cuz it shows that you have not put any thought

**Dave Jones:** into setting up your vibrational test system. And your data that you get out of your accelerometer your product is absolutely worthless. It doesn't matter how calibrated your accelerometers and charge amplifiers and your uh shaker electrodynamic shakers. Doesn't matter a rat. So, until now we've been

**Dave Jones:** playing around with uh that random generator, but we can't actually do a sweep. So, what I got is an external function generator here. I'm actually going to set it up for a 30-second sweep here from uh 10 hertz to 200 hertz,

**Dave Jones:** which is our uh frequency range of interest. There we go. Starts out slow. Starts out slow and over 30 seconds it will sweep. So, let me start our acquisition. Let's have a look. And because we're only at one frequency,

**Dave Jones:** it's you'll find that it's going to slowly sweep across like this. And eventually, 30 seconds later, it will have swept all the way across, and we will actually get coherence values. Now, this is showing a real interesting result now. Here we go. It's getting

**Dave Jones:** 150. It's almost at 200 Hz here. And boom. And then it can give you of course keep doing its RMS averaging or what not. But look at all these notches that we've got here. What's going on? Once again, this is a gross example of

**Dave Jones:** where you might get a response that you might think's coming from your product, but it's not. It's because you haven't set up your sampling system correctly, so can you guess what the problem is here? I'm going to change something here

**Dave Jones:** on our signal gen, and we'll do it again. It's similar, but more frequent. Okay, I changed it yet again. And look at this. Our coherence I actually started it a bit late there. And look, we're getting this little

**Dave Jones:** wiggle wiggle wiggle wiggle yeah in that signal. Check it out. Look at that. That's interesting, isn't it? What's going on here? Is this some sort of little micro resonant thing happening in here? What's going on? Well, for those who were paying attention that

**Dave Jones:** it took a bit longer, you would have realized that I was changing the sweep time. It started out as 30 seconds. Then I increased it to 60. Um and you would have seen that those dropouts we got here were doubling in frequency when I

**Dave Jones:** changed from 30 to 60 seconds. So, it's a function of our record length and sample time in our DSA compared to our sweep speed that we're actually doing this at. Um so, yeah, this makes a huge difference in the measurement. And if

**Dave Jones:** you just whack your accelerometers on your product and started getting your sweep and thinking that you're getting getting the correct values because you've got your whiz-bang expensive calibrated accelerometers and software and everything, uh no. If you haven't set up the system correctly, you can get

**Dave Jones:** all sorts of wibbly-wobbly stuff that has absolutely no correlation to the product that you're actually testing. I was getting sick of the tape here, so I've actually uh super glued it on now. I should have done that from the start.

**Dave Jones:** Now, check this out. I'm actually setting a sweep time now that is uncorrelated with the uh anything to do with the sample rate. So, 7.7 seconds sweep time, just a random number. If I start a new sample, so this is 7.7 seconds uh sweep time,

**Dave Jones:** and you'll notice that right it's all over the shop, but eventually this will get better and better as we do more averages, and because it's uncorrelated time-wise, then slowly we're going to build up a complete picture. So, you can see it there. Yeah, it's

**Dave Jones:** slowly building up a complete picture of this thing. Now, I'm not saying this is uh the the correct uh method uh to do it. I'm just like showing this as an example of how you can have like a

**Dave Jones:** sampling and other um time correlation errors which will cause a drop in your coherence. There we go. We're almost got the the basically the full response of this thing now. So, time and sampling correlation is yet and phase correlation

**Dave Jones:** as well, as I mentioned, can be another um source of error that you can get in your measured signal that if you don't do this coherence measurement test, you'll never be able to see it. The coherence test is a definitive way to

**Dave Jones:** show that you've got no errors in your system or you know, as few errors uh as possible in your system before you actually start your proper quantitative measurement. Here's another example of uh error that we're getting in. You can

**Dave Jones:** see that the response is not that great. Here is it. It's like it's glued on. This response is supposed to be really nice. Can you spot the error? Maybe you can hear the error. It's these damn screws rattling around

**Dave Jones:** cuz I haven't tied them up. Tighten them back up. Start that again. And you'll see that our response is much nicer. We didn't get all this random noise and crap in there, which then would have gone through onto our output

**Dave Jones:** uh signal. All of that crap was happening cuz we had loosey-goosey um stuff on our setup here. And when you're setting up your system like this and getting your coherence measurements, it can matter that whether or not you've

**Dave Jones:** got your actual product that you want to test on your shaker table because it has extra mass, it can change the dynamic properties of the shaker, which you can introduce non-linearity into your system. And look, I haven't changed

**Dave Jones:** anything else. All I've done is screw on that PCB there, and we've got this huge notch here at what, you know, 32 hertz or something like that. Like it's it's terrible. And then, when you go to put your accelerometer on your product here,

**Dave Jones:** um you're going to get all these weird and wonderful results that you didn't expect. And you might think that you have like a design modal mechanical problem in your product that you're actually testing when you don't. It's your setup. Sure, this is like an

**Dave Jones:** extreme example with it flapping around in the breeze, but hopefully that gives you a good example of what can happen here. So, there you go. I hope you found that interesting, the importance of coherence measurement. So, when next

**Dave Jones:** time when somebody shows you their test results for their vibration uh test that they've done for their product, oh, look at this. Ask them, "Hey, where's your coherence data?" Cuz it ain't worth jack unless you've set up your system

**Dave Jones:** properly. So, there you go. I hope you found that really interesting. Coherence, this is not something that you'll learn in school. Basically, you'll only learn this hands-on. I guarantee you will learn about coherence the very first day you start trying to

**Dave Jones:** do vibration testing on everything and your results go to crap and you're wondering what the hell happens then you discover the world of coherence and setting up your jigs and characterizing your test jigs properly so that you know

**Dave Jones:** the results are going to be good. And anytime you change anything, in fact, anytime you do a measurement, you should do a coherence test first to make sure sanity check your results are what you expect. Because there's so many errors

**Dave Jones:** that can go into introducing non-linearity into your test system. Once you get non-linearity, your measurement output data, you don't know whether or not it's real or aha, imaginary. Get it? You know, real and imaginary complex I'm here all week.

**Dave Jones:** Anyway, hope you found that interesting and valuable. If you did, please give it a big thumbs up and as always you can discuss down below and as always EEVblog forum always sort of stuff and all the different channels I'm on. I'm on

**Dave Jones:** every platform. Catch you next time.
