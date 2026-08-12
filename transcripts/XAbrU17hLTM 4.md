---
video_id: XAbrU17hLTM
title: EEVblog #1183 - RIFA Madness (Schaffner Repair)
url: https://www.youtube.com/watch?v=XAbrU17hLTM
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 20, "3": 35, "4": 49, "5": 72, "6": 91, "7": 108, "8": 126, "9": 141, "10": 170, "11": 184, "12": 201, "13": 218, "14": 226, "15": 240, "16": 250, "17": 270, "18": 283, "19": 291, "20": 313, "21": 332, "22": 344, "23": 363, "24": 379, "25": 389, "26": 407, "27": 420, "28": 439, "29": 454, "30": 481, "31": 500, "32": 516, "33": 531, "34": 547, "35": 557, "36": 576, "37": 591, "38": 609, "39": 626, "40": 639, "41": 646, "42": 660, "43": 677, "44": 690, "45": 701, "46": 712, "47": 726, "48": 735, "49": 745, "50": 758, "51": 780, "52": 793, "53": 808, "54": 821, "55": 839, "56": 848, "57": 860, "58": 866, "59": 879, "60": 893, "61": 904, "62": 916, "63": 935, "64": 946, "65": 960, "66": 977, "67": 985, "68": 997, "69": 1013, "70": 1027, "71": 1035, "72": 1047, "73": 1059, "74": 1068, "75": 1079, "76": 1088, "77": 1096, "78": 1116}
---

**Dave Jones:** Hi, in a previous video we took a look at the teardown of this Schaffner NSG 200 and NSG 222A interference mains interference simulator. It's a very cool and interesting bit of kit.

**Dave Jones:** So, I'll link it in down below if you haven't seen it. Anyway, we thought that there was a failure in the transformer over here, but well, let's take a closer look.

**Dave Jones:** Now, of course, when I plug this thing in, it took some time, but it eventually, while I was trying to use it, released the magic smoke. And I thought it was coming around this back area here cuz the the top part of it just has all grills on it like this.

**Dave Jones:** So, the smoke was sort of coming out of this back region. So, when I opened it up and I saw this down here, I thought, "Aha, that looks like the culprit." This huge common mode choke on here.

**Dave Jones:** And you can see it does actually look as if like something like has burnt and then melted and dripped down and something like that. But, as I remarked in that video, because this is just a common mode choke, I I found it really hard to think of the mechanism that would actually cause it to do that because it's not like, you know, a transformer or anything.

**Dave Jones:** If one turn just shorts to another, you know, it's not really a big deal. And anyway, so I didn't really investigate it any further. So, it seemed like that was the culprit, but as it turns out, one of my viewers actually worked or is still working at a uh transformer manufacturing company.

**Dave Jones:** He said, "No, this is actually quite common. It just looks like the residue from the poly put the kettle on coating that they actually apply to this thing and it's it's no big deal." And like that is not a burn mark at all.

**Dave Jones:** And upon closer inspection, I'm pretty darn sure he's right cuz look, it looks like it's sort of like dripped out of there like that. So, yeah. I don't reckon I I now am pretty confident also that this is not the burn mark.

**Dave Jones:** So, let's go have a look elsewhere. Now, as many people in the comments spotted, these are Reifa capacitors. Reifa's a brand of these safety capacitors, filter capacitors that go down to mains earth, X class and Y class caps.

**Dave Jones:** And um these are actually notorious for failing after a long time. Because what happens is the plastic casing on these things actually cracks and moisture gets into them. And then if you've got these things like sitting around in storage for 10 or 20 years, and then you try and power them on, bang, the magic smoke escapes and pretty pungent odor comes out of these things.

**Dave Jones:** But usually they're quite, you know, all the ones I've seen are usually quite violent. And here's some photos just pulled off Google images of various Reifa brand. It can happen to other ones, but these Reifa ones are common that use these plastic enclosures.

**Dave Jones:** They're practically infamous for doing this after, you know, 20, 30 years, something like that. And I originally looked at these and went, "Oh, no, they look okay at first glance." And we had what looked like a burn mark on the transformer where I thought the smoke was coming out of.

**Dave Jones:** But upon closer inspection, these do look a bit dodgy. So, I didn't really give those more than a casual glance before, but if we look closer, upon second inspection, I think we can see something down in here.

