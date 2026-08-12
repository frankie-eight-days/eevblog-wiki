---
video_id: c5M8P6oe9xY
title: EEVblog 1464 - TOP 5 Jellybean Comparators
url: https://www.youtube.com/watch?v=c5M8P6oe9xY
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 23, "3": 38, "4": 54, "5": 64, "6": 78, "7": 90, "8": 99, "9": 110, "10": 119, "11": 141, "12": 153, "13": 163, "14": 178, "15": 191, "16": 203, "17": 212, "18": 224, "19": 235, "20": 250, "21": 268, "22": 283, "23": 303, "24": 315, "25": 332, "26": 342, "27": 353, "28": 374, "29": 384, "30": 398, "31": 411, "32": 425, "33": 433, "34": 457, "35": 467, "36": 486, "37": 509, "38": 520, "39": 530, "40": 545, "41": 561, "42": 572, "43": 584, "44": 595, "45": 606, "46": 618, "47": 625, "48": 638, "49": 646, "50": 665, "51": 676, "52": 686, "53": 695, "54": 704, "55": 713, "56": 724, "57": 738, "58": 747, "59": 755, "60": 766, "61": 777, "62": 790, "63": 800, "64": 812, "65": 824, "66": 837, "67": 852, "68": 866, "69": 879, "70": 890, "71": 908, "72": 925, "73": 935, "74": 945, "75": 955, "76": 966, "77": 978, "78": 990, "79": 1007, "80": 1025, "81": 1036, "82": 1049, "83": 1059, "84": 1072, "85": 1085, "86": 1106, "87": 1125, "88": 1133, "89": 1148, "90": 1157, "91": 1167, "92": 1180, "93": 1190, "94": 1206, "95": 1222, "96": 1232, "97": 1244, "98": 1257, "99": 1266, "100": 1284, "101": 1300, "102": 1315, "103": 1328, "104": 1337, "105": 1352, "106": 1372, "107": 1392, "108": 1403, "109": 1422, "110": 1439, "111": 1452, "112": 1474, "113": 1487, "114": 1499, "115": 1515, "116": 1529, "117": 1538, "118": 1549, "119": 1564, "120": 1580, "121": 1592, "122": 1601, "123": 1610, "124": 1624, "125": 1635, "126": 1648, "127": 1660, "128": 1675, "129": 1685, "130": 1696, "131": 1708, "132": 1718, "133": 1731, "134": 1740, "135": 1753, "136": 1764, "137": 1782, "138": 1797, "139": 1807, "140": 1821, "141": 1835, "142": 1846, "143": 1861, "144": 1877, "145": 1901, "146": 1918, "147": 1931, "148": 1941, "149": 1957, "150": 1977, "151": 1989, "152": 2007, "153": 2015, "154": 2028, "155": 2050, "156": 2062, "157": 2074, "158": 2086, "159": 2098, "160": 2112, "161": 2132, "162": 2145, "163": 2159, "164": 2170, "165": 2184, "166": 2202, "167": 2213, "168": 2223, "169": 2231, "170": 2245, "171": 2255, "172": 2268, "173": 2280, "174": 2294, "175": 2309, "176": 2320, "177": 2337, "178": 2357, "179": 2379, "180": 2391}
---

**Dave Jones:** Hi, it's jelly bean component time again. In two previous videos, we took a look at jelly bean op-amps and jelly bean voltage regulators and references. So, I'll link those in if you haven't seen them.

**Dave Jones:** So, this one is going to be jelly bean comparators and it's not going to be quite as easy. There's a few definite jelly bean comparators, but there's a few oddball ones as well due to probably necessity.

**Dave Jones:** Anyway, let's get into it. A jelly bean component has several criteria. One is that it has to have pretty much been around a long time to become the industry standard part, just the go-to part that you grab when oh, I need a voltage regulator.

**Dave Jones:** I don't need an op-amp. I need a comparator. Don't care too much about the specs. I just, you know, that's the jelly bean one that you pick. And when a jelly bean component's been around for so long, often 30 or 40 years, then it's of course set the sort of like standard specifications.

**Dave Jones:** It's set the standard package, the standard pinout, and thing which most other manufacturers follow. And that's the thing about jelly beans is that they should be available from different manufacturers.

**Dave Jones:** Not only the big name ones, but also like the ones you've never heard of, all the Asian sourced manufacturers and everything else. If it's available from like five or 10 different manufacturers including the no-namers, then you can be pretty sure it's jelly bean-ish.

**Dave Jones:** Now, before we get to our first comparator, you might be saying, "Dave, I don't even need a stinking comparator cuz I can just use one of my spare op-amps that I've got lying around from my jelly bean op-amps.

**Dave Jones:** I might have had a quad package or a dual package or something like those. I got one spare. I can just use an op-amp as a comparator." Well, yeah, nah, as we say here in Australia.

**Dave Jones:** Yeah, you can use it, but there are some traps for young players. The main one being the speed of op-amps. They're just not that thing fast. You might think, "Ah, what's the big deal?

