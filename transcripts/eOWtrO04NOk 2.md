---
video_id: eOWtrO04NOk
title: EEVblog #1153 - 1970's Programmable Calculator Teardown
url: https://www.youtube.com/watch?v=eOWtrO04NOk
source: youtube-asr
timestamps: {"0": 1, "1": 31, "2": 62, "3": 87, "4": 109, "5": 135, "6": 153, "7": 177, "8": 210, "9": 244, "10": 277, "11": 298, "12": 306, "13": 320, "14": 342, "15": 361, "16": 377, "17": 388, "18": 419, "19": 439, "20": 456, "21": 480, "22": 505, "23": 543, "24": 571, "25": 600, "26": 630, "27": 657, "28": 696, "29": 732, "30": 755, "31": 778, "32": 816, "33": 847, "34": 868, "35": 882, "36": 904, "37": 929, "38": 944, "39": 962, "40": 995, "41": 1014, "42": 1026, "43": 1044, "44": 1062, "45": 1082, "46": 1108, "47": 1127, "48": 1142, "49": 1172, "50": 1207, "51": 1240, "52": 1255, "53": 1272, "54": 1307, "55": 1337, "56": 1356, "57": 1385, "58": 1416, "59": 1432, "60": 1465, "61": 1497, "62": 1532, "63": 1547, "64": 1578, "65": 1607, "66": 1625, "67": 1651, "68": 1673, "69": 1703, "70": 1721, "71": 1750, "72": 1787, "73": 1805, "74": 1823, "75": 1852, "76": 1884, "77": 1898, "78": 1908, "79": 1927, "80": 1948, "81": 1986, "82": 2005, "83": 2025, "84": 2060, "85": 2084, "86": 2114, "87": 2151, "88": 2170, "89": 2184, "90": 2215, "91": 2239, "92": 2269, "93": 2282, "94": 2300}
---

**Dave Jones:** All right, got another teardown for you and you know we love vintage computers / calculators here on the EEVblog. Got a Bobby Dez love. Look at this thing. It's the Canon Canola SX-100 straight out of the early 1970s. I don't know a huge amount about this. It's a bit hard to find information. Don't have a manual for it. I do have a manual and a service manual for the later SX-300 which dates from 19 75.

**Dave Jones:** So, I assume the SX-100 is the model like either one or two generations previous to that, but I did get a date of this of 1976. I'm not sure how accurate that date is because for example, the HP famous HP-35, the first pocket calculator came out in 1972 and then 1974 had the HP-65 programmable pocket calculator and this thing which weighs an absolute ton. What is it? 10 kilos or something and is an absolute beast.

**Dave Jones:** Sure, it's got a printer and everything else, but this is actually a programmable calculator, not really a computer as such. I believe it's only got like a few dozen memory registers and stuff like that, but it is fully programmable and you can execute programs and stuff on it. So, programmable calculator, thermal printer, everything else. So, I thought we'd check it out. This could make for an interesting teardown.

**Dave Jones:** Fantastic. Still in pretty good nick by the looks of it and got a full roll of paper, too. Beauty. So, if you used one of these things, let us know down in the comments or over on the EEVblog forum because well, this is a quite an unusual beast for like the early 70s. As I said, those pocket calculators, you know, started coming around from 1972 onwards.

**Dave Jones:** So, you got to question the value of something like this in like 74. The as I said, the 1975 I believe is the date for the SX300, which is basically looks identical to this. It might have some extra performance or features or something like that, but it looks near identical to the SX100 that we've got here. So, yeah, this huge big desktop beast of a thing which weighs a ton.

**Dave Jones:** And, you know, I don't know how it would compare with the HP-65, for example, from 1974, but that could fit your pocket. This thing I don't know. have time. So, was this thing just too late to the party? Did it miss the pocket revolution? I don't know.

**Dave Jones:** When was Canon's first pocket calculator? Did they get into pocket calculators? I think they did eventually. But, yeah, did this one miss the boat? I don't know. Anyway, let's tear it down see what makes this thing tick. So, check it out. It is actually pretty sexy-looking. I mean, you know, the lay I actually do like the keyboard layout, which is quite nice.

