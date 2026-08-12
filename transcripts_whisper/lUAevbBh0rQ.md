---
video_id: lUAevbBh0rQ
title: EEVblog 1530 - Siglent SDS2000X HD 12 Bit Oscilloscope TEARDOWN
url: https://www.youtube.com/watch?v=lUAevbBh0rQ
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 14, "2": 44, "3": 58, "4": 74, "5": 103, "6": 103, "7": 103, "8": 133, "9": 150, "10": 163, "11": 163, "12": 197, "13": 219, "14": 235, "15": 255, "16": 271, "17": 292, "18": 308, "19": 332, "20": 350, "21": 372, "22": 387, "23": 405, "24": 422, "25": 435, "26": 451, "27": 468, "28": 480, "29": 502, "30": 516, "31": 536, "32": 554, "33": 570, "34": 592, "35": 606, "36": 621, "37": 640, "38": 651, "39": 669, "40": 685, "41": 701, "42": 721, "43": 737, "44": 749, "45": 771, "46": 783, "47": 797, "48": 818, "49": 838, "50": 856, "51": 874, "52": 886, "53": 908, "54": 928, "55": 944, "56": 956, "57": 976, "58": 996, "59": 1008, "60": 1024, "61": 1036, "62": 1052, "63": 1072, "64": 1084, "65": 1100, "66": 1120, "67": 1136, "68": 1156, "69": 1176, "70": 1192, "71": 1204, "72": 1220, "73": 1236, "74": 1252, "75": 1272, "76": 1292, "77": 1308, "78": 1324, "79": 1336, "80": 1356, "81": 1372, "82": 1384, "83": 1404, "84": 1416, "85": 1432, "86": 1448, "87": 1460, "88": 1476, "89": 1488, "90": 1500, "91": 1520, "92": 1532, "93": 1552, "94": 1576, "95": 1592, "96": 1608, "97": 1624, "98": 1640, "99": 1656, "100": 1672, "101": 1688, "102": 1708, "103": 1724, "104": 1740, "105": 1756, "106": 1772}
---

**Dave Jones:** Hi, you've probably noticed that we've been on a 12-bit oscilloscope frenzy lately. It's like every company sending in their 12-bit oscilloscope. Thank you, Siglent. This one just magically turned up a little while ago, actually. I just unboxed it the other day. So, this is the SDS-2354XHD, or the 2300XHD series.

**Dave Jones:** So, it's a 12-bit jobby, 350 MHz bandwidth, starts at 100 MHz and 2 gig samples per second. So, it's not like, you know, hugely high performance like that new MXO, Roden Schwartz MXO series scope we saw. But, yeah, this one starts at about $3,200 for the 100 MHz 4-channel one, and the one you see here is about $5,000.

**Dave Jones:** Now, unlike the Rigol, we've seen two 12-bit oscilloscopes from Rigol, and one is, of course, the 1000 series, which starts at $999. So, you know, but that is not expandable at all. Whereas this one is at least expandable with your logic analyzer, and also, you're probably wondering, where's the ARB generator?

**Dave Jones:** Well, it's on the back here. So, it does have WaveGen, does have external trigger, does have aux out, does have LXI LAN. But even if you want to compare it to... So, you know, I do like the sort of, like, squat look of it here.

**Dave Jones:** Obviously, you know, with 4 channels, you can't, and a large touchscreen, you can't have, like, individual controls like this. But, you know, I kind of like the 12-bit unit, which I think is similar sort of price point, but it's not expandable. Doesn't have the logic analyzer or WaveGen capability.

**Dave Jones:** So, both of Rigol's 12-bit offerings are just a basic oscilloscope. So, yeah, at least this one is expandable. Anyway, I do like the sort of, like, squat look of it here. Obviously, you know, with 4 channels, you can't, and a large touchscreen, you can't have, like, individual controls like this.

**Dave Jones:** But, you know, I kind of like the look of it. It's a bit chunky, but it kind of, you know, I rather actually like the look of this one. Apart from the font here, it just looks, everything just looks, like, ordinary and not very professional.

**Dave Jones:** Is that just me? Remove film before use. Well, we'll do it before the teardown. So, let's go. Oh, yeah, look at that. That is a matte finish screen. So, yeah, not hugely reflective. So, thumbs up there. And we'll take off these protective things.

