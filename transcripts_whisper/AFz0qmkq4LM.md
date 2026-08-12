---
video_id: AFz0qmkq4LM
title: EEVblog 1592 - Fluke 287 Multimeter Teardown
url: https://www.youtube.com/watch?v=AFz0qmkq4LM
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 13, "2": 30, "3": 49, "4": 66, "5": 83, "6": 104, "7": 122, "8": 142, "9": 155, "10": 168, "11": 185, "12": 201, "13": 220, "14": 240, "15": 256, "16": 278, "17": 299, "18": 314, "19": 331, "20": 352, "21": 371, "22": 388, "23": 404, "24": 421, "25": 440, "26": 456, "27": 474, "28": 487, "29": 503, "30": 520, "31": 534, "32": 556, "33": 573, "34": 594, "35": 611, "36": 627, "37": 649, "38": 671, "39": 702, "40": 719, "41": 735, "42": 760, "43": 776, "44": 793, "45": 812, "46": 829, "47": 842, "48": 859, "49": 875, "50": 890, "51": 905, "52": 923, "53": 939, "54": 957, "55": 974, "56": 991, "57": 1002}
---

**Dave Jones:** Hi, time for a quick teardown of this Fluke 287 True RMS Digital Multimeter that I scored on eBay. I was hoping it would be faulty, and I'll link into a second channel video up here and down below if you haven't seen it. And, well, yeah, it's not faulty.

**Dave Jones:** It works just fine and dandy. So, let's take this thing apart, because I've never taken apart a Fluke 280 series before. We've got the infrared window down here. Haven't tested that. And it's your traditional over-molded design like this. I'm not a fan of the tilting bale.

**Dave Jones:** When I first got it, when I first started to use it, it just fell off. Is that normal? I don't know. They've just got, looks like, just these little knobbly things here, and then the tilting bale just sits in there like that. But that just easily comes off.

**Dave Jones:** I don't like that at all, so I'm not impressed by that. Have I just got a dodgy one? Don't know. Anyway, the back of it. All they've got is two hooks up here, and just one of these, you know, battery thumbscrew things down here.

**Dave Jones:** And we'll lift this off, and there you go. There's our battery pack in it. Six AA cells. I did actually bend one of these contacts here when I actually first took it off. Now, interestingly, they've got three terminals in here. I'm not sure what that's for.

**Dave Jones:** I would maybe for a rechargeable pack solution. Maybe, but then how do you charge it? I'm not sure, like, because the extra terminal would often be like a temperature thing or something. Anyway, we've got our two HRC fuses there. They're easily replaceable, so looks like we've got two, four, six screws holding this bad boy in.

**Dave Jones:** So let's take it apart. Yeah, we may have to void the warranty. We'll just slice that off, shall we? Unfortunately, the comically long screwdriver doesn't fit. Oh, bummer. Gonna have to get a different size. So will this... Does this have, like, an MSP430 processor like the other Flukes do?

**Dave Jones:** Because Flukes transitioned over to the 430 a few decades ago. It's been a long time. But I don't know. Or do they need something beefier to do the big graphical display? One thing I am disappointed about with the... They do have the trend thing in this.

**Dave Jones:** Time and date need to be reset. So, yeah, I believe this has a super cap in it. So that might... I don't know. That might need replacing, because the batteries were out while I was just shooting this intro here. But it wasn't for that long.

**Dave Jones:** But anyway. Okay, one thing I wanted to show you here is let's just go into record mode here, okay? And we can record like this. So I've got it set for one second recording here. And if we start that, okay, it's going to sample once every second.

**Dave Jones:** And there it goes. Two, three, four. And this thing, of course, famously has the graph trend plot or whatever it is they call it. But I don't believe you can actually do it. I have an RTFM, RTFM'd. But I don't believe you can actually do it until you actually go, until you stop it.

**Dave Jones:** And then you can go trend. Like that. I, like, why? Is there some firmware upgrade that allows you to do it live? But anyway, I find that really annoying. Anyway, I would consider that a bit of a fail, really. They go to effort to have the nice trend plot capability.

