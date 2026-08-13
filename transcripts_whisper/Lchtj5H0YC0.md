---
video_id: Lchtj5H0YC0
title: EEVblog #1028 -  PC104 - The Full Version
url: https://www.youtube.com/watch?v=Lchtj5H0YC0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 23, "2": 52, "3": 74, "4": 94, "5": 114, "6": 133, "7": 151, "8": 170, "9": 194, "10": 219, "11": 240, "12": 263, "13": 281, "14": 295, "15": 317, "16": 343, "17": 359, "18": 380, "19": 400, "20": 423, "21": 436, "22": 460, "23": 480, "24": 498, "25": 519, "26": 535, "27": 556, "28": 574, "29": 591, "30": 608, "31": 637, "32": 653, "33": 668, "34": 682, "35": 699, "36": 715, "37": 730, "38": 743, "39": 756, "40": 771, "41": 788, "42": 804, "43": 827, "44": 843, "45": 868, "46": 890, "47": 914, "48": 932, "49": 950, "50": 972, "51": 988, "52": 1007, "53": 1027, "54": 1042, "55": 1059, "56": 1076, "57": 1091, "58": 1107, "59": 1126, "60": 1144, "61": 1167, "62": 1184, "63": 1212, "64": 1234, "65": 1251, "66": 1278, "67": 1302, "68": 1321, "69": 1336, "70": 1357, "71": 1376, "72": 1392, "73": 1410, "74": 1425, "75": 1441, "76": 1463, "77": 1480, "78": 1494, "79": 1511, "80": 1532, "81": 1554, "82": 1574, "83": 1597, "84": 1615, "85": 1637, "86": 1652, "87": 1674, "88": 1700, "89": 1722, "90": 1745, "91": 1766, "92": 1782, "93": 1809, "94": 1822, "95": 1850, "96": 1867, "97": 1885, "98": 1900, "99": 1916, "100": 1931, "101": 1950, "102": 1972, "103": 2007, "104": 2038, "105": 2056, "106": 2078, "107": 2097, "108": 2118, "109": 2152, "110": 2173, "111": 2195, "112": 2212, "113": 2230, "114": 2247, "115": 2271, "116": 2291, "117": 2307, "118": 2321, "119": 2337}
---

**Dave Jones:** Hi, if you think the Arduino, or one of its many compatible units, started the embedded computer craze with stackable boards and an industry standard form factor, or if you think, you know, Raspberry Pi is the duck's guts with its industry standard interface now,

**Dave Jones:** well, you'd be wrong. Maybe 25 years wrong. Because here is the industry standard embedded computing platform. It's called PC104. And unless you're familiar with the industrially embedded PC scene, you may not ever heard of PC104. But this standard is an industry standard, has been for 25 years now.

**Dave Jones:** In fact, it extends back to the late 80s as an industry standard footprint. And there are countless manufacturers who manufacture stackable boards like this. And you can actually get boards and just stack them on top like that, as many as you want, limited by the power supply or whatever system requirements you've got.

**Dave Jones:** And if you think they've sold a lot of Arduinos and Raspberry Pis, I think you'll find that the PC104 might have completely dwarfed the sales of those over the years, because this is the industrial PC standard. Let's take a look at it. Now, the story technically starts back in 1987 with a company called Ampro,

**Dave Jones:** and they released what was called the Ampro Little Board slash PC. And this was an early version of what was to become the PC104 standard. But before that, back in the early 80s, Ampro actually released a CPM-compatible board, which was basically a CPM single board computer.

**Dave Jones:** So if you think your Raspberry Pis and your Arduinos have pioneered this concept, you're well out of date. This thing's been going on since almost year dot of the computer revolution. And then in 1989, they released another version, which is more like the form factor that we're starting to see here.

**Dave Jones:** And then a couple of other companies started to copy the Ampro one, and then in the early 90s, about 92, a lot of companies got together and said, hey, we need to form a consortium, develop a standard for this thing, which was released as the PC104 standard,