**Dave Jones:** Here, it does have times 10 probe detection. Nice, but you'd expect that for this sort of price point. Doesn't have active probe interface, though. Get rid of those. Oh, this is the best part. Calibration void is sealed, broken. Come on. Where are you?

**Dave Jones:** Oh, there we go. Look at that. Oh, that feels good. Oh, look. I could have just peeled that off and stuck it back on. Ah, well, they do have Loctite. Nice. By the way, if you do like to take your own gear apart, and I highly recommend,

**Dave Jones:** don't turn it on, take it apart. Yeah, you can just buy, like, cow stickers. So, you want to peel the sticker off, and it doesn't come off. You can actually clean it. Usually clean the residue off, and then, if you ever want to resell it, you can just buy, like, a generic warranty void sticker.

**Dave Jones:** No one will know the difference. I don't recall seeing another scope that has screws on the handle like that. Okay, this is not as easy nor obvious as other scopes. Um, do I have to take... these off? Maybe. Yep, looks like I have to.

**Dave Jones:** Okay, that's lifting up, but don't know about the top. Wow, there's something you don't see every day. Look at this. Now, one of the screws were there. This is a die-cast alloy handle. And they're obviously putting that, I presume that just goes into the plastic there, and that's what was, I think that's what was holding in the top.

**Dave Jones:** Yep. Wow, when was the last time you seen a die-cast alloy? handle. Unbelievable. Maybe it actually does go into the metal in there. We'll see. Yeah, that's really something. There you go. That's what we expect. There's nothing else in the case there for you case aficionados.

**Dave Jones:** Yeah, sure enough. Yeah, look at that. Wow. They've got big solid metal things for the handle. That's just incredible. Is this going to set a new trend for scopes? They've got, oh, the Siglent's got an alloy handle. Can I have an alloy handle, please?

**Dave Jones:** So I wonder if there's any other old school tricks inside this thing. Let's find out. Geez, no wonder it costs a lot more than the Rigol. Spinny spin spin. Yeah, it's got lock-in washers. Oh, no, it's only got one lock-in washer. Oh, okay.

**Dave Jones:** Does that lift off? There you go. We've got one cable coming out. Oh, look at that. There's our, what board is that? Ah, okay. Yep, that is the WaveGen. That's interesting, isn't it? Wow, I've never seen a separate WaveGen board like that. That is fascinating.

**Dave Jones:** I'll get some high-res photos, of course, always available on the EEVBlog Flickr account. I like the coax going over there. That's just beautiful. But yeah, they haven't bothered to shield that individually from, like, the rest of the unit, but as an outside product, it's all shielded, of course.

**Dave Jones:** So, no whackers, but that's fascinating. Wow. Ooh, and we've got an open-frame power supply here. Wow, this is, I'm really liking the look of this. This is absolutely different to other scopes on the market. Anyway, yeah, open, we'll have a closer look at the open-frame power supply over here.

**Dave Jones:** But yeah, they've got a separate external trigger board and stuff, so that's a vertical riser board there. And this has, look, they've got a coax going off there. Where's that going to? That's going to something else. Oh, that'd be connecting over to the main

**Dave Jones:** board. And down here, you've got your optocoupler trigger board. They've gone to a lot of effort there. I'm really very surprised by this scope. And look at these standoffs on here. Like, they've got the standoffs, they're pressed into the bent part of the metal chassis there, and to mount

**Dave Jones:** that board on, it's beautiful. So a mains input connector down here, nicely mounted like this, nicely earthed like that, going into a rivet in there, so it doesn't have a screw, so that's just a right-angle spade lug riveted onto there, and then nicely crimped terminaled.

**Dave Jones:** And we've got AC here, in, and then it looks like, just, is that single or double? Oh, I'm guessing that's just a single rail, like, 12 volts out of there. And then they've got it going into this little board here, and it's got some

**Dave Jones:** unpopulated stuff there, so they've just got, like, a bypass cap there, and that's it. Nothing on the bottom, so there's, like, no fusing on that board. Yeah, they had something else in mind. This goes over here, nice cable ties, nice attention to detail, even down

**Dave Jones:** here, stop it flapping around in the breeze, and then that's just 12 volts going over to the main board. Um, that is really quite remarkable. Anyway, for you fan aficionados, uh, Delta, um, Delta are a pretty good brand, uh, DC, you know, Chinese

