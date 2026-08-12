---
video_id: mkx4qZCCHqI
title: EEVblog #900 - STM32 ARM Development Board
url: https://www.youtube.com/watch?v=mkx4qZCCHqI
source: youtube-asr
timestamps: {"0": 2, "1": 21, "2": 34, "3": 51, "4": 66, "5": 80, "6": 97, "7": 111, "8": 126, "9": 144, "10": 160, "11": 175, "12": 189, "13": 207, "14": 224, "15": 240, "16": 251, "17": 265, "18": 279, "19": 293, "20": 309, "21": 327, "22": 338, "23": 352, "24": 367, "25": 380, "26": 395, "27": 411, "28": 428, "29": 446, "30": 464, "31": 478, "32": 493, "33": 509, "34": 523, "35": 536, "36": 548, "37": 563, "38": 583, "39": 605, "40": 617, "41": 632, "42": 647, "43": 660, "44": 672, "45": 686, "46": 701, "47": 713, "48": 729, "49": 743, "50": 756, "51": 774, "52": 790, "53": 811, "54": 828, "55": 856, "56": 874, "57": 889, "58": 899, "59": 916, "60": 935, "61": 953, "62": 967, "63": 991, "64": 1006, "65": 1019, "66": 1031, "67": 1046, "68": 1068, "69": 1085, "70": 1106, "71": 1125, "72": 1143, "73": 1155, "74": 1173, "75": 1189, "76": 1197, "77": 1212, "78": 1226, "79": 1239, "80": 1254, "81": 1266, "82": 1281, "83": 1296, "84": 1310, "85": 1328, "86": 1345, "87": 1365, "88": 1376, "89": 1392, "90": 1406, "91": 1422, "92": 1444, "93": 1463, "94": 1476, "95": 1494, "96": 1513, "97": 1533, "98": 1554, "99": 1576, "100": 1589, "101": 1614, "102": 1636, "103": 1659, "104": 1676, "105": 1690, "106": 1706, "107": 1725, "108": 1740, "109": 1755, "110": 1768, "111": 1779, "112": 1793, "113": 1811, "114": 1829, "115": 1851, "116": 1869, "117": 1886, "118": 1901, "119": 1923, "120": 1937, "121": 1956, "122": 1967, "123": 1985, "124": 1997, "125": 2011, "126": 2044, "127": 2058, "128": 2070, "129": 2087, "130": 2104, "131": 2117, "132": 2131, "133": 2145, "134": 2159, "135": 2177, "136": 2192, "137": 2209, "138": 2226, "139": 2242, "140": 2257, "141": 2271, "142": 2287, "143": 2300, "144": 2317, "145": 2332, "146": 2348, "147": 2362, "148": 2377, "149": 2394, "150": 2414, "151": 2428, "152": 2446, "153": 2459, "154": 2475, "155": 2488, "156": 2507, "157": 2526, "158": 2543, "159": 2559, "160": 2572, "161": 2586, "162": 2601, "163": 2620, "164": 2633, "165": 2646, "166": 2660, "167": 2681, "168": 2701, "169": 2716, "170": 2729, "171": 2743, "172": 2765, "173": 2782, "174": 2798, "175": 2823, "176": 2840, "177": 2852, "178": 2863, "179": 2877, "180": 2895, "181": 2916, "182": 2934, "183": 2947, "184": 2960, "185": 2975, "186": 2987, "187": 3001, "188": 3014, "189": 3026, "190": 3038, "191": 3051, "192": 3068, "193": 3089, "194": 3102, "195": 3118, "196": 3131, "197": 3145, "198": 3158, "199": 3178, "200": 3192, "201": 3205, "202": 3219, "203": 3233}
---

**Dave Jones:** Hi, today we're going to take a look at the ST STM32 ARM Cortex M3 chipset and a very low cost development tool for this. This is basically for me to get up to speed for the STM32 Cortex chipset, the development system,

**Dave Jones:** things like that because one of my new products is going to be using this chip and I'll mention that in a minute. Now, I've got a new setup today. I'm obviously doing a webcam capture here at my desk and I can do funky stuff like go

**Dave Jones:** over to my screen capture and embed my little head down in the corner and hello, I can play around with the actual board and this is the board that we've actually got here today. It's the let's go over. It is the STM32L

**Dave Jones:** Discovery Kit and this thing is only here it is. It's only 13 bucks 83 on Digikey. So, it cost bugger all. I got it from local Farnell's it cost a bit more but they had it available. So, it's

**Dave Jones:** extremely low cost. They're practically giving the thing away and it's a very powerful micro which we'll take a look at. Now, this is what we've got the STM32L Discovery Kit. This is for the STM32L series not to be confused with the

**Dave Jones:** regular STM32 series ST and most of the manufacturers out there have a plethora of different chipsets and different series and there's subtle variations between them but this is the L and if you might be able to guess what that

**Dave Jones:** stands for. Stands for low power and some of the features this is why I'm particularly choosing this chip as I go into in a minute is it's low power functionality but this is a nice little board with the chipset, the programmer

**Dave Jones:** and debugger built in and also a little um as well cuz I'm using it in an LCD application. And uh we're going to try and um get this thing up and running and see what it can do. Now, somewhat confusingly,

**Dave Jones:** this is the 32L152C. Uh and that is different from the actual chipset I'm using in my product, which is the uh D chipset, the 152D. And they are uh different chips. You can actually get a development uh board for

**Dave Jones:** the 152D, but it's like 300 bucks here and well, yeah. No. But, this C version here is practically an identical uh chipset and it's 13 bucks. It's just crazy. And it's got an in-circuit uh programmer built into the thing as well.

**Dave Jones:** And if we actually have a look at the data sheet for the differences between the uh 15 2 uh D and the C one, they're they're basically very very similar. The only difference is that the D version that I'm using in my product comes in

