---
video_id: weJ4JdFat8o
title: EEVblog #20 - The Unusual Oscilloscope Phenomenon Part 2
url: https://www.youtube.com/watch?v=weJ4JdFat8o
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 17, "2": 40, "3": 62, "4": 82, "5": 101, "6": 119, "7": 146, "8": 166, "9": 196, "10": 218, "11": 236, "12": 250, "13": 270, "14": 297, "15": 322, "16": 334, "17": 359, "18": 377, "19": 394, "20": 411, "21": 421, "22": 441}
---

**Dave Jones:** Hi, welcome to the EEVblog. I'm your host, Dave Jones, and this is episode number 20. Now, as what's usually the case, I was going to talk about something else, but there's been a lot of talk recently, a lot of feedback. I've had a lot of feedback on the

**Dave Jones:** blog I did not so long ago on a rather unusual oscilloscope phenomenon, where I stood up from my chair and I generated a static impulse into an oscilloscope probe and it appeared on the oscilloscope. And there were so many people claiming that I got it all wrong,

**Dave Jones:** and what was actually happening was the loop, the actual loop on the ground probe loop on the oscilloscope probe, is the thing that was picking up the signal. And, well, I made the claim that it wasn't, and this is true. And I'll demonstrate it again without this loop, and I'll show you

**Dave Jones:** that it's actually being picked up by the probe itself and not by this loop. The loop certainly helps, but it's not the main contributor to the pickup. Well, you can actually get it with just the probe, so let me demonstrate. Okay, I've got my oscilloscope set up, and first let's see if we

**Dave Jones:** can try and recreate the same problem. I've got my crow probe shorted like that, and everyone knows that's not a true shorted RF, but I did this just as an example to show that, you know, the probe was actually, that it was actually shorted, because your average user, you know, doesn't expect

**Dave Jones:** anything on the crow when it's shorted. So let's try and reproduce the problem. I'll put it down on the bench, and let's go, trigger, and I stand up, and bingo! I've captured exactly the same thing I captured last time. Okay, that's one volt per division.

**Dave Jones:** Okay, one volt per division there. Let's try it again. This time, I'm going to disconnect the ground lead and just have the crow probe on its own. This is a x10, it's on the x10 position. Let's put it down there again, and let's

**Dave Jones:** try this again. Run, here we go. Stand up, and bingo! We got it again, but it's much smaller in amplitude, as you can see. As you'd expect, that's 200, that's actually actually 0.2 volts per division, but you can see it's a similar response.

**Dave Jones:** So I'll just try that again, see if we can duplicate that, and bingo! No? Okay, let's try it again. There we go, I got another one. This is a rather unusual looking one, but once again, you get a response. No ground loop. Okay, now let's try it again, but this time,

**Dave Jones:** I'm going to get some alfoil. Okay, a little bit of aluminium foil. I'm going to wrap it around the top of the probe like that. Okay, so it's making contact, it's shorted out. Okay, I'm going to do it again. I'm going to put the crow probe down like this, and I'm going to set up

**Dave Jones:** the trigger, and stand up, and bingo! There it is again, with a shorted probe. It's got nothing to do with the ground loop, or the ground loop actually helps, but it's not the main contributor. It's being picked up by the coax, by the probe.

**Dave Jones:** It's not the ground loop. There you go. I hope I cleared up that myth. Okay, and if you're still not happy, I'm going to show you another way you can get it as well. I think I mentioned this in the last blog actually.

**Dave Jones:** You can get it using a standard coax. Here's a coax cable. I won't use a crow probe at all. Standard coax. Plug it in. Let's have a look at this. Set the trigger, and stand up, and bingo! There you go. Once again, standard, just a standard, un-terminated coax.

**Dave Jones:** And I know what you're thinking. Okay, it's un-terminated. So, let's run that same test again, but let's put on a 50 ohm terminator, and see what happens. Standard coax, 50 ohm terminator. Watch this. Start again, and bingo! We still get it. There it is.

**Dave Jones:** 50 ohm terminated coax cable. You still get it. You don't think it's being picked up by the coax? Think again. And I'd also like to clear up some other things people have been saying too. They criticised, some people criticised my use of a 100 megahertz

**Dave Jones:** scope to measure a 100 megahertz signal. Fair enough. But this is the only one I had to hand. I just wanted to demonstrate the effect. But you can get exactly the same effect, and it is sinusoidal. Well, usually, it depends on how it actually manifests itself, but it is sinusoidal.

**Dave Jones:** It is around 120, 100, 120 megahertz mark, and you can see it clearly. I actually got exactly, I first found this effect on a 300 megahertz scope. So it's, you know, it's got nothing to do with the bandwidth of the scope. The higher the better, of course, but I just used this one to

**Dave Jones:** demonstrate. And also there's some people have said, oh, I've got something unique in my workshop here, you know, something, or it might be specific to this particular scope. No, I've had the same thing on many different types of oscilloscopes, many different bandwidths, many different types of

**Dave Jones:** crow probes, different coax cables, and all sorts of things. And yeah, the effect is, seems to be quite high here. I seem to generate quite large voltages. My current desk at work, I don't seem to get the effect much at all. It's very difficult to reproduce.

**Dave Jones:** But in my old lab at my old company, it was really easy, where I first found it in multiple locations, different benches, I found it. And it was, you know, and I seem to be able to get this pretty easy. A lot of people having

**Dave Jones:** trouble. Maybe it's the, I don't know, the humidity, something to do with Australia, I don't know. Maybe it only works down under, who knows. But yeah, I can get it. There's nothing unique about this bench at all. I've seen the effect many, many places.

**Dave Jones:** And of course, my main point about showing this originally in the blog was not only because it's interesting, but also was to actually demonstrate that this effect can actually happen while you're actually measuring something, and you think it might be your circuit at fault, when it's not.

**Dave Jones:** It's actually your, you know, injecting static charge into your cable, into your probe cable, and it makes it look like it's coming from your circuit, when it's actually not. So it's just something to be wary of. So there you go. I hope that generates some more controversy.
