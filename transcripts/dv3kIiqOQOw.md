---
video_id: dv3kIiqOQOw
title: EEVblog 1693 - Uni-T UTE310 Power Meter Teardown & Practical Demo
url: https://www.youtube.com/watch?v=dv3kIiqOQOw
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 23, "3": 33, "4": 47, "5": 56, "6": 74, "7": 82, "8": 100, "9": 108, "10": 125, "11": 136, "12": 151, "13": 162, "14": 176, "15": 184, "16": 191, "17": 205, "18": 220, "19": 237, "20": 250, "21": 273, "22": 291, "23": 301, "24": 312, "25": 328, "26": 351, "27": 366, "28": 382, "29": 397, "30": 410, "31": 420, "32": 430, "33": 439, "34": 448, "35": 463, "36": 475, "37": 485, "38": 496, "39": 511, "40": 522, "41": 533, "42": 550, "43": 563, "44": 576, "45": 585, "46": 596, "47": 606, "48": 625, "49": 638, "50": 647, "51": 659, "52": 673, "53": 682, "54": 693, "55": 704, "56": 719, "57": 734, "58": 746, "59": 769, "60": 783, "61": 797, "62": 808, "63": 822, "64": 832, "65": 843, "66": 854, "67": 866, "68": 878, "69": 889, "70": 904, "71": 919, "72": 932, "73": 948, "74": 959, "75": 972, "76": 983, "77": 994, "78": 1005, "79": 1017, "80": 1029, "81": 1040, "82": 1056, "83": 1063, "84": 1077, "85": 1090, "86": 1102, "87": 1119, "88": 1133, "89": 1143, "90": 1153, "91": 1163, "92": 1175, "93": 1188, "94": 1196, "95": 1206, "96": 1222, "97": 1239, "98": 1255, "99": 1266, "100": 1286, "101": 1301, "102": 1321, "103": 1333, "104": 1341, "105": 1361, "106": 1383, "107": 1393, "108": 1419, "109": 1430, "110": 1444, "111": 1459, "112": 1472, "113": 1484, "114": 1500, "115": 1515, "116": 1531, "117": 1543, "118": 1554, "119": 1565, "120": 1577, "121": 1586, "122": 1596, "123": 1611, "124": 1623, "125": 1633, "126": 1660, "127": 1680, "128": 1690, "129": 1700, "130": 1714, "131": 1726, "132": 1742, "133": 1759, "134": 1770, "135": 1785, "136": 1796, "137": 1810, "138": 1820, "139": 1832, "140": 1848, "141": 1857, "142": 1864, "143": 1873, "144": 1883, "145": 1896, "146": 1907, "147": 1919, "148": 1927, "149": 1938, "150": 1948, "151": 1962, "152": 1970, "153": 1980, "154": 1998, "155": 2006, "156": 2018, "157": 2029, "158": 2043, "159": 2053, "160": 2069, "161": 2075, "162": 2085, "163": 2100, "164": 2112, "165": 2126, "166": 2139, "167": 2152, "168": 2167, "169": 2181, "170": 2199, "171": 2218, "172": 2233, "173": 2243, "174": 2252, "175": 2264, "176": 2273, "177": 2286, "178": 2297, "179": 2311, "180": 2323, "181": 2336, "182": 2349, "183": 2363, "184": 2376, "185": 2389, "186": 2402, "187": 2416, "188": 2433, "189": 2445, "190": 2463, "191": 2482, "192": 2490, "193": 2502, "194": 2514}
---

**Dave Jones:** Hi, today we've got an interesting teardown of the Uni-T UT210 digital power meter. And this is not a bit of kit every lab is going to have, but if you're looking at doing product power measurements, then a digital power meter can be really handy.

**Dave Jones:** Yes, you can do it with your, you know, a couple of multimeters. Of course, you've got to have at least two multimeters in your lab, one for measuring voltage, one for measuring current, and then you can calculate the power, etc.

**Dave Jones:** But, to get a measurement of energy over the time, you've got to like accumulate. You've got to like integrate that. And you can can do all sorts of other energy measurements as well.

**Dave Jones:** And uh I'll link it in if you haven't seen it, but a long, long time ago in a blog far, far away, I did a teardown of the Voltech PM 300, which I've been using up until now.

**Dave Jones:** But, it's a really old design, but still a very interesting teardown. And that was quite crude, and you've seen that in a lot of videos where I like might measure sort of like mains power consumption or something like that.

**Dave Jones:** Um but, this thing can do a lot more than that. Um it's 600 V 20 A capable, so yes, I can easily do uh like, you know, energy measurements of mains power equipment, but it also has low current ranges down to like 5 mA maximum current range.

**Dave Jones:** So, can do really do low power stuff. And I might give you a demo of that at the end of this after we do the teardown. But, thank you very much, Uni-T, for sending this in.

**Dave Jones:** It's a real interesting and very incredibly useful bit of kit. And it's about 1,600 uh Yankee bucks or something like that. Anyway, um prices could vary depending on where you are, but that's actually a bargain for a a comprehensive digital power meter like this.

**Dave Jones:** And you can see on the back here, we've got the big current terminals cuz this thing can do 20 A, so we've got massive terminals. And then you got the voltage sense terminals.

