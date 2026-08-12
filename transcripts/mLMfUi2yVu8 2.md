---
video_id: mLMfUi2yVu8
title: EEVblog #49 - Decibels (dB's) for Engineers - A Tutorial
url: https://www.youtube.com/watch?v=mLMfUi2yVu8
source: youtube-asr
timestamps: {"0": 0, "1": 38, "2": 56, "3": 94, "4": 121, "5": 158, "6": 196, "7": 222, "8": 248, "9": 283, "10": 303, "11": 320, "12": 353, "13": 390, "14": 417, "15": 459, "16": 491, "17": 523, "18": 557, "19": 599, "20": 635, "21": 668, "22": 705, "23": 725, "24": 760, "25": 794, "26": 820, "27": 856, "28": 887, "29": 905, "30": 924, "31": 945, "32": 968, "33": 1007, "34": 1026, "35": 1062, "36": 1085, "37": 1115, "38": 1135, "39": 1171, "40": 1202, "41": 1221, "42": 1236}
---

**Dave Jones:** Hi, welcome to the EEVblog an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host Dave Jones. Hi, today we're going to talk about DBs, decibels, because I've had a few people comment about what exactly I mean when I talk about DBs in my blog. I might say the minus 3 dB bandwidth of an oscilloscope or something like that or I might say something 6 dB down or I might say the roll-off of an amplifier is minus 20 dB per decade or something like that.

**Dave Jones:** But, what does that mean? Because beginners seem to get confused with DBs. They seem to think they're some weird, you know, abstract mathematical thing that's all complex and but no, DBs are really easy. They're one of the easiest concepts in electronics.

**Dave Jones:** So, what the heck is a dB? Well, a dB is a decibel. What the hell's a decibel? Well, a decibel is 1/10 of a bell because deci is a one it means 1/10 and a bell is a very old unit which nobody gives a toss about anymore. But, decibels are important because it gives us engineers a way of expressing large values and numbers and working with large values and numbers without making it really cumbersome. The first thing you have to learn about the dB is that it's not really a unit like

**Dave Jones:** volts or ohms or amps or something like that. The a dB is a ratio. It is just a it's a it's a ratio of two numbers, basically. So, it's like saying something is half of something else. It's 0.5 times, you know, if I've got 1 V and something is 0.5 times that 1 volt, right? 0.5 is a ratio, just like a dB.

**Dave Jones:** And in this case, 0.5 is actually -6 dB. Instead of being linear, like saying 0.5, we say -6 dB because dBs are a logarithmic ratio. It has to do with logarithms. Now, I won't go into logarithms and all the math and all that sort of crap, but uh there are some advantages, as you'll see, to talking in terms of dBs instead of 0.5 or 1/10,000 or 1 millionth times or 1 1 billionth of something. You're better off talking in terms of dB when it comes to engineering. And really,

**Dave Jones:** that's all there is to it. dBs are easy. It's just a ratio of one number to another number, usually a reference uh number, a reference level, like 1 volt or, you know, 1 mW or something like that, as we'll go into. But dBs are no more complex than that. It's just another way, a more convenient way sometimes, of expressing a ratio of two numbers. Now, there's two different types of uh formula. One is only for power, when you're talking in terms of watts, okay? Power is the formula the dB

**Dave Jones:** ratio is 10 times log of power 1 / power 2. Now, this power 2 is actually can actually be a reference level. In fact, that's basically what it is. You're comparing this number to this reference value, and it gives you a ratio, a power ratio in dBs. And the same for magnitude, voltage and current.

**Dave Jones:** Uh the ratio in dBs is equal to 20 times log voltage or current uh on the second voltage or current. And once again, this is the bottom one is a reference value that you're working from. And, that's all there is to it. These two formulas, you can do everything in dBs in engineering, and that's all you need to know. Simple.