**Dave Jones:** well, I it's got more memory. It's got uh 384K of uh flash, but it comes in a 144-pin uh LQFP uh package there. Uh whereas the one the C version that we're looking at only goes up to 256K and only goes up to

**Dave Jones:** 100-pin QFP package. But, apart from that, they're, you know, very basically identical chips, really. Now, let's take a look at some of the functionality of the STM32L chipset. And obviously, ultra-low power. They've put that like first, right up

**Dave Jones:** the top of the data sheet. There's a reason for that. It's cuz it is pretty darn low power. Um and it operates from 1.65V to 3.6V. Uh 0.290 nA in standby mode. Uh it's got three different wake-up pins. 1.15 A

**Dave Jones:** microamps microamps uh standby mode including the internal uh real-time clock. That's very good. Uh 440 nano amp stop mode and it's can use 16 different lines to wake the thing up like if you press a button or something like that.

**Dave Jones:** That's what the wake up lines mean. If you hook up a button to one of the external inputs, for example, you have a keypad, then that can wake it up out of that. Uh and it's got an 8.6 micro amp low

**Dave Jones:** power run mode. So, that'll be using the internal like 32 kHz oscillator uh to do that. But, when you're using external crystal, 185 micro amps per megahertz run mode. The D version is actually a bit more. It's 230 micro amps per

**Dave Jones:** megahertz uh in run mode. It's a bigger processor. It's got more memory and stuff. But, apart from that, uh they're pretty identical and have 10 nano amps IO leakage and all that sort of stuff. Anyway, it's an ARM Cortex M3 uh

**Dave Jones:** processor. Works from 32 K up to 32 megahertz. Uh yeah, the MIPS per megahertz if you're into that sort of thing. It's got a memory protection unit. Blah blah blah. Volt low uh ultra low voltage detector. All that sort of

**Dave Jones:** stuff. It's got an internal 32 kHz oscillator with uh RTC. And it's also got an internal high-speed oscillator as well. Plus minus 1%. That's pretty darn handy. And as I said, the low power 30 uh 7 kHz 30 I think I said 30 before 37

**Dave Jones:** kHz um RC mode. And it's got uh a internal PLL as well for USB operation. USB and UART are supported for bootloaders and things like that. Fantastic. My product is going to uh use a bootloader and load firmware images

**Dave Jones:** from an SD card which I'm going to hook up to it. Uh so, you'll see more about that in the future, no doubt. Uh JTAG trace debugging, all that sort of stuff. Uh 70 IOs are 5 volt tolerant.

**Dave Jones:** So, that's very nice. So, you can don't need any interface uh voltage translation chips or anything like that. Uh it's got 32 K of RAM. Uh this version that we got here for our 13 buck board is 256K of flash memory

**Dave Jones:** with ECC. It's got E-squared PROM built-in, which is uh one of the advantages uh that I will be making use of. And also, a big reason why I chose this chip in the product is that it has an LCD driver as well. 8 by 40 uh

**Dave Jones:** segments, which is um pretty much what I need. I think I need like um 36 segments or something like that. So, and it's got decent analog stuff as well. It's got two op amps uh built-in. Not sure of the performance of those. I

**Dave Jones:** don't think I'm going to be able to use those at all. Uh 12-bit ADC, excellent at 1 megasamples per second with 25 channels. Fantastic. It's got a DAC as well. A lot of micros don't have DACs, but it's got a 12-bit DAC uh with two

**Dave Jones:** channel DAC, awesome. So, you could do like stereo audio or something like that, perhaps. Uh with output buffers and uh two ultra low power uh comparators as well with wake-up capability. Uh DMA controllers, if you're into that sort of thing. USB 2,

**Dave Jones:** uh three UARTs built-in. Um eight up to eight SPIs, uh depending on the chip that you use. Or two I2Ss. It's got two I-squared C buses, 11 timers, blah blah blah, six 16-bit timers. All that sort of stuff. And it's got um

**Dave Jones:** capacitive touch sensing as well, up to 23 channels and CRC calculation as well. So, as you can see, it's a very powerful and versatile um micro. So, and you can get the development board for 13 bucks. Amazing. When I was a boy, and just as a

**Dave Jones:** bit of uh background, my original product design actually used a PIC uh 24. It used a 24FJ64GA uh 310. And I've actually got a um several prototypes here actually using that. But uh we decided to um we needed

**Dave Jones:** more memory, more functionality, all that sort of stuff. So, we looked to move to the 32-bit PIC, and well, the third PIC32MX, and I I I like them. They're decent parts and things like that, but the problem is, you'll notice

**Dave Jones:** the features here, nowhere does it really mention low power. It's got a bit of power management modes, but like it's not tooting its own horn when it comes to that. Um and you read the data sheet here, where you know, they're not

**Dave Jones:** tooting the horn of the low power functionality. Whereas, if you go to the data sheet for the uh STM, look, STM32Ls, there it is, bam! These are low power parts. They're selling that. It's the big selling point right up there. It

**Dave Jones:** turns out, I think, you have to go I won't go into it, but uh I provide links down below if you want to have a look. The PIC32 uh MX3 uh or something that we were looking at using actually has like five times the

**Dave Jones:** power consumption or something like that. It's a huge drastic difference in that and that power consumption is really very important in the product I'm developing. The other thing about the Microchip one uh the 32 is that it did

**Dave Jones:** not have a building LCD uh controller, so we would have had to use an external LCD, but the company I'm uh doing this company this design in combination with, they had used an external LCD controller before, so that

**Dave Jones:** wouldn't have been a drama. But, the original PIC24 I had actually had the LCD uh driver built in, and it actually had the nano watt XLP uh thing, and it was very low power. In fact, um slower power

**Dave Jones:** uh than than the uh ST arm uh 32 STM32. This is 150 microamps per megahertz run mode, and if you remember, this one was 185 microamps per megahertz run mode. So, technically the PIC24F lower power 400 nanoamp real-time clock

