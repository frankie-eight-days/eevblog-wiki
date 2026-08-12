---
video_id: Tpvjo6wDFUA
title: EEVblog #1122 - Raspberry Pi 3 PoE Hat FAIL Investigation
url: https://www.youtube.com/watch?v=Tpvjo6wDFUA
source: youtube-asr
---

**Dave Jones:** Hi, this is the new Raspberry Pi Model 3B Plus and it's got the new power over Ethernet capability. That's what this little pin header is here. So, you can get the new ta-da, Raspberry Pi official Raspberry Pi power over Ethernet HAT,

**Dave Jones:** which plugs into the top of that and plugs into that jumper down there and that takes the power over Ethernet that you can plug into the main board, which is quite smart. It actually taps the primary side power pins off, takes

**Dave Jones:** them to those pins up there so that you can put it through a DC to DC step-down converter and generate the 5 volts in here. So, 48 volts comes in here. A DC to DC converter, 5 volts out and then it

**Dave Jones:** goes out and powers your Raspberry Pi. Now, quite a few people have emailed me about this and said, "Hey, Dave, there's a problem with this new official Raspberry Pi power over Ethernet HAT. It powers the Raspberry Pi just fine, but

**Dave Jones:** when you actually plug anything into the USB ports, it can't provide any power and it shuts down the USB ports." So, I thought we'd have a little investigation. See what's going on. Now, a few people have complained about the surface mount power

**Dave Jones:** over Ethernet connector here and when they remove the board cuz it's only got the four little pads there and they are absolutely tiny. They've had this connector rip off the board. Yeah, just be careful when you remove this thing.

**Dave Jones:** They probably There's no reason to use a surface mount connector like that with the holes in back. There's no reason. They should have just used the through hole. But even this one, when you plug it on, it's got the holes

**Dave Jones:** in the top, but you can't really then go plug another HAT on top of that cuz there's really hardly any pin space left and it comes with these stand-offs and anyway, um, yeah, just be careful when you're removing this thing. Now, the

**Dave Jones:** design of this looks okay. A little transformer in the cutout there to get a lower profile. That's, you know, pretty standard fare. They've got an isolation slot down here. But, curiously, okay, they've got, you know, enough gap down there. But, look

**Dave Jones:** at the gap up there, the clearance gap under this surface mount cap here. It's just naff all. So, somebody forgot to peel that back there. But, we've just got a uh 1206 cap here between the grounds on either side of the isolation transformer

**Dave Jones:** there. That's for noise reduction. But, apart from that, you know, it looks pretty good. The transform looks good enough. We've got the controller here. We'll have to have a look at that. We've got an ATtiny micro here. So, I'm not

**Dave Jones:** entirely sure what the ATtiny micro is doing. Anyone? I don't know. I really haven't looked into the details of this. But, it's got a little Sunon brand fan here. There must be a temperature sensor somewhere, and it just comes on. Maybe

**Dave Jones:** that's all the ATtiny is doing. It's doing the fan controller. I don't know. So, likewise with the clearance or lack thereof up here, they've done okay there. But, up here, look. They got that really close as well. This is the

**Dave Jones:** secondary ground over here. And this is the primary side. So, why they need to peel that back as well? You know, maybe they should have put a little slot in there, perhaps. So, yeah, it's not the world's best isolated

**Dave Jones:** design, that's for sure. And of course, the isolation would have to do with around here and how the traces are actually routed. They've pulled back the flood fill around there. But, all the internal traces, you know, who knows

**Dave Jones:** what the spacing is cuz it's got to get all the way from here all the way over to the primary side of the transformer over here to there. So, how they're routing that out here somewhere with uh and all that sort of stuff. I don't

**Dave Jones:** know. And this is the uh controller. It's a monolithic power MP8007, and it's a primary side uh switcher. It's just got a uh quite a very nice actually um ultra-low drop diode here. And these are the output capacitors. They're at They

