---
video_id: 0UksWKuVFFo
title: EEVblog #61 - Crystal Oscillator Drift
url: https://www.youtube.com/watch?v=0UksWKuVFFo
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 35, "3": 50, "4": 69, "5": 84, "6": 100, "7": 114, "8": 134, "9": 149, "10": 162, "11": 175, "12": 190, "13": 211, "14": 226, "15": 245, "16": 260, "17": 274, "18": 293, "19": 311, "20": 325, "21": 340, "22": 358, "23": 374, "24": 387, "25": 403, "26": 414, "27": 429, "28": 447, "29": 461, "30": 478, "31": 493, "32": 507, "33": 525, "34": 540, "35": 556, "36": 576, "37": 590, "38": 606, "39": 621, "40": 638, "41": 651, "42": 668, "43": 684, "44": 705, "45": 721, "46": 737, "47": 757, "48": 774, "49": 786, "50": 802, "51": 818, "52": 831, "53": 844, "54": 857, "55": 869, "56": 884, "57": 899, "58": 914, "59": 929, "60": 945, "61": 962, "62": 977, "63": 992, "64": 1013, "65": 1030, "66": 1045, "67": 1059, "68": 1075, "69": 1090, "70": 1102, "71": 1119, "72": 1135, "73": 1150, "74": 1165, "75": 1182, "76": 1197, "77": 1211, "78": 1224, "79": 1243, "80": 1256, "81": 1270, "82": 1284, "83": 1302, "84": 1320, "85": 1338, "86": 1356, "87": 1373, "88": 1391, "89": 1407, "90": 1422, "91": 1440}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's industry story time again, but this time it's mixed with a a bit of theory and circuit design. This time

**Dave Jones:** around it's about crystal oscillator stability and drift over time, and I think you might find it rather interesting. Quite a few years ago now, I was working on some ocean bottom seismic recording equipment. Now, what this is, they're actually these

**Dave Jones:** autonomous units, battery powered, they're, you know, several feet long and they have a huge battery pack and they have a little data logger and recorder, and they've got a hydrophone, and which measures, basically hydrophones are an underwater microphone, and they've got

**Dave Jones:** an XYZ tilt sensor as well. And basically what they do is they you drop them down in into the deep ocean and they sit on the ocean floor, and they measure, they measure the seismic activity that actually happens from a boat. Now,

**Dave Jones:** this is how it actually works out in the field, right? Here's the ocean up here, okay? You've got a survey a seismic survey vessel up the top, and it's got one of these acoustic pingers on it, a big, a huge noise source which

**Dave Jones:** generates these big bangs, these impulses which travel down to the ocean floor down here. Now, if this is the ocean floor, these autonomous recording units, they actually spread you don't just use one. What you do is you spread

**Dave Jones:** them out, you know, 50 m apart, 100 m apart, something like that, across the ocean floor like this, and you would put down a whole bunch of of them, dozens, hundreds, that actually sit down on the ocean floor and they'd stay there

**Dave Jones:** continuously recording for up to several months. And I would sample the the hydrophone just waiting for these acoustic ping signals that actually travel through the ocean floor and then reflect back up. And you can actually determine oil where fine where oil is and things

**Dave Jones:** like that. And it's quite fascinating. You've got these underwater robotic vehicles which will actually take them down and they'll deploy them in certain locations. They'll know the location of each one. And then after a couple of months, well,

**Dave Jones:** during the couple of months the boat will, you know, troll around the ocean going bang bang bang generating all these noise sources which are picked up by the all these autonomous ocean bottom recorders. And after a couple of months,

**Dave Jones:** before the batteries run out, they send the rover back down, they pick up these units, bring them back on deck, and they they synchronize them and they suck the data out of them. And that's what I'm going to talk about.

**Dave Jones:** Now, the trick with these sort of ocean bottom recording systems is that the recording has to be synchronous across all these units. But they're autonomous. They can't they can't talk to each other and they run from their own independent

