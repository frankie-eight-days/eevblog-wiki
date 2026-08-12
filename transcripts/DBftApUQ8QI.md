---
video_id: DBftApUQ8QI
title: EEVblog #63 - Microchip PIC vs Atmel AVR
url: https://www.youtube.com/watch?v=DBftApUQ8QI
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 37, "3": 63, "4": 77, "5": 100, "6": 112, "7": 126, "8": 133, "9": 149, "10": 159, "11": 172, "12": 195, "13": 212, "14": 220, "15": 234, "16": 248, "17": 258, "18": 274, "19": 290, "20": 306, "21": 315, "22": 328, "23": 343, "24": 359, "25": 382, "26": 397, "27": 413, "28": 426, "29": 438, "30": 456, "31": 474, "32": 490, "33": 505, "34": 517, "35": 526, "36": 539, "37": 552, "38": 561, "39": 584, "40": 593, "41": 618, "42": 627, "43": 644, "44": 660, "45": 678, "46": 688, "47": 698, "48": 710, "49": 724, "50": 736, "51": 749, "52": 769, "53": 779, "54": 788, "55": 801, "56": 816, "57": 827, "58": 838, "59": 850, "60": 871, "61": 882, "62": 903, "63": 914, "64": 932, "65": 960, "66": 974, "67": 982, "68": 1006, "69": 1024, "70": 1035, "71": 1048, "72": 1071, "73": 1088, "74": 1100, "75": 1118, "76": 1131, "77": 1144, "78": 1158, "79": 1171, "80": 1185, "81": 1198, "82": 1214, "83": 1224, "84": 1239, "85": 1251, "86": 1261, "87": 1271, "88": 1288, "89": 1297, "90": 1307, "91": 1322, "92": 1330, "93": 1348, "94": 1359, "95": 1372, "96": 1394, "97": 1405, "98": 1421, "99": 1436, "100": 1446}
---

**Dave Jones:** Hi, welcome to the EEVblog and electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, I'm finally going to get around to doing a blog which has been on my list for almost since the start of this blog.

**Dave Jones:** Every week, probably on average, I get an email from someone saying, "Dave, can you do a blog on PIC versus AVR, PIC Microchip versus Atmel?" You know, I get these emails from beginners wanting to know which one they should be using, which is the best, and uh, you know, have I got any advice for them?

**Dave Jones:** Well, okay, here's my blog on PIC versus Atmel. Now, at first I thought it was a really good idea for a blog. It'd be terrific, you know, I could go through all the technical details of the architectures and the and the tools and the, you know, the feature set and price and everything, and, you know, come to a conclusion as to which one, you know, which best for beginners or which is

**Dave Jones:** best for somebody else. And, oh, the more I think about it, the more I realize I just cannot do a technical blog on it. I just, like, a full-on all the technical details comparing AVR to PIC.

**Dave Jones:** It's just It's I The more I think about it, the more I think it's just totally and utterly pointless. Cuz I know if I do it, I'm going to It doesn't matter what I say, what conclusions I come to, there'll be rabid fanboys of each microcontrollers, but particularly the Atmels, the AVR freaks out there, who will come to the defense and slag me off.

**Dave Jones:** Now, I don't normally, you know, care about people slagging me off, but I know they're going to do it. They're going to point out every technical, not so much error, but they're going to point out, "Oh, you didn't do this.

**Dave Jones:** This isn't right. This better in this respect. This one's better." And, ah, I'm not going to fall for it. So, instead, I'm just going to give you my general opinion on PIC versus Atmel.

**Dave Jones:** Now, let me give you the skinny right up front. I'll get to the bottom line of it straight away. Which should you choose if you're a beginner, PIC or AVR?

**Dave Jones:** Well, the answer is it doesn't bloody well matter. Why? Because it's it it really doesn't. They're both microcontrollers. They're both excellent. They're both some of the biggest on the market.

**Dave Jones:** They've both got excellent support. They've both got excellent beginner kits available. They've both got free development tools. They've both got this. And then it's just really it doesn't matter.

**Dave Jones:** My advice to you is find a development kit, a starter kit, which suits your purposes, suits your needs. Some of them will have various features, either LCDs or motor controls or whatever on it.

**Dave Jones:** Um, pick one that you that's within your price range, that you like, and you know, buy it and go for it because it doesn't matter. Now, if you want to be a good engineer, if you want to be a top engineer, you will not be one of these rabid fanboys who religiously sticks to one particular microcontroller family.

