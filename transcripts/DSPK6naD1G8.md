---
video_id: DSPK6naD1G8
title: EEVblog #80 - Nokia E71 + Garmin Mobile XT = Embedded Hell
url: https://www.youtube.com/watch?v=DSPK6naD1G8
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 33, "3": 50, "4": 65, "5": 78, "6": 92, "7": 104, "8": 116, "9": 129, "10": 142, "11": 153, "12": 165, "13": 178, "14": 190, "15": 205, "16": 217, "17": 235, "18": 252, "19": 266, "20": 281, "21": 295, "22": 309, "23": 320, "24": 338, "25": 353, "26": 366, "27": 383, "28": 399, "29": 411, "30": 426, "31": 444, "32": 458, "33": 478, "34": 491, "35": 507, "36": 526, "37": 544, "38": 555, "39": 572, "40": 584, "41": 598, "42": 611, "43": 630, "44": 646}
---

**Dave Jones:** Hi, welcome to the EEVblog an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's time for a short rant. Now, about 2 years ago or something, my company offered me a free mobile phone

**Dave Jones:** SIM card with unlimited data. And well, you know, I didn't really need a smartphone, but I thought, "Hey, I've got unlimited data. So, you know, I should probably get myself one of these newfangled smartphones." Cuz I've up until then I'd been using, you know,

**Dave Jones:** just a dumb Nokia, you know, just a standard phone, you know, it's and it worked perfectly. And I was I was certainly happy with it, but I decided to get one of these, a Nokia E71 smartphone, a piece of [ __ ] as it turned

**Dave Jones:** out. Anyway, I got one of these Nokia E71s because it was it was sort of in the good price range. It had a nice QWERTY keyboard on it. And the big selling point for me was the battery life. It was advertised as having up to

**Dave Jones:** I think 480 hours battery life, 20 days. It's like wow, fantastic on standby. Now, I don't I hardly use my phone at all. I, you know, I'm lucky if I get one or two calls a week and and use one or

**Dave Jones:** two data connections a week. So, really standby power consumption for me is everything. And 20 days, beauty. My old Nokia had like 10 days. So, I knew 20 days would be a load of [ __ ] you know, just typical

**Dave Jones:** marketing [ __ ] I'd never get it. But, you know, I'd be happy if I got 10 days out of it just like my old phone and I had all the new, you know, the smartphone data capabilities. Uh, so

**Dave Jones:** yeah, I got the Nokia E71 and from day one it was a piece of [ __ ] Not only did the damn thing crash on me all the time, the software wouldn't update, you know, it's got a USB

**Dave Jones:** connection, you hook it up to Nokia's software and it's supposed to download the firmware easily. You think I could download the firmware? No, it just lock up. What a heap of [ __ ] Anyway, uh you know, it's I had all sorts of problems

**Dave Jones:** with it. Lock ups that would cause I'd have to lock the machine up totally. I'd have to physically remove the battery to restart the damn thing. Can you believe it? Oh, unbelievable. Anyway, that wasn't the worst of the problems. Um

**Dave Jones:** one of the first things I did was I wanted Oh, it's got a GPS in it. So, I wanted some GPS software. So, I looked around and Garmin uh the Garmin Mobile XT software looked like the best, you

**Dave Jones:** know, best thing. Everyone said it was the best out there. So, I got that and I downloaded that on here and it worked pretty well and everything. But, from day one the battery life on this thing instead of getting the 20 days or even

**Dave Jones:** 10 days or even 5 days, I was lucky to get 2 days. I was getting like a day and a half. What a complete load of [ __ ] I thought, "Okay, you know, the battery's, you know, dead in it or whatever." So, I

**Dave Jones:** you know, I started reading as you do. You start reading the forums and you know, what what other geeks have, you know, had problems with this device and sure enough, the battery life is was, you know, instead of, you know, being

**Dave Jones:** fantastic that everyone was you know, that the marketing raved about for this thing. No, they actually everyone was saying, "Oh, yeah, I get 3 days. I get 4 days or I get, you know, 2 days." And you know, things like that. And then you

**Dave Jones:** know, so I thought, "Okay, well, you know, it's it was all just really pie in the sky marketing [ __ ] and and I've been had." And uh but then I looked into some some more and I found out that it

**Dave Jones:** was the Garmin Mobile XT software that would install this little uh secret utility uh when your phone boots up. Not even if you run the software, okay? It installs some little utility hidden in memory that uh when you boot up the phone, it

**Dave Jones:** would chew excess power consumption. So, one of the first things I did was install this what's called Nokia energy profile program and it can actually display graphically your continuous power consumption. Watch this, I'll press a key and you'll see it

**Dave Jones:** you'll see it spike there. If you actually hit a key, you can actually see that it actually processes the key and it's really cool. And this will continue to run when the phone is actually shut down, you know, in standby mode. So, you

**Dave Jones:** can actually see the standby power consumption. It was fantastic. So, it allowed users to actually compare their phones and sure enough, I don't have a shot of it anymore, but I'll see if I can find one on the net, but the Nokia

