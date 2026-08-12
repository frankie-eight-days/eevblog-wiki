---
video_id: JsUM-ZcBFE0
title: EEVblog #788 - Apple IIC Teardown
url: https://www.youtube.com/watch?v=JsUM-ZcBFE0
source: youtube-asr
timestamps: {"0": 1, "1": 20, "2": 33, "3": 48, "4": 59, "5": 71, "6": 85, "7": 97, "8": 109, "9": 123, "10": 135, "11": 150, "12": 166, "13": 179, "14": 192, "15": 204, "16": 216, "17": 235, "18": 252, "19": 266, "20": 282, "21": 297, "22": 310, "23": 323, "24": 330, "25": 346, "26": 365, "27": 377, "28": 393, "29": 407, "30": 423, "31": 435, "32": 452, "33": 470, "34": 484, "35": 499, "36": 517, "37": 531, "38": 552, "39": 564, "40": 582, "41": 596, "42": 614, "43": 635, "44": 645, "45": 663, "46": 677, "47": 691, "48": 711, "49": 729, "50": 742, "51": 768, "52": 784, "53": 803, "54": 816, "55": 835, "56": 851, "57": 869, "58": 885, "59": 901, "60": 920, "61": 939, "62": 952, "63": 967, "64": 986, "65": 999, "66": 1012, "67": 1028, "68": 1039, "69": 1052, "70": 1067, "71": 1083, "72": 1097, "73": 1109, "74": 1124, "75": 1139, "76": 1152, "77": 1165, "78": 1178, "79": 1190, "80": 1207, "81": 1222, "82": 1235, "83": 1252, "84": 1265, "85": 1281, "86": 1297, "87": 1312, "88": 1327, "89": 1344, "90": 1357, "91": 1372, "92": 1391, "93": 1402, "94": 1416, "95": 1439, "96": 1457, "97": 1476, "98": 1498, "99": 1511, "100": 1522, "101": 1538, "102": 1552, "103": 1565, "104": 1580, "105": 1597, "106": 1613, "107": 1630, "108": 1644, "109": 1659, "110": 1675, "111": 1691, "112": 1701, "113": 1717, "114": 1730, "115": 1747, "116": 1760, "117": 1772, "118": 1786, "119": 1798, "120": 1813, "121": 1826, "122": 1839, "123": 1861, "124": 1874, "125": 1888, "126": 1903, "127": 1919, "128": 1933, "129": 1947, "130": 1963, "131": 1976, "132": 1991, "133": 2008}
---

**Dave Jones:** Hi, it's teardown time. Even better than that, it's retro computer teardown time. We love retro computers here on the EEVblog. They're one of my more popular teardowns. Today, we've got the classic Apple IIc from 1984. Let's check it out. And still works.

**Dave Jones:** Beauty. And thank you very much to Oliver, who gave this to me at the recent Maker Faire in Sydney. Here's Oliver. Thanks, mate. Um he actually found it on local uh curbside garbage collection. So, it came with the

**Dave Jones:** machine, the original control, uh the original power supply. We've got a mouse and a whole bunch of floppies as well. Awesome. Thanks, Oliver. So, the IIc came out in 1984. It was not a successor to the Apple IIe. They actually sold

**Dave Jones:** them at the same time. The C in the IIc actually stands for compact. And as you can see, it is basically a pretty small and compact unit considering that it has a built-in 5 1/4 in floppy drive. That

**Dave Jones:** was one of the big uh selling points of this puppy back in the day. And it even had a carry handle on the back. Carry handle's actually uh fallen off this one. So, you can actually carry it around. I don't know if anyone really

**Dave Jones:** did that cuz you got to actually lug around this huge big brick linear power supply as well. This big huge uh transformer. Um so, yeah, it wasn't really compact. It wasn't really portable in that sense because I didn't

