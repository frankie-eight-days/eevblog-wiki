---
video_id: _Mup2VnXH_k
title: EEVblog #806 - Siglent SDG2000X Arb Function Generator First Look
url: https://www.youtube.com/watch?v=_Mup2VnXH_k
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 22, "2": 43, "3": 61, "4": 81, "5": 101, "6": 121, "7": 136, "8": 156, "9": 171, "10": 196, "11": 216, "12": 231, "13": 246, "14": 261, "15": 276, "16": 296, "17": 311, "18": 326, "19": 341, "20": 356, "21": 376, "22": 396, "23": 411, "24": 426, "25": 441, "26": 461, "27": 481, "28": 501, "29": 521, "30": 541, "31": 556, "32": 576, "33": 601, "34": 611, "35": 631, "36": 651, "37": 671, "38": 691, "39": 706, "40": 726, "41": 741, "42": 756, "43": 771, "44": 791, "45": 811, "46": 826, "47": 846, "48": 866, "49": 891, "50": 906, "51": 926, "52": 946, "53": 961, "54": 981, "55": 996, "56": 1016, "57": 1036, "58": 1051, "59": 1071, "60": 1086, "61": 1101, "62": 1116, "63": 1136, "64": 1156, "65": 1171, "66": 1191, "67": 1211, "68": 1231, "69": 1246, "70": 1261, "71": 1281, "72": 1301, "73": 1316, "74": 1341, "75": 1356, "76": 1371, "77": 1381, "78": 1401, "79": 1416, "80": 1431, "81": 1446, "82": 1461, "83": 1476, "84": 1491, "85": 1506}
---

**Dave Jones:** Hi, some people wanted me to take a look at the new Siglent STG2100X series TrueArb function generator, which starts at 499 US dollars, 1.2 gig sample per second, 120, this is a 120 megahertz model, the 499 one starts at 40 megahertz. They wanted me to take a quick look

**Dave Jones:** at actually using this thing and maybe plug the output into a spectrum analyzer or something before I have to send it back, and yep, we can do that, and we can compare it with the older model Siglent STG5082, and also we can have a quick comparison with the Rigol DG4162 as well,

**Dave Jones:** which you've seen in previous videos. So let's take a quick look, this certainly won't be comprehensive, but we'll just give it a go. And we've got some spectrum analyzers here, the Tektronix MDO3000, the Rigol DSA815, but I think the Tektronix has a better, we're getting a lower noise floor,

**Dave Jones:** and I've done a couple of quick tests, and I think we'll use the Tekt in this regard today. Now, of the three units here, I'll quickly recap the new Siglent STG2100 or 2000X series, the lowest model unit, the 40 megahertz one starts at 499 dollars, it's 1.2 gig

**Dave Jones:** samples per second, 40 megahertz for the entry level one up to 120 megahertz, 16-bit converter in it, as we saw in the teardown, true 16-bit converter with 16 meg of arbitrary memory. This older model Siglent, which they still sell, I'm not entirely sure why, but anyway,

**Dave Jones:** maybe they might discontinue it. Anyway, we've got it as a reference point, the STG5000 series, this one starts at 680 dollars for the 40, yeah, might be the 40 megahertz version once again, and that's got 512k of sample memory, so not nearly as much, and it's only got a

**Dave Jones:** 14-bit converter. And the Rigol DG4000 series, once again, it's only got a 14-bit converter as well, so that's where the new X series wins. It's got a 16-bit converter, 16 meg sample memory. So the entry level model of this, the DG4062 is 60 megahertz,

**Dave Jones:** this is the 160 megahertz top-of-the-line one, but the 60 megahertz bottom-of-the-range unit, it starts at 920 dollars, so much more expensive than the X series down here. But it's 60 megahertz bandwidth compared to 40 for the base model unit, but it's only a 14-bit converter and only 500 meg samples per second, this is

