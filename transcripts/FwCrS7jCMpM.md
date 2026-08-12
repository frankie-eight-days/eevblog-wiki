---
video_id: FwCrS7jCMpM
title: EEVblog #387 - Oscilloscope Trigger Jitter
url: https://www.youtube.com/watch?v=FwCrS7jCMpM
source: youtube-asr
timestamps: {"0": 0, "1": 22, "2": 37, "3": 47, "4": 64, "5": 88, "6": 105, "7": 115, "8": 131, "9": 142, "10": 161, "11": 175, "12": 190, "13": 201, "14": 220, "15": 236, "16": 250, "17": 264, "18": 277, "19": 288, "20": 307, "21": 320, "22": 347, "23": 361, "24": 376, "25": 395, "26": 417, "27": 432, "28": 460, "29": 472, "30": 484, "31": 494, "32": 507, "33": 527, "34": 540, "35": 550}
---

**Dave Jones:** Hi, just a quick video, and yes, this one will actually be quick. I'll try and do it in a single take. This is a follow-up to my last video, which was the second delay line video, where I was playing around with a delay line, and I was putting a burst signal into it, and we're measuring the delay and looking at the burst coming out of one of these PAL

**Dave Jones:** delay lines. Now, somebody asked, um, I mentioned in the video that, uh, you know, there was the screen jitters like this because the triggering wasn't set up correctly, and I didn't bother because I was playing around with single shot.

**Dave Jones:** I was single shot capturing it, and you can go in there, and you can view the waveform just fine. So, they wanted to ask, how do we fix that trigger jitter like that?

**Dave Jones:** And it turns out I've already done a video on this. It's called trigger hold-off, and I go it's about 20-minute video. It explains how to trigger like this, but there's actually, uh, three ways to, uh, trigger off this thing and make it stable.

**Dave Jones:** So, let's take a look at them. Now, why does it trigger? Um, I be very brief because it's in my more detailed video, but basically, when you've got a burst, a sine wave burst like this, we're triggering off the yellow waveform here, and you'll notice that the jitter is basically the same width as the packet of data like that.

**Dave Jones:** And that's no coincidence because if we single shot capture this thing, this scope is just set for basic triggering, just edge type triggering, um, and, uh, set up for, you know, it's triggering off the yellow waveform, source one, positive going edge, absolute basic trigger.

**Dave Jones:** Now, it's triggering at that point there. You can see the triangle. There it is, but it doesn't know whether or not to trigger off that one or that edge or that edge or so on.

**Dave Jones:** It doesn't know which one of those to trigger on. And depending on when you run this thing, when you run it like that and it's trying to get a trigger, depending on when the rearm time of this scope is, you could actually get the trigger point being anywhere within that period there.

**Dave Jones:** It's not going to trigger in this dead period because, well, it doesn't transition through the trigger point there. There's our trigger level there. It's sort of set halfway between there.

**Dave Jones:** So, it doesn't know which one of those to trigger off. So, that's why it can be you can get trigger jitter up to the width of that. So, one way to Oh, and and by the way, depending on the rearm time, that depends on the input frequency you're inputting to this thing, sometimes you can actually fluke it.

**Dave Jones:** But because we don't have much of a dead time in there, if I actually change the number of cycles here, if I reduce the number of cycles, then there's more chance You see how it becomes more stable?

**Dave Jones:** I've only got 16 cycles now, or there's only six cycles now. You see how it's more stable? It's because less chance that the rearm time is going to be within that period there based on the whole period there.

**Dave Jones:** It's just pure statistics unless you fluke the exact input frequency to make it stable. So, if I increase the number of cycles, you'll see that the jitter increases like that.

**Dave Jones:** And likewise, if I say increase the burst period like this, it has the same effect. It can actually make it more stable because the odds of it triggering within there are quite short.

**Dave Jones:** It's more likely that the rearm time is going to appear somewhere within that long dead period. So, if it appears, say, halfway between here by chance, then it's going to wait until the next edge, and you will get it to trigger off that very first edge there.

**Dave Jones:** There's just more chance of that happening. So, I'll change this uh change this back to get ourselves a really horribly triggered waveform, shall we? So, let's go in there, number of cycles, increase those.

