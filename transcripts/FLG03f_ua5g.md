---
video_id: FLG03f_ua5g
title: EEVblog #411 - MiniPro TL866 Universal Programmer Review
url: https://www.youtube.com/watch?v=FLG03f_ua5g
source: youtube-asr
---

**Dave Jones:** Hi, I just picked this up on uh eBay. It's one of these little uh universal programmers. I got it for like 55 bucks Australian delivered. And it came with a whole bunch of adapters and uh stuff. So, I thought I'd just do a little quick

**Dave Jones:** video just uh overview of just uh trying to install and use it for the first time. And yes, of course, we'll take it apart. So, this is the Mini Pro TL866 and uh it's from a uh company called

**Dave Jones:** autolectric.cn, a Chinese company, which um seem it seems to be um specifically designed for like the automotive uh EEPROM flashing market, you know, that kind of thing where you enhance your uh car by reflashing the uh EEPROM and

**Dave Jones:** stuff like that. But, you know, it's a regular like little very compact universal programmer that, you know, they claim supports uh you know, like 13, 12, 13, 000 uh parts or something like that. It does support uh PICs and

**Dave Jones:** Atmel's and serial uh EEPROMs and flashes and old-style EEPROMs and all that sort of jazz. So, anyway, um for the price, absolutely uh amazing. And here's the box it comes in. It's rather professional. I like it. It's not like a

**Dave Jones:** you know, a lot of stuff from uh eBay Chinese sellers. You just get it wrapped in a bit of bubble wrap and thrown in an envelope. But, it rather instills a bit of confidence. It's uh designed for Windows uh 7. And there's two different

**Dave Jones:** uh models, apparently. I've got this one, the TL866CS. And I believe uh the TL866A. I didn't realize this until I actually got it. But, the um it looks like the A version actually has the um in-circuit uh serial

**Dave Jones:** programming uh port as well on it. So, mine uh mine doesn't have that. So, I don't know whether or not it's just a a connector inside or something like that. I guess we'll have to out when we open

**Dave Jones:** the thing. And for an extra couple of bucks, for like less than 10 bucks extra, I got these these little adapters. Here, fantastic. Why not, I thought, for the price. We've got a couple of PLCC packages here, 44 and a 20 and a

**Dave Jones:** 32. And we've got a couple of these little adapter boards for soldering chips directly on if you have to. You know, if you're desperate and you really need to wire it up you don't have a ZIF socket or whatever, no worries. Just solder it

**Dave Jones:** directly onto those and it came with a couple of uh different two different width SO8 packages with the ZIF socket, the proper ZIF socket. I don't know. I mean, you know, you wouldn't use this I'm sure they're not the greatest quality. You

**Dave Jones:** wouldn't use them for production programming or anything like that. But gee, you know, for yeah, I think less than 10 bucks included all those adapters. So, I thought why not? And uh the unit itself, it comes with a 40-pin

**Dave Jones:** It's supposedly it is branded 3M, but if that's a genuine 3M text tool socket, then I'm a monkey's uncle. But anyway, good enough for one of these low-quality programmers. It feels pretty good. So, let's crack it open, have a look inside,

**Dave Jones:** and after we do that, then we'll hook up the software and give it a whirl. Four screws on the bottom there. I do actually know what it looks like inside because the seller actually proudly showed off the internal circuitry and it

**Dave Jones:** looked quite compact and quite high quality. So, um here it is. Bang, we've got two board construction there. Some standard SO packages on there. We'll take a look at the parts in a minute. Standard SO23s along here uh and some protection diodes as well.

**Dave Jones:** The LEDs sticking up through the top of the board there. And it looks like the boards are uh stacked together using uh dual-way standard 0.1-in headers there. There's actually three of those by the looks of it down in there. And uh that

**Dave Jones:** looks rather quite nice. I mean, the at first glance, the soldering looks pretty good. Let's have a look on the bottom here. Aha, of course, they've shaved the shaved the number off as they do. We might be able to uh put a bit of spit on

**Dave Jones:** that later and uh try and reveal what that is. But lovely um you know, array of uh uh protection diodes down in here. Are they protection uh zeners or something? Anyway, um it looks like we've got double-sided load on both of these. And the soldering

**Dave Jones:** actually looks really quite nice. I'm uh quite quite impressed by this, especially for the price. I mean, you know, but you can get this under $50 delivered if you don't get the adapters. Uh like $45 delivered or something. Anyway, it looks like we've

