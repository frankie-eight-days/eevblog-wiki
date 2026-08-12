---
video_id: pHbooMWS0bU
title: EEVblog #707 - Rigol Oscilloscope Probe Performance
url: https://www.youtube.com/watch?v=pHbooMWS0bU
source: youtube-asr
---

**Dave Jones:** Hi, this is going to be a quick video. I know I always say that, but anyway, I'll do my best. This is in response to a thread on the EV blog forum from a user lightages and it concerns the Rigol

**Dave Jones:** probes that come with the new DS1054Z oscilloscope and you've seen the review on this. They're the RP2200 model here. They're a nominal bandwidth rated bandwidth of 150 MHz, which is you know, reasonable for a 100 MHz scope. But the issue he had was that he

**Dave Jones:** actually compared it with the RP3300 probes. These are a nominal 350 MHz bandwidth probes and these come with the Rigol DS2000 series scope, which is a 200 MHz scope. So you get 350 MHz probes with that, which is more than

**Dave Jones:** enough. But he had a he did a test comparison between these two probes and he didn't think that these probes were suitable although actually affecting the bandwidth performance of the Rigol DS1054Z if it was you know, hacked up to 100 MHz

**Dave Jones:** or you bought the 100 MHz model. And here's a screenshot he did between the two and it looks drastically different. As you can see the yellow waveform is the 350 MHz probe. So he is suggesting that these Rigol RP2200

**Dave Jones:** series probes actually affect the performance. Contrary to what I said in the video, I said that well, these RP2200 probes at 150 MHz were really good enough and shouldn't affect the system bandwidth. In theory, that wasn't quite right, but historically,

**Dave Jones:** oscilloscopes have always come with the same rated bandwidth probes as the bandwidth of the oscilloscope. So that's what I meant by you know, they're pretty good cuz you're getting 150 meg probes with a 100 MHz scope. So is it any good? Can we reproduce the

**Dave Jones:** problem that Lightages has seen? Let's find out. So, just a quick comparison of the specs here. This is the 2200, this is the 3300. Input capacitance is basically the same and by the way, we're only talking about times 10 mode here. So,

**Dave Jones:** 17 puff as opposed to a slightly lower 16 puff on the 350 MHz bandwidth as opposed to 150 meg and of course, you'd expect the corresponding rise time to be different. But apart from that, they're basically the same input capacitance.

**Dave Jones:** And there is one difference to note between the probes. The 2200 one is compensated at the probe tip here. There's a little adjustment and the 3300 is compensated at the end of the cable. It's neither here nor there. They're

**Dave Jones:** just different ways to do it. These higher frequency probes, it's most common to have them compensated at the connector end here rather than on the probes. Just the way it is. Now, the ground leads are different lengths. This

**Dave Jones:** is the 3300 350 meg probe is actually longer than the RP2200 and that's going to make a difference if you're probing like that. We won't use those today. We'll ignore them. That could be the source of Lightages' problem, but he

**Dave Jones:** actually mentioned on the forum that his ones were actually the same length. So, yeah, maybe mine are just different than what he's got. But anyway, now I said before that it wasn't really right when I said that, well, 150 meg probes won't

**Dave Jones:** affect the bandwidth of a 100 meg scope. Not strictly true, but you know, like in the real world, it's like it's near enough. Like if you want to look into it, this isn't precisely correct, but what you need to look at is the entire

**Dave Jones:** system bandwidth and a lot of oscilloscope manufacturers, the big ones, will actually specify the the total system bandwidth based on the matching probe they supply and the scope itself. Anyway, if you want to add bandwidths together like this, i.e. the

**Dave Jones:** bandwidth of the total system that includes the scope and the probe, then this is a standard formula for adding two together. Just one on the the bandwidth of the scope, one on the bandwidth of the probe, square those and

**Dave Jones:** square root that one on, and you punch that in the calculator and you get around 83.2 MHz, but that's not going to be the true answer really cuz it's all to do with actual rise times of this the

**Dave Jones:** probe and the scope and the signals and everything else, but it's going to be ballpark. So, adding a 150 meg probe does actually reduce the bandwidth of your scope, you know, somewhat. Possibly not nearly as much as this, but anyway, that's what happens.

**Dave Jones:** So, yeah, it is going to reduce it just a bit. And you can never have too many scopes for a test. Let's go. So, what I've got is the Rigol DS1054Z, and yes, it has been upgraded to the 100

**Dave Jones:** MHz bandwidth, and I've got my Rigol function gen here, which is just generating a 1 kHz square wave, and I have a matching terminator here just so that we can probe a signal with a known termination. So, I'm going to use each

**Dave Jones:** probe here. Yes, we're going to ditch these ridiculous antenna earth leads, and we're going to use one of these probe to BNC adapters like this so we can get right on there and probe the signal. Let's give it a whirl. So, first

**Dave Jones:** up, the RP2200, the probe that actually comes with the Rigol DS1054Z. You plug it in, and yes, I have got my little adjustment tool going in there and compensated that 1 kHz signal. Okay? So, we zoom into that, and we

**Dave Jones:** notice, hey, look at that. We're getting a couple of wigglies on there. That's going to be normal because of this function generator may not be perfect. We've got little load mismatches, all sorts of things happening there, but it

**Dave Jones:** gives us a good benchmark to actually compare probes to. So, although we're using our times 10 probe here, high impedance probe across our 50 ohm terminator here, it's going to make a difference because it has an input capacitance that we saw in the data

**Dave Jones:** sheet before that 16 or 17 pF what it is what it was. So, even with our 1 kHz signal here, that's it's not a low frequency signal we're measuring. We're interested in this i.e. we're not interested in the 1 kHz signal. We're