**Dave Jones:** uh means the Garmin mobile XT software, that little secret utility in there, what it would do is when the phone's in standby mode, for some reason, it would come on and you would see a a square wave pulse like this of, you know, over,

**Dave Jones:** you know, several seconds that it'd go high and then several seconds that it'd go low and it would pulse like that when it's in standby mode. And that would greatly increase the average standby power consumption. And in this case, it

**Dave Jones:** was like um there you go, it's it's just switched off there. It just went into standby for a few seconds and now as you can see, the average value dropped like that and then when I switched it back on

**Dave Jones:** just then, it pulsed up and it went down. Anyway, um yeah, this secret utility would just continually suck power for some reason. Nobody knew why. And that increased the power consumption to like .18 W in standby mode. And well, if you do the

**Dave Jones:** math based on the capacity of the thing, yeah, you're only going to get like 2 days. And it actually tells you how much time you've got left. There it is. In this case, what's that? 28 hours left based on the current consumption.

**Dave Jones:** So, it's really good. It tells you how much estimates how much supply you got left. And sure enough, there was no way in hell that this thing was going to meet anywhere near its 20 days, let alone 10 days. It was going to get 2

**Dave Jones:** days maximum. I've been had. Anyway, the smart geeks on the forum, they figured out that you know, you could get this background monitor utility that you could actually disable apps in memory, all these hidden apps. So, it told you to download this and you

**Dave Jones:** get rid of you know, you can disable that Garmin XT hidden app in the background and it would increase your power consumption. Great. So, I did that and now I got maybe 2 and 1/2 days if I was lucky. You

**Dave Jones:** know, it was still a heap of [ __ ] And I I just resigned myself to the fact that this was just garbage and I was just going to get crap battery consumption. So, that was until last week when I

**Dave Jones:** actually I got I I I I actually got some SMS spam from Nokia. And normally I just delete the thing. I hate it. I don't know how they got my contact details. Anyway, in the you know, I read the SMS message and it

**Dave Jones:** said, "Garmin um Nokia Maps, the the new Ovi Nokia Maps and they are free. Worldwide maps totally free forever." So, I thought, "Okay, what's the catch?" But no, sure enough, they are completely free. Nokia now give away their GPS mapping software

**Dave Jones:** and it works really good. It's from a company called Ovi, Ovi or something like that. And it works really good. So, I downloaded and installed that. It's terrific. So, I totally uninstalled the Garmin Mobile XT software. And what do

**Dave Jones:** you know? MAGIC. OVERNIGHT, I now get Well, I'll tell you what. I charged this last Sunday night last Sunday, and it's now Tuesday. Sorry, what is it? No, Wednesday. Wednesday the following week, and I've and I'm still down to Where is

**Dave Jones:** it? I'm down to Look at how many bars I've got left. There it is. I've still got like three bars left on the on the actual battery. So, you know, and it says that I'll easily get 30 or 50

**Dave Jones:** hours more out of it. Fantastic. I'm getting my 10, 12, you know, maybe even 15 days out of this thing. Pretty close to its claimed Oh, good enough to its claimed specification. I can't believe it. What's that horrible

**Dave Jones:** Garmin Mobile XT software? What a heap of [ __ ] There's only one thing I hate worse than buggy embedded software, and that's buggy embedded software which doesn't take into account the performance of the device. It pisses me off. IT REALLY

**Dave Jones:** DOES. OH GOD, THESE MONKEYS at Garmin who wrote this Mobile XT software. Usually, I'm a fan of Garmin products, but this Mobile XT software, heap of [ __ ] They probably outsourced the damn firmware to some code monkeys in bloody India or

**Dave Jones:** somewhere. I don't know, and I don't care. But they It's a heap of [ __ ] They didn't even test it to see if it, you know, affected the power consumption. This was 2 years ago, and the reports

**Dave Jones:** are all over the internet about how [ __ ] this is, and Garmin's working on it. Did they fix it? No. Bloody hell. And Nokia you're not getting off the bloody hook, either, because for years the firmware was actually had a big play

**Dave Jones:** in the POWER CONSUMPTION. I I HAD LOTS OF TROUBLE, so much trouble updating the firmware in this thing, but they reckon every time they update the firmware, um you know, you read on the forums, they update the firmware, "Oh, the power

**Dave Jones:** consumption's improved." Well, jeez, no [ __ ] Why didn't you make that a priority when you wrote the software 2 years ago? Unbelievable. So, I've now got the latest firmware in it, and I've I've gotten rid of that

**Dave Jones:** piece of [ __ ] Garmin Mobile XT software, and you know, I'm reasonably happy with it now, but it still crashes, and well, I still think it's pretty much a piece of [ __ ] So, what's the moral of the story? Well,

**Dave Jones:** if you're an embedded programmer designing writing software for devices like this, power consumption is critical. What you do in your software can have a major effect on the hardware, you know, the performance of the hardware, not only speed, power consumption,

**Dave Jones:** responsiveness, uh reliability in terms of lockups. There's lots of things to consider. So, just learn that these things should be tested, and you have to put a lot of thought into doing stuff like that when you're writing this firmware. And if

**Dave Jones:** you're some code monkey somewhere who doesn't know what hardware is, well, bloody hell, get a new job.
