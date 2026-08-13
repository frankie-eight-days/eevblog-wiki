---
video_id: TJcMgoJ4DOE
title: EEVblog 869 - Counting LED Photons!
url: https://www.youtube.com/watch?v=TJcMgoJ4DOE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 24, "2": 45, "3": 65, "4": 89, "5": 104, "6": 120, "7": 138, "8": 157, "9": 174, "10": 187, "11": 203, "12": 215, "13": 235, "14": 258, "15": 286, "16": 299, "17": 315, "18": 330, "19": 343, "20": 359, "21": 373, "22": 388, "23": 400, "24": 414, "25": 435, "26": 462, "27": 482, "28": 506, "29": 526, "30": 542, "31": 562, "32": 582, "33": 602, "34": 618, "35": 630, "36": 650, "37": 666, "38": 686, "39": 702, "40": 718, "41": 738, "42": 754, "43": 766, "44": 782, "45": 798, "46": 814, "47": 830, "48": 842, "49": 858, "50": 870, "51": 886, "52": 910, "53": 930, "54": 958, "55": 974, "56": 994, "57": 1014, "58": 1030, "59": 1042, "60": 1058, "61": 1078, "62": 1094, "63": 1114, "64": 1130, "65": 1146, "66": 1166, "67": 1178, "68": 1194, "69": 1206, "70": 1222, "71": 1246, "72": 1262, "73": 1282, "74": 1302, "75": 1314, "76": 1340, "77": 1356, "78": 1372, "79": 1392, "80": 1408, "81": 1428, "82": 1444, "83": 1464, "84": 1476, "85": 1492, "86": 1508, "87": 1524, "88": 1540, "89": 1560, "90": 1576, "91": 1588, "92": 1604, "93": 1624, "94": 1640, "95": 1660, "96": 1680, "97": 1700, "98": 1716, "99": 1736, "100": 1756, "101": 1772, "102": 1788, "103": 1804, "104": 1820, "105": 1836, "106": 1856, "107": 1868, "108": 1888, "109": 1904, "110": 1916, "111": 1932}
---

**Dave Jones:** Hi, the humble LED, or light-emitting diode, you're no doubt familiar with. And you're also likely familiar with the concept that an LED's light output is roughly linearly proportional, fairly linearly proportional to the amount of current that you put through it. And if you have a look at the data sheet for any LED, you can see that it's pretty much

**Dave Jones:** the intensity versus current is pretty much a linear concept. And that's great, but I got to thinking, what actually happens down at extremely low currents? And in particular, at what current does a typical LED like this red one here actually switch on and start emitting light or start emitting photons?

**Dave Jones:** Hmm, interesting question. Let's test it. So to test this, what we need is a device that allows us to actually not just measure light intensity, but measure essentially small numbers or individual photons. And that's exactly what we've got here. Now this is a reasonably expensive bit of kit I've got here, it's a photon counting module.

**Dave Jones:** And it does exactly what the name tells you, it counts photons. You've seen this in a previous mailbag video. And it's an extremely sensitive photo sensor in here. Basically, it performs similar to or better than a traditional photo multiplier tube. But this allows us to basically feed in a light source here.

**Dave Jones:** So it works by measuring the light input here and giving us a count out here, a pulse every time a photon hits the sensor inside here. So there's no real reason why we can't stick a LED up its clacker here and adjust the current.

**Dave Jones:** I've got a very low current source which can go down to picoamps or even femtoamps if we have to. And count the number of outputs per second or photons per second. Let's give it a burl. Now the part number for this is SPCMAQR13.

**Dave Jones:** And I'll link in the data sheet down below. But if you have the black cap on here, there's no photons getting in there, no light getting in. It'll still actually give you some pulse count outputs, that's called the dark count. And this one actually is supposed to be, not faulty, but it's supposed to have a higher dark count than normal.

**Dave Jones:** But hey, we can actually check that. So this particular model, the AQR13, here's a look at the data sheet. This one has a maximum dark count value of 250 per second, or 200, you know, a nominal base limitation of 250 photons per second.