**Dave Jones:** You will always keep your options open. And you can tell an absolute [ __ ] designer because they're so passionate about one particular um part or one particular manufacturer and they'll just ignore all others um even to their own detriment.

**Dave Jones:** And really, you know, that might be okay for hobby use, but if you're a professional designer, if you're a professional design engineer, you've got to keep your options open.

**Dave Jones:** That's just the way it is. Now, I'm um I've I've got to admit, I'm more of a fan of the uh PICs than the Atmels purely because, um, I've been using them longer.

**Dave Jones:** I think their support is, uh, better in many respects. Um, and I like their tool set better than the, um, Atmel ones, and I'll go into that. And, well, it but there's not much in it.

**Dave Jones:** Now, I've used both PIC and Atmel, and I've used, you know, other brand microcontrollers as well, but PIC and Atmel are sort of the two biggies that you always hear about.

**Dave Jones:** And they're not necessarily the biggest on the market, but, you know, like you don't hear about Motorola at all, right? You hardly ever hear about Motorola, but they're like, still, I I believe number one in the automotive market, or maybe even the white goods market as well, or something like that.

**Dave Jones:** But you don't hear about them cuz they're they're not they're just some, um, you know, industrial thing that companies just use because they've been using them for 20 years, and that's what they use, and they're happy to use it, and they're great, and they just work, and, you know, they don't make the mainstream media.

**Dave Jones:** They don't make the magazines. They don't really have hobbyist level intro kits, or they don't do it as well as PIC and Atmel do. So, that's why you never hear about other ones, you know, um, you know, Motorola and, um, you know, TI MSP430s aren't, uh, too bad.

**Dave Jones:** They've got a bit of, um, you know, in bit of foothold in the beginner market as well. And, but, you know, PIC and Atmel are the two big ones.

**Dave Jones:** And, really, if you're going to I think if you're going to start out with a micro, you should be picking one of them, just purely because of the support available, the beginner supports, the starter kits, the books, and things like that.

**Dave Jones:** Now, when it comes to these fanboys, I think that, um, Atmel AVR ones win hands down. They are most they are the most rabid, fierce defenders of their religion, which is Atmel, and they hate PIC so much.

**Dave Jones:** And they it's laughable. Every You know, if you go on a forum and ask which is the best PIC versus Atmel, a lot of times the PIC guys will say, "Oh, you know, PIC's okay and I use it and that's okay, but you should consider the others." But the Atmel guys won't do that.

**Dave Jones:** No, you must use freaking Atmel. And yet, you know, they will just defend it until death. It's ridiculous. What a bunch of [ __ ] Now, if you want to look at the choice of PIC versus Atmel from a professional point of view, if I was if I was, you know, starting a new company and they asked me, "We have to pick a microcontroller to, you know, to

**Dave Jones:** make our new products with, which one you should you choose?" Well, there's a whole range of factors which go into the decision, but as a first order, you know, a first order guess approximation, I would tend towards PIC Microchip.

**Dave Jones:** Why? Because they're a they're a bigger company. They're bigger, more stable, and I think they've got a better future. That's They And they they just facts, really. I mean, Atmel, it's as far as I'm aware, they have actually not made a profit from day one.

**Dave Jones:** I I could be wrong there, but I think it's that's pretty darn close to the mark. And Atmel are And most of the other manufacturers are most of the other microcontroller manufacturers are in deep financial trouble.

**Dave Jones:** And as you might know, PIC actually tried to buy Atmel. They tried a hostile take take over which failed. That was about 6 months ago or something or something like that.

**Dave Jones:** And really it just didn't work. So, there's going to be but you haven't heard the end of that because there's going to be more consolidation in the microcontroller market because Microchip are pretty much the standouts financially and and their future stability.

**Dave Jones:** They're they're doing pretty well and the others are really struggling. So, you're going to see a lot more mergers in the microcontroller market, I think. Because as a professional designer, often you've got to actually consider the longevity of the parts you're actually building in to your design.

**Dave Jones:** Not just this design, but future designs. And you know, um it's a quite uh common occurrence to actually try and get uh written assurance from a manufacturer that the part you've chosen is going to be available still available in 10 years time.

**Dave Jones:** And and that can be pretty important. It's not going to matter a rat's ass for hobbyists use or you know, designing you know, small-scale projects. But when you're building parts into multi-million dollar bits of equipment or stuff like that, it's very important.

**Dave Jones:** So, for some advice when you're looking to uh get some development kits for your first microcontroller, pick or Atmel. The others are The others are the same really, but I think PIC has an edge.

