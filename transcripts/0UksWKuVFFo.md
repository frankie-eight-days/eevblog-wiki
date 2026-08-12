---
video_id: 0UksWKuVFFo
title: EEVblog #61 - Crystal Oscillator Drift
url: https://www.youtube.com/watch?v=0UksWKuVFFo
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 30, "3": 50, "4": 66, "5": 90, "6": 118, "7": 134, "8": 145, "9": 160, "10": 171, "11": 183, "12": 206, "13": 217, "14": 233, "15": 257, "16": 283, "17": 300, "18": 318, "19": 327, "20": 340, "21": 364, "22": 381, "23": 393, "24": 410, "25": 419, "26": 441, "27": 461, "28": 478, "29": 493, "30": 505, "31": 522, "32": 536, "33": 552, "34": 573, "35": 597, "36": 606, "37": 626, "38": 638, "39": 654, "40": 680, "41": 701, "42": 718, "43": 735, "44": 747, "45": 769, "46": 783, "47": 799, "48": 824, "49": 835, "50": 846, "51": 855, "52": 863, "53": 873, "54": 892, "55": 905, "56": 919, "57": 927, "58": 948, "59": 965, "60": 977, "61": 989, "62": 1005, "63": 1022, "64": 1035, "65": 1050, "66": 1062, "67": 1072, "68": 1090, "69": 1101, "70": 1116, "71": 1130, "72": 1145, "73": 1159, "74": 1187, "75": 1201, "76": 1213, "77": 1227, "78": 1245, "79": 1256, "80": 1279, "81": 1293, "82": 1304, "83": 1323, "84": 1338, "85": 1359, "86": 1376, "87": 1391, "88": 1412, "89": 1427, "90": 1441}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's industry story time again, but this time it's mixed with a a bit of theory and circuit design.

**Dave Jones:** This time around it's about crystal oscillator stability and drift over time, and I think you might find it rather interesting. Quite a few years ago now, I was working on some ocean bottom seismic recording equipment.

**Dave Jones:** Now, what this is, they're actually these autonomous units, battery powered, they're, you know, several feet long and they have a huge battery pack and they have a little data logger and recorder, and they've got a hydrophone, and which measures, basically hydrophones are an underwater microphone, and they've got an XYZ tilt sensor as well.

**Dave Jones:** And basically what they do is they you drop them down in into the deep ocean and they sit on the ocean floor, and they measure, they measure the seismic activity that actually happens from a boat.

**Dave Jones:** Now, this is how it actually works out in the field, right? Here's the ocean up here, okay? You've got a survey a seismic survey vessel up the top, and it's got one of these acoustic pingers on it, a big, a huge noise source which generates these big bangs, these impulses which travel down to the ocean floor down here.

**Dave Jones:** Now, if this is the ocean floor, these autonomous recording units, they actually spread you don't just use one. What you do is you spread them out, you know, 50 m apart, 100 m apart, something like that, across the ocean floor like this, and you would put down a whole bunch of of them, dozens, hundreds, that actually sit down on the ocean floor and they'd stay there continuously recording for up to several

**Dave Jones:** months. And I would sample the the hydrophone just waiting for these acoustic ping signals that actually travel through the ocean floor and then reflect back up. And you can actually determine oil where fine where oil is and things like that.

**Dave Jones:** And it's quite fascinating. You've got these underwater robotic vehicles which will actually take them down and they'll deploy them in certain locations. They'll know the location of each one.

**Dave Jones:** And then after a couple of months, well, during the couple of months the boat will, you know, troll around the ocean going bang bang bang generating all these noise sources which are picked up by the all these autonomous ocean bottom recorders.

**Dave Jones:** And after a couple of months, before the batteries run out, they send the rover back down, they pick up these units, bring them back on deck, and they they synchronize them and they suck the data out of them.

**Dave Jones:** And that's what I'm going to talk about. Now, the trick with these sort of ocean bottom recording systems is that the recording has to be synchronous across all these units.

