---
video_id: SBkW_pzhUSs
title: EEVblog #1308 - 1970's Intel MCS-85 8085 Design Kit!
url: https://www.youtube.com/watch?v=SBkW_pzhUSs
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 40, "3": 60, "4": 70, "5": 84, "6": 99, "7": 108, "8": 122, "9": 131, "10": 149, "11": 166, "12": 183, "13": 203, "14": 213, "15": 224, "16": 239, "17": 250, "18": 264, "19": 280, "20": 297, "21": 314, "22": 324, "23": 340, "24": 351, "25": 371, "26": 380, "27": 396, "28": 417, "29": 432, "30": 443, "31": 453, "32": 475, "33": 485, "34": 501, "35": 511, "36": 527, "37": 540, "38": 553, "39": 565, "40": 579, "41": 590, "42": 608, "43": 623, "44": 638, "45": 652, "46": 671, "47": 681, "48": 705, "49": 717, "50": 734, "51": 750, "52": 768, "53": 780, "54": 806, "55": 821, "56": 833, "57": 849, "58": 863, "59": 876, "60": 891, "61": 901, "62": 924, "63": 936, "64": 948, "65": 969, "66": 985, "67": 1000, "68": 1016, "69": 1028, "70": 1041, "71": 1062, "72": 1073, "73": 1088, "74": 1106, "75": 1118, "76": 1129, "77": 1140, "78": 1147, "79": 1158, "80": 1168, "81": 1183, "82": 1195, "83": 1211, "84": 1225, "85": 1238, "86": 1250, "87": 1262, "88": 1281, "89": 1294, "90": 1302, "91": 1316, "92": 1327, "93": 1339, "94": 1350, "95": 1363, "96": 1393, "97": 1412, "98": 1424, "99": 1440, "100": 1451, "101": 1463, "102": 1484, "103": 1505, "104": 1522, "105": 1536, "106": 1557, "107": 1569, "108": 1581, "109": 1601, "110": 1610, "111": 1621, "112": 1642, "113": 1651, "114": 1670, "115": 1684, "116": 1694, "117": 1704, "118": 1723, "119": 1737, "120": 1755, "121": 1762}
---

**Dave Jones:** Hi, I'm super excited about this one. Check this out. You might have seen this before in the background on my mailbag video. Shelf Intel delivers. Ta-da! What is it?

**Dave Jones:** It is the Intel MCS85 system design kit. It dates from 1976. Yes, that's only four years after man last set foot on the moon. Unbelievable. Now, this is what you got if you wanted to play around with a processor back in the 1970s cuz it was a lot of work just to blink a LED back then.

**Dave Jones:** Not as easy as it was these days, let alone do anything more complicated. So, a development kit or system design kit, as they called it, was a relatively simple way just to get up and running with in this case Intel's latest microprocessors cuz otherwise it would have been like a real chore.

**Dave Jones:** This allows you to play around with the processor and write programs for it and test them out and actually connect up to hardware and things like that, as we'll see.

**Dave Jones:** So, a very nice bit of kit. And yes, it is actually a kit. It's Look, we've got all the chips. I love the block diagram, the system bus. It's just beautiful and all the miscellaneous through hole, not that surface mount rubbish parts.

**Dave Jones:** We even get the IC sockets. Wow. So, these sorts of kits were pretty much the only game in town back then. And because Intel wanted to encourage people to buy their chips cuz that's what that was their business.

**Dave Jones:** They They sold chips and that was basically it. They didn't really want to make money from these development kits, so they sold these relatively cheaply. I'm not sure of these.

**Dave Jones:** Couldn't find the exact cost of this one. So, if anyone knows the cost back in the day, then please leave it in the the down below. So, there it is, the MCS 85 system design kit Intel 1976.

**Dave Jones:** So, what do you get in the kit? Well, you're going to get the bare minimum to get a processor up and running. You're going to get the processor itself, the 8085 A for those playing along at home, copyright Intel 76, fantastic.

**Dave Jones:** And of course, you need a monitor ROM {slash} BIOS, however you want to think about it. We'll talk about these in a minute, and you need some RAM. So, you need a RAM, ROM, and of course, you need a keyboard and display to interface with the thing.

**Dave Jones:** So, this is both a combined keyboard and display controller, the 8279. And you just get a couple of small interface chips, a 74LS156 decoder, and an address decoder up there, and the seven-segment displays.

