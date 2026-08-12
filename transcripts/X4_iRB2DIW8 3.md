---
video_id: X4_iRB2DIW8
title: EEVblog #1012 - Best Bargain Ebay Bench Meter? - Fluke 8842A
url: https://www.youtube.com/watch?v=X4_iRB2DIW8
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 27, "3": 44, "4": 55, "5": 70, "6": 83, "7": 96, "8": 113, "9": 125, "10": 147, "11": 164, "12": 177, "13": 193, "14": 204, "15": 218, "16": 235, "17": 247, "18": 264, "19": 278, "20": 292, "21": 307, "22": 328, "23": 340, "24": 351, "25": 361, "26": 372, "27": 383, "28": 400, "29": 414, "30": 426, "31": 439, "32": 451, "33": 470, "34": 486, "35": 500, "36": 520, "37": 534, "38": 552, "39": 567, "40": 580, "41": 593, "42": 610, "43": 623, "44": 638, "45": 654, "46": 668, "47": 683, "48": 695, "49": 713, "50": 732, "51": 746, "52": 761, "53": 777, "54": 791, "55": 802, "56": 813, "57": 823, "58": 835, "59": 848, "60": 865, "61": 881, "62": 899, "63": 921, "64": 937, "65": 953, "66": 964, "67": 975, "68": 986, "69": 998, "70": 1012, "71": 1023, "72": 1039, "73": 1057, "74": 1068, "75": 1086, "76": 1101, "77": 1115, "78": 1133, "79": 1148, "80": 1164, "81": 1179, "82": 1193, "83": 1207, "84": 1218, "85": 1233, "86": 1245, "87": 1279}
---

**Dave Jones:** Hi, let's take a look at the Fluke 8842A multimeter. It's a five and a half digit multimeter and it is probably one of the best second-hand meters you can pick up on eBay. You can pick these up working

**Dave Jones:** for like I've seen them go for as little as 100 bucks, but you can't always get them for that price, but they do go for around about that and this is a superb meter feature packed and it's .003%

**Dave Jones:** basic DC accuracy class instrument. It's practically like six and a half digit class accuracy for a five and a half digit meter. Fantastic. It's also got a 20 ohm range as well and a 20 millivolt range as well, handy for low level

**Dave Jones:** stuff. But this one unfortunately is faulty and I can't quite remember what the issue is, but it powers up I believe, but it's got some sort of issue. So hopefully we can see if we can fix these things, but yeah, if you're

**Dave Jones:** looking for a cheap, accurate bench meter, like used bench multimeter, do yourself a favor. Now this one seems to be missing a few things. The GPIB of course has gone and whether or not it originally had it, there's a cable

**Dave Jones:** flapping around in the breeze in there, but no external trigger or sample complete. So I'm not sure if that was option or not or whether or not they've ripped it out. Anyway, made in the US of A, USA. And a good thing is about buying

**Dave Jones:** these internationally is it does have a switchable international voltage on this. Anyway, it's got the four wire sense on the back as well. You can switch between the front and the back terminals, handy. So let's power this up

**Dave Jones:** and see what we get, shall we? And one of the things with these unfortunately is the vacuum fluorescent display. They can actually dim with time. All right, so let's power this thing up, fingers crossed. Hey, we're in. The display's not too shabby. I do One

**Dave Jones:** thing I like about this display is that it is big. Look at the size of the digits on these. It is like it's larger than your usual one. So, it really is quite nice. Okay, let's test the functionality. See what's broken. All

**Dave Jones:** right, although this Advantest R6142 voltage current generator reference is not good enough to calibrate this thing, it's good enough for doing some basic checks and it's let's have a look. .5, yeah, that's well, okay, we need to could be but that's significantly out.

**Dave Jones:** So, I'm not sure what that is in percentage but yeah, that's not terrific, is it? But let's go up a range. Okay, not too shabby. So, we might have to get a better meter on there to I might have to hook up my MV106