**Dave Jones:** I've mentioned it before. It's the PICkit, right? The PICkit 2 or the PICkit 3. Don't get put off by my bad remarks about the PICkit 3 because that was in comparison to the PICkit 2.

**Dave Jones:** It sucked. But um on its own, it's still pretty good. And it's only 40 bucks. And it does in-circuit debugging and in-circuit programming. And it's the official um authorized by Microchip.

**Dave Jones:** Now, the Atmel one, you can get the a similar price, you know, $40 or something like that, $50 in-circuit serial programmer, JTAG programmer. But this one, I believe, doesn't Well, it doesn't do debugging.

**Dave Jones:** If you want to do debugging on the Atmels, you've got to pay a lot more for the in-circuit um debugger emulator device. I'm not sure the price of that, but I think it's in the hundreds of dollars.

**Dave Jones:** Now, when you're uh looking at these sort of tools, I highly recommend you don't get these parallel programmers like the PICstart Plus. It It Well, it might be okay if you're building something on a breadboard and you put your chip in and you program it and you move it over to your breadboard, but you know, really you want to do in-circuit debugging and you don't want to be

**Dave Jones:** plugging the chip every time you recompile the software cuz it's a pain in the ass and it can ruin your chip and it's just slow and annoying. So, same with the Atmel.

**Dave Jones:** I've got one of these STK500s. I think it's one of the worst development starter kits I've ever used. It's crap. It's just so convoluted and confusing. And I can remember when I first my first experience with Atmel's was using the ATtiny26 micro and it did it it was supposed This STK500 was supposed to support the chip and it didn't.

**Dave Jones:** It didn't work. All the damn data sheets were wrong and I had to modify jumper cables and stuff like that to get the damn chip working and it's a pain in the ass.

**Dave Jones:** So, don't get this and I really wouldn't recommend you pay money for this. For 40 bucks, you can get one of these serial in-circuit programmers. You can hook them straight up to your breadboard or wire your trip chip straight into your board and do in-circuit programming and debugging.

**Dave Jones:** It's great. Now, I'll give you a big tip here. Do not use any of these third-party or do-it-yourself programmers. These, you know, build-it-yourself designs for $5 you can plug into your parallel port or something like that.

**Dave Jones:** They are complete and utter garbage. DO NOT BUY THEM. PLEASE, you'll regret it. Trust me. When you can buy the official manufacturer's programmer for 40 or 50 bucks, which has proper support for every part in the range and, you know, it it they just cannot be beat.

**Dave Jones:** It's not worth saving 30 bucks and having all that grief when when your project is doesn't work and you got to figure out, oh, is it the is it the software?

**Dave Jones:** Is it my hardware I've built? Is it the programmer I've built? Is it the you know, is it the programming software? Or does it support this? Does it support that?

**Dave Jones:** Give me a break. Buy the real programmer, trust me. Now, when I started back in with PICs very early on, you know, if if you bought the PICstart programmer, which is I think the only one they had at the time, it was hundreds of dollars, very expensive.

**Dave Jones:** The hobbyists couldn't afford it. So, you were forced to use these low-cost, do-it-yourself programmers. And I started out with um the New Found Wolf 3, I think it was at the time.

**Dave Jones:** This is the Wolf 13 I upgraded to. But you know, it's it's done by a guy in Australia, and and it was it was the best third-party cheap programmer for PICs at the time.

**Dave Jones:** But I don't think you can buy this anymore. But there's still lots of these third-party programmers out there. Please, do not touch them. I'll tell you a story about one of my first experiences with and in fact my first experience with um Atmel chips.

**Dave Jones:** It was the ATtiny26s, as I've mentioned. And it's I was using the in-circuit. I soldered it onto my board. I used the in-circuit serial programmer. Great, right? Fantastic. And I was playing around with all the register settings and you know, mucking around trying to experiment with it and figure out how it all works.

**Dave Jones:** And all of a sudden, it just stopped. It just didn't work anymore. And I was scratching my head for ages trying to figure out is it my board? Has something failed?

**Dave Jones:** Have I blown my chip? Have I you know, is the software not working or is the programmer blown or you know, I couldn't read the chip. I couldn't program it.

**Dave Jones:** Well, what it was is I accidentally programmed one of the fuse settings one of the the the main fuse settings in the AVR micro, which disabled the in-circuit programming port.

**Dave Jones:** And it permanently disables it. So, that it that the board you soldered that chip on is useless. You've got to physically unsolder the chip and put it in a parallel programmer to reprogram it or solder in a new chip from scratch.

