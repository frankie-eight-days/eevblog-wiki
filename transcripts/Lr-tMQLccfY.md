---
video_id: Lr-tMQLccfY
title: EEVblog #382 - Cambridge Z88 Teardown
url: https://www.youtube.com/watch?v=Lr-tMQLccfY
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 35, "3": 49, "4": 67, "5": 78, "6": 92, "7": 102, "8": 116, "9": 132, "10": 144, "11": 162, "12": 178, "13": 195, "14": 210, "15": 226, "16": 239, "17": 255, "18": 271, "19": 286, "20": 303, "21": 316, "22": 331, "23": 350, "24": 368, "25": 389, "26": 410, "27": 433, "28": 449, "29": 467, "30": 490, "31": 505, "32": 519, "33": 534, "34": 555, "35": 578, "36": 599, "37": 616, "38": 632, "39": 647, "40": 658, "41": 672, "42": 688, "43": 701, "44": 717, "45": 733, "46": 750, "47": 768, "48": 789, "49": 808, "50": 826, "51": 839, "52": 851, "53": 867, "54": 885, "55": 901, "56": 916, "57": 935, "58": 951, "59": 967, "60": 979, "61": 992, "62": 1007, "63": 1020, "64": 1034, "65": 1050, "66": 1064, "67": 1077, "68": 1096, "69": 1114, "70": 1134, "71": 1152, "72": 1168, "73": 1185, "74": 1205, "75": 1215, "76": 1228, "77": 1246, "78": 1262, "79": 1277, "80": 1297, "81": 1311}
---

**Dave Jones:** Hi, it's retro computer time again. We're going back to the future. Ta-da! It's the Cambridge Z88 notebook computer. Z80 based, of course, as you can tell from the title. This comes from the legendary Clive Sinclair out of the UK. And he's developed uh

**Dave Jones:** several computers over the years, famously the uh ZX Spectrum and the ZX 81, but this is the only one that came from the Cambridge company, which he set up. And this is here. It's A4 notebook size, huh, before they even

**Dave Jones:** called them notebooks. And uh under a kilo. It's a really neat little bit of kit. I like it. Now, I thought we'd tear it down and as a bonus, this one doesn't work. So, I thought we'd have a shot at

**Dave Jones:** uh troubleshooting this thing, possibly fix it. Let's give it a go. Good on you, Clive. And here it is in all its glory. It's got one of these sort of rubber uh membrane type uh keypads. I mean, they're raised keys on there, but

**Dave Jones:** it feels very spongy and uh rubbery. I guess it was designed to be silent, you know, so you're using this thing out on the road, you're a road warrior. Um you know, back in the days when well, you

**Dave Jones:** know, these things were uh used a hell of a lot by uh journalists and things like that, especially the uh Tandy 100/102, which I have uh torn down in a previous video, which I'll link in here if you

**Dave Jones:** haven't seen it. And uh this it it's a really nice bit of kit. I'm not sure what the uh resolution of the screen is. I haven't uh checked, but it's, you know, it looks like it's a 80 characters

**Dave Jones:** by eight lines or something, maybe. Um it's got all the uh uh various shortcut keys. I don't know why they bothered there, really. And uh you know, it's got some arrow keys, pretty basic keypad though. Index, menu, help, blah.

**Dave Jones:** Not much else. Pretty boring. Um, on the side here, we've got a DC input jack, uh, contrast, nothing on the top. And on the side here, it looks like we have a serial port, RS-232 serial port, but that's pretty much, um,

**Dave Jones:** all she wrote in terms of, uh, ports, although there is a uh, connector under here. So, let's have a look at that. And looks like we have a card edge connector there. Um, I'm not sure what, uh, that's

**Dave Jones:** designed for, some sort of, uh, expansion, uh, header connector. One of the big selling points though of this thing were these EPROM and memory packs. Now, these EPROM packs, they're, uh, just like proton packs, except not as cool. Sorry, another 80s joke there.

**Dave Jones:** Um, and yes, they are actually EPROMs. Check it out. There's the EPROM inside there, standard DIP package in there, I'm sure, with the EPROM window. Now, now that one's a 32K EPROM, so that would be, you know, a standard, uh, 27C,

**Dave Jones:** uh, 256 or something like that. This one is a much bigger 128K EPROM, and you can see it in there, much bigger die in there. So, you can actually UV erase these things, and, uh, these were, so this actually contains an

**Dave Jones:** EPROM programmer in it. So, it's got to generate the 12-V high voltage, uh, programming pulse, presumably, um, to program these particular EPROMs. But, you can also plug memory into these. These are 128K RAM pack, and you can expand this thing

**Dave Jones:** up to 4 meg or something like that. It was actually quite, uh, a lot of memory for its time, really. So, um, this thing, in terms of memory expansion, was, uh, really, um, quite a significant machine. And it comes with, uh, 32K of

