---
video_id: mLMfUi2yVu8
title: EEVblog #49 - Decibels (dB's) for Engineers - A Tutorial
url: https://www.youtube.com/watch?v=mLMfUi2yVu8
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 38, "3": 52, "4": 72, "5": 97, "6": 117, "7": 132, "8": 151, "9": 172, "10": 185, "11": 201, "12": 215, "13": 239, "14": 249, "15": 262, "16": 275, "17": 289, "18": 303, "19": 314, "20": 327, "21": 338, "22": 359, "23": 374, "24": 392, "25": 406, "26": 417, "27": 430, "28": 448, "29": 468, "30": 482, "31": 496, "32": 517, "33": 533, "34": 557, "35": 573, "36": 599, "37": 617, "38": 630, "39": 647, "40": 665, "41": 683, "42": 694, "43": 711, "44": 733, "45": 756, "46": 773, "47": 783, "48": 794, "49": 806, "50": 820, "51": 834, "52": 848, "53": 860, "54": 883, "55": 894, "56": 905, "57": 920, "58": 933, "59": 947, "60": 968, "61": 982, "62": 997, "63": 1011, "64": 1029, "65": 1059, "66": 1085, "67": 1094, "68": 1104, "69": 1117, "70": 1135, "71": 1145, "72": 1162, "73": 1173, "74": 1187, "75": 1197, "76": 1205, "77": 1221, "78": 1231, "79": 1246}
---

**Dave Jones:** Hi, welcome to the EEVblog an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host Dave Jones. Hi, today we're going to talk about DBs, decibels, because I've had a few people comment about what exactly I mean when I talk about DBs in my blog.

**Dave Jones:** I might say the minus 3 dB bandwidth of an oscilloscope or something like that or I might say something 6 dB down or I might say the roll-off of an amplifier is minus 20 dB per decade or something like that.

**Dave Jones:** But, what does that mean? Because beginners seem to get confused with DBs. They seem to think they're some weird, you know, abstract mathematical thing that's all complex and but no, DBs are really easy.

**Dave Jones:** They're one of the easiest concepts in electronics. So, what the heck is a dB? Well, a dB is a decibel. What the hell's a decibel? Well, a decibel is 1/10 of a bell because deci is a one it means 1/10 and a bell is a very old unit which nobody gives a toss about anymore.

**Dave Jones:** But, decibels are important because it gives us engineers a way of expressing large values and numbers and working with large values and numbers without making it really cumbersome. The first thing you have to learn about the dB is that it's not really a unit like volts or ohms or amps or something like that.

**Dave Jones:** The a dB is a ratio. It is just a it's a it's a ratio of two numbers, basically. So, it's like saying something is half of something else. It's 0.5 times, you know, if I've got 1 V and something is 0.5 times that 1 volt, right?

**Dave Jones:** 0.5 is a ratio, just like a dB. And in this case, 0.5 is actually -6 dB. Instead of being linear, like saying 0.5, we say -6 dB because dBs are a logarithmic ratio.

**Dave Jones:** It has to do with logarithms. Now, I won't go into logarithms and all the math and all that sort of crap, but uh there are some advantages, as you'll see, to talking in terms of dBs instead of 0.5 or 1/10,000 or 1 millionth times or 1 1 billionth of something.

**Dave Jones:** You're better off talking in terms of dB when it comes to engineering. And really, that's all there is to it. dBs are easy. It's just a ratio of one number to another number, usually a reference uh number, a reference level, like 1 volt or, you know, 1 mW or something like that, as we'll go into.

**Dave Jones:** But dBs are no more complex than that. It's just another way, a more convenient way sometimes, of expressing a ratio of two numbers. Now, there's two different types of uh formula.

**Dave Jones:** One is only for power, when you're talking in terms of watts, okay? Power is the formula the dB ratio is 10 times log of power 1 / power 2.

**Dave Jones:** Now, this power 2 is actually can actually be a reference level. In fact, that's basically what it is. You're comparing this number to this reference value, and it gives you a ratio, a power ratio in dBs.

**Dave Jones:** And the same for magnitude, voltage and current. Uh the ratio in dBs is equal to 20 times log voltage or current uh on the second voltage or current. And once again, this is the bottom one is a reference value that you're working from.

