---
video_id: Rixo78hv_lw
title: EEVblog #1140 - 3 CENT Micro LED Blinky with ICE!
url: https://www.youtube.com/watch?v=Rixo78hv_lw
source: youtube-asr
timestamps: {"0": 1, "1": 12, "2": 34, "3": 47, "4": 59, "5": 76, "6": 94, "7": 106, "8": 124, "9": 137, "10": 148, "11": 163, "12": 178, "13": 197, "14": 211, "15": 226, "16": 238, "17": 253, "18": 264, "19": 283, "20": 293, "21": 308, "22": 320, "23": 336, "24": 349, "25": 365, "26": 379, "27": 390, "28": 403, "29": 415, "30": 431, "31": 448, "32": 465, "33": 481, "34": 494, "35": 512, "36": 527, "37": 543, "38": 561, "39": 576, "40": 591, "41": 604, "42": 618, "43": 633, "44": 653, "45": 666, "46": 680, "47": 694, "48": 708, "49": 724, "50": 740, "51": 754, "52": 777, "53": 791, "54": 801, "55": 817, "56": 828, "57": 841, "58": 853, "59": 865, "60": 880, "61": 899, "62": 916, "63": 930, "64": 943, "65": 957, "66": 976, "67": 994, "68": 1010, "69": 1025, "70": 1039, "71": 1054, "72": 1067, "73": 1079, "74": 1093, "75": 1109, "76": 1125, "77": 1139, "78": 1156, "79": 1168, "80": 1180, "81": 1195, "82": 1210, "83": 1226, "84": 1245, "85": 1261, "86": 1280, "87": 1294, "88": 1308, "89": 1322, "90": 1338, "91": 1350, "92": 1363, "93": 1377, "94": 1391, "95": 1404, "96": 1421, "97": 1438, "98": 1451, "99": 1468, "100": 1482, "101": 1495, "102": 1509, "103": 1522, "104": 1533, "105": 1546, "106": 1556, "107": 1573, "108": 1586, "109": 1604}
---

**Dave Jones:** Hi, in a previous video which I'll link in down below at the end if you haven't seen it and I'm sure you have because like a hundred thousand people watched it seemed very popular. This Padauk if I'm still pronouncing that

**Dave Jones:** correctly, Padauk three cent microcontroller that you can buy from LCSC here. I won't go through but even if you look even in 300 quantity under three cents each for a little eight pin or a soft 23 package micro eight bit microcontroller

**Dave Jones:** not flash but like one time only programmable but three under three cents each. Remarkable. Anyway, one of the questions was from the video after I did that video apparently they completely sold out. There was nothing left on the website. They do actually

**Dave Jones:** have more in stock. So a lot of people asked well, is it was it just a one time buy and stuff like that. It seems not. The LCSC have ordered more and stuff like that. Anyway, I ordered a bunch of

**Dave Jones:** chips. I've actually got them. They delivered no problems. I actually got a whole reel of 10 cent or sub 10 cent or something 3.3 volt voltage regulators. Apparently they're pretty good. They sell really cheap voltage regulators. So why not have 3000 of them? Beauty.

**Dave Jones:** Anyway, we've got the micros and thank you very much to Padauk kindly saw my video and they kindly sent me the programmer. Now they say that it's only available from a Taobao website which is a Chinese like eBay

**Dave Jones:** type website. So it's it's not exactly easy to get. It's like a hundred US dollars I believe for the programmer. They didn't have any of the programming adapters for them in stock. So they couldn't send me that but I can just

**Dave Jones:** make one myself no problems whatsoever. They also kindly sent me the in-circuit emulator. I've done an unboxing on my second channel Focus Bastard. All right, there we go. Um, in-circuit emulator for it as well, because these chips are one-time uh programmable. So,

**Dave Jones:** obviously, like every time you compile your program and run it, you don't want to have to burn a new chip, right? And then plug it in and all that. So, the in-circuit programmer um allows you to run the on like it's

**Dave Jones:** not the real chip on there, but it emulates the real chip in hardware, and then you've got all your pins and you can connect it to your device under test. So, this basically simulates the chip and it and it simulates any of

