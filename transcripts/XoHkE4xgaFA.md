---
video_id: XoHkE4xgaFA
title: EEVblog #1242 - Memory LCD+Supercaps+Low Power Design
url: https://www.youtube.com/watch?v=XoHkE4xgaFA
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 33, "3": 47, "4": 60, "5": 77, "6": 93, "7": 113, "8": 125, "9": 138, "10": 152, "11": 167, "12": 183, "13": 195, "14": 210, "15": 226, "16": 240, "17": 256, "18": 274, "19": 287, "20": 298, "21": 318, "22": 335, "23": 350, "24": 365, "25": 377, "26": 390, "27": 403, "28": 420, "29": 432, "30": 446, "31": 462, "32": 475, "33": 491, "34": 505, "35": 522, "36": 536, "37": 549, "38": 561, "39": 574, "40": 586, "41": 600, "42": 618, "43": 635, "44": 650, "45": 664, "46": 681, "47": 694, "48": 711, "49": 728, "50": 745, "51": 761, "52": 784, "53": 802, "54": 817, "55": 827, "56": 839, "57": 853, "58": 870, "59": 886, "60": 901, "61": 916, "62": 929, "63": 946, "64": 967, "65": 981, "66": 994, "67": 1007, "68": 1022, "69": 1036, "70": 1050, "71": 1068, "72": 1082, "73": 1102, "74": 1114, "75": 1128, "76": 1140, "77": 1152, "78": 1163, "79": 1178, "80": 1194, "81": 1209, "82": 1227, "83": 1242, "84": 1257, "85": 1275, "86": 1289, "87": 1308, "88": 1329, "89": 1345, "90": 1360, "91": 1377, "92": 1390, "93": 1402, "94": 1419, "95": 1433, "96": 1447, "97": 1465, "98": 1478, "99": 1494, "100": 1511, "101": 1530, "102": 1544, "103": 1558, "104": 1570, "105": 1587, "106": 1601, "107": 1613}
---

**Dave Jones:** Hi, this is part two of the power up display counter project. I'll link part one if you haven't seen it. May not make much sense unless you well, no, it's probably a decent standalone video if you're into like low power LCD solutions

**Dave Jones:** and stuff. So, I won't recap that video, but just an update. Not a huge amount. Basically, no one really pointed out any alternative seven segment e-ink e-paper uh displays that were suitable. You know, there there's a couple in here

**Dave Jones:** that we basically got down to and we could potentially get those, but I tried to contact the manufacturers. Haven't really heard back from them yet. So, I don't know. I'm still looking for an e-paper e-ink solution and we might have

**Dave Jones:** to go for a graphic solution in that particular case. So, anyway, that's still not off the table, but it did pretty much rule out in the previous video that seven segment e-ink displays, while you can get them, they're not

**Dave Jones:** really a thing. They're all just graphic these days. So, you know, they're a pretty specialized thing if you want to actually get them. So, what quite a few people asked for is that they wanted to know about the little Sharp memory LCD

**Dave Jones:** that I showed. This is an LCD, but it's manufactured by Sharp and it's basically an ultra low power dot matrix LCD solution. Now, this is not a seven segment display. It's dot matrix, but and that's okay. We can work with that.

**Dave Jones:** So, what I'm going to do and go through in this video is just looking at the options and some calculations on how long we can get an LCD solution like this Sharp memory one or a regular LCD to work from a rechargeable either super

**Dave Jones:** cap or one of those little surface mount rechargeable batteries that you can get these days. As quite a few people said, "Oh, I'll just get a regular microcontroller and just don't do an LCD and have a a coin cell battery or

**Dave Jones:** whatever and Bob's your uncle." Well, okay. Well, let's have a look at that solution as well. So, these are the sharp memory LCDs. This is the one that I've actually got here. They're all dot matrix though. They're a three-wire SPI

**Dave Jones:** interface so you can drive them with a little 3 cent PSoC microcontroller. Hopefully, I'm going to have a follow-up video with the PSoC microcontroller actually getting one of those up and running with a do-it-yourself programmer and also an

**Dave Jones:** open tool C compiler. This is the one I've got is 29 by 6 mm perfect and it's 6 microwatts static power consumption and dynamic power consumption when you're changing stuff on the display, which we don't need to in this case.

