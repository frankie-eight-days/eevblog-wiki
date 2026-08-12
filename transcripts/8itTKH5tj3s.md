---
video_id: 8itTKH5tj3s
title: EEVblog #1152 - 240V-120V = Magic Smoke!
url: https://www.youtube.com/watch?v=8itTKH5tj3s
source: youtube-asr
---

**Dave Jones:** Hi, we have a problem. I needed an extra soldering iron the other day and of course the lab's not completely set up yet, so the soldering bench and soldering room's not completely set up. So, I reached into one of my boxes that

**Dave Jones:** has all my soldering gear in it from the old lab and I went, "Oh, yeah, this Weller will do. I'll just plug that in. Just need something quick." And it started flashing on the screen and I thought, "Oh, that's kind of weird. Like

**Dave Jones:** something's going on as there, you know, a contact thing with the iron probe or something." And in the couple of seconds it took me to process that, wah wah wah wah, smoke started billowing and I'm talking like this wide. It just

**Dave Jones:** started billowing right out the bottom of the this poor old Weller soldering station here. And then I quickly remembered, "Oops, it is a 120-V version. And of course we've got 240-V here in Australia. So, yeah. Um I wish this was smell-a-vision

**Dave Jones:** because if you could smell this, uh yeah, it's got that magic smoke smell. All the magic smoke escaped from this thing. So, I thought we'd take it apart and I might not be able to repair it, but yeah, oops. And I think almost every

**Dave Jones:** soldering iron on the market is like uses a transformer-based system. They are a fixed voltage. Like some of them might have a voltage tap that you could change or something like that, but none of them that I'm aware of anyway off

**Dave Jones:** hand, use a switch-mode converter to get like a universal input mains voltage. And that's probably because I would guess that they really, you know, we've got like a large power heater, like a 50-W or 100-W heater switching off and

**Dave Jones:** on rapidly and stuff like that. And switching a load like that, a 50-W load, isn't great for like a switch-mode power supply. So, it's probably just easier and better performance just to use a transformer. And of course, it gives the

**Dave Jones:** thing a bit of heft. So, there's nothing wrong with the Weller. It was a PEBCAK. It was me. So, let's crack this thing open and see what damage we've done. But by the amount of smoke that escaped from

**Dave Jones:** this thing, it's not pretty. And of course, the active ingredient inside all electronic components, including transformers and everything else, is the magic smoke. And once the magic smoke escapes, it doesn't work anymore. Ah, damn it. And of course, I've done a

**Dave Jones:** previous teardown video on this thing. So, let's have a look. Nothing obvious on the uh Whoa. What? There's nothing obvious at all. That's terribly disappointing, isn't it? No Oh god, that smell is uh That smell is horrible. Anyway, I can't see

**Dave Jones:** anything. Let's check. Let's get the board out and have a look on there. Because it did all waft out this front vent, this bottom vent here. And the smoke was like it must have like filled up all in here. And then

**Dave Jones:** um the pressure of it just like pushed it all out and it billowed in a big wide billow of smoke coming out. So, all right. Let's have a look. What? Wow. I'm not seeing anything. See any blow holes or anything like that. What's

**Dave Jones:** What's going on? Ah. This is incredibly disappointing. Where did the magic smoke escape from? There's only one electrolytic cap in here, which is a non-vented one. It doesn't have the like the little you know, marks on there. The vent

**Dave Jones:** marks, the score marks. So, that must be one of those solid uh electrolyte caps. Oh, yep. I'm just absolutely stunned that nothing is blown on here. So, I can only presume that it must have come out of the

**Dave Jones:** transformer. It was awful amount of smoke and it came out within like 2 3 seconds, it started billowing out of this thing and it was a ton of smoke. It was unbelievable. And of course, I just you know, reflex reaction pulled the

**Dave Jones:** mains cord at the back of the thing and and then I actually what I did is I actually once I made sure it wasn't physically alight, I actually shoved it in a box to stop the all smoke billowing

**Dave Jones:** out, but there's nothing wrong with that main board there. Like the power training here was blowing, you'd expect to see like a big blow hole in it or something like that, but yep, I can only presume that the smoke