**Dave Jones:** their um size chips, any of their packages, cuz you can get them in much higher uh pin counts than this. Anyway, we're going to get this up and running. So, thank you very much for to uh Paduak for sending that in. Now, I just heard

**Dave Jones:** back from Paduak that they don't uh actually offer factory programming services, but they think uh you should be able to get that done at one of their authorized uh resellers. And as it turns out, uh LCSC are not and well, yet, I

**Dave Jones:** guess, an authorized reseller of Paduak parts, but that doesn't mean they're fake. Um, they actually buy LCSC actually buy them from authorized dealer, which is uh Shenzhen Foresight Technology Co. And you go over to their website and well, it's like, yeah, okay.

**Dave Jones:** Um, I think you probably need to know Chinese to uh uh deal over here. But, they do actually look, they do actually have the ICE uh programmer down here. It's the same price as uh sorry, the ICE the

**Dave Jones:** in-circuit emulator is the same price as the programmer, and that's 460 uh yuan there. And what's that in Yankee bucks? That is uh 66 Yankee bucks for the programmer and the ICE. But, of course, uh it's more expensive than that from

**Dave Jones:** other dealers, but that's one of their authorized uh dealers. So, there you go. Um, I've yet to find out if you can actually I've asked LCSC but they haven't gotten back. If they do and you can actually get them

**Dave Jones:** factory program from them through the authorized provider but supplied by LCSC, I'll update the description and leave a sticky comment down below because the value proposition for these parts always comes down to whether or not you can get them factory program.

**Dave Jones:** There's no point paying 3 cents for your microcontroller if you have to program each one, take it out and program each one individually in here. The time and money wasted you may as well just you know get the 40 cent microchip

**Dave Jones:** pre-programmed parts straight from the factory. So, like really it all hinges on that in terms of viability for these types of parts but like it's amazing that LCSC can sell these for three under three cents like in in large quantity 60,000

**Dave Jones:** which is not a lot really in the you know in the mass volume scheme of things. You know two and a half cents let's you know I I call this the three cent micro but really you can get it for

**Dave Jones:** less than that. That's from that's like not even from the official distributor. So, what are they making like one cent each? You know LCSC make their one cent, product make their one cent and their official distributor of that

**Dave Jones:** that they LCSC are buying from they make their one cent. It's crazy. So, let's have a look at the software shall we? I won't take you through the website but if you go to the website you can download you can get the data sheet

**Dave Jones:** for these chips in English. So, we've got the 154C which we're going to compile for but today we're only going to run it on the in circuit emulator. We'll do I have to do another video for the actually getting the real program

**Dave Jones:** using the programmer and then actually program the real chip put on the breadboard and doing that. But if it works on the in circuit emulator we shouldn't have any problems translating in theory translating over that to a program. Anyway, everyone wanted me to

**Dave Jones:** see um if I could actually get how easy it was to get a program running on these 3 cent microcontrollers with using like this weird-looking um IDE interface, which actually turns out to be quite nice. Anyway, you download it. It's like

**Dave Jones:** a 3 meg executable. It installs 0.83 version for those playing along at home. It's the FPAA, which is a field programmable processor array. Um so, it's kind of weird. And then we've got the writer. So, once we've compiled it,

**Dave Jones:** I assume we can just write it. But we haven't tried that. So, let's run this. It's a single XE. It's only 3 meg. And bingo, welcome to Padauk software. Thank you very much. And this is like just a a

**Dave Jones:** change log or whatever. So, let's go in and create a project from scratch. It's not easy. We still haven't found any sort of like uh you know, processor architecture manual with all the instructions listed and stuff like that.

**Dave Jones:** So, I've had to cobble this together, but it didn't take long to figure out all this, like an hour or uh two, you know, tops to to figure this out. So, we cobbled it all together. Don't have everything fully understood yet, but we

**Dave Jones:** can get a LED flashing. So, let's do it from scratch. New new project. Okay. Now, they use what's called mini C. This doesn't appear to be a thing. Apparently, it's their own thing. Um or you can choose ASM, uh for example. Um

**Dave Jones:** but we're going to do the mini C. So, it doesn't look to be exactly, you know, like ANSI C. I like It seems a little bit strange, but it's C-ish. Let's do a project called toggle bot, shall we? We can select our chips.