**Dave Jones:** have a battery, uh external power supply, and it didn't have any built-in display. The most common display for this thing was the uh small CRT, which I do not have, unfortunately, which went um sat on a uh case. This thing was

**Dave Jones:** actually tilted up like this so that you could uh you know, it was more ergonomic to use the keyboard. And then the display would come over the top, and it would sit in. I'll probably link in a photo there. Or there was also an

**Dave Jones:** optional uh one-color, I believe it was, LCD screen, which sort of sat on the top here and kind of made it look like a little laptop but it wasn't really. No internal battery but still, you know, this was a reasonably popular machine

**Dave Jones:** back in the day. Um a lot of people compared it to the IBM PC Junior at the time. That was a bit of a fire and I guess it maybe a lot of people will say the 2C was a fire as well but it is a

**Dave Jones:** classic machine. Now it differed slightly from the Apple II in that it while it used a 6502 processor, it used the 65C02 which is the new CMOS version of it. As such slight differences in there which meant that not all software which made

**Dave Jones:** use of some quirks in the original 6502, they couldn't run on this 2C but it was pretty much compatible. Basically a compatible chip in the end and it worked at the same screaming just over 1 MHz. Beauty. It came with 128K of RAM. The

**Dave Jones:** 140K 5 and 1/4 inch floppy built in as well whereas the Apple II of course all that sort of stuff was separate. Um it's got an 80 column mode as well. That was all built in. So this had a lot of stuff

**Dave Jones:** built in. Serial ports as well on the back. Built in mouse port. These are all optional extra on the 2E. The 2E of course had all the expansion slots in it or the original Apple II all the as well

**Dave Jones:** as the 2E all the expansion slots in it. This has no expansion capability at all but it's most of the stuff you needed to have a functioning computer were built in. So it was you know, it was pretty

**Dave Jones:** decent in that respect. Didn't really need expansion capability in this sort of thing but I guess it wouldn't be nice but you can't fit it in a nice compact case like this. And it had both RGB monitor and composite monitor outputs.

**Dave Jones:** We'll use the composite output today to actually see if we can play Zork on this thing. Beauty. And at whopping colors. It wasn't that shabby for the time I guess but yeah there were better machines out there but still it was fairly

**Dave Jones:** reasonable for the time. The original retail price about 1,300 US dollars. That was from 30 years ago, 1984 dollars here. Woo, that was a lot of money. But hey, it was a fully functioning computer with like 128 K of RAM and everything. And it

**Dave Jones:** also used the integrated was machine custom ASIC chip to actually replace the dedicated disk controller in this thing. So, it'll be interesting to crack this puppy open. And here it is. It's not in bad condition for its age. Yes, it has

**Dave Jones:** yellowed, very common for the time. That comes from the bromide in the plastics that they used to use leaching out. So, very common. You can fix it, but it's yeah, it's not that easy. 5 and 1/4 inch floppy drive, as I

**Dave Jones:** said. There we go. Look at that. Whopping 140 K per disk, double-sided, too. Beauty. And we've got some ventilation slots here in the top. It looks like it's got a filter on the top of it, so you can't actually see the

**Dave Jones:** circuitry down in there to keep all the dust and crap out. And the keyboard's actually really nice. I liked the style of the keys with the sort of the flat part and then they're raised up in the middle. And I love, you know, I loved

**Dave Jones:** always loved the feel of this keyboard. The only time I ever used a 2C, actually, I didn't know anyone who owned one. The only time I ever got to play with one was at the local library. They This was their main computer in the

**Dave Jones:** local library, and you had to go in, give you hand your library card over, they'd give you the floppy disks, and you know, you could go over and use it, you know, you could book it for an hour

**Dave Jones:** or whatever and use the thing. So, I used to do that back in the day. Wow, what was that? Yeah, mid-80s. Geez. Now, there was actually two models of the 2C. This is the original 2C. There was also the 2C Plus, and it came out in

