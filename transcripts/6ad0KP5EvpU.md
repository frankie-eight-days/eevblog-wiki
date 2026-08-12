---
video_id: 6ad0KP5EvpU
title: EEVblog #1028 - What's All This PC/104 Stuff Anyhow?
url: https://www.youtube.com/watch?v=6ad0KP5EvpU
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 43, "3": 64, "4": 78, "5": 93, "6": 110, "7": 124, "8": 140, "9": 155, "10": 173, "11": 191, "12": 211, "13": 229, "14": 247, "15": 263, "16": 278, "17": 291, "18": 311, "19": 329, "20": 345, "21": 359, "22": 374, "23": 387, "24": 403, "25": 423, "26": 435, "27": 448, "28": 463, "29": 481, "30": 496, "31": 509, "32": 524, "33": 541, "34": 555, "35": 571, "36": 582, "37": 595, "38": 616, "39": 632, "40": 645, "41": 657, "42": 672, "43": 684, "44": 697, "45": 707, "46": 720, "47": 734, "48": 750, "49": 770, "50": 785, "51": 805, "52": 825, "53": 844, "54": 859, "55": 875, "56": 892, "57": 909, "58": 925, "59": 938, "60": 950, "61": 962, "62": 976, "63": 997, "64": 1010, "65": 1028, "66": 1046, "67": 1059, "68": 1082, "69": 1105, "70": 1118, "71": 1131, "72": 1150, "73": 1165, "74": 1180, "75": 1195, "76": 1211, "77": 1224, "78": 1244, "79": 1257, "80": 1277, "81": 1290, "82": 1306, "83": 1322, "84": 1336, "85": 1359, "86": 1372, "87": 1388, "88": 1400, "89": 1414, "90": 1428, "91": 1443, "92": 1459, "93": 1485, "94": 1508, "95": 1530, "96": 1544, "97": 1559, "98": 1580, "99": 1607, "100": 1629, "101": 1650, "102": 1665, "103": 1681, "104": 1696, "105": 1714, "106": 1735, "107": 1749, "108": 1761, "109": 1776}
---

**Dave Jones:** Hi, if you think the Arduino or one of its many compatible units started the embedded computer craze with stackable boards and an industry standard form factor or if you think you know Raspberry Pi is the dark horse with its

**Dave Jones:** four with its industry standard interface now, well, you'd be wrong. Maybe 25 years wrong because here is the industry standard embedded computing platform. It's called PC 104 and unless you're familiar with the industrial embedded PC scene, you may not ever

**Dave Jones:** heard of PC 104 but this standard is an industry standard has been for 25 years now. In fact, it extends back to the late 80s as an industry standard footprint and there are countless manufacturers who manufacture stackable boards like this

**Dave Jones:** and you can actually get boards and just stack them on top like that as many as you want limited by the power supply or whatever system requirements you've got. And if you think they've sold a lot of Arduinos and Raspberry Pis, I think

**Dave Jones:** you'll find that the PC 104 might have completely dwarfed the sales of those over the years because this is the industrial PC standard. Let's take a look at it. Now, the story technically starts back in 1987 with a company

**Dave Jones:** called Ampro and they released what was called the Ampro Little Board/PC and this was an early version of what was to become the PC 104 standard. But before that, back in the early 80s, Ampro actually released a CPM compatible

**Dave Jones:** board which was basically a CPM single board computer. So, if you think your Raspberry Pis and your Arduinos have pioneered this concept, you're well out of date. This thing's been going on since almost year dot of the computer

**Dave Jones:** revolution. And then in 1989, they released another version which is more like the form factor that we're starting to see here. And then a couple of other companies started to copy the Ampro one. And then in the early '90s, about '92, a

**Dave Jones:** lot of companies got together and said, "Hey, we need to form a consortium, develop a standard for this thing." Which was released as the PC 104 standard. And then it it just exploded once that standard was It wasn't

**Dave Jones:** ratified by the IEEE or anything else, but it was There was a PC 104 consortium of all these large industrial embedded PC companies. And they all started to develop based on this same form factor of these 0.1 in

**Dave Jones:** header connectors here with modules. So, the PC 104 standard basically defines the size of the board, which is not quite square. It's actually 96 by 90. Why that's the case, I'm not entirely sure. And it defines basically the not only

