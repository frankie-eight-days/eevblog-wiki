---
video_id: 0YiUqPasx28
title: EEVblog #385 - Amstrad NC100 Notepad Repair
url: https://www.youtube.com/watch?v=0YiUqPasx28
source: youtube-asr
timestamps: {"0": 2, "1": 17, "2": 36, "3": 47, "4": 61, "5": 70, "6": 81, "7": 93, "8": 103, "9": 113, "10": 126, "11": 136, "12": 149, "13": 161, "14": 182, "15": 201, "16": 211, "17": 223, "18": 235, "19": 255, "20": 263, "21": 274, "22": 289, "23": 304, "24": 315, "25": 330, "26": 343, "27": 352, "28": 377, "29": 390, "30": 409, "31": 421, "32": 431, "33": 450, "34": 474, "35": 485, "36": 498, "37": 516, "38": 530, "39": 541, "40": 555, "41": 569, "42": 581, "43": 598, "44": 611, "45": 624, "46": 633, "47": 643, "48": 664, "49": 685, "50": 699, "51": 710, "52": 720, "53": 732, "54": 750, "55": 772, "56": 792, "57": 806, "58": 815, "59": 832, "60": 848, "61": 872, "62": 886, "63": 897, "64": 918, "65": 927, "66": 938, "67": 953, "68": 964, "69": 975, "70": 989, "71": 1006, "72": 1019, "73": 1034, "74": 1050, "75": 1073, "76": 1084, "77": 1097, "78": 1111, "79": 1128, "80": 1139, "81": 1150, "82": 1161, "83": 1172, "84": 1183, "85": 1196, "86": 1210, "87": 1217, "88": 1232, "89": 1246, "90": 1263, "91": 1275, "92": 1287}
---

**Dave Jones:** Hi, hot on the heels of the previous video where I tore down the Cambridge Z88 computer, we've got another one of a similar ilk, the Amstrad Notepad NC100 and it uses the same BBC Basic we saw in the Cambridge Z88.

**Dave Jones:** Apparently and it's a little bit younger, I guess. It's 90s early 90s vintage, there we go, 1992 vintage there, made in Japan instead of made in Scotland and it's, you know, similar little battery powered A4 notebook.

**Dave Jones:** Looks like it has a battery backup in there, of course, and little couple little flip out feet. This one's actually missing the battery door here, so a bummer, but still it's going to work.

**Dave Jones:** It's got a serial and a parallel port on it, DC jack, contrast and a memory card expansion slot and the good thing is it doesn't work. So, I thought we'd have a crack at fixing this one.

**Dave Jones:** First thing I'm going to do is check the current consumption of the battery to see if there's any standby current at all cuz it does seem to use a soft power switch.

**Dave Jones:** So, no, I can't see it. That's no, that's not 0.1, it's still the same if I lift the probes off there. So, I expect it to draw at least, you know, that's like in the order of 10 nanoamps.

**Dave Jones:** So, you know, you'd expect it to have some sort of standby power consumption, but it's got zip. Now, there's one totally fascinating aspect of this thing which I absolutely love.

**Dave Jones:** Look at this door down here. You flip that off and look what you've got. You've got what looks like the ROM chips. Let's whack it around here so we can see it.

**Dave Jones:** There it is, Amstrad UK A2. That looks like it's a masked ROM chip so that you can change the ROM just by lifting the panel and whacking in a new chip.

**Dave Jones:** I I think I've seen that on any machine before. Now, there was one of the screws missing on this thing, so maybe somebody's had a crack at this thing.

**Dave Jones:** Only one way to find out. Looks like we have some metalwork under here. Looks like there's a couple of catches along here I've got to snap off first. And here we go.

**Dave Jones:** I got it. I think I thought I did. Yep, there we go. Ta-da! Nakajima I guess that's a uh I don't know. Is that some sort of date code?

**Dave Jones:** Production date code? Look at the shielding on this thing. It's actually quite uh quite quite substantial. They shielded the entire keypad backing on that and the main board as well.

