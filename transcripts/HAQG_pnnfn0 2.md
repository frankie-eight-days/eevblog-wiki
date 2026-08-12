---
video_id: HAQG_pnnfn0
title: EEVblog #1306 (4 of 5): Open Source SDCC C Compiler
url: https://www.youtube.com/watch?v=HAQG_pnnfn0
source: youtube-asr
timestamps: {"0": 1, "1": 30, "2": 60, "3": 85, "4": 117, "5": 139, "6": 160, "7": 190, "8": 218, "9": 230, "10": 255, "11": 292, "12": 323, "13": 339, "14": 358, "15": 384, "16": 413, "17": 442, "18": 470, "19": 485, "20": 516, "21": 540, "22": 556, "23": 587, "24": 615, "25": 651, "26": 665, "27": 683, "28": 708, "29": 739, "30": 760, "31": 800, "32": 828, "33": 860, "34": 889, "35": 919, "36": 950, "37": 964, "38": 987, "39": 1026, "40": 1064, "41": 1089, "42": 1129, "43": 1159, "44": 1192, "45": 1208, "46": 1244, "47": 1279, "48": 1301, "49": 1328, "50": 1349, "51": 1380, "52": 1403, "53": 1434, "54": 1451, "55": 1473, "56": 1496, "57": 1529, "58": 1547, "59": 1571, "60": 1591, "61": 1609, "62": 1630, "63": 1649, "64": 1673, "65": 1698, "66": 1716, "67": 1749, "68": 1767, "69": 1785, "70": 1801, "71": 1842, "72": 1862, "73": 1876, "74": 1893, "75": 1915, "76": 1935, "77": 1947, "78": 1975, "79": 2006, "80": 2029, "81": 2047, "82": 2083, "83": 2111, "84": 2142, "85": 2167, "86": 2207}
---

**Dave Jones:** Hi, welcome to part four of the Padauk a three cent microcontroller programming series where we build up open source hardware and software to program these three cent microcontrollers. Now, in part three, we looked at uh in we got our programmer up and running. We installed the firmware on there using DFU mode. So, in theory, the programmer is ready to go, but we haven't tested it yet. So, this video is actually going to be about uh using the SDCC or the small device C compiler. And this is a

**Dave Jones:** compiler that supports the Padauk microcontroller. A lot of people on the EV blog forum actually worked very hard to get all this stuff working. So, we now have a proper ANSI C compiler that supports the Padauk. So, yeah, can we actually use this SDCC to actually compile a program for one of these Padauk microcontrollers so that then we can generate an Intel hex file to then use in the next part to actually use the programmer hardware to program it.

**Dave Jones:** Sounds easy, but as usual, you know, there's lots of hoops to jump through. Right, so how do we program these Padauk microcontrollers? Well, of course, you've seen in my previous video on this we can use Padauk's software, which is C-like, kind of. It's not really C. It's Padauk's C. And the whole point of this is now that you can use an open source like proper ANSI C compiler to do this.

**Dave Jones:** And to do this, someone, I don't know who, Sorry, if I can find the name, I'll put it up. CDC small device C compiler. And this is an open source C compiler, and it's regularly updated. As you can see, it's you know, just updated in January 2020 4.0 release. And it supports all these architectures, 8051, which is now used in, you know, a ton of generic microcontroller from Asia because they're using little farting novelty gadgets and greeting cards and things like that because you don't pay any

**Dave Jones:** royalties on the 8051 architecture anymore. Um so yeah, that's got Rabbit 2000. I used to do Rabbit 2000 back in the day. Used to love the Rabbit 2000. Had like four serial ports on it. That was whoa, fantastic back in the day. And it also had a great deterministic real-time operating system as well. That was like really easy to use.

**Dave Jones:** Easier than anyone used the old uh Anyone used the Zilog Z80 micros anymore? Um STM8 and Paduk and PIC micros available as well. And uh yeah, so it supports I'm not sure if it supports all of the uh Paduk microcontrollers, but you know, it's going to support a good number of them. So in different various packages.

**Dave Jones:** Now, this is a command line uh compiler. As far as I'm aware, there's no um IDE or integrated uh development environment for it. Um so yeah, use your favorite uh note notepad plus plus or whatever it is uh you want to use to write your actual uh programs in. And then you can just um call the compiler. And there's probably like, you know, various scripts and things you can do to automate all sorts of processes. But the general thing is you write your text file containing your

