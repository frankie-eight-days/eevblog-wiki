---
video_id: Zao8upe4phs
title: EEVblog #335 - Carbon Printed Resistors
url: https://www.youtube.com/watch?v=Zao8upe4phs
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 45, "3": 61, "4": 81, "5": 97, "6": 117, "7": 137, "8": 157, "9": 173, "10": 193, "11": 217, "12": 237, "13": 257, "14": 273, "15": 293, "16": 313, "17": 333, "18": 353, "19": 373, "20": 393, "21": 409, "22": 425, "23": 441, "24": 473, "25": 493, "26": 518, "27": 538, "28": 562, "29": 578, "30": 595, "31": 607, "32": 627, "33": 643, "34": 659, "35": 679, "36": 699, "37": 719, "38": 731, "39": 747, "40": 763, "41": 779, "42": 795, "43": 815, "44": 827, "45": 847, "46": 867, "47": 883, "48": 903, "49": 923, "50": 943, "51": 963}
---

**Dave Jones:** Hi, in the previous video, I did a teardown of a 1986 vintage Scion II PDA, and on a quick scan of the board, there were these black marks on here across component pads, and at first glance, I thought they were just a no-place marker

**Dave Jones:** for, you know, for not actually placing the components on the board. But several people pointed out that they're most likely carbon-printed resistors directly on the board, and I think that's probably the case on second glance here. Now, I sort of casually dismissed this thought at the time

**Dave Jones:** when I was briefly looking over the board doing the teardown, because it didn't really seem to make sense that you would carbon-print resistors on here when you could have just placed you know, cheap as chips. They almost free these resistors placing this so darn cheap.

**Dave Jones:** It just didn't seem to make sense because they weren't using carbon printing anywhere else on the board, like for example the buttons, which is a fairly common technique. You'll get carbon printed on the button surfaces, but they didn't do that. So it would have

**Dave Jones:** been an extra step, an extra cost in the manufacturing process to actually print these carbon resistors on here. But you can see the physical, it looks like they are, because you can see the physical thickness of these ones is much thicker than these ones here, for example.

**Dave Jones:** So they're obviously using a different value of resistance for these ones, which are clearly pull-ups or pull-down resistors there. I'm not sure what rail that is, I haven't actually measured it yet. But these ones are typically thinner, and of course the resistance of these carbon,

**Dave Jones:** these printed carbon tracks is going to depend upon the length, the width, and the surface area of these things. And the thickness of the coating of course, they're actually quite variable, these things. They're typically like in the order of like 30% or so.

**Dave Jones:** So they're very crude resistors, but good enough for pull-up and pull-down resistors like this. But these ones over here, they've obviously got some other pull-ups or pull-downs, probably on this looks like something going into the ROM devices here or somewhere under there, but

**Dave Jones:** they does look like they have printed on there. So let's actually measure these things and see what we get. Now you can't actually measure these in circuit, because you're not actually going to get a reliable reading. But these pull-down resistors here, and they are

**Dave Jones:** pull-down. This side here is actually ground, I've checked that. And these pull-downs just go to these 0.1 inch expansion headers here. So they're not connected to anything else in circuit. So we are actually able to measure the value of these things. So let's get in there, and let's

**Dave Jones:** do that. And we can get in there and measure this individual pad. There we go, 65k, 72k, so there's already 76k, there's already quite a significant 74, very significant spread on these values. And we've got a few in a row there that are quite

**Dave Jones:** close to each other. But there you go, those large thick ones up there in the corner, they're, you know, around about that 75k value. So these are actually carbon printed resistors. Now while it's not great to measure these other ones in circuit, because they're going to active devices,

**Dave Jones:** but at least we can get sort of, you know, a ballpark figure. And this one down here, for example, is 213k. So these are physically thinner tracks, and there you go, it looks like they are a couple hundred k. And of course the voltage

**Dave Jones:** from the multimeter is usually not high enough on the resistance range to turn on any active junctions within these devices here, but you know, it's, if you really want to get an accurate reading, you of course should be getting in there and actually

**Dave Jones:** breaking the PCB traces. But of course it can't, it's not going to give us a higher reading unless there's voltages present in the circuit and stuff like that. So it's not a bad ballpark, and they are all, you know, circa like 200k. So they are effectively at least

