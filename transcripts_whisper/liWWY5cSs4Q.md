---
video_id: liWWY5cSs4Q
title: Microchip - Atmel Collaboration
url: https://www.youtube.com/watch?v=liWWY5cSs4Q
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 40, "3": 55, "4": 75, "5": 95, "6": 115, "7": 130, "8": 145, "9": 165, "10": 185, "11": 205}
---

**Dave Jones:** Hi, just a quick behind-the-scenes video, because quite a few people asked how I did the microchip Atmel April Fools video. And quite a lot of people guessed it, of course. It's pretty easy, so here it is. Yes, I did have something plugged into the back, which you didn't see.

**Dave Jones:** There's an extra USB cable headed off to, you guessed it, a PicKit 3. But no, it's not connected to a different board, it is actually connected to the microcalc here, just like in my triple 5 timer video. What you didn't see are a few wires there.

**Dave Jones:** There we go, headed out the back through my anti-static mat, of course, and over to, ta-da, there it is. There's the culprit, there's a real PicKit 3, of course, dead easy, just like the triple 5 timer. But, aha! A lot of people said, how did I do the LED on there?

**Dave Jones:** This thing was, you know, flickering. Did I actually have modify the real firmware in there? Nah, of course not. Not going to go to that amount of trouble, bugger that. Same thing, when you're on a winner, stick with it. There we go, we've got some wires going under there, and because that lead is driven

**Dave Jones:** by, you know, essentially an open collector output from the microcontroller there, just used a resistor on the back, shorted it out, and the wires come out, front of the mat here. So what you didn't see is me operating this behind the scenes while I was

**Dave Jones:** syncing, while I was using the mouse button with one hand, I was secretly just joining a couple of wires there, and there's the LED going there. Because all I'm doing is shorting out that, well, pulling that resistor low, it's connected to the 5 volt rail on one end, and you just pull it low with the series resistor

**Dave Jones:** on the other end, so you can't harm the AVR dragon at all. And well, that's all there is to it. And you may have actually caught this in the video slightly. You may be wondering, well, how can I wire just the picket 3

**Dave Jones:** in parallel with that micro, and also have the pins from here doing it? Well, I don't know if there's a buffer on there or not that could be disabled or something like that. So I didn't bother doing that. So what it is, is you may have noticed that

**Dave Jones:** in the video, some of these wires have a bit more wobble on them. Well, look, they've just fallen out there, because they're actually had the pins removed from them. So they weren't actually making contact down on that board. Pretty basic. I wasn't actually going to do an April Fool's video.

**Dave Jones:** I had actually given up, because I went on a 7-day holiday just before. And yeah, I was trying, I wanted to do something a bit more elaborate, but I just ran out of time to do it really. So, but yes, I was actually just going to completely forget about it for this year, which maybe

**Dave Jones:** would have made next year's one better. But anyway, at the last minute I decided, oh yeah, I'll do something like this. And I put it together within like the hour of uploading the thing just in time. I did it, I raced to the lab, did it just in time, and it worked a treat, fooled a few people.

**Dave Jones:** So there you go. Catch you next time.
