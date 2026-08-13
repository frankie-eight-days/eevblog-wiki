---
video_id: gzbTXQlxuyo
title: EEVblog #946 - Apple (Raspberry) Pi Cluster - PART 2
url: https://www.youtube.com/watch?v=gzbTXQlxuyo
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 47, "3": 66, "4": 85, "5": 104, "6": 125, "7": 147, "8": 162, "9": 179, "10": 199, "11": 223, "12": 243, "13": 262, "14": 281, "15": 303, "16": 323, "17": 339, "18": 359, "19": 375, "20": 395, "21": 411, "22": 427, "23": 455, "24": 479, "25": 495, "26": 519, "27": 543, "28": 563, "29": 583, "30": 611, "31": 627, "32": 655, "33": 671, "34": 687, "35": 703, "36": 715, "37": 731, "38": 743, "39": 763, "40": 775, "41": 787, "42": 803, "43": 819, "44": 835, "45": 851, "46": 863, "47": 879, "48": 895, "49": 919, "50": 935, "51": 959, "52": 979, "53": 999, "54": 1019, "55": 1039, "56": 1059, "57": 1079, "58": 1099, "59": 1115, "60": 1131, "61": 1159, "62": 1175, "63": 1195, "64": 1207, "65": 1223, "66": 1243, "67": 1263, "68": 1279, "69": 1291, "70": 1311, "71": 1327, "72": 1347, "73": 1363, "74": 1383, "75": 1395, "76": 1415, "77": 1431, "78": 1447, "79": 1463, "80": 1479, "81": 1499, "82": 1511, "83": 1531, "84": 1543, "85": 1563, "86": 1579, "87": 1603, "88": 1619, "89": 1643, "90": 1663, "91": 1679, "92": 1695, "93": 1711, "94": 1723, "95": 1739, "96": 1759, "97": 1779, "98": 1803, "99": 1823, "100": 1835, "101": 1855, "102": 1875, "103": 1887, "104": 1907, "105": 1927, "106": 1947, "107": 1963, "108": 1983, "109": 1999, "110": 2015, "111": 2031, "112": 2047, "113": 2059, "114": 2075, "115": 2091, "116": 2107, "117": 2123, "118": 2143, "119": 2163, "120": 2179}
---

**Dave Jones:** Hi, this is part two of the Raspberry Pi supercomputer cluster that I'm building. And a lot of people have asked for a second part to this thing. Continue on, where's it at? Well, okay, no, I haven't done anything on it, but I was thinking about the case for the thing, and then I remembered

**Dave Jones:** I've got three of these babies I scored from the dumpster. The Apple G5 Power Mac, and these cases are just beautiful. All aluminium cases, and the things are, these are absolutely useless on their own. The processor in them is like the old G5 processor, it's absolutely ancient,

**Dave Jones:** it's of absolutely no use, but, if we can get this thing out, come on, there we go, we have a beautiful aluminium case. We've got the fans, airflow through the front grills here. So I thought, what if we actually, ugh, dust in there is pretty horrible,

**Dave Jones:** but what if we actually, sorry I'll change the angle because I wanted to show you the Apple symbol there, and what if I actually replaced the motherboard in this thing with a huge motherboard that actually contained all of the Raspberry Pi boards on them,

**Dave Jones:** and then we can reuse the power supply which is in the base of this thing, and we've got the fans, and we've got a beautiful aluminium case, and I thought that'd be pretty neat for a redesign to fit all in there. So let's just take this thing apart and have a squiz where we're at with that.

**Dave Jones:** And there's the specs on this thing for those playing along at home, 1.6 gig, look at this, 512 mega memory, 160 gig hard drive, you know, these G5 processor machines, yeah, they're just absolutely useless for anything today, but let's rip the guts out of it and see what we've got.

**Dave Jones:** Guys, a lot of dust in this thing, absolutely terrible, and I'm all out of compressed air, bugger. And people have actually turned these cases into, you know, coffee tables, and seats, and all sorts of weird and wonderful stuff, and they've actually got like a cult following these cases,

**Dave Jones:** and I believe they sell for a pretty penny on eBay. We've got ourselves a fan in there, what brand is... I'm not sure of my brands. Anyway, the fan noise and stuff like this, and I haven't powered it up since the last video,

**Dave Jones:** but I love how it just comes out, and everything is quite modular inside these puppies. So let's try and get the rest of it out. There's a... oh, no, aw, that one's not as modular. Aw, I was just talking it up, and there we go.

