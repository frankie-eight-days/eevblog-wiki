---
video_id: HBBGl_dHqAU
title: EEVblog #1100 - Dumpster Photocopier Repair
url: https://www.youtube.com/watch?v=HBBGl_dHqAU
source: youtube-asr
timestamps: {"0": 0, "1": 37, "2": 59, "3": 80, "4": 99, "5": 126, "6": 146, "7": 180, "8": 198, "9": 216, "10": 232, "11": 266, "12": 284, "13": 305, "14": 321, "15": 350, "16": 373, "17": 403, "18": 432, "19": 468, "20": 502, "21": 530, "22": 560, "23": 590, "24": 623, "25": 654, "26": 686, "27": 703, "28": 719, "29": 751, "30": 770, "31": 800, "32": 818, "33": 838, "34": 855, "35": 872, "36": 893, "37": 925, "38": 957, "39": 982, "40": 1002, "41": 1043, "42": 1065, "43": 1087, "44": 1115, "45": 1146, "46": 1161}
---

**Dave Jones:** Hi, check out my latest dumpster find. It's a Fuji Xerox Apeos Port, whatever on earth that means, 3 C2201 for those playing along at home, and it's a gigantic A3 photocopier. And the great thing about these is that they all they they weigh a ton, they come on the wheels. There's actually some supports on there so you can actually, you know, level it out and stuff once you get it into the office, but it actually looks in really good nick. I believe it dates from well, I don't know when this one

**Dave Jones:** was made, but it it dates from like 2008 or something like that, 2008 vintage, and well, let's power it on and see if it works. This is not the first photocopier I've got in the dumpster. Let's turn the lights off there. So, there we go.

**Dave Jones:** All right. It's going to work. Focus. All right, here we go. Conveniently, the switch is on nice positioning. That's really good design choice. Somebody was thinking there. Here we go. Cross your fingers. So, although it could be like up to a decade old, it's probably not that old, but that's when the model dates from.

**Dave Jones:** These things usually have quite a long longevity. They sell them for quite a long time. It's not like they, you know, replace models every 9 months or whatever, so anyway, mine's power switched on. We'll see if it works. It it doesn't seem to have like a a lease thing on it, so I don't think it's like an ex-lease.

**Dave Jones:** The companies usually take them back. Whoa, hello. We had something. Hey, the screen looks a bit How are you doing? It's it got a Uh, no. Yeah, the screen doesn't look terrific, but it's there. It's whirring. Doesn't I can't see a contrast pot. Come on. It's making the requisite noises. Nothing hideous. There's a biograph there.

**Dave Jones:** Oh, yep. Yep, the screen is a bit washed out. It's just like poor poor angle. Yeah, oh, something beeped. There you go. To begin, select a service. We're in like Flynn. Um calibration setup How do you uh machine status Here we go.

**Dave Jones:** Uh machine serial number, IP address. Um I do believe it has Windows 10 drivers. That's what it looks like on the website anyway. Um print reports. Hello. McFly No. No, maybe the touch screen's gone. The screen does not look good. So, maybe that's why they ditched it. No, yeah, close doesn't work. Okay. Yeah, the touch screen touch screen's died. See if it actually See if it copies.

**Dave Jones:** You can typically Can't get out of that. Interrupt? It's got an old ETI magazine. There you go. Just so happen to have it lying around. And And can we just do start? No, because it's copy email Hey, there we go.

**Dave Jones:** Copy. We're in. We're in. We should auto paper select. Paper select is unavailable. Please select a paper tray load the following paper. Auto. I want some uh It's really annoying. Still don't know if it works or not. Oh, I come on. There's no arrow keys.

**Dave Jones:** Can't manually override this thing. What a bummer. Well, let's not muck around. Let's go straight into it. There we go. We can just take off the front panel like that. It's got it Oh. Is that tape cable pull out conveniently?

