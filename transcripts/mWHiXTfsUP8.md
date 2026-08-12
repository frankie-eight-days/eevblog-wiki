---
video_id: mWHiXTfsUP8
title: EEVblog #308 - Agilent 81160A Function Generator Teardown
url: https://www.youtube.com/watch?v=mWHiXTfsUP8
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 31, "3": 55, "4": 66, "5": 84, "6": 94, "7": 103, "8": 118, "9": 131, "10": 146, "11": 160, "12": 184, "13": 217, "14": 232, "15": 253, "16": 268, "17": 292, "18": 305, "19": 321, "20": 334, "21": 358, "22": 376, "23": 389, "24": 402, "25": 426, "26": 446, "27": 457, "28": 468, "29": 482, "30": 493, "31": 511, "32": 523, "33": 538, "34": 551, "35": 578, "36": 599, "37": 618, "38": 632, "39": 644, "40": 668, "41": 685, "42": 701, "43": 714, "44": 730, "45": 745, "46": 760, "47": 782, "48": 805, "49": 822, "50": 836, "51": 846, "52": 863, "53": 882}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Got a real high-end bit of kit for you today. Ho ho, here we go. It's the Agilent 81160A pulse function arbitrary noise generator, or more affectionately known as the P Fang, or maybe just Fang with a silent P.

**Dave Jones:** Who knows? Hmm. Anyway, it's a really nice bit of kit. We're talking about $20,000 worth here. And this one has got an optional 660 megabit pattern generator as well, worth another six grand.

**Dave Jones:** Oh, going to like this one. Oh, yeah. Here it is, the 81160A. It's labeled as a 350/500 MHz pulse function arbitrary generator, but it does noise as well. And give you a quick sweep across the front panel here.

**Dave Jones:** Very, very nice. Look at those gold BNC connectors. Ah, just oohzes high performance. And of course, it's got the obligatory knob. And this particular unit has options 002 and 660.

**Dave Jones:** 002 means it's the two-channel unit, and 660 means it's got the 660 uh megabit per second uh pattern generation option, which I believe is a possibly a firmware uh option, but don't quote me on that.

**Dave Jones:** By the way, this thing is uh designed in Agilent's uh German facility, and they wanted me to check it out. So, thank you guys for uh sending me this one to pull apart.

**Dave Jones:** And yes, we'll uh eventually get around to uh playing with it, but this is just a teardown. And the other options on the rear, 10 MHz uh reference output.

**Dave Jones:** I'm not sure of the specs of that, whether it's oven oven stabilized or anything like that, but you can hook an external 10 MHz reference in. You can come from it like a uh stratum one GPS reference or something like that, rubidium reference if you really wanted to.

**Dave Jones:** And it's got two different modulation inputs. And here we got two USBs and a LAN connection and good old GPIB. Can't forget that, but still got the plug on there.

**Dave Jones:** I don't think anyone's ever used it. And I do like instruments with these rubber boots surrounding them like that. So, you can just take those off and should get access to the screws underneath.

**Dave Jones:** That's really quite neat. I like it. So, we've got a bunch of screws on the back. It looks like possibly this top cover here is just going to lift off if I take these screws off.

**Dave Jones:** Maybe. Anyway, only one way to find out. Well, it's not going to uh budge off. It looks like maybe the nice carry handles carry straps either side are holding it down.

**Dave Jones:** So, looks like we're going to have to take these off possibly. They might have something to do with it. And it feels like it's going to come off. All right, let's lift the hood on 20,000 bucks worth of function gen.

**Dave Jones:** It's going to slide off. Ta-da! Woohoo! And I've got to say my first impressions are wow, you really are getting your money's worth here. The engineering at first glance looks absolutely phenomenal.

**Dave Jones:** Look at this processor board here. All of these DC-to-DC converter modules, tons of them. Lambda power supply and look at this huge heatsink on this clearly like a large BGA device under there and I love the fan mechanism here and the ducting the ducting mechanism.

