---
video_id: QrYYGS0uZlU
title: EEVblog #1353 - WHY Are These Pins Shorted?
url: https://www.youtube.com/watch?v=QrYYGS0uZlU
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 27, "2": 47, "3": 61, "4": 80, "5": 94, "6": 109, "7": 125, "8": 140, "9": 162, "10": 182, "11": 197, "12": 216, "13": 236, "14": 256, "15": 269, "16": 287, "17": 303, "18": 318, "19": 338, "20": 352, "21": 366, "22": 387, "23": 404, "24": 423, "25": 443, "26": 459, "27": 479, "28": 496, "29": 514, "30": 531, "31": 546, "32": 562, "33": 573, "34": 586, "35": 601, "36": 617, "37": 635, "38": 653, "39": 675, "40": 690, "41": 708, "42": 725, "43": 741, "44": 764, "45": 776, "46": 795, "47": 813, "48": 827, "49": 844, "50": 859, "51": 879, "52": 896, "53": 911, "54": 924, "55": 938, "56": 956, "57": 972, "58": 990, "59": 1008, "60": 1025, "61": 1037, "62": 1055, "63": 1074, "64": 1091, "65": 1111, "66": 1131, "67": 1144, "68": 1156, "69": 1173, "70": 1188, "71": 1206, "72": 1219, "73": 1233, "74": 1244, "75": 1260, "76": 1273, "77": 1290, "78": 1314, "79": 1337, "80": 1354, "81": 1370, "82": 1386, "83": 1399, "84": 1415}
---

**Dave Jones:** Hi. If I don't sound enthusiastic, it's because I have to shoot this entire video again, because I just shot, oh, how many, like 35 minutes, one take, a continuous thing, and my audio wasn't, you can see, I'm supposed to have waveform there. Oh, right, so in a previous video, linked up here and down below, and at the end, if you haven't seen it, I highly recommend you do, it's an aircraft transponder teardown.

**Dave Jones:** And I had lots of comments and also emails about this one from people saying, oh, we spotted something in the video, and I thank you, I love getting comments and things and emails and messages when people spot something in the video. But in this particular case, I did actually see this, and there's a reason why I didn't mention it in the video.

**Dave Jones:** Anyway, let's go. Let's take a look here. Let's go full screen here. Oh, look who we have down here. Oh, shouldn't he use that? He's haunting me. Lewis Rossman, he's haunting me. Look at him. Oh, shouldn't have had the green screen, then I would have covered him up.

**Dave Jones:** Anyway, go and watch Lewis. Let's go, right? So here is the particular thing. I had lots of people comment saying, Dave, did you see this short, this short between two pins up here? Oh, what's the deal with that? There's obviously, you know, this is dodgy design.

**Dave Jones:** Look at the short there. And, yeah, there's a reason. That short is okay. It's actually designed to be there. And I thought, I've mentioned this many times over the years in many videos. I couldn't even point you to it, but I'm sure I have.

**Dave Jones:** And it's actually a common design technique. But I thought, you know, there's always people who just aren't aware of this. They think that it's just a, you know, a manufacturing fault, but it's not. So let's actually call up a higher. There's a photo of this.

**Dave Jones:** This is the 4K screenshot. And sure enough, look in there. You can see that there is a definite solder short between those two pins. So I did actually see this when I was shooting the video, but I didn't really mention it because the video is already going to be long enough.

**Dave Jones:** And I've mentioned it many times over the years. And so why is this not a problem? And why is it a deliberate design short? Well, it has to do when I immediately saw this and I went, oh. It just, that's not a problem.

**Dave Jones:** Because, A, the solder mask expansion. Now, I've done videos on solder mask expansions before, but this video will be going over that again. Okay. You can see that there's no solder mask between pins here. And when you get a short, which just so happens to be practically exactly, I can guarantee it's exactly in the center of these pads as we'll go into like that.

**Dave Jones:** With no solder mask, you know, aha, get 99.9% confident. That short is supposed to be there. So let's find out why. By the way, check out that bodge there. It looks like they, like, lifted, what have they done there? All right, so you can see that this chip is a classic example of having solder mask removed.

**Dave Jones:** You can actually see it like that. It's been removed as one big square, which will, jeez, my five-year-old could follow lines better than that. There we go. That's better. You can see the square solder mask expansion. So you get, that's the green stuff.

**Dave Jones:** You get no solder. There's no solder mask between pins in there. And that can actually potentially cause a problem because when you get your, when you solder this chip, either hand solder it or drag solder it or reflow solder it, however you want to solder this thing, if you get too much solder on there, it can just bridge between pins.

