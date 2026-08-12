---
video_id: WE9pYUVvr00
title: EEVblog #983 - A Shocking Oscilloscope Problem!
url: https://www.youtube.com/watch?v=WE9pYUVvr00
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 28, "3": 49, "4": 67, "5": 79, "6": 93, "7": 108, "8": 123, "9": 139, "10": 152, "11": 170, "12": 184, "13": 203, "14": 215, "15": 232, "16": 246, "17": 261, "18": 277, "19": 290, "20": 303, "21": 314, "22": 329, "23": 346, "24": 359, "25": 370, "26": 384, "27": 399, "28": 415, "29": 426, "30": 438, "31": 454, "32": 471, "33": 487, "34": 504, "35": 518, "36": 533, "37": 547, "38": 566, "39": 583, "40": 597, "41": 615, "42": 631, "43": 645, "44": 667, "45": 689, "46": 710, "47": 733, "48": 751, "49": 766, "50": 784, "51": 804, "52": 823, "53": 832, "54": 849, "55": 865, "56": 880, "57": 901, "58": 916, "59": 937, "60": 957, "61": 974, "62": 988, "63": 1005, "64": 1018, "65": 1026, "66": 1041, "67": 1056, "68": 1074, "69": 1095}
---

**Dave Jones:** Hi, I was going to whack this as a quick video on my second channel like I just uploaded two videos on EV blog two with two little bugs I found in the new Rohde & Schwarz RTB2004 oscilloscope like five minutes after a

**Dave Jones:** couple of minutes after I started using it and I found another issue here. I was about to start like a first impressions review and I just discovered this and I thought it was worth showing you this and sort of comparing

**Dave Jones:** it against different scopes. We're talking about microphonics in particular microphonics in multi-layer ceramic capacitors. Now, I've mentioned this on videos before on multi on ceramic capacitors capacitors and things like that. I've even shown you that how that the humble oscilloscope probe can also

**Dave Jones:** be microphonic if you tap it on the bench because well, this end in here is going to have multi-layer ceramic capacitors in it. So, when you tap it, they can actually be microphonic, generate a voltage inside the capacitor and it can cause a

**Dave Jones:** problem in all sorts of not just the oscilloscope probes and but all sorts of products, all sorts of systems. Real track beyond play is something to watch out for and you'll notice that this will change a bit depending on the surface

**Dave Jones:** I've got. Obviously, if I tap it on the bench here, that's a hard surface. So, that's generating a lot of Gs into the actual probe itself. Now, if I put it onto the anti-static mat over here which is spongier, it's a similar

**Dave Jones:** kind of response. It's slightly it's the same frequency response but the response is a little bit dampened. Now, one of the keys to this is the orientation, the physical rotation orientation of the probe when it actually strikes the

**Dave Jones:** surface like this. That's the position that generates the most amount. Now, if I just rotate it so that the switch is on the top there. So I've rotated 90 degrees, still does it. We get a different response and it is dampened.

**Dave Jones:** So I actually discovered this on this RTB 2004 and I guess it's not surprising that it's possible, but I was a bit shocked at the extent of it inside this thing. Now what I've got set up, I've got all my channels set to 2 millivolts

**Dave Jones:** per division here. I've got it set to 2 milliseconds per division. I've just chosen these as a reasonable example of what we're going to see here. The triggering mode is set to normal. It's just edge trigger, triggered off channel

**Dave Jones:** 1, rising slope, DC coupling, no high frequency reject or anything like that. So a very typical low level triggering configuration with a mid-range time base. Now take a look at this, okay? I'm going to whack it in single mode and

**Dave Jones:** Wow, look at that. Microphonic. I'm just using my little plastic thing here. That was not a particularly hard tap either. That was a just a a pretty That one didn't do it. There's a There's a level There's a

**Dave Jones:** level there that it's actually That's actually that's because of my my trigger level is actually there. Sorry. So if we set the trigger level just above the noise there, Oh, look. It's just the tiniest little knock That was so gentle a knock.

**Dave Jones:** That was I barely even tapped it. And there we go. It's triggering channel 1 seems to be worse than the others. Channel 1 and channel 4 seem to be like the worst culprits. Channel 2 seems to be pretty

