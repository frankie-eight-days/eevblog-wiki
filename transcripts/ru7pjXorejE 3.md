---
video_id: ru7pjXorejE
title: EEVblog #459 - Counter Shenanigans
url: https://www.youtube.com/watch?v=ru7pjXorejE
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 35, "3": 51, "4": 67, "5": 76, "6": 89, "7": 102, "8": 116, "9": 133, "10": 152, "11": 171, "12": 188, "13": 203, "14": 221, "15": 241, "16": 256, "17": 272, "18": 287, "19": 302, "20": 318, "21": 338, "22": 354, "23": 372, "24": 391, "25": 409, "26": 422, "27": 440, "28": 466, "29": 483, "30": 499, "31": 511, "32": 527, "33": 540}
---

**Dave Jones:** Hi. Yes, it's just another quick video on this rubidium standard and frequency counter because Nitro 2001 on the uh 4EV Blog forum, a user on there asked, "What happens if we feed the rubidium reference external input up the

**Dave Jones:** frequency counter's own clacker?" Well, that's exactly what I got. Would it read precisely 10? Well, tada! Let's try it. Yes, it does. All I'm doing is feeding the 10 MHz uh output of my rubidium standard into the external input. You

**Dave Jones:** can see it says external reference there, and I've set it to um 12-digit mode. And yes, it is absolutely bang on. And as I mentioned in the uh forum post, it doesn't have to be a rubidium. So, let's try a few variations of this. It

**Dave Jones:** doesn't matter what frequency you put in there. It assumes uh in in the external reference, it assumes that it's precisely a 10 MHz reference. So, that's why we're reading precisely 10. And um you also want to know what happens if we

**Dave Jones:** add some extra coax on here. I don't have a huge amount of coax, but I'll add a little bit more just to add a little bit of delay from the external input. As you can see, I've got one here. It's

**Dave Jones:** maybe a meter long, and it doesn't matter a rat's bum. And what I've done here is added another uh meter on there. So, we've got about 2 m of uh coax there. And uh because I've got it set to

**Dave Jones:** 12-digit mode, the gate time is I don't exactly know how long it is. I'm timing it now. It's been uh 22 seconds already, and uh still hasn't done it. But we'll come back when it's uh done and see what we get. And I

**Dave Jones:** mentioned on the forum that you could be possibly plus minus one uh least significant digit out there depending on how the counter's designed, how all things are clocked, and uh stuff like that. I mean, I won't go into um

**Dave Jones:** architectures of various modes of how frequency counter work works right here, but come on, 50 seconds. Hey, there we go. Bang on. 10 MHz, not a problem. So, instead of the uh rubidium standard, what I'm going to be a bit

**Dave Jones:** cheeky and I'm going to feed the output of the internal oscillator in here, that crappy 10 MHz stock oscillator, to the external reference input and to the input of this. So, it really is feeding up its own clacker right about

**Dave Jones:** now. So, let me plug that in and uh see what we get because we should read always precisely 10. Let's uh wait for that to redo it. We'll just go back in there and we'll select the that and we'll go back in and it'll

**Dave Jones:** reset and we should find it'll still be 10, even though that frequency is not spot on 10 MHz because it just the counter assumes it is precisely, absolutely, without question, 10 MHz. And bang, there it is, folks. Spot on,

**Dave Jones:** precisely 10, even though it comes directly from the output here and from the internal counter itself. So, it's feeding itself. And no, look, there's no no funny business going on there, folks. It really is looping back and feeding

**Dave Jones:** itself. There's the output there, the 10 MHz crappy internal oscillator output going to the external reference in there and uh to the input. Not a problem. And while we're at it, just for a bit of fun, I thought I'd just uh calibrate my

**Dave Jones:** older Philips frequency counter here, too. And because it's got the oven oscillator, you've seen this in the teardown before. It's the PM 9690 um 01. It's an ovenized oscillator. It's pretty schmick and as you can see I'm not sure why the waveform out looks like

**Dave Jones:** that out of this thing but uh it's not the greatest um but it does have the adjustment part on here so let's it should be much finer adjustment of course than the other one. See if I turn it I'm

**Dave Jones:** turning multiple this one looks like it has actually a proper trim pot in it. It feels like it has a a proper trim pot. Of course I've let this warm up of course very important when you're doing this

**Dave Jones:** sort of stuff although it you know it is oven ovenized um you still have to let it warm up and if I keep dialing the other way it goes back but yeah much finer adjustment range than we were getting

**Dave Jones:** last time and it's really you know we're practically bang on there. I mean there's no movement in that waveform at all. You know there's going to be some there's going to be a little bit of drift in there but uh

**Dave Jones:** can't really see it so it's pretty darn spot on. And for you fans of the Lissajous pattern there it is. You can see some see a slight bit of movement on that of course. You can see it closing in

**Dave Jones:** and if we switch back to uh the um regular time mode probably be able to see that drift in there as well. Yeah very slight. I can just see that tiny little drift in there. Give it one last tweak.

**Dave Jones:** Tada. All right what I've got now is no rubidium at all just using the internal oscillator not using the not connected to the external. you see there's no external uh signal there. So, just the internal oscillator out, the crappy one, into

**Dave Jones:** upper tone orifice. There it is, and yeah, it's going to be almost spot on 10. It's at plus minus one digit I was telling you about, and of course we can go in there and uh increase uh the digits on that.

**Dave Jones:** So, let's uh it's bloody weird operation this. So, let's give that say eight digits and go back. There we go. Bang on 10. So, only at that lower one uh that lower uh count is it actually a problem. So,

**Dave Jones:** I mean, if we go right down to something like three, that's pretty silly. Ah, there we go. 10.00. So, maybe like it maybe that would had a sweet spot there that uh bloody hell, how do I do this again?

**Dave Jones:** Weird. So, let's go up to four. Let's Let's try them all, shall we? There we go. Bang on. Let's try it again. Five. We're bang on again. Is it going to make a fool fool out of us? Let's uh

**Dave Jones:** try that. Six digits. And No, we're bang on. So, we were getting that one one least significant digit uh flip flopping before. I think we were on seven, weren't we? We were one more than that. So, let's have a look at that.

**Dave Jones:** Let's try more. No. Eight digits and uh we're bang on again. Not a problem. So, we were getting the uh one bit uh flip flopping before, but now we're not. It's bang on.

**Dave Jones:** Gate time will take a few seconds for that. Maybe 10, I don't know. Come on. Here we go. Bang on. So, maybe if we actually put that back to auto, for example, hang on. How do we digits? We want Let's

**Dave Jones:** put it on auto, shall we? Let's try that. There we go. And we get a bit of flip-flopping there on auto mode. But, we don't get that on the fixed uh number of digits instead of the fixed uh

**Dave Jones:** gate time. And let's actually set the gate time to some oddball value. I don't know, 0.914 seconds or something like that. Let's give that a go. See what happens.

**Dave Jones:** Nope. We are bang on. So, thanks Nitro 2001. I hope that answered your question of what happens when a frequency counter reads its own reference clock. Not a problem. It's bang on. Worst case, plus minus one least significant digit.

**Dave Jones:** If you want to discuss this, jump on over to the EEVblog forum. That's the place to do it. I won't promise there'll be no more videos on this, but you never know. Catch you next time. Oh, by the way, I

**Dave Jones:** found the schematics for this thing on the Agilent website. Yes, you can just download them. So, the link will be down below. Check it out if you want to see the schematics for this puppy.
