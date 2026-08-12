---
video_id: DJ2nzvX2gBc
title: EEVblog #718 - Keithley 2400 SMU Teardown
url: https://www.youtube.com/watch?v=DJ2nzvX2gBc
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 30, "3": 41, "4": 53, "5": 64, "6": 75, "7": 97, "8": 106, "9": 121, "10": 138, "11": 155, "12": 169, "13": 179, "14": 190, "15": 207, "16": 226, "17": 234, "18": 245, "19": 256, "20": 269, "21": 286, "22": 298, "23": 315, "24": 330, "25": 343, "26": 356, "27": 369, "28": 380, "29": 389, "30": 407, "31": 424, "32": 440, "33": 455, "34": 467, "35": 488, "36": 498, "37": 506, "38": 525, "39": 538, "40": 554, "41": 565, "42": 581, "43": 591, "44": 597, "45": 607, "46": 624, "47": 634, "48": 648, "49": 656, "50": 668, "51": 684, "52": 703, "53": 714, "54": 727, "55": 738, "56": 750, "57": 759, "58": 776, "59": 784, "60": 802, "61": 818, "62": 834, "63": 845, "64": 866, "65": 883, "66": 891, "67": 905, "68": 922, "69": 941, "70": 954, "71": 966, "72": 994, "73": 1002, "74": 1026, "75": 1042, "76": 1055, "77": 1072, "78": 1083, "79": 1104, "80": 1119, "81": 1134, "82": 1148, "83": 1173, "84": 1185, "85": 1200, "86": 1214, "87": 1227, "88": 1247, "89": 1267, "90": 1283, "91": 1308, "92": 1319, "93": 1338, "94": 1351, "95": 1366, "96": 1389, "97": 1406, "98": 1417, "99": 1428, "100": 1437, "101": 1449, "102": 1468, "103": 1477, "104": 1489, "105": 1499, "106": 1509, "107": 1525, "108": 1536, "109": 1549, "110": 1558, "111": 1571, "112": 1588, "113": 1604, "114": 1620, "115": 1630, "116": 1641, "117": 1657, "118": 1668, "119": 1679, "120": 1691, "121": 1704, "122": 1715, "123": 1727, "124": 1738, "125": 1752, "126": 1762, "127": 1777}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. I've had this one sitting around for quite some time. This is the Keithley 2400 SMU or shmoo source measure unit. And you've seen source measure units on the blog before, so I won't go through all the details.

**Dave Jones:** Um, but this is pretty much the industry standard source measure unit, or it was because it's been superseded by the new wiz bang fancy touchscreen 2500 model. So, anyway, this is still a really great bit of kit.

**Dave Jones:** Um, if you can pick one up at a reasonable price, but they do hold their value very, very well. And if it's a point 01% class instrument, five and a half digits.

**Dave Jones:** Um, this particular model, the 2400, there are others in the 2400 series, but this is like the general purpose one. So, it goes up to 200 volts output voltage or thereabouts and one amp.

**Dave Jones:** So, it has sort of has that general purpose capabilities. Other models which have higher current capability, higher voltage, all that sort of jazz. And these things do exactly what their name implies.

**Dave Jones:** A source measure unit. They can source both current and voltage and they can measure current and voltage as well. They're generally used for semiconductor characterization and things like that.

**Dave Jones:** So, if you want to get the like like a modern replacement for a traditional curve tracer, for example, you would have got back in the old days, which can draw your semiconductor characteristic curve of your transistor, your diode junctions, or your um, you know, your TVS devices and a diodes, whatever it is, these things will pretty much test it.

**Dave Jones:** They're designed basically to be automated with PCs and things like that, but they're really precision bits of kit. They really are. So, I expect some really nice precision parts in this.

**Dave Jones:** I expect it to be very, very well made. It is a very expensive instrument. They sell for many, many thousands of dollars. Like the brand new 2400 one is like I don't know $4,000 or something like that.