**Dave Jones:** And, that's all there is to it. These two formulas, you can do everything in dBs in engineering, and that's all you need to know. Simple. And, of course, there's different types of logarithms.

**Dave Jones:** When we're talking about dBs, we're always talking in terms of uh a base 10 logarithm, not a natural logarithm to base e, okay? Let's go through a simple example that you might get it typically in electronics.

**Dave Jones:** Let's say you've got an amplifier like this, and you feed in a fixed amplitude sine wave. It's con- Let's just assume it's absolutely constant over all frequencies. The amplitude is constant, okay?

**Dave Jones:** And, you measure the amplitude of the output sine wave on with either a multimeter or an oscilloscope or anything you like. Now, what you Let's say you measure that at 1 kHz.

**Dave Jones:** That's your reference level, for example. And, you might measure 1 V, okay? So, remember the V2 over here is your reference level. So, that's 1 V, okay? Whoop. 1 V.

**Dave Jones:** And, let's say you wind up the frequency on your function generator, and it goes to 100 kHz or something like that. And, you might measure a value now of 0.5 V, okay?

**Dave Jones:** So, that's your that's your other number. So, now you've got these two numbers, and you want to compare them. Well, obviously, uh the signal is down by 0.5, okay?

**Dave Jones:** It's, you know, it's a half, right? And, and that's a very convenient number to work with, but it doesn't sound very funky, right? In electronics, you've got to have things we talk in terms of dB.

**Dave Jones:** And, because it's just nicer when things get more complex. So, let's convert it to dBs. You got 0.5 V on 1 V, okay? And you do log 20 * log of that, and it's actually equal, you'll find if you get out your calculator, which you won't have to, which we'll talk about, okay?

**Dave Jones:** It's actually minus six, minus six DB. So, you can say that that signal is minus six DB at that frequency compared to the other frequency. Or in other engineering parlance, you say it's six DB down.

**Dave Jones:** Okay, let's take a look at an example where DBs start becoming useful. Okay, let's say that we've got a system here with three amplifiers in series, okay? Three amplifiers cascaded, and the first one has a gain of times two, okay?

**Dave Jones:** The next one has a gain of gain of times 10, and the next one has a gain of times 31.6. Now, if you want to work out what's the total gain out from input to output, okay?

**Dave Jones:** You've got to multiply these together, and well, that's not too hard, okay, with these numbers, but they could be weird they could be harder numbers, okay? And you've got to multiply them.

**Dave Jones:** You get a total gain of 632. But if you convert these to DBs, you'll find it's actually easier. So, if you convert these ratios into DBs, times two is actually six DB if you use the formula which we had before.

**Dave Jones:** Times 10 is actually 20 DB, and times 31.6 happens to be 30 DB. And where we multiplied these before, the good thing the really neat thing about DBs is that now you just add them together.

**Dave Jones:** 6 + 20 + 30 is 56 DB, and that's your total gain. Is And if you actually convert 56 DB back into using that formula in reverse back into a ratio you get 632.

**Dave Jones:** And that's the advantage of dBs is that you can actually, instead of multiplying things, you add them in dBs. And the same as dividing things in in regular ratios in dBs you subtract them.

**Dave Jones:** So it's easier to do calculations and the numbers are smaller and more manageable. Let's take a look at a really good example we can see the benefit of dBs and in this case it's dB scaling.

**Dave Jones:** Now this is a spectrum analyzer. You're you're probably familiar with the spectrum analyzer it displays amplitude versus frequency. Now if you've got say a 1 MHz signal into your spectrum analyzer you expect to see a line on the display like that and if it's 1 V amplitude you expect to see a volt.

**Dave Jones:** Now what you might want to do is well a typical thing with a spectrum analyzer is you want to view where the noise floor is. Now let's say the noise floor is at 10 microvolts for example.

**Dave Jones:** Now 10 microvolts okay that's 1/100,000 of 1 V. So if you've got a linear axis on your volts display like this you have to divide this into 100,000 little you know things and then your noise is going to be so far down here it's it's 1/100,000.

**Dave Jones:** Okay it's less than the width of the one fiber on the tip of this pen. It's tiny. Okay? So you can't possibly see it. You won't be able to display large values sorry small values of noise in at the on the same scale as large values.

