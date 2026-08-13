---
video_id: C1on-LaIsCA
title: EEVblog #b10000000000 - 1K Micro Magic
url: https://www.youtube.com/watch?v=C1on-LaIsCA
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 24, "2": 42, "3": 58, "4": 80, "5": 102, "6": 130, "7": 146, "8": 164, "9": 181, "10": 204, "11": 222, "12": 243, "13": 258, "14": 270, "15": 292, "16": 313, "17": 332, "18": 347, "19": 366, "20": 391, "21": 413, "22": 432, "23": 449, "24": 468, "25": 488, "26": 511, "27": 530, "28": 549, "29": 562, "30": 581, "31": 599, "32": 617, "33": 635, "34": 653, "35": 674, "36": 692, "37": 707, "38": 719, "39": 734, "40": 755, "41": 776, "42": 794, "43": 812, "44": 827, "45": 839, "46": 860, "47": 878, "48": 899, "49": 923, "50": 938, "51": 953, "52": 968, "53": 992, "54": 1013, "55": 1031, "56": 1055, "57": 1076, "58": 1100, "59": 1121, "60": 1139, "61": 1157, "62": 1172, "63": 1193, "64": 1208, "65": 1229, "66": 1244, "67": 1265, "68": 1280, "69": 1298, "70": 1322, "71": 1343, "72": 1361, "73": 1385, "74": 1409, "75": 1427, "76": 1445, "77": 1460, "78": 1478, "79": 1508, "80": 1532, "81": 1553, "82": 1568, "83": 1583, "84": 1595, "85": 1610, "86": 1625, "87": 1637, "88": 1655, "89": 1676, "90": 1694}
---

**Dave Jones:** Hi, welcome to EEVblog number 1024. And yes, you should know the significance of 1024. Some rated it much more important than the 1000th video. So I thought I'd do something 1K related. One, not 1K, as in a thousand, 1024! Two to the power of ten.

**Dave Jones:** We have to go back to the future here, August 1999. I thought I'd show you an old project I had published. Let's go to page 60, shall we? Ta-da! Oh no, that's the... Sorry, this was actually very confusing. There are two projects in this issue.

**Dave Jones:** One is mine, and the other is someone else's. One, by the way, James Barker is a pseudonym for someone who I won't tell you who, but that's not their real name. Anyway, it's a video title generator. Here's mine, here's a name you might recognize.

**Dave Jones:** David L. Jones. And this was a project, a little project that I used to sell in both kit and built-up form. It was actually very popular at the time. It inserted a time date over composite video signals, which was a big deal back in 1999 for security and other applications.

**Dave Jones:** Anyway, well, I won't go through the whole article. I'll actually scan it in and include it down below for those who want to read the whole thing. But it basically used a PIC16F84 inside here, and here's the entire schematic. It used a special STV5730A video text generator chip,

**Dave Jones:** so the PIC16F84 wasn't actually doing any of the titling and stuff like that. It just basically controlled this via the serial interface. But the 16F84, not to be confused with the modern 16F84A, that actually contained one program, 1K, program words of memory. 1024, not bytes, because the PIC processors are actually 14-bit instruction words,

**Dave Jones:** so it's like 1.8K, but it's actually really 1024 program words, 1K. So I thought we'd take a look at this old project and see if we can compile it again. And there's the one-to-one PCB pattern for those who want to build their own at home,

**Dave Jones:** although you'll have to scale this video properly. But you could do it, kind of. And there's my original prototype, which I sent in, which, ta-da, I found in the archives there. There it is, that is, yeah, it's even got the same label. Look at that, same original label on it.

**Dave Jones:** So they sent, they did send the prototype projects back, these magazines, but you had to send it to them to, so that they could test it out before they invent it, before they publish the thing. Anyway, composite video in, composite video out, powered from 12V DC, little 5V regulator in there.

**Dave Jones:** PIC16F84, DELLA semiconductor DS1307, real-time clock chip, the main crystal and the 32kHz crystal for the real-time clock. I bit-banged, as I'll show you in the source code, bit-banged an I2C serial, an I2C port on this thing, and all this wonderful stuff, with the time, date, overlay, everything,

**Dave Jones:** ran in 1k of program memory, just. But that's not all. Two months later, in October 1999, I had another one published, a follow-up project, which was the VTG, as opposed to the VCG, was the Video Title Generator. Where is it? There it is!

**Dave Jones:** Ta-da! Very similar case to this one, except it hooked up to a PC80 keyboard, none of this, you know, modern USB or PS2 rubbish. And it allowed you to insert, it basically used the same PIC16F84 processor, but it allowed you to put video titles, text,

