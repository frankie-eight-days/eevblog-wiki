---
video_id: ttvgJqbCXRs
title: EEVblog #1018 - ZeroPlus Logic Analysers
url: https://www.youtube.com/watch?v=ttvgJqbCXRs
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 26, "3": 41, "4": 54, "5": 69, "6": 84, "7": 104, "8": 120, "9": 135, "10": 152, "11": 169, "12": 183, "13": 202, "14": 217, "15": 231, "16": 246, "17": 264, "18": 284, "19": 304, "20": 320, "21": 337, "22": 352, "23": 362, "24": 375, "25": 391, "26": 404, "27": 416, "28": 430, "29": 441, "30": 454, "31": 466, "32": 479, "33": 489, "34": 501, "35": 514, "36": 526, "37": 543, "38": 559, "39": 573, "40": 587, "41": 603, "42": 621, "43": 638, "44": 655, "45": 668, "46": 683, "47": 701, "48": 716, "49": 730, "50": 744, "51": 759, "52": 779, "53": 791, "54": 801, "55": 817, "56": 832, "57": 853, "58": 872, "59": 887, "60": 901, "61": 914, "62": 928, "63": 941, "64": 957, "65": 969, "66": 980, "67": 999, "68": 1012, "69": 1029, "70": 1044, "71": 1058, "72": 1071, "73": 1086, "74": 1104, "75": 1119, "76": 1135, "77": 1150, "78": 1162, "79": 1178, "80": 1194, "81": 1208, "82": 1225, "83": 1240, "84": 1255, "85": 1272, "86": 1284, "87": 1301, "88": 1321, "89": 1339, "90": 1349, "91": 1364, "92": 1376, "93": 1391, "94": 1404, "95": 1414, "96": 1425, "97": 1439, "98": 1452, "99": 1467, "100": 1479, "101": 1493, "102": 1504, "103": 1517, "104": 1531, "105": 1542, "106": 1554, "107": 1566, "108": 1582, "109": 1601, "110": 1615, "111": 1628, "112": 1649, "113": 1665, "114": 1684, "115": 1694, "116": 1711, "117": 1726, "118": 1738, "119": 1753, "120": 1765, "121": 1776, "122": 1791, "123": 1807, "124": 1816, "125": 1829, "126": 1843, "127": 1856, "128": 1868, "129": 1882, "130": 1903, "131": 1922, "132": 1940, "133": 1954, "134": 1968, "135": 1981, "136": 1999, "137": 2017, "138": 2028, "139": 2039, "140": 2055, "141": 2074, "142": 2092, "143": 2105, "144": 2119, "145": 2130, "146": 2145, "147": 2165, "148": 2180, "149": 2197, "150": 2211, "151": 2226, "152": 2243, "153": 2258, "154": 2276, "155": 2292, "156": 2304, "157": 2313, "158": 2331, "159": 2346, "160": 2360, "161": 2371, "162": 2389, "163": 2409, "164": 2424, "165": 2437, "166": 2455, "167": 2472, "168": 2485, "169": 2500, "170": 2527, "171": 2548, "172": 2566, "173": 2583, "174": 2605, "175": 2622, "176": 2638, "177": 2652, "178": 2670, "179": 2685, "180": 2702, "181": 2718, "182": 2734, "183": 2748, "184": 2764, "185": 2779, "186": 2801, "187": 2814, "188": 2827, "189": 2854, "190": 2870, "191": 2887, "192": 2904, "193": 2926, "194": 2942, "195": 2959, "196": 2973, "197": 2987, "198": 3000, "199": 3015, "200": 3036, "201": 3052, "202": 3069, "203": 3083, "204": 3102, "205": 3118, "206": 3134, "207": 3147, "208": 3163, "209": 3178, "210": 3193, "211": 3210, "212": 3227, "213": 3242, "214": 3255, "215": 3272, "216": 3286, "217": 3299}
---

**Dave Jones:** Hi, today we're going to take a look at an interesting series of logic analyzers from a company that I hadn't heard of before, Zero Plus. They're a Taiwanese company and they very kindly sent in a selection of their products. Now,

**Dave Jones:** go check out their webpage. I'll link it in down below and I'm actually amazed at the range of stuff that they've got. They've got like this Arduino starter kit with their which they've sent in which I don't have price or any other

**Dave Jones:** details on. I don't seem to doesn't seem to be available yet. So, I might leave that for a second video. We've got a low-cost logic analyzer here called the Logic Cube or the LAP-C series and this ranges anywhere from $135

**Dave Jones:** for the bottom of the range unit which is cheap as up to $1900 for the top of the range unit depending on the memory configuration and the number of channels and stuff like that. They've got about a half dozen

**Dave Jones:** models in between that at various price levels and they've got this F standard unit here which looks like it might be some USB hub thing, but it's actually not. Uses USB 3 connections for the interface to the probes which we'll take

**Dave Jones:** a look at which is quite novel. And this one goes there's I think at least two models in this series. It starts at $3000 and goes up to $6000 for top of the range unit for a 64 channel job.

**Dave Jones:** Super high-speed, super professional. And on top of that, they got units which actually they do protocol analyzers as well. They do serial generators and stuff like that. And they've even got one eMMC memory analyzer system which is like $25,000 worth for professional

**Dave Jones:** design and analysis of eMMC memory used in computers and and hard you know cheap cheaper hard drives and cheaper interfaces and stuff like that. So, you know, really a wide range of tools. So, we'll actually do teardowns and have a quick

**Dave Jones:** play around with these two here. And as I said, I'll leave the Arduino starter kit for later. So, let's get to it. Zero plus high-quality professional instruments Taiwan Excellence Award, I guess, 2009. They've been going for a long time and they'd won it for all the

**Dave Jones:** stuff that they've developed. And here's the different models. I believe that we've got this top-of-the-range unit, which is at $1,900. But as I said, the 16 channel unit down here starts at $135. So, very affordable. And I believe, but

**Dave Jones:** have not checked this yet, that in 2016 they say on their website that they are actually giving away all their protocol decoders for free. And they have got a metric buttload of protocol decoders. It's absolutely incredible. I'll have to show you the list. It's one

**Dave Jones:** of the most comprehensive lists of protocol decoders I've seen. But yeah, anyways, from 135 bucks up to like, you know, closer towards 2 grand depending. And let's have a squeeze at it. I love the case. Haven't even opened it yet.

