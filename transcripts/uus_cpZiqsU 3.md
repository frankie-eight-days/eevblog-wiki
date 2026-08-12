---
video_id: uus_cpZiqsU
title: EEVblog 1443 - They Don't Teach This in School! (Coherence)
url: https://www.youtube.com/watch?v=uus_cpZiqsU
source: youtube-asr
timestamps: {"0": 0, "1": 8, "2": 22, "3": 33, "4": 44, "5": 57, "6": 73, "7": 87, "8": 105, "9": 116, "10": 129, "11": 140, "12": 154, "13": 172, "14": 196, "15": 203, "16": 215, "17": 228, "18": 243, "19": 273, "20": 281, "21": 297, "22": 310, "23": 321, "24": 333, "25": 345, "26": 360, "27": 372, "28": 389, "29": 404, "30": 415, "31": 428, "32": 438, "33": 451, "34": 479, "35": 495, "36": 512, "37": 522, "38": 529, "39": 541, "40": 551, "41": 561, "42": 575, "43": 599, "44": 611, "45": 626, "46": 642, "47": 652, "48": 670, "49": 683, "50": 697, "51": 723, "52": 735, "53": 748, "54": 766, "55": 779, "56": 789, "57": 804, "58": 819, "59": 828, "60": 839, "61": 855, "62": 872, "63": 886, "64": 900, "65": 913, "66": 927, "67": 939, "68": 958, "69": 975, "70": 989, "71": 1003, "72": 1014, "73": 1027, "74": 1040, "75": 1060, "76": 1071, "77": 1085, "78": 1108, "79": 1120, "80": 1132, "81": 1143, "82": 1155, "83": 1167, "84": 1181, "85": 1209, "86": 1222, "87": 1245, "88": 1257, "89": 1273, "90": 1283, "91": 1294, "92": 1310, "93": 1321, "94": 1344, "95": 1355, "96": 1365, "97": 1373, "98": 1389, "99": 1402, "100": 1415, "101": 1429, "102": 1440, "103": 1451, "104": 1468, "105": 1478, "106": 1494, "107": 1506, "108": 1520, "109": 1530, "110": 1556, "111": 1565, "112": 1576, "113": 1595, "114": 1609, "115": 1620, "116": 1633, "117": 1643, "118": 1665, "119": 1676, "120": 1685, "121": 1701, "122": 1713, "123": 1722, "124": 1747, "125": 1758, "126": 1771, "127": 1785}
---

**Dave Jones:** Hi, my previous video on this Ling electrodynamic shaker was very popular. So, I thought I'd do a follow-up video to this. I'll link it up here if you haven't seen it and down below.

**Dave Jones:** Highly recommend you watch it. It explains what electrodynamic shakers are, shows you inside this thing, and we have a play around with it. It's for testing. It's designed for to shake PCBs just like this.

**Dave Jones:** You shake them in this direction and change the orientation, this direction, and this direction. And not just shake like this, but actually over a whole frequency span. So, this one goes from a couple of hertz.

**Dave Jones:** I've got this at 5 hertz at the moment. You can count those if you really want to. And it can go up to like, you know, many kilohertz. They usually top out at around, you know, 10 kilohertz.

**Dave Jones:** So, these electrodynamic shakers are great for testing PCBs and products and assemblies. And you're basically testing them to see if they can survive transport. They might whack a satellite on here.

**Dave Jones:** And like a really big one. Cuz you can get ones the size of cars and trucks. And you can shake a whole satellite on there to simulate, you know, launch or, you know, your space probe to simulate re-entry or Now, I'm going to show you how to set up one of these.

**Dave Jones:** And it's all about a mathematical term called coherence. Now, hopefully I'm not going to lose a lot of people, but it involves using, once again, my very cool HP.

**Dave Jones:** None of this Agilent or even Keysight rubbish. HP 3566A dynamic signal analyzer or DSA. And this is the bread and butter tool for the industry I used to work in, the seismic industry, where everything was like low frequency stuff.

