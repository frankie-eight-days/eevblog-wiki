---
video_id: GZHnrGIK9V8
title: EEVblog #1320 - Premature Oscilloscope Triggering
url: https://www.youtube.com/watch?v=GZHnrGIK9V8
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 27, "3": 42, "4": 51, "5": 67, "6": 86, "7": 102, "8": 121, "9": 139, "10": 158, "11": 178, "12": 198, "13": 217, "14": 230, "15": 246, "16": 259, "17": 278, "18": 301, "19": 320, "20": 334, "21": 352, "22": 368, "23": 381, "24": 396, "25": 410, "26": 426, "27": 444, "28": 460, "29": 474, "30": 489, "31": 504, "32": 518, "33": 533, "34": 548, "35": 560, "36": 574, "37": 592, "38": 603, "39": 621, "40": 636, "41": 652, "42": 669, "43": 686, "44": 701, "45": 716, "46": 733, "47": 753, "48": 766, "49": 779, "50": 792, "51": 805, "52": 821, "53": 834, "54": 847, "55": 859, "56": 873, "57": 891, "58": 907, "59": 921, "60": 935, "61": 946, "62": 965, "63": 982, "64": 999, "65": 1014, "66": 1025, "67": 1036, "68": 1045, "69": 1059}
---

**Dave Jones:** Hi, I wanted to show you a trap for young players about triggering on an oscilloscope and I found this while doing a repair video here which my uh patrons and subscribe star and uh forum supporters have already seen. I've done

**Dave Jones:** like a 35-minute video or a progress repair. Anyway, I haven't uh completed it yet. I need uh some parts for it. Anyway, they've already seen that video which is interesting. But, more to come on that perhaps. Hopefully, I fix it.

**Dave Jones:** Anyway, I wanted to show you something interesting here. Now, what I'm doing is I'm just uh triggering off uh the 3.3 V rail here and I'm just going to power up this scope. So, what what I've got here

**Dave Jones:** is it's just on channel two here. My trigger level is just like, you know, set to the middle of the uh 3.3 V waveform here. Okay, so what I'm going to do, I'm going to set it to a slow

**Dave Jones:** time base like 500 ms uh per division. I've got my pro Let's switch the product off. Okay, I'm going to trigger on the rising edge. We expect to see a trigger point right in the middle there. So, here we go.

**Dave Jones:** Uh Hmm. Something's a bit strange. What's going on here? There's our trigger point right in the middle there, yet here's our trigger edge over here. But, I know what you're thinking. Oh, Dave, there's some some there's obviously something in there. We

**Dave Jones:** have to zoom in and see um what it's actually triggered on. Well, okay, I'm zooming in. I'm zooming in. I'm zooming in. I'm zooming in. Um there's nothing there. Here's our trigger point, right? Our Our trigger point's right up here at

**Dave Jones:** like, you know, a volt and a half or something. So, it's got to rise above based on our trigger rules here. Our edge trigger uh positive going slope, it must this signal must transition above our trigger level there before it will trigger, but

**Dave Jones:** there is nothing there. There's absolutely nothing. Our positive going edge is all the way over here. What's going on? So, just for kicks, let's choose another scope here, signal in 1,100, whatever, channel two, slope rising edge, our trigger levels, you know, round about 2

**Dave Jones:** volts, something like that. So, let's switch our thing off, single shot, let's switch it back on, and capture where you know, that was just the decay of the power supply, and let's switch the product on. There it is.

**Dave Jones:** Bueller. Bueller. Look at this. It's There's our trigger point right in the middle, yet we're triggering over here, and there's nothing. I can zoom all the way in there, and there's absolutely waveform extended to the maximum.

**Dave Jones:** Anyway, there's nothing there. Why is it triggering here and when our true rising edge is over here? Really got a trap for young players here. All right, so what's actually going on here is that there's not necessarily a correlation between what

