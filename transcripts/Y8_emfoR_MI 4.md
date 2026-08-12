---
video_id: Y8_emfoR_MI
title: EEVblog #1288 - Synology NAS Dumpster Find! (REPAIR)
url: https://www.youtube.com/watch?v=Y8_emfoR_MI
source: youtube-asr
timestamps: {"0": 0, "1": 23, "2": 43, "3": 62, "4": 86, "5": 101, "6": 113, "7": 129, "8": 154, "9": 170, "10": 181, "11": 189, "12": 198, "13": 210, "14": 228, "15": 243, "16": 253, "17": 262, "18": 276, "19": 294, "20": 306, "21": 316, "22": 325, "23": 348, "24": 361, "25": 370, "26": 389, "27": 411, "28": 424, "29": 450, "30": 468, "31": 478, "32": 490, "33": 504, "34": 515, "35": 540, "36": 558, "37": 571, "38": 583, "39": 593, "40": 604, "41": 610, "42": 623, "43": 633, "44": 650, "45": 669, "46": 681, "47": 690, "48": 705, "49": 720, "50": 730, "51": 742, "52": 755, "53": 775, "54": 790, "55": 812, "56": 825, "57": 836, "58": 848, "59": 864, "60": 878, "61": 899, "62": 911, "63": 919, "64": 928, "65": 948, "66": 959, "67": 987, "68": 1007, "69": 1028, "70": 1037, "71": 1051, "72": 1062, "73": 1072, "74": 1085, "75": 1098, "76": 1109, "77": 1119, "78": 1134, "79": 1143, "80": 1153, "81": 1165, "82": 1182, "83": 1191, "84": 1206, "85": 1231, "86": 1243, "87": 1255, "88": 1268, "89": 1283, "90": 1294, "91": 1304, "92": 1316, "93": 1325, "94": 1340, "95": 1352, "96": 1364, "97": 1376, "98": 1388, "99": 1399}
---

**Dave Jones:** Hi, check out what I found in the dumpster. It's a Synology DS415+ four-bay NAS drive. This is absolutely fantastic. I've never found Well, I found a NAS in the dumpster before was like some old crusty thing, but this one still has the protective film on the front and it looks like it hasn't been used at all.

**Dave Jones:** There's absolutely no dust inside the fans in there. It looks like it's virtually never been Well, not used for any extended period of time at all. Unfortunately, it didn't come with the power adapter and it does need a 100 W four-pin jobby down here and they actually run about at least 80 bucks something.

**Dave Jones:** But anyway, I've already got a DS418. The power supply is the same. So, I can actually power this thing up. So, it is an older model. I believe I think it's discontinued now, but it's worth like seven You can still buy it for like seven, 800 Australian bucks.

**Dave Jones:** Absolutely brilliant. What's the catch? Well, I posted and tweeted a photo of this thing. You got to follow me on Twitter cuz that's where I post all my dumpster photos and find some that a lot of them don't even make it to a video like this one and ordinarily I wouldn't have done a video on this, but yeah, it was almost too good to be true because

**Dave Jones:** somebody on Twitter, thank you very much, pointed out that there's a famous known issue with this. It's not just Synology drives, but actually the Intel Atom C2000 processor used in this thing.

**Dave Jones:** There's a famous bug in this and we'll take a look at the details of that that actually causes thing to fail. And ironically, based on my last video, it was found in a shopping trolley.

**Dave Jones:** So, yeah. If you haven't watched that video, definitely check it out. Oh, and by the way, no, it doesn't come with any drives, but it has all the holders in it, and seriously, it looks like this thing's never been used.

**Dave Jones:** So, anyway, let's just power this sucker up with the my other power supply. Power it on. And unfortunately, it does have this known problem with this DS415+ which runs the Atom C2000 variant of the Atom C2000 processor, and the the blue power light here is not supposed to be blinking like that.

**Dave Jones:** It's supposed to be solid, and all the drive lights are not supposed to be solid orange like this. So, it looks like it has this fault, this bug that causes degradation, apparently, on the Atom CPU in this thing.

**Dave Jones:** But, rather than just toss this thing out, thought we'd have a go, cuz there is actually a fix for this thing. By the way, yes, I have put one hard drive in there, and it makes no difference.

**Dave Jones:** And that is likely why they tossed this thing out. Maybe they had it running for a little while, and it failed, because as I said, like, it's very clean.

