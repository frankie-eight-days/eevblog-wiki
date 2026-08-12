---
video_id: W40qGkp-mEU
title: EEVblog #746 - Sharp X68000 Retro Computer Teardown
url: https://www.youtube.com/watch?v=W40qGkp-mEU
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 26, "3": 40, "4": 50, "5": 64, "6": 74, "7": 88, "8": 99, "9": 114, "10": 125, "11": 144, "12": 157, "13": 169, "14": 180, "15": 189, "16": 197, "17": 207, "18": 220, "19": 246, "20": 260, "21": 275, "22": 290, "23": 308, "24": 320, "25": 331, "26": 348, "27": 357, "28": 367, "29": 380, "30": 400, "31": 410, "32": 419, "33": 434, "34": 452, "35": 464, "36": 476, "37": 487, "38": 503, "39": 513, "40": 537, "41": 552, "42": 561, "43": 577, "44": 584, "45": 602, "46": 612, "47": 639, "48": 655, "49": 668, "50": 681, "51": 695, "52": 711, "53": 726, "54": 742, "55": 757, "56": 769, "57": 778, "58": 789, "59": 812, "60": 826, "61": 846, "62": 855, "63": 879, "64": 890, "65": 911, "66": 919, "67": 934, "68": 956, "69": 970, "70": 980, "71": 993, "72": 1006, "73": 1027, "74": 1042, "75": 1054, "76": 1075, "77": 1091, "78": 1105, "79": 1117, "80": 1130, "81": 1147, "82": 1169, "83": 1176, "84": 1185, "85": 1198, "86": 1213, "87": 1222, "88": 1232, "89": 1252, "90": 1260, "91": 1278, "92": 1294, "93": 1312, "94": 1324, "95": 1339, "96": 1356, "97": 1367, "98": 1389, "99": 1401, "100": 1411, "101": 1424, "102": 1440, "103": 1456, "104": 1473, "105": 1485, "106": 1499, "107": 1511, "108": 1517, "109": 1528, "110": 1541, "111": 1551, "112": 1564, "113": 1580, "114": 1602, "115": 1612, "116": 1621, "117": 1639, "118": 1656, "119": 1671, "120": 1684, "121": 1697, "122": 1718, "123": 1730, "124": 1740, "125": 1750, "126": 1763, "127": 1778, "128": 1786, "129": 1802, "130": 1813, "131": 1824, "132": 1846, "133": 1859, "134": 1869, "135": 1879, "136": 1893}
---

**Dave Jones:** Hi, it's vintage computer teardown time again. We love vintage computers here on the EEVblog and this one is going to be quite interesting. It's one I had never heard of before.

**Dave Jones:** It was sent into the mailbag segment by a Alex from Japan. So, thank you very much, Alex. This is the Sharp uh X68000 home computer gaming machine. It was uh a personal computer if from 1987.

**Dave Jones:** This is one of the original models. In fact, Alex says it's the model CZ-600CB. It's got a 10 MHz processor. Guess which processor, hmm? And a walk-in whopping 1 meg of RAM.

**Dave Jones:** And apparently, this was a quite highly sought-after machine for gamers cuz it had a lots of uh real arcade game uh emulations on here, like real proper emulations and things.

**Dave Jones:** So, it's a it's a real interesting um construction. Yes, it's designed to be vertical like this with the dual uh floppy drives. It's even got a little pop-up carry handle, which doesn't work that well anymore.

**Dave Jones:** So, I thought we'd tear it down and see what makes this puppy tick from 1987. You know, what we say here on the EEVblog, don't turn it on, take it apart.

**Dave Jones:** So, this thing's a little bit annoying to get on camera with this vertical uh profile here. They did actually make uh ones with horizontal profiles. So, we'll just flip it on its side like that and take a look, shall we?

**Dave Jones:** Um down there well, up the uh top here, we've got just some uh status LEDs. Um timer, hmm, not sure what timer is for, but uh high-resolution mode, uh two 5 and 1/4-in floppies.

**Dave Jones:** Ah, 5 and 1/4's for the win, awesome. Um mouse port, keyboard port, volume uh control, one joystick port on the front, the second one's on the back, and some headphones as well, and a soft uh power button.