**Dave Jones:** reference standard up there and then compare it with a 7 1/2 digit meter to uh get an idea of its accuracy but its basic functionality on DC volts seems to be there. Excellent. And the basic current functionality seems to be

**Dave Jones:** there as well. It's got slow updating there. Can we make that faster? Get our data our data rate. There we go. We can change that fast. There you go. You trade off accuracy versus Let's drop down to 10 milliamps.

**Dave Jones:** And let's just change that rate again. Yeah, yeah, there we go. Yeah. No worries. Beautiful.

**Dave Jones:** And the resistance seems to be bang on as well. So, oh jeez, look at this. So fast that it's it's toggling between the two. You can barely make out those digits. Yeah, well, they got like bang on on resistance. So,

**Dave Jones:** DC volts, current and resistance. It's yeah, I'm going to have to do a full calibration check but its basic functionality is there. Um Hmm, okay, I just found the original listing and it said it actually measured DC and volts and current fine, which it

**Dave Jones:** did, but it was out significantly out on resistance, apparently, which we saw it wasn't on one range, so I have to recheck that, but it didn't work on AC. So, I brought it over here to my Cal instruments. Without a fiddling around,

**Dave Jones:** let's recheck the DC volts there. Look at that, 10 volts, absolutely bang on. And we go down to one, there we go. Look at that. No worries. And 100 millivolts, well, it can't get much better. And on the 20 millivolt range, not a problem.

**Dave Jones:** And I think I found the problem. Check this out, volts AC, error 30. I love a meter that actually, you know, goes to the effort to, you know, they knew that this thing would have, well, they can report errors, and

**Dave Jones:** it actually has a an icon on the screen for error. So, error 30, let's go to the manual. And just some basic resistance checks, that's 10 meg. It's I've compared it with my 7 1/2 digit meter, it's just fine. We're good on all the

**Dave Jones:** ranges. So, so much for significantly out. We've got test leads and all sorts of other crap on there, 13 ohms. Okay. So, now we're really starting to shouldn't be 3 ohms out there, 1 ohm and we're measuring 4. Okay. So, we might

**Dave Jones:** have an issue there. Let me actually plug that over into my 7 1/2, and what have we got? Oh, duh. Plugged the wrong leads. Jeez, I'm an idiot. There we go. Oh, 1.4. So, yeah, we obviously have a problem there on the

**Dave Jones:** low ohms, but jeez, I'm not too fussed about that yet. What we really need to look at is that AC volts error message. That's what we want to fix. And I do like faults like this. Not only do we get an error

**Dave Jones:** message, so we'll be able to go to the service manual for this thing. Even if the serv- service manual doesn't have the schematics, it should list all the error codes for us. So, you know, having something that we can, you know, a fault

**Dave Jones:** that we can narrow down and fix like this, this is really what you want. So, if you see an eBay listing for something like this, and it it even tells you that it gives you an error 30 or something,

**Dave Jones:** then, hey, you can go to that you can download the manual before you buy it, check it out, and, you know, at least you got something to work from, unlike getting some meter that just, you know, doesn't power up. Although, that could

**Dave Jones:** be good as well, cuz it could just be a power supply issue or something like that, but something that goes completely haywire, it could be, you know, like, who knows? Um it's nice to have something narrowly focused like this.

**Dave Jones:** Let's go. And just my luck, you read the manual and error 30 is actually not a hardware fault, it's not part of the uh power on or automatic uh self-testing inside this thing, it's simply the lack of a true RMS option for this. It's

**Dave Jones:** saying you can't measure volts AC. This meter is not has not had that option installed. I didn't even know that was an option. It's like, I haven't used one of these for decades, so, yeah. Um so, there's nothing wrong with the volts AC.

**Dave Jones:** It doesn't even contain a physical module to do that, or, mate, I don't think it's a software option. It's probably some like hardware add-in daughter board. So, anyway, um only one thing left to do, tear this thing down.

**Dave Jones:** So, it turns out that, yep, that's actually option 09. So, if you're buying one of these things, there it is there, the AC 09. If you can get a photo of the back of the thing, make sure it has that ticked. Otherwise,

