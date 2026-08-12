---
video_id: z3V-1v-UhTc
title: EEVblog #1289 - Mystery Huawei Teardown
url: https://www.youtube.com/watch?v=z3V-1v-UhTc
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 28, "3": 40, "4": 57, "5": 71, "6": 84, "7": 99, "8": 108, "9": 126, "10": 136, "11": 148, "12": 164, "13": 190, "14": 206, "15": 226, "16": 235, "17": 245, "18": 256, "19": 269, "20": 297, "21": 308, "22": 320, "23": 334, "24": 346, "25": 356, "26": 368, "27": 390, "28": 403, "29": 419, "30": 433, "31": 442, "32": 450, "33": 462, "34": 478, "35": 497, "36": 504, "37": 517, "38": 540, "39": 550, "40": 569, "41": 592, "42": 612, "43": 621, "44": 634, "45": 646, "46": 656, "47": 676, "48": 687, "49": 694, "50": 705, "51": 721, "52": 733, "53": 745, "54": 758, "55": 771, "56": 783, "57": 793, "58": 810, "59": 827, "60": 833, "61": 844, "62": 857, "63": 866, "64": 886, "65": 897, "66": 909, "67": 925, "68": 937, "69": 951, "70": 967, "71": 977, "72": 998, "73": 1010, "74": 1021, "75": 1034, "76": 1046, "77": 1060, "78": 1074, "79": 1086, "80": 1100, "81": 1111, "82": 1125, "83": 1135, "84": 1150, "85": 1167, "86": 1176, "87": 1187, "88": 1200, "89": 1209, "90": 1225, "91": 1245, "92": 1258, "93": 1272, "94": 1283, "95": 1291, "96": 1307, "97": 1319, "98": 1329, "99": 1341, "100": 1359, "101": 1368, "102": 1379, "103": 1388, "104": 1413, "105": 1426, "106": 1440, "107": 1450, "108": 1461, "109": 1470, "110": 1482, "111": 1490, "112": 1501, "113": 1510, "114": 1526, "115": 1535, "116": 1545, "117": 1557, "118": 1571, "119": 1598, "120": 1605, "121": 1621, "122": 1637, "123": 1660, "124": 1672, "125": 1685, "126": 1700, "127": 1719, "128": 1736, "129": 1768, "130": 1781, "131": 1801, "132": 1814, "133": 1824, "134": 1841, "135": 1851, "136": 1862, "137": 1874, "138": 1888, "139": 1902, "140": 1915, "141": 1929, "142": 1947, "143": 1971, "144": 1979, "145": 1998, "146": 2014, "147": 2034, "148": 2049, "149": 2069, "150": 2081, "151": 2092, "152": 2105, "153": 2114, "154": 2126, "155": 2142, "156": 2150, "157": 2161, "158": 2172}
---

**Dave Jones:** Hi, and welcome to everyone's favorite segment, mailbag. Let's get straight into it. Thank you very much, Max Button. Winning name. It's like Max Power. Um Max Button, fantastic. From Aaron Affair here in not only Australia, but New South Wales as well.

**Dave Jones:** And this has to be the heaviest mailbag item I've ever got. Uh it could be pushing 20 kilos or something like that. Don't know what that is in pounds for you Yanks, multiply by 2.2.

**Dave Jones:** It's backwards there, reverse technique. Thought this deserved a look before ending up in the bin. So, we have a bit of junk electronics. It was once a very valuable bit of kit.

**Dave Jones:** By the way, update. Um I hit Woohoo! I hit 10,000 subscribers on Library. Winner, winner, chicken dinner. Thank you very much to everyone who subscribed on Library. And because it's a decentralized That's just on library.tv, by the way.

**Dave Jones:** But because it's a decentralized network, it's actually, um hard to know exactly how many uh people watch and follow on the Library network. Cuz Library's like a uh protocol, just like HTTP is, except it's LBRY.

**Dave Jones:** But yes, 10,000 subscribers. Absolutely fantastic. And uh if you don't know, I've done a video on this, might have to link it in. But I became a full-time YouTuber in 2011 with only 10,000 subscribers.

**Dave Jones:** So, you got to watch my video to know how I actually did that. Anyway, um yeah, so it it feels like old, but new again. Absolutely fantastic. So, if you're not subscribed to Library, please do.