**Dave Jones:** You got your trig and scientific functions over here. You've got your regular keypad, exponents up here, change sign, nice big zero key. I don't know what the start and presumably start program or whatever. Got some additional functions over here, your parentheses. I've got a dedicated inverse key. Fantastic. And then it looks like you got some of the programming keys over here. And then a whole bunch of interesting looking stuff at the top and some sort of recorder. I don't know what that is.

**Dave Jones:** We've got, you know, debug and programs and step backs, insert, delete programs. Then we've got our degrees, radians, gradients, all that sort of stuff. And then we've got how it rounds. Does it always round down? Does it always round up? Or does it do the five-four thing? Fantastic. And then what looks like our fixed number of decimal points. So, F would be floating point, I'm going to assume. And then no decimal points, one through to six, something like that. Anyway, does have a rather interesting layout. No, I

**Dave Jones:** don't mind it at all. I think it's pretty nice. And on the back of this beast, we've got a weird ass mains connector. Don't know what that one is off hand. We've got two unfortunately we've lost the back in plate on this thing. And two things which there doesn't seem to be connectors on the back there. So, I'm not sure what they're actually for, maybe some sort of expansion thing, but there is no mating internal connectors by the looks of it. And what looks like a 48 column to 24 column selector

**Dave Jones:** here for the paper. Presumably we've got a full roll of paper in there and beauty. All the best stuff's made in Japan. And this is the fancy pantsy non-interference model. Anyway, let's crack this thing open. I'm going to assume that the feet aren't part of the thing and these screws around here will hold on the top part.

**Dave Jones:** And the top part should just lift straight off. That'd be very nice. We should get a good look at the innards.

**Dave Jones:** All right, let's try and lift it. Of course, I expect all this, you know, early '70s. Who knows when they started designing this this thing. By the way, if you've got an accurate date when this thing was released, please let us know in the comments.

**Dave Jones:** Anyway, I'd expect all like all dip construction. It's probably will it use a an actual processor or will it use discrete logic processor and stuff like that. I don't know. It's big and heavy enough to sort of have enough chips to have its own, you know, to roll its own processor. So, hello.

**Dave Jones:** Is that Yeah. Oh, there's a few wiring harnesses. Oh, oh, they've got a decent length on that. Look at that. There you go. Yep. No, looks like we've got some sort of uh processor. That's certainly not certainly not all discrete.

**Dave Jones:** That's for sure. Uh, I've got some uh Look at all the hand wiring. Uh, look at this. We've got some diode logic down there by the looks of it. And uh Jeez, that's all pretty how you doing, isn't it?

**Dave Jones:** That's terrible, Muriel. But, you know, not uncommon for the era, though. But, you know, they've sort of like cable tied stuff.

**Dave Jones:** Lots of bodges. Wow, look at this. Wow, none of this uh 0.1 in header and ribbon cable rubbish. Nope, card edge, and each one of them individually um heat shrunk and soldered. I do like how they've uh uh formed the metalwork up here to uh keep the connector in. Uh, that's rather nice. So, it can't fall out. That's pretty good. But, it kind of all sort of uh fell apart up here when they went, "Oh, bugger that connector rubbish. We can just uh hand solder those puppies

**Dave Jones:** on. Thank you very much." Uh, check out these poor old here over on one side. They're like falling over, staggering off to one side. No one took pride in keeping those straight when they soldered them in, that's for sure. But, they've got a diode bodge on here and resistor. Just sort of stand it up.

**Dave Jones:** Those diodes, I don't know if they're a bodge or they're You know, there's no There's no traces on the top. So, have they like drilled through the board and like added those diodes? Hmm, have we got a like a diode uh diode gate there or something?

**Dave Jones:** Anyway, this cap seam here seems to be bodged on. And HD3541. Going to have to go Google that one. Well, even my Google foo is off for uh I can't find any info on that. If I can, I'll link it in. But anyway, we've got HD 3541, which looks like some sort of processor, then the HD 3542, then the HD 3543.