**Dave Jones:** It's got front and rear terminals GPIB RS232 interface none of that newfangled ethernet rubbish. This model dates back quite some time. Some nice heat sinking on the side of course because this is I think it's 100 watts output capability on it.

**Dave Jones:** So yeah, we need some heat sinking on the side. So you know what we say here on the EVBlog don't turn it on take it apart. And these are four quadrant devices and I probably been meaning to do a video on that and that basically means that it can source and sink current as well.

**Dave Jones:** So you can actually so you could use them as a load effectively. So let's try and get this case off here. We probably need some more stuff on the bottom but I reckon that's going to slide off there.

**Dave Jones:** Should slide over the heat sink like that. The warranty void if removed sticker is already broken on this one. I got this at a auction quite some time back.

**Dave Jones:** I'll link in the auction video down below. I got it with a whole ton of other stuff. So oops oops we're coming apart. We're coming apart. Tada! Look at this.

**Dave Jones:** It's um Looks very very nice. Let's come on. You can do it. No, what's going on here? Haha we're in like Flynn. Check it out. Doesn't that look nice?

**Dave Jones:** And surprisingly I think I'm quite spread out. The reason I say that is because look here's the front panel terminals over here. These will no doubt be low thermal tellurium copper contacts same with the ones at the back as well.

**Dave Jones:** You know spared no expense on the terminals cuz this thing does have full scale current range of one microamp. So you know, and 5 and 1/2 digits resolution on that.

**Dave Jones:** So, I think it goes down to, you know, 10 nanoamps or something like that resolution. So, it's, you know, so we're talking very low current in here. Not as low current as the new model, by the way.

**Dave Jones:** The 2450 goes um an order or two lower than that, I think. But anyway, check this out, though. This is the interesting part. We've got our wiring coming over here.

**Dave Jones:** We've got some relays down in there, as you can see. We'll take a look at those in a minute. But basically, here is our output terminal, right? And here are our output driver transistors right all the way on the other side here.

**Dave Jones:** And I can show you the the basic general schematic of this in a minute. But yeah, it's just like these are our These are our output driver transistors. Looks like down here is our output current shunt, by the looks of it, where it's doing some measurement.

**Dave Jones:** That's by the looks of things, anyway. We've got a main control over here, which is not the main digital processor, I don't think, cuz there's a second board right down under this, which has all the digital processing and stuff like that, I believe.

**Dave Jones:** But yeah, so that's some sort of maybe, you know, custom ASIC or something like that. Some sort of, you know, the the high-end converter and DAC, for example. So, it's I just find it interesting that's whole completely spread out like this.

**Dave Jones:** We've got our high-voltage driver here driving the transistors. I'll show you that in a minute with the different taps. We've got some isolation slots along here. Just some short ones actually cut into there, just to differentiate the output driver around here with the rest of it.

**Dave Jones:** But yeah, so it somehow has to get from here over to here and vice versa. Right across the other side of the board. Interesting. Now, of course, this is a top-shelf unit, top specs.

**Dave Jones:** You won't be find any corners cut in this thing in terms of devices used. So, we'll get, you know, analog top-end analog devices parts, linear tech parts, things like that.

**Dave Jones:** So, yeah, it's, you know, really precision op-amps and they'll be precision current shunt resistors, precision range set resistors, all that sort of jazz, you know, and the capacitors will be top class, everything else.

**Dave Jones:** So, that's what you expect from a top-shelf Kii Three model. And there's the rear panel jacks. And as I said, if they're not low thermal tellurium copper, I'll eat my hat, I think.

**Dave Jones:** And we've got that going through a choke here and they're headed all the way down to a couple of relays down in here. We've got some NECs and a Coto.

**Dave Jones:** Exactly the same for the front panel terminals here as well. And no surprises for finding a super high quality Coto 8200 series read relay in there. Couple of NEC jobs, they make terrific relays as well, but it looks like that's a they're probably the high current read relay, so they're using that for the main output switching.

