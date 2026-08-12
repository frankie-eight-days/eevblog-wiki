---
video_id: kb9P1Am9aFU
title: EEVblog #674 - Rigol DS1054Z Teardown
url: https://www.youtube.com/watch?v=kb9P1Am9aFU
source: youtube-asr
timestamps: {"0": 1, "1": 20, "2": 33, "3": 41, "4": 56, "5": 75, "6": 89, "7": 103, "8": 114, "9": 133, "10": 145, "11": 158, "12": 170, "13": 184, "14": 193, "15": 204, "16": 213, "17": 231, "18": 247, "19": 260, "20": 273, "21": 284, "22": 301, "23": 312, "24": 327, "25": 340, "26": 356, "27": 368, "28": 384, "29": 399, "30": 412, "31": 423, "32": 434, "33": 447, "34": 468, "35": 488, "36": 501, "37": 514, "38": 524, "39": 536, "40": 546, "41": 559, "42": 573, "43": 587, "44": 598, "45": 608, "46": 625, "47": 635, "48": 647, "49": 661, "50": 673, "51": 683, "52": 696, "53": 722, "54": 733, "55": 749, "56": 761, "57": 776, "58": 784, "59": 797, "60": 814, "61": 825, "62": 848, "63": 860, "64": 871, "65": 892, "66": 902, "67": 915, "68": 943, "69": 956, "70": 975, "71": 986, "72": 995, "73": 1007, "74": 1023, "75": 1040, "76": 1051, "77": 1070, "78": 1082, "79": 1092, "80": 1107, "81": 1124, "82": 1138, "83": 1156, "84": 1172, "85": 1190, "86": 1199, "87": 1213, "88": 1230, "89": 1250, "90": 1258, "91": 1274, "92": 1290, "93": 1305, "94": 1321, "95": 1332, "96": 1348, "97": 1363, "98": 1382, "99": 1400, "100": 1416, "101": 1429, "102": 1450, "103": 1462, "104": 1486, "105": 1498, "106": 1509, "107": 1521, "108": 1545, "109": 1559, "110": 1571, "111": 1582, "112": 1598, "113": 1609, "114": 1622, "115": 1638, "116": 1651, "117": 1666, "118": 1682, "119": 1691, "120": 1701, "121": 1710, "122": 1720, "123": 1731, "124": 1749, "125": 1762, "126": 1781, "127": 1794, "128": 1809, "129": 1819, "130": 1834, "131": 1845, "132": 1863, "133": 1874, "134": 1888, "135": 1913, "136": 1928, "137": 1939, "138": 1951, "139": 1963, "140": 1985, "141": 1999, "142": 2011, "143": 2021, "144": 2041, "145": 2063, "146": 2077, "147": 2098, "148": 2122, "149": 2141, "150": 2159, "151": 2172, "152": 2179, "153": 2191}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. The venerable DS1052E from Rigol. First released in about 2008, so it's around 6 years old or thereabouts. Older than my blog, and I reviewed this in my very first EEVblog number one video, as horrible as that was.

**Dave Jones:** Yes, I reviewed it way back then, and it was the leading low-cost price performance scope back then. Back when I when this was originally released, it was $800 price point.

**Dave Jones:** A lot of people don't realize that. They think it's always been around half that or that $400 price point people have been used to in, you know, the last few years.

**Dave Jones:** But anyway, this is really long in the tooth, and Rigol have finally released a basically a complete replacement for it, and it's got a ton of stuff, a ton of bells and whistles.

**Dave Jones:** So, although Rigol still officially sell this and support it, it seems you'd be crazy to buy one because they've released, just recently, the new DS1054Z. So, it's the Z series, and the four is a giveaway for the four channels instead of two.

**Dave Jones:** The fantastic thing about this is its price point is very similar to the 1052E that it's been for quite a long time. It's $399 US. Unbelievable. That price varies depending on the country.

**Dave Jones:** It's a bit more than that here in Australia, but still well under 500 bucks. So, it is the leading price performance scope on the market, it seems. So, although this isn't a review, yes, I'll say a couple of things about it.