**Dave Jones:** and calendar operation. 400 nanoamps if we go over to here, it was standby mode plus RTC. There you go. It's like almost triple the consumption, but it's still bugger all. The STM32L series in particular still more than good enough to meet the specs. But, if

**Dave Jones:** you're going for a real ultra low power, like the best you can get in the industry, you probably wouldn't be using something like this. But, for my purposes good enough and it's probably, I don't know, three to five times better

**Dave Jones:** than the PIC32. And it's got all the LCD driver and everything built in. Beauty. Now, you might be asking what do we need to actually program these STM32L micros? Well, you only need one of these things. If you don't have the

**Dave Jones:** development board, you only you get the ST-Link V2 here it's called and it's 22 bucks 61. And it looks like you get all the adapter cables and serial cables and everything with it. Beautiful. It costs bugger all because as you'll see,

**Dave Jones:** there's bugger all in here. Now, there is actually an ISO or ISO version of this. This is just the exactly the same thing, but it has an isolated USB port in it. And if you're worried about you know, if you've got a

**Dave Jones:** ground reference product and things like that, how not to blow up your oscilloscope, I've done a video on that. I might have to link that one in. Then you want the isolated version. But, anyway, the good thing is is that this

**Dave Jones:** kit comes with essentially that thing built in. There we There we go. Onboard ST-Link V2 with selection mode link to use the kit as a standalone programmer. So, I don't even have to go buy the programmer. If you got this

**Dave Jones:** development board, you'll notice the header on the side here. And we can go over to here, you'll notice that the header, there it is, right there. And that can you can just jump that over to your product and it does exactly the same

**Dave Jones:** thing as the programming tool. Unbelievable. So, other stuff we've got on here that can be powered from the USB, as we'll find out. We'll plug it in in a minute. We can measure the chip current, the IDD current.

**Dave Jones:** Fantastic. That's what the little jumper link down there will be for. It's got a alphanumeric LCD on there, a 14-segment LCD on the thing, and it's got LEDs and push buttons and stuff like that. Anyway, it's exactly what I want.

**Dave Jones:** Uses the chip set, allows me to play around with the software programming tools and measure current consumption and typical current consumption and stuff like that. So, winner. I like it. Let's power it up, see if it does something. Hopefully, it

**Dave Jones:** comes pre-programmed. And if we actually have a look at the pack that it came in, there's nothing else in there except the board, and you wouldn't expect it for 13 bucks. But, it looks like it has some operational stuff on the back. And here

**Dave Jones:** we go. I'm going to plug it in and hopefully it does something. It says to put the link in Well, there's there's different positions. We'll plug it in there. Ta-da! Look at that. There we go. Discovery. Boom. JP1 is on.

**Dave Jones:** That's JP1 there. You can probably see that. And we've got lights flashing and it's measuring the supply voltage. So, obviously, it looks like it's got a 3-V voltage regulator on there. And uh that is very nice. So, let's let's just

**Dave Jones:** re-power that. Or reset it. Yeah. Beautiful. And can we play with the slider? No, slider doesn't do anything at this stage. Let's see if we can, change mode, shall we? Sorry, I've got this propped up on a box.

**Dave Jones:** Uh and I have no idea what percentage what that means. Not quite sure. So, what's that? It's not some sort of counter.

**Dave Jones:** Hello. Sleep mode. .0 Run mode. It looks like it's cycling through and measuring the power consumption. This is fantastic. This is great. Sleep mode. 260 microamps. Run mode. Ah, beautiful. Let's push this again. So, it comes pre low power run mode. There we go. That's

**Dave Jones:** using the low power oscillator. 3.7 microamps. Low power run, 7.6 microamps in the low power run mode. There you go. And the card, um here actually tells you what the what the different modes are there for uh My

**Dave Jones:** The auto focus on my Logitech C920 webcam is not working that great. Um I had to set the other one manually. The one on the left there for the board. Anyway, um you've got the different modes and that's great. It measures.

**Dave Jones:** I didn't expect it to measure the power consumption. I thought I'd have to take the jumper link off. That's very common on these develop and what you take the jumper link off and then you insert your current meter in there and measure it.

**Dave Jones:** But, that's that's terrific. Beautiful. It's exactly what you want. If you're into low power, if you want a low power arm processor this one's great. I would presume that's a live measurement. Let's see if we can find the schematic.

**Dave Jones:** So, press that button one more time, though. Do we go into another mode? 1. Yeah, what's that? These are all the different modes. I mean, these modern processors have so many different um modes on them. Standby. Yep. Standby wake up.

**Dave Jones:** Okay. 360 nanoamps. Beautiful. I I'd love to know if that's a real live measurement of that. Anyway, we're back. There we go. Back from the future. Let's change the jumper link here. It resets the processor cuz it interrupts the uh

**Dave Jones:** thing and it looks like Is there anything different? It's the same. That's the same.

**Dave Jones:** That's different. It's milliamp mode. It's displaying the current in milliamps now. 0.03. Yeah, 30 microamps. So, it looks like jumper up is uh microamps and um jumper down below is milliamps. So, there you go. Oh, no. Well, it's displaying microamps

**Dave Jones:** now, but it's like that's 20 nanoamps. Wow. Now, it's down in the That's interesting. I I want to have a look at the schematic and see exactly how it's measuring this and doing this cuz there's nothing else on the board.

**Dave Jones:** You'll note that it's got It's got the main processor, the external crystal isn't fitted. So, if you want to um put in your own external crystal, no worries, you can. It's got a 32 Sorry, it's got a 32 kHz external crystal here.

**Dave Jones:** It's hard to do I should not look at the screen. 32 kHz external crystal and um there's basically nothing else. There's like there's nothing on the bottom of the board, by the way. So, you can actually hook up a battery,

