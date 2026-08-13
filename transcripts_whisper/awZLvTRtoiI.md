---
video_id: awZLvTRtoiI
title: EEVblog #810 - Micsig MS310 Handheld Oscilloscope Teardown
url: https://www.youtube.com/watch?v=awZLvTRtoiI
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 24, "2": 40, "3": 56, "4": 76, "5": 97, "6": 117, "7": 137, "8": 157, "9": 174, "10": 186, "11": 202, "12": 214, "13": 234, "14": 250, "15": 271, "16": 295, "17": 315, "18": 331, "19": 352, "20": 372, "21": 384, "22": 408, "23": 425, "24": 441, "25": 465, "26": 481, "27": 502, "28": 518, "29": 534, "30": 559, "31": 584, "32": 604, "33": 620, "34": 640, "35": 656, "36": 672, "37": 689, "38": 709, "39": 729, "40": 745, "41": 765, "42": 781, "43": 793, "44": 810, "45": 830, "46": 850, "47": 870, "48": 886, "49": 907, "50": 923, "51": 939, "52": 964, "53": 980, "54": 1001, "55": 1013, "56": 1033, "57": 1049, "58": 1061, "59": 1081, "60": 1102, "61": 1122, "62": 1138, "63": 1154, "64": 1179, "65": 1195, "66": 1215, "67": 1235, "68": 1251, "69": 1268, "70": 1288, "71": 1304, "72": 1324, "73": 1345, "74": 1369, "75": 1385, "76": 1401, "77": 1417, "78": 1438, "79": 1462, "80": 1482, "81": 1502, "82": 1530, "83": 1551, "84": 1567, "85": 1583, "86": 1607, "87": 1628, "88": 1648, "89": 1664, "90": 1684, "91": 1709, "92": 1733, "93": 1749, "94": 1769, "95": 1781, "96": 1798, "97": 1822, "98": 1846, "99": 1863, "100": 1875}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Today we're going to take a look at this lovely MICSIG MS310IT 100 MHz, one gig sample per second, handheld multifunctional. Multifunctional? Instead of multifunction, multifunctional. Okay. Multifunctional oscilloscope. And if you don't know about MICSIG, they're an up-and-coming Chinese manufacturer

**Dave Jones:** but they're trying to shoot for the high-end stuff, and this is you know, a reasonably high-end handheld scope. There's a $5,000 model of this. This one's about $1,400 street price, which is really good value for a supposedly, really, it feels like a brick dunny.

**Dave Jones:** It is built really solid, feels like a quality bit of kit. And they're trying to compete against the Agilent. So the higher-end model of this is upwards, like $4,000 or something US, which is pretty much on par with you know, the Agilent and Fluke prices.

**Dave Jones:** And of course the selling point of handheld scopes like this is this one is fully isolated between both channels, so these BNCs are not electrically connected. We can put a multimeter on there and prove it, and also the multimeter input as well, also

**Dave Jones:** electrically isolated from both of the channels. So they're all three independent channels at the BNC, 300 volts cat 3 rated, which is pretty darn good, and 600 volt cat 3 rated on the multimeter inputs, and they're all isolated. And let's prove it. So let's probe that, and we'll show you that they're

**Dave Jones:** genuinely isolated. Look at that. No worries whatsoever. That's what you need on a handheld scope, isolation. And of course to make them safe you also need the proper isolated probes as well, so they've got the full plastic shroud surrounding the BNC, so when you plug it in you can't accidentally touch that BNC.

**Dave Jones:** And also for the oscilloscope probe here itself, it's got this retractable clip here, so for the high frequency probe attachment here, so you can't accidentally touch any of that. So it's all fully isolated. Fantastic. These are quite reasonable, 100 megahertz bandwidth rated probes.

**Dave Jones:** And they're actually manufactured by Multicontact. There you go. UL listed as well, fantastic. So no wuckers there at all. And there's the specs for those playing along at home. Oh, where's the English ones? There we go. 16 path input capacitance compensation range. All standard,

