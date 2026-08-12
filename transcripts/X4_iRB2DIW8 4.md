---
video_id: X4_iRB2DIW8
title: EEVblog #1012 - Best Bargain Ebay Bench Meter? - Fluke 8842A
url: https://www.youtube.com/watch?v=X4_iRB2DIW8
source: youtube-asr
timestamps: {"0": 1, "1": 11, "2": 27, "3": 44, "4": 61, "5": 73, "6": 88, "7": 96, "8": 109, "9": 119, "10": 139, "11": 150, "12": 173, "13": 187, "14": 196, "15": 213, "16": 225, "17": 244, "18": 253, "19": 264, "20": 280, "21": 290, "22": 304, "23": 324, "24": 334, "25": 341, "26": 353, "27": 371, "28": 379, "29": 397, "30": 409, "31": 422, "32": 432, "33": 442, "34": 451, "35": 468, "36": 477, "37": 494, "38": 506, "39": 520, "40": 532, "41": 544, "42": 558, "43": 572, "44": 587, "45": 603, "46": 612, "47": 623, "48": 636, "49": 649, "50": 661, "51": 674, "52": 688, "53": 699, "54": 715, "55": 730, "56": 746, "57": 756, "58": 769, "59": 782, "60": 792, "61": 807, "62": 815, "63": 829, "64": 839, "65": 850, "66": 863, "67": 881, "68": 908, "69": 922, "70": 939, "71": 957, "72": 968, "73": 977, "74": 988, "75": 1003, "76": 1013, "77": 1028, "78": 1057, "79": 1078, "80": 1106, "81": 1133, "82": 1156, "83": 1164, "84": 1177, "85": 1191, "86": 1207, "87": 1216, "88": 1225, "89": 1240, "90": 1252}
---

**Dave Jones:** Hi, let's take a look at the Fluke 8842A multimeter. It's a five and a half digit multimeter and it is probably one of the best second-hand meters you can pick up on eBay.

**Dave Jones:** You can pick these up working for like I've seen them go for as little as 100 bucks, but you can't always get them for that price, but they do go for around about that and this is a superb meter feature packed and it's .003% basic DC accuracy class instrument.

**Dave Jones:** It's practically like six and a half digit class accuracy for a five and a half digit meter. Fantastic. It's also got a 20 ohm range as well and a 20 millivolt range as well, handy for low level stuff.

**Dave Jones:** But this one unfortunately is faulty and I can't quite remember what the issue is, but it powers up I believe, but it's got some sort of issue. So hopefully we can see if we can fix these things, but yeah, if you're looking for a cheap, accurate bench meter, like used bench multimeter, do yourself a favor.

**Dave Jones:** Now this one seems to be missing a few things. The GPIB of course has gone and whether or not it originally had it, there's a cable flapping around in the breeze in there, but no external trigger or sample complete.

**Dave Jones:** So I'm not sure if that was option or not or whether or not they've ripped it out. Anyway, made in the US of A, USA. And a good thing is about buying these internationally is it does have a switchable international voltage on this.

**Dave Jones:** Anyway, it's got the four wire sense on the back as well. You can switch between the front and the back terminals, handy. So let's power this up and see what we get, shall we?

**Dave Jones:** And one of the things with these unfortunately is the vacuum fluorescent display. They can actually dim with time. All right, so let's power this thing up, fingers crossed. Hey, we're in.

**Dave Jones:** The display's not too shabby. I do One thing I like about this display is that it is big. Look at the size of the digits on these. It is like it's larger than your usual one.

**Dave Jones:** So, it really is quite nice. Okay, let's test the functionality. See what's broken. All right, although this Advantest R6142 voltage current generator reference is not good enough to calibrate this thing, it's good enough for doing some basic checks and it's let's have a look.

**Dave Jones:** .5, yeah, that's well, okay, we need to could be but that's significantly out. So, I'm not sure what that is in percentage but yeah, that's not terrific, is it?