**Dave Jones:** by the looks of it. That's nice. Um it's got some reserve stuff up the top. Don't know that what that is. We'll have to read the manual. Have to RTFM. I wonder if we can uh use the slider. The slider's got a piece

**Dave Jones:** of uh Perspex on there. Which is quite nice. So, anyway, I love how it measures the current consumption. It's beautiful. And if I follow the link on there, uh st.com stm321 um L Discovery, it takes me to uh this

**Dave Jones:** page here. Here it is. And uh this has What's this? STM Cube L1. I don't know. They keep throwing names at me. I don't know. Embedded software uh includes low-level drivers, USB file system, RTOS. Wow, touch sensing, graphic coming with examples

**Dave Jones:** running on ST boards. Um Cube is an ST an original initiative to ease developers line to reduce development effort, blah blah blah. Right. So, they call it STM Cube. And that's their initiative to ease development. I don't get it. Anyway, consistent and complete

**Dave Jones:** embedded software offer uh that frees the user from dependency issues. Excellent. All right. To play here, STM Cube overview. Ooh. We can watch this. Hopefully, the audio comes through. And we've got different video showing you. All right. Anyway, generates high-level

**Dave Jones:** code and all that sort of jazz, which is great. Um sorry. It uses high-level GUI to generate initialization code for your micro. Oh, shush. Um because one of the problems with developing for micro, especially for the first time if you're

**Dave Jones:** not used to it, is all the initialization and setup stuff of all the registers and everything else you need to do just to do basic stuff. Um so, if you can get a high-level GUI interface that takes care of all that

**Dave Jones:** stuff for you, then, yeah, great. You'll be up and running much quicker. So, I can actually go down to get software here, and we can get the software version 4.15.1. Get software. Oh, yeah, blah, blah, blah. Accept. Oh,

**Dave Jones:** Bite me. This is just When a company's going to learn, this just pisses people off. To sign you up to They're just going to use crap uh email addresses anyway, and names, and fake names, and everything. And like,

**Dave Jones:** I've got now got to go to my email to get the link to now God.

**Dave Jones:** I hate this crap. So, while that's downloading, about 150 meg or so, um what development tool chains does it use? Well, it uses the IAR uh embedded uh workbench, which I've used uh long time ago in a galaxy far, far away. Uh

**Dave Jones:** Keil. Um ARM. I don't think I've ever used the Keil um software, and the GCC one as well. So, there you go. But, it's not like there's nothing obvious, you know? You go to like the product page here, and there's got like there's

**Dave Jones:** technical documents and descriptions and things like that. But, there's nothing uh that sort of, you know, maybe you got to watch the videos and and go through step-by-step. But, there's nothing like download this, and it just includes like

**Dave Jones:** the GCC uh compiler, for example, by default, with all the stuff already set up for this particular micron, things like that. So, it's not uh you know, it's So, for a beginner coming in, "Oh, how do I use this these ARM uh chips?"

**Dave Jones:** It's, you know, it There are certainly uh better options out there to actually do it. So, yeah, I'm going to have to figure out exactly what I need here, whether or not I'll use the GCC, or whether or not I'll use um

**Dave Jones:** uh the IAR Embedded Workbench cuz I think you get a free version up to 32K or something, is it? Don't quote me on that, but uh you get a Anyway, I think it is. I think you might get a free version of the IAR um and

**Dave Jones:** maybe it's got some optimizations disabled or uh something like that, but anyway, I I have not used the GCC um compiler before, so I don't know. But, they do have uh these things, getting started with the software development short toolchain

**Dave Jones:** document and things like that, but there is no um you know, like click here to download the software kind of thing. So, it's it's just not there. They've got that code uh compiler, which I'm downloading at the moment, but that's actually not a

**Dave Jones:** code initialization thing, but that's just to generate initialization code. It's not uh I don't believe it will include any uh compiler in there at all. Um and by the way, no schematic. Um I can get the Gerber files. I can get the bill of materials.

**Dave Jones:** So, I downloaded the uh Gerber files. They're all there, so that's hunky-dory, but where's the original PCB uh file? It's not there if you wanted that. Um and the schematic? I can't find it. It ain't here. And if I actually go over to Digi-Key

**Dave Jones:** here, it does have Look, there it is. The uh STM32L152C disco schematic. I click on that. And wah wah wah wah Now, it did link through to the page for the uh discovery firmware package, uh which is what we want. I want the code

**Dave Jones:** for this thing to see exactly how it's doing the current measurement and things like that. If I can't get the schematic, still don't know where that is. Um look, they got some documents here. Uh current consumption measurement and touching

**Dave Jones:** touch sensing demonstration firmware. So, if we we a look at that, uh here it is. Here's the application note. Tells you all about it. Fantastic. So, their documentation is pretty good. Here's the um look, it's got separate IDD measurement

**Dave Jones:** circuitry on here. So, that's the uh you know, block diagram. I don't have the schematic. Haven't checked further on, but tada. So, here it is. We've got uh two current sense resistors there, and it looks like look, a digital switch there that uh is

**Dave Jones:** controlled via a counter down here. Um it looks like like a separate counter chip cuz that's the STM32L 15 there, and then there's an external uh differential amplifier with a gain of 50, another electronic switch, another electronic switch here. Um

**Dave Jones:** where's all this circuitry? I was very curious, so the only place left for it was tada. There it is. Sneaky buggers. Ah. But anyway, is the uh schematic in here? Okay, no. No schematic at all. Bummer. Does it Is it linked in

**Dave Jones:** down the bottom? Reference documents, updated clock section. Nah. Nah. But hey, this is neat. It tells you how it all works and the algorithms to actually do it. Sweet. And if you have a look, the IDD jumper JP1 must be placed

**Dave Jones:** in the on position except for bias current record operation. So, I think we saw bias current uh pop up on the LCD when we had the jumper in the other position there. So, what bias currents are we measuring?