**Dave Jones:** I mean, this thing only goes up to 100 kilohertz, 50 kilohertz if you turn on two channels, right? So, these things are designed for really low frequency stuff, but they go right down to DC.

**Dave Jones:** They're low noise, and they're purpose designed. And as you'll see, they have the mathematical capabilities to actually measure coherence, which is a fundamental concept of setting up uh one of these.

**Dave Jones:** So, you can buy your $10,000 calibrated electrodynamic shaker, you can buy your $1,000 uh accelerometer here, and then you can pay another thousand bucks to get it uh NIST-traceable calibrated.

**Dave Jones:** Here's uh the little accelerometer here, and you might think, "Well, I've got all this calibrated gear. This is fantastic. I can just whack my accelerometer on here. I can have another one on my product uh PCB that I'm shaking, and Bob's your uncle.

**Dave Jones:** I can just get these beautifully calibrated measurements." What? Couldn't be further from the truth. If you don't set up your jig properly, and you and you have to do this before you take any serious measurement at all, then your measurements are absolutely useless.

**Dave Jones:** In the industry, if you hand in a test result uh report, and it doesn't have the coherence uh data that I'm going to show you uh setting up today, then they're just going to toss your report in the bin cuz it's absolutely all your data is absolutely worthless if you haven't proven that your uh shaker table, in this particular case, and your setup for the particular measurement

**Dave Jones:** that you're taking at the time, is set up correctly. So, that's what this video's about. I'm going to show you how to set this up and the importance of coherence.

**Dave Jones:** Now, of course, I also have to mention that you don't need to do any of this that I'm talking about in this video if your goal is just to put your product on a shaker and then just shake the crap out of it until something fails.

**Dave Jones:** If if that's your goal, and you're not doing any quantitative measurements at all using uh little accelerometers or bigger accelerometers like this one, then uh that's fine. You don't have to worry about any of this.

**Dave Jones:** But if you're doing any quantitative measurements, you have to do what I'm doing as a first step, absolutely essential. Now, you can think of a dynamic signal analyzer is just like a spectrum analyzer or like an FFT analyzer.

**Dave Jones:** In fact, that's what they're often called, FFT analyzers. But, this one is specifically designed, as I said, for low-frequency measurement. Goes right down to DC. That's where they come into their own in like physical measurements like this or your physical phenomenon that you're typically dealing with in vibration and sound and other, uh, you know, physical, uh, type things, they're all down in the DC to, you know, tens of kilohertz

**Dave Jones:** range. So, this is the bit of kit that you want, and it's got the mathematical functions, as we'll see. So, it works just like a spectrum analyzer. You have frequency on the x-axis.

**Dave Jones:** I'm actually starting from 0 hertz here, and I'm going to 200, uh, hertz, and that's what we're going to analyze today. And on the y-axis, uh, we've got, uh, dB volts, RMS here, and I'm actually feeding in a 100 hertz, um, sine wave, and there it is.

**Dave Jones:** You can just get the peak at 100 hertz. And if we feed in a sweep, you know, we'll we'll see a flat frequency response here because I've just got the source actually connected directly to the input, channel one here, and that's what we're seeing.

**Dave Jones:** Simple. But, the real advantage with a dynamic signal analyzer is all the mathematical stuff that you can actually do, and you can do it when you include a second channel like this.

**Dave Jones:** So, you'll notice that we have, uh, the options of just getting the frequency spectrum of channel one or channel two, uh, PSD. I've shown that in another video. That's the power spectral, uh, density, and, uh, you can get, uh, time as well.

**Dave Jones:** So, we can just work like an oscilloscope. But, and then, you can get Well, you can get frequency response, but you then you can get what's called coherence down here, and that's what this video is all about cuz it's so important.

**Dave Jones:** That's related to, our cross spectrum as well. And you'll notice that they're all grayed out because we don't have the second channel enabled. So, if we actually go into our two-channel measurement here, then we'll find that we'll actually get all of these and we can enable these.

**Dave Jones:** So, what we need to do is enable what's called coherence measurement here. Okay, before I freak you out with what coherence is, let me explain what we're actually trying to measure here.