**Dave Jones:** got some huge inductors here for the uh DC-to-DC supply. They look really really quite nice. I I can't separate those because I'll have to desolder that. So, no, it's not a problem. Okay, that was a little bit annoying. I had to uh

**Dave Jones:** desolder the two LEDs out of there as well. Just uh pull them out and desolder them uh from the bottom and uh was able to sort of use my third hand to crack this board uh to separate the boards while um

**Dave Jones:** desoldering those two pins. And tada! And there you go. There's all the uh switching transistors. They would be uh MOSFETs, I'd be uh assuming for each pin. I I this is um certainly not a you know, it's not like a DAC for pin uh

**Dave Jones:** universal programmer or anything like that, but it's uh it's going to be good enough. It's going to have a reasonable amount of flexibility and we should be able to check that in the uh software perhaps. And that unpopulated J1

**Dave Jones:** connector down there, obviously the uh in-circuit programming {slash} uh JTAG um port for our chip here, which uh has had the number rubbed off. The bastards, but uh we'll get a bit of spit on that in a sec.

**Dave Jones:** Zingong. Zingong. Fourth month, 2012, but I really like the construction of this thing. No problems at all. And uh of course, if you have a look down here, we've got the connector for the in-circuit serial programming. So, I'm assuming that you can just start

**Dave Jones:** solder a connector onto that. So, I might uh do that and uh maybe I don't know if I'll test the uh in-circuit programming capability today, but uh it I assume that uh that's the only difference is that the uh is that the

**Dave Jones:** actual connector is populated cuz I don't see any other missing uh parts on here unless there's like a firmware uh difference between the two or something like that. So, it's time for a bit of spit, so let me get some

**Dave Jones:** magic spit on there. And uh no, they've done a they've done a cracking job there, I think. They've done a really good job on that one. I don't know. I'm probably, you know, going to assume maybe it's a

**Dave Jones:** little arm processor or something like that that we saw in uh a universal programmer tear down a month or two back. Um but yeah, I don't know. I You could reverse engineer that, of course, uh without too much difficulty, but I won't

**Dave Jones:** bother. And all of the drivers on the uh top of the board here, 74HC373, so octal latches. So, they're driving those with a single parallel bus and then latching the individual lines for each of those. And there's another two of those on the bottom here

**Dave Jones:** as well. And they've got a 74HC164 there. Got a voltage regulator down there. That's a no surprise, a 1117 low dropout reg. And up here we've got um a There you go. Motorola 34063. Absolute classic. That's how they've got

**Dave Jones:** the cost down on this thing. They've uh Yep, there's two of those. 34063 DC-to-DC converters. So, you know, pretty cheap. So, it's not surprising that they can get um the cost down on these things cuz there's not, you know, I mean, there's a

**Dave Jones:** huge amount of uh transistors and diodes and stuff in there, but, you know, they're pretty darn cheap. Apart from that, we've got, you know, some HC series logic, some Yeah, cheapest DC-to-DC converters, and the main micro. And that's it. And the ZIF socket, of

**Dave Jones:** course. But what it's all about with these uh universal programmers is the software. So, I've whacked in the little disc here and we've got MiniPro V5807 up. I don't know what that CHM file is. So, let's run the setup program and uh

**Dave Jones:** give it a whirl. Come on. There we go. Welcome. Welcome to use MiniPro TL6866 programmer D/MiniPro. Oh, yeah. Well, install. Bam. All right, lots of Atmel files I saw there. Driver. Yeah, we'll install a driver as well. Not a problem. Install device USB

**Dave Jones:** driver. MiniPro USB driver. Yep. We'll install that. I think we're going to get a lot of Chinglish with this one, folks. I would expect a lot of Chinglish in store. Would you like to to it? Always trust. And I won't always trust, but

**Dave Jones:** yeah, I'll trust it this time. Let's go. And that only took a minute, and we're ready to use. So, let's uh call it up, MiniPro programmer. Bang, we're in. Check it out. There it is. Beautiful. Works a treat. Hasn't detected, of

**Dave Jones:** course, cuz I haven't plugged it in. So, let me do that. And we'll give it a go. See if it detects. Yeah, it detected. It's installing the uh software. Please Please reflash reflash firmware. There we go. We got some great Chinglish