**Dave Jones:** It's built as good or better than the 1052E, or so it seems. We haven't taken it apart yet to find out what it's like inside, but it feels like a really solid instrument.

**Dave Jones:** It's got four channels. It's got a buttload of memory on it, and it's got the intensity graded display, not quite as many levels as the DS2000 series, but still for $399, four channel, 50 MHz, so the same bandwidth as the 1052E.

**Dave Jones:** There is a 100 MHz model available as well. Four channels, incredible for the price point. When I was a boy, scopes were always around about I've done a video on this.

**Dave Jones:** It's still around about that $800 price point level, you know, 20 MHz dual trace analog crow back then was the entry level scope and around about the 800 bucks, and that's what this one was released at.

**Dave Jones:** This one is now half that. It's crazy for four channels, and it's got a ton of memory in it. It's got the intensity graded display. It's got optional software serial decoding, all sorts of stuff.

**Dave Jones:** It's got segmented memory. Um doesn't have quite uh the the nicer segmented memory controls that the DS2000 has, but still, jeez, it's impossible to beat. The value for money for this thing.

**Dave Jones:** Is it any good? I don't know. Have to do a full review of it. So, if this thing is any good, and I have no reason to doubt that it wouldn't be.

**Dave Jones:** Might have a few bugs and things as almost all scopes do these days with the complexity in the damn things. Anyway, Rigol have been refining the scopes. I mean, even before this one.

**Dave Jones:** This was not their first uh digital scope. It started with the I think the 3000 or 5000 series, which was a longer one like this. Been slowly refining them.

**Dave Jones:** Agilent really helped them out there, and well, they're regretting that big time now, cuz Rigol are one of the major players in the market. And well, if this thing is as good as the specs claim, and if it's built well, then it is impossible to beat in today's market, I think.

**Dave Jones:** Four channels, 50 MHz for under 400 bucks with a crap load of memory and and all sorts of functionality, intensity graded display. Oh, man. I don't know. You youngsters these days, the amount of scope you can get for the money just ridiculous.

**Dave Jones:** Couldn't even be dreamed of 5 years ago. And this one is on loan from John South at Emmona Instruments, who you should know the dealers in Australia. So, thank you very much, John, for loaning me this.

**Dave Jones:** It's the only one he's got, I think, in the country at the moment. Yes, I have ordered one and I will be getting my own unit when they hit the country, but this is a demo unit, so he's going to let us take it apart and review it.

**Dave Jones:** Awesome. So, anyway, is it any good? Let's find out. There's only one way to do that. You know what we say here on the EE Blog, don't turn it on, take it apart.

**Dave Jones:** And here it is compared to the DS1052E. It's little smidgen wider, nothing in it. It's exactly the same height and it's looks like it's maybe a little bit thinner.

**Dave Jones:** It doesn't have these protruding bits out the back because this had the feet on the back, so it could sit flat sit flat like that. And this one doesn't need that cuz all the stuff is recessed down in there.

**Dave Jones:** But apart from that, oh, and it's a little bit heavier. Well, it's a it's a reasonable amount heavier. So, you know, it's basically the same form factor as the 1052E, but we've now got four channels and a bigger display.

**Dave Jones:** Look at that. Ah, beautiful. And that there just gives you a good overview of how much bigger that screen is, more usable, got the soft function buttons down here, more of them.

**Dave Jones:** We got the four channels instead of the two, but no external trigger, of course. you have to sacrifice one of your channels here if you want external triggering, but still, you know, you can't complain on such a small form factor.

**Dave Jones:** It's brilliant. And yes, if I'm not careful, I will get carried away into doing a mini review here. Anyway, all the buttons are pushable. It It feels just as good a quality as the 1052E, really.

**Dave Jones:** And you know, Rigol do a pretty decent you know, low-end quality feel to them. And certainly that nice hefty weight just feels like it's nice and solid, so let's take a look inside.

**Dave Jones:** Oh, and of course, I forgot to mention LXI LAN as standard for under 400 bucks. Got to be kidding me. And very similar design feet to the 1052E, which are okay, you know, they could be better.

**Dave Jones:** Nice decent rubber feet on the back there, and yeah, it's not too shabby at all. And of course, it's got universal input voltage and frequency as you'd expect, and claims about 50 watts maximum.

