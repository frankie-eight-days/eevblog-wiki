---
video_id: hpZFiR8kM2g
title: EEVblog #58 - Warm and Fuzzy FPGA Troubleshooting
url: https://www.youtube.com/watch?v=hpZFiR8kM2g
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 31, "3": 44, "4": 66, "5": 82, "6": 97, "7": 114, "8": 129, "9": 145, "10": 160, "11": 181, "12": 205, "13": 218, "14": 232, "15": 246, "16": 261, "17": 272, "18": 285, "19": 299, "20": 314, "21": 326, "22": 342, "23": 358, "24": 373, "25": 389, "26": 402, "27": 417, "28": 431, "29": 446, "30": 461, "31": 475, "32": 488, "33": 503, "34": 518, "35": 535, "36": 549, "37": 563, "38": 578, "39": 596, "40": 619, "41": 636, "42": 652, "43": 674, "44": 691, "45": 714, "46": 733, "47": 750, "48": 766, "49": 784, "50": 801, "51": 820, "52": 840, "53": 856, "54": 872, "55": 885, "56": 899, "57": 912, "58": 927, "59": 939, "60": 958, "61": 974}
---

**Dave Jones:** Hi, welcome to the EEVblog and electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's industry story time again. I was working on something at work the other day and it was a real interesting

**Dave Jones:** problem that I thought would make an interesting blog. So, here we go. Okay, let me set the scene for you. We've got this product which we're putting into production and we've done some product we've done a couple of prototype runs

**Dave Jones:** before and a pre-production run and everything works just fine. And we've got this whole suite of automated tests which test every aspect of the product. And there's a whole bunch of them to be tested, you know, 50 different things to

**Dave Jones:** be tested. And um So, we put this new run a we put a new run through a pre-production thing and all the boards failed this one particular test and it was an audio codec. There's a 24-bit delta-sigma audio codec on there and a

**Dave Jones:** power amplifier for, you know, for actually recording and and actually playing back music, you know, MP3s or wave files or anything else. And that was failing. We're getting no audio out at all. So, I started to investigate the

**Dave Jones:** problem and this is what happened. So, I went through the basic troubleshooting procedures in a situation like this. Basically, the first thing you think of when a board has worked perfectly before and there've been no changes and all of

**Dave Jones:** a sudden you get a new batch back from the assembly factory and it's failed something or you go, "Okay, there's something wrong with the assembly." That's the, you know, that's the typical that's the typical scenario. So, I checked I visually checked every

**Dave Jones:** component in in the sections at fault, these audio sections, and various other sections as well. Couldn't find any visual faults. You know, they hadn't loaded um you know, there weren't any missing components from the board. And um you

**Dave Jones:** know, so I couldn't find anything. So, next step was to get my meter and go in and measure every part in in the um sections at fault. And uh I couldn't I I measured them all, compared them against a previous batch

**Dave Jones:** board, and I couldn't find any problems. They're all measuring okay. So, they hadn't loaded in the incorrect components. Bugger. I've got to, you know, go deeper into this and troubleshoot it further. So, let me take you through a basic

**Dave Jones:** block diagram of uh of the section at fault here. What we've got is a huge um Altera Cyclone III FPGA. It's a big BGA package, you know, 700 odd pin BGA. And it's running a 32-bit um soft core actual processor, and it's got an

**Dave Jones:** I2S um audio bus, and it's got a SPI control bus. And these two buses go to a um a Cirrus Logic CS4270 24-bit delta-sigma converter. And the codec goes into a little uh power amplifier, which drives some speakers and a headphone jack. Um

**Dave Jones:** and it's also got a uh an another audio jack, which you can plug into actually test the power amp. And the codec also has its own little uh local uh voltage regulator. Um and it's also got a little uh

**Dave Jones:** power-on-reset chip as well, and a couple of uh boot mode pins, which determine which mode the chip boots up in, cuz it's a fairly complex uh chip, and it's got various modes. And if you don't put it in the right mode, it

**Dave Jones:** doesn't work. In fact, I've done a blog on this um exact same chip way back, and I'll put the link up, and how that if you don't put it into the right mode, you get um these input lines can be inputs or

**Dave Jones:** outputs. And in and in the old blog, I um was fault finding a thing where it was outputting where it should have been inputting. Anyway, go check that one out as a bit of a background. So, the next thing I did, well, I can't

**Dave Jones:** we're getting no audio out at all. Is it the codec? Is it uh is it the uh something wrong with the FPGA? Is it something wrong with the power amp? Well, thankfully, the power amp's really easy to test because it's got a test