**Dave Jones:** We've got IO as well, so you can automate it into production testing. We've got RS232 and GPIB. We've got the ethernet, and we've got the USBs, and the whatnots, and it looks like we've got um an external uh triggery thing here, too.

**Dave Jones:** So, you know what we say here on the EV blog, don't turn it on, take it apart. So, as I mentioned, this can do uh integral uh energy measurement, but you can also do THD analysis, and uh all sorts of weird and wonderful things.

**Dave Jones:** I don't know if I had to take off the rubber baby buggy bumpers there. No, probably not. Uh And it's got a sampling rate of 1 MHz, which is really quick for this sort of uh you know, uh high resolution, high accuracy thing.

**Dave Jones:** Um hence why it's, you know, it's Some people might think it's it's reasonably expensive, but uh not for the capability that you actually get in this thing. Ooh, is that going to slide off?

**Dave Jones:** So, if you want to know the power consumption, the battery life of your new uh product, then something like this is I the tool you're going to use to measure that, rather than just guessing.

**Dave Jones:** And of course, uh you know, if your product changes into different modes and stuff like that, then uh yeah, this thing is going to help you uh do that, you know, analyze that.

**Dave Jones:** And you can uh get waveform uh measurements, as well. But, I haven't used the software on this thing, so I'm not sure what we can get out. But, look at that.

**Dave Jones:** That's a Bobby Dazzler. That's clean as a whistle. That's beautiful. Look at this one main one large main board directly in the center of like it's literally in the center like this.

**Dave Jones:** What's on the bottom? Oh, look at that. So, there's actually quite a lot of space inside this thing. Wow, look at that. Um unfortunately, some of the cans are soldered down, so um yeah, but interestingly, look at that up there.

**Dave Jones:** These are our input connections, which go directly over a giant cutout here. They're really serious about the layout of this thing. Wow, this is really something else. Well, brutal is probably the word I'd use to describe that input diode clamping up in there.

**Dave Jones:** This is the two current terminals here and the two back-to-back diodes. Look at those beasts. No fusing rubbish in there, so you're guaranteed not to get more than half a volt burden voltage across your current shunt resistor there.

**Dave Jones:** And they're of course coupled directly into these two relays here. This is basically your current switching, you know, when you're in the saw on the front panel, you tell it to, you know, switch on the load or whatever, clunk, the relays switch on and yeah, you're connecting those rear terminals through to no doubt the current shunt resistors under here.

**Dave Jones:** And they're going to be pretty schmick. And the voltage sense terminals on there, they go into these wires directly over to here and and they run across here after nice big ferrite clamp on there into this shielded um voltage amplifier here.

**Dave Jones:** So, this would be your multi-gain ADC and like an input amplifier as well. And that would be doing all your voltage ranging, but unfortunately we can't see that unless we desolder the thing.

**Dave Jones:** Oh, I didn't want to have to do that. And they've got isolation slots just everywhere. Look at this, right? I don't know why they've actually put that giant isolation slot in there.

**Dave Jones:** I because really, this is all really low impedance um stuff. You don't have to worry about any you know, leakage, creepage, anything like that. But you can see all this custom metal work here is just very impressive way to get to shunt.

**Dave Jones:** I'm here all week to carry the current from the relays over to the input resistors over here. And I've got a little board there. That's interesting. That's just like a four That's just like a vertical connection board, um which actually connects to whatever's um under that heat sink.

**Dave Jones:** So, you have your uh current sense amplifiers or shunt amplifiers are under here. And you can see right up there, there's a missing chippy. That'd be your uh GPIB there, and then you've got your pins for your uh right angle GPIB connector, which would poke out the back.

**Dave Jones:** But, we've got the RS232 option in this jobby. Um and yeah, that just goes straight into that little header there. And then we've got a whole bunch of digital isolation from basically uh the measurement um half of this thing over to the uh processing half of this thing.

**Dave Jones:** Arctic-7 uh FPGA there for those playing along at home. And uh nice isolation slots in here. Beautiful. They haven't put the um isolation uh capacitor across there. They um Yeah, it's part of the design, but they went "Nope, we don't need that." for whatever reason.

**Dave Jones:** I don't know. More isolation happening up here with your little uh switching converter. There's an isolation slot under there. They've got another one under here. And up Yeah, somebody's really had fun with this board.

**Dave Jones:** They really know what they're doing. It's very very nice. And power supply-wise, you don't need much uh to power a board like this because, well, there's nothing really happening here.

**Dave Jones:** It's just, you know, measurement of a 1 MHz high-resolution ADC and um some, you know, high-precision shunts and switching and gain switching and stuff like that. And that's And Bob's your uncle.

**Dave Jones:** Um so, yeah, we only need, I don't know, you know, 5 10 W uh coming in here. It's not uh much of a uh power supply at all. That'll just be um some third-party one.

**Dave Jones:** We could have a look at that if you're really interested. But, just measuring the power supply current there, it's about 580 600 milliamps, something like that at whatever voltage is coming out.

**Dave Jones:** 12 V. That's what I thought. So, my initial guess was about right. Yeah, that's like a 7 W power supply. Like, it's really low. Uh one big uh just digital IO going over to all the main front panel uh processing, which handles all the graphics and everything else.