**Dave Jones:** There's this $129 optional pulse width trigger module as well. So, that's interesting. I'm not sure why they couldn't do that inside the unit. Inside, presumably, you're going to find FPGAs inside all these doing all the heavy listing heavy lifting. And these are, while they

**Dave Jones:** are USB logic analyzers, they are not like the cheap Saleae logic, for example. These actually have built-in sample memory. So, they're not streaming logic analyzers. So, let's have a squeeze at this. There it is. It's our Logic Cube. So, this is the

**Dave Jones:** 32-channel version. But you can get the 16-channel version. I presume there's just like an extra board in there with some extra hardware. So, and the memory, I would presume that the memory is the same and it's just software

**Dave Jones:** limited. but we won't know that until we take the thing apart. So, we'll do a quick teardown. 500 milliamps, so USB powered. It's got your standard 1 in header, all nicely color-coded. That looks very nice. We've just got a power

**Dave Jones:** button on the front and some LEDs and USB 1 .1. So, we get a USB cable. We get the requisite into like just you know flying lead cables because these are not particularly quick. We're talking about a 75 MHz bandwidth across

**Dave Jones:** all the models from the low-end one has a 100 megasamples per second 100 MHz sample rate in time in analysis mode and I think 75 in state analysis mode and the top of the range one has 200 MHz sample rate and 100 MHz state

**Dave Jones:** analysis mode. So, you know, great for most you know, generic uses for a logic analyzer. No problems whatsoever. And sample memory on these ranges from 32K per channel for the bottom of the range unit 130 odd dollar unit up to 2 megabits per

**Dave Jones:** channel for this top of the range 32 channel unit, which is the 32,000 for those playing along at home. So, that's not a huge amount of memory. It's probably adequate for most general-purpose use, but it does have sample compression as well up to eight

**Dave Jones:** times. So, you can multiply it depending on the scenario of what you're actually measuring the signals you're measuring. It can actually enable sample compression, which then in can multiply your memory by effectively up to eight times. So, I'm a big fan of logic analyzers that

**Dave Jones:** have both hardware memory like this and software compression-based memory as well. You pretty much get the best of both worlds. The The compression's really handy when you have uh you're trying to measure things that have packets like spread very widely apart.

**Dave Jones:** You know, you might have a packet which lasts for a microsecond of data you want to sample and then it's only once every second. Well, you don't want to be pissing away your memory by sampling all those zeros. So, you can

**Dave Jones:** get sample rate uh compression. So, I don't believe this compression on this is as good as uh other logic analyzers I've seen. They only claim up to eight times, but it's going to be handy. So, what else have we got? We should have

**Dave Jones:** our requisite test clips in there. Yep, we've got our all our little color-coded easy hooks. Very nice. We get our software. Software's what it's all about, of course, and some installation guide and whatnot. Cuz the thing with these logic analyzers, you know, for 130

**Dave Jones:** bucks retail, there's not much in them. There's going to be like an FPGA and then a USB interface micro um and some uh input front end uh to do the plus-minus 6 volts um a trigger. It's got adjustable

**Dave Jones:** trigger threshold level uh from plus-minus uh 6 volts in like 0.1 volt steps or something like that. So, I'll have a bit of circuitry for that. But there's not much in these things, which is why the likes of say the uh Saleae

**Dave Jones:** logic analyzer, uh you can buy a clone on eBay for like 1/10 the price and you just download the software and boom, you can use it. And they just can't stop people from doing that. Um and I don't know if there's any

**Dave Jones:** clones of the Zero Plus's out there, but that's where all their money goes. It's not necessarily in the hardware, although that F series that we'll have to take a look at it's probably some real um decent high-end hardware in it.

**Dave Jones:** But something like this is not, you know, hasn't particularly got a lot of expensive hardware in it. So, it's all in the software and trust me, as someone who has developed logic analyzer software and used to sell it, um my own

**Dave Jones:** one way back in the day um which I'm sure I showed in a video somewhere. Anyway, it's a lot of work, especially all the protocol decoding and everything else. Um so, yeah, all the values in the software, not necessarily the hardware.

**Dave Jones:** They, you know, you almost give the hardware away. But But even though the hardware might be identical between the 100 or not huge amount difference between the $135 one and the $1,800 one, you're paying for the number of channels

**Dave Jones:** and you're paying for, you know, the software. You're paying for the software development, basically. Anyway, let's crack it open. And we're in like Flynn, and there it is. Um not a huge amount of hardware, but that's very nice. I like

**Dave Jones:** the look of that. Um they've got a nice little light pipes here to get from the LEDs up, uh which are up here, and guide the light up to the center of that. Oops, the switch fell out. And as you

**Dave Jones:** can see, they've got a Zero Plus branded chip in here. Now, I doubt this is going to be a custom ASIC, but you never know. But they've obviously had it had it branded to their own chip. So, what that

**Dave Jones:** one is, you know, we're not going to Well, could we use the logic analyzer itself to probe its own clacker and figure out what that chip is? Anyway, I won't be doing that in this video. But we've obviously got some sort of a USB

**Dave Jones:** interface chip here. And then we've got our sample memory up here. That'd be SRAM, of course, none of that DRAM rubbish. Actually, this is very interesting. Look at the Presume that's the day code, 29th week '09. Um is it an ASIC which they developed a

**Dave Jones:** long time ago or maybe like a custom gate array or something like that, perhaps? Um maybe they have gone to that effort, so that wouldn't be easy to clone, really. So, let's have a look here. We've got a LVT 16

**Dave Jones:** 245. So, yep, that's our input logic buffer. And this one over here is actually an FCT 245. So, once again, that's just another transceiver. You may not be able to read that, but I've checked that under the mantis. So, we

**Dave Jones:** haven't found our comparator yet. And do we have a Cypress SRAM there for those playing along at home? And a USB interface chip, I'm not sure what that puppy is. I'll have to look up that, but uh yeah, not a huge amount else. Our

**Dave Jones:** comparators must be over here. Have to take the label off. And nope, we've got another identical um LVT 16245 transceiver under there. So, we've got two of those. And if we go over here, I have no idea what that one