**Dave Jones:** 0 to 250 megahertz. It says 100 megahertz on the probe. So that's strange, not sure what's going on there. And for those who have been wondering, where's David 2? There he is, over there. So yes, I'll have to do a separate review of this, and yes,

**Dave Jones:** I've been using it a bit, and yes, it is a very nice handheld scope. So if you're in your market for a quality isolated scope, it's worth a look. Now, let's have a look at the thing. One thing I don't like about the tilting

**Dave Jones:** bail on the back is usually like they put in like a little cutout there to get your finger under, but it's like you know, they've just got these little finger holds on the side here. to flip out the tilting bail, and you know, it's quite a decent

**Dave Jones:** wide tilting bail. I like it, but you just can't get the damn thing up. I hate it when you can't get your stand up. So anyway, you know what we say here on the AEV blog, don't turn it on, take it apart. With our Swiss tools.

**Dave Jones:** Well, actually I can't do that, because that's a Philips and they're Torx. Let's have a quick look at the battery. It's supposed to have a 4 to 5 hour operating time. 4 to 5 hour operational life, I haven't actually tested that. But let's get this puppy out of here.

**Dave Jones:** There we go, Mixig branded, 6000 milliamp hour. But you could, you know, repack that yourself, I'm assuming. Well, maybe not, it's, yeah, welded shut. But anyway, well, you can buy a new battery pack from Mixig if it ever dies. But yep, there we go.

**Dave Jones:** We've got ourselves, is that a warranty void? If not removed sticker? Okay, this is annoying. There's two other screws in here, and argh, I've got to sort of get right at an angle. Okay, well that's weird. These are different lengths. That one came out of there, and that one came out of there,

**Dave Jones:** and the other ones are also a different length again. Why? Here we go, and we're in like Flynn, right to the good stuff. Look at that! Oh, Altera Cyclone 3, woohoo! Alright, well this looks very nice. Look at how they've got this, and this is the main processor board, by the way,

**Dave Jones:** if you hadn't figured it out with the FPGA, and a Texas Instruments TMS 320, thank you very much, old school. Yeah, look at they've got the grounded vias right around the outside, just trying to stop the magic electrons from escaping and mucking up their EMI, but very little is going to escape

**Dave Jones:** out there. It's just, it's gilding the lily, you know. But anyway, it's nice, but look at it, you know, all ground vias everywhere around here. Anyway, got some DC to DC converters up here for, they're going to be for various rails. Got a TMS 320 processor,

**Dave Jones:** we've got a Altera Cyclone 3 FPGA, not particularly, you know, high-end, but good enough to do the job. This has got, this model I think has 60,000 waveform updates per second, whereas the highest end one has like 160 or something, or 200,000 waveform updates per second.

**Dave Jones:** Really quite a fast scope. And we've got ourselves an EP3 16F484, sort of like, you know, one of the mid-range type Cyclone 3 parts. We're looking at 15,000 logic elements, not a huge one. And 512K bits of internal SRAM. So they're clearly not using this

**Dave Jones:** as the sample memory, because this thing has 240K per channel, I think. I'm not sure if it halves or not, but yeah, 240K. So they obviously can't fit it all inside the Altera Cyclone, so there's going to be some memory next to it.

**Dave Jones:** And sure enough, right next to the FPGA, there's two of these puppies, pretty common as mud in these sorts of scopes, ISSI, 256K x 18-bit wide, 4 megabit, well you can actually choose different widths. 4 megabit SRAM, nice. SD RAM, rubbish, no. SRAM, thank you very much.

**Dave Jones:** Easy to drive with the FPGA, and super quick. And there's two of those. So yeah, this thing's got 240K sample memory, so they could at least double that. They could have 512K samples because there's only 8 bits per sample. Actually, is that the same?