**Dave Jones:** Cuz bias current is not static current, so anyway, um can you to compensate errors due to the uh bias current. Okay. Right, bias current record. Okay, so that's like a calibration feature by looks of it. Bias current This operation consists of storing the

**Dave Jones:** bias current values of operational amplifier A. Hey, they've thought of everything. Compensating for the error in the times 50 amplifier in there. Sweet. And bias current mode, there we go. JP1 off, yep, you betcha. And release the switch and it tells us the

**Dave Jones:** bias current. There we go. Bingo. It's stored it Well, I Yep, I believe it's now Well, 0.16 It's jumping around a bit. Anyway, it's now compensated. So, now I re-power that and it is in it's stored in there. By the way, this

**Dave Jones:** is the uh slider. This is a percentage slider like that. So, that seems to work reasonably well. Go in there and that just It's a crude slider like that. But, that's This is a great example board. And now these are the actual uh

**Dave Jones:** measurements in the various uh modes. So, 260 microamps there. Run mode. 740 microamps. 280 microamps. Beauty. And we can go into those. This is winner, winner, chicken dinner. Right, so let's run this CubeMX thing and see what happens. Next, I accept.

**Dave Jones:** Blah, blah, blah, blah, blah. We don't have to use this. Uh we can just use the compiler uh directly, but um yeah, we haven't gotten there yet. I want to try this out. Target directory will be com- Yeah,

**Dave Jones:** right. Create shortcuts, yep. Right. All users, yep. Right. And here it is. Looks pretty boring. Load projects. Do we have example projects? New project. Here we go. Whoa, hey! This is what we want. Bam, straight in. Thank you very much, board selector.

**Dave Jones:** Here we go. Here's all their boards. Here we go, discovery. Wow. Um 152 Where is it? STM32L Discovery 152 disco. That's the one we're discoing. All right, so we can I guess go like that. Oh, yeah. Okay. Peripherals connectors selection.

**Dave Jones:** Initialize all IP. Oh, vendor. Oh. There's only the one vendor, ST micro boards. Um Okay. So, we've chosen our board. Fantastic. It supports very comprehensive supports all their development boards. Ah. Isn't that sweet? Look at that. I love these GUI. Um oh,

**Dave Jones:** can use my mouse wheel to scroll in and out there. Look at that, graphical representation for the chip. That's actually on there. It's the STM32L152. Uh CTX. It knows exactly what chip's on there. It's pulled it up. And now, look,

**Dave Jones:** can we go in and click on the individual pins? Can we do anything? No, it just hovers over and tells us what that does. Ah, there we go. Yep, so the IO so PB7, we can then change PB7 to do anything we

**Dave Jones:** want. We can change each individual individual pin to be configured. By default, these this is what the configuration for this chip is for this particular demo board. Right, so as you can see, it's already set up for all the segments, coms, and

**Dave Jones:** everything for the LCD. So, the segments and we're using three commons for the LCD there, by the looks of it. And there's the green LED and the blue LED on the board. And wow. Wow. That that is great. That is excellent.

**Dave Jones:** So, there you go. We can configure all this stuff, middlewares, configuration middlewares. Look in the top corner. Fat, so there's a fat file system. Um I guess if we had like an SD card it would come configured. It's got a free

**Dave Jones:** RTOS. I don't know what the uh what which free uh well, is it called free RTOS? Um and the fat file system I guess um if ST have written there um a fat file system which allows you to So

**Dave Jones:** you can include that. Then you can go in and you can configure all your clocks. Look at the block diagram. Oh, I'm so ex- This stuff you usually when you're developing for micros this sort of stuff is in buried in page

**Dave Jones:** 300 of the data sheet and you've got to go in there and look it up. You know, you've got to know that oh, internal register such and such to select the input on this mux here. You know, you've

**Dave Jones:** got to do all that, but this is Can I Yeah, yeah, there we go. I can just select which channel of my mux I want. That's nice. And then I can divide by eight thing. So the system timer for

**Dave Jones:** the clocks and everything else. Wow. Wow, it's almost too powerful. You could get lost in here. Um but that is that is absolutely brilliant. That's what you want as a beginner. You don't want to you know going into the data sheets and try to

**Dave Jones:** find this stuff is a real pain in the butt. Um so other configuration stuff, uh DMA. Okay, so there's all the DMA stuff. Not really interested in GPIO. Uh real time clock. There we go, instruction what? Calibrate there your calibration values

**Dave Jones:** for your real time clock. Uh ask RCC uh Oh, RCC? No, that's not RTC. That's um RCC. What's that? That's something else. Analog? Not there. What do they call it middle wares? That's hilarious. So, uh time base or this is your timer. That's

**Dave Jones:** watch dog. Uh power consumption calculator. Brilliant. So, it will give you an estimate of uh this is very common in the FPGA field and stuff like that. Uh when you want to estimate how much your design how much current your design's

**Dave Jones:** going to take. Now, in this case, we're not you know, generating various using macro or macrocells and things inside, but we are turning on certain functions. We are like a certain uh chipset peripherals and things like that. So, each each peripheral you turn

**Dave Jones:** on and enable and use is going to take extra current, what frequency you're operating at, which clock you're using, all that sort of stuff. Uh it even takes into account the ambient temperature, which supply voltage you're doing um and you can select Ah, look at this.

**Dave Jones:** You can select your battery. CR2032. WOW. WOW. SO, it will it give you the battery life? It'll self-discharge 0.12% per month. Nominal capacity for CR2032, 225 if you got one or two in series or parallel. Wow. This is This is neat. I like

**Dave Jones:** current current consumption calculators. I'm a bit of a current consumption calculator fanboy, if you didn't know. Um so, that is neat. Like, I won't go. I could spend all day here, but the fact that it's got that, that is great. So, that is an

