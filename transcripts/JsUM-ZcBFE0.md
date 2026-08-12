---
video_id: JsUM-ZcBFE0
title: EEVblog #788 - Apple IIC Teardown
url: https://www.youtube.com/watch?v=JsUM-ZcBFE0
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 26, "3": 40, "4": 51, "5": 61, "6": 76, "7": 89, "8": 102, "9": 116, "10": 128, "11": 135, "12": 155, "13": 172, "14": 181, "15": 194, "16": 204, "17": 216, "18": 235, "19": 249, "20": 261, "21": 272, "22": 287, "23": 299, "24": 312, "25": 319, "26": 330, "27": 340, "28": 362, "29": 375, "30": 390, "31": 403, "32": 412, "33": 423, "34": 438, "35": 457, "36": 470, "37": 484, "38": 496, "39": 510, "40": 525, "41": 539, "42": 554, "43": 567, "44": 579, "45": 593, "46": 614, "47": 637, "48": 647, "49": 665, "50": 680, "51": 695, "52": 706, "53": 725, "54": 742, "55": 766, "56": 781, "57": 798, "58": 812, "59": 827, "60": 848, "61": 871, "62": 885, "63": 897, "64": 909, "65": 927, "66": 952, "67": 967, "68": 984, "69": 997, "70": 1010, "71": 1023, "72": 1033, "73": 1041, "74": 1054, "75": 1062, "76": 1072, "77": 1086, "78": 1099, "79": 1109, "80": 1124, "81": 1134, "82": 1150, "83": 1160, "84": 1175, "85": 1184, "86": 1194, "87": 1207, "88": 1220, "89": 1230, "90": 1244, "91": 1264, "92": 1276, "93": 1286, "94": 1302, "95": 1317, "96": 1334, "97": 1346, "98": 1357, "99": 1370, "100": 1387, "101": 1402, "102": 1416, "103": 1436, "104": 1452, "105": 1476, "106": 1498, "107": 1513, "108": 1522, "109": 1536, "110": 1547, "111": 1560, "112": 1571, "113": 1590, "114": 1606, "115": 1619, "116": 1635, "117": 1644, "118": 1659, "119": 1672, "120": 1684, "121": 1697, "122": 1709, "123": 1720, "124": 1736, "125": 1747, "126": 1756, "127": 1765, "128": 1777, "129": 1790, "130": 1803, "131": 1816, "132": 1823, "133": 1835, "134": 1847, "135": 1863, "136": 1874, "137": 1884, "138": 1898, "139": 1906, "140": 1926, "141": 1936, "142": 1956, "143": 1970, "144": 1982, "145": 1998, "146": 2010}
---

**Dave Jones:** Hi, it's teardown time. Even better than that, it's retro computer teardown time. We love retro computers here on the EEVblog. They're one of my more popular teardowns. Today, we've got the classic Apple IIc from 1984.

**Dave Jones:** Let's check it out. And still works. Beauty. And thank you very much to Oliver, who gave this to me at the recent Maker Faire in Sydney. Here's Oliver. Thanks, mate.

**Dave Jones:** Um he actually found it on local uh curbside garbage collection. So, it came with the machine, the original control, uh the original power supply. We've got a mouse and a whole bunch of floppies as well.

**Dave Jones:** Awesome. Thanks, Oliver. So, the IIc came out in 1984. It was not a successor to the Apple IIe. They actually sold them at the same time. The C in the IIc actually stands for compact.

**Dave Jones:** And as you can see, it is basically a pretty small and compact unit considering that it has a built-in 5 1/4 in floppy drive. That was one of the big uh selling points of this puppy back in the day.

**Dave Jones:** And it even had a carry handle on the back. Carry handle's actually uh fallen off this one. So, you can actually carry it around. I don't know if anyone really did that cuz you got to actually lug around this huge big brick linear power supply as well.

**Dave Jones:** This big huge uh transformer. Um so, yeah, it wasn't really compact. It wasn't really portable in that sense because I didn't have a battery, uh external power supply, and it didn't have any built-in display.