**Dave Jones:** And, of course, there's different types of logarithms. When we're talking about dBs, we're always talking in terms of uh a base 10 logarithm, not a natural logarithm to base e, okay? Let's go through a simple example that you might get it typically in electronics. Let's say you've got an amplifier like this, and you feed in a fixed amplitude sine wave. It's con- Let's just assume it's absolutely constant over all frequencies. The amplitude is constant, okay? And, you measure the amplitude of the output sine wave on

**Dave Jones:** with either a multimeter or an oscilloscope or anything you like. Now, what you Let's say you measure that at 1 kHz. That's your reference level, for example. And, you might measure 1 V, okay? So, remember the V2 over here is your reference level. So, that's 1 V, okay?

**Dave Jones:** Whoop. 1 V. And, let's say you wind up the frequency on your function generator, and it goes to 100 kHz or something like that. And, you might measure a value now of 0.5 V, okay? So, that's your that's your other number.

**Dave Jones:** So, now you've got these two numbers, and you want to compare them. Well, obviously, uh the signal is down by 0.5, okay? It's, you know, it's a half, right? And, and that's a very convenient number to work with, but it doesn't sound very funky, right? In electronics, you've got to have things we talk in terms of dB. And, because it's just nicer when things get more complex. So, let's convert it to dBs. You got 0.5 V on 1 V, okay? And you do log 20 * log of that,

**Dave Jones:** and it's actually equal, you'll find if you get out your calculator, which you won't have to, which we'll talk about, okay? It's actually minus six, minus six DB. So, you can say that that signal is minus six DB at that frequency compared to the other frequency. Or in other engineering parlance, you say it's six DB down. Okay, let's take a look at an example where DBs start becoming useful. Okay, let's say that we've got a system here with three amplifiers in series, okay? Three amplifiers cascaded,

**Dave Jones:** and the first one has a gain of times two, okay? The next one has a gain of gain of times 10, and the next one has a gain of times 31.6. Now, if you want to work out what's the total gain out from input to output, okay? You've got to multiply these together, and well, that's not too hard, okay, with these numbers, but they could be weird they could be harder numbers, okay? And you've got to multiply them.

**Dave Jones:** You get a total gain of 632. But if you convert these to DBs, you'll find it's actually easier. So, if you convert these ratios into DBs, times two is actually six DB if you use the formula which we had before. Times 10 is actually 20 DB, and times 31.6 happens to be 30 DB. And where we multiplied these before, the good thing the really neat thing about DBs is that now you just add them together. 6 + 20 + 30 is 56 DB, and that's your total gain. Is And

**Dave Jones:** if you actually convert 56 DB back into using that formula in reverse back into a ratio you get 632. And that's the advantage of dBs is that you can actually, instead of multiplying things, you add them in dBs. And the same as dividing things in in regular ratios in dBs you subtract them. So it's easier to do calculations and the numbers are smaller and more manageable.

**Dave Jones:** Let's take a look at a really good example we can see the benefit of dBs and in this case it's dB scaling. Now this is a spectrum analyzer. You're you're probably familiar with the spectrum analyzer it displays amplitude versus frequency. Now if you've got say a 1 MHz signal into your spectrum analyzer you expect to see a line on the display like that and if it's 1 V amplitude you expect to see a volt. Now what you might want to do is well a typical thing with a spectrum analyzer

**Dave Jones:** is you want to view where the noise floor is. Now let's say the noise floor is at 10 microvolts for example. Now 10 microvolts okay that's 1/100,000 of 1 V. So if you've got a linear axis on your volts display like this you have to divide this into 100,000 little you know things and then your noise is going to be so far down here it's it's 1/100,000.

**Dave Jones:** Okay it's less than the width of the one fiber on the tip of this pen. It's tiny. Okay? So you can't possibly see it. You won't be able to display large values sorry small values of noise in at the on the same scale as large values. Now here's where dBs come in. If you convert that into If you make this into a log scale, okay, in dBs in dBV, okay, 1 V, okay, that's 0 dB is your reference level, and then you divide into -10 dB, -20, and so on, and