**Dave Jones:** excellent configuration thing. So, here we go. So, we can generate the code. Power transitions checker. Oh, looks like you can do you can do sequences and stuff. This power uh consumption calculator might be more powerful than I think. So, if I think it's pretty good

**Dave Jones:** as I thought. But, yeah, look, you can add in steps. There you go. So, you can add steps as you change things. So, if you're going into sleep mode and things like that, it can I I believe it should

**Dave Jones:** be able to calculate all that. Wow. Okay, I'm thoroughly impressed. All right. This STM32CubeMX winner winner chicken dinner. Anyway, we can generate code for all of our current pin outs. So, what you do is you set up when you got a new project, you set up

**Dave Jones:** what pins do what. And like you might want to change them on the fly, of course, but this is like the initialization code. What this software does is generate your initialization code to get your micro up and running

**Dave Jones:** and to be able to do something when you first power it up when you enter your main function, for example, before it gets to the main function in your code. So, we can generate a report. I'd like to generate a crack

**Dave Jones:** uh Hm. Generate code. Test. Project location test. And then we choose our tool chain. Um Oh, yeah. It's where's GCC. I get it. No, that's the Hm. Okay. No, unless there's another name for it. Other tool chains. Anyway.

**Dave Jones:** Code generator. Advanced settings. All right, let's let's project location cannot be found. Oh god, give me a break. Yeah, yeah, yeah. Open.

**Dave Jones:** Firmware package or one of its dependencies required is not available in the Do you wish to download this now? Yeah. Okay.

**Dave Jones:** Okay, why didn't it include it? Download STM Cube firmware. I don't know why it needs to do this. I'll get back to you. Okay, it downloaded that fine. Took a little bit, but it downloaded and then kept going and compiling uh the code and

**Dave Jones:** generated the code then I could have opened the project or um in this case I've opened the source. So, here we go. Main. Just open this in notepad here and bingo, here we go. It's generated all the code. There it is.

**Dave Jones:** And yep, there we go. There's our oscillator initialization code, all that sort of stuff. See, all of this sort of stuff you would have had to have figured out from the data sheet and done manually. Otherwise, your micro sits there and

**Dave Jones:** does nothing. It just won't work. Um and that's you know, a huge hurdle for microcontroller development. That's why Arduinos and things like that are so popular. Every you know, it's much higher level than that. All this sort of

**Dave Jones:** stuff, register level stuff is taken care of uh for you. But then there we go, it sets up the uh pins. And uh well, it's telling you how the pins are going to be set up. And then it goes in and uh and it's setting

**Dave Jones:** pull-ups. Um yep, it's yeah, pull-ups and speed. So, you can set the GPIO speed, you can set the GPIO pull-up. Um then you can set the GPI uh mode. Look at like you know, there's a lot of initialization

**Dave Jones:** code here that that GUI has generated for you. Thank you, mister GUI. That is brilliant. Huge thumbs up. And on that uh firmware page I was actually able to download the actual firmware source code for this uh particular

**Dave Jones:** uh demo board. Downloaded no problems. Here's like the LCD Here are the files on here and uh we can have a look. There. There we go, STM32 Discovery. All it's all in there. And this is like the code for the LCD, for example. And very

**Dave Jones:** well documented. Here's the 14-segment mapping and stuff like that. How they actually map the things in there. And that's terrific. So, all the example source code is there. So, you can re- should be able to recompile this for yourself and then play around with

**Dave Jones:** this. Maybe use this as a basis for your own project. But as I said before, where is like the link to just download the GCC compiler or something like that with everything set up. It's not at all obvious. It's not for the beginner this

**Dave Jones:** thing. Like this is the product page for this development board. And okay, looks like we're going to have to go in here and read this getting started or getting started with the software development toolchains. We're going to have to read a PDF document before we

**Dave Jones:** can just go in there and like, you know, so for sort of, you know, experienced users like me who have used another micro, for example, but haven't really used arm before like this then like I want to know, where's the

**Dave Jones:** programmer software? Where's the compiler software? And I want it all there on the product page so I can just download it and start running with this thing. But no, looks like we're going to have to read some documents.

**Dave Jones:** Bummer. And unfortunately, look, this document provides an introduction on how to use the following software development environments. IAR Embedded Workbench, the Keil one, True Studio. I've never heard that by Atollic. I don't know, maybe there's a few Atollic fanboys out

**Dave Jones:** there. Or Tasking, which I know fairly well because I used to work at Altium. Tasking are good compilers used in primarily like the automotive industry and stuff like that. Really big in the automotive industry, but I don't think,

**Dave Jones:** you know, outside of there it's not that huge, but really good compilers from Altium. Highly do with the task in group at Altium. Still in the Netherlands, I believe. Anyway, the Yeah, but where the emission Where's GCC? Like

**Dave Jones:** If I did my project, everyone will go Everyone will just assume that oh, I'm going to use GCC. Everyone uses GCC, right? It's you know, it's the thing to use, but this is the getting started guide for this discovery board and it does not

**Dave Jones:** tell you how to use GCC. Doesn't tell you where to get it from. It doesn't matter tell you, you know, like links to a compiled version of it. There's the ST-Link thing. So, yeah. Looks like we're going to have to use IAR embedded workbench,

**Dave Jones:** which is fine. I've used IAR before. They're excellent excellent tool. I love the GUI interface and things like that. I've used it for like Atmel and other um ones, but I haven't used it for ARM before, but yeah, um

**Dave Jones:** that's disappointing that GCC is not in there. That's a huge oversight. So, I'm on the IAR embedded workbench website. 62,000 users. Is that all? Thought they'd have more than that. Anyway, they support 11,000 devices, blah blah blah, 30-day free trial, blah blah blah blah

**Dave Jones:** blah, but look at this. You go to the buy page. What what what what request for quotation. Seriously, are you that dumb, IAR? Just put the freaking price there. A PayPal buy it now button or whatever. Have different