**Dave Jones:** look like they're in series, but they're actually in parallel there. And it's the 5 V directly out. So, there is actually no feedback on this thing to uh do secondary side regulation. It's actually done on the primary side. It requires uh

**Dave Jones:** careful uh design of the transformer and diode and load selection and uh stuff like that to ensure that the output is regulated. So, for feedback, it actually uses a uh secondary primary side coil here to actually uh sense the voltage on

**Dave Jones:** the core. So, you know, you got to have uh careful uh design of your transformer here. I'm powering it from a uh 48 V 0.35 A power over Ethernet adapter here, and it works just fine. Trust me, I've had a

**Dave Jones:** look. We're getting 5.07 V on the 5 V rail there. We can just confirm that. I have confirmed that this USB adapter is uh hunky-dory. There we go. Now, my particular board works just fine with the keyboard and mouse and this, which

**Dave Jones:** draws basically, you know, very little. Um but we can plug in an electronic uh load here, and it's drawing uh you know, 15 mA of its own accord. Set this down here, 40 mA like that. I can switch our load on, and it will draw

**Dave Jones:** that just fine. There it is, plus uh plus the Well, there's a little bit of wiggle room there. But if we go up on that, boom, it just it switches off. So, anything over about roughly about, you know, 40 to 50 mA, something like that.

**Dave Jones:** Sometimes you can just leave it there for a bit, and it will actually uh switch off. And if of course, if I, you know, set up to like 190 milliamps, for example, and then just press the button to switch it, it switches off the USB

**Dave Jones:** ports. And of course, they they recover just fine. You haven't damaged anything. So, we want to actually check for switching noise on this because this is a switching step-down regulator. So, I'm going to probe properly. I'm going to

**Dave Jones:** get rid of the crap, you know, the internal earth lead on there. I'm going to use the proper low inductive probing down here, and let's have a squeeze. We've got our switching frequency on there. It's about 24. 6 kilohertz or something like that. It's

**Dave Jones:** actually quite high. 320 millivolts peak to peak. So, we don't have a huge load on there, just the just a Raspberry Pi itself. Although, that is a fairly large load, but it's not doing anything. It's just like booted up and sitting there doing naff

**Dave Jones:** all. But, you can see you'd expect to see some switching frequency there, of course. I don't see any higher frequency uh stuff in here. There's no ringing. It's It's fairly clean, if somewhat relatively high at 320 millivolts, but it's kind of what you'd

**Dave Jones:** expect, really. I mean, it doesn't have much output capacitance and filtering on this thing. Okay, so what I'm going to do now is apply the load, 200 milliamps here. I'm going to set my trigger point just below our ripple there, and here we go. We'll

**Dave Jones:** switch it on and see if our 5-volt rail dips. Nope. Not a sausage. So, it's got nothing to do with the rail dipping. Okay, let's just try that again with some AC coupling at 200 millivolts. We're getting a bit more accurate now.

**Dave Jones:** So, there's our switching frequency like that. It's a fair bit of jitter on there, but that's what you'd expect. And let's just try and do that again. Shall I just take it down a bit just in case it does something, and I'll apply the

**Dave Jones:** load again. See if there's any dynamic change in that. Yeah, there was. Look at that. It's doing something strange now. Is it like some pulse skipping mode or something? Oh, yeah. Look, there's some higher spikes up there that we didn't see

**Dave Jones:** last time. That's interesting. So, if we single shot capture, there we go. Look at that. Oh, yeah, look. It's changed frequency from there to there. Some sort of mode change in the controller chip which causes that to change. Now,

**Dave Jones:** of course, if we unplug that and replug it, and I won't change anything. Oh, no. There we go. Now, it's the occasional We had the occasional glitch there. No, there it is. No, it's still doing it. So, that's got nothing to do with it

**Dave Jones:** being shut down. It just changes frequency a bit there. If you're curious to know, there you go, 23.5 and 32.85. Anyway, the thing that really would be a problem was is any dips in there, and trust me, if I set that single shot on

