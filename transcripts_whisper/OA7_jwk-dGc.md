---
video_id: OA7_jwk-dGc
title: EEVblog #1169 - TI 1972 Computer Interfacing
url: https://www.youtube.com/watch?v=OA7_jwk-dGc
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 0, "2": 41, "3": 75, "4": 106, "5": 140, "6": 169, "7": 202, "8": 223, "9": 265, "10": 285, "11": 325, "12": 385, "13": 409, "14": 432, "15": 453, "16": 471, "17": 498, "18": 518, "19": 539, "20": 557, "21": 579, "22": 596, "23": 623, "24": 647, "25": 669, "26": 685, "27": 703, "28": 719, "29": 735, "30": 754, "31": 771, "32": 797, "33": 813, "34": 832, "35": 850, "36": 870, "37": 892, "38": 911, "39": 932, "40": 955, "41": 977, "42": 996, "43": 1015, "44": 1031, "45": 1048, "46": 1071, "47": 1098, "48": 1115, "49": 1136, "50": 1150, "51": 1169, "52": 1190, "53": 1208, "54": 1227, "55": 1256, "56": 1274, "57": 1297, "58": 1315, "59": 1339, "60": 1359, "61": 1369, "62": 1399, "63": 1549, "64": 1699, "65": 1759}
---

**Dave Jones:** Hi, take your mind back to 1972 when Texas Instruments made more than chips. Look at this bad boy, oh, the Silent 700. It's upside down, so all the electrons are going to fall out. Portable data terminal from 1972, because back in 1972, hey, like, time-sharing computers were all the rage, right?

**Dave Jones:** We didn't have personal computers back then. So, you needed, like, data terminals to connect into time-sharing computers. So, let's have a look at this bad boy, Texas Instruments. Oh, look at that. Thing of beauty. It's a joy forever. And yes, that is an acoustic coupler modem.

**Dave Jones:** Fantastic. And this bad boy was advertised as being three times faster than competing terminals. How fast? What? It'd be lightning fast if it's three times quicker. Well, 30 characters per second. That's characters per second. But if 30 characters per second is just too fast for you, well, you can whack it into low-speed mode, probably down to, what, 10 characters per second?

**Dave Jones:** I love the here is key. What? Leave it in the comments if you've ever used a here is key. But the keyboard is absolute classic. It contains a ton of stuff. About the only one I know is, like, Bell, you know, Acknowledge, stuff like that, where I'm sure were ultra-useful for the terminal market and logging into, like, time-sharing computers and stuff like that.

**Dave Jones:** But I love the, like, switching to uppercase. Oh, state-of-the-art stuff. You've got to remember, this is not a computer at all. It does no internal computing and processing. Apart from, like, the serial interface. Basically, talking to a serial port or through the acoustic coupler modem on the top to some form of time-sharing computer, either via a, presumably, you could have, like, direct connected it up via a serial port, or you hook it up via the acoustic coupler modem, and it doesn't even have a display.

**Dave Jones:** It's got a printer. So everything that you receive, instead of going onto a screen, is a printer. It goes onto a printer. So that's nuts, and it goes to show why this thing really didn't last much beyond, like, the early '80s. Uh, the Wikipedia page, yes, there is one for these series of, uh, TI Silent 7, Silent Series, uh, terminals, was that, yeah, they survived for a bit longer when modems started becoming, like, 1,200 board modems.

**Dave Jones:** This thing literally could not keep up. Not because the electronics in the serial port couldn't keep up, it's because they couldn't print it. Far, they couldn't print the characters fast enough on the paper, the actual printhead, the thermal printhead in here couldn't actually print long enough, but they did, uh, actually release one with a dual printhead that could actually print twice as fast, so it claims they were used into the mid-'80s, but I, like, apart from very niche, old-school apps, like, I doubt anyone was using this past the mid-'80s.

**Dave Jones:** Ooh, supplied by a computer benefit. I wonder if they're still around. And this was pre-eight-digit phone numbers, so, hey, I can remember when I had to change over from a seven-digit to an eight-digit phone number here in Australia, they made it, uh, compulsory, but computer benefits, like, computer with benefits.

**Dave Jones:** Wow, it's got a contrast pot. Made in the United States of America. Beautiful, and there's not much on the back, there's an IEC power connector, there's a, um, non-SIM. It's a non-standard-looking serial interface, presumably, and it was originally owned by Facom, Faecom, I used to, I used to work at Paycom, that was my first job, actually, and for all you young kiddies out there that don't know what this is, it's an acoustic coupler modem, and it went over the phone handset, because phone handsets used to look like this, you know, with the coily cord and everything else, and you used to connect it across here, and it would generate tones, and it would receive tones, and it would receive tones.

