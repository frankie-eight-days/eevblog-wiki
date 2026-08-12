---
video_id: ru7pjXorejE
title: EEVblog #459 - Counter Shenanigans
url: https://www.youtube.com/watch?v=ru7pjXorejE
source: youtube-asr
timestamps: {"0": 1, "1": 22, "2": 34, "3": 46, "4": 59, "5": 73, "6": 84, "7": 91, "8": 114, "9": 126, "10": 147, "11": 161, "12": 186, "13": 200, "14": 213, "15": 228, "16": 254, "17": 265, "18": 292, "19": 308, "20": 331, "21": 346, "22": 361, "23": 375, "24": 388, "25": 409, "26": 420, "27": 433, "28": 458, "29": 481, "30": 489, "31": 500, "32": 522, "33": 533, "34": 543}
---

**Dave Jones:** Hi. Yes, it's just another quick video on this rubidium standard and frequency counter because Nitro 2001 on the uh 4EV Blog forum, a user on there asked, "What happens if we feed the rubidium reference external input up the frequency counter's own clacker?" Well, that's exactly what I got.

**Dave Jones:** Would it read precisely 10? Well, tada! Let's try it. Yes, it does. All I'm doing is feeding the 10 MHz uh output of my rubidium standard into the external input.

**Dave Jones:** You can see it says external reference there, and I've set it to um 12-digit mode. And yes, it is absolutely bang on. And as I mentioned in the uh forum post, it doesn't have to be a rubidium.

**Dave Jones:** So, let's try a few variations of this. It doesn't matter what frequency you put in there. It assumes uh in in the external reference, it assumes that it's precisely a 10 MHz reference.

**Dave Jones:** So, that's why we're reading precisely 10. And um you also want to know what happens if we add some extra coax on here. I don't have a huge amount of coax, but I'll add a little bit more just to add a little bit of delay from the external input.

**Dave Jones:** As you can see, I've got one here. It's maybe a meter long, and it doesn't matter a rat's bum. And what I've done here is added another uh meter on there.

**Dave Jones:** So, we've got about 2 m of uh coax there. And uh because I've got it set to 12-digit mode, the gate time is I don't exactly know how long it is.

**Dave Jones:** I'm timing it now. It's been uh 22 seconds already, and uh still hasn't done it. But we'll come back when it's uh done and see what we get. And I mentioned on the forum that you could be possibly plus minus one uh least significant digit out there depending on how the counter's designed, how all things are clocked, and uh stuff like that.

**Dave Jones:** I mean, I won't go into um architectures of various modes of how frequency counter work works right here, but come on, 50 seconds. Hey, there we go. Bang on.

**Dave Jones:** 10 MHz, not a problem. So, instead of the uh rubidium standard, what I'm going to be a bit cheeky and I'm going to feed the output of the internal oscillator in here, that crappy 10 MHz stock oscillator, to the external reference input and to the input of this.

**Dave Jones:** So, it really is feeding up its own clacker right about now. So, let me plug that in and uh see what we get because we should read always precisely 10.

**Dave Jones:** Let's uh wait for that to redo it. We'll just go back in there and we'll select the that and we'll go back in and it'll reset and we should find it'll still be 10, even though that frequency is not spot on 10 MHz because it just the counter assumes it is precisely, absolutely, without question, 10 MHz.

**Dave Jones:** And bang, there it is, folks. Spot on, precisely 10, even though it comes directly from the output here and from the internal counter itself. So, it's feeding itself. And no, look, there's no no funny business going on there, folks.

**Dave Jones:** It really is looping back and feeding itself. There's the output there, the 10 MHz crappy internal oscillator output going to the external reference in there and uh to the input.

**Dave Jones:** Not a problem. And while we're at it, just for a bit of fun, I thought I'd just uh calibrate my older Philips frequency counter here, too. And because it's got the oven oscillator, you've seen this in the teardown before.

**Dave Jones:** It's the PM 9690 um 01. It's an ovenized oscillator. It's pretty schmick and as you can see I'm not sure why the waveform out looks like that out of this thing but uh it's not the greatest um but it does have the adjustment part on here so let's it should be much finer adjustment of course than the other one.

**Dave Jones:** See if I turn it I'm turning multiple this one looks like it has actually a proper trim pot in it. It feels like it has a a proper trim pot.

**Dave Jones:** Of course I've let this warm up of course very important when you're doing this sort of stuff although it you know it is oven ovenized um you still have to let it warm up and if I keep dialing the other way it goes back but yeah much finer adjustment range than we were getting last time and it's really you know we're practically bang on there.

**Dave Jones:** I mean there's no movement in that waveform at all. You know there's going to be some there's going to be a little bit of drift in there but uh can't really see it so it's pretty darn spot on.

**Dave Jones:** And for you fans of the Lissajous pattern there it is. You can see some see a slight bit of movement on that of course. You can see it closing in and if we switch back to uh the um regular time mode probably be able to see that drift in there as well.

**Dave Jones:** Yeah very slight. I can just see that tiny little drift in there. Give it one last tweak. Tada. All right what I've got now is no rubidium at all just using the internal oscillator not using the not connected to the external.

**Dave Jones:** you see there's no external uh signal there. So, just the internal oscillator out, the crappy one, into upper tone orifice. There it is, and yeah, it's going to be almost spot on 10.

**Dave Jones:** It's at plus minus one digit I was telling you about, and of course we can go in there and uh increase uh the digits on that. So, let's uh it's bloody weird operation this.

**Dave Jones:** So, let's give that say eight digits and go back. There we go. Bang on 10. So, only at that lower one uh that lower uh count is it actually a problem.

**Dave Jones:** So, I mean, if we go right down to something like three, that's pretty silly. Ah, there we go. 10.00. So, maybe like it maybe that would had a sweet spot there that uh bloody hell, how do I do this again?

**Dave Jones:** Weird. So, let's go up to four. Let's Let's try them all, shall we? There we go. Bang on. Let's try it again. Five. We're bang on again. Is it going to make a fool fool out of us?

**Dave Jones:** Let's uh try that. Six digits. And No, we're bang on. So, we were getting that one one least significant digit uh flip flopping before. I think we were on seven, weren't we?

**Dave Jones:** We were one more than that. So, let's have a look at that. Let's try more. No. Eight digits and uh we're bang on again. Not a problem. So, we were getting the uh one bit uh flip flopping before, but now we're not.

**Dave Jones:** It's bang on. Gate time will take a few seconds for that. Maybe 10, I don't know. Come on. Here we go. Bang on. So, maybe if we actually put that back to auto, for example, hang on.

**Dave Jones:** How do we digits? We want Let's put it on auto, shall we? Let's try that. There we go. And we get a bit of flip-flopping there on auto mode.

**Dave Jones:** But, we don't get that on the fixed uh number of digits instead of the fixed uh gate time. And let's actually set the gate time to some oddball value.

**Dave Jones:** I don't know, 0.914 seconds or something like that. Let's give that a go. See what happens. Nope. We are bang on. So, thanks Nitro 2001. I hope that answered your question of what happens when a frequency counter reads its own reference clock.

**Dave Jones:** Not a problem. It's bang on. Worst case, plus minus one least significant digit. If you want to discuss this, jump on over to the EEVblog forum. That's the place to do it.

**Dave Jones:** I won't promise there'll be no more videos on this, but you never know. Catch you next time. Oh, by the way, I found the schematics for this thing on the Agilent website.

**Dave Jones:** Yes, you can just download them. So, the link will be down below. Check it out if you want to see the schematics for this puppy.