**Dave Jones:** Now, we have a signal source here. Um so, we can generate a sine wave, we can generate a sine sweep, which is called a periodic chirp, or as we're going to use here, it's going to generate a random frequency over the frequency range of interest, 0 to 200 Hz.

**Dave Jones:** So, we're we've got our signal source. This is the input to our system. This is our system here. Our shaker table is a system. We have an input, which is our signal that we're feeding in via our big power amplifier over here.

**Dave Jones:** But, that's the input signal to this electrodynamic shaker here. And then, I'm feeding that input signal into channel one of our dynamic signal analyzer so that we can measure the input.

**Dave Jones:** And you guessed it, channel two is going to measure our output here. So, our output here, this comes from our accelerometer. Now, it can be this tiny little PCB piezotronics shear accelerometer.

**Dave Jones:** This is designed for really small systems. It's absolutely tiny. One of the smallest ones you get. This is actually designed to be glued onto here. This is an adhesive mount.

**Dave Jones:** So, we're going to put the accelerometer onto our shaker plate here. Or, we could use a bigger one in this particular case. This one's got a big ass magnet and it just boom, attaches to the plate like that, or you can screw them on.

**Dave Jones:** They're the three different types available. Jeez, that's powerful. So, the system we're trying to measure is the input to the shaker here and the output from the accelerometer. So, what we're going to try and measure with uh coherence here today is we're going to try and ensure that this setup that we've got, this crude pathetic uh setup here, is uh ready for measurement in that it's linear, it doesn't have any issues, it's

**Dave Jones:** got no noise associated with it, it's got no um other vibrational modes or anything like that. There's nothing in this system that is going to cause a problem. Then once we set it up, our accelerometer will actually go onto our product, onto our PCB under test.

**Dave Jones:** Uh for example, we want to get a quantitative measurement uh with the accelerometer in say the middle of the product, how much this board is uh flexing, for example, um over the vibrational frequency range.

**Dave Jones:** So, that will be our output. But, the values we get here won't be worth anything unless we know that our uh system itself is set up and it's coherent.

**Dave Jones:** So, what does coherence mean? Well, it's actually a mathematical concept. You know, if I put up the formula, I'm probably going to freak you out, but it doesn't matter.

**Dave Jones:** Don't worry about the formula whatsoever. It's a coherence is a mathematical concept that and the coherence has to do with uh complex mathematics, which has of course real and imaginary parts.

**Dave Jones:** That's why DSAs have uh real and imaginary uh measurement components. And the coherence is used in all sorts of other uh measurement internally um in the scope as well.

**Dave Jones:** Basically, if we've got an input to a system here and we've got an output to a system, how much does this output signal that we're getting correlate to the input signal?

**Dave Jones:** Like, if we're putting in a perfect sine wave into this thing, are we getting a perfect sine wave out? Basically, and it does that for every frequency element over the entire frequency range.

**Dave Jones:** So, basically think of it how much of the output is correlated to the input and you want, obviously, 100% correlation because if your output signal is not 100% correlated with your input signal, the shake that you're putting into this thing, then obviously, you've got some sort of non-linearity in your system.

**Dave Jones:** You've got noise in the system. You've got vibrational modes in your daggy stupid plate that I've got set up here. Um and I'll we'll hopefully be able to see the difference um in a minute with that.

**Dave Jones:** And you want to make sure that your system is set up because once you go to do your quantitative measurements, if you haven't done your coherence measurement and ensured that your system is completely linear and set up, then uh all bets are off.

**Dave Jones:** Your data's useless. So, here's actually a coherence uh plot here and this is once again over frequency 0 to 200 Hz. And what the coherence mathematical function gives you is a value between 0 and 1 here.

**Dave Jones:** This is not like 1 V or anything like that, right? This is basically this is a factor between 0 and 1. And if your factor is 1 up here, then you have perfect correlation.

