---
video_id: OxlCoKN4W7c
title: EEVblog #153 - YouScope Demo on a Digital Scope
url: https://www.youtube.com/watch?v=OxlCoKN4W7c
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 39, "3": 60, "4": 81, "5": 96, "6": 117, "7": 129, "8": 157, "9": 174, "10": 193, "11": 213, "12": 226, "13": 245, "14": 256, "15": 275, "16": 297, "17": 310, "18": 334, "19": 351, "20": 366, "21": 378}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, no I'm not in the lab today, I'm in the lounge room. Why? Because I've got my old analog, Haymeg analog oscilloscope hooked up

**Dave Jones:** to my desktop computer. As you can see, there's the probes up there. They're connected to the sound card output signal from the desktop, which is actually my media center. It sits in the cabinet behind there, and I'm running the famous U-scope demo, which gets some pretty funky

**Dave Jones:** displays on here. As you can see, it's got scrolling text and really funky images. Check this out. There it goes. Unbelievable. And you can get this on an analog oscilloscope. Now, this U-scope demo, it's not new. It was developed by a 15-year-old kid, I believe, as part of an

**Dave Jones:** assembly language programming contest in 2007. And everyone has played with this before. It's really fun. I highly recommend you download it. What it is, is a sound file. It's just a wave file that generates waveforms on the left and right channel of your audio card, and they're

**Dave Jones:** fed into your oscilloscope into the X-Y mode. And as you'll know, so left channel into X, Y into right, or so forth. And as you can see, you can generate text and scrolling images and all sorts of, you know, rotational cubes and really funky display in X-Y mode.

**Dave Jones:** And if you don't know how X-Y mode works, basically the X input controls... the voltage on the X input controls where the dot is on the screen across the X-axis. And likewise, the Y input down here, the voltage on that, controls the dot in the Y-axis.

**Dave Jones:** So there is no time base anymore. It is a direct correlation. If I take out the input signal here, as you can see, it's just a dot on the display like that. And if I plug in the X and Y inputs, as you can see, away it goes.

**Dave Jones:** And it generates the image based on that. Now, it's really funky because it doesn't... there is no way to blank that signal, okay? Normally some oscilloscopes have a Z-axis input, and that will actually turn off the dot for a brief period. So you can move the dot around, you can draw lines like a vector-based display,

**Dave Jones:** but then you can turn it off. But this uScope demo is great because it doesn't use that. So hence, if I turn up the brightness here, you can see the lines that are used to actually draw it. So you've really got to get your intensity just right, so that you don't see those

**Dave Jones:** flyback lines. All you see is the actual animation. Now, there's nothing new here, but I thought that I'd try and get this working on a digital scope and see what happens. So let's give it a go! And the reason I'm using my desktop computer here is that you really need a good quality

**Dave Jones:** sound card with a line out. I found it doesn't really work on the headphone outputs, which is all my notebook computer's got, so... And here you go! As you can see, it works! And which isn't really surprising, given that this is 50,000 waveform updates per second on this Agilent scope.

**Dave Jones:** You can actually quite clearly see it, but it actually works too good, because you can see all the flyback lines. Now, if I vary the intensity, if I drop it down, you can still see the flyback lines on there, which is quite annoying.

**Dave Jones:** I can turn it all the way up, of course, and get maximum intensity, and... But you can still see those flyback lines, and it, you know, it really is a little bit, uh, really is a little bit annoying. So you can't really get rid of that.

**Dave Jones:** It's too good. You can't sort of drop the intensity right down, and see, that's like zero, you know, that's with the intensity right down. I can see the display quite nicely, but you can still see the flyback lines, and I want to get rid of those.

**Dave Jones:** So let's see what we can do. So here's a little trick we can use to get rid of that display. Now, what I'm going to do is, I'm going to turn on the, uh, infinite persistence. So I'll go into persistence mode, and turn on infinite

**Dave Jones:** persistence, and, okay, what I'm going to do is, I'm going to let that fill up the display. There we go, it's filled up the entire background display with that color there. Now, as you can see, we're left with, uh, if we turn it back down to scale, we're left with the, uh, the actual image

**Dave Jones:** we can see quite well. But what happens is, you actually get to a point where, if you change your intensity over here, okay, if you turn it all the way down, then you can still see the flyback lines on there, which is really quite annoying.

**Dave Jones:** But if you take it all the way up, there will be a point where those flyback lines disappear, and they become the same color as the background. Watch this. And bingo! There it is. It's at about 84 or 85 percent intensity for this particular

**Dave Jones:** scope and setup, and if I turn it past that, as you can see, you know, the flyback lines become completely, uh, completely visible, and they're hopeless. But it reaches a point where it goes from that negative to the positive, and it matches. And I think that's about 84 percent, so I'm going

**Dave Jones:** to leave it at that, and bingo! We've got our nice uScope display on a digital scope. I love it! And I know what you're thinking, what does it look like on the Rigol, on a, like, less than sub-1000 waveform updates per second scope?

**Dave Jones:** As you can see, it's pretty darn crap, and there's not much you can do about it, uh, at all. It just, it just can't cut it. You can kind of, sort of, there's that animation display on there, it just really can't do it.

**Dave Jones:** It's hopeless. So that's no good. Let's watch the full version of the uScope demo on the Agilent scope. Enjoy!