**Dave Jones:** there, I cannot get it to do anything. I've tried it tried mucking around with it quite a bit, and I just cannot get it to dip or anything like that. So, it's it's not a problem there. There's something else. Maybe the

**Dave Jones:** uh USB controller doesn't like the amount of ripple. That's just me disconnecting. You know, or there's some other little, you know, spiky noise aspect to that switching converter. Okay, I'm running the latest uh Raspbian stretch. And what we're looking for here

**Dave Jones:** is to see if we can pick up any of these boot messages, these USB overcurrent change um on the various ports. So, people are reporting this. There we go. And now we can have a look through here, and I've actually had a look through,

**Dave Jones:** and I cannot find any of these USB overcurrent messages. Yes, I've got my mouse and my keyboard hooked up. Okay, we'll actually connect the power, then we'll plug in the USB afterwards. We're in like Flynn. Any USB devices? And now

**Dave Jones:** let's go in and have a look. Right at the end, generic, nothing about overcurrents or anything like that. It's just detected the device. But what I'm going to do now, and I'm going to hook up power meter. We'll adjust that so it

**Dave Jones:** trips. Couple hundred milliamps, you can see it's 5.07 volts there. And then I'm going to switch it on, and it should disconnect it. Anything over like a few tens of milliamps will disconnect it.

**Dave Jones:** Bingo. All right. And reconnect. Overcurrent. There it is. We got it. So, just a Microsoft mouse and a Microsoft keyboard. They're obviously not enough to make it over range in my particular case, but uh your mileage may vary. We got multiple

**Dave Jones:** ones there. And why it like it's shut down like it's saying port two, port three. It's saying multiple ports. And then 248, that's when we plugged our keyboard and mouse back in, and Bob's your uncle. So, there you go. We are getting

**Dave Jones:** something is causing and logging the overcurrent message there. Okay, so what we're going to do now is actually measure the supply on its own and see what happens. Feeding in 48 volts here from my bench power supply, and we've got an electronic load

**Dave Jones:** on the output here. So, I've got it set to 1 W load at the moment and sure enough we're getting 5.08 V there and we're feeding in split 24 V rails there. So, we're drawing a load of 1 W here, but look at the rail here.

**Dave Jones:** We're talking 1.4 W total. So, we're you know pissing away about 0.4 W in this converter, but when you're powering it from power over Ethernet, meh, doesn't matter. Now, here's the issue I talked about before with the antenna earth lead

**Dave Jones:** in this case an inductive loop. A big ground lead like this going suspiciously near the transformer. It just happened to be the way I wired it and what? Look at the output there. Looks horrible. Look at all that switching component on

**Dave Jones:** there and you'll notice that that's actually high frequency switching. We can trigger on that. There we go. We can zoom right in on that. And there's all the switching crap. That's just absolute garbage, but you'll notice that that is just pick up from the lead.

**Dave Jones:** That's just bad probing technique. So, if I actually move that further away from there, it should get lower and lower in amplitude. There you go. That's just bad probing. So, I'll just move the probe over to this side and we don't have to worry

**Dave Jones:** about probing that. Now, it's all hunky-dory. Look at that. So, we're just getting what we saw before. No wackers. 9 kHz. Let's just have a look. See if that changes with our load. So, let's go up to a 2 W load for

**Dave Jones:** example. 2 W. There we go. Yeah, doubled. There you go. 19 kHz now. So, the frequency varies with and I'm sure if you read the data sheet, this is exactly what it's supposed to do, but the frequency varies with the load. But

**Dave Jones:** this baby is supposed to be able to do 5 V at 2.5 A. So, that's 12.5 watts. So, let's go all the way with LBJ. Yep, it's still outputting 5 volts. No worries. But, our frequency well, it's gone way up to 122 kilohertz

**Dave Jones:** there. But, our ripple voltage has still pretty much stayed the same. So, that's not too shabby. And look at those extra switching components. Now, I've actually got a high res mode turned on there. So, that can be a trap