**Dave Jones:** If you've got 1.00000 uh pops out for your coherence up here, that means at that particular frequency, we can move the cursor in the middle there at 100 Hz, we have a coherence of 0.99.

**Dave Jones:** And that's excellent. Basically, you know, anything above like It depends on what actually It depends on what type of measurements that you're uh trying to take, but you know, in a system like this, above 0.95 would be like considered like pretty schmick.

**Dave Jones:** So, this is ideally what we want is a coherence value that's completely flat over the entire frequency range, but of course, you can see like a 10 hertz here, it's starting to roll off and we're not worried about that.

**Dave Jones:** That's just a limitation of our system here. So, things in this particular system that might cause your coherence not to be a perfect one like you want it at a particular frequency, you could be getting noise in your measurement, you know, you could be getting like electrical noise pick up, you could be trunk getting triboelectric noise on your cables which is basically the vibration couples through to the cables.

**Dave Jones:** And then your output signal that you're getting from your accelerometer is then no longer correlated with the input signal. So, it's basically uncorrelated noise is one of the factors that will cause your coherence to drop.

**Dave Jones:** Now, if you've got a really crappy shaker, this one's a particularly good one, but it might be non-linear. And that non-linearity could be in the coil itself. It could be the fact that you're overdriving it.

**Dave Jones:** It could be that you know, you've got like a real dodgy plate sitting on it that's just hanging out flapping out in the breeze over here. And if you've got your accelerometer over here, then you might have a vibrational mode on this plate which causes non-linearity for example and that will screw up your measurements.

**Dave Jones:** Or you could have something that's loose on your plate and it's shaking around and things like that. That will cause uncorrelated noise that's not coming from your source. It's inherent in the system and that will cause you to drop in coherence.

**Dave Jones:** Another thing that will drop the coherence is any delay in the system. If you've got any phase delay, measurement delay, or anything like that, that will cause a drop in coherence as well.

**Dave Jones:** So, let's actually assume that this is our vibration test jig that we've assembled and we want to do quantitative measurements on it. So, let's set this up and test how linear this system is, see what the coherence performance is like before we take any measurements whatsoever.

**Dave Jones:** Because as I said, absolutely essential to do this before taking any measurements. So, what we're going to use is we're going to use our little ICP accelerometer here, and I'm going to just attach this to the plate.

**Dave Jones:** I'm going to be really dodgy. Okay, normally you glue these things with super glue, but I couldn't be bothered. And I think it's going to work fairly well with a bit of electrical tape.

**Dave Jones:** She'll be right. And I've got it right near the actual armature over here like this. Now, these accelerometers are touchy little beasties. They actually require a constant current source.

**Dave Jones:** This particular one, it's a couple of milliamps up to 10 milliamps. So, I'm going to put it around 5 milliamps. So, I've got my constant constant current source here set up for 5 milliamps, and it requires a compliance voltage that is anywhere from 18 V up to 30 V.

**Dave Jones:** If I disconnect the accelerometer, ta-da! There we go. I've got it set up for a 20 V compliance voltage. And then, when we plug in the accelerometer, we're getting This is smack in the middle of its nominal range.

**Dave Jones:** So, 9 V. So, this gives it the DC bias point. So, we have our 5 milliamps coming in here, and this is powering our accelerometer. Now, I'm tapping off that with an AC coupling cap here.

**Dave Jones:** A 0.5 microfarad AC coupling cap, which goes into our input, cuz the inputs are not that robust. And you can actually blow them up. So, you don't want to be going like high voltage high compliance voltage sources.

**Dave Jones:** Even though this does have an AC coupling input option, and we're going to be using that, like it's yeah, I just want to be built and braces to ensure that no no DC is going to the input here.

**Dave Jones:** Okay, I've set it up for 0 to 200 Hz span here. Now, you can actually do a periodic chirp. Like, way. It's sweeping through the frequency range. It's called a chirp, but it's basically you might know it as a frequency sweep.

**Dave Jones:** And that's useful for some things, but we generally don't use that for this sort of test. So, we're going to choose actually a random noise. And you can might be able to hear that now.