**Dave Jones:** So, but, you know, we can measure the average of that, null it out, and then stick the LED up as a clacker, and hopefully, you know, see where this LED actually switches on and emits. You know, maybe not an individual photon, because we're down in the noise of the dark count of this thing,

**Dave Jones:** which is going to be random, so we have to do some averaging and try and, you know, do that. But we could probably measure, see a difference in tens of photons, or we should be able to. Tens of photons coming out of this LED.

**Dave Jones:** And for this test, we're going to use my trusty Keithley 225 current source. It can go up, it can go anywhere from, this is the nanoamps, so there's the decimal point, so 0.1 nanoamp up to, we won't go all the way because we'll blow our LED,

**Dave Jones:** but it can go up to 100 milliamps. So we're driving this LED now at 5 milliamps, and of course we can go down, it's going to be decent. 0.1, yeah, we can still see it, not sure if you can, yeah, you can see that on camera.

**Dave Jones:** And, you know, we can go down to microamps, nanoamps, and if that's not good enough, we can use my Keithley 261 picoamp source, which has a resolution of 10 femtoamps. Beauty. If you're just wondering what other sources I have in the lab, well, I also have a matching Keithley 260 nanovolt source,

**Dave Jones:** so, yeah, how many people have a nanovolt source? Nanovolt source, mmm, brilliant. So I can generate femtoamps, picovolts, and I've got high voltage power supplies as well, so I can go anywhere, in terms of voltage, I can go anywhere from picovolts all the way up to, you know, over 1000 volts, just in those two instruments.

**Dave Jones:** Beautiful. Now this might look pretty ridiculous, but I can assure you it's essential. I've wrapped it all in some alfoil here. This was after wrapping the lead, I hooked on, wrapped it in the black electrical tape here, many turns there. Count was a little bit high without the alfoil,

**Dave Jones:** so I just added the alfoil on here, several turns there, and just folded it all over, so it should be nice and dark inside. And that's exactly what we want, so I'm just going to leave it for a bit, and we'll just get an average figure here.

**Dave Jones:** Mean is up to, yeah, around about 214, 215, or something like that. I've got the current source actually switched off at the moment, so, yeah, we'll get an average figure after a couple of more minutes, and then we'll just take that, and then we'll increase the current.

**Dave Jones:** And for those wondering, do the lights in my lab actually make any difference, is it actually seeping in somewhere, somehow? Well, the answer seems to be no. The mean hasn't really changed, I switched my lights off here in the lab, and no, that is the true dark count.

**Dave Jones:** So it looks like our dark count is just, you know, 212, something like that. It is under the data sheet value of 250, so whoever's written on the front of this thing that has a high dark count, nope, seems to be just fine.

**Dave Jones:** Oh, and by the way, this is a, you know, seems to be just fine. Oh, and by the way, this particular Perkin Elmer unit has a peak sensitivity around 650 nanometers. It can do, like, the whole visual range plus in the outer edges as well,

**Dave Jones:** but it's peak sensitivity about 650 nanometers, which is why I'm using a red lead in there to actually do that. So, you know, it's fairly close, should be fairly close to its peak value. So let's have some fun, let's actually ramp up the current and try it.

**Dave Jones:** I have no feel, I haven't done any ballpark calculations for, you know, E equals HF and all that sort of stuff. You can actually hear the efficiency of the lead, which will change down at the bottom end as well. I'll see if I can pull up a, in edit,

**Dave Jones:** I'll see if I can pull up a graph of how the efficiency actually drops off of the LED at very low current. So that'll change your E equals HF formula if you try and calculate all sorts of stuff and things like that, the efficiency of the LED.

**Dave Jones:** So, yeah, anyway, we're not measuring, like, the voltage across the LED and things like that, we could, but yeah, I'm not doing that in this particular experiment. Here we go, so I'll just reset the statistics here, and I'll switch it on, make sure I don't blow the thing,

**Dave Jones:** it's at 0.00 nanoamps. So here we go, we're going to switch it on. So there should be no difference in that. Let's go for one nanoamp. I don't think it's going to do anything, I'd be very surprised. No, no, our count seems to be the same.

