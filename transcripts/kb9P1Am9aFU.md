---
video_id: kb9P1Am9aFU
title: EEVblog #674 - Rigol DS1054Z Teardown
url: https://www.youtube.com/watch?v=kb9P1Am9aFU
source: youtube-asr
timestamps: {"0": 1, "1": 20, "2": 37, "3": 53, "4": 73, "5": 90, "6": 106, "7": 119, "8": 139, "9": 155, "10": 168, "11": 186, "12": 197, "13": 211, "14": 226, "15": 241, "16": 257, "17": 269, "18": 281, "19": 301, "20": 314, "21": 330, "22": 346, "23": 361, "24": 378, "25": 396, "26": 412, "27": 424, "28": 440, "29": 460, "30": 481, "31": 495, "32": 509, "33": 524, "34": 536, "35": 550, "36": 565, "37": 580, "38": 595, "39": 606, "40": 616, "41": 633, "42": 647, "43": 665, "44": 679, "45": 692, "46": 705, "47": 720, "48": 736, "49": 749, "50": 763, "51": 779, "52": 791, "53": 807, "54": 825, "55": 842, "56": 857, "57": 871, "58": 886, "59": 902, "60": 920, "61": 934, "62": 946, "63": 958, "64": 975, "65": 990, "66": 1004, "67": 1018, "68": 1031, "69": 1048, "70": 1062, "71": 1075, "72": 1087, "73": 1102, "74": 1114, "75": 1133, "76": 1149, "77": 1165, "78": 1182, "79": 1196, "80": 1211, "81": 1224, "82": 1238, "83": 1252, "84": 1269, "85": 1284, "86": 1295, "87": 1313, "88": 1326, "89": 1345, "90": 1367, "91": 1384, "92": 1403, "93": 1421, "94": 1437, "95": 1452, "96": 1470, "97": 1490, "98": 1503, "99": 1518, "100": 1531, "101": 1542, "102": 1555, "103": 1573, "104": 1589, "105": 1602, "106": 1613, "107": 1628, "108": 1645, "109": 1661, "110": 1680, "111": 1691, "112": 1704, "113": 1718, "114": 1731, "115": 1749, "116": 1768, "117": 1790, "118": 1805, "119": 1823, "120": 1839, "121": 1855, "122": 1870, "123": 1888, "124": 1906, "125": 1925, "126": 1942, "127": 1959, "128": 1976, "129": 1989, "130": 2005, "131": 2018, "132": 2032, "133": 2044, "134": 2059, "135": 2071, "136": 2087, "137": 2104, "138": 2120, "139": 2139, "140": 2159, "141": 2174, "142": 2184}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. The venerable DS1052E from Rigol. First released in about 2008, so it's around 6 years old or thereabouts. Older than my blog, and I reviewed this in my very first EEVblog number one video, as horrible as that

**Dave Jones:** was. Yes, I reviewed it way back then, and it was the leading low-cost price performance scope back then. Back when I when this was originally released, it was $800 price point. A lot of people don't realize that. They think it's always been around

**Dave Jones:** half that or that $400 price point people have been used to in, you know, the last few years. But anyway, this is really long in the tooth, and Rigol have finally released a basically a complete replacement for it,

**Dave Jones:** and it's got a ton of stuff, a ton of bells and whistles. So, although Rigol still officially sell this and support it, it seems you'd be crazy to buy one because they've released, just recently, the new DS1054Z. So, it's the Z series, and the four is a

**Dave Jones:** giveaway for the four channels instead of two. The fantastic thing about this is its price point is very similar to the 1052E that it's been for quite a long time. It's $399 US. Unbelievable. That price varies depending on the country. It's a bit

**Dave Jones:** more than that here in Australia, but still well under 500 bucks. So, it is the leading price performance scope on the market, it seems. So, although this isn't a review, yes, I'll say a couple of things about it. It's built as good

**Dave Jones:** or better than the 1052E, or so it seems. We haven't taken it apart yet to find out what it's like inside, but it feels like a really solid instrument. It's got four channels. It's got a buttload of memory on it, and it's got