**Dave Jones:** more than twice as much at 1.2 gig samples per second, and this has only got 16k points sample memory as well. So, but as you can see, it's a different form factor. Rigol actually have the DG5000 series, I think it is, which is a similar form factor to these Siglents down here.

**Dave Jones:** So, which is probably a better comparison, this DG4000 is a bit different. This one has a lot more building waveforms, 130 building waveforms, much more comprehensive arbitrary waveform support built-in than either of the Siglents. So I'll just show you the waveforms on the Rigol here, much more comprehensive

**Dave Jones:** built-in waveforms than, I mean, it's just got a ridiculous array, you've got math functions, and this isn't even the complete list, you can actually scroll through these lists, trig functions, anti-trig functions, window functions, like, it's just, yeah, crazy. If you want built-in waveforms,

**Dave Jones:** this is the puppy to get. And in addition to all those arbitrary waveforms, the Rigol has a harmonic function as well. I don't, I haven't looked through the Siglent, but I don't believe it actually has harmonic functions, you can actually choose what type you want,

**Dave Jones:** odd or even harmonics, and the number of orders of your harmonics and the phase as well. So if you end up, you know, it's just a more flexible instrument, the Rigol, in terms of waveform generation. I mean, you can do that with the Siglents, because it's an R-generator, but you've got to do it yourself

**Dave Jones:** using whatever software to hook up and actually download the waveform to it. You can't do it from the front panel. Now if we go check out the waveforms on the Siglent, it does have, it's got all your basics, it does have built-in ARB functions as well, but not nearly as many as the

**Dave Jones:** Siglent, but it's got a decent amount. Let's have a look. We can actually, by the way, it's got true ARB function, which we'll have to take a look at, I think, anyway. The ARB type, we can do the built-in waveforms, okay? And it's a similar thing, I mean, we've got

**Dave Jones:** common ones here, we've got some math ones, we've got some, yeah, engines if you're doing, but I don't know why they've got cardiac pulse in engine, anyway. Bizarre. Anyway, they've got some Windows and Trigs, and that's, you know, basically it's a reasonable selection, but not as many, not as comprehensive as the Rigol.

**Dave Jones:** And in addition to the waveforms, we can do all your modulation, of course, that's all, you know, that's all pretty much on par. We can do sweeps as well, which is all fine and dandy, so no problems there at all. And we've got burst stuff as well, so it's alright, but as I said, doesn't have

**Dave Jones:** the harmonic feature if that's useful to you. But of course the Siglent is actually touchscreen, and I can go in there and actually touch, and I can select these menu items as well with the touchscreen, but I don't really see the point of the functionality of the touchscreen on this thing,

**Dave Jones:** quite frankly. I mean, you know, you can select a waveform, you can kind of sort of go in there and kind of get your finger on those, but if you've got a big finger, my finger's not big, it's quite small, but I'm having a hard time sort of, you know, getting on there, it's just easier to use

**Dave Jones:** the function button. So, the touchscreen, I'm going to say, eh, bit of a gimmick. I mean, it's not like you can go in there for your ARB one and actually like drawing a waveform with your finger or a little pointy thing or something, that'd be kind of novel, but

**Dave Jones:** yeah, like, it's, I don't get the point of the touchscreen really, I don't think I'd use it. And all these function generators are dual output here, so no problems whatsoever. User interface, I prefer the Siglent one, it's much more intuitive. The Rigol, as I said, the user interface on the Rigol is a pain in the ass.

**Dave Jones:** It really takes some getting used to, some really weird stuff, you know, tiny selection dots for your frequency, and ah, it's just, yeah, don't get me started. But both the Rigol and the Siglent, somewhat annoyingly, like, you'd expect you know, like, to have like an output menu here, but this is just like output

**Dave Jones:** on or off, which is, you know, which is fine, but how do you change the output load impedance, for example? Well, you can touch it there, but if we wanted to find that on the menu, you go into Utility here, and you go into Output Setup, and then that's where