**Dave Jones:** there. I love it. Please reflash firmware. Firmware, obviously. Um why it's telling us to reflash the firmware, I don't know, but uh yeah, it's telling us how to do that. We have to go up into what? Tools. Yeah,

**Dave Jones:** there we go. Reflash firmware. There we go. They've got it correct there, but uh it certainly automatically detected it. There it is, hardware interface, TL866CS. So, it's the CS, not the A version. Version 3.255. So, let's run that

**Dave Jones:** system self-check I saw up here, and please remove IC on 40-pin socket. No worries. Test. Oh, bang. Successful. Hey, look at this. Here we go. Hey. This, there you go. This is going to tell us um how many channels it's actually got.

**Dave Jones:** There we go. There's the VPP programming voltage, and that looks like it's switchable. Not through all 40 pins, of course, but it's uh switchable through 16 different pins. That means they've When when they designed this universal programmer, they

**Dave Jones:** obviously, you know, looked at the variations of the pin outs of the various chips available that they wanted to support, and determined, "Well, we need 16 different pins for the VP VPP, the programmable VPP programming voltage." So, there you go. And they've

**Dave Jones:** done a similar thing here with VCC, I'm assuming. How many channels? So, with the VCC, there we go, 24. So, you can switch the main chip power through to 24 different pins. I'm assuming and ground they would have done

**Dave Jones:** a similar thing. So, it's not a true universal programmer. But there you go, 25 pins for switching ground through. And hey, it looks like it does overcurrent protection testing. And on on the VPP and the VCC. That's That's

**Dave Jones:** really neat. Um I'm assuming that it, you know, has a transistor and it shorts out the rail and determines that the current limit is working. Neat. I like that. Beautiful. All right. Oh, I could test that all day.

**Dave Jones:** All right. So, let's have a look at the rest of the programmer here. They've got language up the top. There we go, you can switch between Chinese and Chinglish. It's not I think we're going to get a bit more

**Dave Jones:** Chinglish in here before the video is out, but it's got all the basic stuff. It's got the edit window. Can we edit that? EE? No. Oh, yeah. There we go. Yep, tells us it's read, not a problem. So,

**Dave Jones:** great. That works a treat. Okay, so we can edit the edit window and data memo, buff select, code memo, data memo, and the config fuses. There we go. There's all the config fuses for What have we got? We've got by default they

**Dave Jones:** selected a PIC 18F 4550. So, that looks That looks like it's doing the business there. I like that. All your configuration bits. So, you can go in and individually set all your configuration bits. Let's set Let's try say an Atmel one. Let's choose

**Dave Jones:** a How do we choose an I Read ID cal- calculator? Ah, just calls up Windows calculator. That's it. Um select IC, there we go. Search and select. Or you can do looks like you can do flash detect. Aha, auto flash detection. There you go.

**Dave Jones:** So, if you've got a flash memory device, eight or 16-pin, you can whack that in there and have it auto detect. Okay. That's neat, but we'll search and select. Let's look at the devices that are supported here. Or you can select

**Dave Jones:** between all ROM, flash, non-volatile RAM. They're all your manufacturers. Lots of them. I mean, a lot of them are going to use identical algorithms and stuff like that, but um MCU MPU, there we go, Atmel. The Atmel support is the AT98 AT89

**Dave Jones:** series, AT90, and it looks like pretty comprehensive list of all the ATmegas and ATtinys, and that's where it ends. Um So, let's look at uh Microchip. Here we go. It does uh so, 10 12 uh 16 and 18 series PICs, but that's pretty

**Dave Jones:** neat deal. Um PLD PLD GAL CPLD Atmel one device Lattice. Yeah, it's got a few Lattice devices in there, but nothing much. SRAM, SDRAM. Neat. But uh of course, you know, most of the time you're going to use this with uh

**Dave Jones:** EPROMs, old EPROMs or E-squared PROMs or something like that, usually. So, it supports all the usual culprits. That's quite neat. So, what I want to do there is just go into uh Atmel and just look at the configuration

**Dave Jones:** fuses. So, let's choose a you know, an ATmega 168 or something. So, let's select that and there's the code memory, data memory, and config. There you go. Nice. It all all seems to be there. Um whether or not you would trust one of