**Dave Jones:** is captured by the analog to digital converter and displayed on your screen and what's actually captured by the trigger circuitry, the analog trigger circuitry inside your oscilloscope. So, maybe there's there really is something happening in in here in the trigger

**Dave Jones:** search circuitry of this scope because it's not going to trigger on nothing. Okay? It's going to It's going to be triggering on something, but why can't we see it on the screen? Aha, we don't have enough detail. We don't have enough

**Dave Jones:** sample memory. So, let's go into a choir here. Memory depth of 1.4 meg, that's pretty good, right? Please quit stop Please quit stop mode. Oh, jeez. Anyway, God, really? Really? I can't change memory depth in stop mode. Let's go to

**Dave Jones:** 14 meg. Okay, let's repeat the exact same thing, exact same time base, cuz the time base is going to matter. Single shot capture that.

**Dave Jones:** Let's zoom in. See what we get. Aha, we start to see some funny business here, but it's still and there's a couple of glitches over here. Look, you can see these, right? They're almost at the trigger level there, but not quite. They're still

**Dave Jones:** nothing there. We still can't see it. Well, let's We're at 100 milliseconds per division before, weren't we? Let's go down to say 10 milliseconds per division. And let's do it again. Single shot capture, 14 meg memory depth. Bingo. Look at this.

**Dave Jones:** There you go. Oh, no, it's still not It's still not enough. Look, it's still not enough. There is still There's our There's our trigger point. There's still There's our trigger level right there. It's still not high enough. But, it is still There's a couple over

**Dave Jones:** here. Now, I hopefully you can see those. They're very faint. Maybe the light's off. So, yeah, we can go into the horizontal here, then we can zoom in on that. There There certainly are some glitches in here, which are

**Dave Jones:** well above that trigger level there. So, you know, it would trigger on that, but that's not the point it actually triggered. It It triggered all the way back in here, where there's nothing. So, hmm, we're still not seeing what's going

**Dave Jones:** on here. But, anyway, where's all this funny business coming from? Well, if you're experienced in probing, you'll no doubt see where we've come a gutsy here. Look at this, big antenna earth loop here, right? This big ground plot probe,

**Dave Jones:** cuz we're being lazy in our probing, right? We're just probing the power supply. We don't, you know, necessarily care that much about high frequency signal integrity. Big ground loop here, okay? It's even worse, cuz we've got this additional one coming over here,

**Dave Jones:** but it's just a convenient point to put your ground probe. Perfectly fine probing just for, you know, troubleshooting around and stuff like that. And we've got big mains magnetic stuff in here. Yes, I've got my Chinese takeaway oopsie protection here. Anyway,

**Dave Jones:** big magnetic components inside here when you switch on, there's a lots of DVDT, okay? The changing magnetic a field, which then couples over to your grounding loop over here. And I've done videos on probing and and things like

**Dave Jones:** that. So, obviously, that's being picked up, okay? So, that poor probing explains why we'd get stuff on there. Still doesn't explain why it's triggered at that point when our trigger level is up here. Let's go back to our Keysight scope here and do

**Dave Jones:** the same thing yet again. So, let's single shot capture, but we'll take our time base out to, I don't know, like a millisecond per division, something like that. Bingo. Look at this. Once again, very faint unless we zoom in, but ta-da! Look

**Dave Jones:** at that. There you go. We've got huge amount of stuff in here, which, by the way, depending on how your scope implements the sine x on x interpolation. If it does it like updates it based on display data, you'll

**Dave Jones:** see this being a nice smooth sine x on x thing here, but the key side is being true and it's just telling us where it got those sample points there. So, yeah, anyway, so this is all switch on glitch

**Dave Jones:** that we got coupled via our probe down here from all the magnetics how it was switching on or whatever's happening over here was coupling over to this big coil over here into the ground system and that was impacting and

**Dave Jones:** this goes right back to like my old videos about the anti-static chair thing where way back, if you remember that, like a decade ago where I stood up from the chair and I could cause impulses on my scope via coupling in via the ground