**Dave Jones:** is. Can't find any info on that whatsoever. So, where's Wally? Where is the logic level threshold comparators? This unit is supposed to have up to plus minus 6 volts selectable threshold for each channel. Are they doing doing some sort of weird

**Dave Jones:** resistor summing thing going on here driving and then a resis- like I don't weird. So, they're definitely not doing it in the probes cuz there are no probes. Um like it can't be doing it in the custom ASIC cuz that's on the other side of the

**Dave Jones:** transceiver over here. You've got to do it on the input side of the transceiver. So, I'm baffled as to how they're achieving that. Hmm. Anyway, I maybe expected like a second board in here for the extra extra 16 channel one, but uh

**Dave Jones:** this is like the 32-channel model. So, I presume it's just a programming difference between and maybe they only populate all the passives and you know, they only populate one of these or something like that for the 16 uh

**Dave Jones:** channel version. But, the PCB layout's likely to be uh absolutely identical between the two models. And once again, you might say, yeah, that's a rip-off. One's 135 bucks right at the bottom end, the other one's like 1,800 bucks right at the top end, but

**Dave Jones:** they've got to pay for all the software development. That's just how it works. And this puppy right down in here is a Microchip uh E-squared PROM. So, is that where they're storing the product configuration or something like that, perhaps? Hmm, might be hackable. I

**Dave Jones:** don't know. Good on you, Pete. Version 1.0 B. Hasn't been many changes. I guess Pete's good. He got it right the first go. And no surprises for finding the pulse width trigger module is just a Lattice ISP mark

**Dave Jones:** PLD. So, yeah, that's all it does is they implement pulse triggering. So, this is an optional thing. I'm not sure how it plugs into your system cuz it doesn't plug into the logic analyzer anyhow. So, I guess you'd have to RTFM.

**Dave Jones:** Read the freaking manual for that one. Aha, there you go. It does actually hook into the this side of it. Is that like a dedicated interface for something like that? But, obviously there was a customer need for pulse width pulse width trigger

**Dave Jones:** module. They couldn't do it in their ASIC or whatever it was. So, they had to develop a little external doohickey to do it. But, anyway, that's not a USB logic analyzer. This is a USB logic analyzer. As I said, I believe it starts at three

**Dave Jones:** grand, but we have the This is the F standard series. This is the fully optioned up 64 channel version, the Lab F1 64 channel. So, USB 3 interface requires a fair bit of grunt. 9 volts at 5.5 amps. Thank you very much. And let's

**Dave Jones:** have a look on the side here. We've got our USB 3, but it's it's basically not designed to stream. It is it's got hardware memory built in, capture memory, all that sort of stuff. It's not a USB streaming, but

**Dave Jones:** you acquire so much data and you want to get it out quick, you can do that. But, hey, look, it's got a little micro USB clock out, a stack, whatever that is. I don't know. I have to read

**Dave Jones:** the manual. And clock in. And DC, a couple of fans. Where are they? Yeah, a couple of fans on the other end because it is probably going to get a bit warm inside this puppy. And look, they actually use USB 3 as the probe

**Dave Jones:** interface. Let me show you the probes. And it's got trigger out for going to, you know, system integration and other sorts of stuff. They even provide you a nice looking BNC cable. Sweet. Now, check out what you get. In fact, that's not all of it.

**Dave Jones:** You get a squillion, well, 64, I guess, US little micro USB 3 cable. So, standard USB 3 to micro USB 3, a little tiny short ones. Nice, and they're all color coded so that you can get the different channels. Sweet, I

**Dave Jones:** like that. And check out what we've got. In all of this, we've got our easy hooks, of course. But in these, we have, once again, 64 of these, all color coded. We have, curiously, look at this. This is our

**Dave Jones:** micro USB 3. We've got a little trimmer pot in there for tweaking the compensation of this thing. You know, hold your tongue at the right angle and compensate the probe. I don't know what the extra two pins out there

**Dave Jones:** is for. Maybe that's to go off to It's the same as the input, anyway. We've got the standard twisted pair input. Now, the thing with this is that is when you're designing a system that you know you're going to like a

**Dave Jones:** real complex digital system, you know you're going to have to debug it with a logic analyzer, protocol decoder. You're going to have to, you know, like debug all the memory system and everything else. You won't jump to the final prototype.

**Dave Jones:** You won't find jump to the final product version of your PCB. Or you might, but you'll also design a version of your PCB that has a whole bunch of these .1 in and breakout headers usually right around the chip that you want to debug.

**Dave Jones:** So, the chip will be there and you'll have a whole bunch of headers surrounding that so that during debug and that'll be a special debug version of the board, special development version of your product PCB where you just go around and plug in your 64

**Dave Jones:** channels right around your memory chip or your processor or whatever it is you're trying to debug. So, anyway, that's rather interesting. It's a little bit how you're doing in terms of the heat shrink, a little bit do-it-yourself. It's not hugely

**Dave Jones:** professional. I don't know why they just didn't, you know, they're making enough of these things. Don't know why they just didn't mold a like a custom little case. That wouldn't have cost much to enclose that. But anyway, they've gone for the heat sink

**Dave Jones:** heat shrink solution. So, we'll cut one of those off and have a look. But these are the probes. So, they use the USB 3 of course to go over to the unit. And there's nothing wrong with that. It's

**Dave Jones:** not actually USB. This won't be a USB interface. They're just using the USB 3 cable for its ubiquitousness, its cheapness, its controlled impedance, everything else for high-speed differential pair. So, that's basically what they're using the thing for. They're probably transferring

**Dave Jones:** some power over as well for doing this. So, USB 3 was actually a smart choice there. So, we'll just strip this puppy open and see what she has to offer in there. We can see the decoupling caps on

**Dave Jones:** the bottom side here and I'm a fan of the heat shrink construction over boards like this. But for a $3,000 to $6,000 logic analyzer, you you expect a case. I mean, I didn't expect to see that. There we go. They've put the strain relief

**Dave Jones:** either side of the piece. Oh, they've blobbed it. They've blobbed it. Look at that. How rude. We've been slimed. Yeah, so we just won't know what's under there. Anyway, it's obviously got uh power and you can see the differential

**Dave Jones:** pair. These are all like individual uh channels, so the differential pair carries the data and then they'd be using the uh power pins to power all that. The compensation uh trimmer resistor there and that's about all she wrote. It's not a huge