**Dave Jones:** Feels like a bit of a clunky power button, but apparently it is a soft power button that was a bit of innovation for the day. And on the top, upside down, so all the electrons are going to fall out, we have a reset switch and an interrupt switch.

**Dave Jones:** I love it. Let's just interrupt the operating system, which by the way, it uses its own custom operating system called Human 68K. And it's like got a similar interface to DOS, um apparently, but yeah, it's it's not compatible.

**Dave Jones:** It's its own thing. So, this is the this is actually the original one released in 1987, the uh CZ-600CB. And there were many other models, like a dozen or so, released um in the years after that, up to 1993.

**Dave Jones:** And on the back here, we have a couple of expansion slots. We've got a remote interface. We've got a printer interface with uh just a uh header ribbon cable there.

**Dave Jones:** We've got a hard disk interface, which um is not SCSI compatible. Yeah, it uses a Japanese variant of um SCSI, which was their own uh thing. Expansion floppy drive.

**Dave Jones:** Not sure why you'd need more than the two internal floppies. Anyway, um big clunky power on-off uh switch um in addition to the soft one on the front. We've got AC output.

**Dave Jones:** This is 100 V, of course. I'm not going to plug it into the 240 V mains here in Australia. We've got a second joystick port port, audio in and out, RS-232.

**Dave Jones:** I don't know if you could ever get like a modem or anything uh for it. Anyway, the main monitor output was analog RGB. And it's got uh image input as well.

**Dave Jones:** See-through color. Not quite sure what that does. TV control and stereoscopic, which I believe somebody mentioned as in like it can do like cinema type of 3D thing with the different colors.

**Dave Jones:** So, to produce stereoscopic images. Very interesting. And curiously, it's got two ground terminals here labeled FG. So, I guess you can ground systems together. Hmm. Now, this thing cost uh 375,000 yen when it was released in 1987, around about uh 1,500 Yankee bucks or thereabouts.

**Dave Jones:** So, you know, it wasn't a uh cheap low-end machine, especially for the day with 1 meg of memory and a and a 10 MHz 68000 processor in it. It uh was quite a high-end machine.

**Dave Jones:** Yeah, apparently it had quite a lot of uh pixel-perfect uh arcade game ports. That's why it was uh extremely popular with the gamers and apparently still is. Um has some niche appeal and things like that.

**Dave Jones:** I have no idea how to take this thing apart, so I've just taken off some screws I found on the bottom, but hmm. And Alex said these things are notoriously bad uh have what have notoriously bad power supplies in them.

**Dave Jones:** So, yeah, that'll be interesting to look at. So, I've got the bottom screws out, but jeez, I don't know. These two things are screwed together somehow. There's some screws on the other side, but how do I separate the two modules?

**Dave Jones:** Jeez, this is a weird-ass teardown, that's for sure. Um please excuse the um when I put my hands in it overexposes and stuff like that. That's a problem with uh recording black objects like this.

**Dave Jones:** It uh it's sort of if I got auto exposure in, it sort of gains it up. I can turn off auto exposure so it doesn't uh do that, but yeah, anyway.

**Dave Jones:** I'm getting somewhere. I've got expansion cover off. There were three screws here, but there's like screws under here, so I don't know how to get to those. And are there plastic clips retaining clips under there?

**Dave Jones:** Ah. Good, isn't it? Hang on. Does this This feels like it might It might slide or pull off or something. Yep, it could be a retaining clip under here.

**Dave Jones:** Let me play with that. Aha. Just had to give it a bit of a hit on there and tada. Ah, we're in like Flynn, but unfortunately we got some shielding in the way.

**Dave Jones:** Bummer. We've got the lid of the first module open and it's clearly the processor module because well, there's our 68,000. I'll show you what that up close for you fanboys in a minute, but it's surprisingly chock-a-block.

**Dave Jones:** Huge amount of memory array up here and well, there's our battery hasn't leaked and it's actually surprisingly tidy actually. Clean and tidy this one because the bottom Well, the other module, I'll call it the second half of this thing actually has the fan down here.

**Dave Jones:** So, this has got the mains power supply and it looks like some, you know, hard drives, you know, some floppy drives and the expansion and stuff like that, but all the processing grunt is all up here.

**Dave Jones:** But look at this second board here which we'll have to take out. There's a huge big PGA device up here. Pin grid array. None of this BGA ball grid array rubbish.

