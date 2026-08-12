---
video_id: l-fuyHCs2Sw
title: Rohde & Schwarz RTB2004 Oscilloscope Acquisition Bug
url: https://www.youtube.com/watch?v=l-fuyHCs2Sw
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 32, "3": 49, "4": 69, "5": 78, "6": 83, "7": 104, "8": 107, "9": 137, "10": 164, "11": 197, "12": 212, "13": 230, "14": 254, "15": 278, "16": 303, "17": 331, "18": 347}
---

**Dave Jones:** Hi, just a quick one. I wanted to show you this Roden Schwartz RTB-2004 oscilloscope, and it is sexy as 10-bit ADC in the thing, and it's got all the bells and whistles, massive big high-res touchscreen. It looks really incredible. Anyway, I just found an issue with it.

**Dave Jones:** I was actually going to do some noise measurements across all the scopes here I have in the lab to see, you know, which one's the lowest noise and all that sort of stuff. So I was feeding it a low-level signal, and I found an issue here.

**Dave Jones:** Take a look at this thing. Now, let's have a look at the screen here, and look at this. I'm feeding in an 11 Hz signal. I was feeding in 20 before, but like 11 Hz just makes it show up a bit more. Consistently, look at this, right?

**Dave Jones:** It's a low-level signal. I don't think the amplitude matters. I can try that later, but look what's going on here. There's this weird-looking artifact, like it's almost as if it's got some-- I've got to be careful, this is touchscreen-- weird, like, memory sampling artifact or something.

**Dave Jones:** Look, that signal should not be doing that. Now, it's absolutely fine and dandy. You put it in single-shot mode and everything's fine. But when it's freaky, I don't think it's going to do that. But when it's freaky, I don't think it's going to do that.

**Dave Jones:** But when it's freaky, I don't think it's going to do that. But when it's freaky, I don't think it's going to do that. But when it's freaky, I don't think it's going to do that. But when it's free-running like this, I've actually got the trigger level-- it's not actually triggering like that.

**Dave Jones:** When it triggers, it-- but, well, it's supposed to be triggering, but it's-- look! Look at that! What's going on there? Now, this seems to be a function of the acquisition memory length. So I've got it on 1 meg at the moment. If I put it on automatic-- please forgive me, like, I've only been using the scope for five minutes, okay?

**Dave Jones:** So, like, you know, I don't know how it's all working. I don't even know how to use it. 15 meg samples, does it even display the memory depth on here? No, that's a bit of a limitation. Where's the memory depth being displayed? That should be on there somewhere, like down here in this unused section perhaps?

**Dave Jones:** Unless I'm missing it, I'm blind, I can't see where it's set the memory depth, or maybe because it's auto. Anyway, so you set it on auto and it's doing it, okay? You can see it's still got that sort of acquisition glitch. I'll call it, but you don't get that down at the low memory depths.

**Dave Jones:** Look at that, and I haven't tried them all, but I've jumped up a few, it's got to 100k, whoop, and you saw that, it just sort of like re-sampled there at a different time base, so that's kind of weird, I don't know if that's a bug, haven't actually looked at that, but we're not seeing it with that sort of memory depth.

**Dave Jones:** I've got to actually go up to, whoa, see that? See that? Wow, that was interesting, so it did, like it's not flushing the sample buffer properly and it's re-sizing it and displaying it, something weird's going on there. Anyway, I don't see it, this issue, this bug, until I get to 1 meg sample per memory, so obviously the automatic mode must be sampling at 1 meg plus, but yeah, so that, it's, look at that, that is just ridiculous.

**Dave Jones:** That's, that's crazy, there's something seriously wrong with that. Anyway, I just wanted to show you that, I've been playing around with this thing, and if we put it on the full 20 meg, whoa, see that? That was a different, it's not acquisition buffer, but why?

**Dave Jones:** It's actually almost like changing the time base there, like the playback time base kind of thing, and compressing that, I don't know. Oh, because you've changed the memory depth, okay, then it's going to show a higher frequency waveform, but yeah. That's, jeez, I don't want that.

**Dave Jones:** Anyway, I don't see that at higher frequencies, by the way, and I don't see that if I, whoop, there we go, yeah, we can still see it, still see it like that, and if I go down, oh, and that's actually supposed to be triggering off that, but it ain't, so I'm not sure what the, what the deal is there.

**Dave Jones:** I've got AC coupling, high frequency, reject. Trigger level, you know, positive slope, I've got all the usual bells and whistles happening there, so it should be doing that, but it's obviously not triggering off, oh, there we go, it's triggering now, so can I get it to, maybe it doesn't like triggering at low frequencies, and that's slow updating, you expect that based on the time base.

**Dave Jones:** Of course, it's interesting that it fills up the post-trigger first, and then comes in and displays the pre-trigger information. So, hmm, no, no, we don't get it, but if we take that trigger off, does it show up, is it going to show up, oh, come on, oh, the auto, normal, sorry, we're in auto, dull.

**Dave Jones:** Come on, come on, show up, you're going to make a fool out of me, nah, oh, we need auto, of course, to keep, oi, keep refreshing the waveform, anyway. I just wanted to show you that little bug that I found, some sort of acquisition bug, and it's got to be, surely, I'm not using this thing incorrectly, come on, I can't be, can I?

**Dave Jones:** Anyway, anyone else want to confirm, I haven't tried any other, like, frequencies, configurations, I was just happening to be using a low frequency like this, I was using 20, I think I was using 20 hertz, was it, because somebody in the EVBlog forum wanted to know about,

**Dave Jones:** oh, look at that, look at that, someone on the EVBlog forum wanted to know about, you know, noise across various oscilloscopes at different bandwidths, so, oh, sorry, at different, at low frequency like this, so I thought I'd, thought I'd try that with 20 meg bandwidth limit on, but wow, that, that, that's crazy, come on, it's got to be a bug, anyway, catch you next time.