**Dave Jones:** USA, USA, USA. Now, here's a simplified schematic from the service manual, which I'll link in down below, of the output stage here. So, we don't actually have to take off these little seal pads against these transistors to, you know, find out exactly what they are.

**Dave Jones:** We've got MOSFETs. Basically, there's going to be four MOSFETs in there and two power transistors as well. So, that's why we've got 2 4 6 devices on the upper half and 6 devices on the lower half here.

**Dave Jones:** And of course, as I said before, this is a four-quadrant device, so it's able to source current as well as sync. So, we've got our main 225-V supply rail up here and then of course, it's able to source current out like this.

**Dave Jones:** So, but it's also able to sync through these transistors down to -225 V as well. It's supposed to be a negative down there. And you'll notice that these are plus 36 volt plus or minus 36 volt taps.

**Dave Jones:** What are they for? Well, on lower ranges, you don't want to dissipate all the power up here. If you only had your 225 volt rail, if you were down on the lower ranges generating, you know, a 10 volts or 5 volts or 1 volts or whatever, you're going to be dissipating a huge amount of power across your power transistor output stage here.

**Dave Jones:** So, you want to what? Tap in these lower voltages here. So, I think they've got a 20 volt range or a something like that. So, that's what those two taps will be there for.

**Dave Jones:** We've got ourselves a driving amplifier here. Whether or not that's a discrete amplifier, I don't know. You'd have to have a look in there. Could be a transistor amplifier.

**Dave Jones:** Who knows? But anyway, interesting thing is is that they've got a a cascode arrangement here. So, these two transistors Q516 and Q518 here are a cascode configuration. You can tell because we've got ourselves a basically a common emitter and then a common base uh joined together configuration.

**Dave Jones:** And they do that for the extra output stability. The cascoded transistor arrangement with their sort of I guess you could call it a hybrid uh arrangement because they got the bipolar transistor and the MOSFET as well.

**Dave Jones:** But hey, you can do that. You know, a transistor's a transistor. So, that really gains them output stability. The cascode arrangement is really known for its stability. And of course, what you need in this sort of device, really high-end, really no low noise, really ultra stable.

**Dave Jones:** You really need a um stable output driver arrangement. And of course, you could go into a ton of detail about exactly how this works until the cows come home, but I'll spare you the details.

**Dave Jones:** But uh yeah, suffice it to say that pretty much matches the physical arrangement here of the um output stage. And you You as a PCB layout person, when you're actually laying out this product, of course you'd have the designer design this thing.

**Dave Jones:** It's usually on a high-end product like this. It's not going to be the same person, typically. Um so, yeah, they've designed the output stage and you go, "Right, I'm going to do an output stage and I need to hook it up to a heat sink.

**Dave Jones:** It's got to be on the side here, of course." So, and I'm going to physically arrange all of my transistors like that because it that's how it routes out.

**Dave Jones:** I don't know whether or not that's positive here and negative here or vice versa. Um I'm assuming that the positive is on this side. But, hey, you get the gist of it.

**Dave Jones:** And here's our high voltage um uh transformer up here generator presumably uh to generate the uh high voltages required for the 220 plus minus 225 V. And the capacitors here, we've got a combination of uh 100 V Nichicon here.

**Dave Jones:** Of course, you get top quality brand caps in this. So, they're 100 V Nichicons for the uh lower rails. And then we've got uh four I think 400 V um or 350 V uh caps up here.

**Dave Jones:** These are um IC brand Illinois uh capacitor. Uh we're they've been acquired by uh Cornell uh Dubilier. So, you know, once again, super high quality uh caps in there.

**Dave Jones:** So, they're for the higher voltage uh rails. You notice the big high voltage uh ceramic ones in there as well. So, yes, looks like we've got a couple of those for each rail.

**Dave Jones:** So, you'd have the likely the positive rail, the uh ground, and then the output, uh and then the negative rail as well. And there you go. If you've never seen the uh Illinois capacitor symbol, I see in there.