**Dave Jones:** Okay, it's rack mount. I can feel the rack mount digging into my stomach. Oh, it's not a bloody UPS or something, is it? It's not just full of bloody batteries, is it?

**Dave Jones:** It's foo. Okay, it's a rack mount bit of kit. Huawei? Um okay. Huawei, I know they did Like that sort of stuff, but anyway. And here it is, it's a Huawei and it's just got some uh Ethernet-y type interfaces.

**Dave Jones:** I'm not sure if they're ones in RS-232 interface. I like how they put the baud rate on there. Check that out. 115,200. Not sure why these are on an angle.

**Dave Jones:** They're optical ports, are they? So that they can come out at a better angle here. But anyway, it's got alarm, run. What's on the back? Uh two IEC um with individual switches, fault, run, alarm, fault.

**Dave Jones:** Slide this out. There we go. That's a uh wow, that's a that's a nice-looking power supply. Wow, I No, I don't think it's a UPS. I think it's just a really heavy something-or-other.

**Dave Jones:** 53-V output, 15-A max. Wow, what a Bobby Dazzler. Well, turns out it's a not a UPS, it's a multipoint control unit for a video conferencing uh system. The VP9630 uh for those uh playing along at home, dates from uh 2013 and Max uh sure enough says that it comes from a backbone for a video conferencing system for emergency services.

**Dave Jones:** Um the one of the power supplies is dud, apparently. So it I just had a quick look and it I'm still not really sure what it actually does, but it somehow controls uh up to 12 1080p uh 1080 60p video channels.

**Dave Jones:** That was apparently the first unit, or they claim it was the first unit on the market to do real-time uh transcoding of that many 1080p 60p channels. I guess they all come via the um optical interface and it processes them and then streams them out somehow.

**Dave Jones:** I don't know. So the amazing weight in this thing just comes from the power supplies and all the electronics and other modules. There's a fan module. Oh jeez, can nick those fans.

**Dave Jones:** Got no idea if they're any good or not, but uh yeah, you know, always uh put those. I've got a fan, I've got a bin full of fans. I love those custom connectors.

**Dave Jones:** Check that out. That's just for the fan module. Wow. Spared no expense. Really spectacular. Spared no expense. Really like how there's a 4-mm jack on here for your ESD strap.

**Dave Jones:** Absolutely fantastic. And a big uh ass earth terminal as well. Aha! Figured it out. I was about to get all medieval on its ass and then I figured out that it actually slides forward.

**Dave Jones:** Uh it seems obvious, but yeah, trust me. Anyway, there we go. Oh, we're in like Flynn. Wow, look at the hardware inside this puppy. But because it does dedicated hardware-based uh H.264 1080p uh encoding and decoding on multiple channels, it's got to have a ton of stuff.

**Dave Jones:** It reminds me of the uh the Sony video systems, which I'll link in at the end and down below. If you haven't seen them, they're absolutely fascinating, those uh video editing professional video editing solutions.

**Dave Jones:** This one's not video editing, but this is uh like video conferencing and things like that. So, we've got multiple cards in here. Wow, this is Wow, LOOK AT THE THICK UH THIS IS THICK AS.

**Dave Jones:** 4.2-mm PCB. Oh, that's thick as, bro. Hi to all my New Zealand viewers. Check out that big power connector over there. Look at that beast. That has got screw terminals on the back of it.

**Dave Jones:** So, this comes in from the power supply. So, they're just distributing What's a little eight-pin dip in a socket there? We'll have to check that out. There's another power connector.

**Dave Jones:** That one's only got screw two screw terminals. Oh, Oh, ripped off. Oh, look at the ground. What is it? A spike? That's not rigidly connected. What on earth What?

**Dave Jones:** As you slide the board out. Oh, does it like make first contact when you slide it in or something like that? Is it a Anyway, wow, there's a ton of engineering in this puppy.

**Dave Jones:** Look at it. Wow, unbelievable. How much If anyone has any i- idea how much this would have cost. And this is like the runt of the litter. Really, there are much bigger ones available as part of a big cascaded, you know, video conferencing distribution type streaming system, but wow.

**Dave Jones:** Anyway, so they're clearly going to be using multiple internal layers, probably, you know, 2 oz or even more copper inside there just to get the power distribution. And of course, you use the 4.2 mm for rigidity as well.