**Dave Jones:** Then you can't do it live. Like, that's just ridiculous. Come on. Seriously? That's our last self-tapper there. So, let's get the, can we get it apart? Is it just going to, it's going to do it without a fight? Or are they clips? There could be something up the top here.

**Dave Jones:** I sense great disturbance in the force up the top. Oh, there we go. Got a spudger in there. And we're in. Oh, look at that. There you go. Nice plastic work there. I rather like that. And those integral. Oh, battery contacts there. They're beautiful.

**Dave Jones:** So, yeah, very happy with that. And inside, we're immediately presented with this nice big shielded plastic here. This will be a conductive plastic. I'll prove that to you. Get the baby fluke jobby here. And there you go. There you go. 50 ohms, 40 ohms.

**Dave Jones:** Yeah. So, conductive plastic. So, let's get that off. And another self-tapper. There you go. We are in. Beautiful. All right. Look at that. Wow. And immediately, let's go straight down. I can't read this on the bloody camcorder screen. And, yep, that is indeed an MSP430.

**Dave Jones:** So, there you go. And, of course, the graphics processing, it's not actually doing all the graphics processing. It's probably like a, that looks like a serial interface over there. Buggering off, is it? Anyway, there's our hybrid resistor network there. There we go. We've got another ceramic resistor network there.

**Dave Jones:** That's just the high voltage input resistor there. Of course, this is Cat 4, 600 volts. Cat 3, 1,000 volts. So, it's going to have pretty decent input protection and space in everything else. And we see that here. We've got the isolation slots all around here.

**Dave Jones:** We've got our fusible input resistor here. We've got a PTC. We've got three MOVs. They're not huge, but there's three MOVs there. There's our 10 amp current shunt. And I'm not seeing the diode e-bridge for the fuse protection. Usually, you have one of those.

**Dave Jones:** Could be on the other side. There's another PTC up here that's missing. So, that's interesting. But, anyway, there you go. And they've got just an isolation slot under the input resistor divider there. Very nice. A whole bunch of miscellaneous stuff. And there's our little super cap over there.

**Dave Jones:** Is that a super cap or a battery? I've been told it's a C. Yes, it's C. It's got C145. So, that's actually, they're using that as a super cap there. And there's our buzzer. And there's a couple of unpopulated footprints up here. What's an E-net 1 and an E-net 2?

**Dave Jones:** Does anyone know? Is this like some sort of expansion model thing? I don't know what the 289. I don't know the exact difference offhand between 287 and the 289. But, anyway, that's interesting. And there you go. We're going to have the transmit and receive LEDs there.

**Dave Jones:** Because I think you can do, it's, you know, bi-directional. You can set calibration and do stuff. Got our large pads for the battery and whatever that extra terminal there is. I'm not going to go through and reverse engineer everything. There's no point in that.

**Dave Jones:** Some nice golden guard traces there. If I get them at the right angle, they'll be nice and shiny. Look at that. Beautiful. Yeah, so they're guard traces to stop any, you know, leakage on the board. Very nice. And, of course, the rotary switch down here,

**Dave Jones:** that looks pretty schmick. This looks very different, doesn't it? Like, I don't know, I rather like that. Anyway, is that dual wipe contacts down in there? It looks like it possibly is. But we can get the, we can get the board out. And, of course, you can view this in, I'm shooting this in 4K resolution.

**Dave Jones:** So we can actually do this. Like, I could put this under the Tagano microscope. But, you know, and then we could go around. But, unfortunately, the Tagano microscope's only 1080p. It's not 4K. So, yeah, if you want 4K, I've got to actually shoot high-res photos

**Dave Jones:** and then do my talking head screen capture. I find it interesting how the side of the case is actually transparent. It's actually a transparent plastic that they've put the rubber over mold over that. So that's rather interesting. And I really like the look of these input jacks here.

**Dave Jones:** They look pretty. They look pretty schmick. So I'm going to have to get those out, I believe, to take the board out. But very nice. Spare no expense. Really spectacular. Spare no expense. All right. So let's flip this board out. That just comes out.

**Dave Jones:** There was just one screw there, which was the same as all the other self-tapping screws. Ah, check it out. No, no, no, no, no, no, no. We have another processor over here. Anyway, oh, I like how the rotary switch is like, oh, wow.

