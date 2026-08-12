---
video_id: hpZFiR8kM2g
title: EEVblog #58 - Warm and Fuzzy FPGA Troubleshooting
url: https://www.youtube.com/watch?v=hpZFiR8kM2g
source: youtube-asr
timestamps: {"0": 0, "1": 33, "2": 72, "3": 91, "4": 123, "5": 140, "6": 158, "7": 174, "8": 197, "9": 217, "10": 246, "11": 268, "12": 281, "13": 301, "14": 320, "15": 350, "16": 384, "17": 402, "18": 426, "19": 451, "20": 479, "21": 511, "22": 544, "23": 575, "24": 600, "25": 624, "26": 663, "27": 695, "28": 735, "29": 777, "30": 805, "31": 844, "32": 878, "33": 909, "34": 939, "35": 969}
---

**Dave Jones:** Hi, welcome to the EEVblog and electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's industry story time again. I was working on something at work the other day and it was a real interesting problem that I thought would make an interesting blog. So, here we go. Okay, let me set the scene for you. We've got this product which we're putting into production and we've done some product we've done a couple of prototype runs before and a pre-production run and

**Dave Jones:** everything works just fine. And we've got this whole suite of automated tests which test every aspect of the product. And there's a whole bunch of them to be tested, you know, 50 different things to be tested. And um So, we put this new run a we put a new run through a pre-production thing and all the boards failed this one particular test and it was an audio codec. There's a 24-bit delta-sigma audio codec on there and a power amplifier for, you know, for actually recording and and actually

**Dave Jones:** playing back music, you know, MP3s or wave files or anything else. And that was failing. We're getting no audio out at all. So, I started to investigate the problem and this is what happened. So, I went through the basic troubleshooting procedures in a situation like this.

**Dave Jones:** Basically, the first thing you think of when a board has worked perfectly before and there've been no changes and all of a sudden you get a new batch back from the assembly factory and it's failed something or you go, "Okay, there's something wrong with the assembly." That's the, you know, that's the typical that's the typical scenario. So, I checked I visually checked every component in in the sections at fault, these audio sections, and various other sections as well. Couldn't find any visual faults. You know, they hadn't

**Dave Jones:** loaded um you know, there weren't any missing components from the board. And um you know, so I couldn't find anything. So, next step was to get my meter and go in and measure every part in in the um sections at fault.

**Dave Jones:** And uh I couldn't I I measured them all, compared them against a previous batch board, and I couldn't find any problems. They're all measuring okay. So, they hadn't loaded in the incorrect components. Bugger. I've got to, you know, go deeper into this and troubleshoot it further.

**Dave Jones:** So, let me take you through a basic block diagram of uh of the section at fault here. What we've got is a huge um Altera Cyclone III FPGA. It's a big BGA package, you know, 700 odd pin BGA.

**Dave Jones:** And it's running a 32-bit um soft core actual processor, and it's got an I2S um audio bus, and it's got a SPI control bus. And these two buses go to a um a Cirrus Logic CS4270 24-bit delta-sigma converter.

**Dave Jones:** And the codec goes into a little uh power amplifier, which drives some speakers and a headphone jack. Um and it's also got a uh an another audio jack, which you can plug into actually test the power amp. And the codec also has its own little uh local uh voltage regulator.

**Dave Jones:** Um and it's also got a little uh power-on-reset chip as well, and a couple of uh boot mode pins, which determine which mode the chip boots up in, cuz it's a fairly complex uh chip, and it's got various modes. And if you don't put it in the right mode, it doesn't work. In fact, I've done a blog on this um exact same chip way back, and I'll put the link up, and how that if you don't put it into the right mode, you get um these input lines can be inputs or

**Dave Jones:** outputs. And in and in the old blog, I um was fault finding a thing where it was outputting where it should have been inputting. Anyway, go check that one out as a bit of a background. So, the next thing I did, well, I can't we're getting no audio out at all. Is it the codec? Is it uh is it the uh something wrong with the FPGA? Is it something wrong with the power amp?

**Dave Jones:** Well, thankfully, the power amp's really easy to test because it's got a test jack. So, I just fed some audio in, and sure enough, it comes out perfectly. So, you know, you can scrap the audio amp. There's nothing wrong with that at all.