**Dave Jones:** So, these are all the different chips that we can select. Well, let's do the 150 C, shall we? Uh select device. PMS PMC serial AP serial. I'm not quite sure what that is yet. So, we're going to leave it default. Now, frame as sysclock

**Dave Jones:** IHCR on two. So, these are the internal various internal clocks. We'd have to have a look at the data sheet. There's like the 8 MHz economy oscillators that like the low power oscillator or whatever. Anyway, if we choose sysclock equals IH

**Dave Jones:** RC on two, we can get that working and we can actually call up some help for that. There you go. They tell you executing IC under sysclock represents the most simple architecture which only needs to provide single easy

**Dave Jones:** frame. But at least we get it in English, right? Even if it is Chinglish. Anyway, it's it's actually got a surprising amount of help available for this thing. So, actually quite impressed. So, these are the different oscillator options. One key plus 10 second LED.

**Dave Jones:** There you go. I Let's just get up and running with our program, shall we? So, we'll leave that the pin five here, PA5, port A5. Pin can be an open drain or a reset pin. That seems to be common across all their

**Dave Jones:** chips. We'll disable the watchdog. So, let's go. Oops. Found this bug before. Um it's You see, it didn't generate what we want. I think because I called up that help file. Oh. Right, so let's try that again. I won't

**Dave Jones:** touch anything else. Go okay. And bingo, we've generated our new template. And it includes extern.h which is the header file all the externals. This void FPPA0, that is like main. So, think of that as main. They don't actually call it main,

**Dave Jones:** but that's what it is. So, you know, as I said, not exactly standard C. And it's just IC sysclock IRHC on two. And look, there's open help here. You can move your cursor down here. You can actually pop up the help.

**Dave Jones:** Look at this. Briefings user who the paddock, I see it first time might be curious about the instruction. This is great. This is like they've gone to really tried to write all this English help, and it's it's all there. I'm quite impressed by

**Dave Jones:** that. How do I shut down that frame? There we go. Got it. Okay. So, it's generated our template. So, we put our code in here like this. It's all automatically generated an interrupt, but we haven't we can actually get this

**Dave Jones:** running. We haven't tried to delete the interrupt yet. Small step at a time. So, you're basically following through as we're as we're really learning with this thing, but this is our main. So, we can type our code into here. Let's go. And here

**Dave Jones:** we go. We can if we want to see what's in extern, we can go open document extern.h and It's not much in there, is there? Um that's it. It's a bit disappointing. Get back. Anyway, so I'm going to put some code in

**Dave Jones:** there to define just a LED out. Um and that defines the port PA.0 and pin zero, so port A uh pin well, port A pin zero, I guess. So, in while here, we'll just put LED out equals zero, LED out equals one.

**Dave Jones:** So, all we'll do is simply toggle a pin. That's it. And it'll just keep repeating in our while uh main as I said, this is main.c as you might be familiar with in your regular embedded programming. And uh

**Dave Jones:** that should be it. We should be able to run that. Although, this interrupt routine, I haven't tried to take this out yet, so we can add a command just to disable interrupts just in case. So, there we go. We can go uh disGint

**Dave Jones:** uh which is found that and copied it uh from somewhere else. So, that's global interrupt disable. That's our code. And we should be able to now run that and compile. Let's try it. Now, our options up here, here we go, build.

**Dave Jones:** We've got rebuild all, we've got stop build, boom, and then we've got go. So, let's just build it. Enable security, so we can actually I didn't know it had a security bit. There you go. So, we can disable security. Um drive a low or

**Dave Jones:** normal. I I I didn't know it had variable drive on the output. That might be like drive capability slew capability. So, um I don't know. I haven't read the data data sheet in detail yet. I'm just running it. Uh the low voltage reset

**Dave Jones:** uh thing. We won't worry about that. Boot up time, slow or fast? No idea. Let's just By by default it's set to slow. That's fine. I Once again, I have not found any um options. Oops, LVR is too low. Please

**Dave Jones:** refer to IDE help on LVR. I goofed it. Anyway, there's our compile. So, I still don't know where the compiler is, what it's it's using this mini C compiler or whatever. I don't know. I haven't looked into any of the details um of that, but