**Dave Jones:** It's just great. We'll check it all out in more detail, but I think yeah, it's one of these spare no expense engineering designs. Now, let's start by looking at these DC-to-DC converter modules.

**Dave Jones:** Clearly the design team have gone we couldn't be bothered spending our time working on you know a power supply DC-to-DC converter. We'll just use an off-the-shelf module. Clearly decided to put them or use separate modules and they use them quite a few times here.

**Dave Jones:** Let's have a look. 1 2 3 4 of those and this one here is slightly different to all the others above it here. It uses a Coiltronics transformer there that it maybe it's a custom device.

**Dave Jones:** I don't know, but it's got a part number on it. I'll have to look that one up and then it looks like they've duplicated a couple of these. 1 2 3 4 at least five further up under there.

**Dave Jones:** And I was right. They haven't bothered to design their own. They've gone oh, what the hell? We need to spend our engineering time on better things. So we'll just use an off-the-shelf Texas Instruments DC-to-DC converter module and that's what that is.

**Dave Jones:** It's a PTH08T240. I knew it was familiar and I've used these TI brick DC-to-DC converters before and they save a ton of design time. And I've actually got a couple of these similar type of modules and they take all of the guesswork out of designing DC-to-DC converters.

**Dave Jones:** Somebody's already done it for you and you know, when you're designing a complex bit of kit or you're you know, you're trying to meet a deadline or something like that and if money's no object as it probably might be in a $20,000 function generator, you're just going to go, "Oh, what the hell?

**Dave Jones:** I'm not going to take the risk. I'll just use an off-the-shelf DC-to-DC converter module. Thank you very much." And these other little modules here, of course, they have rolled their own, but they've used, you know, top-notch components.

**Dave Jones:** They use Coilcraft, they've used linear technology switches and you can see the input fuse down the bottom there. There it is and they're just really neatly laid out. And here's the other one up here.

**Dave Jones:** Oh, they've actually sprung for China. But otherwise, you know, once again, linear technology stuff. They've spared no expense and these are nice little layouts. There's obviously got room inside the device to actually well, cut and paste all these multiple converters and why they need so many, I'm not 100% sure.

**Dave Jones:** Probably for driving all the core voltages for this massive device under here perhaps. Maybe it uses like, you know, three or four different rails at least. There's another device under here and they probably want to keep them separate as well.

**Dave Jones:** And as for the main supply, once again, they spared no expense. It's a TDK Lambda made in the UK. It's an NV 175 and let's take a look at the specs here.

**Dave Jones:** We've got looks like four channels of 12 volts at 15 amps and one auxiliary 12 volt 1 amp channel. What a beast. And there's the IEC mains input filter.

**Dave Jones:** It would actually be a filter inside that can there and it's all nice and neat and tidy. Nice ground spade connections there and also they've got a little ferrite there on the input leads.

**Dave Jones:** And clearly this blue board is a pros the main processor board and they've gone for a separate embedded processor. There's an AMD uh processor there. I'm not sure what type.

**Dave Jones:** I'm not going to lift the label on. There's an SO-DIMM connector and that's for all the world like it's an off-the-shelf um you know embedded processor board. So I'm not actually sure what it's what it is or what it's running.

**Dave Jones:** I can't find any part numbers on it. That label on the processor there didn't turn up anything but uh yeah, they've just gone bugger it. We'll use an off-the-shelf processor.

**Dave Jones:** Probably makes the software development a lot easier as well. And on the modulation inputs here you can see two high quality Coto reed relays. They'd probably be shielded sort of you know going to a couple of Analog Devices chips.

**Dave Jones:** And from those two modulation inputs we get some Analog Devices AD9283. Nothing much doing there. They're just 8-bit 100 megasample per second ADCs. And here's what might be the key to the whole device.

**Dave Jones:** It's a UMC UMX113 D16 -G and it's an ultra low noise coaxial resonator as in ultra low phase noise. And I'm not sure how much that puppy costs but it is probably the key to the excellent jitter performance Um, uh, know excellent performance of this function generator in general.