**Dave Jones:** Gotta get the cables out. Woo, got a speaker. There's the graphics card inside this puppy for those playing along at home. It's an NVIDIA job, I'm not sure, absolutely ancient. It's interesting to see the performance of this ancient NVIDIA card compared to, say, the GPU inside a, you know,

**Dave Jones:** a fairly modest GPU inside the modern Raspberry Pi and all-winner chipsets. Hmm. This fan here pops out as well, once again. And of course, if the existing fan solutions in these were buggered, or they were too loud, or whatever, I'm sure the airflow would be more than adequate for what we need

**Dave Jones:** for a Raspberry Pi supercomputer cluster, although we haven't, you know, calculated the power and everything else yet, but anyway, we could replace those fans if we had to, no worries. And that's an A1047 for those playing along at home. Everyone loves playing along at home.

**Dave Jones:** Now I may have actually picked the wrong machine to open up here, I didn't remember what one was what. But this is different to the one I did, I had a peek inside before on my previous video. This one has got standard, well, you know, not PC standard, but they've got

**Dave Jones:** power supplies under here, of course, so they've got these Molex-type power connectors, but the other machine that I took apart had these beautiful, and here's a video of it from the previous one, these beautiful studs coming out, which went directly into the board.

**Dave Jones:** There was no wiring or anything like that. It was just beautiful design and interfacing from the power supply through to the motherboard. Now, which one might be better? I'm tempted to use the sexy solution, the one with the studs that stick up and then just screw directly into the motherboard,

**Dave Jones:** and I, of course, I can design my Raspberry Pi baseboard, motherboard, to actually support those. You get the dimensions right, everything else, you drill the big holes, you put the studs in, and there's no wiring, so yeah, I don't know which one, pros and cons

**Dave Jones:** both ways. Hmm. Actually the worst part about this Power Mac design, if you look right down in here, there's the modem. It's got a modem connector on the back, an RJ11. You'll note that cable running all the way up there. It runs all the way up,

**Dave Jones:** all the way up, and here is the actual modem module all the way over on the diagonally opposite side of the motherboard. What the hell were they thinking? That's just ridiculous. Otherwise beautiful systems engineering inside this thing, but yeah, that's a big thumbs

**Dave Jones:** down. So I took the memory modules out, and there's the big molex or one of them. They've actually got two of these, as I said, one over that side as well, I got that one out, and there it is. So I'm sure I can get the pinouts for these babies

**Dave Jones:** somewhere, have to look that up. And then from the front panel they've got this, this is like the power connector, it's got a USB and a firewire and an audio, I think, and that's just some little weird ass smaller pitch one. You can probably still get those though, but you know, like

**Dave Jones:** that's really annoying. I don't want, probably don't want to reuse the soft power switch on the front, so I'm not sure if I'd go to the effort to redo that. I'd need to get the pinout for that. I don't know, is the full service manual for this G5 available online?

**Dave Jones:** Haven't even looked yet, kind of just winging it at the moment. But yeah, whether or not I go for the stud solution or put the molex connector like that onto my board and then just, you know, reuse that, I don't know. Six of one, half dozen of the other.

**Dave Jones:** Alright, let's lift this processor module out of here. Ta-da! And there it is. Oh, beautiful! Look at that board-to-board high-speed interface connector, that is just beautiful. Look at the bypassing surrounding that G5 processor, just absolutely ridiculous. Big heat pipe and everything else on there.

**Dave Jones:** And that is just, you know, I believe these are really power-hungry Foxconn job, of course. And yeah, these are just, that is a big-ass heatsink on a processor which is like your mobile phone, probably has more power than this thing these days. It's really interesting trying to get this baby apart.

**Dave Jones:** It slides out, that'd take out a couple of posts, I think I've still got one left there, but this divider here seems to be screwed into the board from the other side so it's probably going to come out with the motherboard, but the motherboard should slide

**Dave Jones:** that way slightly and lift out. And that's what it looks like anyway, because you can see the pins down in there for the sliding part of it. One of those, this should slide like that, and then oh, yep, yep, yep, yep, yep, yep, all the connectors are in the way.

**Dave Jones:** But if you get those over, it should eventually come out. Somehow. Let me work on it. Whoa! That was a bit tricky, but there she is. It's the main board. Ah, look at the heat piping on the bottom of that baby. Didn't see that one in the previous

