---
video_id: 8itTKH5tj3s
title: EEVblog #1152 - 240V-120V = Magic Smoke!
url: https://www.youtube.com/watch?v=8itTKH5tj3s
source: youtube-asr
timestamps: {"0": 1, "1": 12, "2": 21, "3": 41, "4": 62, "5": 74, "6": 86, "7": 102, "8": 112, "9": 124, "10": 132, "11": 145, "12": 158, "13": 172, "14": 183, "15": 193, "16": 209, "17": 219, "18": 234, "19": 244, "20": 264, "21": 272, "22": 285, "23": 298, "24": 315, "25": 325, "26": 346, "27": 358, "28": 369, "29": 379, "30": 396, "31": 408, "32": 418, "33": 433, "34": 446, "35": 461, "36": 475, "37": 491, "38": 507, "39": 524, "40": 537, "41": 557, "42": 571, "43": 585, "44": 603, "45": 623, "46": 635, "47": 645, "48": 655, "49": 664, "50": 676, "51": 687, "52": 702, "53": 714, "54": 730, "55": 739, "56": 755, "57": 764, "58": 775, "59": 785, "60": 796, "61": 807, "62": 822, "63": 836, "64": 848, "65": 863, "66": 870, "67": 890, "68": 904, "69": 918, "70": 938, "71": 949, "72": 967, "73": 983, "74": 998, "75": 1011, "76": 1029, "77": 1045, "78": 1055, "79": 1063, "80": 1076, "81": 1092, "82": 1102, "83": 1115, "84": 1127}
---

**Dave Jones:** Hi, we have a problem. I needed an extra soldering iron the other day and of course the lab's not completely set up yet, so the soldering bench and soldering room's not completely set up.

**Dave Jones:** So, I reached into one of my boxes that has all my soldering gear in it from the old lab and I went, "Oh, yeah, this Weller will do. I'll just plug that in.

**Dave Jones:** Just need something quick." And it started flashing on the screen and I thought, "Oh, that's kind of weird. Like something's going on as there, you know, a contact thing with the iron probe or something." And in the couple of seconds it took me to process that, wah wah wah wah, smoke started billowing and I'm talking like this wide.

**Dave Jones:** It just started billowing right out the bottom of the this poor old Weller soldering station here. And then I quickly remembered, "Oops, it is a 120-V version. And of course we've got 240-V here in Australia.

**Dave Jones:** So, yeah. Um I wish this was smell-a-vision because if you could smell this, uh yeah, it's got that magic smoke smell. All the magic smoke escaped from this thing.

**Dave Jones:** So, I thought we'd take it apart and I might not be able to repair it, but yeah, oops. And I think almost every soldering iron on the market is like uses a transformer-based system.

**Dave Jones:** They are a fixed voltage. Like some of them might have a voltage tap that you could change or something like that, but none of them that I'm aware of anyway off hand, use a switch-mode converter to get like a universal input mains voltage.

**Dave Jones:** And that's probably because I would guess that they really, you know, we've got like a large power heater, like a 50-W or 100-W heater switching off and on rapidly and stuff like that.

**Dave Jones:** And switching a load like that, a 50-W load, isn't great for like a switch-mode power supply. So, it's probably just easier and better performance just to use a transformer.

**Dave Jones:** And of course, it gives the thing a bit of heft. So, there's nothing wrong with the Weller. It was a PEBCAK. It was me. So, let's crack this thing open and see what damage we've done.

**Dave Jones:** But by the amount of smoke that escaped from this thing, it's not pretty. And of course, the active ingredient inside all electronic components, including transformers and everything else, is the magic smoke.

**Dave Jones:** And once the magic smoke escapes, it doesn't work anymore. Ah, damn it. And of course, I've done a previous teardown video on this thing. So, let's have a look.

**Dave Jones:** Nothing obvious on the uh Whoa. What? There's nothing obvious at all. That's terribly disappointing, isn't it? No Oh god, that smell is uh That smell is horrible. Anyway, I can't see anything.

**Dave Jones:** Let's check. Let's get the board out and have a look on there. Because it did all waft out this front vent, this bottom vent here. And the smoke was like it must have like filled up all in here.

**Dave Jones:** And then um the pressure of it just like pushed it all out and it billowed in a big wide billow of smoke coming out. So, all right. Let's have a look.

**Dave Jones:** What? Wow. I'm not seeing anything. See any blow holes or anything like that. What's What's going on? Ah. This is incredibly disappointing. Where did the magic smoke escape from?

