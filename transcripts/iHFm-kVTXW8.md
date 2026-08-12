---
video_id: iHFm-kVTXW8
title: EEVblog #45 - Arduino, PICAXE, and idiot assembler programmers
url: https://www.youtube.com/watch?v=iHFm-kVTXW8
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 25, "3": 36, "4": 49, "5": 63, "6": 77, "7": 97, "8": 113, "9": 131, "10": 145, "11": 160, "12": 170, "13": 185, "14": 198, "15": 214, "16": 225, "17": 234, "18": 244, "19": 254, "20": 275, "21": 290, "22": 310, "23": 326, "24": 336, "25": 350, "26": 361, "27": 371, "28": 388, "29": 398, "30": 415, "31": 435, "32": 443, "33": 456, "34": 473, "35": 485, "36": 505, "37": 520, "38": 534, "39": 542, "40": 556, "41": 581, "42": 594, "43": 626, "44": 638, "45": 653, "46": 664, "47": 680, "48": 691, "49": 708, "50": 720, "51": 733, "52": 752, "53": 766, "54": 777, "55": 794, "56": 809, "57": 822, "58": 833, "59": 848, "60": 868, "61": 886, "62": 899, "63": 908, "64": 930, "65": 939, "66": 957, "67": 981, "68": 993, "69": 1009, "70": 1021, "71": 1035, "72": 1049, "73": 1059, "74": 1070, "75": 1079, "76": 1097, "77": 1105, "78": 1114, "79": 1129, "80": 1141}
---

**Dave Jones:** Hi, welcome to the EEVblog an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host Dave Jones. Hi, today we're going to talk about microcontrollers, but not just any microcontrollers.

**Dave Jones:** We're going to talk about a revolution that's happening at the moment and it's called the Arduino. I kept hearing about these damn things. Arduino this, Arduino that. Ah, every man and his dog's using them.

**Dave Jones:** So I thought I'd get one and check it out and see what all the fuss is about. Now the first thing we have to talk about is the stupid name and it really is stupid.

**Dave Jones:** Arduino. That's how I'm going to pronounce it anyway. But there's as far as I'm I know there's no official way to actually pronounce the stupid name. I think it's some guys in Italy developed it and I don't know it probably means something in Italian.

**Dave Jones:** I don't know. My Italian fans come on, let me know. Anyway, some people call it the Arduino, the Arduino, the silent R, the Addino and all sorts of things.

**Dave Jones:** But I'm Australian so I reckon it should be pronounced Arduino. Arduino mate. Hand me the Arduino mate. No worries. So, what is the Arduino? Well, it's not really a board like this.

**Dave Jones:** People think oh this board is the Arduino. But it's it's it's not really. This is just the generic um board for it. What what the Arduino is I guess is it's a whole development ecosystem based around an Atmel ATmega chip.

**Dave Jones:** A standard ATmega microcontroller. It's basically an open source development system and it's it uses the AVR GCC compiler but that's all hidden away. That's sort of you know, that's really not the point of it.

**Dave Jones:** Basically it's a it's a hardware and software solution that allows you to get projects up and running fairly quickly and expand them and it's you know, it it really is a complete development platform and it is based around it's semi based around this standard footprint.

**Dave Jones:** You can see these headers here. Now these headers actually you can actually there there are standard format for the different boards and you can actually step extend them with like all sorts of boards you can actually plug in like this.

**Dave Jones:** Okay, you can assemble things like this. This is called a wing shield. It's basically any board that plugs into an Arduino platform board is called a shield. Okay, so this is a shield.

**Dave Jones:** This is a prototyping shield and it and it they can all just plug together like this in different ways if I can do it. Geez, feel like a kid again.

**Dave Jones:** And look, you've got like a you know, this looks fantastic. Look at it. It's it's like a you know, a Star Wars shuttle or something like that. Cool. This board is the standard Arduino board in the range really.

**Dave Jones:** It's sort of like the base level one so that everyone gets to start off with. And once again, like as if the Arduino name wasn't stupid enough the guy said, oh what what can we call our main development board?

**Dave Jones:** I don't know, let's make up an even stupider name. This is the I can't even pronounce this. Unbelievable. The Demilenov Demilenov what? What? Unbelievable. Why can't they have decent names?