**Dave Jones:** No, sirree Bob. And it's very well annotated too. All the board all the component designators. Look, even the caps have cap symbols on them. Very, very nice. I've got another large memory array up on here.

**Dave Jones:** So, I'm not sure what else is doing on that board anyway. They obviously couldn't fit on the main board. Surface mount devices over here. Pretty fancy pantsy for 1987 and we've got a and Sharp branded ones as well cuz Sharp are big semiconductor manufacturer.

**Dave Jones:** So, it'd be no surprises for seeing them roll a couple of their own chips at least. And there it is, the 68,000 processor. A lot of people are going, "We are not worthy.

**Dave Jones:** We are not worthy. We are not worthy." Anyway, um yes, socketed, and but it's not a genuine one. It's a Hitachi uh rip-off one. Well, you know, not rip-off, but they did um second source it, I believe.

**Dave Jones:** Now, this is interesting, Buddha. Now, I um I had a look, and this is apparently the system controller. That's the code name for the system controller chip. They didn't use that in all the models.

**Dave Jones:** This This Buddha uh system controller chip um that'll be a custom ASIC manufactured by um Sharp, presumably. It's got Sharp brand on it, anyway. Um Sharp did a ton of their own uh ASICs and semiconductors, so yeah, no surprises they could easily do that.

**Dave Jones:** But um this was not used on later ones. They upgraded and gave them different code names as they released uh bigger and better versions of this system. Anyway, this one's the Buddha.

**Dave Jones:** And check out these 74ALS244s. I just mentioned this because they're ALS. They're not exactly uh low-power devices, although they're advanced low-power Schottky. That's what ALS uh stands for. But no wonder this thing um the these old-school machines uh took like quite a bit of power, even though they're only only, in quote marks, running at a processor speed of 10 MHz.

**Dave Jones:** And no surprises for finding a HD63450 next to that. That's the matching uh DMA direct memory access controller for the 68,000 CPU. And these two socketed puppies here look for all the world like mask ROMs.

**Dave Jones:** There we go. They're not uh window devices. You can actually see maybe the uh a round divot in there. But yeah, these are almost certainly the mask uh ROM firmware in the thing.

**Dave Jones:** And bingo, we have a date. Look, 8730, 30th week, 1987. Awesome. And these surface-mount parts here, these are very interesting. They've all got once again custom Sharp parts, by the looks of it.

**Dave Jones:** You might think, "Okay, look at the array of them. They're memory or something like that." I don't think that's so. They all seem to be like a separate controller.

**Dave Jones:** Look, IX0894, IX0 IX0893, IX092, etc. So, it's almost they got like you know, a separate custom chip and a whole you know, like an array of six of these.

**Dave Jones:** What the What are they doing? Some sort of memory access thing or something perhaps, but we've already got the DMA controller here. What are these things? I got no idea.

**Dave Jones:** Maybe something to do with the expansion bus maybe. Some sort of custom expansion controller perhaps. I'm not sure. Now, I'm trying to get the main board out here. This front panel here does actually clip out as well from the underside under there I think, but I can't quite get it at the moment, but um I think I can actually wiggle the entire board out if I'm very

**Dave Jones:** very careful. Get it over this metal lip here or something and it should lift out. But jeez, yeah, it's kind of tricky business. I got the floppy cable off and ta-da!

**Dave Jones:** We're almost out. It's a bit dusty down the bottom, but bingo, we got it. Awesome. So, there it is. We're in like Flynn. We got the whole module out here and that wasn't actually too bad at all.

**Dave Jones:** So, main processor board on the bottom here. This top board with the separate memory clearly the video card and the big PGA and couple of looks like another couple of sharp system A6 there.

**Dave Jones:** That's got to be all video card here and the RGB is down here. It connects I think it you know, it must be doing all the video processing down there on the bottom.

**Dave Jones:** That's all I can uh Oop. There we go. Ooh, we have Cynthia and Cynthia Jr. Let's check them out. Well, hello Cynthia and Cynthia Jr. Another big PGA device because this is the board-to-board connector here that goes up to the video board.