**Dave Jones:** That'll have, you know, be running the Linuxes, the penguins, or whatever under there, I'm sure. But, yeah, the Artix-7 FPGA that'll be handling the 1 meg high-speed ADC and stuff.

**Dave Jones:** Oh, we've got an arm processor down there. Oh, and a Winbond jobbie. There's a memory. It's tied into the Artix-7 with a big bus. So, yeah. Actually, this is really quite interesting.

**Dave Jones:** We've got one arm processor here. It's an STM something. read that on the screen. But, it's an ST jobbie. And the one and the Artix-7 FPGA over here, as I said.

**Dave Jones:** But, also we almost practically duplicating that over here. We've got another processor. It looks identical. And another Winbond memory over here. We don't have another Artix-7 by the looks of it.

**Dave Jones:** I'd have to get that board out there. But, yeah, basically, we've got dual processor action happening here. The designers obviously Maybe they decided to offload uh voltage and current processing separately.

**Dave Jones:** Or maybe voltage and current in one and then like a dedicated real-time energy measurement in another one, perhaps. And that rear panel board there's just dedicated to your IO, that custom IO connector.

**Dave Jones:** We've just got a little isolated DC-to-DC converter to power that. And this is an ADP5052. And that's just a five-channel switching converter. You can tell it's a switching converter cuz hey, here's your DC input here.

**Dave Jones:** And we need to generate the various rails for the FPGAs and everything else. And yeah, we've got some little inductors around there. And some output caps. So, you can tell that's a little low-power switching reg there.

**Dave Jones:** But, you can see from the traces here that the isolated digital signals, these would be digital, coming out of here and going over to your Artix-7 FPGA, which doesn't have any analog capability.

**Dave Jones:** So, yeah, these are digital um isolated digital signals coming over. So, I'd be guessing these two here for your voltage measurement. Yes, cuz that's tied Here's your voltage input here.

**Dave Jones:** So, this would be your um high resolution ADC uh for your voltage input. And that's powered from this switching converter. And of course, you'd have a low noise uh linear regulator on the output of that as well.

**Dave Jones:** Cuz we're dealing with very low signal levels here. And this one here would be for your uh current ADC. So, yeah, we're going to find our voltage ADC under there and our current ADC under there somewhere.

**Dave Jones:** So, my guess would be that they're doing uh like real-time integration inside the uh Artix-7 there. So, that's you know, it's all hardware accelerated uh stuff. And then the ARM processor would be uh doing some auxiliary uh stuff like energy accumulation over time or uh you know, something like that.

**Dave Jones:** Um, but that that second ARM up there Oh, the second ARM up there could actually be um for like handling like IO and stuff like that. So, this could be a measurement uh processor.

**Dave Jones:** And this other one, which is identical ARM processor up there, could be used to handle um IO and um other stuff. And you know, serial comms and things like that.

**Dave Jones:** And then no doubt, your main processor uh up here is driving your user interface, your operating system, and uh you know, your screen and everything else. So, the giant cutout on the uh current input here um well, this is a 600-V capable unit.

**Dave Jones:** So, we're going to get some uh voltage isolation. And you can see how the You can see that the ground plane and that there's a huge gap in there between your current measurement here and your voltage measurement over here.

**Dave Jones:** And they've got two separate isolated uh paths here getting the data out for the voltage, getting the data out uh for the current. And then they're isol- then they're really isolating.

**Dave Jones:** You can see the isolation in the PCB there from um all the other uh processing side of it. Now, I got the heat sink off. Uh unfortunately, I can't see under there.

**Dave Jones:** The shunt resistor is soldered into these tabs and also soldered into that vertical PCB on the bottom and then clamped on with that. So, wow. They've really gone to town with that.

**Dave Jones:** That is just nuts. But anyway, we can measure it in circuit. Let's get 100 micro-ohms resolution here. Let's null out our leads. There you go. And it's not going to be absolutely precise.

**Dave Jones:** But There you go. I'd probably guess that that is actually a bang on to 10 milliohms. So, yeah, it's getting down there. The longer I leave it there and the more force I put on it, yeah, I think she's going to be a precision 10 milliohms shunt resistor.

**Dave Jones:** That's what I'd expect and it probably costs a fortune with bugger all tempco, of course. And of course, it's all about the tempco or temperature coefficient of the shunt resistor in here.

**Dave Jones:** You can have like a 10% accurate shunt resistor in here. It doesn't matter as long as its tempco is borderline zero, right? If you've got no like zero tempco, it doesn't matter what the accuracy of your shunt resistor is as long as it doesn't change with temperature or anything else like you know, a mechanical stress or anything else, then you can actually calibrate that out.

**Dave Jones:** You can calibrate that accuracy out in software. But when you're designing something like this, there are specialized manufacturers of resistors that will actually sell you a precise you know, 0.01% 10 milliohm resistor.

**Dave Jones:** And that four-terminal board there with the two inner ones pins are the tap going off from that precision resistor. So, yeah, I reckon they've got a real expensive jobbie in there.

**Dave Jones:** That's you know, probably like What's I don't know. I'd have to put this put up the spec of this thing. It's probably like half an order of magnitude or even an order of magnitude if you can get it more accurate than the best spec for this thing.

**Dave Jones:** So, all this mechanical complexity with the custom high current brackets here soldered directly onto the high current relay pins here and the vertical riser board for the current shunt resistor.

