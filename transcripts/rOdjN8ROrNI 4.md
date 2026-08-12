---
video_id: rOdjN8ROrNI
title: EEVblog #898 - LCD Contrast Experiments
url: https://www.youtube.com/watch?v=rOdjN8ROrNI
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 27, "3": 42, "4": 57, "5": 75, "6": 87, "7": 104, "8": 114, "9": 123, "10": 136, "11": 159, "12": 172, "13": 186, "14": 204, "15": 216, "16": 227, "17": 240, "18": 254, "19": 263, "20": 272, "21": 285, "22": 295, "23": 309, "24": 325, "25": 338, "26": 349, "27": 358, "28": 374, "29": 384, "30": 395, "31": 409, "32": 419, "33": 430, "34": 442, "35": 454, "36": 465, "37": 479, "38": 496, "39": 516, "40": 539, "41": 564, "42": 574, "43": 586, "44": 601, "45": 619, "46": 630, "47": 648, "48": 657, "49": 668, "50": 679, "51": 690, "52": 703, "53": 719, "54": 727, "55": 738, "56": 754, "57": 770, "58": 783, "59": 795, "60": 808, "61": 827, "62": 838, "63": 855}
---

**Dave Jones:** Hi, just going to do a quick video taking a look at an issue that some people have had with the EVBlog BM235 multimeter and that is the viewing angle of the LCD.

**Dave Jones:** So, I've got three other meters here just you know randomly chosen and you might notice that the EVBlog meter is just fine. There's nothing wrong with it. In fact, it well, don't know if this will show up on camera, but it's probably the best of the bunch at this particular angle.

**Dave Jones:** The digits are nice and fat. Look at that and they it seems to have pretty good display contrast. And if I take it directly overhead like this and you can see it's still pretty darn good.

**Dave Jones:** In fact, you could say it's probably the best out of those, right? So, what's the problem? Well, the problem has to do with the angle of the light and I actually just did that previous shot with not all of my studio lights turned on here.

**Dave Jones:** So, I'll just repeat it with the lights turned on, all of them and you can see it's exactly the same. Excellent result for the BM235. So, these are all of my studio lights here and you'll notice that I actually have them over the center walkway like this.

**Dave Jones:** I've got my bench here that I do most of my you know tear downs and other main shots on and then I've got the mailbag bench over here that yes, the lab's in a state of flux at the moment so to speak.

**Dave Jones:** So, these lights are angled down like that. There are no lights up above here. There wasn't existing one, but they're not turned on. So, there's no light source coming from behind or on top.

**Dave Jones:** Let's call that the from the top of the LCD. They come in from the bottom of the LCD. If the angle of the light comes in like that, then the BM235 is an absolute winner.

**Dave Jones:** But let's look at what happens if I have the lights coming down at an angle like this onto the meter. So, they're coming from the top instead of the bottom.

**Dave Jones:** Glare, so that's really quite annoying. But, as you can see, it's still doing a reasonable job, reasonable job, reasonable job until you get like on top of it and you might start to see that it's starting to fade out.

**Dave Jones:** Coming down, the light's probably directly onto the LCD like that. And then, if I stand it up so they're straight, uh vertically like that, so the light's coming down from the angle from the top, you can see the BM235 starts to fade out a bit, but they're probably equally as bad at you know, a really bad angle like that.

**Dave Jones:** And if you compare it with the BM257, which is an older model, um the 235 hasn't replaced it, but it is a uh much newer model, then you can see that the new 235 actually does, you know, fade out a bit more.

**Dave Jones:** Now, of course, LCDs displays like these have uh a polarizing filter on the front of them and we'll actually see significant differences here. So, I've got a polarizing filter on the front of my camera here and you can already start to see that the EEVblog is doing something funny.

**Dave Jones:** The other two you look reasonably fine. If I start to turn the polarizing filter, you'll notice that the other two like completely vanish. You can't they display is black, but you can still see the EEVblog LCD, but it sort of changes that might have a function.

**Dave Jones:** Looks to be some function of the curved display at play there. That's rather interesting. It doesn't work exactly the same as the other two. But, this is certainly not just a Brymen thing.

**Dave Jones:** I've got uh two Keysights here. Well, one of them's branded Agilent and you'll notice that the new uh U1282A Keysight here does has a very similar result to the Brymen's.

**Dave Jones:** But, it's just interesting that they must be different polarizing filters between those. You know, you put the Uni-T back there and the Fluke 17B and it just goes whammo black like that.

