---
video_id: 0N5CwjIM5mc
title: EEVblog #31 - Microcontroller Datasheet Utopia
url: https://www.youtube.com/watch?v=0N5CwjIM5mc
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 25, "3": 37, "4": 53, "5": 70, "6": 78, "7": 96, "8": 118, "9": 132, "10": 142, "11": 160, "12": 170, "13": 196, "14": 208, "15": 221, "16": 245, "17": 258, "18": 272, "19": 289, "20": 300, "21": 314, "22": 324, "23": 346, "24": 356, "25": 371, "26": 397, "27": 418, "28": 433, "29": 450, "30": 463}
---

**Dave Jones:** Welcome to the AE blog. I'm your host, Dave Jones, and this is episode number 31. I was trolling some websites the other day looking for a 32-bit micro, as you do.

**Dave Jones:** And in fact, I was looking for the new micro for my new Mark II Micro Watch project I'm slowly working on. And anyway, unlike some engineers, I like to keep an open mind in the parts I select for my next project.

**Dave Jones:** I'm not one of these fanboys or one of these religious fanatics who said, "Oh, I got to use a pic or you've got to use an AVR or you've got to use an arm or something like that." I like to keep my options open, as you do.

**Dave Jones:** So, I was trolling these websites looking for a new 32-bit micro, and I came across the NEC range of micros. They've got eight through to 32-bit micros. Got a whole bunch of them, and I you know, I figured, "Ah, who uses NEC?

**Dave Jones:** Nobody uses NEC. I've never heard of anyone who uses NEC micros." I'm sure there's someone out there. They must sell them for a reason. In fact, they probably sell millions of them, but hey, you know, it's not something I was familiar with, and it didn't quite do the job, but something caught my eye.

**Dave Jones:** And well, you know, they've got the links to the PDF data sheets, and I was looking through, and they had a link to what they called a one-page manual.

**Dave Jones:** And I thought, "Huh, okay, it's just a maybe it's just a summary or something like that. A lot of data sheet makers include a summary sheet, you know, just a couple of pages to explain the basic stuff of the product." But I downloaded it, and I was absolutely gobsmacked.

**Dave Jones:** It was the most beautiful thing I've ever seen. And here it is. You probably I'm sure you can't make out any detail on that at whatsoever. But this is what NEC call their one-page manual, and it really is the most amazing bit of documentation I've ever seen.

**Dave Jones:** It really is a complete one-page manual for the for the microcontrollers. In this case, the 78K series micros. As soon as I saw this thing, I went, "I've got to do a blog on this.

**Dave Jones:** This is great." And a blog on documentation. Now, I'm sure I can put up some better uh shots of this later so you can actually see it in detail, and I'll put up some links, too.

**Dave Jones:** But, what this uh one-page manual is is check it out, right? It's a complete one-page manual for this particular chip. In this case, it's a 78 uh KOS uh KA1 plus the boringly titled chip, as they usually do.

**Dave Jones:** You know what I mean? It means absolutely nothing. And they got another number under there. It's, you know, it's just crap. I hate how they number them. Anyway, that's beside the point.

**Dave Jones:** This is a 20-pin microcontroller, okay? And it's basically um the pins are arranged one one through to 20 in the actual chip order, okay? So, it shows each pin, and then for each pin, it actually shows the detailed operation of that particular pin, the inputs and the outputs and the bits to select and and the register names, and you can read and write to it.

**Dave Jones:** And it shows those for every one of the pins. It shows the multiple pin functions, as well. It's absolutely amazing. I fell absolutely in love with this thing the first time I saw it.

**Dave Jones:** I thought, "Wow, why can't all the manufacturers have documentation this good?" I don't know who's doing this at NEC, but they they seriously need a pat on the back.

**Dave Jones:** This Now, if you're familiar with using micros like I am, you'll you download these data sheets, and they're like 2 300 pages, some of them. They're absolutely enormous. and if you want to know the register for using, you know, timer number one or something like that, you've got to search through or you've got to go through the tab list or something like that to actually find the

**Dave Jones:** information you want on that particular timer. And it can go for pages and pages and it typically has stuff like this. In this case, let's have a look. This is the 8-bit timer they've got there.

**Dave Jones:** They've got all the information you need for using the 8-bit timer and they've got another one down here, 16-bit. It's got the register map, it's got the register names, it's got what each bit and what each bit does, it's got the power on defaults.

**Dave Jones:** It's got It's got absolutely everything and they have these They have these little bubbles as well, these little text bubbles which actually show you which actually highlight any engineering notes.

**Dave Jones:** Like, you know, the normal data sheets are they put the little asterisks next to something and then you've got to scroll down to find out what it actually is and that really often contains a really important meaty bit of info that you need to make the chip work.

**Dave Jones:** And they've included those here next to the pin that they've Look, extended reset output functions right next to the reset pin, exactly where you want it. Look at this.

**Dave Jones:** It's unbelievably good. And of course, they've got the package information on here so you can actually see what packages it comes in. They've got the memory maps as well.

**Dave Jones:** They've got the processor registers, they've got UARTs, they've got standby functions, they've got how the watchdog timer works, how the analog to digital converter works and all the register settings and what you have to do and to set it up and use it, you don't need any more than this.

**Dave Jones:** One page to tell you how a complete chip works. It's incredible. My hat's off to the guys that have done this. And it's not just their small chips, either.

**Dave Jones:** This is another 78K0 micro, but this is one of their big 80-pin quad flat packs. Look at the size of this sucker. It's absolutely enormous. It's It's got everything.

**Dave Jones:** It's even got the kitchen sink. And that brings us to documentation. Now, electronics engineers, they typically hate they absolutely despise documentation until they actually need it. And when you need it, and you get an absolute work of art like this, I it's it just makes your life so incredibly easy, and you go, "I'm going to use these guys' parts.

**Dave Jones:** These are fantastic. Look at the documentation." Documentation can make or break your product. It doesn't matter what it is. Here's a top tip for you newbies out there. Or, heck, even if you've been in the industry a long time, and you're starting a new job, and you want to impress people right away, the best thing you can do is some really cool documentation.

**Dave Jones:** I'm telling you. Most companies out there don't do documentation very well, internal or external. And management and other people, they can be easily and easily seduced and impressed by simple basic documentation.

**Dave Jones:** It's absolutely amazing. The results you can achieve with just a five-page Word document, some Excel graphs Graphs are fantastic. Lots of data, tables, photos. Get a digital camera, take photos of everything.

**Dave Jones:** It's fantastic. Whack them in there, and you don't even need much content. It doesn't even matter what's really in there. If you If it looks fantastic, people will go, "Wow, this guy really knows his stuff." And this is the best thing ever.

**Dave Jones:** Trust me, documentation winner. I think I'm in love, really. Brings a tear to the eye.
