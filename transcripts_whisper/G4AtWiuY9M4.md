---
video_id: G4AtWiuY9M4
title: EEVblog 1053 - Part 2 : IBM PC Jr Troubleshooting
url: https://www.youtube.com/watch?v=G4AtWiuY9M4
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 48, "3": 70, "4": 87, "5": 108, "6": 120, "7": 142, "8": 161, "9": 180, "10": 219, "11": 247, "12": 268, "13": 283, "14": 300, "15": 319, "16": 341, "17": 369, "18": 399, "19": 425}
---

**Dave Jones:** Alright, let's see if this bad boy still works after, what, 34 years or something? They're generally pretty reliable. Most of these old PCs still work unless they're, you know, something physically has been damaged in them. So, I've got a little composite to HDMI adapter.

**Dave Jones:** So, let's, yeah, 110 volt transformer, let's flick the red switch. Hey, fan noise. There's no magic smoke escaping. Don't see anything yet. Whey! Floppy's seeking? That's good, because the floppy wouldn't seek like that unless the processor was doing its business, but zippity-doo-dah on the screen.

**Dave Jones:** Um, and I think we heard a beep there, didn't we? Hmm. Hmm. Plug in the cartridge. Hmm. Nope. Did something, made it do something. The processor's definitely working. Some issue with the screen. I'll get back to you. Unfortunately, I think we do have a dud just measuring the composite video output here,

**Dave Jones:** and I'm getting zippity-doo-dah. That little bit of information down there is just some ground digital stuff. Don't worry about that, but yeah, there's no video signal on the output. So what we're going to have to do is actually strip this thing right back,

**Dave Jones:** because otherwise it's just too hard to get in there and probe everything, and we'll have just a quick look. I mean, I've stripped it out. I've just got the power supply board. I've disconnected the floppy, the floppy controller, the modem card, and the spare RAM expansion card, and just got the main board out.

**Dave Jones:** I don't think it's got any LEDs on it, does it? Anyway, let's switch it on. One of the good things about this is we should be able to just troubleshoot this on the bench. And, you know, when you're looking for... Oh, hello? Yeah, the beep was...

**Dave Jones:** it beeped. Two beeps. Is that like error beeps or something? Let me get in here and... Now, well, let's just double-check the video. It was... hello? Hello? That is composite video, if I ever saw it. Look at that. That's a bobby dazzler. We have video.

**Dave Jones:** So what was... what was causing the problem? Um, I will just... maybe just plug in the cards one by one again and see what happens. Alright, let's try that again. I hooked up the keyboard and the power supply board. Alright, let's try that again.

**Dave Jones:** I hooked up the keyboard and the monitor with my HDMI converter. Let's give it a go. We definitely saw a video signal there. Whereas we weren't seeing that last time. So... Oh, come on. Oh, no, one beep. There's only one beep this time, but still no video.

**Dave Jones:** Oh, what's going on? Do we still have... Ah, no. Well, the video... it's killed. The video signal is... dead. Look at this. So if I disconnect that... Ah, come on. No, video signal dead. Let's power it on again. Ah, is it the keyboard?

**Dave Jones:** The keyboard. Let's power it off again. Yep. Yep. Keyboard. Damn. Alright, so let's... finally, keyboard disconnected. Boot it up. And hopefully we'll see a signal. Come on. Oh, jeez. And in case you're wondering, no, the batteries in the keyboard actually don't make a difference.

**Dave Jones:** And this is the worst designed battery compartment I've ever seen. It's ridiculous. You have to put one side in first and the rails in there. Ah. Winner, winner, chicken dinner. Check it out. Oh, it was the... HDMI connect cable wasn't plugged in hard enough.

**Dave Jones:** It was one of those tight fits and I thought it was all the way in. Nah. Jam it a bit more. And, ta-da! IBM with its color. Look at it. Fantastic. What is it? You know, 16 color palette on this thing. 64K era B.

**Dave Jones:** Yeah, I can't type anything because there's no bloody keyboard. But watch this. We're going to try the original IBM cartridge basic. Let's just plug it in. It should be like hot swap and it should just reboot and boot from the cartridge. There we go.

**Dave Jones:** 4 kilobytes. 64 kilobyte error. No. No. Same crap. Bugger. Anyway, but you can see that it does actually detect the cartridges and it actually reboots. So that's actually quite neat. That's better than a lot of computers of the day you had to dick around like repower and all that sort of stuff.

**Dave Jones:** This one you can just hot swap. That's quite nice. Okay, let's fully populate this puppy. Got the floppy controller, the extra 64K RAM card. Let's power it on. And 4K. 64. Should jump up to 128. Error B. You can see the drive head seek there.

**Dave Jones:** There you go. Beautiful. Yeah, now what? I guess it really doesn't like the keyboard, does it? What I'm going to do is try plugging in that keyboard live. Is that the correct one? Whoa. Oh, psychedelic, man. Whoa. That just, like, killed it. Oh, back to blackout.

**Dave Jones:** There we go. We're back. Wow. Plugging in the keyboard kills the video. Is that, like, the architecture thing in here playing silly buggers? This is just ridiculous. Alright, I've got my newfangled wireless keyboard. Infrared wireless. Let's power it up. And plugged in the infrared receiver module here.

**Dave Jones:** Let's see if we can get it to B. I don't know. Escape. Nup. Nup. One more time with our 500k RAM expansion. Let's see if it does it. Yeah, it doesn't need that external power rubbish, by the looks of it. Let's see if she goes all the way with LBJ.

**Dave Jones:** Yes! Oh, look at this bad boy. Wow. It's going to go to 640k. Nobody, and I mean nobody, will ever need more than 640k.