**Dave Jones:** Um, it's not like it has to be that thick to carry the current. It's just, you know, they're using it as a rigid structure there. Brilliant. Because we saw before 15 amps per power supply, so 30 amps total.

**Dave Jones:** So, you know, it's it's large current, but like not absolutely enormous in the scheme of things. There's another little ground spike down there. Check that out. It's not making contact, but they've certainly gone the effort.

**Dave Jones:** And you can see the good thermal design of this, too. Of course, we've got uh spacings between We've got three layers of boards here. I don't think there's another layer under there.

**Dave Jones:** No, that's the power supply slide at the back. So, we've got three layers of stackable boards. It looks like we can stack more here. And I believe this is part of the system.

**Dave Jones:** You can actually continue to stack these boards up and up. I'm not sure what the limit is. We'll have to look at the manual configuration manual for that. But you can get larger and larger cases for this thing.

**Dave Jones:** Hence why the case is probably a bit unusual in its design and construction because you can actually get thicker ones that expand upwards. And obviously, this is like one of our main processing boards over here, and each one of these boards, this looks like we've got at least 1 2 3 4.

**Dave Jones:** We've got four separate boards, probably the same configuration down on the main board perhaps for doing all the video encoding and decoding. Plus all your web interface and main processing cuz all this sort of stuff, it's got like a web interface control and things like that.

**Dave Jones:** So, that's probably the main web interface processor type thing over there. But anyway, looking at the thermal designs, right? You've got to get a lot of air flow in this thing.

**Dave Jones:** So, it's sucking it through the vents on the side here, and it sucks the air in and blows it out through these three fans fairly evenly spread over all the boards like that.

**Dave Jones:** So, that's really quite nice. And yes, they do have the fins in the correct orientation for that air flow. You'll notice that they're actually long like that. If you flipped them around the other way, so you had mostly the flat part and the air flow going through like that, it would it would you get turbulent flow and all that sort of stuff, and you wouldn't be able to get

**Dave Jones:** the heat as effectively out of there. You're effectively like a blocking that air flow. So, yep, they've chosen the right orientation there. That's not by accident. That's all part of good engineering thermal design.

**Dave Jones:** So, this really is quite amazing. If you have an idea of how much this sort of gear is worth, please let us know in the comments down below. And who knew that Huawei, because we just know them like of them making phones, but other people in the industry, they might know them.

**Dave Jones:** They're into like the professional electronics market like this, just like Sony and other companies are that you don't think of. You know, Sony you think of just consumer gear, but they practically owned the entire like, you know, tons of like professional video editing and all sorts of other professional recording tools and things like that.

**Dave Jones:** Screws out, but I like these this plastic cover here. Oh, oscillator porn. Look at that Vectron OCO. That would be oven controlled oscillator at 32.768 MHz. Thank you very much.

**Dave Jones:** Nice binary multiple there. But yeah, that would be worth a pretty penny. But they're They're They're serious about their stable clock here. Nice. You'd salvage that. Think I got all the screws.

**Dave Jones:** And of course, like we just got a bunch of DRAM on the back and things like that and just some miscellaneous stuff, some local oscillator and other, you know, transceivers and other housekeeping stuff and whatnot.

**Dave Jones:** You can see here by all the bypassing and all the vias there. Huge BGA. One of you know, 1,000 pin BGA. Going to be some custom ASIC processing thingy, video processor, encoder, decoder.

**Dave Jones:** Then another one. Okay, it could be an FPGA, too. And then another one here, another one here, another one here, another one here. Well, geez that's heavy. And we know why.

**Dave Jones:** Oh, look at that beasty. Wow. Huge heatsinking under there. Once again, the orientation of the fins like this. They're very deliberate like this because the airflow is coming in like this and it's got to flow over those fins even though they're not very tall.

**Dave Jones:** So, not a terribly efficient heatsinking that aspect of like a surface area fins there, but they've only got limited height and they would have done all the thermal testing calculations to ensure it's correct.

**Dave Jones:** So, they knew what they were doing. Wow. Absolute beast. That one's just stuck down there. It's a bit how you doing. It's on an angle. What's all the power up there for it?

**Dave Jones:** That's all it obviously we probably going to have like a whole bunch of local supplies. There might be you know 1.2 volts, 1.8 volts, 3.3. Look at those MOSFETs up there.