**Dave Jones:** you do your load. You know, I don't know, I just, I don't, look, and it just popped back as well. So that's kind of a little bit annoying, that it doesn't stay in the menu there. So 50 ohms, bam, it just goes back.

**Dave Jones:** Don't like it. Anyway, I'm just going to whack the output of each of these signal gens onto the Tektronix MDO Spectrum Analyzer, and just have a look at the output. I'm just going to have a nominal 10 MHz sine wave, you know, half a volt

**Dave Jones:** peak to peak, and let's see what we get. And there it is, there's our 10 MHz carrier. We've got a couple little side components here. They're at 10.02, there we go, the markers have automatically 10.0291 and 9.97. They're at minus 92, where 2 dB, minus 2 dBm down on the carrier.

**Dave Jones:** So we're talking about, you know, minus 90 dBc there, or reference to the carrier there. And our noise floor there, looking, you know, just about, what, 105, minus 105 dBm, maybe? Let me disconnect the input and see what the noise floor of the scope is.

**Dave Jones:** And there we go, that's the scope noise floor, about, you know, minus 115 or something like that. And that's the exact same signal there on the Siglent SDG5082, the 5000 series. And as you can see, not nearly as good as the Siglent. Look at those

**Dave Jones:** sideband components. Wow, they are massive! So remember that's a 14-bit converter compared to the 16-bit in the X series, but jeez. Well let's take a look at the Rigol now. And there you go, that's the Rigol. I'll just save that, take a screenshot, and there you go.

**Dave Jones:** The sidebands here are a little bit higher, they're at minus 89, so you know, minus 86 or something relative to the carrier. And looks like we've got a little harmonic of that over here. So yeah, it's a little bit worse, but yeah, noise floor between

**Dave Jones:** them, there's not much doing. So once again, back to the Siglent X series, the new one, and as you can see, it's much much cleaner. But have we got a little something in there perhaps? Hmm. Let's tighten that span up a bit. We're at, what were we before?

**Dave Jones:** 200 kHz span, now we're at 50 kHz span, and there you go, just like, they're gone! Oh, didn't hold my tongue at the right angle. Doesn't matter, nothing doing there. And there's the output of the X series when we're looking at a 50 millivolt

**Dave Jones:** peak-to-peak signal here. So we're at minus 20 dBm reference now, and we're, look, that's clean as a whistle, we're back to 500 kHz span now. And there's the Siglent SDG5000 series, and once again, that ain't pretty. The X series, much much cleaner. And there's the output of the 5000 series Siglent with the

**Dave Jones:** span set to 20 kHz, so you can see those components a bit better. And there's the output of the RIGOL, and once again, that's, you know, it's not too far off the Siglent, but the Siglent X series is actually a cleaner output. Look, lower sidebands.

**Dave Jones:** And we'll just check the spurious performance of the RIGOL here, the 4000 RIGOL, and once again we've got our 50 millivolt peak-to-peak carrier at 10 MHz here. You can see some components, the highest one here is at almost minus dBm down there, but you know, that's reasonably clean.

**Dave Jones:** Our span is over 100 MHz now, so let's check that on the Siglent. And that's the Siglent 5000 series, and look at that! What's going on there? No idea what that business is, but anyway, it's similar to the RIGOL. And there is the new X series

**Dave Jones:** with, you know, decent performance. Well, let's put the new Siglent X series up to 80 MHz, there we go, that's its performance. Once again, 50 millivolts peak-to-peak minus 22 dBm. And check out the Siglent 5000 series, once again we've got some weirdness happening down here, some decent peaks, so not nearly as

**Dave Jones:** clean as the new X series. Hmm. And there's the RIGOL DG4000, clean as a whistle. And as a reference, this is the output of my Marconi 2023 signal generator. Yeah, it's a bit higher performance, although I don't know what's going on here down at the low end though, but

**Dave Jones:** yeah, look at that. Clean as a whistle. And there's my Marconi for those who haven't seen it. It's pretty schmick. And I'm going to have a whinge again about the Tektronix MDA3000. It's as slow as a wet week. Look, it doesn't even detect button presses when you've got a really