**Dave Jones:** amount on there. Some decoupling on the bottom. So, whether or not that's some sort of, you know, custom uh front-end solution, I don't know because this one has a 1-gig bandwidth or it's 1-gig sample rate, I think. So, this one is

**Dave Jones:** like this logic analyzer is serious business. So, yeah. Um, but we won't ever know. Aw, boo hoo. So, anyway, this looks and feels like a serious bit of kit. So, let's crack it open. All right, let's take this sucker

**Dave Jones:** off. I think it's it's going to lift going to lift off. Ta-da! We're in like Flynn and there it is. Woah! Isn't that nice? Wow! Getting your money's worth. Oh, look at that RFI gasket right across the top there. Isn't

**Dave Jones:** that beautiful? Spongy RFI gasket uh sealing down the uh top of the uh top of the USB connectors right through to the front panel to stop the uh all the little electrons escaping. Beautiful. So, this one's actually a

**Dave Jones:** 2015 design uh by the looks of it or at least the last revision was, uh which is quite uh much more recent than the other one which uh dates from the uh 2000s. Um, so as we've seen common in these

**Dave Jones:** sorts of products, like this is $3,000 or $6,000 depending on which configuration, might even be more for a higher-end one, you don't and you're not manufacturing the hardware in high volume, you just don't worry about costing these sorts of things. So, once

**Dave Jones:** once you find that they've used these little expensive power bricks. These are not cheap, you know, they I don't know, five or 10 bucks a pop or something or even more, you know, if you buy from Digikey, like 20 bucks a pop. Little

**Dave Jones:** These are the TI ones or the linear technology ones, but um anyway, little DC-to-DC can power power bricks, you know, designed to do all the voltage rails for the you know, the various FPGA and other logic and they've got no less than two,

**Dave Jones:** four, six, eight, nine of those inside this. So, yeah, I spared no expense. Oh, check out the check out the PTC there on the input. Oh, wow. That's serious business. Look at that. So, the designer just went off, bugger

**Dave Jones:** this, we want to protect that. Well, it's marked as a fuse, so it might be one of those solid-state resettable fuses. Is it marked? Yes, it is. So, they clearly just went off, bugger that, I'm sticking in the biggest, baddest ass one I can

**Dave Jones:** fit in there. Beauty, she'll be right. Now, interestingly, there's a bunch of unpopulated connectors. There's a 0.1 inch header up there, maybe some debug development programming {slash} interface, but look at all these little SMA coax connectors along there. I wonder

**Dave Jones:** what they're for. Hm. And for the massive amount of sample memory, they've gone for an off-the-shelf uh What is that? DDR3 1600. There we go. Well, that, you know, it makes sense cuz this thing is one gig sample

**Dave Jones:** per second sample rate. So, yeah, what a beast. And well, the rest of it, there's not a huge amount of you know, extra stuff in here. We've got our USB 3 interface for those playing along at home. Not sure what that one is. Can you

**Dave Jones:** read it? I don't know. Not too entirely fussed about that, but uh yeah, I mean, you don't need any of the transceivers on here or anything like that. You don't need the logic level threshold comparators or anything like that cuz it's simply

**Dave Jones:** receiving a twisted pair signal. That's all done in the probe. You receive a twisted pair signal on each of the USB connectors, and Bob's your uncle. But there's a whole bunch of dip switches in there, and doesn't seem to

**Dave Jones:** be one per channel. So there's 1 2 3 4 5 6 7 Oh, there's eight of them. Okay, so maybe some sort of bank configuration or something doing. I don't know. But yeah, it's basically all all the twisted pairs are just going to

**Dave Jones:** flow into this badass beastie over here, which is going to be once again some sort of custom FPGA or a custom gate array or ASIC/FPGA. Anyway, you certainly can't fault that hardware. It's very very nicely designed and laid out. Let's check the

**Dave Jones:** bottom. I don't seem to expect anything. No, just your regular bypass pass cap passes. There's a couple of others over here to do with what not. I don't know. Logic level transceivers, perhaps. That'd be just about it. But yeah, what

**Dave Jones:** that main beastie is there, I'm going to have to clip off that heat sink. But uh there's nothing else there. All the differential pairs, I can't see the traces running on the bottom. Can't see them running. Of course,

**Dave Jones:** they're not running on the top, so they're running on an inner layer of the PCB. Once again, super duper high-speed controlled impedance all the way with LBJ, and internal ground plane. So that could be a six or eight layer board.

**Dave Jones:** Aha, got you. Xilinx Kintex 7. That's a beastie. How much is that worth? That puppy is going to be at least a couple of hundred bucks. That's a bit of a beast. But there you go. This is like a

**Dave Jones:** classic use case for it, like a high-end FPGA like this uh one because it's got the transceivers built in for the uh you for the you know the differential pair serial it's got the Serdes uh decoders built in the

**Dave Jones:** serial uh decoders. Essentially it's got the high speed uh logic um stuff it's got built in uh memory as well for any sort of uh caching or anything like that that needs to be done and it can do of course all

**Dave Jones:** the processing that's an FPGA you can get it to do anything you want. You wouldn't be rolling your own uh ASIC for something like this unless you were looking at really high volume and something like this like a three or six

**Dave Jones:** 6,000 logic analyzers you're not going to be selling them in the hundreds of thousands you know you're going to be selling them in the hundreds thousands if you're lucky. So what they're going to be implementing in there of course uh

**Dave Jones:** is serial straight in so the 32 or 64 channel uh serial uh differential pair straight into the Serdes and then into the logic array where they're going to be implementing uh hard serial decoder functions decoder hard serial trigger

**Dave Jones:** cuz you can uh trigger off various a whole slew of different protocols. So that'll be programmed uh in there all your serial decoding you can all do that in hardware because it's all running in parallel on an FPGA. So that's the

**Dave Jones:** beauty of that and yeah I would have been surprised to see a custom ASIC on this puppy although I'm pretty much uh convinced that the one on the lower end the uh logic cube that we saw I think that's a custom

**Dave Jones:** ASIC which they did way way back cuz the company mentioned stuff about designing their own uh chips for various uh products that's like in the company history part of thing but for something like this yeah you wouldn't. You just

