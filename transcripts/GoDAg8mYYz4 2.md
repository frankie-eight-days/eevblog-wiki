---
video_id: GoDAg8mYYz4
title: EEVblog #321 - Google Nexus 7 Tablet Teardown
url: https://www.youtube.com/watch?v=GoDAg8mYYz4
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 29, "3": 53, "4": 80, "5": 98, "6": 130, "7": 157, "8": 178, "9": 206, "10": 227, "11": 260, "12": 295, "13": 330, "14": 372, "15": 410, "16": 434, "17": 472, "18": 493, "19": 514, "20": 540, "21": 556, "22": 588, "23": 614, "24": 650, "25": 675, "26": 708, "27": 739, "28": 770, "29": 802, "30": 830, "31": 869, "32": 889, "33": 926, "34": 961, "35": 988, "36": 1011, "37": 1028, "38": 1063, "39": 1080, "40": 1100, "41": 1118, "42": 1136, "43": 1151, "44": 1186, "45": 1200, "46": 1227, "47": 1255, "48": 1288, "49": 1322}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Got the new Google Nexus 7 tablet in all its black glory. What's inside this thing? I'm glad you asked. You know what we say here on the EV blog, don't turn it on, take it apart.

**Dave Jones:** And well, I don't think we're going to get too many Phillips head screws on this sucker, so out it goes. We need our spudger. I think that's probably all we're going to need. Couple of clips on the outside, should just pop off.

**Dave Jones:** Fingers crossed. And yes, I'm using a metal spudger, not a plastic one. Sue me. Just get my spudger in this top side here and you can see and it's just a couple of plastic clips there. Plastic retaining clips and it looks like it's going to pop off a treat.

**Dave Jones:** Hopefully. That's the plan. We're almost in. Almost in, I think. It just needs a little bit more percussive maintenance. Ta-da! I think I heard it. Yeah. Looks good. That's it. Oh, that was supremely easy. Thumbs up to Google. And no surprises, really. The battery takes up a good lot of the room. What is that?

**Dave Jones:** You know, that's a good, you know, 2/3 of the area or something like that. We've got some beefy copper shielding up here to meet EMI compliance and that sort of stuff. We've got another metal can chipset down here. A small board, you know, a relatively small board, which is just L-shaped.

**Dave Jones:** Wraps around there like that. And I suspect that might be it, because based on the thinness of the tablet, which really, you know, isn't much at all, I think all we've got is the battery, the display is going to be directly under that, probably attached to the front panel, and just this one L-shaped board. They're going to have all the circuitry mounted on that. Of course, there'll be a lot of systems um system-on-chip integration in this thing. So, I'd expect, you know, not much in the chipset department at all.

**Dave Jones:** There'll be a couple of, you know, uh wireless uh chipsets external and stuff like that, but there'll be one main application processor and external memory, and you know, not a huge amount more. And on the side of the unit here, you can see tactile dome switches. Four of them are mounted directly on a flat flex uh cable on an angle like like that, which match up. We've got our uh power button here. We've got a volume up and down, and that one's actually labeled reset. But, it looks like

**Dave Jones:** there's a hole there on the case for it, but uh it hasn't been drilled out. And on the other side here, where it does have a small hole, that goes through into there, and I'm not sure what's going on there, whether or not there's another uh tact switch on the bottom side of that PCB down in there.

**Dave Jones:** That's another reset button, perhaps. And on the same side of the case, just below that button, you can see the four external gold contacts there, clearly for either an external um accessory device and or a remote serial interface for remote programming, monitoring, debugging, factory programming the firmware, whatever it is. Um that is uh a hacker's delight.

**Dave Jones:** And you can see how they've got the main PCB here, and they're just using those little uh leaf contacts to go down to a what looks like a separate physical mounted thing uh you know, uh module for those four gold contacts. If you take a look around the board here, you can see these little spring contacts directly on the PCB.

**Dave Jones:** These are for the three antennas they've got on the back of case. You can see the three pairs of mating contacts here. And if we take a look at them, here's the near field antenna, NFC antenna version 2.0. You can see the contacts, you can see the traces down in there. And there's your GPS antenna version 2.0 as well. And if we come over to here, what do we get? We get our Wi-Fi antenna version 3.0. So, there you go. They're integrated into the back of the case.