**Dave Jones:** It's just a counter that just stays static playing at 6 microwatts at 3 volts for this thing. That's only 2 microamps. There it is. 3 volts supply, that's 2 microamps. That's the sniff of an oily rag stuff. Now, of course, the

**Dave Jones:** downside to these is that they're not particularly cheap. We can get them in stock from Digi-Key. Look at this, 2,700 in stock. No wackers. Um but even in thousand of quantity, they're 8 US dollars. We're just going to assume that

**Dave Jones:** cost is not really an issue here. Now, unfortunately, um the data sheet is just a link to the brochure thing, which is like it's nothing. It's got no technical details on there. I don't know, is an NDA thing? You got to contact them

**Dave Jones:** presumably. What's the protocol for driving this? Uh anyway, let's just assume that we can drive this thing and it's 2 microamps supply current. That's what we have to beat with any alternative solution. Now, to give you an idea of how low 2

**Dave Jones:** microamps is, let's have a look at a CR2016 watch battery for example. If you don't know, the numbers on there tell you what it is. The first two digits, the 20, is 20 mm diameter. The next one, the 16,

**Dave Jones:** means it's 1.6 mm thick. So, it's 20 mm by 1.6. A CR2032 will be 20 mm by 3.2 mm thickness, double the thickness of this. So, you might find that in a typical digital watch these days, a capacity of 100 mA

**Dave Jones:** hours, and that's rated at 30k there load. So, that's 100 microamps load, typically. 3 V / 30k 100 microamps. So, it's lower than that, but you know, the capacity is not going to be hugely greater at any lower

**Dave Jones:** currents. We don't actually have any characteristic curves for ultra low current here. We might be able to find somewhere else, but you know, it's it's not quite shelf life, but it's getting there. Say, a typical digital watch that

**Dave Jones:** might have, say, a 3-year battery life. I know you can get longer, but let's just say, like a little digital watch that just ticks over the seconds, that's all it does, you know, designed for ultra low power. How much

**Dave Jones:** current will that actually take at 3 years? Well, I've got my computer here. Okay? 24, you follow along at home. 24 hours in a day * 365 days in a year 8,760 * 3 is basically 26,280 hours. Divide 100 mA hours by that, and

**Dave Jones:** I'm just invert my register there, and we're looking at about 3.8 microamps here. So, basically, for a 3-year battery life digital watch, for one of these coin cells, you're looking at double the power consumption, 4 microamps, of the sharp memory LCD. Granted, this

**Dave Jones:** one is only this static consumption, but really the dynamic consumption, ticking over at once per second, say, for a digital watch, it's not hugely, you know, larger than this. So, it's you know, it's basically it's not going to

**Dave Jones:** be lower. This is still probably going to beat almost any unless you engineer it really well like you get in a watch with the custom A6 and everything else. Ultra low power solution. Any microcontroller with an LCD is going to

**Dave Jones:** take more than this. So, let's actually just go in and have a look at some microcontrollers and confirm that because there were a lot of people out there that said, "Hey, just roll I've done a do-it-yourself LCD tutorial

**Dave Jones:** make your own LCD tutorial video linked in at the end if you haven't seen it. Where I could design a custom LCD or I could use one. We could search Digikey for a custom seven-segment LCD. I've got some here. You can get them on Digikey.

**Dave Jones:** It's not a problem. Oh, all right. Here we go. Out of the 1500 LCDs, we want a seven-segment one. None of that 14-segment rubbish as much as I love 14-segment displays. So, let's say we want five, six, or eight. Yeah, they're

**Dave Jones:** all they're all pretty large. I'm I'm after a quite a small solution. So, anyway, you might be able to is Okay, that's a plasma. That's been miscategorized there on Digikey. Oops, you know, you you find errors like that occasionally.

**Dave Jones:** Anyway, these are quite large, but you could potentially either roll your own LCD as I've shown in previous videos. It doesn't cost much at all. You could do it if you really wanted to a segmented LCD or you could find an off-the-shelf

**Dave Jones:** solution, but even these like you know, buying one of these is not not hugely cheap either. So, what do you need for a microcontroller plus LCD solution? Well, first of all, you need an ultra low power microcontroller. There's quite a

**Dave Jones:** few of those on the market from many manufacturers. No worries. But, you also need one that's got the LCD driver built in. In particular, for a six-digit display for example, you know, that's a quite a large-ish requirement in terms of number of

