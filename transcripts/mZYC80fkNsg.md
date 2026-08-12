---
video_id: mZYC80fkNsg
title: EEVblog #1235 - How To Align Signals On A Digital Oscilloscope
url: https://www.youtube.com/watch?v=mZYC80fkNsg
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 28, "3": 38, "4": 52, "5": 64, "6": 76, "7": 88, "8": 100, "9": 115, "10": 128, "11": 140, "12": 154, "13": 178, "14": 197, "15": 209, "16": 227, "17": 241, "18": 255, "19": 277, "20": 287, "21": 296, "22": 310, "23": 321, "24": 330, "25": 343, "26": 353, "27": 374, "28": 399, "29": 410, "30": 418, "31": 429, "32": 441, "33": 452, "34": 461, "35": 473, "36": 481, "37": 499, "38": 520, "39": 535, "40": 547, "41": 558, "42": 579, "43": 592, "44": 607, "45": 619, "46": 637, "47": 646, "48": 665, "49": 678, "50": 689, "51": 708, "52": 724, "53": 746, "54": 768, "55": 780, "56": 797, "57": 811, "58": 821, "59": 831, "60": 843, "61": 861, "62": 876, "63": 889, "64": 906, "65": 936, "66": 964, "67": 989, "68": 1014, "69": 1039, "70": 1057, "71": 1068, "72": 1085, "73": 1098, "74": 1110, "75": 1119, "76": 1143, "77": 1159}
---

**Dave Jones:** Hi, it's time for another oscilloscope tutorial and I've actually done, if you don't know, a whole bunch of oscilloscope tutorials. I've got a YouTube playlist which I'll link in at the end and down below.

**Dave Jones:** It's currently got about 30 videos on it for various oscilloscope tutorials. Anyway, this one today is a little bit more obscure and not available on all scopes, but it could be really valuable if you're looking at two correlated signals that are quite far apart.

**Dave Jones:** So, let's take a look at it. We're using our Keysight 3000 X-Series cuz this happens to have the feature that we're looking for that's going to enable this. This is really interesting.

**Dave Jones:** So, what I got here, channel A, channel B, and I've just got two signals here. They're actually like little bursts of square wave here like this and it's the same on channel two down here.

**Dave Jones:** But, of course, to go in and see channel two, that's our problem. How do we go in and look at channel two? Oh, it's easy. Dave, go in there, trigger, select your source, go in there, and we're now triggering off channel two.

**Dave Jones:** Thank you very much and we can go in there and have a look at channel two. Okay, that's great, but how can we look at both of them at the same time with any sort of detail?

**Dave Jones:** Ha, I know what you're saying, Dave, that's easy, too. All you got to do is single shot capture that, put it at a reasonable time base, and then zoom in.

**Dave Jones:** Ah, look at that. Depending on our memory depth, we've come a gutser. There's not much detail in there, is there? That's pretty awful. And then, of course, we can scroll over to channel one over here.

**Dave Jones:** Did I call it channel A before? Anyway, old school. Okay, so we can view independent ones and we can go in there with our cursors and we can measure things and we can, you know, count the number of cycles and we can we can analyze each one independently, but it's kind of like a multi-step process.

**Dave Jones:** If we actually run this thing, how do we actually get uh both of these signals on the screen at the same time correlated together? Hmm, you might think it's impossible, but it's not.

**Dave Jones:** So, pause this video and try to figure out how you can get both of these zoomed in like that, so one above the other, so that we can then compare them.

**Dave Jones:** Because often you'll have two correlated signals like this. One might affect the other, but they're actually spaced a long way apart, and you want to see the response, you know, one compared to the other.

**Dave Jones:** You want to overlay them. How can you do it? So, this seemingly impossible task is actually very easy for an advanced scope that has this feature. Let's go into trigger here and the different types over here, and you might be like modern scopes just have a ton of different types of trigger, you know, runt pulses, nth edge, burst, rise and fall, and all that sort of jazz.

**Dave Jones:** But what we want is this rather obscure one down here called or. So, let's actually select that, and if you have a look down here, we now get an option to set up or it's got all of the channels the four analog channels and the four digital channels like this.