**Dave Jones:** So, this is an indication that it's just not booting up at all. It's not going through the boot processor, and eventually, if I just leave it for a while, it will actually just switch off.

**Dave Jones:** By the way, to get this thing open is a real bugger. These two plastic clips in here, this metal frame actually goes under that, and you got to get your fingers up under there, and like, pull it out.

**Dave Jones:** And but, once you do, it does actually come apart like that, but it's not obvious. And well, inside, not a huge amount on this side. I like the extender board for all the SATA connectors, SATA and uh power, of course, and that just goes into a Focus, you bastard.

**Dave Jones:** That just plugs into a right angle connector on the main board and Bob's your uncle. So, that's really neat and tidy. Then you've got just an I/O board at the back for your ethernet and your USBs.

**Dave Jones:** But the main board is in here. That should do it. For those playing along at home, there's your backplane board. And I love using PCI connectors for board-to-board interconnects.

**Dave Jones:** I've used them for you know, test interfaces and all sorts of things over the years. They're just cheap and got tons of contacts and they're really handy and reliable.

**Dave Jones:** So, that whole board's going to lift out now except for some shielding tape on there. But apart from that, tada! We're in like Flynn. There you go. There's our main Synology processor board.

**Dave Jones:** That's going to be our culprit, the Atom processor. And once again, this is not Synology's fault. It's a systemic fault in the die of the in the design, inherently in the design of the Atom C2000 processor and all variants of it.

**Dave Jones:** So, hundreds of manufacturers would have been bitten by this Intel C2000 bug, unfortunately. Anyway, cuz this is otherwise a very nice raid drive. Well, a lot of people go, "Oh, Synology crap.

**Dave Jones:** Should have left it in the dumpster." Whatever. This looks like it's going to be fairly reliable. These electrodes here, these are all polymer ones. Probably put the kettle on.

**Dave Jones:** You can tell they're not a wet electrolyte type because they don't have your typical cross arrangement pressure vent in the top. Oh, they had to have a ton of them.

**Dave Jones:** I Two more. They're okay these days, but you know, they've they've got a reputation. Model number for those playing along at home and uh copyright 2014. Anyway, interesting that they got the firmware ROM flash up on ROM, old school, up on the uh little daughter board there.

**Dave Jones:** Would they do that for reasons of production efficiency perhaps cuz these things aren't particularly cheap. So, they're not shaving off every dollar of these things. They aren't sold into, you know, the really high volume consumer market.

**Dave Jones:** They're more business oriented, you know, like 700 bucks retail for this thing or whatever, 800 bucks Aussie. Yeah, yeah, you can afford to do that little sort of thing.

**Dave Jones:** It may cuz you can have a mass programmer for example maybe faster to actually program these off board in a big custom designed gang programmer than it is to, you know, have it do it via the USB port or whatever, you know, ethernet port or whatever.

**Dave Jones:** So, yeah, yeah, 2014 date code five plus years old, but anyway, it's like a bought one. So, according to the Intel webs, the fix is to put a 100 ohm resistor between pin one and pin six there and that's it apparently.

**Dave Jones:** So, yeah, I'm curious to know where what that's actually doing and where that goes, but yeah, I don't like the odds of being able to trace this unless we had a schematic cuz you know, this is like a eight layer board, 10 layer board, something like that.

**Dave Jones:** Pin six here, this actually buggers off over to here and there's a zero ohm jumper 356 there. I'm not sure where that goes, but also goes to this unpopulated resistor and it buggers off under here, drops down a via and I think it goes off somewhere over under the to the processor, but yeah, I'm not going to follow the money too much.

**Dave Jones:** So, it's not a huge amount we can actually glean from looking at that unfortunately unless we really spend a long time at it. Couldn't be bothered. And unfortunately, Googling doesn't find any info on the pinout for J3, what that is, or whatever.

**Dave Jones:** Um and of course, no schematics. But if you do happen to have that information, please leave it in the comments down below. Well, that's not pretty, is it? But oh, I've actually run out of 100 ohm axial resistors.

**Dave Jones:** Do you believe it? There was nothing left in my drawer. So, I had to put two 51 ohms in series. So, I We've got 102 ohms. Oh, gosh darn it.

**Dave Jones:** Well, it's not going to work now. Anyway, let's put this back together and uh pair it up and blinkety blink, but Aha! Look at this. The orange lights aren't on.