**Dave Jones:** segments to drive. So, you're looking at a bigger uh chip, for example. So, let's actually go into one of the um traditional leaders in low-power uh micros. They've got an app note here, this white paper thing, uh the TI

**Dave Jones:** MSP430. 100 nA uh storage mode here, less than 500 nA in standby, less than 1 microamp in RTC mode. Um we we don't need a real-time clock here. We just need it to update the display. The display's not static.

**Dave Jones:** You have to be still running the core at, say, 30 the internal low-power clock of 32 kHz, for example. There's no point running it any lower than that, really. 32 kHz is the go. Most micros for low-power solutions will have built-in

**Dave Jones:** uh 32 kHz um you know, RC oscillators, so no problem. You don't need an external crystal. Timing requirements and there's no exacting timer requirements, so it's not a problem. But, already we're pushing a microamp just running the RTC mode. Anyway, um I know this is

**Dave Jones:** TI, and it might be a bit biased, but they're trying to do an unbiased comparison with the PIC uh 24F micros over here, okay? So, storage versus uh sleep mode. Now, storage mode is just where the microcontroller can

**Dave Jones:** retain data on the internal SRAM. It It completely shuts down. The processor's not running, but it can actually wake up with external interrupts and watchdog timers and other uh things like that. But, it's basically just keeping data in

**Dave Jones:** SRAM going, and that's it. And you know, it can get as low as 100 nA over here. The PIC is technically lower, but TI are claiming this is where you need to get into the nitty-gritty. So, you can't

**Dave Jones:** just say go into a data sheet here and take like the banner spec up the top. You know, watchdog timer deep sleep current. Like, you can't just take that at face value. You've got to know exactly what your requirements are, how

**Dave Jones:** you're going going wake the thing up. Does it need Can it wake from an internal watchdog timer? Can it uh wake from an external interrupt and or you know, some other thing like that? And that's what TI are trying to get to

**Dave Jones:** here. So, there's lots of lots of intricacies in low power design like this. So, they're claiming that their low power mode four at 100 nanoamps, even though the PIC claims to be like 35 nanoamps or with the RAM thing enabled

**Dave Jones:** to store some contents, it's 80 nanoamps. But, with a brownout reset option, it's a it actually takes more. So, it's 60% plus higher they're claiming over here with a watchdog timer. They reckon the MSP430 is 600 nanoamps. Over here, 850 nanoamps.

**Dave Jones:** Anyway, what does all this have to do with LCD? Not much because if you search this for LCD, they won't tell you anything. There's no matches whatsoever. So, this is not driving an LCD. But, basically, to drive an LCD, you've got to have the core of

**Dave Jones:** the processor or at least the LCD module running. Then, it's got charge pumps there that have to drive the bias voltages for the LCD. If you got the like a quarter bias LCD or something like that. Like, there's a

**Dave Jones:** there's a few intricacies in there. I go into Microchip's Nanowatt type ones for the ultra low power mode, extreme low power. Do they call it? No, they don't. Used to call it Nanowatt, didn't they? Anyway, you go into the 8-bit

**Dave Jones:** microcontroller ones and none of them Not the 8-bit PICs, low power ones, none of them have LCD controllers built in. So, wah wah wah wah right there. You're basically pushed in to the 16-bit PIC24F family and only these higher-end ones

**Dave Jones:** down here have LCD modules in them. Look, so you're basically got to get one with a crypto engine and a USB and all sorts of things. And then, if you go in and have a look at the minimum bare minimum microchip one,

**Dave Jones:** liquid this year liquid LCD liquid crystal display, I can say that, controller, these are like big chips. They're 64K SRAM. Not only are they expensive, but they're quite large as well. I think the smallest package is like a a 44 or a 64 pin

**Dave Jones:** you know, TQFP or a QFN. It's like man, a gross overkill. With this thing, it takes two microamps static mode. Plus you can drive it with a 3 cent microcontroller. It's going to be hard to beat this if

**Dave Jones:** cost is no object, of course. But hey Dave, there's other LCDs like this STM one, the 32L0X3. It's like a a it's got an LCD driver, 4 by 52, 8 by 48. No worries, right? But once again, it's these are like quite