**Dave Jones:** the size, but the mounting holes in here like this. And also the PC 104 connector on the side. And this was actually 64 pins total. And it basically duplicated the functionality of the original IBM PC bus architecture. They added a few

**Dave Jones:** pins for, you know, some extra grounds or whatnot. But it's basically electrically identical to the IBM PC bus. This second one on here like this, which was an extra 40 pins. And that was equivalent to the PC AT bus. 64 plus 40,

**Dave Jones:** 104 pins. And that's where the name come from, PC-104 standard. So, they released that in 1992, so it's been 25 years since they released that standard, and a whole host of companies started manufacturing these these PC-104 compatible boards. But,

**Dave Jones:** hey, they didn't stop there. Once PCI became a thing, they were like released the PCI-104 form factor board with the additional PCI, and then they added PCI Express, and they've you know reason kept pace reasonably with the interface standards,

**Dave Jones:** but they've always kept the legacy ISA bus connectors on there with all the pins that allow you to stack the boards. But, apart from that, everything else on the board was up for grabs. All these connectors could all be different, and

**Dave Jones:** the processors could be different, memory, whatnot, and you know, there were certain height requirements, you know, physical requirements and things like that, but apart from that, it was only the mounting holes, the size, and the bus that was the standard. And they

**Dave Jones:** were powered from 5 volts through these screw terminals here. Now, you may have guessed by now that this is actually an IBM PC. It's a regular PC in an industrial stackable form factor. This particular board here is the iCop 6050, a company

**Dave Jones:** called iCop who are still going, still manufacturing these boards. This one dates from the early 2000s. You can see the date code there, 2002. And it's got a DMMP chipset, which is the ALi M6117. And this is an 80386

**Dave Jones:** SX combined chipset, so it's got an Intel 80386 SX compatible processor in there, like a low-power version. It's got all the peripherals, everything else built in to the one-chip solution on there. It's got the AMI BIOS over here.

**Dave Jones:** It's got some external memory. It's got an another ALI uh chipset over here, presumably for IO, is it? Almost all single-sided. Got one tiny little thing over there, which is probably some uh TTL job they couldn't fit on the top.

**Dave Jones:** Geez, the PC/104 designer must have been miffed about that. Um geez, you didn't leave me enough room. Anyway, um and then we've got the classic M-Systems disk on chip. And this was an absolute game-changer. This is your uh old-school

**Dave Jones:** equivalent to your solid-state drives you've got these days that you take for granted and they're nothing. Well, this is what started it all. That the M-Systems disk on chip and the disk on chip uh 2000, it's basically a uh flash

**Dave Jones:** drive in one single DIP chip. That's all they pretty much all there was to it. And uh these range from uh I think 16 MB um up to 1 gig eventually before they were bought out by uh Sandisk. So, this

**Dave Jones:** bad boy is basically an Intel 80386 SX uh computer with solid-state drive on it, powered from a single 5-V input with a 16-bit ISA bus. We've got uh floppy drive. We've got IDE interface and uh serial ports and whatnot on the thing.

**Dave Jones:** What's in keyboard and mouse and everything else. This did come in a V version, which included the video, but I didn't have that version. I've only got the non-video. So, you could get all sorts of boards for this thing. And so,

**Dave Jones:** we'll take a look at this. This is the uh uses the Chips and Technologies 65545 uh chipset. This was just a plug-on video card that could either power a uh CRT output or an LCD over here. But the

**Dave Jones:** good thing about the PC/104 standard is you could get boards for anything you wanted. If you wanted eight or 16 serial ports um for controlling all sorts of stuff back in the day, no problem. Just get your add-on boards. You wanted relay

**Dave Jones:** interfaces, isolated opto-digital interfaces, whatever it was, you ADCs, the whole works, you know, data acquisition systems, you could get them for the PC/104 format. An entire company sprung up around just making these PC/104 format boards, and a lot of them

**Dave Jones:** are still around today. This one, in particular, ICOP, still making them. And these things were the ducks guts, and basically still are for embedded computers. There are other platforms around, but the PC/104 standard is still going. The consortium

**Dave Jones:** is still there. They're still promoting it. Companies are still manufacturing all these things, and in real industrial situations, like if you suggested using a Raspberry Pi or an Arduino or anything else, they'd just laugh at you and go,