**Dave Jones:** So, what this is going to allow us to do is exactly as the name implies. It's an or trigger, just like a digital logic function or. So, it can trigger on channel one or channel two.

**Dave Jones:** So, at the moment we've only got trigger one enabled here, and we can select the slope we want, rising, falling, or either, or don't care for channel one. And then we'll select channel two, and we can select rising for channel two as well.

**Dave Jones:** And bingo, if we go in there, look at that. Magic. Now, this is actually quite amazing. We've actually got both signals now. What looks like they're time correlated, but there's not.

**Dave Jones:** There's actually a big difference um in time between them as you uh saw before, but as well as you can still see if we kind of do that. And if we single shot capture that, only one of them will ever be there at any one time.

**Dave Jones:** But, it's just kind of essentially randomly triggering off either channel one or channel two. Hence, the trigger type function called or. Isn't that fantastic? And you can tell that they're uh sort of swapping between them because of the thick Look at at the line down the bottom.

**Dave Jones:** Well, oh, I I just Bloody touch screens. The the line down the bottom. So, you can tell that it's actually uh overlaying that on the uh screen multiple times.

**Dave Jones:** But, yeah. That's beautiful. So, now we can actually get in there and see that our channel two signal is actually half the length of the one up the top.

**Dave Jones:** Then, we can just go in there and analyze those. Isn't that cool? Love it. But, you've got to remember you could actually come a gutser with this because if you just like called your colleague over, "Hey Bill, come over here.

**Dave Jones:** Check this out." And look at these signals here. They would with if they didn't know if you weren't in the trigger screen like that, how would you tell? You would think that they're time correlated, wouldn't you?

**Dave Jones:** You would think, "Oh, look, they're both starting at the same time." Yeah, obviously. The only thing that's telling you is that little trigger annunciator up there, the little green one.

**Dave Jones:** That's just showing the or symbol. And well, unless you know what or triggering's actually doing, there's nothing else on here to indicate that these are not proper time correlated signals.

**Dave Jones:** So, the only indication you're going to get is if you hit that stop button and you only get the one or you hit the single shot button and you go, "Aha, those two aren't really correlated.

**Dave Jones:** It's a trap!" It's a trap. So, we're effectively viewing both in real time, although the scope's actually sort of like altern- the old school alternate trigger on analog scopes it jumps in between them, but it's doing it so fast that they're both on there at the same time.

**Dave Jones:** So, this or trigger type is effectively replacing the alternate trigger function that they used to have on some old school analog scopes. So, I like I really don't know why modern digital scopes don't have alternate trigger as such and and call it as such cuz it's actually really quite handy, but this Keysight one does actually have it in addition to pattern triggering as we'll see.

**Dave Jones:** And because they're on the same time base, they are genuinely like this one is genuinely half the length of that. This is not a dual time base scope, which I might have to go into.

**Dave Jones:** Anyway, that's another rare feature of scopes these days. We can actually go in there and measure various things if we want and you can muck around to your heart's content.

**Dave Jones:** And you can get both on the screen at once. It could be really handy, essential for niche applications. And by the way, it may not just automatically work like this.

**Dave Jones:** You may actually have to go into your trigger menu down here and you might actually have to change your hold off like this depending on your signals and the distance between them and stuff like that.

**Dave Jones:** If we take that up far enough, we'll probably see one vanish. Yep, they are. And yep, we have we have come a cropper and the other one's vanished now and sometimes you've got to have a yeah, twiddle around with it.

**Dave Jones:** Or we can do random hold off. I like the sound of random hold off. Anyway, if you don't know about trigger hold off, I've probably done a video on that, have I?

**Dave Jones:** Anyway, um basically it'll take the first trigger, then it'll wait, it'll hold off for a certain number of milliseconds before it arms itself again, before it can trigger the next one.

**Dave Jones:** Anyway, this is probably not the best example for that, but you may have to twiddle around with that. And this would actually be a classic use case for segmented memory as well.

**Dave Jones:** So, if we go into our choir menu and we go segmented memory, let's set up say 100 segments. Segmented memory, boom, it's captured, and then we can just scroll through those, and you can see how it's capturing those alternately.

**Dave Jones:** So, yeah, there you go, it seems to be doing proper alternate triggering. One, you can see the the frame, it just alternates between those two channels like that. If you get out of segmented mode and just single shot capture it, then it's just going to be it's going to appear random, but it is actually doing an alternate or trigger.