**Dave Jones:** I mean, this is a 13-year-old 12-year-old unit. This was manufactured in November 2003. So, since then they've been acquired. But, yep, world-class caps. And there we go. That's uh likely our buffer driver analog devices AD847.

**Dave Jones:** As always, I'll link in the data sheets down below. Now, um this is an interesting they've got it in a DIP 8 arrangement. And there's a couple of dip eights on this board and you'll notice that primarily like you know almost all of this is all surface mount construction but why have they chosen a dip eight there?

**Dave Jones:** Well, it was the right device for the job. It had the right specs they needed and it was almost certainly only available in a dip eight package well, at the time anyway.

**Dave Jones:** So, they used it. They didn't worry about that sort of thing. No compromises. It's the device the designer wanted. So, whatever it came in that's what they used and you can see that a few times around here as well.

**Dave Jones:** We've got ourselves some amp 03s. There's a couple of those and of course you'll get them on the opto couplers as well. But yeah, there's a couple of amplifiers in there that just buck at that SMD trend there.

**Dave Jones:** And of course that shows really good design intent because the designer goes, "No, screw you manufacturing. I don't care if that dip part's going to be a problem for you.

**Dave Jones:** That's the part we need. This is a high-end market leading precision product. Use that damn part. No substitutes. Thank you very much." And there's quite a few of these spread throughout the board.

**Dave Jones:** These are NAIS top brand of course solid state photo MOS relays AQV214s. So, what is this puppy under here? My guess is some sort of custom part hence you know, they've got the model on there and they've got some sort of code after that.

**Dave Jones:** So, I might just lift the skirt on that and have a look. Running at 12 megahertz. Whatever it is. Well, that's pretty surprising and a Tira Max old school EPM 7000 series PLD.

**Dave Jones:** Not even FPGA. We've got a digital beast under there. I expected some sort of analog magic being from Keithley but no, obviously they're doing that to drive the nearby looks like we have a couple of DACs here.

**Dave Jones:** So, yeah and maybe something else down here. Anyway, that could be Yeah, just some generic glue logic to drive the various DACs and ADCs required. And yeah, on the upper side of this, we have a couple of serial input DACs.

**Dave Jones:** These are Analog Devices 7849 16-bit multiplying DAC. Not a bad DAC at all. Typically typical of what you'd find in such a bit of kit. And next to that, we have a couple of precision op-amp see Linear Tech 11112 up here.

**Dave Jones:** That's a That's a really nice picoamp input level op-amp. The one The 1097's a bit more jelly bean, but I don't see a voltage reference next to those offhand.

**Dave Jones:** So, there's probably going to be one common voltage reference for this whole whole unit, I think, for the various ADCs and DACs, I suspect. And of course, on something like this, high-voltage, high-current precision unit, you're going to have everything optically isolated, all this entire analog board optically isolated from the digital board down in here.

**Dave Jones:** So, that's why we've got our opto-isolators here. This cable goes down, as I said, the lower digital processing board down there. And the CPLD would handle some of that comms as well between that board and then just fanning that out to the various ADCs and DACs and everything else.

**Dave Jones:** So, not a huge amount going on in there, but yeah, it's You've got to have some sort of smarts on the other end of this cuz there's too much going on on this analog board.

**Dave Jones:** So, that's just It takes care of all the housekeeping here. All right, here we go. Let's have a pan around the board with our Takano microscope, shall we? And we can get reasonably good detail, see all the chips and everything.

**Dave Jones:** So, everything's hunky-dory. So, let's have a look around here. And what I'm specifically looking for is the voltage reference. Now, I found a Vref test point here, but look, it's a Linear technology 1097 with linear technology 1007.

**Dave Jones:** These are just all op-amps. We've got a TI 7705, that's a voltage supervisor, some 74HC logic, a DG 4 400 series marks. We've got a max 326, there's nothing special happening here at all.