**Dave Jones:** What it actually takes, haven't measured it yet. And it turns out the answer to that question is 22 watts or thereabouts with all four channels running at the fastest time base.

**Dave Jones:** But if you want to know the apparent power, well, there we go. 40 about 40 and a half because the corresponding power factor, there it is, is about 0.55.

**Dave Jones:** Not that crash hot. But you'll be pleased to know, yes, it does have a real clunking power switch. It draws nothing when you turn it off. Yay. As for getting this sucker apart, looks like very same as the 1052E.

**Dave Jones:** We've got two torques bits there and a couple hidden under the handle down in there. And yes, that is a warranty void if removed sticker. It's lucky then I'm wearing my warranty void if not removed t-shirt available on the EEVblog store, link down below.

**Dave Jones:** One small step for a man, one giant leap for mankind. Yeah. And thankfully the power switch is on the front, so there's nothing on the top here that you can uh break like you can on the 1052E and like I did on mine, oops.

**Dave Jones:** But, tada! We're in and that weight, yep, look at that. Metal everywhere, beautifully shielded. Love it. And you'll notice that it's only got the pass, fail, and trigger output here.

**Dave Jones:** Doesn't have the uh source outputs like the other uh what the higher-end uh 1000Z models do. And no, you cannot get this uh 1054Z with the logic analyzer or the source options.

**Dave Jones:** Not available. Not sure what that one uh is for. I've never seen it. It's got the um uh you know, PCB down in there, so I don't know, maybe they thought of something else and uh left it off.

**Dave Jones:** And you'll notice that on the front panel here, of course, it doesn't have the uh two extra buttons which some of the higher-end models do. It'll have the logic analyzer button and the source button as well.

**Dave Jones:** They are missing on this model because it's not even an option. And look at our lovely RFI gaskets down in there for the USB connector and the Ethernet. Yep, they've done that properly.

**Dave Jones:** It really is quite a belt and braces approach to the whole thing. They've just shielded everything. And there's our big clunking main switch down in there, just uh switching the active, the brown wire there going straight into it.

**Dave Jones:** So, yep, thumbs up. And that real clunking power switch is different to the uh slightly higher-end DS2000 series, which of course has the soft power button on it. So, hey, it must be cheaper to whack in just a manual switch like that.

**Dave Jones:** And they've used a proper uh fuse and rated and compliant uh IEC input connector, no problems whatsoever. Everything's nicely heat shrunk and nice and tidy and and short. So, yeah, no problems whatsoever.

**Dave Jones:** And if you can read down in there, we have board version 1.01. So, that's pretty handy. You can actually see what revision hardware boards you've got by uh just taking the back off.

**Dave Jones:** You don't have to take it in the middle, but I believe it shows you that on the info uh display anyway. It's got the that ID inside, and the software can uh tell you what hardware version you've actually got.

**Dave Jones:** And if I take off a whole bunch of screws right around the outside here, once again, Torx. Come on. You can do it. It's going to come off. And we can't Yeah, we have to disconnect those, but we're in like Flynn.

**Dave Jones:** There all that is. First of all, just the main uh power supply and wiring inside this thing. And as isn't that beautifully neat and tidy. It's exactly the length you need.

**Dave Jones:** They cable tied. They've even cable tied down the fan there just to hold it in place, stop it flapping around in the breeze. And down in there, the earthing, beautiful.

**Dave Jones:** Look at that. It's uh probably got shake-proof washers in there, probably. I think I can see it anyway. Properly crimped and uh all bonded directly down to there. And yep, that's professional.

**Dave Jones:** But, that's what you'd expect from a quality brand unit, and it delivers. And in terms of thermal design, we've got a Sunon brand fan here, so it's not a uh it's not a no-namer.

**Dave Jones:** And uh huge grill over here. And of course, grills on the side of the uh power supply here, which we'll take apart in a second. Well, take apart right now.

**Dave Jones:** Ta-da. Oh, look at that. No, that's very clean, isn't it? Oh, I like that. Anyway, uh yeah, so, you know, if you weren't happy with the noise on this thing, you could actually replace it with a silent, uh, well, a a lower noise one.