**Dave Jones:** The most common display for this thing was the uh small CRT, which I do not have, unfortunately, which went um sat on a uh case. This thing was actually tilted up like this so that you could uh you know, it was more ergonomic to use the keyboard.

**Dave Jones:** And then the display would come over the top, and it would sit in. I'll probably link in a photo there. Or there was also an optional uh one-color, I believe it was, LCD screen, which sort of sat on the top here and kind of made it look like a little laptop but it wasn't really.

**Dave Jones:** No internal battery but still, you know, this was a reasonably popular machine back in the day. Um a lot of people compared it to the IBM PC Junior at the time.

**Dave Jones:** That was a bit of a fire and I guess it maybe a lot of people will say the 2C was a fire as well but it is a classic machine.

**Dave Jones:** Now it differed slightly from the Apple II in that it while it used a 6502 processor, it used the 65C02 which is the new CMOS version of it. As such slight differences in there which meant that not all software which made use of some quirks in the original 6502, they couldn't run on this 2C but it was pretty much compatible.

**Dave Jones:** Basically a compatible chip in the end and it worked at the same screaming just over 1 MHz. Beauty. It came with 128K of RAM. The 140K 5 and 1/4 inch floppy built in as well whereas the Apple II of course all that sort of stuff was separate.

**Dave Jones:** Um it's got an 80 column mode as well. That was all built in. So this had a lot of stuff built in. Serial ports as well on the back.

**Dave Jones:** Built in mouse port. These are all optional extra on the 2E. The 2E of course had all the expansion slots in it or the original Apple II all the as well as the 2E all the expansion slots in it.

**Dave Jones:** This has no expansion capability at all but it's most of the stuff you needed to have a functioning computer were built in. So it was you know, it was pretty decent in that respect.

**Dave Jones:** Didn't really need expansion capability in this sort of thing but I guess it wouldn't be nice but you can't fit it in a nice compact case like this. And it had both RGB monitor and composite monitor outputs.

**Dave Jones:** We'll use the composite output today to actually see if we can play Zork on this thing. Beauty. And at whopping colors. It wasn't that shabby for the time I guess but yeah there were better machines out there but still it was fairly reasonable for the time.

**Dave Jones:** The original retail price about 1,300 US dollars. That was from 30 years ago, 1984 dollars here. Woo, that was a lot of money. But hey, it was a fully functioning computer with like 128 K of RAM and everything.

**Dave Jones:** And it also used the integrated was machine custom ASIC chip to actually replace the dedicated disk controller in this thing. So, it'll be interesting to crack this puppy open.

**Dave Jones:** And here it is. It's not in bad condition for its age. Yes, it has yellowed, very common for the time. That comes from the bromide in the plastics that they used to use leaching out.

**Dave Jones:** So, very common. You can fix it, but it's yeah, it's not that easy. 5 and 1/4 inch floppy drive, as I said. There we go. Look at that. Whopping 140 K per disk, double-sided, too.

**Dave Jones:** Beauty. And we've got some ventilation slots here in the top. It looks like it's got a filter on the top of it, so you can't actually see the circuitry down in there to keep all the dust and crap out.

**Dave Jones:** And the keyboard's actually really nice. I liked the style of the keys with the sort of the flat part and then they're raised up in the middle. And I love, you know, I loved always loved the feel of this keyboard.

**Dave Jones:** The only time I ever used a 2C, actually, I didn't know anyone who owned one. The only time I ever got to play with one was at the local library.

**Dave Jones:** They This was their main computer in the local library, and you had to go in, give you hand your library card over, they'd give you the floppy disks, and you know, you could go over and use it, you know, you could book it for an hour or whatever and use the thing.

**Dave Jones:** So, I used to do that back in the day. Wow, what was that? Yeah, mid-80s. Geez. Now, there was actually two models of the 2C. This is the original 2C.