**Dave Jones:** Got some more 74HC discrete stuff all around there. We've got another amp 03 up there measuring across a current shunt and most likely maybe that's the input there, is it?

**Dave Jones:** I don't know, coming from somewhere. I don't think that our precision current shunt resistors are around there. More DG series maxes, they've got those everywhere. We've got some precision resistors there.

**Dave Jones:** I don't know who they're from offhand, but OP 282s and tons of different types of op-amps. Look, AD 797s, 1124s. What have we got? Classic AD 712s there. Just, you know, fairly jelly bean OP 282s, AD 711, which is the single version of the 712 there.

**Dave Jones:** Goodness, that that that looks weird. On the camera, it looks like like there's two holes burned in the chip, but there's not. That's just a shadow coming from the light.

**Dave Jones:** You can see it down here as well on the on the Tagarno microscope. So, some LM339s and but so a whole bunch of op-amps everywhere. A whole bunch of sort 23s everywhere, but these are all op-amps and I please scream at me if you can see the voltage reference on here.

**Dave Jones:** That puppy looks unusual, but it's an R, so that is a resistor network by the looks of it. So, nothing fancy going on there. There's the um, 16-bit DACs we were talking about before.

**Dave Jones:** Um, marks we've got some op-amps near there. Curiously, we've got a 74F series fast series uh, TTL. Oh, really old school. So, I don't know when this design dates from, but uh, yeah.

**Dave Jones:** To put a 74F in there, wow, that's that's really something. Um, uh, that has got R next to it, so I presume that's another resistor network. Um, more OP177711s, um, 5534 op-amp.

**Dave Jones:** Gee, so they're mixing it up. LM311 comparator. Um, and well, I don't know, scream at me if you can see the voltage reference cuz I haven't damn well seen it yet.

**Dave Jones:** And uh, there's lots of test points all around, of course, and uh, that Vref has got to be doing something. There's an AD um, uh, presumably um, AD converter test point, but uh, once again, I haven't actually found any analog to digital uh, converters or a reference.

**Dave Jones:** Unbelievable. If we go down here to the relays down here, there's nothing much doing down there as well. Anyway, here is our Oops, just hit my microphone. We've got ourselves some Dale uh, precision shunt resistors down in here.

**Dave Jones:** They got those in a series parallel uh, combination there. Got some back-to-back diodes happening. And uh, got an optocoupler there. And but uh, there's a couple of more of those um, NAIS um, MOS relays in there.

**Dave Jones:** So, this is this would be our main output current shunt resistor because it's quite near the output here. It's near all the There's a a um, output uh, filter inductor and there's our looks like our main output switching relay, the Coto one.

**Dave Jones:** Here's all our wires going off, so presumably that's got to be the main output current sense resistor. So, that somehow has to presumably get back into the amp 03 over here cuz that's our uh that's all this one over here cuz they're our two closest uh uh differential amps for measuring that uh current shunt.

**Dave Jones:** But, jeez, I mean, got some MOSFETs down here. But, uh man, where is the voltage reference? I don't know. I must be blind. Looks like we've got ourselves some uh precision polystyrene caps there.

**Dave Jones:** They'd be using those for uh stability. Got a couple of more precision resistors tucked away down in there by the looks of it. Looks like we've got ourselves a big-ass uh precision resistor 2 meg up there.

**Dave Jones:** So, that's doing some uh high-range um shunt stuff, presumably. I don't think it's just there for uh protection, but hey, you know, when it's 2 meg and you use one that size, I you know, is it a high-voltage one?

**Dave Jones:** But, uh there's our output uh stage for those who wanted to see the output stage. The light isn't the best on this Tagarno microscope when you're just using it for uh you know, when you're using it for high components.

**Dave Jones:** Only got the one light at an angle. Anyway, I'm still not coming close to an ADC or a voltage reference. Unbelievable. And if you're wondering what that CAL STD 5400 is there, that's a high-speed uh MOS quad fit analog switch array.