**Dave Jones:** Well, actually they do. There's other boards. There's like this one is the mini. Check it out. This is the Arduino mini and it's a really cool little board. It's like a standard 0.1 inch dip thing.

**Dave Jones:** You can put headers on there. You can plug it straight into your bread board or whatever or you can wire directly on and there's a whole bunch of boards.

**Dave Jones:** There's mega ones and there's minis and there's nanos and all sorts of things. And lily pads, so many boards you can buy now. Every man and his dog because the hardware is open.

**Dave Jones:** You can download the schematics and everything and you can make your own boards. And that's what everyone's doing and that's why this is a bit of a revolution these Arduinos.

**Dave Jones:** Because they just there's so many different versions of the boards or you can just do your own. You can just get a standard ATmega chip and you can program it with the you can download compile your ID Arduino software and download it directly and just use a single chip if if you like just like a regular pic or an Atmel.

**Dave Jones:** Now, the interesting thing about the Arduino is that it uses a it's it's essentially C really. You program these things in almost basically standard C. It's well, it's based on something called wiring or something like that.

**Dave Jones:** You can look it up, but it's essentially C and it's compiled as opposed to interpreted. If you get say a Picaxe chip, it it it runs its own program in there and then the programs that you generate, they aren't compiled into native um pic or you know, native pic assembly language.

**Dave Jones:** They're actually um interpreted code and they're like basic. It's it's like an interpreted basic and they just run inside the chip and that means they're very slow and because the program inside so big, you don't get much user space to write your own programs.

**Dave Jones:** Now, the Arduino actually comes with its own um programming IDE interface. It's real easy to use. Um I got a flashing LED up on this in you know, matter of a minute.

**Dave Jones:** It was real easy. You just download the IDE programming interface and load up. File, open, load the example program, download and that's pretty much it. Um once you choose the right serial port, of course.

**Dave Jones:** So, the Arduino is incredibly good for people who don't know much about microcontrollers, just like the PICAXE. And it's a bit harder to use than the PICAXE because you've got to know C, essentially.

**Dave Jones:** It's not as higher level as the PICAXE. There's tons of example programs out there, and really it's really pretty easy to get a program up and running with these things.

**Dave Jones:** And the good thing about it being essentially C is that you can if you're a if you're a beginner or something, you can start using these Arduinos, get stuff up and running pretty easy, and you can put on your resume that yeah, I program Atmel AVRs.

**Dave Jones:** I'm you know, C, standard C. They're you know, it's really essentially no different. It's just a bit higher level, you know, of abstraction. So, it's really neat. I like it.

**Dave Jones:** Programs, they're not called programs, they're called sketches. So, you write a sketch. You know, I don't know. Somebody made it up. I don't know why the term I don't like it, but anyway, you download you write and download sketches for these things, but they're just regular C programs, basically.

**Dave Jones:** Um and there's a couple of ways to program these Arduinos. Now, uh the I guess the standard or the traditional way to do it is to have is to buy the pre-programmed chip, okay, usually on a board like this, and it's got the bootloader pre-programmed in there.

**Dave Jones:** So, uh it basically just talks to the PC via a serial port, but it's actually a um standard PC USB port, but it actually acts like a serial port.

**Dave Jones:** And the program just um the IDE interface program for the Arduino, it just downloads your code via the serial port, burns it into the chip, and then you can disconnect it and power it on, and it just runs your program.

**Dave Jones:** After about a 5-second boot delay because of the bootloader. Now, if you don't want that 5-second delay when you boot up, then uh you can actually just download the program directly into the chip, or the sketch as they call it, directly into the chip without the bootloader.

**Dave Jones:** But, to do this, because you don't have a bootloader, you can't do it by a serial port. You've got to have an AVR uh Atmel AVR chip programmer, like an AVRISP programmer device.

**Dave Jones:** So, if you buy that, then you can program uh directly onto a chip like this. The Atmel AVR chip, just like that on the board, right? You can just program it directly into there if you want it to boot instantly, and you've got the entire program memory of the chip available.

**Dave Jones:** It's great. And of course, you don't even need one of these boards. You can just have the bare chip and put it into any project you like. So, the So, in that case, the uh Arduino just basically becomes a a sort of just another um C compiler, really.