**Dave Jones:** So, this I think this is some sort of Cynthia is some sort of video interface uh controller, something like that. Um not actually the video controller itself. That's the other uh PGA device up on the main board, but uh yeah, and then another DIP package um there.

**Dave Jones:** Why they're doing a DIP package um synth- for Cynthia Jr. there and not a an SMD like they did for the others, I'm not sure, but anyway, it is um all top-sided uh load except for a little bodge capacitor on Hysteria here.

**Dave Jones:** I love the names. Brilliant. Uh look at that. We better whip that battery out quick smart. It is gonski. It's made in Japan as well. Um and yeah, look, you can see some corrosion happening around here.

**Dave Jones:** Doesn't look that bad and it's extended over to the steel case of this oscillator over here. Woah, thankfully it hasn't gone too much further. It shouldn't really affect it, I don't think.

**Dave Jones:** Maybe there might be a trace broken, might have gotten onto the uh copper layer in there. Mm, not sure though. Let's hope not. There you go. That cleaned up rather nicely.

**Dave Jones:** I think we caught that sucker in the nick of time. The negative pad of the battery down there is a little bit cactus. So, yep, just got that one.

**Dave Jones:** Ooh. Now, the frequencies of these two crystals are rather interesting. Look at this, 69.55199 MHz and 38.86363 MHz. Now, what are they doing? Now, my first thought there was that of course these are a multiple higher multiple of the color burst frequency cuz this unit is supposed to have an NTSC video output.

**Dave Jones:** So, yeah, but you divide that by the 3.579545 MHz NTSC color burst and well, it's not an exact multiple of either of those and neither is the power color burst frequency either.

**Dave Jones:** Hmm, well, check out Cynthia. Wow, ceramic package, metal top. Look at that, beautiful. Poor old Cynthia Jr.'s feeling very Marsha, Marsha, Marsha. So, why would they have split Cynthia up into two chips like this?

**Dave Jones:** Well, it's a good question and of course, as I said, they consolidated, uh, I believe in the pre- in the following models into the one Cynthia chip. So, they absorbed Cynthia Jr.

**Dave Jones:** into Cynthia. So, why didn't they build Cynthia Jr. into Cynthia to begin with? Well, my educated guess is well, they designed Cynthia and then they prototyped it and well, it was okay and then they came along and went, "Oh, it'd be nice if we added this or oops, we forgot to add this." And bingo, rather than respin this whole chip, they just did another little uh, you know, tiny little thing for

**Dave Jones:** Cynthia Jr. here and whacked it in a 28-pin plastic package. Thank you very much. So, there you go. That's the complete main logic board minus uh, I presume is the video uh, board and processor on top.

**Dave Jones:** We've got ourselves yet another sharper custom ASIC here. It's called ET, I think. Um, phone home. Thank you very much. Um, another oscillator here that's 40 MHz so, that'll be divided by four to get the main 10 MHz system clock and 20 MHz and other um, stuff that it needs to do.

**Dave Jones:** And then we've got all our video output section down here we'll take a quick look at. So, Cynthia and Cynthia Jr. I mean, Cynthia here could be the main video processor.

**Dave Jones:** I'm not sure, but then what does that one do? Hmm. So, here's the video board. Nothing two custom ASICs here, Vinas 1 and Vinas 2, whatever the hell they are.

**Dave Jones:** We've got It says reserve over here, so I don't know what reserve does, but got some weird ass names. And then we've got the V Sop. That is the what looks like well, you know, P probably stands for processor, V probably stands for video, so video system output processor operational processor or something like that perhaps.

**Dave Jones:** It's another very sexy ceramic package from Sharp. Interesting. Well, got some I got to be super fast 74F series. Pissing away the power here. And curiously, they've got three of those socketed there, the 74Fs.

**Dave Jones:** What they expect those to fail or maybe they were hedging their bets and goes, "Oh, maybe we can get away with ALS. Oh, I don't know. Oh, damn it.

**Dave Jones:** We'll have to put F in for the final production units." But hey, we've got an F 245 over here. And of course all of our video memory in SIP packages, which we saw on the main board as well.

**Dave Jones:** But what this D25 image in connector was labeled on the back is on this board, I don't know. Is it some sort of video capture thing? It doesn't seem to have any you know, hardcore hardware associated with it.