**Dave Jones:** You know, that is different. That is different to other flukes, isn't it? That's really rather groovy how they've implemented that. I really like it. It's like a two-sided thing. And there must have been a screw access from the other side, which I couldn't see deep down in there.

**Dave Jones:** So you could take that off. I'm not actually going to take that apart. But that looks pretty schmick. So anyway, I was talking about the diode bridge before. Yeah, there it is. It's on the bottom. I've done a video on multimeter input protection.

**Dave Jones:** So I can link. But no, look, look, we have a free scale processor down here. So the MSP430 was just doing the, they were leveraging the MSP430 tech, which they have on their existing multimeters for just doing the multimeter functionality. And then all of the graphics and all the data logging and all the whatnots is done by this.

**Dave Jones:** I can't see it here. I can't see that on the screen here. I'll put it up here. And then it looks like we have two memory devices. And is that our flash? Flash chip. So that's pretty grunty, isn't it? This thing does have 100 hours battery life, nominal, and actually 200 hours in logging mode.

**Dave Jones:** So I presume, you know, because it samples slower than in regular multimeter mode, it chews like half the power. So anyway, that's interesting, is it not? So this is a REV15. That, is that the reference? Is that our reference? I suspect that could be.

**Dave Jones:** That could be our reference. Just looking at that, it looks pretty important, um, perhaps. Got another analog devices jobby there, can't read that on the camcorder screen. There's another conductive plate, so that's sandwiched between there. And look at this! Look at the key!

**Dave Jones:** Look at the, for the keypad thing! It's like a waterproof thing with like a whole plastic, clear plastic enclosure there, isn't it? Why have they gone for clear? Does anyone know? Leave it in the comments. If you got any idea, anyway, there's the, uh, LCD there.

**Dave Jones:** You can actually buy, uh, replacement, uh, LCDs, like screens and whatnot for these, but, uh, jeez, that's, that's really nice. I, yeah, uh, there's our infrared, uh, transmit and, uh, receiver there, so, all right, you know, I'm gonna take some high-res photos, as always, available on evblog.com via my Flickr account.

**Dave Jones:** So yeah, I'm thoroughly impressed with the construction of this thing, and what does it look like? Is it like a 20-year-old design or something like that? Just everything about this, um, screams, uh, quality, spared no expense, and, like, look at all the, uh, shield in here, and then we've got the, does that, no, that's all, okay, so that's all part of the case there.

**Dave Jones:** So the Rubber Baby Buggy Bumper keys there, um, they're just on the front there against the, uh, like, transparent, um, front case on that. It'd be cool if they actually did a transparent case. I don't think they actually did a transparent version, because, uh, they did release a transparent case version of the, uh, Fluke 87 at one point, but, anyway, um, there's our switch, uh, range switch, uh, down there, that's your classic implementation of your, uh, Fluke switch, um, it's, like, a lot of people copy that, too, so, yeah, it's, uh, works a treat.

**Dave Jones:** I really do like the implementation of the, uh, the actual mechanism itself there, that's, that is really quite nice, and, uh, yeah, I think there might be a, I can't see it. I can't see down in there, but I guess there's a screen, put a tiny screwdriver down there, and you can take that off, can you?

**Dave Jones:** But I'm not going to, sorry. Anyway, you can see all the rest of it around here. What are these? I can't read them, but I'd be guessing, uh, you know, 4051s, um, something like that, perhaps, uh, some 4000 series, uh, Muxi-type stuff happening.

**Dave Jones:** See, you guys have the advantage of being able to watch this on your big screen monitors, uh, and, you know, in the glorious 4Ks, and I'm... like watching on this little piddly two-and-a-half-inch, three-inch, uh, camcorder screen. Can't see a diddly squat. And we've got a little plastic, uh, sheet there, so that, uh, it doesn't, so that the rain switch up here doesn't rub, so that's nice attention to detail, so...

**Dave Jones:** kind of put that all back together. That's really groovy. That is really quite nice. This, uh, meter, worth every cent from a, uh, design and build quality point of view, that's for sure. Though I'm surprised that they don't have any... Loctite on the screws holding in the connectors.