**Dave Jones:** interrupt was not used NB bypass. NB bypass. Great. LVR LVR must be greater than 3 V at sysclock IHRC on two. Fine. We'll do that. So, we'll set that to three. LVR there. So, we'll go back. We're all

**Dave Jones:** happy. By the way, I forgot to set up your have to the PA is the port and PAC is the control register for that port. So, the output direction, we have to actually set up the output if you want a pin to

**Dave Jones:** be an output or an input, you've got to set that up. So, we're going to set LED out direction equals one. So, we'll just set that into our in initial code at the start of our main before we hit the

**Dave Jones:** while loop here. Well, let's compile it, shall we? So, look. Yay, zero errors, one warning. Winner winner chicken dinner. Interrupt not be used and be bypassed. That's fine. I'm I'm happy with that. So, let's actually run it. Oh, by the way, there

**Dave Jones:** is a 9-V input on this, but you don't seem to need it. It powered from the USB. Great. Fine. So, we're not sure what the deal is there. We don't have a manual for this. We have no idea. We're

**Dave Jones:** really running blind here, but let's let let's run it. There is no indication of power or anything at the moment. So, let's go to here and go. We found a bug in this. You got to press go once like

**Dave Jones:** this. LVR equals up. Pop. Popped up for a minute. And we get some nice stuff. Look at this. You know, we get like it looks like register. That's the memory dump. Let's we find it it didn't actually run straight away. You have to

**Dave Jones:** go You have to go go go. You have to enter go go mode by pressing it again by the looks of it. So, it's really it's really strange. So, let's do it again. Now it runs. We get a

**Dave Jones:** flashy flashy flash flashy flashy thing. So, now I'll hook up my logic analyzer to the pins and we should be able to see it toggle. So, there you go. We'll just connect up to the first pin that port A

**Dave Jones:** zero pin PA0. Let's bring in my logic analyzer here. Start sampling. Ta-da! Winner winner chicken dinner. Our 3-cent micro is working and that's how easy it is. And as I said, probably like within an hour of just around not even

**Dave Jones:** having proper manuals, we can get this to work. Oh, by the way, it's 2 MHz which is half as what it's supposed to run at. We found something that mentioned that the ICE potentially runs at half the speed. So, I still like

**Dave Jones:** that's that's what they say. So, anyway, yeah. So, I think it's a maybe it needs to do its icy stuff in the background and and whatever it is. Anyway, it recommends that you run it the processor at twice the speed to what you actually

**Dave Jones:** need. But there it is, it's toggling. We've got a pin toggle at 2 MHz. It's not a 50% duty cycle cuz it needs to do its it it needs to loop back or whatever. Now, you might actually notice

**Dave Jones:** something interesting up here. Look at some of the gaps between Look, the the duty cycle of these is actually different, right? It goes to 2.4 MHz, 2 MHz, 2.4 MHz. What's going on? Well, this is actually a trap for young

**Dave Jones:** players with timing analysis mode on logic analyzers like this Saleae logic analyzer, but any logic analyzer. Basically, it's because we're trying to measure a 2 MHz signal at a 12 megasample per second rate here. So, if we actually go higher than that, 24

**Dave Jones:** megasamples per second, it's because we don't have the the temporal resolution to actually get the always get a correct accurate frequency on there. So, really 24 meg will still kind of see it. So, we'll sample now at 24 meg, but you'll notice

**Dave Jones:** that periodically it's showing these sort of like it changes the duty cycle like that. And that's just a nature of the sampling. And it'll get worse the lower your sample rate goes. So, if we go down to say eight, it'll

**Dave Jones:** should be like really terrible, Muriel. Well, it's different Yeah, anyway, look at that. I mean, well, in fact, look at that. At eight meg, there's whole sections where there's just nothing there. So, just be careful of that when

**Dave Jones:** you're using your logic analyzer. So, even at 24 megasamples per second, there will be like it'll show you like 2 MHz everywhere on both of the different duty cycles here, but there'll be one point where it switches over there. Just gets

