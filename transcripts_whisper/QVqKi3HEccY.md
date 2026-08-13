---
video_id: QVqKi3HEccY
title: EEVblog #458 - Industrial Computer
url: https://www.youtube.com/watch?v=QVqKi3HEccY
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 65, "4": 81, "5": 97, "6": 117, "7": 141, "8": 161, "9": 177, "10": 193, "11": 209, "12": 225, "13": 245, "14": 261, "15": 277, "16": 293, "17": 313, "18": 333, "19": 353, "20": 373, "21": 397, "22": 413, "23": 429, "24": 449, "25": 465, "26": 481, "27": 501, "28": 521, "29": 537, "30": 553, "31": 573, "32": 593, "33": 613, "34": 629, "35": 645, "36": 665, "37": 693, "38": 725, "39": 749, "40": 773, "41": 793, "42": 821, "43": 849, "44": 869, "45": 897, "46": 917, "47": 941, "48": 957, "49": 977, "50": 989, "51": 1009, "52": 1033, "53": 1057, "54": 1077, "55": 1101, "56": 1121, "57": 1133, "58": 1157, "59": 1177}
---

**Dave Jones:** And yes, it's another quick follow-up video from the all the auction stuff. Thought I'd take a look inside this ICP industrial computer, because these things bring back lots of memories. I've designed lots of production test systems, and I even believe I've specced in at one stage almost this exact

**Dave Jones:** machine, and I believe the exact motherboard if memory serves me correctly. So these are, you know, rather interesting things if you haven't seen them before. So we'll take a look inside one of these industrial computers. And this one in particular is the IEI

**Dave Jones:** Technology Corp RAC3000GB-R21 slash A130A, and they've got more options than you can poke a stick at. And there's many supplies of these industrial computers, or there were back in the day, there still are. And these things are incredibly reliable, but basically what sets them apart, they're a 90-inch standard rack of course.

**Dave Jones:** This one looks like a 5-rack unit high one. And they're full depth, because take a look at the full-length card in there, and it's still got room for a second hard drive here, plus the fans and filters we'll take a look at. This one comes with a CD driver.

**Dave Jones:** Don't know if a hard drive is installed, it's got a docking bay down there. I don't have the key, so I haven't been able to pull that out yet. But basically what defines these things are the sheer number of slots. I mean this one

**Dave Jones:** has 14 slots on it, both a combination of old school ISA of course, plus PCI, because this is the technology of the day. It's fairly old and you'll notice there's a cross brace support in here and usually the hard drives come with rubber shock mounts

**Dave Jones:** and stuff like that. I mean that might be commonplace these days on modern silent PCs and blah blah blah, but having hard drive shock and vibration mounts was quite the innovation in these industrial computers. You never got them in the old they just weren't really an option in old PCs, nobody cared

**Dave Jones:** you know, the slacked together PCs. But these industrial machines incredibly, incredibly reliable. I've had some of these working for greater than 10 years continuous and that's on the same power supply. This is an IEI branded power supply, I'm not actually sure if they do it themselves or they get

**Dave Jones:** somebody else to make it, but they're incredibly reliable. And these things work out in the factory in the dust and the crap and the temperature extremes up and down, you know, from zero in winter overnight to up to 40 degree heat in 45 degree heat in the middle of

**Dave Jones:** summer, all that sort of stuff. And all sorts of crap in the air and chemicals spilled over them and all sorts of stuff. And they are ultra-reliable. This one has two fans on the front we've got a filter down here which they do get clogged up

**Dave Jones:** a lot, you do have to replace them. And generally you don't typically get anything on the front, because they're designed to just, you know, shut up like that and not do anything. I mean this one's got a couple of power and hard drive status LEDs, some of them

**Dave Jones:** don't even have that. So you know, this one's usually, you just get a big oh, that's a momentary. It's a momentary switch. Check it out. That's not actually a proper clunking switch. So they've put a real, well it's a real clunking switch, but it's not