**Dave Jones:** There was also the 2C Plus, and it came out in 1988 when this one finished selling this. So this one had a 4-year lifetime and major the two major changes in that are they actually replaced the 80 40 column switch here switches here with a volume.

**Dave Jones:** They actually had a volume slider here and they also changed the 5 and 1/4 inch floppy to a 3 and 1/2 inch floppy. And the 2C Plus also ran at 4 MHz instead of the 1 MHz that this ancient puppy did.

**Dave Jones:** But unfortunately I I think it was a bit of a flop at the time the 2C Plus because Apple had already released the 2GS, the graphics and sound model which had a really advanced graphics and sound capability for its day and they didn't include any of that in the 2C Plus.

**Dave Jones:** So yeah, this original 2C it's even worse. It's got like one-bit sound and well, yeah, okay, it can do 560 by 192 15 color graphics but yeah, pretty ordinary.

**Dave Jones:** On the side here, we've got ourselves headphones and a volume slider. For the speaker that's tucked up under there. And there's a label for those playing along at home.

**Dave Jones:** It doesn't I don't think it has a date. I'm not sure what the barcode thing here is if that's a serial number. I'm not or or what's going on there.

**Dave Jones:** I'm not entirely sure but yeah, basically 18 watts for the CPU. Whoa! Geez, you can fly to Alpha Centauri on 18 watts. If we have a look on the back here, we've got ourselves a serial mouse port.

**Dave Jones:** We've got ourselves a modem comms interface. That's our RGB monitor output. That's our composite monitor output which we're going to be using today. Another external second floppy disk drive, a serial printer and the DC power connector using old school DIN connectors of course.

**Dave Jones:** Look at that. You can see the connectors they're a little bit crusty, but uh yeah, she still works. Hmm, this thing's seen better days. And there's the money shot for the fanboys.

**Dave Jones:** And as I said, this is where the carry handle uh goes, and it did come with the carry handle, but look, very different uh type of plastic. It hasn't hasn't yellowed at all, so maybe um yeah, it's like an entirely different type of plastic.

**Dave Jones:** Didn't have the bromide in there to actually uh leach out. So, you know, faded with all that uh ultraviolet exposure. So, anyway, um I don't know how they got that in and out without taking the case off.

**Dave Jones:** Hmm. Anyway, you can carry this around. Ooh, look, I've got my Apple IIc with my big linear transformer as well. Hmm, and my monitor. Rarr. And there's the brick power supply for it.

**Dave Jones:** It's IEC uh input connector here, but uh yeah, it's just a whoppin' great big transformer. That had a nominal output of uh 15 V DC at 1.2 amps or so, so yeah, that wouldn't that wouldn't be uh regulated at all.

**Dave Jones:** That'd just be a bridge rectifier, a full-wave bridge rectifier, and some output caps, and Bob's your uncle. But it did have all the requisite type approvals. Beauty. And here's an original Apple mouse as well.

**Dave Jones:** How original? Well, look at the serial number. 20,452. Geez, that's pretty good for Australia. I I'm 20,000th Apple mouse ever made. It's not many at all. Made in the United States of America.

**Dave Jones:** And the main unit assembled in Ireland. To be sure, to be sure. Here we go. Let's try and boot this puppy up. I've got one of these uh car rearview mirror LCD reversing camera thingamabobs.

**Dave Jones:** Um it'll do. It's got composite video input. We're going to try and play Zork 2. Fantastic. Oh, I've got the original tab. Can you remember putting the tabs on to the right protect tab?

**Dave Jones:** Side A is Zork 2. Side B? Nothing. So, let's whack that in the drive and clunk that down. You have to go clunk. Back in the day, I'll try not to get glare on the screen.

**Dave Jones:** And here we go, let's try and boot it. Listen to the sounds of then. It's reading the floppy. Come on. You can do it. Hey, doesn't like that. And we're in like Flynn.