**Dave Jones:** I seen like they uh put a marker pen or something there at the factory. Make sure that's ticked, otherwise, you're not going to be actually able to measure. It's not just true RMS, you're not going to have any AC voltage or

**Dave Jones:** current measurement at all. So, yeah, bit of a showstopper. Anyway, LET'S OPEN IT. OH, the first thing I notice is the red silkscreen. Check this out. Oh. Oh. Look at that. Look at the red silk screen markers. Oh, that's sex on a stick. Look at that.

**Dave Jones:** Well, I tell you what, this is just a beautiful meter inside. We'll have a a closer look, but look at the uh ceramic resistor uh divider networks. 1 2 3 4 5 6 7 8 is there. Uh that's just that's

**Dave Jones:** just crazy. Uh anyway, yes, and they are all Fluke custom cuz Fluke actually, of course, uh famously make their own uh resistor uh hybrids. I Have I done a video on that? I think I may have. Hmm. Anyway, one of the uh

**Dave Jones:** first things and interesting things I noticed, look at this. They've completely potted that transformer. Look at that. It's like it's in one big potted monolithic block. I have never seen anything like that. That is absolutely amazing. Um anyway, it's very very neat

**Dave Jones:** and tidy. Got ourselves a big ass uh HRC fuse over there. Very nice to see. Got ourselves the common mode uh toroid there for the input uh terminals. One on the front, one on the black and back. Isn't it just beautiful and colorful?

**Dave Jones:** Oh, I love it. Anyway, Zilog Zilog go crazy Zilog fanboys. Um but I don't think No, it's not a Z. It's a Z8. Zilog Z8 processor. Wow. Anyway, we have our date code on this puppy. Uh 1994 thereabouts. I'm not sure when they

**Dave Jones:** stopped uh making this. Like the manual says like, you know, 2000 um copyright 2000. Not sure how long after that they kept uh making it, but it had a long life this puppy cuz it was a really quite a nice meter.

**Dave Jones:** And the good part about this meter when it comes to uh servicing, the manual for it, just the regular manual, has the full uh schematics in there. Absolutely fantastic. Um if you want to repair it, it should be, you know, eminently

**Dave Jones:** repairable. Of course, it's all uh through hole, makes it very nice, very easy to get in there and measure stuff and replace stuff. Of course, uses, you know, like it's going to have some customy Fluke type stuff. And it looks

**Dave Jones:** like there there are the odd Fluke branded chips down there. They could be just off-the-shelf ones, but actually re-badged with the Fluke part number. So, maybe the service manual might shed some light on that, but you know, it should be fairly repairable in

**Dave Jones:** that respect. So, yeah, and it's just a nice layout, easy to access. And you know, I'm a big rod fan boy, look at that. That's the power rod going through. Um, interesting that they've got that PCB on the bottom there. That's

**Dave Jones:** actually quite thin. That's like 0.8 mm or something like that. They're just using that as a big uh shield. So, that's quite neat. Copyright 1983, John Fluke Manufacturing Co. There you go. So, it probably went for like a rev

**Dave Jones:** F in '88. 1988, is it? I mean, that's how long this sucker uh it sold until at least 2000. Um, so I think, according to the manual. But anyway, um yes, they've got another rod down here. Now, that's actually for

**Dave Jones:** the calibration. To like you just stick a screwdriver through and you can push that and that engages the uh calibration mode over there. The other good thing is, check it out. Looks like we've got a Zilog E2 PROM down in there. You'll

**Dave Jones:** notice the lack of a battery in this thing. So, none of that pain in the ass battery backup uh calibration values either. So, E2 PROM all the way with LBJ. No prizes for guessing that custom Fluke chip is the

**Dave Jones:** ADC. Uh the dual slope or a multi slope integrator. And is that our voltage reference down there? I'll get my macro lens out. Woah, for all you LT fan boys. Aha, we don't have an LM399, we have an

**Dave Jones:** LTFLU, which is a LT Fluke manufactured by Linear Technology. It was a custom job for Fluke, and it's not the LT LTZ 1000 either. It's a different variant that doesn't have a built-in heater, but it's used in some of the