**Dave Jones:** But they're autonomous. They can't they can't talk to each other and they run from their own independent free-running clock oscillators. So, what these things need are really accurate internal oscillators calibrated to GPS time when when you deploy them and then they run on their own internal free-running oscillator, each one of them.

**Dave Jones:** Now, they it's very important that they all sample at the same time a sample at a sample rate of anywhere from a couple of hundred hertz up to several kilohertz.

**Dave Jones:** And this is continuous for several months. Now, over that time the internal clocks inside these units can drift. And that causes they can either drift up in frequency, down in frequency, whatever due to the tolerance, the stability of the crystal oscillator in them.

**Dave Jones:** Now, this beacon can become really problematic when you try and post analyze the data um because if the samples are if you've got several channels like this, okay, and then you've got sample points here and this one's here and this one's over here and this one's over here, they're all supposed to line up perfectly like that.

**Dave Jones:** But you don't. When the oscillator is drift, you end up getting um you know, they they can be all over the place like that. And there's a maximum um there's all complex math and theory theory involved, but um really uh you can only tolerate a certain amount of this um drift or instability in in any one of these oscillators over time before the data becomes essentially useless.

**Dave Jones:** Now, you can try and correct for this uh drift as I'll explain, but um really it's important to get as low a um drift in all these um oscillators as possible over the several months that they sit on the ocean floor.

**Dave Jones:** Now, with these ocean bottom recorders, there's a big trade-off between battery life and the stability of the oscillator. You can't just whack in a super duper precision oscillator if, you know, some some rubidium oscillator or something like that cuz it chews too much power.

**Dave Jones:** These things have to sit on the ocean bottom for a couple of months. And the data, massive amount of data over that time, so it's got to be stored on hard drives at the time.

**Dave Jones:** You could probably do it on solid state drives these days which draw a bit less power, but still very power hungry things to actually store all this data and and have a high precision oscillator.

**Dave Jones:** So, let's look at several oscillator technologies. We've basically we the standard crystal oscillator XO. Now, they typically have a typical accuracy stability. I won't go into the difference between stability and drift and aging all that sort of stuff because that's just makes it too complicated but they're basically what's called 10 ppm parts per million.

**Dave Jones:** That is the traditional measure of the stability and accuracy of an oscillator and that's can also be written as 10 to the minus five because as you can see one ppm is 10 to the minus six one part per million 10 to the minus six is a one millionth.

**Dave Jones:** So, so that's how it is. Now, the next type is and then you know, you might use these standard crystal oscillator. You've seen them. You use them on your to power your picker your at mail micro or something else.

**Dave Jones:** So, they they're not very accurate at all. Now, the next type is the temperature controlled crystal oscillator TCXO. That's what stands for and they're a bit better. They can they're roughly in the order of one ppm or 10 to the minus six.

**Dave Jones:** Now, the next type but that's still not good enough. If you do the math, it's still not good enough for these ocean bottom survey things. We need something better.

**Dave Jones:** We need something in the order of 10 to the minus eight for our ocean bottom application. Now, the next type of device is the digital temperature compensated crystal oscillator or digitally temperature controlled crystal oscillator and they they're in the order of 0.1 to 0.01 ppm 10 to the minus seven to 10 to the minus eight.

**Dave Jones:** Aha, that's what's that is suitable for our ocean bottom or it should be roughly but we'll go into that later. The next type is the traditional they've been around a long time these ones the oven controlled crystal oscillator and they're they're basically the same as the DTCXO which is a more modern technology.

**Dave Jones:** They're 0.1 to 0.01 ppm. And then you've got rubidium oscillators, which are becoming more like a primary um atomic standard. They're, you know, they're much better than um 10 to the minus nine or 0.001 ppm, one part per billion, actually.

**Dave Jones:** Um but these are rubidium oscillator. Not only are they quite um uh fragile, uh but they're actually they consume, you know, tens of watts. Huge amount of power. We couldn't even afford that sort of power.

**Dave Jones:** Now, the oven-controlled oscillator, they're typically um 1 to 5 watts or something like that. That's how much power they use. That was too much for us. This thing's got to last for 3 months on the ocean floor.