**Dave Jones:** So, obviously these are SRAMs here. Uh 3542, I'm not sure what that'll be doing. It's probably not a ROM. be a masked ROM. I don't know. Have to take the rest of it open, but uh anyway, we've obviously got some sort of uh Hitachi chipset. Okay, one of the oldest ones I can find is uh 39th week 74.

**Dave Jones:** So, this is getting close to being uh you know, a 1975 model. So, as I said, like it's you know, how competitive was this in small batches up there? Love it. How can be ground strap going off somewhere, buggering off to Is that going off to the printer or whatever? Oh. Oh. Flat flex ribbon, fancy pantsy. Um like yeah, how competitive was this thing in like 1975? Yeah, sure it's got a printer and everything else, and it's got you know, it's got some programmable functionality, and it may you know, a

**Dave Jones:** lot of people will prefer a desk model over a pocket one and stuff like that, but yeah, I don't know. It would have some good advantages. So, you know, maybe for uh you know, scientific engineering teams, something like that, who wanted a paper trail and stuff like that, cuz that you know, it's often that's vital so that you can uh that that's why accountants A lot of accountants will still use the old you know, the paper tape thing as they add their you know, if you're bringing

**Dave Jones:** bringing your shoebox worth of receipts, and then they sit there and add them all up, then they've They've like a paper tra- paper tape trail of uh you know the actual stuff that they ended in so they can go back and check it. So it would have been valuable from that point of view but Jesus a general purpose scientific you know calculator on your desk you wouldn't bother wasting your desk space. So how quickly did something like this go obsolete I wonder. So generally I'm quite surprised by this this has like

**Dave Jones:** less stuff in it than I was expecting it looks like a kind of reminds me of like a you know a 1970s vintage PC something like that you know or like an early 80s vintage PC with the just you know like the looks like processor the RAM and everything else a couple of you know discrete jelly bean glue logic and all the other stuff but uh yeah I was just like I don't know I expect like the big weight of it maybe I was hoping that there were you know lots

**Dave Jones:** of big cards in there with lots of like a discrete processor and you know a ton of stuff and nope looks like it's just a micron something else. Granted I haven't gotten all the way under there but I don't think this card extends too far back under here so all the weight comes from like the three layers of metal work it's got here you know it's all big thick heavy stuff so yeah that's why it weighs a ton. If we lift off the printer and storage mechanism we

**Dave Jones:** get this board under here it's all just you know 74 series logic nothing nothing really much doing there. I love though the green jumper wires look joining these is that power? Yeah that is no that's ground. It's going to be joining joining the grounds like this like they couldn't get that on the board like they couldn't get that on the layout. Doesn't make sense. Anyway I believe that this is the based on where the wiring is buggering off to this is the controller for this mysterious tape drive storage mechanism

**Dave Jones:** thingy. So, this is like really interesting. It's not a tape drive and it's not a cartridge system. This is a head. Okay, you can tell because it's got these coaxes going off here. So, this is like a read-write head and it's like like it can't like there's no loop tape or anything like that to do it. So, I think it's just like like a magnetic stripe card kind of thing which wasn't that uncommon back in the day. HP used some like magnetic swipe cards for storage. I

**Dave Jones:** mean, it doesn't store a lot. It only needs to store like, you know, 100 like I don't know dozens of bytes maybe a few hundred bytes or something like that. So, you can easily store it on like a a strip like a little credit card kind of thing and that's what it looks like it is. And yep, sure enough you can see that down in there. Look, there's a roll that roll shouldn't have touched it. That that roll is gone. I was going to say yep.

**Dave Jones:** That almost looks like a cork kind of That is weird. Anyway, that was a roller. Oops. And then we've got a micro switch there that this one's actually actually a detection for the bottom. So, we've got two slots here. Focus you bastard. All right. So, these rollers down here push against the magnetic head up here.