**Dave Jones:** Anyway. Yeah, yeah, there we go. I can just unscrew that. Check that out. Nice. So, we can go work on that separately. Ah. Brilliant. What a Bobby Dazzler. And we're in like Flynn. Let's check it out. Here's our main board here. We've got our backlight driver there. That could be Well, it could be the CFL tube in there that's going. Maybe you can Maybe you might be able to pump up the voltage on the backlight or something to compensate. But anyway, the screen still works. What we're concerned

**Dave Jones:** about is the touchscreen. And of course, here's the LCD ribbon going off here. We've got all Looks like we've got all our diff pairs running here over to the LCD driver. Would they need diff pairs for that? I don't know, but anyway, they seem to be running them.

**Dave Jones:** And here is your touchscreen. The foot classic four-wire resistive touchscreen. Looks like we got some discrete trendies and diodes around there. So, that's rather interesting. Looks like we have ourselves a five-pin voltage reg there. But I'm just going to uh have a little fiddle around with this.

**Dave Jones:** Measure it. Make sure it's okay. You know, we can get the meter on that and then play around with it and we should be able to see if that's okay. And if the actual touchscreen itself is okay, like there's no breaks in the ribbon or you know, anything else that's gone wrong. Then we might have a look at the circuitry.

**Dave Jones:** Let's just have a probe around there. Half a K. Sounds reasonable enough. 6.7 K. Oh, yeah. Okay, the great thing about this cable is that I can put it on a stand here and work. And they've actually got voltages on the various test points here. Like for example, they've got 3.3 volts here. So, the supply can measure that.

**Dave Jones:** 3.335, no wuckers. And uh uh there's one labeled 4.75. That's actually 5.01. So, that actually sounds okay. Like it's a 5.5 V power supply. Why they put 4.75? That just happens to be the exact uh tolerance of a general 5 V power supply.

**Dave Jones:** So, 5% low. So, maybe it's sort of like some minimum voltage, but I wouldn't worry about that. So, the supply voltages are actually uh they look okay, and there doesn't look to be any physical damage to any other uh components or anything like that. So, that regulator's good. The supply rail's good. Obviously, all the LCD driver and other uh circuitry is all uh working fine. It's just the uh something to do potentially up here with the uh touchscreen.

**Dave Jones:** And if I get in there and actually measure one of the pins on the resistive input, and then I touch the resistive screen, bingo, we've got a change. So, something is changing. That's good. Um so, it should be registering at least something on the screen even if it was like uncalibrated out or something like that. It should be like pushing at least random buttons.

**Dave Jones:** Well, check out the bottom of the board here. Look, I'm surprised they're uh double-sided populated this. Look, they've actually uh wave soldered and check out the uh pads on there. You can see how it like sort of snakes off there. It's not just directly on. That's really quite unusual. Is that some sort of uh solder thieving um type uh system? Anyway, you can see the uh glue under the components down in there. And um yeah, well, the transistors I've checked all the diodes on the top here

**Dave Jones:** and they're all okay. Um they all buzz out. Looks like there's two different types of uh diodes in there. And I assume that they're um some sort of uh little mosfetty uh type thing. Perhaps, but uh yeah, it looks like there's some residue on the board. Check that out. It almost looks like they spilled something on there, but there's absolutely no damage like anywhere else. So, I don't think so. I think that just uh comes from the factory like that. Looks like this, you know, some water or something is is

**Dave Jones:** spilled on there, but that's just uh they just haven't bothered to clean that, I suspect. Okay, sorry, but this is uh actually impossible to film, I think. Um I actually just barged in a touchscreen which had almost the same pitch on there. I think it was I was trying to think it was the same pitch. Pretty close, but it had a tiny little cable, but I can get my fingers under there and I was able to uh get the screen. I put it in like the