**Dave Jones:** interested in the high frequency component of that. So, due to the input capacitance and slight mismatches and all sorts of things, we're going to see a wiggle like that. Anyway, it doesn't the actual practicalities of that doesn't matter.

**Dave Jones:** We've got ourselves a good benchmark. That's 5 ns per division and that's pretty good. We just see a little bit of overshoot, little bit of ringing there and then it settles down pretty well. Okay, now we've got our RP3300 probe.

**Dave Jones:** I've tweaked that with my tongue at the correct angle. Okay, so that probe's compensated and looky what we get. No problems whatsoever. It's practically practically identical to what we got with the other probe. And yes, we've got the exactly the same probing

**Dave Jones:** configuration there. So, bingo, it's busted already. The RP2200 probe doesn't make any difference at all.

**Dave Jones:** So, let's try some other scopes as a comparison. I got the Rigol DS2000 series scope. This is a 200 MHz bandwidth, but because the bandwidth of the scope is going to matter, the good thing about this is that it does have a

**Dave Jones:** 100 MHz bandwidth limit. So, we've turned that on and because each oscilloscope is different and different input capacitance, we have to go in there and adjust the probe for each and every one. So, each uh probe we do on

**Dave Jones:** each different scope, we have to re-compensate. So, there's our RP2200 there. Look, looks practically identical. Let's not quibble about any minor differences in there, and you'll see that if we uh turn the bandwidth off, we'll get some higher frequency

**Dave Jones:** content in there because we're going to get extra ringing due to the now 200 MHz bandwidth, but we're using a 150 MHz bandwidth limited probe. And now we've got our RP3300 probe. That's with no bandwidth limit. So, this is a 350 MHz probe on a 200 MHz

**Dave Jones:** bandwidth scope. And of course, we can put down our on If you're on 20 MHz, it's just going to round it off like there's no tomorrow. Look at that. And there we go. Very similar to what we had

**Dave Jones:** before. So, those two uh Rigol scopes with those two probes, very similar sort of uh pulse uh performance as it's called between the two systems and the two different probes. Now, we're going to use a GW Instek uh GDS-2304 scope. It's

**Dave Jones:** a very nice uh 300 MHz um input bandwidth uh rated scope, and we've got the RP2200 150 MHz probe. Let's turn it on. And the reason I chose this scope is because it has a 100 MHz bandwidth limit. So, there we go.

**Dave Jones:** There's the 200. There's the full 300 MHz bandwidth. Not much difference between the full and the 200 MHz bandwidth, can see, because we're only using a 150 MHz probe here. But basically, exactly the same performance as the Rigol. Look at that. And once

**Dave Jones:** again, every scope is different, so we have to just uh tweak our uh adjustment pot there. Yes, tongue is at the right angle, and we can zoom in on that. This is now our RP uh 3300 350 MHz

**Dave Jones:** probe. And as you can see, it's uh basically very similar performance to what we're getting before and we should see a larger difference between the 200 and uh not a huge amount, but I think it is a little bit bigger

**Dave Jones:** uh difference than we got before cuz this is a 350 MHz probe. And bit of an old faithful scope here, the Tektronix TDS 3054 and uh it's please excuse the dim screen. Yes, it uh fades with time. This

**Dave Jones:** is the RP2200 series probe compensated. This doesn't doesn't have a 100, but it does have a 150. So, as you can see, the pulse response is a bit peakier on this uh Tektronix TDS 3054. Um it's more similar to the GW Instek in that

**Dave Jones:** respect. The Rigols seem to have a lower uh roll-off response in that respect, but it's neither here nor there. We're We're comparing probes here. And with the compensated uh 350 MHz probe here, quite similar response. So, there you

**Dave Jones:** go. It's confirmed on four different oscilloscopes that there is essentially uh very little difference between the RP3300 and the RP2200 probes. And if you want to see what that looks like on the Tektronix MDO uh 3000, which is a 1 gig

**Dave Jones:** uh bandwidth scope, this is the RP2200 probe. Once again, compensated. That's the full 1 gig bandwidth. You can see really really high frequency noise going all over there. Um it doesn't have anything close to the 100 MHz uh

**Dave Jones:** bandwidth. The nearest it's got is the 250 MHz. You can see some of that real high frequency content vanish, but effectively the uh the lower frequency um pulse response is, you know, very similar. So, there you go. That's it.

**Dave Jones:** And of course, the 20 MHz just rolls off. And this is the RP3300, practically identical. Look at that. No problems whatsoever. I think that's done and dusted. The bloody annoying Tektronix 1 2 4 sequence. This is just a

**Dave Jones:** 4 nanoseconds. What's that rubbish? Should be 125. So, there you go. I hope I cleared up Lightages concern that there was a significant performance difference on the DS1054Z at 100 MHz between these two different probes and that the RP2200

**Dave Jones:** probe that came with this thing was, you know, somehow no good. Well, it's Yeah, it's an okay probe. Nothing wrong with it. When you do control test like that, I can't see a difference on my probes anyway. And of course, there are more

**Dave Jones:** subtleties to actually measuring this. I'm not going to go through and actually sweep and get the bandwidth of these probes and all sorts of stuff. There's, you know, lots of little nuances in actually doing things like this. But anyway, I think that's a

**Dave Jones:** fairly decent test under exactly the same conditions. These probes pretty much produce the same result given the 100 MHz bandwidth scope. So, the 150 meg probe that comes with it more than good enough. Hope you enjoyed that. And if

**Dave Jones:** you want to discuss it, jump on over to the EVBlog forum. Catch you next time.