**Dave Jones:** whack a Kintex in there and Bob's your uncle. So that's certainly some uh decent hardware in this um quite professional uh as you'd expect from the uh price tag. This company's been going like uh 10 plus years or something like

**Dave Jones:** that so they know their logic analyzers and they pretty much uh specialize in this sort of stuff, protocol decoding and everything else. But, yeah, as good as the hardware is, it's only as good as the uh software, not only for the

**Dave Jones:** protocol decoding built into here, but also the software that uh runs on the PC, which lets you display it and do all the timing and state analysis and and protocol uh decoding and uh everything else. Although, this would have uh

**Dave Jones:** protocol decoding built in, it would only be for the purposes of trigger, I believe. It wouldn't be like uh they would be doing that, maybe sucking the data out, and then doing the full memory decoding, I would presume, in the software on the

**Dave Jones:** uh PC. But, you definitely want protocol triggering in the hardware. It's useless if you do it on a PC. You got to wait until it streams to the PC first, use the PC to decode it, and forget it. You're You know, your uh

**Dave Jones:** data's already flown off by the time your PC uh triggers that. So, it was all protocol uh triggering hardware is all done in there. That's a sweet bit of kit. Now, we'll be hooking it up and uh playing

**Dave Jones:** around with this, but here's this Arduino starter kit with logic analyzer. It's got like a cut-down version of the logic uh cube we've uh seen. And look at the uh little ring binder uh manual. I haven't put it in a ring binder yet, but

**Dave Jones:** I haven't had a look. It's got all these uh experiments. Wow. Wow. All these glossy cards. This is Oh, yeah, double-sided. This is brilliant. Wow. This is very impressive. So, yeah, I couldn't find a uh price or where this

**Dave Jones:** was available for a real-life applications. This looks really jazzy. Wow. They've put a lot of work into that. That's very impressive. So, let's have a quick squeeze inside the box, shall we? Ta-da. Look at this. That's what you get inside, for those

**Dave Jones:** playing along at home. So, you get your get a nice breadboard. You get What is that? Oh, I squared C RGB interface. Nice. Got a USB interface, we've got a microphone preamp. By the looks of it, you've got a

**Dave Jones:** little motor to make something spin. Um, and let's get that out of there. You get your Arduino Uno, of course. Looks like a genuine one. You get your requisite LCD, couple of little uh looks like it's an eight-channel logic

**Dave Jones:** analyzer, and a little Zero Plus. Cute. The Educator, the Lab Educator. So, they've done just a cut down version of that. Wow. That is and all the requisite probes and USB cables. That's fantastic. If you're after a kit with a

**Dave Jones:** a like a digital experimenter's kit with a built-in logic analyzer that and you want to play around with Arduinos, that could be really good depending on the cost of that. But, that's thoroughly impressive. Wow. Well done, Zero Plus. And well done, Alberto

**Dave Jones:** Piganti and David Anton Sánchez. And Sánchez. J- Sánchez. Got it. Brilliant work. All right, let's take a look at the software for the Logic Cube, shall we? Uh I downloaded this from the website, and it turns out that it wasn't the latest

**Dave Jones:** version from the website. When I ran it and installed it, installed no problems, USB driver, no problems whatsoever. But, then it told me, "Oh, it was way out of date, and here's the latest one." I downloaded a zip file, and I had to

**Dave Jones:** manually go do it. It not impressed. Uh my first impression is that No, it's a bit old school and clunky. It's actually uh designed only for up to Windows uh 2007, it says. So, you know, like what do you say about

**Dave Jones:** that? And here's the version that I'm playing with, uh 3. 14.02. But, yeah. Um, there just seems to be a lack of I mean, look, copyright 1997 to 2017. So, it it it gives me I get the impression that it is from 2007.

**Dave Jones:** They haven't put any mod cons into this thing. Now, let's you know, you've got all your basic stuff up here, okay? You've got your sample rate, you've got your memory size here, you've And you've got your uh pre- and post-trigger

**Dave Jones:** control. So, by default, 50% pre-trigger, 50% post-trigger, and all that sort of stuff, okay? But, have a look at the uh waveforms. Look, I haven't actually set up anything, but like first thing I notice is like I can't drag these waveforms around. I

**Dave Jones:** can't do anything like that. Now, let's actually um trip Well, actually, whoops. No, I'll What I'll do is I like I don't mind this. Of course, you can uh set the trigger up on each channel to uh positive, negative, positive, negative

**Dave Jones:** slope, or either slope, stuff like that. So, I don't mind that at all. So, we'll set that to either slope here, and I will run it. So, it's going to sit there and let me generate a signal. I've

**Dave Jones:** actually got the uh a Digilent Analog Discovery feeding in uh some signals here. So, I'll feed in a UART signal. Here we go. I'll generate that. Boom. And we're in like Flynn. But, look, I mean, we've got this uh navigator window

**Dave Jones:** down the bottom here. Now, the software is actually pretty basic. Um one of the frustrating things I I encountered first is that I couldn't just like drag the waveforms around like back and forth, like hold down the button, hold down either button, and

**Dave Jones:** just drag them around. I had to figure out that you had to do the hand tool up here, you know, I've got to select the tool, and then it's not very responsive. It's a bit jerky. And yes, I can zoom in

**Dave Jones:** and zoom out with the control key like this, and you can then see the There you go. You can see the navigator window and scroll. That's a bit smoother. So, it you know, the functionality's there, but it's pretty

**Dave Jones:** basic. And in the manual, it shows that it has uh timing measurements between uh you know, it'll show you how long this was uh low for, for example, this pulse here, but um it's not popping up with any of that, you know, really cool

**Dave Jones:** stuff, uh, by default or anything like that. You can go in here and you can, um, the menus are a little bit cryptic until you get used to them, but channel assignment is fairly obvious. I can go in there and, uh, type that I've, uh,

**Dave Jones:** changed it to UART and we could have this one as a clock, for example, or something like that. So, we can change that, but I can't drag, just grab them with the mouse and like drag the order of them. I mean, that's just like, you

**Dave Jones:** know, that's like bread and butter 101 stuff for logic analyzer, playing around and setting up your waveforms and and stuff like that, but no. Anyway, it just it feels dated. It feels like it is from the 2000s and they