**Dave Jones:** That's all designed so that you can get the absolute best accuracy out of that precision shunt resistor. Yep, that's kind of like the effort you have to go to when you got this class of instrument.

**Dave Jones:** Anyway, the mains input here is pretty groovy. It's going down to the chassis down there. I think there's a shake-proof washer on there. It's all insulated nicely and and it looks like there might be a small filter inside that.

**Dave Jones:** Not sure. And I'll just power this on so that you can see the current mode up here, 5 milliamps. And I'm curious to know which Oh, it's got all these different current ranges.

**Dave Jones:** Of course, you can't do everything with your 10 milliohm resistor. Get your Ohm's law out and your confuser and figure out well, 5 milliamps across 10 milliohms. It ain't much voltage to read.

**Dave Jones:** Just saying. For those who couldn't be bothered getting your confuser out, that's 50 microvolts full scale. Full scale. So, if you got to read the resolution down in that, we're not going to be using 10 milliohm resistor.

**Dave Jones:** So, obviously, they must be switching other resistors. But anyway, let's listen for the big relay. We should be able to hear the big clunk. Clunk. There it is. Clunk.

**Dave Jones:** Clunk. So, 500 milliamps. Do we get another clunk? No. So, from 500 milliamps up to 20 amps, they're using that 10 milliohm shunt resistor. And for the other ranges, they're probably using like an ohm or something.

**Dave Jones:** I'm sure that LED there was flashing before. I thought I saw three flashy flashy LEDs. Anyway, there's three LEDs doing something. This is interesting. Just noticed that LED there flashed every time I was in the current menu and pushed that button.

**Dave Jones:** There it is. Beep. beep, beep, beep, beep, beep, beep. And when I change the voltage as well. Yeah, but it doesn't do it for other buttons. So, it's not like a button press.

**Dave Jones:** If I do the sideways buttons, it doesn't do anything. So, it's only when changing the voltage and current ranges up and down. So, yeah, my guess would be that that processor there is doing the real-time voltage and current measurements, but that's no surprise considering that the ASIC would be doing that and that processor there's handling.

**Dave Jones:** And this processor over here is, like I said, doing something else. And as for the sizing of this large heat sink for that 10 mli current shunt resistor there, at the maximum 20 amps here, we're only talking 4 W.

**Dave Jones:** But as you can see, there was supposed to be a fan in here, but they decided, "Nah, we don't need a fan. We'll just go with a really quite large." I mean, that's a really large heat sink for 4 4 W maximum power dissipation.

**Dave Jones:** But as I said, tempco is everything. So, you want to actually keep the temperature of that resistor down. You don't Yeah, okay, your resistor might be able to dissipate 4 W, but you don't want it to go from room temperature to 100° C at 4 W.

**Dave Jones:** So, just be aware of that with resistor ratings. Sure, okay, you've got your you've put your 1 W resistor in the circuit. It can dissipate 1 W, no worries.

**Dave Jones:** Yeah, but have a look at what temperature it's going to get to at 1 W. And when you got a critical precision current shunt resistor, yeah, you want to keep that thing as as cool as possible.

**Dave Jones:** I'll see if I can get the metal cans off without breaking anything. Um metal cans top and bottom. And here is under the two metal cans. There's nothing on the back side, just some miscellaneous stuff.

**Dave Jones:** We just got some diodes here on the That's on the current one and on the It looks like just Is that a regulator there? I'm not sure what that is, but anyway, yeah, there's not much doing.

**Dave Jones:** There's a whole bunch of unpopulated caps there on the bottom side of the voltage one, but anyway, let's have a look here. Now, I was wrong. I assumed that the ADC was going to be under these cans here.

**Dave Jones:** It ain't. It's just sitting out here. So, I zoom in and have a look. It's a linear technology jobby. Of course, it is. It's the 23 238016. And if we go to the video tape, and here it is, the LTC2380-16.

**Dave Jones:** It's a 16-bit 2 meg sample per second. The rating for this thing is 1 meg sample per second. So, I don't know why they're not pushing it to two.

**Dave Jones:** They can. Uh they're not multiplexing anything here cuz they've got separate ADCs for voltage and current. So, anyway, it's a successive approximation register or SAR converter, which is none of that flash conversion rubbish.

**Dave Jones:** So, good old school successive approximation converter. It looks pretty schmick. So, yeah, 16-bit jobby. And you know, look look at this. Low power battery operated instrumentation ATIs. That's exactly what we needed for.

**Dave Jones:** Ha, what a coinkidink. The given the signal-to-noise ratio on the THD, and you can go wild in the comments down below. But yeah, that's pretty schmick. So, they've got that outside of the metal can.

**Dave Jones:** Why? Because the metal can is the differential amplifiers in there, and it's really the low noise part of it. And once you amplify that signal up, then and of course drive it to the ADC, it's a low impedance path coming out of the can into the ADC like that.

**Dave Jones:** And once you've got a a relatively like line level voltage as it's called, and a low impedance path drive source impedance, then yeah, any interference is not going to matter in this part.

**Dave Jones:** So, it doesn't really need to be under the can. All the sensitive stuff is under the can because it's at sensitive higher impedance. Well, for the current, it's not very high impedance because you're like 10 milliohm resistor.