**Dave Jones:** tiers of your software if you want. Sure, if you got some need some enterprise version for, you know, a thousand seats at your company or something, fine. Okay, quotation for that. But me, buying my little $15, you know, embedded discovery thing, um

**Dave Jones:** this is where the documents point me towards IAR. There's sure there's some others, but I come here and go, "What quotation? What's all this? No. Fail." And it turns out they've actually got a ton of different versions just for

**Dave Jones:** arm. Look at this. They've got functional safety standard Cortex, Cortex M0 limited baseline versions, blah blah blah blah blah. Anyway, what we want to do is go into the um free trials here and uh take a look. Now, here's where I said before uh you

**Dave Jones:** do get a size limited Kickstart license without any time limit or you get a 30-day full, you know, pretty much the full thing for 30 days. So, you can choose which one you want. Um the uh size limited Kickstart one, as I said

**Dave Jones:** before, uh 32K restriction. Ooh, 16K for Cortex uh versions. Uh so, there's no source code. Uh you don't get the Mistral C support. Um C-Run is not available. Don't know what C-Run is. And limited technical support. But anyway,

**Dave Jones:** that will allow us to get up and running anyway. But anyway, we'll download that. And even with, you know, a 32 um K size limit and, you know, it might not include optimizations and all the other stuff or it just include debugging.

**Dave Jones:** Doesn't say anything about debugging limitations and things like that. But you can still do a lot in 32K. So, yeah. That's only a 1 gig download. Anyway, I've got a reasonable connection, so it's already 1/10 of the way there. Yay! I will

**Dave Jones:** show you my desktop. Just for fun while we idle the time away. Look at this. There's an option for dongle drivers. I don't think I need to install dongle drivers. Did IAR come with a dongle back in the day? Anyway, I'll just install

**Dave Jones:** the uh ST-Link. Yep, you guessed it. Online form to register for your time-limited or code size limited version. Uh All righty, so after loading it in, I got the license keys and all that sort of jazz, I can open a workspace and I've

**Dave Jones:** downloaded the firmware which you saw before. And if we go into the discovery pack firmware projects, let's look at the current consumption touch one that's inside, which is the demo that we're actually running on the board and EWRM.

**Dave Jones:** Here we go, so it's got all the different versions here. Okay, and bingo, there's the E file. Let's open it. Will it work?

**Dave Jones:** My workspace is up. Yep, there we go. There we go. We're in like Flynn. And I just tried the make function, sorry I wasn't recording and it went through with no errors. Okay, so it did actually make that project without error. So what I'm

**Dave Jones:** going to do here is I'm going to I'm in the main I'm in user and then the main.c here and it looks like we can just change the text message that is presumably displayed on the LCD. So I might

**Dave Jones:** simply change that to E Vblog. I could change it to hello world, but you know, meh. Else what? You and else do that. Oh, I don't know. That one can be hello world. There you go. Oh, everyone wants the exclamation mark.

**Dave Jones:** And then we can make this again. So if we go into make, here we go, building tree, blah blah blah blah blah converting number errors zero. Okay, let's try and download it. So remember I have not used this before. I have not

**Dave Jones:** read any instructions whatsoever. I simply loaded in the project. This is the best way to get set set up. Load an existing project that compiles with no errors and then start playing around with it and then, you know, learn that

**Dave Jones:** way. It's, you know, it's one of the best ways to do it anyway. Um, there's some, uh, little buttons up here. Hang on. There we go. Download and debug. Download without debug without downloading. We want to download and debug. I just

**Dave Jones:** want to download, but anyway, we'll download and debug. Uh, what? So, it didn't automatically detect my I installed. It was supposed to install the drivers, the ST-Link drivers, and it just not not not happy at all. Let's go into

**Dave Jones:** projects here. Download and debug. Debug without downloading. Download. Download active application. What? Well, it was supposed to be that easy. Um, here it is. Uh, for the EWARM tool chain, which is what I'm, uh, using. Basically, um, open

**Dave Jones:** the workspace, which is what I did. Um, got the example demonstration was what I did. Uh, rebuild all. Well, I did make. Uh, maybe I've got to rebuild all. Anyway, should have done the business. And then, uh, but that's what I got.

**Dave Jones:** Total number of errors and warnings and everything. So, that's fine. And daddy, and then, uh, include I didn't do project options C++ compiler. Why do I have to do that? Anyway, in the, uh, to change the project settings. Don't have

**Dave Jones:** to do it. There you go. Uh, download and debug. That's all you had to do. Download and debug. I hit that button. Exactly what I thought. And there you go. It's supposed to download and debug. But it hasn't. And that's it. That's the

**Dave Jones:** entire instructions for the, um, for the IAR embedded workbench thing. That's it. And it didn't work. Thumbs down. Oh, no. I think it's a PEBCAK. Looks like I missed a step after installing the EWARM. The user should install the ST-Link V2 driver. The

**Dave Jones:** original ST-Link, not the V2, the original one does not need a driver, apparently, but the ST-Link 2 does. See, like this should be on the Okay, it's in the document. Okay, but it's Yeah. All right, I'll stop complaining. It's

**Dave Jones:** in there. I probably should have read it. So, you have to do this um after you install the IAR uh workbench. So, let's do that. So, it's supposed to be in C um IAR Systems Embedded Workbench um drivers

**Dave Jones:** ST-Link Ta-da! ST-Link upgrade. No? It says to run the No, okay, Windows I guess I've got to go into Windows 7. No, ST-Link Noop. Doesn't match the description. There you go, ST-Link ST-Link V2_USB driver. It doesn't match the

**Dave Jones:** description. Okay, so I ran the batch file here and it's going to Let me install the drivers. I'll probably have to might have to reconnect it, of course. It uh it may take some time to complete. Thank you very much. But once again, you

