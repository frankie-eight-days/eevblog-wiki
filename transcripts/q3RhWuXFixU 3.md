---
video_id: q3RhWuXFixU
title: EEVblog #1347 - SMD Thermal Jumpers could be GAME CHANGING!
url: https://www.youtube.com/watch?v=q3RhWuXFixU
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 32, "3": 66, "4": 77, "5": 89, "6": 100, "7": 113, "8": 124, "9": 136, "10": 149, "11": 165, "12": 183, "13": 195, "14": 212, "15": 228, "16": 246, "17": 262, "18": 274, "19": 287, "20": 298, "21": 314, "22": 327, "23": 339, "24": 352, "25": 370, "26": 379, "27": 393, "28": 404, "29": 419, "30": 432, "31": 443, "32": 456, "33": 471, "34": 484, "35": 496, "36": 512, "37": 524, "38": 537, "39": 551, "40": 567, "41": 583, "42": 597, "43": 611, "44": 622, "45": 636, "46": 650, "47": 663, "48": 679, "49": 697, "50": 710, "51": 725, "52": 738, "53": 750, "54": 762, "55": 776, "56": 787, "57": 800, "58": 813, "59": 827, "60": 846, "61": 861, "62": 873, "63": 885, "64": 895, "65": 908, "66": 922, "67": 933, "68": 949, "69": 962, "70": 977, "71": 992, "72": 1012, "73": 1028, "74": 1042, "75": 1057, "76": 1069, "77": 1080, "78": 1095, "79": 1108, "80": 1121, "81": 1133, "82": 1147, "83": 1157, "84": 1171}
---

**Dave Jones:** Hi, way back in episode number 744, linked in up the top, down below, at the end if you haven't seen it, and I highly recommend you do cuz it's all about surface mount thermal design, how to get uh power out of SMD thermal components

**Dave Jones:** out through your case of your product. And yes, I've actually, this might be familiar, I've redrawn this entire thing. So, why am I going over previous material like this? Aha, it's because there's a new part or new parts on the

**Dave Jones:** market that actually, well, they don't revolutionize this, but they provide another really nice option for getting heat out of SMD thermal parts. So, I thought we'd take a look at them, but we really have to go back to this original

**Dave Jones:** uh diagram to explain what we're talking about here. Now, obviously, I'm not going to go over everything again, but we will recap it. Everything's in that video, highly recommend you watch it. I go into much more detail. Now, of

**Dave Jones:** course, it's very easy to get heat out of through-hole parts like a TO-220 package. They got a big bolt hole in them, you bolt them into your the side of your case, Bob's your uncle, gets the heat out, no worries. How do you do it

**Dave Jones:** for an SMD part, though? Well, once you've decided that your design is going to be surface mount, you want as much of your design to be as surface mount as possible because then it can all go into the pick and place machine, and then it

**Dave Jones:** all just magically comes out. You don't want extra bolts and washers and and heat bars and heat sinks that you have to bolt in and screw on and things like that. They're all extra production operation steps, extra cost, everything

**Dave Jones:** else. And yes, you can actually get a surface mount heat sinks suitable for pick and place machines. They're usually quite small cuz the pick and place machines with their little suction heads don't have, you know, a huge amount of

**Dave Jones:** suction force that's on your board and then reflowed, of course, cuz they're a heat sink. They suck all the heat out of your joint when you try and reflow them. But, you know, you can get Here's an example of some small SMD heat sinks

**Dave Jones:** that you can actually get to put on your design. And they're okay, but your traditional solution for this is in orange here is solder it onto a large copper pad like this. And then there you have firm thermal vias like

**Dave Jones:** this going through the green PCB here. And then in this case through to a thermal transfer block or a thermal transfer bar, which then transfers it to the case and you can get rid of the heat from the case. Beauty. And this is where

**Dave Jones:** you start talking about your electrical thermal equivalent circuit. And basically, the idea is that current is equal to power from your power source, which is your device. Then it flows through all of the thermal resistances instead of electrical resistances,

**Dave Jones:** they're thermal resistors. And they've got theta there. So, JC, you'll see this in data sheets. That's junction to case. So, inside the little transistor, that from the junction in there, how much thermal resistance to get it to the

**Dave Jones:** case. And then you've got thermal resistance of the via here, thermal resistance of your insulating seal pad, thermal resistance of your heat transfer block, your thermal resistance of your case. And then you've got the ambient temperature. And voltage in this equivalent circuit is

**Dave Jones:** equivalent to temperature. And then you've got essentially what you might call a thermal ground, I guess. And then you've got your ambient temperature. So, every part through the step, the voltage will increase. If you got current flowing through here, the voltage at each point