**Dave Jones:** It's a pretty low source impedance for your voltage coming across there. But you're talking about low signal levels, and you have have amplify them up. So, yeah, but once you've amplified them up, then Bob's your uncle.

**Dave Jones:** The voltage one over here is exactly the same. We've got our digital converters up there. I put up the data sheet of those before, and it's exactly the same successive approximation SAR converter here.

**Dave Jones:** And so, we'll have a look at the voltage one briefly here. We've got two Omron relays here. Unfortunately, look at this. China. Why can't I have a genuine Japanese Omron?

**Dave Jones:** Thank you very much. Anyway, the reason why that we've got all these resistors in series there, 1206 jobbies are they? The reason that we've got them all in series like this is because it's a high voltage string, and you can see the traces going like that.

**Dave Jones:** So, yes. And here's the bottom one. So, they're measuring the voltage across. That's just one big high voltage attenuation like that. So, yeah. Here it is. Here's our input connector.

**Dave Jones:** So, you remember this can measure up to 600 V. So, 600 V straight in, and then you know, 100 to 1 divider, whatever that is. In fact, they might tap off a couple of ranges there.

**Dave Jones:** But anyway, op 27, absolutely classic jelly bean precision op amp. And then, of course, yes, look at this. It's 74HC4052s. We've got some classic 74 series logic, but actually 4000 series logic.

**Dave Jones:** HC4053s. Classic triple analog muxes. These are your classic 4000 series muxes, but in the 7400 HCT series or HC. This is HC. This is HCT. So, this must be a TTL input threshold one.

**Dave Jones:** And anyway, they're analog switches. Classic analog switches, they do fine cuz once again, all the all the work's being done by these precision op amps. And this one, the OP1656, take a look at the video tape on this.

**Dave Jones:** It's a Burr-Brown jobby. Yes, all the Burr-Brown fanboys go wild before they were acquired by TI. Now, it's TI, but bloody Burr-Brown make the best stuff. Anyway, ultra low noise, low distortion FET input op amp.

**Dave Jones:** Look at this, point .000035 % distortion at 20 kHz. Ah, an audio fool's wet dream. Um and no, but they don't want really high precision stuff like this cuz they like the smell of their own farts and uh and the noise coming from their valves.

**Dave Jones:** So, you know, whatever. Anyway, um yeah, this is probably probably I don't know the best audio op amp on the market, perhaps? If you've got a better one, leave it in the comments down below, but yeah.

**Dave Jones:** DJ equipment, turntables. You've got your turntable. You put your points .000035% 20 kHz distortion in your turntable amplifier and yeah, okay, whatever. Anyway, fantastic. Probably, you know, if not the world's best op amp.

**Dave Jones:** Anyway, gain bandwidth product 53 MHz. Can easily do the 300 kHz bandwidth that we're looking at here. They're not gaining it up a lot, but very schmick. So, they've got three of those jobbies and yeah, that's it.

**Dave Jones:** And they're using that to drive the ADC. Now, the only other interesting thing here are these parts here. And there's a few of these in both the voltage and current.

**Dave Jones:** It's It's designator is RM8. So, this is like a resistor matched It's some sort of matched resistor array. Some sort of special secret squirrel matched resistor um array like dual resistors in it cuz they want them thermally bonded and thermally matched.

**Dave Jones:** They've got another three of those down here. So, these are like like just precision resistors, really. Um matched. I don't know. I don't know that package offhand. If you do know the manufacturer and if you notice that uh package if you recognize that package, then leave it in the comments down below, but yeah, some sort of matched resistor thing, not just, you know, your regular standard Joe Blog's

**Dave Jones:** resistors here. And as I said, this has got a linear reg out here. That's just an LM 7805 uh jobbie. And this will just be another low noise uh regulator just for powering the ADC here cuz that's important.

**Dave Jones:** So, yeah, cool bananas. And we'll go over here. And on the current amplifier side of things, look at this. Over here, I love how the the this is the uh this is the shunt resistor module version 1.00.000 because you never know when you have to get six uh you know, revision um decimal points in um to here in simple riser board for your shunt resistor.

**Dave Jones:** So, yeah, that's funny. Anyway, yep, so we have our lines coming out of here. We've got a Linear Technology 1037. Take a look at that. That's a low noise high speed precision op amp there.

**Dave Jones:** Yes, I'm not sure why they've chosen that particular one. Um anyway, you have sine wave generators here. Tape head amps, wide microphone preamps, strain gauge amps, microvolt s accuracy threshold detection.

**Dave Jones:** What's the offset voltage on this? This would have Yeah, guaranteed 0.6 microvolts max drift with temperature, 25 microvolts max offset voltage. So, it's not low. So, they're not using a chopping chopper amplifier uh like say we use in the microcard.

**Dave Jones:** I've done many uh videos on that. Um so, yeah, they're not they're not using that there. Um I would have expected a chopper configuration here actually because your offset voltage is going to matter when you've got a current sensing um shunt like this.

**Dave Jones:** Anyway, um we've got this um intercell jobbie. Uh let's take a look at that. And that's just a mux. So, looks like they needed a better mux than the uh 4000 series CMOS the 4053s and whatnot.

**Dave Jones:** So, yeah. And once again, we've got the 1656s here, 1560 56s. And they do actually have the 4053s here and here as well. And once again, we've got those little match resistor things there, those match resistor pairs.

