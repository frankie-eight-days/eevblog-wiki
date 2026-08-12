---
video_id: TWKY6W1C9yM
title: EEVblog #44 Part 1 - Logic Analyzer Tutorial
url: https://www.youtube.com/watch?v=TWKY6W1C9yM
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 30, "3": 43, "4": 56, "5": 74, "6": 91, "7": 105, "8": 122, "9": 140, "10": 155, "11": 170, "12": 182, "13": 197, "14": 206, "15": 221, "16": 235, "17": 251, "18": 268, "19": 281, "20": 297, "21": 311, "22": 324, "23": 341, "24": 360, "25": 378, "26": 396, "27": 409, "28": 425, "29": 438, "30": 451, "31": 468, "32": 483, "33": 499, "34": 512, "35": 527, "36": 542, "37": 561}
---

**Dave Jones:** Hi, welcome to the EEV blog an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, today I'm going to talk about one of the least understood pieces of test gear

**Dave Jones:** that you can own. It's the humble logic analyzer. Now, I don't think there's any bit of basic test gear that is more feared or misunderstood than the logic analyzer. People just don't really understand them or they they're scared

**Dave Jones:** of them or they don't know how to use them properly. The first thing is do you actually need a logic analyzer? And for most developers the answer is not really. Now, generally speaking most designs can be debugged with an

**Dave Jones:** oscilloscope these days and it's even more the case these days now that oscilloscopes have very deep memories on them. So, you can capture tons of data serial or well, usually only serial cuz an oscilloscope is only a couple of

**Dave Jones:** channels. That's the main disadvantage. And the main advantage of the logic analyzer is that they're multiple channels. But the large sample memories in oscilloscopes mean that a lot of the time a lot of traditional uses for these logic analyzers like debugging serial

**Dave Jones:** product protocols like SPI or I squared C or RS232 are done by the oscilloscope these days. Logic analyzers come in three main types that you need to consider. One is the traditional bench instrument. You can still buy them. They're you know, as big

**Dave Jones:** or bigger than a bench oscilloscope and they have and they cost you know, 5,000, 10,000, 50, 100,000 dollars. They can be very expensive and they take up a lot of bench space. And unless you have a very specific need for them, they they're

**Dave Jones:** pretty much a waste of space on your bench. The second one is probably the most useful and that is a combi scope which is a combined uh, and logic analyzer all the major manufacturers make them. You'll have your traditional two or four

**Dave Jones:** channel oscilloscope and it'll have a eight or 16 channel logic analyzer built in usually. And they're really useful because you can actually, uh, trigger easily trigger off say your analog, uh, channels and then capture the data at your digital data at the same time.

**Dave Jones:** So, they're I find they're the most useful type. But, they can add a lot of price to your oscilloscope. So, generally they're not as good value for money as getting the third type, which is a PC based oscilloscope. Uh, they're

**Dave Jones:** the market's flooded with these things these days. You can get them, uh, anywhere from, you know, $50, $100 up to uh, several thousand dollars, something like that. But, your general mid-range ones are about, you know, a couple hundred dollars and they're the most

**Dave Jones:** useful type, I think. They don't take up any room at all. This is quite a large one actually. But, they generally don't take up much room and they're cheap and they're available for when you they can just pull them out of the drawer when

**Dave Jones:** you actually need it. So, I'd recommend you get one of these USB, uh, logic analyzers. There's a couple of reasons why logic analyzers aren't that popular. And the first reason is that they they well, they're just fiddly to

**Dave Jones:** use. You've got all these channels you've got to hook up. All right, you've got to hook all these things up, probe them on. You've got to make sure that they're that they're making good contact and then you've got to label each

**Dave Jones:** channel in your software so that you don't interpret the wrong one. Trust me, if you're going to go to the effort of wiring up more than one or two channels, do yourself a real favor and label get take the take a few minutes to label

**Dave Jones:** each channel in the software. The next major problem with logic analyzers is that what you see on the screen is not necessarily what is actually happening in your circuit. These things have so many traps for young players, it's not

**Dave Jones:** funny. Even for experienced people, you can get tricked into thinking that your circuit's doing something that it's actually not, or not doing something that it should, or whatever. Now, the reason for that is that logic analyzers, what you see on the screen, this