**Dave Jones:** out of whack a little bit. There it is, 2.182 MHz. So, that's just the the sampling resolution that we've got here, but it tells you it's 2 MHz in here, and it tells you it's 2 MHz in this section

**Dave Jones:** here as well. So, you know that's right, but just that little change over point. Timing mode sampling rate, it's a big deal. And the good thing about once you've actually compiled this is that you can actually like hover over your variables

**Dave Jones:** and stuff like that. It shows you your stuff. You can hover over say port A there, and you can right click on that, and you can go to go to definition of port A. And there you go, you can jump

**Dave Jones:** over to where it actually defines port A in the Does it tell you what file? We're currently Oh, inc. Yeah, there we go. PMS150C inc. So, that's the include file. Please don't change the following code. It's only used for the for

**Dave Jones:** internal engineer. I love it. This is great. Um so, there you go. That's the include file that sets up all your you know, your registers, your ports, your timers, and there's TM16 for example. So, we can we we have that

**Dave Jones:** here. Interruptor, go to definition of in interrupt queue. There you go. So, you know, it's all there. It's pretty cool. But, that's all it took, really. It you know, there's a bit of a bit of learning curve there. May maybe we got a

**Dave Jones:** bit lucky in you know, finding things easier than what other you know, if you're having a bad day, Murphy's over your shoulder, you know, you may not be able to have found all this stuff, but anyway, that's pretty groovy. I like it. It

**Dave Jones:** worked a treat. Now, why do we have to do I I HRC on two? I'm still not Can we go like divided by one? Can we do that? Let's Let's just Let's just build. Just build. No. Didn't like that at all. Wasn't a happy

**Dave Jones:** little camper. But anyway, we still don't know why you've got to generate that why you've got to go. You've got to go go. It looks like it It sort of like stops at the start there. Maybe it's like It looks like maybe it's in

**Dave Jones:** breakpoint mode or like a a single step mode or something like that. And yeah, I'm not sure. It's literally the first time I've used it. Okay, now we've got a basically the same thing here, but what we're going to

**Dave Jones:** do is we're use the timer. So T16 so it's 16-bit timer here and we've just got some extra code here. Oh, I've got to take this out. I was just sticking around here. A code which will use our

**Dave Jones:** timer here and now it will toggle our pin slower. Hopefully, we'll get a 1 Hz square wave out of this thing. So I we haven't figured out like delays and stuff like any sort of like delay routines and stuff like that we've got.

**Dave Jones:** So we're just using the timer. There you go. So interrupts not being used. It's just warning us. Use We use four memory. Remains 60 unused memory. So we're using four bytes of memory or 60 you know four words of memory and we've got 60

**Dave Jones:** unused words of memory left and ROM ROM size for the 160 last year's code remain free. There you go. Plus 358 hex for those playing along at home. Do your conversion. Anyway, let's go go gadget. Let's go back to our

**Dave Jones:** Saleae logic analyzer here. Taking 10 seconds worth of data now. I'm a bit overkill on the on on the data there, but there you go. Point It's 1.003 Hz. Of course, internal RC oscillator so it's not going to be absolutely precise,

**Dave Jones:** but good enough for Australia. Like you know 3 mHz out. I'm pretty happy with that. So, there you go. There's our that There it is. We can toggle. And that's all there is to it using the timer thing here. And once again, like I

**Dave Jones:** haven't tried to like look at like haven't single stepped, I haven't done, you know, set breakpoints or anything you know, fancy at all. Just wanted to get a LED flasher up and running, but I know you want to see a LED flash. Okay.

**Dave Jones:** the tongue at the right angle. Please excuse the crude to the model. Didn't have time to build at the scale or to paint it, but there you go. We have our flashing LED. Woohoo! Our blinky. We got the blinky.

**Dave Jones:** Winner, winner, chicken dinner. So, there you go. We actually used this thing without too much mucking around. There was you know, a bit of like going I don't know, you know, try this to get it up and running, you know, cut and paste the

**Dave Jones:** examples. They do have examples by the way. They got some demo projects, but none of them are the processor that we're using, I don't think, but yeah, let's have a look at that stop sys t t six so timer 16 key LED ADC get VDC GPC,