**Dave Jones:** Wow, that's some beefy switch mode right there. And fused as well, a poly switch on the output. So, very nice. Oh, you'd like you'd keep these boards. It's just chock-full of premium goodness.

**Dave Jones:** Well, there's a surprise. I expected these bottom boards to be identical. This one looks like it's going to be, but this one here significantly different. But yeah, I expected four identical.

**Dave Jones:** So, to have that oddball one, but look at all the Look at the bypassing on this bad boy. Look at this. Look at all the huge FPGAs or ASICs we're going to have under here.

**Dave Jones:** This is some serious ass hardware, and this is not going to be built down to a price in any way. There'd be zero penny-pinching in this cuz price is no object in this sort of market.

**Dave Jones:** You buy what you pay for the performance of this. We're talking tens of thousands of dollars just for this kit, let alone all the higher-end models and things like that as part of the system.

**Dave Jones:** Sure, this is tens of thousands of dollars, easy. And there you have it. We have a grand total of three of these boards like this. However many video encoder decoder channels that is, I don't know.

**Dave Jones:** And it looks like nine identical channels on here. They could be FPGAs for example. Lots of huge tantalum bypassing on there, and a bunch of memory for each one, of course.

**Dave Jones:** And Is Is there No, there's no more memory on the other side, but a ton of bypassing. I mean, that's just that's nuts. But, that's what you get on uh modern FPGAs, and a lot of designers tend to go overboard, but once again, all power supply stuff up here.

**Dave Jones:** And check out the uh high-speed board-to-board inner connects like this. You notice that the inner one is big ground contact like that. Very nice. So, these are all really ultra high-speed uh differential uh pairs you can run through these things and design for high-speed board-to-board inner connects.

**Dave Jones:** Not sure of the uh brand or model of this. It could be, I don't know, a Samtec or something like that. They cost a pretty penny in their own right.

**Dave Jones:** And so much for my theory that uh it would contain uh more channels on the baseboard like, you know, you'd get you buy the base model unit and you'd get X amount of channels, and then you expand them up with the modules.

**Dave Jones:** Nope. Nope. That's just a It's just a bare board on the bottom, and uh looks like they have something on the other side here. These bypass caps aren't going to be there for nothing.

**Dave Jones:** Not only do we have bypass caps, but we also have little uh series termination resistors. So, yeah, it's something on the other side. I think I'm going to have to get this whole puppy out.

**Dave Jones:** And yep, there's another chip under there. So, yeah, the whole thing's going to come out. Jeez. All right, this whole puppy is going to slide out like this. Little Got some foam down here.

**Dave Jones:** Oh, careful uh when you pull the other boards like this, the pins on the bottom, they can rip you open. I've already uh drew some blood on the the case of this thing.

**Dave Jones:** Having a play. Oh, hang on. Uh No. Oh, that's what those pins. Right. Those pins up there, that one there, and that one there, they're designed to stop this board sliding out.

**Dave Jones:** Wow, I didn't expect that. I thought this would just pull out, but I guess they were I think the The is is that that whole backplane has to come out before this board can slide.

**Dave Jones:** That's a bit disappointing. Here you go. This whole thing now just lifts out like that. And by the way, check out this. Uh the huge power input there is just a press fit contact.

**Dave Jones:** They aren't soldered. No, they didn't forget to solder that. That's just how they are. You can actually get those. They do work quite well in the industry. And no need for that solder rubbish.

**Dave Jones:** And there's the other mating side of that huge big power one. There's the three-way jobbie. And those big uh spikes look like they're just for alignment when you put the boards in.

**Dave Jones:** They don't actually do anything electrically. Really. Anyway, version A board is upside down, so all the electrons are going to fall out. There's our five-row data connector. I'm not actually sure where that goes.

**Dave Jones:** Like there's nothing else like there to do anything with it. So, yeah, I'm not sure what the deal is. It's like it's really just a power distribution. And absolutely no surprises at all for finding that's an e squared promise doing some sort of product ID something like that.

**Dave Jones:** You know, they're not going to worry about it's not for like security or anything. They're not going to worry about anyone ripping off this product the engineering. If you can rip off this product, good luck to you.

