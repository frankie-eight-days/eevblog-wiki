---
video_id: gpwkiJC5hfU
title: EEVblog #1266 - PSU Probing Screw Up!
url: https://www.youtube.com/watch?v=gpwkiJC5hfU
source: youtube-asr
timestamps: {"0": 0, "1": 27, "2": 60, "3": 77, "4": 105, "5": 135, "6": 159, "7": 176, "8": 207, "9": 239, "10": 267, "11": 299, "12": 330, "13": 348, "14": 380, "15": 412, "16": 426, "17": 437, "18": 461, "19": 482, "20": 516, "21": 547, "22": 581, "23": 613, "24": 647, "25": 682, "26": 714, "27": 750, "28": 765, "29": 794, "30": 822, "31": 838, "32": 860, "33": 881, "34": 920, "35": 939, "36": 964, "37": 977, "38": 1003}
---

**Dave Jones:** Hi. Well, I completely come a cropper on the previous video where I measured the noise on this Ryden RD6006 power supply here. And I was measuring much higher than spec here. I was measuring in the order of, you know, half a volt peak-to-peak noise. And it looked pretty horrible. Well, it turns out that dumb ass Dave didn't engage his brain and actually measured this wrong.

**Dave Jones:** So, let me show you what I did wrong and how to measure this properly. So, here's the signal here that I was measuring at uh 6 amps. And as you can see, uh peak-to-peak, um just over 500 millivolts there. And you can see that uh there is some ripple on there. So, there's some lower frequency ripple. The ripple's only in the order of two divisions, you know, uh 40 millivolts actually. Um it's not that bad. But I completely come a cropper on measuring this peak-to-peak stuff. Why? And how?

**Dave Jones:** Aha, it's an interesting question. And it's a real trap for young players, including dumb ass Dave, when he doesn't have his brain engaged. Because, well, I knew this, but I just well, just completely forgot. Come a cropper. So, the problem lies, as you might have guessed, in my probing technique.

**Dave Jones:** Channel two there, I've just got a regular uh like a 50 ohm RG58 uh coax BNC. And I've got one of these uh BNC to uh banana plug adapters. And I'm plugging this directly into my power supply. So, this is actually it's using uh coax like this is actually a pretty good way to get nice high frequency uh bandwidth measurement. Have I done a separate video on that? I'm not sure.

**Dave Jones:** YEAH, I MIGHT HAVE TO. BUT it while using coax is a brilliant way to get high frequency uh bandwidth of probing stuff, especially low signal measurements, because often you don't want to use your uh traditional times 10 probe here, which uh contrary to its name actually divides your signal by 10. So, if you've got if you're trying to measure a you know, 10 mV noise, the last thing you want to do is be dividing it by 10 to give you like only 1 mV. So, then it's much harder to

**Dave Jones:** measure on your oscilloscope. You're you know, you're really down in the low-end uh noise of your oscilloscope there. So, yeah, you want to avoid the times 10 probe if possible, and using a BNC is one way to do that. But, I completely goofed it. While this is fine for measuring the low frequency ripple stuff, it's no good for the high frequency content. Although, in theory, it should be. What have I done wrong?

**Dave Jones:** Ha! Put your thinking cap on and try and figure it out before the next clip. And no, it has absolutely nothing to do with the fact that these leads are just like uh flapping around in the breeze. They're unshielded for a reasonable length here. That's not the problem.

**Dave Jones:** Now, just a regular uh coax like this is of course going to measure um 0 ohms for the conductor in there. Well, basically, right? It's it's just a wire that goes directly through. But, and this will be important in a minute, trust me. Now, this uh coax of course is a uh shielded uh coaxial cable. You've got the center conductor, and then you've got the outer braid as well. And this is a transmission line uh as far as high frequency content it goes, and the stuff

**Dave Jones:** we were seeing on the oscilloscope, that high frequency ringing content, um that's all about uh high frequency content. And when viewing uh high frequency content like that, you need a proper transmission line like a coaxial cable. And you can see that this is a RG58 uh CU cable. It's you know, a pretty industry uh standard cable. It's not bad uh coax, and it's got relatively high bandwidth. So, it's not a problem with the coax in itself, but the part where we've come a gutsy here is that

**Dave Jones:** because it's a transmission line, it has to be a have a matched impedance in the system. Otherwise, you're going to get mismatch, and as a result, what we're going to see on our oscilloscope is um any ringing or high-frequency content like this because we've got a mismatched transmission line, mismatched impedances. It's going to effectively, in this case, amplify the uh the what's actually happening here.

**Dave Jones:** This switching power supply does actually have noise, as we'll see in a minute. We'll do a proper comparison with um some proper probing, but in this particular case, it's going to amplify that and give us a much different result. In this case, like half an order of magnitude different result than what we're expecting. So, yeah, it can really play a big role matching your coax cable. Now, of course, this is a 50-ohm impedance coaxial cable. So, what we need to do is actually match the impedance. And there's two ways to do