**Dave Jones:** So, we used this new technology, DTCXO. It had uh the one we actually used had uh 0.03 um ppm was its basic um stability, and that was fairly close to what we wanted.

**Dave Jones:** Now, a DTCXO is a is a fairly uh complex bit of thing, and they're actually quite expensive. It's got a built-in microcontroller, and um what it does is that um they're individually calibrated at all temperature points over the entire range.

**Dave Jones:** They're stored in the micro, and then the micro actually adjusts the frequency of the oscillator based on the current temperature. And it basically takes out um it basically flattens out the temperature characteristic curve of the actual crystal used in there.

**Dave Jones:** And um and they do actually work quite well. The technology is quite good. Now, here's where the story comes in. We weren't quite sure, even the manufacturer couldn't tell us the actual uh long-term drift characteristics of a digitally temperature-controlled crystal oscillator or any oscillator for that matter.

**Dave Jones:** It's quite hard information to actually get, um, let alone measure. So, we thought we'd, um, we had to come up with a way to actually measure the drift over time of one of these oscillators to actually see if it was good enough for our application and if it wasn't, could we correct for it in post-processing software?

**Dave Jones:** Now, when you're looking at the drift of an oscillator or it's changing its absolute frequency over time, uh, you basically have to compare it against something. You need a reference.

**Dave Jones:** Um, so let's just assume we've got a perfect reference. Now, um, if you have if you plot the, um, the drift characteristics or the or the aging characteristics or anything of an of a, uh, crystal oscillator, you will get and a perfect one, you would get a flat line over time.

**Dave Jones:** Time is, you know, hours, days, weeks, whatever. It'll have zero drift over time. But, they, you know, that's you can't get a perfect oscillator like that, a perfect crystal.

**Dave Jones:** So, what you're going to get is you're going to get some sort of drift over time like this. Now, it can actually be in either direction because you don't actually know which direction it's going to be, but let's just say it's in the positive direction like this.

**Dave Jones:** Now, it'd be ideal if this drift over time was completely linear. It was straight like this because then what you can do is you can actually, um, when you start your, uh, data logging, you can, um, get a real accurate time date stamp at the start of it using a precision rubidium GPS locked rubidium standard, you know, orders of magnitude better than the oscillator you're actually using, right?

**Dave Jones:** You calibrate it at the start and then when you get it back, you actually, um, calibrate it at the end and you flatten it out, okay? You calculate the difference between the um the true time that um you get from your precision reference against the recorded time, and you basically can offset that.

**Dave Jones:** You know how far it's drifted if it's drifted, you know, 20 seconds over the order of 2 days or something like that. You can actually correct it, which has the um which will actually have the process of flattening this curve out.

**Dave Jones:** It brings it down here. So, this curve drift, you can actually correct it and make it flat like that, perfectly flat. And that's ideal. But, a crystal oscillator is never actually flat like that over time.

**Dave Jones:** And we're not talking about temperature variation here, either. Even at a perfectly fixed temperature that does not vary over days, weeks, and months, the oscillator will not drift linear like that.

**Dave Jones:** It'll actually have um a typical characteristic, which will be like that. Or it could be like that. Or it can even reverse itself sometimes and go like that. But, it typically has a sort of a a you know, a quarter sinusoidal or a half sinusoidal um envelope to it.

**Dave Jones:** Now, um so, when you do your correction at the end, as I said, when you do your it's often called a a skew correction or a time correction, you end up with not that straight curve, but you end up with this curve down here like this.

**Dave Jones:** So, you don't know what your data has done during, you know, 5 days ago or something like that. So, it's really that's a real problem. So, we had to measure what this maximum drift over time was at a fixed frequency.

**Dave Jones:** So, that's what we did. Now, measuring clock drift over time is actually quite an obscure measurement. Hardly anyone ever needs to do it. Um, especially when you have to compensate it at the start and the end and then correct for this drift over time, it's something quite specific to the um to the uh seismic industries which I was working in.