**Dave Jones:** We've got six of them here, and the keys as well. There's the individual key switches, and a bunch of passive parts, and the sockets because, well, you know, you don't want to solder them into the board cuz, you know, these processors might have been relatively expensive back then, and the ROM and the RAM, and, you know, so who actually bought these kits?

**Dave Jones:** Well, you might think, oh, people who are developing computers, but that's actually not really the case. The vast majority of customers for these kits would have been looking at using a processor to add intelligence, in quote marks, to their new consumer product or their industrial control product or something like that.

**Dave Jones:** So, they needed a processor to do that, so they would have bought this design kit to get them up and running, and hence why it's going to have a large prototyping area, as we'll see when we take this puppy apart.

**Dave Jones:** Now, because this thing is mint in box, I'd probably get death threats, not that I don't anyway, you know, YouTuber, but like if I tried to assemble this thing, yeah, the hate comments would flow.

**Dave Jones:** So, ta-da, here's one I've assembled earlier. Well, I didn't assemble it. I managed to procure another one which was already assembled. Ah, isn't it a thing of beauty? Joy forever.

**Dave Jones:** Now, I think this one is a later model because look, it's different up the top here. System this system design kit is different and it's just got Intel up here.

**Dave Jones:** It doesn't have copyright 1976 anymore and some of the date codes on some of the chips, although these could have been added later. We're talking about 1982. It's got the genuine Intel sticker on the ROM there.

**Dave Jones:** This one does actually have a few additions that you didn't get in the standard kit. Only had the processor, the ROM, one RAM chip and the keyboard and display interface driver kit chip.

**Dave Jones:** This one has got an additional RAM chip for a whopping 512 bytes total. That's bytes, none of that K rubbish. 2K of ROM which came standard in the kit and all this extra stuff up here has been added.

**Dave Jones:** This was this is a bus expansion driver section of the board and you can see that whoever built this is obviously populated that but looks like they didn't do an awful lot with it because they just develop programs because look at this large prototyping area.

**Dave Jones:** They didn't interface with this at all. They've got some connector ports here which you could have gone off to your own products or you could use this large interfacing area.

**Dave Jones:** They've got power strips down the middle like this and that's very nice to be able to prototype your industrial widget in mid to late 1970s. This would have been absolutely fantastic and you could probably afford to use this section because I don't believe the development board was very expensive.

**Dave Jones:** So yeah, if you needed another one or whatever, you just buy another one and you build up more circuitry, various uh, revisions of your hardware until you perfected it, then you design and layout your own PCB, and Bob's your uncle.

**Dave Jones:** You You got your 8085-based product. Uh, look at the keypad down here. Speaking of which, who designed this? This is just absolutely ridiculous. Of course, uh, got the, uh, hexadecimal, of course, A B A through to F here.

**Dave Jones:** You've got six keys across here. Why not have A B C D E F? That would have made more sense than have 0 1 2 3 4 5 6 7 8 9 up here.

**Dave Jones:** That's not the usual arrangement. Like, that is just why? Why would anyone do that? I don't know. Anyway, this one's had a little bit of an oopsy. It did come with this switch, but it, uh, broke off, and there's a trace, um, just flapping around in the breeze there.

**Dave Jones:** So, hopefully, um, it still works, but I can fix that relatively easy. Anyway, this is to select between either, uh, keyboard mode, either, uh, keypad keyboard mode, or, uh, TTY, which is a, uh, teletype interface, and there it is, the, uh, TTY teletype interface, which goes off, uh, to a D connector up here, and you could whack in a D connector.

**Dave Jones:** I don't think it No, it doesn't come with one, but you could whack one in optionally, and that would go off at a whopping 110 baud, 110 baud, not this 300 baud rubbish, and, uh, yeah, you could hook that up to a, uh, serial terminal.

**Dave Jones:** They were very common back in the '70s if you wanted to actually, uh, like, view information on the on a screen instead of the limited, uh, six-digit seven-segment display here.

**Dave Jones:** So, the TTY interface is basically just a serial port that you're familiar with, uh, these days. The 110 baud limit on this would have been, uh, due to the 8085 on this.

**Dave Jones:** It wasn't the limit of the terminals at the time. The DEC VT50 and 52 that came out in 1974. So, 2 years before the uh, 8080 processor here. So, that could go up to 9600 board, and then the VT100, classic VT100 terminal came out, which supported the ANSI standard, which then took off.

