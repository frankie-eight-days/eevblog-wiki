---
video_id: HWlpqSrabKs
title: EEVblog #448 - New PICkit 4 & AVR Dragon
url: https://www.youtube.com/watch?v=HWlpqSrabKs
source: youtube-asr
timestamps: {"0": 1, "1": 11, "2": 22, "3": 46, "4": 63, "5": 79, "6": 109, "7": 128, "8": 143, "9": 153, "10": 167, "11": 187, "12": 197, "13": 210, "14": 224, "15": 247, "16": 260, "17": 271, "18": 287, "19": 303, "20": 316, "21": 339, "22": 355, "23": 365, "24": 373, "25": 387, "26": 400, "27": 412, "28": 425, "29": 435, "30": 458, "31": 473, "32": 484, "33": 506, "34": 521, "35": 526, "36": 541, "37": 556, "38": 566, "39": 578, "40": 589}
---

**Dave Jones:** Hi. You may have read in the last day or two about some news in the PIC and AVR camps, Microchip and Atmel for you fanboys out there. Pretty exciting stuff.

**Dave Jones:** Um, as you may know, Microchip actually tried to buy Atmel like, you know, 3 4 years ago or something now, but it all fell through. The negotiations didn't work out.

**Dave Jones:** The financial crisis happened. Some other partner pulled out. Blah blah blah. But the two companies have been talking ever since then and they've finally announced what is it? A cross-platform technology sharing agreement between the two companies where the tools from both companies are going to support the other company's products.

**Dave Jones:** What the? But as it turns out, it's not as silly as it sounds because they're now sharing fabs. The two companies are cooperating on various levels, so it makes sense, I guess, for the two companies to offer support for the individual products.

**Dave Jones:** So, what Atmel first start cab off the rank, they're going to have a new AVR Dragon almost identical to the current AVR Dragon, but it's going to support the Microchip parts and vice versa.

**Dave Jones:** There will be very shortly, if not already, a new PICKit 4 which will also have device support for Atmel parts. Now, Atmel have um they don't have the new production hardware ready right now, but they've sent me some firmware upgrades for my existing AVR Dragon board, as you may may be familiar with, that allows it to program Microchip PIC parts and be compatible with the MP the

**Dave Jones:** new MPLAB X environment. So, woohoo! Give it a go. Now, this is actually a rather clever and possible because of not too dissimilar programming interfaces between the two. If you know the PICkit 3 and the ICSP interface, six-pin single inline header, of course.

**Dave Jones:** But the AVRISP interface is a six-pin dual inline header, but nothing you can't fix with a adapter cable, of course. But there are, of course, you know, protocol and other differences between the two.

**Dave Jones:** And of course, um a lot of the PICs require that a high voltage programming source, that VPP source, which of course the AVR Dragon, you can do the high voltage programming part on there.

**Dave Jones:** But I believe that the you have to wait for the new version of the AVR Dragon to get that capability. They will have the Microchip ICSP port directly on the board, so you can just, you know, the inner pin, you don't need the adapter cable, just plugs directly in.

**Dave Jones:** But I don't have the new hardware. I've only got the new firmware for the existing one, which you're able to download for owners of the old AVR Dragon. So this old version of the board with the new official firmware will only support PICs with the low voltage programming, LVP programming mode.

**Dave Jones:** So we're going to actually try that today. I've got the new firmware programming. We're going to bring in an old friend, the Micro Calc project. You may remember this from quite a few years ago.

**Dave Jones:** I did a video on this, never finished the thing. Unfortunately, world's uh um first credit card thin scientific calculator. Really awesome little project. Those Bob Budge wise, if you remember.

**Dave Jones:** Um that was a silicon bug. Did a video on this, silicon bug inside the PIC 24 series chip. Real pain in the ass that one was. So um it swapped the ICSP interface.

**Dave Jones:** Real Anyway, um this 24F PIC supports LVP mode, so we should be able to program it with this new firmware. Let's give it a try. And as far as I know, uh Microchip are not going to release firmware for the existing PICkit 3 to support the AVR devices, but you will be able to buy the new PICkit 4, which will support, I believe, what they're telling me is the

**Dave Jones:** full range of AVR chips. Awesome. Because really, um it's just a apart from the high voltage uh programming stuff, it's really just a protocol uh difference between the two because you're just driving logic I/O pins, basically.

**Dave Jones:** So, you know, that's how they're able to do this. It's actually rather cool. So, it's got to get uh power from the actual uh board itself, and it does that by um there's a second uh VCC connector up here.