**Dave Jones:** 1988 when this one finished selling this. So this one had a 4-year lifetime and major the two major changes in that are they actually replaced the 80 40 column switch here switches here with a volume. They actually had a volume slider here

**Dave Jones:** and they also changed the 5 and 1/4 inch floppy to a 3 and 1/2 inch floppy. And the 2C Plus also ran at 4 MHz instead of the 1 MHz that this ancient puppy did. But unfortunately I I think it was a bit

**Dave Jones:** of a flop at the time the 2C Plus because Apple had already released the 2GS, the graphics and sound model which had a really advanced graphics and sound capability for its day and they didn't include any of that in the 2C Plus. So

**Dave Jones:** yeah, this original 2C it's even worse. It's got like one-bit sound and well, yeah, okay, it can do 560 by 192 15 color graphics but yeah, pretty ordinary. On the side here, we've got ourselves headphones and a volume

**Dave Jones:** slider. For the speaker that's tucked up under there. And there's a label for those playing along at home. It doesn't I don't think it has a date. I'm not sure what the barcode thing here is if that's a serial number.

**Dave Jones:** I'm not or or what's going on there. I'm not entirely sure but yeah, basically 18 watts for the CPU. Whoa! Geez, you can fly to Alpha Centauri on 18 watts. If we have a look on the back here,

**Dave Jones:** we've got ourselves a serial mouse port. We've got ourselves a modem comms interface. That's our RGB monitor output. That's our composite monitor output which we're going to be using today. Another external second floppy disk drive, a serial printer and the DC

**Dave Jones:** power connector using old school DIN connectors of course. Look at that. You can see the connectors they're a little bit crusty, but uh yeah, she still works. Hmm, this thing's seen better days. And there's the money shot for the fanboys.

**Dave Jones:** And as I said, this is where the carry handle uh goes, and it did come with the carry handle, but look, very different uh type of plastic. It hasn't hasn't yellowed at all, so maybe um yeah, it's like an entirely different type of

**Dave Jones:** plastic. Didn't have the bromide in there to actually uh leach out. So, you know, faded with all that uh ultraviolet exposure. So, anyway, um I don't know how they got that in and out without taking the case off. Hmm. Anyway, you

**Dave Jones:** can carry this around. Ooh, look, I've got my Apple IIc with my big linear transformer as well. Hmm, and my monitor. Rarr. And there's the brick power supply for it. It's IEC uh input connector here, but uh yeah, it's just a whoppin' great big

**Dave Jones:** transformer. That had a nominal output of uh 15 V DC at 1.2 amps or so, so yeah, that wouldn't that wouldn't be uh regulated at all. That'd just be a bridge rectifier, a full-wave bridge rectifier, and some output caps, and

**Dave Jones:** Bob's your uncle. But it did have all the requisite type approvals. Beauty. And here's an original Apple mouse as well. How original? Well, look at the serial number. 20,452. Geez, that's pretty good for Australia. I I'm 20,000th Apple mouse ever made. It's not

**Dave Jones:** many at all. Made in the United States of America. And the main unit assembled in Ireland. To be sure, to be sure. Here we go. Let's try and boot this puppy up. I've got one of these uh car rearview

**Dave Jones:** mirror LCD reversing camera thingamabobs. Um it'll do. It's got composite video input. We're going to try and play Zork 2. Fantastic. Oh, I've got the original tab. Can you remember putting the tabs on to the right protect tab? Side A is

**Dave Jones:** Zork 2. Side B? Nothing. So, let's whack that in the drive and clunk that down. You have to go clunk. Back in the day, I'll try not to get glare on the screen. And here we go, let's try and boot it. Listen to the

**Dave Jones:** sounds of then. It's reading the floppy. Come on. You can do it. Hey, doesn't like that.

**Dave Jones:** And we're in like Flynn. It works. It still reads a floppy disk after like 30 years. And more than 30 years. Unbelievable. So, we can go Let's play Zork. Pick up sword.

