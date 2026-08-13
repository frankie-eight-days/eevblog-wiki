---
video_id: 3zAWgNjx5Ew
title: Intel MCS-85 Design Kit THERMAL IMAGING
url: https://www.youtube.com/watch?v=3zAWgNjx5Ew
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 14, "2": 33, "3": 47, "4": 63, "5": 77, "6": 98, "7": 117, "8": 137, "9": 164, "10": 187, "11": 208, "12": 237, "13": 255, "14": 268}
---

**Dave Jones:** Hi, just a quick follow-up video to this Intel MCS85 system design kit that you've seen on the main channel. Now, I've actually had this running overnight just for kicks, just to see if it would hold up, and of course it holds up. Look, no whackers whatsoever, right?

**Dave Jones:** But then I actually went around and was touching some of the chips, particularly the ones at the top with the back of my finger, just seeing how warm they are, because the thing actually does take 5 watts, you know, and it's only running at 3 megahertz, doesn't, you know, it's not exactly a speedster,

**Dave Jones:** but it's taking a lot of power. And these chips, particularly the ones up in the I.O. bus expansion driver up here, they're really too hot to keep my finger on, which means that they're over, you know, 55 degrees, something like that is like a rule of thumb.

**Dave Jones:** If you can't keep your finger on there, you know, 60 degrees plus, then you're going to go ouchie, ernie, bernie, and you're going to keep your finger, you know, you're just going to have the reaction that you pull your finger away, because it's too hot.

**Dave Jones:** So I was just feeling the chips, so I thought I'd just get out the thermal imaging camera and actually have a look here at some of the chips. I'm going to have to make sure I don't get this stupid reflection of the lights,

**Dave Jones:** but let's have a look here. You can see the arrow, see the cursor in the middle, okay, so that's the, oh, come on, let's see if I can get it to go, that's the processor there. So the processor's at 41 degrees, it's supposed to find the hot spot in there, 48, you know,

**Dave Jones:** it's almost 50 degrees, something like that, for the actual processor. And this one over here is the keyboard and display driver, so that's 42, and this one down here is the ROM, that's about 35, so it's the coolest out of the whole lot.

**Dave Jones:** This is the RAM down here, the bottom RAM is 47 degrees, this is Celsius by the way, not this Fahrenheit rubbish, and then 42 the top one, so I assume that the bottom one's the one being used, I guess, which is why it's hotter, or is there that much discrepancy between, you know, silicon.

**Dave Jones:** But look, and the little address latch, address decoder in there, that's 53, the 74LS over here, yeah, oops, actually that's the, yeah, the 74LS takes nothing, because it's an LS, LS stands for Low Power Shotkey. And this one up here is an S device, you can see my finger, so that's running,

**Dave Jones:** it is a bit warm, I can't get the cursor to lock into that one, really. So anyway, the S and the LS devices are running cool, but these ones up here, these are Intel 8216s, and they're running at 57 degrees, 58, 59, we're almost talking like 60,

**Dave Jones:** we're talking 60 degrees up there for those ones up there. If I try and keep my finger on that, that's getting a bit hot. Ah, yeah, yeah, yeah, yeah, that one's getting really hot. So, and these ones over here, which are Intel 8212s, these are 8-bit latches,

**Dave Jones:** the smaller ones here, the 8216s, they're actually bidirectional 4-bit latches. And these bigger ones, the 8212s, they're actually 8-bit latches, and they're 64 degrees. Wow! And if you actually have a look at the datasheet for these 8212s, they're like 90 milliamps. Like, it only gives you, you know, a typical power consumption,

**Dave Jones:** and that's presumably like static doing nothing, right? It's drawing 90 milliamps. It's like, it's not only CMOS rubbish, it's, you know, it's high-power old-school. And, like, sitting there doing nothing, we're not actually driving, and the program's not actually talking to the expansion bus, or I don't think it is.

**Dave Jones:** It shouldn't be. Anyway, but, like, some of the address lines will all be toggling and stuff like that. But anyway, yeah, they're rated for like 90 milliamps a pop. I don't know what these ones are, couldn't, didn't get a full datasheet for those,

**Dave Jones:** but, yeah, interesting, these ones get hotter than the actual 8085 processor itself. And the RAM down here gets hotter than the processor itself. It's just, you know, it's just crazy stuff. Anyway, I thought you'd find that interesting. Catch you next time.
