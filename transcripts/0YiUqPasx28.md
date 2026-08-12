---
video_id: 0YiUqPasx28
title: EEVblog #385 - Amstrad NC100 Notepad Repair
url: https://www.youtube.com/watch?v=0YiUqPasx28
source: youtube-asr
timestamps: {"0": 2, "1": 20, "2": 38, "3": 54, "4": 68, "5": 78, "6": 93, "7": 109, "8": 123, "9": 137, "10": 154, "11": 172, "12": 189, "13": 207, "14": 221, "15": 235, "16": 251, "17": 263, "18": 279, "19": 294, "20": 310, "21": 327, "22": 345, "23": 357, "24": 378, "25": 398, "26": 418, "27": 431, "28": 446, "29": 465, "30": 485, "31": 501, "32": 518, "33": 532, "34": 551, "35": 565, "36": 581, "37": 601, "38": 620, "39": 633, "40": 646, "41": 664, "42": 685, "43": 700, "44": 714, "45": 730, "46": 750, "47": 768, "48": 791, "49": 808, "50": 821, "51": 837, "52": 855, "53": 869, "54": 885, "55": 900, "56": 922, "57": 934, "58": 946, "59": 960, "60": 972, "61": 991, "62": 1013, "63": 1026, "64": 1050, "65": 1073, "66": 1087, "67": 1101, "68": 1121, "69": 1139, "70": 1152, "71": 1168, "72": 1180, "73": 1195, "74": 1210, "75": 1221, "76": 1240, "77": 1258, "78": 1277, "79": 1289}
---

**Dave Jones:** Hi, hot on the heels of the previous video where I tore down the Cambridge Z88 computer, we've got another one of a similar ilk, the Amstrad Notepad NC100 and it uses the same BBC Basic we saw in the Cambridge Z88. Apparently and it's a

**Dave Jones:** little bit younger, I guess. It's 90s early 90s vintage, there we go, 1992 vintage there, made in Japan instead of made in Scotland and it's, you know, similar little battery powered A4 notebook. Looks like it has a battery

**Dave Jones:** backup in there, of course, and little couple little flip out feet. This one's actually missing the battery door here, so a bummer, but still it's going to work. It's got a serial and a parallel port on it, DC jack, contrast

**Dave Jones:** and a memory card expansion slot and the good thing is it doesn't work. So, I thought we'd have a crack at fixing this one. First thing I'm going to do is check the current consumption of the battery to see if there's any standby

**Dave Jones:** current at all cuz it does seem to use a soft power switch. So, no, I can't see it. That's no, that's not 0.1, it's still the same if I lift the probes off there. So, I expect it to draw at least,

**Dave Jones:** you know, that's like in the order of 10 nanoamps. So, you know, you'd expect it to have some sort of standby power consumption, but it's got zip. Now, there's one totally fascinating aspect of this thing which I absolutely love.

**Dave Jones:** Look at this door down here. You flip that off and look what you've got. You've got what looks like the ROM chips. Let's whack it around here so we can see it. There it is, Amstrad UK A2. That looks like it's a masked ROM chip

**Dave Jones:** so that you can change the ROM just by lifting the panel and whacking in a new chip. I I think I've seen that on any machine before. Now, there was one of the screws missing on this thing, so maybe somebody's

**Dave Jones:** had a crack at this thing. Only one way to find out. Looks like we have some metalwork under here. Looks like there's a couple of catches along here I've got to snap off first. And here we go. I got it.

**Dave Jones:** I think I thought I did. Yep, there we go. Ta-da! Nakajima I guess that's a uh I don't know. Is that some sort of date code? Production date code? Look at the shielding on this thing. It's actually quite uh

**Dave Jones:** quite quite substantial. They shielded the entire keypad backing on that and the main board as well. Neat. It looks like this just lifts out here. The keyboard's connected. Looks like I can probably flip it over like this and

**Dave Jones:** lift that off. Ta-da! That's easier. We have board predominantly uh surface mount, almost all of it, and we've got the uh LCD up here which we didn't see last time on the Z 88. So, yeah, that's actually um fairly modern, but that's

**Dave Jones:** what you'd expect in the differences between the uh 1987 vintage uh Z 88 and this 1992 vintage NC 100. Now, let's have a look and see what we've got here. Yes, we do have a soft uh tactile power switch up here. So, maybe there's

**Dave Jones:** something wrong with the uh just the power on circuitry. It could be that simple or it could be more complex. I guess we'll find out. Got our DC input jack up here. There's the uh battery backup CR2032 backup battery. Got a

**Dave Jones:** couple of mod wires going around here. They've uh hacked in there. There's a little resistor there plus two mod wires, so they've done this after uh after production, obviously. They decided to make those changes. Uh couldn't be bothered to respin the