**Dave Jones:** But let's go up a range. Okay, not too shabby. So, we might have to get a better meter on there to I might have to hook up my MV106 reference standard up there and then compare it with a 7 1/2 digit meter to uh get an idea of its accuracy but its basic functionality on DC volts seems to be there.

**Dave Jones:** Excellent. And the basic current functionality seems to be there as well. It's got slow updating there. Can we make that faster? Get our data our data rate. There we go.

**Dave Jones:** We can change that fast. There you go. You trade off accuracy versus Let's drop down to 10 milliamps. And let's just change that rate again. Yeah, yeah, there we go.

**Dave Jones:** Yeah. No worries. Beautiful. And the resistance seems to be bang on as well. So, oh jeez, look at this. So fast that it's it's toggling between the two. You can barely make out those digits.

**Dave Jones:** Yeah, well, they got like bang on on resistance. So, DC volts, current and resistance. It's yeah, I'm going to have to do a full calibration check but its basic functionality is there.

**Dave Jones:** Um Hmm, okay, I just found the original listing and it said it actually measured DC and volts and current fine, which it did, but it was out significantly out on resistance, apparently, which we saw it wasn't on one range, so I have to recheck that, but it didn't work on AC.

**Dave Jones:** So, I brought it over here to my Cal instruments. Without a fiddling around, let's recheck the DC volts there. Look at that, 10 volts, absolutely bang on. And we go down to one, there we go.

**Dave Jones:** Look at that. No worries. And 100 millivolts, well, it can't get much better. And on the 20 millivolt range, not a problem. And I think I found the problem.

**Dave Jones:** Check this out, volts AC, error 30. I love a meter that actually, you know, goes to the effort to, you know, they knew that this thing would have, well, they can report errors, and it actually has a an icon on the screen for error.

**Dave Jones:** So, error 30, let's go to the manual. And just some basic resistance checks, that's 10 meg. It's I've compared it with my 7 1/2 digit meter, it's just fine.

**Dave Jones:** We're good on all the ranges. So, so much for significantly out. We've got test leads and all sorts of other crap on there, 13 ohms. Okay. So, now we're really starting to shouldn't be 3 ohms out there, 1 ohm and we're measuring 4.

**Dave Jones:** Okay. So, we might have an issue there. Let me actually plug that over into my 7 1/2, and what have we got? Oh, duh. Plugged the wrong leads. Jeez, I'm an idiot.

**Dave Jones:** There we go. Oh, 1.4. So, yeah, we obviously have a problem there on the low ohms, but jeez, I'm not too fussed about that yet. What we really need to look at is that AC volts error message.

**Dave Jones:** That's what we want to fix. And I do like faults like this. Not only do we get an error message, so we'll be able to go to the service manual for this thing.

**Dave Jones:** Even if the serv- service manual doesn't have the schematics, it should list all the error codes for us. So, you know, having something that we can, you know, a fault that we can narrow down and fix like this, this is really what you want.

**Dave Jones:** So, if you see an eBay listing for something like this, and it it even tells you that it gives you an error 30 or something, then, hey, you can go to that you can download the manual before you buy it, check it out, and, you know, at least you got something to work from, unlike getting some meter that just, you know, doesn't power up.

**Dave Jones:** Although, that could be good as well, cuz it could just be a power supply issue or something like that, but something that goes completely haywire, it could be, you know, like, who knows?

**Dave Jones:** Um it's nice to have something narrowly focused like this. Let's go. And just my luck, you read the manual and error 30 is actually not a hardware fault, it's not part of the uh power on or automatic uh self-testing inside this thing, it's simply the lack of a true RMS option for this.

**Dave Jones:** It's saying you can't measure volts AC. This meter is not has not had that option installed. I didn't even know that was an option. It's like, I haven't used one of these for decades, so, yeah.

**Dave Jones:** Um so, there's nothing wrong with the volts AC. It doesn't even contain a physical module to do that, or, mate, I don't think it's a software option. It's probably some like hardware add-in daughter board.

**Dave Jones:** So, anyway, um only one thing left to do, tear this thing down. So, it turns out that, yep, that's actually option 09. So, if you're buying one of these things, there it is there, the AC 09.