**Dave Jones:** double those thicker resistor values there, and that's exactly what you'd expect, just based on the size and shape of them. And if you have a close-up view of these again, that's pretty much precisely what you'd expect. You'd expect sort of these thicker ones to be, you know, roughly double the value

**Dave Jones:** of these thicker ones here. And so they definitely are printed resistors. The million-dollar question is why they've gone to the effort of doing that. Let's do a quick test here to see if we can modify the value of one of these resistors. I'll do the one on the end there, right on the very end.

**Dave Jones:** So it's 65.3. So it's 65.2k, and I'll get my knife out, and let's give it a bit of a scrape here and see if we can change its value. Actually what I'll do here is I'll show you something on the camera here. I've currently got this to

**Dave Jones:** auto aperture, and it's got an aperture value of f2.8 on my lens here. I'm using my Opteka x10 macro lens, and you'll notice that in here, right in the center is in focus and because my camera is at an angle like this, maybe a

**Dave Jones:** 60 degree angle or something, up here, because it's a very low aperture value of f2.8 you get blurring right at the back here, so back's not in focus, center's in focus, and this one's not. And now I've I haven't moved the camera and I've gone into aperture priority mode, now I've set

**Dave Jones:** it to f4.8, and you can see it's gotten a bit better, but the image has gotten darker of course, and a bit more grainy because of the relatively low lighting here, and I'll increase that even further, and let's see if we can get it all in focus.

**Dave Jones:** And there you go, I've gone up to f8, and now you can see all of it is in focus right at the back and right at the front, but this is as high as it goes and it's very grainy, very dark. That's just an interesting effect of when you shoot things at an

**Dave Jones:** angle like this, if you're using a low aperture value like that, and you've got a good camera, things aren't in focus. The end of the board and the front of the board is not in focus, and that's just an interesting side effect of

**Dave Jones:** shooting stuff like this. So anyway, I'll scrape away some of that. So what was it? 72.5k so we'll scrape off hopefully I won't, I shouldn't cut it, these are fairly rigid, fairly solid things, so, but that will definitely, I'm sure that would have changed the value, so let's measure it now.

**Dave Jones:** There you go, 74.5k. It's gone up very significantly. Chipped away a little bit more there, let's see what we get now. Hey, there we go, 186k. Beauty. Now you've got to remember that this is 1986 we're talking about here, but because of the date code, this one was actually

**Dave Jones:** manufactured in 1989, but we're still talking, you know, 23 years ago or greater, so you know, just the pick and place manufacturing technology and the cost of the individual component resistors was much different back then. We, you know, it's a totally different world today, which is why

**Dave Jones:** you would essentially never ever see a carbon printed resistor like this in a bit of modern gear you know, actually in the last, well I haven't seen these for like the last, oh, probably 15 years maybe, or something like that, as a rough ballpark

**Dave Jones:** that you can actually do them in, you know, more exotic products for various exotic and niche reasons, but as far as a general purpose product goes, it's just much cheaper to just place an 0805, 0603, 0402 resistor, because they cost virtually nothing, you know, .0001 cents each

**Dave Jones:** or something like that, when you're manufacturing hundreds of thousands of items like this, they're practically free, and the pick and place machines these days are so fast that really, you know, it's going to be cheaper to place a physical resistor than is to do the carbon printing process on the PCB

**Dave Jones:** because a lot of cost in a product will be bare board PCB manufacturer, especially if it's multi-layer and, you know, high density and all that sort of stuff, so adding the extra step on there to, you know, imprint, to print those carbon resistors on there is

**Dave Jones:** pretty much unheard of these days, but what were they thinking back in 1986 or 1989 here when they manufactured this board, I presume they did it on the original board back in, the first board back in 1986 as well, so what were they thinking there?

**Dave Jones:** There would be a couple of reasons, one would be that the machine that they were using at whatever factory they were using to assemble these, the pick and place machine didn't have enough real spaces available for all the different types of components, but

**Dave Jones:** you know, one of these pick and place machines might typically have, say, for example, 50 feeders, real feeders on it, and if you want to have a look at these things you can go have a look at my video of a typical modern, anyway, PCB pick and place

