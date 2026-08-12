---
video_id: Dez9KG6whb0
title: CMRR Followup Micsig DP10007 vs HVP70
url: https://www.youtube.com/watch?v=Dez9KG6whb0
source: youtube-asr
timestamps: {"0": 0, "1": 32, "2": 51, "3": 75, "4": 103, "5": 123, "6": 136, "7": 162, "8": 187, "9": 215, "10": 229, "11": 261, "12": 277, "13": 302, "14": 319, "15": 348, "16": 375, "17": 404, "18": 424, "19": 455, "20": 489, "21": 518, "22": 547, "23": 574, "24": 598, "25": 635, "26": 660, "27": 680, "28": 707, "29": 733, "30": 771, "31": 789, "32": 817, "33": 835, "34": 855, "35": 872, "36": 905, "37": 933, "38": 955, "39": 978, "40": 995}
---

**Dave Jones:** Hi, this is just a quick follow-up to my main channel video on the common mode rejection ratio and how to use an oscilloscope to actually measure that and also get a use the frequency response analyzer to get a response plot of that of common CMRR versus frequency. And someone mentioned on that video, can I do that with the Bode 100 that I've got, the VNA, the vector network analyzer and impedance response analyzer? And yes, I can. So, let's try.

**Dave Jones:** It's not going to be as good as what we got on the oscilloscope due to the well, we'll talk about that in a minute. Anyway, by the way, that was like a a pretty terrible performing video. Actually, I'm quite disappointed with the views in that. It's probably my worst video worst performing video in a long time. The feedback is great.

**Dave Jones:** Everyone seems to love it, but nobody seems interested. I don't know. Did I get the title wrong? Did I get the thumbnail wrong? I did actually put a poll on Twitter over which thumbnail to use and I used the one that everyone voted, you know, the vast majority voted for. So, I don't think it's the thumbnail. It's probably just like the subject title. Who wants to I don't know. If you've got a suggestion for a better title, I can try and change it.

**Dave Jones:** Nobody seemed interested in it. Anyway, it's one of those good long term videos cuz I don't think there's few if any videos like that on YouTube. That's why they're like, you know, I thought it was good. Anyway, let's use my Bode 100, none of that Bodey rubbish, the Bode 100 frequency response analyzer, which you've seen in previous videos. Oops, I'll just turn off my overlay there. And this is not the response. I haven't turned it on.

**Dave Jones:** Let me show you the setup here. Sorry, I don't have my second camera set up, but there's the Bode 100. Got our output here. Got channel one input here and uh two input is coming from the output of the uh HVP100.

**Dave Jones:** I'll turn that on, switch it, we'll measure it at uh times um 1:10 uh division ratio. I can't really do 1:100, I don't think. I haven't tried it yet, but uh anyway, and then just like last time, I've got a 50 ohm load.

**Dave Jones:** There's an internal 50 ohm load, but I've disconnected that. So, just an external uh 50 ohm load on there. And um as before, just uh uh twisted leads on the input and both connected um shorted together to the uh output there across the uh 50 ohm load. So, we can now plug that in and see what we get.

**Dave Jones:** Too close. Now, um I downloaded the latest version of the software here. Now, we're getting uh well, we could have gone back. We can go Can we just go to new measurement? Oh, I could goof that up. Yeah, here we go. So, these are the different types of uh measurement I can do. We don't want our transmission reflection. What we want is uh gain phase. So, this is part of the VNA or vector network analyzer capability um of this thing. And you can see that the

**Dave Jones:** output here um and then we're what we want is effectively the transfer function of our device under test, which was the HVP uh 70. So, we've got that going off into channel one there. Then uh yeah, the output of our uh device is at um there. So, anyway, and we can do our impedance analysis as well. I've shown shown this in our previous videos. This is all the stuff that I can do. It's very cool. I should play with this more, actually. Um yeah, we can get uh

**Dave Jones:** responses of surface I've got uh little surface mount jigs with it and everything, so that we can you know, anyway, it can do lots of cool stuff. So, let's just go back to recent. Uh uh Can we just go backwards? There we go.

**Dave Jones:** Good. Okay. Now, what we want is our highest possible source voltage. Now, here is the problem here. Our source level 13 DBM, that's only 1 V RMS into a 50 ohm load. Unfortunately, you know, we were using 5 V in the previous video, so that's why it's not going to be as good here cuz we This all has to do cuz we're measuring very low signal levels, and I think that the Well, down here we can the receiver number two, we don't have any amplifier fires on there. All we've got is an

**Dave Jones:** attenuator. And I think the lowest range is 7 mV full scale, I think. Don't quote me on that. But anyway, so we want no attenuator on the input that we're trying to measure the common mode noise output of the probe.