**Dave Jones:** And the smaller the pin pitch gets and these modern newfangled devices these days, you know, less than like 0.5 millimeters pin pitch, this particular one, this Pix 17C756, it's a 0.5. So that starts getting down there. But once you go below that, as we'll see shortly, then, you know, you can really, really come agutsa with shorts between pins.

**Dave Jones:** So it's important to try and have solder mask between pads. But you can't always do this, as we'll discuss shortly about various manufacturer tolerances and pin pitches and solder mask expansion rules and minimum solder mask width rules and manufacturing rules and stuff like that.

**Dave Jones:** So you can't always do it. But anyway. This board dates from about 2000 or something like that. So let's go to a PCB, shall we? I just picked, this is just a random example. I'm using that Circuit Studio here for no particular reason.

**Dave Jones:** And we can actually see that this is, because people will ask, it's a, looks like a four channel piece, RS485 serial interface. There you go. But it has a nice, big quad flat back here, which we can experiment with. And if we go right in here, we're in the

**Dave Jones:** 3D view, in the 2D view here, we can actually go into single mode here. So we can only see the blue top layer and you'll notice there is no solder mask expansion around these pins. And if you're sure enough, if you go into 3D view, you can see that there's no solder mask expansion between pins.

**Dave Jones:** So, oh, look at this. Oh, there's a, you can see the render thing. You can see how the solder mask expansion, this is the white one here, goes big over here and little over here. That's the perspective. That's the perspective. That's the perspective change.

**Dave Jones:** Isn't that nice? I really like that. Anyway, you can see that there is no solder mask expansion around that pad. It is basically, the solder mask does not, solder mask expansion means it expands past the width of the pad. The pad is the copper one there, that gold color, and the blue solder mask, none of that green rubbish this time,

**Dave Jones:** the blue solder mask just does not extend beyond that. And we can actually, I'll show you what it does look like. We can go here to the individual pin. We can specify the solder. We can specify the solder mask expansion value. In this case, you know, you can come from the global rules.

**Dave Jones:** You can do it on a global basis or a chip base, a component basis, or whatever. It depends on your package you're using, or you can do it on a pin-by-pin basis. You can see it's zero, right? But if we set that to 0.1 millimeters, it doesn't sound like much, but it will be.

**Dave Jones:** Watch, whoa, that's heavy. Look at that, you can see how huge the pin, there it is down there, that's the white stuff. That's the fiberglass, right? That's the solder mask expansion, like that, okay? So you can see, even 0.1 millimeters was a huge solder mask expansion, right?

**Dave Jones:** So we can go back in there and go like 0.025, which is, you know, a reasonable, might be a reasonable solder mask expansion value, okay? 3D view, there you go, right? So we can do this actually on, we will do this on a global basis, right?

**Dave Jones:** So let's go into our rules up here. Let's go into our solder mask expansion, it's currently zero, so global, we'll just do 0.025 millimeters, okay? So there we go, let's change that. So we're going down here, 3D view mode, and you'll see that we have, you know, a reasonable

**Dave Jones:** amount of solder mask expansion around the pads, and you can see the tracks, individual tracks coming off the pads there, okay? So you know, we now have solder mask between the pads, and we can actually measure the solder mask in there, too. Between there, there you go, that is actually at 0.1 millimeters, or 4 thou.

**Dave Jones:** In fact, this is a good example of where you can come and get that. And I've done a video on this, but I'll go over here again because it's appropriate. If you use metric for all of your board stuff, which you can do, there's nothing wrong with

**Dave Jones:** that. I'm still, you know, old school, I've been doing this almost practically my whole life, right? As well as professionally. You know, I still use Imperial, thou's, or mils for track and space, but I use metric for board sizes, hole sizes, and for, you know, SMDs, they're all in metric these days

**Dave Jones:** and stuff like that. But I still like doing track and space in thou, just for, you know, old school. But some manufacturers, PCB manufacturers will have, they'll specify imperial, or they'll specify metric, or they'll try and specify both. Right, so let's say the manufacturer specified a minimum solder width of 4 thou, they say,

**Dave Jones:** but we're not going to manufacture it below this value, right? Then if you did all in metric, you know, you're going to be using like 0.1 millimeters. That's fine. That's near enough. 3.937, geez, that's near enough. But no, your manufacturer, especially if you're getting a cheap prototype service, they will