**Dave Jones:** large, 20K of SRAM, 6K of embedded EEPROM, 32 pin is the minimum package, right? These I don't even have to look up the prices to know these aren't going to be hugely cheap. So you go into the product selector here, LQFP48

**Dave Jones:** package, 32K of flash, 32 like you know, that's that's a significant part that has an LCD. Like wow, like gross overkill for simply a power up counter like this. It's sacrilege. But hey, if you look at the data sheet for this, okay, 400 nanoamps

**Dave Jones:** in stop mode, 16 wake up lines, that's pretty good. 800 nano in stop mode plus RTC plus 8 kilobytes of SRAM retention, data backup, 88 micro microamps per megahertz in run mode. So you'd be using like stop mode for sure,

**Dave Jones:** assuming that the LCD controller works in stop mode. It may not. Search for that. Liquid crystal display. Drives up to eight common terminals, 32 segments, late phase inversion to reduce power consumption and EMI. And bingo, the LCD controller can operate in stop

**Dave Jones:** mode. There you go. So, it can be continuously updating. And then if you wanted to change it, like if you had a a clock, for example, and a real-time clock running, you just interrupt that like once every second, and then you

**Dave Jones:** just update the display, and then go back down into stop mode, which was what, you know, 800 nanoamps or something like that. So, in RTC mode, real-time clock mode. Right. So, you've got to go right down to the LCD

**Dave Jones:** controller down here, okay? And this is supply current and VDD 2 volts. Well, let's say it's supply current at 3 volts. Bingo, we're up to 3 microamps. And that is going to be I think that's in addition. Look at the asterisks down

**Dave Jones:** here. One, LCD enable with 3 volts internal stepper active. One 1/8 duty, quarter bias, division by all pixels active, no LCD connect no LCD connected. So, with the extra little bit of capacitance on there, it depends how like often you update it and stuff like

**Dave Jones:** that. Like like it's anyway, it's already more just this. And also, it doesn't say anything about not including the residual consumption. So, basically, you know, you're looking in the order of really not going to get out of jail

**Dave Jones:** under 4 microamps. So, double the consumption of this sharp memory LCD just to keep that solution of an LCD on a microcontroller running for this particular one here. Right. And I'm back to the PIC here, and I'm trying to find,

**Dave Jones:** you know, it's got deep sleep, brownout reset, delta and current like I've found the LCD yet. And by the way, there's I I spoke about the low-power RC oscillator, the 32 kHz one before. Here's the typical figure. This is over temperature

**Dave Jones:** range, doesn't vary a huge amount, but it could be anywhere from the min-max there. So, as I said, if you want time and accuracy, you're going to have to use that external 32 768 kHz watch crystal. And but for an

**Dave Jones:** application like this, no wuckers. Look at all these performance curves. Ah, going to town. Low power sleep, but ah, give me LCD. Op amp, comparators. Ah, wow. How many at 353 page data sheet? How many errors in it?

**Dave Jones:** Guaranteed. Aha, DC characteristics. Here we go, LCD. Right, so that looks like a static from anywhere from 0.8 to 3 microamps external internal. So, once again, that's just the LCD module current. LCD external internal 1/3 bias delta LCD. Right. Okay, so that's

**Dave Jones:** without the charge pump. With the charge pump here, you're Yeah, it bumps it right up to 20 microamps. So, if you've got a complex LCD, it needs all the charge pumps and stuff, going to come and get you there. And it jumps up by

**Dave Jones:** almost an order of magnitude there. So, but once again, like 3 microamps, right? Max. Okay, the typical figure might be 0.8. So, looks like the PIC's doing better than the STM micro in this particular case, but if you're designing

**Dave Jones:** for worst case parameters, which will change over temperature and and stuff, then you've got to which gives minus 40 to plus 85 here. That's only for the LCD, so then you've got to add on the extra. The PIC24F

**Dave Jones:** plus a custom LCD couldn't do the same current consumption as this. I'll give it that. But as I said at the start, yeah, you've got not only the cost of the custom LCD, but the cost of the micro as well, and it's a

**Dave Jones:** big micro cuz this is the smallest one we can get. I don't even want to know like the cost of that. It's not going to be a cheap micro, not with that amount of memory. What? No. Ah, damn it. Dev kit. Let's see what