**Dave Jones:** C program, you run it through the SDCC uh compiler, you tie you know, with a specific target to whatever Paduk microcontroller you're uh using, what part number you're actually using, and then it'll generate a binary file, which then we can use our newfangled programmer to program into it. So unfortunately, it's not like a seamless automated system like you'd get with your PICs or your AVRs, and it's all under one environment, and all just seamlessly works. And like, you know, you push a few menu buttons at the top,

**Dave Jones:** and it compiles and downloads and does everything for you. This is a bit, you know, it's it's a bit more tedious. And but these could get better um over time in terms of like integration support, scripting support, and things like that.

**Dave Jones:** But in this video series, the aim is just to write a standard ANSI C program, compile it using an open-source compiler, and then program it using our open-source hardware. So, you don't have to All you have to do is buy the microcontrollers from Padauk. You don't have to buy their secret squirrel hardware. You don't have to use their secret squirrel C compiler integrated environment and things like that. It can all be done using open-source tools.

**Dave Jones:** Cool. Now, which Padauk microcontrollers does this support? Well, it's a new in development a back-end for the PDK 13 with which is a 13-bit, which is uh the developers' names for the 13-bit wide program memory architecture. And like previous releases down here, they've actually added support for the PDK 14 as they call it, the 14-bit wide memory, and the 15-bit wide memory architectures as well. Now, if we go over to the GitHub's for the free PDK, as you can see, they've got the programmer software. They've got uh code examples.

**Dave Jones:** They've got uh looks like evaluation boards. And they've got documentation for the programming architecture. Then they've got the programmer hardware, which we've just built. And they've got an emulator as well, VHDL emulator to emulate the core. That seems pretty cool. So, yeah, you don't even need to buy the micros from Padauk. Um you can put it in an FPGA. I don't know. Does anyone want to try that out? Give it a bell. They've got disassemblers as well, and they've got code examples and stuff.

**Dave Jones:** Like, wow. Hats off to everyone who's contributed to all this because it went from, you know, this weird obscure Asian brand uh micro with Yeah, you had to buy the programmer. You had to use their quasi C like compiler, and that was it.

**Dave Jones:** To now, it's like it's They've practically completely opened the whole thing. Amazing. All right. So, if we go into code examples over here, here we go. Um this is from like 2 years ago. It's been around for quite some time, but let's try and just blink a LED, shall we? Simple blinking program.

**Dave Jones:** Um so let's go to the simple blink sub subdirectory here. We've got our our C program. That's it. We don't want our project or pre you know, we'll just like could. But anyway, we've just got our C program. Here it is. Simple blink program. That's all it does. And look, it's incredibly simple. Then you've got port A C. I don't know what the labeling is. Anyway, it's that port and that pin.

**Dave Jones:** So it doesn't matter whether you're using an eight-pin PIC micro or using like a 14-pin one or whatever size chip you're using, it'll have all the just the different ports on there and you can choose whatever pins you want. So that's actually bit three on there and then you can use the pinout diagram of the chip to actually translate. We've got that over here somewhere. Yep, that's over here. There you go. PA3. There you go. Is actually this pin down here and I believe the eight-pin chip will just

**Dave Jones:** use the bottom eight pins down there. So it's the same pinout. So it's got VCC and ground like that. And on the 14-pin chip, they're in the middle, but on the eight-pin chip, the pinout should be exactly the same. So PA3 will be this pin down in the bottom right corner down here. And that's the pin that we're going to actually toggle. So we'll just download SDCC here. Let's go to the download page. Win 64. That's the one we want. Version four cuz that supports the

**Dave Jones:** latest one. You always want the latest. Don't always want the latest version. Might be some obscure reason you might want to use an older version, but anyway, let's just run that. And oh, set up. Nice. 300 other people have downloaded it. Yeah, we want to include Oh, there we go. That's include support for everything, shall we? There we go. We can get uh 13, 14, 15. And I don't know what the stack auto library is. No idea. But, we want to insert Should we like you could just disable

**Dave Jones:** everything else, but it doesn't matter. I'm just going to go, "Yep, install." Install. No wackers. And all there there's all the pick files, there's all the header files. We'll see the PDK header file shortly. Blink and you'll miss it. Blink and you'll miss it. Whoa, missed it.