**Dave Jones:** "No. Rubbish. Give me PC/104, thank you very much." And of course, there's been plenty of other embedded PC platforms that have tried to become sort of, you know, de facto industry standards and things like that. Some of them have. There's little

**Dave Jones:** modular base ones in DIMM sockets and all sorts of weird and wonderful ones, but nothing has proven the test of time like the PC/104. I mean, they after 25 years, still going strong. But of course, modern ones have

**Dave Jones:** kept up with the times. They've got Intel Atom processors or whatnot, and Ethernet and wireless and all sorts of fancy pantsy stuff will be built onto them. Anyway, we've got this old school 80386SX with disk on chip. So, I thought

**Dave Jones:** it'd be interesting to see if we can get this actually booted up and still working after what, 15, 17 years or something like that. Of course, it will. These things lasted forever. They're still going. Now, of course, we have the manual for this one,

**Dave Jones:** no worries, but was not able to find the manual for the video card. So, we're just going to have to suck it and see with this one and uh uh so, what we're going to do is pair up the processor

**Dave Jones:** board on its own first. Uh 5 V input, 5 V and just 1 amp current limit. Um it should be enough. Wouldn't take more than 5 W surely. Uh from memory, these are only like a couple of watts. Fingers

**Dave Jones:** crossed. Hello. Hello. 1.8 W I expect that to maybe be changing. Yeah, 1.9. Yeah, 2.3. Okay. So, half an amp maybe. It should be in the bias now if it's uh still working. And you'll notice that there's none of this, you know, power or

**Dave Jones:** status LED rubbish on this thing. Nah, that's just a waste of space. So, um yeah, no indication at all that that thing's going apart from the current consumption. So, the power consumption 2.3 W. Yeah, it's a bit higher on idle

**Dave Jones:** than say a modern Raspberry Pi or something like that. But, for back in the day, that was pretty impressive. All right, so we'll switch that off now and we'll stack our video card on. I'll keep the current limit on there. This should

**Dave Jones:** take another, you know, half a watt or something like that perhaps. Got a jumper on here which says 5 V / 3.3 V, but there's no header on there at all. There's a header on this one over here,

**Dave Jones:** E1 E3. I presume that's some sort of address. Um but, I think I don't think that's for the regulator. I think that might be for maybe something external over here perhaps. It should just power up. That's what I'm going to do. I'm not going to

**Dave Jones:** bother putting a jumper on. Let's see what happen. It's going over there. There's some plane going over there. I think I could be right on that. Now, of course, we can choose to either stack this on the top or stack it on the

**Dave Jones:** bottom. The problem with the bottom is we know this is, you know, this should be working. We've got the full manual, everything for it. Um so, I'm going to stack it on top just so we have access to our probe things and stuff like that

**Dave Jones:** while we're mucking around trying to get at least a signal out of this video card and get it hooked up to a monitor. Now, if you've never plugged these on before, you don't know the force of a hundred

**Dave Jones:** pins uh like that. It is very substantial. Don't put it down like that and just press because you can accidentally bend uh the long fragile pins on the bottom. So, you've got to stand it upright like that and

**Dave Jones:** gently uh get it in there like that and it stands off like that. We can put the extra standoffs in there later, but you know, there's fairly good rigidity in that already. You didn't really have to put the jumpers in. Certainly not just

**Dave Jones:** for bench evaluation and stuff like that. All right, here we go. I've kept my 1 amp current limit. Hey, it has five. It's more 2.7 watts. Once again, this should increase. So, it's drawing more current than before. So, my hunch on that regulator was

**Dave Jones:** right. It didn't need that jumper. 3.7 odd watts with the Chips and Technologies video card. Awesome. I mean, that was absolutely incredible power consumption for the day because like your typical PC was drawing, you know, tens and tens of

**Dave Jones:** watts. Even your laptops and stuff like that were. So, to get an embedded platform working on just a couple of watts was really amazing stuff. Now, we have to try and get some video out of this and we've got our three connectors on here.

**Dave Jones:** It's not these. These are for your flat panel display because the Chips and Technologies 65545, for those playing along at home, could do both RGB CRT output and flat panel display. So, tada, this one over here must be

**Dave Jones:** your CRT RGB. And a dead giveaway. You've got three resistors like that. They're They are for your R, G, and V output impedances. And if we have a look, 14, coincidentally, the standard VGA video connector is 15. So, they've