**Dave Jones:** It works. It still reads a floppy disk after like 30 years. And more than 30 years. Unbelievable. So, we can go Let's play Zork. Pick up sword. Why does it have to access the disk?

**Dave Jones:** It's got to access the disk. You Oh, no, it doesn't like that. Internal error. Floppy drive is a bit dodgy, I'm afraid. Let's try that again. Here we go.

**Dave Jones:** We've got our Apple 2c. We're in. And pick up sword. Yeah, why can't it It's got 128 K of RAM. Why can't it load? Why does it have to keep reading the disk?

**Dave Jones:** Jeez. Just to do Oh, no, it Trust me, it does work. Hmm. Anyway, you can see that it still works 30 years later. Fantastic. I love it. Now, the thing with the Apple 2c is that it's really quite annoying.

**Dave Jones:** If you boot the thing up without a floppy disk in it, then you get the Apple 2c up there and then you just get What? Check disk drive. There's nothing like it doesn't pop straight up into your basic uh command prompt.

**Dave Jones:** So, the way you do that, which is completely non-obvious, control reset like that, and bingo, we're at our prompt. And we can find out what version of the ROM we had.

**Dave Jones:** We can go peek minus 1089. That is completely obvious, of course. And we've got ROM version 255. And if we do call minus 151, ta-da, we enter the monitor.

**Dave Jones:** The power, can you feel it? You can also do the exact same thing using the command print peek 6447, which again is completely obvious. And this is 255 means it's the original ROM version.

**Dave Jones:** Kill. Grew. Wha wha wha wha. If you don't reset it properly, chucks a wobbly. And it came with a whole bunch of these disks. They aren't Apple original. They're all like Apple use Sydney Apple users group.

**Dave Jones:** Look at that, Blackjack and cards, the Applefest 1992. Fantastic double-sided. Even a sticker on the bottom. Integer on flip side. Love it. So, there you go. Anyone remember the Apple or was anyone part of the Sydney Apple users group?

**Dave Jones:** Is this your machine? Did you dump it on the roadside? Surely not. Anyway, yeah, no original disk. We've got Masters Beginner Calc Layer, whatever that is. Anyway, we've got a whole bunch of them.

**Dave Jones:** Fantastic. Which one do we want? I'll have global thermonuclear war. So, looks like this was like a monthly disk or something and from the users group and came with a whole bunch of different programs by the looks of it.

**Dave Jones:** All right, let's crack this puppy open and see what Cupertino has to offer. Now, it's all going to be through-hole DIP technology, of course. That's pretty much what it was back in the '80s.

**Dave Jones:** So, don't expect any surface mount stuff in here at all. I'm not sure where I got four bigger screws here. I'm not sure what the deal is there, but anyway, I'm not sure if the Woz himself actually worked on this because he, after his plane crash in the early '80s, left Apple for a bit.

**Dave Jones:** He did come back and famously, you know, worked as just an engineer. And but I don't think he's ever credited with the two C's. So, probably working on the 2GS more than the two C cuz this is basically just an Apple II and then they just, you know, it's just packaging integration and stuff like that.

**Dave Jones:** Probably something that the Woz wouldn't have been that interested in, I'd be guessing. So, these four here are actually metal threaded inserts where the uh other ones were just self-tappers into the plastic.

**Dave Jones:** So, I'm not sure if this is the correct order to take it apart. I guess we'll find out. We're getting somewhere. I can see the crusty phenolic single-sided board for the keyboard.

**Dave Jones:** Um something came out here, a bit of rubber sort of rubber strip. Um that looks like it's surrounding the keyboard, but uh it's probably clips on the back or something like that.

**Dave Jones:** But yeah, this top plate, obviously, obviously just comes off somehow. There we go. There we go. Uh almost. Ta-da! We're in like Flynn. Errol, that is. And as you can see, there's not a huge amount doing here.

**Dave Jones:** We're got our dominated by the big 5 and 1/4 inch floppy. We'll take that out separately, of course. And that was, you know, 140 K job. And of course, the Woz famously with the Apple drives, actually how he got the cost down was just had the mechanism itself and then developed his own interface electronics and famously did it with like five chips or something.