**Dave Jones:** teardown. Nice little chunky fin heatsink on the bottom of the BGA there, which is under the processor, that's like interface, I don't know the Mac architecture, the G5 processor system architecture and stuff, but obviously they need that big-ass BGA there to interface with the processor.

**Dave Jones:** Is that some, is that like a memory controller or IO interface, something like that? You can see the differential pair tracers all come down here to this baby, which is another one. Ah, there. That would be, given its location, that would be a bridge slash interface driver for the

**Dave Jones:** slots there, I would be guessing. And wow, there's a lot of heat sinking on the backside of that thing. I'm quite surprised. Jeez. But look at the flux residue left over on those pins. That's pretty how you're doing for an apple. And they've got some cables coming through here, these are, it looks like they're coming from the power supply.

**Dave Jones:** They're going up to the hard drives and everything else up on the top half, so that's how they've got them across. It's rather nice, there's actually no dust there, a little bit accumulated on some of the channels. The reason they've got these plastic channels in there, they'd be

**Dave Jones:** some thermal ducting. And oh, this thing is, oh, it's dust all over. Awful, absolutely awful, the dust in this thing, but there we go. We have an empty case. We can whack our apple pie motherboard straight back in and Bob's your uncle. Now the good thing about having this case for the project

**Dave Jones:** is that, well, decision made. You work around the case you've got, and that's so often I've found for various projects I've worked on that you will, you know, choose a nice case for it and that'll decide the form factor, it'll even sometimes decide the features

**Dave Jones:** and the user interface and all sorts of stuff like that. So, you know, like choosing this and going, right, I'm going to build into this. You've got a framework to work from, and engineers work best when they're given, you know, specifications to work from.

**Dave Jones:** And in this case, yep, we know our motherboard's going to be this big, our fan air holes are here, we've got X amount of power, we've got X amount of airflow everything else, X amount of thermals and whatnot. And we've got what's available on the front panel, for example, like this is all just, you know,

**Dave Jones:** solid aluminium here. None of this aluminium rubbish for you yanks. You know, maybe we could have like a, take out the CD drive up here and have like a display, something like that. You could have like an LCD in there or something like that, or a whole bunch of LEDs.

**Dave Jones:** You could do like a custom display board to show them all working. Because you can, you know, you can have LEDs and stuff shining through here, but it's not, you know it's not the same. You know, it's not nearly as good. So maybe

**Dave Jones:** you know, you can have some sort of LCD interface. As on the back, we've already got our cutouts here, so we could probably have our Ethernet exactly where it was before down here. So most likely the board's, well, it was mounted on the other board wasn't it?

**Dave Jones:** I'll get that in a second. So it's going to be the right height, everything else. So my standard 1.6mm thick board, you whack it in there, you whack your Ethernet connector on there, and it's going to line up. So it'll be the master Ethernet interface, the RJ11 down here, you could use that as a

**Dave Jones:** serial. You could break out some USBs or something if you wanted to do. So to have a framework to work from, well bingo! You just go for it. I mean, now all we've got to do is get there and measure all the dimensions of everything.

**Dave Jones:** You can either work from the standoffs on here, or work from the board. It's probably easier to work from the board, you know, get a big metal, rather than try and get a big metal rule in here and it doesn't fit for these standoffs.

**Dave Jones:** You can get them all from the PCB, and we can do the slots in there for those ones where it slides in and gets hold of that. Or you don't have to even put those in if you don't want to. If you don't want to get fancy-pantsy, you

**Dave Jones:** can just make a big cut-out hole for those things. And well, I don't know, yeah, we're not going to hook drives or anything like that up, but you know, we could if we really want to do. But this is quite exciting. And from a thermal point of view, it's brilliant.

**Dave Jones:** We're going to have airflow right through the front here and blow it out the back. No worries. Now of course you can reuse components as well. For example, if you didn't want to go out and source and buy the power connector here, you could

**Dave Jones:** de-solder it. You need a decent solder sucker, because this is going to be a multi-layer board connected through the big ground planes. It's probably going to have thermal relieves on the pads. But anyway, you need a decent solder sucker, but you can get that puppy out and reuse it on

**Dave Jones:** your own board. And bingo, you've got a matching power connector for it. And so we've got two of those there. You know, if you didn't want this board, say it was faulty, or you probably couldn't even sell this thing for $5 on eBay, could you?

