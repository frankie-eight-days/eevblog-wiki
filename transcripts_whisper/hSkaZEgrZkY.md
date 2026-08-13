---
video_id: hSkaZEgrZkY
title: Alkaline Battery Discharge Testing Part 3
url: https://www.youtube.com/watch?v=hSkaZEgrZkY
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 23, "2": 39, "3": 57, "4": 72, "5": 87, "6": 105, "7": 125, "8": 140, "9": 154, "10": 168, "11": 188, "12": 206, "13": 232, "14": 252, "15": 267, "16": 281, "17": 298, "18": 316, "19": 335, "20": 352, "21": 373, "22": 389, "23": 405, "24": 425}
---

**Dave Jones:** Hi, this is just a follow-up to the previous, I guess, Part 1 video of just discharging some batteries here, which is in turn a follow-up to my main channel video, which was the alkaline battery leakage test. So, I've got another set of batteries, 13 different brands, 2 of each different brand.

**Dave Jones:** I'm going to start out with the Duracell Ultras here, no reason why, just random order. And I'm going to discharge these ones as well, but of course, the last video was a classic example of why you probably shouldn't discharge or charge tons of different batteries in series like that,

**Dave Jones:** especially different brands with different capacities and stuff like that. Because you can come a-gutza, even with just, and you can, like, reverse charge them, and that's the problem that we had in the previous one. Once one brand of batteries might have had a slightly less capacity than the others,

**Dave Jones:** so they started to reverse charge, so all the other batteries in series started to charge those ones, and yeah, it can really come a-gutza. But even with 2 in series that I'm going to do now, I've got a better battery holder. This time, I've got a thicker gauge wire going over.

**Dave Jones:** I'm still not going to bother to use the 4 terminal sense wires here, because with all the contacts and everything else, there's not, you know, there's not a huge real advantage there to actually doing that. As long as you've got the thick gauge wire and keep it short, should be reasonable.

**Dave Jones:** But yeah, anyway, because battery holders are terrific. You really need, like, to sense each individual battery. So I'm going to discharge 2 at a time this time, instead of all of them in series. I was trying to save time last time, and we sort of come a-gutza on 2 of the brands there,

**Dave Jones:** which reversed charge. But anyway, they have been discharged, and yes, these ones, heaps of comments on the previous video, yes, as I said in my main channel video, I will be putting this batch of batteries with a, like, 100k resistor in parallel, or whatever, to give, like, 10 microamps leakage current.

**Dave Jones:** So yes, these ones will actually have in, I'll do them in pairs, because I have all these battery holders over here in pairs. So I'll do each brand, I'll discharge them in series like this. And even when you discharge them in series, there can be slight capacity differences

**Dave Jones:** between one cell or the other. You know, in the manufacturing bell curve, these, even from the same packet which these are, they may not, you know, one may be slightly, have slightly higher ESR than the other one, and it can be a problem.

**Dave Jones:** So anyway, I don't want to discharge these slowly, so I'm going to, in this particular case, I'm going to do 500 milliamps to make it faster to actually discharge these, because I've got 13 different pairs to do. I'm going to set my stop voltage,

**Dave Jones:** I'm not going to set a stop capacity, I'm only going to set a stop voltage, normally 1.4 volts, so it's, that's actually on the terminals here, not actually on the batteries themselves, so, anyway, when you're discharging at a higher current like this, which, you know, half an amp is pretty high,

**Dave Jones:** like, you really don't want to go over one amp with double A's, because the ESR just sort of kills you, so, but when you're discharging at higher currents like this, yeah, you might think, okay, 1.4 volts, that's 0.7 volts per cell, you think, oh, we're really killing these things, but we're actually not,

**Dave Jones:** there will still be a fair amount of capacity in these, maybe 10%, 5% capacity, maybe even, like, 10%, depending on the intricacies of the losses in the contacts and sensing voltage and everything else, so, when you discharge these at the higher current, you will actually get, you won't be able to extract as high a capacity from the battery

**Dave Jones:** as you would at lower currents, so there will be, you know, a significant amount of capacity left in these things, and, as I mentioned in the previous one, somebody has actually pointed out a research paper on leakage of batteries and has shown that, apparently this paper effectively says that if you discharge them

**Dave Jones:** at a high current and then just leave them, that they stand the most chance of leaking, so in this particular case, I'm going to put a load on these ones, the other ones that I did in the previous video, they will just be sitting there with no load,

**Dave Jones:** so, that's why I'm doing two different types of loads, just to see if it makes a difference. Anyway, so, and somebody mentioned on the previous video that, oh, I need to collect better data and stuff like this, this is not about collecting data

**Dave Jones:** on battery capacity or anything else, this is simply discharging batteries to, you know, like 90% discharging them or something, just so that more pressure can build up in the batteries because they're more susceptible to leaking, apparently, when they're mostly discharged. So that's the whole idea.

**Dave Jones:** So I'm going to do 13 sets here, so let's whack it on, I've got half an amp, 1.4 volts stop voltage, which is total, so 0.7 volts per cell nominal, I won't worry about timers or anything else, so let's switch that on, 3.23 volts open circuit,

**Dave Jones:** and we'll see that drop very quickly at half an amp, there we go, yeah, it drops a lot straight away. So there we go, we've got our half amp there, and that could take a while, 1 milliamp hour total, and the good thing about this, the battery capacity app here, is that it just switches off

**Dave Jones:** when it gets to 1.4 and tells you the total capacity and the total time. Fantastic, so, yeah, I won't bore you with the details, but I'm going to do this for 13, lucky 13 set of batteries, and then I will modify all of my battery holders back here

**Dave Jones:** to add like a 100k load across each one, and, oh, that's actually, no, 200, probably should get 200k if I, because they'll be, normally, these will recover to like 1.2, 1.3 volts, these will actually, you know, the voltage will actually recover a fair amount after you discharge them like this.

**Dave Jones:** So, yeah, they'll get back to easily over a volt. So, if I get two of those in series, that's two volts, I'm going to need 200k to get a nominal 10 microamps, which is what I figure is a fairly typical standby power consumption for a particular product.

**Dave Jones:** You know, it can be as high as, maybe I might use 100k, 20 microamps, meh, you know, do it a bit more, maybe, I don't know, 100k, nice round value, so I might do that. Although I don't want to deplete my resources of 100k, my stock of 100k resistors,

**Dave Jones:** so I might use like 110k or something like that. Anyway, these ones will have a light load over them. So, yeah, that's all for this video, and at the end of it, I won't bother showing you all the results from these, I'll just simply put them, load across them, whack them in a box, and if there's any updates,

**Dave Jones:** yeah, on the second channel here. Catch you next time.