**Dave Jones:** It looks like this like I don't know. It's just disintegrating. Sorry, I'm not putting any force on that. It would So, I didn't destroy it. It it just had stood no chance of working at all. Anyway, so we've got the gear chain for all that to actually drive that shaft in there that drives that. Not sure what's doing down the bottom though. Got a micro switch. There doesn't seem to be a Oh, okay. No, I know what happens. Oh, yes. It's obvious. People are probably screaming at me. It's a paper thing. You

**Dave Jones:** put it in the top, it pulls it through, and shoots it out the bottom, or vice versa. Maybe it Yeah. By the way that It can't It can't go in here and come out here cuz it'll get caught on that lever in there, that micro switch lever. So, obviously, you have to shove it in the bottom here, and it sucks it through. It gets caught on this plastic roller on there, pulls it through, and then over the head like that. Yeah, that's the way it goes. So, some sort of uh you know,

**Dave Jones:** paper magnetic strip card storage you know, program storage thing. Probably held, you know, 100 couple hundred bytes tops. Uh thing of beauty is a joy forever. Look at that. That is beautiful. Look at all those end-on resistors with the uh white insulation over them. That's fantastic.

**Dave Jones:** Then we've got a bunch of uh uh op amps there by the looks of it. And this is all the um uh the head circuitry. So, this is all the head uh driver and the head uh receiver for the magnetic drive there.

**Dave Jones:** So, yep, that's all in its own separate shielded can. Whereas all the bottom board down here is just all digital logic and uh and there's not much smarts in that at all, but that's gorgeous. I love that. And I do believe take these two screws out here, this board is going to slide out from here. Yep.

**Dave Jones:** Yep. Look at that. Ah. Someone was thinking. Ooh. I don't know. I was going to say, is that a delay line? Look, remarkably like a delay line, but ah It will come out. Ah. Well, this has seen better days. Look at the I'm not sure I'm not sure if you can see that. It's sort of like Yeah, you can see the shine on that.

**Dave Jones:** It's Is it some almost looks like it's conformally coated, but not all the way. Seems like stop up like it's really patchy. It's like stops here. It's just If it is conformal coat, look at patches in there. It's the worst I've ever seen.

**Dave Jones:** Or is it some sort of I don't think it's like any sort of fluor contamination or something like that. I don't know. Is it like just like they did didn't clean the board. It's got some old school flux cleaner residue on there or something like that.

**Dave Jones:** I don't know. Phew. And this layout's all hand taped, too. None of that CAD rubbish. So, as you can see, it's just a 74 logic. And once again, none of the 74 LS or any sort of 74 HC rubbish or any HC wasn't invented then. Um yeah, just this good old 74 series logic. So, yep. And bodges on there. Like, I don't understand that ground. Like, why can't that Look, that's connected to there.

**Dave Jones:** Why can't Like, did they actually leave it off here? Like, look, there's room for that trace to go around there and around to there. Did they Oh, no, maybe not. Well, they could have then dropped it. Yeah, could have come through there like that under that cap. So, I'd like What?

**Dave Jones:** Or that maybe they just had an issue with uh you know, via current. Um something like that, you know, they would just want to lower impedance. Anyway, you can see that there's not not that many uh bypass caps on there.

**Dave Jones:** They've got little jumper links, MC, whatever that means. And a couple of uh you know, steering diodes and whatnot. But uh yeah, not too many bypass caps. Don't need any of that rubbish. I love how the uh the silk screens under the chip. That's really handy, isn't it?

**Dave Jones:** And the backside of here is mostly, you know, 74 logic and that sort of jazz. It Oh, look. It's another another slot there. Don't know what plugs into that one cuz the other board was plugs into the top here.

**Dave Jones:** The the tape drive things so card reader drive. So, there's another another socket down there, which is interesting, but once again, oh, yeah, what's this thing? I see 6270. It's upside down, so all the electrons are going to fall out. Is that You know, there's a whole bunch of diodes there.