**Dave Jones:** system and things like that. Anyway, fascinating old video that one, but you can see that's why it triggered at that point there, right? So, it certainly did trigger at the right location and the key side is showing us that true

**Dave Jones:** trigger, but unfortunately, because we're at such a slow time base now, we can't actually see that because the these pulses occur a couple of 100 milliseconds before what was happening over here. So, you know, we might have to set it back to

**Dave Jones:** say 100 milliseconds or something like that. Let's go even down to say 50. Maybe we can capture that and if we put if we move, you want to see more post trigger data, you can move your trigger point over to here, for example.

**Dave Jones:** I don't like putting it right over here. I like to get a little bit of pre-trigger here so on on the screen. So, I I usually set it over to the one reticule one division over like this and

**Dave Jones:** we trigger again and on, bingo. Once again, like we we got it. So, we can actually go faster. Let's go for broken and try 10 milliseconds, shall we? So, let's yeah, look look at that, okay? So, let's take

**Dave Jones:** it over here and let's try that again. No. But, check this out. Here's our trigger point, the key site. Even at that fast time base is still not showing genuinely what's going on in here. It hasn't picked it up. So, whether or not

**Dave Jones:** it picks it up or doesn't is kind of like a Well, it's I'm not going to say random, but it's kind of, you know, you just don't know. And if Murphy's not on your side that day, you'll you know, you

**Dave Jones:** won't see anything there. So, as I said, what's actually going on here is that the trigger system inside the oscilloscope is a separate analog system to the analog-to-digital converter and what's displayed on the screen. And especially if you use like your external

**Dave Jones:** trigger input as well, that'll you know, it's physically a different channel. It's not taking that from the analog-to-digital converter. So, there can be, and this is the trap for young players, there can be trigger signals which are which your oscilloscope is

**Dave Jones:** genuinely seeing and genuinely triggering off or your trigger circuitry is seeing, but your analog-to-digital converter is not. So, how can we solve this problem? Well, as it turns out, oscilloscope manufacturers have thought of this and they implement trigger

**Dave Jones:** filtering. So, if we go into our mode coupling menu here, there's actually to most scopes you'll have these two options. They'll have noise rejection and high frequency rejection like this. Now, if we turn on noise rejection, what this does is that it actually implements

**Dave Jones:** a hysteresis type action on the trigger so that it's more resilient to noise. All right, so let's try that again. I've got noise rejection turned on and 100 ms per division. Let's switch that on. See if it makes a difference. Nope.

**Dave Jones:** Unfortunately, that hasn't done it. And once again, there's a there's a little something doing down there, but obviously some sort of impulse is getting into the trigger system and the ADC is just not seeing that based on the

**Dave Jones:** sample rate and the memory depth and everything else, right? So, let's go high frequency rejection. Let's try that. I think we might have a winner winner chicken dinner because on the key side here, the high frequency reject is around about 50

**Dave Jones:** kHz. So, it'll reject It's an analog filter. It'll reject anything like above that. And we're specifically probing like essentially low frequency stuff here. I E the ramp up of a power supply. So, high frequency reject is the more

**Dave Jones:** correct thing to use here. So, I can pretty much guarantee you this is going to work. Where were we? 100 ms per division. Bingo. Winner winner chicken dinner. There is our trigger level right there. There's some noise on that, but yep, it triggered at

**Dave Jones:** the exact point that we told it to. Huh, funny that. So, there you go. Let that be a lesson to you. Um these options exist for a reason. Maybe I could find like a better example of where noise

**Dave Jones:** rejection works. I won't do that in this video, but high frequency reject is what we want here cuz we've got like, you know, even though yes Fourier and fast changing waveforms very high frequency blah blah blah, but in this particular

**Dave Jones:** case, we want to reject any any sort of high frequency stuff in this case for this scope above 50 kHz. It's probably going to be similar for other scopes. It's in the order of, you know, tens of kHz, something like that perhaps. You'll