**Dave Jones:** Oh, hang on. I looked at the simple PDK code examples. Is that different to the SDCC PDK code examples? Uh-huh. Yep, I think this is the one we want. Come a gata. Count PFC 151154. Don't know what chip I'm going to be using yet. Let's do hello. A timer LED example. So, it's going to flash a LED, is it? For the I don't know. Um looks like they've got like a demo board.

**Dave Jones:** thing. So, I don't have a demo board. I'm just programming the chip. So, here's these eval boards. Let's go to the SO8. It's just got schematic. No, what's No. Got a SCH. Hmm. No. Let's not go there. Anyway, count.c. Let's have a look.

**Dave Jones:** What's in there? A four-bit counter for the Paduak 151154 161 blah blah blah blah count seconds from zero to three in binary using two LEDs on the lowest and highest ports of port A written by Philip Kraus Kraus Klaus Kraus.

**Dave Jones:** There's no way I'm going to be able to pronounce that correctly, I'm sure. Anyway, um standard bull.h. Okay, this is more your familiar C stuff. So, your C aficionados are going crazy. Now, I'm actually starting to think that this simple PDK code example that we looked at that is actually only going to work within the Padauk environment. So, we don't really want that. We want uh ones that work for SDCC.

**Dave Jones:** Yeah, so it looks like we should be using this SDCC PDK example, which unfortunately is a bit more complicated to set stuff up. Now, if we go into the uh bin directory of what our SDCC SDCC compiler has installed, we'll find that like there's uh S51 for example, so that'll be the 51. Yep. Uh whoop. Let's get Helps if I type it right.

**Dave Jones:** SDAS PDK15 boop And there you go. Uh that looks like our That's the assembler written by Alan Bowden. Good on you. Awesome effort. Um absolutely no warranty implied, but uh yeah, so this is what the compiler will call It'll call up this assembler, which actually does the actual hardcore work. It'll actually call up this assembler when we uh tell it to target the Padauk microcontrollers. It'll know to call this up. So, unless you wanted to write Padauk assembly language for example, because the whole idea of the C compiler

**Dave Jones:** is that the C compiler then converts it into assembly language, and then the assembler actually compiles it into the binary. So, yeah. Um it's just calling this up. So, unless you want to write assembler, you wouldn't muck around with this.

**Dave Jones:** But we can run our SDCC and whoa There it is there. Um There's lots of options. Lots of special options. Uh we probably shouldn't have installed all of the micros. We should have just installed the Padauk ones. So, there's the Z80.

**Dave Jones:** Uh you know, it's all different standards it supports for those playing along at home. If we go into our free PDK section here, we can find the instruction set. There you go. So, let's go for the 15-bit instruction set. And it's just a HTML file that will give us the instruction set, so we can download that. So, there you go. If we call that up, there's our 15-bit instruction set.

**Dave Jones:** Cool. Wow, somebody's gone to hats off. That's a lot of effort to reconstruct that and get it right. I'm sure there were bugs in the early version, but you know, as people use it, it gets ironed out and it becomes rock solid. Sweet. Unless they make changes to the hardware. So, I thought I'd just have a googly search for integrated development environments for SDCC. It looks like there's one this SourceForge one IDE integration Eclipse perhaps.

**Dave Jones:** There's this Xanadu one down here. I don't know. Some hardware vendors create IDE bundles support for their hardware. Oh, the Penguin know IDE bundle which is the PIC version. What about this Xanadu? An IDE for SDCC is integrated for small device C compiler.

**Dave Jones:** Sounds all right. Unfortunately, this looks very old like latest commit was 2017, but look, you know, and I don't even think there's I don't think it's a Windows one, so system requirements Python. Yeah, I Yeah. Nah. So, I thought what I'd do is just I'll use Notepad++ here. I cut and pasted this code for this. I don't expect it to work cuz I suspect it only works with the Padouk uh programmer you know, environment quasi C compiler, but it's worth a shot. Basically, you're just learning as I learn here. I'm just

**Dave Jones:** like going through until I get something that works. But, the good thing about this is that this is how you can expect to you know if you're in the same position I am. Oh, I want to use these Pinguino microcontrollers for something. You know, I've got a specific application. I got to build up the hardware. We've got to download all the stuff and figure out how all this works. And of course it I just ran a simple with no parameters whatsoever and it simply did not like