**Dave Jones:** I doubt it. Anyway, the case is the thing that's worth all the money. This motherboard is probably useless to almost anyone. I stand to be corrected on that. Sorry for all you G5 Power Mac aficionados out there who go, I'll have it. By the way, look at this.

**Dave Jones:** We have a genuine bodge wire. Look at that. Wire wrap wire going all the way over there. And I have no idea what that puppy is for. Hmm. Anyway, yeah, they didn't want to re-spin the board for that one, so let's just mod it.

**Dave Jones:** No worries. I like the little heatsink there. I'm going to keep that. But that's not as big a goof as the one we've got up here. This is the power connector with the crusty flux residue soldering. And obviously they've screwed up some, you know, star grounding type

**Dave Jones:** thing, I would presume. And yeah, they brought it back to that big power resistor there. That'd be a current shunt resistor. I think you can see the two tracers going off there. That'd be going into a diff amp, measuring the current presumably for this expansion connector.

**Dave Jones:** Check this out. I was taking this bracket off here, and look what we've got on here. A little plastic TO-220 package, just you know, just cable tied on there like that. I can't quite see the part number on that. It's a 2N3904. Wow, yep, there it is.

**Dave Jones:** Wow, I thought that would have been like a little temp sensor jobby. It could still be, but why they've actually put that transistor up there? Look, they've even gone to the effort to make a bloody connector for that! Like, it wasn't using that as a heat sink, so

**Dave Jones:** whaaaaaaat? Like, why would you want to measure? I mean, you can actually use the PN junction of a transistor if you want to measure temperature, you know, you get 10 millivolts per degrees C, I think, or thereabouts, but like, sticking, like, but they're not, what?

**Dave Jones:** Woo, look at all the dust still on there. Yuck-o. Anyway, here's our key slots, and we can easily make those out. How you would, well you could either specify, you could do that two ways. You specify either in the PCB I'm talking about, you either specify like a drill

**Dave Jones:** like that, so you specify a hole, a non-plated hole, and then you specify a slot going in front, which is a hole with a with a dimensional length on it from that point through to the center of that one. And we're in like Flynn on the power supply, just two screws here, lifted off a metal

**Dave Jones:** cover, got two crusty fans on the end there, they really need a decent clean-out, no doubt. And unfortunately no pin-out on the thing, well whatever. 450 watt max capability, now that sounds great, but that 450 watts of course capability is spread across all these different rails.

**Dave Jones:** So and look, a total of 340 watt maximum on those. Now, you know, you could potentially get in there and try and, you know, hack the thing and remod it, because we only need the 5 volt output, okay? Because this thing's got a 3.3 volt output, and, you know, it's

**Dave Jones:** we're basically going to be pissing away 22 amps of the, well, times 3.3 in watts as the total capacity of this thing. So, you know, if we don't modify it in any way, we either have to have an external DC to DC converter to use

**Dave Jones:** the power available in these 12 volt ones and the 3.3 volt rail as well. You know, you wouldn't worry about the negative rails or the, you know, standby, you can get a little bit of power from the standby ones. In fact, the standby, my, would it come

**Dave Jones:** in handy? Maybe you could have like one Raspberry Pi in there working continuously off the standby, and then only when you press the soft power do you, boom, you know, power up all the others. I don't know, you know, I hadn't planned on anything like that, I don't think I will, but

**Dave Jones:** you could, hey? And 25 volts standby at 5.2 amps capability? Holy power availability, Batman, that's insane, what the hell do they need like 125 watts standby for? Wow, I don't get it. And there are some people saying, well, you know, you probably shouldn't use this power supply anyway

**Dave Jones:** because it's, you know, too old, at least go in and recap it or something like that. Yeah, maybe, you know, that's a half reasonable argument, but for the time being I think I'll just use the thing, because it does work. Now if we just look at the unmodified power

**Dave Jones:** supply with the 5 volt 19 amp rail, that's 95 watts, if my math is correct, I'm not that good at math. And the Orange Pi one, I've measured at 3.7 watts nominal for all 4 cores running BOINC software at you know, 100%. So that gives us 25

**Dave Jones:** volts nominal we can power from that single 5 volt 19 amp rail. Might be able to get a bit more juice out of that, but I don't know. You know, this is going to be a decent power supply, they're probably going to have