**Dave Jones:** Can't remember the exact number. And that was in the original Apple and then for the Apple starting with his 2C, I believe, and then the 2GS and other ones they put it that same circuitry into a small ASIC chip or PLD or whatever it was.

**Dave Jones:** And that became the integrated Woz machine. So, as I remarked before, the keyboard itself, this is not high-quality fiberglass board. It's what's called a phenolic base board. It's very cheap, very common in consumer gear.

**Dave Jones:** So, nothing inherently wrong with it. They still use it today. You open up any, you know, you open up your $5,000 LCD TV or something and you'll probably find that the power supply uses a phenolic base board.

**Dave Jones:** They can shave a few cents off there, so they do. So, yeah, we've got a ribbon up here that uh connects that down in there. So, that actually just slides into they've put a little cutout in the drive there.

**Dave Jones:** That's pretty good. Ta-da! Oh, we're more in like Flynn. Look at that. I actually really liked how they've added this strengthening bar across here. This probably like, you know, ABS plastic or something, but that strengthens the keyboard.

**Dave Jones:** So, you can see that that brace is in there and over in here. So, that'll So, when you've got this in like this, when you're pressing the middle of the keyboard, it doesn't flex and feel cheap and nasty.

**Dave Jones:** So, that's a That's a really nice addition there. Somebody was thinking. And if we take a look at the main guts down here, we've got ourselves a date code.

**Dave Jones:** The main uh 65C02 made by NCR, by the way. There you go. It was Yeah, made by all and sundry back in the day. Uh date code uh fourth week 84.

**Dave Jones:** Uh we've got first week 84. We've got 31st week 84. But, uh these are fairly You know, they might have had, you know, a ton of these in stock.

**Dave Jones:** DRAMs were like these were the precious thing back in the day. My precious. And uh we've got a date code of um first week 80 uh fifth week 85.

**Dave Jones:** So, there you go. This They would have put this into production like weeks after that. So, very early 1985 vintage this machine. And here's some attention to detail on the EMC, the electromagnetic uh conformity for this thing.

**Dave Jones:** This is like a steel ring here, like a you know, a steel wool steel mesh ring that connects the one of the ground points here. And this is one of the mounting posts for the uh floppy drive.

**Dave Jones:** So, that just uh electrically connects the floppy drive down to the main board there. Very nice. They've got uh two of those. And there you go. That's just for the 6502 fanboys.

**Dave Jones:** And of course, it wouldn't be an early '80s computer without a couple of bodges on it. There we go. Genuine mod wire there. And a resistor going between the pin on this uh GAL/power device over to uh one of the vias there.

**Dave Jones:** Nice. No surprises for finding the famous integrated Woz machine, I seek up here. There it is, IWM, right next to the uh floppy port, of course. There's the internal floppy connector.

**Dave Jones:** There's the external floppy connector. So, I haven't actually looked at the uh schematic and architecture of this thing yet, but obviously like they're just uh parallel uh data, and then they've probably just got a different uh selection or uh some other uh miscellaneous control lines for the separate uh floppy drive.

**Dave Jones:** You probably couldn't use both at once. Now, it's interesting to note that this is the original Apple uh 2c, and you can tell because all there is no memory expansion.

**Dave Jones:** All the memory, the 128k, is on the board here, right down here. Now, in 1986, they did release a memory expansion version of this. It's a substantially different uh board layout, and it's got a um Here's a photo of it.

**Dave Jones:** It's got a memory expansion connector down here, and this allows you to expand the memory and thing. Not so in this original one. And you can see there's a few other uh circuit changes as well.

**Dave Jones:** One thing I really like about these old machines is that they put proper silk screen labels on. Look, they told you what all the uh block parts of the unit were, what all the main chips.