**Dave Jones:** Looks like it is. They've actually got three of these, so I'm assuming that there's one per channel for the sample memory, and the other one, video memory would be my guess. And there's a good old-fashioned old-school TMS 320 in there for you 320 fanboys.

**Dave Jones:** I know there's a lot out there, and they're still as relevant today as they were I don't know, jeez, when did they first come out? Jeez, would it be 20 years? TMS 320, Dave's a fanboy. TMS 320, he's a fanboy. And this segment is brought to you by Texas Instruments.

**Dave Jones:** Tell us why you like the TI 320, TMS 320. Yeah, so I'm using it in the 3D printer board. It's superb for control stuff. It has, like, it can do, like, complex number maps, and like it has this, like... Hence its name, Digital Signal Processor, that's

**Dave Jones:** It's fantastic for control! Yeah, and it's got, what did they call it? A control-lore accelerator, I think they call it? Which sounds like a... Which means that you basically have, like, this kind of, like, micro-code engine type thing that runs in the background, and then you can use DMA, like, direct memory

**Dave Jones:** stuff, and transfer between data, and it's like you have absolutely no overhead on... On the actual processor itself. Yeah, yeah, yeah. So that just runs on the side. Yeah, yeah, so you can get ADC sampling, convert all those samples to real numbers, and

**Dave Jones:** put it into your main program, like, memory, with, like, just about no overhead. No processor overhead. Yeah. Apart from memory. Not all of the 320 parts would have that, though. No. You'd have to choose a specific one. Yeah, the TMS 320, I think it's F28069 is the one that I'm using at the moment.

**Dave Jones:** It's pretty high-end. How many variants would they have? 1,000? Yeah, it's... Yeah, yeah. I think it was 68, 60-something else, 62. Yeah. You're a fanboy! Yeah! Alright, 320 for the win! Woo! This one's actually a beast! Just like Dave said, this is the 6,000 series, the 6748.

**Dave Jones:** And it's 375 or 450 megahertz, but it's got, like, 3,500 MIPS. And, what, 2,700 megflops? So it's a real hunkin' beast. So, yeah, they didn't skimp there. That thing's haulin' ass. Got some external memory on there, too. And I thought that puppy was

**Dave Jones:** two little cells stacked there, but it's not. It's a SuperCAP 0.33 farads, for all you SuperCAP fanboys. Well, hello, sailor! This is our ADC from Intersil, the big eye on there. And the CAD 5510P. I hadn't seen this before. Dash 50. This is a

**Dave Jones:** 500 meg sample per second part, so obviously to get their banner spec of 1 gig sample per second, they must be interleaving both channels. I haven't even looked at the spec, but I'm sure if you do, it'll say that. But this puppy is not 8, it's not 9, but it's

**Dave Jones:** a 10-bit converter. Fan-freaking-tastic! Why have they got a 10-bit converter in there? That is brilliant! I wonder if they're, how they're making, how they're taking advantage of that. Are they actually sampling the full 10 bits, or are they just, you know, pissing away 2 bits?

**Dave Jones:** I don't know. Well, I just checked the specs for this thing, and sure enough, it says that it's an 8-bit converter. But these are clearly 10-bit converters in here, so maybe they're using them for the extra performance, and just tossing away the 2 bits.

**Dave Jones:** But that seems a shame. You could do some nice boxcar averaging with that, but I don't even think this scope actually has any form of, you know, high-resolution type mode. A real shame, especially, like I know you can't see it on the screen,

**Dave Jones:** but it's good for math stuff, and also if you want to capture the data and export it, then, you know, it's fantastic for that too. So I'm not sure what's going on there. Wow! They've spared no expense, that's for sure. Oh, and by the way,

**Dave Jones:** our TMS320 processor also has an LCD driver, so it can probably easily drive the 640 by, what is it, 640 by 480 LCD screen in this thing? No wuckers. And this is rather interesting. Here's our two InterCell ADCs here, but we've got one little micro coax coming up here.