**Dave Jones:** But, uh, anyway, we need to investigate that, but it gets hot. And if that part gets hot, this part gets cold. Anyway, um, there's a quite a lot of space inside here, actually, which is, uh, good for airflow, but it also kind of just, uh, makes me think, "Well, if you're Well, really super keen, you could, uh, design a new board to go in there and have like a battery-powered

**Dave Jones:** version of it, some sort of aftermarket, uh, kit to do that, perhaps. Perhaps there's a little market for that." Anyway, um, interesting that we have check this out, all of the Chinese characters down there.

**Dave Jones:** Sorry, I don't know my Chinese characters, of course, but for the various, uh, voltage outputs down in there. That's just rather unusual. I know this is made in China, but, uh, well, no, there are Maybe on the other side it's got, uh, trig there.

**Dave Jones:** It's got fans. So, it's got a couple of other Uh, a fan, is it? Hmm, interesting. Why? But, anyway, um, yeah, Chinese characters instead of just, you know, ground and plus 5 volts and all that sort of jazz.

**Dave Jones:** And that's version 1.01 for those playing along at home. And as we'll see on the main board as well, this one has another little graphic on there, another bird which we saw in the DS2000 teardown, but this is a different bird.

**Dave Jones:** And I I think it was the like the code name for the project. I can't remember exactly what type of bird it was. I'm not actually sure what type of bird that is.

**Dave Jones:** I don't know my birds. Sorry for all you bird people out there. Um, but that's probably the code name for this, um, 1000, uh, this new 1000 series. Anyway, look, we have some nice, uh, common mode chokes here.

**Dave Jones:** They're they're silastic down, uh, very nice. We've got input, uh, protection. We've got all the requisite stuff happening. Look, we've got the high voltage isolation slots between our bridge rectifier directly on the input there and it all looks very neat and tidy.

**Dave Jones:** It really does. Only one issue. And of course they're going for the CapXon caps. Not to be confused with a very similar sounding one which are actually cheaper yet again.

**Dave Jones:** So yeah, they're not the best caps. Let's say that. But hey, you know, it the ventilation and thermals look pretty good on this. Okay. Well, they are 105° C rated one and the I guess the good thing is there's a lot of companies um like mix and match all their manufacturers of capacitors but not not Rigol in this case.

**Dave Jones:** They've stuck with all of their output caps as well, not just the input main filter cap. All the output caps are exactly the same brand CapXon and exactly the same series.

**Dave Jones:** So yeah, at least they've stuck with it and they've specified them which is good rather than just sticking in any brand cap willy-nilly that they can get, you know, this week at the markets or whatever.

**Dave Jones:** So that's the positive side. And we've got our filtering down there. Another high voltage isolation slot down to the mains earth there. Nice little attention to detail. Got our rectifiers input protection and yeah, it's all going on and there's our the transformer looks like it's quite reasonable quality and the opto-isolators there.

**Dave Jones:** No issue at all. Okay, let's have a look at the main board and as I said this is version 1.01 of the hardware and obviously we're missing the logic analyzer part.

**Dave Jones:** Huge BGA here missing. It's most likely an FPGA and the connector for the logic analyzer. So you can forget about modding this to add the logic analyzer functionality. It's just not there.

**Dave Jones:** End of story. Although obviously they are still using the same PCB across all of the 1000 uh series models here. So, yeah, um some of the higher end ones do have the logic analyzer uh capability as an option, but this one, yep, to cut the cost, they've just haven't installed the chip and haven't installed the memory, and uh that's actually and a couple of local regulators for that, and well,

**Dave Jones:** that's about it. But, hey, that shaves cost off, and that's what they've done here. That's how they can sell this thing for $399 retail. Now, if we have a look at the whole thing, we've obviously got our four analog uh channels under the can, and we'll take a good look at that later.

**Dave Jones:** But, uh you'll notice that the basic layout isn't as complicated as the DS2000, of course. There's quite a few things missing. The DS uh 2000 had uh two main FPGAs here, one dedicated directly for the display processing, and well, that's not on the top side here.