**Dave Jones:** Why does it have to access the disk? It's got to access the disk. You Oh, no, it doesn't like that. Internal error.

**Dave Jones:** Floppy drive is a bit dodgy, I'm afraid. Let's try that again. Here we go. We've got our Apple 2c. We're in. And pick up sword. Yeah, why can't it It's got 128 K of RAM. Why can't it load?

**Dave Jones:** Why does it have to keep reading the disk? Jeez. Just to do Oh, no, it Trust me, it does work. Hmm. Anyway, you can see that it still works 30 years later. Fantastic. I love it. Now, the thing

**Dave Jones:** with the Apple 2c is that it's really quite annoying. If you boot the thing up without a floppy disk in it, then you get the Apple 2c up there and then you just get What? Check disk drive. There's nothing like

**Dave Jones:** it doesn't pop straight up into your basic uh command prompt. So, the way you do that, which is completely non-obvious, control reset like that, and bingo, we're at our prompt. And we can find out what version of the ROM we had. We can go peek minus

**Dave Jones:** 1089. That is completely obvious, of course. And we've got ROM version 255. And if we do call minus 151, ta-da, we enter the monitor. The power, can you feel it? You can also do the exact same thing using the

**Dave Jones:** command print peek 6447, which again is completely obvious. And this is 255 means it's the original ROM version.

**Dave Jones:** Kill. Grew. Wha wha wha wha. If you don't reset it properly, chucks a wobbly. And it came with a whole bunch of these disks. They aren't Apple original. They're all like Apple use Sydney Apple users group. Look at

**Dave Jones:** that, Blackjack and cards, the Applefest 1992. Fantastic double-sided. Even a sticker on the bottom. Integer on flip side. Love it. So, there you go. Anyone remember the Apple or was anyone part of the Sydney Apple users group? Is this

**Dave Jones:** your machine? Did you dump it on the roadside? Surely not. Anyway, yeah, no original disk. We've got Masters Beginner Calc Layer, whatever that is. Anyway, we've got a whole bunch of them. Fantastic. Which one do we want? I'll have global

**Dave Jones:** thermonuclear war. So, looks like this was like a monthly disk or something and from the users group and came with a whole bunch of different programs by the looks of it. All right, let's crack this puppy open and see what

**Dave Jones:** Cupertino has to offer. Now, it's all going to be through-hole DIP technology, of course. That's pretty much what it was back in the '80s. So, don't expect any surface mount stuff in here at all. I'm not sure where I got

**Dave Jones:** four bigger screws here. I'm not sure what the deal is there, but anyway, I'm not sure if the Woz himself actually worked on this because he, after his plane crash in the early '80s, left Apple for a bit. He did come back

**Dave Jones:** and famously, you know, worked as just an engineer. And but I don't think he's ever credited with the two C's. So, probably working on the 2GS more than the two C cuz this is basically just an Apple II and then they just, you know,

**Dave Jones:** it's just packaging integration and stuff like that. Probably something that the Woz wouldn't have been that interested in, I'd be guessing. So, these four here are actually metal threaded inserts where the uh other ones were just self-tappers into

**Dave Jones:** the plastic. So, I'm not sure if this is the correct order to take it apart. I guess we'll find out. We're getting somewhere. I can see the crusty phenolic single-sided board for the keyboard. Um something came out here, a bit of rubber

**Dave Jones:** sort of rubber strip. Um that looks like it's surrounding the keyboard, but uh it's probably clips on the back or something like that. But yeah, this top plate, obviously, obviously just comes off somehow. There we go. There we go.

**Dave Jones:** Uh almost. Ta-da! We're in like Flynn. Errol, that is. And as you can see, there's not a huge amount doing here. We're got our dominated by the big 5 and 1/4 inch floppy. We'll take that out separately, of course. And that was, you know, 140 K