**Dave Jones:** actually switching the mains. So that's unusual. I don't remember having one with that before. And basically what we've got here is the main motherboard down here. Check out all the PCI slots. No, this is not the days of PCI Express, folks. This is PCI, tons

**Dave Jones:** of PCI slots. Why do you need 14 slots? Well these industrial machines typically control industrial machinery. And like, you know, I've almost fully kitted out these. You'll have, you know, multi-channel data acquisition cards, you know, National Instruments cards are pretty much standard fare in these kind of things you'll find.

**Dave Jones:** Shame I didn't get any National Instruments cards in this one. This one looks like just a serial machine. All it's got is fitted out with a couple of extra serial port cards in here, a comms card which I'll take out and we'll take the motherboard

**Dave Jones:** out and we'll have a closer look at that. We've got a bar across the top to hold the cards in, they usually hold those in with rubber mounts and stuff like that. Really quite well designed. And of course the chipset down in there is a

**Dave Jones:** PCI expansion chipset, because the standard chipset on the motherboard down in there obviously can't drive, you know, like 14 PCI slots. And by the way, yes, there is a couple of ISA slots over there. And that's what these motherboards are designed to do.

**Dave Jones:** I mean you won't find these, this configuration, in a regular PC. Like there's an ISA slot towards the rear and then there's the PCI slot here, and that's what the motherboard plugs into. The PCI comes out of here, straight into the expansion chipset, which then drives the 14

**Dave Jones:** PCI expansion slots. So that's a fairly standardized design in these industrial machines, which you won't get in the more consumer ones. So I'll press stop, I'll rip a few of the boards out, and we'll have a look at the main board. And the main board we've got in this thing is the Rocky

**Dave Jones:** 4786EV-RS-40 version 4. And that version 4's important, folks, because this board, well this series board, this Rocky series board, I remember these Rocky series boards, I've specced them in a few times myself, but there's many many variants. But this particular model board was first

**Dave Jones:** first released in 2006. And since then, they've actually, this one was version 4.0, that was version 1, and this is version 4.0 last updated in 2010 to include the Intel 865G Northbridge chip in here. They just keep updating these boards, keeping them compatible

**Dave Jones:** so that you can, you know, move your industrial stuff, keep the same chassis, replace ones in the field, stuff like that. That's the advantage with buying these industrial computers. I mean, this thing, just this one model of board, went through many changes, had a 4-year

**Dave Jones:** time frame, and they'd all be fully compatible. That's the advantage of this. I mean, you know, look, the 6-9 month churn time in the regular PC industry, I mean, 4 years for this particular model is nothing. You know, even now, you'll still be able to

**Dave Jones:** buy one, they'll still manufacture it, or if they don't sell the exact one they'll sell an upgraded version that's fully compatible, and everything else to keep your legacy systems up and running. Because as I said, you know, it wasn't uncommon for in industrial places I've worked at, to have the same machine working for 10

**Dave Jones:** years, and then even if it fails, you've still got to replace it with the same board. You don't want to replace the whole PC and the operating system. You know, we were still running Windows 3.11 for, you know, right up until just, you know, 4 years ago, or something like that.

**Dave Jones:** Absolutely crazy. So yeah, these industrial machines. This one, it's probably got like a Celeron processor in it, I don't know, haven't powered it up. I'm not going to take the heatsink off there, it'll have all the gunk on the back of it. But yeah, these things use

**Dave Jones:** prime-spec parts. I've never seen one of them fail due to a bad cap, for example. You know, I'm sure, you know, they probably do. In fact I'm sure they do eventually. But you know, even working in, you know, high-temperature industrial factories at, you know, 40 degree ambient, stuff like that, they don't

**Dave Jones:** miss a beat. They are absolutely fantastic design boards. I've got a couple of DIMM slots up here. Regular DIMM slots. Some people may not have even seen those before. Oh dear. Compact flash slot. Because often we wouldn't even have a hard drive. Sometimes you could

