---
video_id: DBftApUQ8QI
title: EEVblog #63 - Microchip PIC vs Atmel AVR
url: https://www.youtube.com/watch?v=DBftApUQ8QI
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 32, "3": 46, "4": 60, "5": 77, "6": 89, "7": 107, "8": 120, "9": 137, "10": 155, "11": 170, "12": 186, "13": 203, "14": 218, "15": 234, "16": 251, "17": 264, "18": 275, "19": 287, "20": 301, "21": 315, "22": 328, "23": 346, "24": 357, "25": 372, "26": 384, "27": 401, "28": 415, "29": 433, "30": 446, "31": 465, "32": 480, "33": 495, "34": 513, "35": 526, "36": 542, "37": 558, "38": 570, "39": 583, "40": 595, "41": 615, "42": 627, "43": 639, "44": 659, "45": 673, "46": 688, "47": 700, "48": 713, "49": 729, "50": 742, "51": 759, "52": 771, "53": 784, "54": 801, "55": 816, "56": 830, "57": 843, "58": 858, "59": 875, "60": 892, "61": 911, "62": 925, "63": 940, "64": 956, "65": 971, "66": 982, "67": 999, "68": 1014, "69": 1026, "70": 1039, "71": 1056, "72": 1071, "73": 1093, "74": 1108, "75": 1123, "76": 1140, "77": 1156, "78": 1169, "79": 1185, "80": 1198, "81": 1216, "82": 1232, "83": 1247, "84": 1261, "85": 1274, "86": 1291, "87": 1305, "88": 1317, "89": 1328, "90": 1340, "91": 1353, "92": 1364, "93": 1380, "94": 1394, "95": 1407, "96": 1421, "97": 1439}
---

**Dave Jones:** Hi, welcome to the EEVblog and electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, I'm finally going to get around to doing a blog which has been on my list

**Dave Jones:** for almost since the start of this blog. Every week, probably on average, I get an email from someone saying, "Dave, can you do a blog on PIC versus AVR, PIC Microchip versus Atmel?" You know, I get these emails from beginners wanting to

**Dave Jones:** know which one they should be using, which is the best, and uh, you know, have I got any advice for them? Well, okay, here's my blog on PIC versus Atmel. Now, at first I thought it was a really good idea for a blog. It'd be

**Dave Jones:** terrific, you know, I could go through all the technical details of the architectures and the and the tools and the, you know, the feature set and price and everything, and, you know, come to a conclusion as to which one, you know,

**Dave Jones:** which best for beginners or which is best for somebody else. And, oh, the more I think about it, the more I realize I just cannot do a technical blog on it. I just, like, a full-on all the technical details comparing

**Dave Jones:** AVR to PIC. It's just It's I The more I think about it, the more I think it's just totally and utterly pointless. Cuz I know if I do it, I'm going to It doesn't matter what I say, what

**Dave Jones:** conclusions I come to, there'll be rabid fanboys of each microcontrollers, but particularly the Atmels, the AVR freaks out there, who will come to the defense and slag me off. Now, I don't normally, you know, care about people slagging me off, but I know

**Dave Jones:** they're going to do it. They're going to point out every technical, not so much error, but they're going to point out, "Oh, you didn't do this. This isn't right. This better in this respect. This one's better." And, ah, I'm not going to fall for it. So,

**Dave Jones:** instead, I'm just going to give you my general opinion on PIC versus Atmel. Now, let me give you the skinny right up front. I'll get to the bottom line of it straight away. Which should you choose if you're a beginner, PIC or AVR? Well,

**Dave Jones:** the answer is it doesn't bloody well matter. Why? Because it's it it really doesn't. They're both microcontrollers. They're both excellent. They're both some of the biggest on the market. They've both got excellent support. They've both got excellent beginner kits available.

**Dave Jones:** They've both got free development tools. They've both got this. And then it's just really it doesn't matter. My advice to you is find a development kit, a starter kit, which suits your purposes, suits your needs. Some of them will have

**Dave Jones:** various features, either LCDs or motor controls or whatever on it. Um, pick one that you that's within your price range, that you like, and you know, buy it and go for it because it doesn't matter. Now, if you want to be a good engineer,

**Dave Jones:** if you want to be a top engineer, you will not be one of these rabid fanboys who religiously sticks to one particular microcontroller family. You will always keep your options open. And you can tell an absolute [ __ ] designer because