**Dave Jones:** haven't really updated the interface, but it does look very powerful. I've no idea what single what MSO is. Single DSO channel? What? DC couple? What? Does it actually have an oscilloscope function? No. No. What's going on? So, that's really

**Dave Jones:** quirky. I have no idea what is going on there at all. I can't do What are these lines? I got no idea. Close DSO analog. That is really weird. Look, trigger What? What's OPB? It's just God. It's really quite It's really quite

**Dave Jones:** strange and it's reset when I change that mode. It's reset my waveform. Jeez, it's reset everything, has it? Uh, it it yeah, it's not intuitive. It's not nicely polished. It's just pretty frustrating to use. Like like straight off the bat. I'm sure you'd get

**Dave Jones:** used to it, but but no, the vibe I'm getting is just, uh, it yeah, it's just not great. Not great. Look, I can't even expand that window, can I? No, I can I can delete channels. I can go in there

**Dave Jones:** and sort of delete. I can't Do you wish to delete it? Yeah, just freaking delete it. Don't ask me like I can highlight those and I can delete those to get rid of them. Yeah. Okay, but I don't know. I'm just not feeling it.

**Dave Jones:** And I'm not sure if there's any way to change the color of the waveforms either. Like I know what they're you know, different colors have different assignments on them. They probably match the color coding on the thing, but I I

**Dave Jones:** don't know. Like I just find that red just the red on the black kind of hard to see. So, yeah. Anyway. Now, this signal filter stuff here. This is kind of interesting. If you read the manual, it it basically says filtering is used to

**Dave Jones:** increase the record length by only storing samples when certain unit user-defined signals are high or low. So, you know, it's very powerful, but certainly something that could confuse a first-time user. That's for sure, but hey, you don't have to use it

**Dave Jones:** if you don't want it. But if you accidentally clicked on that, you know, you could be in for a world of hurt. Now, one thing I don't get, okay, is we've got this window down here which doesn't really match up

**Dave Jones:** to the display window at the top. I mean, look, you know, like there it is, right? It's clear. Look, we're we're right on the last pulse there, but we can see all those pulses in there. We're we're in the center like that. It takes

**Dave Jones:** up most of the frame, but up here we've got all this dead space. Like what? Um that's just that that just doesn't even work properly. I don't know what the deal is there. That's just it's hopeless. And then these numbers

**Dave Jones:** along here, like you know, 12,837 what? Like is it microseconds? Milliseconds? Samples? What? Like they're Where's the units? There's nothing there that tells you anything. So, it actually took me ages to figure out how to do this serial

**Dave Jones:** decoding in this software. It's not obvious. If you go up here, like acquisition, no, nothing doing there. Analysis, that is surely. No, nothing doing there. View, no, nothing doing there. Um the MSOs, still don't know what that is. It's an optional product or

**Dave Jones:** something. But, uh look, what we need to do is we need to go in UART here and then channel assignments. It's not this one, but it's like add bus {slash} signal. But, this is not where you add a

**Dave Jones:** bus. We have to actually sign a bus, which okay, we need to group in the bus here. So, bingo. And now we're starting to get there and you can group various signals. So, you we could have like selected all

**Dave Jones:** three of those, like if we had a spy bus, for example, and then we could group those. Um and well, we can yeah, if we did before, we can group those into a bus. So, now let's try and get

**Dave Jones:** this to decode a UART. And only then, if we right-click on the bus, do we get bus properties. Protocol decoders, thanks for telling us that. Um here we go. And this is where it gets impressive, cuz look at all I mean, this is that you can

**Dave Jones:** get the $139 version of this, I I believe, and the software is same. You get all of these. One wire, seven segment, LIN module, AC-97. Like this is just CAN, two, CCIR, compact flash, CMOS image. Wow, is that

**Dave Jones:** like CMOS camera? But, like look at all that. DS1302, um that's the RTC, isn't it? I believe. Um I I don't think it has eMMC. Um I think you have to look up the list, but it supports most of these, I

**Dave Jones:** believe. So, all different I squared um C's, IRDA, IR modules, infrared um decoding, key lock, code hopping stuff. This is absolutely incredible. I believe you get most if not all of these decoders with like the bottom of the

**Dave Jones:** range $130 you know, $140 unit. So, if you're just looking for a serial decoder, this could be the bomb for you know, not much dosh at all. Anyway, we want to go in there and select our UART. Bingo, we're in

**Dave Jones:** like Flynn and it obviously we haven't set that up properly yet. So, we're going to go in there and select our configuration. All right, so let's go in. Everything's right here 9600 eight data bits one stop bit etc.

**Dave Jones:** No parity. The packet Oh, that's nice. We can set up look the color for all that sort of stuff. So, that's jazzy and data format bingo. That's what we want binary decimal hexadecimal. We want ASCII. Beautiful and use UART for free. Yay! Cuz they

**Dave Jones:** released all the decoders for free, which is fantastic. So, this should now decode this hopefully. Oh, come on. It's like it's just quirky that you have to go through that extra menu. Hello world. There we go. Okay, we'll

**Dave Jones:** send that again. Let's capture. It's sitting there triggering. It probably shouldn't delete those waveforms when you trigger. Probably to show you I I don't know. That's a personal preference thing. Anyway, send data. Bingo EEVblog. Nice. And check this out

**Dave Jones:** like there's just no spit and polish at all on these fonts up here. They just look overlaid on the waveform. It's just No. No, it's just clunky. There is one thing I do like though is that when you do select the bus and you

**Dave Jones:** go back out, it's annoying that it does it when you go back out and save it that it actually changes the channel names for you. It puts data S clock and SS um for the select line there, so that's you

**Dave Jones:** know, kind of handy. You don't have to go in and do that manually. Nice touch. It's the only nice touch I've found so far, I think. But I tell you what, it does seem to have everything you need

**Dave Jones:** here. It has all the different modes in the transmission direction and the data length and you can do a virtual select as well after a time period and I think that's pretty much comprehensive for SPI bus reading. sample. And sure

**Dave Jones:** enough, if I do an SPI bus and execute, I'm writing AA as the command. So, you can see that there's two down here. That's the command and I'm writing AA hex. That is correct and I'm writing the next