**Dave Jones:** No worries. I'm feeding the op-amp into a gate or something like that, a flip-flop." Well, let me show you the trap for young players. Let's take the LM358, one of our bog standard jelly bean op-amps down here.

**Dave Jones:** Frequency response. Our op-amps are slow, at least the jelly bean ones are. So, you look at the slew rate here, okay? 0.5 V per microsecond. So, if you want to sle- swing from 0 to 5 V for example, like you would for a like a 5 V comparator, then you're talking 10 microseconds um to do that.

**Dave Jones:** And not only that, because it's an op-amp, it's not designed to be driven non-linearly like this and sla- have the inputs uh and outputs slammed like this, you've got another thing called the overload recovery time.

**Dave Jones:** I'm sure I've mentioned this in another video somewhere. There's another 10 microseconds just to recover. And then you got settling time and stuff. These things are as slow as a wet week.

**Dave Jones:** And not to mention other problems with uh you might have diode clamping on the inputs for example of an op-amp, which actually designed to protect the input. Well, that means they could have a limited differential voltage range on the input.

**Dave Jones:** And you can't like compare big voltage differences and stuff like that. You could come a cropper there very easily. Not to mention the basic fact that an op-amp does not have an open collector output like a standard comparator will as you'll see later.

**Dave Jones:** So, can't use them as window comparators to do your regular you know or in function on the output and stuff. It's just you know, it's the not not the right tool for the job.

**Dave Jones:** Yes, you can use I've used op-amps as comparators cuz I had a spare op-amp available, but yeah, you have to be very careful. But let me show you why the speed could be a problem.

**Dave Jones:** Input slew rate limitations on digital chips, which you might be feeding an output of a comparator into for example. So, I know we started out on a complete tangent here, but it's pretty important.

**Dave Jones:** So, let's go like just a regular 74HC74 flip-flop Uh, for example. It'll be similar for other digital uh, logic. And here it is, right here. Input transition rise and fall rate.

**Dave Jones:** You're you're talking like four, 500 nanoseconds. So, right there, your op amp is not fast enough to drive just a jelly bean 74, you know, HC74 logic. So, what does that mean?

**Dave Jones:** Well, if you've seen my previous uh, digital logic uh, tutorial videos and stuff, you'll know that uh, flip-flops can get into a metastable state. Basically, any digital logic, be it discrete logic like this, it could be an FPGA, they're going to have a maximum input uh, transition time unless they're a Schmitt trigger input.

**Dave Jones:** And a good majority of them aren't Schmitt trigger inputs. So, you've got to be careful. If you exceed that maximum input rise and fall rate, then your gate can go into a metastable state and just go absolutely crazy and you'll wonder why your circuits are going silly buggers.

**Dave Jones:** But, anyway, enough of that. What is the jelly bean? It is and isn't the LM311. Sorry for all you 311 fanboys or 311 fanboys. Um, it is the industry standard jelly bean component in that it's been around since September 1973.

**Dave Jones:** And yes, it is the industry standard, but it's probably not the go-to jelly bean component uh, for a single op amp. If you just need one amp op amp in one package, you're probably not going to be using the 311 these days.

**Dave Jones:** I'll show you one uh, shortly. But, by definition, the jelly bean uh, comparator is the LM311. Always has been to a lot of people, always will be. Uh, as with all these jelly bean components, you should uh, have them available in your CAD library.

**Dave Jones:** For example, in like different packages and things like that and different uh, suppliers in in your bill of materials and supplier information and stuff like that. So, you can just drag and drop these jelly bean components in.

**Dave Jones:** That's the whole point of these. You have them in your standardized component library, uh I I need a comparator, I'm just going to drop in I don't care about the specs, I'm just going to drop in a jelly bean part.

**Dave Jones:** But the problem with um the LM311, it it has some good points and it has some not go so good points. The uh good points are that it actually has um extra inputs, a balance and uh strobe input here, uh which we can talk about, and it also has what's called a floating um output here or an uncommitted uh output.

**Dave Jones:** So this is what's called an open collector um output because the there's nothing else internal. It's just got an output uh driver transistor like this and the collector is not connected to anything.

**Dave Jones:** This allows you to uh do wire or configurations with your uh comparators. You can like tie all the outputs uh in parallel. You can get wire or wire and depending on how you uh configure the inputs and stuff and you can do a logic functions with the output and that's very useful.

**Dave Jones:** Uh one of the main reasons why um a good lot of probably the majority of comparators are open collector. Comparators like this, but the LM311 is special in that the emitter here is not uh tied.

**Dave Jones:** It's like essentially floating so that it's not tied through to your ground terminal like you'd get on a good majority of uh comparators out there. So the LM311 is still useful uh for that.

**Dave Jones:** If you needed an uncommitted um output like this or a floating output like this, yeah, the 311 would be your go-to thing. So what are the downsides of this?

