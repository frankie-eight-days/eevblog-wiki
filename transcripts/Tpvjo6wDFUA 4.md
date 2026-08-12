---
video_id: Tpvjo6wDFUA
title: EEVblog #1122 - Raspberry Pi 3 PoE Hat FAIL Investigation
url: https://www.youtube.com/watch?v=Tpvjo6wDFUA
source: youtube-asr
timestamps: {"0": 0, "1": 27, "2": 42, "3": 57, "4": 73, "5": 86, "6": 98, "7": 118, "8": 132, "9": 140, "10": 151, "11": 160, "12": 174, "13": 188, "14": 197, "15": 213, "16": 227, "17": 242, "18": 251, "19": 273, "20": 285, "21": 298, "22": 312, "23": 320, "24": 333, "25": 344, "26": 354, "27": 362, "28": 376, "29": 391, "30": 402, "31": 415, "32": 429, "33": 446, "34": 457, "35": 468, "36": 483, "37": 495, "38": 508, "39": 529, "40": 540, "41": 548, "42": 562, "43": 574, "44": 591, "45": 601, "46": 616, "47": 634, "48": 651, "49": 668, "50": 680, "51": 700, "52": 716, "53": 726, "54": 740, "55": 752, "56": 765, "57": 776, "58": 785, "59": 798, "60": 812, "61": 826, "62": 838, "63": 852, "64": 864, "65": 878, "66": 891, "67": 907, "68": 924, "69": 934, "70": 949, "71": 968, "72": 982, "73": 1000, "74": 1011, "75": 1030, "76": 1054, "77": 1070, "78": 1089, "79": 1116, "80": 1130}
---

**Dave Jones:** Hi, this is the new Raspberry Pi Model 3B Plus and it's got the new power over Ethernet capability. That's what this little pin header is here. So, you can get the new ta-da, Raspberry Pi official Raspberry Pi power over Ethernet HAT, which plugs into the top of that and plugs into that jumper down there and that takes the power over Ethernet that you can plug into the main board, which

**Dave Jones:** is quite smart. It actually taps the primary side power pins off, takes them to those pins up there so that you can put it through a DC to DC step-down converter and generate the 5 volts in here.

**Dave Jones:** So, 48 volts comes in here. A DC to DC converter, 5 volts out and then it goes out and powers your Raspberry Pi. Now, quite a few people have emailed me about this and said, "Hey, Dave, there's a problem with this new official Raspberry Pi power over Ethernet HAT.

**Dave Jones:** It powers the Raspberry Pi just fine, but when you actually plug anything into the USB ports, it can't provide any power and it shuts down the USB ports." So, I thought we'd have a little investigation.

**Dave Jones:** See what's going on. Now, a few people have complained about the surface mount power over Ethernet connector here and when they remove the board cuz it's only got the four little pads there and they are absolutely tiny.

**Dave Jones:** They've had this connector rip off the board. Yeah, just be careful when you remove this thing. They probably There's no reason to use a surface mount connector like that with the holes in back.

**Dave Jones:** There's no reason. They should have just used the through hole. But even this one, when you plug it on, it's got the holes in the top, but you can't really then go plug another HAT on top of that cuz there's really hardly any pin space left and it comes with these stand-offs and anyway, um, yeah, just be careful when you're removing this thing.

**Dave Jones:** Now, the design of this looks okay. A little transformer in the cutout there to get a lower profile. That's, you know, pretty standard fare. They've got an isolation slot down here.

**Dave Jones:** But, curiously, okay, they've got, you know, enough gap down there. But, look at the gap up there, the clearance gap under this surface mount cap here. It's just naff all.

**Dave Jones:** So, somebody forgot to peel that back there. But, we've just got a uh 1206 cap here between the grounds on either side of the isolation transformer there. That's for noise reduction.

**Dave Jones:** But, apart from that, you know, it looks pretty good. The transform looks good enough. We've got the controller here. We'll have to have a look at that. We've got an ATtiny micro here.

**Dave Jones:** So, I'm not entirely sure what the ATtiny micro is doing. Anyone? I don't know. I really haven't looked into the details of this. But, it's got a little Sunon brand fan here.

**Dave Jones:** There must be a temperature sensor somewhere, and it just comes on. Maybe that's all the ATtiny is doing. It's doing the fan controller. I don't know. So, likewise with the clearance or lack thereof up here, they've done okay there.