**Dave Jones:** Do they go into it? I'm not entirely got no idea. Anyway, this is interesting. Look at these Hitachi chips here. We got HN35401, 402, 403, 404. And you'd expect it to go 405, but it doesn't here. It goes 405 is actually down here, 406, and then 409.

**Dave Jones:** So, where's like 407 408? Anyway, lots of blue bodge wires running everywhere, and we've got a little Is that a little Yeah, that's it. Yeah, little transistor in there, and they put a little That looks almost like conductive foam on the back of that.

**Dave Jones:** What on earth? Little trimmer there. Don't know what they're Don't know what they're doing there, but the the main crystal down here, I don't know what What frequency is that? Does it even have it written on there? Weird.

**Dave Jones:** And one thing you don't see here is your traditional EPROM. You know, where's Wally? Where's the ROM? Obviously, this thing's the uh processor. These are all the same part number, so this has got to be RAM, but there's only five like there's five of them. So, that's like an odd ball number. This one here could be some sort of memory controller or something, but like I don't but why you'd need it for SRAM, I don't know. Anyway, um and it looks like these are probably the ROMs. Once

**Dave Jones:** again, 2 4 6 7. That doesn't make sense really, and it's not that one cuz that's not number along with them. So, those in sequential number order kind of makes sense from a uh like a ROM uh point of view. So, they'd they'd be like mask uh ROMs. All right, check this out. We actually have the service menu with full schematics for the SX-300 and the only real difference I can find between the SX-300 and the SX-100, maybe apart from, you know, like a memory difference or something like that, is

**Dave Jones:** that the SX-300 actually uses a magnetic tape system as opposed to the uh magnetic card system. And that's about it, but everything else seems identical. Check it out. We have a ton of stuff here, and here's a uh block diagram. We got the optional memory box they call it. I guess it's a memory uh card. There's the uh control chip, which is that main one that I thought was the processor. It's not actually a processor as as such because this is not a microprocessor based system. This is

**Dave Jones:** like a multi-chip processor system, which is different. So, it's got a control and so in effect they're making up a microprocessor with multiple chips. So, we've got a control chip, a data chip, and an SR arithmetic uh chip here.

**Dave Jones:** And they're those three main chips that we saw, and I'll point out in a minute. We've got six different ROMs, and we'll go into the uh different ROMs. They're not all program ROMs. Um and then we have a printer controller which has its own ROM. It's got a character generator ROM.

**Dave Jones:** Uh, well, we've got a a display controller and gates and various other stuff. So, there you go. Um, mag card amplifier, all that sort of stuff. I love the little wiring diagrams. Here's the keyboard circuit. So, it's pretty basic matrix arrangement. Now, I find this part really interesting. This is the auto clear and clear. You remember those two buttons on the top. Um, they're actually like they've I think they're wired outside the matrix and into this dedicated circuitry which literally like hard resets stuff within the processor.

**Dave Jones:** So, it's a it's very serious business. It's not like the processor, it's not like the instructions in the processor read the matrix keyboard and oh, you've pressed the clear key and it just clears it in memory. It actually it resets the processor um, to a to a like a known state and stuff like that. They've got diagrams and things like that which is really cool. Uh, crystal oscillator 3.57 MHz. Whether or not it's slower in the SX-100, I don't know. And here it is. Here's the HD3541.

**Dave Jones:** That's that control chip. And once again, here is that uh, HN35409. Those six ROMs. Um, seven was it down the uh, side there. This is ROM number five. So, these ones uh, the uh, TWE and TD. These are like uh, two keyboard.

**Dave Jones:** There you go. So, that'd be uh, so this is a keyboard mapping ROM. So, it doesn't actually contain processor instructions or anything like that. It's a like it's a mapping ROM. They do some old school mapping. Maybe I'm going to show you an old project I did. I might I'll make a mental note. I'll do a video showing you a um, an old school um, sort of like um, state machine compiler that I uh, wrote back in the day using ROMs to execute instructions and programs. I

