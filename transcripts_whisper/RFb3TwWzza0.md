---
video_id: RFb3TwWzza0
title: Alkaline Battery Leakage Test Setup
url: https://www.youtube.com/watch?v=RFb3TwWzza0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 38, "3": 63, "4": 81, "5": 98, "6": 113, "7": 129, "8": 146, "9": 168, "10": 188, "11": 197, "12": 221, "13": 248, "14": 267}
---

**Dave Jones:** Hi, just a quick follow-up to my main channel video about the alkaline battery discharge test electric boogaloo. I've got 13 sets of batteries here, lucky 13. I've got two of each different type that I had available. And silly me, I didn't put my thinking cap on in the previous video when I said,

**Dave Jones:** oh, I'll just use like a 10 ohm resistor on each pair, for example, and I will just discharge them for like 24 hours or something with a 10 ohm resistor. Oh, if you actually do the calculations, you can't just use like a 10 ohm quarter watt resistor.

**Dave Jones:** Oops, you need like almost like 0.9 watts or something. So I need, well, maximum. So I need, needed a whole bunch of like 1 watt 10 ohm resistors and I just don't have those in my kit. Like I've got, you know, more than enough quarter watt resistors, but I don't have in the huge volumes that I would require to like put multiple resistors in parallel to try and get a 1 watt resistor and all that sort of jazz.

**Dave Jones:** So that wasn't going to work. So I decided, bugger it, I'll just whack them all in series and discharge it with a constant current. So what I'm going to do is I'm going to discharge with a 100 milliamps for 24 hours or 86,400 seconds.

**Dave Jones:** So that means that that'll give roughly, based on say the Duracell data sheet, that'll give basically a 1 volt end voltage. So I didn't want to pull up every data sheet and some data sheets aren't available for these crap brand ones and things like that.

**Dave Jones:** Others just don't have a characteristic curve for 100 milliamp discharge. So I'm going to say, you know, they're all roughly equivalent in terms of capacity, give or take, you know, 5% or something perhaps. So there's probably not going to be, you know, a lot in it.

**Dave Jones:** So I'll take a figure of 100 milliamps for 24 hours, so 2,400 milliamp hours total will be extracted from these batteries and I'll do this twice. One of them I'll just like leave with no load and the other one I'll actually put a small load.

**Dave Jones:** I might actually leave them all in series and actually put just one 10 microamp constant current load on the whole string for storage. What do you think? Rather than having to disconnect it all and then just solder on individual resistors on each one, I think I'll just do it for the whole string.

**Dave Jones:** Anyway, so that's the plan. So I've got it hooked up to my electronic load here and I'm about to run a 24-hour test. So I've set it to 0.1 amps here, 100 milliamps. Voltage stop, I'm not going to stop on voltage, so if any of these happen to go reverse voltage or whatever, I'm just going to have to live with it.

**Dave Jones:** Okay, so I'm not worried about that. The current stop, I'm not worried about that. Sorry, capacity stop, milliamp hour stop, not going to worry about that. But the time stop, 86,400 seconds is 24 hours. The voltage on will be 0.5 volts, so that should work.

**Dave Jones:** So, I don't use this all that often. How do I run it? So I'm running the battery app. Do I just, I think I just hit on, don't I? I think that's how I started, can't remember. Anyway, let's go. Ta-da, and there it is.

**Dave Jones:** So I've got 40 volts total, and we'd expect that to drop a bit. It's drawing 976. That's a bit disappointing. Why isn't it exactly 1 amp? I want to do 1 amp constant current. Anyway, I'll just leave it at that. 0.024 watt hours, 24 seconds, I'm going to assume that is on.

**Dave Jones:** That is definitely on time stop, 24 hours. So, I'll just come back tomorrow at, it's now 3 o'clock on a Saturday, so I'll come back, hopefully if I'm available, I'll come back 3 o'clock tomorrow and just double-check that it's actually, or maybe slightly before then, and double-check that it's switched off.

**Dave Jones:** But anyway, there you go, I'm going to 1 milliamp hour extracted total. So, anyway, I'll come back, it should give us a nice total there, so I don't have to be there when it ends. It should just automatically stop after 86,400 seconds, and it should give us the total milliamp hour extracted, and the watt hours as well.

**Dave Jones:** But we don't care about the watt hours, or we care about, so we're going to suck out 2,400 milliamp hours out of these things, and we'll see what happens. So, there you go. That's it. I'll come back tomorrow. Anyway, catch you next time.