**Dave Jones:** came out of the transformer. And sure enough, if I actually smell that board, there's like no sign of it whatsoever. So, yeah, I think that is just hunky-dory. Must have all come out of the transformer. And sure enough, if you

**Dave Jones:** smell the transformer, yeah, that's where the that's where the magic smoke escaped from. So, I can only presume that it like burnt the enamel off the wires. Once that amount of smoke escapes from something like a transformer, even if it

**Dave Jones:** even if I powered this up again and it worked, I wouldn't trust it because that smoke came it must have come from the you know, the the laminated wires on there. So, that just breaks down the insulation. Yeah, not a good thing. So,

**Dave Jones:** I would I would not trust that and reuse it even if it worked after a smoking overload like this. And you can see that this does have both fuse and poly switch protection, but unfortunately, this is only on the

**Dave Jones:** secondary side of the transformer here. You can see over here, this is a 120 V fixed 120 V transformer, so you can't like just choose another tap and convert these from 120 into 240. There's the mains input, goes straight through the

**Dave Jones:** switch, straight into the primary side of the transformer there. So, yeah, that's where it must have smoked, on the primary side. So, let's just measure some stuff here. The uh secondary side of the transformer, you'd expect it to be like,

**Dave Jones:** you know, an ohm, sub an ohm, something like that. Bugger all, 0.3 ohms. Yep, something like that. That's fine. Is our fuse intact? So, our fuse did blow, by the looks of it. Yep, that that protected that. No worries. And then a

**Dave Jones:** poly switch. Uh there Yeah, there we go. So, that's low, but that fuse has blown. So, it looks like that protected the uh secondary side of it, hence why we don't, you know, well, there's no visible signs of damage. Doesn't mean we

**Dave Jones:** don't You know, doesn't mean that this thing is not damaged. You know, you'd have to uh power it up with uh some AC here and uh do it that way, but um we've got another fuse on there. Let's

**Dave Jones:** measure that, baby. There we go. That fuse is intact. So, yep, that's fine. So, this uh design is quite good from a secondary side uh protection uh point of view. So, that board, but unfortunately, there's just nothing on the primary side. The primary

**Dave Jones:** side is not fused at all, and I assume that's legal, cuz well, wouldn't do otherwise. I assume it's legal in might vary in other countries, but there's no fusing at all. I don't think I actually mentioned that in my uh review at all of

**Dave Jones:** this thing and uh tear down previously, but now it's it's it's obvious. There is no primary side fusing, and they should at least have an integrated uh fuse with the holder, and that probably would have uh well, should

**Dave Jones:** have, if you size the fuse correctly, should have uh at at least, you know, stopped it. But, anyway, let's measure the primary side cuz I'm pretty sure that's where the magic's go smoke escaped from. And of course, primary side

**Dave Jones:** transformers, you'd expect like, you know, tens of ohms, hundreds of ohms, that kind of thing. But, uh What what what? 0.2 ohms. Um yeah, that's a lot. Um get your calculator out. I'll leave that for an experiment from home. But, like, 0.2 ohms calculate

**Dave Jones:** 240 or 110 volts across 0.2 ohms. How much power is that? Bueller? Bueller? So, obviously, what's happening inside there is there's going to be some enamel burnt off the insulation inside there. So, it might be time for a

**Dave Jones:** teardown of that. And for those who want to see, let's compare it with a rip-off Hakko FX-951. This is a 240-V version, but of course, the primary side transformer will be in the tens or hundreds of ohms category. And there we go, 64 ohms. By

**Dave Jones:** the way, these rip-off Hakko FX-951s are absolute garbage. I haven't opened it yet, but I used it on a live stream video assembling that Gigatron board, and it was just utter trash. So, we can get these caps off

**Dave Jones:** here. They're all They're sort of Oh, yeah. Uh-oh, hello. Hello. Oh, that poor primary side transformer. And you can tell it's the primary side, by the way. For those who don't know, the secondary side in a step-down transformer, which