**Dave Jones:** boot these things from the compact flash. There were, I remember I think there were particular drivers where you could actually do that. You could boot them from the compact flash slots. And yeah, it's got ethernet built in. Whoa, look at this, that's advanced.

**Dave Jones:** Couple of SATAs down there. Whoa, so modern. Backup battery of course. And it's got a chipset to drive all the peripherals. As you can see, these are all serial cables coming out here. So it's got, you know, serial parallel, they all have parallel ports, all those legacy

**Dave Jones:** ports on them, even modern ones still made. And of course regular IDE cables, because this one has the hard drive and floppy, both IDE interface. So really fascinating boards. So this is a fairly modern one, I think it's about 2010. In fact I might try and get a

**Dave Jones:** date code on that. I've got a heatsink and bracket bar on the back there. BIOS version 2.4. Let me try and get a date code. Yeah, some of the chips down there have date codes of practically the end of 2009. So basically this is a

**Dave Jones:** 2010 vintage board. And this chipset, the PCI chipset down here, expansion chipset, that's late 2010. So yeah, this thing is like, you know, only a couple of years old. And well, it certainly looks in that good a condition, there's certainly not much in terms of

**Dave Jones:** dust or anything else in here. It's in very good nick. And then we have this 8-port serial card with the RJ11s on it. There you go. And that's from a company called the Cyclades Corporation. It's an 8YS board. There you go. A basis chipset.

**Dave Jones:** Never heard of it. But there you go. 8-port serial card. Neat. So they're obviously doing lots of serial cobs with this thing. It was its primary purpose pretty much. It didn't seem to do anything else except control, hook up to a modem and control a whole bunch of serial devices.

**Dave Jones:** And there's one thing you won't ever see on a PC motherboard. Nice big internal screw terminals, look at that. Plus minus 12 volts and 5 volts for any custom internal stuff you wanted to build into these things. And build, we certainly did! And this puppy

**Dave Jones:** has once again come from the National Measurement Institute. B-Block at Linfield, here in Sydney. There you go. Last tested, 2011. Alright, let's power it on and see what we get. Here we go. Wait. Do I have to hold that on? No. No. Whoa!

**Dave Jones:** Fail. No, there's no other power switch on the back. No. Dammit. What's going on? Let's have a look. That's all plugged into the board down there. And the power supply. Let's fire the switch. Where's the wire? Looks like it's this one here. Which comes up here.

**Dave Jones:** And goes across. Ah, here we go. So the switch doesn't go over the power supply, it goes to the motherboard. And then that PSON is labelled this wire, so this one comes out. Oh! I must have accidentally pulled that out when I was moving the card out.

**Dave Jones:** There we go, I think there's a... yeah, it's PSON is it? There it is. PSON standby. Bingo. So that controls the standby pin on the power supply. So if we plug that in, it'll probably power up. Or at least do something. Oh! Yes, look.

**Dave Jones:** Got some LEDs on the motherboard now. And, oh we did. Oh, hello. And the other thing is, these things do make a bit of a racket. The fans do have a lot of capacity. Oh, oh, oh, oh, oh, I missed it! It's booting!

**Dave Jones:** Linux! There you go. It's got Linux. Enterprise Linux. Grub. Whatever grub is, I'm sure all the penguins are going insane now. Because this sucker has Linux on it. And I think somebody mentioned that on the comments. Somebody mentioned that because the serial outs were labelled as per a Linux

**Dave Jones:** standard. So they called it. It is Linux and it's booting. And it's a Red Hat variant. So, yeah, it was labelled TTYS for all the serial. Focus. TTYS for all the serial ports. And that is apparently the Linux stuff. Checking root file system.

**Dave Jones:** Oh, 655 days without being checked. Checked forced. I've got no keyboard plugged into this thing so I guess it's just going to keep going. I have to turn it off and come back when it's done. And here we go. I think it's getting ready to do the business.