**Dave Jones:** So, I've installed one hard drive just to uh make it do something, but it's certainly changed. So, I'm going to leave that for a bit. Aha! Look at this.

**Dave Jones:** Look. Status. Blinking orange light, disk one green, solid blue. So, it just took like a minute to boot there. And winner winner chicken dinner, that has fixed it. Likely to work as a lot of people have done this uh modification, and they said, "Yep, it got it back up and running after it uh died." But there is something about apparently degradation of the chip, perhaps.

**Dave Jones:** But uh Synology have said they actually extended the warranty product and others that use the uh C2000 uh chipset and uh in full knowledge that, "Hey, these things," they reckon, "that's their engineering analysis anyway, is that uh these, you know, these chips uh don't die.

**Dave Jones:** Well, at least not for the warranty uh term that they they extended it for anyway." So, winner winner chicken dinner, there it is. Disk Station, it found a DS415 plus.

**Dave Jones:** So, we can connect into that end user license agreement. Yeah, blah blah. And we should be in like Flynn. And that is local address 192168.20.30. Your mileage may vary.

**Dave Jones:** Set up. There you go. So, yeah, it knows that we're booting this for the first time. Install the latest DSM for security fixes. DiskStation Manager. Yeah, we can install that now.

**Dave Jones:** So, all data on hard disk will be removed all in DiskStation Manager. 10 minutes. Come back. But anyway, it's it's working. It's it's fine. There's nothing wrong with it.

**Dave Jones:** So, I expect Yeah, I mean, you put in all your four disks and you set them up in whatever configuration you want. Bob's your uncle. And there you have it.

**Dave Jones:** We are good to go. System health good. Everything's uh hunky-dory. Uptime 3 minutes. It's lasted 3 minutes. It's going to last 3 years, right? Mhm. I don't know. Uh no wackers.

**Dave Jones:** And up We've got the one used drive. So, now if you want to use it, you'd put in uh your uh however configure your drives however you want. It's fine.

**Dave Jones:** So, practically a brand new DS 415 four-drive uh NAS in the dumpster. Well, it was faulty cuz it did have this uh C2000 uh Intel Atom bug, but it's fixed and it's rearing to go.

**Dave Jones:** Should I trust it? Mhm. Okay, so what I'm going to do is just uh probe the signal here on pin six. Pin two's actually ground. I'm using my uh low inductance uh probe here cuz we've actually got as you'll see a 25 meg signal.

**Dave Jones:** Look at that. And that's a bit how you're doing. That's not my probe uh doing all that funny business in there. That is uh the actual signal. So, that's that's the clock.

**Dave Jones:** There you have it. It's pretty poor stuff. And uh yeah, my probe is compensated. Everything's hunky-dory. So, it looks like they are potentially like shorting out two clocks here.

**Dave Jones:** and wow, that's got to be over the low threshold at that point. So, that's like for like your CMOS levels, I don't really like that sort of like uh porch uh so to speak in there.

**Dave Jones:** That's like a classic when you have like two signals shorted together. That's not good at all. This is after the mod, of course. Apparently, the output of the clock fails or deteriorates on uh the chip, and that's the actual uh silicon fault.

**Dave Jones:** It's a failure mode. Apparently, the output driver sort of maybe deteriorates over time due to whatever process um you know, they're they're using uh in on the die there.

**Dave Jones:** And so, that's a really awful clock. I don't like that at all, but it's working. And pin number one, it looks like it is just the rail. I couldn't uh measure that before, but it looks like yep, 1 2 3.3 V.

**Dave Jones:** So, it's pretty solid, but you can see some uh noise on that. And that's just a noise superimposed on that. So, yeah, you know, that's perfectly fine. Nothing wrong with that.

**Dave Jones:** So, they're just basically um it's a low-impedance pull-up, a 100-ohm pull-up resistor uh to the to the rail on that clock. So, it's a bit how you doing, but it does a job, and it's better than like a maybe better solution than like having to run mod wires and cut tracks and all that sort of jazz.

**Dave Jones:** Let's just check that. I pulled the resistor, so this is the original failed configuration. And uh there it is. Yeah, look at that. Wow, let me capture that. So, that's actually uh the same frequency.

**Dave Jones:** So, this is really fascinating. It's like it it's about ground there. You can see that the ground is like in the center of that waveform. So, it's almost as if like this is like an input that's picking up noise, like it's or it's a high-impedance, you know, tri-state output or something like that, or it's an output driver uh that has failed, which I think some people have