**Dave Jones:** I'm going to It's hard. I'll try and get the lens down cuz it's hard to get this board out, by the way. It's It's like, yeah, it's not easy.

**Dave Jones:** But if you have a look down in there, now it seems pretty obvious. I didn't notice this, but you'll notice that big crack in there like that. I I didn't see that before.

**Dave Jones:** And if you can see it, big crack down there as well. And I can Yeah, I can feel that. There we are There we go. Get the screwdriver in there.

**Dave Jones:** So, yeah, I pays to look a little bit closer and not get caught up in uh thinking that you've uh found the culprit, especially when I I couldn't really explain why that common mode choke would have uh like caught on fire and smoked it really.

**Dave Jones:** There was just no mechanism for it. So, yep, that now seems pretty obvious. So, what I'm going to do is get all those caps out of there. And uh the good thing about these is that they're not actually necessary for the operation of the unit.

**Dave Jones:** So, I can simply uh remove them and uh power the thing back up and at least get it working. I mean, I you know, I should actually replace them, and I will, of course.

**Dave Jones:** Um and you should, by the way, if you find any old gear, vintage computers, or any other vintage uh test gear, or anything else that uses these uh Reefa brand caps, or similar-looking ones um for mains input uh filtering either directly across the mains or uh down from uh active and neutral down to earth, then replace them.

**Dave Jones:** It's a real good idea cuz they might eventually go bangsky. Um by the way, if you getting in there and uh desoldering um like old uh gear like this, there can be like lots of real crusty old flux residue on there, and it really goes up in smoke, and it's just It's nasty stuff.

**Dave Jones:** Um I've actually um been at a job where we actually set off somebody in the lab that liked uh repairing old gear, and they brought some old gear in uh once and started working on it.

**Dave Jones:** Nope. Fire alarm went off, building evacuated, and uh yeah, lots of red faces all around. Oops. Yeah, look at that. Lots of it. Woo. I think what they've actually done with this thing is the board actually gets assembled onto the transformer.

**Dave Jones:** The transformer dropped in, all the wires are plugged in, and then they screw it down like this. So, I've unscrewed the transformer. It kind of sort of comes out, but there's a lots of wires just like some of them are permanently connected and stuff like that.

**Dave Jones:** So, if I get the bottom plate on, I can kind of sort of get in there and maybe get the uh desolder the board off, but jeez, it's it's really quite annoying.

**Dave Jones:** Well, yep, that's obvious, isn't it? Look at that. And if that was just sitting on the board, like that would have been just so obvious that this thing was blowing, but because it was like, you know, tucked away in there, and it was harder to see.

**Dave Jones:** You can see it's like bulged out and expanded. All of the cases just completely cracked everywhere. Like, big two big splits on the bottom, and yep, the magic smoke has escaped.

**Dave Jones:** And all the other ones look real dodgy brothers, too. Look, you can see the cracks in there. Look at them all. Wow. That's just yep. Look, straight across. But that's, you know, most of these other ones were impossible to see inside there.

**Dave Jones:** And once again, you might be able to probably see maybe the bulge and the cracks. These things are just absolutely hopeless. There's practically a 100% failure rate. In fact, there is a 100% failure rate on these.

**Dave Jones:** Wow. And lucky last. Here you go. Yep, all completely dodgy. And these smaller ones are the Y class caps, and the Y class caps are go from active and or neutral down to earth, whereas this one is an X cla- yep, X class and half an X class, and half cuz half the magic smoke has escaped, and the X class goes directly across the 240 V or 110 V mains.

**Dave Jones:** So, there you go. Yep, classic reefer capacitor failure. Yep, and it would have been blatantly obvious if they weren't sort of like hidden away in there, and we didn't have the other red herring that we chased with the transformer.

**Dave Jones:** So, there you go, easy peasy. So, according to the schematic, this one was a five microfarad job, and the only X2 I have to hand brand new is this 0.1 micro one, and look, it doesn't really matter.

**Dave Jones:** Five microfarads actually is a for the 60 60 Hz model. It's actually lower value for the 400 Hz capable thing, and we're only talking about a you know, basically filtering here.

**Dave Jones:** So, as I said, this thing will no doubt work without any of these caps installed. They're just suppression filtering caps, basically. So, I don't know, I could try this, or maybe I could like steal some from an old board perhaps, something like this.