**Dave Jones:** There's only one electrolytic cap in here, which is a non-vented one. It doesn't have the like the little you know, marks on there. The vent marks, the score marks.

**Dave Jones:** So, that must be one of those solid uh electrolyte caps. Oh, yep. I'm just absolutely stunned that nothing is blown on here. So, I can only presume that it must have come out of the transformer.

**Dave Jones:** It was awful amount of smoke and it came out within like 2 3 seconds, it started billowing out of this thing and it was a ton of smoke. It was unbelievable.

**Dave Jones:** And of course, I just you know, reflex reaction pulled the mains cord at the back of the thing and and then I actually what I did is I actually once I made sure it wasn't physically alight, I actually shoved it in a box to stop the all smoke billowing out, but there's nothing wrong with that main board there.

**Dave Jones:** Like the power training here was blowing, you'd expect to see like a big blow hole in it or something like that, but yep, I can only presume that the smoke came out of the transformer.

**Dave Jones:** And sure enough, if I actually smell that board, there's like no sign of it whatsoever. So, yeah, I think that is just hunky-dory. Must have all come out of the transformer.

**Dave Jones:** And sure enough, if you smell the transformer, yeah, that's where the that's where the magic smoke escaped from. So, I can only presume that it like burnt the enamel off the wires.

**Dave Jones:** Once that amount of smoke escapes from something like a transformer, even if it even if I powered this up again and it worked, I wouldn't trust it because that smoke came it must have come from the you know, the the laminated wires on there.

**Dave Jones:** So, that just breaks down the insulation. Yeah, not a good thing. So, I would I would not trust that and reuse it even if it worked after a smoking overload like this.

**Dave Jones:** And you can see that this does have both fuse and poly switch protection, but unfortunately, this is only on the secondary side of the transformer here. You can see over here, this is a 120 V fixed 120 V transformer, so you can't like just choose another tap and convert these from 120 into 240.

**Dave Jones:** There's the mains input, goes straight through the switch, straight into the primary side of the transformer there. So, yeah, that's where it must have smoked, on the primary side.

**Dave Jones:** So, let's just measure some stuff here. The uh secondary side of the transformer, you'd expect it to be like, you know, an ohm, sub an ohm, something like that.

**Dave Jones:** Bugger all, 0.3 ohms. Yep, something like that. That's fine. Is our fuse intact? So, our fuse did blow, by the looks of it. Yep, that that protected that. No worries.

**Dave Jones:** And then a poly switch. Uh there Yeah, there we go. So, that's low, but that fuse has blown. So, it looks like that protected the uh secondary side of it, hence why we don't, you know, well, there's no visible signs of damage.

**Dave Jones:** Doesn't mean we don't You know, doesn't mean that this thing is not damaged. You know, you'd have to uh power it up with uh some AC here and uh do it that way, but um we've got another fuse on there.

**Dave Jones:** Let's measure that, baby. There we go. That fuse is intact. So, yep, that's fine. So, this uh design is quite good from a secondary side uh protection uh point of view.

**Dave Jones:** So, that board, but unfortunately, there's just nothing on the primary side. The primary side is not fused at all, and I assume that's legal, cuz well, wouldn't do otherwise.

**Dave Jones:** I assume it's legal in might vary in other countries, but there's no fusing at all. I don't think I actually mentioned that in my uh review at all of this thing and uh tear down previously, but now it's it's it's obvious.

**Dave Jones:** There is no primary side fusing, and they should at least have an integrated uh fuse with the holder, and that probably would have uh well, should have, if you size the fuse correctly, should have uh at at least, you know, stopped it.

**Dave Jones:** But, anyway, let's measure the primary side cuz I'm pretty sure that's where the magic's go smoke escaped from. And of course, primary side transformers, you'd expect like, you know, tens of ohms, hundreds of ohms, that kind of thing.

**Dave Jones:** But, uh What what what? 0.2 ohms. Um yeah, that's a lot. Um get your calculator out. I'll leave that for an experiment from home. But, like, 0.2 ohms calculate 240 or 110 volts across 0.2 ohms.

**Dave Jones:** How much power is that? Bueller? Bueller? So, obviously, what's happening inside there is there's going to be some enamel burnt off the insulation inside there. So, it might be time for a teardown of that.