**Dave Jones:** If you're familiar with the AVR Dragon, you can supply power through to the board, no worries. So, I've uh just got it hooked up to the ISP. We've got the new uh official uh firmware in there, and um let's see if we can uh get this thing talking.

**Dave Jones:** I mean, we're plugging it. Plug it in, and uh it doesn't auto detect. What I've got here is the um PICkit uh 3 um programmer software, but it'll work inside MPLAB X or whatever um software you want to use.

**Dave Jones:** So, it doesn't auto detect. Let's go into tools, and it should check communication. It should identify it as a genuine PICkit 3. It shouldn't know the difference. Ta-da! Hey, PICkit 3 connected.

**Dave Jones:** ID, no worries. All right. Now, let's uh give this thing a go, shall we? We've got it connected, no device uh detected there yet cuz we haven't chosen our device family, but once we choose our device family, 24F, hopefully it should auto read, and let's give it a go.

**Dave Jones:** Yep. And bingo! Look at that. PIC Woohoo! We have a winner. PIC24 device found. There it is, 24 FJ256GA106. All right, we've got all FFs at the moment in that chip.

**Dave Jones:** So, if we read it, let's give it a go. I can't remember what's actually programmed into this thing. Um you know, I as far as I know, it it doesn't work.

**Dave Jones:** There's nothing on the LCD. I was in, you know, debug mode or whatever. I was mucking around with it last many years ago. So, I don't know, but it should read in something.

**Dave Jones:** We should be able to read in some data. So, let's give it a go, shall we? Read. There we go. Hey, our lights come on. It's reading. It's reading.

**Dave Jones:** Come on. It's taking its fat time about it. Whoop, done. Look at that. Beautiful. And now we have What do we have? Yeah, we've got data. It's no longer FF.

**Dave Jones:** It's all 1670, whatever that is. Config done. But there is, yeah, yeah, there is data there. So, I don't know what program I had in this thing, but it doesn't matter.

**Dave Jones:** So, there you go. It reads. There you go. We have a um We have a An AVR Dragon now supports PIC chips. Awesome. And we'll try that same thing again.

**Dave Jones:** Let's just write the same data back cuz I don't have the original program. Who cares? Let's just see if it writes. It reads no problem at all. Program memory also the configuration fuses, everything.

**Dave Jones:** So, we'll just write that. And writing device program memory. Yeah, it could take a while. Come back when it's done. Well, this thing's got like 256K of flash. It's got a lot of flash in there, so it will take a bit.

**Dave Jones:** Woohoo! There we go. Programming successful. Bingo! That works a treat. I declare that to be a winner. It's not running, of course. Nothing actually runs on this firmware. I powered it up before and before this and it doesn't run at all.

**Dave Jones:** So, we have a winner. I like it. So, there you have it. That worked an absolute treat. We now have the AVR Dragon programming well, in this case, a PIC 18F part.

**Dave Jones:** No problems at all reading and programming. This is just awesome and apparently they're going to now support Atmel are going to support all of the Microchip parts and Microchip are going to support all of the Atmel parts officially in their various development environments and on their programming platforms like the AVR Dragon and the PICkit 3.

**Dave Jones:** So, watch out for the new AVR Dragon version of this, which has the ICSP support on it and the new PICkit 4, which is coming out shortly. I have been promised one.

**Dave Jones:** I don't know. It could be in the mail, but I'm definitely going to do some more videos on this when it arrives cuz this is a big historic announcement.

**Dave Jones:** I like it. It means that you can choose either of the companies' development tools to support each other and it makes sense. Companies like this have to you know, team up like this these days in order to survive.

**Dave Jones:** So, it uh I you know, it's probably going to piss off a lot of the fanboys. They're not going to be happy. Oh, the Atmel fanboys. Okay, I don't want my development tools polluted with that Microchip crap.

**Dave Jones:** They're ranting in their mother's basement. Goodness. Anyway, I I like it. I give it a thumbs up. It works. I haven't don't know what happens with the compiler support at the moment.

**Dave Jones:** I haven't tried that, but all the details are on the um Atmel and Microchip websites and I'll link those in down below and you can check out the announcements and stuff for yourself.

**Dave Jones:** So, more videos coming soon. If you want to discuss it, jump on over to the EV blog forum. And if you like the video, please give it a big thumbs up as always.

**Dave Jones:** Catch you next time.