**Dave Jones:** low-resolution bandwidth filter on the thing. So it just becomes unresponsive. It's... ahhh! It's really rather annoying. But hey, it does perform. Ooh, it popped up eventually. Half the time it doesn't. But yeah, only when it's set to those low-resolution settings. Menu off, dammit!

**Dave Jones:** Menu off! Ah, I'll just show you while I found it. You can actually upgrade the bandwidth with a license key on this thing. So if you buy the 40 MHz model for $499 bucks. Sorry, jeez, $199 would be a bargain. $499, which is still a bargain.

**Dave Jones:** Yes, you can actually, presumably, buy a license key and upgrade that. I don't know how much that costs though. Alright, let's have a look at its square wave performance. I've just got a 1 MHz square wave, 1 volt peak-to-peak on the output here.

**Dave Jones:** And I've got some averaging set on the scope, of course. And we get a little bit of ringing there, but that's exactly what you'd expect. Yes, I am 50 ohm input terminated on the scope, by the way. So that's no problems at all.

**Dave Jones:** Let's switch that over. In fact I'll leave it right there, and I'll switch it over to the Siglent 5000. You can see the averaging doing its business there. And the Siglent 5000, there we go. That one's a you can argue it's a little bit cleaner, but the

**Dave Jones:** you can tell the higher sample rate of the Siglent X series on there. No problems whatsoever. So that's a winner. Let's go to the Rigol, exactly the same signal. And there we go. It's very similar. Got a little bit of something happening there, but you know, like

**Dave Jones:** it doesn't matter. They're all fine. And by the way, the fastest rise time you can get on this is 8.4 nanoseconds, whereas fastest rise time on the Rigol, 5 nanoseconds. So just a little bit faster edge rate. And Siglent claimed to have this easy pulse technology.

**Dave Jones:** And here's an explanation from the data sheet here. It tells you that if the impulse mode, if the output frequency is not an integer multiple of the clock rate, then well you're going to get a one clock sample jitter on the thing. And well, I set up the same

**Dave Jones:** conditions that they've got here, and I cannot reproduce that on the Rigol 4000. So the Rigol 4000 doesn't have the same problem. I'll plug the exact same signal here into the Siglent X-Series, there it is. Siglent X-Series, so what I'm doing is I'm measuring the

**Dave Jones:** rising edge, I'm triggering here, measuring, looking at the rising edge here. So that's the Siglent X-Series, and there's your Rigol. Eh, no difference. And that's using the exact same condition they have with the 1.01 megahertz 50% duty cycle pulse waveform. But here's where the Siglent X-Series has a massive advantage with this

**Dave Jones:** easy pulse thing. If you generate a 10 hertz, like very low frequency pulse waveform, it still allows the rising and falling edges to be that minimum 8.4 nanoseconds. And you might think, well yeah, that's ordinary, but let's have a look at the Rigol.

**Dave Jones:** Okay, we're in pulse mode, the same 10 hertz, but the like trailing edge and leading edge, okay? Look, it's set it to a minimum of 195 microseconds. Look, if I try and put in 1 nanosecond, it'll tell me the minimum is 195 microseconds.

**Dave Jones:** That's the limitation the DDS technology used in the Rigol, but the Siglent doesn't have that. Let me show you on the scope. And I've got a 10 hertz output here, but as you can see, they're not the same edge, because they're, it's the classic

**Dave Jones:** two free-running clocks issue. It's a trap for young players. I just wanted to show you this. If you've got two free-running oscillators like we have here, you don't know where it's, where they're going to start relative from one to the other. So you've either got to reference them from the same

**Dave Jones:** master clock, or trigger them in some way, or maybe actually set a delay output or something like that. So yeah, I just wanted to show you that classic problem with two separate free-running clocks. I always love that. And eventually, if you sit there long enough, and they're not both exactly 10 megahertz reference, I've done a