**Dave Jones:** these $50 programmers, you know, I mean, it's It's good enough, but you'd expect the odd bug, perhaps, or something like that. Um Um it's not as good as the vendor tools, of course. And if you have a look around here, there's the ICSP

**Dave Jones:** port. So, if we click on that, using ICSP interface program, make sure yeah, power supports 128 milliamps maximum. So, it looks like you can uh select So, it can generate a voltage on the ICSP port, I'm assuming, to gen

**Dave Jones:** to power your uh particular product. Um So, yeah, it's actually allowing me to do that. So, um VCC enable, you can turn the voltage off and on there. So, I'm assuming it will allow us, if we solder on that

**Dave Jones:** connector, we can probably do in-circuit serial programming, as well. Now, I've plugged in a real uh 40-pin PIC chip here. I've got a PIC 16F877 in a 40-pin DIP package, and I selected that there, 16F877. It was certainly in the library,

**Dave Jones:** and uh let's see if we can uh uh I don't know if this one's actually programmed with anything or not, but uh let's look at the configuration fuses. Can we read the uh configuration fuses at all? Let's uh

**Dave Jones:** Let's have a look. We can program it up here. We can erase it. So, we can read from the chip. We can fill it. We can verify. So, it's doing all the usual stuff, blank check, read ID. So, yeah, there we go. I just read the

**Dave Jones:** ID there, and it got chip ID um 04 D uh rev 03. I'm assuming that is the correct one. I'd have to look up the uh Microchip information to have a to actually uh verify that, but it certainly read it. And if I disconnect

**Dave Jones:** it, let me pull the chip out. Let's read the ID again. No, it's reading zero. So, if I whack it back in, and boom, put the ZIF socket down. Yep. So, it's reading that PIC chip. Not a problem at all. So, let's read it all

**Dave Jones:** in. Read from chip. Please ah Please reflash reflash the fire fire wear. Bummer. Um I wonder why out of the box it's making me reflash the firmware. So, it looks like we can't really do anything. We probably can't program it

**Dave Jones:** either until we reflash that firmware, I'm assuming. Um oh, serial number. Here we go. Ah, there we go. Auto serial number. There we go. We can do auto serial number. It does have that feature that I was talking about before. So, brilliant.

**Dave Jones:** Random serial number time mode default excellent. Ah, great stuff. Okay. Now let's reflash the firmware, shall we? I'll disconnect my uh PIC chip just in case and here we go. Fingers crossed reflash firmware. Attention, please carry on this upgrade

**Dave Jones:** operation on computer reliably. Guaranteed the computer's power supply blah blah blah blah blah. Um it's the TL866 CS. Current firmware is 3.258. Click reflash to upgrade. Doesn't tell us which version we're upgrading to, but well, here we go. Um

**Dave Jones:** reflashing fire wear. Elapsed time erasing. Okay, hope it doesn't brick it. If it bricks it, I won't be happy. I've done my 50 bucks. Reflashing the fire wear successful. Neat. Okay. Well, let's see if we can read our

**Dave Jones:** chip this time. Put my PIC back in. Read ID. Yep. Working a treat. Let's read the chip. Here we go. There we go. It's telling us to put it in. And make sure you get code memory, data memory, config fuse, user ID, and read.

**Dave Jones:** Boom. Done. That was quick and it read it all in. Not a problem. You know, I've got nothing useful to program into this, but we can just test that it verifies and stuff like that. So, let's go up to

**Dave Jones:** verify here and verify cuz it read in all of the config fuse stuff and things like that. So, yep, bang. It verified. Now, let's actually test that and go in here and modify say let's uh disable uh brownout detection there. So, let's

**Dave Jones:** disable that. And right, so I've disabled that. Now, it should not verify. It should tell us that there's an error. There you go. Bam, got it. Memory error, config. Yep, continue marked. Don't know what marked is. It works. That's a bit

**Dave Jones:** of a sanity check. Not a problem. It's got all the um you know, all the functionality you expect of a good universal programming software. I like it. So, let's uh program this PIC chip. And we've turned off the uh

**Dave Jones:** uh the brownout there. And programming elapsed time, blah blah blah. It's taking its time. I can't remember off hand what uh size this 18F877 is. Like 8K or something, 16K. It's taking a bit of time, but uh apparently this uh advertises itself as

**Dave Jones:** being fast and you can go to the um there's a chart on the eBay uh seller's page and they had like, "Oh, I can do a 4 meg flash chip in, you know, 10 seconds and stuff like that." So,