**Dave Jones:** Then, they've got a smaller FPGA here for the acquisition engine. Yeah, so it's much more simplistic, although they're still getting 30,000 waveform updates per second out of this thing.

**Dave Jones:** So, yeah, they might have rejigged their uh architecture and how they implement it a little bit to still get quite really decent performance, especially for the price point. Absolutely incredible.

**Dave Jones:** 30 uh maximum of 30,000 waveforms per second for, you know, under 400 bucks with the four channels and everything else. Oh, it's crazy. Anyway, um they've used the uh ProASIC uh 3 again from Actel.

**Dave Jones:** Um but it's looks like a smaller device than what we did before. We've got our applications processor here. We'll take a good look at those, but yeah, it's much simpler as you'd expect being built down to a lower price point than the uh DS2000.

**Dave Jones:** And you'll also notice that our eight that looks like our ADC in there. It's got the four channels with the differential pair going out to each of those. I'll show you a close-up, but it's much smaller, much different than the huge, uh, rebadged, um um, one we saw in the DS2000.

**Dave Jones:** Big difference there. And there it is. It's got a custom Rigol part number on it. And well, no, it's not going to be a most likely not a custom Rigol, uh, part.

**Dave Jones:** It's just a rebadged, uh, part number from a different manufacturer. I think the one in the DS2000 from was from National Semiconductor if I remember rightly. So, for those who want to go and, uh, reverse engineer that one and, uh, just, uh, you can tell just from the, uh, pin outs you can see where the differential pairs are coming in here.

**Dave Jones:** These are our, uh, four analog channels coming in differential and these are our data output channels and, uh, other stuff going around here. And well, we've just got some decoupling and power.

**Dave Jones:** There's not a huge amount to it actually. But yes, it is one ADC across all four channels. So, yes, when you turn on, uh, all four channels you don't get the full one gig sample per second.

**Dave Jones:** It drops down, uh, to 250 meg samples per second. And under that heat sink after I clear away the thermal compound, no surprises. A Xilinx Spartan 6 and XC6SLX25.

**Dave Jones:** And that ProASIC 3 from Actel is an A3P030. Now, this is really interesting. Up near this ProASIC 3, look what we have here. Hardware version. And then what looks like a whole bunch of, uh, configuration resistors.

**Dave Jones:** So, that's really interesting. Look, they've even got equals one equals zero next to it. Now, I don't think they're just pull-ups for, like, this, uh, JTAG interface or whatever we've got here.

**Dave Jones:** Um, that's what likely that is. And SP version as well. That's really interesting. Are they configuring this thing just based on the position of the hardware jumpers? That'd be really like the difference between the 50 and the 100 MHz version.

**Dave Jones:** That'd be interesting. And as far as the applications processor goes, they've completely changed it. If you remember in the DS2000 series, it was a Blackfin DSP processor, but now they've gone with a Freescale processor in this thing.

**Dave Jones:** That's a big change. That's rather curious why on these different platforms they choose different processors. That's just making it hard for themselves, but maybe that's what they have to do to meet the price target on this lower-end model cuz the DS2000 is in the $1000 plus range.

**Dave Jones:** This one is sort of, you know, your your $400 to $1000 price range. So, they've got to shave costs somewhere. So, maybe they've Yeah, they've retooled it to use the Freescale processor.

**Dave Jones:** Must be cheaper. So, that's an i.MX 283 applications processor. It's a quite a beast. It's an ARM 9 operating about 450 MHz or capable of that. And it's got all sorts of stuff built in.

**Dave Jones:** It's got all the LCD controllers, got Ethernet PHY, and all sorts of jazz built in. So, really quite a powerful thing, but different to that Blackfin DSP. And under the can for the analog front end, which people are always keen to have a look at, I have no surprises, of course.

**Dave Jones:** You always get these four absolutely identical channels between them. And it looks very similar to the one used in the original 1052E. Now, of course, you would expect this front end to be uh more like the DS1052E than the DS2000 cuz the DS2000 is capable of double the bandwidth of this thing.

**Dave Jones:** And that's exactly what we see. Because if you compare it, here we go with a photo of the DS2000 front end, it's totally different. The DS2000 has dual relays.