**Dave Jones:** That's interesting. Um, yeah, I'd, uh, I'd like to see some Loctite on there, pretty please. But, I guess it hasn't been a problem for them. I don't know, leave it in the comments down below, but... There you go. Beautiful. And just a quick one, we do actually have the schematic here.

**Dave Jones:** It's not for the, uh, 280 series, but it's for the 189 series 2, which this one, uh, came from. They just, uh, discontinued the 189. It became the, uh... 287, 289, basically. So, I do believe it's pretty identical. So, um, yeah, let's actually just have a very brief look.

**Dave Jones:** Here's our, uh, front end here, of course. So, here's our, uh, like, there's our current shunter, 10 amp current shunter down there. I've done videos on, uh, front ends like this. There's our diode, uh, bridge protection. Got some extra clamp in here. Looks like LM4141 is our, uh, reference there.

**Dave Jones:** And then you just calibrate it, uh, out. So, it's all about the, uh, Temco. Um... Stuff. Then they've got that milliamp jack, uh, sent in here. And here's our input jack here. Here's our, uh, fusible resistor. We've got our high voltage resistor here.

**Dave Jones:** We've got our, uh, PTC here. And then we've got three MOVs there like that, uh, in your classic arrangement. And, you know, you've got range switch stuff happening up here. Looks like they've got some, uh, Zener, uh, clamping there. That's interesting. Got some more clamping action happening here.

**Dave Jones:** And here's your main, uh, Fluke chipset, which you saw next to that, uh... Uh, hybrid, uh, divider network, which is actually here. That's all, that's, uh, Z2 there. So, those resistors are all, uh, thermally matched in the, uh, ceramic hybrid. That's why they put them on the, uh, ceramic there.

**Dave Jones:** And it looks like they use an LTC1968, uh, for the true RMS, uh, output there. That's got 100 kilohertz, uh, well, the meter has 100 kilohertz bandwidth. Um, yeah, there, there's some 4053s, which I noted before. And there's our MSP, uh, 430 processor.

**Dave Jones:** So, they're just using it, like, as a regular. Fluke multimeter. They're treating it as a regular Fluke multimeter. And they basically bolted on, uh, the bigger, badass, uh, processor on there to drive the LCD and do the, uh, data logging and, uh, the whatnot.

**Dave Jones:** So, you know, there's some more 4053 action. That's the ADG714, uh, marks that was on, uh, the bottom side of the board. And this is, uh, decoding the range switch here. So, they actually do that using, uh, voltage. So, they have a little crude ADC there, and they can measure the, uh,

**Dave Jones:** the value and know which range switch position they're in there. And here's the main processor, and it's an MC93, uh, 28. And we've got the extra memory over here, and we've got the ROM here. And, well, that's about all she wrote. There's a for development header down there.

**Dave Jones:** And, um, yeah, they actually, um, those expansion things, that's an Ethernet. Ethernet connector. Ethernet interface for development. Um, I, okay, made development easier, but, uh, yeah, it wasn't used for anything else. Then, you've just got all your fancy-pantsy power supply stuff, and, uh, Bob's your uncle.

**Dave Jones:** Ooh, LCD drive down here, uh, classic arrangement, giving you the different levels, um, for the, using LM32, well, LP324, it's low power, not that high power, um, LM, rubbish, um, for the, uh, LCD there. So, there you go, quick teardown of the Fluke 287.

**Dave Jones:** If you liked that as much as I did, please give it a big thumbs up. As always, discuss, uh, down below, and over on the EEVBlogger forum, of course, where all the test equipment nerds hang out. Catch you next time. And just a pro tip, when you're putting screws back into, uh, plastic cases like this,

**Dave Jones:** what you do is don't just put it in, don't just whack the screw in, and then start screwing, 'cause you can strip the thing. What you do is you just turn it backwards, like this, until you can feel it drop into the existing thread,

**Dave Jones:** and then screw it into the existing thread, 'cause you don't want to cut a new one. Turn it back, turn it, oh, yeah, there we go, got lucky, and that just screws in really, really easy, peasy, lemon squeezy.