**Dave Jones:** apparently, you know, it does actually promote itself as being reasonably quick. So, but for a one-off, you know, you're not going to use this thing as a production programmer, really. I mean, you know, if you're doing critical production stuff,

**Dave Jones:** you wouldn't be using a $50 programmer, but you know, so its speed isn't that important for just one-off stuff, which most people will use it for, but yeah. No problem. Program that just fine and dandy. Now, there's one interesting thing I've

**Dave Jones:** noticed here. When I'm switching through all these uh ROM flash stuff, I don't notice any 256 K variants. They're all 128 or 512. And it just so happens that I do have an Atmel uh 27C 27C uh 128 in DIP 28 package. So, I've got

**Dave Jones:** that in the socket there. It's exactly the same. It's It's really old. It's like 1988 uh vintage. But uh I'll whack that in there and let's read. Boom. Yes, we actually got it. Okay, there we go. It read that. No problems

**Dave Jones:** at all. So, and here we go. Uh it's staring me in the face. Check device ID. There it is. So, you can just disable that. So, not a problem. If you've got an unsupported uh chip and you know it's the same pinout

**Dave Jones:** and same type and everything like that, just disable that and you shouldn't have any problems. So, verify after. There we go. And I've read in the data and I do remember kind of re- writing a sequence of data in there.

**Dave Jones:** Um this was many, many years ago when I used to sell uh EPROM programming software way, way back um when I had my own little software business. And uh yeah, it's um I believe that's the data that's still in there. I

**Dave Jones:** would have programmed that in 90 uh 93 or something like that, perhaps. But uh it's a 1988 vintage chip anyway. What I'm going to do is I'm going to fill this sucker with uh let's fill it with just random data.

**Dave Jones:** Shower value FX random. Here we go. Let's just fill the whole thing with random data. There we go. I'm going to see if I can program a 1988 vintage Atmel AT27C 128. So, let's give it a go. I like that

**Dave Jones:** Check Check this out. You can actually um change the uh VPP voltages. It looks like you can't enter them, but you can select different ones at least. So, that's so you can at least do some margin testing there. VCC verify, there

**Dave Jones:** you go. You can test it at um lower margins, lower voltage margins if you want. That's really quite nice. Pulse delay, okay, you can So, you've got a little bit of control over there over your programming information. That's pretty good. Anyway, I want to

**Dave Jones:** program this sucker. Here we go. Programming chip. Are we ready? You bet. Oh, no, of course it's not uh it's not erased. Oh! Ah, not an EPROM array. This is a freaking EPROM. But, here we go. I do have a uh blank um

**Dave Jones:** AMD uh 27C128. So, I've got that selected in there and I've already read it. It is actually blank. Read. There we go. So, it's got It looks like it's blank. Well, I could do a blank check. Here we

**Dave Jones:** go. Where's the blank check option? Blank check. There we go. Blank. Ah, no. No. Uh hang on. Device ID check, it doesn't really like that at all. Blank check. I don't know. It's the exact type, but it is empty. There you

**Dave Jones:** go. So, I'm going to try and program that sucker. So, we'll fill it with random gunk again and give it a go. I don't know. This is a uh There's no date code on that one. So, that's interesting.

**Dave Jones:** Let's pop it over over. And uh ah, 9011. There you go. So, 1990 vintage. Let's put it back in. And let's give it a go. Uh here we go. Program. And fingers crossed, don't do the device ID ID check. Bugger that off. But, will

**Dave Jones:** it program? Ah, overcurrent protection action. No external short circuit IC reverse or damaged. And uh something's going on there, folks.

**Dave Jones:** But of course I just noticed that this has 12.5 V programming voltage written on it. And by selecting that device in library it had 13.5 V. So VDD right? No, let's No, let's whack that to five. I don't I don't like

**Dave Jones:** that. Let's leave it at five. Five and five for verify and write and 12.5 for the programming voltage. Let's give that a go. Pulse delay, let's up the pulse delay. I don't know, let's double it. 200 microseconds is not going to hurt.

**Dave Jones:** So let's let's program that again. Do a blank check. Make sure it's blank. Yep, it's still blank. And let's program. Programming stop. No overcurrent protection again. Prah, fail. Now I've actually got a National Semiconductor 27C16 here. And as I noted before, there were