**Dave Jones:** have to read the data sheet. Hopefully they'll tell you for your scope, but we want to eliminate all of that stuff into our trigger system. And now with high frequency reject option on for our triggering, you can guarantee that this

**Dave Jones:** is going to work every time. And those little glitchy things picked up by in this case poor probing, but adequate probing for the task at hand. You know, just really just looking at in this case I'm just troubleshooting the PCB. You'll

**Dave Jones:** have to support us seeing the other video to know what I'm actually doing here. And you know, it's like adequate probing for just you know, probing around. We don't necessarily care about signal integrity. Just making sure signals are there. You

**Dave Jones:** know, and they're doing the right thing and stuff like that. So, yeah. But you can come a cropper when you try and trigger off something like that with nearby magnetic components which then couple into your ground system. Yes, we

**Dave Jones:** could get out our little high frequency attachment thing there, but then you've got to hold it on there. And hopefully I might actually do another interesting video which follow follows on from this which shows about you know, a neat

**Dave Jones:** little tip for when you're probing stuff like this and you don't have many hands and you don't have many places to hook your probe on. Anyway, okay. Just to show you a real deep memory scope here. We've got this new Siglent 5000X. We've

**Dave Jones:** set it for 250 meg memory here. We're at 100 milliseconds per division. So, let's do exactly the same thing as before. Bingo. There's our There's our trigger point once again. Like my trigger point is like smack in the middle here. But if

**Dave Jones:** we zoom right in here, yes, we can actually see Look, we have to go right in. Look how high frequency this is. It's 20 nanoseconds per division, right? There it is. It's just above. There you go. It just peaked above our trigger level here

**Dave Jones:** and that's why it triggered on that point. And you can see that it's doing the on-screen sign X on X interpolation. The waveform actually doesn't, you know, well, it's not necessarily looking like that. It is just interpolating that

**Dave Jones:** where the actual You can go Well, we can actually switch that off. There we go. There we go. We can switch Ah, jeez, that purple's not easy to see, is it? Um, sorry about that. But, uh, yeah, there you go. It switches on like that,

**Dave Jones:** and sine x on x. But, you can see that with enough memory, we were able to capture that. And if we go down to like uh, well, you know, 2 and 1/2 meg of memory or something like that, we simply

**Dave Jones:** won't see that. 100 milliseconds per division. And off. Single shot. And then, capture. And bingo. Without that memory, we're just not going to see that data in there. We We're just not going to get it. Um, but of course, it's

**Dave Jones:** gone into the trigger system. So, this scope, interestingly though, if we go into uh, where's our trigger setup? If we go in here, we've only got noise rejection. We don't have high frequency rejection. But, let's turn noise rejection on here, and see if that does

**Dave Jones:** the business. 100 milliseconds per division. Single shot capture. And Nope. Look at that. Still doesn't do it. And in the case of the Siglent 5000, we can just go into coupling here. It doesn't have a separate option. You've

**Dave Jones:** got to actually go into the coupling for to get the HF reject. And we're good to go. There it is. Sweet. And this actually might be an example where I you see the noise on the signal there? Where where your noise

**Dave Jones:** reject might actually come in, because if you had like maybe just some higher noise there. We don't actually know how much the hysteresis is, whether it's like half a division, a division, or whatever. We We just don't know, unless

**Dave Jones:** you Uh, the manual doesn't actually tell you that, unless you uh, experiment with it. I guess you could eventually find out. But, uh, yeah, like if you had like a glitch over here, and you're really critical about your trigger point and

**Dave Jones:** stuff like that, um, then you might want to turn on your noise reject as well. So, there you go. I hope you found that video useful and interesting. If you did, please give it a big thumbs up as

**Dave Jones:** always and discuss down below. But, we saw what the high-frequency filter rejection option is capable of on our scope that has that. So, anyway, I just thought that was a really cool example which I I didn't set up. I I simply uh

**Dave Jones:** stumbled across this while I was doing um troubleshooting a repair of a product. So, yeah, it's fascinating. Catch you next time.