**Dave Jones:** If you can get a photo of the back of the thing, make sure it has that ticked. Otherwise, I seen like they uh put a marker pen or something there at the factory.

**Dave Jones:** Make sure that's ticked, otherwise, you're not going to be actually able to measure. It's not just true RMS, you're not going to have any AC voltage or current measurement at all.

**Dave Jones:** So, yeah, bit of a showstopper. Anyway, LET'S OPEN IT. OH, the first thing I notice is the red silkscreen. Check this out. Oh. Oh. Look at that. Look at the red silk screen markers.

**Dave Jones:** Oh, that's sex on a stick. Look at that. Well, I tell you what, this is just a beautiful meter inside. We'll have a a closer look, but look at the uh ceramic resistor uh divider networks.

**Dave Jones:** 1 2 3 4 5 6 7 8 is there. Uh that's just that's just crazy. Uh anyway, yes, and they are all Fluke custom cuz Fluke actually, of course, uh famously make their own uh resistor uh hybrids.

**Dave Jones:** I Have I done a video on that? I think I may have. Hmm. Anyway, one of the uh first things and interesting things I noticed, look at this. They've completely potted that transformer.

**Dave Jones:** Look at that. It's like it's in one big potted monolithic block. I have never seen anything like that. That is absolutely amazing. Um anyway, it's very very neat and tidy.

**Dave Jones:** Got ourselves a big ass uh HRC fuse over there. Very nice to see. Got ourselves the common mode uh toroid there for the input uh terminals. One on the front, one on the black and back.

**Dave Jones:** Isn't it just beautiful and colorful? Oh, I love it. Anyway, Zilog Zilog go crazy Zilog fanboys. Um but I don't think No, it's not a Z. It's a Z8.

**Dave Jones:** Zilog Z8 processor. Wow. Anyway, we have our date code on this puppy. Uh 1994 thereabouts. I'm not sure when they stopped uh making this. Like the manual says like, you know, 2000 um copyright 2000.

**Dave Jones:** Not sure how long after that they kept uh making it, but it had a long life this puppy cuz it was a really quite a nice meter. And the good part about this meter when it comes to uh servicing, the manual for it, just the regular manual, has the full uh schematics in there.

**Dave Jones:** Absolutely fantastic. Um if you want to repair it, it should be, you know, eminently repairable. Of course, it's all uh through hole, makes it very nice, very easy to get in there and measure stuff and replace stuff.

**Dave Jones:** Of course, uses, you know, like it's going to have some customy Fluke type stuff. And it looks like there there are the odd Fluke branded chips down there. They could be just off-the-shelf ones, but actually re-badged with the Fluke part number.

**Dave Jones:** So, maybe the service manual might shed some light on that, but you know, it should be fairly repairable in that respect. So, yeah, and it's just a nice layout, easy to access.

**Dave Jones:** And you know, I'm a big rod fan boy, look at that. That's the power rod going through. Um, interesting that they've got that PCB on the bottom there. That's actually quite thin.

**Dave Jones:** That's like 0.8 mm or something like that. They're just using that as a big uh shield. So, that's quite neat. Copyright 1983, John Fluke Manufacturing Co. There you go.

**Dave Jones:** So, it probably went for like a rev F in '88. 1988, is it? I mean, that's how long this sucker uh it sold until at least 2000. Um, so I think, according to the manual.

**Dave Jones:** But anyway, um yes, they've got another rod down here. Now, that's actually for the calibration. To like you just stick a screwdriver through and you can push that and that engages the uh calibration mode over there.

**Dave Jones:** The other good thing is, check it out. Looks like we've got a Zilog E2 PROM down in there. You'll notice the lack of a battery in this thing. So, none of that pain in the ass battery backup uh calibration values either.

**Dave Jones:** So, E2 PROM all the way with LBJ. No prizes for guessing that custom Fluke chip is the ADC. Uh the dual slope or a multi slope integrator. And is that our voltage reference down there?

**Dave Jones:** I'll get my macro lens out. Woah, for all you LT fan boys. Aha, we don't have an LM399, we have an LTFLU, which is a LT Fluke manufactured by Linear Technology.