**Dave Jones:** and then it just exploded once that standard was ratified. It wasn't ratified by the IEEE or anything else, but there was a PC104 consortium of all these large industrial embedded PC companies, and they all started to develop based on this same form factor

**Dave Jones:** of these 0.1 inch header connectors here with the stackable modules. So the PC104 standard basically defines the size of the board, which is not quite square, it's actually 96 by 90. Why that's the case, I'm not entirely sure. And it defines basically the, not only the size, but the mounting holes in here like this,

**Dave Jones:** and also the PC104 connector on the side. And this was actually 64 pins total, and it basically duplicated the functionality of the original IBM PC bus architecture. They added a few pins for, you know, some extra grounds or whatnot, but it's basically electrically identical to the IBM PC bus.

**Dave Jones:** This second one on here like this, which was an extra 40 pins, and that was equivalent to the PC80 bus, 64 plus 40, 104 pins. And that's where the name come from, PC104 standard. So they released that in 1992, so it's been 25 years since they released that standard,

**Dave Jones:** and a whole host of companies started manufacturing these PC104 compatible boards. But hey, they didn't stop there. Once PCI became a thing, they released the PCI-104 form factor board with the additional PCI, and then they added PCI Express, and they've, you know, kept pace reasonably with the interface standards,

**Dave Jones:** but they've always kept the legacy ISA bus connectors on there with all the pins that allow you to stack the boards. But apart from that, everything else on the board was up for grabs. All these connectors could all be different, and the processes could be different, memory, whatnot,

**Dave Jones:** and, you know, there were certain height requirements, you know, physical requirements and things like that. But apart from that, it was only the mounting holes, the size, and the bus that was the standard. And they were powered from 5 volts through these screw terminals here.

**Dave Jones:** Now you may have guessed by now that this is actually an IBM PC. It's a regular PC in an industrial stackable form factor. This particular board here is the iCop 6050, a company called iCop who are still going, still manufacturing these boards. This one dates from the early 2000s.

**Dave Jones:** You can see the date code there, 2002. And it's got a DMMP chipset, which is the ALIM6117. And this is an 80386SX combined chipset, so it's got an Intel 80386SX compatible processor in there, like a low-power version. It's got all the peripherals, everything else built in to the one-chip solution on there.

**Dave Jones:** It's got the AMI BIOS over here. It's got some external memory. It's got another ALIR chipset over here, presumably for IO, is it? Almost all single-sided. Got one tiny little thing over there, which is probably some TTL job they couldn't fit on the top.

**Dave Jones:** Geez, the PCB designer must have been miffed about that. Gee, you didn't leave me enough room. Anyway, and then we've got the classic M-Systems disk-on-chip. And this was an absolute game-changer. This is your old-school equivalent to your solid-state drives. You've got these days that you take for granted, and they're nothing.

**Dave Jones:** Well, this is what started it all. The M-Systems disk-on-chip and the disk-on-chip 2000, it's basically a flash drive in one single DIP chip. That's pretty much all there was to it. And these range from, I think, 16 megabytes up to 1 gig eventually,

**Dave Jones:** before they were bought out by SanDisk. So this bad boy is basically an Intel 80386 SX computer with solid-state drive on it, powered from a single 5-volt input with a 16-bit ISA bus. We've got floppy drive. We've got IDE interface and serial ports and whatnot on the thing.

**Dave Jones:** It's in keyboard and mouse and everything else. This did come in a V version, which included the video, but I didn't have that version. I've only got the non-video. So you could get all sorts of boards for this thing. And so we'll take a look at this.

**Dave Jones:** This uses the chips and technology 65545 chipset. This was just a plug-on video card that could either power a CRT output or an LCD over here. But the good thing about the PC104 standard is you could get boards for anything you wanted. If you wanted 8 or 16 serial ports for controlling all sorts of stuff back in the day, no problem.

**Dave Jones:** Just get your add-on boards. You wanted relay interfaces, isolated opto-digital interfaces, whatever it was, UEC ADCs, the whole works, you know, data acquisition systems, you could get them for the PC104 format. An entire company sprung up around just making these PC104 format boards,