**Dave Jones:** Um, on here, and, that's how it did it, it sent it through the phone line, as little beeps, and you could send, you know, like, well, 300 board, 300 bits per second was, you know, huge back in the day, and then it went to 1200 bits per second, 1200 board, ah, that was, you know, black magic.

**Dave Jones:** Because you've got to remember, the analog phone line has, and still has, like, a very limited bandwidth, so it's actually quite difficult to get more than, like, a few. You've got to remember, the analog phone line has, and still has, like, a few.

**Dave Jones:** You've got to remember, the analog phone line has, and still has, like, a few. Oh, yeah, look, the head's moving, so obviously it's got some sort of echo thing happening, where my stuff, what I'm typing, echoes onto the keys, but it's obviously not doing anything, return, there we go, there we go, so, hey, this sucker works, but obviously, the thermal head's not doing anything.

**Dave Jones:** Oh, yeah, look, the thermal head's not working, and it's not, it's not advancing, so, not sure what the deal is. Line feed, paper advance, oh, fail, but, like, it's going through the business. Oh, look at the yellowing on the plastic from all the fire retardant, and flathead screws, none of this Phillips rubbish.

**Dave Jones:** Oh, no, my paper fell out, dammit. Still in great nick, by the way. Date code, October 1978, fantastic. Ah, lease, it's a lease job. Look at lease, this bad boy. And the use of paper not meeting TI specification may void warranty. Warning, Will Robinson.

**Dave Jones:** And here we go. I'm afraid this is not going to be the most interesting teardown. I'm more intrigued by just the novelty of a terminal like this. And, oh, look at that optical encoding wheel. Wow. So, that does your positional movement for your printhead.

**Dave Jones:** So, that'd be like each individual character, each individual position. And you could drive it and go, next character, next character. But this is hilarious. This was what was making all the noise. I'm not sure if you heard it, but look at the fan.

**Dave Jones:** It's just blowing air over there. Sorry, that's hilarious. Somehow it blows air into here, out of there. I don't know. It seems to be like blowing it over the paper. What? This is just hilarious. I don't know why that's funny. It just is.

**Dave Jones:** And the sprog capacitor fanboys go wild. Oh, fantastic. No wonder they still work. Oh, tip 41 power transistor. Just stuck on with the mica washer and the how-you-doin' thermal paste. Terrific. I think we've got a 79 series regulator in there. Probably got a 78 series over there.

**Dave Jones:** Probably another couple of trannies stuck down there as well. Just like on this little aluminium vertical heat sink. Does the business. As for the PCB, none of this solder mask rubbish. We've got a tin plate, of course. And with the black silk screen just directly on top of the tracers.

**Dave Jones:** No wuckers. State-of-the-art flat flex going over to our printhead. There we go. There's the rest of our board under there. As you can see, there's basically no processor in there. It's just going to be a serial interface and printhead driver. That's it. And, you know, keyboard decoder.

**Dave Jones:** Check out the podding-type gunk they've got down there. I don't know why they decided... ...to whack it on just that top bunch of components there. Um, I'm not sure what the deal is. Oh, check out the mains input. What's doing here? Anyway, we do have it input mains fused.

**Dave Jones:** Check out the three kilovolt ceramic caps in there. Just love the old schoolness. And they've got the heat shrink, well, the insulation tubing over the leads as well. Thank you very much. Looks like there's a common mode choke going on... ...down in there and presumably...

**Dave Jones:** What? This is a weird-ass-looking... I assume it's a transformer. What? Anyway, this is the main switch. TO3 power tranny there. Offhand, I don't know it. And SJ7432. 78, uh, mid. All the components in here are mid-78 date code. Those of you who want to see the base of that,

**Dave Jones:** they've also... Where they put that, uh, gunk before, they've also put some on the bottom side here. So, I, like, was moisture a problem at that part in the circuit? I'm not sure. Made in the U.S.A. T.I., love the T.I. logo, classic. Anyway, there's no obvious, uh, bodges on this board, so...

**Dave Jones:** Nice job, whoever did the layout on that. Sweet. Oh, some dust accumulation. From 1978. I presume it's never been cleaned. Ha-ha. And they're, they're all, uh, tip series power transistors. Probably been used as, uh, series pass regulation elements. Actually, looking at all this,

**Dave Jones:** I think this is all part of the power supply here. And given that this puppy is not your standard linear transformer, it looks like this is a switch-in, uh, converter, given that the power of this thing, uh, would be taking two, of course.