**Dave Jones:** It was a custom job for Fluke, and it's not the LT LTZ 1000 either. It's a different variant that doesn't have a built-in heater, but it's used in some of the It's used in the Fluke 732 voltage reference standard.

**Dave Jones:** That's why this meter is so darn good. It's, you know, .003% class meter, because the reference in it, the LTFLU, is brilliant. So, that is massive overkill for a five and a half digit meter.

**Dave Jones:** It'd be overkill for a six and a half digit multimeter, which would use the classic, you know, LM 399, for example, which is not as good as this. This is like almost a transfer standard class reference, and they've got it in this five and a half digit meter.

**Dave Jones:** So, if you buy one of these, you can buy one of these. I paid 60 bucks for this, you know, broken, in quote marks, you know, sold as not working.

**Dave Jones:** And some people would say it's worth it just for the reference alone, all the volt nuts out there, anyway, I'm sure. Check out down on the PCB, copyright 1983.

**Dave Jones:** So, this one was manufactured in '94, and as I said, so it probably had, you know, getting on to a 20-year lifespan, I would suspect. Awesome. Now, if you're wondering, where does the AC09 true RMS option go?

**Dave Jones:** Well, it actually goes into this big ass header here, and I'll include a photo of that. It's actually a separate board, separate whole separate module that actually plugs into that.

**Dave Jones:** So, obviously, the software detects, it's got a pin on there that detects whether or not it's installed, and it's not error 30 when you press AC. Of course, they didn't even bother to take the button out of the front panel, because that would be a user installable option, just, you know, opening this thing up, plugging the board in.

**Dave Jones:** Yeah, you'd void your calibration if there was a cal sticker on it, etc. But, still, you know, it's not something that has to be done at at the factory, that's for sure.

**Dave Jones:** Now, if you are working on these, it should be pretty safe, you know, all the transformers potted, everything else, all the mains wiring's nice and neat and tidy, but the range switch on the back of the the rear side of the board there is exposed.

**Dave Jones:** So, just be careful that you don't, you know, accidentally just go, "Ah, yeah, I'll just move it and grab the the thing like that." Just be careful, but apart from that, should be pretty safe to work on.

**Dave Jones:** I love how that poor power resistor there has been almost bodged in, although it does show the silk screen does imply that it sort of supposed to be mounted vertically, but neat.

**Dave Jones:** And more bad news, it works. Oh, the EVBlog repair curse is just hopeless. I buy a, you know, a faulty bit of gear, and there was nothing wrong with that ohms range.

**Dave Jones:** What it was, it it was most likely just the input input selection of what the front rear selection switch here probably just had a dicky contact. It just needed to be cycled a couple of times, and bingo, like what 1.4, that's the leads in the box and everything else.

**Dave Jones:** That's what my other 7 1/2 digit meter measures with this box on that range. So, that is it it's fine. Everything's practically bang on with this meter. Like, it's Ah, yeah, I need to probably a bit more exhaustive calibration checking, which is, you know, can be really tedious, but it spot check on each range so far is well within spec.

**Dave Jones:** So, yeah, I like unbelievable. Unbelievable. Anyway, very useful 20 ohm range that for, you know, 1 milliohm resolution, very nice for tracking down shorts and stuff like that. Very handy.

**Dave Jones:** As is the 20 mV mode as well. That's that's pretty jazzy, 1 microvolt resolution. And given that this is a .003% class basic instrument, I like if you can pick one of these up for a you know 100 bucks, definitely do yourself a favor and get one.

**Dave Jones:** Awesome. So it's that switch down there. That's the culprit there and they're going to be like self effectively self-wiping self-cleaning contacts in there. So unless it proves to be an intermittent issue, it will require more use and more playing around with them to determine that, but it seems rock solid now.

**Dave Jones:** So I think it just had a bit of crud in there and just needed to be cycled once and bingo. So I wouldn't be going spraying contact cleaner in there willy-nilly.

