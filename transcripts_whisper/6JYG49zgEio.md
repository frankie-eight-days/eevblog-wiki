---
video_id: 6JYG49zgEio
title: EEVblog #93 - PCB Autorouters Suck
url: https://www.youtube.com/watch?v=6JYG49zgEio
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 38, "3": 62, "4": 88, "5": 111, "6": 125, "7": 138, "8": 164, "9": 179, "10": 206, "11": 225, "12": 249, "13": 271, "14": 282, "15": 305, "16": 327}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's time for another stream of consciousness drive time rant. Yes, it follows on from the last one. I've just gone a couple

**Dave Jones:** hundred meters down the road and I'm going to do another topic. This one comes from the forum, yet again, the eternal fountain of rant material, really. And somebody posted, once again, I forget who you are, sorry, posted the classic beginner question that I get all the time by email and I

**Dave Jones:** see on other forums. And, oh man, I'm getting a bit sick of it, actually, is that they're looking for a low-cost PCB tool. And, you know, great, okay, you know, everyone's always looking for a low-cost PCB schematic EDA tool. And one thing they always, a lot of beginners, tend to add on

**Dave Jones:** is that, oh, it must have an auto router, because auto routers save so much time. And every time I hear that, I just get so irate, because these beginners don't understand the fundamental concepts of auto routers. Oh, M2 tunnel, wee! Dark and spooky and exciting.

**Dave Jones:** And we emerge, here we go. Anyway, bit of fun there. And, yeah, and they think that, you know, these auto routers will save them a whole bunch of time and make their PCB layout easy. And, and it's just crazy that they don't realize that PCB auto routers are a very advanced tool

**Dave Jones:** that should only be used by advanced PCB layout people to do very specific tasks, if they should be used at all. Some, you know, old-time PCB designers like me, you know, pretty much have a blanket rule that they won't use an auto router.

**Dave Jones:** But, you know, in a lot of cases, it makes sense to. But it's only in when you set them up correctly with all the rules and everything, and you let them rip on a very specific aspect of your, or a very specific area of your board.

**Dave Jones:** You do not just throw down your components and hit the auto route button, and it routes your entire board. That is just bullshit. It always has been, and always will be. And the simpler your board is, once you get down a single layer or a simple double layer, and you've got components nicely spread out, like a

**Dave Jones:** beginner might do a simple project with through-hole components, etc. Then, the simpler the case, the worse the auto router works, in many respects. In terms of, A, being able to actually do the job, and B, actually doing a good job, and doing a nice job.

**Dave Jones:** And it just basically doesn't work. Try and let an auto router rip on a, you know, on a single-sided board, and it's just, or a simple double-sided board, and the results are just horrendous. They really are. And considering that you spend most of your time actually selecting the components, as I've mentioned before, you know,

**Dave Jones:** using DigiKey, and Mouser, and other websites to select and find the right components, and then draw a nice schematic, and then check it, and you know, do everything else. And then you, you know, you place your components all nicely. Doing that, and doing those steps alone, is like, you know,

**Dave Jones:** 95% of your work. It always will be in any design, really. And for someone to say that a PCB auto router on a simple board is going to save them a massive amount of time, what? It's just crazy! It's nuts, because you spend 95% of your time doing all the other stuff, and only 5% of the time

**Dave Jones:** routing. So why not take a bit of pride in your work, and do it properly? Manually route it, learn how to route, because you'll learn so much by routing it yourself, and actually going and studying all about, you know, how to do a nice PCB layout, tight PCB layouts for like switch mode power supplies, and

**Dave Jones:** you know, things like that. There's lots of things, little things to learn that auto routers have no freaking idea about, quite frankly, and they're just going to produce horrible results. So really, ah, please, beginners, do not use an auto router. It's just, it's just pointless.

**Dave Jones:** It's a waste of your time. So you see a package like, um, say Eagle, which is a very popular low cost, well, you can get a free version which does very small boards, and they charge a lot extra, um, for the auto router.

**Dave Jones:** Um, you can buy it separately, I think, and, uh, really, I don't know why anyone would bother, because Eagle's not a high-end tool. It's, you know, it's, it's a reasonably low-end, you know, um, PCB, uh, and, you know, layout, EDA tool. Why it bothers having an auto router is, you know, it's, it's almost beyond me.

**Dave Jones:** Why, and why anyone would buy it is, is beyond me as well. It's just crazy. So, yeah, auto routers, please, beginners, don't touch them as much as you think they might be saving you time or effort. Trust me, they're not. See you next time.