**Dave Jones:** Another IDE interface and C compiler. Nothing unusual there at all. So, that's a good thing. It It has the whole spread that's easy to use with these boards that already have the USB interface, and you can get all sorts of different types.

**Dave Jones:** Or, you can just, if you want, uh program an individual chip or your own board, or whatever. Solder your chip onto your own board, put in the ISP header, and program it.

**Dave Jones:** So, it really uh does the full range of um of really development solutions. And because the Arduino is essentially standard C, you've got all the usual uh C type stuff, you know?

**Dave Jones:** It supports floats and double precision floating-point uh numbers and for loops and all the usual um C type stuff, basically. And the other good thing about the Arduino is that it's it's slightly higher level than just a regular than just using the um AVR uh GCC compiler for the Atmel or say the the C compiler for the PICs.

**Dave Jones:** It's It's a slightly higher level than that. So So you don't have to worry about header files and you know, setting up registers and stuff like that. It sort of takes care of all that for you, which is really nice.

**Dave Jones:** So um you know, I think it's a It's a It's a small but very significant step forward in how people use microcontrollers. And I reckon it's a beauty. So advice for you newbies out there who want to get into microcontrollers, well, I've usually recommended the PICAXE because it Well, it still is probably the simplest way to get a program up and running on a microcontroller.

**Dave Jones:** It's even simpler than an Arduino. It's That's just the way it is because you can You don't even need to know a programming language. The PICAXE allows you to just use flowcharts if you want to.

**Dave Jones:** You can just write your program in a regular flowchart, you know, start, do this, branch, do do. And you know, compile and and away you go. You can flash a LED without really any source code, which is really quite amazing.

**Dave Jones:** But the next Really, but the problem with that is that it's like a basic type interpreter language. It's really slow. You haven't got much space in there. It's proprietary.

**Dave Jones:** It's not open source. It's not really professional. So unless you want to just do a couple of hobby projects, I I really wouldn't recommend the the actual PICAXE because it's you know, it it really is just really basic hobby level stuff.

**Dave Jones:** It's definitely not professional. No professionals use it. But the Arduino on the other hand, you can essentially program in C. So it's it's It's not just a hobbyist platform.

**Dave Jones:** It kind of you know, it essentially is a professional uh development platform. And you know, some people can argue it's not, but I think it essentially is. Because your programs are portable, they're essentially C, and really you are using the AVR GCC compiler.

**Dave Jones:** It's just a nicer front end. And of course, your traditional technique is just to use a regular PIC or Atmel or any other microcontroller. They're they're not the only two, there's plenty of others.

**Dave Jones:** And you need a you know, a a programmer, even an in-system one like the PICkit or the AVR AVR ISP or or some other programmer. There's tons on the market.

**Dave Jones:** And then you use um either assembly or C. Now, the big difference there is that um you know, there's many different types of IDE interfaces, development platforms, lots of traps you have to worry about setting up the individual registers inside the actual PIC or Atmel or some other micro.

**Dave Jones:** You've got to set them up, you've got to configure the input pins, and you've got to There's lots of traps, oscillator options, and there's lots of you know, traps for young players for just starting out with just a PIC or an Atmel.

**Dave Jones:** That's why the Arduino and the PICaxe are you know, the higher level ones are so good. You know what I really hate? Something that really ticks me off. Assembly language programmers.

**Dave Jones:** These old pro These you know, these programmers who go, "Ooh, I program in assembly. It's the only way to do it. I can write an assembly program quicker than you can in your stupid C language or your stupid PICaxe or your stupid Arduino." And they really tick me off.

**Dave Jones:** They're [ __ ] really. Next time you hear somebody say they can program something in assembler quicker than C or BASIC or some other higher level language, you tell them Dave said they're a [ __ ] and slap them over the head for me.

**Dave Jones:** And then they argue, well, the Atmel's better than the PIC. The architecture, it's a nicer assembly language. It's a heaps better to write in assembly. Well, that's idiot. Idiots.

**Dave Jones:** Really. It's like arguing that uh Revenge of the Nerds 3 is better than Revenge of the Nerds 4. They both suck. You should be, you know, you should be watching the original Revenge of the Nerds.

**Dave Jones:** You should be programming in C. Really. Assembler is for, you know, archaic [ __ ] basically. Uh but, you know, okay, there are uses for assembly language for, you know, doing nice, tight, fast routines or something like that.