**Dave Jones:** That came out in 1978, so 2 years after this. But, yeah, they did have a terminals back then. You'd have keyboard and display. Wow, 80 characters by 24 lines.

**Dave Jones:** Incredible. Oh, I totally forgot to show you the documentation that came with this assembled board. Intel Puerto Rico. What about all my Puerto Rican viewers? Fantastic. I wonder if their Telex still works.

**Dave Jones:** Dear SDK-85 customer, Intel is pleased to provide you with the enclosed 8085 system design kit. We appreciate the opportunity to provide the equipment aid to aid in your understanding and evaluation of the 8085 microcomputer.

**Dave Jones:** As a supplier of high-technology equipment, Intel is committed to providing design aids that will simplify your evaluation process and shorten your development cycle. Before proceeding further, please take a look at the following checklist.

**Dave Jones:** The design kit user's guide has very complete step-by-step instructions. Follow them closely. Review the assembly language reference before attempting to write programs. Special note, please be advised that the Intel service hotline numbers on the top of page in the system design kit are incorrect.

**Dave Jones:** The correct numbers are There you go. Anyone want to call those numbers and see who answers? The 8085 is a very powerful yet easy to use microprocessor, allowing you to pursue cost-effective microcomputing.

**Dave Jones:** Intel is committed to making your 8085 experience both pleasurable and profitable. Ah, back when they used to provide schematics. Those were the days. Absolutely fantastic. Look at that. Ah, it's double-sided.

**Dave Jones:** Ah. You can view that in glorious 4K. Who's responsible? And I wonder if they still work there. Hmm. And an overlay diagram. Bobby Doesler. So, before we power up this bad boy and see if it still works after almost 40 years.

**Dave Jones:** We'll get to that. Stick around. We have to talk about the 8080 itself and the history, or at least I want to because I'm a bit of a computer history buff.

**Dave Jones:** So, this bad boy here, the 8085, released in March 1976 and only discontinued in 2000. So, absolutely remarkable to get like 24 years out of a like a single micro that you can continue to buy.

**Dave Jones:** Absolutely incredible. Do modern ones like do they have production times of 24 years? Unbelievable. Leave it in the comments. Anyway, it's an 8-bit processor, hence the name 8085, but we'll get into the history of why it's named that.

**Dave Jones:** It's clock speed three up to a blistering 6 MHz and that was really quick for the day. Uses 16-bit address bus. Has 60 500 transistors in it on a three micron process.

**Dave Jones:** So, like 6500 transistors these days is like it it's nothing. That's head of a pin stuff. But hey, back then, you know, like doubling the number of transistors on the silicon, Moore's law and all that sort of stuff.

**Dave Jones:** It was yeah, it was ramping up. Anyway, let's go back to the almost the beginning of 1970 when Intel of course released the classic 4004 for use in calculators and primarily for calculators back then, but also used in industrial applications too.

**Dave Jones:** And then in 1972, a year later, they released the 8008, which is an 8-bit version of that. And they also released the 4040, but nobody really cared about that in 1974.

**Dave Jones:** What we care about in 1974 is that they actually released the 8080 processor. And of course, the 8080 is the classic chip that was used in arguably one of the first consumer hobbyist personal computers available, which was the Altair 8800, but that didn't come around until January 1975.

**Dave Jones:** So, it was you know, the chip had been out for like a year before the Altair actually got around to using it and it was famously published in January and then Bill Gates saw it and well, you know, that started the Microsoft thing.

**Dave Jones:** But in 1974, Intel weren't the only show in town. You had the Motorola 6800 as well, which came out in the same year and that one actually used a it was really good cuz it used a single 5-V power supply.

**Dave Jones:** You got to remember the 8080 didn't actually use a 5-V supply. It required three rails, plus 5-V, minus 5-V, and plus 12-V. So, you know, that really was a pain in the ass and not hugely compatible with you know, all these 5-V TTL type stuff coming on the market.

**Dave Jones:** So, yeah, that's where the 6800 kind of had an edge at that stage. But also in 1974, if you didn't want to use a microprocessor like this, which required external ROM, external RAM, and you know, stuff, it was a multi-chip solution, hence the name processor.

**Dave Jones:** It was just a processor. If you wanted what's now known as a microcontroller, the first microcontroller came out in 1974 as well. I've done a video on this the old Merlin game used to use it.