**Dave Jones:** test.c. It just wouldn't pass it at all cuz we've got the dot in dot delay there. So, yeah, it doesn't like that. That's a Pinguino thing. By the way, I looked in this timer IRQ example, which is an interrupt example, and it seems to mix. Like here's some original code that they copied, original mini C code, and then they looks like they're mixing like this is how you mix ASM. You just go ASM engine int. Don't know what that is. Maybe hello C. I like the idea of hello C.

**Dave Jones:** Does it simulate a serial port or something? It outputs a string hello world at 9600 baud one stop. That's what we want. Good on you, Philip with two P's. Wow. So, here's all the code. So, this is like you know, it's once again they're mixing ASM. They've got engine int. I don't know what that is here. So, it's not the world's simplest stuff like I'm not the world's best program like SFR at address, you know, I mean yeah.

**Dave Jones:** He's factory calibration code and all this sort of stuff. So, it's not the it's not the easiest thing to use if you're a newbie, that's for sure. But anyway, it's going to use printf. It's going to put like it's going to call the code. It's going to assemble the code, include the code for printf. I don't know how much memory that will take cuz printf is usually you know, quite a memory hog. Many times I've had to avoid using printf on small micros because of you know, it

**Dave Jones:** can take one or two good couple of kilobytes of program memory just for printf for example. So, yeah, you can really come a gutser on that. So, anyway, we seem to be able to use printf here, but it's probably optimized it you know, good optimizing compiler will take out stuff you don't need and things like that. So, anyway, I like I like the idea of having a hello world example running on my that outputs a serial port. I think that's a very worthy example. So, I'm going to copy that and we'll just

**Dave Jones:** paste that in here. There we go. And we'll save that as our test.c. And I like that it's got color syntax highlighting. I can remember when that it was introduced. That was a big thing. You know, color syntax highlighting your code.

**Dave Jones:** So, here we go. Let's try this again. I once again I've got no target whatsoever. I haven't used SDCC's before, but it seems to simply go in and at least at first pass the code. Absolute address for SFR probably out of range. Probably we don't care about probably's. We deal in absolute's. Only a Sith deals in absolute's.

**Dave Jones:** Um Probably out of range. We don't care about that. Cast of literal value to generic pointer. I don't know. They're they're only warnings. They're not errors from type constant unsigned in literal. I error for F open failed to failed on file test.asm. Yes, because we haven't specified I presume because we haven't specified an assembly target. A particular Peduque or some other microcontroller. Z80, 8051, whatever it is. It's just compiled that C program for us. So, that's what it does. Like it compiles the C program and then it

**Dave Jones:** it converts the C program into assembly language cuz we haven't told it a target. It goes what architecture do you want me to assemble this thing for? I could just uh you know, go for an example somewhere and maybe someone's got like a command line uh example, but uh help verbatim's execute Actually, I like to execute verbosely. Compile and assemble, but do not link. Uh preprocessor Do we have to do {dash} m and then put PDK or something cuz it's used the EG example of the Z80 and then you got to

**Dave Jones:** select the specific processor. Whoa, yeah, I can muck around with it for a little bit while. I'll see if I can find a uh command line um example just to do it. Just to get us started. That's the best way. I mean, you know, you can learn to do it by failing here. That's fine, but um yeah, when in doubt, RTFM.

**Dave Jones:** So, when in doubt, wow, they've they've really gone to town on this. Um it looks like though, they have a wiki. So, let's go over to the wiki. Oh. Uh The wiki's goneski. Oh well, maybe somebody didn't update that. Anyway, let's see if we can find some command line options. So, what I did is just search for the word padauk and uh there you go. {dash} MPDK13 uh for the 14-bit better figure out which one I'm doing it for, but let me just try the 15-bit wide one, shall we?

**Dave Jones:** So, can we just do that? And try it? Nope. Didn't like that. Test ASM. So, uh silly me, that's not for the SDCC. That's the Is that the linker or something? Yeah, yeah, yeah. Dumbass Dave. It's got specific uh entries on padauk intrinsic name spaces and stuff like that. Very nice. Looks like the Pedukas somehow tied to the 8051 type Oh, that's it.