**Dave Jones:** It's used in the Fluke 732 voltage reference standard. That's why this meter is so darn good. It's, you know, .003% class meter, because the reference in it, the LTFLU, is brilliant. So, that is massive overkill for a five and a half digit meter. It'd

**Dave Jones:** be overkill for a six and a half digit multimeter, which would use the classic, you know, LM 399, for example, which is not as good as this. This is like almost a transfer standard class reference, and they've got it in this five and a half

**Dave Jones:** digit meter. So, if you buy one of these, you can buy one of these. I paid 60 bucks for this, you know, broken, in quote marks, you know, sold as not working. And some people would say it's worth it just for

**Dave Jones:** the reference alone, all the volt nuts out there, anyway, I'm sure. Check out down on the PCB, copyright 1983. So, this one was manufactured in '94, and as I said, so it probably had, you know, getting on to a 20-year lifespan,

**Dave Jones:** I would suspect. Awesome. Now, if you're wondering, where does the AC09 true RMS option go? Well, it actually goes into this big ass header here, and I'll include a photo of that. It's actually a separate board, separate whole separate

**Dave Jones:** module that actually plugs into that. So, obviously, the software detects, it's got a pin on there that detects whether or not it's installed, and it's not error 30 when you press AC. Of course, they didn't even bother to take

**Dave Jones:** the button out of the front panel, because that would be a user installable option, just, you know, opening this thing up, plugging the board in. Yeah, you'd void your calibration if there was a cal sticker on it, etc. But, still,

**Dave Jones:** you know, it's not something that has to be done at at the factory, that's for sure. Now, if you are working on these, it should be pretty safe, you know, all the transformers potted, everything else, all the mains wiring's nice and

**Dave Jones:** neat and tidy, but the range switch on the back of the the rear side of the board there is exposed. So, just be careful that you don't, you know, accidentally just go, "Ah, yeah, I'll just move it and grab

**Dave Jones:** the the thing like that." Just be careful, but apart from that, should be pretty safe to work on. I love how that poor power resistor there has been almost bodged in, although it does show the silk screen does imply that it sort

**Dave Jones:** of supposed to be mounted vertically, but neat. And more bad news, it works. Oh, the EVBlog repair curse is just hopeless. I buy a, you know, a faulty bit of gear, and there was nothing wrong with that ohms range. What it was, it it

**Dave Jones:** was most likely just the input input selection of what the front rear selection switch here probably just had a dicky contact. It just needed to be cycled a couple of times, and bingo, like what 1.4, that's the leads in the

**Dave Jones:** box and everything else. That's what my other 7 1/2 digit meter measures with this box on that range. So, that is it it's fine. Everything's practically bang on with this meter. Like, it's Ah, yeah, I need to probably a bit more exhaustive

**Dave Jones:** calibration checking, which is, you know, can be really tedious, but it spot check on each range so far is well within spec. So, yeah, I like unbelievable. Unbelievable. Anyway, very useful 20 ohm range that for, you know, 1 milliohm resolution, very nice for

**Dave Jones:** tracking down shorts and stuff like that. Very handy. As is the 20 mV mode as well. That's that's pretty jazzy, 1 microvolt resolution. And given that this is a .003% class basic instrument, I like if you can pick one of these up for a

**Dave Jones:** you know 100 bucks, definitely do yourself a favor and get one. Awesome. So it's that switch down there. That's the culprit there and they're going to be like self effectively self-wiping self-cleaning contacts in there. So unless it proves to be an intermittent

**Dave Jones:** issue, it will require more use and more playing around with them to determine that, but it seems rock solid now. So I think it just had a bit of crud in there and just needed to be cycled once and

**Dave Jones:** bingo. So I wouldn't be going spraying contact cleaner in there willy-nilly. You know, there's people who say, "Oh yeah, the first thing I do is contact cleaner right throughout the switch." And yeah, you could just do it on the