**Dave Jones:** no 256 options, but there are also no 27C um 16 options either. Like it's you know, regardless of the manufacturer you choose, it looks like it has 128K and 512. That is you know, that's ridiculously limiting. I don't like that

**Dave Jones:** at all. And you know, you've got I mean it's expecting now to see a 28 pin pin device in there and it's not. Crazy. So if it can't support 24 pin EPROMs, I mean they're all 28 pin. Let's

**Dave Jones:** go through them. They're all DIP 28, DIP 28. It only supports EPROMs that are 28 pin and 32 pin. Are you kidding me? All right, folks. Here we go. Hold on to your hats. I found um, the device uh

**Dave Jones:** support list. There's the URL and it does support all of, um, those uh devices which I was trying to do. Let's Let's go to AMD, for example. Look, 2716B. There's the 25 Yeah, there's a Well, there's a H256.

**Dave Jones:** But, uh, it's so it's Look, it had all these different devices which weren't in my included um, software. It's so I'm not sure if Yeah, look, TSOP44, TSOP48 DIP24. Look, all these different packages. So, there's a hell of a lot

**Dave Jones:** more devices this thing supposedly supports than what came in the software. I'm going to have to investigate this. See if there's some sort of update or something I can get. Yeah, here you go, folks. I just downloaded and installed

**Dave Jones:** the latest, uh, software. It's same version 5.80 that I was using before, I believe, but it seems to have all the device support in it. So, I don't know why the included CD didn't have it. But, look, with your find the ROM flash AMD,

**Dave Jones:** boom, here it is. Look, there's the 2716 I had before in the DIP24 that I couldn't get. And, ah, heaps more than we had before. Brilliant. And now, if I plug my, uh, 1989 vintage, uh, National Semiconductor, it's got the exact type,

**Dave Jones:** the NMC327C16Q. And, uh, yeah, I've got the the Q version. So, it's even got that in there. Fantastic. So, I can read that. Yeah, bang. Let's read. Nope. There we go. FFFFFF. It's all blank. Let's do a blank check.

**Dave Jones:** Yep, it's blank. So, let's, uh, fill this sucker up. See if we can program this one. May or may not be able to. 21 volts. These are the old 21 volts programming voltage. So, it supports these. Fantastic. I like

**Dave Jones:** it. Here we go, fingers crossed. Program. Yes, it's doing it. It's doing it. Ripper, a 1989 vintage EPROM. Well, I assume it's going to work. Ah, there you go. Beautiful. We just programmed a 23-odd 23-24-year-old um 21-V ancient EPROM. Brilliant. And let's

**Dave Jones:** verify that. Uh verify, there it is. Yep, verify finished. No problems at all. And we can read that back in. Ah. Read finished. Fantastic. I love it. There you go. Absolutely spot on. So, there you have it. There's the Auto

**Dave Jones:** Electric Mini Pro TL866CS programmer that you can get for under 50 bucks on eBay. And uh it's it's not bad at all. A few little, you know, few little niggling issues, but it seems to have quite wide uh device

**Dave Jones:** uh support. And uh the hardware's pretty decent quality. And the software does pretty much everything you'd expect. Yeah. Could do a lot more testing, but uh this just covers the basics. It does seem to work. So, I think that's pretty

**Dave Jones:** much a winner in the low the low price. And there you go, 258 yuan. Woo. You can get a Barbara Due Powerful software smooth, easy to use, cheap generic programming. Fantastic. And you can see that inside all their

**Dave Jones:** inductors are a little bit different to what we had on ours. There you go, but anyway, I think yeah, not a bad quality little programmer. It's amazing what you can get for 50 bucks these days. And uh ultra-low power

**Dave Jones:** consumption, portable super performance, best overvoltage overcurrent protections. So, it protects your devices and the programmer. Ah, and you can get it with all the those little adapters thrown in for um you know, next to nix as well. So, that's pretty impressive

**Dave Jones:** and it seems like a pretty quick programmer as well. So, anyway, worth having in your toolbox at that sort of price just in case you need to read an old EPROM or a serial EPROM or you know, hack around with products or do

**Dave Jones:** something like that or even for pick or Atmel programming. Worth a look. So, anyway, if you want to discuss it, jump on over to the EEVblog forum and I hope you enjoyed it. Catch you next time.