**Dave Jones:** speculated for this thing, a clock output, cuz it is coming from that 100 ohm resistor. So, but why our 25 why it comes good when we simply pull that up to 3.3 volts?

**Dave Jones:** I don't know. If that clock is coming directly from the chip and simply pulling it up, hard pulling it up with 100 ohms solves the problem, then oh man, that's dodgy as.

**Dave Jones:** Um but like I said, it works. But this If anyone knows the exact details of you know, the failure mechanism of here, and if we can hopefully get the schematic, it's rather puzzling.

**Dave Jones:** Anyway, when you pull it up, it the clock comes good. When you have no pull up, it's bad. It's not like it was originally floating. It's failed. I mean, you know, this was a working design, and it just fails because there's this known problem on the chip.

**Dave Jones:** So, the output driver is failing, but you pull it high, hard pull it high, and it works. Well, okay. So, yeah, apparently this was a big deal in February 2017, and Intel Atom C2000 bug is killing products from multiple manufacturers.

**Dave Jones:** As I said, it's nothing to do with Synology. Everyone was impacted, and the problem is the SOC, which is the system on chip, the actual C2000 processor. The LPC clock out zero and or LPC clock out one pins low that's part of the low pin count bus.

**Dave Jones:** You'd have to go into the topology of the C2000 processor to know what that is. I'm sure, you know, Intel designers out there know what I'm talking about. Anyway, it may stop functioning.

**Dave Jones:** It just may stop functioning. If the LPC clock stops functioning, the system will no longer be able to boot. It depends on how the system is designed, of course.

**Dave Jones:** Some I'm sure some systems weren't actually affected. Anyway, that was a good did India didn't tell you NDA's to squash reporting of this anyway. I I have no idea.

**Dave Jones:** Anyway, a week later Synology announced product status update and the 415 plus was one of the as of today all of our products use this component are performing in line with Synology's quality standards blah blah blah testament to our confidence in the reliability we're extending the warranty on the products utilizing this specific component by an additional year.

**Dave Jones:** So it's going to last at least a year according to Synology. Well, well. And AnandTech have a great write-up on this. I'll link all these down below for those playing along at home.

**Dave Jones:** Ryan Smith great write-up here. This was February 8th 2017. This is not a new thing but anyway, just discover things in the dumpster don't I? And it we won't go into huge details but we'll actually search the data sheet for the LPC clock out pin cuz it generates a well in this case 20 measured 25 megahertz signal that then can power other stuff inside your products and you know boot

**Dave Jones:** ROM and all sorts you know boot functionality and all sorts of things like that. Here you go. It tells you along with legacy IO devices second most common device to hang off the LPC is the boot ROM bias owing to the fact that it is a simple device that needs little bandwidth and this is where the C2000 floor truly rears its I'm going to add ugly head is that yes in this particular

**Dave Jones:** case it looks like that's how the design of the Synology NAS is happening. They're using the this low pin count bus to interface with the external boot ROM and well by doing that and tons of other manufacturers doing that it's come agata and they failed unfortunately due to some sort of degradation of the silicon.

**Dave Jones:** It's weird but it does happen. Here it is early circuit degradation and this is actually from the Intel errata from cuz they have to release errata and this is quite common.

**Dave Jones:** Go look at any complex microcontroller or CPU from any manufacturer and you'll find often pages of things that simply just don't work. Um and they they just advertise this feature and they go, "Oh, sorry.

**Dave Jones:** No, serial port two. No, that doesn't work. Sorry, in these versions of silicon. Sorry. Our bad." And here it is. Here's the specification update here and we can have a look.

**Dave Jones:** Uh February 20 It's you know, this has had lots of changes over the years, but the one we're interested in is system may experience inability to boot or may cease operation.

**Dave Jones:** You think? The system may experience inability to boot, blah blah blah. The obvious that will stop functioning no longer be able to boot. And they don't offer things why and then you can go down to the summary table to see which uh steppings of the silicon are affected.

**Dave Jones:** Number nine down here. Look, B0 and C0 steppings of the die, no fix. We we just sorry. Don't have a fix for all these things, all these problems. Sorry, we just don't have a fix.

**Dave Jones:** And this is not just an Intel thing. It happens to practically every manufacturer. These modern processors and micros are so complex and they copy them from other designs. They copy elements from it.