**Dave Jones:** Okay, here we go, 10 nanoamps. Hey! No, no, see, got fooled. You've got to use the mean, got to use the mean. No, alright, let's ramp it up a range. So let's go to 100 nanoamps. 100 nanoamps. No, no, it's not looking like it's changing,

**Dave Jones:** I mean, I'm not going to quibble it, you know, I'm not going to muck around with, oh, it's got a, hey! Whoa, what did I do? Whoa! What happened there? Hello? Something happened there, are we right on the threshold? Is the need where that LED will actually come on?

**Dave Jones:** Or not? Because wow, we just jumped up to 1500 photons per second. Wow! Okay, let me ramp that back down to 10. Yeah, I'm back down to 10 nanoamps now. And we're back down to where we were, that's interesting. Okay, I'll ramp it back up to 100.

**Dave Jones:** Actually, it's 110 now. Yeah, there we go. So, okay, back down to 10. It looks like we found it. We found the current at where it starts. Let me go to 20. This is 20 nanoamps. Yeah, look at that! Around about 20 nanoamps.

**Dave Jones:** Yep. Yep, it's starting to go up. I mean, we can reset our stats now. I mean, I'm just looking at the count there and you can sort of see from the count that it's doing that. It's, yeah, there we go. Bingo! About 20 nanoamps is all you need.

**Dave Jones:** Maybe 10, you know, between 10 and 20 nanoamps for this particular LED. Different ones with different, you know, manufacturing with different technologies, with different sensitivities, things like that. There's going to be huge difference. But this is just a, by the way, just a junk bin

**Dave Jones:** eBay kit LED, so I have no idea, don't know what the data sheet is, you know, it's just like, yeah, one I got from eBay in a kit. So, there you go! At 20 nanoamps we're going up, we're getting about 266. So we're about

**Dave Jones:** 42 photons there per second at 20 nanoamps. I'm going to see if we can get some data on this thing. Hmm. Okay, so what I'm going to do is I'm going to go up and graph the data here in 20 nanoamp jumps. So 20, 40, 60, 80,

**Dave Jones:** et cetera. I'll take it over, there we go, a minute 427. So I'll take that count as 427 and I'll try and get a graph of this thing. I just find it amazing that we're actually counting individual photons here. I mean, this is, you know, quantum

**Dave Jones:** physics stuff. How the LED works, you know, the bandgap voltage of, you know, the voltage of the LED in this case, it's probably not 1.8 volts for a typical red LED because we're down at, you know, right at the knee of where the thing switches on.

**Dave Jones:** Well, not the knee where it kicks up, but right down where it just starts emitting the photons and the recombination causes, you know, emission of photons. It's like E equals HF fundamental quantum physics. This is absolutely brilliant. Oh, you could play around with

**Dave Jones:** this sort of stuff all day. And one thing I was curious about, is there any triboelectric effect in the cable? Because I'm actually using a coax cable coming out of my current source here, and just vibration in cables, shock and vibration in cables, it's a legitimate phenomenon

**Dave Jones:** and can actually inject charge into the cable. So I'm just having to play around with it here, and I don't know, it's... it doesn't seem to be any different. So yep, I can't... I don't think I can see anything there, so that's not an issue.

**Dave Jones:** It just popped in my head. Hmm. Yes, I am aware that putting the alfoil over this might change its thermal properties of the cases. The sensor dissipates a fair bit of power, there's little fins in there, but I don't have any airflow here in the lab, so you know

**Dave Jones:** it's not really a big deal. And hey, it's aluminium! No worries! And I know what you're thinking. Dave, this isn't the right tool for the job! Horses for courses, come on! Use the proper tool! Alright, normally I would say that, but there's a little bit of a snag.

**Dave Jones:** Here's my Agilent 53131A universal counter, and in my opinion any lab who does not have a proper universal counter is probably not a fully equipped lab. So you've got to have one of these and ordinarily, yes, this would be the right tool for the job.

