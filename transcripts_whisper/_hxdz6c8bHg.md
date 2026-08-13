---
video_id: _hxdz6c8bHg
title: EEVblog #696 - Apple Lisa Retro Computer Teardown
url: https://www.youtube.com/watch?v=_hxdz6c8bHg
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 61, "4": 81, "5": 101, "6": 116, "7": 141, "8": 156, "9": 176, "10": 186, "11": 201, "12": 221, "13": 241, "14": 261, "15": 276, "16": 296, "17": 311, "18": 326, "19": 341, "20": 361, "21": 381, "22": 401, "23": 416, "24": 436, "25": 451, "26": 471, "27": 496, "28": 516, "29": 536, "30": 556, "31": 571, "32": 591, "33": 616, "34": 631, "35": 646, "36": 666, "37": 681, "38": 701, "39": 721, "40": 741, "41": 756, "42": 776, "43": 791, "44": 811, "45": 831, "46": 851, "47": 866, "48": 886, "49": 901, "50": 916, "51": 931, "52": 951, "53": 966, "54": 986, "55": 1006, "56": 1021, "57": 1036, "58": 1061, "59": 1081, "60": 1096, "61": 1116, "62": 1131, "63": 1146, "64": 1166, "65": 1181, "66": 1201, "67": 1216, "68": 1241, "69": 1256, "70": 1276, "71": 1291, "72": 1311, "73": 1336, "74": 1351, "75": 1366, "76": 1381, "77": 1401, "78": 1421, "79": 1436, "80": 1456, "81": 1471, "82": 1491, "83": 1511, "84": 1531, "85": 1546, "86": 1566, "87": 1581, "88": 1601, "89": 1621, "90": 1641, "91": 1666, "92": 1681, "93": 1701, "94": 1716, "95": 1741, "96": 1761, "97": 1776, "98": 1796, "99": 1816, "100": 1831, "101": 1846, "102": 1866, "103": 1881, "104": 1896, "105": 1916, "106": 1931, "107": 1951, "108": 1966, "109": 1981, "110": 2001}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We love retro computers here on the EEVblog. Doesn't get as much retro as this little Nolan puppy. Everyone knows about the Apple Macintosh, of course, absolute classic. And, well, it's still around today. But not many people, except your

**Dave Jones:** computer aficionados, know about the Apple Lisa. And this was Apple's first graphical user interface machine. It predates the Macintosh. This one came out in January 1983. So it's over 30 years old. Fantastic. And I've got one. I think they're pretty rare here in Australia.

**Dave Jones:** They're over 100,000 made, which it was pretty much a failure. They expected to sell a lot more of these things, but unfortunately it was originally released at 10,000 US dollars. That was 1983 dollars. And just the price of it, even though the hardware and the graphical user interface and everything

**Dave Jones:** else was pretty impressive, it was just too darn expensive. So it died. What a shame. Now rumor has it this thing cost Apple about $50 million to develop, and it actually took them about 5 years to do it. They originally started developing this in around 1978, designed to be

**Dave Jones:** like the replacement for the Apple II, which of course was the killer machine of the day. And the graphical user interface technology of this, of course, comes from 1979, after Apple were allowed in to visit the park and see the Alto and their graphical user interface technology, the mouse, and everything else.

**Dave Jones:** So unfortunately I don't have a keyboard with this, and I don't have the mouse, which was an absolute killer thing for this at the time. Everyone raved about the mouse and the graphical user interface. Largely, well, the concept was stolen from Park. But hey, credit where it's due to the Apple team.

**Dave Jones:** They actually developed that. They basically developed their own graphical user interface system and, you know, bought it to commercial reality, whereas the Park hardware wasn't really commercial. It was just sort of prototyped. They never really took it to market. Now of course this was famously Steve Jobs' baby, and

**Dave Jones:** it was named after Steve Jobs' baby, Lisa. That's where the name comes from, which he finally admitted later in the game. A lot of people came up with what you know, ideas for what the acronym actually stood for, but no, it was named after

**Dave Jones:** his daughter Lisa. And it's a pretty sexy looking machine. Check it out. Just, you know, even today I think it still holds up. Obviously modern computers don't look like this, but it still is, has a sort of beautiful quality to it. I really like the design of this thing.