**Dave Jones:** good. Now I can experiment with this. I haven't actually done this yet, but tap the tap the probe front end like that on channel 1. Just gentle tap on channel 2. Look at channel 2. It's coupled straight through the BNC. The vibration from

**Dave Jones:** tapping this couple straight through the BNC onto the PCB, onto the front-end multi-layer ceramic capacitors. If you've no doubt seen my teardowns of analog front-ends of oscilloscopes, they're filled with multi-layer ceramic capacitors. And if you get, you know, if

**Dave Jones:** you're not careful, you can get ones that are, you know, much more mic- microphonic than others. You've got to be careful in particular the high-value ones, the real multi-layer 10 microfarad 10-V ones or something like that that have a horrible dielectric there. They

**Dave Jones:** can be really horribly microphonic with all those, you know, hundreds of layers or dozens or however many layers they have inside there. Um so, they're piezoelectric. It's a piezoelectric effect. Anyway, I won't go into details, but that would is almost certainly that

**Dave Jones:** what's at fault here. But you can see this is horribly to me. That is horribly microphonic. I originally found this because I was actually Yeah, I was I think I was tapping like the touching the annotation button. noticed that the

**Dave Jones:** trigger LED came up every time I touched the It's not going to do it now. I'd probably have to set up the configurations, but that's how I I discovered the the problem here. Sorry, I've got to go back. Annoying thing

**Dave Jones:** about the scope, by the way, you put in auto mode, you hit single, it doesn't take it out of auto mode. Like I want it to go when I press that single button, I want it to just go into normal

**Dave Jones:** mode and be ready to trigger. I I don't like the way that operates. It's not It's not a bug, it's just an undesirable feature in my opinion. Anyway, so let's actually compare that to many other oscilloscopes I have in the

**Dave Jones:** lab and see if this is a common problem in oscilloscopes, mic- microphonics on the multi-layer ceramic capacitors on the front end. Hmm, but by the way, um this is like a high That, you know, this is a high-frequency tap, right? So this

**Dave Jones:** is a relatively, you know, that's a pretty high frequency tap. What is that, you know, like you can go in there at the time base and measure it. But, also you can get the lower frequency thumps. Now, if I actually do the bench, it's,

**Dave Jones:** you know, you can see it coming through, but it's reasonably well isolated from the bench, uh presumably cuz it's got, you know, a big, huge rubber feet on the bottom there. Some of the biggest I've seen on any scope. So, that's going to

**Dave Jones:** dampen any vibration coming through the bench. So, I wouldn't be too concerned about about that. We're down at We can go down to 1 mV per division if we want. But, yeah, it's not, you know, I'm not too

**Dave Jones:** not too concerned about coming through the bench like that, even though it is possible. But, as I said, I just saw it like tapping on the screen, and this is a big touchscreen. It's designed to be touched and prodded and poked and everything

**Dave Jones:** else. But, you know, I'm I'm always tapping the scope. You know, I go like that and boom. You know, I Anyway, let's compare with some different scopes, shall we? Okay, let's do another Rohde & Schwarz. Exactly the same settings, 2 ms, 2 mV

**Dave Jones:** per division. I'll keep the settings the same on all the scopes we do here. This is actually even though it's Rohde & Schwarz, Rohde & Schwarz bought out Hameg like I don't know, 7 8 years ago. So, a

**Dave Jones:** long time ago. And this is actually a Hameg designed and produced unit, but it's Rohde & Schwarz. So, anyway, um same thing. It might even have some Rohde & Schwarz tech, Rohde & Schwarz front end. By the way, that RTB2004

**Dave Jones:** Rohde & Schwarz scope we just saw has its own 10-bit ADC. It's absolute killer. There's no other scope in that price range with a 10-bit ADC in there. And that's a Rohde & Schwarz designed ADC custom ADC in there. So, you know,

**Dave Jones:** this might have a Rohde & Schwarz ADC as well. So, let's um have a look at this. No, it's possible, too. Up, not as not as big as uh Up, there we go. Got some low frequency stuff. So, the Rohde & Schwarz really

**Dave Jones:** seem to be uh really seem to be susceptible, don't they? And that's not a particularly you know, big thud, really. I mean, it's just you probably wouldn't do it normally, but it's uh it's just something Let's see. If we tap it, there we go.