**Dave Jones:** is most products, the secondary side is going to have thicker wire in there cuz it's like it's stepping down, so higher current. Whereas, the uh Oh, that's It's Oh, there we go. Oh, that's more spectacular than a and a component and a

**Dave Jones:** blow hole in a uh like output transistor, isn't it? Wow, look at all the Yeah, all the enamels burn off that. Anyway, uh thinner wire on the primary side. Wow, no wonder it shorted. Look at that. So, that's what happens

**Dave Jones:** when you apply like 240 V to a 110 V transformer. And this could have been prevented if they had a fuse cuz this thing could have like, you know, could have caught on fire. Imagine if I turned it on and

**Dave Jones:** then uh like walked away and then didn't realize and went to the bathroom or something and, you know, this thing could have like complete like that would have been 240 V just delivering pumping the power into this thing, but my uh

**Dave Jones:** mains fuse did actually um eventually blow. I'm not sure how uh long after it actually blew, but anyway, um you know, you could maybe fix it, but you'd have to rewind the whole damn thing. There's just like it's silly. Anyway, if you

**Dave Jones:** haven't seen a transformer construction before, this is what's called an E core uh transformer. It gets its name from the shape of the laminations. These are the laminations. You can see all the different and you know, count how many

**Dave Jones:** laminations are in there. Anyway, uh it gets its name from the shape of the lamination. In this case, you can't see it, but there's another part of this core this laminate. You can see it's broken there and there. It goes around

**Dave Jones:** like that like a C, but it's actually got a center one that goes through. So, it's actually shaped like an E, the letter E. So, it's like E and I it's called. Um and then you can see that

**Dave Jones:** they just weld the I part onto the E part there. So, that's how and this is just the center lamination goes through like that. And then they wind the primary and the secondary in separate uh plastic enclosures like this and they

**Dave Jones:** have the electrical separation. So, that's the electrical isolation between your primary and just secondary here. So, yeah, that's a typical for a mains transformer. I wonder if there's anything on the bottom. Let's get that out of there. Oh, yeah. Yeah.

**Dave Jones:** Just as crusty on the bottom as it is on the top. Oh, the top. This is the top. Yeah, sorry. All the poor enamel coated wire. So, that was the That's the smell in this thing. It's the burnt enamel. And wow,

**Dave Jones:** you can just Yeah. It could just turns into this brown. Really, I don't I don't know if I've actually seen that. Like burnt in to that extent before. I've seen like little, you know, blow holes in transformers and stuff like

**Dave Jones:** that. But, this one is like completely like consistently burnt. The secondary side is also is is of course completely intact. And of course, we would have got Initially, we would have got double the voltage out of But, you know, the fuse

**Dave Jones:** probably kicked in or maybe it No, it did actually cuz I said there was something on the LCD. Cuz it actually flashed something on the LCD. I can't remember what it was. It was just a couple of characters or So, it looked

**Dave Jones:** like the processor was actually working. And then, yeah. Panic set in and I pulled the mains plug. So, yeah. But, isn't that terrific? I love it. So, let that be a lesson to you. Don't plug 240 V into 110. And yes, I

**Dave Jones:** should have labeled this I know it's labeled on the bottom, but I should have put a huge label on the top of the unit. Stupid me, lazy me, didn't do that. But, of course, for these circumstances where I just needed an extra iron somewhere,

**Dave Jones:** you know, I'm going to pick up just any, you know, random iron that's sitting around. So, yeah, I I did know like I did know this. I was just too lazy to do it. And ah, she'll be right. I'll remember that it's 110.

**Dave Jones:** So, yeah, that was a PEBCAK. Don't do that. And I know what you're thinking, Dave, does the controller still work? All right, well, let's find out. Um as per the labeling on here, 120 V primary, 23 V secondary, uh 60 Hz. It should be fine,

**Dave Jones:** 50 or 60. I can generate that with my Appso pulse generator here. Uh 23 V secondary, 60 Hz. So, let's plug that in and see what's what. We're probably going to get some light drops on these leads and stuff like that, especially if

