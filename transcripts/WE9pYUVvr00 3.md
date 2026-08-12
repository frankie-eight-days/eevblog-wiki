---
video_id: WE9pYUVvr00
title: EEVblog #983 - A Shocking Oscilloscope Problem!
url: https://www.youtube.com/watch?v=WE9pYUVvr00
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 28, "3": 60, "4": 71, "5": 81, "6": 93, "7": 108, "8": 118, "9": 134, "10": 146, "11": 163, "12": 178, "13": 189, "14": 204, "15": 215, "16": 227, "17": 244, "18": 259, "19": 272, "20": 282, "21": 294, "22": 306, "23": 317, "24": 338, "25": 348, "26": 367, "27": 379, "28": 395, "29": 408, "30": 416, "31": 430, "32": 441, "33": 456, "34": 474, "35": 487, "36": 499, "37": 511, "38": 530, "39": 554, "40": 569, "41": 583, "42": 595, "43": 608, "44": 628, "45": 645, "46": 658, "47": 672, "48": 692, "49": 707, "50": 728, "51": 741, "52": 753, "53": 764, "54": 779, "55": 794, "56": 809, "57": 827, "58": 843, "59": 859, "60": 875, "61": 887, "62": 902, "63": 916, "64": 933, "65": 949, "66": 965, "67": 974, "68": 991, "69": 1005, "70": 1025, "71": 1041, "72": 1050, "73": 1066, "74": 1080}
---

**Dave Jones:** Hi, I was going to whack this as a quick video on my second channel like I just uploaded two videos on EV blog two with two little bugs I found in the new Rohde & Schwarz RTB2004 oscilloscope like five minutes after a couple of minutes after I started using it and I found another issue here.

**Dave Jones:** I was about to start like a first impressions review and I just discovered this and I thought it was worth showing you this and sort of comparing it against different scopes.

**Dave Jones:** We're talking about microphonics in particular microphonics in multi-layer ceramic capacitors. Now, I've mentioned this on videos before on multi on ceramic capacitors capacitors and things like that. I've even shown you that how that the humble oscilloscope probe can also be microphonic if you tap it on the bench because well, this end in here is going to have multi-layer ceramic capacitors in it.

**Dave Jones:** So, when you tap it, they can actually be microphonic, generate a voltage inside the capacitor and it can cause a problem in all sorts of not just the oscilloscope probes and but all sorts of products, all sorts of systems.

**Dave Jones:** Real track beyond play is something to watch out for and you'll notice that this will change a bit depending on the surface I've got. Obviously, if I tap it on the bench here, that's a hard surface.

**Dave Jones:** So, that's generating a lot of Gs into the actual probe itself. Now, if I put it onto the anti-static mat over here which is spongier, it's a similar kind of response.

**Dave Jones:** It's slightly it's the same frequency response but the response is a little bit dampened. Now, one of the keys to this is the orientation, the physical rotation orientation of the probe when it actually strikes the surface like this.

**Dave Jones:** That's the position that generates the most amount. Now, if I just rotate it so that the switch is on the top there. So I've rotated 90 degrees, still does it.

**Dave Jones:** We get a different response and it is dampened. So I actually discovered this on this RTB 2004 and I guess it's not surprising that it's possible, but I was a bit shocked at the extent of it inside this thing.

**Dave Jones:** Now what I've got set up, I've got all my channels set to 2 millivolts per division here. I've got it set to 2 milliseconds per division. I've just chosen these as a reasonable example of what we're going to see here.

**Dave Jones:** The triggering mode is set to normal. It's just edge trigger, triggered off channel 1, rising slope, DC coupling, no high frequency reject or anything like that. So a very typical low level triggering configuration with a mid-range time base.

**Dave Jones:** Now take a look at this, okay? I'm going to whack it in single mode and Wow, look at that. Microphonic. I'm just using my little plastic thing here. That was not a particularly hard tap either.

**Dave Jones:** That was a just a a pretty That one didn't do it. There's a There's a level There's a level there that it's actually That's actually that's because of my my trigger level is actually there.

**Dave Jones:** Sorry. So if we set the trigger level just above the noise there, Oh, look. It's just the tiniest little knock That was so gentle a knock. That was I barely even tapped it.