**Dave Jones:** And they certainly haven't erased the hard drive because they're measurement.gov.au. It's all still there. Nobody bothered, they just put this thing to auction without erasing the hard drive. Having a bit of lunch. I'm a bit hungry. Got to have a banana. Welcome to Kudzu.

**Dave Jones:** Ah, okay, does that mean that's like a fresh installation? I've got a mouse plugged in, I don't have a keyboard plugged in. So normal boot up will continue. Hmm. Mmm. Nice banana folks. Starting UPS model drivers. Oh, yeah, this was all tied into the UPS.

**Dave Jones:** It's trying to load the UPS drivers there and it's not going to, well it's going to load the drivers but there's no UPS attached so maybe it could take a while to time out perhaps. Oh, there we go, failed. Jeez, taking a while to boot, let me

**Dave Jones:** tell ya. Windows 3.11 used to boot like in a couple of seconds on these industrial computers. It was absolutely brilliant. And the good thing about Windows 3.11 that we were running on some machines I've worked with is that in the middle of, on these mobile

**Dave Jones:** test trolleys that went around the factory, the operators could just unplug them and you wouldn't corrupt your file system at all. Windows 3.11 was great. It just, hey, there we go, welcome to ambly.in measurement.gov.au. Username, please enter your username. Oh, I don't know, I don't have a username because I don't have a keyboard attached.

**Dave Jones:** D'oh! I want to actually repower this thing and have a look at that processor again, because we missed it. The keyboard and mouse didn't work by the way, so it looks like I have to reboot anyway, so let's give it a go and

**Dave Jones:** let's have a look. There we go, we've got an Intel Pentium 4 3 gig okay, with 500 meg, 512 meg of RAM and yeah. Not sure what the hard drive was, missed it. Alright, we're into the BIOS and it looks like we've got a

**Dave Jones:** fairly modern, I guess, 7200 RPM 250 gig hard drive. Not too bad at all, considering it's an industrial PC like this. And we've got a phoenix award BIOS, and as we saw we had a got all the chipset goodness, all the integrated peripherals, woohoo!

**Dave Jones:** PC health status. And frequency voltage control, spread spectrum. Nah, we don't want to spread the spectrum to do EMC, to pass our EMC compliance. Nah, no need to do that. But there you go, so quit without saving, yes. And we'll boot up, we've got keyboard, the mouse didn't work

**Dave Jones:** maybe it has to detect it, I don't know much about Linux. But yeah, 512 meg, and a Pentium 4 at 3 gig. So it's no slouch in terms of an industrial computer, that's for sure. So Enterprise Linux do I want EL custom or do I want standard EL?

**Dave Jones:** I don't know. EL custom sounds interesting. And presumably it will detect the mouse now when it boots up, because I plugged the mouse in before, after it's booted. We'll force... ooh. PowerPoint sound card has been removed from your system. Somebody took a do nothing.

**Dave Jones:** Sound card, do nothing. There we go, we're booting up. Alright, let's try that again. And by the way, I just looked up eBay and somebody has this exact same Rocky model card for $350 on eBay. Buy it now! Absolute bargain. So, and probably get

**Dave Jones:** someone who will, you know, need a replacement board or something and they'll probably buy it, because the board is probably like $1000 or something. I can't remember the exact prices or what they are these days, but username, I don't know, Dave. Oh, I can't even type anything!

**Dave Jones:** No, the mouse, ah, bloody mouse doesn't work, it's plugged into the USB, it didn't detect it. Bloody Linux. Type... like, the keyboard worked before! Why doesn't it work now? Unbelievable. Crap. Ah, I give up. So anyway, there you have it. There's a look at an ICP

**Dave Jones:** Electronics IEI industrial computer with the well-renowned Rocky motherboard. They're used absolutely everywhere, they're phenomenal. And this one looks to be fairly new, fairly modern, and in really good shape. I like it, so I don't know what I'm going to do with it, I don't really have a need for it, so probably go on

**Dave Jones:** eBay, I guess. Eh, unless you've got better ideas. Catch you next time.