**Dave Jones:** the intensity graded display, not quite as many levels as the DS2000 series, but still for $399, four channel, 50 MHz, so the same bandwidth as the 1052E. There is a 100 MHz model available as well. Four channels, incredible for the

**Dave Jones:** price point. When I was a boy, scopes were always around about I've done a video on this. It's still around about that $800 price point level, you know, 20 MHz dual trace analog crow back then was the entry

**Dave Jones:** level scope and around about the 800 bucks, and that's what this one was released at. This one is now half that. It's crazy for four channels, and it's got a ton of memory in it. It's got the intensity graded display. It's got

**Dave Jones:** optional software serial decoding, all sorts of stuff. It's got segmented memory. Um doesn't have quite uh the the nicer segmented memory controls that the DS2000 has, but still, jeez, it's impossible to beat. The value for money for this thing. Is it any

**Dave Jones:** good? I don't know. Have to do a full review of it. So, if this thing is any good, and I have no reason to doubt that it wouldn't be. Might have a few bugs and things as almost all scopes do these

**Dave Jones:** days with the complexity in the damn things. Anyway, Rigol have been refining the scopes. I mean, even before this one. This was not their first uh digital scope. It started with the I think the 3000 or 5000 series, which was a longer

**Dave Jones:** one like this. Been slowly refining them. Agilent really helped them out there, and well, they're regretting that big time now, cuz Rigol are one of the major players in the market. And well, if this thing is as good as the

**Dave Jones:** specs claim, and if it's built well, then it is impossible to beat in today's market, I think. Four channels, 50 MHz for under 400 bucks with a crap load of memory and and all sorts of functionality, intensity graded display.

**Dave Jones:** Oh, man. I don't know. You youngsters these days, the amount of scope you can get for the money just ridiculous. Couldn't even be dreamed of 5 years ago. And this one is on loan from John South at Emmona Instruments, who

**Dave Jones:** you should know the dealers in Australia. So, thank you very much, John, for loaning me this. It's the only one he's got, I think, in the country at the moment. Yes, I have ordered one and I will be getting my own unit

**Dave Jones:** when they hit the country, but this is a demo unit, so he's going to let us take it apart and review it. Awesome. So, anyway, is it any good? Let's find out. There's only one way to do that. You know what

**Dave Jones:** we say here on the EE Blog, don't turn it on, take it apart. And here it is compared to the DS1052E. It's little smidgen wider, nothing in it. It's exactly the same height and it's looks like it's maybe a little bit

**Dave Jones:** thinner. It doesn't have these protruding bits out the back because this had the feet on the back, so it could sit flat sit flat like that. And this one doesn't need that cuz all the stuff is recessed down in there. But

**Dave Jones:** apart from that, oh, and it's a little bit heavier. Well, it's a it's a reasonable amount heavier. So, you know, it's basically the same form factor as the 1052E, but we've now got four channels and a bigger display. Look

**Dave Jones:** at that. Ah, beautiful. And that there just gives you a good overview of how much bigger that screen is, more usable, got the soft function buttons down here, more of them. We got the four channels instead of the two, but no

**Dave Jones:** external trigger, of course. you have to sacrifice one of your channels here if you want external triggering, but still, you know, you can't complain on such a small form factor. It's brilliant. And yes, if I'm not careful, I will get

**Dave Jones:** carried away into doing a mini review here. Anyway, all the buttons are pushable. It It feels just as good a quality as the 1052E, really. And you know, Rigol do a pretty decent you know, low-end quality feel to them. And

**Dave Jones:** certainly that nice hefty weight just feels like it's nice and solid, so let's take a look inside. Oh, and of course, I forgot to mention LXI LAN as standard for under 400 bucks. Got to be kidding me. And very similar design feet

**Dave Jones:** to the 1052E, which are okay, you know, they could be better. Nice decent rubber feet on the back there, and yeah, it's not too shabby at all. And of course, it's got universal input voltage and frequency as you'd expect, and claims

**Dave Jones:** about 50 watts maximum. What it actually takes, haven't measured it yet. And it turns out the answer to that question is 22 watts or thereabouts with all four channels running at the fastest time base. But if you want to know the