**Dave Jones:** Beauty. So a lot of the credit for the hardware in this thing generally goes to Wayne Rosin, who was the key architect behind the hardware in this puppy, which is what we're going to take a look at. I most likely can't get it booted.

**Dave Jones:** I don't think this thing works. As we'll see in the back here, I've already like just taken off the back panel, had a look, and it doesn't look that terrific. So yeah, I don't know. To get it back up and working, it may require significant effort.

**Dave Jones:** No idea if there's actually a hard drive in here at all. So anyway, this is Teardown Tuesday, and you know what we say here on the EEVblog, don't turn it on, take it apart! And yes, I know what all you aficionados are going to say, Dave, you're pulling a Swifty, this isn't the original

**Dave Jones:** Apple Lisa. Well, no it's not. This is actually the Lisa 2, which came out a year later, January 1984, but it's damn close to the original. The only thing they changed was that basically they changed to the Sony 400K 3.5 inch micro floppy here, because the

**Dave Jones:** original Lisa had two 5.25 inch drives, they were codenamed Twiggy. And they were apparently horribly unreliable, so they just dropped that and they had to use special disks. So apparently they were horribly unreliable drives, those Twiggy's. So it made sense to change over to the Sony micro drive,

**Dave Jones:** which was pretty much the duck's guts at the time. And if you look under the bottom here, which has room for the keyboard here, how it's all recessed in, and that is a very nice design aspect of this I really like. And it's got nothing but a big clunking power switch under there,

**Dave Jones:** you know, you can't easily hit that, very nice. And the keyboard port as well. And just for the Apple fan boys, there's the money shot. And by the way, this thing weighs a bloody ton! And on the back here we've got what looks like a reset switch, but I can't press that at all,

**Dave Jones:** it ain't working like a switch. We've got a video out, which is kind of weird considering it has video built in. We've got a parallel port, we've got our mouse port, and two serial ports as well. And it looks like it's only 120

**Dave Jones:** volt AC supply only. So yeah, I'm not going to be able to power it up without a mains transformer to drop the voltage. And it looks like we've got brightness and sync controls as well for the monitor here. So a little bit crusty.

**Dave Jones:** Another Apple logo for the fan boys. And credits also got to go to Robert Paratore as well. Apparently he worked on the hardware too, was one of the key designers of this thing. By the way, yes, it does use a Motorola 68000 processor at a screaming 5 megahertz.

**Dave Jones:** So not as fast as the original Macintosh. Now apparently these things are really sort of like modular and designed to be easily open. And apparently there's two clips on the bottom here. I haven't never tried this, but apparently you're supposed to be able to lift.

**Dave Jones:** There we go, supposed to be able to lift that out. Ah! No hard drive! Ripped off! This is where the hard drive is supposed to go. And wah wah wah wah. And there's the Sony micro floppy, and as you can see it has seen better days.

**Dave Jones:** Lots of rust and corrosion on there, and it's going to get worse when we take a look inside. This is not a prime example of an Apple Lisa unfortunately. And for those playing along at home, here is the serial number, there's an Apple number as well, and there's a manufacture date, but

**Dave Jones:** I have no idea what that means. Now one interesting feature is that here's the front panel that comes off. Got ourselves a micro switch there to detect whether or not somebody's taken off the front panel. And apparently these things would shut down if you took off the front or

**Dave Jones:** the rear panels. There's the original build plate on the bottom, it's the model number A6S0300 Made in the USA! USA! USA! And it has memory option, whatever that is. But this thing, the Apple the Lisa 2 came standard with one mega memory. Now you will see a lot of

**Dave Jones:** rust and corrosion inside this thing as we saw on the Sony floppy drive here, but all the, like all the aluminium metal work here really looks in good nick. Nothing wrong with that at all, like it just was built yesterday. Yeah, look at some of the

**Dave Jones:** corrosion on the serial port connector there, but that's not uncommon for machines of this vintage. I did get this one from near the beaches, near the northern beaches in Sydney, so yeah, not the best environment with the saltwater air. And to get the back panel off, you just do these thumb screws here and