**Dave Jones:** And there we go. It's triggering channel 1 seems to be worse than the others. Channel 1 and channel 4 seem to be like the worst culprits. Channel 2 seems to be pretty good.

**Dave Jones:** Now I can experiment with this. I haven't actually done this yet, but tap the tap the probe front end like that on channel 1. Just gentle tap on channel 2.

**Dave Jones:** Look at channel 2. It's coupled straight through the BNC. The vibration from tapping this couple straight through the BNC onto the PCB, onto the front-end multi-layer ceramic capacitors. If you've no doubt seen my teardowns of analog front-ends of oscilloscopes, they're filled with multi-layer ceramic capacitors.

**Dave Jones:** And if you get, you know, if you're not careful, you can get ones that are, you know, much more mic- microphonic than others. You've got to be careful in particular the high-value ones, the real multi-layer 10 microfarad 10-V ones or something like that that have a horrible dielectric there.

**Dave Jones:** They can be really horribly microphonic with all those, you know, hundreds of layers or dozens or however many layers they have inside there. Um so, they're piezoelectric. It's a piezoelectric effect.

**Dave Jones:** Anyway, I won't go into details, but that would is almost certainly that what's at fault here. But you can see this is horribly to me. That is horribly microphonic.

**Dave Jones:** I originally found this because I was actually Yeah, I was I think I was tapping like the touching the annotation button. noticed that the trigger LED came up every time I touched the It's not going to do it now.

**Dave Jones:** I'd probably have to set up the configurations, but that's how I I discovered the the problem here. Sorry, I've got to go back. Annoying thing about the scope, by the way, you put in auto mode, you hit single, it doesn't take it out of auto mode.

**Dave Jones:** Like I want it to go when I press that single button, I want it to just go into normal mode and be ready to trigger. I I don't like the way that operates.

**Dave Jones:** It's not It's not a bug, it's just an undesirable feature in my opinion. Anyway, so let's actually compare that to many other oscilloscopes I have in the lab and see if this is a common problem in oscilloscopes, mic- microphonics on the multi-layer ceramic capacitors on the front end.

**Dave Jones:** Hmm, but by the way, um this is like a high That, you know, this is a high-frequency tap, right? So this is a relatively, you know, that's a pretty high frequency tap.

**Dave Jones:** What is that, you know, like you can go in there at the time base and measure it. But, also you can get the lower frequency thumps. Now, if I actually do the bench, it's, you know, you can see it coming through, but it's reasonably well isolated from the bench, uh presumably cuz it's got, you know, a big, huge rubber feet on the bottom there.

**Dave Jones:** Some of the biggest I've seen on any scope. So, that's going to dampen any vibration coming through the bench. So, I wouldn't be too concerned about about that. We're down at We can go down to 1 mV per division if we want.

**Dave Jones:** But, yeah, it's not, you know, I'm not too not too concerned about coming through the bench like that, even though it is possible. But, as I said, I just saw it like tapping on the screen, and this is a big touchscreen.

**Dave Jones:** It's designed to be touched and prodded and poked and everything else. But, you know, I'm I'm always tapping the scope. You know, I go like that and boom. You know, I Anyway, let's compare with some different scopes, shall we?

**Dave Jones:** Okay, let's do another Rohde & Schwarz. Exactly the same settings, 2 ms, 2 mV per division. I'll keep the settings the same on all the scopes we do here.

**Dave Jones:** This is actually even though it's Rohde & Schwarz, Rohde & Schwarz bought out Hameg like I don't know, 7 8 years ago. So, a long time ago. And this is actually a Hameg designed and produced unit, but it's Rohde & Schwarz.

**Dave Jones:** So, anyway, um same thing. It might even have some Rohde & Schwarz tech, Rohde & Schwarz front end. By the way, that RTB2004 Rohde & Schwarz scope we just saw has its own 10-bit ADC.

**Dave Jones:** It's absolute killer. There's no other scope in that price range with a 10-bit ADC in there. And that's a Rohde & Schwarz designed ADC custom ADC in there. So, you know, this might have a Rohde & Schwarz ADC as well.

**Dave Jones:** So, let's um have a look at this. No, it's possible, too. Up, not as not as big as uh Up, there we go. Got some low frequency stuff. So, the Rohde & Schwarz really seem to be uh really seem to be susceptible, don't they?