**Dave Jones:** board. Cheaper just to put a couple of mods on there. There's our Zilog Z80 CPU. Uh our main uh LSI uh ASIC up here, which would handle pretty much uh everything else the um ex- part from the CPU because we've

**Dave Jones:** basically got the big LSI, we've got the memory, there's the ROM socket on the back. There's another device there, not sure what that is offhand. And a couple of the miscellaneous uh chips over here and another one up

**Dave Jones:** there. But apart from that, that's it. I mean, this would be the serial chip up here cuz that goes off to the serial port. Um but this puppy would handle all of the system architecture for the Z80 uh for a Z80 uh CPU computer. And

**Dave Jones:** we've got our date code, 20th week '92. So, it was uh manufactured would have been manufactured fairly shortly after that. And all the date codes are for the various chips seem to uh match. So, been manufactured in the weeks or months

**Dave Jones:** after that. Um there's no crystal, it just uses a ceramic resonator there at uh 12.2 MHz. This is the real-time uh clock chip, of course. I You know, I don't know the number offhand, 8521, but there's the 32 Oh.

**Dave Jones:** Can't see that on the screen. There's the 32 kHz uh watch crystal right there. Nice little solder strap on that. I like it. Um pretty old-school stuff. A HC 00, which they didn't populate for some reason, not sure why. And it is all um

**Dave Jones:** you know, uh fairly modern surface-mount stuff. It's not ancient like we saw in the 1987 vintage Z88. And there's the main chipset, D65034 GD093. Uh man, I reckon you'd have a hard time finding data on that. I don't even think

**Dave Jones:** I'd bother Googling it. We'll just have a quick look at the display board here. We've obviously got some sort of you know, eight-bit parallel interface or something like that. And we've got OKI brand display controls, very common for

**Dave Jones:** the time and still nowadays as well. These are 5299C's. So, it's got a bunch of 5299C's all the way across there until we get to the end where it is an M5298I instead of a 5299C. And on the back of the board here, we've

**Dave Jones:** got a surprising amount of passive stuff around here. Tons of it. Check it out. They've got that plastic insulating sheet there so it doesn't short out to the shielding. There's an absolute buttload of resistors and SOT23's on here as well.

**Dave Jones:** Tons of them. There's our ROM. And uh there's a few more stuff up there near the parallel port as you'd expect. Couple near the serial and whole bunch more. Looks like series resistors on the expansion header there. Now, before we

**Dave Jones:** start to go feral on this thing with the scope, let's check out some basics. Here's our battery input here. It looks like it's got these two traces going directly all the way under there, all the way under there, nowhere else directly over to the

**Dave Jones:** DC power jack. So, it looks like it's just in parallel with the DC power jack there. Now, if we this soft button obviously has to do with something around here. Soft start power switch, but let's have a zoom

**Dave Jones:** up in here and there's something that immediately sticks out. F301 0.8 amps. Fuse. Haha, can it be that easy? Let's get the meter out and measure it. Let's have a go Here, the meter works as both a convenient

**Dave Jones:** uh prop for the item on video and Ah, man, it's blowing. Ah, so so much for the repair video, folks. Sorry. Thought it'd be more interesting than that. No, probably not. But, of course, the thing is, why did it

**Dave Jones:** blow? I don't know. Let's um measure the other side of it and ground, shall we? So, we'll get our ground here. Let's assume that this around here is ground. I'm pretty sure the big plane is always ground. So,

**Dave Jones:** if we measure this side of it, no. No, 0.25 meg. That's all fine and dandy. Don't mind that at all. And it looks like they uh specked into the design a common mode choke there, but they've just decided to uh short it out. There's

**Dave Jones:** the ground, so it would have gone from the DC input jack through to the ground like that, but it doesn't. And uh of course, the DC input jack through to those filter caps there, but it doesn't. And we'll just measure across

**Dave Jones:** that filter cap there to make sure it's not shorted, and no, it's not. 46k, and you'd expect it to rise as the uh capacitors charge up. So, that's all working hunky-dory. So, um I'm going to presume that the uh power rails. And I'm

**Dave Jones:** not sure if there's another voltage regulator on here. There certainly could be. Um that there looks like it could be a voltage regulator. So, maybe they have a 5-V regulator on this thing. Although, if you're powering it from uh 6-V

**Dave Jones:** batteries, the four uh double A's in series, that's um 6-V uh nominal. Um but, that's going to drop fairly drastically. So, a 5-V regulator, even a low dropout one, isn't going to regulate uh for very long over that

**Dave Jones:** full battery discharge curve. So, what I'll do is I'll just power this thing from a 6-V bench supply, and uh let's give it a go. So, 6 V, switch it on, and soft power switch. Is it drawing any current? Oh, yep.