**Dave Jones:** Look, IWM, integrated was machine. TMG, that's the uh main timing uh chip. Uh GLU, that's a It's Well, it's glue logic, but it stands for uh you know, general-purpose uh interface logic unit.

**Dave Jones:** Um We've got our character generator up here. We've got video latch here, and there's the 80 latch, uh for example, for the 80 column mode. And just everything is labeled.

**Dave Jones:** It's brilliant. And the main elements down here, I've already uh pointed out the main uh CPU, the MMU, that's the memory management unit, handles all the memory addressing and all that sort of jazz.

**Dave Jones:** Um IOU, that's pretty uh obvious. That's the um IO uh interface IO peripheral uh type interface. And then we've got our uh character generator uh ROM here. That's what map stands for, the character, you know, keyboard mapping unit.

**Dave Jones:** And then mon down here is monitor, of course, the old-school uh word for the um firmware. And this puppy here is the um ink, which is uh encoder. And of course, that's the keyboard encoder, because you need a uh keyboard encoder to decode all the uh keys, of course, like to do the um matrix address uh mapping.

**Dave Jones:** As you you see, there's basically uh nothing for the sound here. Here's our volume uh knob over here on the side, our headphone output, and just like yeah, there's no sound chip, no nothing.

**Dave Jones:** It was just single bit sound output. Beep. Beep. Beep. And you might actually have been wondering about this switch here that looks like a keyboard. That's because it is the keyboard switch.

**Dave Jones:** And what that one does is it switches between your standard layout like this that every your QWERTY layout and the four old school Dvorak layout. So, yeah, for those Dvorak fans, I guess you could get like a different key uh tops and put them on.

**Dave Jones:** And um or maybe they actually sold a Dvorak uh configured uh machine for those uh yeah, Dvorak fans. So, anyway, yeah, nobody does that anymore, do they? Does anyone out there use a Dvorak keyboard?

**Dave Jones:** Come on, there must be somebody. So, what happens with your keyboard, of course, is the keyboard encoder uh takes the uh keyboard matrix and gives you a matrix location of which actual key was pressed, and then the character uh generator map ROM here cuz that's effectively what it is.

**Dave Jones:** It's just a uh it's just a ROM essentially, a lookup table, that then converts that matrix value into a particular ASCII character, which then can be uh displayed on the screen and everything else.

**Dave Jones:** And these two S uh 6551s, which are labeled 6851s here on the uh silkscreen, they are actually your two uh serial chips cuz this thing had uh two serial ports on it.

**Dave Jones:** And the main clock for this thing, there it is, 14.24982 MHz. And that, in combination with the uh timing chip here, generated all the system timing, including the main uh processor clock.

**Dave Jones:** So, the main processor clock run at just over 1 MHz. They would have divided that puppy in here by 14. WE'VE GOT ONE! YES, 555 timer! And then well, a dual 555 timer the 556 brilliant and the ventilation slots on the back here.

**Dave Jones:** I don't know how they're working that well cuz there's a metal grid on there. I'll show might be able to see that on the other side and then there's an insulating card under there of course cuz you can't have the bottom of these dip packages shorting out to the metal on the back.

**Dave Jones:** So there's like that just covering up all the all the vent holes are under there. What the that's not going to be effective at all. There they are. We've got a metal screen under there, but yeah, the board just sat flat on there.

**Dave Jones:** It's yeah, useless and just for kicks. We'll check the processor clock. Now we need the uh pin 37 of the 6502 which is the main input clock phase and the 6502 actually has separate clock outputs as well.

**Dave Jones:** So there you go. My Rigol scope 1.01562 megahertz or thereabouts. You can see that it's all a little bit jittery here. Now I don't know if there's like the odd missing cycle in there or not.

**Dave Jones:** Not sure what's going on. So if we stop it and go in it all looks uh it all looks fairly fairly normal. So you might have some trigger jitter no uh uh no is that my imagination might have some trigger jitter or something in there, but that looks uh see little bit jittery.