**Dave Jones:** It's got dual adjustable trimmer caps in there. And yeah, it's just a totally different beast. Whereas if you compare it with a photo, here we go with the DS1052E, you'll notice that it's very similar.

**Dave Jones:** Only got the one relay, only got the one adjustment cap, very similar amount of passive circuitry and stuff like that. There are differences. It is a different topology by the looks of it, assuming that there's no components on the other side, that they're all on the top, and that's what we've seen in previous designs.

**Dave Jones:** So, I expect this one to be no different. Yeah, it it is going to be slightly different again. But, yeah, it's these are 100 MHz rated front ends, and yes, it is software limited to 50 MHz.

**Dave Jones:** So, it's probably going to have that varicap diode in there again to adjust the bandwidth, which would be my guess. And then when you buy the software license to get the 100 MHz version, bingo, it just toggles that line to the varicap diode and adjust the bandwidth on the front end.

**Dave Jones:** And if you have a look down in there, we can see there's one diode down in there. So, possibly is that it? That's the only one that's marked as a diode there.

**Dave Jones:** So, I don't know. And there's certainly less in here than the 1052E. We've got what looks like our driver here, because there we go. It's driving that pair up there, which then goes out.

**Dave Jones:** There's our output going through the bottom of our can there. But, basically, that's the only um like amplifier chip in there. We've got a 4053 mux here, 4000 series CMOS.

**Dave Jones:** But, everything else is discrete. So, they're doing a discrete transistor fit uh front end, of course, like they were doing on the 1052E, but they also use an AD8510 on the 1052E, which doesn't seem to be there.

**Dave Jones:** So, it looks like it's a different topology. So, if we look at the DS1052E schematic here, uh, drawn by A. Helene, thank you very much. He's, uh, reverse-engineered this and, uh, look at, well, what's here and what's missing in this, uh, Z series.

**Dave Jones:** I mean, we've got no, I mean, they use an AD, um, AD8510, uh, high-speed JFET amp on the input here. We haven't got that. There's nothing like that here, uh, down on Here we go.

**Dave Jones:** They've got a programmable gain amp. It's an AD, um, 8370, a digitally programmable gain amp. And then they've got an output, um, driver, the, um, LMH6552. It is totally different.

**Dave Jones:** We've got none of that. We've only got one active device in all of this. So, wouldn't surprise me that they got the same, um, JFET, uh, amp on the, uh, input side here that have something very, uh, similar to that, but looks like they've at least done away with the, uh, input amp and all they got is basically an output driver.

**Dave Jones:** There's no programmable gain amp anymore. And there we go. We have a Texas Instruments part and it's got P27444K A6CP and I'm not having too much, uh, luck decoding that at first try.

**Dave Jones:** There's lots of very similar transistors on here. Look, 780 C. Pardon there. Absolutely everywhere. All over here. And there's a couple of others and, uh, yeah. Go for your life, but, uh, it's basically There's very little in this thing at all.

**Dave Jones:** We've got our, uh, relay down the bottom, a solid-state relay, and not much. It's one of the simplest front ends I've seen on, uh, these Rigol scopes. And also you would have noticed that there's no uh, Rigol re-branded parts inside here.

**Dave Jones:** So they're not trying to obfuscate what parts they're actually using. Yeah, you could pretty much from the photos you could easily reverse engineer this channel if you put the time into it.

**Dave Jones:** So the interesting thing is that all these Rigol scopes that seem to have opened all seem to use a different topology front end. So it's not like they designed one years ago and then just stuck with it.

**Dave Jones:** They've you know, they're really opti Seems like they're optimizing it all the time for the to meet the price target. And that's not surprising at all with the DS2000 all those analog devices parts and those national parts they don't come cheap especially when you got you know, a couple of all of them in your bill of materials and well, you're trying to save every dollar trying to meet an

**Dave Jones:** really aggressive price point and well, they had to redesign for this one hence why we've probably got just one active part. You know, transistors are usually quite cheap. It's just that much trickier to design and compensate using those.

**Dave Jones:** So But save cost and of course the you know, that only cost a cent for the you know, 74,000 series not even that. So they're really optimized down. I like it.

