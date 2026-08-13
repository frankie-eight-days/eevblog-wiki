---
video_id: cBNOxg8Px8M
title: Playing with short current pulses on multimeters
url: https://www.youtube.com/watch?v=cBNOxg8Px8M
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 43, "3": 58, "4": 76, "5": 90, "6": 114, "7": 132, "8": 152, "9": 169, "10": 183, "11": 204, "12": 220, "13": 240, "14": 263, "15": 288, "16": 313, "17": 330, "18": 343, "19": 360}
---

**Dave Jones:** Hi, this is just a quick video just comparing some meters here based on a discussion on the EEVblog forum. We've got the BM235, the Keysight U1272A, the BM869. We've got the new $150 class meter which I've ordered, and we've got this mystery meter over here as well,

**Dave Jones:** which actually performs in this particular test the same as the 121. I just didn't want to put too many meters in series here. Anyway, what we're doing is we're putting in a... we've got a 60 Hz repetitive square wave here with a pulse width of 5 milliseconds.

**Dave Jones:** And we can shorten this, but let's just use 5 milliseconds here. And we've got a 50 ohm source, and I'm just driving them all in series. I've got fixed current ranges on all of them, so they don't auto-range. Now, watch this. This is the interesting bit.

**Dave Jones:** When I disconnect this, and there's obviously no current. You know, the current instantly stops. Oh, by the way, we've got 5 volts peak-to-peak there. So, you know, we're putting in a very short pulse into these things. So this is a, like, not something you'd ordinarily measure with a multimeter,

**Dave Jones:** like very short pulses like this. Ordinarily, something like this, you'd get like a peak, you know, capture, like, you know, something like that. But multimeters, you'd use a scope. Multimeters aren't really designed for this. But it's just an interesting thing. So I'm going to compare them all.

**Dave Jones:** I'm simply going to disconnect it and watch all the readings. Only one of them will instantly go to zero. Check it out. The new $150 class meter. The BM-235, it sort of went, it got there reasonably quickly, but not instantly. And you'll see that there's this residual countdown.

**Dave Jones:** This key side is still going. It's still got these residual values. So this is something to do with the true RMS converter inside these things. That, you know, some sort of, like, residual offset settling, you know, capacitor storage charge thing. Something's going on.

**Dave Jones:** The key side is still measuring an offset there, which is just, like, crazy. I don't know what's actually going on there. So, but yeah, there it, let's put it back to AC. Is that still there? It's still there. There's a residual offset there.

**Dave Jones:** That is bizarre. Anyway, let me put it back in and we'll see them ramp up. And you'll notice that the BM-869 sort of, like, takes quite some time to settle. It gets, you know, close pretty quickly. But yeah, like, it's still mucking around.

**Dave Jones:** You know, it's only just sort of decided to settle now. And yes, the BM-235 is going to read a bit lower because this doesn't quite have the bandwidth and the proper true RMS converter chip that the other meters have. So yeah, that's interesting, huh?

**Dave Jones:** Look at that. It goes, new $150 class meter goes instantly to zero. I'll be selling this one soon, hopefully. I've ordered them, but anyway. Yeah, but yep, the Keysight and the BM-235 say, oh well. No, you could say that the, and the 121 performs near identically to this meter here.

**Dave Jones:** So, and, well, there we go. That's interesting, isn't it? That one just jumps instantly. Hang on, let me have a look. I've only got one set of eyes. Whoa, it just goes to that, you know, within two sample periods it gets smacked to that

**Dave Jones:** and then just stays there. The others are still sort of, you know, the BM-869 seems to be the worst in that regard. Anyway, I just thought that was interesting. So let's actually go down to one millisecond. And as we get shorter, these meters just have a hard time reading these ridiculously short pulses.

**Dave Jones:** The BM-235 is going to do the worst, like 500 microseconds, for example. Yep. And let's go down to 100 microseconds. Well, actually, I know that 200 microseconds is where they, this one and the 121 starts to fall off, or around about 150 microseconds or something like that.

**Dave Jones:** So, you know, if you go down to 100 microseconds, yeah, the BM-235 has dropped off, the 121 and this new-ish meter has fallen off as well. Has that gone down a little bit? Anyway, if we go down to, so that's 100 microseconds. If we go down to 50 microseconds, then it turns out that actually,

**Dave Jones:** if you go down to 30 microseconds, the new $150 class meter actually holds up better than the BM-869, which has a much higher bandwidth, by the way. It's 100 kilohertz true RMS bandwidth. Don't know what the, like, bandwidth is. Well, that's the bandwidth for the true RMS converter.

**Dave Jones:** This one's much lower, if I recall correctly. It's like 8 to 10 kilohertz, something like that. But on these short pulses, it seems to hold up better. The Keysight actually does the best. I haven't actually gone below this. I think they're all just going to, yeah.

**Dave Jones:** But the Keysight, yeah, Keysight looks to be doing the best there in holding up. But once again, this is not a realistic test. It's not a realistic thing. It's just an interesting tidbit. Let's go down to 10 microseconds there. Whoa, there you go.

**Dave Jones:** Interesting, huh? So let's go back up to 5 milli. But I just thought that was interesting when you pull that out. Some of them do take quite some time to settle back down. What if I actually put it up like that, take it out,

**Dave Jones:** and then plug it back in like that? Whoa, no, it gets it, no. Anyway, there you go. Leave your comments down below. Catch you next time.