**Dave Jones:** We can see that doing it. I might have you know, have to turn down the 1 mV or something to really start seeing that, but that's there's not a lot of And the bench, you know, and Whoa! Look at that. Tapping the BNCs.

**Dave Jones:** That's horrible, Muriel. Okay, let's have a look at the good old uh Keysight 3000 uh X-Series, shall we? It's been around for a long time. It's a stalwart. Let's give it a a tap on top, and it looks like it's it's doing

**Dave Jones:** it's doing it. It's got something there. Oh, yeah. Really got a hit it hard, but it's certainly it is possible that it's much higher frequency content than what we were getting on the uh Rohde & Schwarz ones. Um and of

**Dave Jones:** course, that's going to be totally dependent upon the uh construction of the multi-layer ceramic capacitors used inside these things. So, you know, it's all to do with mechanical resonant modes of the piezoelectric material and the size of the plates and you know, every

**Dave Jones:** uh you know, a ton of other uh It's not easy to get in here and do that, but look, um one coupled through to channel one and two there. Two, yeah. Okay. Yep, it's getting through. Whoa! Haha. That's a shocker, isn't it? But that's

**Dave Jones:** some real high frequency uh stuff going on there. 200 microseconds per division. So, much higher frequency, but you know, it's still doing the business. So, I'd say the Keysight one is uh fairly susceptible as well. The brand spanking new, not

**Dave Jones:** even released yet. That's not the correct number. It's going to be the 1202 XE uh Siglent. This is the only one in the wild in the world, apparently. Oh, gee. I'm Uh once again, 2 mV uh per division. This

**Dave Jones:** can go down to 500 uh microvolts. So, let's actually uh turn that down to 500 microvolts. Good having separate con- trols there. Oh. There we go. Oh, wow. Geez, there's not much, is there? Not Well, yeah, I can see that.

**Dave Jones:** Really got to whack Ah, can I even whack that? I can't. I can't. Is uh is good from a point of view of, you know, tapping on the box, but if we Yep, we can see that coming up. Definitely, if

**Dave Jones:** we uh tap that. Once again, like the Keysight, very high frequency uh stuff there being coupled through. So, you know, but this one doesn't have the issue like, you know, touching the screen, touching the top of the box.

**Dave Jones:** Unless you're directly coupled through to the BNCs, this one's rock solid. And the good old Rigol DS1054Z, once again, 2 ms 2 mV per division, 2 ms uh time base there. And yep, wow. THAT'S ACTUALLY WOW. That's potentially What That's got

**Dave Jones:** to be Is that That is worse than the Rohde & Schwarz, is it? Or it's on par. WOW. I'M JUST gently gently tapping the top of that. Geez, I thought the Rohde & Schwarz was Oh, man. The Oh, that's terrible.

**Dave Jones:** Wow, tap on the BNC there. There we go. Once again, that's like just totally saturated that. We Yep. Even tapping on the second channel is enough to trigger channel one. Wow. I'm barely I am barely touching that. Seriously.

**Dave Jones:** Wow. That is terrible. What a shocker. We try Keysight's new DSOX 1100 uh 1000 X series uh scope and Whoa, it's a little bit little bit going on there. Once again, 2 mV per division. I've got to whack it pretty hard to uh

**Dave Jones:** do anything. It doesn't do the low frequency stuff. It's rock solid on the low frequency Oh, maybe. Yeah, if you're lucky. Geez, but uh let's uh Yep. Yep. There we go. We can get it. Once you're directly coupled

**Dave Jones:** there, you get it every time, don't you? Geez. Anyway, all right. The GW Instek GDS-1104B. Sorry, but I I still can't get over how sort of ugly this scope is. I'm sorry for any fans of it out there. It's It's

**Dave Jones:** an okay scope, but it's you know. Anyway. Whoa, low frequency stuff is not It's got some low frequency stuff in there. Let's try and single Whoa, yeah. Maybe in channel four there, but geez, you really have to whack it hard.

**Dave Jones:** Generally, that's pretty solid. Plastic poker. Oh, you really have to go to town. You really have to get, you know, nothing. Really got to get Uh quite vicious with it before it'll do anything. Wow. Wow, that's probably the best, isn't it?