**Dave Jones:** So, yeah, that makes sense. That's all uh fine and dandy. Now, based on the fact that I can't find a uh dedicated ADC chip in here, and of course the um precision uh high-end performance of this thing, that's it's a five and a half digit uh converter in the thing.

**Dave Jones:** It must be, by deduction, absolutely must be, I have no doubt, implemented in the Arturia Max POD. They're doing a multi-slope uh conversion in there, similar to uh other high-end uh multimeters we've seen before.

**Dave Jones:** So, yep, um some sort of um you know, charge balancing um variation of a dual-slope uh converter or multi-slope uh converter. It won't be just a dual-slope, sorry. So, and that is yep, that's exactly what they must be doing there, but I still don't know where the voltage reference is uh coming from.

**Dave Jones:** Um I might be able to power it up and measure that, perhaps, but I still don't see the voltage reference. But uh yeah, that's what they're implementing the POD in there and uh talking to the ADC over there.

**Dave Jones:** So, um obviously it must do some uh there must be some other interfaces uh coming from the microcontroller to do all the range um switching and other miscellaneous uh housekeeping stuff, but that one that So, that could be done somewhere else, but that that could actually be dedicated just to the ADC itself.

**Dave Jones:** So, sorry to all you uh volt nuts out there. Uh for the life of me, I can't find the actual voltage reference uh used for the multi-slope uh converter in here.

**Dave Jones:** Could be one of the SOIC-23 packages, could be a a precision uh buried Zener reference uh for example, something like that, perhaps. Hmm. Well, there very well may not even be a specific voltage reference in here.

**Dave Jones:** It may be that the uh that the rails are, you know, ultra-low noise, ultra-low drift uh voltage rails, for example, and everything uh is referenced from that, perhaps, because um of course, you don't need an absolute uh reference in there like an absolute precise value reference like 2.50000 volts.

**Dave Jones:** I mean as long as you've got a power supply that is stable i.e. you know, however many ppm drift this thing is or ppm reference you know, 5 ppm, 10 ppm or whatever it is, then as long as your power supply doesn't drift, then well you can use those as your voltage reference.

**Dave Jones:** So maybe that's what's going on here, but I don't know. I'd need the uh specific uh schematic to figure that out. And sure enough it pays to read the service manual.

**Dave Jones:** It turns out that uh the PLD here is the ADC as I suspected. It's the uh control element for that and yes, it is a charge balancing multi slope uh converter.

**Dave Jones:** That's the only way to get the uh performance you expect out of uh an instrument of this class. And no, there are no uh parts on the bottom of the board.

**Dave Jones:** I've had a look in there. Um, down the bottom here we've got ourselves the uh digital control board. Um, it's not worth taking apart to look at. It's just a um 68 uh 332 micro uh controller with driving some GPIB.

**Dave Jones:** Nothing uh fancy whatsoever. Deep down inside there is the uh power supply. So there's switching power supply down in there. There's a metal shield uh separating them all. It would be I think quite a pain in the ass to uh take this sucker apart.

**Dave Jones:** I'd have to take out all the uh heat sink components and lift everything out. No, it's looking really messy. So sorry, I don't think I'm going to go any further with that uh today.

**Dave Jones:** Nothing interesting in a switching power supply and just a um a dumb ass micro uh controller board. All the interesting stuff we want to see is of course on the top which we've taken a look at.

**Dave Jones:** And there really is a lot of analog goodness going on in here. It is actually quite complex. If you've got the schematic, um yeah, I I don't know. You may not be able to make heads or tails of it.

**Dave Jones:** It is a quite a complex measurement system and range switching, of course. It goes from anywhere from, you know, 500 V down to millivolts and 1 amp down to 1 microamp.

**Dave Jones:** So, it scales, you know, quite a significant range there. And the output drivers, that's an art in itself. All the output stage there, the multi-slope conversion, which Keithley no doubt have a patent on that.

