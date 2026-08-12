---
video_id: GZHnrGIK9V8
title: EEVblog #1320 - Premature Oscilloscope Triggering
url: https://www.youtube.com/watch?v=GZHnrGIK9V8
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 22, "3": 40, "4": 48, "5": 57, "6": 70, "7": 84, "8": 97, "9": 106, "10": 123, "11": 139, "12": 156, "13": 178, "14": 207, "15": 224, "16": 239, "17": 253, "18": 270, "19": 286, "20": 305, "21": 320, "22": 328, "23": 340, "24": 354, "25": 369, "26": 383, "27": 394, "28": 407, "29": 421, "30": 438, "31": 455, "32": 467, "33": 497, "34": 511, "35": 529, "36": 548, "37": 560, "38": 572, "39": 587, "40": 599, "41": 616, "42": 644, "43": 658, "44": 677, "45": 686, "46": 702, "47": 716, "48": 729, "49": 741, "50": 753, "51": 766, "52": 784, "53": 792, "54": 805, "55": 819, "56": 832, "57": 845, "58": 865, "59": 877, "60": 895, "61": 909, "62": 924, "63": 935, "64": 946, "65": 963, "66": 975, "67": 990, "68": 1004, "69": 1018, "70": 1029, "71": 1040, "72": 1052, "73": 1065}
---

**Dave Jones:** Hi, I wanted to show you a trap for young players about triggering on an oscilloscope and I found this while doing a repair video here which my uh patrons and subscribe star and uh forum supporters have already seen.

**Dave Jones:** I've done like a 35-minute video or a progress repair. Anyway, I haven't uh completed it yet. I need uh some parts for it. Anyway, they've already seen that video which is interesting.

**Dave Jones:** But, more to come on that perhaps. Hopefully, I fix it. Anyway, I wanted to show you something interesting here. Now, what I'm doing is I'm just uh triggering off uh the 3.3 V rail here and I'm just going to power up this scope.

**Dave Jones:** So, what what I've got here is it's just on channel two here. My trigger level is just like, you know, set to the middle of the uh 3.3 V waveform here.

**Dave Jones:** Okay, so what I'm going to do, I'm going to set it to a slow time base like 500 ms uh per division. I've got my pro Let's switch the product off.

**Dave Jones:** Okay, I'm going to trigger on the rising edge. We expect to see a trigger point right in the middle there. So, here we go. Uh Hmm. Something's a bit strange.

**Dave Jones:** What's going on here? There's our trigger point right in the middle there, yet here's our trigger edge over here. But, I know what you're thinking. Oh, Dave, there's some some there's obviously something in there.

**Dave Jones:** We have to zoom in and see um what it's actually triggered on. Well, okay, I'm zooming in. I'm zooming in. I'm zooming in. I'm zooming in. Um there's nothing there.

**Dave Jones:** Here's our trigger point, right? Our Our trigger point's right up here at like, you know, a volt and a half or something. So, it's got to rise above based on our trigger rules here.

**Dave Jones:** Our edge trigger uh positive going slope, it must this signal must transition above our trigger level there before it will trigger, but there is nothing there. There's absolutely nothing.

**Dave Jones:** Our positive going edge is all the way over here. What's going on? So, just for kicks, let's choose another scope here, signal in 1,100, whatever, channel two, slope rising edge, our trigger levels, you know, round about 2 volts, something like that.

**Dave Jones:** So, let's switch our thing off, single shot, let's switch it back on, and capture where you know, that was just the decay of the power supply, and let's switch the product on.

**Dave Jones:** There it is. Bueller. Bueller. Look at this. It's There's our trigger point right in the middle, yet we're triggering over here, and there's nothing. I can zoom all the way in there, and there's absolutely waveform extended to the maximum.

**Dave Jones:** Anyway, there's nothing there. Why is it triggering here and when our true rising edge is over here? Really got a trap for young players here. All right, so what's actually going on here is that there's not necessarily a correlation between what is captured by the analog to digital converter and displayed on your screen and what's actually captured by the trigger circuitry, the analog trigger circuitry inside your oscilloscope.

