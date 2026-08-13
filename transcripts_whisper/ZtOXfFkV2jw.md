---
video_id: ZtOXfFkV2jw
title: LCD Bias Experiment!
url: https://www.youtube.com/watch?v=ZtOXfFkV2jw
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 31, "3": 62, "4": 80, "5": 98, "6": 117, "7": 145, "8": 166, "9": 185}
---

**Dave Jones:** Hi, just a quick video. This is going to be an experiment, because somebody asked, the previous video I did on this LCD that I just released, somebody asked, well, what happens if you do leave the DC, if you do have the DC bias on the LCD?

**Dave Jones:** What actually happens to it? How long does it take to actually kill it? And I thought that's an interesting question. So I'm going to run an experiment to find out, like a long-term experiment. So what I've done here is I've taken the exact same thing before.

**Dave Jones:** It's the same wiring except the common pin now, the common pin is actually going down to ground. So instead of going, being driven, alternate phase, like I explained in the previous video, I'll link it in if you haven't seen it, I'm going to drive it like common ground, so we're simply driving each segment, it's not 100 Hz driven anymore, it's not frequency driven at all,

**Dave Jones:** it's simply turning a segment on, off. So I've got it counting up from 0 to 9, and it's simply the Arduino outputs here are simply outputting a 1. That's it. So obviously we're going to introduce, we're going to have a long-term DC bias on this LCD.

**Dave Jones:** So I thought I'd just whack it in the corner here, leave it running 24-7, and see what eventually happens to it. Will it fade out? Will the liquid crystals in there, I don't know, harden up or do whatever and they just won't switch on anymore, or they'll stay on or they'll stay off?

**Dave Jones:** Or will it, yeah, eventually fade? I don't know. We'll try it, who knows, it could last forever. That'd be kind of embarrassing, wouldn't it? But no, the experts, the manufacturers, the experts in the industry all tell you the correct way to drive them is not to have a DC bias on there, because that will eventually ruin them.

**Dave Jones:** But off the top of my head, I don't know how long that actually takes, so this will be an interesting experiment, we'll find out. I'll just keep this running, it'll just keep counting up, and I'll keep you posted. Hmm, interesting. By the way, if I take that out and plug it into 5 volts, hang on, I can see, heh, it's now inverse.

**Dave Jones:** There we go, because, there you go. And the good thing is, look, if, well, no, hang on, plug it back into ground, there we go, we're counting up. If I disconnect ground, still works. It still works, but, yeah, see, it's starting to fade there a little bit, there you go.

**Dave Jones:** It's a little bit dodgy, that's just the capacitance of the charge build-up on the capacitive segments on the LCD and stuff like that, so if you wave your hand over it far across the room, it'll change. All that sort of stuff. So there you go, I'm going to plug that back in, if I can damn well see this, the black connectors.

**Dave Jones:** There you go, I'm just going to leave it in the corner, keep you posted. I should have put a webcam on it 24-7, the world's most boring webcam. Catch you next time.