**Dave Jones:** and a lot of them are still around today. This one in particular, iCop, still making them. And these things were the duck's guts, and basically still are, for embedded computers. There are other platforms around, but the PC104 standard is still going, the consortium's still there, they're still promoting it,

**Dave Jones:** companies are still manufacturing all these things, and in real industrial situations, like if you suggested using a Raspberry Pi or an Arduino or anything else, they'd just laugh at you and go, no, rubbish, give me PC104, thank you very much. And of course there's been plenty of other embedded PC platforms

**Dave Jones:** that have tried to become sort of, you know, de facto industry standards and things like that. Some of them have, there's little modular-based ones in DIMM sockets, and all sorts of weird and wonderful ones, but nothing has proven the test of time like the PC104.

**Dave Jones:** I mean, by after 25 years, still going strong. Unbelievable. But of course, modern ones have kept up with the times, they've got Intel Atom processors or whatnot, and Ethernet and wireless and all sorts of fancy-pantsy stuff will be built onto them. So, anyway, we've got this old-school 80386SX with disk-on chips,

**Dave Jones:** so I thought it'd be interesting to see if we can get this actually booted up, and still working after, what, 15, 17 years or something like that. And of course it will, these things lasted forever, they're still going. Alright, let's power this system up, shall we, and see if we can actually get it working.

**Dave Jones:** Now of course we have the manual for this one, no worries, but was not able to find the manual for the video card, so we're just going to have to suck it and see with this one, and try and get it working. So, what we're going to do is power up the processor board on its own first,

**Dave Jones:** 5 volts input, and that should be all we need, so I've got it hooked up, I've set it to 5 volts and just 1 amp current limit, it should be enough, I would guess it wouldn't take more than 5 watts, surely, from memory these are only like a couple of watts.

**Dave Jones:** So, let's power it on and see what we get. Here we go. Fingers crossed. Hello? Hello? 1.8 watts? I expect that to maybe change, yeah, 1.9, yep, yep, that's a bit, 2.3, okay, yeah, so half an amp maybe, it should be in the bias now if it's still working,

**Dave Jones:** and you'll notice that there's none of this, you know, power or status lead rubbish on this thing, no, that's just a waste of space, so no indication at all that that thing's going apart from the current consumption. So the power consumption, 2.3 watts,

**Dave Jones:** yeah, it's a bit higher on idle than, say, a modern Raspberry Pi or something like that, but for back in the day, that was pretty impressive, but a Raspberry Pi could actually take slightly more than that if it was, you know, running at full tilt,

**Dave Jones:** so, yeah, that's pretty good. Alright, so we'll switch that off now, and we'll stack our video card on, I'll keep the current limit on there, this should take another, you know, half a watt or something like that perhaps, so it may go over an amp, I'm not sure,

**Dave Jones:** but yeah, I have no idea, we've got a jumper on here which says 5 volts, 5 volts slash 3.3 volts, but there's no header on there at all, there's a header on this one over here, E1, E3, I presume that's some sort of address,

**Dave Jones:** but I think, I don't think that's for the regulator, I think that might be for maybe something external over here perhaps, so whether or not, you know, you're selecting 5 volts, I think it should just power up, that's what I'm going to do, I'm not going to bother putting a jumper on,

**Dave Jones:** let's see what happens. It's going over there, there's some plane going over there, I think I could be right on that, I think it does not power up the rest of it, we've got a fixed 3.3 volt LDO on there, so let's give that a go.

**Dave Jones:** Now of course we can choose to either stack this on the top or stack it on the bottom. The problem with the bottom is, we know this is, you know, this should be working, we've got the full manual everything for it, so I'm going to stack it on top,

**Dave Jones:** just so we have access to probe things and stuff like that while we're mucking around, trying to get at least a signal out of this video card and get it hooked up to a monitor to see the bias. Now if you've never plugged these on before,

**Dave Jones:** you don't know the force of a hundred pins like that, it is very substantial. Don't put it down like that and just press, because you can accidentally bend the long fragile pins on the bottom. So you've got to stand it upright like that,