**Dave Jones:** So, channel two, basically. Don't know why they call it receiver two, channel two. And then we do actually I've tweaked this It will tell you if it overloads. So, I've tweaked this 20 dB seems to be the right level there for our receiver number one for our input across our 50 ohm load there. It does work on lower ones, you just won't get as big a signal to noise ratio there.

**Dave Jones:** Receiver bandwidth This is just how long it's you know, the bandwidth at each sample point. 10 Hz is okay. And we're going to go from 100 Hz right up to 40 MHz here. And so, what else have we got? We've got 201 points here.

**Dave Jones:** We're going to do a logarithmic sweep here. And transmission gain setup This is really cool. It It shows you the internal configuration here. So, we've got our source mode, and there we go. And we can set up these things here as well. It's a really nice user user interface. It's They've really polished this. It's very nice. Anyway, so there's our output. As I said, it does have a 50 ohm internal load. I've just I just had the external one there already. Um, the probe is one to one.

**Dave Jones:** Um, now here's the cool thing, we can actually set up the probe 10 to one on the uh second channel, so it'll cater for the gain of that thing. So, uh for the HVP-70. So, we don't have to add on uh 20 dB on there, and we're going to get our transfer function of our device under test. No 50 ohm loading on that. They're both AC coupled. Um, and the attenuator setting you saw before, receiver does settle in time. We don't need to uh I don't think we have

**Dave Jones:** to add do that at all. So, we will close that down, and let's run a single sweep, shall we? And let's see what we get. Now, of course, down at the uh low end, you can see on the uh uh Y axis on the left-hand side here, that's our magnitude in dB, and we're down in the noise there. So, that's why we're getting like, you know, it's it'll come smoother in a sec. It'll now start being really smooth because we're now out of the signal to Now, we've got decent

**Dave Jones:** signal-to-noise ratio, and it's pretty schmick. So, we're getting garbage on our uh phase, and the blue one is the phase. So, the red one is the magnitude there. So, it's ramping up. Now, our spec at 1 meg is 50 dB, and I think we're getting 51 in the previous video, but we don't seem to be getting that here.

**Dave Jones:** One 1 meg, you can see the cursor up the top there, 47 and a half. So, not quite. But, uh 20 meg, where we're measuring before, getting a little bump in there. Up at 20 meg, uh 43 dB, and the spec is uh 40. I so, I think 40 uh so, 44. I think that's pretty close to where we're measuring with the scope. Um, so, yeah. And you can see that the uh phase um I used the incorrect phase. Somebody pointed this out, and yeah, uh totally correct.

**Dave Jones:** Thanks for actually uh pulling me up on using just sloppy terminology. I said a phase reversal like this. It's not a reversal. It's a phase essential essentially wrap around. Like the phase is actually continuing. The cool thing about the uh the Bode 100 is that uh yeah, here we go. It's got the option option here to unwrap phase, okay? So, we can unwrap that and boom, it's just basically the phase is just it it just keeps going. It doesn't suddenly you know suddenly change phase that drastically.

**Dave Jones:** It doesn't suddenly flip 180° instantly. Uh no, it's just continuing to essentially, you know, drift in phase in that in that direction. But, you know, I mean a lot of the time you can't actually display that or you don't want to display that on a um on a scope or a VNA or whatever. So, you uh so, you do a wrap. So, you wrap it and you understand that when it goes vertical like that instantly, you've wrapped from one side to the other just so that you can keep a better scale on

**Dave Jones:** your um screen. So, anyway, you can wrap or unwrap uh that. There you go. Um that's it. That's that that's all we can do. That's the absolute best we can do unfortunately um because yeah, we don't have a high enough voltage level. They do sell a times four amplifier for this thing which which isn't much. Times four isn't a lot. It only takes us up to four times uh four volts RMS, which is, you know, So, yeah, I'd need a decent at least a times 10 amp in there. Like a

**Dave Jones:** times 20 would be really nice. Um and then we could uh really do that, but I don't have like a 50 meg bandwidth um you know, I could maybe I could cobble something together perhaps or something like that, but not for this video. So, there you go. Um yeah, I don't know why it's um it it is under spec at that one meg and down at 20 kHz, what was that spec at 20 kHz again? It was Let me read the data sheet. Uh minus 60 and we're getting up the top

**Dave Jones:** there minus 50. So, it it doesn't meet the spec by 10 dB. And but once again, that could be the fact that we're, you know, don't have the signal level required for that. So, yeah. Anyway, so what I'm going now going to do is use this same setup and I'm going to measure the same that Well, look, we can we can try the times 100.

**Dave Jones:** Let's Let's do it again for the times 100 transmission gain. But it's going to be, of course, an order of magnitude worse. So, we can now do that again and it won't be smooth for a long time. So, well, it's just it's just flat flat flat cuz it's just like the it's higher noise floor now. So, we've got a higher noise floor on the actual probe itself and uh it's Oh, it's starting to do okay, isn't it?