**Dave Jones:** they're so passionate about one particular um part or one particular manufacturer and they'll just ignore all others um even to their own detriment. And really, you know, that might be okay for hobby use, but if you're a professional designer, if you're a

**Dave Jones:** professional design engineer, you've got to keep your options open. That's just the way it is. Now, I'm um I've I've got to admit, I'm more of a fan of the uh PICs than the Atmels purely because, um, I've been using them

**Dave Jones:** longer. I think their support is, uh, better in many respects. Um, and I like their tool set better than the, um, Atmel ones, and I'll go into that. And, well, it but there's not much in it. Now, I've used both PIC and Atmel, and

**Dave Jones:** I've used, you know, other brand microcontrollers as well, but PIC and Atmel are sort of the two biggies that you always hear about. And they're not necessarily the biggest on the market, but, you know, like you don't hear about

**Dave Jones:** Motorola at all, right? You hardly ever hear about Motorola, but they're like, still, I I believe number one in the automotive market, or maybe even the white goods market as well, or something like that. But you don't hear about them

**Dave Jones:** cuz they're they're not they're just some, um, you know, industrial thing that companies just use because they've been using them for 20 years, and that's what they use, and they're happy to use it, and they're great, and they just

**Dave Jones:** work, and, you know, they don't make the mainstream media. They don't make the magazines. They don't really have hobbyist level intro kits, or they don't do it as well as PIC and Atmel do. So, that's why you never hear about other

**Dave Jones:** ones, you know, um, you know, Motorola and, um, you know, TI MSP430s aren't, uh, too bad. They've got a bit of, um, you know, in bit of foothold in the beginner market as well. And, but, you know, PIC and Atmel are the two big

**Dave Jones:** ones. And, really, if you're going to I think if you're going to start out with a micro, you should be picking one of them, just purely because of the support available, the beginner supports, the starter kits, the books, and things like

**Dave Jones:** that. Now, when it comes to these fanboys, I think that, um, Atmel AVR ones win hands down. They are most they are the most rabid, fierce defenders of their religion, which is Atmel, and they hate PIC so much. And they it's

**Dave Jones:** laughable. Every You know, if you go on a forum and ask which is the best PIC versus Atmel, a lot of times the PIC guys will say, "Oh, you know, PIC's okay and I use it and that's okay, but you

**Dave Jones:** should consider the others." But the Atmel guys won't do that. No, you must use freaking Atmel. And yet, you know, they will just defend it until death. It's ridiculous. What a bunch of [ __ ] Now, if you want to look at the choice

**Dave Jones:** of PIC versus Atmel from a professional point of view, if I was if I was, you know, starting a new company and they asked me, "We have to pick a microcontroller to, you know, to make our new products with, which one

**Dave Jones:** you should you choose?" Well, there's a whole range of factors which go into the decision, but as a first order, you know, a first order guess approximation, I would tend towards PIC Microchip. Why? Because they're a they're a bigger company. They're

**Dave Jones:** bigger, more stable, and I think they've got a better future. That's They And they they just facts, really. I mean, Atmel, it's as far as I'm aware, they have actually not made a profit from day one. I I could be wrong there, but I

**Dave Jones:** think it's that's pretty darn close to the mark. And Atmel are And most of the other manufacturers are most of the other microcontroller manufacturers are in deep financial trouble. And as you might know, PIC actually tried to buy Atmel. They

**Dave Jones:** tried a hostile take take over which failed. That was about 6 months ago or something or something like that. And really it just didn't work. So, there's going to be but you haven't heard the end of that because there's going to be

**Dave Jones:** more consolidation in the microcontroller market because Microchip are pretty much the standouts financially and and their future stability. They're they're doing pretty well and the others are really struggling. So, you're going to see a lot more mergers in the microcontroller

**Dave Jones:** market, I think. Because as a professional designer, often you've got to actually consider the longevity of the parts you're actually building in to your design. Not just this design, but future designs. And you know, um it's a quite uh common occurrence to

**Dave Jones:** actually try and get uh written assurance from a manufacturer that the part you've chosen is going to be available still available in 10 years time. And and that can be pretty important. It's not going to matter a rat's ass for hobbyists use or you know,

**Dave Jones:** designing you know, small-scale projects. But when you're building parts into multi-million dollar bits of equipment or stuff like that, it's very important. So, for some advice when you're looking to uh get some development kits for your first microcontroller, pick or Atmel.

**Dave Jones:** The others are The others are the same really, but I think PIC has an edge. I've mentioned it before. It's the PICkit, right? The PICkit 2 or the PICkit 3. Don't get put off by my bad remarks about the PICkit 3 because that