**Dave Jones:** Neat. It looks like this just lifts out here. The keyboard's connected. Looks like I can probably flip it over like this and lift that off. Ta-da! That's easier. We have board predominantly uh surface mount, almost all of it, and we've got the uh LCD up here which we didn't see last time on the Z 88.

**Dave Jones:** So, yeah, that's actually um fairly modern, but that's what you'd expect in the differences between the uh 1987 vintage uh Z 88 and this 1992 vintage NC 100. Now, let's have a look and see what we've got here.

**Dave Jones:** Yes, we do have a soft uh tactile power switch up here. So, maybe there's something wrong with the uh just the power on circuitry. It could be that simple or it could be more complex.

**Dave Jones:** I guess we'll find out. Got our DC input jack up here. There's the uh battery backup CR2032 backup battery. Got a couple of mod wires going around here. They've uh hacked in there.

**Dave Jones:** There's a little resistor there plus two mod wires, so they've done this after uh after production, obviously. They decided to make those changes. Uh couldn't be bothered to respin the board.

**Dave Jones:** Cheaper just to put a couple of mods on there. There's our Zilog Z80 CPU. Uh our main uh LSI uh ASIC up here, which would handle pretty much uh everything else the um ex- part from the CPU because we've basically got the big LSI, we've got the memory, there's the ROM socket on the back.

**Dave Jones:** There's another device there, not sure what that is offhand. And a couple of the miscellaneous uh chips over here and another one up there. But apart from that, that's it.

**Dave Jones:** I mean, this would be the serial chip up here cuz that goes off to the serial port. Um but this puppy would handle all of the system architecture for the Z80 uh for a Z80 uh CPU computer.

**Dave Jones:** And we've got our date code, 20th week '92. So, it was uh manufactured would have been manufactured fairly shortly after that. And all the date codes are for the various chips seem to uh match.

**Dave Jones:** So, been manufactured in the weeks or months after that. Um there's no crystal, it just uses a ceramic resonator there at uh 12.2 MHz. This is the real-time uh clock chip, of course.

**Dave Jones:** I You know, I don't know the number offhand, 8521, but there's the 32 Oh. Can't see that on the screen. There's the 32 kHz uh watch crystal right there.

**Dave Jones:** Nice little solder strap on that. I like it. Um pretty old-school stuff. A HC 00, which they didn't populate for some reason, not sure why. And it is all um you know, uh fairly modern surface-mount stuff.

**Dave Jones:** It's not ancient like we saw in the 1987 vintage Z88. And there's the main chipset, D65034 GD093. Uh man, I reckon you'd have a hard time finding data on that.

**Dave Jones:** I don't even think I'd bother Googling it. We'll just have a quick look at the display board here. We've obviously got some sort of you know, eight-bit parallel interface or something like that.

**Dave Jones:** And we've got OKI brand display controls, very common for the time and still nowadays as well. These are 5299C's. So, it's got a bunch of 5299C's all the way across there until we get to the end where it is an M5298I instead of a 5299C.

**Dave Jones:** And on the back of the board here, we've got a surprising amount of passive stuff around here. Tons of it. Check it out. They've got that plastic insulating sheet there so it doesn't short out to the shielding.

**Dave Jones:** There's an absolute buttload of resistors and SOT23's on here as well. Tons of them. There's our ROM. And uh there's a few more stuff up there near the parallel port as you'd expect.

**Dave Jones:** Couple near the serial and whole bunch more. Looks like series resistors on the expansion header there. Now, before we start to go feral on this thing with the scope, let's check out some basics.

**Dave Jones:** Here's our battery input here. It looks like it's got these two traces going directly all the way under there, all the way under there, nowhere else directly over to the DC power jack.

**Dave Jones:** So, it looks like it's just in parallel with the DC power jack there. Now, if we this soft button obviously has to do with something around here. Soft start power switch, but let's have a zoom up in here and there's something that immediately sticks out.

