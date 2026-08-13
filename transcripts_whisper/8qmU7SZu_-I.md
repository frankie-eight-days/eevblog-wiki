---
video_id: 8qmU7SZu_-I
title: Altera Software Dongle Teardown
url: https://www.youtube.com/watch?v=8qmU7SZu_-I
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 43, "3": 58, "4": 84, "5": 105, "6": 125, "7": 142, "8": 162, "9": 176, "10": 201, "11": 223, "12": 242, "13": 263, "14": 284, "15": 302, "16": 326, "17": 345, "18": 366, "19": 385, "20": 406, "21": 428, "22": 446, "23": 464, "24": 483}
---

**Dave Jones:** Hi, quick teardown time. Check out what I found in just a box of stuff that I was moving. An Altera Development Tools software guard, otherwise known as a dongle or a software lock. This was very common back in the 80s, probably into the 90s.

**Dave Jones:** I don't think any software was still dongled in the 2000s, was it? If it does, if it was, let us know. Anyway, for high-priced software, which Altera Development Tools, I believe it was Quartus, it was still Quartus back then, was it? I'm not sure of the timeline of that, but anyway, you used to pay a ton of money for that.

**Dave Jones:** And you still can if you buy the top tool, but anyway, none of this free rubbish that they give away these days. But yeah, it used to cost a lot of money. It was very common for very expensive engineering software like these FPGA Development Tools,

**Dave Jones:** other, like, compilers. Altium Designer, which was ProTel Autotracks back then, used to come with a dongle. Anyone remember version 1.61? Fantastic, that was the industry standard forever. And you could actually get, it was a big deal when they released the 1.61 ND, or the no dongle edition of ProTel Autotracks.

**Dave Jones:** And yeah, then a lot of people pirated the no dongle version. Anyway, they used to have these hardware dongles, which are software locks. In this case, it plugs into the computer parallel port, and it contains some sort of magic-y doodad that the software checks to see if you actually have one of these, and if you do, then it'd run the software.

**Dave Jones:** If you didn't, it'd fail. Um, hands up, if you had software that did this, did you circumvent it? How easy was it? Of course, you could hack, you could either hack these a couple of ways. One would be a hardware hack, of course, to either duplicate or simulate this or whatever yourself,

**Dave Jones:** or you could just hack the software to, you know, like bypass the check-in routine or whatever. But I thought we'd tear this down, have a look inside. Will it be simple or complex? Let's go. But I just wanted to mention, the PC parallel port, the Centronics parallel port, you could do a ton of stuff with that.

**Dave Jones:** And a lot of projects I developed in the 80s and 90s used the parallel port. Because it was a bi-directional I.O. port. You could actually, and you could get reasonable transfer rates. So I did, you know, real-time oscilloscopes that updated at like, you know, 30 frames per second back then.

**Dave Jones:** Capture, I don't know, don't remember what the actual data rate was, but I'd be getting, you know, really fast real-time oscilloscope updating through the parallel port. Ah, I love the parallel port. Ah, none of this USB rubbish. Well, this seems like it's going to be easy.

**Dave Jones:** And a lot of these were potted, of course, so that you couldn't reverse-engineer them. No, not potted. Look at that. Wow. There's not much in it, but oh, have they, they've rubbed the numbers off. Ah, there you go. In a vain attempt to protect reverse-engineering of this thing,

**Dave Jones:** they've scrubbed all the numbers off. Are they? They're probably just like some 7-4 series logic, you know, something like that, perhaps. I don't know. Well, that's interesting that there's an 8-pin jobby on there. Maybe not. Maybe it's a bit more complicated. Maybe it was like a E-squared PROM or something, perhaps.

**Dave Jones:** Hmm. Of course, we could get in there and reverse-engineer that, but it's decades out of date, and yeah, there's just no point anymore. But if anyone wants to do it for an exercise, then by all means do so. But I suspect we've just got some latches or something,

**Dave Jones:** and maybe, you know, the 8-pin, if they are like standard 7-4 series logic, like, it's not going to be a microcontroller, because A, they didn't have the micros with, like, you know, I don't see any crystal on here, or anything like that. So I doubt it's going to be that, you know, with the internal oscillator.

**Dave Jones:** None of that rubbish, especially in a 2-4, in a 14-pin package like that. So they're obviously going to be, I believe, my money would be on, you know, standard 7-4 series logic there. With this jobby here, well, can we see some pull-up resistors on that?

**Dave Jones:** Perhaps? Do we have a couple of... that'd be center, would it? So this one goes over here like this. This one goes over here. These two Vs here. That one goes to that cap, which I presume might be a... Oh, no, I don't see another...

**Dave Jones:** I don't see another V going off that. Hang on. No, and those two Vs there. So there's so much to the theory about that being a I2C, you know, EEPROM or something like that. Could be like an SPI interface, but that's actually got a surprising amount of resistors on there.

**Dave Jones:** That's actually a fairly complicated beast. A couple of diodes in there, what have they got? Like steering diodes or something? That's, you know, they've gone to a lot of effort. So, hmm. Let us know what you think down below. Has anyone ever, did anyone ever reverse engineer one of these Altera dongles?

**Dave Jones:** Someone out there surely has. Come on. Aha! As it turns out, this is actually a Rainbow Technologies, Rainbow Tech module. And Rainbow Tech are one of the, well, were one of the leaders in these dongles. If not, they were like, you know, if they weren't one of the biggest, they were the biggest.

**Dave Jones:** So this could be the Sentinel model, it's called. And this is actually now being like fully emulated, because a lot of companies are still like running really old software that still rely on these dongles. And of course, you know, companies gone bust, you can't buy them anymore.

**Dave Jones:** Rainbow Tech were bought out by Safe Inc., a company like that. So, yeah, and these like transitioned into USB modules and, you know, PCI bus modules and all sorts of things. But this original parallel port module, anyway, you can actually get an emulator to apparently read these,

**Dave Jones:** if it is the Sentinel model, that is. And yeah, and then emulate it 100%. So, cool bananas. Unfortunately, I don't have a ready PC available with a parallel port to sort of run that on right now. But if anyone wants to have a crack at that, to tell us what's going on there.

**Dave Jones:** And of course, these, you know, later ones contain all sorts of encryption and stuff like that. So it's likely this one has the serial number embedded in there to actually match this thing up. It's most likely, because this is not an amateur AI dongle.

**Dave Jones:** This is, you know, from one of the best in the business. So, but all the other stuff to interface, there's lots of resistors and caps on there. Some of them are going to be pull-ups. Some don't seem to be pull-up-like values. So, yeah, I'm not sure what the deal is there.

**Dave Jones:** And the diodes, you know, we've got some diode steering or something. Hmm, not sure. So if you've got any more info on this little baby, this RainbowTech, and if you can verify that it is a Sentinel-1. I couldn't find any ready available, like, teardown photos on the net.

**Dave Jones:** Maybe my Google-foo, I'm not trying hard enough. But anyway, if you've got any details on that, or like a schematic, let us know.