**Dave Jones:** And right near that resonator, we've got an AD7738. And that's an eight-channel 24-bit uh, sigma-delta analog-to-digital converter. And either side of our huge uh, presumably a circ or something under this large heatsink, either side of those you can see a little BGA.

**Dave Jones:** And what is it? It's an Analog Devices TX and DAC. In fact, it's an AD9739. And that is a Here we go. It's a 14-bit 2.5 gigasample per second.

**Dave Jones:** That's gigasample RF DAC. And you can also see the serpentine traces coming out of this device here under the heatsink, right next to this one. And so, that's an expensive DAC.

**Dave Jones:** They've obviously got two of those, one for each channel. And that's uh, $50, almost 50 bucks each in thousand of quantity right there. And one thing I really like is this airflow duct here.

**Dave Jones:** They've formed it out of aluminum like this, and it slopes right down there. And what it's designed to do is take the air input from the sides here, from both sides here, suck it under like this, and then through the fans, and then blows it out the bottom through the heatsink, the main processor heatsink like this, and then it blows over all the circuitry and comes out the back of the case through

**Dave Jones:** all that grating there. So, it's just really nice. They've gone to a lot of effort there, and they've integrated that main heatsink there with sort of, you know, with this aluminum plate as well, which would also act as part of the heatsink as well.

**Dave Jones:** It's great. I like it. And I I this thing just uh sort of oozes that German engineering feel, you know, the uh German design division at uh Agilent, they've you know, they really spared no expense of then at this thing.

**Dave Jones:** And uh all of the uh metalwork, too, by the way, they got multiple folded uh metalwork inserts. It's not just the one box with the board just uh stuck in there.

**Dave Jones:** There's multiple layers to this whole thing. It really is uh quite a work of art. And if we take off this top strip here, see you can see all the RFI prongs here to actually connect and get uh better RFI shielding to that plate there.

**Dave Jones:** And but they've got this But check this out. They've got this uh uh metal flap here going over this um flat flex ribbon cable, which looks like it goes to the uh front panel uh keypad or uh something like that.

**Dave Jones:** And here's some of the other circuitry on the front panel. And once again, they've got a TDK Lambda uh backlight uh supply for the uh LCD backlight there. So, you know, spared no expense at all.

**Dave Jones:** And there's an ISB 1521. That's a uh multi-channel USB controller. And they've got a Xilinx XC95288XL CPLD on here. Uh maybe that's the uh display controller. Who knows? And here's something I haven't seen inside a bit of Agilent gear before.

**Dave Jones:** It's a Microchip PIC18LF4455 18-series microcontroller. Go figure. And down in there, they've got a large uh board-to-board interconnect to join the front panel through to the main board. And unfortunately, to get all this duct-in metalwork off, it looks like I'm going to have to actually take the whole thing apart.

**Dave Jones:** and like all the other metal work and and uh you know, to access the screws down in there to get that thing off. So, I don't really want to do that and uh uh they Agilent were a bit hesitant for me to open this thing to begin with.

**Dave Jones:** But, of course, um the German design group should be very proud. This is beautifully engineered. I love it. And uh of course, you can't complain that uh you're not getting your money's worth as far as the engineering goes.

**Dave Jones:** So, you can see the other devices under there on the heat sinks. Really almost impossible to get the camera in there, but uh looks like there's at least three, maybe four of them.

**Dave Jones:** Uh little maybe uh BGA devices with heat sinks stuck onto them. We'll call it uh quits for now. But, anyway, I hope you liked that. That's uh a teardown of a $20,000 function generator and it's engineered as well as I would have expected.

**Dave Jones:** So, that's the Agilent German design group. Awesome work, guys. And uh as always, if you want to discuss it, jump on over to the EEVblog uh forum. And if you like Teardown Tuesday and this video, please give it a big thumbs up.

**Dave Jones:** Catch you next time.