**Dave Jones:** gone for 14 and pin 15 on a regular VGA connector is not used. Basically, we only use pins 1, 2, and 3 for your RGB signals and four Sorry, 13 and 14 for your horizontal and vertical sync. So,

**Dave Jones:** my educated guess would be if this designer was competent in the least, they would have made the pinout match the pinout for the VGA. But, you know, 1, 2, 3, and then four Yeah, the two on the end. They

**Dave Jones:** should be it. So, what I'm going to do is I'm going to probe the just the resistors on top first cuz they're easy and see what we get. Hello. Hello. There we go. Single. There's our video information. And yeah, so that's our

**Dave Jones:** RGB. Well, that's one of them. It's a red, green, or blue. And bingo, there's the other resistor. And there's the other one. So, if I'm right, hello. Yep. And because it's going to be a staggered pin configuration, there you go. And pin

**Dave Jones:** three, bingo. So, by that logic, huh, no pun intended, the two end pins here, 13 and 14, should be the H sync and V sync. Oh, hello. Because they'll be TTL level signals, 1 V per division. So, the RGB

**Dave Jones:** was lower, of course. Bingo. That will be our horizontal because of the frequency of it and the continuous nature. And the vertical should be a pulse like that. We got it. We're in like Flynn. So, we at least

**Dave Jones:** have a video signal coming out of this. I'll just solder some wires on the back going off to a D15, and I reckon we're going to get the BIOS to boot on this puppy because the power consumption you

**Dave Jones:** saw it went through the different stages. Have a look, and you see that it it starts up. It's jumping all over the place, which indicates the processor is going through different various modes, and then it will eventually settle on

**Dave Jones:** power figure, which should be the BIOS uh screen. I decided to just chop up an existing VGA lead. I've got a bunch of these. If you haven't seen inside these, these are actually uh very well shielded, and you can get like crap

**Dave Jones:** quality ones back in the day, and for high resolution uh displays, you really needed a high-quality uh cable for it anyway. So, they've got the outer uh braid, then encasing the whole thing, they've got the uh foil, and inside

**Dave Jones:** these are, once again, individually shielded cuz they're serious. That's to stop uh crosstalk between the two internally. That's your red signal. That's your green signal, and that's your blue, conveniently color-coded your RGB uh because they they're analog signals. The VGA is an analog uh

**Dave Jones:** display. And this white one here, that would be your uh horizontal sync cuz that's a high frequency. And the rest of that, uh you can just uh buzz those out to figure out what one's what. No worries. All right, fingers crossed.

**Dave Jones:** Let's give that a whirl. See if we get lucky. All right, are we feeling lucky, punk? You've got to ask yourself one question. Do I feel lucky? Well, do you, punk? Switching on. Uh Yes! We're in like Flynn. A little bit,

**Dave Jones:** how you doing because uh you know, we've mucked up the signal integrity just a tad, but it boots, no worries whatsoever. Main processor ALI M 6117, screaming 40 MHz 640K. No one will ever need more than 640K. EMS, you remember

**Dave Jones:** when you had to use EMS? That was uh those were the days. Okay, so we can fix that uh display. This should be the braid. So, what I'm going to do is just um forgot to connect up the braid. So, I'm

**Dave Jones:** going to hook the braid just up to ground here and we should see a very significant improvement. Ta-da! That's the difference between the shield and no shield on the signal integrity. It's just the clock recovery inside there. It's all jittery as

**Dave Jones:** buggery. Full boot sequence for those playing along at home. Ta-da! Copyright 1996. Wow! 32 meg. Wait. Wait. Wait. We're in. Now, it came with the uh keyboard cable on it. Unfortunately, it's the old five-pin DIN PS/2 standard. And the only keyboard I had that had a

**Dave Jones:** five-pin DIN is my old Tandy 1000 keyboard. I've actually done a video on the Tandy 1000 PC and how I uh designed a turbo board uh for that back in the day. So, that's a really old video. I

**Dave Jones:** don't think it's got a huge number of views. I'll link that one in at the end. So, what I've done is hacked in a PS/2 keyboard. I didn't have a PS/2 keyboard, but luckily I found one down in the