**Dave Jones:** video on this measuring clock drift. You'll actually see them slowly drift relative to each other. So if we wait long enough, and they're not both exactly 10 megahertz oscillators inside that, well they don't actually have to be 10 megahertz precisely, but they have to be exactly the same.

**Dave Jones:** Otherwise, if they're not exactly the same, you'll see them slowly start to drift. And I'm buggered if I can find a way to actually synchronize or trigger the start of the pulse signal here to the external input. Like there's an external in-out on the back, which you can use for sweep mode, I believe, to start the sweep.

**Dave Jones:** But not in pulse mode, so I... bleh! Anyway, it doesn't matter, because we can do it with the delay. We can just tweak the value, hold your tongue at the right angle until you get the signal, or you can actually measure it on the scope and then just

**Dave Jones:** punch it in. Okay, I found what I would call a bug, okay? We've got our buttons here which select our cursor position, right? Everything's hunky-dory. So if I want to adjust the delay like this, right? It works fine. But look, what happens if I go over here, and then I go

**Dave Jones:** down like this? 76, 75, 4, 3, 2, 1. Look what happens, it jumps cursor position over, and then goes to the next digit. Damn, that's annoying! That is really freaking annoying. Why have they done that? It's got to be a bug, surely. Because it doesn't do it in the up direction,

**Dave Jones:** it stays put, only on the down direction. Grrr! Anyway, it turns out I can't fix this delay, because we've got a maximum of 100 milliseconds delay here, so we can't actually get the waveform over. I'm going to have to invert it on the scope

**Dave Jones:** to actually be able to line up these waveforms. So that's just a bit of bad luck. I mean, you know, look, if I adjust the delay, look, see? We can, that's that feature there, jumping down by one. Grr, that bug I was telling you about.

**Dave Jones:** See, we can't quite get there. We can get with the different edge here, but yeah, we just can't delay it enough. But that's okay, I can just go into channel 2 here, and I can invert channel 2. No dramas. There we go. Now we can line up our edge.

**Dave Jones:** Ta-da! Right, now here's where the wheels fall off the billy cart with the Rigo, and here's where the Siglent X series saves the day. You can't see it, but I've actually got both waveforms in there, okay? So they're identical, we've got a 10 hertz waveform, but the minimum rise and fall time

**Dave Jones:** of the Rigo was that massive 200 microseconds, you saw it. So if we go in there and actually have a look, look! Look at the yellow waveform there is the Rigo, look at that! You can see the individual steps there, but look at zoom all the way in, and there's the blue one of course is our Siglent, absolutely

**Dave Jones:** perfect. It's a bobby dazzler, look at that! But look at the horrible well in this case fall time, it'll be the same for the rise time on the Rigo! It's absolutely atrocious. So that's the difference between the DDS output, you can actually see the individual samples there.

**Dave Jones:** Wow. And you can actually see that drift I told you about. You see it slowly drifting? Slowly drifting towards there? It means the two clocks, the two free-running oscillators inside this thing aren't exactly the same frequency. And there's nothing wrong with that, that's just what you'd expect.

**Dave Jones:** But yeah, see we can see the clock drift. They're actually pretty close. Hmm. And you'll see exactly the same thing on the rising edge here, look at that. So that is the massive difference, and a big limitation of the Rigo and a lot of other DDS generators.

**Dave Jones:** So that's a win for the Siglent X series, that EasyPulse technology, very very nice. I like it. And even though it's a 120 meg function generator, well you try and do a 120 megahertz square wave and no siri bob, 25 megahertz maximum. And we can actually get 20 volts peak

**Dave Jones:** to peak output into a high impedance load of course, at 1 megahertz, but that's not going to be the same over the entire frequency range, so let's actually do an experiment. 10 megahertz, okay, we're still 20 volts peak to peak. You know, let's go

**Dave Jones:** 50, or let's go, I don't know, 25 megahertz. Bingo, we drop down to 10 volts peak to peak. And let's go for the full, let's go the full Monty. 120 megahertz. Yeah, we can still, even at 120 megahertz, we can still do 10 volts peak to peak, so that's not too shabby.