**Dave Jones:** There's probably a few other industries where it matters as well, but um it's it's quite a specific problem and you can't just buy a bit of equipment even from a company like Agilent who make gear for everything.

**Dave Jones:** Can't just walk in and buy a bit of kit, stick your oscillator on it, and it tells you the dri- it tells you the maximum drift over time. It just, you know, you can't really get such a thing.

**Dave Jones:** So, uh we decided to actually um to make our own. We really had no choice. And so, this is the idea I came up with for measuring clock drift.

**Dave Jones:** Now, there's probably more than one way to skin a cat here, but this is the idea I came up with for measuring clock drift, and this is how we did it.

**Dave Jones:** Okay? We basically had a rubidium standard reference oscillator, and this was like, as I said, you know, 10 to the power of minus 11 or something like that, super accurate.

**Dave Jones:** For all practical purposes, it can be considered an absolute um frequency reference. And that normally is available at 10 MHz, but we divided it down to an 8 kHz signal for reasons of well, for several technical reasons, but um uh which I won't really go into cuz it's not worth it.

**Dave Jones:** Now, um the we our DTXO we were trying to measure here, um we actually divided that down to 96 kHz. Once again, for technical reasons that um aren't really important.

**Dave Jones:** Now, what we're trying to do here is measure, okay? This is an absolute reference, okay? Now, the 96 kHz signal we're trying to measure will drift with time back and forth.

**Dave Jones:** It's It's doesn't just go in one direction. It can drift back and forth. So, these clock edges, when you first start them, when you first calibrate them, they're spot-on.

**Dave Jones:** But, it will slowly just drift with time in either direction. And we need to measure that. So, how do you do it? So, what you do is you actually have a sample clock, a high-frequency sample clock going continuously like this, and you count the number of pulses between this start point.

**Dave Jones:** Okay, you use your you use your frequency reference, the rising edge of that as a start point for a counter here, and then you count the number of pulses until the first rising edge of the signal you're trying to measure.

**Dave Jones:** And then, at the end of it, you will have X number of counts. You might have, say, you know, 30 counts or something like that to actually, um, measure that the difference between that edge and that edge.

**Dave Jones:** Now, that gives you the difference in time, but you need to track that, how it's trending, how it's drifting, how this signal is drifting back or forth compared to this signal.

**Dave Jones:** So, what you do is you actually, um, divide this entire cycle here, okay, into four Well, I chose to do it into four quadrants like this: A, B, C, and D.

**Dave Jones:** Now, where this counter, um, finished, a 30 will put it in quadrant A, like that. But, then you then you would sample again at at this point here, but then you'd start the process again at the next, um, cycle of your reference clock.

**Dave Jones:** And you would you would see it in this first case, it might be 30 counts, and then it might be the next one, it might be 50 counts, and you know it's moved from from a quadrant A to quadrant B.

**Dave Jones:** So, you you can actually see it drifting in that direction. And likewise, if the count if the next one goes back down to 30, you know it's drifted back in the other direction.

**Dave Jones:** Now, because there's there's going to be jitter here, okay? The the actual signal you're trying to measure could jitter back and forth, and you don't want those to count as part of the drift.

**Dave Jones:** You only want to see it moving one direction or the next. So, what you do is you ignore anything that any counts which go between two quadrants like this.

**Dave Jones:** And you only count when it goes when it travels from one quadrant through another quadrant to the next one. And then, if it did that if you see it drift between three quadrants, you would increment a um count and up or a down count.

**Dave Jones:** You would increment that by one if it's going in this direction. And then if it's going the opposite direction, you would um you would actually um get plus one for the down count.

**Dave Jones:** It's going in the opposite direction. So, and then you timestamp all of these things. You timestamp every time you get one of these pulses. And then, you can actually count you log these on a PC over the hours, days, and months.

**Dave Jones:** And bingo, you can actually see it drift in comparison to your reference. And you know exactly which direction it's going and at what time and how fast. And then, you can actually get a plot.