**Dave Jones:** apparent power, well, there we go. 40 about 40 and a half because the corresponding power factor, there it is, is about 0.55. Not that crash hot. But you'll be pleased to know, yes, it does have a real clunking power switch. It draws

**Dave Jones:** nothing when you turn it off. Yay. As for getting this sucker apart, looks like very same as the 1052E. We've got two torques bits there and a couple hidden under the handle down in there. And yes, that is a warranty void if

**Dave Jones:** removed sticker. It's lucky then I'm wearing my warranty void if not removed t-shirt available on the EEVblog store, link down below. One small step for a man, one giant leap for mankind. Yeah. And thankfully the power switch is on

**Dave Jones:** the front, so there's nothing on the top here that you can uh break like you can on the 1052E and like I did on mine, oops. But, tada! We're in and that weight, yep, look at that. Metal everywhere,

**Dave Jones:** beautifully shielded. Love it. And you'll notice that it's only got the pass, fail, and trigger output here. Doesn't have the uh source outputs like the other uh what the higher-end uh 1000Z models do. And no, you cannot get

**Dave Jones:** this uh 1054Z with the logic analyzer or the source options. Not available. Not sure what that one uh is for. I've never seen it. It's got the um uh you know, PCB down in there, so I don't know, maybe they thought of something

**Dave Jones:** else and uh left it off. And you'll notice that on the front panel here, of course, it doesn't have the uh two extra buttons which some of the higher-end models do. It'll have the logic analyzer button and the source button as well.

**Dave Jones:** They are missing on this model because it's not even an option. And look at our lovely RFI gaskets down in there for the USB connector and the Ethernet. Yep, they've done that properly. It really is quite a belt and braces approach to the

**Dave Jones:** whole thing. They've just shielded everything. And there's our big clunking main switch down in there, just uh switching the active, the brown wire there going straight into it. So, yep, thumbs up. And that real clunking power switch is different to the uh slightly

**Dave Jones:** higher-end DS2000 series, which of course has the soft power button on it. So, hey, it must be cheaper to whack in just a manual switch like that. And they've used a proper uh fuse and rated and compliant uh IEC input connector, no

**Dave Jones:** problems whatsoever. Everything's nicely heat shrunk and nice and tidy and and short. So, yeah, no problems whatsoever. And if you can read down in there, we have board version 1.01. So, that's pretty handy. You can actually see what revision hardware

**Dave Jones:** boards you've got by uh just taking the back off. You don't have to take it in the middle, but I believe it shows you that on the info uh display anyway. It's got the that ID inside, and the software

**Dave Jones:** can uh tell you what hardware version you've actually got. And if I take off a whole bunch of screws right around the outside here, once again, Torx.

**Dave Jones:** Come on. You can do it. It's going to come off. And we can't Yeah, we have to disconnect those, but we're in like Flynn. There all that is. First of all, just the main uh power supply and wiring inside this thing. And

**Dave Jones:** as isn't that beautifully neat and tidy. It's exactly the length you need. They cable tied. They've even cable tied down the fan there just to hold it in place, stop it flapping around in the breeze. And down in there, the earthing,

**Dave Jones:** beautiful. Look at that. It's uh probably got shake-proof washers in there, probably. I think I can see it anyway. Properly crimped and uh all bonded directly down to there. And yep, that's professional. But, that's what you'd expect from a quality brand unit,

**Dave Jones:** and it delivers. And in terms of thermal design, we've got a Sunon brand fan here, so it's not a uh it's not a no-namer. And uh huge grill over here. And of course, grills on the side of the

**Dave Jones:** uh power supply here, which we'll take apart in a second. Well, take apart right now. Ta-da. Oh, look at that. No, that's very clean, isn't it? Oh, I like that. Anyway, uh yeah, so, you know, if you weren't happy with the

**Dave Jones:** noise on this thing, you could actually replace it with a silent, uh, well, a a lower noise one. But, uh, anyway, we need to investigate that, but it gets hot. And if that part gets hot, this part gets cold.