**Dave Jones:** It was the Texas Instruments TMS 1000. The Merlin used the TMS 1100. But anyway, the TMS 1000, the world's first microcontroller came out in 1974 as well. So, if you wanted to develop a little smart sort of widget back then and you could fit in the tiny constraints of the microcontroller, then the TMS 1000 that a neat solution and it was only a couple of bucks a pop.

**Dave Jones:** And, you know, so that was quite nice. But, if you wanted any decent sort of uh processing capability, you had to go for a microprocessor like either the 6800 or the 8080 and have external memory and ROM and the whole works.

**Dave Jones:** But, generally back then, people weren't making small stuff. You know, as I said, they're still making big like industrial controllers and other sorts of stuff where, you know, you needed the extra processing power of this.

**Dave Jones:** So, that was pretty much the only game in town until 1975 when the classic 6502 came out, and that was a low-cost 5-V uh CPU. But, it really wasn't used in anything in 1975.

**Dave Jones:** It was out, but it wouldn't be a year later until 1976 when the Apple I started to use and other computers started to use the 6502, especially in 1977 with the PET and the Apple II and the Atari 2600 and all those sort of ones.

**Dave Jones:** 1977 is when sort of things started to take off. But, I'm getting ahead of myself. So, even though we had the 6502 in 1975, yeah, there were no like mainstream computers around using the thing.

**Dave Jones:** I'm not sure if you were around back in the day, were you using 6502 in any like industrial applications or uh something like that? Anyway, in 1975, Intel realized, "Yeah, we have to come up with, you know, this single 5-V thing seems to be a hit.

**Dave Jones:** Have to come out with a single 5-V uh controller." So, what do you call it? Well, the other one was the 8080. We'll call this the 8085. The five means 5 V only.

**Dave Jones:** And they finally released the 8085 in March 1976. But, also famously in March 1976, a another company called Zilog were working on the Z80. They started that in uh '75 as well, and they came out with uh the Z80 in the same month as the 8085 came out.

**Dave Jones:** And unfortunately for the poor old 8085, the Z80 was just a better solution for all sorts of various uh reasons. It was like multiple manufacturers could sell it and things like that.

**Dave Jones:** So, the Z80 really took off as the processor of uh choice for various personal computers from then on. The 8080, uh I don't know. Uh try and name computers that used the 8085.

**Dave Jones:** You have to sort of go to 1983 with the Tandy TRS-80 or Trash-80 Model 100, which used a uh CMOS version of the 8085, the 80C85. And Zilog didn't come out with a CMOS version of their processor Z80 processor until uh well after that.

**Dave Jones:** So, but you know, pretty much, I don't know. The Model 100's probably it for the eight famously for the 8080, but that was used well into uh the 1983, well through uh probably most of the 1980s still in the Model 100.

**Dave Jones:** But all the Motorola fanboys, "Dave, what about the 6809?" Um yeah, sorry. That didn't come out until 1978. So, you know, it's it was used in quite a few um PCs on the market and things like that.

**Dave Jones:** But yeah, Intel with their 8085 pretty much uh ruled sort of sort of like the embedded uh market. I I don't know why. Cuz they had better tools, people were familiar with it with the uh from the 4004, the 8008, the 4040, the 8080.

**Dave Jones:** They were just, you know, so they just took up uh the 8085. It was pretty much like the embedded uh processor of choice back then. So, hey, what's your favorite processor of the 1970s?

**Dave Jones:** Is it the 8080, the 8085, the Z80, 6502, 6809, 6800? Let us know in the comments down below. Flame away. Anyway, our old friend here, the 8080, that was uh superseded by the 8086.

**Dave Jones:** And then, of course, they did the lower-priced or uh easier-to-interface, lower-cost solution that was uh called the 8088, which was used in which had an external 8-bit uh architecture and could use all the 8-bit chips.

**Dave Jones:** Um hence, the uh name 8088. As opposed to 8086, which was a 16-bit architecture. Anyway, that was famously used in the original IBM PC, and well, the rest is history.

**Dave Jones:** But, as was common uh back in the day, the 8085 and all the other processors from Motorola and uh you know, Zilog and other they also came with uh like many different support chips to build entire systems.

**Dave Jones:** The 8080, here's a list of like I think there's about three dozen or so different uh companion chips that help you build up the you know, any sort of industrial or embedded uh or PC, you know, consumer device uh computer that you could possibly imagine.

**Dave Jones:** They had GPIB controllers and serial ports and all sorts of you know, really whiz-bang uh accessory chips for this thing to build up complete systems. All right, enough of the history lesson.