**Dave Jones:** They got those all over the shop. So, yeah, that's interesting. Um but, yeah, I don't see a chopper amplifier here. So, that's surprising because you saw that we only change between two different shunt resistor values, the 10 mΩ one and whatever the higher one is.

**Dave Jones:** I actually I don't know where the higher shunt resistor is and on that board. No, it wouldn't be on that board, would it? Um might be on the riser board cuz I don't see a precision shunt resistor in here, really.

**Dave Jones:** Um you know, like a 1 Ω or 10 Ω or something like that. Anyway, like even with say the 10 mΩ one, it's great when you have like a full scale like half a volt drop across it or something like you know, several hundred millivolts drop maximum.

**Dave Jones:** But, when you're down in the resolution of your converter down in there, you've got like microvolts and then uh you know, this app op amp here had 25 microvolts offset voltage, for example.

**Dave Jones:** And then it's going to vary with temperature and stuff like that. Whereas a chopper amplifier is going to auto zero. It's called an auto zeroing amplifier. I've done videos on this and it's going to zero out that offset, basically.

**Dave Jones:** So, you get like, you know, 0.1 microvolts offset or something like that, you know, it's practically zero. Yeah, I'm not seeing any chopper package in here at all. So, that's interesting.

**Dave Jones:** Although, this you'll notice when I switch it on later, I'll show you that it does actually have a residual offset in it and it does actually put have that in the specs as well.

**Dave Jones:** So, they just didn't bother to put a chopper in there and make it better? I don't know. At this price point, another couple of bucks for a precision chopper amp.

**Dave Jones:** So, don't know what's going on there. LM393 dual op amp. Yeah, we've got another one of uh those low noise TL072 absolute classic jelly bean amplifier in there. That's not doing much to write home to your mum about.

**Dave Jones:** Um as and we've got some regulators here, but yeah, I expected a like really low offset chopper in there and we didn't get it. But yeah, they've got some pretty schmick op amps and they're using these what matched resistor dividers or something.

**Dave Jones:** So, we've got it back together and it seems to work. So, let's go into the current here and I'll tell I'll show you what I said about that offset there.

**Dave Jones:** Let's go down to the smallest current range that we actually can, 5 milliamps here and well, we can go down to the smallest voltage, but it's only got 15 volts up to 600 volts there, but anyway, we can go down to say 15 volts here and you see that we have a residual offset there of about 1.8 micro there and that is probably that that residual offset of that op amp that

**Dave Jones:** we actually looked at there. Because what I think they're doing there is they're actually trading off the ability to have lower offset here in the measurements with noise. So, they've opt they've decided we're going to prioritize like a lower noise floor on this thing rather than the offset down at the, you know, incredibly low values.

**Dave Jones:** Cuz this isn't designed to go down to, you know, nanoamps and stuff like that, but it's like it's really quite good as you can see, right? We've got like 100 nanoamps resolution on this thing.

**Dave Jones:** You can see it's changing by a single least significant digit is 100 nanoamps there, which is really great for most products unless you're really into ultra ultra low power stuff.

**Dave Jones:** So, but for most general product uses, this is really good, but they've decided to trade off just in that like lowest range there. And we should notice that doesn't really change except for the resolution there.

**Dave Jones:** So, there we go. It's now three microvolt three microamps offset there and they do actually include this in the spec. I'll try and put it up here. I can't remember offhand, but yeah, so it is in there and once we've lost that digit, boom, it goes away.

**Dave Jones:** Cuz as I said, when we go to the 200 milliamps maximum range for that 1 ohm or 10 ohm shunt resistor, whatever it is. When we switch to 500 milliamps, hear the relay click, clunk, like that, and then we restart the offset again.

**Dave Jones:** Um so, yeah, 500 milliamps, unfortunately, we've got the 0.33 milliamp offset. So, there we go, until you lose a digit and it vanishes. It's exactly the same. So, there's two current shunt resistors there, but unfortunately, that's the tyranny of ranging there.

**Dave Jones:** Unless you're going to have an entirely separate shunt resistor and amplifier for each one of those ranges, or at least shunt resistor, and then you can switch them using MOSFETs or whatever.

**Dave Jones:** Um but unless you like if you've only got the two shunt resistors, then yes, um on the slower on the lower ranges, um which is 5 milliamps and 500 milliamps here, uh you're going to get a greater effect of the offset uh voltage there.

**Dave Jones:** It's just going to beat the laws of physics, Captain. But as I said, if maybe if they used like a really, you know, best in industry uh chopper amp, they probably could have eliminated that.

**Dave Jones:** Um and you can do it with like manual tweaks and things like that, but then that's it just gets ugly, and well, you don't really want that. So, um yeah, cuz that adds adds a lot of time, and time is money, of course, when you're producing instruments like this.

**Dave Jones:** You don't want to be in there with some, you know, graybeard his tongue at the right angle uh trimming little uh trimmers in there, or even a software offsetting and stuff like that.

**Dave Jones:** So, you know. Let me show you a real-world measurement example here that I've been actually wanting to do. Uh this is the new Brymen/Eevblog BM787BT, the Bluetooth multimeter. I've done a video on that on the second channel.