**Dave Jones:** Let's plug it in here, and yes, we can measure frequency, of course, that's, you know, it's a frequency counter, right? But the key is in the title. Universal counter, it actually counts stuff. It's got other modes, where... many different modes, you can do phase,

**Dave Jones:** duty cycle, all that sort of jazz, but it's got a totalised mode. It does exactly what you think it does. It counts things, and here it is. And you go into gate, time, and you can actually set the gate time to one second like this.

**Dave Jones:** So there it is. We can actually get our count on this thing. But just like any instrument, you've got to actually set it up properly. And notice we're getting like the 206, 212, or whatever it was before. That's because we haven't 50 ohm terminated, and

**Dave Jones:** it's a bit over the level, so it's probably counting some extra pulses. Let's put the attenuator on there. You've got to set it up, but once you set it up, bingo! We're getting the exact same thing. And ordinarily, yes, this is an excellent tool, and yes it does have statistics on it, but unfortunately

**Dave Jones:** the reason I didn't use it for this is A, it's not visual, so you can't actually see the waveform, which is kind of handy on a scope. But also the stats unfortunately do not work in the totalised mode. Wah wah wah wah. They work

**Dave Jones:** just fine in frequency counter mode, of course. You can go in there and you can view all your stats and everything else, but in totalised mode, it doesn't work. Why? It's just a software thing, why can't they put you know, just a simple average on the thing for

**Dave Jones:** totalised? I don't get it. Anyway, you can like single shot capture it just like on a scope. There you go. And of course you can extract the data out of it and average it that way and get a graph and everything else. You know, a plot and everything else.

**Dave Jones:** But meh. Anyway, so yeah. Ordinarily this would be the tool for the job, because you don't have to worry about sample rate and your memory depth and all that sort of rubbish. As long as you set it up correctly, this puppy will do the job.

**Dave Jones:** It'll capture those counts no matter how short they are. It's got hardware in there specifically designed for it, if your scope doesn't have it. And of course we finally reach a point where we just can't go any higher and we just can't do it at the current time-based setting.

**Dave Jones:** I'm up to 500 nanoamps at the moment, and if I go to 600 we should expect a... we've got 15,000 counts at the moment. Go up to 600 here, we should expect it to actually go up, and it doesn't go up by the requisite amount.

**Dave Jones:** We go up to 700 nanoamps, and it actually starts to drop. So eh, we've reached the limit of our current test setup. That's 800 and 900 nanoamps. There you go. But anyway, I've got... ta-da! All the data from 20 nanoamps up to 500 in

**Dave Jones:** 20 nanoamp steps. Beauty. So can we actually see this lead at 500 nanoamps? Well, this is actually 5 microamps so let's turn it back down to 500 nano, shall we? There we go. Nope. Can't see it. 600, 700, 800, oh you can start to see it!

**Dave Jones:** Just... just... wow! That's at 900. That's at 900 nanoamps. So if we turn it up, there we go. There we go, that's 1 microamp. 2, 3, so you can start to see it. But yeah, it basically is not visible at 500 nanoamps that we're measuring here.

**Dave Jones:** But of course that photon counter can easily see it. It is ridiculously sensitive, that's why these things are very, very expensive and also very sensitive to light and things like that. You can actually blow the thing if you just turn your lights on here if you're not careful.

**Dave Jones:** And here's the fun part, we get to look at the data! Here we go, I've actually taken it, put all the data into a spreadsheet here, and you can see I've taken out, I've subtracted the dark count value of 212, so I've plotted this data here of

**Dave Jones:** oh, can't quite see it, there we go, of the photons per second versus the lead current in nanoamps. And bingo! It is not linear, far from it in fact. Look, it ramps up there and then it starts to taper off again. Shame I couldn't go any higher than that

**Dave Jones:** to see what it did, you know, plot it over up to milliamps or something like that right down from nanoamps. But anyway, that's a very interesting result. It is not linear. And it would be interesting to see if that changes with different types of

**Dave Jones:** leads as well. I'm sure it does, you know, you get like a super high efficiency red lead. This is just, as I said, one of those eBay cheapies, I have no idea what. But it would be interesting to get, you know, one data set doesn't really show you much.