**Dave Jones:** squirt on the top and it'd get down the individual pins down in there. So if you got your favorite contact cleaner, then by all means go for it, but I I don't think I'd bother on this one cuz it

**Dave Jones:** hasn't caused me an issue apart from that one time. You know, it's probably been sitting in storage for 15 years. And by the way, if you're worried about, you know, the annoying part about having to take off the cover to replace

**Dave Jones:** the fuse down there, don't really worry about it because it's actually just a backup fuse. The primary one is on the front. Non-HRC, of course, but that puppy's going to you know just in general use is going to blow first. You

**Dave Jones:** typically wouldn't be using these on high power and main stuff. They're like more for bench measurement use and stuff like that. So that's all fine and dandy. You shouldn't have to open the case, especially if you've got one with a

**Dave Jones:** recent cal sticker, then yeah, you can just replace the fuse on the front. No worries. And here's an old friend I haven't dragged down in a while, the Fluke 5458 resistance calibrator. I've been meaning to do a calibration of this

**Dave Jones:** a calibration of the calibrator using my we come resistance standard which I've got which is actually better than this and you can use the one single 10k transfer standard to actually calibrate all the ranges on this there's a sneaky procedure that

**Dave Jones:** allows you to do that I'll be meaning to do a video on that for a long time so I might get around to it one day anyway this allows us this is a reference resistor standard I've done a teardown

**Dave Jones:** of this I'll link it in down at the end it's beautiful inside check out that video trust me it's fantastic it's almost pornographic and this allows me to generate a low value resistances I'm on the 10k standard at the moment but I haven't

**Dave Jones:** verified the calibration of this right down so it claims to be 10.00012 anyway more than good enough for this there we go we're in a last couple of last least significant digits there of course if we switch over to the two wire

**Dave Jones:** mode you see 10.3 cuz it includes all the lead resistance and all contacts and every you know the contacts inside the switching in there and everything else but on four wire mode of course there you go it's basically bang on and we can

**Dave Jones:** actually use the one k the one ohm standard down here you got to say yeah that's 9996 so it's a once again couple of least significant digits out that's got to be well within spec so no worries whatsoever and yeah we could

**Dave Jones:** do this until the cows come home I know everyone wants to see every range don't they yes all right all right I haven't tried this oh look at that almost bang on oh oh and you know it's all these are going to

**Dave Jones:** be well within spec well within spec so this meter is a winner winner. Yep. That's good enough. Winner winner chicken dinner. Oh, look at that. And 100 mega, I don't think it does 100 meg. No, I think it

**Dave Jones:** only goes up to 20. I can't remember how many counts this is. Uh 20 Uh 200,000 count? Something like that? Anyway, there you go. Bang on. So, once again, sorry. I was hoping to bring you a repair video. I buy these

**Dave Jones:** repair things occasionally. Um and you know, hoping, crossing my fingers, that they'll be an interesting repair, not just a simple blown fuse, or not beyond economical repair, as quite a few of my repairs have turned out to be. So, yeah,

**Dave Jones:** I'm not even going to title this a repair video, cuz it's not. It's just a look at the Fluke 8842A multimeter with a pretty like almost a transfer class reference standard in there, that FLU uh one uh reference

**Dave Jones:** standard. If you can pick like for like for 100 bucks, you can get these that are working. You wouldn't get one that's, you know, recently calibrated for that. If you can, um then an absolute bargain. But yeah, by all

**Dave Jones:** means, uh put a search term on eBay. I know that if I mention something's good and available on eBay, they, you know, double in price instantly. So, sorry, you know. But these things have gone for as little as like 100 bucks. But yeah,

**Dave Jones:** uh it's like fantastic meter. If you can still pick it up with a decent display, cuz these uh vacuum fluorescents do fade over time. I think someone might have even done like a replacement display project for it or something like that.

**Dave Jones:** But yeah, really nice old school meter, the 8842A. If you can pick one up, do yourself a favor. Anyway, if you like that video, please give it a big thumbs up. As always, discuss down below. Catch you next time.

**Dave Jones:** Mhm.