**Dave Jones:** That's it. Where do we have processor target support? Processor selection options, there you go. That's what we want. Processor command line option. No, that's that's SD to manage libraries. No? Okay, we're back to where we were. All right, looks like it's going to be more complicated than I thought. And of course, where else are you going to find this but the EEVblog forum, which is I think pretty much where it all started with the original reverse engineering video from David 2. He was experimenting with like, you know, just looking at the

**Dave Jones:** signals from the Peduk. And I think it all sort of started to flow from there. Anyway, this is a message from JS blah blah blah, lots of numbers. And down here we've got an example commands to compile. Here it is.

**Dave Jones:** I I was right. SDCC MP DK14. Oh, and I didn't put the dash C, but I didn't have the extra stuff, but I was I was close. I was close. So anyway, we should just be able to put that, I guess. So if we do the example they got there, SDCC MPDK15-C test.asm, it doesn't work. And if you add in the dash O and test.rel or whatever, it it just gives you the same thing. And by the way, that line 105 there, where it's getting the error, the program's only

**Dave Jones:** 104 lines long. So the 105th line is just basically saying that it can't find it can't open the file test.asm, which it would which is what it would have generated if it knew what processor target it was compiling for. Cuz you can't compile to an assembly file unless you know your processor a And I think uh SDCC just assumes it's 8051 target um if you don't put anything. Oh, I figured it out. It was simple. Um, I was actually running the program. I had my source file in the

**Dave Jones:** Windows program files subdirectory and I was calling it up from there and that's actually a Windows protected subdirectory. So, it wasn't actually able to write. It was Windows actually stopping it from being able to write to that same subdirectory. So, I just created a subdirectory called, you know, /a on my C drive and that's where I put my files and here we go.

**Dave Jones:** There we go. I just had test.c in there before. Now, I've got test.asm, test.list, test.rel, test.sim. Ah. Unbelievable. Dumbass Dave. So, what we have to do here is this multi-step process that's produced this rel file and then we've got to do it again. So, then we just have to go test.rel like that and then the output Oh, no, sorry. Got to take out the dash C there.

**Dave Jones:** And then test.rel and then the output file test. uh ihx, which is the Intel hex format file and that should work. We should now have ta-da! There you go. 936 bytes in all its glory for a hello world program. That's pretty good when it's going to include like a printf thing.

**Dave Jones:** Um, that's great. Um, there's the Intel hex file. We can actually uh load that into here and it should actually display the hex file. There's our Intel hex file. So, that is what we can use to now program into our use our programmer software, our programmer firmware embedded here, put our chip in and then with the right right command line options in this, then you do it. Of course, yes, you could script and automate all this and maybe there's already somebody out there who's done all this so that or if you had, as

**Dave Jones:** I said, an IDE an integrated development environment uh specifically for well, that supported Peduino micros and supported this uh particular open source hardware and supported the SDCC and all that sort of jazz. Yeah, you could uh potentially just like, you know, push a single button, compile, and download program, you know, and like in one hit, literally one button press, it could compile and then program uh in one hit.

**Dave Jones:** Uh but it uses all these different command line tools to do that. But yeah, that's the value of scripting. So, there you go. That wasn't too hard at all. But yeah, you got to know what you're doing. It's not trivial stuff, but you know, even dumbass Dave was able to figure it out. But as it turns out, I've actually got a uh PMS131 chip in here, which in an eight-pin uh SO package, which curiously not even the data sheet has a pinout for. It's got like the 14-pin

**Dave Jones:** uh packages, it's got the 10-pin MSOP and stuff like that. But anyway, um so I assume that this is like the 13- bit word architecture. This one's I've got like a built-in 12-bit ADC and stuff like that. So, I'm going to go do MPDK13.

**Dave Jones:** Now, this is not uh tested yet like not like fully tested yet. So, So, anyway, I'm going to recompile that. So, I'm going to compile that. There we go. And then I'm going to Here we do remove the compiler, put in the rel, and then we put in the I hex like that.

**Dave Jones:** Ta-da! And we should have our I hex file for uh no, uh text. text I did text. Should be test. Oh. Anyway, text That's appropriate. We did a printf. text.ihex Actually, I'm going to have to rerun that again for text.rel.

**Dave Jones:** Confusing myself. Anyway, this is for compile for the 13-bit architecture, so All right, so we need to go back to our free PDK, the programmer software. We're going to have to figure out how to run the command line for this now. So, here's our install readme, and then it's got usage in here. Easy PDK program option, and then you can read, write, erase, start, and stuff like that. So, presumably, if you've got I don't know if Do they have copy protection? Anyway, um yeah, you can read back an existing