**Dave Jones:** So, maybe there's there really is something happening in in here in the trigger search circuitry of this scope because it's not going to trigger on nothing. Okay? It's going to It's going to be triggering on something, but why can't we see it on the screen?

**Dave Jones:** Aha, we don't have enough detail. We don't have enough sample memory. So, let's go into a choir here. Memory depth of 1.4 meg, that's pretty good, right? Please quit stop Please quit stop mode.

**Dave Jones:** Oh, jeez. Anyway, God, really? Really? I can't change memory depth in stop mode. Let's go to 14 meg. Okay, let's repeat the exact same thing, exact same time base, cuz the time base is going to matter.

**Dave Jones:** Single shot capture that. Let's zoom in. See what we get. Aha, we start to see some funny business here, but it's still and there's a couple of glitches over here.

**Dave Jones:** Look, you can see these, right? They're almost at the trigger level there, but not quite. They're still nothing there. We still can't see it. Well, let's We're at 100 milliseconds per division before, weren't we?

**Dave Jones:** Let's go down to say 10 milliseconds per division. And let's do it again. Single shot capture, 14 meg memory depth. Bingo. Look at this. There you go. Oh, no, it's still not It's still not enough.

**Dave Jones:** Look, it's still not enough. There is still There's our There's our trigger point. There's still There's our trigger level right there. It's still not high enough. But, it is still There's a couple over here.

**Dave Jones:** Now, I hopefully you can see those. They're very faint. Maybe the light's off. So, yeah, we can go into the horizontal here, then we can zoom in on that.

**Dave Jones:** There There certainly are some glitches in here, which are well above that trigger level there. So, you know, it would trigger on that, but that's not the point it actually triggered.

**Dave Jones:** It It triggered all the way back in here, where there's nothing. So, hmm, we're still not seeing what's going on here. But, anyway, where's all this funny business coming from?

**Dave Jones:** Well, if you're experienced in probing, you'll no doubt see where we've come a gutsy here. Look at this, big antenna earth loop here, right? This big ground plot probe, cuz we're being lazy in our probing, right?

**Dave Jones:** We're just probing the power supply. We don't, you know, necessarily care that much about high frequency signal integrity. Big ground loop here, okay? It's even worse, cuz we've got this additional one coming over here, but it's just a convenient point to put your ground probe.

**Dave Jones:** Perfectly fine probing just for, you know, troubleshooting around and stuff like that. And we've got big mains magnetic stuff in here. Yes, I've got my Chinese takeaway oopsie protection here.

**Dave Jones:** Anyway, big magnetic components inside here when you switch on, there's a lots of DVDT, okay? The changing magnetic a field, which then couples over to your grounding loop over here.

**Dave Jones:** And I've done videos on probing and and things like that. So, obviously, that's being picked up, okay? So, that poor probing explains why we'd get stuff on there. Still doesn't explain why it's triggered at that point when our trigger level is up here.

**Dave Jones:** Let's go back to our Keysight scope here and do the same thing yet again. So, let's single shot capture, but we'll take our time base out to, I don't know, like a millisecond per division, something like that.

**Dave Jones:** Bingo. Look at this. Once again, very faint unless we zoom in, but ta-da! Look at that. There you go. We've got huge amount of stuff in here, which, by the way, depending on how your scope implements the sine x on x interpolation.

**Dave Jones:** If it does it like updates it based on display data, you'll see this being a nice smooth sine x on x thing here, but the key side is being true and it's just telling us where it got those sample points there.

**Dave Jones:** So, yeah, anyway, so this is all switch on glitch that we got coupled via our probe down here from all the magnetics how it was switching on or whatever's happening over here was coupling over to this big coil over here into the ground system and that was impacting and this goes right back to like my old videos about the anti-static chair thing where way back, if you remember that, like a

**Dave Jones:** decade ago where I stood up from the chair and I could cause impulses on my scope via coupling in via the ground system and things like that. Anyway, fascinating old video that one, but you can see that's why it triggered at that point there, right?