**Dave Jones:** just reject your board automatically because it's less, slightly less, half a bee's dick less than 4 thou. It doesn't matter because you're sharing the panel with, you know, a hundred other customers. They're not going to dick around. If they've got automated software which checks all of their parameters, and if it's under

**Dave Jones:** that 4 thou, you can come a gutter. So there you go. Just be careful with that. I've done a whole video on that. So that's a good example. But anyway, this one should be easily manufacturable, right? And you've got some solder mask expansion.

**Dave Jones:** Now you want some solder mask expansion around the pad like this because the, when they manufacture the board, the copper layer and the solder mask layer, there can be like little. Little alignment issues like that, right? They can be tiny little alignment issues.

**Dave Jones:** And if they happen to be misaligned, which is a normal thing, especially on your low cost boards where they're not, you know, taking a huge amount of care there, you know, there's a reason you get the board for two bucks or five of them for two bucks, right?

**Dave Jones:** Is because it's a really cheap service, right? That you can pay for a more high quality service and they'll take more care in the alignment and the tolerances are better and all that sort of stuff, but you'll really pay for it, right? So on the cheap services.

**Dave Jones:** Then if you've got no solder mask expansion or then your solder mask will cover some of your pad and when it covers some of your pad, then the solder mask, then the paste can be applied on some of the solder mask and then you're going to get little solder balls everywhere

**Dave Jones:** and it can really ruin your day. That's why you should be looking to get, you know, some solder mask expansion always, okay? In fact, some manufacturers say, in fact, we can go over here and we're going to have a look. In fact. JLC here.

**Dave Jones:** Let's go to their solder mask stuff and have a look, right? And they're just a cheap prototype manufacturer and this is their, I believe this is their prototype capability, is it, or is it just the general capability? I don't know. Anyway, they might have different capabilities for their higher cost production panels and

**Dave Jones:** for their cheap prototype service. So just be aware of that. Okay. But in this particular case, they don't actually specify here a solder mask. Right? They don't specify, you know, a solder mask width, right? Or a solder mask slither. It's sometimes called, but it can be inferred here, but look, they actually tell you, you

**Dave Jones:** must have a solder mask opening, a minimum of 0.05 millimeters, right? Around pads. So right there, what we thought was a manufacturable board, you know, you might look at this, oh, that looks reasonable. Right? 0.025 millimeter solder mask expansion, bingo. This would, should, don't be surprised if it gets automatically rejected by JLC in this

**Dave Jones:** case. They go, no, you don't have adequate solder mask expansion on there. So oh, bugger that. You'll have to go back into your rules in here, your global rules. So you know, you've just been rejected. You thought you'd finished your board and you haven't.

**Dave Jones:** You've come a gutter because you're, you forgot to match their actual requirements. So 0.05 millimeters, right? So there's our global rules set to match JLC's requirements. Let's go in here and have a look. Oh, geez. Look at that. That's thin. That's thin as.

**Dave Jones:** Right? We've now got a tiny little solder mask sliver in there, which is what? We can actually measure that. Near enough. We don't have to be exact. We're talking two mil, two thou or 0.05 millimeters, right? So 0.05 millimeters. Does that meet JLC's requirements?

**Dave Jones:** Let's have a look. So they don't actually specify, as I said, a minimum width, but 0.05. So they imply point, you must have a minimum of 0.05 here between copper and copper. And you sold a mask and here they specify minimum copper to copper, right?

**Dave Jones:** So 0.2 millimeters minus 0.2 times 0.05 is 0.1 millimeters. So from this, we can infer that our 0.05 millimeters is going to be acceptable because they didn't actually specify a minimum. And this is quite common, right? They may not actually, some manufacturers will, some won't, they will, some will have

**Dave Jones:** a minimum slither in there. They just don't like it. If it's too thin, they'll reject it. But in this case, it sounds like JLC will just have a go. They don't care, right? If the solder mask doesn't work, it doesn't work. That's your problem.

**Dave Jones:** That's not their problem, right? And when you've got solder mask that thin, it may not like it adhere to the fiberglass or whatever, right? It could just easily peel off or simply, but if you've got your solder paste on this pad here and this pad and this tiny little thin bit of solder mask there.

**Dave Jones:** Yeah, it can easily bridge across. It's almost as if you're having, some solder mask is better than none, but if you have it too thin and your pins are too close together, then you know, the thin solder mask isn't going to help. But anyway, actually don't pause this video now.

**Dave Jones:** I was going to say pause this video, don't because that'll ruin the watch time metrics or whatever, you know, audience engagement metrics. So after this video, go get a PCB with solder mask. It doesn't have to be blue. Either that green rubbish or it can be black.