**Dave Jones:** you get down to say -100 down here. Now, 100,000 10 microvolts, which we were looking at before, is actually, if you convert it, it's actually -100 dB. So, you will actually be able to see it. You'll see your noise down here, and you'll see your signal like that. And bingo, it allows you dB scaling allows you to view small signals at the same in in the same space as large signals, and that's the real benefit of dBs. One of the huge benefits.

**Dave Jones:** Okay, let's give you yet another example of a frequency response of an amplifier, which is a very typical application. And let's say you want to plot the frequency response, okay? You've seen a frequency response of an amplifier. It might look something like that, okay? Now, it, you know, it rolls off at some low frequency, and it rolls off at some high frequency, and its gain is pretty much constant at, you know, 1 or 1 V, say, right in the, you know, somewhere in the middle. Now, this can actually span

**Dave Jones:** frequency responses of amplifiers can span very large ranges, or what we call lots of decades. Now, um it can span anywhere, you know, from basically 1 Hz up to say 1 MHz, and that is six decades. Now, if you try and plot six decades, if you have 1 MHz up here, if you divide that once again into a million little things, you can't see anything down at this end down here. If your signal starts rolling off at, you know, 10 hertz or something like that, it's going to

**Dave Jones:** your actual response is going to look something like this. And you're actually going to see something like that. Now, you can't see any detail down here. So, what you do is you compress it using decibels into what are called decades. So, that's 1 hertz, okay?

**Dave Jones:** 1 hertz, and then you go to 10 hertz, and then you go to 100 hertz, and then you go to 1 kilohertz, and then you go to 10 kilohertz, 100, and so on. These are decades, and if you have this scale, your x-axis in dBs or what you call it or what they call a log scale as opposed to a linear scale, then it allows you to once again show detail at the extreme ends of your frequency spectrum. So, it allows you to once again view

**Dave Jones:** large numbers in the presence of small numbers, and that's the beauty of dBs. Now, I actually put up two real screenshots here for you of two frequency responses. Now, you can see this first one, this is using a linear scale, and well, look at that, right from zero to 1 megahertz, it's, you know, what is that, right? It's certainly not linear, like that is not a straight line, and you can't see any detail down at zero megahertz, right? Or zero hertz, you can't see any detail at

**Dave Jones:** all. But, if you take that same at the exact same frequency response, and you plot it on a log axis or a dB axis with six decades like this, bingo. That's the exact same data and you can see that it starts rolling off at about 100 h and goes down. And in this case, it's 25 dB down. There we go.

**Dave Jones:** We're using the jargon. 25 dB down at around about that 1 h figure. And you can see it's about 20 dB down at 1 MHz. And you'll notice that the slopes of those lines are actually straight. They're linear when you plot them on a logarithmic axis. Go figure. And that allows you to say to that allows you to easily determine the roll-off of an amplifier. In this case, it's going to be about 20 odd dB per decade. And there you go.

**Dave Jones:** Okay, let's look at some rules of thumb, some ways you can work with dBs without using your silly calculator. Okay? These are numbers ratios which you should remember, which will make working with dBs real easy for you. Now, if you're talking in terms of magnitudes, which is probably most I dare I say most of the time in electronics when you're dealing with voltages and and signal levels and things like that, you'll be dealing with magnitude. So you'll be using the 20 log formula. Remember that. Now, what you

**Dave Jones:** have to remember, minus 3 dB is 0.707, which is one on the square root of two. You may have seen that before. It might be familiar to you. Now, that's what's called the half power point. And we'll actually see that down here. Minus 3 dB for a power is 0.5.

**Dave Jones:** Now, it's called the half power point because the basically if that voltage into a resistor is going to be half the power what it is at if you put 1 V into into the same resistor. So that's why they call it the half power point.

**Dave Jones:** And they use that for things to determine like the minus 3 dB bandwidth of an oscilloscope or an amplifier. They use it it's a it's kind of an industry convention to use the half power point, but it's actually 0.707 times the voltage.