**Dave Jones:** brand, but they're pretty darn good, reputable, at least, no one. Just small things I noticed, like, this is just, like, a riveted alignment pin, which seems to match up with that pin, but I don't see how it physically helps, apart from, yeah, assembly alignment.

**Dave Jones:** Why would you go to that amount of effort? Somebody gilded the lily. Well, they really wanted you to know who manufactured the power supply. It's, uh, Meanwell, and they're very, uh, reputable, um, and yeah, it's, look, you know, it's got all the requisite, uh, certifications

**Dave Jones:** and everything, and yeah, they really went to town. I like the, uh, heatsink, uh, folded heatsink bracket over there. It's, you know, it's anodized and everything, um, along with this one over here. So I'm not sure what brand that cap is. They're covering it up there.

**Dave Jones:** Leave it in the comments if you know. Um, anyway, comment, mode, uh, choke by the looks of it. It's got all the requisite, uh, X and Y class caps, and yeah, it's really compact, though. Now, it says 120 watts maximum, uh, on the back of the scope, so, you know, operationally, it might be, I don't know,

**Dave Jones:** 60 watts or something. Could be half that. Don't know. But yeah, nice little compact. And it's so compact, this is labeled FB here. Feedback, flyback, um, they've got that going over right under the cap there. And of course, the cap is off the board.

**Dave Jones:** So they've really tried to keep the footprint of this thing small. Um, anyway, it's got all the isolation slots and everything. Everything looks hunky-dory. Don't know, uh, over-voltage, uh, protection connector there, so I'm not sure what the deal is there. Um, adjustment pot there, so maybe you can trim your, uh, presumably, uh,

**Dave Jones:** 12 volts out. It's got a little operational lead there, but, um, geez, yeah, that's pretty funky power supply. I mean, you know, they had a bit more room there. So, I don't know, is that like an off-the-shelf jobby? Uh, wouldn't surprise me. Now, I'm sure that I was just, uh, well, complaining, I guess,

**Dave Jones:** or, uh, highlighting in previous, uh, scope teardown videos that, um, yeah, they all sort of are manufactured the same these days, and there's no differences in terms of physical, uh, construction. You know, they're all like a single board, and they all open, uh, the same

**Dave Jones:** way. And this has been true of, uh, Siglent and Rigol and other, uh, brands. And, well, this one is just, um, surprisingly different. So, yeah, I'm, I'm really liking this. I like seeing, uh, design variability like this, because it, it, uh, this is why teardowns are interesting, because you get to

**Dave Jones:** see different methods used in construction, and then you can, you know, store those away in your mind for, uh, when you have to design products, and you go, oh, yeah, like, uh, you know, this idea that this, uh, company used doing this thing, and then, um, but I like, but I didn't like that one.

**Dave Jones:** So, it's still one little, uh, design touch from one manufacturer, another from another, and, um, yeah, it's really, oh, is that gonna come off? Have I forgotten something? Uh, all right, you look, you look. And once again, you can see those alignment pins there.

**Dave Jones:** Isn't that neat? So, they've put those in, uh, looks like to save production time, so that your holes then line up, the holes for the screws, so you don't have to dick around. Because, yeah, there's a gap in there, and there's a gap at the other end as well.

**Dave Jones:** So, if you put it in without any sort of, like, alignment there, then you're gonna, you know, waste time in your production step, dicking around, trying to get all your holes, uh, to line up. You can end up stripping threads and doing all sorts of annoying stuff, as well as wasting time.

**Dave Jones:** And, yeah, um, that's a really nice touch. Anyway, uh, airflow thermal-wise, it looks like, uh, of course, uh, air comes out the back here like this, um, so it's sucked in, the sides here, and they've got one on the, uh, side here as well.

**Dave Jones:** Looks like that grill up there doesn't really do anything in terms of, uh, that. So, yeah, air's flowing over the heat sinks. The heat sinks seem to be in the right direction, like that. I can see down in there, they're in this way, so it's sort of, yeah, it's getting over the,

**Dave Jones:** uh, fins, and let's pop the hood on this. How does that uh, okay, I need to get a couple of ribbon cables out there. There's the power connector. There you go. We're in. There you go. We've got five, uh, major, uh, heat sink,