**Dave Jones:** But, up here, look. They got that really close as well. This is the secondary ground over here. And this is the primary side. So, why they need to peel that back as well?

**Dave Jones:** You know, maybe they should have put a little slot in there, perhaps. So, yeah, it's not the world's best isolated design, that's for sure. And of course, the isolation would have to do with around here and how the traces are actually routed.

**Dave Jones:** They've pulled back the flood fill around there. But, all the internal traces, you know, who knows what the spacing is cuz it's got to get all the way from here all the way over to the primary side of the transformer over here to there.

**Dave Jones:** So, how they're routing that out here somewhere with uh and all that sort of stuff. I don't know. And this is the uh controller. It's a monolithic power MP8007, and it's a primary side uh switcher.

**Dave Jones:** It's just got a uh quite a very nice actually um ultra-low drop diode here. And these are the output capacitors. They're at They look like they're in series, but they're actually in parallel there.

**Dave Jones:** And it's the 5 V directly out. So, there is actually no feedback on this thing to uh do secondary side regulation. It's actually done on the primary side. It requires uh careful uh design of the transformer and diode and load selection and uh stuff like that to ensure that the output is regulated.

**Dave Jones:** So, for feedback, it actually uses a uh secondary primary side coil here to actually uh sense the voltage on the core. So, you know, you got to have uh careful uh design of your transformer here.

**Dave Jones:** I'm powering it from a uh 48 V 0.35 A power over Ethernet adapter here, and it works just fine. Trust me, I've had a look. We're getting 5.07 V on the 5 V rail there.

**Dave Jones:** We can just confirm that. I have confirmed that this USB adapter is uh hunky-dory. There we go. Now, my particular board works just fine with the keyboard and mouse and this, which draws basically, you know, very little.

**Dave Jones:** Um but we can plug in an electronic uh load here, and it's drawing uh you know, 15 mA of its own accord. Set this down here, 40 mA like that.

**Dave Jones:** I can switch our load on, and it will draw that just fine. There it is, plus uh plus the Well, there's a little bit of wiggle room there. But if we go up on that, boom, it just it switches off.

**Dave Jones:** So, anything over about roughly about, you know, 40 to 50 mA, something like that. Sometimes you can just leave it there for a bit, and it will actually uh switch off.

**Dave Jones:** And if of course, if I, you know, set up to like 190 milliamps, for example, and then just press the button to switch it, it switches off the USB ports.

**Dave Jones:** And of course, they they recover just fine. You haven't damaged anything. So, we want to actually check for switching noise on this because this is a switching step-down regulator.

**Dave Jones:** So, I'm going to probe properly. I'm going to get rid of the crap, you know, the internal earth lead on there. I'm going to use the proper low inductive probing down here, and let's have a squeeze.

**Dave Jones:** We've got our switching frequency on there. It's about 24. 6 kilohertz or something like that. It's actually quite high. 320 millivolts peak to peak. So, we don't have a huge load on there, just the just a Raspberry Pi itself.

**Dave Jones:** Although, that is a fairly large load, but it's not doing anything. It's just like booted up and sitting there doing naff all. But, you can see you'd expect to see some switching frequency there, of course.

**Dave Jones:** I don't see any higher frequency uh stuff in here. There's no ringing. It's It's fairly clean, if somewhat relatively high at 320 millivolts, but it's kind of what you'd expect, really.

**Dave Jones:** I mean, it doesn't have much output capacitance and filtering on this thing. Okay, so what I'm going to do now is apply the load, 200 milliamps here. I'm going to set my trigger point just below our ripple there, and here we go.

**Dave Jones:** We'll switch it on and see if our 5-volt rail dips. Nope. Not a sausage. So, it's got nothing to do with the rail dipping. Okay, let's just try that again with some AC coupling at 200 millivolts.

**Dave Jones:** We're getting a bit more accurate now. So, there's our switching frequency like that. It's a fair bit of jitter on there, but that's what you'd expect. And let's just try and do that again.

**Dave Jones:** Shall I just take it down a bit just in case it does something, and I'll apply the load again. See if there's any dynamic change in that. Yeah, there was.

**Dave Jones:** Look at that. It's doing something strange now. Is it like some pulse skipping mode or something? Oh, yeah. Look, there's some higher spikes up there that we didn't see last time.