**Dave Jones:** will increase. And therefore, in the thermal equivalent circuit, uh your temperature will increase. So, your junction up here, the junction temperature up there, it can't exceed the maximum data sheet recommended junction temperature. So, the art of thermal design is trying to keep your in

**Dave Jones:** worst-case conditions, worst-case ambient, cuz if ambient rises, everything else rises, as well, is trying to stay under within your data sheet temperature limits and temperature of other parts inside which might be affected like electrolytic capacitors. For example, if you have them close,

**Dave Jones:** they might, you know, the electrolyte inside heats up, you shorten their life, etc., etc. Now, here's where we get into the detail of we're going to talk about these thermal jumpers here, these new components out that might change the

**Dave Jones:** game for a lot of designs. So, let's take a look at them, right? Your traditional uh way of getting your heat out of your part is to have a large amount of copper like this, okay? Which you dedicate to

**Dave Jones:** that particular component or that tab of that uh component, and then you get the heat out. And you want that not only cuz it's a large surface area, but then you have all these vias in here, which via

**Dave Jones:** stitch. And this is roughly There's a uh limit thermal resistance of a via is about roughly 50° C per watt for a 1-mm hole, for example. And depending on the number of holes you got, then the lower the overall thermal resistance of your

**Dave Jones:** via here. So, if you've only got one via trying to get all the power through one via, it's very high high thermal resistance. So, it turns out the optimum value is about 10, cuz beyond that, it starts to like the

**Dave Jones:** you get the effects of the heat spreading across the pad and all sorts of, you know, intricate thermal stuff. You really need like really expensive thermal modeling software to actually do that properly. But, you know, 10 vias or

**Dave Jones:** something like that might be optimal. Anyway, let's actually forget all about uh getting the heat out to your external metal case through your thermal transfer block and your seal pad and everything else cuz that was the previous video. Go

**Dave Jones:** watch it. What we're going to focus on today is using these new thermal jumper parts to actually utilize the internal ground plane in your PCB in as a heat sink instead of actually like you know, using a little SMD heat sink on top or

**Dave Jones:** using a thermal or just using one large pad. You don't have to use a thermal via cuz they're only if you want to transfer the heat down to the bottom layer for some reason cuz you might have more

**Dave Jones:** routing room down there. Like you might this might be the top layer, but then you might happen to have like this much space on the bottom layer for example, you know, cuz you didn't need the routing room. You might have that room

**Dave Jones:** for a large extra heat sink plane on the bottom side as well as a small one on the top. So you might use thermal vias to get down to the bottom layer and then spread the heat across there. And how that heat

**Dave Jones:** gets out to the external case, we're not going to worry about in this video. So we're going to assume that the device you're trying to get the heat out of cannot be electrically connected to ground or power plane because you've got

**Dave Jones:** your four layer PCB, right? These days four layer PCBs are cheap as chips. And if you're doing any sort of advanced design, you're probably going to be doing a four layer board anyway. So you've got this a huge ground and power

**Dave Jones:** and likely power plane inside your product. Why can't you use that as a heat sink? And it's like those SMD heat sinks that we showed before. Yeah, you could use one of those, but they're actually fairly expensive in their own

**Dave Jones:** right and they take up physically height, you know, extra room inside your case. But if you've got a really compact design, really low form factor, it might be advantageous, greatly advantageous, it might be game changing for you to use

**Dave Jones:** your internal ground plane which is all the way through like this, all the way through your product. Why not use that as a heat sink? And of course, you might want to change your layer stack on your PCB if you do this. Like usually when

**Dave Jones:** you do a full layer board, the ground and power planes are going to be in the middle of your PCB and the signals are top and traces are top and bottom layers. But if thermal is a major consideration in your design, you may

**Dave Jones:** actually want to flip that. You may want to have power and ground on the outside or at least ground on the outside layer so that either top or bottom so that then you can use it as a heat sink as

**Dave Jones:** we'll see using these thermal jumpers cuz they're absolutely fantastic and game-changing. And then of course because the copper's on the outside of the PCB, it's actually more readily available to transfer. It doesn't have the insulative properties of the fiberglass wedged in the middle

**Dave Jones:** of the PCB. So having your copper on your top or bottom layer, your big ground plane is much more effective. But then you've got to take signal integrity into account and all that sort of stuff. But let's assume that thermal is one of

**Dave Jones:** your major priorities and you want and you want to or need to just use your ground plane. Well, if you've got your traditional method like this, you can't because this device that you're using can't be electrically connected to

**Dave Jones:** ground or power plane because it'll short out because the tab on the device is electrically it's the V out pin or it's the you know, V in pin or some other electrical pin that's not ground. So you can't just via stitch to ground.

**Dave Jones:** If you're lucky enough to have a device where your thermal tab is either isolated or is grounded, then great. Just thermal via stitch down to your ground plane either internal or external. But where the thermal jumpers come in is if most parts like this need