**Dave Jones:** It is significantly different result. So, they obviously some type of different polarizing filter in them. Just thought I'd show that. It's interesting. So, let's have a look at the LCD module here.

**Dave Jones:** It just pops out after you get the board out. We have a look at the parts inside here. There's just a back in plate holder. There's a diffuser for the LED backlight.

**Dave Jones:** You can see that there's three LEDs in there and that just goes into the side of here. It's just using it as a light pipe basically to get the even backlight on the thing.

**Dave Jones:** And then we have the LCD itself. That's the flexible zebra strip there. It's got just multiple conductors in there, carbon carbon conductors that transfer the contacts over to it.

**Dave Jones:** It's just a rubber strip. It just peels off. And as you can see, there is no other layer in there at all. There's no you know, polarized layer or anything like that.

**Dave Jones:** It's all built into the glass. So, it's not like we can sort of you know, take something out or anything like that. Now, some people are saying that the curved nature of this uh display causes an issue and it does.

**Dave Jones:** But hey, you know, the Fluke 17B for example has a similar sort of reflection issue with the curved display like that. So, yeah, it is a problem, but that's not the cause of our contrast issue.

**Dave Jones:** There are two things that are going to cause a contrast issue in here. One is the actual physical manufacture and design and filtering on the LCD itself and the other is the contrast bias voltage that you actually apply to the LCD.

**Dave Jones:** And just in case you're wondering, there are different types of LCDs. There are reflective types that don't have a backlight and they will have a completely mirrored silver back on them.

**Dave Jones:** This is not one. This one's what's called a transflective one, and or transreflective one, and because it's got to have the backlight. The backlight has to get through like that.

**Dave Jones:** It's got to be able to shine through. So, it's part reflective and part transparent. So, there's obviously nothing we can do physically to the LCD like replace the filter or, you know, change it or remove it or anything like that.

**Dave Jones:** So, we now have to go look at the bias voltage to the LCD itself. So, let's go to Davecad here for a second because it's important to understand the difference between viewing angle and bias angle.

**Dave Jones:** They're two different things, and let me try and explain this. We've got our LCD here, okay? Then we've got a perpendicular axis right smack in the middle like this.

**Dave Jones:** Now, when they design an LCD, it's going to have a view a certain viewing angle like that, okay? So, that in there will be the viewing angle. It might be, I don't know, 90° or whatever it is.

**Dave Jones:** And that is the viewing angle where you can view it anywhere within side that plane, and it's going to be acceptable. It's not just going to suddenly vanish when you get outside.

**Dave Jones:** You got to pick an acceptability point. Now, that is viewing angle, and that is designed into the LCD material itself in terms of what liquid crystal materials that they actually use.

**Dave Jones:** I just realized I still have my polarizing filter on there. There it is. That's better. And what type of liquid crystal they use in there and the chemicals and everything else.

**Dave Jones:** It's a complex LCD manufacturing technology. So, that's viewing angle, and but that will not change when you adjust the bias contrast voltage. And you might be familiar with this.

**Dave Jones:** A product might have a, you know, a knob on it, for example, or it might have a software control that can that changes the contrast of your LCD. You're no doubt familiar with this, and it changes the bias voltage to the LCD.

**Dave Jones:** Now, it's important to understand that bias voltage does not change this viewing angle here. All it changes is the bias angle. So, the LCD will always have this fixed viewing angle like this.

**Dave Jones:** What the bias angle does is it actually rotates the viewing angle like this, depending on how you want it. So, you can adjust that bias voltage, and that's effectively what it's doing is changing that fixed viewing angle.

**Dave Jones:** So, if you want your product to work from the low side like this, the bottom side of the LCD, you want better, you know, you got the you meter laying flat on the bench like this, and you want to be able to see it at an angle, then you want to adjust your bias voltage so that you get and you know, so that you get the best

**Dave Jones:** viewing down at the bottom angle. So, that's all that that bias voltage does. And of course, the EV blog meter is no different. It has Well, it does not have an adjustment for the bias bias voltage, but it has a resistor in there which fixes the bias voltage at a particular point that Brymen determined was acceptable, and I don't think it necessarily is.

**Dave Jones:** I don't think they've optimized it enough. And sometimes the bias angle is specified in degrees, and what that is is if you take the center line, the center mark of the viewing angle here, then the bias angle is the angle between the perpendicular plane of the LCD like that up to the center of the the middle point of the viewing angle like that.