**Dave Jones:** data as 11 hex. So, that is correct. No problems whatsoever. Yeah, check it out. It just doesn't like format this font properly. Look, it can hang off the end and it can vanish like that and give you that result and it's just

**Dave Jones:** it's there's no spit and polish in the way that data is actually presented. It's not the font size and everything is not scaled properly. That's pretty annoying. I expected better. But if you're going to some of the other

**Dave Jones:** protocol decoders like USB 2.0 for example, look, here's all the stuff that it actually decodes. Fantastic. And yeah, it's free. Use USB 2 for free and we can cancel out of that. Let's choose something else. What have we got here?

**Dave Jones:** Something that's good. Maybe maybe one of people want to muck around with SMBus for example. Once again, it's all free. All these decoders, all included. Fantastic. So again, I have not seen a more comprehensive list of protocols decoders than this one. It's just

**Dave Jones:** absolutely remarkable and I believe you can get this for the 135 buck unit. And check it out. It looks like we can even do like SD card uh decoding and stuff like that for the pack of for the um

**Dave Jones:** for the actual SD card protocol. Like brilliant. What other logic analyzer does all this? None. But of course, right out of the block here, we can drag the cursors across like this and and do stuff like that, but there's no

**Dave Jones:** snapping, you know, to an edge or anything like that, you know, no small spit and polish like that at all. And well, okay, A minus B A is a 751 what samples? I'm presuming. Are you kidding me? Like tell me what that is in

**Dave Jones:** microseconds. Time. I like that I I it's capable of doing it, I'm sure, but I have to select some sort of freaking timing analysis mode or something. It's just uh give me a break. And so frustrating. Like out of the box, you you want to be

**Dave Jones:** able to just, you know, check the frequency of this uh clock, for example. I uh Anyway, we can do uh different views like uh state list, for example. You can get that, so you know, great for you uh

**Dave Jones:** list aficionados. Aha, here we go. Look at this. Uh bugger reading the manual. Um look, we got a time display. Hello. There we go. Look at what it Look at the size of these fonts. They're all over the place. What?

**Dave Jones:** What What is that information measuring? Are you like What are they got 31.825 milliseconds from where to where? Like what? I don't understand what that is. Just a mess. Isn't That makes no sense whatsoever. Wow. Like they've been doing this for so long. And

**Dave Jones:** okay, so that's the sampling the sample number. Frequency display, there we go. 31.323 Hz, but like show like it little arrows on there that it's it's detecting the right frequency. That's just that's nuts. Like that that is I do not understand what the hell

**Dave Jones:** is going on there. That's terrible, Muriel. Really hide time of waveform. Like ah no. No, no, no, no, no. This is how not to do logic analyzer software. Ah, here we go. Only if we like zoom in to this

**Dave Jones:** look, does it actually put 100 microseconds between there and there? That is the ugliest thing I've ever seen. This is like beta software or something. This This is that like maybe you can change the font size or something, but it should

**Dave Jones:** automatically do that. THAT IS TERRIBLE. AH, NO. Like otherwise, ridiculously powerful software just ruined by spitting polish on the user interface. That What a shame. An absolute shame. But yeah, they need somebody who knows how to do a GUI

**Dave Jones:** interface. Please. And it looks like we've got a packet list display as well, so that's okay. And of course the list view. Um but yeah, it does have a find capability. Ah, there there it is. I find. I found

**Dave Jones:** it. Data value. Oh, it disappeared off screen. So you can actually search through and find stuff, so that's handy. Oh, look. I just noticed you can connect multiple Lap C's. Okay. Um RTFM for that one. I guess you can

**Dave Jones:** like all those extra Yeah, they've got various other extra pins on the connector there to allow you to connect multiple ones together to form a large number of channels. Brilliant. And connect a DSO. Well, I didn't see on

**Dave Jones:** their webpage a DSO, so I'm not sure what's going on there. Why you would even enable that? Like the single DSO, you know, double DSO when it knows that there's no DSO connected. Like why even have that as an option? Hmm, I

**Dave Jones:** don't know. Sure enough, you go at acquisition trigger properties, you can actually set up um the level user defined. You can set up like 0.1 volts or something like that. So, they're doing that somehow. It's kind of weird. Anyway, you can set up

**Dave Jones:** the threshold levels based on a port. So, they might have something in there which maybe a DAC in there which drives the voltage pin, the power pin on the level chip. So, I think maybe that's how they might be doing it.

**Dave Jones:** Yeah, based on the various ports. So, anyway, you can actually do it. Now, let's have a look at the software for the F series. This is a multi-thousand-dollar logic analyzer. And yes, it is different software. So, now we can actually look. We can drag

**Dave Jones:** these around. Isn't that neat? Can we even expand them? Can we Yeah, we can Look at that. We can expand it. Exactly what you wanted from the last one. So, it looks a bit jazzy, but once again, they're are just like it is not polished

**Dave Jones:** at all. Look, if I expand this window, I've got three monitors set up here. So, this is actually on my secondary window which I capture on. And if I try to go full screen, it just jumped over to my

**Dave Jones:** like my main desktop screen. It can't even stay like it can't even expand to the full screen. I mean, it's completely out of file and got wanky dials over here. By the way, the minimum sample rate on this puppy is 5 MHz. So, if you want to

**Dave Jones:** go under that, I think you're out of luck. So, this one's actually nicer in that you can right-click over here and add protocol decoder. Okay, that's a bit neater. Um but, let's go up here. We can actually select our trigger, our probe type. Uh

**Dave Jones:** so, we actually This is quite troublesome. Um it hasn't I've got a P200 probe. It doesn't even support the probes they've supplied. What the? So, that is just crazy. I'm not sure what's going on there. I've got the P200 EM probes, and they're just not

**Dave Jones:** in the list at all. Anyway, you can see how down here I have actually done my packet, my UART packet down here and captured it. But, look at all this spurious data either side here. So, I presume that's because the probe is set

**Dave Jones:** up incorrectly. Okay? But, anyway, we have the same thing going on here. I can't even I can hold down control, but it doesn't seem to work all the time. I've had issue with this I swear it did not work

**Dave Jones:** before holding down control and then doing that. But, anyway, so why is A0 and A1 Why are they're Oh. Oh, okay. Maybe A1 is the other connection on Uh okay. No, sorry. A1 might be the other connection on that probe, that