**Dave Jones:** Now, the other one you got to remember is 6 dB. Now, minus 6 dB is 0.5. So, it's half of something. Okay? Now, similarly, plus 6 dB equals two times something. So, if something's double something else, if you you know, if 2 V is twice as high as 1 V, then it's 6 dB.

**Dave Jones:** Easy. And the same thing with minus 20 dB. It's 0.1. And conversely, so it's 1/10 of something. Conversely, plus 20 dB equals 10 times something or an order of magnitude bigger. So, if something There's another engineering buzzword for you. Order of magnitude is 10 times bigger or 1/10. Now, that's real easy to do. Now, okay, why why do you have to remember these? Because it allows you to do simple basic calculations. Let's say if something is 1,000 times bigger than something else in magnitude.

**Dave Jones:** Okay? Don't get out your calculator and and plug in 1,000 and do the log and everything. No. You can just add dBs. Remember, plus 20 dB is 10 times. So, 20 each decimal point, 40 60. So, 1,000 equals 60 dB.

**Dave Jones:** Easy. And the same thing with let's say you had 1 mV. Okay? 1 mV is same thing. 20 40 60 dB equals minus 60 dB. Piece of cake. Now, if you're talking in terms of power, okay, or intensity like sound intensity or something like that, then minus 3 dB is half the power or the same with plus 3 dB equals double the power, twice the power. And minus 10 is 1/10 the power.

**Dave Jones:** And same thing again, plus 10 dB equals 10 times the power. Simple. Rules of thumb. You don't need your damn calculator. Think you can do dBs in your head and you can impress people cuz a lot of people just don't realize that you can do dBs simply by, you know, how many decimal places and adding them up and remembering a few simple things.

**Dave Jones:** Now, I mentioned before that dBs are just a ratio. They don't have any units. And you might see something like this. You might see minus 6 dB. Well, what does that mean on its own? Well, it actually means absolutely nothing. It's a useless bit of information because you can assume it's a magnitude, for example, in which case it's going to be 0.5, but 0.5 of what? I mean, half a rabbit? What, you know, it could be anything. So, it's a useless bit of information. So, you can actually get a

**Dave Jones:** reference which appends to the end of it. In this case, you might see minus 6 dBV. And in this case, V is actually an industry standard um thing and it's 1 V. So, in this case, minus 6 dB equals 0.5 uh minus 6 dBV is 0.5 V.

**Dave Jones:** And uh same thing again, you can Well, so that actually means something on its own. It's actually got inherent value cuz there's a reference attached to the end of it. And you might also see something like minus 3 dBm. In this case, m is an industry standard reference for 1 mW. So, it's -3 dB relative to 1 mW, which is going to be 0.5 mW like that. Easy. And there's a whole slew of these industry standard terms out there. There's, you know, there's probably a couple of dozen standard

**Dave Jones:** ones, but there's hundreds. Or you can even make up your own. I've made up stuff that I'm sure nobody's ever done before. So, uh just go check them out. dB references. Now, there's only one tricky thing with logs that you have to remember, or you have to be aware of. You've got to be aware of whether you're working with a power or a magnitude. In this case, uh dBV, as we've mentioned, is a volt. So, it's a magnitude. So, you know you've got to use the 20

**Dave Jones:** log formula. You You You know you're dealing with that formula. But, if you see dBm, as I said, is mW. So, it's a power. So, you know you're going to be working with the 10 log formula. So, you know, just be careful, cuz that's really the only major trap with dBs.

**Dave Jones:** So, start using dBs in your everyday life as well. Take the classic half a glass of water. Is it half full or is it half empty? Are you an optimist or a pessimist? Well, I'm an engineer, so it's 6 dB down.

**Dave Jones:** Cheers. And yes, check it out. This is a triple five timer t-shirt. Isn't it cool? It's part of the new EEVblog merchandise. Pick yourself up one.