**Dave Jones:** RAM built in, but of course, you can expand that with the pack. It, uh, operating system in this thing is a custom one. It's called Oz. Beauty. And it came with you know a word processor and stuff like that called

**Dave Jones:** Pipe Dream and a spreadsheet I believe. So there were some built-in apps. You just power the thing on and it ran from four double A batteries for about 20 hours. Brilliant. There's a nice little flip out thing here so it tilts it while

**Dave Jones:** you're using it on the desk there. Really quite neat. And there's something you don't see every day. Made in Scotland by SCI UK Limited. Serial number 2938. Hi to all my Scottish viewers. Sorry, I can't do a Scottish accent. And if I

**Dave Jones:** could, you wouldn't be able to understand me cuz nobody can understand the Scottish accent, can they? And damn it, wouldn't you know it, it decided to work. This thing was not working before and I was hoping to do a troubleshooting

**Dave Jones:** video. Ah, what a bummer because I was able to going to start out with the fact that when I plugged in the batteries I could hear a very faint high-pitched you know DC to DC converter noise in there. So I was going to you know

**Dave Jones:** mention that you know start troubleshooting. Ah, you've got to use all your senses. You know your sense of sight, your sense of smell and your sense of hearing as well as touch. You know as to see if anything gets hot.

**Dave Jones:** Things like that. So I thought I you know I heard something in there and I was going to start with that. What a bummer. Ah. Sorry. It's just going to be a teardown video I think unless it's intermittent. I don't know. Mike and I

**Dave Jones:** uh Oops. Hey, I just got into basic there somehow. There you go. I just got into the uh Z80 basic version 3 copyright RT Russell. There you go. Who is RT Russell? Hmm. There you go. I just Googled it and it's a Richard Russell

**Dave Jones:** and his company RT Russell was set up to supply the basic to the BBC micro back in the early '80s and the same basic interpreter was also included in the Amstrad and NC100 and other machines. So, there you go. Good

**Dave Jones:** on you, Rich. Now, this thing I expect to find uh through-hole technology, of course. There might be some surface-mount stuff. There'd be some surface-mount stuff for like the LCD driver and uh stuff like that, I'm assuming. Because it was definitely a '87, so

**Dave Jones:** surface-mount was around before then, but uh I expect to see some classic stuff. It'll smell like vintage electronics, too, which will be fantastic. And uh Got a whole bunch of Phillips screws here. And this is based on the Z80A

**Dave Jones:** CPU. Working at a whopping 3.5 something MHz. So, absolutely screaming along for the day, but you didn't need anything faster than that, really. Have I forgotten something? No. Ta-da! Oh, hang on. Hang on. Hang on. It's falling apart.

**Dave Jones:** Looks like this top just pops off. Oh. Here we go. I forgot to take the batteries out. Oops. So, there you go. It's rather interesting in that uh that front bezel just lifts off and there's the battery compartment. Looks

**Dave Jones:** like there's an inductor down there. We'll have a look at. Look at that. There's the D9 connector with a resistor soldered onto the shell, as well. Look at that. I love that. Absolutely classic and the LCD Oh, there we go. It's an Epson made in

**Dave Jones:** Japan and that one is a just like an 8-bit parallel interface or something. So, that will have a whole bunch of SMD drivers in there, but uh that will come out later and hey, here we go. Ta-da! There it is. Yep, a mix of uh basically

**Dave Jones:** mostly through hole um through hole resistors, through hole caps. Just briefly go through the main board here. We've got uh contrast pot over here. We've got a reset switch right up in the corner there. DC input jack. Um

**Dave Jones:** we've got a super cap there to hold the uh charge when you replace the batteries cuz you don't want to lose every everything if you haven't got them inside your 128K RAM pack. I mean, these are these aren't dynamic RAMs. These are

**Dave Jones:** only SRAMs, so they don't need anything. They can run off the sniff of an oily rag these things. And there's the main uh there's the built-in 32K SRAM chip. We've got our EPROM there. That's the system ROM. I think it was

**Dave Jones:** 128K system ROM or something. It's got 2.2 written on it. Version 2.2 presumably. And what's SKS? Not sure, but 1987 Cambridge Computer Limited. Uh we've got another chip over here. We'll have a look at that. Here's the main uh Z80 CPU. That'll be the Z80A.

**Dave Jones:** There's the 3. uh 8.304 MHz crystal and a little piss-ant speaker there. And it looks like there's another little switch hidden inside there. So, you can sort of access it through that option compartment. I to what that little uh sneaky switch there does. I

**Dave Jones:** don't know, but uh there's a whole bunch of uh TO-92 transistors all bent over here. Lovely standard uh axial 5% carbon resistors. Oh man, beautiful. Oh, classic double-sided board, folks. All through-hole technology. Just love it. Looks like there's got a 32 kHz