**Dave Jones:** Um you deserve to because a phenomenal amount of engineering's gone into this. Looks like we've got another 4.2 mm PCB down in here, which uh connects all of the well, the other side of the power supplies.

**Dave Jones:** And you can see the power supply connector down in there. Uh it's a beauty. Wow, look at those jewel wipe contacts there. So, that really is just a beautiful piece of system engineering design, really.

**Dave Jones:** And as I said, it's designed, I believe, to stack up like even higher and higher. And you can put like larger and larger cases on this thing, and it's designed to grow upwards.

**Dave Jones:** Every aspect of this spared no expense. And that is a gorgeous PCMCIA holder. Wow, that thing alone must have cost Imagine the single one-off bomb cost of that. That's going to be enormous.

**Dave Jones:** Anyway, that's a Western Digital Silicon Drive registered trademark. 1 gig, solid state drive. Manufacturing date, 44th week, 2013. So, you know, that would have been hot stuff back in the day, I guess.

**Dave Jones:** Okay, over here, we start off with our We've got our ethernetty interfaces, whatever they are, and that RS232 one as well. We've got the magnetics down in here. They're not built into there.

**Dave Jones:** These are your two fiber interfaces. So, they're like fiber modules just slide into there. So, all the laser diode goodness is inside. The module, the receivers, and transmit stuff is in there, and this is basically just a holder.

**Dave Jones:** Pretty much board-to-board interconnect. Got an Altera Max 2 CPLD there. It's just doing some like general housekeeping stuff. And battery backup, of course, for the real-time clock. That'd be the real-time clock chip.

**Dave Jones:** I think I see an ST branding on that puppy. And then, we've got all the power supply goodness. Wow, look at these. You would salvage these. These are like Obviously, they farm out the design of these to someone.

**Dave Jones:** But, you know, you can do them in-house. But anyway, people ask, "Why would you put it on a module? Why not just put all these parts on the main PCB?" Like what you do here, okay?

**Dave Jones:** This is integrated with this. Well, this is a higher power solution. And look, the magnetics, that's complete ferrite going on both of the sides of the boards there. And we've got a planar transformer, which means that the windings are going to be inside on the PCB there.

**Dave Jones:** So, and you don't want to be designing this sort of stuff on this massive a board. I mean, you've got enough issues with this board. Imagine if you like a goose stuff and you have to re-spin this whole board just because somebody screwed up on one of the little power supply ones like this.

**Dave Jones:** You could argue well, why didn't they do it here? This is a lot simpler than this solution here. So anyway, and they as I said, they probably farm that out and buy it in.

**Dave Jones:** So you definitely want to desolder there are solder direct get those out cuz they're valuable. They'd be like super efficient really high power converters you can use for your projects and things like that.

**Dave Jones:** Gorgeous. No surprises for guessing the brand of the capacitors down in there. I don't even think I need to show you. Top notch quality everything on this. They would not be saving a single cent anywhere.

**Dave Jones:** They just wouldn't bother. Tiny little oscillator down in there. That's for something going on there. And then a Broadcom chipset over here. We can have a look what that's doing.

**Dave Jones:** Do we have a part number on that? Let's have a look at that. I'm sure that's doing something that we can find out about. And other stuff on the bottom well, drivers maybe like interfacing housekeeping for interfacing with the other boards up here.

**Dave Jones:** So there's the board in all its goodness and there's those power supply modules soldered down there. So you definitely want to try and get those out. Unfortunately, you know, they're often like a tight as a nun's nasty inside the holes there and well, sucking out the solder on those could be a a bit of a pain.

**Dave Jones:** But anyway, worth a shot. Not much doing. Not sure what's going on down in the corner down there. Oh, that's all the ethernetty type stuff over there. They've removed some of the ground plane for controlled impedance reasons.

**Dave Jones:** All this other stuff up here well, this is all TI. We've got a TI jobby in there. I'm not sure what that's doing. Xilinx uh Spartan again. Got a couple of chips in there which I do not recognize at all and then another one of these uh TI chips up there.

**Dave Jones:** So, if I can get the data on those, I'll pull them. And is that some sort of clock driver? That wouldn't surprise me. That kind of looks PLL-y to me.

**Dave Jones:** So, I'd say clock driver off hand. Got a couple of surface mount fuses down here. Very nice. As I said, that oven controlled oscillator, oh, you want to get that bad boy out of there.