**Dave Jones:** Anyway, um, there's a quite a lot of space inside here, actually, which is, uh, good for airflow, but it also kind of just, uh, makes me think, "Well, if you're Well, really super keen, you could, uh, design a new board to go in

**Dave Jones:** there and have like a battery-powered version of it, some sort of aftermarket, uh, kit to do that, perhaps. Perhaps there's a little market for that." Anyway, um, interesting that we have check this out, all of the Chinese characters down there. Sorry, I don't

**Dave Jones:** know my Chinese characters, of course, but for the various, uh, voltage outputs down in there. That's just rather unusual. I know this is made in China, but, uh, well, no, there are Maybe on the other side it's got, uh, trig there.

**Dave Jones:** It's got fans. So, it's got a couple of other Uh, a fan, is it? Hmm, interesting. Why? But, anyway, um, yeah, Chinese characters instead of just, you know, ground and plus 5 volts and all that sort of jazz. And that's version 1.01

**Dave Jones:** for those playing along at home. And as we'll see on the main board as well, this one has another little graphic on there, another bird which we saw in the DS2000 teardown, but this is a different bird. And I I think it was the like the code

**Dave Jones:** name for the project. I can't remember exactly what type of bird it was. I'm not actually sure what type of bird that is. I don't know my birds. Sorry for all you bird people out there. Um, but that's probably the code name for this,

**Dave Jones:** um, 1000, uh, this new 1000 series. Anyway, look, we have some nice, uh, common mode chokes here. They're they're silastic down, uh, very nice. We've got input, uh, protection. We've got all the requisite stuff happening. Look, we've got the high voltage isolation slots

**Dave Jones:** between our bridge rectifier directly on the input there and it all looks very neat and tidy. It really does. Only one issue. And of course they're going for the CapXon caps. Not to be confused with a very similar sounding one which are

**Dave Jones:** actually cheaper yet again. So yeah, they're not the best caps. Let's say that. But hey, you know, it the ventilation and thermals look pretty good on this. Okay. Well, they are 105° C rated one and the I guess the good thing is

**Dave Jones:** there's a lot of companies um like mix and match all their manufacturers of capacitors but not not Rigol in this case. They've stuck with all of their output caps as well, not just the input main filter cap. All the output caps are exactly the

**Dave Jones:** same brand CapXon and exactly the same series. So yeah, at least they've stuck with it and they've specified them which is good rather than just sticking in any brand cap willy-nilly that they can get, you know, this week at the markets or

**Dave Jones:** whatever. So that's the positive side. And we've got our filtering down there. Another high voltage isolation slot down to the mains earth there. Nice little attention to detail. Got our rectifiers input protection and yeah, it's all going on

**Dave Jones:** and there's our the transformer looks like it's quite reasonable quality and the opto-isolators there. No issue at all. Okay, let's have a look at the main board and as I said this is version 1.01 of the hardware and obviously we're

**Dave Jones:** missing the logic analyzer part. Huge BGA here missing. It's most likely an FPGA and the connector for the logic analyzer. So you can forget about modding this to add the logic analyzer functionality. It's just not there. End of story. Although obviously they are

**Dave Jones:** still using the same PCB across all of the 1000 uh series models here. So, yeah, um some of the higher end ones do have the logic analyzer uh capability as an option, but this one, yep, to cut the

**Dave Jones:** cost, they've just haven't installed the chip and haven't installed the memory, and uh that's actually and a couple of local regulators for that, and well, that's about it. But, hey, that shaves cost off, and that's what they've done

**Dave Jones:** here. That's how they can sell this thing for $399 retail. Now, if we have a look at the whole thing, we've obviously got our four analog uh channels under the can, and we'll take a good look at that later. But, uh you'll notice that

**Dave Jones:** the basic layout isn't as complicated as the DS2000, of course. There's quite a few things missing. The DS uh 2000 had uh two main FPGAs here, one dedicated directly for the display processing, and well, that's not on the top side here.

**Dave Jones:** Then, they've got a smaller FPGA here for the acquisition engine. Yeah, so it's much more simplistic, although they're still getting 30,000 waveform updates per second out of this thing. So, yeah, they might have rejigged their uh architecture and how they implement