**Dave Jones:** bingo! Bob's your uncle, we're in like Flynn, look at that! Look down here. Look at the corrosion on that card edge connector. Oh man, I haven't seen anything that bad in a long time. That is just awful. That may be like, well, I'm not going to say unrepairable, but jeez, that is pretty

**Dave Jones:** awful. Anyway, we'll have to give it a clean up and see what we can do with that, but this has bugger-all chance of working. And then we've got 4 backup batteries there. Well, they've seen better days. Ugh, yuck. And there's our 3 expansion slots there, and they're rather unusual in that they're not very deep,

**Dave Jones:** but they're as tall as the machine. So rather unusual form factor expansion cards, but it makes sense of course, given their overall system design. And there's the main ROM for this thing. And you're probably wondering, who is Sun Remarketing Inc? Well, it turns out that they were a reseller

**Dave Jones:** back in the day, and they sold Apple computers and older Apple computers as well. And they were very obviously very keen on this Lisa, and did lots of like aftermarket development for it and things like that. So maybe they've customised this ROM a little bit.

**Dave Jones:** Now I said this thing was modular, and that doesn't just extend to the front and rear panels. All of this circuitry, all this card cage, because this is just the I.O. card at the back, we're going to have the system I.O., we're going to have the processor board behind that,

**Dave Jones:** we've got a baseboard, and it's all supposed to just pull out. And that's why they've, presumably why they've got a metal bar here. And I'm going to, it's supposed to pull, it's supposed to pull out. Um, yep. Could be a bit rusty, it's giving, it's giving.

**Dave Jones:** Yep, there we go. And this is some clever, clever system design. I like that. Check it out. We've got ourselves a total of four boards, plus obviously memory boards, there's our main processor, there's the big beast 68000 up there, and plus the baseboard.

**Dave Jones:** That's a really nice designed card cage, I really love that. Thumbs up to whoever worked on that one. And just look at the attention to detail on this card cage. Look, they've gone to the effort to silkscreen the labels in here, two memory cards

**Dave Jones:** of course, the CPU and the I.O., and they've color-coded them. Brilliant. And you can see that basically nothing has changed on the Lisa 2 here. These are all using, you know, the copyright 1982 boards here, so same with the CPU one as well.

**Dave Jones:** So really essentially no difference, they just change the drives over and just sort of change the marketing spec of the thing. And it seems like this one might have the latest, in quote marks, firmware in this thing. Look, 1985. And for all you 68000 fanboys out there, here it is.

**Dave Jones:** Oh, isn't it beautiful in that huge DIP package? Socketed of course in a crappy dual-wipe contact socket. Date code, 21st week 1983. And as I said before, this board is like 1982 vintage, and there's other chips on here which are around about 83 vintage.

**Dave Jones:** So yeah, this thing was manufactured in the time that they, or around about the time that they manufactured the Lisa 1. So this is a Lisa 2, but as I said, it's basically the same machine. And you bet your arse we've got a

**Dave Jones:** 556. Awesome. And there's the crystal on it. It doesn't say what speed, but the processor operated at 5 MHz, which was much less than the first Mac, which ran at about 8 or something like that. So yeah, it was a pretty sluggish machine,

**Dave Jones:** and with its complex operating system, as fantastic as the OS wasn't groundbreaking for its time, it was just apparently very, very sluggish. And we've got ourselves a classic 4-layer board construction here, very typical of the day of course. All the chips pretty much lined up in rows, the

**Dave Jones:** top side of the board has all the traces, and most of the traces running in this direction, because this is how you routed these boards back in the day. And of course ground plane and power plane, and on the other side of course you see

**Dave Jones:** all the other traces running in this direction like this. So it was just much easier to route. It could have been routed by hand, I think it probably was, although they did have the auto-routing algorithms to actually do these boards. It was a fairly common

**Dave Jones:** task back in the day to auto-route these, but I think somebody took a bit of pride in this one and actually hand-laid that out. And the board was made in Singapore, that might have just been the bare board, it could have very well been