**Dave Jones:** And that's inputting random noise over that frequency range from 0 to 200 hertz. So, then when we average our data, we take multiple samples, we average, average, average, you know that you're going to get energy input at each frequency over here, because it's random.

**Dave Jones:** And eventually, you will build up a waveform over frequency. Okay, so we've got our coherence measurement here. Our input, we can like auto range our inputs, so that it gets a suitable selects a suitable input range.

**Dave Jones:** And I've turned on averages as well. Let's just get an RMS average, and then we'll just start like this. So, it's going to now take a few seconds before it starts getting a couple of averages, and then it starts displaying it.

**Dave Jones:** Bingo. We now have This is our coherence response over frequency. And you'll see it slowly gets better as we take more samples, and then it gets more samples at each particular frequency.

**Dave Jones:** And you can see that this is actually a pretty schmick response. The coherence is pretty darn close to one over the entire frequency range. This is just for a bit of tape like this.

**Dave Jones:** And if we actually glued it down, we might get a smidge better, but that's not bad performance at all. So, what happens if we move our accelerometer right out to the edge here?

**Dave Jones:** Let's actually do that again. We've got to restart. Before we had it right on the armature here, now it's out here flapping around in the breeze over here. and Oh, that's not very good, is it?

**Dave Jones:** Look at that. Really have something happening here at 100 Hz, and it's like and it's all over the place at even at, you know, it's not just 100 Hz, but what's happening here is um our system has become non-linear because we've moved the accelerometer from right on the arm and you're here right out here.

**Dave Jones:** So, we now got it So, now this is taking into account the mechanical properties of this plate. And with this plate flapping around in the breeze over here going wiggle wiggle wiggle, yeah, right?

**Dave Jones:** It's it's causing all of this uncorrelated noise that's not coming from our signal source. It's coming from um the mechanical It might be the mechanical resonance. It might be, you know, just basically the non-linearity in the system.

**Dave Jones:** Bam! Look at that. So, this is horrible. So, if we put if we built this and we would want to do some uh quantifying measurements and our accelerometer's mounted over here like this, then if we didn't do this coherence measurement, we would have had no idea that this thing is horribly unlinear between like, you know, 80 Hz and like 140 or something.

**Dave Jones:** Okay, so let's run the same test again, but we'll use uh this accelerometer. This is a Vibra Metrics Inc. made in the United States of America Model 7000. It's really old, but it still works.

**Dave Jones:** It's got a magnetic mount. So, let's whoa, put it on there. But, this one is much heavier. I mean, this weighs practically nothing, um but this one is heavy as It's designed for much bigger systems.

**Dave Jones:** So, that extra weight's going to affect the uh magnitude here. It's going to uh possibly affect the uh mechanical mode of this plate hanging out in the breeze here.

**Dave Jones:** And let's start that again and see how this one performs. That's not too shabby at all. And it's going to get better and better as we build up more data there with the averages.

**Dave Jones:** But yep, that's a really schmick response, is it not? Now, what happens if we move this all the way out to the end here? So, that that wasn't there before, was it?

**Dave Jones:** So, if we slide that back, yeah, you can see, yeah, it is very different. So, that was causing, down at about 10 hertz there or something, um yeah, that was causing an issue, definitely, just by having it out there like that.

**Dave Jones:** And this is smart enough to know that if I try and measure coherence without turning averaging on, yeah, nah, you can't do that. And as I mentioned before, the coherence is actually related to the cross spectrum, and they're mathematically they are actually different, but we can actually do a cross spectrum measurement as well, and you'll notice that it's fairly linear, but we won't go into cross spectral analysis versus

**Dave Jones:** coherence, but suffice it to say, they are intimately related. Pop quiz, hot shot. We've got our nice response like this, it's all happening, exactly what we've seen before. Now, I'm going to change something, see if you can spot the difference.

**Dave Jones:** Check this out, there's something horrible happening at like what, 65 hertz there? Something like that, right? Pretty awful. You might think, "Oh, there's something wrong with my thing." Or, if you've actually got your a second accelerometer on your uh product, on your actual PCB, and you're getting your response, and this is what all this coherence is about.

