---
video_id: RvYnt7HvoL0
title: EEVblog #12 Part 2 of 2 - Shanghai Special - Dodgy USB Hubs
url: https://www.youtube.com/watch?v=RvYnt7HvoL0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 42, "3": 65, "4": 89, "5": 109, "6": 130, "7": 155, "8": 177, "9": 194, "10": 206}
---

**Dave Jones:** This time, it's something we encountered in Shanghai, we're over there. We needed a whole bunch of, for our test system, we needed a whole bunch of USB hubs. So we went to the local markets and, you know, we bought some rather cheap, or what we were told were, you know, fairly decent quality, you know, multiple port USB hubs.

**Dave Jones:** And we had all sorts of problems with them, and I'm going to show you why. Now, it looks fairly fancy on the outside, you know, it's got an aluminium case and it's got, you know, nice little stickers on it saying it's USB 2.0 and 480 megabits per second and all the usual stuff.

**Dave Jones:** But if you take it apart, check it out. What a load of garbage. Absolute crap. I haven't seen anything this bad in a long time. The list of problems on this thing is as long as my arm. Okay, issue number one. It's a cheap, crap, single-sided, phenolic base board.

**Dave Jones:** It's not even FR4, and that means there's no ground plane, there's no controlled impedance routing for the high-speed USB stuff, and, yeah, it's just as cheap as you can get. Problem number two, they've used a ceramic resonator instead of a crystal. Why? Because they saved, like, you know, half a cent.

**Dave Jones:** And to squeeze extra, you know, extra margin out of this thing, they just decided to use a crappy crystal resonator. That's just not on. Now, the next problem with this thing is the power supply filter, or lack of it. It's powered from an external DC power jack, but, you know, where are the bypass caps?

**Dave Jones:** There just, there aren't any. There's a, well, there's, I think I can see, like, two little hundred ends there, which aren't actually directly bypassing the power input, they're actually hooked into the chip somehow. But, yeah, that's just crap. Essentially, no power supply filtering.

**Dave Jones:** Now, the biggest problem with this thing, though, as if the other things weren't actually enough, is the soldering. I've never encountered anything like it. I'm not sure if you can see it. I'll try and include a close-up photo of the solder joints. But the actual, the actual USB connector, the shields are not soldered at all.

**Dave Jones:** And the actual pins on there, the data pins, they've, you know, they've barely got half the solder on some of the pads, and they're just, they're just crap. They're dry joints, and there's only half the solder there. That's, that's real amateur stuff. So we were trying to debug our test system using these crappy USB hubs,

**Dave Jones:** and we're wondering why we're getting all sorts of problems. We thought, you know, brand new, out of the box, they should work, right? No. Absolute load of garbage. So, in the end, we had to go out and buy a, you know, a top-quality Nohan brand unit.

**Dave Jones:** Oh, well, we weren't quite sure it was a Nohan brand, but it came with a nice 4-amp plug pack, which is really what we needed. It was a 7-port one. And I'll show a photo of that. I don't actually have the actual unit now.

**Dave Jones:** And you'll see the quality difference between this heap of garbage and the much more expensive, professionally designed and assembled hub board. So, watch out for it next time. Cheap USB hubs, or just cheap consumer products. They're just garbage. Thanks for watching.