**Dave Jones:** Is that the best on the BNCs that we've seen. That's That's pretty good. Compared to the others, that's not bad at all. And the Tektronix MDO 3000 series scope, once again, 2 mV per division, 2 ms.

**Dave Jones:** Got the trigger point just above CHANNEL ONE THERE. OH, THAT'S PRETTY AWESOME. THAT'S PRETTY AWESOME.

**Dave Jones:** THIS ONE LOOKS LIKE THE BEST SO FAR. BINGO, we got the front panel, but it it it requires, you know, a significant little significant little whack there. Um, you know, so yeah, we got the susceptibility in here, maybe not as good as the GW

**Dave Jones:** Instek we just saw, I don't think from memory, but yeah, as far as our actual uh case coupling through to the front end goes, no, this one is the best so far. Rock solid. And probably the equally ugly uh Teledyne LeCroy WaveAce

**Dave Jones:** Touch 3054, I can just switch this on cuz its boot time is ridiculously quick. Look at that. Um, so I've already set it up, 2 mV, all the rest of it. Oh, let's put in single mode. Geez, I'm having a hard time.

**Dave Jones:** Yep, not susceptible whatsoever. Something else fell down on the bench there. Let's go channel one. Oh, hello. Yep. Yep, that's pretty violent. That's pretty violent. Yep, I'm just touching that. Is that Is that the worst one, perhaps? Teledyne LeCroy, it's not Oh, yeah, you

**Dave Jones:** got to couple through, you got to trigger off that channel. That could potentially be the worst in terms of the BNC. I'm just gently touching that. I mean, low frequency stuff, not all. You really need that high frequency, even a gentle

**Dave Jones:** tap like that. That is really That is really quite That's feather touch. Wow, that's the most susceptible, I suspect. And the Rigol 2000 series? Yep, it's susceptible from uh to low frequency and yep, high frequency, but not uh it's about average. Let's try the

**Dave Jones:** BNC. Oh, yeah. Thank you very much. Look at that. And I know you want to see old school. Let's get the HP 54616B and give it a whirl. Yep, we can do exactly the same thing. But giving it a good whack ON THE CHASSIS

**Dave Jones:** WHOA! THAT'S fine and dandy. Even on the case down here. Wow. That's the uh shielding metal shielding for the front end. You really have to tap the BNC to get that directly coupled to the front end uh coupling cap. So, there you go. I think

**Dave Jones:** that's every scope I have in my lab. I'm not entirely sure. Anyway, I still contend that the Rohde & Schwarz RTB2004 is an issue because not only of course does it work on the BNC input, it just goes absolutely off the scale, but it

**Dave Jones:** it's actually Sorry, yeah, it is the most sensitive. I mean, what is what is that? I mean, that's you know, let's go to 20 mV per division. And yeah, there we go. So, that's just a gentle tap, let alone a

**Dave Jones:** let alone a good whack like that. But not only that, but the problem is this is touch screen. I mean, I can just tap like that and cause that to come up. Especially if you've got like fingernails for example and you you

**Dave Jones:** know, which I don't, but you tap it with a fingernail, it's probably going to be a bit high frequency than if you've got you know, a bit of a stump of a digit and cause that to go in, but you don't

**Dave Jones:** want that when you're just playing around with your touch screen. And this is a capacitive touch screen, so my non-capacitive poker is not going to work, but um, like in terms of actual uh operating the screen, but look what

**Dave Jones:** happens. I mean, if you did have one of these uh, you know, I think you can get capacitive pokers, can't you? I mean, that's just ridiculous. I'm just gently touching that. And look at the amplitude. Wow. That's just like

**Dave Jones:** I swear, like I'm not even holding that rigidly. Just like like loosely going like that. Anywhere on the screen. That's just That That's insane. You can't have that. And they advertise that their front, you know, super low noise front end with their 10-bit ADC

**Dave Jones:** and custom blah blah blah and everything. Fantastic until you actually use their big functional touchscreen. That's just like isn't a feature? You could say that's a feature, right? It's a touch triggering, whack triggering. Trademark. Hm. Anyway, I hope you

**Dave Jones:** enjoyed that. Catch you next time.