**Dave Jones:** If you're getting this response, you might think that your product is doing that. But it's not, it's not your product, it's not the jig. What has changed? Well, it's the auto range.

**Dave Jones:** Your input values matter, cuz we're actually clipping. You might have seen there that we're getting an overload on channel two here, which was the accelerometer input. Now, if we put it back to auto range to range it properly, bingo, we go back to exactly where we were before.

**Dave Jones:** And this is the importance of coherence. There's all sorts of factors that can go into this. It's not just the physical jig um itself, the physical mounting and everything else.

**Dave Jones:** You have to ensure that your entire system is set up correctly because at the moment we're just testing the response of this uh plate and you would leave a reference accelerometer on the plate.

**Dave Jones:** But, this is just setting the system up. Then you'd add a second accelerometer onto your actual product or multiple accelerometers onto your product and you'll get your various frequency sweeps to see if they meet some uh you know, military uh performance vibration standard or whatever it is you're in-house company standards.

**Dave Jones:** Doesn't matter what it is. You'll get a response on here and you might see all these dips and everything else and you might think, "Ooh, I've got some mechanical resonance in my product.

**Dave Jones:** Oh, I better redesign it quick. Panic." And no, you just haven't set up your jig properly. And that's the importance of coherence here. This is why I was saying if you don't have your coherence data with your report of your test results of your product, then it's worthless cuz it shows that you have not put any thought into setting up your vibrational test system.

**Dave Jones:** And your data that you get out of your accelerometer your product is absolutely worthless. It doesn't matter how calibrated your accelerometers and charge amplifiers and your uh shaker electrodynamic shakers.

**Dave Jones:** Doesn't matter a rat. So, until now we've been playing around with uh that random generator, but we can't actually do a sweep. So, what I got is an external function generator here.

**Dave Jones:** I'm actually going to set it up for a 30-second sweep here from uh 10 hertz to 200 hertz, which is our uh frequency range of interest. There we go.

**Dave Jones:** Starts out slow. Starts out slow and over 30 seconds it will sweep. So, let me start our acquisition. Let's have a look. And because we're only at one frequency, it's you'll find that it's going to slowly sweep across like this.

**Dave Jones:** And eventually, 30 seconds later, it will have swept all the way across, and we will actually get coherence values. Now, this is showing a real interesting result now. Here we go.

**Dave Jones:** It's getting 150. It's almost at 200 Hz here. And boom. And then it can give you of course keep doing its RMS averaging or what not. But look at all these notches that we've got here.

**Dave Jones:** What's going on? Once again, this is a gross example of where you might get a response that you might think's coming from your product, but it's not. It's because you haven't set up your sampling system correctly, so can you guess what the problem is here?

**Dave Jones:** I'm going to change something here on our signal gen, and we'll do it again. It's similar, but more frequent. Okay, I changed it yet again. And look at this.

**Dave Jones:** Our coherence I actually started it a bit late there. And look, we're getting this little wiggle wiggle wiggle wiggle yeah in that signal. Check it out. Look at that.

**Dave Jones:** That's interesting, isn't it? What's going on here? Is this some sort of little micro resonant thing happening in here? What's going on? Well, for those who were paying attention that it took a bit longer, you would have realized that I was changing the sweep time.

**Dave Jones:** It started out as 30 seconds. Then I increased it to 60. Um and you would have seen that those dropouts we got here were doubling in frequency when I changed from 30 to 60 seconds.

**Dave Jones:** So, it's a function of our record length and sample time in our DSA compared to our sweep speed that we're actually doing this at. Um so, yeah, this makes a huge difference in the measurement.

**Dave Jones:** And if you just whack your accelerometers on your product and started getting your sweep and thinking that you're getting getting the correct values because you've got your whiz-bang expensive calibrated accelerometers and software and everything, uh no.