**Dave Jones:** stuffed, which is the technical term, it really is, in the US, I'm not sure, but yeah, probably the blank board made in Singapore. I am really concerned with the oxidization on this board, I've really got to clean this up quick smart, but yeah, it's not in great condition, let me tell you.

**Dave Jones:** We still have the odd bodge, there we go. We've got a pin there, obviously needed a cap to ground. Yeah, some sort of, just to take the edge off that sucker. We've presumably got some sort of gal or pal array under there, dead giveaway that it's got a part number on it, but

**Dave Jones:** the majority of the other chips are just, you know, off-the-shelf Jelly Bean 7.4 series. And just below the CPU there, we've got a little bit of memory, so I'm not sure what they're doing there, but anyway, most of the other chips we've got a mix of all standard 7.4 series

**Dave Jones:** Jelly Bean logic. We've got LS series chips, nicely silkscreen, of course. We've got F series, we've got ALS down here, we've got our Solesome S series logic, so that was fairly typical of the day to mix and match your logic families like that.

**Dave Jones:** Just, you know, like you use the 7.4F for the fast stuff, obviously they coupled that into the memory there, so they decided to use F, and for the lower speed stuff, in interfacing, they use LS, or they might use, you know, slightly faster ALS,

**Dave Jones:** and of course you had the decoupling spread across the board like this, there we go, a couple of axial caps, just, you know, not quite one per chip, you know, they might be sharing one per two chips in the processor, might have one up near it here, but that's about it for the decoupling,

**Dave Jones:** because this didn't run particularly fast, and also with the huge ground plane on this thing, you'd get a fair bit of capacitance between, you'd get a fair bit of distributed capacitance on the ground plane as well. That was fairly common for the day, you could pretty much

**Dave Jones:** get away with, you could probably remove half those caps, or, you know, a good majority of them, the thing would probably still work. Now back over to this IO board now, and this is pretty fancy-pantsy, look at this, you can see it's got its own ground plane,

**Dave Jones:** this is something you don't often find on here, they've got a switching regulator with a 4193 on there, there's the big-ass inductor, they've got the output filter cap for that, and that's, you know, I don't know what rail voltage they're generating there, but yeah, they obviously needed a bit more efficiency than what a

**Dave Jones:** regular regulator could provide, or maybe they're, you know, stepping it up, maybe it's a boost, I'm not even sure of the configuration there. And we've got some bodges and mod wires on here, look, running all over the place, this 74LS, couple of pins, there we go,

**Dave Jones:** absolute classic stuff, I love it. We've got another bodge cap down in here, obviously have to take the edge off that pin, and, you know, quite a few mods on here. And we've got our custom Apple COPS chip here, 1981, so pretty ancient, look at that, look at that corrosion, oh my goodness,

**Dave Jones:** is there anything left under that? Probably, I don't know, but mmmmm, colourful, crusty stuff under the switch, mmmmm, look at that, yum yum. Well there you go, that might fairly definitively date this bare board to the 21st week 84, so that's relatively late actually.

**Dave Jones:** And by the way, if you're wondering what these numbers across here and these letters, these are grid coordinates, this was fairly common back in the day, so that the service manual could go, well, replace the chip at 11D, like that, and bingo, that'd be that one.

**Dave Jones:** And if you hold it up to the light, there you go, you can actually see through that, and this is a double-sided board, there's no ground plane in there, so they saved a fair bit of cost, they didn't need it like they did on the main processor board.

**Dave Jones:** And the keyboard and parallel port controllers here, these are the 6522 VIA, the standard IO interface chip for the 6502 processor, even though this is not a 6502 processor-based machine, it's a Motorola 68000, you know, totally different architecture, still you can reuse these sort of interface chips,

**Dave Jones:** no problems at all. And the serial port up here is controlled by the Zilog 8530, so once again this was designed for the Z80, like a serial interface controller, but just like the 6502 VIAs, you can reuse these things in pretty much any processor architecture, and that's what they decided to do, they were familiar with them,

**Dave Jones:** eh, just reuse it. But they are their own individually mast-rommed processors just to handle those single tasks. And we've got ourselves a 6504 here, I'm not sure what task that one's actually running, got ourselves a GAL here, but most of the other stuff on