**Dave Jones:** might see if I can, uh, dig that one out of the archives. Uh, remind me, pester me if I if I don't get around to it. And then once again, there's mention of the, uh, 3542. That's the data chip, so that was the one next to it. And it looks like the, uh, 3541, so we're what we thought was the processor, but actually called the control chip, it actually handles the keyboard, but it's not a keyboard controller. It actually is a part of the microprocessor uh, system, multi-chip processor system.

**Dave Jones:** Look at all the stuff they got in here. This is amazing. Wow, nobody does documentation like this anymore. It's great. So, there are various flags, you know, processor flags and stuff like that. So, you know, it's it's implementing all this stuff which you'd expect inside a microprocessor.

**Dave Jones:** It's doing this with these dedicated, uh, well, with these, uh, like separate chips, joining them together to form microprocessors. So, there's the controller yet again, and it's got the memory box and interface. You see how that controller not only ties into the keyboard system, it ties into the memory box, memory and interface and the auto clear and instrument converter, inst converter and ROM and all sorts of stuff and data transfer. So, there's a separate that separate data chip. Um, it's not actually a So, it's just part

**Dave Jones:** of the processor. It's it's I don't know. You know, processor internal what actual architecture, uh, this is, how many bits it is, all that sort of stuff, um, and what sort of, uh, architecture it'd be closest to. Is it Is it like emulating old, you know, 8080 or 8008 or something like that? I, you know, I don't know. Or is it its own thing? Who knows? And here's our ROM, the HM35401, 02, 03 and 04. So, four of those ROMs are actually dedicated to the printer

**Dave Jones:** unit. So, one is the character generator here and looks like the others are just like generate the uh uh the the data to control the printer and stuff like that. So, once again, these aren't instruction-based ROMs. They're like hard-coded like almost, you know, you could replicate these with PLDs and FPGAs and, you know, stuff like that. So, it's using the ROM as a lookup table to generate you know, waveforms and in- like not instructions, that's not the correct term. Generate uh the required waveforms to drive the printer. Then

**Dave Jones:** you've got your other four ROMs here. Two of them are display ROMs. One is a TW That was the keyboard, wasn't it? TWE and timing type type thing and this was another one. And they're Some of them are open drain, are they? Anyway, ooh.

**Dave Jones:** What's a NAND gate? Here's a display block diagram, cathode driver. And once again, the these ROMs down here are controlling the actual segments going into the seven the multi-channel seven-segment display. So, they in effect, they're like data to seven-segment uh decoder ROMs. So, they're actually doing those in ROMs, which is really quite You know, it's not a bad way to do it cuz mask ROMs, not going to say that were cheap, but they were, you know, simple and effective back then for for doing stuff like this.

**Dave Jones:** So, you didn't have to generate uh so, you in effect, they're using these mask ROMs as custom logic. Then we might have some sort of uh block diagram here. There you go. Mentally flip between those and uh you can see and there's the uh block diagram of the card driver. In this case, that would be the uh read and write uh that would be the tape controller and stuff like that. So, this would be different on the um uh SX-100, of course, cuz there's a card reader

**Dave Jones:** instead of a tape. Maybe it uses like the same system except a physical tape they can just store more maybe that makes sense that they'd probably use the same protocol. So maybe all the you know, a lot of the electronics are the same maybe the tape and everything else and it's just like motor drive and stuff like that that differs between the two.

**Dave Jones:** And then we've got our power supply circuit and there's our standard you know, there's our Darlington pass configuration like that and we've got a zener in there to plus 5 minus 7 and a half plus 12 plus 9 minus 12 minus 6 minus 4 Jeez, needs a lot. Anyway, how cool is that? I love the diagram of the capacitor and the leads going off.

**Dave Jones:** That's great. Nobody makes manuals like this and they give you the pin outs. Little data sheet pin outs and stuff. Absolutely fantastic. Hats off. Someone went to a lot of more maybe it's one person put this manual together and then they've got the uh the foil United Like yeah, I'm going to follow that.