**Dave Jones:** heat sunk devices and two giant metal cans. Hang on one second. What's going on here? I thought this would be like an internal can. I could see. That was that grill I was telling you about there. That grill goes into this. It's sealed on this side, this side, and this side.

**Dave Jones:** So it's designed to get air, uh, out of this. So, uh, how? I don't get it. If the air's blowing out the back, what, it sucks some in? Oh, I think I get it. This is some sort of thermal gu- like, um, air

**Dave Jones:** duct guide for all this stuff on the top. Right? We're, we're, we're talking power supply here, and we're talking, uh, you know, well, here, over, this is in there as well. You know, there's a bit of heat generated in the, uh, function gen here.

**Dave Jones:** Although, this, this vent here, that doesn't do anything, because there's no matching vent on the outside here. So, I don't know why they added that, but, um, is that sort of like a change in design halfway through the process? We were gonna put, like, a matching, uh, vent

**Dave Jones:** on the back of the case, but then we decided after testing to change it, or go for a different thing, and they just left it. They didn't wanna, you know, change the, um, tool in for that, or whatever. So, yeah. I've never seen, like, uh,

**Dave Jones:** like, a power supply on top of this. So, on top like that, the fan here, so this power supply is cooled by sucking the air out of this. Is there vents on the side? Oh, yes. Yes. Look, there's larger vents on the side here.

**Dave Jones:** Okay? So, there's air coming in here, right? But only on one side. So, air coming over the power supply, and then to get it out through the fan, it's gotta go down into this vent, through, and then through here, like this. And then, and then it's guided, and sucked out through the fan here.

**Dave Jones:** Wow! Um, wow! This is just, like, really remarkable! It's so different to other scopes. I, I'm just finding this absolutely fascinating. So, there you have it. We'll have to take a high-res photo, and then do the, uh, talking Dave head thing, uh, once I remove, uh, the heat sinks here, but obviously we've got

**Dave Jones:** ADC, ADC, uh, and then the FPGA up there. Um, I don't think they have a custom ASIC in this. Uh, curiously, there's a lattice there. That looks like it's driving. Is that, like, a LCD driver? Maybe that's how they get fast. Do they, are they using that as sort of like a way to

**Dave Jones:** pump the, uh, waveform information directly into the screen? So, this is called the Atom. That's obviously their code name for this, uh, architecture here. But, uh, yeah. Really nice board. Liking the look of it. Um, so, let me get the cans off. Actually, these clips are

**Dave Jones:** not trivial to get off. I can't just bend them, and I, it looks like I have to like, maybe bend them a bit first before I can get them out. I've never had to do that before, I don't think. Alright, let's take a brief

**Dave Jones:** look at the board here in glorious 4K screen capture. And, uh, you can see here, obviously, ADC, ADC, they're National, uh, Semiconductor jobbies. Got the main acquisition ASIC here. Got the acquisition memory, well, actually, they're very different. That's the acquisition memory. And, that looks like

**Dave Jones:** some firmware for, um, a little processor core running in here, or something, presumably, cause that is, that part is very, very different. Check that out. So, yeah. Yeah, they're definitely different. And, as I said, we've got this lattice jobby over here, which is very close to, and you can see

**Dave Jones:** some resistors here, very close, this is the LCD connector going across. So, you've got to assume that that is somehow doing the mapping for the screen. And, maybe, you know, and my thought is, is that they're dumping, this is how the Keysight works, but the Keysight does it all in its, uh, Megazoom

**Dave Jones:** for, uh, ASIC. Um, they, it might just be using a direct dump in there like that to get the waveform data out of, well, out of memory, into, straight into the screen like that, and that might be how they're getting their fast waveform updating.

**Dave Jones:** Anyway, that one is not particularly grunty, cause it doesn't have a, uh, heatsink on it. And, uh, then, we've got a Xilinx, uh, zinc over here. So, yeah, um, I don't know why they need this, plus the zinc over here, and then, of course, the zinc has the

**Dave Jones:** ARM, uh, processor in it, and then it's got a crap ton of memory around there. So, so, yeah, it's a rather, uh, confusing architecture, and, and, obviously, this, uh, Spartan down here, this Spartan 7, um, is running the Linux operating system inside, presumably, um, or maybe, actually, no, I think