**Dave Jones:** representation, you see your waveforms, 1 0 1 0, that's not necessarily what's happening actually in your circuit. What that represents is what the internal latch chip thinks your circuit is doing at the exact point that it samples that

**Dave Jones:** clock. Now, your input waveform, it can be noisy, it can be all over the place, it can be overshooting, undershooting, doing all sorts of things, and there's going to be a logic low threshold and a logic high threshold

**Dave Jones:** at that point. And that has to do your probes can affect that and all sorts of things. So, it's really not as good as an oscilloscope, cuz an an oscilloscope actually shows you what's there, as long as you probe it correctly, of course.

**Dave Jones:** But really, you're working a bit blind with a logic analyzer. You've got to either you've got to basically trust it, and that's one of their major pitfalls. Now, you can actually get some logic analyzers that do work like an

**Dave Jones:** oscilloscope. They're basically a crude oscilloscope, so you can actually see the wave shape as well, just like on a So, it's like a you know, a 32-channel oscilloscope, basically. But if you have to ask the price, you can't

**Dave Jones:** afford it. Now, when it comes to how logic analyzers work, there's two modes of operation, and here they are. The first one's called timing analysis mode. The second is called state analysis mode. And the difference between these two is basically that's

**Dave Jones:** timing analysis mode, it works like your oscilloscope. It's got an internal clock, and it basically takes fast samples, and you can see your input waveform or waveforms change with time. Just like a Basically, it's a binary oscilloscope, if you want to think of it

**Dave Jones:** like that. But, in state analysis mode, it doesn't use an internal clock. You have to provide it with an external clock, your own clock, that is generally uh in uh that is synchronous to the data that you're actually trying to analyze.

**Dave Jones:** That's why the state analysis is synchronous, and timing analysis is asynchronous. Now, for most purposes, you're going to want to use timing analysis mode uh because that is more useful, unless you have a specific need to analyze uh your system, to do system

**Dave Jones:** analysis of actually what's happening within your system on a given clock edge or something like that, a specific state in your system, you're really not going to want to touch state analysis much. If you're going to need it, you're going to

**Dave Jones:** know it. And because of various uh factors to do with um the the design of the capture system in the logic analyzer and various other things, generally, the spec the sample rate for state analysis for any given logic analyzer is going to

**Dave Jones:** be less than timing analysis. That's just the way it is. There's another thing you've got to consider when you buy the logic analyzer, and that's sample memory. Now, just like an oscilloscope, you need to get the biggest, deepest sample memory you can

**Dave Jones:** get. It's very important on a logic analyzer, cuz usually you're analyzing data, and lots of it. So, you need a big sample memory. But, to confuse the issue, there are two different types of sample memory. Well, the same sample

**Dave Jones:** memory, but two different types of systems, and here they are. The first one is sequential sampling. It's That's not really its name. It's just normal, the traditional method. That's how almost every most logic analyzers uh will work, okay? And the other is

**Dave Jones:** compression sampling. That's really cool. What that means is that it actually compresses the data before it stores it in memory. And here's how they work. Here's the differences. Now, in the sequential sampling system, if this is your sample clock, and this is the

**Dave Jones:** input data you're sampling, it doesn't matter what the input data's doing. You're going to use the same amount of memory. Your data can be sitting there at all zeros, and it's going to be chewing up precious memory. Because you've got a sample at each

**Dave Jones:** interval like this, and each one of those is using 1 2 3 4, it's using up a byte or a word of your memory at each one of those samples, and right up to 1,000 and so on. And this uh

**Dave Jones:** this isn't very good if you're trying to measure, say, a packet of I squared C data here, and then another packet of data which is way down there. That means you've got to have a huge, massive, many megabytes of sample memory, um otherwise

**Dave Jones:** you're not going to be able to capture all these widely spaced um packets of data that you want to analyze. This is where compression sampling comes in. Now, compression sampling is will only it it still samples at the same

**Dave Jones:** rate as this one, okay? But it will only store data it will only use a a word or a byte of memory whenever one of the input data channels changes. So, in this example here, it's only used 1 2 3 4

**Dave Jones:** words of memory, because the data's only changed, it's only transitioned four times. Whereas up here, the same waveform might take, say, 1,000 or even more, a million bytes of memory to capture just that same couple of little thing.