**Dave Jones:** free-running clock oscillators. So, what these things need are really accurate internal oscillators calibrated to GPS time when when you deploy them and then they run on their own internal free-running oscillator, each one of them. Now, they it's very important that they all

**Dave Jones:** sample at the same time a sample at a sample rate of anywhere from a couple of hundred hertz up to several kilohertz. And this is continuous for several months. Now, over that time the internal clocks inside these units can drift. And that

**Dave Jones:** causes they can either drift up in frequency, down in frequency, whatever due to the tolerance, the stability of the crystal oscillator in them. Now, this beacon can become really problematic when you try and post analyze the data um because if the samples are if you've

**Dave Jones:** got several channels like this, okay, and then you've got sample points here and this one's here and this one's over here and this one's over here, they're all supposed to line up perfectly like that. But you don't. When the oscillator

**Dave Jones:** is drift, you end up getting um you know, they they can be all over the place like that. And there's a maximum um there's all complex math and theory theory involved, but um really uh you can only tolerate a certain amount

**Dave Jones:** of this um drift or instability in in any one of these oscillators over time before the data becomes essentially useless. Now, you can try and correct for this uh drift as I'll explain, but um really it's important to get as low a um drift

**Dave Jones:** in all these um oscillators as possible over the several months that they sit on the ocean floor. Now, with these ocean bottom recorders, there's a big trade-off between battery life and the stability of the oscillator. You can't just whack in a

**Dave Jones:** super duper precision oscillator if, you know, some some rubidium oscillator or something like that cuz it chews too much power. These things have to sit on the ocean bottom for a couple of months. And the data, massive amount of data

**Dave Jones:** over that time, so it's got to be stored on hard drives at the time. You could probably do it on solid state drives these days which draw a bit less power, but still very power hungry things to actually store all this data and and

**Dave Jones:** have a high precision oscillator. So, let's look at several oscillator technologies. We've basically we the standard crystal oscillator XO. Now, they typically have a typical accuracy stability. I won't go into the difference between stability and drift and aging all that sort of stuff

**Dave Jones:** because that's just makes it too complicated but they're basically what's called 10 ppm parts per million. That is the traditional measure of the stability and accuracy of an oscillator and that's can also be written as 10 to the minus five

**Dave Jones:** because as you can see one ppm is 10 to the minus six one part per million 10 to the minus six is a one millionth. So, so that's how it is. Now, the next type is and then you know, you might use

**Dave Jones:** these standard crystal oscillator. You've seen them. You use them on your to power your picker your at mail micro or something else. So, they they're not very accurate at all. Now, the next type is the temperature controlled crystal oscillator TCXO.

**Dave Jones:** That's what stands for and they're a bit better. They can they're roughly in the order of one ppm or 10 to the minus six. Now, the next type but that's still not good enough. If you do the math, it's

**Dave Jones:** still not good enough for these ocean bottom survey things. We need something better. We need something in the order of 10 to the minus eight for our ocean bottom application. Now, the next type of device is the digital temperature

**Dave Jones:** compensated crystal oscillator or digitally temperature controlled crystal oscillator and they they're in the order of 0.1 to 0.01 ppm 10 to the minus seven to 10 to the minus eight. Aha, that's what's that is suitable for our ocean bottom or

**Dave Jones:** it should be roughly but we'll go into that later. The next type is the traditional they've been around a long time these ones the oven controlled crystal oscillator and they're they're basically the same as the DTCXO which is

**Dave Jones:** a more modern technology. They're 0.1 to 0.01 ppm. And then you've got rubidium oscillators, which are becoming more like a primary um atomic standard. They're, you know, they're much better than um 10 to the minus nine or 0.001

**Dave Jones:** ppm, one part per billion, actually. Um but these are rubidium oscillator. Not only are they quite um uh fragile, uh but they're actually they consume, you know, tens of watts. Huge amount of power. We couldn't even afford that sort

**Dave Jones:** of power. Now, the oven-controlled oscillator, they're typically um 1 to 5 watts or something like that. That's how much power they use. That was too much for us. This thing's got to last for 3 months on the ocean floor. So, we used