**Dave Jones:** was in comparison to the PICkit 2. It sucked. But um on its own, it's still pretty good. And it's only 40 bucks. And it does in-circuit debugging and in-circuit programming. And it's the official um authorized by Microchip. Now, the Atmel one, you can get the a

**Dave Jones:** similar price, you know, $40 or something like that, $50 in-circuit serial programmer, JTAG programmer. But this one, I believe, doesn't Well, it doesn't do debugging. If you want to do debugging on the Atmels, you've got to pay a lot more for the in-circuit um

**Dave Jones:** debugger emulator device. I'm not sure the price of that, but I think it's in the hundreds of dollars. Now, when you're uh looking at these sort of tools, I highly recommend you don't get these parallel programmers like the

**Dave Jones:** PICstart Plus. It It Well, it might be okay if you're building something on a breadboard and you put your chip in and you program it and you move it over to your breadboard, but you know, really you want to do in-circuit

**Dave Jones:** debugging and you don't want to be plugging the chip every time you recompile the software cuz it's a pain in the ass and it can ruin your chip and it's just slow and annoying. So, same with the Atmel. I've got one of these

**Dave Jones:** STK500s. I think it's one of the worst development starter kits I've ever used. It's crap. It's just so convoluted and confusing. And I can remember when I first my first experience with Atmel's was using the ATtiny26 micro and it did it it was supposed This

**Dave Jones:** STK500 was supposed to support the chip and it didn't. It didn't work. All the damn data sheets were wrong and I had to modify jumper cables and stuff like that to get the damn chip working and it's a

**Dave Jones:** pain in the ass. So, don't get this and I really wouldn't recommend you pay money for this. For 40 bucks, you can get one of these serial in-circuit programmers. You can hook them straight up to your breadboard or wire your trip

**Dave Jones:** chip straight into your board and do in-circuit programming and debugging. It's great. Now, I'll give you a big tip here. Do not use any of these third-party or do-it-yourself programmers. These, you know, build-it-yourself designs for $5 you can

**Dave Jones:** plug into your parallel port or something like that. They are complete and utter garbage. DO NOT BUY THEM. PLEASE, you'll regret it. Trust me. When you can buy the official manufacturer's programmer for 40 or 50 bucks, which has

**Dave Jones:** proper support for every part in the range and, you know, it it they just cannot be beat. It's not worth saving 30 bucks and having all that grief when when your project is doesn't work and you got to figure out, oh, is it the is

**Dave Jones:** it the software? Is it my hardware I've built? Is it the programmer I've built? Is it the you know, is it the programming software? Or does it support this? Does it support that? Give me a break. Buy the real

**Dave Jones:** programmer, trust me. Now, when I started back in with PICs very early on, you know, if if you bought the PICstart programmer, which is I think the only one they had at the time, it was hundreds of dollars, very expensive. The

**Dave Jones:** hobbyists couldn't afford it. So, you were forced to use these low-cost, do-it-yourself programmers. And I started out with um the New Found Wolf 3, I think it was at the time. This is the Wolf 13 I upgraded to. But you

**Dave Jones:** know, it's it's done by a guy in Australia, and and it was it was the best third-party cheap programmer for PICs at the time. But I don't think you can buy this anymore. But there's still lots of these third-party programmers

**Dave Jones:** out there. Please, do not touch them. I'll tell you a story about one of my first experiences with and in fact my first experience with um Atmel chips. It was the ATtiny26s, as I've mentioned. And it's I was using the in-circuit. I soldered

**Dave Jones:** it onto my board. I used the in-circuit serial programmer. Great, right? Fantastic. And I was playing around with all the register settings and you know, mucking around trying to experiment with it and figure out how it all works. And

**Dave Jones:** all of a sudden, it just stopped. It just didn't work anymore. And I was scratching my head for ages trying to figure out is it my board? Has something failed? Have I blown my chip? Have I you know, is the software not working or is

**Dave Jones:** the programmer blown or you know, I couldn't read the chip. I couldn't program it. Well, what it was is I accidentally programmed one of the fuse settings one of the the the main fuse settings in the AVR micro, which disabled the in-circuit

**Dave Jones:** programming port. And it permanently disables it. So, that it that the board you soldered that chip on is useless. You've got to physically unsolder the chip and put it in a parallel programmer to reprogram it or solder in a new chip