**Dave Jones:** and gently get it in there like that, and it stands off like that. We can put the extra standoffs in there later, but you know, there's fairly good rigidity in that already, you didn't really have to put the jumpers in, certainly not just for bench evaluation and stuff like that.

**Dave Jones:** Alright, here we go, I've kept my one amp current limit. Hey, it hasn't hit five, it's more, 2.7 watts. Once again, this should increase, so it's drawing more current than before, so my hunch on that regulator was right, it didn't need that jumper.

**Dave Jones:** And, well it's going up, will it go over an amp? I don't think so, I think we're going to be safe. 3.7 odd watts, with the chips and technology video card. Awesome! I mean, that was absolutely incredible power consumption for the day, because like, your typical PC was drawing, you know,

**Dave Jones:** tens and tens of watts, even your laptops and stuff like that were, so to get an embedded platform working on just a couple of watts was really amazing stuff. We have to try and get some video out of this, and we've got our three connectors on here,

**Dave Jones:** it's not these, these are for your flat panel display, because the chips and technology 65545, for those playing along at home, could do both RGB CRT output and flat panel display. So, ta-da! This one over here must be your CRT RGB D15 output.

**Dave Jones:** And, a dead giveaway, you've got three resistors like that, they are for your RGB output impedances, and, if we have a look, we've got 2, 4, 6, 8, 10, 12, 14, coincidentally the standard VGA video connector is 15, so they've gone for 14,

**Dave Jones:** and pin 15 on a regular VGA connector is not used. Basically we only use pins 1, 2, and 3 for your RGB signals, and 14, sorry, 13 and 14 for your horizontal and vertical sync. So, my educated guess would be, if this designer was competent in the least,

**Dave Jones:** they would have made the pin-out match the pin-out for the VGA. So we'd probably go, you know, I don't know where pin 1 is, is that square up there, or is it the other one? Not entirely sure. Anyway, it should be pins like, you know, 1, 2, 3,

**Dave Jones:** and then, yeah, the 2 on the end. They should be it. So what I'm going to do is I'm going to probe just the resistors on top first, because they're easy, and see what we get. So we'll probe our resistor here. Nothing. Hello!

**Dave Jones:** Hello! There we go. Single. There's our video information. And that's, yeah, it's changing. Yeah, so that's our RGB. Well, that's one of them. It's red, green, or blue. And bingo, there's the other resistor. And there's the other one. So, if I'm right, let's...

**Dave Jones:** I think I might see a square pad in there for pin 1. So I'm going to go top pin. Hello. Yep. And because it's going to be a staggered pin configuration, the next one, well, I don't know which is pin 1. There you go.

**Dave Jones:** And pin 3. No, it's not that one. Bingo, there's your pin 3. So that one, by deduction, that one up there must be pin 1, pin 2, pin 3, and we should get nothing else on the other pins. So, by that logic, no pun intended,

**Dave Jones:** the two end pins here, 13 and 14, should be the H-sync and V-sync. Oh, hello. Hang on, we're going to... Yeah, because they'll be TTL level signals, one volt per division. So the RGB was lower, of course. Bingo. That will be our horizontal,

**Dave Jones:** because of the frequency of it, and the continuous nature, and the vertical should be a pulse like that. We got it! We're in like Flynn! So we at least have a video signal coming out of this, so I'm very confident if we just...

**Dave Jones:** Like, I don't have this connector, so I'll have to just solder some wires on the back. Maybe it could get in there with easy hooks. Oh, no. I'll just solder some wires on the back, going off to a D15, and I reckon we're going to get the bias to boot on this puppy,

**Dave Jones:** because the power consumption you saw, it went through the different stages of the power-up sequence, so that indicates that the process is working, it's going through various modes and whatnot, and then it's settled. Yeah, we can actually power that up again, and have a look,

**Dave Jones:** and you see that it starts up, it's jumping all over the place, which indicates the process is going through different various modes, and then it will eventually settle on a power figure, which should be the bias screen, because that should be fairly constant.