**Dave Jones:** this new technology, DTCXO. It had uh the one we actually used had uh 0.03 um ppm was its basic um stability, and that was fairly close to what we wanted. Now, a DTCXO is a is a fairly uh complex

**Dave Jones:** bit of thing, and they're actually quite expensive. It's got a built-in microcontroller, and um what it does is that um they're individually calibrated at all temperature points over the entire range. They're stored in the micro, and then the micro actually

**Dave Jones:** adjusts the frequency of the oscillator based on the current temperature. And it basically takes out um it basically flattens out the temperature characteristic curve of the actual crystal used in there. And um and they do actually work quite well. The

**Dave Jones:** technology is quite good. Now, here's where the story comes in. We weren't quite sure, even the manufacturer couldn't tell us the actual uh long-term drift characteristics of a digitally temperature-controlled crystal oscillator or any oscillator for that matter. It's quite hard information to

**Dave Jones:** actually get, um, let alone measure. So, we thought we'd, um, we had to come up with a way to actually measure the drift over time of one of these oscillators to actually see if it was good enough for

**Dave Jones:** our application and if it wasn't, could we correct for it in post-processing software? Now, when you're looking at the drift of an oscillator or it's changing its absolute frequency over time, uh, you basically have to compare it against

**Dave Jones:** something. You need a reference. Um, so let's just assume we've got a perfect reference. Now, um, if you have if you plot the, um, the drift characteristics or the or the aging characteristics or anything of an of a, uh, crystal

**Dave Jones:** oscillator, you will get and a perfect one, you would get a flat line over time. Time is, you know, hours, days, weeks, whatever. It'll have zero drift over time. But, they, you know, that's you can't get a perfect oscillator like

**Dave Jones:** that, a perfect crystal. So, what you're going to get is you're going to get some sort of drift over time like this. Now, it can actually be in either direction because you don't actually know which direction it's going to be, but let's

**Dave Jones:** just say it's in the positive direction like this. Now, it'd be ideal if this drift over time was completely linear. It was straight like this because then what you can do is you can actually, um, when you start your, uh, data logging,

**Dave Jones:** you can, um, get a real accurate time date stamp at the start of it using a precision rubidium GPS locked rubidium standard, you know, orders of magnitude better than the oscillator you're actually using, right? You calibrate it at the start and then when you get it

**Dave Jones:** back, you actually, um, calibrate it at the end and you flatten it out, okay? You calculate the difference between the um the true time that um you get from your precision reference against the recorded time, and you basically can offset that. You know how

**Dave Jones:** far it's drifted if it's drifted, you know, 20 seconds over the order of 2 days or something like that. You can actually correct it, which has the um which will actually have the process of flattening this curve out. It brings it

**Dave Jones:** down here. So, this curve drift, you can actually correct it and make it flat like that, perfectly flat. And that's ideal. But, a crystal oscillator is never actually flat like that over time. And we're not talking about temperature

**Dave Jones:** variation here, either. Even at a perfectly fixed temperature that does not vary over days, weeks, and months, the oscillator will not drift linear like that. It'll actually have um a typical characteristic, which will be like that. Or it could be like that. Or

**Dave Jones:** it can even reverse itself sometimes and go like that. But, it typically has a sort of a a you know, a quarter sinusoidal or a half sinusoidal um envelope to it. Now, um so, when you do your correction at

**Dave Jones:** the end, as I said, when you do your it's often called a a skew correction or a time correction, you end up with not that straight curve, but you end up with this curve down here like this. So,

**Dave Jones:** you don't know what your data has done during, you know, 5 days ago or something like that. So, it's really that's a real problem. So, we had to measure what this maximum drift over time was at a fixed frequency. So,

**Dave Jones:** that's what we did. Now, measuring clock drift over time is actually quite an obscure measurement. Hardly anyone ever needs to do it. Um, especially when you have to compensate it at the start and the end and then correct for this drift over time, it's