**Dave Jones:** Grant Imahara tells us. Do they have it? There you go, five bucks. Like, you know, four bucks in 100 off quantity. That that sort of stuff. And it's a big ass micro. Like, okay, so let's have a quick look at the TI MSP 430.

**Dave Jones:** About there's nothing in the parametric search here for LCD. Aha, there it is, LCD there. So, you got to select drill down into features, select that, and we can sort by price here. 95 cents. There you go, 60 60 pins.

**Dave Jones:** Like, you know, overkill, but okay, let let's just run with this 48-pin jobby here, shall we? And once again, uh doesn't tell you anything in your high-level specs. You've basically got to drill right to the end. At first

**Dave Jones:** browse over this, I'm just not having any luck finding a consumption uh for the LCD. It could be in there, but really it's not that terrific. Okay, it might be lower cost than this if you get like a $1 LCD uh micro, for example,

**Dave Jones:** and you get your custom LCD, however much uh that uh cost to get made, and you amortize the cost over there. They're still like a dollar each or something like that. It could be a cheaper solution, but it's bigger, more

**Dave Jones:** overkill than this little job, as I said, with a 3-cent micro. Right, so let's assume that we've got either of those solutions, and we're talking in the order of like two microamps uh standby consumption. Don't worry about when it powers up and all that sort of

**Dave Jones:** jazz. If we look at the uh circuitry here, we've got our product circuit. Let's say it's powered from a USB, it's powered from whatever. Anyway, we have to isolate our battery that we're going to use or our supercap or whatever our

**Dave Jones:** charge storage element is, we have to separate it from the rest of this, so that when you power down this, um all the back circuitry in here we're we're we're we're not going to get any back charge. So, that's why you need to put

**Dave Jones:** uh that a diode in there, so it stops any reverse current. We're going to assume that we're going to get no leakage on that diode, like a you know, a 1N4148 or something will have like tens of nanoamps. It's not, you know,

**Dave Jones:** it's not much. It It's good enough for Australia. So, then the battery or the supercap is only powering the micro or and the LCD, and that's it. Total consumption, 2 microamps. So, I just wanted to have a look at these funky new

**Dave Jones:** TDK CeraCharge things. These are basically surface mount batteries, 1812 case size. You can pick and place them with your regular pick and place machine. And like really cool. I'm not actually sure how much these things cost, but unfortunately, they've only

**Dave Jones:** got to up to 1,000 recharging cycles. So, I you'd have to go into the details of what happens, the longevity of them after that. Anyway, it's it's basically a multi-layer ceramic capacitor. And you might think, "Okay, well, it's

**Dave Jones:** just a capacitor. Why is it got 1,000 charging cycles?" Well, basically, they're going to have ridiculously thin tolerances in there, and basically, they're Yeah, they're going to have a finite life. Unlike a regular regular multi-layer ceramic capacitor, which wouldn't. This only goes to 1.6

**Dave Jones:** volts. Wow, that's bugger enough, all isn't it? Something like that'll be good enough to operate like a real-time clock chip. That's no good to operate our sharp memory LCD over here, which needs It just says 3 volts. There's actually

**Dave Jones:** no Without the data sheet, we don't know what the lower limit of that is. Let alone the micro. So, you can actually let's stack them in in series to get the 3.2 volts. Beauty. That could do the business. But you halve your

**Dave Jones:** capacity. And well, unfortunately, I think we're going to come a gutser here. 100 microamp hours. You can't get any That little tiny size is not magic. unfortunately. Um 100 microamp hours at 2 microamps, that's only 50 hours. Mhm, what what what what? Not good

**Dave Jones:** enough. So, let's actually look at some super capacitors, shall we? Um 1,500, wow. They're a thing these days. When I was a boy, super capacitors, jeez, that was only a wet dream. Here we go. Like the look of those. Nice surface mount

**Dave Jones:** ones from Seiko. 11 millifarads. 6.3 V surface mount, 30,000 in stock, 68 cents. That's the business. Tape and reel packaging. Winner, winner, chicken dinner. Let's have a look. It's the thinnest and smallest chip-type electric double layer capacitor. Unique ceramic packaging,

**Dave Jones:** superior air tightness is used. As a result, it offers leakage resistance. Cool. Backup power supply. It's It's exactly what we're looking at. Ah. What what what what? 4.6 microamp hours. Ah. So, that's really for short-term stuff. Once again, what do you expect in a