**Dave Jones:** job. And of course, the Woz famously with the Apple drives, actually how he got the cost down was just had the mechanism itself and then developed his own interface electronics and famously did it with like five chips or

**Dave Jones:** something. Can't remember the exact number. And that was in the original Apple and then for the Apple starting with his 2C, I believe, and then the 2GS and other ones they put it that same circuitry into a small ASIC chip or PLD

**Dave Jones:** or whatever it was. And that became the integrated Woz machine. So, as I remarked before, the keyboard itself, this is not high-quality fiberglass board. It's what's called a phenolic base board. It's very cheap, very common in consumer gear. So, nothing inherently

**Dave Jones:** wrong with it. They still use it today. You open up any, you know, you open up your $5,000 LCD TV or something and you'll probably find that the power supply uses a phenolic base board. They can shave a

**Dave Jones:** few cents off there, so they do. So, yeah, we've got a ribbon up here that uh connects that down in there. So, that actually just slides into they've put a little cutout in the drive there. That's pretty good. Ta-da!

**Dave Jones:** Oh, we're more in like Flynn. Look at that. I actually really liked how they've added this strengthening bar across here. This probably like, you know, ABS plastic or something, but that strengthens the keyboard. So, you can see that that brace is in there and over

**Dave Jones:** in here. So, that'll So, when you've got this in like this, when you're pressing the middle of the keyboard, it doesn't flex and feel cheap and nasty. So, that's a That's a really nice addition there. Somebody was thinking. And if we

**Dave Jones:** take a look at the main guts down here, we've got ourselves a date code. The main uh 65C02 made by NCR, by the way. There you go. It was Yeah, made by all and sundry back in the day. Uh date code

**Dave Jones:** uh fourth week 84. Uh we've got first week 84. We've got 31st week 84. But, uh these are fairly You know, they might have had, you know, a ton of these in stock. DRAMs were like these were the precious thing back in

**Dave Jones:** the day. My precious. And uh we've got a date code of um first week 80 uh fifth week 85. So, there you go. This They would have put this into production like weeks after that. So, very early 1985 vintage this machine.

**Dave Jones:** And here's some attention to detail on the EMC, the electromagnetic uh conformity for this thing. This is like a steel ring here, like a you know, a steel wool steel mesh ring that connects the one of the ground points here. And

**Dave Jones:** this is one of the mounting posts for the uh floppy drive. So, that just uh electrically connects the floppy drive down to the main board there. Very nice. They've got uh two of those. And there you go. That's just for the 6502

**Dave Jones:** fanboys. And of course, it wouldn't be an early '80s computer without a couple of bodges on it. There we go. Genuine mod wire there. And a resistor going between the pin on this uh GAL/power device over to uh one of the vias there.

**Dave Jones:** Nice. No surprises for finding the famous integrated Woz machine, I seek up here. There it is, IWM, right next to the uh floppy port, of course. There's the internal floppy connector. There's the external floppy connector. So, I haven't actually looked at the uh

**Dave Jones:** schematic and architecture of this thing yet, but obviously like they're just uh parallel uh data, and then they've probably just got a different uh selection or uh some other uh miscellaneous control lines for the separate uh floppy drive. You probably

**Dave Jones:** couldn't use both at once. Now, it's interesting to note that this is the original Apple uh 2c, and you can tell because all there is no memory expansion. All the memory, the 128k, is on the board here, right down here. Now,

**Dave Jones:** in 1986, they did release a memory expansion version of this. It's a substantially different uh board layout, and it's got a um Here's a photo of it. It's got a memory expansion connector down here, and this allows you to expand

**Dave Jones:** the memory and thing. Not so in this original one. And you can see there's a few other uh circuit changes as well. One thing I really like about these old machines is that they put proper silk screen labels on. Look, they told you

**Dave Jones:** what all the uh block parts of the unit were, what all the main chips. Look, IWM, integrated was machine. TMG, that's the uh main timing uh chip. Uh GLU, that's a It's Well, it's glue logic, but it stands for uh you know, general-purpose