**Dave Jones:** And yeah, they can simulate until the cows come home and they can test their dies until the cows come home, but until it gets out there and designers use it, do we find and report bugs.

**Dave Jones:** Like I've I think I've mentioned this before. I used to pick 24F series chip once and I couldn't figure out why my serial port wasn't working working. And sure enough, I checked the latest errata for the chip and buried right down the bottom like this.

**Dave Jones:** It you know, it said something along lines of, "Oh, sorry, the serial port two just doesn't work." And on serial port one we swapped the pins. We got that we goofed that up.

**Dave Jones:** So, you know, it was like no fix and oh, here's a fix. And then I had to put mod chop up my circuit, put mod wires in to make the damn serial port work again.

**Dave Jones:** Anyway, yeah, these things happen. And of course, if you go over to the EE blog forum, it's got everything. EE blog, if you're not on the EE blog forum, seriously, it's the world's best um electronics forum.

**Dave Jones:** Absolutely, like everything's on there. And yeah, sure enough, Intel Atom C2000 fire is back in 2017, uh bison posted this and and all sorts of issues and somebody talked about um sure enough, the Synology DS415 box died um and needed to do the workaround.

**Dave Jones:** So, yeah. All right, so if you go over to the data sheet over here and we search for LPC clock out zero, there it is and frequency are 25 MHz.

**Dave Jones:** It looks like it is a fixed 25 MHz uh provided to devices requiring LPC clock. So, it's just a internal clock generated from uh the main uh processor clock, whether or not it's it's phase sync or not.

**Dave Jones:** Well, it is internal, but whether or not that's important. So, you could potentially get around this fault even if this pull-up didn't work by putting in like a little having a little mod board with your own 25 MHz oscillator and then powering and then using that to power whatever boot circuitry, ROMs, or whatever uh legacy uh bus devices you've got powered on there.

**Dave Jones:** But as I said, uh the synchronization could be a problem. So, but you could also have clock sync as well. So, it it's possible even if this pull-up uh resistor fix didn't do it.

**Dave Jones:** So, this could still potentially be fixed in products if you haven't had enough incentive to do so. You could design a little mod board. I've done videos on designing mod boards and they can you can potentially have that with a little oscillator and some uh clock sync circuitry, I would imagine.

**Dave Jones:** And then LPC host signals uh same 33 MHz. Huh? Okay, so it might be the LPC serves as a PCI to ISA bridge. Oops, sorry, my screen capture was way off there.

**Dave Jones:** I'm a dumbass Dave. Okay, yeah, professional YouTuber, sure. And it can support up to two loads here. It's a 3.3 signal. So, you know, it's obviously just like a stand-in totem pole driver output.

**Dave Jones:** Why this particular one is affected, I don't know. You'd have to talk to one of the you know, silicon designers to know exactly what's going on there. There you go.

**Dave Jones:** That's That's interesting. Fix. What should I do with this? Should I actually go out and spend 80 bucks on a power adapter and then also going to fill it up with hard drives.

**Dave Jones:** Geez, I think it to fill it up with to match my other one, I'd have to fill this up with like 8 900 dollars worth of hard drives. I've got four six gig NAS hard drives.

**Dave Jones:** I think they're Western Digital Reds or something. Um, you know, to fill that up and get a duplicate mirror drive. I can have them in different locations and back it up.

**Dave Jones:** It could be potentially be a cheaper backup solution than what I use at the moment. I actually back up my entire RAID drive to Backblaze, which is an online cloud service provider and it's all up there.

**Dave Jones:** So, you know, that's actually quite expensive to back up that amount of data. So, anyway, should I trust this thing or not? Please leave it in the comments down below.

**Dave Jones:** If you've got any experience or seen any other stories about people apply this fix and well, they've come a gutter, you know, six or 12 months later. So, I don't know.

**Dave Jones:** It's a bit dodgy, but anyway, and and if you know if Synology actually do this fix or did this fix cuz they I think they still sold this unit after they knew about this problem.

**Dave Jones:** So, and apparently they would Yeah, so you would good version of it, a fixed version. So, anyway, let us know what you think. If you enjoyed that video, please give it a big thumbs up.

**Dave Jones:** And as always, discuss it down below and over on the forum. And subscribe to my library channel. I'm By the time this video goes up, I'm probably going to hit 10,000 subscribers.

**Dave Jones:** It's insane. Catch you next time.