**Dave Jones:** And for those who want to see, let's compare it with a rip-off Hakko FX-951. This is a 240-V version, but of course, the primary side transformer will be in the tens or hundreds of ohms category.

**Dave Jones:** And there we go, 64 ohms. By the way, these rip-off Hakko FX-951s are absolute garbage. I haven't opened it yet, but I used it on a live stream video assembling that Gigatron board, and it was just utter trash.

**Dave Jones:** So, we can get these caps off here. They're all They're sort of Oh, yeah. Uh-oh, hello. Hello. Oh, that poor primary side transformer. And you can tell it's the primary side, by the way.

**Dave Jones:** For those who don't know, the secondary side in a step-down transformer, which is most products, the secondary side is going to have thicker wire in there cuz it's like it's stepping down, so higher current.

**Dave Jones:** Whereas, the uh Oh, that's It's Oh, there we go. Oh, that's more spectacular than a and a component and a blow hole in a uh like output transistor, isn't it?

**Dave Jones:** Wow, look at all the Yeah, all the enamels burn off that. Anyway, uh thinner wire on the primary side. Wow, no wonder it shorted. Look at that. So, that's what happens when you apply like 240 V to a 110 V transformer.

**Dave Jones:** And this could have been prevented if they had a fuse cuz this thing could have like, you know, could have caught on fire. Imagine if I turned it on and then uh like walked away and then didn't realize and went to the bathroom or something and, you know, this thing could have like complete like that would have been 240 V just delivering pumping the power into this thing, but my uh

**Dave Jones:** mains fuse did actually um eventually blow. I'm not sure how uh long after it actually blew, but anyway, um you know, you could maybe fix it, but you'd have to rewind the whole damn thing.

**Dave Jones:** There's just like it's silly. Anyway, if you haven't seen a transformer construction before, this is what's called an E core uh transformer. It gets its name from the shape of the laminations.

**Dave Jones:** These are the laminations. You can see all the different and you know, count how many laminations are in there. Anyway, uh it gets its name from the shape of the lamination.

**Dave Jones:** In this case, you can't see it, but there's another part of this core this laminate. You can see it's broken there and there. It goes around like that like a C, but it's actually got a center one that goes through.

**Dave Jones:** So, it's actually shaped like an E, the letter E. So, it's like E and I it's called. Um and then you can see that they just weld the I part onto the E part there.

**Dave Jones:** So, that's how and this is just the center lamination goes through like that. And then they wind the primary and the secondary in separate uh plastic enclosures like this and they have the electrical separation.

**Dave Jones:** So, that's the electrical isolation between your primary and just secondary here. So, yeah, that's a typical for a mains transformer. I wonder if there's anything on the bottom. Let's get that out of there.

**Dave Jones:** Oh, yeah. Yeah. Just as crusty on the bottom as it is on the top. Oh, the top. This is the top. Yeah, sorry. All the poor enamel coated wire.

**Dave Jones:** So, that was the That's the smell in this thing. It's the burnt enamel. And wow, you can just Yeah. It could just turns into this brown. Really, I don't I don't know if I've actually seen that.

**Dave Jones:** Like burnt in to that extent before. I've seen like little, you know, blow holes in transformers and stuff like that. But, this one is like completely like consistently burnt.

**Dave Jones:** The secondary side is also is is of course completely intact. And of course, we would have got Initially, we would have got double the voltage out of But, you know, the fuse probably kicked in or maybe it No, it did actually cuz I said there was something on the LCD.

**Dave Jones:** Cuz it actually flashed something on the LCD. I can't remember what it was. It was just a couple of characters or So, it looked like the processor was actually working.

**Dave Jones:** And then, yeah. Panic set in and I pulled the mains plug. So, yeah. But, isn't that terrific? I love it. So, let that be a lesson to you. Don't plug 240 V into 110.

**Dave Jones:** And yes, I should have labeled this I know it's labeled on the bottom, but I should have put a huge label on the top of the unit. Stupid me, lazy me, didn't do that.

**Dave Jones:** But, of course, for these circumstances where I just needed an extra iron somewhere, you know, I'm going to pick up just any, you know, random iron that's sitting around.

**Dave Jones:** So, yeah, I I did know like I did know this. I was just too lazy to do it. And ah, she'll be right. I'll remember that it's 110. So, yeah, that was a PEBCAK.

**Dave Jones:** Don't do that. And I know what you're thinking, Dave, does the controller still work? All right, well, let's find out. Um as per the labeling on here, 120 V primary, 23 V secondary, uh 60 Hz.