**Dave Jones:** uh interface logic unit. Um We've got our character generator up here. We've got video latch here, and there's the 80 latch, uh for example, for the 80 column mode. And just everything is labeled. It's brilliant. And the main elements

**Dave Jones:** down here, I've already uh pointed out the main uh CPU, the MMU, that's the memory management unit, handles all the memory addressing and all that sort of jazz. Um IOU, that's pretty uh obvious. That's the um IO uh interface IO

**Dave Jones:** peripheral uh type interface. And then we've got our uh character generator uh ROM here. That's what map stands for, the character, you know, keyboard mapping unit. And then mon down here is monitor, of course, the old-school uh word for the um firmware. And this puppy

**Dave Jones:** here is the um ink, which is uh encoder. And of course, that's the keyboard encoder, because you need a uh keyboard encoder to decode all the uh keys, of course, like to do the um matrix address uh mapping. As you you see, there's

**Dave Jones:** basically uh nothing for the sound here. Here's our volume uh knob over here on the side, our headphone output, and just like yeah, there's no sound chip, no nothing. It was just single bit sound output. Beep. Beep. Beep. And you might

**Dave Jones:** actually have been wondering about this switch here that looks like a keyboard. That's because it is the keyboard switch. And what that one does is it switches between your standard layout like this that every your QWERTY layout and the four old school Dvorak layout.

**Dave Jones:** So, yeah, for those Dvorak fans, I guess you could get like a different key uh tops and put them on. And um or maybe they actually sold a Dvorak uh configured uh machine for those uh yeah, Dvorak fans. So,

**Dave Jones:** anyway, yeah, nobody does that anymore, do they? Does anyone out there use a Dvorak keyboard? Come on, there must be somebody. So, what happens with your keyboard, of course, is the keyboard encoder uh takes the uh keyboard matrix and gives you a matrix

**Dave Jones:** location of which actual key was pressed, and then the character uh generator map ROM here cuz that's effectively what it is. It's just a uh it's just a ROM essentially, a lookup table, that then converts that matrix value into a particular ASCII character,

**Dave Jones:** which then can be uh displayed on the screen and everything else. And these two S uh 6551s, which are labeled 6851s here on the uh silkscreen, they are actually your two uh serial chips cuz this thing had uh

**Dave Jones:** two serial ports on it. And the main clock for this thing, there it is, 14.24982 MHz. And that, in combination with the uh timing chip here, generated all the system timing, including the main uh processor clock. So, the main processor

**Dave Jones:** clock run at just over 1 MHz. They would have divided that puppy in here by 14. WE'VE GOT ONE! YES, 555 timer! And then well, a dual 555 timer the 556 brilliant and the ventilation slots on the back here. I don't know how they're

**Dave Jones:** working that well cuz there's a metal grid on there. I'll show might be able to see that on the other side and then there's an insulating card under there of course cuz you can't have the bottom of these dip packages shorting out to

**Dave Jones:** the metal on the back. So there's like that just covering up all the all the vent holes are under there. What the that's not going to be effective at all. There they are. We've got a metal screen under there, but yeah, the board

**Dave Jones:** just sat flat on there. It's yeah, useless and just for kicks. We'll check the processor clock. Now we need the uh pin 37 of the 6502 which is the main input clock phase and the 6502 actually has separate clock outputs as well. So there

**Dave Jones:** you go. My Rigol scope 1.01562 megahertz or thereabouts. You can see that it's all a little bit jittery here. Now I don't know if there's like the odd missing cycle in there or not. Not sure what's going on. So if we stop it

**Dave Jones:** and go in it all looks uh it all looks fairly fairly normal. So you might have some trigger jitter no uh uh no is that my imagination might have some trigger jitter or something in there, but that looks uh see