**Dave Jones:** There we go. Yep, it's on. Ah. Man, too easy. Where is he? Yeah, there we go. Lithium battery is low. Please switch off and replace battery. Haha. We have a winner, folks. All it was was a fuse. That's actually very disappointing, cuz

**Dave Jones:** I was hoping that we'd hopefully we get something more exciting than that. But, no. Well, I didn't have a direct surface-mount replacement, so I just put a little axial one in there. No problem. It should fit nicely against that metal

**Dave Jones:** shield, I think. We've got insulator there. Not a problem. So, I'm going to put this sucker back together, and we'll power it up. And here we go. We can see the standby current consumption here, about 72 microamps or thereabouts. So,

**Dave Jones:** let's switch this sucker on. Bloody default AC, pain in the ass. So, let's see. About 60 milliamps. So, very similar to the draw of the Z88. Let's have a quick squeeze here at the main clock.

**Dave Jones:** And should be 12. There we go. 12.363 MHz. That's the That's, of course, not a crystal. That's a ceramic resonator. And let's have a look at the main oscillator as well, which is pin one of the 44-pin PLCC package, and it is continuously

**Dave Jones:** Why I say it? Yes, it is continuously running. Although this thing isn't at in at its application mode yet. It's just giving that display. There you go, it just switched off. So, but let's What was that running at? Let me switch it back on. There you

**Dave Jones:** go. It's running at 6.18 MHz. So, that's pretty quick for a Z80 processor. And because the back case is not on this thing, I need to still access and probe the circuitry. I can't put the coin cell in back, which is

**Dave Jones:** really annoying. So, I've hooked up another supply over here. So, let's power it on and we should get No. Lithium battery Ah, helps if I turn the load switch on. Let's give that a go again. There we go. Ta-da! We're up. We're in

**Dave Jones:** the main screen. Brilliant. Works a treat. And interestingly, the current draw is now jumping around a bit, but it's, you know, going anywhere from 40-odd milliamps up to 50. So, that possibly could indicate that the clock is skipping again to save cycles and

**Dave Jones:** save power. So, let's probe that again and see what we get. And bingo, there it is. Let's single shot capture that. See what we get. We've got a couple of bursts large bursts here of uh 2 milliseconds, 6 just over 6

**Dave Jones:** milliseconds each with a dead time of almost 4 milliseconds between them. And then we've got a shorter little burst here which that's about 200 microseconds per division. 200, 400, 600, you know, 700-odd microsecond burst there. There you go. So, it looks like it has a

**Dave Jones:** couple of these shorter bursts with a couple of longer bursts. And uh it's just waiting for the keypad. I'm assuming it's just waiting for a key. So, let's press a key. And yeah, we can see it insert. There Ah, there we go. It just

**Dave Jones:** not only did it insert a couple of more, I'm not sure what I'm actually running here. I have to flip my screen over. I'm not doing anything, actually. Um enter doesn't do anything at the main screen. So, let's go into the word

**Dave Jones:** processor. Press the yellow and red. So, there we go. It does seem to jump around a bit between uh actually between having none of those longer bursts. See? There it is. Very interesting. So, let me call up the

**Dave Jones:** word processor. There we go. Bam. You saw it uh just go full speed there, and we're now inside No, we're not inside the word processor. It's weird. So, you can see how this main uh system ASIC here is always running by that uh

**Dave Jones:** 12 MHz ceramic resonator, and you know, it's they inter- I guess it can shut down its internal uh parts as well when it's not doing anything to save power, but the oscillator's always running there, and it only supplies the clock

**Dave Jones:** through to the CPU uh when it needs to. So, this will handle the uh keyboard as well so that it's uh sitting there waiting for the key presses to uh turn the thing on, supply power, interrupt the CPU, boot it up, and uh start it

**Dave Jones:** running again, and action those keys. And that's how they save power on these types of systems. And this is the coolest key ever. Secret menu. Woah. Let's see what's in there. Let's press this sucker and see what we get. Here we

**Dave Jones:** go. Uh enter password. Woah, let's try I don't know, 0000. What the? Sagan was here? This is one heck of a big calculator display. Woo. Love it. No scientific functions, though. Bummer. Unfortunately, there seem to be a couple

**Dave Jones:** of stuck keys on this thing. The shift and this one up here seem to uh get stuck. I've tried to sort of clear them, but it doesn't seem to work. If anyone's got any good ideas for that, let me know. And it's really not obvious

**Dave Jones:** how to get into the BBC Basic either because looks like you can't scroll this main menu. It's only got the word processor, calculator, and diary, address book, which you use, you know, function, sort of, you know, word that'll take you into the word

**Dave Jones:** processor, start a new document, and this takes you into the calculator, and uh you know, um press stop takes you back to the main menu. Well, it's function B. Apparently, there it is. And there's RT Russell again. And we've got