**Dave Jones:** this. The traditional method is if your oscilloscope had 50-ohm input uh impedance termination, you could just enable that, and Bob's your uncle. But, you can come a gutsy with this very easily when measuring power supplies like this. Now, we're only measuring uh 5 V here, but 5 squared, V squared on R to calculate power, 25 divided by uh 50 ohms, that's going to give you half a watt. So, you need at least a half a watt rated uh 50-ohm load in this particular case to actually do that. So,

**Dave Jones:** I happen to have one here. This is a good old HP, none of that Agilent or uh Keysight rubbish. This is a 50-ohm 1-watt um terminator, but it's a like an in-line one, and they're just cooler. So, if we stick that in like that, bingo. Look at this. There you go.

**Dave Jones:** There's our signal. We're now talking 143 mV peak to peak instead of 500. So, that is our true signal that we're getting, not the one that we'll see in before. No. But, there's another way to do this, especially if you're measuring higher voltage uh power supplies like this. So, you can just do this with a 50-ohm resistor. You don't have to put it at the end of the coax cable here. You can actually put it in the front of the coax cable like this. So, I've got a 50-ohm

**Dave Jones:** resistor. It's actually 51, uh good enough for Australia, hanging off here. So, let's plug our coax directly back in like we were before, and we get our horrible, you know, 500 mV signal. But, instead of probing it from here, let me probe it from the other side of this 50-ohm resistor. Bingo. We're getting uh 200 mV uh peak to peak uh because we no longer have the 50-ohm termination load here. So, yeah. But, anyway, you can put in just a 50-ohm terminator. It doesn't matter whether

**Dave Jones:** it's at the start of the coax or at the end like that. You've just got to terminate it properly. But, I know what you're saying. Dave, stop [ __ ] around with this coax cable stuff. Just use your oscilloscope probe. Well, the duh.

**Dave Jones:** Of course, we can just use our oscilloscope probe. So, let's try that now. I've got that plugged into channel one. Let's hook that up. I'm not putting it on the other side of resistor. I'm just using that as a connection point.

**Dave Jones:** And bingo, there it is there. There's our same signal. We're 50 mV per division now, uh and measurement uh around about 210 mV uh peak to peak. So, that's with our probe in uh times 10 like this. So, it's actually uh dropping that uh signal down to uh effectively uh 5 mV instead of 50 mV per division.

**Dave Jones:** And that's okay for large uh amplitudes like we get in here, but for much smaller levels of noise that you're trying to measure, you don't want to use the times 10 position like this. So, anyway, sig- oh, it's come off. There we go. There's our actual signal using a properly compensated times 10 probe like this.

**Dave Jones:** And yes, I have done the compensation adjustment on here, which is important. Cuz let me show you, if you don't compensate your probe properly in times 10 mode, whoa, looking really come a gutsy, and measure the wrong signal amplitude. Look at that. See, we can actually get the incorrect level. So, make sure you compensate your probes correctly in times 10 mode. And of course, you compensate your probe using your compensation adjustment on the front there, and you can see it's peaking, and whoop, go down like that. But you'll

**Dave Jones:** notice that if I switch that to times one, compensation does absolutely nothing because it's not a thing in times one mode. So, there you go. Get your tongue at the right angle. Probe is compensated. So, now you're ready to measure your signal, in this case, the noise that we want to measure, or the high frequency content. Um you've now got a high bandwidth compensated probe. But, aha, there's one thing. But, if we go into the vertical menu here, you'll notice that I've had my bandwidth limit

**Dave Jones:** turned on. There it is, bandwidth. This is the 20 MHz bandwidth limit. I can turn that off, and look, it's going to be completely different. So, why would I want the 20 MHz bandwidth limit turned on? Well, it's basically due to convention. Almost like as a de facto standard, uh noise is measured over a 20 MHz bandwidth. So, if you go look up data sheets for any power supply that specifies noise, for example, it's usually specified over a DC to 20 MHz bandwidth. And this is why almost every

**Dave Jones:** scope, practically every scope on the market, has a 20 MHz bandwidth limit like this. Don't ask me where exactly that came from and why the industry standardized on 20 MHz. It just did, and that's why every scope has a 20 MHz bandwidth limit. And when you're doing noise measurements like this, you should have the 20 MHz bandwidth enabled because that's just by definition. Like, you got have to if you want to specify your noise over a different bandwidth, like the 400 MHz 200 MHz bandwidth of this

**Dave Jones:** scope, even though I'm only using a 100 MHz probe here, then knock yourself out, but that's not industry standard. Use 20 MHz, please. But you might be thinking, and you should be thinking, but Dave, this is coaxial cable, and it is, and it's not 50 ohm terminated. So, why can these probes work without the 50 ohm termination at either the front or the end of the cable like this? Well, that has to do with the particular design and construction of oscilloscope probes.