**Dave Jones:** Let's power this thing on and see if it still works all these years later. Now, the manual says a 1.3 amps uh nominal supply. That seems a bit high to me.

**Dave Jones:** Um so, anyway, I've set my current limit to 1.3. If you're powering up like old stuff like this and you you want to be cautious. Um I probably would have like set like 500 milliamps or something like that.

**Dave Jones:** And you're not really going to damage it if you set too low a current limit. It the voltage is just going to drop and it's just not going to work uh basically.

**Dave Jones:** So, um yeah, better safe than sorry. So, you definitely don't want to go over the rated limit and looks like the previous owner had these wires in here already.

**Dave Jones:** So, it looks like that's how they powered the thing up. Looks like there's one tantalum in there. So, apart from that, I think all the rest of them are ceramic.

**Dave Jones:** So, there's nothing really that should have gone wrong with this. So, unless there was some other fault, I I kind of expect this to work. Confidence is high. I repeat, confidence is high.

**Dave Jones:** Confidence is high. I repeat, confidence is high. And we don't need the minus 10 volt rail there. That's only for the teletype interface, which I'm not going to use.

**Dave Jones:** All right, I've definitely got the polarity around the right way. Let's power it on and Tada! 8085. Winner, winner, chicken dinner. Geez, that's not very bright. Um, but yeah, old-school displays.

**Dave Jones:** Genuine HPs for those playing along at home. And that's drawing just over an amp there. So, no worries. So, 5 W nominal, but as I said, this actually has some extra port expansion here and a whopping extra 256 bytes of RAM.

**Dave Jones:** Now, these chips, by the way, these RAM and ROM chips, these are very interesting. These aren't just RAM and ROM. They actually contain data latches as well in them.

**Dave Jones:** So, that's rather interesting. That was just part of the 8085 system. So, yeah, you couldn't you couldn't just I don't believe you can just replace this like with any old ROM.

**Dave Jones:** You've got to actually use the genuine Intel ROM or compatible if there were any. I don't know. Now, speaking of the ROM, what we've got this is called a monitor ROM and it's kind of sort of different to a BIOS.

**Dave Jones:** A BIOS does more stuff like BIOS on a modern computer, a monitor ROM is just designed to have a simplistic keyboard and display interface so that you can just interact and monitor all of the addresses, hence why it was called monitor ROM.

**Dave Jones:** So, you can it's basically like just a like a peek and pokey type thing for you peek and poke fanboys. But anyway, reset, it displays 8085. I assume the dash is correct there.

**Dave Jones:** And it's got a dedicated vector interrupt button. That's nice. We'll actually use that in a minute. Oh, the board's a bit how you doing. Let me prop it up.

**Dave Jones:** I assume this is 100% working. So, we should just be able to jump into a memory address and actually enter code that way. So, sub ST is substitute memory or type in the memory address.

**Dave Jones:** Now, 2000 is the memory address. Here's the memory map over here. 2000 is where the RAM actually started. So, we go 2000 and we go next and F7 is the current data in there.

**Dave Jones:** But we can overwrite that with, you know, AA, something like that. And we can just go next and it'll increment to the next memory address and that's what's there.

**Dave Jones:** And we're basically just overriding what's in memory there. And if we want to execute the program we just ended at the address 2000, we just go go 2000 like that and execute.

**Dave Jones:** And well, it's it does nothing cuz I've typed in random stuff. But let's actually program in a program. Let's see if we can get this sucker to count. All right, so let's reset.

**Dave Jones:** Substitute memory. 2000. Next. 31. 8 20 3D 08 30 50 28 3C 27 47 35 3D 60 50 51 55 61 63 66 60 Now here's where we want to jump to another address, 20D4.

**Dave Jones:** So, substitute memory and enter FB D5 is 76 and C9. And that is our program. Woohoo! Okay, so we'll just go back. Hit reset here. That won't erase our program.

**Dave Jones:** It doesn't actually reset the memory. It just uh resets the uh processor. Um yes, this is RAM, so it's volatile. So, if you remove the power, you will lose your program.

**Dave Jones:** Uh well, none of that uh flash or even E-squared prom rubbish back then. So, yeah, we can reset that. And uh to run the program, we want to go go 2000 and fingers crossed execute.

**Dave Jones:** Tada! Counting. And we should be able to uh vector interrupt that to stop it. Yes. Vector interrupt was supposed to stop it. Um it was supposed to be able to resume.

