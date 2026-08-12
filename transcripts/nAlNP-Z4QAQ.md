---
video_id: nAlNP-Z4QAQ
title: EEVblog #44 - Part 2 - Logic Analyzer Tutorial
url: https://www.youtube.com/watch?v=nAlNP-Z4QAQ
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 30, "3": 46, "4": 71, "5": 94, "6": 119, "7": 128, "8": 138, "9": 154, "10": 169, "11": 184, "12": 203, "13": 212, "14": 226, "15": 246, "16": 268, "17": 285, "18": 296, "19": 308, "20": 319, "21": 333, "22": 351, "23": 370, "24": 385, "25": 396, "26": 420, "27": 436, "28": 445, "29": 459, "30": 475, "31": 487, "32": 502, "33": 521, "34": 532}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. So, a logic analyzer with compression sampling is extremely valuable.

**Dave Jones:** It makes it maximizes your use of memory. Now, the best oscilloscope will have an incredibly deep memory, megabytes of memory with a compression sampling system. That is the best scope you will get.

**Dave Jones:** But generally, on the market in mid to low priced logic analyzer, you won't get that generally. Your logic analyzers that use compression sampling will generally only have a couple of kilobytes or something like that of sample memory.

**Dave Jones:** So, that means there's a trade-off with these small sample memory logic analyzers. Don't be fooled into thinking that they're magic because they're not always magic because what it will do is if any one of your input channels changes, any one of your data channels changes, then it's going to actually take a sample across all your channels.

**Dave Jones:** It's going to use up a byte. So, if you've got one channel which is clocking away, going really fast, and then you've got another channel which is having, you know, having a slow data or it's got widely spaced packets of data that you want to analyze, then that fast input changing channel can chew up all your memory before you get a chance to view your next packet.

**Dave Jones:** So, in that case, a deep memory sequential sampling logic analyzer can be better. Now, generally speaking, cheap USB logic analyzers, they really aren't a professional tool. Why? Well, because probing and your input sampling is everything.

**Dave Jones:** Your input front end on a logic analyzer, just like an oscilloscope, you buy a cheap oscilloscope with some toy front end on it, you know, it's a crap oscilloscope.

**Dave Jones:** Same thing with logic analyzers. If you buy a cheap logic analyzer with cheap probes and a cheap input circuit, cheaply designed and made input circuit, it's not a serious tool.

**Dave Jones:** Why? Because there's so many issues involved with getting uh I I good signal integrity on the input to a logic analyzer. There's There's noise. There's skew across channels. There's uh transition times.

**Dave Jones:** There's metastability issues. There's all sorts of things. Input capacitance, inductance, and rise time, and fall time, and cross talk, and all sorts of things that can actually affect your measurement.

**Dave Jones:** Now, generally speaking, if you're forced to bring out your logic analyzer, it means you're getting pretty desperate. Your design's not working, or it's 99% there, and it's only the 1% that, you know, there's that is failing.

**Dave Jones:** There's a timing issue, or something like that, a very subtle timing issue in your system uh that you're trying to resolve. Now, really, hooking just the act of hooking up your logic analyzer to your circuit can change it, just like an oscilloscope.

**Dave Jones:** And if you're trying to measure If you've got like a a multi-channel system that you're trying to probe, and you probe one of the channels, it can make your system come good, or make it go bad.

**Dave Jones:** So, unless you've got a really high-priced, properly designed logic analyzer probe system, you're you're you're really kidding yourself. You're You've really only got a toy. Now, there's nothing wrong with just having a toy logic analyzer.

**Dave Jones:** They're They're useful for, you know, most jobs, really. Uh just for analyzing your I squared C bus or something like that. But, if you're into serious high speed, you know, 50, 100, couple hundred megahertz, something like that, these toy logic analog USB logic analyzers really aren't going to cut it.

