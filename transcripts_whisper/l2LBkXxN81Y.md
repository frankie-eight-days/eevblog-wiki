---
video_id: l2LBkXxN81Y
title: µCurrent Offset Voltage Fix
url: https://www.youtube.com/watch?v=l2LBkXxN81Y
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 24, "2": 44, "3": 67, "4": 88, "5": 108, "6": 126, "7": 142, "8": 159, "9": 182, "10": 198, "11": 220, "12": 239, "13": 258, "14": 281, "15": 302, "16": 324, "17": 347, "18": 371, "19": 394, "20": 412, "21": 430, "22": 446, "23": 462, "24": 481}
---

**Dave Jones:** Hi, just a follow-up to the microcurrent video on my main channel, which I'll link in down below if you haven't seen it. Just showing an additional fix here for those who may have an existing unit with the 321 marked op-amp in there, 321T or S,

**Dave Jones:** or maybe some other letter variant in there. And if you have an issue with a capacitive load, there is an additional fix which I've tried here. And let me show you, I've put 0.1 microfarads ceramic bypass caps to either side of C2 there,

**Dave Jones:** which is basically across the battery, so each supply rail to the virtual ground there. And a few people commented on this in the main video and said, well, that seems to be the obvious solution. And my recollection from when I designed this way back at the start is this actually did cause stability problems.

**Dave Jones:** But maybe that was with the one maximum variant and not the microcurrent gold with the two maximum variants, I don't know, I don't think I have my notes from that anymore. But this one, in this particular case, seems to work. But it's not a given that it would actually work bypassing the virtual ground,

**Dave Jones:** which is the negative output terminal here, to both supply rails. Because then you, what you're doing is effectively adding that capacitance via the 270 ohm resistor. In there, there it is, the 270 ohm resistor. Sorry about the crudity of this video, didn't have time to build it to scale or to paint it.

**Dave Jones:** Even though you've got the 270 ohm series output cap, that doesn't magically isolate you from any capacitive load. But what it will do is actually shift the pole so that, I won't go into poles and op amps and response and all that sort of jazz,

**Dave Jones:** that's a whole video or two in its own right. But yeah, it doesn't magically fix that. Putting in that series resistor, which is in there, doesn't magically fix that. So adding these capacitors on effectively the output of the op amp via that 270 ohm resistor

**Dave Jones:** to the virtual ground, to the two different rails, positive and negative like that, is actually adding capacitance to the output. And that's generally not a good thing to actually do. But in this case, I have tested it, and it does seem to work just a treat.

**Dave Jones:** So let me demonstrate here. So I've actually got two boards molded. One has the good in quote marks TI part, the RC1F chip, and this one has the troublesome 321T or 321S part on it. So let me try. So what I'm doing is, well, actually, here we go.

**Dave Jones:** It did oscillate before. Trust me, you'll have to trust me on that. Here it is. So this has got the 321 marked chip in it, and that's just hunky-dory. Don't worry about those, that when I switch the, I'm just switching the input load there.

**Dave Jones:** But yeah, you can see there's no problems whatsoever. And if I, well, hang on, yes, I've got the capacitors. Yep, hang on. Which way around does this go? Hang on, sorry. If I turn on the capacitive load, yes, it works fine. It seems to work fine with almost any capacitive load that I can give it.

**Dave Jones:** And it basically works identical to the RC1F chip. So that seems to be additional fix, but let's just feed in a signal, shall we? And see if we can check the response of this. So this is, don't worry about all that noise, because I've now not shorted the input,

**Dave Jones:** and I've got it on the nanoamp range, and it's just picking up anything. So once we plug in our signal, we'll be hunky-dory. Oh, we're way off scale here. Let me put it in, there we go. There we go, yep, we're good. Don't touch it.

**Dave Jones:** Alright, so that's 100 kHz with no capacitive load. So there we go, 100 kHz, no capacitive load. And if I whack on some additional capacitive load, of course we're going to change our response. So what we want to do is get like worst-case overshoot, like something shocking like that, right?

**Dave Jones:** Which should, you know, like when you get worst-case like that, you should expect to start seeing it oscillate, or potentially oscillate, but it doesn't. So what I'll do is I'll then, so that's the response we get with, what have we got? I think a couple of, no, one N load.

**Dave Jones:** We've got one nanofarad load on there, and of course if we, at that sort of frequency, if we put any high capacitance on there, it just kills that because of the capacitive reactance. So let's put that on our board with the TI part,

**Dave Jones:** and let's give that a whirl, there we go, it's basically the same response, there you go. So there's the no capacitive load, so it's good right up until, well let's go 300 kHz, what's the, I think 300 kHz is the bandwidth where it starts to drop off on the microcurrent, isn't it?

**Dave Jones:** Something like that, yeah, you can see it start to, the response start to drop off. Actually that's 700 kHz, that's 700 kHz there, so that's a megahertz. So that's with the TI part and no capacitive load. Let's put back the part, yep, there we go, so that's all good.

**Dave Jones:** So that looks hunky-dory, even with a worst-case capacitive load. But now, so that is a fix, a potential fix for those who don't want to, well who A, have a problem with this op-amp oscillating, and B, don't want to change the chip, and well they don't want to go and order a chip or whatever,

**Dave Jones:** couldn't be bothered, looks like you can use a 0.1 mic ceramic bypass to the positive and negative rail. But as I said, that's not a guaranteed, well in theory it's not a guaranteed fix, and kind of is not necessarily a good thing to do,

**Dave Jones:** adding the capacitive load directly on the output of the op-amp, even though it is via a series resistor. And I recall my testing way back in the day, we're talking many years ago now, is that I was seeing oscillation. I can't remember what parts I was using in what, you know, I can't remember,

**Dave Jones:** but I remember that being a problem, which is why I didn't add the bypass caps to the virtual ground, because I found that A, I didn't need them, and B, it could potentially cause some sort of issue. But in this particular case, it seems to have fixed it.

**Dave Jones:** So there you go, that is an additional fix for those who have a problem and want to do it. Once again, I could probably do further testing, but setting the worst case capacitance on the output, that's always a good, that's always a decent way to do it.

**Dave Jones:** That's always a decent way to do it. Look, our gain's gone right up, because it's just, whoo, overshooting severely there now. And if it doesn't oscillate in that sort of, you know, worst case configuration like that, then you can be sure that's a pretty solid fix,

**Dave Jones:** unless you want to go in there and, you know, sweep it with your network analyzer and do the whole bells and whistles. But yeah, that looks good. There you go. Thanks, catch you next time.