**Dave Jones:** Like, I thought, okay, if they're going, you know, this top board is the ADC plus the processor board, you know, there it is, like hooked right into the ADC, hooked right into the Altera FPGA sampling subsystem there, but like, yeah, I would have expected two cables to

**Dave Jones:** come over. But anyway, we've got some headers here which connect the top and bottom boards, so our bottom boards must just be the front end preamp and isolation, and that's pretty much it. But interestingly, note these little ground strips along here, and they've

**Dave Jones:** gold-plated those because, well, just left the solder mask off, the whole board is gold-plated of course. And so they're, you know, designating that as something special. Is that the trigger stuff? And if you check out, they've got some slots here as well. It's almost as if that was designed to have

**Dave Jones:** a metal can over it, and they haven't populated it. Yeah, I'm pretty sure that's what they intended there, but nope, they haven't done it. And here's something you don't see every day. There's an 8051 processor flash base, presumably that's what the F stands for.

**Dave Jones:** I haven't looked up the data sheet, but that is right next to this ribbon cable which goes off. That would be the front panel. Keyboard controller would be my guess, and they've implemented that in their own little micro. Okay, nothing wrong with that.

**Dave Jones:** So that's actually really smart, and they've, you know, spared no expense, gilded the lily there. They went, oh well, we don't want to have to do that in our TMS320 processor, we don't want the extra little overhead of handling and scanning the keyboard,

**Dave Jones:** bugger that, let's just separate that out into a micro and then this little 8051 micro can then interrupt the TMS320 processor when you actually press the key and want to actually do something, so there's more grunt there to update your screen. And that puppy there, it presumably like

**Dave Jones:** sort of, you know, one side is presumably the output side of this thing. That's an analog device's 4857, or ADA 4857, and that's an 800 meg bandwidth voltage feedback op-amp. And the rest of the stuff in here is just all jellybean, you know, 4052s and

**Dave Jones:** nothing special, nothing much doing in there at all. 4051, MUX, hmm. And no surprises for finding this right here, this is a Texas Instruments CDCM61002VCO, designed to take our little oscillator there, there it is, not sure who's making that one, but is that a 10 megahertz reference?

**Dave Jones:** Can't read, no, 26 megahertz, there you go. And that's actually got two clock outputs which can drive the two ADCs there. No wuckers. Nice part, that one. You know how I was confused with only one micro coax coming up here? I actually found the other one.

**Dave Jones:** It's over here wedged in between these DC to DC converters here, so what the? That's got BB on there, don't know if it's Burr Brown or not, doesn't look like the original Burr Brown type symbol. It is, it's a Burr Brown part. There you go, Dave's nodding.

**Dave Jones:** David, sorry. DAC 7614, that's a quad voltage output 12-bit DAC, so they'd be using those for all the offset stuff. Well, really impressed with this puppy so far, they're really gilding the lily on here. Let's pop this top ADC and processor board off.

**Dave Jones:** A couple of flat flexes here, this would be going down to the LCD, as I said, this one over here going off to the touch, the keypad membrane on the front, so four screws it looks like, and get rid of those micro coaxes, they'll go out through the little holes in the board.

**Dave Jones:** Should just pop off and we'll have our three isolated channels. Let's have a squiz at those. So we've got our board-to-board headers, they're only like 0.1 inch, they're not like high frequency headers of course, so I believe that's why our two coaxes, surely that would be our two channels.

**Dave Jones:** Ta-da! We're in. But you know, I guess they had to, they probably, you know, they had to have it coming off, because here it is over here, you know, channels, one channel's over here, one channel's over here, so they had to put it in over here, but it's, you know, smack right in the middle

**Dave Jones:** of the DC-to-DC converters. You know, if I was the layout guy for this board, and you know, and the designer came across and said, we want this, you know, analog, you know, analog coax connector right there, smack in the middle of the DC-to-DC converters, I'd be going, can't do that, can't do that,