**Dave Jones:** So, that'll be the bias angle in degrees. And the backlight actually tends to have a worsening effect on that display angle, too. I mean, it that's It's yeah, pretty bad.

**Dave Jones:** So, there you go. So, Brymen have investigated this and they've uh said that the bias resistor is actually uh 67, which is that one right there. Little 0603 job.

**Dave Jones:** Luckily, it is accessible on the uh top side here, so you don't have to take the entire board out if you want to uh change it. But, anyway, that one right there, R67, currently 12.7k.

**Dave Jones:** Um but, they said they have selected values of 7. 17.8k and 21.5k before, but they settled on 12.7k. So, I'm going to change that. So, what I've done is soldered two wires onto there and we can feed that out the case because the battery terminals go uh spring terminals onto there.

**Dave Jones:** So, I have to put the back case on to power it up. So, we get some wires out, go to our decade resistance box. No worries. So, let's switch this back on and I've got it not connected to anything, just flapping around in the breeze.

**Dave Jones:** And tada, look at that. Oh, super contrast. Look at how black as the ace of spades that is. But, we can see the ghosting on here and ghosting is where it uh basically turns on or partially turns on the other segments, just appear to be on like that.

**Dave Jones:** So, that is yeah, that's not great. Obviously, even when you bring it up like that, you can still get ghosting down there. So, our contrast is far too high.

**Dave Jones:** Okay, so let's just start from the minimum angle here coming down from the bottom of the LCD and the lights from the bottom as well. That's where we're seeing the ghosting.

**Dave Jones:** Typically, when you're setting contrast like this, you want to set it for your uh best possible viewing angle and then uh just get rid of the ghosting. So, I've got 100k at the moment.

**Dave Jones:** Um so, let's actually drop that down to uh 10k and see what we get. Bingo, it's gone. So, that's what we're getting. That's would have been the level that we're getting before, the 12k uh level.

**Dave Jones:** So, let's actually go up to 20K. You can see that there is very significant differences. I've got fixed exposure on the camera, so that's hoping on that's turning up.

**Dave Jones:** I can really see a big difference in there. So, their recommended value is 21.5K or whatever. 17 K, they well, I could do 17, but yeah, I reckon like 20K does the business.

**Dave Jones:** No worries. And then if we go back to our original setup where the light is coming from the top and we're also looking slightly down from the top as well.

**Dave Jones:** So, you can see the BM257 and the the new one, much better. Beauty. Yeah, it makes a hell of a difference. Look, this is the original one and this is our 20K one modified.

**Dave Jones:** If we go to like 30K, so you can switch in here and really see it. 10K. That's 20, 10, 20. But ultimately, the bias angle can change with temperature on these things.

**Dave Jones:** So, to engineer this solution properly, you would cycle this over temperature and determine, you know, over the typical operating range determine the best value and things like that. But yeah, I think they've just chosen a too lower value here.

**Dave Jones:** I think there should be 20K in there instead of the 12.5 that they've put in this thing. And quite a few people have mentioned this, not everyone, cuz it depends on your light condition and everything like that.

**Dave Jones:** So, I guess they didn't I don't know what their temperature is over there. I don't know what their light conditions were when they you know, obviously they had people sit around deciding, oh, what, you know, which contrast looks better.

**Dave Jones:** It's a like a subjective thing. And if you don't take into account angles of the not only the viewing angle of the person looking at it, but also the angle of the light coming to it, then it can make a big difference.

**Dave Jones:** Anyway, I hope you found that interesting. I'm not going to thermally cycle this thing or anything like that now, but yeah, it looks like I'm going to feed this back to Brymen and I probably think they should at least change it to 20k cuz I can't see by doing that I can't see any significant ghosting, but hey, you might get ghosting at a different temperature, who knows.

**Dave Jones:** Anyway, if you enjoyed that, please give it a big thumbs up. As always, links to the forum and to discuss it and YouTube comments and blog website and all that sort of jazz.

**Dave Jones:** Catch you next time. Hi, it's engineering terminology time. We're going to talk about orders of magnitude. And you hear me say it all the time, not just me, but it's a very common term in electronics and other engineering and science for that matter.

**Dave Jones:** Order of magnitude, what exactly does it mean? You'll hear me use it in terms of oh, I was out by an order of magnitude or that was an order of magnitude bigger than I thought or it's dropped, something's dropped by an order of magnitude.