**Dave Jones:** Well, unfortunately, it's only available in um basically an eight-pin um package. And most of the time, when you want just one uh comparator like this, same with an op amp, you you know, and you go in SMD and you want small because you don't you know, you want to minimize uh your footprint, you'd want to go for like a five-pin sot uh package for example instead of this eight-pin um

**Dave Jones:** SO1 because this has um some some balance and strobe and the uh extra emitter output like this, they just can't fit the 311. You just can't get it in like a five-pin sock 23 package.

**Dave Jones:** So, the 311 is not classified as a fast comparator, but 165 nanoseconds isn't too bad. It's not too shabby. Basically, we'll look at fast ones later and they're an order of magnitude better than that, but you know, it's you can get a certainly a lot slower than this one.

**Dave Jones:** And then you've got the input bias and offset current to your 300 nA and 70 nA. We'll look at low power ones later and they're orders of magnitude better than this down in like the pico amp region, but you know, this ain't too shabby for just, you know, if you're not talking about like real high impedance applications, it's not too bad at all and it can operate from a single 5-V

**Dave Jones:** supply. But the good thing is this is one of the high voltage op-amps we'll look at more later and it can do basically plus minus 15 V, so 30-V supply, but it works happily at regular 5-V.

**Dave Jones:** But this is by no means a low voltage compatible. We'll look at those later. And of course, it's got decent drive output capability, 50 V at up to 50 mA drive.

**Dave Jones:** And this is one of the things with comparators is that you have the big open collector driver because you don't just want to drive digital logic, for example. You want to In fact, one of the advantages of open collector like this is you might want to drive a relay coil.

**Dave Jones:** You might want to drive, you know, solenoid, you know, even a real high current LED, you know, tens of milliamps, something like that or even a string. And the output voltage is capable of handling 50 V, basically well above the rated supply voltage of the chip.

**Dave Jones:** Nice. And this is why you'll find like one of the applications here, white goods, for example, like you might find these in, you know, washing machines and dishwashers that have solenoids and drive things and stuff like that.

**Dave Jones:** You might just use the good old LM311. So, really the only reason you'd use the 311 these days is if, you know, you wanted like a eight-pin DIP package if you're doing through-hole or something like that.

**Dave Jones:** It's just fine. You can get it in SO or you wanted like a balance. For example, you wanted to make this a bit more precision. You wanted to put a pot in there and tweak it so that you can tweak the offset voltage.

**Dave Jones:** It was not that terrific in this. It's not that good cuz they don't tell you up the top in the data specs. But, it's not that bad. If you take a look over here, typically a plus minus 15 V, you're talking, you know, a couple of millivolts, something like that.

**Dave Jones:** Could be as bad as 10 millivolts, for example, over the full temperature range. But, you can actually put in a pot and trim that if you don't want to use like a real expensive precision op-amp.

**Dave Jones:** Then you got to pay for the pot and then you got to pay for someone's time to tweak it. You know, it's just like it's really old school, like 1970s stuff.

**Dave Jones:** So, here's an example of using the balance there with the pot and everything. It's just, you know, like there's just better ways to do it these days. You just spend the money and, you know, get a more precision op-amp if you need it.

**Dave Jones:** Anyway, the other function is the strobe, which is used as shares a pin with the balance pin. And what this does, you need an external You can't just strap it.

**Dave Jones:** You need like an external transistor here cuz this is a current-driven thing. And it will actually disable the output. So, it allows, you know, a micro or some other digital logic to actually disable the output transistor if you want to actually turn it off remotely or you want to gate it or something or strobe it, as it's called.

**Dave Jones:** So, once again, it's a pretty old school thing, more obscure application these days to have like a strobe capability on your op-amp. But, if you need it, hey, the LM311's for you.

**Dave Jones:** So, what would be the go-to jelly bean single comparator these days? Well, you could argue probably the TS391. This is like an ST one, but there are many other manufacturers.

**Dave Jones:** This I'll show you in a minute. And it's available in the SO-23, Uh, some, you know, DFN 8 for those who, you know, DFN fan boys, but very similar to 311.

**Dave Jones:** It's got 2 V to 36 V uh, capability. Uh, can be operated from plus minus 1 V supplies to plus minus 18. So, you know, it's really quite schmick.

**Dave Jones:** Um, it's got reasonably low current, uh, 200 microamps, and which is independent of the supply voltage. So, it doesn't matter. Um, so, you know, that's not too shabby. But, this is not a low power op amp.

**Dave Jones:** We'll show you an option for that in a minute. Um, it's 25 nanoamp input bias current, not too shabby. Um, input offset 5 nanoamps. Uh, input offset voltage plus minus 2 mV max.

**Dave Jones:** And once again, there are variations like A and B, you know, various versions. So, this this is the 301 and 391A. Um, and this will vary between manufacturers. All these sorts of specs will actually slightly vary between manufacturers.

**Dave Jones:** In particular, um, things like, you know, offset uh, voltages and bias currents and, you know, stuff like that. So, just be careful of that if you're doing a drop-in replacement.

**Dave Jones:** But, as with all jelly bean components, if you're caring about, "Ooh, I do care about the difference between 2 mV offset and 5 mV offset, then, you know, what a card.