**Dave Jones:** overcurrent protection and all the rest of it, I would be guessing. And then you'll get like another 20 or so maybe from the, if you were able to, well maybe less than that with conversion efficiency and stuff if you had an external, like an onboard

**Dave Jones:** boost converter from 3.3 up to 5, you know you could power some more boards. Or you have a buck converter, 12 volts at 23 amps, that's where most of the power on this baby goes. And you know, so if you're going to tap off something, I would tap the 12 volts and take that down to

**Dave Jones:** 5, and then you can power as many boards as you want. But yeah, 25 is not a huge number of boards for, you know, this huge monster case here. And well, you know we wouldn't want greater capability than that. Right, so looking at your standard Raspberry Pi or your Orange

**Dave Jones:** Pi 1, that I've got a few of these. I've got the new Orange Pi PC2 on order, it's just come out. And it's got the new H5 quad core processor in it, so that looks pretty jazzy. And it's $20 I think, and it's got

**Dave Jones:** double the memory, or 1 gig, or something like that. Anyway these boards are tiny compared to the space inside here. Now if you've watched the previous video, and you should have, you know I came up with some sort of slot arrangement to plug this in.

**Dave Jones:** I don't think I'll do that because it ties me to one particular type of board because as I said previously, while the pinout on the Orange Pi 1 is compatible with the Raspberry Pi 2, it's actually backwards. They put it on backwards because the boards actually come

**Dave Jones:** out this, the expansion boards actually come out this way. So if you had an expansion board it comes out like that, instead of on the Raspberry Pi which is over the top like that. So the pinout's actually backwards. So what I'll do is just design a simple vertical

**Dave Jones:** riser board. So the motherboard, so instead of this connector here, you know, slotting into the motherboard like this and then clipping onto a right angle connector on the motherboard I'll actually have it like this, and then have a riser sorry for the crudity of the model here, I didn't have time to build it

**Dave Jones:** to scale or to paint it. Then you'd imagine this is a blank, oh like let me get a blank board. Okay, so what you've got is a little just design a custom riser board like this that converts the vertical header on the Raspberry

**Dave Jones:** Pi or the Orange Pi into a right angle header basically, so then you can plug that into your motherboard like that. So the Raspberry Pi one would have say a small one like that, and the Orange Pi one would have, because it's, well, you'd have to design it so it's upside down

**Dave Jones:** like that actually. So you'd have to design this one with the short board like that, that then plugged in, and then the Raspberry Pi with the big one, because the pin-out's back the front, and then the Raspberry Pi plugged into the motherboard like that.

**Dave Jones:** If you get what I'm getting at. So the good thing about using a riser board plug-in like that is that you can use basically any board. Your motherboard will be compatible, it'll use the standard Raspberry Pi header but then the physicality of actually loading the board

**Dave Jones:** on there, and you know, you have to do a slot and you've got to you know, not have connectors fail and all sorts of things. It just, you know gives you options later for installing that. So the width and then you don't lose any, with the slot you don't lose any space

**Dave Jones:** by plugging that in and then moving it over like that. So you can just plug it in vertically. So you can actually fairly densely pack these things like that, because they're basically plugging in vertical and because you've got the large connectors like that

**Dave Jones:** the ethernet and the USB. The header board is smaller than that, but you've got your right angle connector on there it could be on the other side. Yeah, you know, work out the pin-out arrangements later, and you know, everything else. Yeah, so you should

**Dave Jones:** get about that much space between your boards. You've got to watch out for your heat sink, of course that could be an issue. But once you do that, you can even mix and match different types of boards, any ones you had in there, all you've got to do is design

**Dave Jones:** a little header, you know, a little riser board to match whatever, Raspberry Pi or other style board that you wanted to use on this thing. Now of course one of the big things on a super computer, like a cluster-y thing, high-powered, anything high-powered like this, just your regular PC of course, the airflow, the

**Dave Jones:** thermals of this are a big deal. Got the fans at the back, they'd be blowing out so they'd be sucking in through the nice front grill here. Ooh, you can see my hand, look at that, it's beautiful. Love this case, it's pornographic, it really is.

**Dave Jones:** So you want a nice airflow with as little resistance and a little turbulence as possible in there. So would you mount your Raspberry Pi boards like that? Or like that? I'll give you a second to think about it. Of course you would mount them like this, because if you mount them