**Dave Jones:** so you could actually move the cursor around the screen, you could type in any text you actually wanted, and this is like the menu interface on it, so this did a lot more stuff than the time-date one, but this one also fitted in 1k of program memory.

**Dave Jones:** And you could actually do bigger fonts and stuff like that as well. So it was quite jazzy. So let's take a look at the source code, and see if we can compile it. And by the way, when I had the first one there published in August,

**Dave Jones:** that was the very last editorial, the very last time that the famous Jim Rowe actually edited the magazine, and he said, nope, I'm handing over to Graham Cattley, and, well, it lasted a couple of more months as Electronics Australia before it became EA, well it still had Electronics Australia,

**Dave Jones:** but it became EA and Gadget Mania, and that was the beginning of the end, and like nine months after that they renamed it EAT, or EA Today, they dropped the Electronics Australia title, and everyone unsubscribed. Literally everyone unsubscribed from the magazine, and they folded like two or three issues later or something like that,

**Dave Jones:** but basically that was the end, April 2000, let's say the end of 1999 when I had these projects published, was the end of the venerable Electronics Australia as we knew it, and it had lasted for, well, if you believe Jim, oh there you go, and you should,

**Dave Jones:** because he's right, 77 years it was going for at that point. Absolutely under various names, Radio TV and Hobbies and then Wireless Weekly. Anyway, a bit of nostalgia for those Aussies. Alright, I thought it'd be interesting to see if I could still compile

**Dave Jones:** my original assembler source code 18 years later, after the fact. Is it still possible? Because here it is, I've got the original source files version 1, that's how I labelled them, VCG, Video Character Generator, 1.0, looks like a jump from 1.0 to 2.0, I can't remember the differences,

**Dave Jones:** 2.0a, 2.0b, 2.1 seems to be the latest. Now I do remember that 2.1a is the version for a PIC16C61 chip, not the F, so I think I used that in production, because that chip was cheaper, the CMOS version, the one-time programmable CMOS version was cheaper than the Flash program,

**Dave Jones:** I only used the F84 for software development, I think. I think the ones I actually shipped were the C versions. Because I didn't include an in-serial programming header on there, because it wasn't easy to program these things back then, right? So it's not like you have your PIC kits and all sorts of stuff you do these days.

**Dave Jones:** Here's all my original assembler code, there it is, it's got a lot of comments on there, yay me! Look at that, it's quite comprehensive. So I just want to cut and paste this code into the new MPLAB environment, or whatever it is, and see if we can use it.

**Dave Jones:** Now I don't think I've used MPLAB X integrated, I've downloaded this and it's 667 megabytes. I've downloaded it, installed it, and yeah, it's shocking. Is that, or is that, yeah, I assume that's the one, I presume you can just download the command line assembler,

**Dave Jones:** if that's what you want to do. But I'm just going to go for broke and install MPLAB X IDE, see if they still support the chip, and still support just compiling it straight out of the box 18 years later. Let's go. Alright, here's the MPLAB X IDE, I'm not an expert on using this,

**Dave Jones:** so please forgive me dicking around and what not, but let's go in and let's create a new project. Standalone project is what we want. Yep, no worries, we don't want any of that rubbish. So we want, I believe they're a mid-range pick, they have different ranges, so if you go into the baseline ones,

**Dave Jones:** I think they've got, yeah, your tiny ones, your 10, 12, oh no, 16C, no it doesn't, see it doesn't even have the 16C61, which I originally used. So let's go into them, and it certainly doesn't have the F84 in there. Ta-da! 84! We have the 84, and the original 84,

**Dave Jones:** not just the new 16F84A, which is just like, I think they just used like a new manufacturing process or whatever, but they still, there might be very minor differences, programming-wise I'm not sure, but mine was the original 16F84, and they still support it, and this is one of the good things about microchip,

**Dave Jones:** hats off to them, they do support legacy products really well. So we'll choose the original 16F84, next, and we can choose our hardware tools, ICD, what other, microchip starter kits, we can choose, I don't know what I'm going to try and program it with yet,

**Dave Jones:** I don't know, probably the PIC chip, but I don't have the ISP on there, I'd have to bodge something up, but we can just choose the simulator, so let's just choose the simulator for now, we can always change it later, and here we go, we don't want to use the PIC-C compiler,

**Dave Jones:** not that rubbish, this is what we want, so we're going to choose the assembler, and VC, we'll just call it VCG, shall we? Set as main project, boom, encoding, don't care about that, we'll just go, and we're in like Flynn, there's our device, the 16F84,