**Dave Jones:** That's interesting. So, if we single shot capture, there we go. Look at that. Oh, yeah, look. It's changed frequency from there to there. Some sort of mode change in the controller chip which causes that to change.

**Dave Jones:** Now, of course, if we unplug that and replug it, and I won't change anything. Oh, no. There we go. Now, it's the occasional We had the occasional glitch there.

**Dave Jones:** No, there it is. No, it's still doing it. So, that's got nothing to do with it being shut down. It just changes frequency a bit there. If you're curious to know, there you go, 23.5 and 32.85.

**Dave Jones:** Anyway, the thing that really would be a problem was is any dips in there, and trust me, if I set that single shot on there, I cannot get it to do anything.

**Dave Jones:** I've tried it tried mucking around with it quite a bit, and I just cannot get it to dip or anything like that. So, it's it's not a problem there.

**Dave Jones:** There's something else. Maybe the uh USB controller doesn't like the amount of ripple. That's just me disconnecting. You know, or there's some other little, you know, spiky noise aspect to that switching converter.

**Dave Jones:** Okay, I'm running the latest uh Raspbian stretch. And what we're looking for here is to see if we can pick up any of these boot messages, these USB overcurrent change um on the various ports.

**Dave Jones:** So, people are reporting this. There we go. And now we can have a look through here, and I've actually had a look through, and I cannot find any of these USB overcurrent messages.

**Dave Jones:** Yes, I've got my mouse and my keyboard hooked up. Okay, we'll actually connect the power, then we'll plug in the USB afterwards. We're in like Flynn. Any USB devices?

**Dave Jones:** And now let's go in and have a look. Right at the end, generic, nothing about overcurrents or anything like that. It's just detected the device. But what I'm going to do now, and I'm going to hook up power meter.

**Dave Jones:** We'll adjust that so it trips. Couple hundred milliamps, you can see it's 5.07 volts there. And then I'm going to switch it on, and it should disconnect it. Anything over like a few tens of milliamps will disconnect it.

**Dave Jones:** Bingo. All right. And reconnect. Overcurrent. There it is. We got it. So, just a Microsoft mouse and a Microsoft keyboard. They're obviously not enough to make it over range in my particular case, but uh your mileage may vary.

**Dave Jones:** We got multiple ones there. And why it like it's shut down like it's saying port two, port three. It's saying multiple ports. And then 248, that's when we plugged our keyboard and mouse back in, and Bob's your uncle.

**Dave Jones:** So, there you go. We are getting something is causing and logging the overcurrent message there. Okay, so what we're going to do now is actually measure the supply on its own and see what happens.

**Dave Jones:** Feeding in 48 volts here from my bench power supply, and we've got an electronic load on the output here. So, I've got it set to 1 W load at the moment and sure enough we're getting 5.08 V there and we're feeding in split 24 V rails there.

**Dave Jones:** So, we're drawing a load of 1 W here, but look at the rail here. We're talking 1.4 W total. So, we're you know pissing away about 0.4 W in this converter, but when you're powering it from power over Ethernet, meh, doesn't matter.

**Dave Jones:** Now, here's the issue I talked about before with the antenna earth lead in this case an inductive loop. A big ground lead like this going suspiciously near the transformer.

**Dave Jones:** It just happened to be the way I wired it and what? Look at the output there. Looks horrible. Look at all that switching component on there and you'll notice that that's actually high frequency switching.

**Dave Jones:** We can trigger on that. There we go. We can zoom right in on that. And there's all the switching crap. That's just absolute garbage, but you'll notice that that is just pick up from the lead.

**Dave Jones:** That's just bad probing technique. So, if I actually move that further away from there, it should get lower and lower in amplitude. There you go. That's just bad probing.

**Dave Jones:** So, I'll just move the probe over to this side and we don't have to worry about probing that. Now, it's all hunky-dory. Look at that. So, we're just getting what we saw before.

**Dave Jones:** No wackers. 9 kHz. Let's just have a look. See if that changes with our load. So, let's go up to a 2 W load for example. 2 W. There we go.

**Dave Jones:** Yeah, doubled. There you go. 19 kHz now. So, the frequency varies with and I'm sure if you read the data sheet, this is exactly what it's supposed to do, but the frequency varies with the load.