**Dave Jones:** Anyway, go and try and put some solder onto a solder mask. The whole idea of solder mask, it's, well, its purpose is to prevent a solder mask over bare copper, SMOVC. It prevents oxidization of the copper, but it's one of its primary purposes is to stop

**Dave Jones:** shorts between pins like this. Solder just does not adhere to solder mask. Try and put solder onto a solder mask, it'll just ball up, right? And then it just fall off, you know? It'll pick off because the flux will kind of hold it there, but you know, you can just

**Dave Jones:** like flick it off. No problems whatsoever. It gets everywhere. Only little solder mask balls, pain in the ass. Anyway, so yeah, that's the purpose of having solder mask and that's the purpose of having it between pins is to prevent shorts between this. But anyway, back to the original question, Dave, why is there a deliberate short in here?

**Dave Jones:** I guarantee it's a deliberate short. I'll tell you. Let's go in here. Here we go. It's a pad, right? Pad 22. So let's actually just change that so it's actually ground. It doesn't chuck a wobbly when we try and connect a track to it, okay?

**Dave Jones:** So when we're laying out a board like this, PCB designers, we love to use snap grids. If you're not using a snap grid, you're not a proper PCB designer, okay? Your designs are going to be crap, right? Snap grids, I've done whole videos on that of what, you know, the best snap grid.

**Dave Jones:** You're always changing snap grids when you're doing a layout. You're always changing snap grids when you're doing a layout. Because there's not just one snap grid to rule them all. So we can go like 0.05 millimeters snap grid. So you can see, they're the little dots in there, okay?

**Dave Jones:** So everything's going to snap. So when you're actually routing traces, you want them to snap, and you particularly want them to snap to the center of the pad. You'll notice that when I move my cursor like this down, whoa, look, look, look, it's trying

**Dave Jones:** to drag me. Oh, look, it's dragging it, right? It's automatically snapping to the center of that pad. It wants to be there. And trust me, you want your track to snap to the center of pads. That's how you want to do it. And so a natural thing, if you had two ground points like this, well, you should actually

**Dave Jones:** just connect that up to the ground plane up there, the copper paw, right? But let's say, right, this layout was tight as a nun's nasty. It was just really, you know, so tight that you could not route traces up here, okay? Then there's absolutely nothing wrong with grids.

**Dave Jones:** There's nothing wrong with going, well, in theory, there's nothing wrong with going between pads like that. And that's an age-old tradition of doing that, right? And that's, and that's what the P, I guarantee you, that's what this PCB designer has done here. So if we go to our 3D view, you can see the trace in there.

**Dave Jones:** So let's just change our solder mask expansion back to, what was it, you know, 0.1 millimeters or something like that, right? Something crazy. So that there's no solder mask between pins on there. Bingo. We now have a copper short, a deliberate short between those two pins.

**Dave Jones:** And when you see lack of a solder mask between pins and a short that looks like it's directly in the center like that, then you know, you can almost 99.9% sure that that is going to be a deliberate trace across there. So no worries whatsoever.

**Dave Jones:** This is why I didn't mention it in the video. It's just a common PCB designer thing to do that if you'll run out of room. In this particular case, I will. I will actually criticize the designer because this truck, look, there's a whole area of

**Dave Jones:** room up here, okay? This particular trace could have come up here like this and gone like that and up. Or it could have, you know, simply gone up there like that and across like that, leaving room for this one to come across and drop down here as well as down there.

**Dave Jones:** And I can show you that. So let's assume that we were going to do this on our board here and let's say we had absolutely no room. Okay? But we had no room to route it under the chip here. But we want to route it outside the chip so let's get rid of this polygon, Skonsky, okay?

**Dave Jones:** Then we can actually route our trace on here. We want to drop, that's too thick, okay? We want to, oh, let's, none of that metric rubbish, okay? Let's just say we had a five-thou trace like this, right? You'd go like that, out, and you'd go like that.

**Dave Jones:** Haven't properly set the... The snap grids and some things like that, but there you go, right? And you can see we've automatically got a design rule, online design rule, minimum between pad and track here. So yeah, that's, doesn't matter. But you can see, yeah, so, you know, a proper PCB design, if you can, route the traces out

**Dave Jones:** like that. It just avoids any confusion whatsoever, especially an optical camera inspection system could actually see that. Could actually... It could deliberately flag that up. But of course, it'd be the same on every single board. So you just mask out that error if you're doing an optical camera inspection.