**Dave Jones:** watch crystal there as well as you know, they've got some uh some crusty old sided tape there sticking down that crystal. That used to be be a very time-honored uh method of uh dodgily sticking down your crystal. Just whack it on some double-sided tape.

**Dave Jones:** Who cares how long it lasts? And there's the Z80 CPU. It's supposed to be a Z80A, but it only says Z80 on there. Anyway, it's 8722. So, this one was manufactured Well, that chip was manufactured the 22nd week of

**Dave Jones:** 1987. So, this one uh is because it's serial number 2000 or something. These are very early unit. It's probably one of the first uh runs. In fact, it probably was the first uh production run on the thing. So,

**Dave Jones:** uh looks like we've got an inductor there for some sort of little switch mode. I don't even know if it's a cuz I don't see a controller around there. There might be, you know, a couple of switching transistors or

**Dave Jones:** something. I don't know, but so I'm not sure what that inductor's doing up there. Uh Not entirely sure, but anyway, oh hey, hang on. It just switched off. It just switched off. Oh, I'm not sure if it did that because

**Dave Jones:** it's going to sleep or uh because I touched something or or it's intermittent somehow. Well, I managed to get it going again by just uh hitting this button here, which looks like it's a power button cuz you hit it

**Dave Jones:** and it you know, but why it's recessed like that? Maybe it Well, no, it looks like there's, no you know, looks like it was actually a recessed hidden switch. And by the way, this one down in here, if

**Dave Jones:** you hit this, it beeps. And looks like it it doesn't Well, it resets the thing and refreshes the screen. So, all right, I figured it out. This is the soft reset switch down here, and this one is the hard reset, by the looks of

**Dave Jones:** it. There you go. And because if you push this one up here, it'll actually tell you it very quickly up there, soft reset. So, there you go. And it tells you it's running OS. I like it. Brilliant. Um so,

**Dave Jones:** it seems to work just fine. So, let's have a look at some other stuff we've got in here. I mean, all the TO-92s uh transistors there bent over, absolute uh classics. They're uh BC uh 558s and stuff like that, 548s. And we've got an

**Dave Jones:** NEC uh D What is it? D 65031GF168 there. I have no idea what that one is. Obviously some sort of uh glue logic to replace a couple of uh devices that, you know, that are used in a traditional Z80

**Dave Jones:** architecture machine. But uh yeah, look at all the I mean, they've got one resistor network there, one single in-line resistor network there. But everything else, they got resistors everywhere and transistors everywhere. Very discrete design. And uh there's a super cap. Of

**Dave Jones:** course, that's a 5.5 V uh NEC 0.047 F. There it is. And uh that is about all she wrote. There's not much else. There's a variable resistor there. Not sure what that one uh is doing. But yeah, there's a curiously

**Dave Jones:** there's this metal bar along the uh along these expansion plugs here. So, I'm not actually sure what that's used for. You know, it's like a stiffener or something like that. You know, it's not really performing any sort of um shielding function at all

**Dave Jones:** really. So, um probably some sort of stiffening bar just for that just for holding that connector in place. But, why it doesn't go all the way extend all the way to the end, I don't know. And there's a there's a weird ass uh

**Dave Jones:** expansion connector for the cartridges. And uh you can it looks like you can hot swap these things. It just sort of uh blanks the screen for a second and then pops back up, but I can't seem to access those.

**Dave Jones:** Got no idea how to use these things, but there you go. Pretty old school. And I've got manual wiring, of course. You know, they've just soldered that uh serial cable directly into the uh pins on the board. They're pretty dodgy. You know, they've

**Dave Jones:** got that there's that resistor going through to the uh uh shield on the um D9 connector. Uh dodgy as. It's a very dodgy 80s construction here, you know, but this is what it was like back in the 80s. This is how they'd manufacture

**Dave Jones:** these things. So, um you know, it's they sort of really haven't hadn't perfected the mass manufacturing techniques that they have these days with the surface mount pick and place machines. Although, you know, we've got a perfectly good, you know, surface mount device there.

**Dave Jones:** They didn't extend that anywhere else on the board. And if we flip the board over and have a look, it's uh pretty uh conventional. Nothing going on there at all. No hacks, no mods, except for this weird looking

**Dave Jones:** add-on. Check this out. I don't think I've ever seen anything like that before. They've got this big copper strap going from this ground trace over here near the battery section down the bottom here and it's just jumping that all the way over

**Dave Jones:** to there. They've got a plastic spacer which moves on the bottom of that and so it basically connects this big ground trace over here all the way over to here and why they've done that I have no idea.

**Dave Jones:** It's obviously not serving any useful shielding purpose so they've it seems as though they've done it for layout reasons. Like they you know they routed the the battery ground point down here and they went well you know I we have to somehow get this