**Dave Jones:** There we go. That's how long it takes to boot. So, very, very confident we'll get a bias out of this. And given that I don't have a spare female D15, I decided to just chop up an existing VGA lead. I've got a bunch of these.

**Dave Jones:** If you haven't seen inside these, these are actually very well shielded, and you can get, like, crap-quality ones back in the day, and for high-resolution displays, you really needed a high-quality cable for it anyway. So they've got the outer braid like that, so that's, you know,

**Dave Jones:** in fact there's another copper one mixed in there. Anyway, got the outer braid, I've just twisted that, then encasing the whole thing, they've got the foil, so you need to peel that back as well. And inside these, you're, once again, individually shielded, because they're serious,

**Dave Jones:** that's to stop crosstalk between the two. Internally, that's your red signal, and that's your green signal, and that's your blue, conveniently color-coded, your RGB, because they're analog signals. The VGA is an analog display. And this white one here, that would be your horizontal sync,

**Dave Jones:** because that's a high frequency. So, and the rest of that, you could just buzz those out to figure out what one's what. No worries. Alright, fingers crossed, let's give that a bell, see if we get lucky. Alright, are we feeling lucky, punk? You've got to ask yourself one question.

**Dave Jones:** Do I feel lucky? Well, do you, punk? Let's give it a go. Here we go. Switching on. Come on. Come on. Ah, yes! We're in Lake Flynn! AMI BIOS, sorry, that's very, very low amplitude. There we go, had my studio lights on here.

**Dave Jones:** AMI BIOS system configuration, it's a little bit, a little bit how you're doing, because, you know, our WEF mucked up the signal integrity just a tad, but it boots no worries whatsoever. Main processor ALI-M6117, floppy drive A, 1.44 meg, screaming 40 megahertz, 640k,

**Dave Jones:** no one will ever need more than 640k, extended memory, EMS, you remember when you had to use EMS? That was, ah, those were the days. Okay, so we can fix that display. We should, because it should be the braid, so what I'm going to do is just,

**Dave Jones:** I forgot to connect up the braid, I'm going to hook the braid just up to ground here, and we should see a very significant improvement. Here we go. Ta-da! That's the difference between the shield and no shield on the signal integrity. It's just the clock recovery inside there,

**Dave Jones:** like, you know, it's just, it's all jittery as buggery, and huge difference. Look at that. The full boot sequence for those playing along at home. Ta-da! Copyright 1996. Wow. 32 meg. Wait, wait, wait. We're in. Now it came with the keyboard cable on it,

**Dave Jones:** unfortunately it's the old 5-pin DIN PS2 standard, and the only keyboard I had that had a 5-pin DIN is my old, whoops, Tandy 1000 keyboard. There it is. I've actually done a video on the Tandy 1000 PC and how I designed a turbo board

**Dave Jones:** for that back in the day, so that's a really old video. I don't think it's got a huge number of views. I'll link that one in at the end. So what I've done is hacked in a PS2 keyboard. I didn't have a PS2 keyboard,

**Dave Jones:** but luckily I found one down in the dumpster, no worries at all, and had a real hard time finding a PS2 connector for that. Hmm. Anyway, I bodged that one in. Let's power it up. Alright, so let's power this thing on. I can't remember if the AMI bias is delete or F2 or whatever.

**Dave Jones:** For the, I'll try delete and F2. I'll just press them both. Who cares? Come on. And we're in like Flynn. Ha ha! It worked. Beautiful. For those playing along at home, it was the delete key instead of F2. So we've got standard CMOS setup.

**Dave Jones:** The date's a little bit out because we don't have a battery in there, as you no doubt saw. And we can select our floppy drives. Haven't hooked up a floppy drip sector via boot sector virus protection. Love it. Ah. And our boot up sequence is okay.

**Dave Jones:** It's going from C, but we've got nothing in our disk-on-chip thing. So, yeah. The only way I can get into this, I think, is to hook up a floppy and get it running that way. Oh, geez. We just take for granted our USB ports