**Dave Jones:** Agilent have got their own system, as we saw in the 34116A multimeter, and so forth. And yeah, they all have their particular flavor of implementation. But that is really quite a nice design.

**Dave Jones:** It's, you know, impossible to fault that. There's no bodges on it. But it is a very well-proven design over decades, really. So, I mean, this one was manufactured in 2003, but I think it even predates that.

**Dave Jones:** I think it came out before that. And it really is quite a nice example. As I've said of the design-driven aspect to this. It's not driven by anyone else.

**Dave Jones:** It's driven by the design side of things, the engineers who actually designed it to meet the really awesome performance specs of this thing. And they said, "Yeah, we must use that device.

**Dave Jones:** We must use that. Must use that." Available in DIP? Doesn't matter. All the different types of op-amps and switches on this. It's not like they've gone in there, "Oh, yeah, we're just using an Oppo 7 for everything, you know?" No, they've it's chosen very specific parts for very specific purposes.

**Dave Jones:** On both like the high-voltage side of things over here, you're going to use high-voltage muxes, the two precision current shunt differential amplifiers. And I'm sure if you looked in the type of precision resistors they've used in here, the polystyrene caps, for example.

**Dave Jones:** And they've chosen these parts very specifically to get the best performance uh possible or the performance that they wanted anyway out of this thing. It's not, you know, absolute world best uh performance, but yeah, these are a really nice accurate bit of kit.

**Dave Jones:** And I mentioned right back at the start, here's our IO terminals over here. Our wiring to those. And now output stage is right at the back here. How are they getting it across?

**Dave Jones:** Well, I think they're it's different it's differentiated by the cutouts, those little slots in there. There's our high voltage driver over here. Here's our output stage. It comes around.

**Dave Jones:** We've got some high voltage muxes over here. We've got the big the big two mega precision resistor over there for high voltage. And that's coming down here. And I think that's coming through this stage, which is where our output current shunt resistor is.

**Dave Jones:** And then it's going directly to our switched output terminals there. So, I think that's the that's the general flow of things. And here's our block diagram. We've got our voltage deck and our current deck over here.

**Dave Jones:** These are the two decks that we would have seen over here, no doubt. And then we've got our voltage and current clamping where that's actually happening in here, I'm not sure.

**Dave Jones:** But we've got some error amplification. And then our high voltage output stage, which we're seeing well, switched high end volt and low voltage output stage. And then we've got our sense resistors that, as I said, I think flows around here.

**Dave Jones:** So, we've got our current limits and our limiting stuff's probably over here somewhere. And then flows around here to our output um sense our output sense resistors there, which is down there.

**Dave Jones:** And Bob's your uncle. We've got some feedback and stuff like that, all sorts of muxing. Got some overload protection and stuff like that. But um that's about all she wrote.

**Dave Jones:** It's I'd love to see a more detailed block diagram of that and the schematic. So, if anyone does have the schematics for this thing, if it is available online, uh, please leave it in the comments.

**Dave Jones:** Yeah, anyway, it is quite a nice design. I hope you enjoyed that look inside a Keithley 2400 source measure unit. Very high-end bit of kit, and if you can pick up one of these, um, I highly recommend it.

**Dave Jones:** There's nothing like having an SMU, um, for doing, uh, characterization of, basically, um, almost any type of, uh, component you can think of. They're absolutely fantastic, uh, devices. And, yeah, I've done, uh, separate videos on that.

**Dave Jones:** I'll have to try and um link them in if possible. As always, uh, high-res teardown photos of this, uh, mainly just the board, really, cuz I didn't tear down the rest of it.

**Dave Jones:** Mm, sorry. Um, but, yeah, high-res teardown photos available on evblog.com. The link to that is down below somewhere or up above, depending on where you're reading this. And, as always, if you liked it, please give it a big thumbs-up.

**Dave Jones:** And if you want to discuss it, jump on over to the EVblog forum. Link is down below, as well. Catch you next time.
