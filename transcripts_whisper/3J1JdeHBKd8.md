---
video_id: 3J1JdeHBKd8
title: 20 Core Dual Xeon Processor Upgrade!
url: https://www.youtube.com/watch?v=3J1JdeHBKd8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 42, "3": 66, "4": 97, "5": 118, "6": 133, "7": 146, "8": 167, "9": 205, "10": 221, "11": 249, "12": 281, "13": 302, "14": 327, "15": 348, "16": 366, "17": 383, "18": 403, "19": 426, "20": 446, "21": 467, "22": 494, "23": 510, "24": 529, "25": 550, "26": 568, "27": 585, "28": 604, "29": 617, "30": 641, "31": 662, "32": 682, "33": 703, "34": 726, "35": 749, "36": 772, "37": 794}
---

**Dave Jones:** Hi, just a quick one. I'm going to do a small processor upgrade on my Dual Xeon main editing and rendering machine. I'll link in the videos down below if you haven't seen this puppy, but yeah, it uses a Supermicro motherboard, a XD9-something, AD-something or other.

**Dave Jones:** Anyway, I'll link it in down below. And we've got Dual Xeon processors, E5-2630s. And I'm going to upgrade these because I got a couple of cheap... It uses the LGA-2011 socket, I think. There we go, hopefully that's showing up. I'm going to upgrade this to the...

**Dave Jones:** so from the E5-2630 to the E5-2680. Both of them are V2s. Now the... I've got two of these. I got them cheap, so they're a drop-in replacement for the existing 2630s that I've got in here. And these have a typical bench... like a passmark benchmark

**Dave Jones:** of 10,500 or thereabouts, I think. And I think the new 2680s have about 16,500. So it's quite a significant upgrade, and I think it's worth doing. So I'll just quickly whip these out and put the processor in. Shouldn't take long at all. Now the E5-2680 V2 is not the fastest you can get in this socket 2011 that we have on this Dual Xeon motherboard here.

**Dave Jones:** But it's by far, I think, the best bang-per-buck upgrade. Well, they might be better, but they're slightly lower. So I already had a pretty fast 2630 V2 in there, but this was by far the best bang-per-buck upgrade. And I think I could take it up to 19,000 passmark or something, but it would have cost like, you know,

**Dave Jones:** 500 bucks per processor or 1,000 bucks per processor or something, you know, nuts like that. So it just wasn't worth the extra. I've already done some benchmarks on this thing before I did it, and I'll do after as well. You might notice that I don't have all the RAM populated.

**Dave Jones:** I did actually have a full 128 gig of RAM, but I've only been operating... I had that for a while, but when I was having problems with this thing, I thought it might have been memory-related problems, so I took some out, and I only left...

**Dave Jones:** ended up leaving 32 gig in there. And that is plenty, for those who are wondering, for my video editing purposes. I don't even use half of that. I typically will run... use 16 gig. I never get anywhere near the 32 gig I've got in here, let alone the 128 gig I originally have.

**Dave Jones:** Anyway, let's do the upgrade. Clean off the existing solder paste on there with some isopropyl wipes. Put some paste on there. That should do it. We've got five beeps. Oops, that's not good. No, turns out that it does work, so maybe it just needed to...

**Dave Jones:** I might need to tweak the bias, but I missed the bias, and now I'm just running a memory diagnostic. But yeah, the processors are working. We wouldn't get this if it didn't. And we're in like Flynn. Here we go. It's the X9DA7E, by the way.

**Dave Jones:** Motherboard, and we've got 32 gig of RAM, and everything's hunky-dory. CPU configuration, 2800 megahertz, 2.8 gig, that's what we want. That's what this processor is designed to run at. Hyper-threading, we want that disabled power technology, disabled energy, we want performance. Power technology, disabled energy, we want performance.

**Dave Jones:** You know, we could set that for more balanced performance, energy efficiency, whatever. Let's just go for the maximum performance. Anyway, CPU information, make sure we haven't been diddled. No, E5-2680v2 at 2.8 gig. No wuckers. Alright, let's check it out. We have the E5-2680v2, 115 TDP, the maximum power dissipation, operating power dissipation in this thing,

**Dave Jones:** up from, I think, 85 from the 2630. So, but the big thing we see, look on my CPU monitor over here, we now have 20 cores, because there's 10 cores per CPU. Physical cores, none of this virtual rubbish, as opposed to the 6 cores we had before.

**Dave Jones:** Here's a screenshot of my previous processor running its 12 cores. So hopefully, it should be much quicker for those programs, like Handbrake, for example, that I use for compression, sorry, for transcoding the videos, before I upload, then it should be much quicker. Excuse the banana, this is a banana.

**Dave Jones:** It's a very good banana. Mmm, banana. Yes, Socket 2011, LGA, everything's hunky-dory, 2.8 gig. Alright, we're cooking with gas. So, I'll just run some benchmarks and see how it compares. Alright, so what I'm going to do is, sorry you can't see this, it's off the screen here,

**Dave Jones:** but I'll just drag and drop my, I've got a test file, 50 frames per second. Here we go, here it is, the Handbrake is running. There we go, and this took 10 minutes and 57 seconds before. You can see now all the CPUs, it's using all 20 cores, practically 100%.

**Dave Jones:** It's amazing, I can screen capture in the background. In fact, I better shut down the screen capture. That's no doubt impacting the processor. Alright, I've done that test, I'll just run it again, just, this is not a genuine one, but I'll just run it to show you it running.

