---
video_id: EVRdTY4LNhg
title: Rigol DHO800 Disappearing Waveform BUG
url: https://www.youtube.com/watch?v=EVRdTY4LNhg
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 57, "4": 81, "5": 105, "6": 125, "7": 141, "8": 165, "9": 205, "10": 221, "11": 245}
---

**Dave Jones:** Hi, just trying to reproduce another Rigol bug here. Once again from Surge65536 on the forum. Thank you very much. And he's done a video showing it. And yes, I am able to reproduce it. So what I've got here is I've got the memory set to 25 megapoints here.

**Dave Jones:** I've just got channel 1 enabled like this. And I've got it set to actually, let me turn that back to 500 milliseconds per division. We'll go single-shot capture. And we'll just go... So we get some, well, 200 millivolts per division. There we go.

**Dave Jones:** Okay, so we captured some data. Whoa! Whoa! Okay, right. So we captured some data. Okay. Not sure what it was doing there. Maybe it was just the time it took to process and update the screen. Anyway, we can make it. This is my first experimentation with it.

**Dave Jones:** And if we now change it back to, this is exactly what Surge did. Change it back to one millisecond, one second per division. And then turn the Vernier on. And... Oh, no. One second. And then turn Vernier on. And then adjust the time base like that.

**Dave Jones:** I swear I got it. I swear I did get it. Whoa, no. And then change, and then sorry, whoa. Yeah, it's taking time to update. Whoa, whoa. Okay. And then move it. Boom. Boom. Gonski. Right? Like that. Gonski. So that has something to do with the memory depth.

**Dave Jones:** If I change that back, I can't get it until it comes back. Whoa, see? If I move it either way, it disappears. So we'll call this the disappearing waveform bug. Shall we? Yeah. Once again, like, I'm able to reproduce it like that. Can do some more experimentation, but it's there.

**Dave Jones:** It's there. I'm not sure if it has to do with the Vernier or not. So let's actually, so if we turn the Vernier off, we go back to five milliseconds per division. And if we just go the way, whoa. Just move the waveform like that.

**Dave Jones:** Whoa. No, look. I don't even have to do the Vernier. Look. Look, it's gone. What? Whoa. Look at that. Look at that. I didn't even have to do the Vernier. So let's actually try that again, shall we? 500 milliseconds per division. Okay, I'll put it back in the center.

**Dave Jones:** Yeah, center. Okay, single shot capture. Okay, so we've captured, we've got our single shot capture. Okay, that's fine. If I just move it, are we going to get it? No. No. No. No, it seems okay. So is it because we've changed it? Like that?

**Dave Jones:** No. No, it looks like you do have to do, whoa. You expect this on like the really slow time base, I guess. But, come on, stop. Go back to the one second per division. Turn the Vernier, whoa, Vernier on. And it's Gonski. Yeah.

**Dave Jones:** Okay, so maybe it is a Vernier bug or something perhaps. But if we turn it back, it's still gone. Didn't it? Oh, well it did before. Anyway, yeah, weird bug. Yeah, some sort of memory allocation thing going on? I don't get it. But yeah,

**Dave Jones:** that's a confirmed bug. Thanks. Catch you next time.