**Dave Jones:** it a little bit to still get quite really decent performance, especially for the price point. Absolutely incredible. 30 uh maximum of 30,000 waveforms per second for, you know, under 400 bucks with the four channels and everything else. Oh, it's crazy.

**Dave Jones:** Anyway, um they've used the uh ProASIC uh 3 again from Actel. Um but it's looks like a smaller device than what we did before. We've got our applications processor here. We'll take a good look at those, but yeah, it's

**Dave Jones:** much simpler as you'd expect being built down to a lower price point than the uh DS2000. And you'll also notice that our eight that looks like our ADC in there. It's got the four channels with the differential pair going out to each of

**Dave Jones:** those. I'll show you a close-up, but it's much smaller, much different than the huge, uh, rebadged, um um, one we saw in the DS2000. Big difference there. And there it is. It's got a custom Rigol part number on it. And well, no, it's not

**Dave Jones:** going to be a most likely not a custom Rigol, uh, part. It's just a rebadged, uh, part number from a different manufacturer. I think the one in the DS2000 from was from National Semiconductor if I remember rightly. So,

**Dave Jones:** for those who want to go and, uh, reverse engineer that one and, uh, just, uh, you can tell just from the, uh, pin outs you can see where the differential pairs are coming in here. These are our, uh, four analog channels coming in

**Dave Jones:** differential and these are our data output channels and, uh, other stuff going around here. And well, we've just got some decoupling and power. There's not a huge amount to it actually. But yes, it is one ADC across all four

**Dave Jones:** channels. So, yes, when you turn on, uh, all four channels you don't get the full one gig sample per second. It drops down, uh, to 250 meg samples per second. And under that heat sink after I clear away the thermal compound, no surprises.

**Dave Jones:** A Xilinx Spartan 6 and XC6SLX25. And that ProASIC 3 from Actel is an A3P030.

**Dave Jones:** Now, this is really interesting. Up near this ProASIC 3, look what we have here. Hardware version. And then what looks like a whole bunch of, uh, configuration resistors. So, that's really interesting. Look, they've even got equals one equals zero next to it.

**Dave Jones:** Now, I don't think they're just pull-ups for, like, this, uh, JTAG interface or whatever we've got here. Um, that's what likely that is. And SP version as well. That's really interesting. Are they configuring this thing just based on the

**Dave Jones:** position of the hardware jumpers? That'd be really like the difference between the 50 and the 100 MHz version. That'd be interesting. And as far as the applications processor goes, they've completely changed it. If you remember in the DS2000

**Dave Jones:** series, it was a Blackfin DSP processor, but now they've gone with a Freescale processor in this thing. That's a big change. That's rather curious why on these different platforms they choose different processors. That's just making it hard for themselves, but

**Dave Jones:** maybe that's what they have to do to meet the price target on this lower-end model cuz the DS2000 is in the $1000 plus range. This one is sort of, you know, your your $400 to $1000 price range. So,

**Dave Jones:** they've got to shave costs somewhere. So, maybe they've Yeah, they've retooled it to use the Freescale processor. Must be cheaper. So, that's an i.MX 283 applications processor. It's a quite a beast. It's an ARM 9 operating about 450

**Dave Jones:** MHz or capable of that. And it's got all sorts of stuff built in. It's got all the LCD controllers, got Ethernet PHY, and all sorts of jazz built in. So, really quite a powerful thing, but different to that Blackfin DSP. And

**Dave Jones:** under the can for the analog front end, which people are always keen to have a look at, I have no surprises, of course. You always get these four absolutely identical channels between them. And it looks very similar to the one used in

**Dave Jones:** the original 1052E. Now, of course, you would expect this front end to be uh more like the DS1052E than the DS2000 cuz the DS2000 is capable of double the bandwidth of this thing. And that's exactly what we see.

**Dave Jones:** Because if you compare it, here we go with a photo of the DS2000 front end, it's totally different. The DS2000 has dual relays. It's got dual adjustable trimmer caps in there. And yeah, it's just a totally different beast. Whereas if you compare it with a