**Dave Jones:** here is as before, standard 7.4 series logic. And by the way, the Lisa had very advanced copy protection for its day, pretty horrendous, actually, if you think, you know, DRM is a pain in the arse these days, each machine had an individual serial number programmed into it, I'm not sure where it is, it's gotta be either

**Dave Jones:** a GAL or a ROM somewhere, but an individual serial number programmed into each machine, which would then be written onto the original software disk when you ran it for the first time. So when you got your software for the thing, you could only register

**Dave Jones:** and run it on your Lisa machine. So if you're, you know, if you replaced your hardware, eh, your software doesn't work anymore, and you couldn't sell the software or anything. So pretty horrendous, you know, I mean, if this machine actually got popular, no one would have stood for that.

**Dave Jones:** In fact, you could say it was sort of destined not to become popular, even if it was affordable, because of that horrendous digital rights management on the thing, and locking that software in on the original disks. But hey, people are clever, you know, they found ways around

**Dave Jones:** all the copy protection schemes back in the day, so I'm no doubt somebody would have found a way around this, but because it wasn't popular, I don't think anyone bothered. Does anyone know? And here are two memory boards, and they're slightly different. I mean, this one here has

**Dave Jones:** your traditional green solder mask on it, but this one here looks like, yeah, different colour, so sort of manufactured maybe in a different factory or a different time, certainly a different batch process, and the memory chips are actually different, same type, but from different

**Dave Jones:** manufacturers. And it's separated into the lower byte and the upper byte. I believe these boards are total of 500 and, well, 512k words, because it's a 16-bit machine, or one megabyte of memory. And, but that was a lot back in the day. One meg was, whoa!

**Dave Jones:** Once again, made in Singapore, looks like the 44th week 1983, this one. And still made in Singapore yet again, but much older, 39th week 84, so like a whole year difference between these two boards. So you've got to wonder, like, yeah, was this machine like a, you know, aftermarket

**Dave Jones:** upgraded or something like that? Not entirely sure. But yeah, there's a huge difference between them. So obviously not, probably not factory original boards like fitted when the machine was originally bought. And these look for all the world, like the bare board manufacturer markings here.

**Dave Jones:** So we've got ourselves Astro, so is that the name of the company that made this one? And Sanmina there, so if anyone's got any detail on those companies, but maybe they're long gone, I don't know. Well, they could be still around making boards,

**Dave Jones:** who knows? But as with all these boards in the Apple Lisa, they're all branded like the processor board, the IO board, and these boards, they're all got a date of 1982 on there, so that's when they would have been laid out. And on the older board,

**Dave Jones:** check it out, we have Apple branded MOSFET DRAMs here, these are the MK4564N-20, these are 200 nanoseconds, 64k by 1 bit. And they were manufactured 30th week, 83 by MosTech. So yeah, Apple ordered enough of these, they got their logo on them. That's common.

**Dave Jones:** And the other board from 84, these are Hitachi, these are HM4864s-3, so they're 300 nanosecond jobs. Anyway, got the little Apple logo on there and assembled in the USA. And we've got 9 of these chips per bank, look at that. So obviously we had a parity bit there, because to make up a byte,

**Dave Jones:** these are 1-bit chips, so you really only need 8 of them, but they've got a 9th one there, so that must be for parity, I'm presuming. And so each bank of those is 64k, so 6428. We've got 8 of those total, so this is actually a

**Dave Jones:** 212k board. So the total system memory on the Lisa was 1 meg, and I believe, well this Lisa 2 was sold standard with 1 meg of memory, so it would have been populated with 2 of these boards. But it was capable of going up to 2 meg, but

**Dave Jones:** I don't know if anyone ever sold boards that allowed it to be expanded up to 2 meg, at least not Apple, possibly not Apple, maybe a third party. And what's left in this card cage? Well, it's just pretty sad looking, isn't it? There's

**Dave Jones:** not much in, we've got one chip down here and a socket, and looks like we have a couple of inductors and caps in there for the mouse port, that's some RFI stuff. So, and a couple of dip switches down here for this serial, and they look really really crusty, and look at the corrosion