**Dave Jones:** And that's not a particularly you know, big thud, really. I mean, it's just you probably wouldn't do it normally, but it's uh it's just something Let's see. If we tap it, there we go.

**Dave Jones:** We can see that doing it. I might have you know, have to turn down the 1 mV or something to really start seeing that, but that's there's not a lot of And the bench, you know, and Whoa!

**Dave Jones:** Look at that. Tapping the BNCs. That's horrible, Muriel. Okay, let's have a look at the good old uh Keysight 3000 uh X-Series, shall we? It's been around for a long time.

**Dave Jones:** It's a stalwart. Let's give it a a tap on top, and it looks like it's it's doing it's doing it. It's got something there. Oh, yeah. Really got a hit it hard, but it's certainly it is possible that it's much higher frequency content than what we were getting on the uh Rohde & Schwarz ones.

**Dave Jones:** Um and of course, that's going to be totally dependent upon the uh construction of the multi-layer ceramic capacitors used inside these things. So, you know, it's all to do with mechanical resonant modes of the piezoelectric material and the size of the plates and you know, every uh you know, a ton of other uh It's not easy to get in here and do that, but look, um one coupled through

**Dave Jones:** to channel one and two there. Two, yeah. Okay. Yep, it's getting through. Whoa! Haha. That's a shocker, isn't it? But that's some real high frequency uh stuff going on there.

**Dave Jones:** 200 microseconds per division. So, much higher frequency, but you know, it's still doing the business. So, I'd say the Keysight one is uh fairly susceptible as well. The brand spanking new, not even released yet.

**Dave Jones:** That's not the correct number. It's going to be the 1202 XE uh Siglent. This is the only one in the wild in the world, apparently. Oh, gee. I'm Uh once again, 2 mV uh per division.

**Dave Jones:** This can go down to 500 uh microvolts. So, let's actually uh turn that down to 500 microvolts. Good having separate con- trols there. Oh. There we go. Oh, wow.

**Dave Jones:** Geez, there's not much, is there? Not Well, yeah, I can see that. Really got to whack Ah, can I even whack that? I can't. I can't. Is uh is good from a point of view of, you know, tapping on the box, but if we Yep, we can see that coming up.

**Dave Jones:** Definitely, if we uh tap that. Once again, like the Keysight, very high frequency uh stuff there being coupled through. So, you know, but this one doesn't have the issue like, you know, touching the screen, touching the top of the box.

**Dave Jones:** Unless you're directly coupled through to the BNCs, this one's rock solid. And the good old Rigol DS1054Z, once again, 2 ms 2 mV per division, 2 ms uh time base there.

**Dave Jones:** And yep, wow. THAT'S ACTUALLY WOW. That's potentially What That's got to be Is that That is worse than the Rohde & Schwarz, is it? Or it's on par. WOW.

**Dave Jones:** I'M JUST gently gently tapping the top of that. Geez, I thought the Rohde & Schwarz was Oh, man. The Oh, that's terrible. Wow, tap on the BNC there. There we go.

**Dave Jones:** Once again, that's like just totally saturated that. We Yep. Even tapping on the second channel is enough to trigger channel one. Wow. I'm barely I am barely touching that.

**Dave Jones:** Seriously. Wow. That is terrible. What a shocker. We try Keysight's new DSOX 1100 uh 1000 X series uh scope and Whoa, it's a little bit little bit going on there.

**Dave Jones:** Once again, 2 mV per division. I've got to whack it pretty hard to uh do anything. It doesn't do the low frequency stuff. It's rock solid on the low frequency Oh, maybe.

**Dave Jones:** Yeah, if you're lucky. Geez, but uh let's uh Yep. Yep. There we go. We can get it. Once you're directly coupled there, you get it every time, don't you?

**Dave Jones:** Geez. Anyway, all right. The GW Instek GDS-1104B. Sorry, but I I still can't get over how sort of ugly this scope is. I'm sorry for any fans of it out there.

**Dave Jones:** It's It's an okay scope, but it's you know. Anyway. Whoa, low frequency stuff is not It's got some low frequency stuff in there. Let's try and single Whoa, yeah.

**Dave Jones:** Maybe in channel four there, but geez, you really have to whack it hard. Generally, that's pretty solid. Plastic poker. Oh, you really have to go to town. You really have to get, you know, nothing.