**Dave Jones:** like this, you're blocking all the airflow coming through here with your damn boards! And then you're not getting good airflow over your heatsink, because we'll glue a little, with some thermal glue, glue little heatsinks on these. So you want to mount them in this direction, like this.

**Dave Jones:** So you want to stack them like that, so that the air flows over the heatsink. I know you've got airflow issues caused by the connectors and everything else, but hey, that's better than the entire board blocking like that, because at least you've got, you know, gaps between there

**Dave Jones:** and then, you know, a gap between each board. But if you put it like that, you're really restricting that airflow, and the airflow, it'd come in here like this, and then flow around the board, and you'd have this dead space in here, you wouldn't get, you know, the airflow, well, the airflow

**Dave Jones:** over your heatsink here would be horrid. So you want them in that direction like that. So how many of these things can we fit? Well, I bought 1, 2, 3, 4. Okay, so 4 across. Oh, you could space them, say, 30 apart. It's 250 high, so that'd round to like

**Dave Jones:** maybe 8 of these. So 1, 2, 3, 4, 5, 6, 7, 8, something like that. Maybe, you know, to just give yourself some wiggle room, everything else, you know, you might say, I'll be generous and say 40, that would bring you down to 6.

**Dave Jones:** So 6 4s, well, you know, 6 4s, 24, 24, 25. Hmm. Now of course we could gain some more space by just saying, well, you know, we're only going to design the thing around the Orange Pi 1 because it's much smaller than the Raspberry Pi, but

**Dave Jones:** you know, I think compatibility's probably important, mix and match boards, you know, I might use the Orange Pi 2 1, the Orange Pi PC 2 I'm going to get. So, you know, that's I think even bigger than the Orange Pi 1. Anyway, yeah, you've got to

**Dave Jones:** sort of design it for the worst case biggest board. So we could squeeze more in like this. I mean, we're talking you know, like 20, with the Raspberry Pi 2 either, you know, up to maybe 32 of these we can comfortably fit in this.

**Dave Jones:** But the problem is, look, we're wasting all this space in here. We could at least get another depth like that. And that's where these riser boards come in. Your riser boards, you could actually have two of them that plug vertically into your riser

**Dave Jones:** board, and then your riser board plugs horizontally over to here. And of course you can supply your 5 volts power through the Raspberry Pi header from your riser board like this, but you could actually have two of them which then plug in like that.

**Dave Jones:** But then you'd maybe have to change the pin out over here, couldn't use the standard Raspberry Pi one, or you wouldn't have to wire them all the way through if you wanted to get, say, the serial and other ports out of their SPI and everything else out of these things.

**Dave Jones:** So you might have to have a custom header, a custom pin out on your riser board like that. Or you could just have some extra pins, or something like that. So instead of a 40-way header, you could use a slightly larger one, or a

**Dave Jones:** separate one actually next to it that had like a smaller number of breakout pins to share between the two boards if you wanted to stack them like that. So 32, we could probably get 64 Raspberry Pi, regular Raspberry Pis inside this thing without too much of a problem.

**Dave Jones:** Now the one thing I haven't decided on yet is whether or not I'm going to go for the SPI solution that I figured last time and do my own, you know, SPI to Ethernet converter chip on there, or whether or not I'd get, you know, because this case is

**Dave Jones:** all super high-powerful, looks fancy-pantsy, you know, you've got this thing sitting there, oh yeah, it's got hundreds of ARM calls in it, and you know, you get piddly little SPI bandwidth out of your Ethernet. So I am tempted to actually maybe have a little short Ethernet jumper for each one, and then

**Dave Jones:** maybe next to each one of the boards just have the Ethernet cable coming out. But then you've got to decide whether or not you do what everyone else does with their clusters and they just use existing hubs or switches like this one, you know, and you can mount them up here

**Dave Jones:** of course, there's no worries about that at all. You can mount a whole bunch of switches up there, oh well, yeah, you get what I'm getting at. And then you can have all the cables coming out and you can loom it and look all very impressive and stuff like that.

**Dave Jones:** So I could just pop, you know, do it as a cop-out, do it that way, or, but if you did it the other way, you know, and you used the Ethernet and you actually had vertical RJ45s on your motherboard here coming out, and then little short cables, you can actually buy pre-made

**Dave Jones:** little couple of inch long Ethernet cables. So, you know, you could use those and, oh, but then you've got to have the magnetics on there, you've got to design basically this switch onto your board, which is just a single chip solution, I tore this apart last time, but you can design

