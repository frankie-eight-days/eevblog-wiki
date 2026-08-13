---
video_id: 8iiatoU4yd4
title: EEVblog #53 - Mr Murphy and Microchip PIC Silicon Bugs
url: https://www.youtube.com/watch?v=8iiatoU4yd4
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 12, "2": 39, "3": 50, "4": 68, "5": 99, "6": 120, "7": 142, "8": 163, "9": 184, "10": 200, "11": 219, "12": 240, "13": 269, "14": 285, "15": 305, "16": 323, "17": 341, "18": 362}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, I'm going to talk about silicon bugs again. Now, I've mentioned these before in one of the very first blogs I did.

**Dave Jones:** In this case, silicon bugs in PIC microcontrollers. Now, it's not a problem with just PICs. It's every micro every type of processor on the market has silicon bugs in them. And it's a trap for young players. And as I mentioned before, you've got to read the silicon errata data sheet for the device you're

**Dave Jones:** actually intending to use in your projects just in case there's a feature in there that doesn't work or it has bugs in it that you're going to have problems with later down the track. And it's better to know that up front. And yeah, you guessed it, I've been caught out again.

**Dave Jones:** This is the new project I'm working on. It's my new credit card scientific calculator. And there's a quick sneak peek of it, but that's all you're going to get, okay? Anyway, it's a credit card scientific calculator slash computer. It's based on a PIC24FJ256K part.

**Dave Jones:** It's the 16-bit PIC24F series, just like on my MicroWatch project. And yeah, I hooked it up. And of course, it didn't work. First go, the PICkit programmer couldn't see the device at all. And Murphy's law, the thing never works first go. So I checked out all the lines and everything.

**Dave Jones:** The ICSP, the in-circuit serial programming bus on PIC microcontrollers only has five pins. It's very simple. There's clock, data, ground, power, and the programming pulse. And that's it. So I checked those lines and they're all working just fine. And so, you know, how do I fry my chip?

**Dave Jones:** It's one of these little, really tiny 0.5 millimeter pitch devices, you know, and they're easily damaged and pin shorted and all sorts of things. But I checked it all out and there was nothing wrong. The MPLAB and the PICkit programmer just wouldn't talk to my chip at all.

**Dave Jones:** And I was scratching my head for a little while debugging it. And then, you know, I came to the conclusion either it's a dead chip or there's something else going on. Yep, you guessed it. It's a damn silicon bug. And yes, I followed my

**Dave Jones:** own advice back in my very early blog. I read the silicon errata for this PIC device first before I put it on my board and got the first prototype manufactured. I checked it out and there were quite a few bugs in there, but they didn't seem all that relevant to what I was doing,

**Dave Jones:** really, or they wouldn't be serious. I could overcome them easily or something like that. So, yeah, I thought, okay, that's fine. I'll use that chip. And I didn't give it a second thought until now, until it didn't work. I checked this, downloaded the silicon errata data sheet for the

**Dave Jones:** PICchip again. And what do you know? Here it is on page six, module ICSP. I don't know if you can read that, but anyway, ICSP. Yes, it basically says the ICSP port pair number three does not, cannot be used to read or program the device.

**Dave Jones:** In other words, it doesn't bloody well work at all. And, of course, Murphy's Law, this particular PICchip, it's a 64-pin one, has three of these ICSP buses. It's really quite neat. It means that when you're laying out the board, you can choose whichever data and clock pair you want from three different ones.

**Dave Jones:** And I was intending to use number one, which doesn't have a problem at all. But very late in the design process, the layout of this thing, I thought, oh, it'd be nice if I used number three instead. And I didn't remember that when I read this, you know, a bit before, that it had a problem with number three, the ICSP bus

**Dave Jones:** number three. And I didn't recheck the silicon errata, and lo and behold, Murphy's Law says that, you know, if I'm going to pick the, you know, if I'm going to pick that particular pair, it's going to be the wrong one. And I picked number three, and number three doesn't work.

**Dave Jones:** Ah! And of course, Murphy's Law works even deeper, because there's two revisions of silicon, REV3 and REV5. And REV5, it says on here, doesn't have the problem. But of course, I've got a REV3 chip, don't I? Yeah! One of the real funny things about these silicon

**Dave Jones:** errata data sheets, in particular these microchip ones, is that they always word it as if, like, it's not a big deal, and they always have a workaround. And in this particular case, it basically says, it cannot, you know, that particular pair cannot be used to read or

**Dave Jones:** program the device. And the workaround is, well, use either the first or the second one. Well, no shit, Sherlock, thanks for that. That's not a workaround. I mean, if this thing, if Microchip were an Australian company, this thing would read something like, Ha!

**Dave Jones:** Sucked in, mate. This one doesn't work at all. This feature's rooted. Tough luck, try the other ones. So there you go. It's another warning to check the silicon errata for any device you're going to use. And keep checking it during the design process.

**Dave Jones:** You know, I just can't win with Murphy. He gets me every time. Maybe I should give up engineering and get, like, a Jim's lawnmowing franchise or something like that. Ah.