**Dave Jones:** okay, so what we want to do is new assembly file, ASM, so I won't find the original file, I'll just get a new one, I'll just make a new one in the project directory, and here we go, VCG.ASM, there it is, and now I can just cut and paste

**Dave Jones:** in my code, okay, so I've just highlighted all my code there from the text file, we'll copy that, and we'll paste it, bingo, we're in like Flynn, we've got this newfangled color syntax highlighting, which makes it look a lot better, look, it knows its comments,

**Dave Jones:** so they're all green, it knows the defines, and it knows the variables and all that sort of jazz, so that is quite nice, and there's all my assembler code, so we can save that, save that, and let's try and compile it. One thing I really like is this navigator,

**Dave Jones:** look at this, VCG.ASM.Navigator, and this has, it's pulled in all my variables and what not, so we can go like cursor loop, we can jump to my function in there for cursor loop, look at that, isn't that great? Stable, whatever that means, oh, I2C, there's my I2C

**Dave Jones:** bus as stable condition, so here we go, here's all the I2C routines, so I wrote my own bit banging I2C routine for this, because the 16F84 does not have an I2C hardware in it, there we go, so I'm using the Tristan instruction to set the bits, and I2C start

**Dave Jones:** condition, and then send byte, so there's my routine for pass byte to the send buff reg, I like, I don't know, I've forgotten like almost all of this, I used to be pretty good at microchip assembler code, but now it's like it's almost cling on to me now,

**Dave Jones:** it was 18 years ago, give me a break, yeah, not long after this I sort of like switched to C and like I never really touched much assembler after that, it was, you know, only very occasional things that I needed to do, so yeah, I've

**Dave Jones:** forgotten more than I've remembered unfortunately, but of course it wouldn't take me long to pick up all this again and get back up to speed, you know, it's just a matter of hours, like it's not you know, days or weeks or anything like that

**Dave Jones:** so anyway, so we've got our VCG ASM, so what I want to do is now, I just want to build it, clean build and main project, let's just hit the button see if it works, we've selected 16 we've selected our part, the 16F84, we've included our

**Dave Jones:** source code, we've only got the one ASM file, we don't have to link anything in, we don't have to do anything, this should work! Fingers crossed 18 years later, come on microchip don't let us down! Woo! Build successful! Total time, one second! There you go!

**Dave Jones:** Done! VCG, it's generated, there we go it's generated VCGXproduction.hex it's generated our hex file, there's the command line that it used, slash q slash 16F84 build production, blah blah blah blah blah and VCGASM was our only file, now it gave us a couple

**Dave Jones:** of messages, line 78 register in operand, not in bank 0, ensure that bank bits are correct, I don't remember all this the memory architecture of the baseline pixels like you have to swap banks and stuff like that, if I remember right, so if we go up the top, we'll probably find

**Dave Jones:** that I mention, I do banks, here we go, so the originate 0, so it actually starts at address 0 and yep, select bank 1, there it is there we go, so I'm selecting memory bank 1, I don't and then I do something else and select bank 0

**Dave Jones:** I can't remember the architecture off the top of my head it'll take me a while to get back up to speed on that, but yeah, so that's register in operand not in banks, I don't know if that was a regular if I got that message back then and it's just something I ignored

**Dave Jones:** or what not, like it's not an error, so it's like just a message, I guess it's just ensure that the bank bits are correct, I'm sure I got it right I knew what I was doing right in the assembler code, so it's not

**Dave Jones:** an error, it compiled 18 years later with the big MPLABX environment, all 690 whatever meg of it and it just, it simply worked it's generated the production hex file, so if we go up here distribution, there we go, distribution default production, there's our hex file

**Dave Jones:** that's our hex file which we can program into our 16F84 using whatever programmer you like, winner winner, chicken dinner alright, so the whole point of this video was also to see how much memory I had left, I was using, so if we go into memory down here

**Dave Jones:** dashboard usage symbols what I think I'll do is I'll just go in here and debug main project and see what there it is, there it is, winner winner chicken dinner data, I've got 0 bytes free, oh data use 0, free 68, yeah I didn't use any

**Dave Jones:** data like IES RAM and there you go I've used 95% I've got, I used 974 program words and I got 53, so I don't have much left out of all this source code I'm not sure if I went, like if early versions were, you know, worse and I went through an optimizer

**Dave Jones:** I do recall kind of doing that, thinking that I do remember being right on the edge of the 1K, like 50, heaps you know, 53, I probably went through and optimised it a bit trying to get it down, just so that further on