**Dave Jones:** package that small? I don't know. I'm going to tell him he's dreaming. Okay, so they're 11 millifarads. Uh 80 millifarads. We're still not there. Look, these aren't These These are getting decent size ones, but you know, 200 millifarads, we're we're still not

**Dave Jones:** there. It was only like a couple of hours discharge. And of course, uh you have to watch the thing with uh well, batteries and with super caps as well, you have to look at the time over the minimum uh discharge. So, what what can

**Dave Jones:** your uh product, in this case the LCD, the sharp memory LCD, or your micro control plus LCD work down to and still give you required contrast uh that you need to actually display your uh number when the power's off. We We just don't

**Dave Jones:** know what that minimum limit is. It could be 2 V, it could be 2 and 1/2. Don't know. And really what I want is an SMD, like a small solution. I'm going for a small LCD like this. Once again, your mileage

**Dave Jones:** may vary, but I I'm going for an LCD something this small. Ideally, I want a tiny little source for it, right? So, if you go up to a 1 farad capacitor, that's what a 1 farad supercap uh looks like.

**Dave Jones:** That's a 2.7 volts. That's an AVX uh job. Really top quality. That's a 10 farad jobby. And that's a 50 farad 2.7 volt. So, these things are just like enormous. All right, so let's calculate how long a supercap will last. In this

**Dave Jones:** case, I'll take this monster example, 50 farad supercap. Okay, uh we'll use an online calculator makes it uh easy. Uh you can There's the formulas down there. Have I done a tutorial on time constant formulas? So, we're looking at 3 volts.

**Dave Jones:** And of course, we need a minimum voltage that we're going to discharge to. Let's say 2 volts. Our capacitor size 50 farads. We don't worry about the ESR. Doesn't matter with uh this sort of uh low current. And maximum of 2 microamps.

**Dave Jones:** And bingo, it calculates out that uh you put it on the confuser. Calculates Let's round it to 7,000 hours. It might be okay for my application, but look at the size of the thing. Anything smaller, 1 farad jobby, it's 50 times less.

**Dave Jones:** Forget it. So, supercaps aren't any good at all if you need small size and long discharge. Even at a tiny 2 microamps, which is about as low as it gets. Really, you can engineer it slightly lower, but you're not going to get an

**Dave Jones:** order of magnitude lower, really. Um but even then, they they still aren't going to do the business. They might if you've got heaps of space available. Okay? No workers. You can't beat battery chemistry. The CR2016 battery over here.

**Dave Jones:** Oh, I love the high energy density chemistry. Uh 100 milliamp hours and that is to 2 volts. Okay, so exactly the same from 3 volts to 2 volts discharge. It's much smaller volume than this. 100 milliamp hours divided by our 2

**Dave Jones:** microamps, that's 50,000 hours. No comparison between a coin cell battery and you can even use like a smaller one. I'm just using 2016 as an example. Or you can get you know, solder ones onto the board, the tabs and and stuff

**Dave Jones:** like that. If you are okay with the product actually being like like single use. But in my particular case, it'd be nice if it like recharged. If it did it Look, this is why I'm trying to avoid a

**Dave Jones:** battery solution altogether, a super cap solution altogether. And that's why I looked at originally the e-ink display cuz it takes all this out of the equation. And if we could simply get an e-ink display like this, this size with

**Dave Jones:** the seven segments, you don't need any backup solution at all and it does exactly what I want, which is just leave the static image on the display. There's just no contest between two solutions. You'd go e-ink every time if you could

**Dave Jones:** get it because there's just no contest. around with super caps and batteries and and discharge curves and and and times of recharging schemes and back diode to prevent this and that. Nah, like come on. Anyway, poor old super caps, they just

**Dave Jones:** don't cut it and even these these like little cool technology of these little micro SMD batteries, they just don't cut it either. Only for very short cycle times for preventing stuff when they go down and things like that. So there you

**Dave Jones:** go. I've waffled on enough already, long enough, more than long enough. And there you go. I wish I could get an e-ink. I'm still going to look at getting e-ink uh still working on it. I just wanted to

**Dave Jones:** people wanted to know about this stuff. So, hope you found it interesting. If you did, please give it a big thumbs up. As always, discuss down below. Catch you next time.
