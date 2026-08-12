---
video_id: cwNBfnNO4AY
title: EEVblog #1130 - Mailbag Monday
url: https://www.youtube.com/watch?v=cwNBfnNO4AY
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 24, "2": 49, "3": 73, "4": 95, "5": 114, "6": 126, "7": 143, "8": 163, "9": 180, "10": 194, "11": 210, "12": 227, "13": 241, "14": 258, "15": 272, "16": 286, "17": 305, "18": 326, "19": 344, "20": 362, "21": 377, "22": 397, "23": 418, "24": 434, "25": 451, "26": 472, "27": 487, "28": 507, "29": 533, "30": 543, "31": 566, "32": 587, "33": 606, "34": 626, "35": 644, "36": 657, "37": 671, "38": 682, "39": 698, "40": 709, "41": 721, "42": 733, "43": 745, "44": 757, "45": 769, "46": 781, "47": 793, "48": 805, "49": 817, "50": 829, "51": 841, "52": 853, "53": 865, "54": 877, "55": 889, "56": 901, "57": 913, "58": 925, "59": 937, "60": 949, "61": 961, "62": 973, "63": 985, "64": 997, "65": 1009, "66": 1021, "67": 1033, "68": 1045, "69": 1057, "70": 1069, "71": 1081, "72": 1093, "73": 1105, "74": 1117, "75": 1129, "76": 1141, "77": 1153, "78": 1165, "79": 1177, "80": 1189}
---

**Dave Jones:** Thank you very much, Mike Rothen from Maidstone in the Old Dart. Let's check it out. I like what's in here because it's obsolete, apparently. Hmm. I don't know what is obsolete, but something is. Ooh, it's been X-rayed. Alright. I wonder if that was X-rayed by the POMS or locally.

**Dave Jones:** I don't think we give a toss. Oh, there's a note. Oh, no! No! No! It tore the box! Personal computer design tool. Hands up if you had one of these. Design in Taiwan '87. The good design. The good product design award. It won a good product design award.

**Dave Jones:** Fantastic. It's obviously some sort of logic trainer. It hooks up to a PC, so I wonder if it, like, hooks up to the AT, XT AT bus or whatever. Oh, fantastic. Oh, yeah. Oh, not yet. No, it's got its own, yeah, it's got its own dedicated interface board.

**Dave Jones:** Oh, sweet as. Check it out. It's just basically I/O. Like, there's nothing else, nothing else doing on there. It's just doing some address decoding. Yeah, it doesn't even have any gals or pals. It's just, uh, gals and pals. Look at the yellow in on the bottom red board there.

**Dave Jones:** The bromine, um, leached out of the plastic. It was for, like, designing and developing PC cards, I guess. 'Cause why else would you, you know, want to access the address and data bus on a PC bus? Wow. Never seen this before. And a logic probe interface.

**Dave Jones:** Oh, we don't have the logic probe. Aww. But anyway, um, it's an interesting bit of kit. Thank you very much, Mike. Let's check it out. There's the interface board for it. As I said, like, there's no gals or pals or anything. Look at this.

**Dave Jones:** 7407. Fantastic. Thank you very much. Some, uh, 244s for latching out the data and, uh, driving it. And that's about all she wrote. You don't really need much to interface with the, uh, ISA bus. It's all just, yeah, just latches and buffers and stuff.

**Dave Jones:** I do find it interesting how they've mixed and matched their, uh, 244s. They just, like, couldn't get 'em all from the same batch. Neat. Wow, this is really something. The ATEC AT601 design tool for personal computer use. Thank you very much. It's actually got, uh, PC bus input and output

**Dave Jones:** so that you could, uh, you know, breadboard stuff and breadboard your circuit inline and then, uh, feed it back out and stuff. So it's, uh, got a mains, uh, power supply on it. Flight house. Southampton. Hmm. And a switch-in, uh, basically the internal power.

**Dave Jones:** Looks like it's only for its own dedicated switch-in power supply, which gives you a plus/minus 5, plus/minus 12. Doesn't tell you anything about, uh, power and it just gives you multiple connectors for that. Logic probe. Unfortunately, Mike, uh, lost the logic probe, but it's just a digital logic probe.