**Dave Jones:** other two-pin header, maybe, that we saw on there. So, something weird is like I I don't know. I don't know. I We can Well, no, I won't I won't delete that. Anyway, here's our serial data. We certainly got it, although not sure what

**Dave Jones:** that spurious thing there is. Check that out. And once again, I can't just grab this, left-click, and pan around. It's just like ridiculously frustrating. Where is the hand thing that we had on the previous version? It's just like

**Dave Jones:** No. Fail. Absolute Ah. So, anyway, we've got spurious data, but that could be could be because of the probe setup. So, anyway, the software is different. You can actually set up protocol decoding. So, um this is a bit nicer interface. I do

**Dave Jones:** like this. It's a wizard. Um fantastic. So, look at all the uh protocols you've got. I mean, I see interfaces. That's just like JTAG. It's got everything. Um unbelievable. Look at the digital audio ones. HDMI. Wow. That's just ah MIDI, MIPI. Crazy.

**Dave Jones:** Um I don't know what the JK logic thing is. Basic logic application? I don't know. Is it some demo thing? I don't you sample application? I don't know. But, compact flash, eMMC, and this is just absolute like a PM bus, um all your

**Dave Jones:** various uh buses, your infrared stuff, your IrDA, NEC, FeRAM protocols, wireless protocols, the key lock logger again. It's just incredible the amount of decoders you get with this. Absolutely stunning. Okay, so when you do that, it actually adds the separate

**Dave Jones:** uh UART bus here, which you can actually Oh, can you expand that? Does it Let you? Yes, it does. There we go. Nice. Um so, this actually works slightly uh differently. It's not the bus decoder properties in here. We're in

**Dave Jones:** hex at the moment. So, we can't actually change it in there, unlike the previous uh software. We've actually got to go into numeric base encoding, and we go to ASCII, and EEV. Oh. Trust me, it will If I can zoom Ah,

**Dave Jones:** I'm holding down control, and now it's going vertical. Like, do I have to actually select the act I have to select the axes. All right. No, I I don't know. Anyway, EEVblog, there it is. Um but look, you

**Dave Jones:** know, once again, it's not formatting the data and like the the text maybe it's a little bit better, but where's this one I wanted to go show you over here, this state list. Look at this, the state list. All the fonts are

**Dave Jones:** chopped off. Like, what? This is like a multi-thousand-dollar logic analyzer and this software is just so unpolished. It It's a real shame. It's a real shame. Really, the main thing this software has going for it is the serial protocol

**Dave Jones:** the free serial protocol decoding because everything else is just so clunky. Anyway, I'm sure it's like ridiculously powerful if you actually went in there and had a look at it with a signal noise filters, math operations, the acquisit Like, I'm I'm sure it will

**Dave Jones:** eventually do the business. Um but just driving this thing is just Ah, no. No, get someone who knows how to do a decent GUI, for goodness' sake. And if we actually go into options over here, then we can find our waveform

**Dave Jones:** and once again, they got the silly frequency, number of samples, time thing. Don't show values. Why can't when you put your cursor over it, automatically like or left click or something or automatically say, you know, a button up here which says like

**Dave Jones:** auto cursor mode or something. It automatically tells you the frequency, the time period between there and all sorts of stuff like that. Anyway, so let's go let's go time and we're in. Hang on.

**Dave Jones:** Ah, that one's a little bit more polished, is it? Slightly more polished. At least it's not overhanging, but once again, no font size scaling. So, yeah, it's it's just really amateur hour. And once again, it looks like we have no ability

**Dave Jones:** to snap cursors or anything like that, like real basic stuff. Aha, I stand corrected on the probes. Sorry, I goofed that up completely. They did actually include in the packet, um, some 120 LV probes, which are in here. Now, here's

**Dave Jones:** an example. Oh, no, there was I thought I had it where it didn't do the protocol decoded. Anyway, the same window thing like in the other software. Look. Look, it's got extra space at the end. It just doesn't

**Dave Jones:** render that uh, preview window correctly. That's just nuts. Anyway, um, I've got the 120 LV probe, which is the low voltage CMOS probe, and it's got two channels. The probe I was using before is actually the eMMC uh, probe. So, that was entirely

**Dave Jones:** different designed for probing an entire eMMC um, signal. So, um, I've now got the regular well, regular low voltage CMOS uh, TTL type. They do have a TTL probe specifically, um, but you have to get the specific type. And this is a

**Dave Jones:** two-channel. So, there's there's a 32 ports on the unit itself, 32 USB ports, and you can get up to 64 channels cuz each probe supports two, depending on what you're probing. So, there you go. I resampled it, and now we don't get any

**Dave Jones:** of the crazy data. So, that's just fine. So, yep, sorry about that. EE Vblog, that's correct. But, what why do you have to put data? Like, why does that word data have to be there? Why? That's just totally redundant. So,

**Dave Jones:** anyway, that's a look at the ZeroPlus logic analyzers, and well, I the high end like the hardware's really good. Um, the software I it's it's almost a fail. It like it's it's going to do the business, but it's just

**Dave Jones:** it's just not polished at all, which is a real shame cuz this probably has the most serial decoders of any logic analyzer that I've used. So, I Yeah. But, anyway, if you can get like this one for what is it the 16 16 or

**Dave Jones:** something for like 130 bucks and get all those serial decoders, that could be very very useful. Very well worth checking out. And you can see that they've got uh protocol analyzers as well. Ooh, what's I squared C SPI

**Dave Jones:** control center? I wonder. Geez, they've got all sorts of stuff. The website's a bit weird, but uh anyway. Hmm. I'll have to do the starter kit in another in software control. I squared C SPI control center. Oh, this

**Dave Jones:** is the Is this this generator? I think it might be the protocol generator, I don't know. Anyway. Huh, weird. They've got all sorts of stuff. Anyway, thank you very much Zero Plus for sending those in. A lot more

**Dave Jones:** work on the software required, uh please. Um just would make the experience a heck of a lot better cuz your hardware seems to be quite reasonable. Anyway, I hope you found that interesting. If you did, please give it a big thumbs up and as

**Dave Jones:** always, comment down below. Catch you next time. Sorry about my voice, by the way. I'm just sick as a dog at the moment. Uh going to go have a lie down on the bean bag. Catch you next time.