**Dave Jones:** I have to pick this manufacturer over that one, then you're not really in the jelly bean category." You just strolled in there, and 2 mV, 5 mV offset, "Eh, she'll be right.

**Dave Jones:** No worries." So, the major specifications you're going to care about for a comparator are the input um, offset uh, voltage, just like op amps. They have offset uh, voltages.

**Dave Jones:** And if you have to really precision voltage uh, comparisons, then this could matter, but you wouldn't be choosing a jelly bean for this. So, you know, input like typically 1 mV, you know, could be as bad as 9 over max uh, temperature and stuff like that.

**Dave Jones:** And then you're going to have your input bias and offset currents, and this is pretty much uh, due to the technology of the devices. Is it a CMOS device, which we'll look at, or is it a bipolar device like this one?

**Dave Jones:** Um, and you can tell because it uses, well, where's where's the internal diagram? There you go. It uses bipolar transistors there. None of that MOSFET rubbish. Then of course the other thing you care about is your supply current, your ICC here.

**Dave Jones:** This has got, you know, 200, 500 microamps, something like that. So it's not low power. We'll we'll look at those in a minute, but you know, good enough. I mean, once you start getting into a couple of milliamps, jeez, that's a real high power jobbie.

**Dave Jones:** Now the input differential voltage, we might have a look at this later, but that matters cuz you can have like a real big like 30 volt range comparator. Yet it only has a small differential input voltage.

**Dave Jones:** So a bit of a trap for young players that one. So that could be important. Just keep a watch out for it. Of course the other biggie with comparators cuz as I said you usually want to drive relays or you know, something grunty, LEDs, solenoids or something, is the output drive capability.

**Dave Jones:** This one not that great, 16 milliamps typical. They don't actually give you an upper bound maximum on that. I don't know why ST aren't doing that. We might get it on another manufacturer, but yeah, I mean, you know, but that's good enough to drive like a relay or something.

**Dave Jones:** And the other biggie of course is the speed of the op amp. So the small signal response time here, 1.3 microseconds, but as we saw before, that might be too slow to actually drive like a digital logic for example.

**Dave Jones:** So you got to be careful. But because this is an open collector one here, then it's going to be dependent upon that's a pull resistor, the external pull up resistor you pull here for your positive going transition.

**Dave Jones:** That will depend on the the capacitance of your line and the pull up resistor value. But that's the same with all open collector comparators. So if you don't believe me that the 391 is available from different manufacturers, well, let's go over to LCSC here, which is like the Asian Digikey kind of thing.

**Dave Jones:** 319 comparator, whack that in there, and we sort by price down here, and we get the TS 391 from UTC, Unisonic Tech, and then we've got Rohm. Not sure if that one's if that's a T-sub 5.

**Dave Jones:** I'm not sure if that's the same. High-gain voltage comparator. Don't know. It looks looks similar, doesn't it? Then you've got the ST Micro one here, and then you've got the Texas Instruments.

**Dave Jones:** You've got an ON Semi one down here. You've got No, the ROM one to 2901. We won't go into that whole family. And then you've got TLV variants from Texas Instruments.

**Dave Jones:** There's another variant from ON Semi here, and well you start getting into lots of different variants, but you have to actually be careful here cuz there's another trap. And here it is.

**Dave Jones:** Check this out, right? It's got 391 in the number here from Analog Devices, but uh-uh, it ain't the same. Look, 2.3 V to 5 V to 5.5 V operation only.

**Dave Jones:** For example, the TLV 1391, which you might think, "Oh, it's got 391 in the number. It's the same." 2 V to 7 V open collector. It's not that high voltage range.

**Dave Jones:** So, just be careful of that, and I'll show you another trap in a minute where the same thing applies. So, just because it has the same digits in the number, it doesn't necessarily mean it's going to be an equivalent part.

**Dave Jones:** So, you want to be careful. And after all that waffle, we finally get to the what I think is the industry standard comparator out there, that jelly bean one that you're just going to use absolutely everywhere, which is the LM393.

**Dave Jones:** Once again, it dates from October 1979. Old school. And as its name says, it is a dual comparator. So, it's basically roughly equivalent to the 311, but it's available in the same SO8 package, but you get two comparators for the price of one.

**Dave Jones:** And it's pretty much the one you want to drop in. If you don't use the other comparator, meh, doesn't matter. It just, you know, tie it off or leave the pins uncommitted, and just use the single one, and you might be able to hack it in later.

**Dave Jones:** One of the advantages of using a dual package. So, it's got 38 V voltage rating, input offset point, you know, 370 microvolts. But, yeah, you got to you know, watch out for the spread of that.

**Dave Jones:** Input bias current 3.5 nA. It draws 200 microamps, which isn't too shabby. So, it's not super low power, but you know, it's lowish. It's got 1 microsecond response time.

**Dave Jones:** Once again, might not be fast enough for driving digital logic stuff and things like that. But, you know, it's for everything else, it's good to go. And as I mentioned before, there are like this you know, 2903 series.