**Dave Jones:** It's [ __ ] It's a real trap for young players. Now, I know a lot of people, the fanboys will come out and say, "Well, that's that's actually a feature because it's designed to secure the chip." Well, okay, fair enough.

**Dave Jones:** You can look at it both ways. It is a feature, but it's a real big trap for young players. You've got to watch out with with the Atmels. The PICs don't have such a problem.

**Dave Jones:** You use the in-circuit serial programmer and if you blow the wrong fuse bits, it doesn't matter. You can erase the chip, start again. Not a problem. So, watch out for it.

**Dave Jones:** Now, one of the big differences which will the AVR fanboys like to trump with the Atmels is that they're four times faster than the equivalent 16 series PIC. And well, technically that might be true because the Atmels execute things typically in one clock cycle, whereas the PICs typically take four clock cycles.

**Dave Jones:** Now, it's not always like that. The Atmels don't always do it in one, so don't get carried away, but yes, the Atmels are faster, higher millions of instructions per second when you compare them.

**Dave Jones:** But, you know, it's my argument to that is well, who gives a [ __ ] Really. If you're actually if you're designing some high-speed high-processing Why the hell are you pushing it to 16 or 30 MIPS or something on an 8-bit micro?

**Dave Jones:** Go and use a 16 or a 32-bit and you'll probably cut your power consumption for the same price. God. It's you know, don't be sold by the fact that the Atmel is faster.

**Dave Jones:** It's not the huge advantage which they claim it to be, I don't think. But, you can argue until the cows come home, of course, but it's application specific. And then, of course, the differences aren't the same when you start talking about the uh the PIC 16-bit series and the PIC 32-bit series, you know?

**Dave Jones:** They are They are excellent um architectures that are quite fast and efficient. Um the PIC 32 uses the MIPS 4000 series, and the um AVR, they don't do a 16-bit version, they only have a 32-bit version, which uses the uh their own proprietary 32-bit um architecture, whereas the MIPS has the advantage there in the 32-bit one in that um it uses standard MIPS 4000, so there's more development tools

**Dave Jones:** available, technically. But, Atmel also offer an ARM solution, the ARM the the 32-bit ARM 7 and ARM 9 stuff. So, really um you know, if you're going 32-bit, it's uh you know, if you want to use ARM, go Atmel.

**Dave Jones:** If you want to If you're happy with the MIPS 4000, then go for the PIC. But, the good thing about the PIC is that um the MPLAB development environment and the tools, okay?

**Dave Jones:** This $140 tool and the one MPLAB development environment will allow you to go seamlessly from a little six-pin 8-bit PIC all the way up to their PIC 32s. It'll be a common interface, and that's one of the big advantages, I think, of the um of of the Microchip development system over Atmel.

**Dave Jones:** And that's not to be um taken lightly, really, because that that can be a huge advantage for a lot of people. One other advantage of the Microchip is that um you can get the online You can buy them direct online, and you can have them pre-programmed, as well, directly from the factory, which is which is a really cool feature.

**Dave Jones:** So, something to consider. Now, when it comes down to architecture, I'm not going to go into the huge differences, but the Atmel fanboys will claim that the Atmel architecture is more efficient than the PIC.

**Dave Jones:** And well, you'll get no argument from me, really. It is. Okay? Um it's, you know, it's it's more efficient in uh in in quite a few ways, okay? But, um that doesn't mean that doesn't mean much at all.

**Dave Jones:** It might mean totally squat for your application. A lot of the people uh will claim that the PIC 16 series does not work with C compilers. Well, that's absolute and utter [ __ ] Because if you get a high-quality C com- compiler like the HI-TECH C compiler, which Microchip have just bought, I've They're very efficient.

**Dave Jones:** They're brilliant compilers. And I've actually used C easily on the 16-bit um PIC micros with only 1 or 2 KB of flash memory and, you know, 300 bytes of SRAM, right?

**Dave Jones:** Really tiny memory footprints. Work fine with C. So, don't give me that rubbish that it doesn't support C, because the PICs do. You've just got to have a good compiler for it.

**Dave Jones:** And Microchip actually offer that compiler um free. They Well, it's a um the HI-TECH one for the 16 series is free, and the one for the 18 series and the 30 uh the 16-bit series PICs and the 32-bit series PICs, they're all free, but they're limited in code optimization.

**Dave Jones:** Now, on the Atmel side of things, they offer the uh free GCC compiler, and there's a front end for it called WinAVR, I think it is. Now, when I last used that, it was the most atrocious piece of software I've ever seen.