**Dave Jones:** F301 0.8 amps. Fuse. Haha, can it be that easy? Let's get the meter out and measure it. Let's have a go Here, the meter works as both a convenient uh prop for the item on video and Ah, man, it's blowing.

**Dave Jones:** Ah, so so much for the repair video, folks. Sorry. Thought it'd be more interesting than that. No, probably not. But, of course, the thing is, why did it blow?

**Dave Jones:** I don't know. Let's um measure the other side of it and ground, shall we? So, we'll get our ground here. Let's assume that this around here is ground. I'm pretty sure the big plane is always ground.

**Dave Jones:** So, if we measure this side of it, no. No, 0.25 meg. That's all fine and dandy. Don't mind that at all. And it looks like they uh specked into the design a common mode choke there, but they've just decided to uh short it out.

**Dave Jones:** There's the ground, so it would have gone from the DC input jack through to the ground like that, but it doesn't. And uh of course, the DC input jack through to those filter caps there, but it doesn't.

**Dave Jones:** And we'll just measure across that filter cap there to make sure it's not shorted, and no, it's not. 46k, and you'd expect it to rise as the uh capacitors charge up.

**Dave Jones:** So, that's all working hunky-dory. So, um I'm going to presume that the uh power rails. And I'm not sure if there's another voltage regulator on here. There certainly could be.

**Dave Jones:** Um that there looks like it could be a voltage regulator. So, maybe they have a 5-V regulator on this thing. Although, if you're powering it from uh 6-V batteries, the four uh double A's in series, that's um 6-V uh nominal.

**Dave Jones:** Um but, that's going to drop fairly drastically. So, a 5-V regulator, even a low dropout one, isn't going to regulate uh for very long over that full battery discharge curve.

**Dave Jones:** So, what I'll do is I'll just power this thing from a 6-V bench supply, and uh let's give it a go. So, 6 V, switch it on, and soft power switch.

**Dave Jones:** Is it drawing any current? Oh, yep. There we go. Yep, it's on. Ah. Man, too easy. Where is he? Yeah, there we go. Lithium battery is low. Please switch off and replace battery.

**Dave Jones:** Haha. We have a winner, folks. All it was was a fuse. That's actually very disappointing, cuz I was hoping that we'd hopefully we get something more exciting than that.

**Dave Jones:** But, no. Well, I didn't have a direct surface-mount replacement, so I just put a little axial one in there. No problem. It should fit nicely against that metal shield, I think.

**Dave Jones:** We've got insulator there. Not a problem. So, I'm going to put this sucker back together, and we'll power it up. And here we go. We can see the standby current consumption here, about 72 microamps or thereabouts.

**Dave Jones:** So, let's switch this sucker on. Bloody default AC, pain in the ass. So, let's see. About 60 milliamps. So, very similar to the draw of the Z88. Let's have a quick squeeze here at the main clock.

**Dave Jones:** And should be 12. There we go. 12.363 MHz. That's the That's, of course, not a crystal. That's a ceramic resonator. And let's have a look at the main oscillator as well, which is pin one of the 44-pin PLCC package, and it is continuously Why I say it?

**Dave Jones:** Yes, it is continuously running. Although this thing isn't at in at its application mode yet. It's just giving that display. There you go, it just switched off. So, but let's What was that running at?

**Dave Jones:** Let me switch it back on. There you go. It's running at 6.18 MHz. So, that's pretty quick for a Z80 processor. And because the back case is not on this thing, I need to still access and probe the circuitry.

**Dave Jones:** I can't put the coin cell in back, which is really annoying. So, I've hooked up another supply over here. So, let's power it on and we should get No.

**Dave Jones:** Lithium battery Ah, helps if I turn the load switch on. Let's give that a go again. There we go. Ta-da! We're up. We're in the main screen. Brilliant. Works a treat.