**Dave Jones:** Hmm. Now we can actually change the speed of this thing uh with the by changing the value in address 2010. So, we go substitute memory 2010 like that and next and it's currently got 18.

**Dave Jones:** I'm not sure if it's faster or slower. So, let's just go 10, shall we? So, next go 2000 execute. There you go. Is that faster? Yep. And if we put the value of one in there, it should be really quick.

**Dave Jones:** Go 2000 execute. Ah, blinding speed. We can mine some Bitcoin on this sucker. So, what speed is this bad boy running at? Well, it's got a 6.14 mega clock, which is actually divided by two internally, which gives an actual clock speed of 3.072 megahertz.

**Dave Jones:** But, the processor can't do single cycle in well, instruction cycles vary anywhere from like one to five clocks, I believe. So, depending on what it's actually doing. So, yeah, not single cycle instruction stuff.

**Dave Jones:** So, you're not going to get 3.072 million instructions per second or mips. It's not going to happen. But, you know, it's pretty good for the day. It's 1976. And if we probe the clock pin, pin 37, ta-da!

**Dave Jones:** There it is. 3.072 megahertz. So, the neat thing about the 8085 is that it did have a clock out pin that then you could use. So, you could like it had an internal oscillator for starters, and then it divided that by two, and then you could use that clock pin to drive other synchronous external stuff in your system.

**Dave Jones:** Neat. Well, it was neat for 1976. So, there you have it. That's the Intel MCS 85 system design kit from 1976. I hope you found that as interesting as I did.

**Dave Jones:** And of course, it's still works. You know, there was never any doubt, really. I mean, these chips are just so robust, like multi-micron process technology. They're just not these newfangled things.

**Dave Jones:** But anyway, you take for granted like just buying a microcontroller kit these days for like a couple of bucks delivered, and all software's free and everything else, and there's tons of tutorials, and it's all flash program memory, and you know, nothing like this old school microprocessor where you had to store it in volatile RAM.

**Dave Jones:** I guess there you could actually have a battery back You could hack in a battery backup to this if you were desperate, I guess, to keep your program in there.

**Dave Jones:** But every time you wanted to test out your program, you had to enter it and if some, you know, manager came along and accidentally bumped the power or something like that, you could lose days work just programming this thing.

**Dave Jones:** So, there might have been like external storage solutions, I'm not sure, but anyway, yeah, you just enter it in on the keypad. It's actually pretty quick once you've actually got your list in to actually, you know, enter it in just bam bam bam bam, you know, automatically increments to the next address and, you know, you just type in the numbers and and that's it.

**Dave Jones:** But, if you make a single mistake, you come a cropper and your program doesn't work or it's, you know, buggy. So, you just have to go through and check each address.

**Dave Jones:** And of course, it comes with a full human debugger. You can go in there and single step and check individual memory addresses and stuff like that. And well, that's what you have to do, but anyway, yeah, to develop programs for this, you would use the Intel Intellec system pretty much.

**Dave Jones:** There might have been other systems available at the time to actually, you know, assemble your program and things like that, but yeah, this is how it was done. And then you program a mask ROM that we've got here.

**Dave Jones:** When was the first EPROM? Anyway, it certainly weren't electrically erasable. You know, get your UV light out, thank you very much. Leave it in the comments if you actually had one of these and you played around with.

**Dave Jones:** This is unfortunately before my time, but I can still certainly appreciate this. It's awesome and I mean, just imagine this back in the day. This would have been like absolutely phenomenal.

**Dave Jones:** And please, if you know how much this thing cost, I believe it was actually pretty cheap. So, like cuz Intel just wanted to get you into doing this. And I believe like just regular Joe Average could just buy this from Intel and you could develop your processes back then.

**Dave Jones:** So, yeah, fantastic. So, also leave it in the comments if you know what the equivalent systems were for like the 6502 and the 68 hundred, the 6809, and things like that, the Z80.

**Dave Jones:** Did they have like equivalent things? I mean, the Intel was pretty much became the de facto standard for like embedded products and things like that because maybe because of their support and their Intellect design programming system and things like that, perhaps.

**Dave Jones:** So, anyway, hope you enjoyed that. If you did, please give it a big thumbs up and as always discuss down below in over in the comments and check out my library channel.

**Dave Jones:** I'm like 24,000 subscribers over in the library channel. Still going gangbusters. Fantastic. Catch you next time.