**Dave Jones:** So, next thing I look into is the codec. Now, I started the one of the golden rules of troubleshooting, thou shall measure voltages. And because, you know, a lot of the time, it's simply a going to be a power supply problem. So, I check the power supply. No problems there at all. So, rule that one out.

**Dave Jones:** Next, I think, "Aha, maybe the chip just isn't doing anything because um it's been the reset part of it's not working." So, I check that out, and no, sure enough, um the pin was high, and it's an active low reset, so there was nothing wrong with there. It should be working.

**Dave Jones:** Now, the next thing I checked is these boot mode um pins also because, you know, if it doesn't boot up in the correct mode, well, it's, you know, it's pretty much screwed. So, but I checked those, and they were okay, too. So, that left the communication that basically left the I2S and the SPI buses. Now, the first thing I did was probe the I2S bus, see if there's any um audio going in and out. You can look up what an I2S bus actually does. I won't explain it now,

**Dave Jones:** but it's basically a serial It's a standard serial audio interface. And I checked it and there was no data on there at all. There was nothing, which pretty much told me that either the software in here is doing nothing or this chip, as I knew from the previous encounter I had in the other blog, that if this chip obviously wasn't booting up in the correct mode because um when the when the whole system powers up, this the soft processor has to send a command via the SPI bus to switch this chip into

**Dave Jones:** um into the required mode. And that obviously wasn't happening. So, the next thing I do is go aha, it's got to be the SPI bus. So, I probe the SPI bus. And what do you know? There's no activity on there at all. Uh you know, there was just there was nothing.

**Dave Jones:** It was like it was dead. Um but I knew that the soft processor was working, the FPGA was fine because it run this um FPGA controls dozens and dozens of other things as well. And all of those passed their automated tests. And for each one of those tests, they have to download firmware in here. So, I knew, you know, every aspect of the FPGA was working.

**Dave Jones:** So, it was unlikely, I thought, to be a problem with just the pins on the BGA cuz BGAs are notorious for, you know, having having bad solder joints under them. So, I thought, it's you know, it's a bit too much of a coincidence that well, it's in fact it's impossible that every board in the batch could be faulty just on those pins. It's just not possible. So, I ruled that out.

**Dave Jones:** So, I thought, what's going on here? I was scratching my head for ages. And the other thing, there was there's a also a reset switch on here as well, which resets the soft processor. And I was playing around with that, and uh I could actually get stuff to happen on the SPI bus. When I was playing around with this reset, you do it enough times and and it it didn't work. It didn't make the chip work, but it made it do something, and I got something on the

**Dave Jones:** SPI bus and then something on the I2S bus. But it was just it was just garbage, really. Um but that that sort of indicated something, but I wasn't quite sure what. And it's about at this point where your mind starts going whacko, and it switches into super detail mode, and you start trying to think up all these weird and wonderful ways in which the uh FPGA can um somehow boot up and get into some mode that'll cause a problem with just that application and not the 20 other

**Dave Jones:** applications and things like that. You just start going bonkers. Now, being a hardware guy, I naturally blamed the software because well, you know, software's a pain in the ass, it really is. And so I thought, "Aha, have I got the wrong uh bit file which I'm downloading to this?" And I double-checked, triple-checked, and I did all sorts of things, and uh no, I'm downloading the correct bit file like we always have. I could test I could download the same bit file into a good board from the old batch and this

**Dave Jones:** new board, and the new board just wasn't working with the exact same bit file, exact same soft processor, same code, same everything. It was bizarre. So just as a sanity check, I was getting pretty desperate. So I I what I did is I wrote I wrote a brand new project for the FPGA that outputted data on all the pins so that I could check that there was actually, you know, continuity between the FPGA and the thing. And it was fine, there was no problem at all. This thing

**Dave Jones:** just got stranger and stranger. So, really, I'd started to exhaust all of the hardware avenues. I just I just knew it wasn't a, you know, a component loading problem or or something else. It just wasn't really a hardware issue. It must be a software issue, regardless of how weird that sounds. The software works on one board, but doesn't work on another.