**Dave Jones:** you know, they've got some I don't like PWM There you go. So, maybe we can like open up PWM project and have a look at this. So, you know, they've got some example code which you can copy and it

**Dave Jones:** seems to be their own mini C whatever it is that you know, it would have been nice if they just written it for GC support for GCC for example. That would have been great, you know. So, I don't know why they did that, but

**Dave Jones:** somebody could easily write a G GCC thing, couldn't you David? Yep. Yep. How how long do you think it would take you to write a GCC port? Fat put in padook. 3 weeks. 3 weeks. There you go. 3 weeks.

**Dave Jones:** I broke a partially broken one. Partially broken GCC port. Yeah. But there you go. Like we were able to get to Blinky with not much trouble at all. Granted, we had the in-circuit emulator. The next step will be of

**Dave Jones:** course the programmer. So, this will be a part two video where we'll program the chip, make a little programming adapter for it, but I'm sure it works. The writer program haven't even loaded up OTP writer. There we go. So, load file.

**Dave Jones:** Don't even know auto program rolling code. Um is that like serial code generator? Whatever. Anyway, I like it works. And their interface is actually surprisingly good. Um you know, it's got color syntax highlighting. It's got context sensitive uh stuff. Their

**Dave Jones:** help seems, you know, surprisingly comprehensive considering that there's Well, not that I've found. There might be like a processor manual or whatever that lists all the assembler code. Haven't done assembly yet. Still not sure what the deal is and all that sort

**Dave Jones:** of stuff. But this mini C, they call it, we're able to get something running. And some people may go, "Well, I wouldn't trust this thing at all. Like some, you know, obscure Taiwanese company making their 3-cent microcontroller with their

**Dave Jones:** little 3-meg IDE using mini C and non-standard stuff. I wouldn't trust it at all." And well, you know, fair enough. But at the end of the day, if it works and you have use for a 3-cent in fairly lowish volumes, you know, only

**Dave Jones:** 300-plus volumes, 3-cent microcontroller, if you can program the things, then you know, like and it works and you can test and verify that it works and you can still get them from LCSC. They keep them in stock by the looks of it. I have

**Dave Jones:** asked them if you can actually order these pre-programmed. They're still getting back to me on that. So, maybe I'll update you in the next video. I haven't heard back from. Might give them another poke. Pun intended cuz we're talking about

**Dave Jones:** programming. I'm here all week. So, yeah, like the the value proposition if you can't get these programmed and you know and if this is your only programmer and you need to program 10,000 of them, it's kind of going to

**Dave Jones:** ruin your day and takes away the value proposition of the 3-cent micro. So, it like so the value of these in volume hinges on the fact well, hinges on whether or not you can get these pre-programmed from the factory. If you

**Dave Jones:** can, that that's killer. You can simulate your code on the ice and you can actually get it running. You can experiment and you can you know do all sorts of stuff. Then you can program it. You can verify your code. These micros

**Dave Jones:** only can you know very small programs on these, so it's not hard to So, you could like verify a complete micro. You can test it over voltage and temperature and and you can qualify these things yourself. It's not necessarily difficult

**Dave Jones:** if you have the means to do it. And you know there are people who will say, "Well, you know, just go for a 30- or 40-cent or what I think it's 40-cents for the lowest cost uh PIC that you can

**Dave Jones:** order pre-programmed from the PIC factory. It's got industry standard support, etc., etc." And well, you know, yeah, that's a valid argument, too, but 3 cents. I just love it. It's great. There's got to be niche uses for this. This is fantastic. Anyway, if

**Dave Jones:** you like the video, please give it a big thumbs up. And if you want to see us program stuff and things like that and get something running and we're thinking about now that it's all working and now we see how I'm sure we'd be able to

**Dave Jones:** program this thing. Shouldn't be too much effort. Thinking about a big project that needs like you know 10,000 of these things. That'd be great. Mhm. Somebody actually bought up 10,000 of these after I did the video. Somebody went and purchased like 10,000 of the uh

**Dave Jones:** SOT-23 version or something. Anyway, I've got the SO8. I've got some SOT-23s. I've got some other variants of it um as well. So, yeah, we might be able to do some interesting projects. Anyway, comments down below. Catch you next time.
