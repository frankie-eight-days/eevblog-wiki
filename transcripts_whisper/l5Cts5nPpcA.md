---
video_id: l5Cts5nPpcA
title: EEVblog #610 - Why Digital Scopes Appear Noisy - Part 2
url: https://www.youtube.com/watch?v=l5Cts5nPpcA
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 45, "3": 65, "4": 85, "5": 105, "6": 121, "7": 137, "8": 161, "9": 177, "10": 193, "11": 209, "12": 229, "13": 245, "14": 265, "15": 273, "16": 293, "17": 309, "18": 329, "19": 345, "20": 361, "21": 381, "22": 401, "23": 421, "24": 437, "25": 457, "26": 473, "27": 489, "28": 505, "29": 525, "30": 541, "31": 561, "32": 577, "33": 593, "34": 609, "35": 625, "36": 641, "37": 657, "38": 677, "39": 697, "40": 717, "41": 733, "42": 749, "43": 765}
---

**Dave Jones:** Hi. Just a quick follow-up video to one I did a couple of weeks back on why digital oscilloscopes appear, in quote marks, to be so noisy compared to old analogue scopes. And if you haven't seen that video, click somewhere in here and I will link it in, or click down below if you're not

**Dave Jones:** following the annotations on YouTube. And there were basically four main reasons why digital oscilloscopes can appear more noisier than an analogue scope, even though they actually aren't. One was memory depth, the second one was the analogue bandwidth, and the third one was the lack of, or when they can appear less

**Dave Jones:** noisy when you include things like boxcar averaging or high resolution mode. And fourth was the intensity-graded display available on modern digital storage scopes. And the answer was is that modern digital scopes are not any noisier than analogue. They're just better. They're better at showing

**Dave Jones:** what's really on your signal here. And how, analogue oscilloscopes may actually be worse in that case in that they're hiding that high-frequency content which modern digital oscilloscopes show. Well, I just wanted to quickly update you on two more subtle things that can also affect the apparent noise

**Dave Jones:** on the displayed waveform on a digital scope. Let's take a quick look at them. Now I've chosen the Agilent InfiniiVision MSOX3000 scope here because this is, this appears to be, in quote marks, the noisiest scope that I have in my lab. And if you saw that I compared a couple of

**Dave Jones:** digital storage oscilloscopes in the previous video. Well, if you've seen me use this scope in videos, you might have seen a waveform like this. Look, I've got nothing connected to channel 1 here. Channel 1 is set to 50 ohms input impedance, right? It's not even high impedance, makes

**Dave Jones:** no difference if I terminate that input at all. And look at that! I'm 1 volt per division, and look at the noise on that waveform! Oh, you would think that this is the world's noisiest oscilloscope. And, well, as you know from the previous video, it's not.

**Dave Jones:** And it's precisely because this is one of the world's best oscilloscopes in this price-performance bracket is why it is appearing to be so noisy. And if we wind it down, look, here we go, 50 millivolts per division, 10, 5 millivolts per division, 2 millivolts per division, 50 ohms input

**Dave Jones:** terminated! Are you kidding me? I switched that to 1 making you see there's not a huge amount difference there. Are you kidding me? Look at that! That's a whole division! Unbelievable! How bad is this oscilloscope? Well it's not bad, it's actually brilliant. So let's

**Dave Jones:** go back to 1 volt per division here, and I'll show you why this particular oscilloscope appears to be one of the noisiest scopes, i.e. displays a visually thick line like this, in addition to those four things that we saw in the previous video.

**Dave Jones:** Well, as you should know, this is one of the world's quickest oscilloscopes. And check out down here, I've got it connected up, the trigger out from the oscilloscope, I've got it connected to my frequency counter down here. And you should know that this scope has an incredible waveform

**Dave Jones:** update speed of 1 million, or you know, roundabout claimed 1 million waveform updates per second. And yes, it actually gets slightly more than that. Check it out, 1.038 megahertz, or you know, over a million waveform updates per second. And it's incredibly high update speed, which is showing

**Dave Jones:** additional noise on this waveform here, compared to another oscilloscope that would have slower update rate. So, how do we prove this? Well, it turns out to be very easy, and let's demonstrate. All we have to do is slow down the update rate of this

**Dave Jones:** oscilloscope, and we should see the corresponding amount, or the apparent amount of noise on that waveform reduce. So how do we do that? At the moment we're in auto-trigger, and then we're just triggering from channel 1, so it's just auto, free-running trigger because we don't have any signal actually

**Dave Jones:** hooked into it. But what we can do is we can go into the trigger mode, or we can go into coupling mode here, we can go into, if we go into normal mode, you can see that there's no trigger event at the moment.

**Dave Jones:** So it's actually stopped. And you can get a hint of it. Look at how thin that line has suddenly become. Uh-huh! Well, what happens if we go into the trigger menu here and we set the source, trigger source here, to the internal wave gen, because this has a function gen built in.

**Dave Jones:** You can do this yourself using an external function generator into your trigger into the oscilloscope or another channel, okay? We can go into our wave gen here, and you'll notice that our frequency is 10 megahertz. Well, what happens if we lower that frequency?

**Dave Jones:** And what I'll do is I'll show you this on the display as well and show you the value dropping. So we're currently at 966,000 waveform updates per second, 966 kilohertz, okay? Let's adjust that frequency. You can see the frequency here drop. So it won't start dropping

**Dave Jones:** until we get below a megahertz or so. Here we go. Well, we're only getting, you know, 870 waveform updates per second. Here we go. So now it should drop, because the frequency corresponds to, there we go, the waveform update speed corresponds to our trigger frequency almost precisely.

