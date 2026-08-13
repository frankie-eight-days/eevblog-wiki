---
video_id: I3FhAhxet7s
title: Rigol DHO800 Bug Testing
url: https://www.youtube.com/watch?v=I3FhAhxet7s
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 45, "3": 65, "4": 81, "5": 97, "6": 117, "7": 137, "8": 153, "9": 169, "10": 189}
---

**Dave Jones:** Hi, I'm just trying to reproduce a bug that an EEVblog forum member, Serge65536, did a video on and showed this really remarkable bug. And I'll splice it in here. It's just, like, really weird. Anyway, I'm going to try to reproduce the exact conditions that he got.

**Dave Jones:** So, basically, one meg points of memory. Roll mode is off. He deliberately specified that. And I've got the same voltage range here, if that actually matters. I've got a sine wave here. And also, he showed that the frequency was 188.1 kHz. And that's exactly

**Dave Jones:** what I've got here. 188.1 kHz. I've got one meg points of memory here. And he showed that if you slowed the time base down, and you actually got to 200 milliseconds. Okay, so let's go 100, right? And this is kind of the point

**Dave Jones:** that you'd expect it to alias. And I've showed in my review video that it does actually alias, as most scopes do. And they don't give you any warning. So I'll go to 200 milliseconds, and I don't get the display issue at all. But his one

**Dave Jones:** shows, like, all this remarkable patterning out here, which I don't know what caused that. Some sort of, you know, reconstruction algorithm or something? That's a big, because it's aliasing, it's going crazy. I don't understand it. Anyway, I can't get it. I can't reproduce it.

**Dave Jones:** Even if I slow it down even further to 500 milliseconds per division, 125 k points, I'm at 1 k samples per second, 1 meg points here. And I'm not seeing it. I tried measurements on and all sorts of things. I even tried, like, putting the trigger outside

**Dave Jones:** the window, like, outside here, so that it's not actually triggering. It's going to guarantee that it's auto-triggering here. And still nothing. So I'm not able to reproduce his issue here. And you can see, like, if I put it to, like, 100 milliseconds here

**Dave Jones:** or, like, you can really see, like, let's actually stop that and zoom in, you can really see that, you know, it ain't sinusoidal anymore, right? So, yeah, we're approaching the, you know, where it's going to, where you guarantee that it's going to start aliasing.

**Dave Jones:** And here's one, although his one's an 8.0, is the 8.0 model. So his is the 70 megahertz, mine is the 100, but there shouldn't be any difference. And he said firmware 1.00. I've got firmware 1.00. There it is there. So, yeah, I can't reproduce it.

**Dave Jones:** But anyway, I will start an EEVblog, it was suggested, that I start an EEVblog forum thread for any issues found on the 800-900 series model. So I'll start that thread and include this video here. But yeah, anyway, I couldn't find that. So that one's

**Dave Jones:** really weird. Please leave it in the comments or over on the EEVblog forum if you're able to reproduce this. Because I'm pretty sure I've got the exact same configuration that he's got, but it's just not doing it. So anyway, weird. Catch you next time.