**Dave Jones:** when I was actually selling this product, I could like add the odd feature or tweak a few things and stuff like that, you know, you don't want to be shipping with a thousand and, you know, using every single last program word in your actual processor

**Dave Jones:** because then you can't fix bugs and insert maybe a little tiny feature or what not, so yeah having 50 bytes free, you know, that just gives you some flexibility to fix some stuff, but there you go I used almost all of my 1K

**Dave Jones:** and it compiled fantastic okay, what I've done now is I've taken my other project the VTG, the video title generator which uses the AT keyboard to type characters in and do video overlay and I've included that, so I've created a project for that, and here's my VTG

**Dave Jones:** source code, used the same PIX16F84 there it is there, and it also was, if memory serves me correctly, very close to the 1K, ooh, I've got some lookup tables there, there you go, lookup table, convert keyboard codes into STV5730 display codes, there you go, so I put that at a specific

**Dave Jones:** address in memory right at the end, alright you've got to right click on here and set that one as main project if you've got multiple projects in here, so we should just be able to compile that Ta-da! Build successful! Of course it did the other one, it looks like we've got the same bank error messages

**Dave Jones:** here, but there's no errors there's no errors, it has generated VTG production.hex Fantastic! And what I want to do now is actually go in and have a look at, where is it, Windows debugging? No? Pick memory views, I want to go in and actually view

**Dave Jones:** the program memory, and here we go so let's have a look at the program memory and because this is assembler, you've got to remember this, right? I'm telling this processor what to do, instruction by instruction so the code that I've typed up here should match what's

**Dave Jones:** the disassembled code down in here so if you look at address 0 here I originate my code at address 0, that's what originate 0 there means, it's the processor reset vector, the start of code in the pics it's 0 and my first instruction is clearf port b

**Dave Jones:** and sure enough down here is clearf port b. It's compiled it and then we're looking at the simulated memory there and it's decompiling it and it's exactly the same, look you'll see it just matches every single instruction and if we go right to the end

**Dave Jones:** can we go right to the end? Here we go, 1024 let's go to our lookup table that all looks the same, haha, our last one there is 7a, so if we go right to the bottom of my code, this is interesting 7a, there it is

**Dave Jones:** 0x7a, that was the very last line of my code, but I actually did include so that matches by the way, 0x7a matches that 5f, everything is, you know byte for byte, word for word, instruction for instruction exactly what I wrote in my assembler code, because that's the whole point

**Dave Jones:** of assembler. Why I've put all these extra spaces in here I think I, for some reason I decided that I should just fill the rest of the memory, because that was a table that I looked up to do the instructions and I just thought

**Dave Jones:** well, I'm not using the rest of that memory so, you know, I might as well fill it with something that I know is going to be a space right, so it, like yeah, there was some there was some program reason why I actually just filled the rest of the processor memory

**Dave Jones:** with that, but of course if I wanted to add extra space if I wanted to use extra instructions I could have just changed that originate instruction 300 to closer to where I was at the end of memory, and I could tweak it just to the last

**Dave Jones:** byte there. Yes, they're the keyboard code lookups, that's right, it converts the keyboard code into display code. Aha! Here's another lookup table which was my, this is what I'm looking for, 0x I specifically put that into address 0x there, and this has all of my menu items

**Dave Jones:** so if you had a look over here, my menus there you go, this is what my title generator looks like you know, VTG01, so all that text has to be stored in the program memory somewhere and I put that in this table here

**Dave Jones:** so there you go, it matches VTG01 version 2.1, etc, copyright 99, and then F1, all the instructions to tell the user what to actually do, and they were all in that lookup table there. So I had to expend all of my precious, like a good part of my precious 1K program

**Dave Jones:** memory, putting in all these strings, I mean you know, the more strings you have, the more of that 1K that you're chewing up, you've got to store them in there, there are ways to compress and do other stuff if you're really desperate and for those playing along at home, you want to know how many

**Dave Jones:** bytes I had left over on the video title generator, I used 930, so not as many as the, I don't, yeah, I used like 970 in the video character generator, so I've got 94 program words free in flight of the freaking moon on 94 program words

**Dave Jones:** right, I think I'll go edit this now shooting the video out of sequence video killed the radio star I heard you on the wireless back in 52 Video killed the radio star So, does it actually still work after all this time? Well, there's only one way to find out, that's to plug it up

**Dave Jones:** I've got this 01XDS3202 which actually has a composite video output, and sure enough you turn on the power and there it is on the external screen, no worries at all, but there's no title text, so that means that the STM chip on here must be working