**Dave Jones:** So, it certainly did trigger at the right location and the key side is showing us that true trigger, but unfortunately, because we're at such a slow time base now, we can't actually see that because the these pulses occur a couple of 100 milliseconds before what was happening over here.

**Dave Jones:** So, you know, we might have to set it back to say 100 milliseconds or something like that. Let's go even down to say 50. Maybe we can capture that and if we put if we move, you want to see more post trigger data, you can move your trigger point over to here, for example.

**Dave Jones:** I don't like putting it right over here. I like to get a little bit of pre-trigger here so on on the screen. So, I I usually set it over to the one reticule one division over like this and we trigger again and on, bingo.

**Dave Jones:** Once again, like we we got it. So, we can actually go faster. Let's go for broken and try 10 milliseconds, shall we? So, let's yeah, look look at that, okay?

**Dave Jones:** So, let's take it over here and let's try that again. No. But, check this out. Here's our trigger point, the key site. Even at that fast time base is still not showing genuinely what's going on in here.

**Dave Jones:** It hasn't picked it up. So, whether or not it picks it up or doesn't is kind of like a Well, it's I'm not going to say random, but it's kind of, you know, you just don't know.

**Dave Jones:** And if Murphy's not on your side that day, you'll you know, you won't see anything there. So, as I said, what's actually going on here is that the trigger system inside the oscilloscope is a separate analog system to the analog-to-digital converter and what's displayed on the screen.

**Dave Jones:** And especially if you use like your external trigger input as well, that'll you know, it's physically a different channel. It's not taking that from the analog-to-digital converter. So, there can be, and this is the trap for young players, there can be trigger signals which are which your oscilloscope is genuinely seeing and genuinely triggering off or your trigger circuitry is seeing, but your analog-to-digital converter is not.

**Dave Jones:** So, how can we solve this problem? Well, as it turns out, oscilloscope manufacturers have thought of this and they implement trigger filtering. So, if we go into our mode coupling menu here, there's actually to most scopes you'll have these two options.

**Dave Jones:** They'll have noise rejection and high frequency rejection like this. Now, if we turn on noise rejection, what this does is that it actually implements a hysteresis type action on the trigger so that it's more resilient to noise.

**Dave Jones:** All right, so let's try that again. I've got noise rejection turned on and 100 ms per division. Let's switch that on. See if it makes a difference. Nope. Unfortunately, that hasn't done it.

**Dave Jones:** And once again, there's a there's a little something doing down there, but obviously some sort of impulse is getting into the trigger system and the ADC is just not seeing that based on the sample rate and the memory depth and everything else, right?

**Dave Jones:** So, let's go high frequency rejection. Let's try that. I think we might have a winner winner chicken dinner because on the key side here, the high frequency reject is around about 50 kHz.

**Dave Jones:** So, it'll reject It's an analog filter. It'll reject anything like above that. And we're specifically probing like essentially low frequency stuff here. I E the ramp up of a power supply.

**Dave Jones:** So, high frequency reject is the more correct thing to use here. So, I can pretty much guarantee you this is going to work. Where were we? 100 ms per division.

**Dave Jones:** Bingo. Winner winner chicken dinner. There is our trigger level right there. There's some noise on that, but yep, it triggered at the exact point that we told it to.

**Dave Jones:** Huh, funny that. So, there you go. Let that be a lesson to you. Um these options exist for a reason. Maybe I could find like a better example of where noise rejection works.

**Dave Jones:** I won't do that in this video, but high frequency reject is what we want here cuz we've got like, you know, even though yes Fourier and fast changing waveforms very high frequency blah blah blah, but in this particular case, we want to reject any any sort of high frequency stuff in this case for this scope above 50 kHz.

**Dave Jones:** It's probably going to be similar for other scopes. It's in the order of, you know, tens of kHz, something like that perhaps. You'll have to read the data sheet.