**Dave Jones:** dumpster. Uh no worries at all. And had a real hard time finding a PS/2 connector for that. Anyway, I bodged that one in. Let's power it up. And we're IN LIKE FLYNN. HAHA, it worked. Beautiful. So, we've got standard CMOS set up. The uh date's

**Dave Jones:** a little bit out because we don't have a battery in there. Boot sector virus protection. Love it. Uh and our boot up sequence is okay. It's going from uh C, but we've got nothing in our disk-on-chip. We just take for granted

**Dave Jones:** our, you know, USB ports and everything else these days, but I got to find and hook up an old 3 1/2-in floppy. And in the advanced chipset setup, this GPCS function, this is actually uh how we set up the um M-Systems disk-on-chip.

**Dave Jones:** And these are the, according to the manual, these are the settings that you need. So, it's all set up hunky-dory, but of course, there's nothing on it. Well, found myself a 3 1/2-in uh floppy drive, but uh I had to scrounge together

**Dave Jones:** an old machine to actually uh get a floppy drive connector in it. You might recognize this one. This is a uh dumpster the XPS uh 420. Used to use this as the uh live the lab uh live machine. Uh and make a DOS-bootable

**Dave Jones:** disk. I do have a DOS-bootable disk somewhere, but um I I don't know. Might just be easier to do this than try to dig that out of the archives. Damn it. Setting up old computers is a pain in the ass. It

**Dave Jones:** really is. Look at the write speed on this puppy. Like a bat out of hell. Really have to get myself one of those newfangled USB 3 1/2-in floppies on eBay. I just This is ridiculous. All right, let's try

**Dave Jones:** it. I've got it hooked up. I've got the uh drive powered from an external PC cuz I don't want to uh dick around trying to do that. So, let's switch her on. It's reading. Drive light's coming on. IT'S READING.

**Dave Jones:** X-DOS. X-DA OH. OH. Fatal error reading disk. Loading aborted. What what what what? That's the disk that came with it. So, it actually came with the X DOS operating system. Wow. Hands up if you use that. Designed and

**Dave Jones:** written by Thierry Giron. Good on you, Thierry. Okay, this has got the MS-DOS boot disk disk IO error.

**Dave Jones:** I'm having no luck, but I found this in the attic. Clean boot disk DOS 6.22 with scan and TBAV. So, obviously this was my boot disk from way back if I had any virus troubles. This one was like a

**Dave Jones:** guaranteed, you know, write protected version of DOS 6.22 with antivirus. I think Thunderbolt. Let's give it a whirl. It's been up in the attic though, which is not temperature controlled, so it's temperature cycled. So, I don't like the

**Dave Jones:** chances of that. It's been up there for a long long time. Especially with the Australian heat and everything. I still can't find my box of floppies, by the way. My original I had two boxes of floppies, cannot find them. IT'S

**Dave Jones:** LOADING. WOW! STARTING MS-DOS. No no disk errors yet. This is promising. We're in. We're in. New date. Whatever. I don't care. New time. Are we in? We're in. The prompt. The A prompt. Yes! Finally. So, we actually do have a

**Dave Jones:** C drive that's working, but obviously there's nothing in there. It's called disk on chip, so we need to copy the operating system a bootable version of the operating system onto there. For fun, let's go into TBAV here. So, who

**Dave Jones:** had Thunderbolt the virus detector back in the day? 89 to 95. Those were the days. And I just love the mix of old school prompt here with the rest of the screen overlaid in memory. Anyway, do we have sys? No, we don't

**Dave Jones:** have sys cuz that's normally how you uh do that. All we've got is literally nothing else on there. It was just command.com cuz sys was the command that you use to transfer the operating system to another disk. And that's what we want

**Dave Jones:** to do. We want to copy sys 6.22 onto the C drive. Maybe we can actually install this XDOS thing. It This is the original disk that actually came with it. So, I'm going to do it's just got command.com.

**Dave Jones:** It's got those DOS files, of course. I'm going to do install and see what that does. So, cuz otherwise we've got to take the floppy drive to another machine, hook it up, transfer from USB, download the sys files from somewhere like the internet,

**Dave Jones:** and then uh it's just messy. Please boot first with the XDOS 5 to run install. And we know it doesn't boot. Oh, finally, I'm at the point where I've got a bootable MS-DOS disk. I've got all the files on