**Dave Jones:** You can see we've got some more copper. You see we've got more copper shielding on the back of the case over here. So, they've really gone to town there in terms of our shielding. If we try and pry our battery out here, it should, in theory, be just held down with a bit of double-sided tape. And that does look to be the case. I had to use a bit of force down around here. They used a quite a very aggressive double-sided tape there, but it came off really essentially no

**Dave Jones:** problems at all. And that's a huge thumbs up. No planned obsolescence in this thing. You can easily replace that battery. And just, you know, it's even got a connector. You can just pull the thing out, and I'm sure you'll be able to buy third-party batteries for this before you know it. Beautiful. And if we have a look at the battery pack here, it is an Asus lithium polymer battery pack C11ME370T, rated for it's a single cell, of course, rated for 3.7 volts at 4325 mA hours or

**Dave Jones:** 16 watt hours. Beautiful. And clearly down in here on the side there, I can feel it and I can kind of see it down through there. They've got a battery protection PCB, which is absolutely essential for lithium polymer batteries so you don't abuse them. Don't overcharge them. Don't over discharge them. And so, they don't explode, basically. And that will be good quality, professional protection circuitry in this device. Not just some slap-together one hung low chippy. And the EU obviously rate things differently cuz in the EU it's 4170

**Dave Jones:** milliampere hours. Go figure. And down here you'll notice that the micro USB and the 3.5 mm phone jack, they're actually mounted on separate boards. So, in theory, if they wear out, I know the micro USB's rated to, you know, many thousands of cycles, but still if these wear out, in theory, you could probably replace them. And in the speaker department here, they do actually have dual speakers. There we go. Boing. And it looks like to get at these devices under these metal shielding cans here, we're going to have

**Dave Jones:** to take off the stickers and then pry the cans off. Trusty Swiss Army knife under there and we should be able to lift off that can. No problems at all. Ta-da. And this is going to be our GPS chipset. Dead giveaway goes to the GPS antenna terminals here. And there it is. It's a Broadcom BCM 47511.

**Dave Jones:** If we jump on over here to the Broadcom website, BCM 47511. Here it is. It's an integrated monolithic GNSS receiver. So, it supports both GPS and GLONASS as well, which is the Russian counterpart to the GPS. So, obviously they're maybe targeting the Russian market here. And up here it says accurate real-time navigation and improved sensitivity in urban canyon environments. Love the term urban canyon, but give me real canyons any day of the week. Anyway, it claims that, you know, low power consumption, ultra low power tracking mode, and it's

**Dave Jones:** got a built-in LDO as well, which of course reduces your bomb cost. And they make a point of doing that, of course, because, you know, systems integration stuff. You're looking to lower your bill of materials cost in these sort of things. If you're trying to eke out every cent, having an LDO, you know, a voltage regulator in there don't have to provide a local one.

**Dave Jones:** And uh you know, you still probably need the bypass cap there, of course, for the LDO, but still, you know, you're saving a few cents there. Try and get under the other shielded can here. They're really gone to town to ensure that these things pass.

**Dave Jones:** Hey, mate. Ta-da! There we go. It's just a shielded top, and it contains a cage soldered directly soldered onto the PCB. And what we've got here is our Wi-Fi antenna here, so that looks like it's going to this chipset. And this chipset here is for the near field communications antenna. And for the Wi-Fi, we've gotten a Zwave A W N H 665.

**Dave Jones:** And I've had to use my Mantis microscope to get a look at this one. It's very hard to read the brand on there, but I can definitely, if I get it at the right angle, it's an uh InvenSense um MPU-60 50. And here we go. Let's check it out.

**Dave Jones:** It's a six-axis gyro accelerometer MEMS motion tracking chip. Beautiful. And if you go through the marketing spiel, uh the world's first and only six-axis motion tracking device designed for low power, low cost, high performance smartphones, tablets, and wearable sensors. It contains InvenSense's motion fusion and runtime calibration firmware, beautiful. That eliminates cost costly and complex selection qualification and system level integration of discrete devices.

**Dave Jones:** Beautiful. Once again, more system-on- chip stuff. They're really integrating all this stuff together. And it combines a three-axis gyroscope and three-axis accelerometer on the same die together with a digital motion processor as well. So, it's not just your usual, you know, serial output accelerometer analog output MEMS accelerometer what you might be used to. You know, cheapest chips.

**Dave Jones:** This one's got built-in processor as well. Capable of processing complex nine-axis motion fusion algorithms. Sounds complex. And it has an external I squared C bus as well for an external magnetometer. So, this thing claims to have a magnetometer in it. So, that must be an external I squared C device on the board somewhere. It's a QFN footprint as we saw. And it looks quite nice for precision tracking of both fast and slow algorithms. Part feature user programmable gyro full range plus minus 250 up to plus minus 2,000° per second

