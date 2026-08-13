---
video_id: OBOgiMA89Ks
title: My Keysight 1000X Oscilloscope FAILED :-(
url: https://www.youtube.com/watch?v=OBOgiMA89Ks
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 22, "2": 38, "3": 54, "4": 78, "5": 98, "6": 122, "7": 142, "8": 162, "9": 190, "10": 210, "11": 230, "12": 246, "13": 274, "14": 298, "15": 314, "16": 334, "17": 354}
---

**Dave Jones:** Hi, I just thought I'd show you something with my Keysight 1000x scope here. Check this out. User calibration failed. Because I had an issue with the DC offset on this thing, and, like, the firmware was way behind, and I thought, oh, OK, I'll, like, do the user calibration, which takes about 7 minutes.

**Dave Jones:** It's very comprehensive, it generates, like, its own internal test signals and it, like, you know, it calibrates, like, the channel offset, the channel gain, and all sorts of weird and wonderful stuff. So, you know, it really is fantastic, but I ran the user calibration,

**Dave Jones:** you're supposed to disconnect all the inputs, which is what I did, I ran the user calibration, and it failed. So I don't know what's going on. Let's see if the issue was here. I just wanted to show you that error message. What I was seeing is that when I changed

**Dave Jones:** the time base here, let's go down, look, look, the offset, look at that, it's jumped, like, 600 millivolts, like that, and then it jumps back. So on those two ranges, on the 200 millivolt and 500 millivolt ranges, there's this huge DC offset, it still works, but there's this, the channel still works, but there's this massive

**Dave Jones:** DC offset. All the other ranges are fine. So has this scope, like, failed on its 200 millivolt and 500 millivolt ranges? I don't know. Let's turn on channel 2 here, and let's see if this does the same thing. Okay, oh, yep, 50 volt range.

**Dave Jones:** Has an offset, look at that, compared to the ground. Let's see if it's, oh, 500, 200, 100 millivolts, exactly the same on both channel 1 and channel 2. So what the hell's going on there? I've got another older 1000x prototype scope, I'm going to update the firmware on that, well, no, I'll just

**Dave Jones:** go get that and show you. Alright, so this is my prototype unit, PP stands for production prototype, I believe, it was the 70th unit, so this is one I've done, like, hacking around on and stuff, so yeah, it's got unreleased firmware, there was an error message, like a warning message when I booted it up, this is unreleased firmware,

**Dave Jones:** so I haven't updated this firmware, let me try this. Nah, see, that one's a win-a-win, a chicken dinner. But the other one has a real issue, so I'm not sure if there's a hardware fail, I'll try the user calibration again, whoa, I just repowered

**Dave Jones:** it up, system concerns detected, instrument is uncalibrated, yeah, because it failed the calibration, like, the user cal, okay, wonderful, anyway, let's feed in a, so let's feed that right in the middle, whoa, look at that, 5 volts and 10 volts per division, wow, look at that, that's

**Dave Jones:** seriously, that is, that's failed big time. Yeah, 2 volts, yeah, and here we go, you can see that DC offset, shift like that, the waveforms, like, you know, it works, but it's completely shifted, so yeah, this is one sick puppy, I don't know what's wrong with it.

**Dave Jones:** Alright, so let's just run that calibration again, you've actually got to go into options here, auxiliary and cal protect, so you've got to disable the calibration protection, and then you've got to go into service here, and then start user calibration, and boom, there

**Dave Jones:** it goes, take approximately 7 minutes, you can see it, like, generating all sorts of stuff like this, I'm not sure if that is a normal signal that it's supposed to generate, but I don't know, I guess I'd have to compare it with my other 1000x

**Dave Jones:** to see what, what's what, but anyway, I'll let you know, but I don't expect it to just magically pass again. Something wrong with this. And surprise surprise, it failed again. And the interesting thing of course, is that it happens on both channels. There it is, sure we're not triggering off

**Dave Jones:** channel 2 there, source 2, there we go. But, like, they're both got both channels have that DC offset on the 500mV and the 200mV ranges. Like, that's just nuts. Why? Both channels, so it's not like a physical hardware fail on a channel, they're

**Dave Jones:** two independent channels, so I just I'm not getting it. Leave your thoughts in the comments down below. If you've seen this issue, if you've heard about it let me know, because yeah, this one's a loser. Which is a shame, because this is one of my favorite scopes in the lab.

**Dave Jones:** I love my little 1000x, you know, so nice to, you know, it's small compact, it's ridiculously easy to use, it's one of the you know, it's probably the friendliest scope to use that I've got in the lab. If I just want to make some simple measurements, I usually reach for my

**Dave Jones:** Keysight scope. It just works, except in this case I guess it doesn't. Yeah, so Houston, we have a problem. Hmm. And also I love the glare, you know, there's not much glare on this screen compared to some of my other scopes. So for video work, it's actually quite nice.

**Dave Jones:** But, anyway, let me know what you think. Catch you next time.