**Dave Jones:** email mode or something where there were lots of different uh things on the screen and I was able to get it to respond um to my touches. Of course, it's not going to be calibrated properly for this particular resistive uh touchscreen or whatever, but it kind of shows that it you know, the circuitry is probably working and doing its thing. So, it looks like the it it is um possibly that uh faulty touchscreen on the uh panel itself. Now, I'm just trying to uh get everything disassembled

**Dave Jones:** here. It's a bit of a uh pain, but take a look at the keys, what they have to go through to uh uh do this. Here's the uh Here's the board, of course, you know, it's got uh tactile um switches on there, right? But look at the effort they have to go to to uh That's just a it's just a thing to keep out spillage or whatever coming through I guess all sorts of crap coming through the keys you know cuz everyone's drinking their coffee and eating their

**Dave Jones:** muffin around the copy machine stuff like that anyway look at all the you know the intricate moldings that they have to produce okay that's all in one big thing but like you know this individual button here with these little retainers that one's a different size and a different color to this one here I don't think they fit do they no they're actually different so the price you pay for wanting a stylish button which is slightly bigger than this one here they could have reused the same molding no got to do a different

**Dave Jones:** one no got to do a different one up here for all this got to do this one down here just for that one button like they have to design and get those manufactured it's just you know ridiculous the effort they go to but I guess that's you have separate teams that do this one that you know a marketing or product design team or whatever that actually you know designs the look and feel of the thing and then you know the poor implementation engineers have to go oh

**Dave Jones:** god I got to get another separate molding for that unbelievable I'll tell you what it's quite a bit of a convoluted system they got some screws on the front you have to get this front cover off first but to do that you've got to get the back part of the back cover off first and it's just all rather complicated um so yep it's all weird but anyway we should be able to now if I can we should be able to take all this out and access the touchscreen tada

**Dave Jones:** cheers what a mess I hope I can remember how that all goes back together okay hopefully you can get this I don't want to breathe, but watch it. I'm probing like the bottom two pins there. And look, look, if I move this, look at that.

**Dave Jones:** And I can actually get it to come good. All right, so if I get my finger on the bottom, touch it, slide it along like that. There you go, it's changing. But if I move it, yeah, I can get it to go open. There you go.

**Dave Jones:** So, there's definitely something wrong on here. And I suspect um I I'll have a good look under the uh microscope at any like micro uh cracks or anything in the uh copper on there. But uh it could very well be the hot uh bar uh attachments on there. So, I might be able to just uh maybe reheat those, but let me go have a look under the microscope. So, just as a matter of course, one of the things I'm going to look for is any uh micro cracks on the

**Dave Jones:** uh copper or anything like that, and that all looks okay. So, so if we actually get a good resistive uh touchscreen, this is on the back of uh one of these um 4D uh systems things, then we'll notice that the uh the way it works is exactly the same.

**Dave Jones:** Pins one and two have nothing. Pins one and three have a resistance. Pins one and four have nothing, but pins two and four also have a resistance. So, that's exactly the same as we're uh measuring on this one. But as you saw, I think it might have some sort of uh you know, uh crack or something like that that's stopping it um from doing that.

**Dave Jones:** Okay, it seems to be doing the business now. And if I touch it, then it obvious and then it can vary. There we go. Like that. So, um all four wires seem to now be functional. But, uh anyway, I might sort of cobble it back together.

**Dave Jones:** Um see if it works now after uh sort of like, you know, heating up all those pins. Maybe it was some intermittent contact that broke it that didn't get the uh XY coordinates required. So, therefore, it just didn't respond. All right, that's nicely cobbled back together. Should work a treat. Let's turn it on.

**Dave Jones:** And uh it should all power back up. Yep, screen's upside down though. All the electrons are going to fall out. Uh sorry, you probably can't see that. The contrast I don't think is terrific. Hey! Hey! It's doing stuff.

**Dave Jones:** Have we fixed it? Can I go near the top? Sorry, I don't know which orientation's what. Okay, I'll try and line the screen up on here. Oh, there we go. Yep. Yep. There we go. Close. Got it. Yep.