**Dave Jones:** It'd need a fairly decent, uh, linear supply. I think we've got a big-ass switch-in supply here. And I think you'll find that these two, um, big-ass caps here are, uh, 240 volt, um, direct, uh, as in 240 volt AC, um, much higher, uh, DC volt.

**Dave Jones:** I think it's got, uh, direct mains rectification and your traditional switch mode, um, supply. So there seems to be a lot of, uh, quite a bit going on here. All, uh, discrete transistor, none of this integrated circuit rubbish going on in the switch-in power supply.

**Dave Jones:** So I'll see if I can find a, find a schematic for this thing. Um, because, yeah, it looks, power supply looks fairly involved. So let's have a look at some of these puppies down here. Where you'd expect to find, uh, TTL, we've got, uh, TI, of course.

**Dave Jones:** TI are going to win the, uh, win the bomb for this thing. Um, SN98614. I don't know those offhand. Um, I don't know what the unpopulated socket, uh, is there, but all these other, like, little 8-pin jobbies up here, they're all op amps and whatnot.

**Dave Jones:** So I would presume that all that is part of the, uh, bit detection, you know, uh, level detection and, uh, bit detection, uh, circuitry for the, uh, serial interface. Let's get this keyboard out of here. It pops out of these little plastic holders.

**Dave Jones:** Hello? Oh, no. Oh, hello. No, it does have this microprocessor rubbish. I was hoping it'd do everything discreet with some character generator ROMs, but no. Oh, for all you 8080 fanboys. Look at that. Genuine TI, TMS 8080 from 1978. Beautiful. I know you want the close-up.

**Dave Jones:** There it is. Isn't it a thing of beauty? And it's got hot snot on either end just to keep it in. Oh, I do believe that's a single wipe socket, too. Ugh, evil things they are. And we got some TTL 74S series 'cause they needed the extra speed in there

**Dave Jones:** just for, uh, some sort of interface there. I am gonna presume that this puppy down here is a mask ROM 'cause I don't see a ROM anywhere else, so, yeah. Uh, we got some 74LS stuff around here. Ooh, 74L. Oh, they didn't want to piss away.

**Dave Jones:** Uh, the extra current with the LS series, they didn't need the speed, so they went, "Oh, we'll, we'll put in the low-power version. Thank you very much." And, uh, what's that crystal up there? 12 meg by the looks of it? Screamin'. I don't know what that other 40-pin jobby is down in there.

**Dave Jones:** I'll have to look her up. And the keyboard's made by Microswitch in Freeport, Illinois. Were they the duck's guts back in the day? I don't know. Leave it in the comments. The keys do actually have a beautiful, tactile, feel to them. Oh. Ooh, is that an inserted pin mistake?

**Dave Jones:** You notice it? Yeah, it's bent out there. Or is that a genuine open-pin mod? Hmm. Well, I think that's an insertion mistake, so maybe that pin didn't matter. All pins matter. No, it's actually connect--it's--yeah, it's connected to a trace. Don't think that was making contact.

**Dave Jones:** And if you're gonna do an open-circuit mod, you would definitely bend the pin out horizontal. Um, definitely wouldn't bend it back under like that. I stand corrected slaggin' this poor thing off for potentially having single-wipe sockets. No, they're dual swi-- uh, dual-wipe in the vertical form factor.

**Dave Jones:** Wow, you don't see many of those. Let's just plug this thing back in when it's opened up, shall we? . Ta-da. Return. Line feed. Hey, we're feeding the paper now. So I actually plugged that-- I bent that pin back in and plugged it in.

**Dave Jones:** So, uh, I--I don't know. Was that a--whoa. Nice, but thermal printhead's not working, though. But it--the process is obviously working, and it's responding to, um, stuff. So, yeah. D'oh! I'm an idiot. Forgot to plug the printhead in. Like, the thermal printhead's moving, but it's not connected.

**Dave Jones:** D'oh! Let's try it again. Oh, yeah! It's there! It's there! I think it's printing something. I can maybe just see that. It's very faint. I love how, yeah, line feed. It just literally just feeds it. Yeah, you can see some of the-- like, there's one line of dots there.

**Dave Jones:** So it looks like only one of the-- one pin on the printhead is working. Ooh, five ohms, impedance protected. Just to show you the other side of the mechanism here, don't know why that's got-- it's sort of, like, just flapping around in the breeze at the end there.

**Dave Jones:** Not sure, was that supposed to push in or screw on? Not sure what the deal is there. Anyway, that looks like, oh, maybe it-- that--you can see the head, see the head moving out with that. I think it was all the way on.

**Dave Jones:** I think it was touching. Did manage to get a couple of characters up there, so maybe the printhead wasn't against it, but it doesn't seem to be actually printing characters anymore, so, oh, I don't know. This thing's a bit temperamental. But wait, I found the service manual for this thing.