**Dave Jones:** our little basic program there looping through printing I. Yes, it has to scroll the whole screen. I know I haven't put the semicolon at the end of it. Whatever. Let's run it. Well, it does seem to be substantially quicker

**Dave Jones:** than the uh Z88. No surprises. It's running exactly the same basic interpreter on the Z80, uh but it's running at like a double the clock rate. So, let's uh probe this clock again and see what we get. Stick it in here.

**Dave Jones:** And pin one on our clock. There you go. It is fully fully continuous. So, let's uh put this down here, and we are getting more than just over 5 V there. 1 2 3 4 5. There we go. And if I adjust the uh

**Dave Jones:** voltage on my supply, that doesn't go up. So, that's clearly being regulated. Now, here's our main clock, and it's just over uh 5 V there. And what I'm going to do is I'm going to drop my supply voltage here and see

**Dave Jones:** where that thing drops out. Ah, no, it looks like There you go. It's regulated. It's regulated, folks. It's not a It's not a 5-V linear regulator. So, it's working all the way down. Wow, there we go. It drops out at about

**Dave Jones:** 3.3 V. That's very impressive. And with everything tech, there's an enthusiast group for everything. I present to you the cpcwiki.eu, a surgical guide to the Amstrad NC. Here it is. They've got some cool-looking ASCII diagrams here, which show which tell you all the details.

**Dave Jones:** There it is, 6 MHz. Yeah, we measured that. 64 K internal memory, 15 K system, 11 K upper, 32 K lower. It's got a PCMCIA slot, which allows you to expand to 1 meg maximum. It's got a 480 by 32 pixel

**Dave Jones:** display, usually 8 by 80. There you go, 40 to 60 milliamps, which is what we what what we measured. And how to get the firmware number, memory cards, how to open it. Already done that. What's inside. They've labeled all the chips.

**Dave Jones:** There we go, there's the 6 MHz Z80. There's the UPD65034 custom chip. They call it customer chip. But, that's just a custom ASIC. And you know, a bunch of miscellaneous other stuff. They've got the UART and the RS232 driver and the real-time clock.

**Dave Jones:** And And interestingly, down here, this is what I like, a simplified block diagram. And as I mentioned before, IC302 here is the main ASIC, and it runs continuously on the 12.2 MHz ceramic resonator there, and everything hooks into it. I mean,

**Dave Jones:** here's IC301 up here. Here's the CPU, but it's hardly, you know, according to this block diagram, it's hardly doing anything at all. And And everything runs off that. So, you've got the the LCD controller is built in there. There we go, directly off it. The

**Dave Jones:** keyboard matrix, of course, so it knows um when you've actually pressed a key, so it can, you know, start up the clock and interrupt CPU and all that sort of jazz. And uh then we've got our uh real-time clock, PCMCIA is all hooked in

**Dave Jones:** there. All your memory address and all that stuff is all hooked into that system ASIC. So, the thing, man, wouldn't be able to do a damn thing without that ASIC. And let's scroll down here. We've got our power

**Dave Jones:** supply block diagram. We can probably zoom into that a bit more. Here it is. Um yeah, there it is. 6 V DC in, battery directly connected across it. There's the fuse that blew, little pain in the ass. And uh plus 6 V and looks like

**Dave Jones:** there's plus 5 V voltage regulator as well. 5 V BK there, which is the uh backup for the buffer RAM, so the SRAM. SRAM doesn't need to be refreshed. It, you know, it only takes microamps or nanoamps to uh to actually retain the

**Dave Jones:** information. So, as soon as you stop the clock and you've as long as you got uh power on those SRAMs, it will um retain the data in there for you. So, you got minus 15 V for the LCD display.

**Dave Jones:** Ah, couple of other things, 4.2, 2.3, 3.2. Ah, man, this thing's got everything. Here we go, the microprocessor. Ah, the customer chip. Custom chip. I love it. And it's got a has multiple functions, clock generator for CPU and UART. Uh

**Dave Jones:** the PIA adapter for the printer or also the screen, keyboard, memory management, PCMCIA, sound generator, of course. Forgot about that. Man, a whole ton of stuff. Firmware, static random access memory. Ah, this wiki's got everything. I love it. And good on your hands, Jürgen

**Dave Jones:** Böhling, if I'm pronouncing that correctly, from Düsseldorf in Germany. Fantastic. And contributors McDeath and Nilquader as well. Awesome. Thanks for sharing the information. It's brilliant. So there you go. Here's a little look at yet another vintage notebook computer. Hope you

**Dave Jones:** liked it. Sorry about the repair. Boring as bat poo. You can't win all the time. But anyway, if you want to discuss it, jump on over to the EV blog forum. If you like it, please give it a big

**Dave Jones:** thumbs up. Catch you next time.