**Dave Jones:** You bet your bottom dollar. Uh probably FPGA under there, is it? Uh driving for interfacing, perhaps. Stuff like that. And uh the power supply input up there. Got another uh surface mount fuse jobby there.

**Dave Jones:** And oh, this is brilliant. And if you're wondering, can you bend a 4.2 mm PCB? Yeah? Well, it's just fiberglass. There you go. Wiggle, wiggle, wiggle. Yeah. All right.

**Dave Jones:** So, what's going on with this board here? Massive uh FPGA or ASIC. Got some firmware down here. Did give away with the uh stickers on it. And what's a Cortina?

**Dave Jones:** Well, I know what a Ford Cortina is, but I don't know what a Cortina is here. Made in Canada? Really? Is there a fab in Canada that makes that?

**Dave Jones:** If there is, please leave it in the comments. No less than 1 2 3 4 5 6 7 oscillators. None on the bottom. No. That's really quite remarkable. Anyway, looks like we've got some Is that SRAM?

**Dave Jones:** That could be high-speed SRAM, is it? Or is that DRAM? I don't know. Looks like we've got some sort of Broadcom chipset down there. Not sure what that is.

**Dave Jones:** Two of them. And as for all the power supply stuff around here, no surprises for finding like a Linear Tech part on here. They're one of the most expensive in the business, but then they're brilliant.

**Dave Jones:** Doing some uh shunt current shunt measurement there by the looks of it. And I got the heat gun out and I managed to get that heat sink off. It was stuck on there good and proper.

**Dave Jones:** I don't think my isopropyl is going to get that off. Some scraping, but we'll get there. Well, no surprises for finding an Intel in there. What's a WPIIXP2350? Well, it turns out the IXP2350 is a network processor.

**Dave Jones:** 2004 vintage is when that came out. So, yeah, this is the main processor that's running all the applications software and and probably like doing lots of the like the networking, OS, and all sorts of stuff.

**Dave Jones:** Anyway, this is running the application. This is running the whole show. So, onto this board here. Now, I looked at the manual. It says it contains, well, the base model anyway, contains eight dedicated audio processors.

**Dave Jones:** And we have nine here unless my count is out. And wouldn't be the all the video stuff cuz I think that's all on the other boards cuz that's the main purpose of this thing.

**Dave Jones:** Best guess would be that this is doing the audio processing. I've got a Max 2 CPLD. That's just doing housekeeping. And we'll have a Well, I can't really find any info on that apart from that well, it's related to Huawei in some way.

**Dave Jones:** So, I'm not sure whose logo that is. If you do know what that is, leave it in the comments down below. Anyway, this puppy here is a PCI to PCI bridge.

**Dave Jones:** So, obviously, we've got the PCI interface. We saw these on the other boards as well. So, they're just using those as a generic PCI interfaces to each one of these boards.

**Dave Jones:** And that makes sense. There's lots of experience and knowledge with PCI interfacing. It's fantastic to use and it's going to do the business. So, yeah, no surprises for there.

**Dave Jones:** But anyway, I'll try and pop one of these off. Not too hard. You just get the uh heat gun? I had it to 100 uh 50° and then just heated it up for like 30 seconds and then it just pops.

**Dave Jones:** Well, it doesn't pop off. You got to put a bit of force, but yeah, we're going to have to scrape this one as well. And the TMS320 fan boys go wild.

**Dave Jones:** I'm a bit of a 320 fan boy myself. And uh yeah, this would almost certainly be doing the audio uh processing cuz that be a classic I've done on a TMS320 is it is like a they de facto industry standard uh digital signal processor.

**Dave Jones:** One of the classic uses for these would be for audio process real-time audio processing. So, yeah, no doubt that's what it's doing. I think this is the audio uh card.

**Dave Jones:** Why there's nine of them? I don't know. An extra one for housekeeping or an extra channel just for good measure. Not sure, but uh yeah, one of those dedicated to uh each audio processing stream.

**Dave Jones:** And once again, like it's all digital. It's got it like it comes in digital. It's not like this is like sampling analog audio. This is not an analog uh product.

**Dave Jones:** It comes in via the fiber ethernet internet of things thing, you know, whatever. Um all comes via that digital and um then it does its uh dedicated uh uh processing of the audio, you know, probably uh filtering or other uh type stuff.