**Dave Jones:** Look at that. It's very arty, isn't it? That's terrific. Wow, that's great and then exploded views and that looks like a parts list. That's That's incredible. And for all you power supply aficionados, there you go. Um don't you love the the tubing? That's not even heat shrink. I don't think that's just tubing. We've got our capacitors mounted down to the chassis quite old school.

**Dave Jones:** It's a bit how you're doing over here with the uh What is that? The the series pass transistor for the linear regulator? Um they've got heat shrink on there but you know, they're putting it down there using it as a heat sink and well, there's not much else on there. Bunch of caps.

**Dave Jones:** That's a Is that a big ass inductor? Or is it? What the What on Earth? No, it's a bridge rectifier. That's a big-ass bridge rectifier. Look at that. Wow. AC's on the other side, four-leg bridge rectifier with a hole in the middle, so you can like mount it on a chassis mount and an arrow telling you where to shove it.

**Dave Jones:** Oh, Nippon Chemicon, fantastic. You think this is still going to work? Yeah, I think so. Oh, it gets a bit more interesting on the back. Check it out. There's a whole bunch of other pass transistors as well with some little smaller in front just to drive the base of those suckers. So, are they little Darlington configuration, perhaps? So, a fuse up here. Love our little connectors like that. Look at that beau- Look at that soldering onto the wires there, beautiful, wrapped around. A thing of beauty. Look at that.

**Dave Jones:** Fantastic. And our transformer over here made in Japan. All the best stuff's made in Japan. That's certainly a hunk of iron. Contributes to the weight, obviously. And then we've got our motherboard down in there, which is like Please excuse the crudity of the shot here.

**Dave Jones:** All sort of, you know, like a phenolic base type thing. It's not uh not exactly a first-class board, that backplane there. But it doesn't have to do much. So, there you have it. There's an aerial view of our Canon programmable calculator.

**Dave Jones:** Isn't it fantastic? Early or, in this case, mid uh '70s, but this would have been designed in the uh very early '70s, I'm sure. And uh it's just got mysterious Hitachi processor in there, but coming in for landing on our camera there. No, I don't have any of that stabilizer rubbish turned on. Anyway, look at that. Oh, if you want to see, everything's made in Japan. There you go, there's your motor for all your motor fanboys.

**Dave Jones:** There's a closer look at the head. It's all gunked up. It's all potted. Couple of coax's coming off there. Not much else doing. Here's another look at the keyboard. Got our diode steering, of course, for our and all be a matrix and uh and we've got there's some physical switches up there. They got cutouts in the board for those. There's our rotary selector for our uh decimal point indication switch for our degrees, radians, gradients, and all that sort of stuff.

**Dave Jones:** And then our display up there, and uh the wiring for that, that's all pretty how you doing. Unbelievable. All right, let's see if this thing works. Let's power it up. Uh 240, I've got some alligator clips on the back.

**Dave Jones:** She'll be right. No worries. Neutral and phase. 240 V, 50 Hz. Here we go.

**Dave Jones:** Whoa! Hey! Winner! Check it out. You can hardly see it. Geez, that's a tiny little seven segment LED display. Look at that. But, it looks like ha!

**Dave Jones:** It works! We going to win a chicken dinner. And check it out, it still prints. What? Let's do a paper. Do a paper. Paper feed. Print. Whoa! Check that out. 13 decimal places. That's pretty impressive. Whoop. Yep. Yep.

**Dave Jones:** I've got printer off. Thank you. So, that's pretty impressive. We've got 16-digit mantissa, three-digit exponent. Wow! this thing was kicking some serious ass. All right, so let's clear that. Let's do the old up Woah, ginger. Okay, bit sticky. Let's do the old 69 factorial, shall we? We've got a dedicated factorial key, which is, you know, it's a bit how you doing. Oh, it printed the Oh, you see how it sequentially came up with that. Now, our printer is going haywire. What?

**Dave Jones:** Uh-oh. Uh, it's one sick puppy. Okay, I repowered it. I think it it got past the out of the jam over to the end stop there, so maybe it'll maybe it'll do something now, so let's try our 69 factorial again, shall we?