**Dave Jones:** So, there are other manufacturers like series numbers in there as well. So, they're basically an equivalent part. Now, I won't go into the details. It's just same thing. We Everyone just calls it the 393.

**Dave Jones:** How jelly bean is it, I hear you ask? Well, put in 393 comparator into LCSC. 116 Right. We sort by price here, and yeah, like down in like 3 cents per part, you know, 3,700 in stock.

**Dave Jones:** 3,39,000 in stock. 210,000 in stock. Right, 173,000. No worries, right? And we comes from Hands Chip, ones you've never heard of. HGC, HG Semi, Zelonda, ID Chip, Diodes Incorporated.

**Dave Jones:** You've probably heard of those. EG Micro, never heard of. Who's Three Peak? Ones you then three but right. And then yeah, you know, even you know, you go up to five massive five cents.

**Dave Jones:** You know, you're into your ON Semi, you know, your real big brand names. You know, your Diodes Incorporated and Texas Instruments. One is still down in six, you know, the six cents region for a genuine TI jobby.

**Dave Jones:** And they're just available from Poolop. Got to see Poolop. Poolop. up. I I think we've had those before, haven't we? I think we discovered them on a previous video.

**Dave Jones:** But yeah, right. It's all there. And just to prove there's no component shortage when it comes to jelly bean comparators, let's go to Digikey here and search for LM393.

**Dave Jones:** And here we go. Look Look at this. 1.4 million in stock on the shelves at Digikey. You got to pay Well, look at this. Almost 12 cents in thousand off quantity.

**Dave Jones:** You get a genuine on semi though, but you know, like serious stock, right? And this is just a Digikey. No worries. And of course it's the comparator of choice for vacuum robots.

**Dave Jones:** So here's this family comparison table which I showed you before with the you know, the 2903 and stuff like that and then and the B version. And also like there's 193 and 293 which is available in same with the LM311 as well.

**Dave Jones:** And these are like just higher temperature range military components. You can see like minus 55 to 125° range. Whereas your regular one here is like 0 to 70°. But your B version minus 40 to plus 85 for example.

**Dave Jones:** Some of these might have different ESD human body model ratings and stuff like that. And your offset voltages might be higher. The only reason they're higher is cuz they're rated over like bigger temperature ranges.

**Dave Jones:** So go to the on semi data sheet. It just shows like the packages better and stuff like that. Shows the internal connections better than the TI data sheet. And this is the industry standard pinout for a dual comparator.

**Dave Jones:** Of course you lose the strobe and offset balance capabilities you get on the 311. But like if you're going to like these are cheaper. These are often the dual is often cheaper than the 311.

**Dave Jones:** So you're just going to throw in the dual anyway. Cuz odds are if you're going to use one comparator, you might need another one. But of course one of the big applications for our is a window comparator.

**Dave Jones:** So, you need those two op amps and you need the open collector output like this so that you can just here it is here the output is open collector so that you can just tie the two pins together and you can all the outputs and you can get make yourself a window comparator.

**Dave Jones:** Beauty. And if the dual job is not enough for you, well, you can get the classic 339 quad comparator. Here it is once again available in the 291, the 3239 and the 139 configurations, but it's basically both the 393 and the 339.

**Dave Jones:** I know they're a bit confusing, but they are basically dual and quad versions of the classic LM311. And once again, dates back to October 1979. Old school, but the 339 everywhere.

**Dave Jones:** Jelly bean as. The good thing about the 311, the 393 and the 339, I think I got that right, is that the common mode input voltage includes so it can be zero it can go right down to zero.

**Dave Jones:** So, hence you can use these as single supply applications and that's called ground sensing as well. So, you can sense all the way you can compare all the way down to ground.

**Dave Jones:** But the downside is these are not what's called rail to rail input op amps. We'll show you those in a minute. So, yeah, you can go down to zero volts, but you notice that it's it has to be at least 1.5 volts below VCC.

**Dave Jones:** So, it can't you can't compare voltages right up to the to the supply voltage the VCC voltage. So, that's something to consider for these jelly bean ones. So, let's now go have a look at what you might use for a lower power more lower voltage application.

**Dave Jones:** Now, if you're talking about low voltage comparators, window comparators, window detectors, you know, just general low voltage sensing and comparison applications, then you probably you might be looking at uh the basically the same as the 311, but it's the LMV series, and you might remember this from our op amps, which had a similar thing.

**Dave Jones:** Well, the same thing is available in comparators as well. So, the LMV331 is the single uh comparator, the LMV393 it's the same as the 393, but you'll see how the difference is in a minute.

**Dave Jones:** It's the dual version, and then we've got the quad version, the 339, but it's LMV in front of it. Uh V stands for voltage or low voltage. And it tells you right here, these are low voltage uh versions of the dual, quad, and single uh comparators, which operate uh from 5 to 30 V before, now they operate uh from 2.7 to 5.5 V only.