**Dave Jones:** Uh copy. Yep. It's working. Beautiful. Paper select. That's the one I want. If I CAN PRESS START. AH, WE'RE ON OUR WAY. IT'S SCANNING. OH, NO, I didn't have the magazine in there properly. It should HAVE COPIED SOMETHING. YES!

**Dave Jones:** WINNER, WINNER, chicken dinner. And yeah, there's no no uh fuser um problems on there. The toner is all fused. It was a dead touchscreen. Reheating the connections down on there. I just used an iron at uh 260° uh no no solder on it. That's that's probably like actually conductive adhesive on there rather than a reflow soldered under there. I believe it, you know, probably just something like that. Anyway, I just heated it up and it seems to it now work a treat. You beauty. Going to put it back together

**Dave Jones:** now. It doesn't mean it still could not be intermittent or something like that. By the way, it actually came with this cable here which goes into this empty port under the paper clip thing here. So, I'm not sure actually what went under there, but it came supplied with the cable. Man, okay, we'll just try it before I put the whole back cover on and then whack it back on.

**Dave Jones:** Uh screen contrast Hey, winner winner chicken dinner. There you go. Turn up the contrast. Turn it down. Maybe looks a bit better down there. Save that. Ah, we're back in action. It's just like a bought one now. Machine status. Print reports. Here we go. Configuration Please read the report what you want to print and press start. Oh, look at that.

**Dave Jones:** Beautiful. Okay, that's a configuration report. blah blah blah Oh man, going to run out of paper. Okay, we want to check faults. Error history report. Why can't I just display it on the screen? I don't Maybe there is and I I don't know. Whatever. Couple of jams back in 2017.

**Dave Jones:** Wow, what nothing since 2017? That's all right. And 50% remaining black, 75% cyan, magenta, and 50% yellow. Beautiful drum cartridge all okay waste toner all okay. Awesome. There you go. That is like a bought one. I did it was just set to standard image enhancement and everything else, but that looks to work just fine. And tada, there's inside the main processor board which just pulls out. You undo screws, comes out. We've got all the memory and whatnot. Looks like we've got a like a separate real-time clock chip. And

**Dave Jones:** there's the hard drive. Yes, it does stores everything it copies, apparently. Um that's just a regular SATA drive, so when you toss these things out, you want to erase the hard drives. Anyway, um huge Freescale uh part down in there. Um and some custom Fuji Xerox stuff.

**Dave Jones:** Absolutely enormous. Like uh whether they you know custom ACs, they could very well be. They um these they put a lot of engineering into these things. Absolutely remarkable, but yeah. Mhm, nice, huh? Ton of engineering goes into photocopies. It's unbelievable. So, there you have it. Repair successful.

**Dave Jones:** Beautiful. It's classic dumpster find. And turned out to be a reasonably interesting repair. Just a touch grainy. That's why they threw this thing out. They couldn't be bothered. It was probably already 10 years old. I still don't know the manufacture date of this thing. Probably not that old, maybe 8 years old or something. And it obviously it looks like it works fine. I haven't tested like the ethernet and functionality and everything else. But apparently I can get Windows 10 drivers for this thing. It's got A3 capability.

**Dave Jones:** It's got like four paper trays on the thing. Absolutely amazing. Full color. And it's it's a pretty reasonably modern photocopier. What's that bracket? Don't know. Just a random bracket. I think that that was on there when I got it from the dumpster. Haven't tried like the feeder and stuff like that. I don't know. Maybe it could have been having issues. But the fault report was pretty good. So, it looks like it was just the adhesive, the conductive adhesive holding that flat flex strip down to the

**Dave Jones:** glass on the LCD. And just I just heated that up. There's probably other ways to repair our stuff like that. If you do that a lot and let let us know how you repair it, but I just heated it up each one and it came good. No worries.

**Dave Jones:** Winner. So, if you like that, please give it a big thumbs up as always. Discuss down below. Catch you next time.