**Dave Jones:** little bit jittery. Oh, what's going on? Well, yeah, I'm not sure that's actually trigger jitter. I think it's uh something genuine on the clock. So I'm not sure what's happening there. I don't know enough about the Apple uh timing chip to uh

**Dave Jones:** to know what that deal is. There you go. There's the main processor clock and it's rock solid. Uh it's a little bit rounded off there because I've got uh my bandwidth limiter turned on and I'm not exactly uh probing this uh properly,

**Dave Jones:** hence all the ringing and crap like that. But yeah, it's rock solid. So, there's something else. Um yeah, so the timing coming out of the timing chip, it's probably missing a pulse here or there for uh some particular reason.

**Dave Jones:** Maybe some sort of, you know, I don't know, interrupt wait statey type thing. And even Apple couldn't escape the clutches of Bill. There we go. Copyright Microsoft 77 cuz there's some uh Microsoft Basic happening in there. And all we've really got left to look at

**Dave Jones:** is this brick here, this nice big shield of brick TDK did give away. That's a DC-to-DC converter. Here's our DC input from our linear uh plug pack that we've got. Um this looks like a melted capacitor on the top, but

**Dave Jones:** it's a it's not. I think it's a big uh Yeah, it's just a big wrapped uh wire wound inductor there, just a big choke. And then we just got a big uh mains input uh filter cap Nippon Chemi-Con.

**Dave Jones:** Thank you very much. Tell you what though, I do really like how they've got the card edge connector here, completely separate shielding enclosure. And along with those um uh shielding um EMI uh gaskets I told you about going up to the

**Dave Jones:** floppy drive, they they took EMI reasonably seriously. Um you know, it's hard when you've got like a a double-sided board like this and you've just got traces, buses, big buses running everywhere. But uh you know, they're done a pretty decent job there. How does

**Dave Jones:** that come out? Just got to pull out. There we go. We're in like Flynn. Well, I'll tell you what, I don't mind that puppy at all. That looks actually quite nice. End-on resistors, which were uh lead formed end-on resistors, very

**Dave Jones:** common for the day, of course, and that's a very nice clean neat layout. Huge big ground plane on the top. Nippon Chemicon caps, fantastic. No expense spared there. So, you know, they're they're still going. No leaks in those

**Dave Jones:** whatsoever. And that's a very nice implementation of a DC DC converter. I'm not sure how many rails it's going to have 5 volts and minus 5 volts and 12 volts or something. From a 12 to 15 like up to 15 volt input

**Dave Jones:** from the plug pack. If I put it back together and just take the lid off, you can see this bracket that they're using at an angle there to hold in and push the switching transistor across against the back end here, which is

**Dave Jones:** using this as a heat sink. That's rather novel, but yeah, a little bit convoluted to try and get in though. And last, but certainly not least, this ugly looking floppy drive here, but my hat's off, it still worked. I found some gunk in here

**Dave Jones:** and everything. So, it it still worked a treat. It just goes to show the robustness of these things, really. It's just incredible. And of course, there's our head right down in there. And if we whack our floppy in, of course, so there you go.

**Dave Jones:** And then the stepper motor just moves the head in and out and turns the disk. Not much going on there at all, but I love the bottom. Look at this. They've put an old school timing chart on here

**Dave Jones:** so that you can actually get the rotational speed with your stroboscope. Fantastic. And made in Japan. Hi to all my Japanese viewers. It's an Alps drive and serial number only 60,000. That's That's pretty low. This is one of the

**Dave Jones:** earlier units, really. I mean, how many of these things did they make? A million Apple IIs? I'm not sure of the exact number, but as you can see, there's not much on here at all. There's just a motor control stuff Uh pretty much

**Dave Jones:** because all of the digital decoder and head amplifier and stuff like that. But apart from that, there's you know, there's bugger all on here because all of it cuz was did his own controller famously and that saved a