**Dave Jones:** It was awful for a beginner. You had to be some, you know, super computer science PhD script nerd just to get the thing to compile a Hello World program.

**Dave Jones:** It was ridiculous. To set it up and get this GCC program working, you had to be the Linux bloody penguin. And it was hopeless. Now, I haven't used it for quite some time, so don't quote me on that.

**Dave Jones:** It could actually be much better these days, much easier to use, much simpler to install, and things like that. But, a lot of these Atmel fanboys will claim that the you know, it has this ACC GCC compiler and it's the greatest thing since sliced bread.

**Dave Jones:** Don't necessarily believe them cuz I reckon the Microchip one is really easy to install and really easy to use. So, you know, it's you got to look at it from both sides of the fence.

**Dave Jones:** Give them both a try and see what you think. Now, as far as feature sets go on the market, all the all the peripherals which surround the actual CPU, well, you can compare those until the cows come home.

**Dave Jones:** But, one thing you got to consider is that Microchip have like five or 600 hundred different variations of PIC micro. So, you can choose exactly the one tailored to your particular niche application.

**Dave Jones:** And that can have some huge advantages. It can have some disadvantages too in terms of you know, supply and lead times and and product viability in the future and things like that.

**Dave Jones:** But, it's it's good to have choice. Atmel can't even come close to competing in terms of choice for the micros. But, as a general rule, the Atmels might be more feature equipped for in a generic type device than the PIC ones.

**Dave Jones:** But, there's there's nothing in it, really. So, feature wise, it's very hard to compare. Now, sometimes as a professional designer, I like to keep my options open for micros as I've said.

**Dave Jones:** And sometimes I can when I start a new project, it can take me weeks to investigate and choose the mice the best microcontroller for the particular project I'm working on.

**Dave Jones:** Now, some companies don't give you that choice as a designer because they will you'll be locked into some particular family or some particular part because that's the approved part.

**Dave Jones:** It's got an approved part number. It's got a purchasing schedule and God knows what. But if you do have the choice then you know you can spend weeks investigating just the just the right micro for the task and I'll always keep an open mind when I start a project.

**Dave Jones:** So you know I'll go I'll look at my requirements the processing speed. Do I have to worry about low power ultra low power. Do I need DSP? Am I doing FFT stuff?

**Dave Jones:** Do I need a you know a differential amp in there? Do I need a voltage reference in there? Do I need a DAC output? Do I need this? Do I need an LCD interface?

**Dave Jones:** Etc. etc. And doing the research on that can just it can take a long time. Now you have to do that or you should do that in a professional application cuz it's worth it to get the right part for the job.

**Dave Jones:** But if you're just a hobbyist you know you you just might go out and use the same part over and over again cuz it's some huge generic part and it does everything you need.

**Dave Jones:** Well that's fine but just realize when you get more advanced and you get into professional design you really need to keep your options open and you know even though PIC have say you know 500 600 different parts it doesn't mean I'm going to find a suitable part in there in their entire range.

**Dave Jones:** Sometimes I don't. So I'm I'm going to use I'll look at Atmel or I'll look at TI or I'll look at Motorola or I'll look at somebody else. You know that's just the way it is.

**Dave Jones:** Now I've got to admit because I've been using PIC for quite some time when I start a new project I'm probably going to on the side of microchip as a first choice but only because that's the micro I'm familiar with at that particular point in time.

**Dave Jones:** Sometimes I can go for a year or more without using PICs. I might use Atmel for a year and when I I a new project I'm going to consider Atmel because that's the one that's familiar in my head at that particular time because I found that if you don't keep up, if you don't keep your skills up, you can easily lose them when you move to a different micro.

**Dave Jones:** You can easily acquire them back fairly quickly, but you know, you're going to err towards the side of the micro that you're familiar with. And well, there's nothing inherently wrong with that.

**Dave Jones:** So, who's going to win the big fistfight between PIC and AVR? Well, just like I said at the beginning, it doesn't matter a rat's ass. And if you argue over it, well, you're just a complete and utter [ __ ] and a bad engineer cuz you should keep your options open.

**Dave Jones:** So, beginners, my advice is it doesn't matter. Choose whichever one you think is going to suit your needs. And if you don't know, well, toss a damn coin. And no doubt I've pissed off the fanboys.

**Dave Jones:** I guarantee I have. So, fanboys, go for your damn life. Leave all the comments you want. Point out all the errors. Point out all, you know, why I'm wrong and why I don't care.

**Dave Jones:** You're a [ __ ] and I'm going to ignore you.