**Dave Jones:** Actually, I'm rather surprised by that. There There you go. There you go. It is It's It's almost identical plot. Almost identical on divide by 100. Which shows that what dominates here is the Oh, no. No, there you go. It's falling off. It's falling Oh, look at that response. Look at that.

**Dave Jones:** Look at that. Isn't that interesting? There you go. Wow. Wow. Fascinating. So, yeah, that response here I was going to say that's more to do with the amp with the differential amplifier itself than mismatches in the input divider.

**Dave Jones:** But, you know, once you start getting up in frequency, those input divider resistors, they're hard to hard to compensate for and that's why you get, you know, sort of like lousy response like you know, he's sort of like um response that's all over the shop like that. But, there there There you go. That's interesting, huh? So, at a at a couple of megs it starts to fall off and become uh not as good as the divide by 10.

**Dave Jones:** Fascinating, huh? And if we by the way, you know, if like like we set the receiver bandwidth to like a kilohertz or something, we could do that much quicker. So, boom. Look. You can see it's not as it isn't as smooth there. And if we set it down at one If you're really keen and set it down at 1 hertz, but you're not going to get any advantage to that. So, even 300 hertz will give you a little bit better response.

**Dave Jones:** And then 100. Boom. Boom, baby, boom. Gets better each time. There you go. Fascinating, huh? I'm now going to get the Mixig Pro, the DP10007, is it? And try that. So, here it is, the DP10007. And for that it's got to take the sticker off the back cuz I've done a teardown video of this. There's some adjustment pots. For those who don't know, Mixig actually specifically developed this product for me. They they didn't have this and I said, "Hey, can you make an equivalent unit to my to

**Dave Jones:** match the specs like times 10 and times 100 to match basically my HVP70 probe at a lower cost?" And they went, "Um we'll have a go at it." And and they did. They actually developed this, but now it's on for sale anywhere.

**Dave Jones:** And I had some issues with the common mode on this and they never got back to me on it. So, I'm going to re-measure this now. I can't remember the exact details, but anyway, yeah, so this is So, they did match practically specs for spec. If you look at the two data sheets side by side, they're almost identical. So, Mixing just copied the HV Sapphire HVP 70 specs because I told them to. And so, the reason you can get this is because of me. There you go. Anyway, let me hook

**Dave Jones:** it up. All right, here we go. Got it connected. Times 10. Single shot. Oh, well, that's uh well Let's fix that up. Let's go down to 30 Hz, shall we?

**Dave Jones:** And whoa, look at that peaky peak. Whoa, something's something's happening there. Uh maybe that's a mismatch in the input uh divider. Oh, sorry. I was completely wrong before. It's not 20 MHz, it's 10 MHz on the HVP 70.

**Dave Jones:** Why did I think 20? Um anyway, so yeah, yeah, oops, I completely goofed that. Uh yeah, so it's the same spec, minus 40. Yeah, and minus 60 at 20 kHz. So, minus 40 at 10. So, minus 40 at 10.

**Dave Jones:** And yeah, they're getting minus 30 three. Minus 33.6. So, yeah, and at 1 meg uh 1 meg is 52. So, it does meet the uh 1 meg spec. And at 20 kHz, minus 60. So, yeah, it does it does actually meet that, but it's got this yeah it's got this big response in there, and yeah, uh something's happening. Oh, sorry, I didn't uh so, we'll change that to 100.

**Dave Jones:** We'll repeat that. Oops, there we go, minus 60. Boom. Uh and up she goes, up she goes. Yeah, see how it gets see how it gets jaggy there once you're down you know below the noise floor there. So you start getting into the noise. But yeah, um at at 10 meg it's yeah, minus 20.8.

**Dave Jones:** So, yep. So there you go. That's the that's the uh Mixig compared to the uh HVP 70. Uh HVP 70 is smooth you know, doesn't have this big issue down here. So, yeah, is that an imbalance in the uh divider front end on the Mixig?

**Dave Jones:** What's going on there? Is there something or the diff amp in there? And or the diff amp. Um the response to the diff amp. But yeah, that's uh But yeah, you can notice that uh yeah, the phase just goes whoop and then once again we've got a wrap like that and then it goes and back up. It's like It's like a roller coaster.

**Dave Jones:** So, yep. It's all over the shop. Um yeah, not not quite as good a response as the HVP 70, but the Sapphire do make some of the best probes in the business. So, yeah, Mixig just haven't nailed that in, but it is much cheaper. So, you know, yeah.

**Dave Jones:** Yeah. But there you go. Hope you found that interesting. If you did, give it a big thumbs up. Catch you next time.