**Dave Jones:** So, if you have a product that has a product micro in it, you can read back the uh the binary file from it. So, so there we go. We specify our target, and uh we can read and write. There we go. That's what we want. {dash} n. What's {dash} n do?

**Dave Jones:** IC name. There it is. Yep, IC name. So, presumably, cross my fingers and it supports my uh 131 chip. Now, the thing is, where is the like executable? Where is the Windows executable? Well, now programmer source, but I want a Windows executable.

**Dave Jones:** Make file. I hope I don't have to build it. No, hang on. Okay, I keep going, and sure enough, browser open GitHub free easy pay releases. Ah, did I not see that? Okay, I must not have seen the releases. Awesome. Somebody's compiled it and released it. Fantastic.

**Dave Jones:** Okay, I now have that unzipped easy PDK prog. And what do we need? Uh oh, well, we can list uh first. There we go. Oh, it supports the 133 uh 131 PMS 131. That's the one I've got. Beauty.

**Dave Jones:** So, {slash} n PMS 131. Right. Oh, this is exciting. text.ihex Will it work? Um, it's got some leads on it. I don't know. I don't know if the uh the programming voltage hardware on here. We have still haven't tested that.

**Dave Jones:** So, I'm just going to go for broke here. Let's give it a whirl. Ah, right for this IC. Oh. Bloody Murphy. It's okay. I found my tubes of PMS 151's. Hopefully, that works. They're 8-pin SO as well. All right, let's do this again.

**Dave Jones:** So, I got to recompile for the I assume it's the 15 the fifth I assume the 151 is the 15-bit architecture. Probably a poor assumption on my part, but anyway. So, I'll do that and then I'll So, I'm doing test this time rel and then ihex ihx No definition of area home data.

**Dave Jones:** Ooh, link warning. Internal version error. Oh, that's interesting. Duh, did I forget to put the dash C in there? I think I might have. I think that might make a difference. Let's try it again. Okay. Now, we take out the C and we do the rel and we go to the ihex.

**Dave Jones:** Ta-da, winner winner chicken dinner. So, we have test.ihex there. Yep, there it is. 4:37, yep. That's right about now. Well, you can see the date and time that I'm making this video. Yep, we're good to go because it's a four-part video, you might not see this for like a week or two. Who knows?

**Dave Jones:** So, let's list again. Uh, PMS 15 4 Ooh, C or B? I've got C. PMS 154C. Pretty sure that matters. So, 154C. Write test .ihex. Fingers crossed. Um, will it go flishy flash and will it write it? Error. Command ack failed. Wrong ICID.

**Dave Jones:** Oh, ICID. Wrong ICID. Ah, what? So, it it tried to read the ID from the chip and it didn't, I guess. Is there a bad contact in my I've got the SO 8 adapter plugged in. I've got the chip around the right way.

**Dave Jones:** Ah, but yeah, these are the like all these little things are what you have to go through when you're using something like this for the first time or even coming back to it. Like I could do this now, come back in 3 or 6 month time and forget how to do all this. I'd have to watch my own tutorial or go to someone else's, you know. It's It's just nuts.

**Dave Jones:** So, no, or there could still be something wrong with the hardware. We could um cuz I don't know about the programming voltages. Maybe it needs it needs that to read out the needs that to be working to read out the uh ID. Let's try it again, just in case. No.

**Dave Jones:** Okay, definitely putting in a 154C. Aha, people are probably screaming at me, "Dave, look down this column here. The PMS 154C is a 14-bit in brackets. So, there you go. I've come a gata. I assumed You remember how I said before, I assumed that the 15 uh you know, 15X series would be the 15-bit. Uh-uh, it's 14-bits. And the 154 up here, which has the flash, they're all 14-bits. So, I need to recompile again with the Here Here it is. With the 14, right? That's probably why I can

**Dave Jones:** only assume that's why. Here we go. So, compile that again and then do that. Change it to 1 4. Test real test Intel hex. Okay, and now we can go to write that. So, let's try it again. By the way, there's one thing I noticed.