**Dave Jones:** assembly line, and I'll paste the link in here for that if you want to take a look, I highly recommend it, if you haven't seen it. So, you know, if you exceed that, you know, that maximum number of reels of components, say you've got 50 different values of resistor

**Dave Jones:** on this board, and 50 different values of caps, then you need that number of feeders to manufacture this board in a single pass, and of course the machines these days, you know, they're double-sided, not double-sided board but double-sided as in they have reels on both sides of the machines

**Dave Jones:** and they can have hundreds of feeders, or 100 plus feeders on them. So, really, but I don't remember. Back in 1986 I actually wasn't, you know, that was a year or two before I actually started working in the industry. I was still doing my hobby stuff

**Dave Jones:** back then, but I certainly wasn't involved in the industry, so maybe somebody, a viewer out there who was in the PCB assembly business back in 86 or 89 can actually clue us in on that, but anyway, that would be a reason for going for these carbon printed resistors.

**Dave Jones:** And they would have done it. The key reason would have been cost. It would be cheaper to do that, because there's no way you'll go to the effort to print these carbon resistors here and pay more for it, because there's no advantage. They're just freaking pull-down resistors.

**Dave Jones:** That's all they are. So, you know, you don't care about the value. So let's look at the number of components on this board. You know, we're talking one, two, you know, I assume that these are all the same value cap here, and so they only

**Dave Jones:** take one feeder each, and there's only a couple of resistors on here. You know, there's a couple of caps down there, but really, there's not that many. So a couple up here. So even if they're all different values, and of course there's nothing on the bottom, it's just the

**Dave Jones:** board itself, and you'll notice that these are gold-plated and not carbon plated traces, so it's not like you get those carbon printed resistors for free. It's an expensive extra step. How expensive it was back in 86? I don't know, but you can bet your bottom dollar

**Dave Jones:** they did it because it was cheaper. Now we've just got to figure out why. So really, they wouldn't have exceeded the number of feeders on there, even in a basic machine back in 86, I'm sure. So maybe it was the physical speed of the machine

**Dave Jones:** and the price of the resistors themselves. Maybe they were much more expensive back then than they are now. You know, they practically give them away now, but back then, hey maybe 0805 surface mount resistors cost, you know, a couple of cents each, and that takes X amount of machine time to

**Dave Jones:** actually place each one. The head's got to go back, it's got to fly back, pick up the component, move over, boom. Drop it down, if it's a multiple head one, do it a bit more efficiently, pick up five at a time or something like that,

**Dave Jones:** and drop them in. But it still takes time, so there's that machine assembly time cost there, which you'll typically pay cost per minute, or something like that of the machine time, plus the cost of the resistors. So yeah, they've decided, well, it's going to be cheaper to carbon print these things.

**Dave Jones:** I wonder how much it would have cost them, per bare board, to get those carbon resistors. And in terms of the feeders, these SO packages here, they may have come on tapes, and maybe the small quad flat pack here may have come on tape,

**Dave Jones:** but these larger ones probably weren't on tape, they might have been in trays, or something like that, so they're a different part of the pick-and-place machine, but really there's very few components on there. So I don't think it was I'd be incredibly surprised if it was the limit of the

**Dave Jones:** feeders, you know, and the requirement for a second pass through in that case. Now, I can't actually see any penalization breakout marks on the side of this PCB here. Like, there's no breakout tabs or anything, so I think this is a fully routed

**Dave Jones:** PCB. So they would have assembled this in, like, a custom holder, as it went through the pick-and-place machine. So it's not like that they got, so they probably assembled this one here differently, this one looks fully routed as well. So they probably assembled the two boards differently, as two different

**Dave Jones:** processes, so it's not like they, sort of, you know, penalized the board like this, and they put both boards through the pick-and-place machine at the same time, rolling through like that. Gee, I don't know! They're clearly done as carbon-printed resistors. So if you've got any better

**Dave Jones:** insight into that, back in the late, mid-to-late 80s, then leave it in the comments or jump on over to the EEVblog forum. So I hope you found that interesting. It's not something that you see very often these days, carbon printed resistors. If you liked the video, please give it a thumbs up.

**Dave Jones:** Catch you next time.