**Dave Jones:** no, the zinc would be running, the zinc would be running the thing. So, what's this Spartan 7 doing? Well, we can't see on the bottom of the board. Here's the logic analyzer connector down here, so maybe it's got something to do with that, perhaps?

**Dave Jones:** I don't know. Interesting. Anyway, um, that's basically all there is to it. Uh, the front end's, of course, the 350 MHz front end. Now, let's actually compare this to the, uh, well, you can still get it, um, it's not obsolete, but the non-HD

**Dave Jones:** version, which is the SDS, uh, 2000+ series, and I've done a video on that. I've done a Teardown video on that, and I'll have to link it in. So, here's, here's the two. We can swap between them like that, and you can see significant differences.

**Dave Jones:** They've got a, uh, smaller ADC down here, because, once again, this is an 8-bit, uh, dual channel, uh, Joby, as opposed to the 12-bit one that we've got now, hence the bigger heatsink and everything. Oh, right, this has a giant heatsink on it, and it's much more gruntier.

**Dave Jones:** We'll have, might have a look at the data sheet of that in a minute. And then, instead of, uh, having that one big RTX Capture FPGA, which is here, by the way, couldn't see it there, but that's actually an RTX, uh, 7XC7A 200T, 1156-pin

**Dave Jones:** Joby, thank you very much, uh, for playing. And, yeah, as you can see, that micron memory there is very different to this. So, we could have a look at that. I don't know who makes that, actually. So, yeah, instead of one big acquisition ASIC, they've got two of them, um, like that.

**Dave Jones:** And then, um, I don't think I, I don't think I took the, did I take the heatsinks off that? I don't know. You'll have to watch my previous Teardown video. Maybe I did. But in the high-res photos here, I don't have it. Anyway, I think that's, is

**Dave Jones:** that the zinc, uh, processor that the application's running on? And once again, they still have that lattice. So, it's a similar sort of thing. Acquisition ASIC, and then something else doing up here, and then the mysterious lattice one, which is that, yeah. So, there are significant

**Dave Jones:** differences there, but if we have a look at the front end, now we can actually compare the front end between the two of these, and the top here is the older one, and this is the new 12-bit jobby. And you can see that there's nothing in it.

**Dave Jones:** There's a few little, like, component differences in terms of, like, that transistor there is, like, flipped orientation and stuff. You know, just tiny little layout things like there, those, that pair there is like, if they are a pair, they're side to side, and they're offset a little bit here, but basically, um,

**Dave Jones:** oh no! Hang on. There's an extra transistor down there, which is not on here. But, geez, it's it's a very similar architecture front end. Slight differences in there. Um, there's their input termination resistor, and, you know, AC coupling and stuff. They'll have a, do they have a

**Dave Jones:** separate, uh, 50-ohm, uh, path and things, but, um, yeah. Near identical between the 12-bit and the 8-bit version, because, like, there's nothing special. Maybe it's slightly lower noise floor, but that would be, you would get that in a different part for your, uh,

**Dave Jones:** programmable gain amp here, and maybe, you know, some of the, uh, discrete transistors you use and stuff like that. But, you know, all the magic happens in the, uh, PGA here, the programmable, uh, gain amp. But, um, yeah, there's not, there's not really a difference in there.

**Dave Jones:** Um, and I can't quite make out the number on that one. Didn't get the photo in the right orientation, but there you go, that was the NatSemi jobby before, and we've looked at that previously, I'm sure. I don't know if I found the actual part, and it's

**Dave Jones:** got one of those obscure part numbers, I think. But there you go! So, yeah, all the magic, um, happens, of course, over here on the, uh, new, um, 12-bit analog-to-digital, uh, converters. So, we can have a look at that over here. Here's your PDF, and, uh, there it is.

**Dave Jones:** 12-bit, uh, 2/3.2 gig sample per second, ultra-high speed ADC, um, uh, May 2010. There you go, it's, it's nothing new, um, but you know, these would be pretty pricey. Oh, come on, they don't have it in the application down here, put crows! No, this oscilloscope rubbish.

**Dave Jones:** There you go, it's actually got programmable, uh, offset in there, that's pretty good. Wow, it's got programmable, uh, time adjust feature as well, so, you know, this is, this is really neat. Anyway, um, yeah, that's a dual, uh, channel one, but, and although this is a 2 gig sample per second, in fact