**Dave Jones:** Well, it shows you that it's not linear. It's potentially not linear right down at that low region. And maybe there's some fundamental quantum physics actually behind that. It'd be interesting to find out. So perhaps maybe a follow-up video in the future, I don't know.

**Dave Jones:** But I just love getting data like this and, you know, that sort of not entirely unexpected result. But I would have been disappointed if it was just linear. I was like, oh, that's boring. But no, look, it's very smooth. There's like, I haven't applied any smoothing to that

**Dave Jones:** at all. It really is that shape. So you know, I think that experiment worked really well. And this is some quite reliable data from this particular lead at least anyway. So that's terrific. Love it. So there you have it. That is very cool indeed.

**Dave Jones:** I don't really know what it means. I don't know the physics behind it. I haven't researched it at all. But I just wanted to do that experiment because I didn't seem to find any data out there. Let me know if you if there is other data out there which I couldn't find in my

**Dave Jones:** very quick search. But that is fascinating. And it did switch on it. I think if I, you know, really got down there and measured the fine scale right down under the 20 nano amp figure, we might find the point where it does actually, you know, might be able to see

**Dave Jones:** a little bit down there. But obviously it's going to follow that curve. And it's not linear. So very, very interesting. Anyway, hope you enjoyed that video. If you want to leave comments always down below, link to the forum down below, all that sort of jazz.

**Dave Jones:** Catch you next time. First of all, what we need is a baseline of the dark count. So I've still got the protective cap on the end, that's the factory cap I believe. And it will see if we actually get the below the maximum

**Dave Jones:** data sheet value for the dark count. So I've got my Rigol DS1054Z here. And I'm going to show you an example of where, you know, you have to have the right tool for the job. You may think you have the right tool, or you may

**Dave Jones:** think you know how to use the tool properly, but you may not. Anyway what we've got here, okay, here's all the pulses. Alright? You can see I'm just jumping out, jumping out here like this. But if we set it to a second, which is what we want, because we want

**Dave Jones:** pulses per second. So I'm going to set it for 100 milliseconds per division here, because we want to measure the number of pulses per second. Okay? So if we have a look here, and we actually single shot capture that, okay, there it is.

**Dave Jones:** Look, we've got lots of little pulses in here, and I mentioned this in a previous video, and we can go in and actually have a look at those, and you can see that if we actually zoom in on that, it's a tiny little

**Dave Jones:** tiny little thing there. But look, all we've got is a single sample pulse. That's it. Because we don't have enough memory depth to actually capture one full second of the thing and actually get the 20 microsecond pulse, which is what this module generates, a 20 microsecond pulse each time it gets

**Dave Jones:** one photon out. So it just does not have the sample memory required, okay? And we can go into the acquire menu here, and we can see that our memory depth is the full 12 meg that this thing is capable of. It's still you know, it does not have the ability to do it.

**Dave Jones:** So how do we do it? Aha! I'm glad you asked. Let's go back to we'll set this back to the middle there, okay? Let's go to our 100 milliseconds per division here, and what we need to do is set the oscilloscope to go to the

**Dave Jones:** acquire menu. Instead of normal mode here, now not all scopes have this, but this one does. We can actually go into peak detect mode, okay? Bingo, watch what happens. Ta-da! Look at that! They're now all full height pulses on the scope. That's because it's not using the sampling

**Dave Jones:** it's using dedicated hardware to actually detect short pulses you can go read the data sheet and you might be able to find what the minimum peak value is. We're only looking at like a 20 microsecond pulse, can easily do that. It's down in

**Dave Jones:** the tens of nanoseconds or something like that. That's what peak detect mode on your oscilloscope is really, really good for. ... ... So now we can go in there and we can actually single shot capture that, and we can go in and we can actually

**Dave Jones:** see all of our pulses. Now it will, now it won't sorry, it won't actually be, show the proper 20 microsecond pulse like we should see, but it at least detects each and every one and will actually show them at their full peak value, okay?