**Dave Jones:** on the contacts, and they are pretty colours though. And there's the Lisa expansion bus, 3 slots, and looks like we have a card ejector of some description here. And then going into the main chassis there, that looks like the video output connector, so it's just got free wires, just

**Dave Jones:** hard to see in there, it's a bit dark, but yeah, just the wires going off to the CRT in there, and then we've got ourselves the disk drive connector, and it's seen better days, the contacts, it all needs thorough cleaning as well, and that just goes off to a ribbon to the hard drive controller.

**Dave Jones:** And apparently it was pretty intelligent for the day, it would map out bad sectors and do stuff like that, I mean we take it for granted these days, but that was pretty advanced stuff back then. And once again with the nature of this thing, check it out, the power supply

**Dave Jones:** switching of course, just pops out. There we go, we've got some big high current contacts down there. Very nice, Datapower Inc. actually did that. There we go, December 20th 1984. They're in Orange County, California. Fantastic, so that's made in the US as well.

**Dave Jones:** We've got ourselves a little single-sided riser controller board here, that might have been common across different products perhaps, but it's okay, you know, for the day. Look at all the hot snot down in there. Well, it's not hot snot, it's actually celastic type stuff.

**Dave Jones:** And just holding a few of the wires down, and that's not too shabby. Look, they've got the spacers down here on the diodes, so they're lifting those off to get the air flow and the extra heat-sinking of the leads down there. So it's not too, you know,

**Dave Jones:** it's okay, it does look a bit how you're doing, but I don't mind it at all, especially for the vintage. There we go, we've got some extra heat-sinking on these diodes down here. They've put them on that plate just to heat-sink those. And a little spacer in there, they're just, it's a bit loosey-goosey,

**Dave Jones:** but it does the business. And I was wondering where the micro-switch was for the back panel, there it is there. But I'm led to believe that the Lisa has like a soft shutdown function, even the power button, which I said was a big clunking

**Dave Jones:** power switch before on the front panel, apparently it's still a soft button, and the Lisa would actually gracefully shut down and then reboot to where it was, which was pretty advanced for the day. And maybe if you removed the front and back panels, this is the back panel one, so that would interrupt the processor

**Dave Jones:** and gracefully shut the machine down. So you certainly can't power this thing up, you've got to override these switches if you want to power it up with the front or back covers off. And by the way, yes, this isn't quite the original colour, it has

**Dave Jones:** yellowed with age, which is very typical of the machines of the day, it's the bromide that was used in the plastic. And you can actually rejuvenate these things, not terribly easy, but you can rejuvenate and get that original beige colour look back. And the colour should be reasonably accurate here on the video, I have colour-balanced

**Dave Jones:** video cameras, so this is, you know, not exactly factory original colour, but very common. And unfortunately on this processor board, even after trying to clean this up, like really heavy scraping with a conductive brush and isopropanol alcohol, look, the pads are just eaten away on this

**Dave Jones:** card edge connector here, and that gunk is just caked on there, and there's just, I mean, ultimately it's repairable, but jeez, you've got to put a lot of work into fixing something like this, so unfortunately those batteries have done their business and ruined this poor innocent processor board.

**Dave Jones:** What a shame. Look what we have to deal with here, and like that's like, the rot has started on these connectors, and yeah, I think this one is beyond economical repair. That looks like a capacitor, hmm, used to be. Wow, look at that.

**Dave Jones:** And even the batteries are branded Apple, check it out. Assembled in Mexico. And you can see the rot has started setting under the water mask there, and well, yeah, that's just starting to eat away the copper under there in many places on the board like this, check it out.

**Dave Jones:** And that's only going to get worse with time unless you got in there and thoroughly stripped it all down and put in new traces, and well, yeah, this thing is pretty much gone. And here's the Sony floppy drive controller, it's called the Light Adapter, and

**Dave Jones:** there is the only Lisa logo that we've actually found inside this thing so far. There it is, silkscreened onto the board, the other boards don't have it at all. And there's not a huge amount on there, there's just some 74 series chips and a 5.068 megahertz crystal, there it is.