**Dave Jones:** What an optical inspection system, soon as the board comes out of the oven, so it'd go along the conveyor. It doesn't sound like that. But you go along the conveyor belt, it'd come out of the oven, it's still smoking hot, and then it might go into an manual inspection, then it might go into an optical inspection

**Dave Jones:** machine, big camera on top, and specialized software. It takes a high-res photo of the board, and then it just analyzes and looks for things like shorts. But in this case, it'd probably compare it to a reference, so it may not pick that up.

**Dave Jones:** But anyway, it might be intelligent enough to go, "Oh yeah, there's a short in there," and something like that. Or somebody else inspecting the board or somebody in YouTube comments could go, "Oh, there's a short in there. That product's crap." When no, it was actually designed to be that way.

**Dave Jones:** So anyway, the moral of the story is, you know, don't try and do that. But I'm still guilty. Guilty as charged of, you know, just putting between pads, because if you've got solder between your pads, which you should be doing anyway if you can, then it's not a problem.

**Dave Jones:** It's only a problem when you remove the solder mask like that, and you'll notice that if you do it on a pad-per-pad basis, there's, like, it's got these little half moons like that, right? It follows the shape of the pad. But this one over here, although these are square pads, so it's hard to say whether or

**Dave Jones:** not they've done this manually, because, you know, I've seen that done over the years. I've even done it myself on occasion, depending on what. I don't know what package I'm using for or whatever reason. You might actually deliberately put a big square of solder mask like that.

**Dave Jones:** So you could actually manually do that, but generally, you know, you don't want to do manual stuff like that on a board. So on the top solder mask layer there, you could actually go in there and just put manually if you wanted to, like a big square.

**Dave Jones:** There's occasionally reasons that you go in and manually tweak stuff like that, but generally you don't want to. You want to do it on a global basis or an individual component basis. Especially if you've got a critical part, like a BGA or something like that.

**Dave Jones:** You don't want to be using global rules, otherwise you'll come a gutser. So you want to, you know, specifically have that chip have its own local rules just for that chip for solder mask expansion. But anyway, yep, that's all solder mask expansion. So that's all it is.

**Dave Jones:** I know I've waffled on for quite a lot of time, and all this is covered in many, many videos I've done in the past. But that is the reason why you get shorts like that on a board. It's deliberate. In fact, I guarantee it's deliberate.

**Dave Jones:** In fact, I guarantee, so deliberate, I'm now willing to go to the bench or solder, wick the solder up. I bet you there's a copper trace there. Let's go. All right. Here we go. Tigano microscope. Let's zoom in. Oh, there's our short. There it is.

**Dave Jones:** It's all a bit hairy scary, isn't it? It's been in an aircraft for, what, 20 years or something. So just put some flux on there. Because there's never enough flux in the bloody solder wick, because the stuff just dries out, ages, and not like a fine wine, not that I drink wine.

**Dave Jones:** Anyway, let's wick that up. Ta-da. There you go. Needs a good clean. Oh, this actually was, I forgot, this actually was conformal coat too, by the way. Probably why this looks a bit janky. Yeah. Absolutely no doubt that that down in there, see, that is copper, genuine copper.

**Dave Jones:** That is not a short. Well, it's a deliberate short. It's supposed to be there. But as I said, yeah, poor work on the PCB layout. That trace should have gone up there like that, and they should have just went around there, knowing that they were going to have no solder mask expansion in there.

**Dave Jones:** So there you go. I hope you found that video interesting, waffled on a bit. It's been covered before. A lot of people didn't seem to realize. So please, no more comments in future videos when you spot shorts like that. And hopefully you can now recognize them and go, "Oh, yeah, I'm pretty sure that's deliberate."

**Dave Jones:** Although, you know, not always, you know, Murphy can get you, and you think that it's all, you know, just happens to be right in the middle of the pad and there's no solder mask. But that short shouldn't have been there. But yeah, in this particular case, yep, that's a deliberate design thing snapped between

**Dave Jones:** two pads. Absolute classic. So now I've got a video to link to people. And they comment on this in the future because I'm sure we'll see that because I'm still guilty of going between pads like that. But anyway, there you go. I hope you enjoyed the video.

**Dave Jones:** If you did, please give it a big thumbs up. As always, discuss it down below over on the EEVblog forum. And check out my alternative platforms here if you don't particularly like the YouTubes. Catch you next time. I have no idea if this was actually better the second time around.

**Dave Jones:** I think the first time, the first time I shot this, I nailed it. Shoot it again. Dammit.