**Dave Jones:** And it does it all in dedicated hardware. Ev- every channel gets its own dedicated DSP. And that's what you're paying for. You're paying for this dedicated hardware. You know, maybe try and do this on even a like a you know, a top-range gamer kiddy PC and uh like it's just going to bog down once you render dozens of different uh 1080p videos and audio all at the same time

**Dave Jones:** and things like that. Like in filter it and do all that sort of stuff. It's just going to keel over. This is why you have dedicated hardware. And I got the heat sinks off this bad boy.

**Dave Jones:** Uh this is the obviously the video encoding decoding. And unfortunately, um my scraping technique didn't work very well with this. It is an Altera something. So, it's an Altera FPGA, something FPGA, a big-ass FPGA.

**Dave Jones:** As you'd probably expect, I looked at the numbers on these, but herein lies the issue. If you want to get the heat out of all these, you can put like individual small heat sinks on all of them, or you can go for one larger heat sink, which they've decided to do here.

**Dave Jones:** The problem is is that these chips are different height profiles. So, how do you solve that? Well, there's you can do it a couple of ways, but one way they decided to do it is to actually machine out the heat sink, so it's actually got the like a raised part that comes in contact with the chips down there, the smaller chips.

**Dave Jones:** So, bingo. Like, how many times multiple have you just increased the cost of that heat sink by having to do that operation? But, certainly, that was the best decision that they came with.

**Dave Jones:** As I said, they wouldn't be saving cost on this thing. No siree Bob. Anyway, interestingly, this one is different to those three. And the TMS320 fanboys go wild again.

**Dave Jones:** The bigger device under there is a TMS320DM8168 for those playing along at home. Well, as it turns out, that's just not any TMS320 like audio processor, that's actually a DaVinci co-processor.

**Dave Jones:** It's got an ARM Cortex on there at like over a gig plus a DSP processor as well, as well as a video encoding engine, and yeah, it's specific DSP and dedicated hardware encoding for video and audio processing.

**Dave Jones:** So, there's four channels of those. I presume one per video, cuz there's only one video engine on there. And this one, it's an Analog Devices jobbie. Aha, that ADV chip, that is a HDMI receiver and 12-bit HDMI digitizer.

**Dave Jones:** So, obviously there maybe the giant FPGA over here is decoding all the serial data coming in from the network and let's say you've got you know streaming video coming in and then splits it up into the multiple channels and then feeds it into the separate encoder separate sorry HDMI receiver and then processes it inside the DSP and then that'll shoot it back out perhaps.

**Dave Jones:** That'd be my guess anyway, but but I haven't looked into the architecture of this thing. So, yeah, I don't know. Why is this one different? Well, turns out that's actually a now owned by Broadcom PCI switch.

**Dave Jones:** So, like a six-port PCI switch. So, there you go. They're still doing PCI stuff at that point in the system. So, that's another Analog Devices under there. So, because they had for it's just the layout's a bit odd because this one's probably associated with this one and this one with this one.

**Dave Jones:** Something like that. So, yeah, they probably just that could just be a layout thing. They just went you know but you would have laid this out as a block first and then duplicated it like this and then figured out how to fit this in.

**Dave Jones:** So, seems a bit oddball but anyway, you didn't seriously think I was going to finish this video without showing you inside this bad boy. Let's check it out. These are obviously two fans and yep.

**Dave Jones:** Whoa, look at that. Oh, beautiful. Thing of beauty. Mix of surface mount and through hole as you'd expect. Once again, uh spared no expense on this thing. Designed by designed and manufactured by a company called Vapel.

**Dave Jones:** Um and I never heard of them but look, they've got a real lay down in there. Real fair dingum relay. We've got Look, jewel mov protection. It just looks really gorgeous.

**Dave Jones:** Look at the single-sided phenolic PCB up here. They're just Look, they're just using that board there just for the mains wiring. So, the mains starts over here. Look at the protection.

**Dave Jones:** Look at the size of those movs. They just suck up the jewels. Wow. Thank you very much. So, that's just super impressive. Wow. And is that a spark gap there?

**Dave Jones:** I think it might be. Brilliant. Belt and braces. And then we've got our multi-stage common mode chokes here. Absolutely fantastic. Look at the the earthing up there is first class, of course, as you'd expect.