**Dave Jones:** So, only for your like your 3.3 V and 5 V TTL logic stuff. But, that's a lot It's everything these days, isn't it? When I was a boy. But, you'll notice that this is uh still uses uh bipolar transistors mostly in here.

**Dave Jones:** There's one little FET sneaky bugger FET in there, but basically these are uh it's still a bipolar. It's not a CMOS uh comparator. Haven't gotten to those yet. And it's the same open uh collector output, no worries, but it's just designed for different voltage applications.

**Dave Jones:** So, we'll have a look at the specs. So, all of your parameters here, they're all very quite similar to the um the non and just the LM version uh that we got before, but the difference is um in its sensing capability, which is But, the difference is if you power it from 5 V here, it does have a better um input voltage range, but still not rail-to-rail.

**Dave Jones:** So, it will be ground sensing, so the common mode input uh voltage range does go does go below ground, so that includes sensing to ground, uh but it'll still only go to 4.2 V.

**Dave Jones:** So, still not quite rail-to-rail input, but these are better suited if you know you're working at 3.3 or 5 V, you you know, drop this into your uh schematic instead of the regular uh 393 for example.

**Dave Jones:** But once again, be very careful with 331 in the number, LMV331. Well, this is TI, right? TI also make a TL331. It's very different. Um yeah, it's like the like 38-V um comparator again.

**Dave Jones:** It is not the low-voltage jobbies. So, just be aware, same number, but that uh prefix matters. Now, unfortunately, at this point, all the ones we've seen up until now, they are truly jelly bean op amps.

**Dave Jones:** But here's where the wheels fall off the jelly bean billy cart, and uh pretty much you start getting to single-source and maybe only like a two sources or something like that.

**Dave Jones:** Now, um all the ones we've looked at have been open-collector ones, and they've had limitations in terms of like non-rail-to-rail inputs, they've had limitations in terms of speed and all sorts of stuff.

**Dave Jones:** So, let's go and look at like a better class of uh comparator here. Um and let's go for the TLV370x family. So, the 3701, 3702, and the 3704. You can also get these second-sourced.

**Dave Jones:** These are TI, but you can also get them second-sourced from um ST as well. They do the TSR3702. And these are, you know, pretty decent ones. Even though I wouldn't call them jelly bean, these are kind of like the next step up in uh comparators uh for, you know, useful applications.

**Dave Jones:** As you can see here, these are nano power, so they're low-power jobbies. They're push-pull outputs, so no more open-collector outputs. It can both uh push the output voltage high, so it can actively drive it high.

**Dave Jones:** You don't need an external pull-up resistor uh to get uh the output. And of course, if you're driving relays and things like this, um then this is not something that you'd be using.

**Dave Jones:** So, they're available in single, dual, and quad versions. Uh 560 nA per channel, right? So, we're none of this microamp rubbish, we're like nanoamps now um per uh comparator.

**Dave Jones:** Input uh common mode range exceeds, uh, the rails. So, um, you can actually go to VCC plus 5 V. So, the input voltage range you can actually, um, sense higher input voltages than the rail.

**Dave Jones:** And the actual operational rails can go from 2.5 to 16 V. So, that's very useful using for like 12 V applications. So, even if you used it for a 12 V application, you could still sense 5 V above that.

**Dave Jones:** So, up to 17 V. Nice. So, this is a push-pull CMOS output stage. So, we're going from our bipolar technology to our CMOS technology, just like you do in op amps.

**Dave Jones:** Uh, this is the same for comparators and there's probably hundreds of CMOS, uh, comparators, um, out there. But, I think, you know, these are good ones that you should have, um, in your, you know, your parts library so you can just drop them in.

**Dave Jones:** And the input offset voltage is nice on this. So, you could almost call this like a precision, uh, comparator as well. 250 microvolts, of course, that's just typical. Like, it could go up to 5 mV or 7 mV over the full, uh, temperature range and stuff like that.

**Dave Jones:** But, you know, it's, you know, it's fairly tight, um, if you're generic, uh, spec there. And now, because it's CMOS, your input offset and bias current is down in the pico amps range.

**Dave Jones:** None of that nano amp rubbish. Uh, 20 to 80, uh, well, you could, you know, over the maximum temperature, but barely sneaking into the nano amp range. But, typically, like, under 100 pico amps.

**Dave Jones:** Nice. So, really good for like, um, you know, high impedance, uh, sensing applications. And of course, because it's rail-to-rail output now, it can actually drive directly to the VCC output, uh, rail.

**Dave Jones:** So, it can go to within 80 mV of the VCC rail. Unfortunately, they're not perfect. They're not the fastest, uh, things around. So, yeah, seven, you know, ish microseconds, something like that.

**Dave Jones:** So, if you need a really fast op amp, but they these are but that's the you trade off power consumption with speed, of course. So, these are like these are literally nano power, right, for a reason.

**Dave Jones:** But, you know, like for low voltage, uh low power, and like high input impedance applications that can go beyond a rail and stuff like that, these are just incredibly useful.