**Dave Jones:** All these chips have the numbers rubbed off them. There's not Well, not rubbed off. There's just no numbers on them. They're blank. Great if you want to copy protect your product, I guess. Um well, makes it harder, you know. Anyway, here we go.

**Dave Jones:** Turn it at the right angle. Uh Aha, we can use the probe command. There you go. Um thank you very much uh JS um all sorts of 1 through 855 AA. I don't know what that means. This is awesome.

**Dave Jones:** Um you know, this is what makes the EVblog forum great. It's basically the community members on here who have developed a lot of this stuff and you know, I couldn't find this anywhere else except the EVblog forums. Absolutely amazing. I probably wouldn't have figured out all this stuff all this myself. So, let's probe. Probe up the clacker.

**Dave Jones:** Probing IC. Nothing found. So, there you go. That's why. It can't read the ID. So, there could be something wrong with my contacts, with my SOIC adapter, could be something wrong with the chip, but that's, you know, unlikely cuz I got them directly from LC SC. They're an authorized supplier even though they got no numbers on them.

**Dave Jones:** Uh which is a bit of a worry. Or the hardware, um there could be something wrong with the hardware. That'd be cool. I'd have to debug it. I just tried the 1 3 1. I probed that and nothing found.

**Dave Jones:** So, yeah. Uh hardware maybe. Okay, I tried to measure the VCC pin on the chip when it uh like when I actually press program and I had to put in min-max mode capture mode to capture that. It only captured 0.55 volts. So, yeah, I don't know if it's simply too fast for the multimeter to capture or whether or not there's something wrong with the hardware. Winner winner, you know what?

**Dave Jones:** BMS 154 B/C, I guess they're identical. There you go. I see ID. What it was is that yep, dumb ass Dave missed the joint. Missed it on the inspection and yeah, I soldered that joint properly. It was on the DC-to-DC converter. So, that's one of the things that I didn't do in the previous hardware testing. And come with guts. See? If you don't test it, yep, Murphy will get you every time. Anyway, I thought I still had a problem because I tried it with the other chip which I

**Dave Jones:** think is because it's unmarked the 131 and it it it didn't probe it at all. But then I put this one back in and it's working. So, I don't know if the 131 is just it just can't detect it or what's going on. So, I don't know. So, don't just assume that you've got a good chippity do dah in there. I'll try it again. I think that's making contact.

**Dave Jones:** Not nothing. Anyway, the 151's a winner. The 154, there it is. So, let's go back and try and write this, shall we? Here we go. I was no there's no LEDs. I you may not be able to see that yet. Anyway, LEDs.

**Dave Jones:** Here we go. Done. Aha. Oh, and it's it's only one time program. I only get one shot at it, but done. The 154 without a letter on the end is a flash version because if you do this.list, it actually tells you the only flash part or the only two flash parts. One is the 154. I don't know, and the 154C is the uh and the B which we've got here, um which has got uh 2K words of memory, by the way. And as you saw before, we used 900 and

**Dave Jones:** something uh bytes. So, we're using like half the memory just to do a hello world. These things are not designed for huge programs, but printf takes a lot of space. So, you know, you could if you hard-coded that in like, you know, handwritten C or something like that, it'd be much better. All right. So, this writes hello world on pin zero of port A there. So, if we go have a look at our uh chip-a-di-dooda 154. There we go, the eight-pin jobby.

**Dave Jones:** Although, they're all the same. It's all in Chinese. Mandarin, you know, whatever. Some people have complained that I call it Chinese and it's actually you know, anyway. So, there we go. Uh pin zero, PA0. So, pin seven there. So, if we hook up VDD and ground of these 5 V or 12 V, I can't actually remember. Um so, if we hook up 5 V and ground, the good thing is that because I've got it in my socket, I can just take that off uh and stick that in my breadboard, and we

**Dave Jones:** can play with this thing. Although, as Luckily, I've got a lot of chips because they're one-time programmable only. But, you can buy lots of chips when they only cost like a couple of cents each. And yep, we can go to 5.5 V. So, there you go. Um that's handy. So, we should be able to hook this up and we should get hello world out, and we should be able to view that on the scope. Let's give it a burl. Will it work? After all this.

**Dave Jones:** How many videos? This is the fourth video. I haven't properly edited this yet, but this is probably the fourth video. It's like 2 hours worth of content or something. We're finally there. Almost.

**Dave Jones:** Mhm.