**Dave Jones:** and a user programmable acceleration range from 2 G to plus minus 16 G. Beautiful. And it works at 3.8 milliamps. Presumably down at 3.3 volts. If you have a look over here, it's got a low power operating modes 10 microamps at 1 hertz up to 140 microamps at 40 hertz. And it contains a 5 microamp idle mode as well.

**Dave Jones:** And it's the I squared C interface up to 400K or a 20 megahertz SPI as well. Excellent. And it's tolerant up to 10,000 Gs of shock, which sounds like a lot. But when you, you know, if you drop this thing onto, you know, a hard, concrete, or steel surface on its edge, and the plastic is coupled directly through to the printed circuit board, which is connected, soldered directly onto the chip, you can, um, in theory, uh, easily exceed that, uh, 10,000 G, uh, shock, uh, rating, and

**Dave Jones:** damage the device. And also contains a built-in, uh, digital out temperature sensor, as well, and a, uh, sync capability supports electronic, um, image stabilization and GPS, so it can, you know, sync and track together with your GPS. Brilliant. And it's smart enough to generate an interrupt, as well, for gesture style type stuff, when you're panning, zoom in, um, you know, a free fall interrupt. Oh, no, it's falling, you know, the device is falling, quick, do something. Like, I don't know what, you know.

**Dave Jones:** Actually, uh, play a a wave file that says, "Catch me, catch me." I don't know. There you go. Um, it's got zero motion detection, as well, attached, uh, tap detection, shake detection. So, um, all these things, um, can interrupt the CPU, and then, you know, so the CPU doesn't have to be continually processing this sort of stuff. It's all done on the processor, on this chip, freeing up the resources from the main processor, uh, which allows it to detect all these, uh, you know, user interactions with the device. Excellent.

**Dave Jones:** Well worth having. Well worth paying, you know, um, you know, 50 cents or a dollar more for, compared to, uh, discrete, um, accelerometers and stuff like that. And for our near field communications, we've got an NXP PN65. And NXP seem to be getting a few design wins for this, uh, chip set. It's also used in the Samsung Galaxy, uh, S3, and, uh, others. So, it's, uh, almost becoming a bit of a, uh, little, uh, de facto standard for, uh, near field communications there. I suspect when we

**Dave Jones:** lift up all this stuff, and even if I did unscrew this board, I'm not sure if I'm going to do it, but uh, I wouldn't expect there to be anything on the bottom side of the board. Why? Cuz you got a fair bit of, you know, area on top of here. This is more than enough square surface area for all of the processing and all the sensing required for one of these tablets. So, no reason to go double-sided load. And it's got a highest brand 072WX2

**Dave Jones:** display. That's the IPS display 1280 by 800. And if we peel off some of this black tape holding down this flat flex cable here going to the display, then we get another metal can there which we can lift the skirt on that and have a look. Looks like we got power supply circuitry. So, nothing terribly surprising or interesting in there for the switch-mode power supply apart from the shielding, of course. You know, full metal can shielding. You don't want your DC-to-DC converter to be spewing out any

**Dave Jones:** garbage. It'd be, you know, high-frequency one at a megahertz or more. It'd be, you know, quite efficient, optimized for the power consumption of this device. So, you know, I'd expect, you know, upwards of like 90% efficiency, something like that. And inside there I spied a Texas Instruments TPS63020.

**Dave Jones:** And yeah, there you go, up to 90% efficiency maximum 3 amp output current 3.3 volts. Um, you know, and 2. amps output at VIN is 2.5. So, that'll be like the lowest point of the lithium ion rechargeable, lithium polymer battery, sorry. So, that'll be the sort of, you know, the top end to the low end of the battery voltage. So, it's anywhere from 3 amps at the maximum battery voltage as, VIN 3.6. And as the battery drops, the maximum output current available is only 2 amps. And of course,

**Dave Jones:** that's a buck boost topology as well because the battery voltage as it drops from say 3.6 volts to 2.5 volts input, you got to maintain that 3.3 volts output. So, the input voltage can be above or below the regulated output voltage. So, you even need a SEPIC converter or you know, a buck boost topology. And here's an efficiency versus output current graph here. And you can see the efficiency from 0 to 100% on the Y axis and the output current from basically nothing up to 4