**Dave Jones:** and everything else these days, but I can find and hook up an old 3.5 inch floppy, no doubt. They don't work from 5 volts either, do they? Don't they need a 12 volts as well? Or is that... Oh, I don't know. I can't remember.

**Dave Jones:** It's been too long ago. And in the advanced chipset setup, this GPCS function, this is actually how we set up the M-Systems disk-on-chip. And these are the, according to the manual, these are the settings that you need. So it's all set up hunky-dory,

**Dave Jones:** but of course there's nothing on it. Well, found myself a 3.5 inch floppy drive, but I had to scrounge together an old machine to actually get a floppy drive connector in it. You might recognize this one. This is a dumpster. The XPS 420 used to use this as the live machine,

**Dave Jones:** and that was a dumpster find. So it's got a floppy connector on it. So now I've got to power this thing up, try and get this floppy drive working, and make a DOS bootable disk. I do have a DOS bootable disk somewhere, but I don't know.

**Dave Jones:** It might just be easier to do this than try to dig that out of the archives. Dammit, setting up old computers is a pain in the arse. It really is. This machine won't boot, so yeah, I think it's going to recognize a floppy,

**Dave Jones:** but I... And I couldn't find my 3.5 inch DOS boot disk at the bunker, but I found this dumpster PC, which I got, AMD Athlon X2. It's actually got a floppy drive in there, and I put one of the disks in from the...

**Dave Jones:** that came with the PC104 card, and it's just not working, so... Can't win. I'm going to have to take that out and install this floppy, which worked last time I used it, so... Unbelievable. Just trying to get these old PCs to work is just a real pain in the arse.

**Dave Jones:** Installed, and it just gets more fun. Yay. Seriously, I can't cop a break. Activate bloody Windows. There's a sticker on the side of the machine with the Vista business code on it. Doesn't work. Oh! Yes! I can read the original floppy disk that came with it.

**Dave Jones:** This is the manual. Ah, pretty sure it's the exact same one I'm downloading on the web, or maybe slightly out of date. From 2000? It's only 17 years old. It's loading from floppy. Ah, thing of beauty. It's a joy forever. Ah, driver. Interestingly, it's got DOS over here.

**Dave Jones:** And there's check disk, debug, disk copy, EMM386 for the extended memory, and all the whatnot. Wow! So what I want to do now is create an MS-DOS boot disk, because I've got tons of them somewhere, but I can't damn well find them. Just so happens, though, I've got some old 3M.

**Dave Jones:** These were the ducks guts back in the day. Um, original unused disks. I've actually got a couple of packets of these. So we whack one in there, and it's blank, of course. They came pre-formatted. Did it say? Yeah, formatted. Thank you very much.

**Dave Jones:** And we right-click on the floppy drive. Ah, even in Vista, we should be able to format, and bingo, it gives us an option to create an MS-DOS startup disk. Fantastic. Let's give it a burl. Yeah, erase everything. Let's go. Jeez, they don't give you much on it, do they?

**Dave Jones:** Tight asses. Look at the write speed on this puppy. Like a bat out of hell. Really have to get myself one of those newfangled USB three and a half inch floppies on eBay. This is ridiculous. Alright, let's try it. I've got it hooked up.

**Dave Jones:** I've got the drive powered from an external PC, because I don't want to dick around trying to do that. So let's switch her on, and see if it'll boot. Come on. You can do it. I've got the original flash disk in there at the moment.

**Dave Jones:** Because it seemed to have DOS on it. Hello? Go. Go. Oh, damn it. Aha, I think we might need the end with the swapped drive select. Let's try that one more time for the dummies. It's reading. Drive lights coming on, it's reading. X-DOS.

**Dave Jones:** X-DOS. Oh. Ah. Fatal error reading disk. Loading aborted. Wah, wah, wah, wah. That's the disk that came with it. So it actually came with the X-DOS operating system. Wow. Hands up if you use that. Designed and written by Thierry Guiron. Good on you, Thierry.