**Dave Jones:** Now here's where dBs come in. If you convert that into If you make this into a log scale, okay, in dBs in dBV, okay, 1 V, okay, that's 0 dB is your reference level, and then you divide into -10 dB, -20, and so on, and you get down to say -100 down here.

**Dave Jones:** Now, 100,000 10 microvolts, which we were looking at before, is actually, if you convert it, it's actually -100 dB. So, you will actually be able to see it. You'll see your noise down here, and you'll see your signal like that.

**Dave Jones:** And bingo, it allows you dB scaling allows you to view small signals at the same in in the same space as large signals, and that's the real benefit of dBs.

**Dave Jones:** One of the huge benefits. Okay, let's give you yet another example of a frequency response of an amplifier, which is a very typical application. And let's say you want to plot the frequency response, okay?

**Dave Jones:** You've seen a frequency response of an amplifier. It might look something like that, okay? Now, it, you know, it rolls off at some low frequency, and it rolls off at some high frequency, and its gain is pretty much constant at, you know, 1 or 1 V, say, right in the, you know, somewhere in the middle.

**Dave Jones:** Now, this can actually span frequency responses of amplifiers can span very large ranges, or what we call lots of decades. Now, um it can span anywhere, you know, from basically 1 Hz up to say 1 MHz, and that is six decades.

**Dave Jones:** Now, if you try and plot six decades, if you have 1 MHz up here, if you divide that once again into a million little things, you can't see anything down at this end down here.

**Dave Jones:** If your signal starts rolling off at, you know, 10 hertz or something like that, it's going to your actual response is going to look something like this. And you're actually going to see something like that.

**Dave Jones:** Now, you can't see any detail down here. So, what you do is you compress it using decibels into what are called decades. So, that's 1 hertz, okay? 1 hertz, and then you go to 10 hertz, and then you go to 100 hertz, and then you go to 1 kilohertz, and then you go to 10 kilohertz, 100, and so on.

**Dave Jones:** These are decades, and if you have this scale, your x-axis in dBs or what you call it or what they call a log scale as opposed to a linear scale, then it allows you to once again show detail at the extreme ends of your frequency spectrum.

**Dave Jones:** So, it allows you to once again view large numbers in the presence of small numbers, and that's the beauty of dBs. Now, I actually put up two real screenshots here for you of two frequency responses.

**Dave Jones:** Now, you can see this first one, this is using a linear scale, and well, look at that, right from zero to 1 megahertz, it's, you know, what is that, right?

**Dave Jones:** It's certainly not linear, like that is not a straight line, and you can't see any detail down at zero megahertz, right? Or zero hertz, you can't see any detail at all.

**Dave Jones:** But, if you take that same at the exact same frequency response, and you plot it on a log axis or a dB axis with six decades like this, bingo.

**Dave Jones:** That's the exact same data and you can see that it starts rolling off at about 100 h and goes down. And in this case, it's 25 dB down. There we go.

**Dave Jones:** We're using the jargon. 25 dB down at around about that 1 h figure. And you can see it's about 20 dB down at 1 MHz. And you'll notice that the slopes of those lines are actually straight.

**Dave Jones:** They're linear when you plot them on a logarithmic axis. Go figure. And that allows you to say to that allows you to easily determine the roll-off of an amplifier.

**Dave Jones:** In this case, it's going to be about 20 odd dB per decade. And there you go. Okay, let's look at some rules of thumb, some ways you can work with dBs without using your silly calculator.

**Dave Jones:** Okay? These are numbers ratios which you should remember, which will make working with dBs real easy for you. Now, if you're talking in terms of magnitudes, which is probably most I dare I say most of the time in electronics when you're dealing with voltages and and signal levels and things like that, you'll be dealing with magnitude.

**Dave Jones:** So you'll be using the 20 log formula. Remember that. Now, what you have to remember, minus 3 dB is 0.707, which is one on the square root of two.

**Dave Jones:** You may have seen that before. It might be familiar to you. Now, that's what's called the half power point. And we'll actually see that down here. Minus 3 dB for a power is 0.5.

**Dave Jones:** Now, it's called the half power point because the basically if that voltage into a resistor is going to be half the power what it is at if you put 1 V into into the same resistor.

**Dave Jones:** So that's why they call it the half power point. And they use that for things to determine like the minus 3 dB bandwidth of an oscilloscope or an amplifier.