**Dave Jones:** know, these little things where it doesn't match the description and it's buried away, you got to No, like they need to have a more compelling first-time user experience cuz, you know, you can be left scratching your head if

**Dave Jones:** you you know, if you managed to figure out how to download IAR and all that and then open the workspace and all that, you're following the instructions, and yeah, it doesn't kind of work. And then, oh, what is what

**Dave Jones:** are these error messages down here mean? That it fatal error failed search for probes. Ensure that the USB drivers are installed. Like, you know, yeah. It just occurred to me. You remember way back at the start where I was installing this

**Dave Jones:** thing and it said, "Do you wish to install like the US like the dongle?" Right? That dongle thing. Was that Is that what they're talking about? Maybe. If so, that's, you know, dodgy terminology. Anyway, hopefully it'll work now. Can we just do it? Can we just

**Dave Jones:** do it? Yes! Look at that! It's flashing! It's downloading! Will we get EVblog? Hello. Run. It worked. I didn't have to reconnect it. Did I accidentally set up a breakpoint? Toggle breakpoint. I don't know. No, why is it pointing to

**Dave Jones:** int main there? Anyway, it downloaded. Maybe I saw an option leave target running. Here we go. Like So, all this is enabled now. So, leave target running. Is that uh No. Maybe if I hit the reset button. Hey! EVblog!

**Dave Jones:** Winner, winner, chicken dinner. So, there you have it. This has been long enough. Sorry for the length of this. It was sort of like a me going through it sort of like first try just to see how good the uh how easy the tools were to

**Dave Jones:** set up. And well, ultimately, it took like a few hours to do this. Granted, I'm shooting a video and doing, you know, everything else. But, you know, I'm around. But, hey, you know, it wasn't the best uh first impression.

**Dave Jones:** Not suitable for a complete beginner. And maybe some things might be a little bit uh you know, annoying for like an experienced person like me, but somebody who hasn't touched uh the arm toolchain like this before. So, anyway, I was um

**Dave Jones:** quite surprised that there is no support, or it doesn't look like I will stand to be corrected, no support for the uh GCC or whatever. Or, you know, like I don't know how to use GCC with this thing yet. I'm sure everyone's

**Dave Jones:** screaming, "Oh, it's easy. Set up the command line. Do this. Do that." Yeah, whatever. Okay. I got um the IAR Embedded Workbench working fine as long as I followed the silly instructions to the letter. And installed the drivers and

**Dave Jones:** everything's hunky-dory. I'm up and running now. So, you know, yeah, it's not the best first impression. I mean, if you go over to the um you know, just the website for this thing, it's a little bit quirky. It

**Dave Jones:** doesn't really have everything. It's not you know, everything's not in the one place. Um stuff like that. I mean, this is the main page for the Discovery Kit and you know, it leaves a bit to be desired, but

**Dave Jones:** ultimately, you know, after a couple of hours of mucking around, anyone should be able to get a tool chain up and running for this thing. Uh GCC or something might be a bit more confusing or take longer. They would

**Dave Jones:** don't have the step-by-step instructions for that. I think they should. Um but anyway, you can get a 32K version of the IAR Embedded Workbench. You can do some decent stuff with that. Um although this thing's this board has

**Dave Jones:** 256K, so you know, anyway, if you want the full version, you pay the money, etc. But for a $13 um development board and this part what what it can actually do is is very impressive. The functionality for it and everything

**Dave Jones:** else, it it's an absolute winner. What is the What is the price on these? The STM 32 L152 I won't include the rest of it. And uh integrated circuits. There we go. What have we got? Sort by price. They're not cheap in

**Dave Jones:** one-offs. Oh, no, there we go. Yep, the 152C that we're looking I don't know if it's exactly the same one, but two bucks 30. You know, oh, actually, that's 1,500 uh quantity. So, yeah, we have to go down

**Dave Jones:** before we can get to uh anyway, you know, a few bucks. It's not the cheapest, but it is a high-end um, you know, quite a powerful uh, um, micro. And for a 13 buck development board, um, yeah, why the

**Dave Jones:** hell not? I like its low power modes and everything. It supports LCD and all sorts of stuff. And hopefully you'll see uh, some more upcoming videos. Although the supporters might actually see those videos before or find out information on

**Dave Jones:** that before uh, the regular audience cuz the pro- product I'm working on is not uh, general knowledge yet. So, anyway, um, that ultimately worked in the end. Just a few little quirks, the odd PEBCAK or two, as to be expected.

**Dave Jones:** So, if you combine that uh, low-cost development board, which is really nice, with the power management and the LCD and everything else, uh, the low-cost programming tools for them easily available, uh, they've got an even an isolated version, which is

**Dave Jones:** very nice, which is still uh, even reasonably priced. And then when you combine in the awesome uh, STM32 uh, CubeMX uh, software, like configuration software, that's absolutely brilliant. Looks to be very comprehensive, very powerful. And uh, then I think they've

**Dave Jones:** got a winner here. Uh, combine that with the chip, the capabilities of these ARM STM uh, chips, I'm I think I might be a uh, ARM STM32 fanboy. I certainly like this uh, low power series anyway, very comprehensive

**Dave Jones:** capabilities. So, well worth a look at it if you're right into um, development. There might be ones that are slightly easier to get started, but this one's very compelling in the arms. No worries. Anyway, I hope you enjoyed that. If you

**Dave Jones:** want to discuss the ARM uh, development tools and tell me, "Dave, you're doing it all wrong." Yeah, go ahead. Comments down below. Catch you next time. Hi. In this video, we're going to take a look at a couple of affordable FPGA

**Dave Jones:** starter kits to get you into FPGAs. But before I jump into that, I thought I'd just do a quick little primer here on exactly how easy is it to hook up and use an FPGA? As I mentioned in my

**Dave Jones:** previous videos, which I'll link in, the answer is not very easy at all. Take for example, your classic microcontroller here. You pick your AVR or your