**Dave Jones:** Worth having in your component selection library. And you can see that the ST Semi has the internal diagram here. And yeah, it's like a mixture of bipolar and bit fit input ones here.

**Dave Jones:** And of course, the totem pole output there or push-pull as it's called. None of this if it just had like an open drain output, then it would just have this.

**Dave Jones:** If it says open drain instead of open collector, then you know it's a CMOS version instead of a bipolar version. But, yeah. So, it's a push-pull output stage. Now, the interesting thing to note, if we go into comparators over on LCSC, which of course lists all the major Asian manufacturers, they stock all of those.

**Dave Jones:** Now, if we actually search for anything, but you know, anything like really performance like fast, for example. So, let's go search for, okay, propagation delay. Let's search for I I would consider anything under probably 20 nanoseconds.

**Dave Jones:** Let's just go 50 nanoseconds, right? So, let's go for a really fast comparator here, okay? And let's search and see what we get under 50 nanoseconds for a comparator.

**Dave Jones:** What do we got? TI, Analog Devices, Maxim, TI, TI, TI, this Analog Devices. Oh, three peak. We finally got one. We finally got one. There's no There's no data sheet.

**Dave Jones:** Don't even look at it. But, that is 12 nanoseconds. There you go. But, basically, look, these are all name brand stuff. The second page here, same. Analog Devices, Maxim, you know, right?

**Dave Jones:** Right? There's onsemi, right? There's basically there's only that one manufacturer couldn't even Asian manufacturer couldn't even get a data sheet for that makes a fast comparator under 50 nanoseconds.

**Dave Jones:** So, there you go. If you want all this high performance stuff, and then if you want precision ones as well, then you start talking all your major manufacturers. The, you know, the generic Asian ones that you haven't heard of before, they typically won't go into those sort of product areas.

**Dave Jones:** So, that raises the question, why wouldn't they go into those areas? And this might be, it's not just comparators, it's other parts as well. Now, if you need, you know, if you open up like a cheap consumer thing and it's, you know, it needs some precision part for something, you're probably going to find one of the major manufacturers in there.

**Dave Jones:** You're not going to find one of the no name Asian brands in there. If you've got any like really detailed info on why, leave it in the comments down below, but I suspect it's, you know, it's process variation and they just, you know, can't control or they don't want to try and control the, you know, the the processes to actually get and all the testing requirements else that goes into

**Dave Jones:** manufacturing really high precision, you know, high performance parts. They just generally don't seem to go into those sort of areas. It's really interesting. So, if you wanted higher speed than these nano power type ones available, like the 3701, 370204, then take a look at the TS30, 21.

**Dave Jones:** Once again, I think this is only single sourced. Maybe you can get it somewhere else, but I can't readily find it. But anyway, this is, you know, a 38 nanosecond job here and it's available.

**Dave Jones:** So, if you only need one comparator, it needs to be reasonably fast and, you know, you need rail-to-rail and you need low voltage and stuff like that, then this is, I would say this is probably one of the picks that you'd go for.

**Dave Jones:** It's reasonably priced, does 38 nanoseconds, it only takes 73 microamps, rail-to-rail input, it's got your push-pull outputs, 1.8 to 5 volt operation, it's got a high ESD uh and, you know, it's not too shabby.

**Dave Jones:** Well worth checking out. And in terms of precision, um you're talking input offset voltage, you know, like 500 microvolts, so that's not too bad. Once again, like over temperature, if you want to, you know, play the absolute specs uh game, then it, you know, could be as high as, you know, a couple of millivolts or something like that, but yeah, it's not too shabby.

**Dave Jones:** But, here's where it counts. Rise and fall times over here, 8 and 9 nanoseconds. Not that microsecond rubbish, so, you know, this it is a pretty nice little fast, um you know, low voltage uh comparator I really quite like.

**Dave Jones:** And then you got your propagation delays and stuff like that. It's, you know, it's not too shabby at all, so well worth having in your parts uh selection. But, if you want kind of when you think about like a fast precision comparator, um like old-timers like me would think of the LT1016.

**Dave Jones:** That That was, you know, it used to be like the go-to one. I don't know. Leave it in the comments down below. Um do we got a date on this?

**Dave Jones:** No, revision, no. They don't seem to have a date on this. But, anyway, the 1016, it was like at the time was like the sort of like, you know, a fast it it was the 10 nanosec ultra-fast precision 10 nanosecond comparator.

**Dave Jones:** That says it all, right? So, you would expect this thing in. It's not cheap. It's not jelly bean. And there's lots of other parts that beat it uh these days, you know, but it's sort of like a baseline where it's a lot of uh manufacturers are going even Analog Devices {slash} LT will go, "Look, it it's an improved version of the 1016." So, it's ultra-fast, you know, operates from a 5-V supply.

**Dave Jones:** It's got low offset voltage. No No minimum input slew rate requirements as well, so it's not going to latch up. It's pretty stable, um you know, and output latch capability as well.

**Dave Jones:** So, yeah, it's like lots of like precisiony type outputs, and it's got complementary outputs, so that's why it's in your 8-pin uh package, because it's got Q and not Q outputs as well.