**Dave Jones:** for young players. So, we'll take that off. And there we go. That's our that's our switching component down in there where it's 100 millivolts per division. So, you know, 10 20 30 almost 40 sorry, 400 millivolts peak to peak there. That's on our 5-volt

**Dave Jones:** rail at the full output power. It's not terrific, is it? And if you want to know what happens, does it regulate properly at lower loads as well? Well, check it out where it's 0.1 watts there. And well, you know, 5.1

**Dave Jones:** it's creeping up. If we go down, look at that 5.8. Yeah, it it needs a minimum of like 0.1 watt. But, of course, that's no problem whatsoever cuz it's always getting that load due to the Raspberry Pi. So, yeah, nothing to worry about

**Dave Jones:** there. No wackers. And it's supposed to operate down to 37 volts. So, I've changed it down to 37 volts and our 12 and 1/2 watts output and it's working just fine. So, there's essentially nothing wrong with this Raspberry Pi power over Ethernet hat.

**Dave Jones:** Pretty much, you know, it's doing the business except perhaps in the ripple department. It may just have too much ripple, which is passing possible I've done a video on this how ripple can easily pass through our regulators, the

**Dave Jones:** linear the 3.3 volt linear voltage regulator. So, any ripple on the 5 volt rail is going to translate through mostly it's going to you know, especially at these sort of frequencies it's pretty much mostly going to pass through to the 3.3 volt rail. And if you

**Dave Jones:** got as as we're seeing there like hundreds of millivolts ripple like that can cause all sorts of issues to digital USB chips and stuff like that. So, it it the issue has to be there. The chip is glitching doing something. I

**Dave Jones:** suspect it's that USB chip that's glitching due to just noise and crap on the rails perhaps cuz like it's certainly not dropping out which was my first thing that I suspected and it's definitely not doing that. The the

**Dave Jones:** supply is doing the business. Okay, so what I'm doing now is 37 volts again input so sort of like you know, worst case voltage at the rated 12 and 1/2 watts output power 5 volts at 2 and 1/2 amps. Let's just get the

**Dave Jones:** thermal camera on here and it's pretty horrendous. Yes, it's calibrated there you go you know, near enough. I'm using emissivity of 95. We got the diode here. That's the that's the output diode on the secondary side. We're talking over

**Dave Jones:** 100°. On that diode 110 the alignments a bit off in terms of like the image camera in this thing to the heat map. But yeah, that diode and then the other diode on the input over here like 130°

**Dave Jones:** this is ridiculous. The chip sorry, the chip is uh like we're we're talking like 120. This is nuts. This thing is getting ridiculously hot. It's right next to that electrolytic cap, too. Uh by guy, I think I killed it.

**Dave Jones:** Unfortunately, I've killed it. Um it it it I was I was going to show you that, you know, if you don't trust the thermal camera, I was getting in there with my thermal couple. I was going right on the output

**Dave Jones:** side of the diode down in here. So, I was going right on the output side, and unfortunately, I shorted the output of the diode to that filter cap. So, um wah wah wah wah. D'oh! Um so, there you go. I'm going to um

**Dave Jones:** sorry, but I'm going to call it quits now because I'm not going to go and troubleshoot repair this stupid power supply. So, if you like the video, uh give it a thumbs-up, and uh by all means, have a

**Dave Jones:** good laugh down in the comments at my uh uh the stupidity in my alignment of the um temperature probe cuz it's metal, and it shorts out, and I got in there, and it just slipped off, and boom, it got

**Dave Jones:** between one of the uh caps and the diode, and something just went and um it doesn't work anymore. Magic smoke escaped. Um damn. So, I'm not going to be able to readily troubleshoot uh this thing right now. USB chip. Um yeah,

**Dave Jones:** we'll have to leave that for a part two, perhaps, but that's where this is looking. So, I hope you like that investigation. Catch you next time.