**Dave Jones:** to be electrically isolated. That's why seal pads exist. That's why you use insulation on majority of thermal devices because they can't be electrically connected to ground. So in this case, you have two choices. You can devote a whole lot of your PCB routing

**Dave Jones:** area to just the heat sink, the isolated electrically isolated heat sink for that particular device. But, then you've you've ruined like you're wasting all of that space. If you've got a really dense design, then you can't put any traces on

**Dave Jones:** there at all. Um it's a real problem. But, if you use your ground plane, aha, that changes your entire routing uh dynamics and your routing density and everything else. So, how do you do it? With these thermal jumpers. Okay, so

**Dave Jones:** let's assume that you've got your SMD part that you want to get the heat out of. It needs to be electrically isolated, but you want to use your big ground plane as a heat sink. And why wouldn't you? Now, of course, you're

**Dave Jones:** going to have your uh copper pad to solder your uh part down onto, of course, your SMD part. But, then how do we get the heat out to the ground plane? Well, we can get our thermal jumper like this. It looks something

**Dave Jones:** like this. Let's just I'll just draw it like this. They come in different shapes and sizes. And by the way, when it comes to thermal jumpers, is width better or length better? No, I'm telling you width is better. You want a short, fat, stubby

**Dave Jones:** one than a big long one. Trust me. You're going to get much better thermal transfer from a big fatty. So, these thermal jumpers, here's a photo of them. They just look like, you know, regular SMD resistors available in long, thin,

**Dave Jones:** narrow ones, big, fat, wide ones. Or uh you know, they they just look like regular resistors, but they're electrically isolated. There's no resistance in them. And but they're thermally conductive. So, you just use uh just your regular pads like this for any for that regular

**Dave Jones:** package uh size like that. And then, you simply put a big fat trace in there like that that connects through to this thermal jumper. And then, of course, this one here, you would just then put your thermal vias like that to stitch it

**Dave Jones:** down to your ground. So, now you've got your heat, it flows from your device, it flows through your copper like this. It's pretty efficient at this point. Then it flows through your thermal jumper like this. Then they don't have a

**Dave Jones:** zero thermal resistance, but you know, they're reasonably low. We'll take a look at the data sheet in a minute. And then uh it flows into your vias like this, and then it flows down your vias into your big power plane,

**Dave Jones:** big ground plane all over like this. So, you can use your entire board as a heat sink, but taking up very little space. So, you know, I've drawn it quite large here, but these things can actually take up a small amount of space. And if you

**Dave Jones:** want to, you can actually use multiple ones. You can have one here, one here, one on this side. You can put them all around your device if you're you know, do your thermal calculations, your back-of-the-envelope calculations at the

**Dave Jones:** design stage and go, "Yeah, I think I'll probably need three of them." or something like that. Now, these things aren't particularly cheap. They start from like, you know, a thousand of quantity start from about 30 cents a pop. But hey, the the little SMD heat

**Dave Jones:** sinks uh that we looked at before, they're not cheap, either. Um and they take up vertical height, but this way everything's low profile. So, it enables your design to be a really small size, but it could be much more efficient

**Dave Jones:** because you're using your entire ground plane, which could be on the outside of your layer of your board, as I said. And then you take the solder mask off, of course. If you're using your ground plane as a uh heat sink, then you

**Dave Jones:** wouldn't cover it with solder mask generally. Um that's just less efficient. So, that's the beauty of these thermal jumpers, and it really is game-changing. As far as I'm aware, they've only been out for like the last year or two. Um and they might be

**Dave Jones:** expensive, but it could radically change your thermal design for your product. It could really enable it. Whereas before, you know, you had to have this big isolator pad. Now, in every design, you can use your ground plane as a heat

**Dave Jones:** sink. Beautiful. All right, we'll just take a quick look at the data sheet here because, well, there's nothing to it. And these are fairly new parts. You can see down here, first revision, January 2019. So, they're available from two

**Dave Jones:** manufacturers that I'm aware of. One is Vishay, and the other is this company I've never heard of, The Engineers' Choice. There they are. American Technical Ceramics. They call them thermal conductors. Vishay call them thermal jumpers. Basically, look, it looks very much like a

**Dave Jones:** resistor, except it's non-conductive. They've just got an aluminum nitride substrate inside, and that's what is makes it thermally conductive. They've then just got the regular end caps with a nickel and solder termination. You get different finishes and things like that.

**Dave Jones:** You can get lead or lead available. Yes, lead or lead-free. They're saying it's greater than a gig, but they're basically, yeah, they're as good as open. Suitable for power supplies, RF amplifiers, synthesizers, switch-mode power supplies. That'd be a biggie. And