**Dave Jones:** Uh if you haven't seen or a little bit of it, I'll be getting that fairly soon on the eevblog.store. Anyway, I want to measure, um, its battery power consumption when it's in Bluetooth mode, when it's actually transmitting data.

**Dave Jones:** So, I've got it hooked up here. I've got my, uh, power supply here generating 4 and 1/2 V, which is the nominal, uh, three, uh, AAA uh, battery thing here.

**Dave Jones:** And I've got the, uh, digital power meter connected to it. Let me show you how I've got that hooked up with the Dave card here. Uh, we've got our power supply here.

**Dave Jones:** Um, so our positive goes into the, uh, current shunt, the internal current shunt there. The positive side of the current shunt, you get that back to front, it'll be then your readouts will be negative.

**Dave Jones:** Then the output of the current shunt just goes into the positive input, uh, the battery terminal of the multimeter, and the ground is just connected to the ground. And this is the voltage sense, uh, terminals here.

**Dave Jones:** So, what I've done is I've put the voltage sense terminal actually on the negative side. So, any power that we're measuring is actually the current going into the device and the voltage across it.

**Dave Jones:** Now, uh, you can actually, uh, put this terminal on the positive side here across the power supply, and then you're actually measuring the true power supply source. But we won't go into reasons when you might want to do that and might not.

**Dave Jones:** But in this particular case, so we're just avoiding any power that's dissipated or power lost in the measurement shunt resistor inside this thing. But at these sorts of power levels, it doesn't really matter.

**Dave Jones:** Anyway, I've got it hooked up, and you can see I've just got the meter. It's it's not, um, transmitting anything, so data mode is not actually, uh, switched on.

**Dave Jones:** And you can see in AC voltage mode, we get our 4 and 1/2 V voltage there, U, not that V rubbish. U, hate it. Don't get me started, it's V, not U.

**Dave Jones:** Anyway, I can live with it. Um, and you can choose your different measurement parameters here for each of these, uh, four settings. So, we're we've just chosen the voltage, which is U, and the current, uh, I there.

**Dave Jones:** And you can see it's drawing 8 and 1/2 mA. And we're just multiplying those two together to give us the instantaneous power, 38 mW there. And I love this um, FU error cuz we're actually trying to measure Hz.

**Dave Jones:** I don't know. It was just there from default or whatever. So, that's why it's showing error because we're in DC mode up here. And you can watch that power change, okay?

**Dave Jones:** When I go into the different it should drop. Yeah, cuz AC is going to take more because it's doing more stuff. And millivolts there. So, it's round about 20 mW.

**Dave Jones:** Ohms keys is a bit less. And capacitance, more less again. Look at that. Temperature measurement mode, current. And other currents. So, yeah, the highest the highest mode here is your AC volts.

**Dave Jones:** But let's just put it in say DC volts. But watch what happens when we turn our data on here. I'll hold this on. And boom, we're in data mode there.

**Dave Jones:** And you see that's going that that kicked up there. That was very short, but anyway, we can adjust adjust the update, right? Let's do it 0.1 per second, shall we?

**Dave Jones:** So, there we go. It's updating really quick now. So, let's actually switch that data back off, okay? And bingo, we've got our 4.5 mA, okay? Watch this. Switch it on.

**Dave Jones:** Whoa, it was 20 something mA there. It's jumped up. And so, it's actually trying to negotiate hooking up with the shoe phone at the moment, the Bluetooth app. You might say it bright look, it's jumping up, right?

**Dave Jones:** 14 15. So, there's like a brief there's, you know, current spikes in there. And we can of course log this data. We're just viewing it on the screen at the moment.

**Dave Jones:** Okay? So, let's see if it'll log. Will it Come on. There we go. It's connected. Did that change? I wasn't watching the screen over here. But it could actually be consuming more current when it's actually like in in negotiation mode.

**Dave Jones:** And then I can and the channel here. And we can actually go into a real time logger here and we can actually log Oh, did it jump up there?

**Dave Jones:** Like seven, eight? I mean, we can turn on like average modes and stuff in here, right? So, we're we're just reading uh noise at the moment. So, it's just, you know, least significant digit there.

**Dave Jones:** No, I don't think there's anything in that. It's really hard to see there. We probably need to uh log this. And we can actually view the waveform here and we can see those spikes generated being generated there.

**Dave Jones:** Those those current spikes. And you can actually see that there's little modes in there where it actually increases. Now, not only is there that little uh transmit spike there where it's transmitting the packet, but it's I can't get it to sync there.

**Dave Jones:** You know, this is not as uh groovy as a proper scope for uh triggering wise, but you can see that we've got peak currents there of like 48, 49 milliamps there.

**Dave Jones:** So, you know, it's getting up there. And then, watch that waveform data if I switch off the transmit mode. There we go. And now, we've got peaks of like, you know, 3 milliamps.

**Dave Jones:** So, the answer is yes, of course, it's going to actually chew probably a significant amount of power extra um it when you're actually logging um Bluetooth data to your shoe phone.

**Dave Jones:** And nothing surprising there, you expect that, of course. Now, if we want to measure energy, which is basically our power with respect to time, then we want to use the integrate mode uh which basically it integrates the power to give us a watt-hour figure over time.