**Dave Jones:** Here's a bunch of a What? There they'd be yep, they're X2 class caps. So, 470, and there you go, so slightly larger. So, maybe I can steal some for them.

**Dave Jones:** And these look like Y class caps in here. You can tell because they're actually going to ground here. You can see that they're across there like that. So, they're actually going in there to ground, but the part number fortunately is a bit oddball.

**Dave Jones:** And these ones are actually a X1 and Y1 class cap. So, they're I quite nice. Unfortunately, very low in value. 101 there would be 100 or 100 puff. But hey, check out that one.

**Dave Jones:** That's a 820 nanofarad Y class cap. Nice. And of course, once again, because it's Y class, you see it going over to ground here. So, as you can see, it's handy to have like a scrap board like this in your junk bin cuz you can, you know, these are still great quality caps.

**Dave Jones:** So, you can, you know, suck these out and use them if you got like an old bit of gear that's, you know, all the magic smoke, all the snot's escaped from these old Reefa type or other brand, you know, X or Y class caps, then yeah, you can, you know, these are perfectly good to use.

**Dave Jones:** So, as I said, these are X class capacitors. In this case, X2, which is the second highest rating one. X1 is actually the highest, and you can get lower than that, but X2 is by far the most common.

**Dave Jones:** And Y2 ones, which we've got This one just says Y. So, I'm not, you know, it's a really old one, so I'm not sure what the deal is there.

**Dave Jones:** But anyway, but they are designed for different purposes. As I said, the X class goes across the mains, and they're designed so that they don't fail short. I e., they don't catch on fire because they're directly across the mains.

**Dave Jones:** It's got low impedance, lots of energy behind it. So, they're designed not to explode. Um that was the plan anyway. But yeah. These older ones do, unfortunately, degrade over time, but they're supposed to not do that.

**Dave Jones:** Whereas your Y class caps are designed to go from active or neutral down to ground, and they're designed not to have any leakage at all down to ground. So, they're designed for for purposes.

**Dave Jones:** Now, you can actually use a Y class cap in the X configuration, but you can't use an X class cap, or you shouldn't use an X class cap in a Y class configuration.

**Dave Jones:** Um it's just a safety thing. You can see some ooze down there on the board. That's just spewed out the bottom of that cap. We'll just uh clean that off before we uh put a replacement in.

**Dave Jones:** Now, one of the problems with soldering a board in situ like this when it's vertical like that is the solder actually with large like ground planes with no solder mask, the solder actually falls down under its own weight under gravity.

**Dave Jones:** So, you really have to flip this board up horizontal in order to solder it properly. I've just got a uh regular like a tinned copper uh PCB like this one.

**Dave Jones:** Right, so I'm actually fairly confident to turn this back on now cuz I'm pretty darn sure that there's nothing wrong with that uh transformer. We've taken out all the X and Y class caps.

**Dave Jones:** I mean, we we had five for five fires there. That's just uh insane. I don't have any Y class uh caps in there, which uh power these two neons as well as uh doing some filtering down to earth.

**Dave Jones:** Now, uh a few people in the uh comments, and quite a few actually, uh mentioned that possibly this thing could have died because I was like uh uh pulsing this thing without a load, and there's absolutely no way uh that I can imagine where that would cause a problem because this big ass filter That's what this big ass filter and this big ass choke do here.

**Dave Jones:** Um that's the whole point of having these enormous things, so that all the output uh pulse um all the output pulses on here don't affect the input. And not having a load on there shouldn't be an issue whatsoever.

**Dave Jones:** So, um let's just power it on and see what we get. Yep. We're back up and running. Sweet as. There you go. And I've I've of course uh seated that uh chip back in there.

**Dave Jones:** So, that's maybe why um I got like before it uh the magic smoke escaped, I couldn't actually uh get any pulses on the uh scope. So, I'll hook up the scope again, give it a whirl.

**Dave Jones:** K, switch the output on. Bingo, there's our sine wave. Beautiful. Let's see if we can get a pulse on it. And of course, as I've mentioned, when you're doing uh tests like this, high voltage stuff, you need a proper high voltage probe available on the EV blog store.

**Dave Jones:** Plug my merch. Um a lot of people don't know that I sell this. Um it's a very nice high voltage probe. Uh divide by 100. Beautiful. And it plugs straight in with the banana jacks.