**Dave Jones:** Bang, okay. So, we we want to trigger off this thing here. Now, the way we do it is with trigger holdoff. I've done a whole video on this. So, let's go into the mode coupling menu here, and there's an option here called holdoff.

**Dave Jones:** And this is available on analog scopes as well as digital. And it's currently set to the minimum value of 40 ns. So, I won't go into the details, but watch my other video if you want to see it.

**Dave Jones:** Now, we can increase that value, and because this burst here is 20 µs, if we if it's under 20 µs, then it can still trigger on parts of that waveform.

**Dave Jones:** We want it to delay or hold off. That's why it's called holdoff, trigger holdoff. Hold off for that entire 20 µs period. Because if it happens to trigger off the first uh edge there, then it needs to hold off for at least 20 µs to make it stable.

**Dave Jones:** So, if we increase this holdoff value here, you'll find at 20 µs, it will magically become stable. There we go, 4 µs, 5, 6. It's a bit touchy. I don't want to turn it too fast.

**Dave Jones:** 10, we're still not stable, but as soon as we hit that 20 µs, here we go. We're almost there. Bam. There we go. We're just over 20 µs, and now we're stable at all time bases there, and it's always going to trigger off that first period because the holdoff, trigger holdoff is going to occur regardless of which random cycle the the first time you run it, it might

**Dave Jones:** trigger in the center there or something like that, but after that, it's going to rearm only during the dead period, so it will always trigger on that very first if it re-arms in this dead period, it waits until that very first cycle.

**Dave Jones:** Bingo. There you go. Treat that's using trigger hold off to stabilize your waveform, and that's the traditional way to do it. Now, the next way you can do it is using a more advanced trigger type that you can get on these modern digital scopes.

**Dave Jones:** Let's trigger on a pulse width here. So, we want to go down, select pulse width there, and we basically want to trigger on we're triggering on the source, which is the yellow waveform channel one again, and we want to trigger on the negative part of that, so we want to trigger on the negative when it's greater than a certain amount of time.

**Dave Jones:** So, when when we get to that dead period between the bursts, we want to trigger on that. You can see it's still unstable because it's set to 2 ns, which of course is less than the one one period less than the individual I'm feeding in a 10 MHz signal, so it's less than that.

**Dave Jones:** So, if we just increase that value here, let's increase that. 6 ns, 8, 12, 15, 20 ns. All we have to do is make it faster than that cycle time, and bingo.

**Dave Jones:** There we go. At about 60 odd ns, there we go. We now have a nice stable waveform. So, you can do it using that pulse width trigger. And the third option for doing this, because we're using in this particular case an external function generator to generate that burst signal, any good function generator like this will have a sync or a trigger output that will generate a trigger pulse at

**Dave Jones:** the start of that burst because we want to trigger off the start of that burst there and that's and this the function gen will actually generate a trigger pulse output during that burst period.

**Dave Jones:** So it will it will like generate a gating or trigger pulse or synchronization pulse, whatever you want to call it for that particular thing. So I've set it up, it'll output that synchronization pulse.

**Dave Jones:** A lot of function gens might even be output that by default and there's various options for that. You can have negative going, positive going. So what we need to do, go into our trigger menu here.

**Dave Jones:** Our source here instead of being channel one, we don't want to trigger off our signal anymore. We want to trigger off our external signal. Bingo, there it is. And we can display that by turning on channel three.

**Dave Jones:** There is that sync pulse. Check it out. Exactly there where as soon as it goes here, we want to trigger off that. And once again, we can use our trigger level here and we can cause it make that go unstable eventually because it's now triggering where our trigger level's working off external trigger pulse.

**Dave Jones:** But that's the third option to do it. So there you go. Piece of cake for triggering on complex signal. Well, this isn't really complex. It's just a simple burst.

**Dave Jones:** So there are the basics. Once again, I've done a whole tutorial on trigger hold off which uses basically this same example and it shows analog and digital scopes as well.

**Dave Jones:** So if you like it, please give it a big thumbs up. If you want to discuss it, jump on over to the EEVblog forum. Catch you next time.