**Dave Jones:** And interestingly, the current draw is now jumping around a bit, but it's, you know, going anywhere from 40-odd milliamps up to 50. So, that possibly could indicate that the clock is skipping again to save cycles and save power.

**Dave Jones:** So, let's probe that again and see what we get. And bingo, there it is. Let's single shot capture that. See what we get. We've got a couple of bursts large bursts here of uh 2 milliseconds, 6 just over 6 milliseconds each with a dead time of almost 4 milliseconds between them.

**Dave Jones:** And then we've got a shorter little burst here which that's about 200 microseconds per division. 200, 400, 600, you know, 700-odd microsecond burst there. There you go. So, it looks like it has a couple of these shorter bursts with a couple of longer bursts.

**Dave Jones:** And uh it's just waiting for the keypad. I'm assuming it's just waiting for a key. So, let's press a key. And yeah, we can see it insert. There Ah, there we go.

**Dave Jones:** It just not only did it insert a couple of more, I'm not sure what I'm actually running here. I have to flip my screen over. I'm not doing anything, actually.

**Dave Jones:** Um enter doesn't do anything at the main screen. So, let's go into the word processor. Press the yellow and red. So, there we go. It does seem to jump around a bit between uh actually between having none of those longer bursts.

**Dave Jones:** See? There it is. Very interesting. So, let me call up the word processor. There we go. Bam. You saw it uh just go full speed there, and we're now inside No, we're not inside the word processor.

**Dave Jones:** It's weird. So, you can see how this main uh system ASIC here is always running by that uh 12 MHz ceramic resonator, and you know, it's they inter- I guess it can shut down its internal uh parts as well when it's not doing anything to save power, but the oscillator's always running there, and it only supplies the clock through to the CPU uh when it needs to.

**Dave Jones:** So, this will handle the uh keyboard as well so that it's uh sitting there waiting for the key presses to uh turn the thing on, supply power, interrupt the CPU, boot it up, and uh start it running again, and action those keys.

**Dave Jones:** And that's how they save power on these types of systems. And this is the coolest key ever. Secret menu. Woah. Let's see what's in there. Let's press this sucker and see what we get.

**Dave Jones:** Here we go. Uh enter password. Woah, let's try I don't know, 0000. What the? Sagan was here? This is one heck of a big calculator display. Woo. Love it.

**Dave Jones:** No scientific functions, though. Bummer. Unfortunately, there seem to be a couple of stuck keys on this thing. The shift and this one up here seem to uh get stuck.

**Dave Jones:** I've tried to sort of clear them, but it doesn't seem to work. If anyone's got any good ideas for that, let me know. And it's really not obvious how to get into the BBC Basic either because looks like you can't scroll this main menu.

**Dave Jones:** It's only got the word processor, calculator, and diary, address book, which you use, you know, function, sort of, you know, word that'll take you into the word processor, start a new document, and this takes you into the calculator, and uh you know, um press stop takes you back to the main menu.

**Dave Jones:** Well, it's function B. Apparently, there it is. And there's RT Russell again. And we've got our little basic program there looping through printing I. Yes, it has to scroll the whole screen.

**Dave Jones:** I know I haven't put the semicolon at the end of it. Whatever. Let's run it. Well, it does seem to be substantially quicker than the uh Z88. No surprises.

**Dave Jones:** It's running exactly the same basic interpreter on the Z80, uh but it's running at like a double the clock rate. So, let's uh probe this clock again and see what we get.

**Dave Jones:** Stick it in here. And pin one on our clock. There you go. It is fully fully continuous. So, let's uh put this down here, and we are getting more than just over 5 V there.

**Dave Jones:** 1 2 3 4 5. There we go. And if I adjust the uh voltage on my supply, that doesn't go up. So, that's clearly being regulated. Now, here's our main clock, and it's just over uh 5 V there.

**Dave Jones:** And what I'm going to do is I'm going to drop my supply voltage here and see where that thing drops out. Ah, no, it looks like There you go.