**Dave Jones:** that on there, but then the magnetics and everything else isn't worthwhile for a one-off project. You'd almost say you're better off if you had the room actually buying these, stripping them down to board level and then just sticking that board onto your motherboard.

**Dave Jones:** In fact you could even have this as like a vertical solution like that, you can either have short cables or vertical, somebody actually pointed out I thought you couldn't get them, but somebody actually posted a link to one, you can actually get a vertical male

**Dave Jones:** RJ45 connector, a PCB mount RJ45 male, so in theory you could have, you know, eight of those on the board and just come along and go click, and in theory your switch would just click into your board like that, and it wouldn't into your motherboard, and it wouldn't take up much room, so that's

**Dave Jones:** you know, it's almost a sexy solution to actually do it that way. So that you know, hands up, if you think maybe that would be the go, to put those vertical male ones on there, and you know, you'd have to line them up properly, you'd have to make sure, get all your dimensions precisely right, so you've got

**Dave Jones:** eight of them mounted on your board and just go click. I mean, and then all you've got to do is wire up the DC jack here, so that'd be, I don't know, that might be kind of jazzy, but hmm. So yeah, there's lots to decide on here, I want to do the motherboard of course, lay out

**Dave Jones:** the motherboard, so the next step will be to get all the dimensions, measure it, lay out the motherboard, and then start planning. Often when you've got that template, that PCB template in your CAD software, then you know, you start playing around with modules and see how they fit, and you know, like

**Dave Jones:** then you start sort of, and you can even do like a paper or a cardboard mockup like this. So you can actually, once you've done all your dimensions, put in your PCB CAD file, print it out, and then often I've done this before, is I'll print it on a big A3

**Dave Jones:** sheet of paper in a one-to-one scale for my PCB, and then I'll just get some glue, stick that paper onto the cardboard just so it's a bit more rigid, and then I've actually got a real mockup board to actually play with inside this thing, and then you can

**Dave Jones:** start come along and you know, seeing exactly, you know, start refining how many boards you can fit in. But then, you know, you've got your thermal trade-offs, as I said, you know, 95 watts, we can only for the, without modifying the supply, we're only going to be able to

**Dave Jones:** probably get, you know, power 25 boards or thereabouts. So if we wanted to tap in to more power, we're going to have to have on-board DC to DC converters, whether or not you design those on the board or you buy the expensive little bricks that you can, you know, plug in.

**Dave Jones:** So if cost is no object, I wouldn't roll my own DC to DC for that, I'd just you know, buy them. Or you can just buy them on Ali, you know, you can get cheap ones, like you don't have to buy the TI power modules that, you know, cost, you know, what, $20 or

**Dave Jones:** $30 each or something like that, you can just maybe get them on Ali Express or something like that, and just, you know, eh, they're going to be probably good enough to do the job. And, you know, have some power bricks on there, because you wouldn't have just one,

**Dave Jones:** I would, if I was going to tap into that 12-volt rail there, I'd probably have maybe a power brick per, depending on what one I got, you know, if it was like a fat or 8-watt, jeez, I don't even add up. Multiply that by 2, then you might have one of those per 2.

**Dave Jones:** But then if you had, then if you had the dual board riser like that, then you'd have to dedicate one of those power bricks, you know, a 10, 8-watt power brick or whatever, to each one of those 2, and then you'd have to have the power brick

**Dave Jones:** next to it, so that's taking up more room. And there's massive trade-offs galore in this thing. So yeah, we've decided on our case, but, you know, we've got a whole bunch of new problems. Anyway, I just wanted to show you this, that I thought

**Dave Jones:** I'd use this very cool and sexy-looking G5 Powermac case, because they are incredibly good-looking. I mean, won't this thing be the duck's guts? With the Apple logo on there, and of course we'll add the Raspberry Pi in the middle, so it'll be an

**Dave Jones:** Apple Pi cluster, and it'll look very, very sexy, will it not? So anyway, I want people's feedback on this puppy, you know, what do you think is the best arrangement, best solution, especially in terms of, you know, an off-the-shelf switch, maybe that plug-in one,

**Dave Jones:** or maybe put them up here and just be, you know, just do it easy, run the cables or whatever, and do it that way. So yeah, let me know your opinion down below in the YouTube comments, on the blog, or on the EEVblog forum.

**Dave Jones:** Anyway, it's a very sexy case. Catch you next time.