**Dave Jones:** So, here's how you implement that as a basic circuit. This is how I did it. You got your 10 MHz rubidium reference coming in here. You divide it down, in this case to 8 kHz, which goes into the enable of a counter, a binary counter.

**Dave Jones:** And the signal you're trying to measure, 96 kHz, goes into a latch flip-flop, which then resets the counter. And the counter is clocked from the 10 MHz reference. So, what that gives you is what we saw on the previous thing.

**Dave Jones:** You got your 8 kHz reference like this, and then your 96 kHz, and your counter uh it counts between the clock edges of the two signals, and then it repeats, and then you have a microcontroller here, which just reads when it's finished the count, and then it determines whether or not this 96 kHz signal has drifted in that direction, or has drifted in that direction, or has

**Dave Jones:** just stayed still. And if it's drifted a certain amount in one direction, it'll increment the fast It'll give an output on this fast um It'll give a pulse on this fast output if it's drifted in the slow direction, it'll give an output on the slow pulse.

**Dave Jones:** And if it's drifting too fast, i.e. it goes through more than two of those quadrants at once, well, that indicates that there's something grossly wrong, and it gives you an error pulse as well.

**Dave Jones:** So, you know if it's, you know, something's gone completely screwy with your measurements. And then, you just have a data logger PC, which sits there and timestamps these signals coming out, and bingo, you can get a a graph of drift over time.

**Dave Jones:** Magic. So, what did we see when we actually measured a bunch of these oscillators over the span of days and weeks and even a month, um how much drift did we actually see, and what did the characteristic look like?

**Dave Jones:** Well, it's exactly what we expected basically. Well, we actually didn't know what to expect at the start of this, but we knew with um further research, we actually knew that this is a typical characteristic of what to expect.

**Dave Jones:** We actually found that it, you know, it had it had it had actually jumped back and forth. It's not smooth. It would have characteristic and it jump around like this, and it might go down like that, and another one might go, you know, drift like this, and another one might go in this direction like this, and another might go like that, maybe.

**Dave Jones:** And this would be over the span of, you know, days or weeks or even a month and 2 months is the longest recording period we actually did. And this was at constant temperature.

**Dave Jones:** And of course, this result is actually um skew corrected. We've actually corrected the slope of that we've actually corrected the time as I mentioned before. And you still get this characteristic drift over time.

**Dave Jones:** And that's what this is all about. Crystal oscillators are not stable with time. And we're not just talking temperature variations. These variations are due they're actually inherent in the quartz crystal itself.

**Dave Jones:** And as you also see in probably another blog I'm going to do on this is that this characteristic can also reset itself and change based on vibration and shock of the quartz crystal itself, which is another interesting characteristic.

**Dave Jones:** And basically, we realized that they all sort of fit a this generic sort of you know, half sinusoidal envelope. So we were actually able to come up with a based on a whole bunch of empirical measured data, we're able to come up with a a a formula for our maximum drift over time.

**Dave Jones:** And we found that it was, you know, it was within basically what the customer could tolerate. So we found that we were actually capable of post processing this signal, correcting it, and and bingo!

**Dave Jones:** And then getting the data we needed. So that's how we got away with using these cheap and and very low power which was the key for us DTCO modules in our ocean bottom seismic survey gear.

**Dave Jones:** They drifted but because we did all this empirical measurements and came up with a curve fit formula and came up with techniques to actually correct the data when they were resynchronized when they came up on the boat, we found that the error was within side the customer's required tolerance and they could use our system and everyone was happy.

**Dave Jones:** So it worked out really well and it's a rather interesting thing which most people will never get to deal with. Clock drift and clock drift correction and well it's just something you might need to be aware of one day.

**Dave Jones:** Quartz crystal oscillators drift and they can drift outside of temperature. They can drift just due to their inherent characteristics of the crystal itself, all sorts of factors they're involved away going into the physics of it.

**Dave Jones:** It's it's very deep to actually try and understand it and shock and vibration and all sorts of other things. So crystals aren't as simple as they appear.