**Dave Jones:** jack. So, I just fed some audio in, and sure enough, it comes out perfectly. So, you know, you can scrap the audio amp. There's nothing wrong with that at all. So, next thing I look into is the codec.

**Dave Jones:** Now, I started the one of the golden rules of troubleshooting, thou shall measure voltages. And because, you know, a lot of the time, it's simply a going to be a power supply problem. So, I check the power supply. No problems

**Dave Jones:** there at all. So, rule that one out. Next, I think, "Aha, maybe the chip just isn't doing anything because um it's been the reset part of it's not working." So, I check that out, and no, sure enough, um the pin was high, and

**Dave Jones:** it's an active low reset, so there was nothing wrong with there. It should be working. Now, the next thing I checked is these boot mode um pins also because, you know, if it doesn't boot up in the correct mode,

**Dave Jones:** well, it's, you know, it's pretty much screwed. So, but I checked those, and they were okay, too. So, that left the communication that basically left the I2S and the SPI buses. Now, the first thing I did was probe the I2S bus, see

**Dave Jones:** if there's any um audio going in and out. You can look up what an I2S bus actually does. I won't explain it now, but it's basically a serial It's a standard serial audio interface. And I checked it and there was no data on

**Dave Jones:** there at all. There was nothing, which pretty much told me that either the software in here is doing nothing or this chip, as I knew from the previous encounter I had in the other blog, that if this chip obviously wasn't booting up

**Dave Jones:** in the correct mode because um when the when the whole system powers up, this the soft processor has to send a command via the SPI bus to switch this chip into um into the required mode. And that obviously wasn't happening.

**Dave Jones:** So, the next thing I do is go aha, it's got to be the SPI bus. So, I probe the SPI bus. And what do you know? There's no activity on there at all. Uh you know, there was just there was nothing.

**Dave Jones:** It was like it was dead. Um but I knew that the soft processor was working, the FPGA was fine because it run this um FPGA controls dozens and dozens of other things as well. And all of those passed

**Dave Jones:** their automated tests. And for each one of those tests, they have to download firmware in here. So, I knew, you know, every aspect of the FPGA was working. So, it was unlikely, I thought, to be a problem with just the

**Dave Jones:** pins on the BGA cuz BGAs are notorious for, you know, having having bad solder joints under them. So, I thought, it's you know, it's a bit too much of a coincidence that well, it's in fact it's impossible that every board in the batch

**Dave Jones:** could be faulty just on those pins. It's just not possible. So, I ruled that out. So, I thought, what's going on here? I was scratching my head for ages. And the other thing, there was there's a also a reset switch on here as well,

**Dave Jones:** which resets the soft processor. And I was playing around with that, and uh I could actually get stuff to happen on the SPI bus. When I was playing around with this reset, you do it enough times and and it it didn't work. It didn't

**Dave Jones:** make the chip work, but it made it do something, and I got something on the SPI bus and then something on the I2S bus. But it was just it was just garbage, really. Um but that that sort of indicated something, but I wasn't

**Dave Jones:** quite sure what. And it's about at this point where your mind starts going whacko, and it switches into super detail mode, and you start trying to think up all these weird and wonderful ways in which the uh FPGA

**Dave Jones:** can um somehow boot up and get into some mode that'll cause a problem with just that application and not the 20 other applications and things like that. You just start going bonkers. Now, being a hardware guy, I naturally

**Dave Jones:** blamed the software because well, you know, software's a pain in the ass, it really is. And so I thought, "Aha, have I got the wrong uh bit file which I'm downloading to this?" And I double-checked, triple-checked, and I did all sorts of things, and uh

**Dave Jones:** no, I'm downloading the correct bit file like we always have. I could test I could download the same bit file into a good board from the old batch and this new board, and the new board just wasn't working with the exact same bit file,

**Dave Jones:** exact same soft processor, same code, same everything. It was bizarre. So just as a sanity check, I was getting pretty desperate. So I I what I did is I wrote I wrote a brand new project for the FPGA

**Dave Jones:** that outputted data on all the pins so that I could check that there was actually, you know, continuity between the FPGA and the thing. And it was fine, there was no problem at all. This thing just got stranger and stranger. So,

**Dave Jones:** really, I'd started to exhaust all of the hardware avenues. I just I just knew it wasn't a, you know, a component loading problem or or something else. It just wasn't really a hardware issue. It must be a software issue, regardless of how