**Dave Jones:** There's hardly any delay in there at all for processing that information and displaying the waveform update on the screen, because the Agilent has the MegaZoom 4 ASIC, does it all in that ASIC hardware. It's really, really quick. So you'll find that these two are going to match.

**Dave Jones:** So we can adjust this to any waveform update rate we like. And you'll see the way it hasn't changed, because 200,000 waveform updates per second, we won't see it change much until we get down to like, you know, like tens of hertz, hundreds of hertz, something like that, okay?

**Dave Jones:** 10 kilohertz waveform update rate, it's still quite similar, okay? And let's get down there, and you can see it's still in 7.7 kilohertz. Let's go all the way down. Let's not muck around, aha! Look, there we go, a kilohertz, you can start seeing

**Dave Jones:** the waveform, look. Look at that. And I'm not changing anything else, this is still 1 volt per division, 10 nanoseconds per division. All I'm doing is adjusting how many times a second this waveform is being captured and displayed effectively. And we're getting, once we get down to

**Dave Jones:** 400 odd, look at that, 440 hertz, okay? Look at that waveform! It is, let's go right down, let's, you know, go down to something silly, 16 hertz. Look at that, 16 waveform updates per second, and you can see it going really, really quite slow there.

**Dave Jones:** And to prove that nothing has actually changed here, that line is still as thick as it was before, what we can do is we can go into the display menu over here, and we can turn infinite persistence on. So effectively that's simulating what we were doing before

**Dave Jones:** pretty much. And you'll notice, although now it's not the solid color we were getting before, but if we zoom into that, over time that is going to build up. So there you go, I'm hoping you can see that. Because that line is now as thick as it was before

**Dave Jones:** with that dimmer information there, but that's basically exactly the same. And if I clear the persistence, you can see that information build up there. It's not very good. Let me go down in volts per division, and we'll really see it. And let's do that

**Dave Jones:** experiment again, but dramatically at 2 millivolts per division. I won't go down to 1 millivolt, because that's just a software thing in this Agilent R3000X. This is essentially the lowest hardware volts per division setting that it actually goes. Look, it's almost a full

**Dave Jones:** division, we're getting nearly that 1 million waveform updates per second but let's drop that frequency right down. Here we go, let's not muck around. 10 kHz, 3.5 kHz, 1 kHz and look at that. Look at that waveform change. If I go right down to, whereabouts were we before at around

**Dave Jones:** about 16 Hz before, look at that. It's totally changed. But I turn on that, well it hasn't changed, it appears as though it's less noisier. So now you can clearly see it there. With the infinite persistence turned on, that waveform is just as noisy as it was before.

**Dave Jones:** But it's only that it appeared as a solid line on the oscilloscope because it was just updating so damn fast. This scope was so good that you're being fooled into thinking that it's noisy when it's actually not. It's nothing's changed, it's just how it displays the information.

**Dave Jones:** So let's go back in reverse. Let's change our trigger source back to channel 1 here, let's go to our coupling set it auto mode, and look at that. Nothing else has changed, that signal hasn't changed but it appears totally different on the screen.

**Dave Jones:** You've got to understand how your oscilloscope works in this respect, otherwise you think your scope can be a lot noisier, and especially if you're doing comparisons between oscilloscopes. Really, if you want to do apples versus apples comparisons on the noise floor of two digital scopes, well you

**Dave Jones:** have to make sure not only are they the same memory depth, the same analog bandwidth, they've both got the intensity graded display set to the same level, but also that they've got the same update rate and sample rate as well. Now to show

**Dave Jones:** you where that sample rate can come into it, the Agilent always displays 4 gig samples per second here. So it won't drop from that unless I go down to... where is it? There you go. 100 microseconds per division, and if we go back to 50, we're still 40 gig samples per second.

**Dave Jones:** But let's turn on, shall we, let's go to the acquire menu and let's turn on that boxcar averaging or high resolution mode as it's often called these days, and you'll notice that it hasn't done much right up at this high speed. That's because there's not enough samples in there

**Dave Jones:** for it to actually work and do that boxcar averaging function. It's too fast. But look what happens if we lower our time base down. Look, look at that, it's going down, down, down. Look, the magic of that boxcar averaging at your slower sample rate.

**Dave Jones:** And because the sample rate isn't as high, then your noise is going to be less at your lower sample rates. That's just how digital scopes work, and you've got to be aware of it. And of course I haven't been using this scope to its full potential

**Dave Jones:** either, because I've been, I've had the intensity graded display set to 100%, so it's working just like a, you know, an old school one without intensity graded display. But of course you turn that down, and look, the less frequent noise just hides into the background there, as I explained in

**Dave Jones:** that previous video. And there's the true average noise that you'll see on an analogue scope right in there. There you go! Digital scopes, they're just better than analogue scopes and that's why they appear noisy. So from those two videos I hope you can better appreciate how digital scopes work,

**Dave Jones:** how they display their signals, and why that, why they appear to be noisy when they actually aren't. They're just a better tool than an analogue scope. And how there are six different things, no less than six different things, apart from the actual noise

**Dave Jones:** floor of the digital channel itself and the analogue to digital converter. You've got memory depth, analogue bandwidth, the boxcar average and the intensity graded display, the update rate, and the sample rate. It's ridiculous! You've got to know how all these things work and how to

**Dave Jones:** use your digital scope. These are vastly powerful tools compared to their analogue predecessors. So really, if you don't know how to use them properly, well, that's why there's this myth going around that they're noisier. You've just got to use it right and understand what is happening with them.

**Dave Jones:** So if you haven't seen the previous video, it's linked in down below and if you want to discuss it, the forum link is down below as well. And I hope you found that useful. Catch you next time. .