**Dave Jones:** And you also would have noted that there's no local voltage regulation on these individual front ends either. Likely they've got a 2.5 linear regulator over here. So that's likely powering all four channels.

**Dave Jones:** So they don't have the extra low noise one like the DS2000 does cuz it's got the 500 microvolt per division race. So it needs a lower noise linear regulator specifically designed for the task and a bunch of other little touches to make it low noise.

**Dave Jones:** This one only 1 millivolt per division just like your standard scope. So they didn't have to do anything special here. Once again saving the cost I wouldn't have expected the 500 microvolts per division capability in this ultra low end one.

**Dave Jones:** And I'm just trying to get the rest of it apart and like I've done all the screws out of here and unfortunately the board doesn't lift up because the B&C's on the front panel are caught in there and there's no accessible nuts on the front.

**Dave Jones:** So, I have to take all of the cage out by the looks of it before I can unscrew those to get the main board out. Oh goodness. And tada, here's our front panel board and you can see the extra switches down in here.

**Dave Jones:** They've even populated the LEDs on there for those extra two switches which aren't which are present on the higher-end model but aren't present down here. So, they've actually cut those out.

**Dave Jones:** Look, they've actually cut the buttons out of the membrane there. That's hilarious but they've installed the LED. So, somebody who did the did the pick and place file for this thing forgot to remove those two LEDs.

**Dave Jones:** So, oops. Spending a couple of extra points of ascent. For those curious to know what rotary encoder they're using there, I'm not uh sure of that brand offhand. Anyway, if anyone wants to look that one up, by all means go for it.

**Dave Jones:** And to get that main board out, I've had to take out the unscrew the LCD from here and access the flat flex through this cutout on the back there.

**Dave Jones:** Little bit annoying but uh yeah, I can understand why they've done it. And that is the LCD if that's an identifier for those interested. Huh, well, there you go.

**Dave Jones:** That completely changes the equation on the front end. Look at all the stuff that they've got on the back here. Actually, as it turns out, it doesn't change the equation a huge amount.

**Dave Jones:** Um look, if we split it down the middle here, uh we've got some common parts for two channels. We've got an analog devices part here which turns out to be a digital potentiometer.

**Dave Jones:** We've got another um not sure if it's the exact same part number as what's on the top the TI part. Haven't looked at it. We've got a TL072 and another 4053.

**Dave Jones:** And there though well, anyway, those three parts there are shared between two channels and then duplicated on the other two channels next to it. So, the only additional active component on here is another one of these beasties.

**Dave Jones:** Everything else is once again all passive and transistor-based stuff all around here. So, it's still not a huge amount. And there we go. We have an Analog Devices AD5207.

**Dave Jones:** And as I said, that's a digital potentiometer, Weird. Aha, as for that piece there, HA595, it's just a 74HC595. Exactly what's used in the previous model. So, really, that that is not another active amplifier.

**Dave Jones:** I mean, up here we've got a TL072. I mean, that's not going to be you know, it's going to be used for offset or something like that. It's not going to be used as any part of the signal chain.

**Dave Jones:** So, still we have a complete 100 MHz amplifier front end is discrete transistor-based. And here we go. We have found another one of these TI parts and it is a quad op-amp.

**Dave Jones:** I I that's what I was starting to think that it probably was. And that looks like it is. So, can I I can only presume that's a TLV274 from TI.

**Dave Jones:** It's only a like a low-power 3 MHz bandwidth quad op-amp. Aha, and on a second look at the front of the board here on this analog channel, once again, we've got ourselves that TLV274, which I think it is.

**Dave Jones:** And what what I thought I was a bit misled before, the differential output here is not coming from here. I thought it was. I thought those tracks were going under there, but they're not.

**Dave Jones:** They're coming from this transistor amp here. So, obviously, it looks like they've got a complete transistor solution from go to woe here. Very interesting. But then, well, I can really see how they've gotten the price point down on this sucker.

**Dave Jones:** And as for the rest of the board here, well, it is pretty bland. We've just got, you know, more local regulation around here. Nothing fancy at all. We've just got our decoupling under there.

**Dave Jones:** Nothing all at all more on the analog channel side of things. And we've just got an extra memory there for our application processor. Is that a that that could be the flash.