**Dave Jones:** photo, here we go with the DS1052E, you'll notice that it's very similar. Only got the one relay, only got the one adjustment cap, very similar amount of passive circuitry and stuff like that. There are differences. It is a different

**Dave Jones:** topology by the looks of it, assuming that there's no components on the other side, that they're all on the top, and that's what we've seen in previous designs. So, I expect this one to be no different. Yeah, it it is going to be

**Dave Jones:** slightly different again. But, yeah, it's these are 100 MHz rated front ends, and yes, it is software limited to 50 MHz. So, it's probably going to have that varicap diode in there again to adjust the bandwidth, which would be my guess.

**Dave Jones:** And then when you buy the software license to get the 100 MHz version, bingo, it just toggles that line to the varicap diode and adjust the bandwidth on the front end. And if you have a look down in there, we can see there's one

**Dave Jones:** diode down in there. So, possibly is that it? That's the only one that's marked as a diode there. So, I don't know. And there's certainly less in here than the 1052E. We've got what looks like our driver here, because there we go. It's driving

**Dave Jones:** that pair up there, which then goes out. There's our output going through the bottom of our can there. But, basically, that's the only um like amplifier chip in there. We've got a 4053 mux here, 4000 series CMOS. But, everything else is discrete.

**Dave Jones:** So, they're doing a discrete transistor fit uh front end, of course, like they were doing on the 1052E, but they also use an AD8510 on the 1052E, which doesn't seem to be there. So, it looks like it's a

**Dave Jones:** different topology. So, if we look at the DS1052E schematic here, uh, drawn by A. Helene, thank you very much. He's, uh, reverse-engineered this and, uh, look at, well, what's here and what's missing in this, uh, Z series. I mean, we've got no, I mean,

**Dave Jones:** they use an AD, um, AD8510, uh, high-speed JFET amp on the input here. We haven't got that. There's nothing like that here, uh, down on Here we go. They've got a programmable gain amp. It's an AD, um, 8370,

**Dave Jones:** a digitally programmable gain amp. And then they've got an output, um, driver, the, um, LMH6552. It is totally different. We've got none of that. We've only got one active device in all of this. So, wouldn't surprise me that they got the same, um,

**Dave Jones:** JFET, uh, amp on the, uh, input side here that have something very, uh, similar to that, but looks like they've at least done away with the, uh, input amp and all they got is basically an output driver. There's no programmable

**Dave Jones:** gain amp anymore. And there we go. We have a Texas Instruments part and it's got P27444K A6CP and I'm not having too much, uh, luck decoding that at first try. There's lots of very similar transistors on here. Look, 780 C.

**Dave Jones:** Pardon there. Absolutely everywhere. All over here. And there's a couple of others and, uh, yeah. Go for your life, but, uh, it's basically There's very little in this thing at all. We've got our, uh, relay down the bottom, a solid-state relay, and not

**Dave Jones:** much. It's one of the simplest front ends I've seen on, uh, these Rigol scopes. And also you would have noticed that there's no uh, Rigol re-branded parts inside here. So they're not trying to obfuscate what parts they're actually

**Dave Jones:** using. Yeah, you could pretty much from the photos you could easily reverse engineer this channel if you put the time into it. So the interesting thing is that all these Rigol scopes that seem to have opened all seem to use a different

**Dave Jones:** topology front end. So it's not like they designed one years ago and then just stuck with it. They've you know, they're really opti Seems like they're optimizing it all the time for the to meet the price target. And that's not

**Dave Jones:** surprising at all with the DS2000 all those analog devices parts and those national parts they don't come cheap especially when you got you know, a couple of all of them in your bill of materials and well, you're trying to

**Dave Jones:** save every dollar trying to meet an really aggressive price point and well, they had to redesign for this one hence why we've probably got just one active part. You know, transistors are usually quite cheap. It's just that much

**Dave Jones:** trickier to design and compensate using those. So But save cost and of course the you know, that only cost a cent for the you know, 74,000 series not even that. So they're really optimized down. I like it. And you also would have noted that