**Dave Jones:** But, really, just some inline assembly is great. But, to write your entire programs in assembly language is, you know, is the mark of madness. It really is. You know, and these high-level languages like C and and and basic and, you know, other ones, they've been developed for a reason.

**Dave Jones:** It's because they're easier, they're quicker. There's no anyone who claims they can write an assembler program quicker than someone in C or basic is an absolute idiot. And then, of course, the idiots will try and argue, oh, but if the assembly language is more efficient, you can fit more into the India chip.

**Dave Jones:** You can cram it all in there. Well, I'll tell you something for free. If you have to uh worry about every last byte uh to fit your program into a chip, then you've chosen the wrong chip for your project.

**Dave Jones:** Choose a decent one with a decent amount of memory. There's no excuse anymore. It's not 1985. So, if you got one of these uh little boards or just the chip on its own, how do you program it?

**Dave Jones:** Well, if it's you can use the app, you know, the in-system Atmel programmer if you want. But, if you buy one with the uh with the bootloader pre-programmed, or you can just download it from the uh Arduino environment if you have the ISP, but you just get one of the little um USB to serial converter boards, and they don't cost anything.

**Dave Jones:** They You know, they're practically giving them away, and uh it converts the USB into two RS232, and it or serial, and it just, you know, plugs into your board, and you program your chip.

**Dave Jones:** It's really quite neat and easy. I wanted to see how easy it was to get a project up and running. So, the classic project is an LCD. So, I hooked an LCD up to this uh wing shield board with the screw terminals, which makes it real easy, and within like a minute, I had a uh hello world running on my LCD, and there it is.

**Dave Jones:** And here's the source code to show you how easy it is. Now, just that simple, you know, 10 or 12-line uh program, that takes, as you saw maybe down the bottom, it took about 2.3 K of uh 30 K available memory on this board.

**Dave Jones:** And that might seem like a lot, but it's not really cuz there's the LCD driver there and string handling and all sorts of other overhead. So, that's, you know, fairly typical of a project like that.

**Dave Jones:** Now, I did actually have some problems with the Arduino software. Uh on my work machine, it it I had all sorts of problems. It was locking up. It would take uh when you boot up, it takes like 3 minutes to even do anything, and then it locked up when it tried to download, and it took minutes, and it was jerky.

**Dave Jones:** It's probably something wrong with my Java driver or something. I don't know, but it works fine on my home machine. So, go figure. Now, the funny thing is, there's really nothing uh sort of original about the Arduino at all.

**Dave Jones:** Really, it's been done but hundreds of times before. There's There's nothing unusual about a, you know, a demo board with a, uh C compiler uh interface and some nice pre-written libraries and a boot and a serial bootloader and things like that.

**Dave Jones:** So, why is this damn thing so popular? Well, it's just the whole you know, the whole industry, the whole ecosystem which has grown around it, I think. And it's it's just a open source hells, but there's nothing new about that.

**Dave Jones:** It's just I don't know. It just seems to have caught on with the with the hacker and the maker crowd and and all those sort of people who are into that sort of thing these days.

**Dave Jones:** That's why like 5 years ago, those sort of people didn't exist. And uh the sort of market for this thing just wasn't there. It was just it was just another demo board, but really this is this you know, somehow it's worked.

**Dave Jones:** All the little things have added up and it's a winner. So, what do I think about the Arduino? Well, I give it the thumbs up. I think it's really very, very good.

**Dave Jones:** It gives you the power of you know, C a C development environment without all the fuss. It's easy. It's really easy for beginners to start on these things and do something really useful with a wide range of boards.

**Dave Jones:** And then if you want to do something more powerful, you can, but it's it it is fairly you know, if you really want to do like a low power solution or something.

**Dave Jones:** As far as I'm aware, they don't have a low power solution yet. Or if you want to do really fancy stuff that you can you know, if they don't have a library for it, you've got to write your own.

**Dave Jones:** Or if you want to do a real fancy huge detailed project that you would you know, max out a regular micro, then maybe it's not the best choice, but it's a pretty darn good all round solution and I like it.

**Dave Jones:** I think I'm going to actually start using these things. They aren't just a toy for the hobbyist. They're really I think they're quite a professional level tool. So, check them out.

**Dave Jones:** Really. The Arduino.