**Dave Jones:** And the Lisa 2 also has this extra socket here for the AMD AM9512 floating point math coprocessor, it's a 64-bit job, and it's, you know, it doesn't have a huge amount of functionality, it's only got your basic operations. But hey, a math coprocessor was not too bad in the day, but by the time this one

**Dave Jones:** was out, I think like the Intel 8087 was around and it was better and sort of, yeah, this one wasn't that popular, so it's not even fit into this, not even sure if any of the Lisa software took advantage of it. Now this is actually a Lisa 2 machine, as opposed to the

**Dave Jones:** different Lisa 2 slash 10, which had the built-in 10 meg hard drive in it, and I probably should have known that before I even opened it, because it does have the Lisa 2, had the parallel port connector on the back for connecting over to the hard drive module,

**Dave Jones:** whereas the 2 slash 10, they redesigned this motherboard and left out the parallel connector on the back. Oh, and in case you're wondering about the glorious screen, a whopping 720x360 resolution, monochrome only of course, but hey, this was actually considered a high-resolution screen back in its day, so not too bad

**Dave Jones:** at all. And at the bottom of the CRT, after you remove the main cover plate on here, we can see we've got our system speaker, and you can probably just see the part number on the tube down in there, and it's dated 11, 28th of the 11th, 03.

**Dave Jones:** And quite frankly I'm not hugely keen to take all the chassis apart just to get in there and see the CRT, but it looks like a reasonable quality board in there as you'd expect, and nice and tidy on the wiring looms and things like that, so yeah, it wasn't just slapped together how you're doing.

**Dave Jones:** So there you have it, I hope you enjoyed that look at the Apple Lisa, 1983 vintage, 31 years old or more. And it was designed in the late 70s, took them 5 years, almost 5 years to get this thing to market, absolutely incredible.

**Dave Jones:** And then it just flopped, it was, you know, it wasn't a bad machine at all. It looked the business and the GUI operating system way ahead of its time with lots of advanced memory protection features and things like that, that, you know, a lot of things didn't come around until

**Dave Jones:** a decade or more later. So really advanced machine for its time, but its price killed it. That is why the Apple Macintosh won, because it was targeted as a lower priced machine, and when it came out it was very wimpy as well. Kind of this thing

**Dave Jones:** was, the hardware was ultimately underpowered for what it was trying to do. Same with the original Macintosh but then the laser printer came out and desktop publishing and that's what sort of, you know, created the success for the Apple Macintosh, and this thing is just a footnote in

**Dave Jones:** Apple's history. But anyway, my hat's off to all the designers and software people who worked on the Apple Lisa, and ultimately a total flop, but I still like it. Doesn't it look snazzy? Look at that. Geez. I think, obviously the boards in this thing, you

**Dave Jones:** could, if you're a really keen fanboy and had a lot of time and energy on your hands, you could repair the boards and get it up and working in original condition, but who knows? Maybe I could run an emulator inside or something like that, drive the CRT directly,

**Dave Jones:** get it back working as an Apple Lisa, but maybe not using the original boards, unfortunately. I think they're probably a bit too far gone and might not be worth attempting to repair those. And obviously I can't power the thing up because it's just not going to work, it's not even worth trying, or because the

**Dave Jones:** edge connectors on the cards are eaten away and things like that. So yeah, it really requires substantial work just to get it to a bootable condition, let alone not having a hard drive in the OS and everything else. So anyway, if you've got any good ideas what I can do,

**Dave Jones:** replace the CRT and turn it into a fish tank maybe. Hmm. No, sacrilege, I'd get hate mail, death threats. Eh, what's the difference? Get those anyway. So I hope you enjoyed that. If you want to discuss it, EEVblog forum links are down below.

**Dave Jones:** And as always, if you liked Teardown Tuesday, please give it a big thumbs up, because that helps on YouTube. With the search engine algorithms and all that sort of crap. Anyway, catch you next time. Oh, there it is. Ah, look at that. Look at that.

**Dave Jones:** Thing of beauty. And for those who are curious about the famous signatures on the inside of the case, yep, they're all there. Check it out. And there, folks, is Steve Jobs. Ta-da! www.eevblog.com