**Dave Jones:** there's no local voltage regulation on these individual front ends either. Likely they've got a 2.5 linear regulator over here. So that's likely powering all four channels. So they don't have the extra low noise one like the DS2000 does cuz it's got the 500

**Dave Jones:** microvolt per division race. So it needs a lower noise linear regulator specifically designed for the task and a bunch of other little touches to make it low noise. This one only 1 millivolt per division just like your standard scope.

**Dave Jones:** So they didn't have to do anything special here. Once again saving the cost I wouldn't have expected the 500 microvolts per division capability in this ultra low end one. And I'm just trying to get the rest of it apart and

**Dave Jones:** like I've done all the screws out of here and unfortunately the board doesn't lift up because the B&C's on the front panel are caught in there and there's no accessible nuts on the front. So, I have to take all of the cage out by the looks

**Dave Jones:** of it before I can unscrew those to get the main board out. Oh goodness. And tada, here's our front panel board and you can see the extra switches down in here. They've even populated the LEDs on there for those extra two switches which

**Dave Jones:** aren't which are present on the higher-end model but aren't present down here. So, they've actually cut those out. Look, they've actually cut the buttons out of the membrane there. That's hilarious but they've installed the LED. So, somebody who did the

**Dave Jones:** did the pick and place file for this thing forgot to remove those two LEDs. So, oops. Spending a couple of extra points of ascent. For those curious to know what rotary encoder they're using there, I'm not uh sure of that brand offhand. Anyway, if

**Dave Jones:** anyone wants to look that one up, by all means go for it. And to get that main board out, I've had to take out the unscrew the LCD from here and access the flat flex through this cutout on the

**Dave Jones:** back there. Little bit annoying but uh yeah, I can understand why they've done it. And that is the LCD if that's an identifier for those interested. Huh, well, there you go. That completely changes the equation on the front end.

**Dave Jones:** Look at all the stuff that they've got on the back here. Actually, as it turns out, it doesn't change the equation a huge amount. Um look, if we split it down the middle here, uh we've got some common parts for two channels. We've got

**Dave Jones:** an analog devices part here which turns out to be a digital potentiometer. We've got another um not sure if it's the exact same part number as what's on the top the TI part. Haven't looked at it. We've got a TL072

**Dave Jones:** and another 4053. And there though well, anyway, those three parts there are shared between two channels and then duplicated on the other two channels next to it. So, the only additional active component on here is another one of these beasties.

**Dave Jones:** Everything else is once again all passive and transistor-based stuff all around here. So, it's still not a huge amount. And there we go. We have an Analog Devices AD5207. And as I said, that's a digital potentiometer, Weird. Aha, as for that piece there,

**Dave Jones:** HA595, it's just a 74HC595. Exactly what's used in the previous model. So, really, that that is not another active amplifier. I mean, up here we've got a TL072. I mean, that's not going to be you know, it's going to be used for

**Dave Jones:** offset or something like that. It's not going to be used as any part of the signal chain. So, still we have a complete 100 MHz amplifier front end is discrete transistor-based. And here we go. We have found another one of these

**Dave Jones:** TI parts and it is a quad op-amp. I I that's what I was starting to think that it probably was. And that looks like it is. So, can I I can only presume that's a TLV274 from TI. It's only a like a low-power 3

**Dave Jones:** MHz bandwidth quad op-amp. Aha, and on a second look at the front of the board here on this analog channel, once again, we've got ourselves that TLV274, which I think it is. And what what I thought I was a bit misled before, the

**Dave Jones:** differential output here is not coming from here. I thought it was. I thought those tracks were going under there, but they're not. They're coming from this transistor amp here. So, obviously, it looks like they've got a complete transistor

**Dave Jones:** solution from go to woe here. Very interesting. But then, well, I can really see how they've gotten the price point down on this sucker. And as for the rest of the board here, well, it is pretty bland. We've just got, you know,

**Dave Jones:** more local regulation around here. Nothing fancy at all. We've just got our decoupling under there. Nothing all at all more on the analog channel side of things. And we've just got an extra memory there for our application processor. Is that a that that could be