**Dave Jones:** So it's going to allow us to actually get proper measurements without missing pulses and things like that due to the sample rate. Now if we actually turn it on, and we turn the time base up, there's our actual pulse, there it is. Sorry, I thought that pulse was

**Dave Jones:** microseconds, it's actually nanoseconds, so it's 10 nanoseconds per division, 10, 20, 30, you know, 35 nanoseconds or something like that per pulse. And you can see you'll see, you know, you'll see pulses pop up occasionally, hopefully. Oh, it's very dim, but you can maybe

**Dave Jones:** turn up our intensity, there we go, you start to see them jumping around there just randomly. And that randomness is our dark count. It's much nicer having that intensity up, isn't it? Excellent. But unfortunately we can't use this scope, it's no good, it's not the right tool

**Dave Jones:** for the job. It's got lots of ability, you know, it's got lots of measurement options here horizontal, vertical measurement options, like multiple pages worth of measurement options, but nowhere in here does it have an option to actually measure the number of pulses. So this scope, unless you want to, you know, capture them and go in

**Dave Jones:** there and manually count them, you know, it's going to have a couple hundred pulses, meh, this ain't the right tool for the job. And no, you can't use the hardware frequency counter, because the frequency counter is not actually counting the pulses, it's counting the distance between the pulses, which is

**Dave Jones:** of course completely, if we have a look at it, come on parameter limited, my arse, come on. Ah, what's it doing? Sorry, I went up to seconds there, I just turned the knob too quickly, there we go. They're completely and utterly random, because that, and that's probably going to change with

**Dave Jones:** temperature of the sensor and, you know, all sorts of stuff. And you can actually buy a different grade, you get a different model here, as we saw in the data sheet, to get different dark counts. So they bin them, you know, higher quality ones, so you'll actually pay more for that.

**Dave Jones:** But this one is rated for 250 counts per second when the sensor is dark. And by the way, I had to use a 50 ohm terminator there, because this thing expects 50 ohm termination on the output, there's a little transformer in there as we saw in a previous teardown.

**Dave Jones:** So let's break out one of the big guns here, the Tektronix MDO3000. Let's see if this puppy can do it. Well first of all, we actually have something annoying here. You'll notice that it's updated exactly like it did on the Rigol, it might be a bit hard to

**Dave Jones:** see the, can we change the intensity? There, there we go. Let's turn the intensity right up so that we can see these things. It's working just like it did before, but we're at 20 milliseconds per division, and if we actually change to 40 milliseconds per division

**Dave Jones:** you'll notice that it's actually in roll, and I'll show you this, it's in roll mode. You saw it, it automatically changes to roll mode, and that's actually, it can be a little bit annoying in this instance. But the good thing about this scope is that we are on

**Dave Jones:** 100 milliseconds per division, and we actually have 10 horizontal divisions across, so that's precisely one second. So even if this Rigol scope actually had the ability to count the number of pulses, you'll notice that it's actually got 2, 4, 6, 8, 10, 12 different, 12 divisions on here

**Dave Jones:** on the one screen. So even if, so if you set it to 100 milliseconds per division you're actually doing 1.2 seconds instead of a second, so you're not getting the right value. So you'll have to make sure that it actually has have what's called a gated measurement function, which

**Dave Jones:** allows you to set cursors in here, i.e. at that point there and that point there, to chop out the two extra divisions here, and actually only measure between 10 divisions. But eh, the point is moot because, well, it doesn't have the count function.

**Dave Jones:** Anyway, it doesn't matter whether it's using the regular single-shot capture, repetitive capture, or whether or not it's rolling like that, eh, in theory, you know we can still get the same result out of this. And this one does actually have the number of pulses.

**Dave Jones:** If we actually go into the measure menu here and we go add measurement, one of the measurement types is, oh, stupid jewel bloody button, pain in the arse, interface, who invented that crap? Oh, goodness, maybe if you used it every day you might

**Dave Jones:** oh, I don't know, get used to it. Anyway, it does have the ability to, ta-da, measure the positive pulse count, and also the negative pulse count if you wanted to, and you can set reference values as well. Very nice. So I've already added that