**Dave Jones:** Thanks for playing and a latch enable as well. So, it can latch the output. So, like sample and hold type stuff and things like that. It's really nice. Time to throw a curveball in.

**Dave Jones:** So, we're definitely non-jellybean now and this is just a bonus one cuz I think it's really cute and it's fairly cheap, too. It's like in the 25-cent category and you can get it from two different sources.

**Dave Jones:** Very versatile part. Um it's the TSM102 and you can get it from TI and ST as well. So, let's let's take a look inside here. So, what are you getting in this bad boy?

**Dave Jones:** Well, you get a dual op-amp, a dual comparator, and a voltage reference. Would you like steak knives with that? Anyway, yeah, check out this bad boy. So, you've got two comparators in there, two op-amps, and an adjustable reference all in the one chip.

**Dave Jones:** So, yeah, you might have guessed what applications, you know, switch mode power supplies, battery chargers, voltage and current sensing, overvoltage, undervoltage, window comparators, alarm detectors, sensors. So, if you're doing all sorts of analog stuff, you can actually combine.

**Dave Jones:** This is good part bomb consolidation. You know, if you need a jellybean op-amp and a jellybean comparator and a jellybean reference, this will do it all in one or it might do it, you know, you've got to check your specifications.

**Dave Jones:** So, they're relatively low power. The op-amps are 200 microamps a pop. The comparators are 200 microamps a pop and the voltage reference Vref up to 36 volts which is adjustable.

**Dave Jones:** Can sink from 1 milliamp to 100 milliamps just like the jellybean references we looked at last time, you know, 0.4% A grade. You can get standard grade versions. It's got latch up immunity for the comparators, of course, which is what we care about here.

**Dave Jones:** Input common mode includes ground, but this is not a rail-to-rail one. It's going to be open collector um output. And you know, it's a 2.1 meg um op amp, and it's once again ground sensing, and uh basically 3 to 30 V operation here for both the op amp and the comparator.

**Dave Jones:** So they just, you know, similar to the other ones we're seeing. So they got separate specs for the op amp, separate specs for the comparators, and you know, 1 mV input offset voltage typical.

**Dave Jones:** They don't give you a typical uh for the comparator, but you know, it's like in the same class as your 393s and your 311s and um stuff like that, right?

**Dave Jones:** And uh your input offset currents, this is not uh you know, it's down in the nanoamp region. You don't get a typical value there. You might get it over on the ST uh data sheet or something like that.

**Dave Jones:** And it's not got huge output current capability, just you know, 16 mA typical. Doesn't give you like an upper one. Does it give you a maximum over here? No, it doesn't give you anything over here in the recommended uh operating conditions for the maximum.

**Dave Jones:** So, you know, but you know, tens of milliamps, something like that. Good enough to drive uh you know, a relay or a decent LED or something like that. Yeah, unfortunately ST is not going to tell you either.

**Dave Jones:** Um yeah, it's like it's it's practically yeah, it's identical. They don't give you a maximum uh value for your sync current for for your uh comparator, but you know, so yeah, it's it's got your reference uh you know, your adjustable reference like this.

**Dave Jones:** Oh, application note. There you go, a battery charger using the TSM102. So, um yeah, like TSM102, like there would be a voltage uh reference that you might use. And then, right?

**Dave Jones:** So you're using the internal voltage reference, hence the pin numbers there, 9, 8, and a 13. You've got your adjustable um output uh you know, divider here to set your reference voltage, and then a um series pass transistor in here to give you, right?

**Dave Jones:** A a like a high current precision reference supply like that. So that's not too shabby. So, they've got, you know, an application circuit for a battery charger here, for example, but you can use this thing for like all sorts of stuff.

**Dave Jones:** When you've got dual comparator, dual op amp, and a adjustable shunt reference in there. So, I reckon that's a very nice little bonus part there, well worth having in your kit.

**Dave Jones:** Anyway, I hope you enjoyed the comparators. I know that's been long, and there's Leave it in the comments down below. I know I left out your favorite comparator. Everyone will have their five Oh, I use these little dual CMOS jobbies, and it's the duck's guts, and yep, leave it in the comments down below.

**Dave Jones:** I know there's thousands of them. So, yeah, just calm down, calm down. I know we haven't even scratched the surface of comparators. What, a 4,539? Like there wouldn't be There'd be more op amps, I guess, than there would be comparators, but yeah, anyway, yeah, there's just an absolute ton of them.

**Dave Jones:** So, anyway, I hope you found that comparatively interesting. I'm here all week. If you didn't find it useful, give it a big thumbs up. As always, discuss down below, and please tell us your favorite like jelly did it like there's probably other jelly bean out ones out there, but you know, the ones I covered were pretty much the jelly bean, but if you've got a good one that's available from like at

**Dave Jones:** least like three or four different manufacturers, for example, then that could be considered jelly bean, but also jelly bean in price and availability as well. Leave your favorite one down below.

**Dave Jones:** Catch you next time.