**Dave Jones:** Now, I've done a whole video on this, "Times Revealed." And I highly recommend that you actually take a look at that video. But if we actually measure the resistance, just like we did before, of an oscilloscope probe, let's put it in times one mode like that. Okay, so we're just measuring the conductor through the middle. Of course, we we got zero before cuz in a regular coax, it's just a single strand copper going right through the middle like that. But on an oscilloscope probe, aha, 330

**Dave Jones:** ohms. And in that other video, I've actually taken apart a probe and I've showed you why. Because it's a lossy coax. They do this deliberately inside the cable. They don't just use regular copper, they use a different like nichrome-y type material and they give it a little bit of wiggle wiggle wiggle year in the middle and that actually creates a lossy coax and that's why oscilloscope probes are specifically designed and matched for the 1 MHz and capacity front end of oscilloscopes.

**Dave Jones:** Whereas coaxial cables, while whilst you can get much better higher bandwidth from them than an oscilloscope probe cuz a a passive oscilloscope probe like the best ones you can get sort of like stop at 500 MHz really. So, you can get much higher than that using a like regular coax cable, but they're less forgiving because you have to terminate them properly. Whereas your passive oscilloscope probes are specifically designed and constructed and matched for your oscilloscope and that's the difference. So, when in doubt, use your oscilloscope probe. I

**Dave Jones:** didn't. I was just like lazy day even just plugged in the coax like this and well, yeah, we came a cropper. So, if I put both probes down there like that and bingo, look at this, they match pretty well, don't they?

**Dave Jones:** They're both 50 100 mV per division. We can change that a little bit. There we go, 50 mV per division and well, you can't there's a little bit of a difference. The yellow one is the oscilloscope probe in times 10 mode. Can see it's got like a bit more high frequency content, but now we're sort of getting down to the details of the probe here. Like if I touch that, if I fiddle around with that, you might be able to see that signal change a bit. Look at that.

**Dave Jones:** See, wiggle wiggle wiggle yeah and you can yeah, you can see that change. So, you know, you start getting down to like high frequency probing techniques and stuff like that, but it's not you see that it's not actually changing the peak up here. It's just changing the more high frequency detail and that's not really the important stuff when you're measuring the peak-to-peak noise. And you know, we're getting like 200 millivolts, 210. It's sort of, you know, it's neither here nor there. So, both of those probing

**Dave Jones:** techniques with the 50 ohm and in front like this and the coax is working a treat. But this is in times 10 mode. What if we switch this to times one probe here? Look at that. There we go. That's times one probe.

**Dave Jones:** And you'll notice it's a little bit higher. It's not that terrific and it's lost all that high frequency content in there that we're seeing in times 10 mode. And that is because if you watch my times one oscilloscope probe revealed video and you should, I explain why a times one probe has a lower bandwidth.

**Dave Jones:** In this case, it's usually about like 5 megahertz, something like that. It's not terrific. So, yeah, it's actually lower than your 20 megahertz. But, you know, you're still going to get your peaks like that. You know, it's going to be sort of like near enough. This is not You know, if you really want to do this with the utmost of precision, well, you know, there's better, you know, you got to fiddle around. So, there you have it.

**Dave Jones:** I turned my goof into a hopefully informative video where you learned something about probing. And in this particular case, apologies to RDTech uh re- re- doing. Um their Rigol RD6006 does not have huge amounts of noise. In fact, it's a little bit, you know, I I need to probe it a little bit better, maybe. But, you know, it's it's it's spec was 100 millivolts peak-to-peak, I think. And we're measuring about 200 at full load. But anyway, if we drop this down to an amp, for example, put

**Dave Jones:** something different, you know, 130 mV peak to peak RMS noise, we're only talking 8 mV, something like that. So, it's not nearly as noisy as I made out in my review video because I goofed it. So, you know, yeah, I might still do a video investigating how to like take the edge off some of that ringing in there.

**Dave Jones:** Maybe we need to put some internal ferrite beads across some of the like the switching components like the MOSFET or or something like that. You know, there's several ways to do that depending on uh you know, the best mitigation uh strategy for getting rid of that. But, so yeah, sometimes I just don't engage my brain and I should have picked that up in the video cuz I knew that, but ah well, you know, [ __ ] happens.

**Dave Jones:** Anyway, hope you enjoyed it. If you did, please give it a big thumbs up. As always, discuss it down below. And I might have to do a video on this soon. I'm available over on library.tv or l b r y.tv.

**Dave Jones:** So, definitely go check that out. It's a decentralized uh video sharing platform. And I've got almost a thousand I'm at 700 subscribers. I want to get over a thousand subs. You know, it feels like the early days of YouTube back in the garage and you know, like, "Yeah, let's get a thousand subs on l b r y." Anyway, it's quite a nice platform. It's up and coming. It's a decentralized crypto-based thing. Definitely check it out. I'll link that in down below as well. Anyway, hope you enjoyed it. Catch

**Dave Jones:** you next time.