**Dave Jones:** Really got to get Uh quite vicious with it before it'll do anything. Wow. Wow, that's probably the best, isn't it? Is that the best on the BNCs that we've seen.

**Dave Jones:** That's That's pretty good. Compared to the others, that's not bad at all. And the Tektronix MDO 3000 series scope, once again, 2 mV per division, 2 ms. Got the trigger point just above CHANNEL ONE THERE.

**Dave Jones:** OH, THAT'S PRETTY AWESOME. THAT'S PRETTY AWESOME. THIS ONE LOOKS LIKE THE BEST SO FAR. BINGO, we got the front panel, but it it it requires, you know, a significant little significant little whack there.

**Dave Jones:** Um, you know, so yeah, we got the susceptibility in here, maybe not as good as the GW Instek we just saw, I don't think from memory, but yeah, as far as our actual uh case coupling through to the front end goes, no, this one is the best so far.

**Dave Jones:** Rock solid. And probably the equally ugly uh Teledyne LeCroy WaveAce Touch 3054, I can just switch this on cuz its boot time is ridiculously quick. Look at that. Um, so I've already set it up, 2 mV, all the rest of it.

**Dave Jones:** Oh, let's put in single mode. Geez, I'm having a hard time. Yep, not susceptible whatsoever. Something else fell down on the bench there. Let's go channel one. Oh, hello.

**Dave Jones:** Yep. Yep, that's pretty violent. That's pretty violent. Yep, I'm just touching that. Is that Is that the worst one, perhaps? Teledyne LeCroy, it's not Oh, yeah, you got to couple through, you got to trigger off that channel.

**Dave Jones:** That could potentially be the worst in terms of the BNC. I'm just gently touching that. I mean, low frequency stuff, not all. You really need that high frequency, even a gentle tap like that.

**Dave Jones:** That is really That is really quite That's feather touch. Wow, that's the most susceptible, I suspect. And the Rigol 2000 series? Yep, it's susceptible from uh to low frequency and yep, high frequency, but not uh it's about average.

**Dave Jones:** Let's try the BNC. Oh, yeah. Thank you very much. Look at that. And I know you want to see old school. Let's get the HP 54616B and give it a whirl.

**Dave Jones:** Yep, we can do exactly the same thing. But giving it a good whack ON THE CHASSIS WHOA! THAT'S fine and dandy. Even on the case down here. Wow. That's the uh shielding metal shielding for the front end.

**Dave Jones:** You really have to tap the BNC to get that directly coupled to the front end uh coupling cap. So, there you go. I think that's every scope I have in my lab.

**Dave Jones:** I'm not entirely sure. Anyway, I still contend that the Rohde & Schwarz RTB2004 is an issue because not only of course does it work on the BNC input, it just goes absolutely off the scale, but it it's actually Sorry, yeah, it is the most sensitive.

**Dave Jones:** I mean, what is what is that? I mean, that's you know, let's go to 20 mV per division. And yeah, there we go. So, that's just a gentle tap, let alone a let alone a good whack like that.

**Dave Jones:** But not only that, but the problem is this is touch screen. I mean, I can just tap like that and cause that to come up. Especially if you've got like fingernails for example and you you know, which I don't, but you tap it with a fingernail, it's probably going to be a bit high frequency than if you've got you know, a bit of a stump of a digit

**Dave Jones:** and cause that to go in, but you don't want that when you're just playing around with your touch screen. And this is a capacitive touch screen, so my non-capacitive poker is not going to work, but um, like in terms of actual uh operating the screen, but look what happens.

**Dave Jones:** I mean, if you did have one of these uh, you know, I think you can get capacitive pokers, can't you? I mean, that's just ridiculous. I'm just gently touching that.

**Dave Jones:** And look at the amplitude. Wow. That's just like I swear, like I'm not even holding that rigidly. Just like like loosely going like that. Anywhere on the screen. That's just That That's insane.

**Dave Jones:** You can't have that. And they advertise that their front, you know, super low noise front end with their 10-bit ADC and custom blah blah blah and everything. Fantastic until you actually use their big functional touchscreen.

**Dave Jones:** That's just like isn't a feature? You could say that's a feature, right? It's a touch triggering, whack triggering. Trademark. Hm. Anyway, I hope you enjoyed that. Catch you next time.