**Dave Jones:** you use the heater, but I got the heater unplugged. So, hey. Hello. There you go. LCD works. Let's plug the iron in.

**Dave Jones:** Yeah, it's happy with that. It's set for 270. We'll just leave it at that. That's fine. It's not going anywhere. Oh, it's dropped a Yeah, 15 up there. So, yeah, we're getting some loss in the leads. Didn't normally take Yeah, it's

**Dave Jones:** going up. Didn't normally take that long to start up anyway. That's looking good. That's looking good. She's heating up. Not going to touch it. I'm going to assume that the thermocouple in the tip is still good. And uh

**Dave Jones:** that it should You can see it's delivering power. That's what the little little lightning bolt icon on there is. And will it get to Will it get to 270? Should maybe start to be able to melt the Yeah.

**Dave Jones:** There you go. It's melting solder. Will it actually get to 270 and regulate? Yep. Yep. No problem. The little icon thing is flashing off and on. There you go. Works a treat. Winner, winner, chicken dinner. Good on you,

**Dave Jones:** Weller. it's obviously a like a a robust designed secondary. The fuse did its job on the transformer here, kicked in, but obviously like the power train and everything else was robust enough to survive double volts on the secondary.

**Dave Jones:** Nice. And well, I've got to ask like how did this actually happen? Because you're plugging 240 volts into a 110 volt transformer, double the voltage on the output of course. That means for a resistive like element loaded that

**Dave Jones:** we've got here, roughly like that's going to be four times the power. So, okay, it's going to be delivering four times the power, but surely like this thing started smoking literally like two or three seconds after I plugged it in.

**Dave Jones:** So, even if it like it cuz it would have probably started applying power to the heating element straight away. So, how it was able to just like completely melt the insulation like that after a couple of seconds at four times the power, I

**Dave Jones:** don't know. Is it a transformer design issue? Of course, it should be fused. I reckon that's a that's a bad mistake there is not having the primary side transformer fused especially when it could be quite common to you know, to sell these things in

**Dave Jones:** different regions at a different voltages. It's not like oh, you're going to suddenly plug a 240 volt iron into 600 volts mains or something like that, you know, that doesn't really exist. It's not going to happen, but accidentally plugging a 115 120 into a

**Dave Jones:** 240, that's certainly possible. So, certainly should be fuse worthy, but is there not enough enamel insulation on the primary side? Is it a poor design transformer? I don't know, but jeez, like wouldn't have expected that, really. Oopsie. If you like the video and my screw up,

**Dave Jones:** give it a thumbs up cuz that always helps a lot. And discuss down below if you got like photos or anything of stuff that like mains transformers that you've burned out or other products you burned out when you incorrectly hooked up the

**Dave Jones:** wrong mains voltage. That's a problem here in Australia. We get a lot of you know, if you import a lot of stuff, you'll get 110 V. Use test equipment on eBay, you've got to be very careful importing it

**Dave Jones:** here. And it's not a problem. You Yanks wouldn't have too much of you know, who else uses 110 V? But you guys wouldn't have too many problems because you import stuff. And if you're 240 V product, you hook it up

**Dave Jones:** to 110, meh. The magic smoke like this isn't going to escape. It's just going to like either not power up or have reduced performance or whatnot. So there's a lot of power behind a 240 V mains. In fact, there's 2400 W

**Dave Jones:** or even more before the main fuse will blow anyway. Like I think I got a 16 amp breaker here for my 240 V nominal well, 230 V nominal. I actually get a bit 240 V in the lab here, which is still within

**Dave Jones:** specification. Anyway, there's a lot of power behind that and it kept on delivering it. And probably a thumbs down to Weller for not including any mains fusing in that. I Yeah, not sure if I mentioned that in the previous review. I'll have to have a

**Dave Jones:** look. Anyway, yeah, that could have prevented my lab almost burning down. And luckily, the smoke alarm here didn't go off cuz if it did, would have cost me about 1800 bucks for the uh fire engine callout. Anyway, if you liked it, give it a big thumbs

**Dave Jones:** up. As always, discuss down below. Catch you next time. Mhm.