**Dave Jones:** Okay, this has got the MS-DOS boot disk. Disk IO error. I'm having no luck, but I found this in the attic. Clean boot disk DOS 6.22 with scan and TBAV. So obviously this was my boot disk from way back if I had any virus troubles.

**Dave Jones:** This one was like a guaranteed, you know, right protected version of DOS 6.22 with antivirus. I think Thunderbolt TB was Thunderbolt antivirus, I think. Stretchy. This goes way back. But let's see if this works. So let's give it a burl. It's been up in the attic though, which is not temperature controlled, so it's temperature cycled.

**Dave Jones:** So I don't like the chances of that. It's been up there for a long, long time. Especially with the Australian heat and everything. I still can't find my box of floppies. By the way, my original, I had two boxes of floppies, cannot find them.

**Dave Jones:** It's loading. Whoa! Starting MS-DOS! No disk errors yet, this is promising. We're in! We're in! New date, whatever. I don't care. New time. Are we in? We're in! The prompt! The A prompt! Yes! Finally! So we actually do have a C drive that's working, but obviously there's nothing in there.

**Dave Jones:** It's called disk on chip. Whether or not it came shipped like that, or whether or not I played around with this back in the day, I've got no idea, but it's not on there, so we need to copy the operating system, a bootable version of the operating system onto there.

**Dave Jones:** For fun, let's go into TBAV here. TB scan. There we go. Thunderbolt, yes, Thunderbolt virus detector. Who had Thunderbolt virus detector back in the day? 89-95 Thunderbolt BV. Scanning. Ah, those were the days. I just love the mix of old school prompt here with the rest of the screen overlaid in memory.

**Dave Jones:** Anyway, let's go back and let's do... Oh no, we don't have sys. Do we have sys? No, we don't have sys, because that's normally how you do that. All we've got is literally nothing else on there. It was just command.com, the boot disk.

**Dave Jones:** Oh, we need to copy over the sys file, because sys was the command that you used to transfer the operating system to another disk, and that's what we want to do. We want to copy DOS 6.22 onto the C drive. Maybe we can actually install this xDOS thing.

**Dave Jones:** This is the original disk that actually came with it, so I'm going to do... it's just got command.com. It's got those DOS files, of course. I'm going to do install and see what that does. So, because otherwise I've got to take the floppy drive to another machine,

**Dave Jones:** hook it up, transfer from USB, download the sys files from somewhere like the internet, and then, ah, it's just messy. Please boot first with the xDOS 5 to run install. And we know it doesn't boot. D'oh! Seriously, I just can't cop a break with this thing.

**Dave Jones:** Like, at every stage, I just... Murphy gets me every time. No luck whatsoever. I'll get there eventually, but, ah, now I've got to transfer the file, hook up the machine, and, ah, whatever. I'm going to damn well do this if it kills me.

**Dave Jones:** The blue screen of death when I was trying to download the DOS files from a website. Unbelievable. Finally, I'm at the point where I've got a bootable MS-DOS disk. I've got all the files on there I need, including the all-important sys, ah, slash question mark, there we go, so drive,

**Dave Jones:** and, ah, then copy from drive A to drive C. So that should work. So let's go sys, ah, drive, one specifies the location of the system files, A, and then C. Transfer the system. Please. MS-DOS 6.2 parameter not correct. Ah, sys, A, C.

**Dave Jones:** How's that? I think it likes that. Yep. Come on. Come on. Let's boot this disk on chip. System transferred! Woo! Yeah, command.com. Now let's reboot this puppy and see what happens. So I'm going to take the disk out. No longer going to boot from, ah, there, I can give it the three-finger salute.

**Dave Jones:** Ah, it should know there's no drive in A, and it should try and boot from C. So, fingers crossed. Come on. Starting MS-DOS! We're in! We're in! Ta-da! C prompt, and that was with no floppy! We did it! Winner, winner, chicken dinner! I finally got a bootable DOS 6.22 PC104 board.