**Dave Jones:** something quite specific to the um to the uh seismic industries which I was working in. There's probably a few other industries where it matters as well, but um it's it's quite a specific problem and you can't just buy a bit of

**Dave Jones:** equipment even from a company like Agilent who make gear for everything. Can't just walk in and buy a bit of kit, stick your oscillator on it, and it tells you the dri- it tells you the maximum drift over time. It just, you

**Dave Jones:** know, you can't really get such a thing. So, uh we decided to actually um to make our own. We really had no choice. And so, this is the idea I came up with for measuring clock drift. Now, there's

**Dave Jones:** probably more than one way to skin a cat here, but this is the idea I came up with for measuring clock drift, and this is how we did it. Okay? We basically had a rubidium standard reference oscillator, and this was like, as I

**Dave Jones:** said, you know, 10 to the power of minus 11 or something like that, super accurate. For all practical purposes, it can be considered an absolute um frequency reference. And that normally is available at 10 MHz, but we divided

**Dave Jones:** it down to an 8 kHz signal for reasons of well, for several technical reasons, but um uh which I won't really go into cuz it's not worth it. Now, um the we our DTXO we were trying to measure here, um

**Dave Jones:** we actually divided that down to 96 kHz. Once again, for technical reasons that um aren't really important. Now, what we're trying to do here is measure, okay? This is an absolute reference, okay? Now, the 96 kHz signal we're

**Dave Jones:** trying to measure will drift with time back and forth. It's It's doesn't just go in one direction. It can drift back and forth. So, these clock edges, when you first start them, when you first calibrate them, they're spot-on. But, it will

**Dave Jones:** slowly just drift with time in either direction. And we need to measure that. So, how do you do it? So, what you do is you actually have a sample clock, a high-frequency sample clock going continuously like this, and

**Dave Jones:** you count the number of pulses between this start point. Okay, you use your you use your frequency reference, the rising edge of that as a start point for a counter here, and then you count the number of pulses until the first rising

**Dave Jones:** edge of the signal you're trying to measure. And then, at the end of it, you will have X number of counts. You might have, say, you know, 30 counts or something like that to actually, um, measure that the difference between that

**Dave Jones:** edge and that edge. Now, that gives you the difference in time, but you need to track that, how it's trending, how it's drifting, how this signal is drifting back or forth compared to this signal. So, what you do is you actually, um,

**Dave Jones:** divide this entire cycle here, okay, into four Well, I chose to do it into four quadrants like this: A, B, C, and D. Now, where this counter, um, finished, a 30 will put it in quadrant A, like that.

**Dave Jones:** But, then you then you would sample again at at this point here, but then you'd start the process again at the next, um, cycle of your reference clock. And you would you would see it in this first case, it might be 30 counts, and then it

**Dave Jones:** might be the next one, it might be 50 counts, and you know it's moved from from a quadrant A to quadrant B. So, you you can actually see it drifting in that direction. And likewise, if the count if

**Dave Jones:** the next one goes back down to 30, you know it's drifted back in the other direction. Now, because there's there's going to be jitter here, okay? The the actual signal you're trying to measure could jitter back and forth, and you

**Dave Jones:** don't want those to count as part of the drift. You only want to see it moving one direction or the next. So, what you do is you ignore anything that any counts which go between two quadrants like this. And you only count

**Dave Jones:** when it goes when it travels from one quadrant through another quadrant to the next one. And then, if it did that if you see it drift between three quadrants, you would increment a um count and up or a down

**Dave Jones:** count. You would increment that by one if it's going in this direction. And then if it's going the opposite direction, you would um you would actually um get plus one for the down count. It's going in the opposite

**Dave Jones:** direction. So, and then you timestamp all of these things. You timestamp every time you get one of these pulses. And then, you can actually count you log these on a PC over the hours, days, and months. And bingo, you can actually see

**Dave Jones:** it drift in comparison to your reference. And you know exactly which direction it's going and at what time and how fast. And then, you can actually get a plot. So, here's how you implement that as a basic circuit. This is how I