**Dave Jones:** I don't know if anyone's got any clue what image in does, then let us know. Some sort of display synchronization thing between machines perhaps. Hmm. On second thought, if you follow these traces down here from the connector over here, then bingo, it's going to this reserve controller by the looks of it.

**Dave Jones:** There's a chipset near the crystals here called hysteria. Once again, a custom Sharp ASIC. Geez, they really went to town on this thing. So, what does it do? Well, most likely some sort of uh clock controller timing chip, something like that.

**Dave Jones:** It's down here. Now, there's a real-time clock crystal here. There's a real-time real-time clock chip right there to match up with that, but this is the main oscillator, of course.

**Dave Jones:** And tucked away down in there is the MC68901. That's the multi-function peripheral chip for the 68000 CPU. It's a bit of a big uh beast physically, but it's got the like timers, counters, interrupt control, and all that sort of miscellaneous stuff you need in a PC.

**Dave Jones:** Not sure what the deal is with that symbol there. Anyone know? And then our main system memory here, this is the DRAM. These are in single in-line packages. You don't see those anymore these days, but in terms of board mounting density, very, very nice.

**Dave Jones:** So, it's actually a nice package. I I like it. Um these are MB81256-12. You can probably yep, just see that in there. And 120 nanoseconds, of course, access time.

**Dave Jones:** That's what the dash 12 on the end means. And the 256 is a dead giveaway that this is a 256K bit DRAM, not megabit. K bit, thank you very much.

**Dave Jones:** We're talking 1987 here. And of course, eight in a bank like that makes one byte. So, you've got 256K bytes, 512, and then total of 1024, 1 meg of system memory.

**Dave Jones:** Awesome. Now, for me, one of the interesting things to note about this whole thing is look at the amount of standard 7400 series logic. As we saw mostly ALS, but some other families like S and S and just straight 7400 even on here.

**Dave Jones:** And that's strange considering that they've rolled their own chips everywhere else, right? Sharp are one of the big semiconductor manufacturers. They can do this sort of stuff. Why they didn't consolidate a lot of this other miscellaneous stuff into at least CPLDs, for example, PALs and GALs and things like that.

**Dave Jones:** I don't know. They could have gotten a bit more density out of the thing. But yeah, maybe that was just easier at the, you know, at the design time.

**Dave Jones:** Maybe they didn't have the resources. Maybe they were too busy doing all their big custom ASICs and and everything else. So, who knows? And here's the video output driver.

**Dave Jones:** We've got a Mitsubishi M51 387P. That's a triple video driver, so an RGB driver, one for each channel, red, green, and blue. And there's our video output down here.

**Dave Jones:** So, yeah, lots of analog stuff associated with that. That's basically pretty much the only analog stuff on this main design. And of course, it looks like the video is coming from Cynthia up here cuz these are the board-to-board that go over to the main video board.

**Dave Jones:** But look, you can just just follow the traces. Just follow the traces all the way down here. And this ET chip set is modeled in here somewhere as well.

**Dave Jones:** And this has got its own memory over here, Cynthia or Cynthia Junior does anyway. It looks like it's for Cynthia actually. If you follow some of the traces, they're headed up there.

**Dave Jones:** And that memory down in here looks super quick, 45 ns MB81C 78A. Turns out they're 8K bytes, 64K bits SRAMs, 45 ns. So, they're really screaming along, taking the video very very seriously.

**Dave Jones:** There. So, that's some sort of, you know, that could be like the like the frame buffer or something like that perhaps. Aha, I finally found some info on these custom chips.

**Dave Jones:** Well, not any detailed information, but just what each one does. So, let's see how close I was. The ET chipset ET home is the memory controller. The Cynthia and Cynthia Junior up here, they're a combo as you would expect.

**Dave Jones:** That's the sprite controller actually. So, and this memory around here, I'm still guessing, but I would say that's probably might be the background plane memory perhaps because this thing can do up to 512 by 512 background.

**Dave Jones:** And as in background graphics and things like that. So, by the way, the video this thing quite advanced for its day. Could go up to 1024 by 1024 resolution in 16 colors or 512 by 512 in 65,000 colors.

**Dave Jones:** As I said with that background stuff, it's got its own sprite controller and everything else. So, really advanced graphics for the day. Actually, this memory here is most likely to be the sprite memory cuz this thing does have 32K of sprite memory.