**Dave Jones:** There we go. Ha, that's pretty quick. All right, so let's try the famous calculator forensics. So, what I'm going to do is nine, sign, cosine, tangent, arc tangent, arc cosine, arc sign. There we go. There's our calculator forensics result.

**Dave Jones:** For those playing along at home, not not bang on nine, 8.99999 86441800, and I'm sure that doesn't match and well, it'd be interesting. I'll look up the database of that and see if it matches, but of course, it's not going to um probably who knows? It might use the same algorithm as, you know, some other calculator chip set or something like that, but this one Anyway, um and that's full floating point mode, of course. What if we haven't actually tried this? What if we change that on the fly? Not doesn't do

**Dave Jones:** anything, but if we did that on the fly, let's say we had six decimal places. Try it again. Nine, sign, cosine, tangent, arc tangent, arc cosine, arc sine. There we go. And whoa, some of that's supposed to be six. Okay, so that doesn't work. All right, I know you want to see me run a program, so let's do it.

**Dave Jones:** It's actually not too bad at all. Um OPE is operation mode. So, you know, this is like 1 + 2 = There we go. And it's going to print it out. 1 + 2. There we go. It actually prints it out. But if you want to record a program, you put it into learn mode like this. Okay, it will clear all like that. Now, this is uh you can actually store multiple programs on here. So, SPNN key here, it means uh store program NN.

**Dave Jones:** So, you got to give it a hex number. So, we'll store program and it says unfinished here. So, we actually have to give it tell it 00. Okay? So, we're now inside uh the uh So, we're storing a program. Now, we can do our sequence. So, if we go 1 + 2 + 3 = Print it all that uh stuff out. And then when we just go end program like this, 00 and we're good to go. So, we've stored our program now and we can go back to

**Dave Jones:** operation mode like this. And we just press start and it'll run our program. It just executed our program and gave us Well, it gave us our answer here. Fantastic. So, it's given that and it's displayed Uh you can't see it. It's not very good.

**Dave Jones:** The printer The printer's not great, but it has actually printed out that and it was printing out our program as we were going cuz we had the uh you can turn the uh printer key off here if you don't want it to uh do that. But there you go.

**Dave Jones:** That's pretty neat, huh? Let's try program print. Haven't read the manual on that, but I assume if we press that, yeah, 1 + 2 + 3 + There it is. That's our program that we entered in. Fantastic. And you can store multiple programs um and you can uh like go into debug mode. You can uh check mode which allows you to go in and uh edit and all that um sort of jazz and I assume load and record. So, if we shoved our card in there, we could uh record our program to

**Dave Jones:** magnetic card, I guess. So, that's pretty groovy, isn't it? I actually like that. It's actually, you know, it's fairly well thought out. It's fairly uh simplistic once you know. I mean, you can't like obviously just walking up to it and trying to use it, but once you, you know, spend just a few minutes reading the manual and you go, "Yeah, that's, you know, that's pretty obvious." Of course, you can go in there, you know, if you want to edit your thing, you can go to uh

**Dave Jones:** particular lines and do edits and inserts and, you know, all sorts of stuff. So, you can modify your uh program. And of course, you can do uh go-tos, go to various steps. Looks like you can set uh you know, flags and things like that. Uh column prints and line feeds. It's obviously um fix, you know, does that fix the number of your decimal places or whatever? But anyway, you can do various uh you know, programmatic uh functions like that. So, that's that's not too jazzy. I

**Dave Jones:** I'm kind of liking this thing. It's really good and it works. Works a treat. Still trying to figure out why if you go to clear all and then see, it gives a couple of ones, a one there and a something over here.

**Dave Jones:** Yeah, I don't know. Not sure. Anyway, that's a fascinating example of 1970s calculator technology. Hands up if you used one of these or an older model or something like that. But anyway, I hope you found that interesting. If you did, give it a big thumbs up and as always, you can discuss down below.

**Dave Jones:** Catch you next time.