**Dave Jones:** Basically, it was, I was getting, as you can see up the top here before, I was getting like an average of 56 frames per second or something, and it took 11 minutes, sorry, yeah, it took almost practically 11 minutes to do that, and now it's actually 100, this screen capture's not slowing down a huge amount,

**Dave Jones:** it was actually 120 before, maybe average, now it's 112. Anyway, it only took 6 minutes and 42 seconds compared to 10 minutes and 57 seconds before. So that's like a 40% increase in speed. So that's actually better than what the PassMark benchmark, which is kind of that industry standard website benchmark,

**Dave Jones:** that would lead you to suggest. That's because we've got an extra 8 cores now, we've gone from 12 cores before to 20 cores now, and Handbrake can make use of every one of those cores, as you can see. So it's splitting up the encoding, the transcoding tasks into more cores,

**Dave Jones:** more cores, even though, I think this is, is this slightly slower processor? Is this like 2.8 gig as opposed to 2.9? I can't remember. Anyway, yes, and as for power consumption, I've got the open hardware monitor here. Yeah, it's drawing a bit more power, this is what we had before, I think.

**Dave Jones:** What was it? Yeah, like the CPU core was at 30, hang on, was it 51 watts during rendering or something? Yeah, 40 degrees, now the processor's up to 50, no. Yeah, the processor's like at 42 degrees, it's not getting warm, you know, it's not hugely hot or whatever, the idle power is just like slightly more than what I had before,

**Dave Jones:** there's really nothing in it, because these modern processors are very good, when they're doing nothing they sort of, you know, go into a, you know, they go into low power mode, and I haven't tweaked the bias to go into, like this is tweaked for performance as well, full-on performance,

**Dave Jones:** so I haven't done that, but yeah, as you can see, the CPU's near 100%, and the total package dissipation is only 70 watts at, you know, and the core's internally at like 40 degrees, whoop-dee-doo, like 42, 43, 44 maximum, so it's not much at all.

**Dave Jones:** So it's running really quite cool, the fans don't spin up in the case, the Corsair case I've got, you know, it's fantastic, it's super silent, and it's quick, that is a really good processor upgrade. And now I'll just try a, not a Sony Vegas, not Sony anymore, just a Vegas test,

**Dave Jones:** but transcoding is the big test, because it flogs all the CPUs at 100%, and I'm getting basically a 40% increase in that, under the exact same conditions, right into the same drives, no, the drives are not a bottleneck, trust me, that's almost pure CPU horsepower,

**Dave Jones:** we've just got more cores now, winner winner, chicken dinner. And I'll just run a quick render test here, and I'll render, I've just got a test project mixing 50 frames per second footage and 60 frames per second footage, just exactly 2 minutes long

**Dave Jones:** with a couple of text overlays, you know, quite typical of what I would do here, and I'm going to use the main concept one, because that'll flog the CPU, and I'm going to do 1080p, 50 frames per second, so I'll just run that, and save it to my solid state drive,

**Dave Jones:** so there's no bottleneck, yes, I wish to overwrite, and well, yeah, I'm screen capturing now, so obviously it's not going to be relevant, let me run it, shut down my screen capture, I'll come back. Okay, I've ran all the tests, I've got the numbers,

**Dave Jones:** basically Handbrake gives the best performance, because it's optimized for the multi-core application, uses all 20 cores, flogs them at near 100%, and I've got a 40% speed increase on that, so if it took 100 seconds before, it now only takes 60 seconds, which is awesome, and it's slower on Vegas,

**Dave Jones:** with Vegas rendering using the main concept codec at 12 megabits average, it was 4 minutes 25, now it's 2 minutes 55, that's about a 35% increase, which is still pretty good, but not as good as Handbrake, and then we've got the Sony codec,

**Dave Jones:** which I typically use for the 50 frames per second, that went from 5 minutes 21 to 4 minutes 12, only a 20% increase, so not that great, because for some reason, because of Vegas, it only uses half the cores, so it was only using 10 cores,

**Dave Jones:** and doesn't even use them all at 100%, so 20% is where I would have guesstimated anyway, and with the 30 frames per second XD cam, where I can render a 2 minute video in 54 seconds before, it was really super duper quick, it now takes 49 seconds,

**Dave Jones:** so not a huge increase there at all, so obviously there's some IO bottleneck, and other stuff happening there, the processor didn't really dominate there, otherwise we would have seen a huge improvement, but overall, that is a fantastic upgrade, especially for Handbrake, and especially if I use the X264 rendering from Sony,

**Dave Jones:** I haven't actually tried that, but that uses the same X264 as what's used in Handbrake, Handbrake's just a shell around X264 encoding engine, so that's a huge, so I can get like 40% increase in that, for what, 100 or 200 bucks maybe, because I'll sell my old processors,

**Dave Jones:** depends on how much I get back for those, and it was probably not a very expensive upgrade at all, for like a 40% processor improvement on video rendering, so that's absolutely fantastic, happy with that, gone from 12 cores, which was kickin' ass, to now 20 physical cores at 2.8 gig.

**Dave Jones:** Xeon, so fantastic. Yes, you can get slightly faster processors, as I said, in the socket 2011 format, which my motherboard, Supermicro motherboard uses, but unfortunately they are really, really expensive, so this was by far the best bang-per-buck processor upgrade. So anyway, hope you liked that, I'm very happy with that,

**Dave Jones:** worked a treat. Catch you next time.