**Dave Jones:** It's regulated. It's regulated, folks. It's not a It's not a 5-V linear regulator. So, it's working all the way down. Wow, there we go. It drops out at about 3.3 V.

**Dave Jones:** That's very impressive. And with everything tech, there's an enthusiast group for everything. I present to you the cpcwiki.eu, a surgical guide to the Amstrad NC. Here it is. They've got some cool-looking ASCII diagrams here, which show which tell you all the details.

**Dave Jones:** There it is, 6 MHz. Yeah, we measured that. 64 K internal memory, 15 K system, 11 K upper, 32 K lower. It's got a PCMCIA slot, which allows you to expand to 1 meg maximum.

**Dave Jones:** It's got a 480 by 32 pixel display, usually 8 by 80. There you go, 40 to 60 milliamps, which is what we what what we measured. And how to get the firmware number, memory cards, how to open it.

**Dave Jones:** Already done that. What's inside. They've labeled all the chips. There we go, there's the 6 MHz Z80. There's the UPD65034 custom chip. They call it customer chip. But, that's just a custom ASIC.

**Dave Jones:** And you know, a bunch of miscellaneous other stuff. They've got the UART and the RS232 driver and the real-time clock. And And interestingly, down here, this is what I like, a simplified block diagram.

**Dave Jones:** And as I mentioned before, IC302 here is the main ASIC, and it runs continuously on the 12.2 MHz ceramic resonator there, and everything hooks into it. I mean, here's IC301 up here.

**Dave Jones:** Here's the CPU, but it's hardly, you know, according to this block diagram, it's hardly doing anything at all. And And everything runs off that. So, you've got the the LCD controller is built in there.

**Dave Jones:** There we go, directly off it. The keyboard matrix, of course, so it knows um when you've actually pressed a key, so it can, you know, start up the clock and interrupt CPU and all that sort of jazz.

**Dave Jones:** And uh then we've got our uh real-time clock, PCMCIA is all hooked in there. All your memory address and all that stuff is all hooked into that system ASIC.

**Dave Jones:** So, the thing, man, wouldn't be able to do a damn thing without that ASIC. And let's scroll down here. We've got our power supply block diagram. We can probably zoom into that a bit more.

**Dave Jones:** Here it is. Um yeah, there it is. 6 V DC in, battery directly connected across it. There's the fuse that blew, little pain in the ass. And uh plus 6 V and looks like there's plus 5 V voltage regulator as well.

**Dave Jones:** 5 V BK there, which is the uh backup for the buffer RAM, so the SRAM. SRAM doesn't need to be refreshed. It, you know, it only takes microamps or nanoamps to uh to actually retain the information.

**Dave Jones:** So, as soon as you stop the clock and you've as long as you got uh power on those SRAMs, it will um retain the data in there for you.

**Dave Jones:** So, you got minus 15 V for the LCD display. Ah, couple of other things, 4.2, 2.3, 3.2. Ah, man, this thing's got everything. Here we go, the microprocessor. Ah, the customer chip.

**Dave Jones:** Custom chip. I love it. And it's got a has multiple functions, clock generator for CPU and UART. Uh the PIA adapter for the printer or also the screen, keyboard, memory management, PCMCIA, sound generator, of course.

**Dave Jones:** Forgot about that. Man, a whole ton of stuff. Firmware, static random access memory. Ah, this wiki's got everything. I love it. And good on your hands, Jürgen Böhling, if I'm pronouncing that correctly, from Düsseldorf in Germany.

**Dave Jones:** Fantastic. And contributors McDeath and Nilquader as well. Awesome. Thanks for sharing the information. It's brilliant. So there you go. Here's a little look at yet another vintage notebook computer.

**Dave Jones:** Hope you liked it. Sorry about the repair. Boring as bat poo. You can't win all the time. But anyway, if you want to discuss it, jump on over to the EV blog forum.

**Dave Jones:** If you like it, please give it a big thumbs up. Catch you next time.