**Dave Jones:** So, that adds up. That's what they memory chips must be doing. Just dedicated to the sprites. That's pretty impressive. Then over on the video board here, yes, the V sub as I suspected is the video control main video controller chip.

**Dave Jones:** Venus 1 and Venus 2 here, these are the CRT controller chips. Doesn't give any more info apart from that. And the reserve chip down here, yeah, I think I was I think I guessed that one was some sort of you know bank select and that's exactly what it is.

**Dave Jones:** It's a video data selector chip. Some of these things are like, you know, quite obvious when you look at them. I mean, this being a video data selector chip, just its physical location, all this memory here, right?

**Dave Jones:** We've got, you know, large banks of memory and generally, you know, you might have to in a video situation, you might have to swap those in and out. So, it's no surprises for guessing that this physical location sort of like it's not wedge between here and here, but it's sort of, you know, on the way kind of thing between the video controller and the memory, then yeah, okay, it's a

**Dave Jones:** video data selector. Not hard to guess. And most of the custom chips on here actually changed after this very first model. So, all the following models used different chip sets.

**Dave Jones:** They consolidated Cynthia up here. They changed another one to the Ohm chip set, very apt for the EE Vblog, and there's the Messiah chip set, and yeah, all sorts of jazz.

**Dave Jones:** So, yeah, they just completely revamped it for the following models. Now, as for the video memory here, I couldn't find any data on this MB81461. 461's unusual cuz usually they have the size of the thing.

**Dave Jones:** They're like, you know, 256, 512. It's going to be, you know, a power of two multiple. But, I do know that this thing has 512K text video memory and 512K graphics VRAM.

**Dave Jones:** So, that means this bank of 16 here must be 512K, and this one must be 512K. So, that works out to 36 Sorry, 32 K bits per device. So, yeah, I'm not sure of the part number there, but they are split into two banks, and that's very interesting.

**Dave Jones:** Separate text graphics memory and separate video graphics memory. That's why they need this reserve controller chip here for the video bank switching. These things are maddeningly hard to get off.

**Dave Jones:** To try and get these clips out of here, and then slide it all back, and then it's got retaining clips in here, and I don't little bit of plastic snapped off at the back there.

**Dave Jones:** It was Man. Anyway, got it. We're in like Flynn. First thing I'm doing, going outside, dusting this thing down cuz cuz all accumulated down the bottom. And here's inside the disk drive and power supply part of it.

**Dave Jones:** This is our power supply module from very well shielded, no problems at all. Two 5 and 1/4 in floppies. These are the soft eject type, so they have soft eject buttons on the front.

**Dave Jones:** Very nice, you know, not the old fashioned lever, you know, turn the lever and then get your fingers and pull it out. They actually had a motor to eject the disk.

**Dave Jones:** Very nice separate board up the top here for your hard drive interface and your floppy drive interface. And a relatively small fan on the top of the thing here.

**Dave Jones:** And then we've got our mains input and output over here with our main switch. Bit of insulating card here, but yeah, it's all a bit It's all a bit messy, but it does the job, I guess.

**Dave Jones:** Now, I don't know if the floppy is actually manufactured by Sharp or not, but it certainly does have a Sharp sticker on it. Now, down here on the baseboard, this is the Silian System I/O controller chip.

**Dave Jones:** That's the code name. Now, we get to the sound part of this thing. This OKI part here, this M6258V, that's a 4-bit ADPCM sound chip, but this is where all the magic happens.

**Dave Jones:** This is a Yamaha YM2151. It's so famous, it's got its own Wikipedia page. Fantastic. This was used in the early DX series Yamaha keyboards. A very advanced FM synthesis chip for its day.

**Dave Jones:** And it's an 8-channel FM synthesis chip with a four different operators. And very powerful thing. It was used in a lot of the arcade games of the era, like as in the big proper arcade game machines from, you know, Konami, Capcom, Namco, and Sega, and Atari, and all those ones all use this sound chip.

**Dave Jones:** That's why this thing, not only can it do pixel perfect graphic arcade emulations, it can also do It's got the same sound chip used in a lot of those game machines.

**Dave Jones:** But this uh FM synthesis chip just doesn't work on its own cuz it just generates the data. You need a DAC to convert that to audio, and so that's paired up with another Yamaha.