**Dave Jones:** from scratch. It's [ __ ] It's a real trap for young players. Now, I know a lot of people, the fanboys will come out and say, "Well, that's that's actually a feature because it's designed to secure the chip." Well, okay, fair enough. You

**Dave Jones:** can look at it both ways. It is a feature, but it's a real big trap for young players. You've got to watch out with with the Atmels. The PICs don't have such a problem. You use the in-circuit serial programmer and if you

**Dave Jones:** blow the wrong fuse bits, it doesn't matter. You can erase the chip, start again. Not a problem. So, watch out for it. Now, one of the big differences which will the AVR fanboys like to trump with the Atmels is that they're four times

**Dave Jones:** faster than the equivalent 16 series PIC. And well, technically that might be true because the Atmels execute things typically in one clock cycle, whereas the PICs typically take four clock cycles. Now, it's not always like that. The Atmels don't always do it in one, so

**Dave Jones:** don't get carried away, but yes, the Atmels are faster, higher millions of instructions per second when you compare them. But, you know, it's my argument to that is well, who gives a [ __ ] Really. If you're actually if you're designing

**Dave Jones:** some high-speed high-processing Why the hell are you pushing it to 16 or 30 MIPS or something on an 8-bit micro? Go and use a 16 or a 32-bit and you'll probably cut your power consumption for the same price. God. It's you know,

**Dave Jones:** don't be sold by the fact that the Atmel is faster. It's not the huge advantage which they claim it to be, I don't think. But, you can argue until the cows come home, of course, but it's application specific. And then, of

**Dave Jones:** course, the differences aren't the same when you start talking about the uh the PIC 16-bit series and the PIC 32-bit series, you know? They are They are excellent um architectures that are quite fast and efficient. Um the PIC 32

**Dave Jones:** uses the MIPS 4000 series, and the um AVR, they don't do a 16-bit version, they only have a 32-bit version, which uses the uh their own proprietary 32-bit um architecture, whereas the MIPS has the advantage there in the 32-bit one in

**Dave Jones:** that um it uses standard MIPS 4000, so there's more development tools available, technically. But, Atmel also offer an ARM solution, the ARM the the 32-bit ARM 7 and ARM 9 stuff. So, really um you know, if you're going 32-bit,

**Dave Jones:** it's uh you know, if you want to use ARM, go Atmel. If you want to If you're happy with the MIPS 4000, then go for the PIC. But, the good thing about the PIC is that um the MPLAB development

**Dave Jones:** environment and the tools, okay? This $140 tool and the one MPLAB development environment will allow you to go seamlessly from a little six-pin 8-bit PIC all the way up to their PIC 32s. It'll be a common interface, and

**Dave Jones:** that's one of the big advantages, I think, of the um of of the Microchip development system over Atmel. And that's not to be um taken lightly, really, because that that can be a huge advantage for a lot of people. One other

**Dave Jones:** advantage of the Microchip is that um you can get the online You can buy them direct online, and you can have them pre-programmed, as well, directly from the factory, which is which is a really cool feature. So, something to consider.

**Dave Jones:** Now, when it comes down to architecture, I'm not going to go into the huge differences, but the Atmel fanboys will claim that the Atmel architecture is more efficient than the PIC. And well, you'll get no argument from me, really.

**Dave Jones:** It is. Okay? Um it's, you know, it's it's more efficient in uh in in quite a few ways, okay? But, um that doesn't mean that doesn't mean much at all. It might mean totally squat for your application. A lot of the people uh will

**Dave Jones:** claim that the PIC 16 series does not work with C compilers. Well, that's absolute and utter [ __ ] Because if you get a high-quality C com- compiler like the HI-TECH C compiler, which Microchip have just bought, I've They're

**Dave Jones:** very efficient. They're brilliant compilers. And I've actually used C easily on the 16-bit um PIC micros with only 1 or 2 KB of flash memory and, you know, 300 bytes of SRAM, right? Really tiny memory footprints. Work fine with C. So, don't

**Dave Jones:** give me that rubbish that it doesn't support C, because the PICs do. You've just got to have a good compiler for it. And Microchip actually offer that compiler um free. They Well, it's a um the HI-TECH one for the 16 series is free,

**Dave Jones:** and the one for the 18 series and the 30 uh the 16-bit series PICs and the 32-bit series PICs, they're all free, but they're limited in code optimization. Now, on the Atmel side of things, they offer the uh free GCC compiler, and

**Dave Jones:** there's a front end for it called WinAVR, I think it is. Now, when I last used that, it was the most atrocious piece of software I've ever seen. It was awful for a beginner. You had to be some, you know, super computer science

