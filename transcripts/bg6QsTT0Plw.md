---
video_id: bg6QsTT0Plw
title: Laser Driver PCB & Circuit Review
url: https://www.youtube.com/watch?v=bg6QsTT0Plw
source: youtube-asr
---

**Dave Jones:** This is cool. It's a prototype for a battery-powered laser driver to be part of a microgravity experiment we'll be flying on a Blue Origin flight. We hope to laser ablate materials in a microgravity environment and observe the results using cameras. That's cool. I

**Dave Jones:** assume that you can do that like at a 100 kilohertz up where you reach space is the like you know the definition of space. The laser we're trying to drive is 10 watts optical output power and the board

**Dave Jones:** is meant to drive about 20 amps through the laser for a few minutes while we are in microgravity. I assume it's it's just constant current driver, is it? I don't know. Along with this the board will be monitoring the temperature of

**Dave Jones:** the laser to make sure it doesn't overheat. A schematic of the board using an op-amp in feedback a runner around I assume. Power FET as a current source. Yeah, it's just the basic constant current source source circuit that we've seen many times.

**Dave Jones:** There's DACs to control the exact current through the MOSFET and some ADCs to monitor the voltage. Any feedback on the layout board is greatly appreciated. Designed for a club I'm in Space Technologies in California, a student-run space group. There you go.

**Dave Jones:** Check them out stack.berkeley.edu. They're in the middle of a Kickstarter campaign. Just researching. Cool, it's not a product. I assume it's just research. Nice, I'm going to go check that out. And it turns out they raised 15 grand.

**Dave Jones:** It's over now unfortunately, but maybe you can still contribute if you want to. Anyway, I've got lots of big buses here for your output current and your output filter in here using SMD caps. You of course you'd use like low

**Dave Jones:** ESR type ones in there no doubt. Looking down in here there we go. We're obviously got a current sense resistor over to here. Nice lots of via stitching here. Tiny little pads for this little uh tiny power package here. Are those

**Dave Jones:** pads too small? Look how small they are. Wow, I did what package is that? That's insane. They're the two MOSFETs, obviously, but uh jeez, tiny little pads on them. Can hardly see them. Anyway, in terms of uh layout, that looks uh quite

**Dave Jones:** reasonable. I mean, they're, you know, tapping off the the voltage sensor, not quite exactly on the pads, but yeah, you know, near enough. Um and they've obviously got I haven't even looked at the schematic yet. They've obviously got

**Dave Jones:** a uh difference amp uh in there, which uh then the microcontroller here senses. Um it The layout actually looks fine and dandy. Yep, plenty of ground plane on the bottom, lots of via stitching. Nice. Okay, I was wondering what that is

**Dave Jones:** there, and that is a uh They don't have it labeled. Why is it like a couple of other But it's like that's labeled. That chip there is labeled U10. What happened to the rest of the designators? If you go

**Dave Jones:** into the effort to put your silkscreen, um make sure you get all your designators on there. I assume I've got it upside down, so all the electrons are going to fall out. Um and Anyway, turns out that is a uh

**Dave Jones:** transformer over here like this, because, you know, in a system like this, doesn't surprise me that you have to uh galvanically isolate that. That's what uh it's traditionally called just when your transformer isolates something like that. It's called galvanic

**Dave Jones:** isolation. It just means it's electrically isolated between one side and the other. So, all this laser driver is all uh floating. No worries. And I hadn't seen this chip before, but damn, I like it. The LT6820. What they're doing here is I thought,

**Dave Jones:** you know, oh, they're just doing some uh you know, like simple custom serial interface. This is actually SPI over a galvanically isolated twisted pair, and that's what this chipset does from Linear Technology. Here's the data sheet, and it uh you just put one of

**Dave Jones:** these at each end, and you've got a full um SPI compliant interface over one galvanically isolated twisted pair. Fantastic. I don't care what this thing cost. It's brilliant. Anyway, that takes all the dickery out of Yes, that's an industry

**Dave Jones:** term. Dickery out of like your interface. Just use a standard SPI interface and you don't have to use like multiple optocouplers or anything like that in multiple lines. No, that's a great solution. I'm going to have to remember that chip. That's really neat.

**Dave Jones:** Wonder how long that's been around. Then again, it's been a long time since I've do any galvanically isolated serial interface. Often I've rolled my own for that sort of aspect. Anyway, we've got an ATtiny here. We've got the

**Dave Jones:** programming header. We've just got some decoupling. No worries. And it looks like we've got a serial analog-to-digital converter there. Couple of Maxim parts. MAX4130. More Maxim parts. Guaranteed not to be able to get them. That's a 90 90s joke for those who get

**Dave Jones:** it. Maxim 53 31. That'll be a DAC. Don't even have to look up the data sheet for that. It's a voltage output DAC using an internal reference. Just a buffer driver to drive. Just your standard constant current circuit. You've got two

**Dave Jones:** MOSFETs in parallel here. Don't have a current sharing resistor between the MOSFETs. Often you'd put like a low value resistor in the line, you know, into one going here, one going here. Just so they share the current more evenly cuz when you're trying to

**Dave Jones:** drive those I don't know. You know, you'd have to do some practical testing on that cuz you won't might find that one just due to the parasitic differences in the specs in these chips cuz they aren't going to be identical

**Dave Jones:** even if they're they're better matched if they're from the same wafer, but they're unlikely to be. Um, and well, you can't assume that they're going to be matched. And otherwise, you buy a matched pair of MOSFETs. Anyway, I'm tangenting. Um, you

**Dave Jones:** put in a current sharing resistor, so it just load balances uh between the two. Just a really low value um in there. And then they've just got their 10 a milliohm shunt resistor, which will be that job over there. That we looked at where it

**Dave Jones:** is. There. And as um and it senses that off. No, it doesn't. Okay, I was wrong about the uh difference amplifier there. It looks like that they're just tapping that off. They probably the ground line. Yep, I'd say that's the ground line for

**Dave Jones:** the chip. Now, they've done that right. Like hats off. Well done. But I would have put a design note, just a little box on here where my you know, an arrow pointing up some design notes on your schematic just to remind yourself that

**Dave Jones:** uh yeah, the ground for this because it that's the reference has to come back to here like this. It has to be that, you know, star pointed uh type thing. Otherwise, if you just gave the schematic into anyone, they wouldn't

**Dave Jones:** have not known to do that if they didn't didn't know about the design topology going on here. So, that's why uh design notes help on your uh schematic. But that was sort of obvious to me. It may not be obvious to uh someone else who,

**Dave Jones:** you know, you might have gave given the layout to someone else or you give the layout to someone else to check and they go, "Well, what's this?" Just tie it down to ground over here and, you know, eh.

**Dave Jones:** Anyway, no, I have no problems with that at all. That's nice work. I hope it uh works well for you. Keep us updated in the EV blog forum for future projects.