**Dave Jones:** And then you can get access to all the interrupt pins, all the, um, knowledge pins, the oscillator, data bus, address bus, power bus. Fantastic. And output sync, oh, chop. I don't really know what that is. Designed to hook up to a scope or something?

**Dave Jones:** Hmm. Strange. So my guess inside this is that we're just gonna have a couple of, uh, buffers on the input 'cause I doubt that we're, uh, the 244s on the card over there are gonna drive the ribbon cable and just, like, come out directly, like, break out directly to this.

**Dave Jones:** They've probably got some more, uh, buffering there would be my guess. Um, and the switch-in power supply. Let's crack it open. Made in Taiwan. All of this stuff was made in Taiwan back in the 90s. Let's, oh, look at this. Like, Bakelite. Uh, yeah, there we go.

**Dave Jones:** Yeah, got some extra buffers, called it. And it looks like it's just got, like, it's just, like, repurposed. A, uh, a switch-in, uh, power supply. I'm sure they wouldn't have, uh, done that themselves. They, like, well, they definitely didn't. It's, uh, TPI Electronics, uh, Co.

**Dave Jones:** They, you know, but that could have just been a switch-in power supply at the time. Look at that. The resistor on top of the diode. It's pretty how you're doing. Oh, the snot is, uh, oop. The hot snot is, uh, a bit worse for wear.

**Dave Jones:** Hmm. Anyway, that's not the world's best. Just stop 'em flapping around in the breeze there. It's not the world's greatest power supply, is it? It's all a bit how you're doing, but, uh, there we go. They've just, like, bussing those between the, um,

**Dave Jones:** there was some hot snot to hold the screws down. And, once again, some, uh, 244s on there just to, uh, buffer everything. And a Gold Star! Oh, I haven't seen a Gold Star chip for a long time. Anyone remember Gold Star? Yes, they, that's the consumer electronics company,

**Dave Jones:** Gold Star. They did actually, um, make their own chips back in the day. Anyway, it's just a 74LSR153 from 9in. Jesus, soldering's pretty how you're doing, isn't it? Wow. Unbelievable. And what's that rattling noise? Oh, there we go. It's a screw. But, yeah, like, there's not much in it.

**Dave Jones:** It just basically just goes up to the, uh, sockets and then, like, they just didn't engineer that well, did they? Some poor bastard had to solder all that in by hand. And getting that stranded wire through each individual holes, if you could do all that and not have a little daggy,

**Dave Jones:** uh, short go over to the next one, you were having a good day. Trust me, that's terrible, Muriel. So, thank you very much, Mike, for that two-minute teardown. Wow, like, I didn't know, I don't think I've ever seen something like this with, uh, the breadboards like this.

**Dave Jones:** You've got four of 'em. That's, uh, standard-sized breadboards. That's, you know, fairly decent to, uh, uh, prototype your circuits and stuff that hook up to the ISA bus. Of course, it was only the 8-bit ISA bus. You want to do the 16-bit? I don't know, maybe they had another model for that.

**Dave Jones:** But, yeah, hands up. Yeah, hands up if you used one of these or you developed stuff for the ISA bus back in the day. Thanks, Mike. Yes, it's the Gigatron again. Thank you very much. Biosecurity screened. Thank you very much. Um, fantastic. Um, yes, they clued me up

**Dave Jones:** that they were sending me some extra stuff, which is fantastic, and I'll show you in a minute the four-layer board that now works. Spoiler alert. Sorry. But apparently we have a, uh, keyboard. Oh, here's a note. It's a long note. Um, it's a Pluggy Mc...

**Dave Jones:** Pluggy McPlugface. Um, an adapter that lets you hook up a retro PS2 keyboard. Still got one of those, I think. It translates, uh, into ASCII code, which the Gigatron can read. Fantastic, 'cause the Gigatron's only got, like, the PC. Uh, sorry, the controller input.

**Dave Jones:** And they sent me a new ROM as well, which has the, um, a WAS monitor, the original Apple I. So it, uh, it simulates and emulates an Apple I and has a basic, uh, interpreter. Fantastic. Let's power it up. Let's check out Pluggy McPlugface.