**Dave Jones:** Hopefully they'll tell you for your scope, but we want to eliminate all of that stuff into our trigger system. And now with high frequency reject option on for our triggering, you can guarantee that this is going to work every time.

**Dave Jones:** And those little glitchy things picked up by in this case poor probing, but adequate probing for the task at hand. You know, just really just looking at in this case I'm just troubleshooting the PCB.

**Dave Jones:** You'll have to support us seeing the other video to know what I'm actually doing here. And you know, it's like adequate probing for just you know, probing around. We don't necessarily care about signal integrity.

**Dave Jones:** Just making sure signals are there. You know, and they're doing the right thing and stuff like that. So, yeah. But you can come a cropper when you try and trigger off something like that with nearby magnetic components which then couple into your ground system.

**Dave Jones:** Yes, we could get out our little high frequency attachment thing there, but then you've got to hold it on there. And hopefully I might actually do another interesting video which follow follows on from this which shows about you know, a neat little tip for when you're probing stuff like this and you don't have many hands and you don't have many places to hook your probe on.

**Dave Jones:** Anyway, okay. Just to show you a real deep memory scope here. We've got this new Siglent 5000X. We've set it for 250 meg memory here. We're at 100 milliseconds per division.

**Dave Jones:** So, let's do exactly the same thing as before. Bingo. There's our There's our trigger point once again. Like my trigger point is like smack in the middle here. But if we zoom right in here, yes, we can actually see Look, we have to go right in.

**Dave Jones:** Look how high frequency this is. It's 20 nanoseconds per division, right? There it is. It's just above. There you go. It just peaked above our trigger level here and that's why it triggered on that point.

**Dave Jones:** And you can see that it's doing the on-screen sign X on X interpolation. The waveform actually doesn't, you know, well, it's not necessarily looking like that. It is just interpolating that where the actual You can go Well, we can actually switch that off.

**Dave Jones:** There we go. There we go. We can switch Ah, jeez, that purple's not easy to see, is it? Um, sorry about that. But, uh, yeah, there you go. It switches on like that, and sine x on x.

**Dave Jones:** But, you can see that with enough memory, we were able to capture that. And if we go down to like uh, well, you know, 2 and 1/2 meg of memory or something like that, we simply won't see that.

**Dave Jones:** 100 milliseconds per division. And off. Single shot. And then, capture. And bingo. Without that memory, we're just not going to see that data in there. We We're just not going to get it.

**Dave Jones:** Um, but of course, it's gone into the trigger system. So, this scope, interestingly though, if we go into uh, where's our trigger setup? If we go in here, we've only got noise rejection.

**Dave Jones:** We don't have high frequency rejection. But, let's turn noise rejection on here, and see if that does the business. 100 milliseconds per division. Single shot capture. And Nope. Look at that.

**Dave Jones:** Still doesn't do it. And in the case of the Siglent 5000, we can just go into coupling here. It doesn't have a separate option. You've got to actually go into the coupling for to get the HF reject.

**Dave Jones:** And we're good to go. There it is. Sweet. And this actually might be an example where I you see the noise on the signal there? Where where your noise reject might actually come in, because if you had like maybe just some higher noise there.

**Dave Jones:** We don't actually know how much the hysteresis is, whether it's like half a division, a division, or whatever. We We just don't know, unless you Uh, the manual doesn't actually tell you that, unless you uh, experiment with it.

**Dave Jones:** I guess you could eventually find out. But, uh, yeah, like if you had like a glitch over here, and you're really critical about your trigger point and stuff like that, um, then you might want to turn on your noise reject as well.

**Dave Jones:** So, there you go. I hope you found that video useful and interesting. If you did, please give it a big thumbs up as always and discuss down below. But, we saw what the high-frequency filter rejection option is capable of on our scope that has that.

**Dave Jones:** So, anyway, I just thought that was a really cool example which I I didn't set up. I I simply uh stumbled across this while I was doing um troubleshooting a repair of a product.

**Dave Jones:** So, yeah, it's fascinating. Catch you next time.