**Dave Jones:** Oh, what's going on? Well, yeah, I'm not sure that's actually trigger jitter. I think it's uh something genuine on the clock. So I'm not sure what's happening there. I don't know enough about the Apple uh timing chip to uh to know what that deal is.

**Dave Jones:** There you go. There's the main processor clock and it's rock solid. Uh it's a little bit rounded off there because I've got uh my bandwidth limiter turned on and I'm not exactly uh probing this uh properly, hence all the ringing and crap like that.

**Dave Jones:** But yeah, it's rock solid. So, there's something else. Um yeah, so the timing coming out of the timing chip, it's probably missing a pulse here or there for uh some particular reason.

**Dave Jones:** Maybe some sort of, you know, I don't know, interrupt wait statey type thing. And even Apple couldn't escape the clutches of Bill. There we go. Copyright Microsoft 77 cuz there's some uh Microsoft Basic happening in there.

**Dave Jones:** And all we've really got left to look at is this brick here, this nice big shield of brick TDK did give away. That's a DC-to-DC converter. Here's our DC input from our linear uh plug pack that we've got.

**Dave Jones:** Um this looks like a melted capacitor on the top, but it's a it's not. I think it's a big uh Yeah, it's just a big wrapped uh wire wound inductor there, just a big choke.

**Dave Jones:** And then we just got a big uh mains input uh filter cap Nippon Chemi-Con. Thank you very much. Tell you what though, I do really like how they've got the card edge connector here, completely separate shielding enclosure.

**Dave Jones:** And along with those um uh shielding um EMI uh gaskets I told you about going up to the floppy drive, they they took EMI reasonably seriously. Um you know, it's hard when you've got like a a double-sided board like this and you've just got traces, buses, big buses running everywhere.

**Dave Jones:** But uh you know, they're done a pretty decent job there. How does that come out? Just got to pull out. There we go. We're in like Flynn. Well, I'll tell you what, I don't mind that puppy at all.

**Dave Jones:** That looks actually quite nice. End-on resistors, which were uh lead formed end-on resistors, very common for the day, of course, and that's a very nice clean neat layout. Huge big ground plane on the top.

**Dave Jones:** Nippon Chemicon caps, fantastic. No expense spared there. So, you know, they're they're still going. No leaks in those whatsoever. And that's a very nice implementation of a DC DC converter.

**Dave Jones:** I'm not sure how many rails it's going to have 5 volts and minus 5 volts and 12 volts or something. From a 12 to 15 like up to 15 volt input from the plug pack.

**Dave Jones:** If I put it back together and just take the lid off, you can see this bracket that they're using at an angle there to hold in and push the switching transistor across against the back end here, which is using this as a heat sink.

**Dave Jones:** That's rather novel, but yeah, a little bit convoluted to try and get in though. And last, but certainly not least, this ugly looking floppy drive here, but my hat's off, it still worked.

**Dave Jones:** I found some gunk in here and everything. So, it it still worked a treat. It just goes to show the robustness of these things, really. It's just incredible. And of course, there's our head right down in there.

**Dave Jones:** And if we whack our floppy in, of course, so there you go. And then the stepper motor just moves the head in and out and turns the disk. Not much going on there at all, but I love the bottom.

**Dave Jones:** Look at this. They've put an old school timing chart on here so that you can actually get the rotational speed with your stroboscope. Fantastic. And made in Japan. Hi to all my Japanese viewers.

**Dave Jones:** It's an Alps drive and serial number only 60,000. That's That's pretty low. This is one of the earlier units, really. I mean, how many of these things did they make?

**Dave Jones:** A million Apple IIs? I'm not sure of the exact number, but as you can see, there's not much on here at all. There's just a motor control stuff Uh pretty much because all of the digital decoder and head amplifier and stuff like that.

**Dave Jones:** But apart from that, there's you know, there's bugger all on here because all of it cuz was did his own controller famously and that saved a lot of the cost there.