**Dave Jones:** Let's take a look. I love the old school service manuals. I just love these old brochures. Check these out. Look at this. Hey, only $19.95. Only weighs $13.95. 13 pounds. It's half the weight of the currently most popular portable, our own Model 735.

**Dave Jones:** This is the 745. This is great. And I'm surprised it didn't have a rotary dial phone. Brilliant stuff. I had a rotary dial phone when I was a kid. Geez, right into my teens, probably. Oh, you young whippersnappers. New portable data terminal from TI, 25 pounds, 25.95.

**Dave Jones:** Love it. How does she type with fingernails like that? She doesn't, is the answer. And look, she looks so happy walking to work, carrying her 35-pound portable data terminal. That's great stuff. 30 characters per second, twice as fast. Sorry, three times faster than the competition.

**Dave Jones:** Texas Instruments, Incorporated. All right. But here we have the service manual. This is the 1978 edition, so, or maintenance manual, they call it. And these things are so comprehensive. They don't do this anymore. Just be amazed at how much detail they're gonna have in this.

**Dave Jones:** I haven't looked through it all, but I'm sure it is massively comprehensive. Full duplex, they're explaining, yep. Full and half duplex and all that sort of stuff, because, you know, people have to, well, technicians have to understand this stuff. How the paper goes in, the platen, all the rest of it, theory of operation.

**Dave Jones:** Nobody does a theory of operation anymore. Give me the old school magazine projects, like I used to write back in the day and get published, and you'd have a theory of operation of your circuit. You know, everyone publishes their open source stuff these days, and

**Dave Jones:** you almost never see, like, a theory of operation anymore. You never see a block diagram, you never see anything like that. So, gone are those days. It's a real shame, 110 board, 300 board, and all your ASCII tables, your control codes and what not.

**Dave Jones:** There's the printhead driver, there you go, contrast is 0 to 75 milliamps, ceramic heatsink, and there's the printhead element driver, well, did we see those? Mate, that, let me go to the power supply section, because I might have been wrong about those tip 41 transistors.

**Dave Jones:** They might be the printhead drivers, because I didn't see them near the connector, so I think they're way back up. And there's the printhead stepping motor with the wheel that we saw with the phototransistor, nice. There's the printhead stepping motor driver, look, it's all there.

**Dave Jones:** This is all the theory of operation, there's your character set, which would be burned into the mask ROM, because we didn't see any of that EEPROM rubbish in here. And there's all the, like, all the other codes. I've really used more than, like, a handful of those, really, even back in the day, when

**Dave Jones:** you, control G still works, there's the power supply converter, voltage regulator, failure protect, soft start, oh, it's even got soft start, fantastic, look at this, here's all the theory of operation just for the power supply, fantastic, the 8080, so comprehensive, got flow charts, wow, brilliant, oh, there's the acoustic, there's the frequency shift

**Dave Jones:** key-in for the, I thought they only used frequency shift key-in at the 1200 board, oh, yes, no, of course they did frequency shift key-in, they, there's two separate frequencies they use, the two separate ones they use, there's a transmit and a receive pair with two different

**Dave Jones:** frequencies each, and that's how the 300 board worked. My rusty memory, I'm sure everyone will tell me if I'm wrong, I'm not going to bother to check that, and, like, you know, 1100 kilohertz or something, you know. Now we're getting into troubleshooting checklists, fantastic, like, this is brilliant stuff, look

**Dave Jones:** at these, like, they're going to have lots of exploded diagrams too, I'm sure, look at this, everything's got its own part number, yeah, here we go, now we're talking, look at this, beautiful, we've got the bomb. Look at, you know, it's a huge amount of details gone into this, some people drew this

**Dave Jones:** and then checked it and then triple checked it, fantastic. I was still doing hand-drawn stuff like this at, yeah, yeah, we're still doing it at CERCEL, so we're still doing it, like, I'm talking 12 years ago, probably, not that long ago, we were still, oh, maybe, okay, like, I'll say, you know, we were still doing it

**Dave Jones:** 15 to be safe, but, yeah, like, 12, 15 years ago, I was still doing hand-drawn documentation like this on sheets, and we'd have to, we'd have to master copy, then we'd have a photocopy copy, which was on a different part of the site, just in case half the building burnt

**Dave Jones:** down or something, and then we had an off-site copy as well, and all these huge A3 folders, I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid.

**Dave Jones:** I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid.

**Dave Jones:** I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid.

**Dave Jones:** I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid.

**Dave Jones:** I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid. I've still got some of the original CERCEL grid.

**Dave Jones:** I've still got some of the original CERCEL grid.