**Dave Jones:** I can do 3.2 here, it's configurable as either a 2 gig sample per second interleaved one, so, uh, you've got to use both, uh, channels or 1 gig sample per second, uh, dual ADC. So, um, yeah, if you're, of course, got channels 1 and channel 2 turned on here, both of these

**Dave Jones:** share the same ADC like this, so, uh, yeah, your sample rate's going to half if you turned on. This is why most scopes work like this. If you want your full sample rate, you use channel 1, and then channel 3 goes into a separate ADC.

**Dave Jones:** Now, somebody on the EEVblog forum actually asked, uh, why don't they have, or like, why doesn't channel 1 go into here, and channel 2 go into this one over here, and channel 3 go into that one, and channel 4 go into that one, so that, you know, most

**Dave Jones:** people are going to turn, if they're going to use 2 channels, they're going to turn on channels 1, and channel 2 here. Well, you can probably see the reason. It's basically, um, elegance of layout here. You can see that this is the differential pair.

**Dave Jones:** You can see it here. This is the differential pair running into the ADC, so this is the programmable gain amplifier, okay? So it converts single-ended, uh, input here, i.e., grounded, and it converts it into a differential, uh, driver, which then drives on this differential pair into the ADC like

**Dave Jones:** this. Now, of course, there's nothing stopping you routing that over to this ADC over to here like this, but then you've got to run channel 3 and cross it over like that. And you can see they're running the traces on the top here, and there's going to be a ground plane, inner ground

**Dave Jones:** plane layer, uh, below that, and of course these are controlled impedance, uh, traces, right? And so this is called a, uh, microstrip when it's on the top. You can actually route them on the inner layer, and then it's a strip line, but then you've got to use additional layers.

**Dave Jones:** I don't know how many layer board this is. Maybe we could find out, um, if they've annotated it properly somewhere, but yeah, anyway, um, yeah, you can actually run them on the inner layers as a, uh, strip line, um, and then you could actually cross them over like that, but

**Dave Jones:** it's just not an elegant thing to do. It's just, it's just not the dumb thing. So, like, you could, but it's just more elegant to simply, you know, run them like that. And then you've got to match the trace lengths like this, okay?

**Dave Jones:** So channel 1 has to match the length. This is why it doesn't go straight down here like this, okay? Because this path would be shorter than this path over here. So this is why they have to snake it around here. This is called, uh, length

**Dave Jones:** matching, and they're matching the length of the pairs like this. So the delay, the propagation delay of channel 1 is exactly the same as channel 2. So if you had channel 1, if you had the chips in this exact position, channel 1 would go over to here, and channel 2 would go all the way

**Dave Jones:** over to here. Sure, you could, like, add some extra snake around there to, like, match it, you know, you could do it, um, but it's just, eh, meh, it's just not very elegant. As a PCB designer, I'd go, and they wanted me to do that again.

**Dave Jones:** Really? Really? You want me to do that? Why can't we just get the user to, you know, plug into channel 1 and channel 3? What's the problem? Anyway, check it out, we have a power and reset switch over here, so that's interesting. They've put that on the board,

**Dave Jones:** so obviously, you know, you can do lots of board-level, uh, debug and stuff like that. That looks fun. Um, have they got a, uh, JTAG? Yeah, is that a JTAG up there? That looks like a JTAG port, so knock yourself out. There, there's another JTAG.

**Dave Jones:** There's a serial. There you go. You wanna get a serial dump out of this sucker? I won't do it in this video. Um, there's another JTAG? 3-pin? What's going on there? Is that, no, that might be some sort of jumper, or something like that.

**Dave Jones:** Curiously, that one's not labeled and all the other ones are, so, eh, don't know what's doing there. Anyway, power supply-wise over here, uh, you can tell it's a power supply because, well, it's got a nice, big, fat, chunky chip there, which will have, uh, the built-in, uh, you see there's no external MOSFETs there, so it's got big

**Dave Jones:** chunky internal, uh, MOSFETs, and of course you can tell by the, uh, decoupling there as well. There's a little, uh, 3.3 volt linear, uh, reg there, and they've got a few of these, actually. There you go, it's an MP. Is that an MP52145?