**Dave Jones:** Now of course on this because it's a single-sided disk, this top part here isn't the head. It's just like a It's just like a little felt pad type thing.

**Dave Jones:** There is our head. Right down in there. There we go. It's got some gunk on it. That could do with some cleaning. Oh, there it is. Look at that.

**Dave Jones:** For those who remember back in the day, you used to be able to get 5 and 1/4 inch cleaning disk. It was like a cloth instead of having like the mylar magnetic coated disk itself.

**Dave Jones:** The it actually had like a cloth in there like a microfibery type cloth that didn't have microfibers back then. I don't know. An equivalent type thing and then you'd put your you'd put your cleaning fluid onto that.

**Dave Jones:** You'd stick it in and then you'd start the drive up and clean your head. I think that's what we need to do here. What you need is a cotton swab like this and you need some isopropyl alcohol.

**Dave Jones:** This is the pure stuff 99.8% or you can also use one of these medical swabs as well. These are only 70% alcohol, but they'll do the business. So they've actually got a little cleaning cloth inside already pre-moistened.

**Dave Jones:** So you can actually use that to just to get in there and wipe the head. Now we just lift up this pressure pad here cuz this is only a single-sided drive.

**Dave Jones:** The double-sided ones will have heads on both sides and they'll actually have a head on this mechanism that lifts up. So you'll have to do both, but just repeat it.

**Dave Jones:** And we can see our head in there. Very, very dirty. Look at that. So we've dipped our cotton bud in the alcohol. Not too much, but just getting there and start scrubbing.

**Dave Jones:** You can see it might take a bit of elbow grease this one. I don't think this one's been cleaned in 30 years, maybe. Hmm. And there we go. Head is perfectly clean now.

**Dave Jones:** Now, just make sure there's no uh fibers in there. Just get inside because you can actually get fibers that come off these. If you get good uh micro uh fiber type uh cotton buds, they're the best.

**Dave Jones:** Now, you shouldn't wipe this at all because the alcohol will just evaporate. So, don't worry about it. Just leave it a few minutes and she'll be right. Here we go.

**Dave Jones:** That's 1/500 shutter speed. You can see the inner loop, which was the 50, almost standing still. Almost. Oh, pretty close. And this disk drive seems to be working a treat after we uh cleaned it.

**Dave Jones:** I think there's something wrong with physically wrong with this old disk. I can see some physical uh damage to it. So, anyway, I'll load in another one. Check it out.

**Dave Jones:** High resolution demonstration. Oh, biorhythms. They were all the go back in the day. Oh, let's go for the uh USS Enterprise. High-res picture. Oh, got to do it. Okay, I think what's happening here is this LCD somehow maybe not can be compatible with the graphics mode.

**Dave Jones:** Perhaps I regardless of what program I seem to run, if I try and go into graphics mode, it just blank screens. So, sorry. There we go. You saw it.

**Dave Jones:** We had the Enterprise. I'll try and capture that. Fantastic. So, there you go. That's a probably a rather lengthy look at the Apple 2c, the original one, not to be confused with the 2c plus or that one uh with the upgraded memory module.

**Dave Jones:** 1990 This was like the first early weeks 1995. So, this is just over 30 years old and it still works. Beauty. No problems with the power supply cuz they use top quality caps in there.

**Dave Jones:** It's well-built and really not much I can wrong go wrong with you know 5 volt TTL stuff at all. And the floppy drive amazingly still works. I've cleaned that and I think I'll just go play some Zork.

**Dave Jones:** And by the way, I'll link the full service manual for this thing. It's got the schematics and it's like 560 pages and it's got the ROM dump listing and man, everything including the kitchen sink.

**Dave Jones:** It's fantastic. They really did proper technical reference manuals service manuals back in those days. It's fantastic. So, terrific bedtime reading. So, if you like that, please give it a big thumbs up on YouTube cuz that always helps a lot.

**Dave Jones:** And if you want to discuss it YouTube comments or eevblog.com forum or blog down below. Catch you next time.