**Dave Jones:** So, I've got it in non-transmit mode and we can start our integrator and boom, it's going to get our milliwatt-hour figure and we can take this over, you know, we can leave it logging until the battery's run out um or, you know, for an hour as a benchmark or a day's worth of logging or something like that.

**Dave Jones:** And we can get an accumulated milliwatt-hour figure. But anyway, just use your noggin at the moment and look at how fast that's counting up. Maybe count that digit three, four, five, six, and well, actually, we'll do it live here.

**Dave Jones:** Ready? We'll turn on the data mode. Boom! It's now transmitting. And that's counting up significantly quicker now. So, we can get an accumulated milliwatt hour figure over time. And if we know the milliwatt hour capacity of our battery, for example, for a given cutoff voltage, I know it gets a bit complicated.

**Dave Jones:** We can start talking about cutoff voltages and things like that, but um yeah, we can we can use this tool to actually um get a like a nice battery consumption figure, uh a comparative battery consumption figure for our product that we're developing.

**Dave Jones:** So, it it's very cool. And it can do a lot more stuff, of course, you know, as I said like you can do harmonic analysis and stuff like that, but um yeah, and and of course, we can use the other stuff, right?

**Dave Jones:** We can go back into the data here live, and it's still integrating in the background. And that's that probably doing it inside that ASIC and the arm processor there.

**Dave Jones:** It's it's just doing that integration um with inside that, so you can operate the menus and do everything else while you're actually doing uh the long-term integration uh measurement, which is really cool.

**Dave Jones:** And we can get milliamp hours there if we didn't want uh milliwatt hours uh depending on what battery spec we're doing and stuff like that. So, a very comprehensive bit of kit.

**Dave Jones:** Now, of course, you can do this uh like with a you know, two multi two logging multimeters, but then you've got to have the software to actually you know, the data logger software to actually do that and accumulate that over time.

**Dave Jones:** This is like it just a nicety that you've got this built into the one bit of kit. And because this is doing integration in hardware, that's what that ASIC, no doubt what that ASIC is for, it's doing that in hardware.

**Dave Jones:** It at one meg sample per second for the voltage and current. It's doing it in a real time and really fast in the hardware, so it's not going to miss any of those transmit little transmit spikes and stuff like that.

**Dave Jones:** Whereas if you're doing this sort of measurement with your regular multimeters, they're slow as a wet week, right? Whereas this is like a precision voltage and current meter, but it's capable of 1 megasample per second.

**Dave Jones:** So you're not going to miss all of those little transmits. So you're going to end up with a true energy indication and you haven't missed any of these like fast spikes or you know, your processor is changing modes and doing things like that.

**Dave Jones:** Or in this particular case, they're doing a little RF transmission burst and things like that. So yeah, you really need a fast digital power meter in doing that integration in sampling and integration in real time in the hardware to capture all this.

**Dave Jones:** And that's what this thing can do. It's pretty cool. So I've switched off our load and you'll notice that our residual current there has shifted a bit because we've got the whole setup actually connected in the back.

**Dave Jones:** So if I disconnect, let's diddle the let's diddle the back here and boom. No, there you go. I've interesting. I thought that would go back, but that has actually drifted.

**Dave Jones:** The the residual offset has actually drifted. Anyway, we can actually calibrate that out. Unfortunately, I'd love to have it actually get it back to where it was before. Maybe I should turn it off for a while.

**Dave Jones:** So we can actually calibrate and zero that out with the cal function there. But yeah, I don't have to. But you can see that it does drift. So unfortunately, down at the least significant digits here, you are going to drift a bit.

**Dave Jones:** And you can calibrate it out, but then you might drift again due to temperature, whatever. I just actually repowered the thing and we're getting that negative point triple 0 5 there, but we can null that out.

**Dave Jones:** and what? Yeah, it gets a bit tricky but you can see so you could have eliminated the need to actually do that and you know, you can get like one LSB in digital or something offset if you really want to design that in but then that impacts the noise floor and the bandwidth as well.

**Dave Jones:** So this thing wants to be really fast. So yeah, we're we're sort of trading off a bit of that DC that absolute offset accuracy for bandwidth and noise floor really.

**Dave Jones:** And you can just do a whole bunch of stuff in the one instrument. So that's a very cool bit of kit. I like that. Yeah, sorry I can't give you a final result on this but yeah, we probably expect the battery life to maybe halve or go down by a third or something like that if you continuously log in the Bluetooth data.

**Dave Jones:** So anyway, I hope you enjoyed that video and look at this interesting bit of kit that a lot of labs don't have but if you're doing any sort of product development where you need any sort of energy or power measurement or something like that, having a dedicated digital power meter like this very cool bit of kit worth having.

**Dave Jones:** Anyway, thoughts and comments down below and if you like the video, please give it a big thumbs up cuz that helps with the engagement on YouTube. I'm trying to beat the bots.

**Dave Jones:** It's almost impossible these days. Anyway, yes the Bluetooth version of the multimeter will be available as soon on the EV blog store. It will cost a bit more than the regular 786 but I'll have it shortly.

**Dave Jones:** This is a prototype which just has like stickers on there and you can see it's just got the it's just got the stickers and no blue for the EV blog yet and no blue holster but anyway, it's coming.

**Dave Jones:** Anyway, hope you enjoyed that and found it useful. Catch you next time.