**Dave Jones:** They use it it's a it's kind of an industry convention to use the half power point, but it's actually 0.707 times the voltage. Now, the other one you got to remember is 6 dB.

**Dave Jones:** Now, minus 6 dB is 0.5. So, it's half of something. Okay? Now, similarly, plus 6 dB equals two times something. So, if something's double something else, if you you know, if 2 V is twice as high as 1 V, then it's 6 dB.

**Dave Jones:** Easy. And the same thing with minus 20 dB. It's 0.1. And conversely, so it's 1/10 of something. Conversely, plus 20 dB equals 10 times something or an order of magnitude bigger.

**Dave Jones:** So, if something There's another engineering buzzword for you. Order of magnitude is 10 times bigger or 1/10. Now, that's real easy to do. Now, okay, why why do you have to remember these?

**Dave Jones:** Because it allows you to do simple basic calculations. Let's say if something is 1,000 times bigger than something else in magnitude. Okay? Don't get out your calculator and and plug in 1,000 and do the log and everything.

**Dave Jones:** No. You can just add dBs. Remember, plus 20 dB is 10 times. So, 20 each decimal point, 40 60. So, 1,000 equals 60 dB. Easy. And the same thing with let's say you had 1 mV.

**Dave Jones:** Okay? 1 mV is same thing. 20 40 60 dB equals minus 60 dB. Piece of cake. Now, if you're talking in terms of power, okay, or intensity like sound intensity or something like that, then minus 3 dB is half the power or the same with plus 3 dB equals double the power, twice the power.

**Dave Jones:** And minus 10 is 1/10 the power. And same thing again, plus 10 dB equals 10 times the power. Simple. Rules of thumb. You don't need your damn calculator. Think you can do dBs in your head and you can impress people cuz a lot of people just don't realize that you can do dBs simply by, you know, how many decimal places and adding them up and remembering a few simple things.

**Dave Jones:** Now, I mentioned before that dBs are just a ratio. They don't have any units. And you might see something like this. You might see minus 6 dB. Well, what does that mean on its own?

**Dave Jones:** Well, it actually means absolutely nothing. It's a useless bit of information because you can assume it's a magnitude, for example, in which case it's going to be 0.5, but 0.5 of what?

**Dave Jones:** I mean, half a rabbit? What, you know, it could be anything. So, it's a useless bit of information. So, you can actually get a reference which appends to the end of it.

**Dave Jones:** In this case, you might see minus 6 dBV. And in this case, V is actually an industry standard um thing and it's 1 V. So, in this case, minus 6 dB equals 0.5 uh minus 6 dBV is 0.5 V.

**Dave Jones:** And uh same thing again, you can Well, so that actually means something on its own. It's actually got inherent value cuz there's a reference attached to the end of it.

**Dave Jones:** And you might also see something like minus 3 dBm. In this case, m is an industry standard reference for 1 mW. So, it's -3 dB relative to 1 mW, which is going to be 0.5 mW like that.

**Dave Jones:** Easy. And there's a whole slew of these industry standard terms out there. There's, you know, there's probably a couple of dozen standard ones, but there's hundreds. Or you can even make up your own.

**Dave Jones:** I've made up stuff that I'm sure nobody's ever done before. So, uh just go check them out. dB references. Now, there's only one tricky thing with logs that you have to remember, or you have to be aware of.

**Dave Jones:** You've got to be aware of whether you're working with a power or a magnitude. In this case, uh dBV, as we've mentioned, is a volt. So, it's a magnitude.

**Dave Jones:** So, you know you've got to use the 20 log formula. You You You know you're dealing with that formula. But, if you see dBm, as I said, is mW.

**Dave Jones:** So, it's a power. So, you know you're going to be working with the 10 log formula. So, you know, just be careful, cuz that's really the only major trap with dBs.

**Dave Jones:** So, start using dBs in your everyday life as well. Take the classic half a glass of water. Is it half full or is it half empty? Are you an optimist or a pessimist?

**Dave Jones:** Well, I'm an engineer, so it's 6 dB down. Cheers. And yes, check it out. This is a triple five timer t-shirt. Isn't it cool? It's part of the new EEVblog merchandise.

**Dave Jones:** Pick yourself up one.