**Dave Jones:** Anyway, I can confirm that the flat flex the display there's a flat flex for the display. It, of course, if you flip it over, is there's the termination resistors there connected directly into that Freescale applications processor down in there as opposed to the separate FPGA display processor that they used in the DS2000.

**Dave Jones:** So, once again, completely different architecture. This isn't responsible for the 30,000 waveform updates per second because this is just the display. It's you know, you're not actually displaying 30,000 waveforms per second on the screen.

**Dave Jones:** It's not updating 33 30,000 times per second, but the that's all happening within inside the FPGA capture engine over here. And then it's displaying at a lower rate, of course.

**Dave Jones:** And yep, that's our Hynix flash memory for the Freescale applications processor, as suspected. And what's interesting, this is the main capture FPGA around here. So, they've got no extra memory on the bottom.

**Dave Jones:** So, they've only got the one memory chip on the top. If we flip it over like that, there we go. That's it down there. Well, they've got uh two, one here and one here.

**Dave Jones:** And that Cypress part there is a 9-megabit uh SRAM in a 256 uh Kbit * 32 configuration. So, that's uh almost certainly used uh for the buffer for the variable intensity display to capture all the data and then uh you know, overlay it on top of each other and do the color grading and uh all that sort of jazz.

**Dave Jones:** And here's our only uh sample memory chip. It's a beast though. It's 512 uh megabit DDR2. And of course, that's 512 megabits equates to uh 64 megabytes uh assuming an 8-bit uh sample of course.

**Dave Jones:** And you divide that by all four channels obviously have to be stored in there. We've got 16 megabytes or meg samples per channels. And this thing has uh 12 meg points of memory and an optional 24.

**Dave Jones:** So, I'm not sure where you can where they get in the 24 from. And this flat flex over here goes off to the uh side soft buttons on the left-hand side of the screen.

**Dave Jones:** And I find it interesting that they've got a little uh cutout there for a uh card-edge connector which tests in obviously some sort of part of the uh te- test system for the board, but they don't do the same thing for the other uh keyboard uh the main uh you know, the rotary encoder and all the other keys.

**Dave Jones:** They don't uh do the same thing over here. So, that's interesting. So, that kind of makes me speculate that these keys over here possibly have some sort of uh uh factory testing capability or something like that cuz they're the ones that go off to that card-edge connector which they uh presumably you know, they plug that in for a reason, some sort of jig or something like that at production.

**Dave Jones:** It may be a like a debugging uh thing during the design process, but eh Anyway, so there's something special about these, I suspect. There's our main crystal oscillator there and our PLL for raising that up.

**Dave Jones:** And look, we've got a couple of more of these TLV 274 quad op-amps here. So, they've used those a lot. So, there you have it. That's a look inside the new DS 1054Z or essentially the DS1000Z series, be it with the extra logic analyzer down here or whatever.

**Dave Jones:** It's just got the extra chips populated. And the other thing I didn't mention is the source outputs. Look, they've got a cutout over here and well, the the board, the source board, I think I've heard mention that there's a separate board or something like that that has the source connections, but I can't find any connector there that it would go to.

**Dave Jones:** So, that's interesting. So, you almost have to wonder is the the S model with the source output a completely different board? I don't know cuz yeah, there is no connection to put a second board for the source module there.

**Dave Jones:** So, that's yeah, that's very curious. And well, I can't fault this sucker at all, really. I mean, it is it is very nicely engineered and built and the soldering quality's excellent and for 395 bucks for all the capability it offers as well.

**Dave Jones:** Yeah, I I couldn't even probably nitpick on this if I tried apart from maybe the caps-on-caps in the in the power supply, but jeez, thumbs up. Anyway, I hope you enjoyed that teardown.

**Dave Jones:** As always, if you liked it, please give it a big thumbs up on YouTube cuz that helps a lot. And if you want to discuss it, EEVblog forum is the place to do it.

**Dave Jones:** Link is down below and as always, high-res teardown photos of all of this I usually do them as I go along. I'll link on evblog.com. That's down below as well.

**Dave Jones:** Hope you enjoyed it. Catch you next time.