**Dave Jones:** here's a very nice look at They've got a thermal camera. I I could maybe do some tests, but buy these and set up custom PCB in different configurations. That'd be nice. Let me know in the comments down below if you want me to go to that sort

**Dave Jones:** of effort, but I don't expect any results different to this, but it'd be nice. Maybe I can check thermal vias and things like that. Show the difference between pads and ground planes. And I, you know, so they just got a resistor

**Dave Jones:** here. I don't know what is that like 1206, something like that. And they just put in a current through it, heating up the resistor, and with nothing, right? So, with just the extra size pad here, so they have not installed the thermal

**Dave Jones:** jumper like they had here. Okay, this is a 1206 size thermal jumper. So, this is without the thermal jumper, the resistor gets up to 150° C. But if you whack in the thermal jumper like this, and it's got like a large uh in there just

**Dave Jones:** connecting the two pads. So, this is one pad for the thermal jumper. This is the other pad here. Well, it's got this large um pad over here. There's no Looks like there's no via stitching or anything like that. They're just using

**Dave Jones:** the thermal jumper going to just a larger pad here acting as a heat sink. Um and look, it's dropped down to 95°. Wow, that makes a That makes a huge difference. And that's not uh connecting it through to the ground I presumably

**Dave Jones:** not connecting it through to the ground plane. So, I reckon if you put little thermal vias in there going down to a ground plane, you'll get a substantial improvement over that 95°. What you get? I don't know. You can do some

**Dave Jones:** back-of-the-envelope calculations um and but then of course it's going through to a much larger heat sink, which is your ground plane. And how much thermal resistance we're talking about? Well, we've got the data here. Look at this. So, thermal resistance in degrees C per

**Dave Jones:** watt, not of that milliwatts per uh degree C the uh thermal conductance rubbish. It's one over. No, bugger that. Um we're we're talking for like an 0603, okay, 14° C per watt. So, it's not that great. But as I said, if you go for the

**Dave Jones:** short fat one, like this is What 0603 means is that it's uh half as wide as it is long. So, but this one, the 0612, is twice as wide as it is long and it drops from 14° um C per watt to 4° C per

**Dave Jones:** watt. So, 4° C per watt is you know, on par with like 10 thermal vias or you know, something like that. So, it's it's pretty decent performance. And once again, you get a nice big fat one over here, the 1225. That'll be that jobby

**Dave Jones:** there. Look at that. Look at that. Just short and fat. Cuz you want it fat and wide so that all the thermals can get through. And dielectric uh with standing voltage 1.5 kV and capacitance is a big thing as

**Dave Jones:** well cuz if you've got if you're using these on switching power transistors, especially in RF applications and things like that, that can be a big deal. So, you want them to have ultra-low capacitance. It is 0.07 pF. That's like half a bee's dick. And that

**Dave Jones:** does, of course, increase for your uh wider ones, your short fatties like that. So, it's a trip, but it's still like it's, you know, 0.2 pF. It's nothing. These other parts from my Q bridge, I won't go through them. You can

**Dave Jones:** look I'll link the data sheets in down below. They're exactly the same. Uh the thermal resistance slightly better. These can get down to, look, three uh degrees C per watt, but these ones are available and they're available in

**Dave Jones:** aluminum nitride or beryllium oxide as well. And the beryllium oxide just a smidge lower thermal resistance. So, you know, if you've got some, you know, wiz-bang military application and you don't care about cost and they aren't just yeah, it's better. More better.

**Dave Jones:** It's actually uh substantially different for some of these others. Look at this, 13 compared to 20 for an 0603. So, there's advantages there. And the Vishay ones, they're available on Digi-Key here. I'm not sure where the other website I'm not sure where the others

**Dave Jones:** are available from. But look, uh these are 1,000 of uh quantities. We're talking like, you know, like 38 uh cents here and stuff like that. But they can actually go up like 50 a dollar. Now you're to a dollar 26 for the big

**Dave Jones:** fatties down here. Oh, worth every cent. So, I think these things are really quite game-changing and they seem to be fairly new parts. Please leave it down below if these are have been available for donkey's years, but this is the

**Dave Jones:** first I've heard of them. So, thank you very much for the viewer who uh pointed these out to me. These are great. Um yeah, I could radically enable uh designs uh small form factor designs that you just couldn't do before. So,

**Dave Jones:** yeah, could be game-changing. Check them out. So, there you There you I hope you enjoyed that video. If you did, please give it a big a thumbs up. And as always, leave comments down below or over on the EV blog forum link down

**Dave Jones:** below. Every video has its own forum thread. That's where people can discuss stuff if you don't want to discuss it on the YouTubes and all of my alternative platforms. YouTube went down today famously. But the good thing is all my

**Dave Jones:** videos are available on like half a dozen alternative platforms. So, check it out. Catch you next time.