**Dave Jones:** oh, I'm going to need extra layers on my board to run it through an internal channel, so it's you know, avoids any switching noise and stuff like that, but I'm sure they've done their homework on that. You know, it's not insurmountable, it's just, you know, not ideally done, that's all.

**Dave Jones:** And for those wondering about the back of the board, yes it is double-sided load, but not much doing there, just all for your requisite bypass caps for the BGA. There's no real avoiding that. When you've got a BGA FPGA like that, you can't just whack your caps around the outside, you don't get the

**Dave Jones:** performance, your loop areas are terrible, which diminishes the effectiveness of your bypass capacitors, so yep, they've got to go right on the pins, right in the bottom. So, you know, that's the penalty you pay when you go for a BGA FPGA like that, you're instantly whacked

**Dave Jones:** for the extra cost of a double-sided load. This is all rather very nice, our little plate here comes off with our USB here, and we've got a rotary encoder wheel, that just pops out, they've greased that up, you've got to grease your wheels.

**Dave Jones:** And we can, two screws on here, we should be able to lift this whole board out, but yeah, we've got ourselves a shielding plate, some relays sticking out. Oh no, they're not relays, I think they're DC to DC isolator blocks, perhaps. So there we go,

**Dave Jones:** that's just going to pop out of there, like that. No whackers, we've got a couple of spacers which came out, but weehee! We're in like Flynn. OK, this is kind of a what the? Look at this, there's an unsoldered pin there, and it's actually still inside the socket

**Dave Jones:** there. It's actually pulled through, so I don't know what the deal is there, what the? So apart from that bizarre pin sticking out, I'm thoroughly impressed at every turn of the design of this thing. Here we go, very nice. Look at our isolation slots

**Dave Jones:** in here between our channels, no worries whatsoever. So that's our analog section, these are our, sorry, our multimeter section and our two scope front ends. Once again, it looks like they might have just, you know, they've done, well, the shielded can on the top, so they've

**Dave Jones:** you know, they're completely shielding that, they've got the individual stitched vias down there, so you know, they're forming one complete ring and sort of can around that thing. And we'll lock the can off in a second, but yeah, it's really well laid out.

**Dave Jones:** We've got our isolation between our processor ground side and our multimeter input side, no problems at all. And as I guessed, those black bricks there, I haven't looked at the part numbers, but they're our DC to DC converters. Typical single-in-line 5-pin arrangement here, with the isolation

**Dave Jones:** slot down in there, you can see. So they're actually isolating the primary, so that'd be, you know, plus minus 5 volts in and sorry, 5 volts in from the digital side, and probably plus minus 5 volts out to power all of the analog section.

**Dave Jones:** Fully isolated. And they've done their isolation slots right. Very nice. And yep, I should have just looked, but I was right! AH0505, that indicates it's an 05, that's 5 volts in and 5 volts out, but because they've got 3 pins on the output, that'd be plus minus 5 volts, and it's

**Dave Jones:** Succeed brand, is it? Love it. 2 watts. Check out that! It's a Mark T2 transformer, but that looks like it's a common mode choke to me. There is a matching one up here, but it's got the top on it. So I'm not sure why the top has fallen off that one down there.

**Dave Jones:** There's nothing rattling around in the case, so I don't know, it must have been that way before they put it in. Anyway, they're common mode choking the input to the isolated DC to DC converter here, so that the crap doesn't, from the digital,

**Dave Jones:** doesn't make its way. Because these things aren't magic, these are switching converters and they're really, once again, gilding the lily there. I don't think I've ever seen somebody put a common mode choke on the input to that. Phew! And I was busy talking them up,

**Dave Jones:** and what do you know, I've got a genuine bodge resistor there, and they've also got another one around here. Where is it? There we go, they've bodged a little cap between those two pins. Oh, what a shame! And those puppies would be our opto-isolators, because the ground split