**Dave Jones:** You can just see it tucked in there. That's the uh YM 3012 DAC. And given the otherwise excellent systems engineering we've seen in this thing, especially for it like a first um unit, like a you know, a first release one, um it's got this big green bodge wire going all the way over there.

**Dave Jones:** Not sure what that one's doing. Oops. And also down on this baseboard, which we may not get to the rest of it. So I am running out of time for this teardown and to get into the other side of this, um it could be like to get the whole board out for photography and things like that could be a bit of a pain in the ass.

**Dave Jones:** But anyway, um uh down on the bottom board there, we're going to have a floppy controller. That's an NEC uh 72065. Apparently, that'll be on the other side, and then there'll be the um well, it's not a SCSI controller because this predates a SCSI controller.

**Dave Jones:** This thing uses what's called an SASI uh controller. It's a Shugart That stands for Shugart Associates System Interface, and it was a forerunner to uh SCSI, but um updated models to this did include a proper SCSI uh controller.

**Dave Jones:** I believe SASI was, you know, fairly pin compatible with it, but technically different. And this Sharp LH8538A here, that's a serial communications controller handling all sorts of miscellaneous stuff.

**Dave Jones:** Now, I would love to try and get this power supply out for you, and I've I've tried, but there's something like holding it in in the center, by the looks of it, and it's getting really, really annoying, and I'm not sure I'm going to be able to get the thing out without sort of maybe like taking the whole damn thing apart.

**Dave Jones:** So, um which is a bit of a shame because um Alex said that these things were notoriously bad, these power supplies, and they used dodgy caps, and you had to replace them all and and everything else like all sorts of dodgy parts.

**Dave Jones:** So, yeah, I would have liked to have had a peek in there, but I can't get this off without getting this out to get the screws under here and oh, it's all just oh, it's all too much.

**Dave Jones:** Sorry, I'm running out of time. It's already Wednesday. So, sorry. Yep, I'm going to have to call it quits there. I I don't have the time to take this down further.

**Dave Jones:** I'm going to have to stop filming, go edit, and upload this sucker. But, thank you very much Alex for sending in this X68000 from Japan. Very interesting. I'd never heard of it and by a real state-of-the-art machine.

**Dave Jones:** Unbelievable. You got to remember this was released around about the same time as the Amiga and the Atari ST and it pretty much spec-wise it and capability-wise it just, you know, blows those ones away.

**Dave Jones:** Everyone raves about the Amiga and everything else, but this thing is, you know, for its day it was absolutely incredible. And apparently highly sought after by the gaming fanboys.

**Dave Jones:** Who knew? Because of pixel-perfect graphics, the sound, everything else of the arcade emulated games on this thing. So, I I don't know if this one works at all. I don't think Alex mentioned it, but yeah, you might have to clean up the power supply.

**Dave Jones:** It looks in pretty good nick. I see no reason why this thing shouldn't work or shouldn't be fairly easy to get going, although the floppy drives, I don't know about the floppy drives.

**Dave Jones:** They could be the big thing. Apparently all the games ran drives really you didn't essentially need the hard drive in the thing. And this is actually a very well engineered machine.

**Dave Jones:** I'm actually very impressed. Interesting dual tower format with the carry handle and and everything else. I don't know whether or not they originally designed it that way. You know, they came up with the you know, some artists came up with the you know, marketing people or whatever came up with the concept of the dual towers like this and then the engineers were given the task to uh fit it in or

**Dave Jones:** whether or not it just naturally evolved into this sort of case. Um I don't know, but very interesting bit of retro computer history right here. The Sharp X68000 only sold in Japan.

**Dave Jones:** If they sold this outside of Japan, might have been incredibly popular. Who knows? So, thank you very much, Alex. That was most generous of you to send this all the way from Japan.

**Dave Jones:** And if you like the video, please give it a big thumbs up on YouTube cuz that helps a lot. If you want to discuss it, leave YouTube comments and all that sort of jazz or you can jump on over to the EVblog forum.

**Dave Jones:** That's where everyone hangs out and chats about the videos and everything else. Links down below. And also, I've got high res teardown photos of this thing on evblog.com. Link again down below.

**Dave Jones:** Catch you next time.