**Dave Jones:** it's processing the surface mount one under there, it's processing the video, but we're getting no overlay whatsoever the menu buttons do absolutely nothing so I think that might be a difference this oscilloscope might be generating NTSC and I think I had the flag set in here for

**Dave Jones:** well, for the Australian PAL version, so let's try a known PAL video source, this RLungna, it's actually an Australian video generator, quite old, but you know still works, so let's plug it in, handily we've got a... ta-da! It works! Look at that! Beautiful!

**Dave Jones:** And that is gorgeous video, yes I'm actually generating a black signal, so I'm generating a PAL, so I can go... hang on there we go, checkerboard that's black, there we go, we've got crosshatch whatever that is yep, also... whoa, that doesn't work too well, there you go, the old monochrome colour bars

**Dave Jones:** we can switch those to colour, and there you go, we get a bit of shimmering on there, but you know, I don't know I can adjust the burst level on this for example so, that's just all, yeah so, I don't know, whatever looks beautiful, look at that, oh look at the funky stuff

**Dave Jones:** I can do, sorry, I'm just playing just having a bit of fun with some modes on this puppy, neat so what we could do is we could actually go in there and adjust the time and date, and also this title so I restored a bit of text, if you just press

**Dave Jones:** yeah, if you just press mode, button, oh I don't know why I did that, but you can go in there and you can just increment all this stuff go across, you can increment your date sweet as, but there you go, you can go in there

**Dave Jones:** and set just a short title text. Now I could actually program this with my Pickit 3 of course but hey, I've already got this little mini pro programmer you've seen in a previous video, and it does pics and it does the 16F84 so I've loaded that file in, let's give it a

**Dave Jones:** go, program yep, program jeez, it's pretty slow for 1K wow do one of your thumbs says it's done alright, were we able to program this brand spanking new Pic16F84 the pins weren't even bent on this puppy so only one way to find out, let's power it up

**Dave Jones:** and see if everything worked after 18 years, here we go woo winner winner chicken dinner by the way, if you're wondering where I actually stored this text up here, because this Pic16F84 doesn't have any built in E2P and you couldn't rewrite it's own program memory that I recall

**Dave Jones:** anyway, so I actually stored it in the Dallas Semiconductor DS1307 chip, it actually had like 50 or 128 bytes or something of memory, of SRAM memory and that was battery back down there so over the I2C I just stored that video text in there

**Dave Jones:** so there you go, I hope you enjoyed that look down memory lane of what is capable, a pretty primitive example of what's capable inside a 1K of program memory, it'd actually be an interesting experiment to actually try to see if we could get a

**Dave Jones:** in this case, any of the microchip RC compilers to do that exact same code in 1K the modern C compilers are very very good if you're optimizing for code space and stuff like that but back when I did this, I don't think there was any really

**Dave Jones:** even like using the best one at the time, which was like the Australian high tech C compiler, which Microchip eventually bought I don't even think that could do it back in the day, because I think I had it and I just went nah, you know, and you paid

**Dave Jones:** a lot for the 2K chip versus the 1K chip it was like double the cost or something so it added to the cost of the kit and things like that so I sold that little kit until they ST discontinued like 2, 3 years later

**Dave Jones:** or something, the chip in there and there really wasn't anything else in the industry that could just take video in, video out, and then some sort of digital serial interface to do video text overlay I know there are these days, but back then, this was the only

**Dave Jones:** chip on the market that I was aware of that actually did this and it was a real bummer, there were a lot of people using this chip and a lot of people upset when they discontinued the thing anyway, if you liked that video, please give it a big thumbs up

**Dave Jones:** because that always helps a lot, and leave your stories down below in the comments or on the EEVblog forum about if you've done some magic in 1K of program memory we've talked about it in the Amp Hour before, actually doing a contest like the 1K programming contest, because it's just

**Dave Jones:** a nice, round, small value that just lets you appreciate assembly language programming and trying to extract the maximum possible stuff from 1K of memory. I know this is a fairly primitive example but it doesn't do a hell of a lot but I was pretty impressed that I managed to fit that in

**Dave Jones:** 1K of assembly code without trying too hard anyway, so yeah, leave your stories down below or even better yet, link to a project if you've done something really cool in 1K of memory so I hope you enjoyed that 1024th video, I hope I did something appropriate

**Dave Jones:** catch you next time 1K of memory I'm not sure what I was talking about I don't know, I don't know I don't know what I'm talking about I don't know I don't know I don't know I don't know I don't know