**Dave Jones:** Great. And this Siglent 1104X E here, we can actually get it working, but we have to use a pattern type. We don't actually have a specific or slash alternate trigger function.

**Dave Jones:** So, we're going to use a pattern which is designed for digital and can actually get in there and set those, and I set them both to low. Ironically, I can't actually set them both to high.

**Dave Jones:** It doesn't work, just goes all over the place, but low will get that to work. So, we can actually kludge that using what's designed to be a digital logic function.

**Dave Jones:** Now, in this particular case, we happen to be using digital waveforms here. So, you could come a guts completely on that with other types of waveforms. We just happen to be able to get this, you know, to kind of sort of work, and we should be able to see this cuz most scopes have pattern triggering on them these days.

**Dave Jones:** So, you can sort of get it, but just remember it's not the same as proper or triggering that we saw on the Keysight one. Now, you can achieve this same thing on old-school analog scopes.

**Dave Jones:** Unfortunately, my Tech 2465, which I haven't fully repaired yet, I didn't realize this, but the the B time base is actually buggered on it. Anyway, you can see that there's options for B trigger delay hold off.

**Dave Jones:** So, we could potentially get both on the screen at once there. Can the Rohde & Schwarz RTB 2000 do it? Well, let's go into trigger types here. Looks like it doesn't have it.

**Dave Jones:** But, pattern triggering, woah, fancy pantsy. Just like the Keysight, all of the digital channels, the four analog channels, and we've got an and or or function. So, it's basically and we can set those going true.

**Dave Jones:** And if we do that, there you go. Works an absolute treat. There's a little bit of you know flickering action happening there. No, stupid me is in auto trigger mode.

**Dave Jones:** You need normal trigger mode. I suspect that might work. No, it's still the same. We might have to use hold. Anyway, you shouldn't use auto trigger mode. Should be using normal cuz you don't want the auto trigger to accidentally trigger when you don't really intend it to.

**Dave Jones:** Seems a little bit better there if I do the hold time. It just seems a function of the or pattern on this particular scope. Anyway, does the business. In this Rigol DS2000 series scope here, we can get it working on the pattern mode here.

**Dave Jones:** Seems to be a bit quirky. You can't actually select both the rising edge on both of them, but I was able to get it working both of them on low like that.

**Dave Jones:** So, yeah. Does the business. And the venerable DS1054Z, we do have a pattern option down in here. Let's go check it out. Woah, lots of relays clicked. Anyway, yep, we can looks like we might be able to do the business.

**Dave Jones:** Once again, the DS1054Z, I cannot set both of them to an an edge type. So, there's some sort of weird limitation. Anyway, if I set both of those to low, winner winner, chicken dinner.

**Dave Jones:** But, let's take a look at an interesting scope here, the Uni-T UPO3000E series, among a couple of other scopes on the market, including the I believe the original Rigol DS1052E, not the Z, the old the old school E model, which I reviewed in EEVblog number one video.

**Dave Jones:** That actually has a feature called dual time base. So, if you actually go into the horizontal menu here, let's have a look. Time base is normal, okay? But, if we go in there and select independent time base, what we get now is you can see we've got four independent time bases for the four channels.

**Dave Jones:** We don't need three. Oh, you can't actually turn that off. Really? Wow, okay. Function disabled. Oh, it forces all four channels on. That's kind of weird. Didn't know about that.

**Dave Jones:** Anyway, um we have an independent time base. So, if we select channel one, we can adjust the time base independently on channel one. Now, if we select channel two, we can independently select that and it's triggering off the two different ones.

**Dave Jones:** Of course, the advantage of having different time bases for uh each channel is that we can see as much detail as we like. Isn't that absolutely fantastic? But just be aware they are different time bases.

**Dave Jones:** So if you're going in there and uh you know, measuring stuff like visually off the screen, then you can potentially come a cropper there forgetting that you've got the different time bases.

**Dave Jones:** But these uh dual time base scopes are you know, a reasonably rare on the uh market. So but this Unity happens to have it. There's a couple of other models out there.