**Dave Jones:** You have no idea of the amount of effort I went to. It's taken me probably like a full day's work to get this thing booted. Like, and many trips to the bunker, and back home, and up in the attic, and all sorts of places to get this damn thing working.

**Dave Jones:** There's been so many showstoppers in the way. It's just been incredible. But it boots, and the disk-on-chip from M Systems still works a treat. Awesome. Ah, I can remember when DOS 6.22 came out, and we got things like, ah, you know, and I'm not sure whether it was 6.25 from to 6 or something,

**Dave Jones:** and we got edit, and we got things like scan disk, and, ah, like, you know, Dell, probably Dell Tree was a more recent command, and, um, it, you know, we got some decent upgrades in, ah, I think from DOS, at least from DOS from 4 to 6.

**Dave Jones:** I started out with DOS 3.1 or something. Something like that, I can't recall. Hmm, anyway, copied a couple of games on there too, tiny little DOS games. Ah, I think with all this stress, I'm going to have to, ah, copy them over. I'm going to have to play...

**Dave Jones:** Ah, they're all in the one thing. Eliza. Hi, I'm Eliza, I'm your personal therapy computer. Yeah, I need it. Please tell me your problem. Old computers are hard. Do computers worry you? Yes. Are you sure? Yes. Why did you repeat yourself? I don't know.

**Dave Jones:** Don't you really know? No. Are you saying no just to be negative? Yes. I see, this is not getting very far. Now I'm running an old version of Donkey. Um, apparently this one is famous because it was actually co-written by Bill Gates himself

**Dave Jones:** to demonstrate the graphics capabilities of the early PC. Hey, what do I have to do? Oh, I've got to avoid donkeys. Hang on. Yep. Wow, this is stunning. Ah, doesn't get any better. Better. No, I can't go backwards. Spacebar to switch lanes, that's it.

**Dave Jones:** Good on you, Bill. Bill G, I should say. Because that's what he was known as. That was his internal handle at Microsoft. Ah, there you go. Winner. I tell you what, a game I really liked when I was a kid. I played this forever.

**Dave Jones:** Pango. Do you use a colour monitor? You bet your ass. Do you use a joystick? No. No. Level 1. Novice. You haven't played it in 30 years. Pango. Oh, I used to. Whoa, that's super quick. That's, yeah, that was the problem with games back in the day.

**Dave Jones:** That's why we had turbo buttons, so you could slow down the computer. Um, for these old DOS games. So, ah, it's not moving. Aw. Anyway, it always looked better than that. Maybe they had like a higher res version or something. Hmm. Welcome to Breakout.

**Dave Jones:** Whatever happened to Ken Silverman, I wonder. Good on you, Ken. Ah, look at this. Oh, I'm not quick enough. It can't, can't, can't respond quick enough. The key, the keys cannot respond quick enough to play this game. No. No kidding, I suck. So I hope you enjoyed that look at the PC-104,

**Dave Jones:** which is still a standard these days, especially in military and lots of other industrial applications. They still swear by the PC-104 standard. And it started in the late 80s. Still going what? Ah, close to 30 years later for a standard. That's pretty awesome.

**Dave Jones:** Will the Arduino be around in 30 years? Raspberry Pi? Anyone? Hmm. I don't know. But PC-104? I don't hear about it, but it's still going strong. So I hope you enjoyed that. And my struggle to get disk-on-chip working. Trust me, you didn't see the half of it.

**Dave Jones:** Wow, it's just so difficult getting these old machines up and running, unless you've got everything there, and you work on old computers all the time. I've got stuff scattered from here to Timbuktu, and, well, that was not easy at all. A bit of luck didn't go my way.

**Dave Jones:** Things screwed up, but I eventually got the thing working. So anyway, if you liked it, please give it a big thumbs up. And as always, discuss down below, and subscribe over here, and subscribe to EEVblog2 up here. I'm releasing lots of videos on EEVblog2.

**Dave Jones:** So if you're not subscribed, it'll be at the end. It's not right now, but it'll be right at the end. Subscribe to EEVblog2, because there's heaps happening over there. Anyway, catch you next time.