**Dave Jones:** Okay, so I'm going to set it to a 100 nanosecond uh pulse here, just symmetrical whatever. I'm going to set it to uh 500 V pulse, and we're going to single pulse this thing.

**Dave Jones:** And we'll set the scope up for a 100 to 1 probe, because that's what our um the high voltage probe is, and we're at 200 V per per division there.

**Dave Jones:** So, let's run that. You can see that's actually live. So, what we want to do is set our trigger point just above that. There you go. So, it's now free running.

**Dave Jones:** We'll put it on normal mode. Then we'll single shot capture that. Now, if we trigger it, hopefully we'll capture something. That's the plan. Whoa, yep, got one. Something in there.

**Dave Jones:** Let's say it doesn't look like there's anything in there, but uh-huh, because it's only a 100 nanosecond pulse, and we're currently at 5 ms per division. Bingo, there it is.

**Dave Jones:** Look at that. And that's at uh 20 nanoseconds per division, 40. So, you know, it's roughly a 100 nanosecond pulse, something like that. Let's actually set it for a 10 nanoseconds, and see if it's faster.

**Dave Jones:** So, we'll keep the time base like that. And single shot capture that again. 10 nanoseconds. And single. Bingo. Oh. It's the same. Uh Bueller? Bueller? Let's try that again.

**Dave Jones:** It's the same again. 10 or 100 nanoseconds doesn't seem to make much of a difference. Oh. Anyway, it's working. And if we change the polarity on there, sorry about the glare of the screen.

**Dave Jones:** Um yeah, I do have like an anti-glare uh filter. I um just haven't put it on yet. It's great scope, but yeah, the screen glare is terrible. Um I've I've changed polarity and uh let's zoom in.

**Dave Jones:** And bingo. There's our pulse. Nice. And I'll double the amplitude. I'll single shot it again. And Oh. There we go. It's a bit problematic. Um it's it's just picking a random location on the uh waveform cuz I'm just free uh pressing it here.

**Dave Jones:** So, I've actually set it to 1 kV pulse this time, and let's sing There we go. That's our 1 kV pulse. Pulse. It's not It's not that huge, is it?

**Dave Jones:** So, we're actually working a treat there. This is a winner winner chicken dinner. So, there you have it. As predicted um in the previous video, this thing actually works.

**Dave Jones:** I didn't think there'd be anything hugely uh wrong with it. I just think it was just surplus to requirements or whatever. Maybe, you know, it doesn't support the new testing standard they're testing to or whatever, but it's probably been sitting around for a long time, which is why these damn uh reefer caps have failed.

**Dave Jones:** And these are, you know, like notorious for failing like this. Um they just like over long term. Uh the modern ones are a lot better, but these um older ones just absolutely horrible.

**Dave Jones:** They're they're infamous for doing that. So, if you've got any old gear or anything with these, just replace them as a matter of course, even if they haven't failed.

**Dave Jones:** Um, especially if the thing has been like, uh, I believe it's different if you keep them like, uh, you know, powered up 24/7 for like, you know, 15, 20 years or or or whatever.

**Dave Jones:** I believe they're they actually do, uh, have a longer life. But, uh, yeah, if you put them in storage and then, um, just try and power them up and they've got moisture in there or whatever, it's like poof.

**Dave Jones:** All the magic smoke's going to escape. In this case, we were five for five. I mean, all of those have failed. They've all got cracks in the case or whatnot.

**Dave Jones:** Um, they they just look horrible. Look at them. They're just, uh, awful. And that's how bad these things are. Five for five. Unbelievable. But, it looks like we've got it working.

**Dave Jones:** I'll eventually get some, uh, Y-class caps to put it uh, back in there and, uh, you know, restore it to its original thing. But, it looks like I have um, uh, roughly working.

**Dave Jones:** You know, you could try out all the functionality and everything. But, uh, that could, uh, take some time. But, it seems to be generating the pulses that we want.

**Dave Jones:** So, that's a very nice mains interference simulator for the lab. Awesome. Test out products now. Just pulse it in there. See if they fail. Terrific stuff. Anyway, if you like the video, please give it a big thumbs up cuz that always helps a lot and you can discuss it down below in the comments or over on the EV blog forum.

**Dave Jones:** Catch you next time.