**Dave Jones:** the flash. Anyway, I can confirm that the flat flex the display there's a flat flex for the display. It, of course, if you flip it over, is there's the termination resistors there connected directly into that Freescale applications processor down in there as

**Dave Jones:** opposed to the separate FPGA display processor that they used in the DS2000. So, once again, completely different architecture. This isn't responsible for the 30,000 waveform updates per second because this is just the display. It's you know, you're not actually displaying

**Dave Jones:** 30,000 waveforms per second on the screen. It's not updating 33 30,000 times per second, but the that's all happening within inside the FPGA capture engine over here. And then it's displaying at a lower rate, of course. And yep, that's our Hynix flash memory

**Dave Jones:** for the Freescale applications processor, as suspected. And what's interesting, this is the main capture FPGA around here. So, they've got no extra memory on the bottom. So, they've only got the one memory chip on the top. If we flip it over like that,

**Dave Jones:** there we go. That's it down there. Well, they've got uh two, one here and one here. And that Cypress part there is a 9-megabit uh SRAM in a 256 uh Kbit * 32 configuration. So, that's uh almost certainly used uh for the

**Dave Jones:** buffer for the variable intensity display to capture all the data and then uh you know, overlay it on top of each other and do the color grading and uh all that sort of jazz. And here's our only uh sample memory chip. It's a beast

**Dave Jones:** though. It's 512 uh megabit DDR2. And of course, that's 512 megabits equates to uh 64 megabytes uh assuming an 8-bit uh sample of course. And you divide that by all four channels obviously have to be stored in there. We've got 16 megabytes

**Dave Jones:** or meg samples per channels. And this thing has uh 12 meg points of memory and an optional 24. So, I'm not sure where you can where they get in the 24 from. And this flat flex over here goes off to

**Dave Jones:** the uh side soft buttons on the left-hand side of the screen. And I find it interesting that they've got a little uh cutout there for a uh card-edge connector which tests in obviously some sort of part of the uh te- test system

**Dave Jones:** for the board, but they don't do the same thing for the other uh keyboard uh the main uh you know, the rotary encoder and all the other keys. They don't uh do the same thing over here. So, that's

**Dave Jones:** interesting. So, that kind of makes me speculate that these keys over here possibly have some sort of uh uh factory testing capability or something like that cuz they're the ones that go off to that card-edge connector which they uh

**Dave Jones:** presumably you know, they plug that in for a reason, some sort of jig or something like that at production. It may be a like a debugging uh thing during the design process, but eh Anyway, so there's something special

**Dave Jones:** about these, I suspect. There's our main crystal oscillator there and our PLL for raising that up. And look, we've got a couple of more of these TLV 274 quad op-amps here. So, they've used those a lot. So, there you have it.

**Dave Jones:** That's a look inside the new DS 1054Z or essentially the DS1000Z series, be it with the extra logic analyzer down here or whatever. It's just got the extra chips populated. And the other thing I didn't mention is the

**Dave Jones:** source outputs. Look, they've got a cutout over here and well, the the board, the source board, I think I've heard mention that there's a separate board or something like that that has the source connections, but I can't find any

**Dave Jones:** connector there that it would go to. So, that's interesting. So, you almost have to wonder is the the S model with the source output a completely different board? I don't know cuz yeah, there is no connection to put a second board

**Dave Jones:** for the source module there. So, that's yeah, that's very curious. And well, I can't fault this sucker at all, really. I mean, it is it is very nicely engineered and built and the soldering quality's excellent and for 395 bucks for all the capability it

**Dave Jones:** offers as well. Yeah, I I couldn't even probably nitpick on this if I tried apart from maybe the caps-on-caps in the in the power supply, but jeez, thumbs up. Anyway, I hope you enjoyed that teardown. As always, if you liked it,

**Dave Jones:** please give it a big thumbs up on YouTube cuz that helps a lot. And if you want to discuss it, EEVblog forum is the place to do it. Link is down below and as always, high-res teardown photos of

**Dave Jones:** all of this I usually do them as I go along. I'll link on evblog.com. That's down below as well. Hope you enjoyed it. Catch you next time.