**Dave Jones:** did it. You got your 10 MHz rubidium reference coming in here. You divide it down, in this case to 8 kHz, which goes into the enable of a counter, a binary counter. And the signal you're trying to measure, 96 kHz, goes into a latch

**Dave Jones:** flip-flop, which then resets the counter. And the counter is clocked from the 10 MHz reference. So, what that gives you is what we saw on the previous thing. You got your 8 kHz reference like this, and then your 96 kHz, and your

**Dave Jones:** counter uh it counts between the clock edges of the two signals, and then it repeats, and then you have a microcontroller here, which just reads when it's finished the count, and then it determines whether or not this 96 kHz

**Dave Jones:** signal has drifted in that direction, or has drifted in that direction, or has just stayed still. And if it's drifted a certain amount in one direction, it'll increment the fast It'll give an output on this fast um It'll give a pulse on

**Dave Jones:** this fast output if it's drifted in the slow direction, it'll give an output on the slow pulse. And if it's drifting too fast, i.e. it goes through more than two of those quadrants at once, well, that indicates that there's something grossly

**Dave Jones:** wrong, and it gives you an error pulse as well. So, you know if it's, you know, something's gone completely screwy with your measurements. And then, you just have a data logger PC, which sits there and timestamps these signals coming out,

**Dave Jones:** and bingo, you can get a a graph of drift over time. Magic. So, what did we see when we actually measured a bunch of these oscillators over the span of days and weeks and even a month, um how much drift did we actually see, and

**Dave Jones:** what did the characteristic look like? Well, it's exactly what we expected basically. Well, we actually didn't know what to expect at the start of this, but we knew with um further research, we actually knew that this is a typical

**Dave Jones:** characteristic of what to expect. We actually found that it, you know, it had it had it had actually jumped back and forth. It's not smooth. It would have characteristic and it jump around like this, and it might go down like that,

**Dave Jones:** and another one might go, you know, drift like this, and another one might go in this direction like this, and another might go like that, maybe. And this would be over the span of, you know, days or weeks or

**Dave Jones:** even a month and 2 months is the longest recording period we actually did. And this was at constant temperature. And of course, this result is actually um skew corrected. We've actually corrected the slope of that we've actually corrected the time as I

**Dave Jones:** mentioned before. And you still get this characteristic drift over time. And that's what this is all about. Crystal oscillators are not stable with time. And we're not just talking temperature variations. These variations are due they're actually inherent in the quartz

**Dave Jones:** crystal itself. And as you also see in probably another blog I'm going to do on this is that this characteristic can also reset itself and change based on vibration and shock of the quartz crystal itself, which is another interesting

**Dave Jones:** characteristic. And basically, we realized that they all sort of fit a this generic sort of you know, half sinusoidal envelope. So we were actually able to come up with a based on a whole bunch of empirical measured data, we're able to

**Dave Jones:** come up with a a a formula for our maximum drift over time. And we found that it was, you know, it was within basically what the customer could tolerate. So we found that we were actually capable of post processing this

**Dave Jones:** signal, correcting it, and and bingo! And then getting the data we needed. So that's how we got away with using these cheap and and very low power which was the key for us DTCO modules in our ocean bottom seismic

**Dave Jones:** survey gear. They drifted but because we did all this empirical measurements and came up with a curve fit formula and came up with techniques to actually correct the data when they were resynchronized when they came up on the boat, we found that the error was

**Dave Jones:** within side the customer's required tolerance and they could use our system and everyone was happy. So it worked out really well and it's a rather interesting thing which most people will never get to deal with. Clock drift and clock

**Dave Jones:** drift correction and well it's just something you might need to be aware of one day. Quartz crystal oscillators drift and they can drift outside of temperature. They can drift just due to their inherent characteristics of the crystal itself, all sorts of factors

**Dave Jones:** they're involved away going into the physics of it. It's it's very deep to actually try and understand it and shock and vibration and all sorts of other things. So crystals aren't as simple as they appear.