**Dave Jones:** PhD script nerd just to get the thing to compile a Hello World program. It was ridiculous. To set it up and get this GCC program working, you had to be the Linux bloody penguin. And it was hopeless. Now, I haven't used it for

**Dave Jones:** quite some time, so don't quote me on that. It could actually be much better these days, much easier to use, much simpler to install, and things like that. But, a lot of these Atmel fanboys will claim that the you know, it has

**Dave Jones:** this ACC GCC compiler and it's the greatest thing since sliced bread. Don't necessarily believe them cuz I reckon the Microchip one is really easy to install and really easy to use. So, you know, it's you got to look at it from both sides of

**Dave Jones:** the fence. Give them both a try and see what you think. Now, as far as feature sets go on the market, all the all the peripherals which surround the actual CPU, well, you can compare those until the cows come

**Dave Jones:** home. But, one thing you got to consider is that Microchip have like five or 600 hundred different variations of PIC micro. So, you can choose exactly the one tailored to your particular niche application. And that can have some huge

**Dave Jones:** advantages. It can have some disadvantages too in terms of you know, supply and lead times and and product viability in the future and things like that. But, it's it's good to have choice. Atmel can't even come close to competing in terms of choice for the

**Dave Jones:** micros. But, as a general rule, the Atmels might be more feature equipped for in a generic type device than the PIC ones. But, there's there's nothing in it, really. So, feature wise, it's very hard to compare. Now, sometimes as a

**Dave Jones:** professional designer, I like to keep my options open for micros as I've said. And sometimes I can when I start a new project, it can take me weeks to investigate and choose the mice the best microcontroller for the particular

**Dave Jones:** project I'm working on. Now, some companies don't give you that choice as a designer because they will you'll be locked into some particular family or some particular part because that's the approved part. It's got an approved part number. It's got a

**Dave Jones:** purchasing schedule and God knows what. But if you do have the choice then you know you can spend weeks investigating just the just the right micro for the task and I'll always keep an open mind when I start a project. So you know I'll go

**Dave Jones:** I'll look at my requirements the processing speed. Do I have to worry about low power ultra low power. Do I need DSP? Am I doing FFT stuff? Do I need a you know a differential amp in there? Do I need a voltage reference in

**Dave Jones:** there? Do I need a DAC output? Do I need this? Do I need an LCD interface? Etc. etc. And doing the research on that can just it can take a long time. Now you have to do that or you should do

**Dave Jones:** that in a professional application cuz it's worth it to get the right part for the job. But if you're just a hobbyist you know you you just might go out and use the same part over and over again

**Dave Jones:** cuz it's some huge generic part and it does everything you need. Well that's fine but just realize when you get more advanced and you get into professional design you really need to keep your options open and you know even though

**Dave Jones:** PIC have say you know 500 600 different parts it doesn't mean I'm going to find a suitable part in there in their entire range. Sometimes I don't. So I'm I'm going to use I'll look at Atmel or I'll

**Dave Jones:** look at TI or I'll look at Motorola or I'll look at somebody else. You know that's just the way it is. Now I've got to admit because I've been using PIC for quite some time when I start a new project I'm probably going

**Dave Jones:** to on the side of microchip as a first choice but only because that's the micro I'm familiar with at that particular point in time. Sometimes I can go for a year or more without using PICs. I might use Atmel for a year and when I I a new

**Dave Jones:** project I'm going to consider Atmel because that's the one that's familiar in my head at that particular time because I found that if you don't keep up, if you don't keep your skills up, you can easily lose them when you move

**Dave Jones:** to a different micro. You can easily acquire them back fairly quickly, but you know, you're going to err towards the side of the micro that you're familiar with. And well, there's nothing inherently wrong with that. So, who's going to win the big fistfight

**Dave Jones:** between PIC and AVR? Well, just like I said at the beginning, it doesn't matter a rat's ass. And if you argue over it, well, you're just a complete and utter [ __ ] and a bad engineer cuz you should keep your

**Dave Jones:** options open. So, beginners, my advice is it doesn't matter. Choose whichever one you think is going to suit your needs. And if you don't know, well, toss a damn coin. And no doubt I've pissed off the fanboys. I guarantee I have. So,

**Dave Jones:** fanboys, go for your damn life. Leave all the comments you want. Point out all the errors. Point out all, you know, why I'm wrong and why I don't care. You're a [ __ ] and I'm going to ignore you.