**Dave Jones:** It should be fine, 50 or 60. I can generate that with my Appso pulse generator here. Uh 23 V secondary, 60 Hz. So, let's plug that in and see what's what.

**Dave Jones:** We're probably going to get some light drops on these leads and stuff like that, especially if you use the heater, but I got the heater unplugged. So, hey. Hello.

**Dave Jones:** There you go. LCD works. Let's plug the iron in. Yeah, it's happy with that. It's set for 270. We'll just leave it at that. That's fine. It's not going anywhere.

**Dave Jones:** Oh, it's dropped a Yeah, 15 up there. So, yeah, we're getting some loss in the leads. Didn't normally take Yeah, it's going up. Didn't normally take that long to start up anyway.

**Dave Jones:** That's looking good. That's looking good. She's heating up. Not going to touch it. I'm going to assume that the thermocouple in the tip is still good. And uh that it should You can see it's delivering power.

**Dave Jones:** That's what the little little lightning bolt icon on there is. And will it get to Will it get to 270? Should maybe start to be able to melt the Yeah.

**Dave Jones:** There you go. It's melting solder. Will it actually get to 270 and regulate? Yep. Yep. No problem. The little icon thing is flashing off and on. There you go.

**Dave Jones:** Works a treat. Winner, winner, chicken dinner. Good on you, Weller. it's obviously a like a a robust designed secondary. The fuse did its job on the transformer here, kicked in, but obviously like the power train and everything else was robust enough to survive double volts on the secondary.

**Dave Jones:** Nice. And well, I've got to ask like how did this actually happen? Because you're plugging 240 volts into a 110 volt transformer, double the voltage on the output of course.

**Dave Jones:** That means for a resistive like element loaded that we've got here, roughly like that's going to be four times the power. So, okay, it's going to be delivering four times the power, but surely like this thing started smoking literally like two or three seconds after I plugged it in.

**Dave Jones:** So, even if it like it cuz it would have probably started applying power to the heating element straight away. So, how it was able to just like completely melt the insulation like that after a couple of seconds at four times the power, I don't know.

**Dave Jones:** Is it a transformer design issue? Of course, it should be fused. I reckon that's a that's a bad mistake there is not having the primary side transformer fused especially when it could be quite common to you know, to sell these things in different regions at a different voltages.

**Dave Jones:** It's not like oh, you're going to suddenly plug a 240 volt iron into 600 volts mains or something like that, you know, that doesn't really exist. It's not going to happen, but accidentally plugging a 115 120 into a 240, that's certainly possible.

**Dave Jones:** So, certainly should be fuse worthy, but is there not enough enamel insulation on the primary side? Is it a poor design transformer? I don't know, but jeez, like wouldn't have expected that, really.

**Dave Jones:** Oopsie. If you like the video and my screw up, give it a thumbs up cuz that always helps a lot. And discuss down below if you got like photos or anything of stuff that like mains transformers that you've burned out or other products you burned out when you incorrectly hooked up the wrong mains voltage.

**Dave Jones:** That's a problem here in Australia. We get a lot of you know, if you import a lot of stuff, you'll get 110 V. Use test equipment on eBay, you've got to be very careful importing it here.

**Dave Jones:** And it's not a problem. You Yanks wouldn't have too much of you know, who else uses 110 V? But you guys wouldn't have too many problems because you import stuff.

**Dave Jones:** And if you're 240 V product, you hook it up to 110, meh. The magic smoke like this isn't going to escape. It's just going to like either not power up or have reduced performance or whatnot.

**Dave Jones:** So there's a lot of power behind a 240 V mains. In fact, there's 2400 W or even more before the main fuse will blow anyway. Like I think I got a 16 amp breaker here for my 240 V nominal well, 230 V nominal.

**Dave Jones:** I actually get a bit 240 V in the lab here, which is still within specification. Anyway, there's a lot of power behind that and it kept on delivering it.

**Dave Jones:** And probably a thumbs down to Weller for not including any mains fusing in that. I Yeah, not sure if I mentioned that in the previous review. I'll have to have a look.

**Dave Jones:** Anyway, yeah, that could have prevented my lab almost burning down. And luckily, the smoke alarm here didn't go off cuz if it did, would have cost me about 1800 bucks for the uh fire engine callout.

**Dave Jones:** Anyway, if you liked it, give it a big thumbs up. As always, discuss down below. Catch you next time. Mhm.
