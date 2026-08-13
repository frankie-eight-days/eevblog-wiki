---
video_id: AVuVCrYMBwk
title: Rohde & Schwarz RTB2004 Timebase Quirk
url: https://www.youtube.com/watch?v=AVuVCrYMBwk
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 24, "2": 53, "3": 81}
---

**Dave Jones:** Hi, check this out. I love my Rodin-Schwarzer ICB2004, but there's something strange about the time base, which I don't think I've noticed before because I don't use it enough. I'm at 1 nanosecond per division here, okay? And everything's 1, 2, 5, 10. So we've got our traditional 1, 2, 5, 10 sequence, right?

**Dave Jones:** Let's see what happens when we go up. 20 nanoseconds, you'd expect 50, but you get 40. And then, well, okay, it may be 1, 2, 4, and then 100. No, you go to 80, and then 200. You can't get 100 nanoseconds. Why? And then it goes back to 5, and then the rest of the time base sequence is 1, 2, 5.

**Dave Jones:** Sequence all the way up to like 500 seconds or something. But why is it just down at the 10, at the 20, 40, 80 nanoseconds? Why is there no 100 nanoseconds per division? Strange. If you've got any idea, let me know. Something to do with the architecture and the sampling memory depth or something.

**Dave Jones:** I have no idea. Leave your answer in the comments.