**Dave Jones:** Absolutely terrific. And look at all the Look, they're just individually heat shrunk all of the wires there. Just this ribbon cable going over here. Like, they just didn't care about optimizing uh, manufacturing cost of this.

**Dave Jones:** They couldn't give a rat's. And are they two input fuses there? Look at the input resistors there for surge. And it's just fantastic. You want to salvage that board, put it in your junk bin, for sure.

**Dave Jones:** And don't know the brand of those caps, though. Anyone? Shanghai or something? Sorry, I just can't can't see that from here. So, main switching devices, they gunked them down down in there.

**Dave Jones:** And it all looks really top quality. No worries whatsoever. Fantastic. Got multiple mov protection on the output here. Wow. So, yeah, that likely cost a pretty penny. If anyone would want to hazard a guess, please leave it in the comments down below.

**Dave Jones:** Like, they just like didn't care. What's When this power supply fails, which has got jewel This is a jewel redundant power supply system, by the way. It's not because there's It says it's two plus two redundant, which means I do believe it needs both of these power supplies in the system to work, but when you tie it into another system, it can actually have a redundant power supply.

**Dave Jones:** So, there'd be outputs here, which would you know, allow them like tell them it's they'd be monitoring, tell them it's failed, or they'd be monitoring on the other board.

**Dave Jones:** They know it's failed, and they can switch them over redundantly to keep your video stream going. So, it's all about reliability, both in terms of power supplies, and also they've got redundant capability in the switches as well, the fiber optic interfaces and the ethernet interfaces.

**Dave Jones:** So, yeah, very highly redundant product. So, there you go. I hope you enjoyed that, and thank you very much, Max, for sending this fairly unique and almost certainly hideously expensive, if you have to ask the price, you can't afford it, bit of video encoding technology.

**Dave Jones:** Just the bomb cost in this is absolutely enormous, but look at all the engineering that goes into this. If you think designing a new Huawei mobile phone is a big job, and it is, imagine the team that it took to work on this, and how many years they worked on just this niche product.

**Dave Jones:** And then, they've got to get the return all that NRE engineering cost to design these things. If you've got any idea how big the market is for this video streaming type technology, how many units they sold or they typically sell.

**Dave Jones:** When is this thing still around? Is people Are people still using them? Leave it in the comments if you know what replaced it. Are they like just like racks PCs, server rack PCs, just you know, and graphics cards just chewing through the same stuff that this dedicated hardware did, but it's not that old.

**Dave Jones:** It's only what, you know, six, seven years old. So, but it's was destined for the dumpster. Probably because it's faulty. Otherwise, you know, it it probably still probably be used.

**Dave Jones:** But anyway, who knew that Huawei were into this sort of stuff? I had no idea. Just like a lot of people had no idea that Sony and other companies like that are into the professional audio and video type markets as well.

**Dave Jones:** And I've done lots of teardown of like really obscure bits of Sony kit. And Huawei? Well, I don't know. It's cuz they're fairly new like in the public consciousness now.

**Dave Jones:** And I only heard of them when they, you know, started making, you know, routers and mobile phones and things like that. So, but yeah, it's a real interesting bit of kit.

**Dave Jones:** So, yeah, if you're really after like real high-end systems engineering stuff, then like go try maybe try and get a job on a like a design team for something like this.

**Dave Jones:** Rather than it might be cool to put on your resume, "Oh, yeah, I worked on the latest iPhone 7." Whoop-de-do, wank wank. And but, you know, working on something like this is there's a ton of engineering that the team wouldn't surprise me if it's a 100-plus team and they work for years on this.

**Dave Jones:** And yeah, just truly remarkable. There's a lot of hardware and software engineering that goes into this. So, anyway, if you like that, please give it a big thumbs up.

**Dave Jones:** And yes, I did injure myself in this. So, you know, true blood to the teardown gods. Beauty. And as always, leave comments down below. I do try and not read, respond, and I pin them and all that sort of stuff.

**Dave Jones:** Usually when the video is is first released, I sort of, you know, taper off in the days after that. But I do try and read as many comments and reply to as many as I can.

**Dave Jones:** So, yeah, if you got any info on this, please leave it down below. As always, catch you next time. Mhm.