**Dave Jones:** amps. And they would have chosen this device extremely carefully. Not only based on cost, that may not have even been a major factor. They probably would have wanted maximum efficiency because battery life in a product like this is, you know, can can kill you. It can kill your market. If you're you know, got an hour less battery life than the new iPad or the new other, you know, X brand tablet, then you're going to get killed.

**Dave Jones:** So, it's worth spending, you know, as whatever you need to to get a DC to DC converter to match your requirements. And you want the utmost in efficiency. So, they would have chosen this device based on mostly, you know, most of the decision would have been based on the operating point, the operating current, you know, it would have been around the peak of this curve here, the efficiency curve.

**Dave Jones:** So, they'd be getting, you know, 85 to over 90% efficiency with this thing. And that's how you design these sort of products to meet your target market. And the one on the right here, of course, is the one for the just the main operation.

**Dave Jones:** Power save mode is disabled. But this one on the left, power save mode enabled also when the thing's powered down, Um, it's also got various efficiencies. That's actually a pretty darn good over a quite a uh range of low output currents there. I really like it. So, you can bet your bottom dollar that the uh design engineers would have just poured over these data sheets and they would have, you know, dozens and dozens of different DC-to-DC converters to choose just the right perfect one. You know, they're up to midnight reading

**Dave Jones:** these graphs and the efficiency curves and, you know, trying to pick the best bang for buck chip they can get, trade-off between cost and efficiency over your various operating modes, which they would have known, you know, they would have done tests on this system.

**Dave Jones:** They would have known and when they're trying to design the final board for production, they would have had um current targets and they would have, you know, all these things matter in terms of when the battery voltage drops, you know, when it's above, when the battery voltage is above the output voltage, what's the efficiency?

**Dave Jones:** When it's below, when the input voltage is below the output voltage, what's the efficiency and power down? Oh, and, you know, as some poor design engineer, um, power design engineer at Asus, probably, you know, spent a month pouring over these bloody data sheets.

**Dave Jones:** And if we peel back our main foil here, which was a bit of a pain, but I managed to get it out. We've got our main Nvidia processor and the memory and some more power supply stuff. And down in the power supply section here, Maxim have a design win. It's the MAX77612A.

**Dave Jones:** But somewhat curiously, I couldn't find any info on that one on the Maxim website, but clearly it's some sort of power management controller. And we have a date code on the silkscreen here, 20th week 2012. And the processor's a bit of a beast.

**Dave Jones:** It's an Nvidia who you usually associate with uh just uh graphics cards and graphics uh processors. It's a T30L Tegra. And if you have a look here at the corners, they've actually gunked that down. They've epoxied the corners of the chip down uh to really keep this in place, and they've done that on all four corners. And that's a quad-core ARM Cortex uh processor working up to a maximum of 1.2 GHz. And here we've got our uh SDRAM split into two different devices here. They're an Elpida uh

**Dave Jones:** brand, and that's a DDR3 memory. And it seems like I was a little bit uh off on this single-sided load uh comment here. Clearly they've uh there's extra circuitry on the bottom because we're missing the uh flash memory as well.

**Dave Jones:** There's got to be a couple of flash devices in there, the 8 and the 16 gig. And I think if I look under the board here, I can uh see extra circuitry on the bottom. And we're missing um other stuff like the uh touchscreen uh controllers as well. Really, um I'm running out of time, and uh really I don't want to tear down this any further. I want to put it back together, rush home, let the wife play with it um hopefully if I haven't killed it. And uh

**Dave Jones:** so I won't take the board off. As you can see, it's a rather interesting uh construction they've got, you know, a um uh chassis in there to keep the uh battery in place. They've got the L-shaped board. They haven't really wasted a lot of space in this thing. Uh they've tried to keep it as uh thin as possible. I'm not sure uh what's going on with this over here, but yeah, it's um quite it's a very well built. They they certainly haven't uh cut uh any

**Dave Jones:** costs at all, and they've really knocked uh the EMC on the head. They've done a really good job there, and the all the uh antennas integrated in the top of the case. I didn't find an RFID chip in there, by the way. Uh haven't uh maybe, you know, I don't think there is one. Anyway, it's all been a rather interesting teardown, and I hope you liked it. And if you want to discuss it, uh jump on over to the EEVblog forum. The link's right there.

**Dave Jones:** And remember, if you like Teardown Tuesday, please give it a big thumbs up. Catch you next time.

**Dave Jones:** You little ripper. Not a problem.