**Dave Jones:** weird that sounds. The software works on one board, but doesn't work on another. Aha, right? We're dealing with FPGAs here. The FPGAs are notorious for having all sorts of, um, timing issues. Every time you, uh, recompile or synthesize a a a program to go in a, um,

**Dave Jones:** you know, a thing to go inside the FPGA, all the timing is is different. Everything changes every time you make a small change to the, um, you know, to the how it actually works. And it's they're incredibly complex. So, I

**Dave Jones:** naturally thought, aha, do we have some sort of, um, weird marginal timing issue? So, I went to the software, um, guy who who wrote the software, and sure enough, right? Well, he was scratching his head too for a

**Dave Jones:** while, but it suddenly dawned on us that, um, that, uh, he had actually seen this problem or a similar problem with SPI bus initialization before. Because the FPGA, right? The, um, soft processor has a a very complex, uh, protocol, um, stack

**Dave Jones:** and it has an SPI, uh, protocol interface and it has it goes off to another FPGA up here, and, um, and and it's got an SPI, uh, SPI multiplexer in it, and it talks back and forth and does all sorts of

**Dave Jones:** weird, um, weird and wonderful things. And, uh, as it turns out, there was a compiler switch in the, uh, in the C compiler software, which which said, "Use this SPI, um, multiplexer." But, we were actually talking direct from here to here. We

**Dave Jones:** weren't using this SPI multiplexer, but it was enabled. And, sure enough, we disabled it, we recompiled it, we downloaded it, and it works. It was a software issue. Okay, so what's so remarkable about a software issue? Well, if you remember, it works perfectly on

**Dave Jones:** different batches of boards. It worked fine. The old software just worked absolutely perfect, rigorously tested, no problems at all. So, we're still not sure 100% what actually, the exact mechanism which caused it, um, because we didn't want to

**Dave Jones:** go into the SPI multiplexing code for the, for the, stack and all that sort of thing. It, you know, it it just wasn't worth the time. But, obviously, the, the protocol, um, stack for that SPI thing it was

**Dave Jones:** calling up, uh, relied on, was wasn't entirely robust enough to, um, to, uh, account for various timings in the FPGA. And, FPGAs also do, um, can, you know, do weird things with their port pins and things like that. They can read back all

**Dave Jones:** sorts of different things depending on, you know, a whole slew of different circumstances. So, it was clear that there was something wrong in that, um, driver, um, that protocol stack, uh, SPI driver, which was which was causing an

**Dave Jones:** issue. It wasn't tolerant enough of the hardware. But, hardware is fixed, isn't it? No, it's not. It's manufactured in in different batches of silicon. It's manufactured in different plants. It's You know, there's all It's got silicon revisions and silicon bugs, as I've

**Dave Jones:** talked about, and FPGAs are no different. In fact, they're orders of magnitude more complex than you know, a micro or some other you know, fixed silicon chip. They're incredibly complex. So, hardware can't be relied upon to have fixed static

**Dave Jones:** requirements. They're a bit warm and fuzzy. They're a bit analog, too. And well, software has to be robust enough to take that into account. And if your software is not robust enough, you're going to see problems like this.

**Dave Jones:** You can get problems like this between not only silicon revisions, but different batches of silicon. And here's a photo of the two Altera FPGAs side by side. And one of them was was the bad batch one, and one

**Dave Jones:** was the good batch one. And and sure enough, most of the numbers are the same. But if you look at the two lines down the bottom, they're actually slightly different. So, and they aren't serial numbers, either. They're some

**Dave Jones:** sort of weird batch number or weird process number or something like that. And I can't find that information in the Altera data sheet. It's really annoying. So, I can't actually know what those numbers actually mean. I just know they're

**Dave Jones:** different. Our previous batches of boards all had a different number, and they were all the same. And this new batch has a new number, and they're all the same. And that was the difference. But you know, it's it's not a silicon

**Dave Jones:** revision. I don't think it's a mask difference. I think it's just a process difference between batches. And it's really subtle. And the software just happened to be so on the edge that it was probably requiring some sort of

**Dave Jones:** um the state of some pin to be high or you know to float high or to do within a certain amount of time, otherwise it dropped out of its routine and shut down the SPI bus and something like that.

**Dave Jones:** So what does this story show? Well, it shows that uh silicon is not fixed and programmers have to know about hardware and uh write tolerant software to handle all aspects, you know, all the timing margins and the temperature

**Dave Jones:** uh variations and all sorts of things in the FPGA. And that's why when it comes to this sort of stuff, hardware guys make the best programmers. And things like this always remind me why my favorite programming language is

**Dave Jones:** solder.