**Dave Jones:** measurement down here, and you can see, number of pulses, bingo, 212, like that. But, you'll notice that I'm also using, of course, that we learned before, peak detect mode. If we use regular sample mode, we get the same crap we got before, and we get a grossly incorrect

**Dave Jones:** low value here. So, yep, real trap for young players. You've gotta know precisely how to use your instrument to actually get this functionality working. But, because, as I said before, the whoop, there we go, single shot capture, the pulses in here are all random each time, we actually have to do some averaging to

**Dave Jones:** actually get this thing to give, you know, a reasonable average value that we can use to then detect a rise above that when we connect the lead to it and try and count the photons. So the value's jumping around here, and yes, it does actually have statistics in this thing, so you can actually go into

**Dave Jones:** statistics, and it does have a gating function that I talked about before, so even if it didn't have the correct number of divisions on the screen, you can set the cursor to exactly where you want it. And yes, I know what some people are going to say, you don't

**Dave Jones:** have to use a one second total window here, you could use like a hundred milliseconds total window get the count, which should be ten times lower on average, and then multiply it by ten. And, you could do that, but it's a little bit dodgy, it's just

**Dave Jones:** doesn't have the vibe. So we're getting the value we want, and this thing has extensive statistics in it, and I've set it enabled the statistics, look, mean, min, max, and standard deviation, everything's hunky-dory, but it does not work! It says low resolution, and regardless of what I try and do to this thing, I cannot get it

**Dave Jones:** to give me a mean value on the number of pulses. It simply does not seem to work. I don't know why I'm using full memory depth, so it's not like we're not using enough memory depth or anything like that. And by the way, this thing is slow

**Dave Jones:** as a wet week on the full memory depth, as always. Not available while acquiring here, because I've actually set the memory depth to ten meg, I had it on one meg before, and if we go into one meg there we go, you can actually see it count like that, it'll be slower if I go to

**Dave Jones:** five meg, clunk clunk clunk clunk clunk, it'll eventually get there and actually measure it, but well, thirty, that's a bit dodgy for the first count, 140, you know, this is not good, if I put it to ten meg, it just takes forever. Anyway, it's not

**Dave Jones:** a limitation of the memory depth that it's doing, it's not doing the mean, so I can't use this scope either. And I've got all the right options in here, the full record mode, or we can just do the screen, it makes no difference, we still can't get any of the mean values

**Dave Jones:** and you set it between cursors, does the gating and everything, and we can go up to the statistics, standard deviation, we can reset the like, just nothing works, we can set our reference levels our reference level is 50%, it was set to 90% before

**Dave Jones:** it's still, it's very powerful, but it just doesn't work. And let's use our key site, InfiniiVision MSOX 3000 series, and this one is a bobby dazzler, it does exactly what we want, not only does it have the peak detect mode that we need here to get the proper ones, by the way I'll show it

**Dave Jones:** again, just a go in normal mode there, and yep, you just miss all the pulses, it's absolutely useless. That's a brilliant example of peak detect mode there, I should just do that as a one minute tech tip video or something like that that'd be good.

**Dave Jones:** And it can also count the number of pulses, that's one of our extensive measurement functions here, we can go there and scroll all the way through those, and it's in there somewhere. Positive, negative pulse count, it's got everything. And most importantly, it has a statistics mode, and this one

**Dave Jones:** works a treat. And here we go, we get our mean value, I've done 80, been yapping on for 88 counts here or something, or 88 sweeps of one second, so you know, 88 seconds worth of measurements. And the mean is around about 206, so you know, I'm going to leave

**Dave Jones:** it running for a while, and then we'll take that figure, okay, and that will be our baseline figure and we'll subtract that from when we hook the lead up to this thing and then try and increase the current. So we should see it go up on the

**Dave Jones:** mean. And we have to use the mean, we can't just rely on the individual counts because as I said, they're all random in there, so you know, you don't know if the LED is contributing to the thing or not just on, you have to rely, you have to get that mean figure

**Dave Jones:** otherwise you're down in the noise, and you won't be able to pick the signal to noise. Or you've got an extremely low signal to noise ratio as a score.