**Dave Jones:** lot of the cost there. Now of course on this because it's a single-sided disk, this top part here isn't the head. It's just like a It's just like a little felt pad type thing. There is our head. Right

**Dave Jones:** down in there. There we go. It's got some gunk on it. That could do with some cleaning. Oh, there it is. Look at that. For those who remember back in the day, you used to be able to get 5 and 1/4

**Dave Jones:** inch cleaning disk. It was like a cloth instead of having like the mylar magnetic coated disk itself. The it actually had like a cloth in there like a microfibery type cloth that didn't have microfibers back then. I don't

**Dave Jones:** know. An equivalent type thing and then you'd put your you'd put your cleaning fluid onto that. You'd stick it in and then you'd start the drive up and clean your head. I think that's what we need to do here.

**Dave Jones:** What you need is a cotton swab like this and you need some isopropyl alcohol. This is the pure stuff 99.8% or you can also use one of these medical swabs as well. These are only 70% alcohol, but they'll do the business. So

**Dave Jones:** they've actually got a little cleaning cloth inside already pre-moistened. So you can actually use that to just to get in there and wipe the head. Now we just lift up this pressure pad here cuz this is only a single-sided drive. The

**Dave Jones:** double-sided ones will have heads on both sides and they'll actually have a head on this mechanism that lifts up. So you'll have to do both, but just repeat it. And we can see our head in there. Very, very dirty. Look at that. So we've

**Dave Jones:** dipped our cotton bud in the alcohol. Not too much, but just getting there and start scrubbing. You can see it might take a bit of elbow grease this one. I don't think this one's been cleaned in 30 years, maybe. Hmm.

**Dave Jones:** And there we go. Head is perfectly clean now. Now, just make sure there's no uh fibers in there. Just get inside because you can actually get fibers that come off these. If you get good uh micro uh fiber type uh

**Dave Jones:** cotton buds, they're the best. Now, you shouldn't wipe this at all because the alcohol will just evaporate. So, don't worry about it. Just leave it a few minutes and she'll be right. Here we go. That's 1/500 shutter speed. You can see the inner

**Dave Jones:** loop, which was the 50, almost standing still. Almost. Oh, pretty close. And this disk drive seems to be working a treat after we uh cleaned it. I think there's something wrong with physically wrong with this old disk. I can see some physical uh

**Dave Jones:** damage to it. So, anyway, I'll load in another one. Check it out. High resolution demonstration. Oh, biorhythms. They were all the go back in the day. Oh, let's go for the uh USS Enterprise. High-res picture. Oh, got to do it.

**Dave Jones:** Okay, I think what's happening here is this LCD somehow maybe not can be compatible with the graphics mode. Perhaps I regardless of what program I seem to run, if I try and go into graphics mode, it just blank screens. So,

**Dave Jones:** sorry. There we go. You saw it. We had the Enterprise. I'll try and capture that. Fantastic.

**Dave Jones:** So, there you go. That's a probably a rather lengthy look at the Apple 2c, the original one, not to be confused with the 2c plus or that one uh with the upgraded memory module. 1990 This was like the first early weeks 1995. So,

**Dave Jones:** this is just over 30 years old and it still works. Beauty. No problems with the power supply cuz they use top quality caps in there. It's well-built and really not much I can wrong go wrong with you know 5 volt TTL

**Dave Jones:** stuff at all. And the floppy drive amazingly still works. I've cleaned that and I think I'll just go play some Zork. And by the way, I'll link the full service manual for this thing. It's got the schematics and it's like 560

**Dave Jones:** pages and it's got the ROM dump listing and man, everything including the kitchen sink. It's fantastic. They really did proper technical reference manuals service manuals back in those days. It's fantastic. So, terrific bedtime reading. So, if you like that, please give it a

**Dave Jones:** big thumbs up on YouTube cuz that always helps a lot. And if you want to discuss it YouTube comments or eevblog.com forum or blog down below. Catch you next time.