**Dave Jones:** You know, there's people who say, "Oh yeah, the first thing I do is contact cleaner right throughout the switch." And yeah, you could just do it on the squirt on the top and it'd get down the individual pins down in there.

**Dave Jones:** So if you got your favorite contact cleaner, then by all means go for it, but I I don't think I'd bother on this one cuz it hasn't caused me an issue apart from that one time.

**Dave Jones:** You know, it's probably been sitting in storage for 15 years. And by the way, if you're worried about, you know, the annoying part about having to take off the cover to replace the fuse down there, don't really worry about it because it's actually just a backup fuse.

**Dave Jones:** The primary one is on the front. Non-HRC, of course, but that puppy's going to you know just in general use is going to blow first. You typically wouldn't be using these on high power and main stuff.

**Dave Jones:** They're like more for bench measurement use and stuff like that. So that's all fine and dandy. You shouldn't have to open the case, especially if you've got one with a recent cal sticker, then yeah, you can just replace the fuse on the front.

**Dave Jones:** No worries. And here's an old friend I haven't dragged down in a while, the Fluke 5458 resistance calibrator. I've been meaning to do a calibration of this a calibration of the calibrator using my we come resistance standard which I've got which is actually better than this and you can use the one single 10k transfer standard to actually calibrate all the ranges on this there's a sneaky procedure that

**Dave Jones:** allows you to do that I'll be meaning to do a video on that for a long time so I might get around to it one day anyway this allows us this is a reference resistor standard I've done a teardown of this I'll link it in down at the end it's beautiful inside check out that video trust me it's fantastic it's almost pornographic and this allows me to

**Dave Jones:** generate a low value resistances I'm on the 10k standard at the moment but I haven't verified the calibration of this right down so it claims to be 10.00012 anyway more than good enough for this there we go we're in a last couple of last least significant digits there of course if we switch over to the two wire mode you see 10.3 cuz it includes all the lead resistance and all contacts and

**Dave Jones:** every you know the contacts inside the switching in there and everything else but on four wire mode of course there you go it's basically bang on and we can actually use the one k the one ohm standard down here you got to say yeah that's 9996 so it's a once again couple of least significant digits out that's got to be well within spec so no worries whatsoever and yeah we could

**Dave Jones:** do this until the cows come home I know everyone wants to see every range don't they yes all right all right I haven't tried this oh look at that almost bang on oh oh and you know it's all these are going to be well within spec well within spec so this meter is a winner winner.

**Dave Jones:** Yep. That's good enough. Winner winner chicken dinner. Oh, look at that. And 100 mega, I don't think it does 100 meg. No, I think it only goes up to 20.

**Dave Jones:** I can't remember how many counts this is. Uh 20 Uh 200,000 count? Something like that? Anyway, there you go. Bang on. So, once again, sorry. I was hoping to bring you a repair video.

**Dave Jones:** I buy these repair things occasionally. Um and you know, hoping, crossing my fingers, that they'll be an interesting repair, not just a simple blown fuse, or not beyond economical repair, as quite a few of my repairs have turned out to be.

**Dave Jones:** So, yeah, I'm not even going to title this a repair video, cuz it's not. It's just a look at the Fluke 8842A multimeter with a pretty like almost a transfer class reference standard in there, that FLU uh one uh reference standard.

**Dave Jones:** If you can pick like for like for 100 bucks, you can get these that are working. You wouldn't get one that's, you know, recently calibrated for that. If you can, um then an absolute bargain.

**Dave Jones:** But yeah, by all means, uh put a search term on eBay. I know that if I mention something's good and available on eBay, they, you know, double in price instantly.

**Dave Jones:** So, sorry, you know. But these things have gone for as little as like 100 bucks. But yeah, uh it's like fantastic meter. If you can still pick it up with a decent display, cuz these uh vacuum fluorescents do fade over time.

**Dave Jones:** I think someone might have even done like a replacement display project for it or something like that. But yeah, really nice old school meter, the 8842A. If you can pick one up, do yourself a favor.

**Dave Jones:** Anyway, if you like that video, please give it a big thumbs up. As always, discuss down below. Catch you next time. Mhm.