**Dave Jones:** there I need, including the all-important sys / question mark. There we go. So, drive and uh then copy from drive A to drive C. So, that should work. So, let's go sys drive. One specifies the location of the

**Dave Jones:** system files, A, and then C. Sys A C. How's that? I think it likes that. Come on. Let's boot this disk on chip. System transferred. Woo! Yeah, command.com. Now, let's reboot this puppy and see what happens. So, I'm going to take the

**Dave Jones:** disk out. I can give it the three-finger salute. Uh it should know there's no drive in A, and it should try and boot from C. So, fingers crossed. Come on. Starting MS-DOS. We're in. We're in. Tada! C prompt, and that was with no

**Dave Jones:** floppy. We did it. Winner winner chicken dinner. I finally got a bootable DOS 6.22 PC 104 board. You have no idea of the amount of effort I went to. It's taken me probably like a full day's work to get this thing

**Dave Jones:** booted. Like and many trips to the bunker and back home and up in the attic and all sorts of places to get this damn thing working. It's but it boots and the disk on chip from M Systems still works

**Dave Jones:** a treat. Awesome. I can remember when DOS 6.22 came out and we got things like you know I'm not sure whether it 6.22 or 5 from 2 6 or something and we got edit and we got things like scan disk. You know we

**Dave Jones:** got some decent upgrades in I think from DOS at least from DOS for 4 to 6. I started out with DOS 3.1 or something something like that. I can't recall. Hmm. Anyway, copied a couple of games on there too. Tiny little DOS games. I

**Dave Jones:** think with all this stress I'm going to have to play Eliza. Hi, I'm Eliza. I'm your personal therapy computer. Yeah, I need it. Please tell me your problem. Old computers are hard. Do computers worry you? Yes. Are you sure? Yes.

**Dave Jones:** Why did you repeat yourself? I don't know. Don't you really know? No. Are you saying no just to be negative? Yes. I see. This is not getting very far. Now, I'm running an old version of Donkey. Apparently, this one is famous

**Dave Jones:** because it was actually co-written by Bill Gates himself to demonstrate the graphics capabilities of the early PC. Hey, what do I have to Oh, I've got to avoid donkeys. Hang on. Yep. Hop. Wow, this is stunning. Ah. Doesn't get any better.

**Dave Jones:** Good on you, Bill. I'll tell you what, a game I really liked when I was a kid, I played this forever, Pango. Do you use a color monitor? You bet your ass. Level one, novice. You haven't played it in 30 years. Pango, ah, I used

**Dave Jones:** to Whoa, that's super quick. That's Yeah, that was a problem with games back in the day. If that's why we had turbo buttons, so you could slow down the computer um for these old DOS games. So, it's not moving. Ah.

**Dave Jones:** Anyway, it always looked better than that. Maybe they had like a higher res version or something. Hmm. Welcome to Breakout. Whatever happened to Ken Silverman, I wonder. Good on you, Ken. Ah, look at this. Oh, I can't I'm not

**Dave Jones:** quick enough I can't can't can't respond quick enough. The key The keys cannot respond quick enough to play this game. No. No kidding, I suck. So, I hope you enjoyed that look at the PC 104, which is still a standard these days,

**Dave Jones:** especially in military and lots of other industrial applications. They still swear by the PC 104 standard, and it started in the late '80s, still going what, close to 30 years later for a standard. That's pretty awesome. Will the Arduino be around in 30 years?

**Dave Jones:** Raspberry Pi anyone? I don't know, but PC104 you don't hear about it, but it's still going strong. So, hope you enjoyed that and my struggle to get disk on chip working. Trust me, you didn't see the half of it.

**Dave Jones:** Wow, it's just so difficult in getting these old machines up and running unless you got everything there and you work on old computers all the time. I got stuff scattered from here to Timbuktu and well, that was not easy at all. Bit of

**Dave Jones:** luck didn't go my way. Things screwed up, but I eventually got the thing working. So, anyway, if you liked it, please give it a big thumbs up and as always discuss down below and subscribe over here and subscribe to EVblog 2 up here. I'm

**Dave Jones:** releasing lots of videos on EVblog 2. So, if you're not subscribed, it'll be at the end. It's not right now, but it'll be right at the end. Subscribe to EVblog 2 cuz there's heaps happening over there. Anyway, catch you next time.