**Dave Jones:** Yet another decision you need to make when you're buying a logic analyzer is there's once again there's two different types. There's those that uh capture and buffer the signals within the thing itself and then upload the data to the PC or there's the ones that uh work in real time and they're the cheap ones.

**Dave Jones:** They're the, you know, your your $100 ones or 50 or $100 ones. They're generally the ones that will just uh really stream data in real time over your USB 2.0 interface and generally they're limited to, you know, 10 or 20 megahertz or something megasamples or something like that.

**Dave Jones:** And that's because they stream data in real time. Now, the advantage with those low-cost ones that stream in real time is that you effectively have an infinite amount of sample memory.

**Dave Jones:** You've got your hard drive. You've got You've got a terabyte hard drive. Whoa! You know, fantastic. You can store a terabyte of damn data. It's incredible. So, you got unlimited buffer.

**Dave Jones:** That's the advantage with those ones over the ones that these faster ones which will actually um have internal uh sample memory and buffer it and then transfer it uh later.

**Dave Jones:** Yet another thing to look for when you buy a logic analyzer, there's a whole host of things. The next thing is uh make sure your logic analyzer supports pre- and post-triggering.

**Dave Jones:** It should actually capture half of the or maybe uh selectable. The it captures data before the trigger point and after the trigger point because often in a system you're triggering on a fault and you want to see the data that caused that fault.

**Dave Jones:** Another thing to look for in a logic analyzer is that it can actually decode serial data in real time and trigger on serial data in real time. So, it actually analyzes each bit like this and you can set it up to trigger on a particular word or a particular byte.

**Dave Jones:** And this is most useful for serial decoding, uh I-squared-C and SPI and all those serial type buses once again. If your system supports those, then it's going to be super valuable for you.

**Dave Jones:** Now, generally a logic analyzer will come with these easy hook probes. They're actually little tiny probes that you pull down and they're a standard they just pull straight off here.

**Dave Jones:** Make sure your probe comes with your logic analyzer comes with these probes cuz they're most valuable. And make sure it comes with a good set of short short, not long probe wires because the longer Look, the ground on this, the longer you make that ground, the less reliable your signal integrity is going to be on the input to this thing.

**Dave Jones:** So, you don't want super duper long probes. You want them as short as possible. And I can't say it enough, probing on a logic analyzer is critical. Unlike Well, it's critical on an oscilloscope, too, but at least you can see the problem.

**Dave Jones:** You can see the overshoot, the undershoot, the ringing and and but you can't see it on a logic analyzer. You're operating blind, completely blind. You have to trust this thing.

**Dave Jones:** So, you have to know how to probe and keep them really short and preferably you might use a buffered probe which will actually have a proper buffer in there, but really your your low-cost ones aren't really going to have that.

**Dave Jones:** Another thing to look for in a logic analyzer is input threshold settings. Now, a good logic analyzer, a higher quality mid to high range one, will actually have adjustable threshold levels.

**Dave Jones:** They'll actually have a DAC inside them that you can actually set this level each of these levels anywhere from, you know, minus might be minus 5 volts up to plus 5 volts.

**Dave Jones:** And you can do the same thing with this as well. You can adjust the threshold level. And that's that's really useful. But once again, they will have quick set up options for like CMOS and TTL and low voltage CMOS and all that sort of stuff.

**Dave Jones:** But generally you might have to fiddle around with those, but they're very flexible. Now, the other type will just have fixed thresholds cuz they'll just use a simple, you know, a 3 volt a gate on there, you know, they'll they might use a like a 5 volt just a logic gate straight on the input or something like that.

**Dave Jones:** And really these thresholds are going to be fixed. And that's what you get That's the disadvantage of the low-priced logic analyzers. So there you go. That's logic analyzers. Don't be scared of them.

**Dave Jones:** They're a valuable tool. They're not used very often, but I highly recommend you get a, you know, a simple USB logic analyzer and keep it in your kit drawer just in case.