**Dave Jones:** Let us know if your one has it. But anyway, this does the business without having to muck around with your triggering. Because by default when you enable a dual time base scope, it has a separate trigger for each one.

**Dave Jones:** It's actually triggering off channel one and channel two totally independently. So technically dual time base scope is better than the alternate trigger system because if now if we actually single if we stop that or if we single shot capture that, we'll actually get both at the same time.

**Dave Jones:** Oh, single shot capture. Come on. I'm pressing the single button. I swear. Single. Function is disabled. You can't Oh my goodness. I I hadn't used this scope in depth.

**Dave Jones:** Unbelievable. Single shot capture mode disabled in dual time base. Dual time base scopes are great, but for some reason manufacturers well, you know, it's more complicated. So you know the reason why.

**Dave Jones:** It's more complicated to implement a proper dual time base and dual independent triggering system, but it's really handy. So that's pretty neat. And I do believe the uh Tektronix entry level the TBS or Tech Basic scope series also has uh dual time base as well.

**Dave Jones:** GW Instek GDS uh 1000 series n- doesn't have the triggering. And our Tektronix uh MDO 3000 here, yep, sure enough it has logic down here. So we can go in, we can define our inputs exactly like the Keysight and the Rohde & Schwarz and we can set both to high like that we can define our logic as or trigger when goes true and you can set up your thresholds

**Dave Jones:** and stuff as well and there we go that works it's a little bit sort of clunkier but it does the business and I had to set the thresholds up here as you can see if you adjust the threshold you can see the channel one threshold going up and then boom channel one is gone goneski cuz we don't have the independent thresholds set so just be aware of that when you're

**Dave Jones:** playing around with it trying to get it working you need both of those thresholds and how about the Siglent SDS 5000 well well I got a patent here let's see if we can do the business on that but it logic oh yeah there we go or yep here we go and it disables the ones we haven't got on nice so we'll go high we'll go high we can set the independent

**Dave Jones:** level values that's too low we need to tweak that up a bit oh yeah no no it's all good and yep that works a treat look at that beautiful Bobby dazzler and once again it's not dual time base we're only capturing one of those at a time so it's alternate trigger or it's going or or or or or actually out of all the scopes that did that I think the the Keysight and the

**Dave Jones:** Siglent both give the nicest most responsive uh display on that if those playing along at home you want to know that anyway and check this out the 01 XDS 3200 this one actually if you go into the trigger menu here edge okay if you well single if you go into here nothing there, but look, alt.

**Dave Jones:** Alternate trigger, straight in. Beautiful. And it also supports logic as well. I've set up logic with the or mode here and xor and xnor and and. And of course and will never work because they're never both true at the same time.

**Dave Jones:** You saw that on the main time base. So you can set that goes true. So that one's actually got true. Alternate trigger mode. Isn't that neat? Kind of like that.

**Dave Jones:** You can't single shot capture in alt mode though, but you can run stop and get both at the same time. Winner. So only one of my scopes seem to have had like a proper old school alternate trigger mode even though you couldn't do it in single mode and the Keysight is the only one that has both pattern and or.

**Dave Jones:** And of course the pattern one does work, but the or one you can set both of your channels or you can basically set all of your channels to slopes.

**Dave Jones:** Well, you can't do that and I found this pretty consistent across all the other scopes as well. If you go into pattern triggering, you can only set and it does actually tell you this in the manual if you read it that only one of them can actually be a rising edge.

**Dave Jones:** So check it out, right? If I try and set the first one to a rising edge, I can do that. Try and set the second one to a rising edge, you can't.

**Dave Jones:** You can only have one as a rising edge, which I don't really know why that limitation exists. If you do know, please leave it in the comments. But anyway, just bear in mind that if you're using pattern trigger on your scope and it doesn't have a true alternate trigger or an or function like this Keysight, then really it's only good for digital channels.

**Dave Jones:** If you're trying to do this on analog waveforms, you may not be so lucky. So there you go. I I you enjoyed that and found it useful. If you did, please give it a big thumbs up and share the video and all that sort of jazz because that really helps a lot cuz YouTube algorithm kind of sucks these days.

**Dave Jones:** Doesn't really share very well. Anyway, as always, discuss in the comments or over on the EEVblog forum. Catch you next time.