**Dave Jones:** is right on the other side directly under those. So they've got those on the top side to isolate the data, because there's two things you need for an isolated scope like this. One is the isolated power, isolated DC to DC converter, and also the isolated data as well.

**Dave Jones:** So we've got ourselves our data isolators here, we've got ourselves our isolated power, and some more data isolation here for our oscilloscope channel. But how do we get that signal across? Well, you can tell by the physical arrangement here. Here's our coax going out to the main board, so that's our signal out.

**Dave Jones:** Here's our signal in. Ta-da! What do you think that does? It's an analog isolator to get the 100 megahertz analog signal, that's the highest bandwidth for this thing, across. So that's fully isolated. Because you can't, because our digitizer is on this side, our ADC's over here, on this, on the non-isolated

**Dave Jones:** side. But unfortunately, that can is soldered in. Oh, boo-hoo! And I've popped one side of this metal can here, and look at that! Oh, the cheeky buggers have rubbed the smart number off, and then they've silastic gunked down either side. What the? That's their secret

**Dave Jones:** source, I don't want people knowing how they do their isolation there. Ha ha! Anyone want to guess? And then on the bottom here, there's the isolation gap in the ground, you can see it right there, and then they went, well, will we or won't we capacitively

**Dave Jones:** couple across the isolation? Eh, but it looks like they've done it. And we've got the cans off both our oscilloscope channel, I won't bother doing the second channel because it'll be absolutely identical, and then our multimeter. Let's take a closer look at the multimeter first.

**Dave Jones:** Here's our multimeter input, that's some, we've got some diode protection over there perhaps, and we've got ourselves a MOVs. There was nothing on the bottom side here, they've got some isolation slots. Curiously, we've got ourselves a 20 megahertz oscillator there, but what that's used for, is it that device there?

**Dave Jones:** We'll have to have a look what that puppy is, but it's pretty minimal setup anyway. We've got like non-traditional multimeter type input, doesn't have your traditional multimeter chipset, that's for sure. And that's what our oscillator is for, that's a Silicon Labs F330, that's actually

**Dave Jones:** an 8051. Once again, they're 8051 fanboys at mixing. And that one's got a built-in 10-bit IC, so that's probably what they're using for the multimeter there. Apart from that, everything, you know, once again you see some 4051s, and we've got an LM7332, just an op-amp.

**Dave Jones:** 4052's got some more muxing happening there, and not much really doing around this. Pretty boring. That there is interesting, Q24, it's actually, by the designated Q, it's a transistor, and that's an N-channel, that's a 60-amp N-channel MOSFET. So what are they doing there?

**Dave Jones:** They're doing some switching or some form of protection. We've got two of those puppies in there, so what's the go there? Let's have a look at our oscilloscope input. Got a couple of little trimmer caps down there, there we go. Just to tweak

**Dave Jones:** the front-end performance there. Relay switching looks like a pretty typical kind of front-end. And there's our BNC. What's hanging off the end there? Why have they heat-shrunk that? What the? Another 8051! Are you kidding me? Inside the oscilloscope front-end! They're obviously doing that, like serial decoding.

**Dave Jones:** Hey, what's that in there? Is that? Hey, look, oh, that's no good. A little bit of solder dag there, where'd it go? There it is. A little bit of solder dag. Don't know if I like that. Where did that come from? Oh, must have, maybe one of the front-panel solder connections or something.

**Dave Jones:** Yeah, they're a bit, ugh. Yeah, they don't look the best. So there's our in-serial programming header for it. So what they're doing is using these remote processors on the other side of the serial interface, because they've got to come across this serial interface here, right?

**Dave Jones:** So you've only got limited data lines, like, you know, transmit and receive. That's basically it. And then, you know, you've got to have some sort of active processor to decode that. So I guess there's no surprise for finding a micro on there. And that's got