**Dave Jones:** Aha, right? We're dealing with FPGAs here. The FPGAs are notorious for having all sorts of, um, timing issues. Every time you, uh, recompile or synthesize a a a program to go in a, um, you know, a thing to go inside the FPGA, all the timing is is different.

**Dave Jones:** Everything changes every time you make a small change to the, um, you know, to the how it actually works. And it's they're incredibly complex. So, I naturally thought, aha, do we have some sort of, um, weird marginal timing issue? So, I went to the software, um, guy who who wrote the software, and sure enough, right? Well, he was scratching his head too for a while, but it suddenly dawned on us that, um, that, uh, he had actually seen this problem or a similar problem with SPI bus

**Dave Jones:** initialization before. Because the FPGA, right? The, um, soft processor has a a very complex, uh, protocol, um, stack and it has an SPI, uh, protocol interface and it has it goes off to another FPGA up here, and, um, and and it's got an SPI, uh, SPI multiplexer in it, and it talks back and forth and does all sorts of weird, um, weird and wonderful things.

**Dave Jones:** And, uh, as it turns out, there was a compiler switch in the, uh, in the C compiler software, which which said, "Use this SPI, um, multiplexer." But, we were actually talking direct from here to here. We weren't using this SPI multiplexer, but it was enabled. And, sure enough, we disabled it, we recompiled it, we downloaded it, and it works. It was a software issue. Okay, so what's so remarkable about a software issue? Well, if you remember, it works perfectly on different batches of boards. It worked

**Dave Jones:** fine. The old software just worked absolutely perfect, rigorously tested, no problems at all. So, we're still not sure 100% what actually, the exact mechanism which caused it, um, because we didn't want to go into the SPI multiplexing code for the, for the, stack and all that sort of thing. It, you know, it it just wasn't worth the time. But, obviously, the, the protocol, um, stack for that SPI thing it was calling up, uh, relied on, was wasn't entirely robust enough to, um, to, uh, account for various timings in the FPGA. And,

**Dave Jones:** FPGAs also do, um, can, you know, do weird things with their port pins and things like that. They can read back all sorts of different things depending on, you know, a whole slew of different circumstances. So, it was clear that there was something wrong in that, um, driver, um, that protocol stack, uh, SPI driver, which was which was causing an issue. It wasn't tolerant enough of the hardware.

**Dave Jones:** But, hardware is fixed, isn't it? No, it's not. It's manufactured in in different batches of silicon. It's manufactured in different plants. It's You know, there's all It's got silicon revisions and silicon bugs, as I've talked about, and FPGAs are no different. In fact, they're orders of magnitude more complex than you know, a micro or some other you know, fixed silicon chip. They're incredibly complex. So, hardware can't be relied upon to have fixed static requirements. They're a bit warm and fuzzy. They're a bit analog, too. And

**Dave Jones:** well, software has to be robust enough to take that into account. And if your software is not robust enough, you're going to see problems like this. You can get problems like this between not only silicon revisions, but different batches of silicon. And here's a photo of the two Altera FPGAs side by side. And one of them was was the bad batch one, and one was the good batch one. And and sure enough, most of the numbers are the same. But if you look at the two lines

**Dave Jones:** down the bottom, they're actually slightly different. So, and they aren't serial numbers, either. They're some sort of weird batch number or weird process number or something like that. And I can't find that information in the Altera data sheet. It's really annoying. So, I can't actually know what those numbers actually mean. I just know they're different. Our previous batches of boards all had a different number, and they were all the same. And this new batch has a new number, and they're all the same. And that was the difference.

**Dave Jones:** But you know, it's it's not a silicon revision. I don't think it's a mask difference. I think it's just a process difference between batches. And it's really subtle. And the software just happened to be so on the edge that it was probably requiring some sort of um the state of some pin to be high or you know to float high or to do within a certain amount of time, otherwise it dropped out of its routine and shut down the SPI bus and something like that.

**Dave Jones:** So what does this story show? Well, it shows that uh silicon is not fixed and programmers have to know about hardware and uh write tolerant software to handle all aspects, you know, all the timing margins and the temperature uh variations and all sorts of things in the FPGA. And that's why when it comes to this sort of stuff, hardware guys make the best programmers.

**Dave Jones:** And things like this always remind me why my favorite programming language is solder.