**Dave Jones:** Aw, gotta solder it. Oh, the irony of a TTL microcomputer needing one of these newfangled micros to do the serial conversion. Unbelievable. And I thought they had, uh, goofed this up for a second, um, because it just doesn't fit in there. But if you turn it over,

**Dave Jones:** no, the instructions are there. Mount U1 to the other side first, and they've conveniently cut away some of the socket there so we can whack it in. Someone was thinking. So, yes, this is the four-layer DaveCAD version, which you've seen in previous videos.

**Dave Jones:** And, yes, it does work. So we got ourselves the new version 3 ROM. Let's stoke it up. First world nerd problem. First world nerd problems. Check it out. We've got some extra options. Beautiful. Look at this. Wasmon. Basic. Tic-tac-toe. Bricks. And Tetronus. No idea what that is.

**Dave Jones:** Anyway, our keyboard works. And, of course, you've seen the, uh, pictures and stuff before. Tic-tac-toe. The Wasmon. Enter. Enter. Bueller. Spacebar. No. How do we enter the Wasmon? Uh. Uh. Do I have to read the instructions? Hmm. Yep. Home or end. There you go.

**Dave Jones:** Tiny basic. Version 2. Oh, whopping 5,900 bytes free. And four bytes free. You can do a lot in the extra four. Check it out. If I press the page down key, haven't read the instructions yet, just dicking around, um, it gives us the extra,

**Dave Jones:** um, you know, uh, instructions. It gives us the extra, uh, um, uh, uh, instructions. It gives us the extra resolu- look, a horrible resolution. It's stealing more cycles away from the video. Oh, we can have nice solid. Oh, sweet as. CLS. You ever seen a clear screen that slow?

**Dave Jones:** Oh, there's our OK. I was waiting for our OK to come up. Supports uppercase. Oh. Fancy, fancy stuff. Let's list our program. Let's run our program. Hello, world. Fantastic. So, um, fantastic. Doesn't the Wozmon supposed to have a flashing, uh, @ cursor here?

**Dave Jones:** Anyway, um, let's see if we can, uh, explore some memory contents. Oh, oh, we can go backspace. Oh, there we go. Yes, we can see the memory. Beautiful. Let's go all the way with LBJ, shall we? Ha, we're dumping the lot. Beautiful. And,

**Dave Jones:** of course, if we press page down, it'll go quicker. And, oh, that's flying. Oh, we can't do the last command. 00.FF. Wow. But, of course, if we, uh, aren't stealing as many cycles for the video, just takes a lot longer. Sweet as. Thanks,

**Dave Jones:** guys. Thank you very much, Robert. What has Robert sent? Let's have a look. Vintage tech. Tektronix is great. We're using, oh, cool. A museum of vintage tech. Cool. Oh, we've got some sort of generator board. Oh, yes. I won't show you what it's going to generate,

**Dave Jones:** but you can probably guess. Fantastic. What we're going to do, it's a programmed micro that generates XY data, which goes into our scope. Oh, let's have a look. And, of course, I've got to use, can you see it? Tektronix 2225. Let's do it on that.

**Dave Jones:** Beauty. It's the Tektronix Wizard. Woo hoo. Check it out. And the old Tektronix. And the old Tektronix. And the old Tektronix. And the old Tektronix. And the old Tektronix. And the old Tektronix. Woo hoo. Check it out. And the old Tektronix logo. Bring it back.

**Dave Jones:** Thank you very much. Fantastic. A bit of flicker on there. That's not the camera. That's actually just the rate that they're doing this at. But that's pretty smooth. Look at that. It's great. Anyway, if you don't know, the Tektronix Wizard used to appear back in,

**Dave Jones:** you know, schematics and manuals and stuff back in the day. Neat. And, of course, we can move that on the screen like that. Fantastic. It looks better. It looks better. And, of course, we can move that on the screen like that. Fantastic. And,

**Dave Jones:** of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that. And, of course, we can move that on the screen like that.

**Dave Jones:** And, of course, we can move that on the screen like that. And,