**Dave Jones:** But this baby is supposed to be able to do 5 V at 2.5 A. So, that's 12.5 watts. So, let's go all the way with LBJ. Yep, it's still outputting 5 volts.

**Dave Jones:** No worries. But, our frequency well, it's gone way up to 122 kilohertz there. But, our ripple voltage has still pretty much stayed the same. So, that's not too shabby.

**Dave Jones:** And look at those extra switching components. Now, I've actually got a high res mode turned on there. So, that can be a trap for young players. So, we'll take that off.

**Dave Jones:** And there we go. That's our that's our switching component down in there where it's 100 millivolts per division. So, you know, 10 20 30 almost 40 sorry, 400 millivolts peak to peak there.

**Dave Jones:** That's on our 5-volt rail at the full output power. It's not terrific, is it? And if you want to know what happens, does it regulate properly at lower loads as well?

**Dave Jones:** Well, check it out where it's 0.1 watts there. And well, you know, 5.1 it's creeping up. If we go down, look at that 5.8. Yeah, it it needs a minimum of like 0.1 watt.

**Dave Jones:** But, of course, that's no problem whatsoever cuz it's always getting that load due to the Raspberry Pi. So, yeah, nothing to worry about there. No wackers. And it's supposed to operate down to 37 volts.

**Dave Jones:** So, I've changed it down to 37 volts and our 12 and 1/2 watts output and it's working just fine. So, there's essentially nothing wrong with this Raspberry Pi power over Ethernet hat.

**Dave Jones:** Pretty much, you know, it's doing the business except perhaps in the ripple department. It may just have too much ripple, which is passing possible I've done a video on this how ripple can easily pass through our regulators, the linear the 3.3 volt linear voltage regulator.

**Dave Jones:** So, any ripple on the 5 volt rail is going to translate through mostly it's going to you know, especially at these sort of frequencies it's pretty much mostly going to pass through to the 3.3 volt rail.

**Dave Jones:** And if you got as as we're seeing there like hundreds of millivolts ripple like that can cause all sorts of issues to digital USB chips and stuff like that.

**Dave Jones:** So, it it the issue has to be there. The chip is glitching doing something. I suspect it's that USB chip that's glitching due to just noise and crap on the rails perhaps cuz like it's certainly not dropping out which was my first thing that I suspected and it's definitely not doing that.

**Dave Jones:** The the supply is doing the business. Okay, so what I'm doing now is 37 volts again input so sort of like you know, worst case voltage at the rated 12 and 1/2 watts output power 5 volts at 2 and 1/2 amps.

**Dave Jones:** Let's just get the thermal camera on here and it's pretty horrendous. Yes, it's calibrated there you go you know, near enough. I'm using emissivity of 95. We got the diode here.

**Dave Jones:** That's the that's the output diode on the secondary side. We're talking over 100°. On that diode 110 the alignments a bit off in terms of like the image camera in this thing to the heat map.

**Dave Jones:** But yeah, that diode and then the other diode on the input over here like 130° this is ridiculous. The chip sorry, the chip is uh like we're we're talking like 120.

**Dave Jones:** This is nuts. This thing is getting ridiculously hot. It's right next to that electrolytic cap, too. Uh by guy, I think I killed it. Unfortunately, I've killed it. Um it it it I was I was going to show you that, you know, if you don't trust the thermal camera, I was getting in there with my thermal couple.

**Dave Jones:** I was going right on the output side of the diode down in here. So, I was going right on the output side, and unfortunately, I shorted the output of the diode to that filter cap.

**Dave Jones:** So, um wah wah wah wah. D'oh! Um so, there you go. I'm going to um sorry, but I'm going to call it quits now because I'm not going to go and troubleshoot repair this stupid power supply.

**Dave Jones:** So, if you like the video, uh give it a thumbs-up, and uh by all means, have a good laugh down in the comments at my uh uh the stupidity in my alignment of the um temperature probe cuz it's metal, and it shorts out, and I got in there, and it just slipped off, and boom, it got between one of the uh caps and the diode, and something just went and um it

**Dave Jones:** doesn't work anymore. Magic smoke escaped. Um damn. So, I'm not going to be able to readily troubleshoot uh this thing right now. USB chip. Um yeah, we'll have to leave that for a part two, perhaps, but that's where this is looking.

**Dave Jones:** So, I hope you like that investigation. Catch you next time.