**Dave Jones:** H1F943 on it. My first guess was that it's a Hitite brand, but if you look up Hitite 943, what is it, Dave? Microwave power amplifier. Microwave power amplifier, up to what, 30 gig or something? It's for satellites. It's for satellites. So yeah, I don't think we're into rocket science here today, so it must be something

**Dave Jones:** else. So yeah, if you want to find that one, go for your life. We've got another obscure part, HVB-051, whatever that is. Some sort of output driver for the transformer, perhaps? For the isolation transformer, because you can see it. There's a signal bugger

**Dave Jones:** over there, under to the CAN, but yeah, I don't know. Anyway, I'll post high-res photos of all these sections, and you can have a play along at home. Follow the datasheet. So that is the front-end board, and well, that's quite impressive. There's a few potential quality control production

**Dave Jones:** issues there, but jeez, no, that's, it's, you know, that aside, it's a very impressive bit of work. You know, they really aren't cutting corners, and they're doing everything properly, and I have no doubt it meets all its rated specs and everything else. This is a real high-performance unit.

**Dave Jones:** It's not built down to a price. And well, you pay for it. These things are, you know, these are not cheap handheld scopes. Mixing don't make cheap instruments. Oh! Put it back together, got all the ribbon cables, and forgot the bloody encoder wheel, didn't I?

**Dave Jones:** Oh. When I got the wheel back in, I forgot the bloody isolation pad. Unbelievable. I'm an idiot! Forgot the bloody plate! Oh. I think I'm going home. I should have gone home. Forgot to put the bloody strap thing in, holder in. Oh. This is not my day.

**Dave Jones:** So let's see if she works. Ta-da! Mixi! Handheld multifunctional oscilloscope. Hilarious. There we go. And... no worries. It's a quite, actually, it's quite a responsive scope. I've got no I've got to hold it up here. If I hold it at an angle, I get reflections

**Dave Jones:** off the lights and everything else. It's no good. It's actually quite a reasonably responsive scope. Like the fast waveform update rate, I really like it. And it goes from 5 millivolts per division up to have a look down there. I can hear the relays click.

**Dave Jones:** Look at that, 50 volts per division. Ripper. Because that's one of the uses for handheld scopes. Used out in the field traditionally in sort of more, sort of, you know, industrial higher power, you know, higher voltage type environments. So at the BNC, to have 50 volts per division, that's very nice.

**Dave Jones:** So yeah, I really like the performance of this. It's speedy, responsive, and everything works a treat. But one thing I do miss is an intensity graded display. But eh, because it's a handheld scope, you know, not an everyday use scope, then eh, that's alright.

**Dave Jones:** So, you know, no worries at all, but yeah, it just would have been a nice touch. And for those who haven't seen it, we can go into meter mode as well, just whack the button. Nice big bright display, lots of functionality, it's all touchscreen of course.

**Dave Jones:** And there's capacitance, 10 puff resolution, and continuity buzzer, I can check that out. It's a bit on the slow side, okay-ish, but yeah, not the fastest. And its performance is nothing fancy, I mean, we're only talking, you know, 5000 counts, so eh, you know, it's got your basic functionality.

**Dave Jones:** It's good if you're out in the field, you know, shouldn't have to take a separate meter. So anyway, I hope you enjoyed the teardown of that MixSig MS310-IT. 1 gig sample per second on single channel only, 100 megahertz bandwidth, fully isolated scope. And I'm really quite impressed, Sig really know what they're doing.

**Dave Jones:** You know, design, pretty first rate. A few little production issues, you know, small production issues as I said, which they'll get better. But you know, they're basically new in the game, MixSig, and they're trying to compete at the high end. So you know, if you're in the market for a decent quality handheld scope,

**Dave Jones:** well worth a look, this puppy. And as always, I've got high-res teardown photos over on EEVblog.com, and if you want to discuss it, leave YouTube comments, or there's always a link down below to the forum thread, which is all lively, that's the place to do it.

**Dave Jones:** As always, if you liked it, please give it a big thumbs up. Catch you next time.