**Dave Jones:** If you haven't set up the system correctly, you can get all sorts of wibbly-wobbly stuff that has absolutely no correlation to the product that you're actually testing. I was getting sick of the tape here, so I've actually uh super glued it on now.

**Dave Jones:** I should have done that from the start. Now, check this out. I'm actually setting a sweep time now that is uncorrelated with the uh anything to do with the sample rate.

**Dave Jones:** So, 7.7 seconds sweep time, just a random number. If I start a new sample, so this is 7.7 seconds uh sweep time, and you'll notice that right it's all over the shop, but eventually this will get better and better as we do more averages, and because it's uncorrelated time-wise, then slowly we're going to build up a complete picture.

**Dave Jones:** So, you can see it there. Yeah, it's slowly building up a complete picture of this thing. Now, I'm not saying this is uh the the correct uh method uh to do it.

**Dave Jones:** I'm just like showing this as an example of how you can have like a sampling and other um time correlation errors which will cause a drop in your coherence.

**Dave Jones:** There we go. We're almost got the the basically the full response of this thing now. So, time and sampling correlation is yet and phase correlation as well, as I mentioned, can be another um source of error that you can get in your measured signal that if you don't do this coherence measurement test, you'll never be able to see it.

**Dave Jones:** The coherence test is a definitive way to show that you've got no errors in your system or you know, as few errors uh as possible in your system before you actually start your proper quantitative measurement.

**Dave Jones:** Here's another example of uh error that we're getting in. You can see that the response is not that great. Here is it. It's like it's glued on. This response is supposed to be really nice.

**Dave Jones:** Can you spot the error? Maybe you can hear the error. It's these damn screws rattling around cuz I haven't tied them up. Tighten them back up. Start that again.

**Dave Jones:** And you'll see that our response is much nicer. We didn't get all this random noise and crap in there, which then would have gone through onto our output uh signal.

**Dave Jones:** All of that crap was happening cuz we had loosey-goosey um stuff on our setup here. And when you're setting up your system like this and getting your coherence measurements, it can matter that whether or not you've got your actual product that you want to test on your shaker table because it has extra mass, it can change the dynamic properties of the shaker, which you can introduce non-linearity into your

**Dave Jones:** system. And look, I haven't changed anything else. All I've done is screw on that PCB there, and we've got this huge notch here at what, you know, 32 hertz or something like that.

**Dave Jones:** Like it's it's terrible. And then, when you go to put your accelerometer on your product here, um you're going to get all these weird and wonderful results that you didn't expect.

**Dave Jones:** And you might think that you have like a design modal mechanical problem in your product that you're actually testing when you don't. It's your setup. Sure, this is like an extreme example with it flapping around in the breeze, but hopefully that gives you a good example of what can happen here.

**Dave Jones:** So, there you go. I hope you found that interesting, the importance of coherence measurement. So, when next time when somebody shows you their test results for their vibration uh test that they've done for their product, oh, look at this.

**Dave Jones:** Ask them, "Hey, where's your coherence data?" Cuz it ain't worth jack unless you've set up your system properly. So, there you go. I hope you found that really interesting.

**Dave Jones:** Coherence, this is not something that you'll learn in school. Basically, you'll only learn this hands-on. I guarantee you will learn about coherence the very first day you start trying to do vibration testing on everything and your results go to crap and you're wondering what the hell happens then you discover the world of coherence and setting up your jigs and characterizing your test jigs properly so that you know

**Dave Jones:** the results are going to be good. And anytime you change anything, in fact, anytime you do a measurement, you should do a coherence test first to make sure sanity check your results are what you expect.

**Dave Jones:** Because there's so many errors that can go into introducing non-linearity into your test system. Once you get non-linearity, your measurement output data, you don't know whether or not it's real or aha, imaginary.

**Dave Jones:** Get it? You know, real and imaginary complex I'm here all week. Anyway, hope you found that interesting and valuable. If you did, please give it a big thumbs up and as always you can discuss down below and as always EEVblog forum always sort of stuff and all the different channels I'm on.

**Dave Jones:** I'm on every platform. Catch you next time.