**Dave Jones:** all the way over to here and well we've only got a double-sided board don't have the luxury of a multi-layer board so we're going to have to jump the thing all the way across and rather than putting your traditional link which you

**Dave Jones:** don't see any of here on on this unit by the way there's no wire links on this thing. Um they've just used a big wide copper strap. I don't know they don't need the current handling capability so why they

**Dave Jones:** don't just didn't wire in just a you know a black mod wire or something like that um I don't know for some reason they decided on that. Weird. Well I jumped to the conclusion that what that was the ground but I measured

**Dave Jones:** it and it's not it's actually the battery positive and uh it's and there it is of course it's obviously here. Look at the wire the battery positive's there and the negative of the battery is not until all the way over on this side

**Dave Jones:** of the board here. So it's almost as if like they um maybe you know needed some extra current cuz it does go out to one of these traces out here for this expansion header but jeez you know why it's that

**Dave Jones:** huge and wide just to jump over to here? I don't know. And how much does it draw during operation? Well, 60 odd milliamps just sitting there at the main index screen. And they have actually used two jumpers on the top here. You can see these two

**Dave Jones:** black wires going from the negative terminal of battery over here. One goes once terminated there at that point, and the other jumps all the way over right to the other side of the battery terminal right over here. So, instead of

**Dave Jones:** routing those, I guess they ran out of routing room. They had to jump those all the way across. Oops. Now, I was actually wrong on that clock frequency. It's actually 9.8304 MHz. So, what I'm going to do is just

**Dave Jones:** probe the clock here and see what this thing's doing because I suspect that it's not possibly not running all the time. Um because these things like, you know, this to get it's 20 hours uh battery life. These things went into sleep a lot, so it

**Dave Jones:** might be waking up, for example, when you press a key. So, it might be sitting there waiting for a key press. So, let's probe the Z80 processor down here. Um pin six is the clock line for a Z80, a 40-pin

**Dave Jones:** DIP Z80. So, 1 2 3 4 5 6 Hello. Hello. There we go. And look at that. I'm at 2 V per division, so it's 2 4 6. So, it's running practically directly from the battery voltage. So, it looks like it's

**Dave Jones:** not 5 V regulating that, and that looks continuous. Uh Let's say no. Hello. There you go. Check that out. Aha. Look at that. There's Looks like there's a group of two bursts. Oops, the thing just switched off on me.

**Dave Jones:** The screen's gone. So, let me reset that. Ah, there we go. And we're back. So, there was no clock frequency when it was dead like that. So, I'm not sure what's going on there. But anyway, we're uh 50 microseconds per division there. So,

**Dave Jones:** 100 200 300 400 microseconds it goes for in two bursts there. I'm not sure why it has that uh dead period in the middle of it. But uh 400 odd microseconds and then aha, there you go. It repeats

**Dave Jones:** that. Repeats that every two divisions 10 milliseconds. So, there you go. Every 10 milliseconds there's a 400 microsecond burst of clock and uh it's able to get away with that because uh it's obviously doing nothing. And if we actually ran a program, we would

**Dave Jones:** probably see that change. So, I might try and run a basic program and or something and see what happens. All right, I've got a very simple basic program there. It's just going to count up to a high number, print it on the

**Dave Jones:** screen, and keep doing that for a while. So, let's run that and see what we get. All right, so that's what we're currently getting. So, let me just type in run here. Oh, you can see that every time I press a key,

**Dave Jones:** bang, it sort of extends that pulse out there. So, I'm going to press run and we should get a continuous clock. Yep, there we go. Fully continuous. And our screen Now, things counting up. It's only to Oh, it's not even to 200 yet. So,

**Dave Jones:** it's uh pretty slow this old sucker. And I've turned on the hardware frequency counter here and it's 3.266 odd MHz. So, there you go. It's obviously dividing that crystal that 9 MHz crystal by three. But if you have a look at that, there is

**Dave Jones:** still a period in there where it blanks out even though it's continuous. I'll try and single-shot capture that. There we go. Bingo, we got something. And we can zoom into that here. And notice there's a dead period there

**Dave Jones:** of 5 10 15 20 almost like around 24 microseconds. There's a dead period. So, it obviously needs to or is stopping the clock for some particular reason for 24 microseconds in there. Not sure why. And look at this. This is what it was

**Dave Jones:** like in the '80s. This is how slow computers were in the '80s. Check that out. Haha. Every cycle was sacred. Ooh, it's like whistling Monty Python. So, I'm sorry I wasn't able to bring you a troubleshooting video that I was

**Dave Jones:** hoping for. Maybe next time, but we all like a good vintage retro computer teardown. And this one was an absolute classic. I hope you liked it. The Cambridge Z88. Haha. Clive. What a winner. Catch you next time.