**Dave Jones:** You can go look that up if you want. Anyway, that looks like the USB there, is it, perhaps? And our logic analyzers here, so there's probably some logic analyzer stuff on the bottom, I would guess. And this is the board-to-board interconnect, which goes over to that, uh, rear panel, and of course that, uh,

**Dave Jones:** coax, which goes over to the, uh, function gen. Got some old school for a HC4051, analog MUX, nice. And what is that? Anyway, there you go, it is a very interesting architecture, one capture FPGA, uh, the, yeah, this Spartan 7, has that got a, uh, it's, I reckon that's got a processor on it, let me check

**Dave Jones:** that. No, the Spartan 7 doesn't have a hard, um, arm processor, it only supports, like, the software micro-blaze, uh, processor and, uh, stuff like that. So they should, could be running a micro-blaze core in there, but, I don't know. Eh. But of course the zinc here, the zinc bad boy, we're seeing this in all tons

**Dave Jones:** of, every modern oscilloscope uses a zinc, uh, FPGA slash, uh, processor in it, and they're pretty grunty, and, um, yeah. No whackers. But it's interesting that what that actually makes Xilinx and Lattice here, so, I don't know, maybe they've got, like, previous, um,

**Dave Jones:** previous design tech that they reused, on their more modern, um, scopes here? That's the Mark XO, uh, family, it's only got 640 lookup tables, uh, 6K bits of distributed RAM, ha, when I was a boy I would've killed for that. Is that a lead?

**Dave Jones:** I think it is. It's a heartbeat lead, is it? Some oscilloscopes, uh, we've seen, I think, aren't they just like the zinc, like this, ADC, straight into the zinc, 'cause in theory that's all you need, right? 'Cause inside this zinc they're pretty powerful, it's got the ARM processor, uh, the hardcore ARM

**Dave Jones:** processor, none of that softcore rubbish, hardcore ARM processor that runs the operating system, uh, runs the, you know, Linux or whatever, uh, that this thing's working on, and then it's got the FPGA fabric to do all the capture. So that's the Atom there, it's their, I guess, their new architecture, so maybe

**Dave Jones:** expect new scopes to, like, be based on this particular architecture, and then maybe the ADCs are gonna vary, which, uh, feed into here, but, yeah, maybe all the new scopes, but, um, yeah, this is quite a significantly increased price point compared to the Rygols.

**Dave Jones:** I know this one has, you know, it's got the function gen, it's got the logic analyzer, and, you know, it's, it's more better-er, but it's not like it's massively high sample rate, it's only 2 gig sample, uh, per second, and, uh, well, yeah, I mean, the, uh,

**Dave Jones:** 4-channel Rygol, um, HD, 4-channel Rygol starts at $999. This one is, what, $3200 US, uh, dollars, of course, and even the, uh, Rygol 4000 HD series, they've just changed the name of it, I think it's the DHO now instead of the HDO, like, why?

**Dave Jones:** They've, they've, they've changed it since I've done the video on that, I don't know what the deal is there, uh, differentiation, market differentiation, I don't know, search term optimization, I don't know, anyway, it's the DHO 4000. So, yeah, it's, um, significantly more pricey, so if you're looking for a

**Dave Jones:** budget-conscious, uh, 12-bit, um, entry level, um, this Siglent's not it. Rygol are absolutely killing that market, aren't they? There's others on the market as well, uh, that, I think, sort of like the Ness- lesser name brand, but, you know, Rygol and Siglent are now

**Dave Jones:** almost, you know, nipping at the heels of the top-tier manufacturers, they've got some really high-embedded kit, and Siglent have been killing it lately, um, and, yeah, I'm, I'm very impressed by this, uh, design, and, uh, they've put a lot of effort into it, and by the looks of, uh, we saw

**Dave Jones:** in there, um, also that it was rebadged for LaCroix, uh, as well, and, of course, Siglent have made LaCroix, uh, scopes before, that's nothing, uh, new, but LaCroix are obviously gonna badge this, and maybe they just, yeah, um, they're shooting for a higher, uh, price point market,

**Dave Jones:** and, and the alloy handle! Yes! Please! Manufacturers, can we have alloy handles for everything? Fantastic! Anyway, if you enjoyed the teardown, give it a big thumbs-up, as always discussed down below. Catch you next time!