**Dave Jones:** And sure enough, at 10 megahertz we can do our 10 volts peak to peak, there we go, we're at 10 point 2 volts peak to peak, near enough. But if we increase the frequency on that let's go up to say 50 megahertz. It's dropped a bit,

**Dave Jones:** 9 point 8 or thereabouts, but this is to be expected, but we just want to see what it's like. And let's go the full Monty, 120 megahertz. It's still doing okay! Now that, that's its performance at 120 megahertz. As you can see, it's starting not to be a really good looking

**Dave Jones:** sine wave there, but that's what you get. As a comparison, here's the Rigol at 120 megahertz. Granted, it's got an output, rated output bandwidth of 160 megahertz, but it only allows 2 point 5 volts peak to peak maximum. But as you can see, much cleaner sine wave.

**Dave Jones:** Let's actually change that to 160 megahertz, its maximum output. So there we go, it's dropped significantly in amplitude, but it's still a pretty good looking sine wave. So if we plug the Siglent back in, you can see that it's, yeah, its sine performance

**Dave Jones:** at its rated bandwidth of 120 megahertz is not that great. So yeah, it's a lose there. And by the way, it does come with a Cal certificate. Just found that in the box. And by the way, it's shorter and a bit more compact than the

**Dave Jones:** older 5000 series, so I rather like that. And the only thing you get with it is CD. I haven't looked at it. Presumably the manual and maybe the waveform editing software and a Cal certificate and the power cord in the box. Nothing else.

**Dave Jones:** So that's a bit disappointing. Why can't they throw in a couple of BNC cables or something? Come on. So I think that's about all I've got time for today. I have to actually send this unit back. It wasn't designed to be a full review.

**Dave Jones:** I haven't got time to test, like, install and test the arbitrary waveform software and stuff like that, which is a big deal with an arbitrary waveform. It can generate, if you're going to generate them, how well it integrates with the oscilloscope for example, or if it does at all, the Siglent scopes to be able to capture, or other scopes to be able to capture

**Dave Jones:** and import waveforms and then output them on an arbitrary generator like this. That's one of the benefits of arbitrary generators. You can actually capture and then simulate that same waveform and then slightly modify it and stuff like that. That's one of the true benefits.

**Dave Jones:** And this thing has more bells and whistles than you can poke a stick at. And I haven't even looked at half of them, haven't even tried the dual outputs and everything else. But yeah, and all the synchronization and modulation and sweep functionality and burst functionality.

**Dave Jones:** But it's a, jeez, I'll tell you what, for $499 for the entry-level 40 MHz one, wow, this one's got winner, winner, chicken dinner written all over it. There's a few little quirks in it, but I don't mind the operation of it. Its performance is pretty good.

**Dave Jones:** You know, 16-bit converter at 1.2 Giga samples per second, kind of does the business. And well, for the price, you can't complain. It certainly seems to kick the pants off the Rigol one anyway, bang per buck. So there you go, I hope you found that

**Dave Jones:** little, I guess, first look, first impressions review of this thing. And if you want to discuss it, jump on over to the eVblog forum, links down below, leave comments, all that sort of stuff. And thanks to Charles at Trio Test and Measure for loaning me this one, it's the only one in the country at the moment,

**Dave Jones:** and he wants it back. I just got a pestering email. When are you going to be finished with that? Alright Charles, I'll take it back now. Thanks mate. Catch you next time. Oh, and by the way, the none other than the Siglent CEO

**Dave Jones:** will actually be coming to the eVblog lab on his tour of Australia. So there you go, how many CEOs do that? That's in December, early December sometime. So I guess if you've got any questions, I think that I'll put up like a forum thread for it or something perhaps.

**Dave Jones:** Anyway, if you've got any questions for the Siglent CEO himself, then yeah, please leave them. I'll try and get him to answer them.
