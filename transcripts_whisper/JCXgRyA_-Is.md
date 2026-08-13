---
video_id: JCXgRyA_-Is
title: EEVblog #990 - Getting The PCB Manufactured (Nixie PART 5)
url: https://www.youtube.com/watch?v=JCXgRyA_-Is
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 22, "2": 36, "3": 60, "4": 82, "5": 91, "6": 111, "7": 125, "8": 146, "9": 164, "10": 187, "11": 202, "12": 215, "13": 229, "14": 249, "15": 263, "16": 282, "17": 294, "18": 313, "19": 329, "20": 353, "21": 365, "22": 382, "23": 396, "24": 414, "25": 431, "26": 445, "27": 466, "28": 482, "29": 498, "30": 515, "31": 530, "32": 548, "33": 566, "34": 584, "35": 601, "36": 617, "37": 633, "38": 648, "39": 664, "40": 679, "41": 698, "42": 714, "43": 730, "44": 748, "45": 765, "46": 785, "47": 808, "48": 824, "49": 841, "50": 854, "51": 877, "52": 893, "53": 905, "54": 921, "55": 942, "56": 958, "57": 975, "58": 991, "59": 1007, "60": 1018, "61": 1036, "62": 1049, "63": 1062, "64": 1081, "65": 1098, "66": 1114, "67": 1134, "68": 1150, "69": 1163, "70": 1178, "71": 1197, "72": 1213, "73": 1230, "74": 1249, "75": 1267, "76": 1285, "77": 1298, "78": 1315, "79": 1330, "80": 1343, "81": 1360, "82": 1370, "83": 1387, "84": 1408, "85": 1427, "86": 1443, "87": 1463, "88": 1484, "89": 1498, "90": 1515, "91": 1530, "92": 1548, "93": 1564, "94": 1577, "95": 1591, "96": 1604, "97": 1622, "98": 1643, "99": 1660, "100": 1673, "101": 1688, "102": 1705, "103": 1719, "104": 1734, "105": 1753, "106": 1773, "107": 1790, "108": 1814, "109": 1830, "110": 1845, "111": 1860, "112": 1878, "113": 1898, "114": 1910, "115": 1924, "116": 1940, "117": 1958, "118": 1977, "119": 1991, "120": 2009, "121": 2025, "122": 2045, "123": 2060, "124": 2075, "125": 2096, "126": 2111, "127": 2129, "128": 2145, "129": 2164, "130": 2180, "131": 2191, "132": 2208, "133": 2222, "134": 2234, "135": 2251, "136": 2270, "137": 2286, "138": 2304, "139": 2319, "140": 2335, "141": 2350, "142": 2364, "143": 2383, "144": 2400, "145": 2417, "146": 2433, "147": 2448, "148": 2465, "149": 2484, "150": 2501, "151": 2517, "152": 2534}
---

**Dave Jones:** Hi, welcome to part 5 of the MixiTube display project. Part 4, we left off actually doing the routing for the PCB, and so it'll be click here up in the card, up in the top right corner if you haven't watched that. That's like how to go through and actually route and layout a board.

**Dave Jones:** And by the way, there was actually one error in this board which nobody, well only one person found. This error is that my packages here, these SO packages, I actually used the narrow version of these packages and the chip, the 74, what is it?

**Dave Jones:** Sorry, the TPIC6B595 only comes in the wide-bodied package. So, yeah, trap for young players and well, I didn't spot that and goofed it up completely. It would have been okay. If I went and got the board manufactured, it would have been fine because you can actually bend the legs under these chips.

**Dave Jones:** You can actually bend them back under, so turn it into a J-lead package where it comes back under and then solder them down like that as like an old-school, you know, J-leaded package or whatever. So, yeah, because there's not a huge amount of width difference in there.

**Dave Jones:** So, you know, we could have clutched it. It wouldn't have been a showstopper. It wouldn't have been great for production, of course. It would have sucked. You would have fixed it for production. But given that this is a one-off board, you know, it would have been fine.

**Dave Jones:** But anyway, we went through and fixed it. Actually, David went through and fixed it. David 2 is over there. Say hi, David. Hello. He's in the, yes, he's in the same room. And so, but an interesting thing happened, right? So I just gave him the task of going through and changing from a narrow package,

**Dave Jones:** which, you know, the pins were up here somewhere. I could do a side-by-side. But, you know, there was three or four millimeters in it or something like that. So I changed it all, but that changed all the routing and everything. But we haven't got, like, all our machines set up and all our libraries set up and everything yet.

**Dave Jones:** So I sent him the project files and everything else, and he edited it on his version of Outium, and it actually swapped. You'll notice that I used SMD resistors before, but now it's got these through-hole resistors in here. And Dave didn't know that I, because he hadn't seen my video, so he didn't know that I used SMD.

**Dave Jones:** And he just assumed, as you would, that the PCB package is right. And it somehow swapped all of the SMD resistors to through-hole. And these ones on the bottom I've had to change back manually, by the way. So what it did is, we believe it changed the...

**Dave Jones:** Well, it definitely added the package reference in here as Axial-04, and it actually deleted, or added an extra Axial-04 in here, and changed them all. And it didn't warn him or anything, it just happened. So he just rerouted it based on that. And he sent the board back to me, and I was a bit confused for a few minutes.

**Dave Jones:** And, like, did I use through-hole resistors before? But no. So we're not sure if that's a bug in Altium or what, not. But anyway, so I've just left them. I've changed the ones on the bottom to through-hole. Sorry, to SMD, but I've left the ones on the top,

**Dave Jones:** just because to change those would require going in and rerouting a whole bunch of stuff. It'd be, like, I just couldn't be bothered. This is just a one-off board. So anyway, so what we're going to do today, sorry for the waffle at the start,

**Dave Jones:** is we're going to actually get this board manufactured. So we've finished our routing, what is the next step to getting it manufactured? So let's go through it. Now, first of all, you'd want to, I probably said this before, but you want to use the 3D view.

**Dave Jones:** And this is where 3D view is fantastic, not for the packages. In fact, you can get rid of the packages, and just look at things like solder mask expansion, for example, in there. Do I have solder mask between all of my pins? You can capture all, you can get this sort of stuff using DRC rules and stuff like that.

**Dave Jones:** But, you know, nothing beats a good visual look at what your board is physically going to look like when you get it manufactured. And that's the great thing about 3D viewing. So yes, whilst all these, you know, 3D models are all great and everything,

**Dave Jones:** you actually want to disable those. So if we go into PCB down here, and PCB window, and then 3D models down here, and actually disable those 3D bodies showing up, and bingo, this is what our blank board is going to look like. This is what it's going to come back from the manufacturer as.

**Dave Jones:** And you can see, you know, that you've got, you know, solder mask between stuff. You can see whether you've got tinted vias or not, which we do have some tinted via. Like this one here is untinted. Oh, look at that. So that's a complete, where was it?

**Dave Jones:** There it is. That's a complete fail. So let's, is it, yeah, it was that one, was it? It wasn't tinted. There we go. Force the tinting on top. I may have covered this in the previous, there you go. And you can see, actually, the holes are, see the holes are tinted there,

**Dave Jones:** which means solder, tinting just means the solder mask goes over the holes, basically. And not always, if you've got really large holes, it obviously, you know, it's difficult to completely cover them. But if they're small enough, then you can do that. We don't care about under the chips because, as I said,

**Dave Jones:** this is going to go into a box which will have, like, just a simple rectangular cutout on here. So anything that looks through here, like this, will be visible. So if you've got, like, components in here, they will be visible. If you've got, you know, traces in there or whatever it is, they will all be visible.

**Dave Jones:** So in this case, that should be all fine and dandy. So you just look for stuff like that, silkscreen over pads and other stuff. You can do all this as DRCs, which we'll find out in a minute. But this is a one-off board.

**Dave Jones:** We simply don't care. Like, you know, there's a dot here, for example, you know, a silkscreen dot for pin one marker of that SOT-223 package there. But, like, we just don't care, right? So you would fuss about this sort of stuff if it was a, you know, a proper production board.

**Dave Jones:** You're doing it for a client or a company or something that's professional and everything else. You'd, you know, you'd go to town. But we don't care. It's a one-off. So what we want to do now is we want to do a DRC, a design rule check.

**Dave Jones:** So we go into design rule check. And I've shown, I'm pretty sure I've shown DRC in the previous video, did I? If not, my apologies. We run our DRC check. And once again, all of the electrical, you can enable and disable all sorts of various stuff in here,

**Dave Jones:** what you want actually checked. The online one, whether or not you do it live or via the batch thing, which is what we're running now. So anyway, let's just assume that we've got all of our settings set up correct, and bingo, this is the ultimate goal before you get a board manufactured,

**Dave Jones:** is to have zero DRC errors. So all your traces are connected. All your connectivity matches all the pins. There's no breaks in any of the tracks. There's no shorts on any of the outputs. I've covered this in previous videos and stuff like that.

**Dave Jones:** And you've got, there's no violations. Like we're checking clearance constraint. Okay, so we've got 0.381 millimeters. What's that in, here we go. If we switch back to Imperial, we're now in Imperial. We're now in Imperial. Look at the bottom right corner there. Bottom left corner, sorry.

**Dave Jones:** And we run our DRC again. Design rule check. Bingo, it should give it to us in mils. There we go. So we've got 15 thou clearance. 15 mil. Mil is the same as thou. 15 thou clearance. We've got no short circuit constraints. We've got no unrouted nets.

**Dave Jones:** We've got width constraints. So we're 10 mil. So we've got 10 mil clearance. 10 mil width. And, you know, we're checking hole-to-hole clearances. All sorts of stuff. We can check a lot more. But we don't care. It's a one-off board. It's looking good.

**Dave Jones:** It's looking good in 3D view mode. The vibe, it's all about the vibe. The vibe's happening. It's all there. So next step to get our board manufactured is Gerbers. I think I spent quite a significant amount of time in the previous video talking about outjobs.

**Dave Jones:** And that's a different way to automate this sort of process. Automate doing DRCs. Automate this board release process, as it's called. You do a DRC, you will do the Gerber file generation, your NC file generation. You might export a bill of materials. You might do all that sort of stuff.

**Dave Jones:** We're not going to go through that. That's like an Altium-specific thing. I want to keep this as generic as possible. So what we want is fabrication outputs here, and we want our Gerber files. We won't do the new Gerber X2. We'll just do the traditional Gerber files.

**Dave Jones:** Inches or millimeters doesn't really matter. Everything's such fine resolution anyway. The manufacturers are just going to handle it. It's not a problem. And the format, 2 to 5 format, it explains down there. 2 to 3 has 1 mil resolution, so you don't want that.

**Dave Jones:** It's okay for a rough board like this, maybe. But 2 to 4 has 0.1 mil resolution, and so 2 to 5. You just want the highest resolution possible, just because, the vibe. So we want to go in here, and we want to plot our various layers.

**Dave Jones:** Okay, so let's, whoop, and these are going to be the filename extensions down here for the ones we want. So what do we want? We want our top overlay because we want the manufacturer to print us the silkscreen overlay. That's the white one there with all the component designators.

**Dave Jones:** We do not want a paste mask because we're not getting this manufactured professionally with a solder mask stencil, a solder paste stencil, so we don't need that. So we want the top solder mask because we're getting, we're basically going to get a standard double-sided

**Dave Jones:** silkscreen solder mask board. So we want to do the solder. We want to do the top layer. We want to do the bottom layer. The bottom solder, no bottom paste, and we want the bottom overlay as well because we're getting this manufactured on a prototype PCB panel,

**Dave Jones:** which generally includes top and bottom overlays or top and bottom silkscreen. If you hear me use the word silkscreen, I refer to overlay and vice versa. It's the same thing. Silkscreen is just an old term for it. No one actually does real silkscreens anymore,

**Dave Jones:** but, you know, it's just a diehard term. And then mechanical layer one. In this case, let's actually, well, I'm sure I showed in the previous video, the board outline as mechanical layer one, as some traces. So we will include that and we'll see it.

**Dave Jones:** So we don't, this is a real simple board. We don't have anything else fancy. So, and we do not want to add the mechanical layers to all of the plots. We just, like, you want to separate it out. There'd only be specific reasons,

**Dave Jones:** manufacturer-specific reasons that you would do that. So they're all the layers we want. Top and bottom, silkscreen, solder mask, and trace. And drill drawings, we're not fussed about any drill drawings. Apertures, we would just embed the apertures in there. We'll just leave it all default.

**Dave Jones:** We're not mucking around here. Now this is a reasonably important one because you have to define the size of the film. I'm just going to, you know, this is a massive size film. What is it? 20,000 mil by 16,000 mil film. The film means the actual board size

**Dave Jones:** on the generated Gerber file. So it's more than big enough for any size board that you might want. But the reference is important. So the position of your board on the film, we want the reference to be relative to this origin down here,

**Dave Jones:** which is this origin zero marker that we set. So it basically sets it smack in the middle and then, like, in the middle of our film. That's, well, you've got a center on film option, but reference to relative option, relative origin, is just fine.

**Dave Jones:** So separate file per layer, everything optimized, changed, just all default stuff. We don't want to muck around with anything here. Suppress leading zeros, don't worry about that. It's all default, and we go, okay. That's it. It's generated. You saw it down the bottom.

**Dave Jones:** Bingo. All of our Gerber files have been generated, and it generates a Camtastic file, .cam over here. This is an Altium thing. I think Altium bought Camtastic or something donkeys years ago. And this is now not our PCB file anymore. This is actually a composite view

**Dave Jones:** of all of our Gerber layers superimposed one on top of the other, and we can view individual files down here. So we can go Camtastic documents, and here's our individual layers because Altium has a built-in Gerber viewer, basically, and it works okay. Good enough for just viewing.

**Dave Jones:** It's not the best thing in the world. There are better third-party Gerber viewer programs, but anyway, this allows us to simply go in there and look at the individual layers. So now we can see that's our bottom, and you see how it actually has no border

**Dave Jones:** and where the origin is here. So that origin is important. Otherwise, if we said center on film, the origin would be way down in the other corner or whatever. Oh, that was a bit of a display bug there. Oh, look at that. Display bug.

**Dave Jones:** Oops. I don't know if my screen capture is interfering with that or not, but I can certainly see that, and you notice how we didn't have that option to add the board outline. We simply don't need it, okay? So that's GBL. So that's BL is bottom layer.

**Dave Jones:** So GBL stands for Gerber bottom layer. That's sort of like an industry standard file, you know, naming convention, extension convention. There's our bottom silkscreen, our bottom overlay. BO stands for bottom overlay, and BS does not stand for what you think it might. It stands for Gerber bottom solder mask.

**Dave Jones:** So that's our solder mask expansion on the bottom, and this is our mechanical layer, as I said, because I manually put those traces. Oh, have I left a gap up there? Do you see that? Left a gap up there. It doesn't matter. They're going to know what it is.

**Dave Jones:** They're going to know that that's my board outline, and I've just gooped it. It's going to make no difference to them, so I wouldn't even bother fixing that. Maybe if it was a professional, you know, thing and a real complex board, I might fix that,

**Dave Jones:** but obviously this is just a plain square board. That's really all they need to know. And there's our top layer traces, so it all looks nice and clean. It all looks like it's generated nicely. Our top overlay. Yep, there it all is. And our top solder mask.

**Dave Jones:** So it all looks hunky-dory. Happy as Larry. So we're almost done. We've generated our Gerber files, but the Gerber files are just the film files that generate the masks that manufacture the board, but that doesn't have any information to do with actually drilling the board,

**Dave Jones:** so we have to generate NC drill files, they're called. So if we go to fabrication outputs again, we go NC drill files, and once again, you can automate all this, so, you know, it's a single, almost practically a single click to do all sorts of stuff,

**Dave Jones:** generating Gerbers, NC drill files, bill of materials, and DRCs, and all sorts of stuff, if you want. But, yeah, once again, we're going to do the inches thing, 25 here, suppress trailing zeros, reference relative to origin. You want to make sure that matches your one before,

**Dave Jones:** otherwise they're going to be, they will not line up. When it imports into their CAM software, both the NC drill file and the Gerbers, they've got special CAM software. They do not use Altium, by the way. If you think the manufacturers will import your Gerber files into Altium

**Dave Jones:** and then print them, that's not how it works. They've got special CAM software that handles all this stuff. The origin's not the same, nothing will line up. I mean, they probably wouldn't be silly enough to just go and press manufacture, right, and do it, but they'd have to manually fix it,

**Dave Jones:** and they'll probably charge you for that, or they'd come back and tell you, or something like that. They should come back and tell you, hey, you don't know what you're doing, you know, in a nice about way, and your origins don't match up.

**Dave Jones:** But the problem with PCB manufacturers is they often will not tell you anything. They will just fix stuff. So you could be sending them boards for years in the wrong format, you know, and they will just fix, you know, things. A lot of them are not good at telling you that,

**Dave Jones:** hey, you know, this isn't the best way to do it, here's what you should do. Which is good in that you'll most often get working boards back, but yeah, you know, they don't like to help you out in any way in that respect.

**Dave Jones:** Which I, it's not a great thing, because that doesn't help them out, it's just extra work for them to do. But I guess they just secretly charge you for it. Anyway, reference relative to origin. Same as before, optimize, we don't want any of this,

**Dave Jones:** generate separate for drill files for plated and non-plated holes, we're not fussy about that. This time, use drilled slot commands, we're not fussy about that. We've got no slots or anything, we're just going to go, bog standard, thank you very much. Import drill data, just leave all this standard,

**Dave Jones:** we won't change any of this sort of stuff. And bingo, there is our, once again, it's generated a CAMtastic file. Once again, the origin is over here, so if you merge those two CAMtastic documents that all overlay and everything else. So here is the actual file.

**Dave Jones:** So, we've generated our Gerbers, and we've generated our NC drill files. We're ready to go to the manufacturer. Woo-hoo! All right, so we have generated our files, they're going to be in this sub-directory here, project outputs, and here are all the wonderful files that we've got,

**Dave Jones:** all our Gerber files. Now, it's generated a few additional files, which we don't necessarily need to send to the manufacturer. Like, I don't think we had any slots in here, right? So, were there any slots? It says there's the odd slot. Oh, yes, yes, yes, we do have slots, sorry.

**Dave Jones:** The DC jack over here, the 12-volt DC jack is done with a slot. They're the NC drill file commands for actually drilling those slots. Use this drill size, put it in there, move it X millimeters in this direction, etc. And then we've got the round holes,

**Dave Jones:** these are most of our holes in here. So, once again, it comes, if you want to know the format here, it's got, like, T1 stands for Tool 1. So, this is the tool. These are plated files. I shouldn't be going through the format.

**Dave Jones:** And this is the N, N in inches. We probably should have done this, actually, we should have done our NC drill file in millimeters. Shouldn't we have, David? Yes, David's nodding in the background. Let's do it again, in millimeters. And the reason we're going to redo it,

**Dave Jones:** like, we don't have to. This is just purely for our entertainment purposes, really. So, let's, oh, I wasn't, David's laughing in the background there. Export. NC drill, he's a big fan boy of everything metric. NC drill files, again, let's try that again in millimeters,

**Dave Jones:** just so it's easier for us to read. And, technically, they do use millimeter drill bits these days. Every, you know, .05 millimeter increments, or they'll have a whole stack of, on the machine, in, like, 0.05 millimeters, or whatever it is, and they will increment those.

**Dave Jones:** So, they would have just, like, their software would have automatically handled that and converted the Imperial to the nearest metric drill. It would have been, you know, would have been fine. But, just for kicks, just for kicks, we will redo that, and we'll go back to our file over here,

**Dave Jones:** and round holes, we are now metric. Thank you very much. Plated holes, 0.6 millimeters, that'd be the vias, 0.85, 0.9. And, once again, you get charged for these, what are called tool changes. So, you actually want to minimize these. So, if you're doing a real complex board,

**Dave Jones:** and you're importing libraries from everywhere, and they might have subtly different drill sizes, you know, one might be 0.8 instead of 0.85, and you might, like, if you've got a real hotchpotch design, getting parts from libraries from everywhere, you might end up with, like, 20 different drill hole sizes.

**Dave Jones:** So, you want to consolidate those. That would often be a step, which I didn't cover here, you would for a professional board, that you're getting especially high volume manufactured, you know, when it's a big deal. This prototype doesn't matter a rat's bum. But, you know, you don't want to have 20 tool sizes,

**Dave Jones:** because that'll slow down your board, they won't be able to produce as many, they won't be able to produce them as fast enough, they'll charge you for that extra machine time when it's got to go in and change the tool from the 0.85 to the 0.80.

**Dave Jones:** You know, so often, hole size consolidation is another entire step in the process, which we didn't do here. But just be aware of that. And then you've got non-plated holes, 4 millimeters, that'd be the big mounting holes in the corners here. And there's, so then they go tool 1, there it is,

**Dave Jones:** and here's all the commands, the NC drill file commands, moving X direction, blah, blah, blah, blah, blah, etc. And that's all the file is. But you don't need to know that. I just showed you that because. Okay, some other files in here which you don't have to send to the manufacturer,

**Dave Jones:** for example, this DRR, that's a drill report file. So if we open that, it can give you some valuable information, you know, here's the tools, that's stuff I said before, number of hole counts and all that sort of jazz, and total tool travel,

**Dave Jones:** that determines how long it's going to take them to actually drill this board, because it takes time for the NC drill machine to move from one spot to the next, so the tool travel time in distances can matter, and stuff like that. So, you know, we don't have to include those files,

**Dave Jones:** it doesn't matter at all. So in the zip, generally you just want to zip them all up, so what we want to do, the aperture file, I don't think you have to include that these days, but I just do as a matter of course,

**Dave Jones:** and I also include the DRR, just because they might want to see it, it might be nice for them. We don't need external rep file, but we need all our Gerbers, but just include everything, why not? Simulation netlist, we don't need that, so we might actually leave that out.

**Dave Jones:** So we'll highlight all those, and we need our, of course, our text files. Once again, I'm pretty sure they don't need the aperture library and stuff like that, but just send it. Just send them everything. It doesn't really matter. So they'll just ignore the ones,

**Dave Jones:** so we will zip that up, project outputs, zip. Thank you very much. There it is, and we're ready to send our zip file off to the manufacturer. Beauty. Now, just before we actually go to some PCB manufacturers and get quotes and things, online quotes,

**Dave Jones:** just a quick word about board size here. Now people these days just expect, you know, prototype boards, you know, dirt cheap PCBs or Oshpark or something like that, you know, it's not going to be $5 or $10. Why? Because look at the board information.

**Dave Jones:** It's about the size. Sorry, go to millimeters. Board sizes, yeah, okay, board information. It is 185 millimeters by 69 millimeters. Now that's not a huge board by any stretch of the imagination, but it's much bigger than the average person's doing a little Arduino shield these days,

**Dave Jones:** and they're so used to buying these cheap boards, right? 185 by 69, that's about 20 square inches, right? In the old money, right? So, and let's go to Oshpark, for example. You pay $5 per square inch for its standard two-layer board. Yeah, you get three copies of your board.

**Dave Jones:** I don't need three copies, right? But, hey, that's $100, right? It's not a $5, $10 board, because you pay, when you're taking up a large part of a prototype panel or surface area, they're going to charge you for it, like a wounded bull.

**Dave Jones:** So, yeah. Don't go wildly down in the comments, oh, you can get it for $10 here, no, you can't. Okay? The board is bigger than your average shield. Now, I may not actually use Oshpark to get it manufactured, in fact, one of the PCB manufacturers we'll see later

**Dave Jones:** actually gave me a half-price coupon, so I might just use their service just because they gave me a coupon. I'm a tight ass, right? But, hey, let's try Oshpark, um, because I've never actually gone through and done a full thing with them. I may not get it ordered,

**Dave Jones:** but let's just, you know, select the files on the computer. Can we drag and drop? Oh, we've got to select. Can't drag and drop. I want to drag and drop. Bugger. No. Brr. Now, here's one thing, like Oshpark, and pretty much, oh, you saw it there before,

**Dave Jones:** they actually accept Eagle board files and, uh, KiCad files directly as well. I don't recommend you do that, um, like, any decent PCB manufacturer will accept Altium files directly, so the Altium dot, you know, PCB file, or whatever it is, right? You could,

**Dave Jones:** technically you could just send them that PCB file, and they will get your board made. Um, you know, they may not question it at all, but it's, it's not the most, uh, controlled way to do it. Um, so the reason that you generate Gerbers and do everything else

**Dave Jones:** is that you can check everything, and, you know, you can manually know what you see is what you're going to get with, uh, Gerbers and the NC drill files and everything else. So, I highly recommend learning how to do, generate Gerbers and doing it that way,

**Dave Jones:** and don't, not just lazily upload your Eagle board file. If you're doing a one-off, okay, you know, it, it might work just fine, but, you know, if you want to do anything semi-professionally, and you want to control the process, Gerber files is the way to do it.

**Dave Jones:** That's how all your professionals, uh, do it. So two-layer board of 7.29 inches, by 2.7 inches. It looks like it all works in, uh, as an Altium zip file. There you go. It's automatically recognized it. Detected unsupported drilled slots. There you go. Don't they support,

**Dave Jones:** doesn't Oshpark support slots? Uh, your project contained two drill files. We've merged them. Um, maybe that was the issue. Ah, now, something's gone horribly wrong here. Um, it does not like this. Look at this. Our drill file, our board bottom, it has not expanded that

**Dave Jones:** to scale. So I don't know. It's, it is not working. Top layer's worked just fine and dandy. The GTL file, the Gerber top layer, bottom layer looks spectacular. That's all lined up. It's all, everything's hunky-dory. Solder masks are all good. The board outline,

**Dave Jones:** there it is, GM1. It's, it knows it's a board outline. Pretty industry standard method of doing it, so I guess they know that, that, you know, you use one of the mechanical layers as just a board outline. It's detected that. So that's really quite groovy,

**Dave Jones:** but, I'm a bit concerned about the drill. That's not going to work. Um, so we might have to fix that. That's not what this video's going to be about because I don't intend to use OSPARK anyway. Ah, they're not hugely quick. Um, they're not hugely cheap

**Dave Jones:** for a big board like this. I'm, let's go look at some others. But, yeah, normally that should have worked. So, maybe there's a bug somewhere where I didn't, ah, use something that wasn't, ah, compatible. Ah, they actually tell you. There you go. Um,

**Dave Jones:** absolute coordinates. Um, oh, they wanted absolute. They wanted absolute and not the origin. Let me see if I can fix this, just out of curiosity. Okay, I'd love to show you OSPARK working, but I re-uploaded, ah, by removing the, you know, trailing zeros and 4,

**Dave Jones:** 3, and the whatnot using the, ah, absolute origin, but it just hasn't worked. So, I'm not happy with that. Um, I'm just gonna, yeah, assume that there's some quirky little thing happening, and we'll move on. Okay, I think I officially give up. I went to the effort to generate,

**Dave Jones:** re-generate all the Gerbers, in absolute origin, using imperial, 4, 3, like the whole, like to match the NC drill files, and it does not work. So, maybe it's the merge, the merge of the two files. Ah, it didn't like that, or something, and it's like,

**Dave Jones:** nah, it doesn't work, even following their, sort of, ah, instructions there. Now, because all, ah, like PCB manufacturers are always chopping and changing who's the best, who's the cheapest, who's the fastest, who's the best quality, blah, blah, blah, you know, you can't keep up these days.

**Dave Jones:** More PCB prototype manufacturers, and you poke a crow probe at. It's unbelievable. Anyway, so I'm gonna use like, um, a PCB shopper, um, service. I've never used it in, um, a lot of different, actually, in these ones. 25 different PCB manufacturers, PCBWay, Seed Studio,

**Dave Jones:** Shenzhen thing, Osh Park as well, ah, Breadboard Killer, which is an Australian, ah, one, dirty PCBs, dirty, cheap, um, reminds me of Akadaka. Dirty deeds, done dirt cheap. Dirty PCBs, done dirt cheap. Anyway, Thunderstruck. Yeah, um, so, let's go in. Sorry, 69 millimeters,

**Dave Jones:** ah, two layers, least expensive color, we're just not fussy, it's just a prototype thing, we don't care. Ah, only, we can do both, but, you know, really we only need top, you know, I'm a tight ass, right? So we don't need that bottom silk screen,

**Dave Jones:** it's rubbish. In fact, we don't even need the top silk screen, really, but, you know, you're probably gonna get it for free, whatever, because it's on a prototype panel. Um, surface finish cheapest, one point, standard 1.6 millimeter thickness, standard one ounce copper, none of that thicker rubbish,

**Dave Jones:** ah, 10 mil trace and space, we've got a very coarse board here, no fine tolerances, so it's gonna, anyone can make this. You can make this at home, with your own, ah, laser printed transparent overlays. I can do, like, 8.8 at home, easy,

**Dave Jones:** even down to 6.6 sometimes at home. Um, I've done way in my deep, ah, dark past, um, double sided even. Um, anyway, 10 mil, so, ah, cause that will have an impact on your price. The, what services are available, to do your minimum trace and space.

**Dave Jones:** So, ah, 10 is plenty, minimum drill size, no 0.6 millimeters, you can select either. I think our one was 0.6 millimeter, smallest via, no gold fingers, ah, no stencil, ah, cause we're not, stencil's the, ah, SMD, ah, stencil. A lot of you, a lot of them will include,

**Dave Jones:** like a free Mylar, so, a few of your higher priced ones, might give you a free stainless steel, ah, stencil, or something like that, which is nice if you want it. Um, certainly if you're doing a board, you know, and you're going to reflow oven it,

**Dave Jones:** yeah, you throw in a stencil please. Quality certifications, don't want any of that rubbish. Ah, number of designs, one, quantity one, Australia. And default time, you can set the number of business. Let's go default, let's get prices. This is what we want to see.

**Dave Jones:** Here we go, here we go, this is really, this is quite jazzy. You know, look, it's going to cost, for five boards, okay, there you go, 712, that's pretty good, that's pretty cheap from Seed, isn't it? Wow, have I got the right dimensions?

**Dave Jones:** Even, nine days. Oh, sorry, Easy ADA's beat them, has it? Is it sorted by, ah, cheapness? Wow, look at this, I like this service, this is really quite, and it jumped, link to jump to the order page as well, great. 43 days, total boards plus shipping,

**Dave Jones:** that's pretty good actually, 56 bucks, that's pretty cheap, from Easy EDA, in China, wow, green, you know, standard green solder mask or whatever, but that's, that's pretty jazzy. Seed Studios also, you know, punching above their weight there at 68 bucks, all PCB, PCBWay,

**Dave Jones:** a lot of people are talking about PCBWay at the moment, they've got a good process that follows, you can, I think that's PCBWay, you follow step by step through the production process, which is quite good, I can't remember which one I've got the half price coupon from,

**Dave Jones:** might be them, anyway, DHL, including DHL posting, so the board itself is okay, well you can get it for 17 total actually, but then the shipping of course, shipping costs more than the boards do, so that's actually, I'm very surprised at that, for a board of this size,

**Dave Jones:** that is quite surprising. So you can see this is a really good tool to, look, dirty PCBs, a lot of people say they're cheap as well, not for a board of, you know, 185 millimetres width for example, it's not very high, it's only like 69 millimetres high,

**Dave Jones:** which isn't much, but that width adds, PCBCart, I've been using PCBCart for like a decade or something, they were one of the cheapest pioneering companies, in terms of shared panel service, when PCBCart originally came out, that was pretty groundbreaking, and Breadboard Killer here in Australia,

**Dave Jones:** they don't make them here in Australia, they just subcontract out, so you know, even that's like 12 days delivery, so once again, you've got a PCB zone in New Zealand, hi Richard, so there, you know, then we start getting into the $100 region,

**Dave Jones:** but the quality of their boards is really good, and five days, right, so that's, you know, that's pretty quick, so you know, you compare that to, well we can have it nine days up here, total days for those, so you know, these cheap ones,

**Dave Jones:** yeah, you know, eight, nine days, and that'd be working days too, probably, I know that PCBCart are, they're usually specified working days, so anyway, PCB with a five day lead time, and, of course, if you want, that's why, I was probably, I was basing,

**Dave Jones:** let's say we want it in four days, right, let's go do that again, let's go do, you know, we're in a hurry, we want our board, dammit, and now you'll see it be much more pricey, you know, so if you're happy to wait,

**Dave Jones:** there you go, PCBZone in New Zealand is going to be the cheapest so far, at $155, including DHL, so you're going to get that puppy in three days, and $131, that's not much to, like when I was a boy, right, you know, that was unheard of,

**Dave Jones:** to get a prototype board for $130, it was like, you know, $700, $800, $500 for a new, you know, whiz bang, cheap service, because you pay for the whole panel, but now they've got, everyone's doing these shared panel services, and that's, you know,

**Dave Jones:** awesome price for three lead, three days lead time, so there you go, New Zealand, who knew, right, PCB, everyone thinks, oh, China's the cheapest, eh, you know, four business days, maybe if we get five, because five is a more, sort of, standard, ah,

**Dave Jones:** fast process time, I think we'll have a few more choices here, this, this works great, it's just sucking the data from all these PCBs, no, no, it's alright, it's got a few more, few more, but once again, PCB Zone is winning, oh, so actually,

**Dave Jones:** there must be a quirk in this, because the other companies offer it, so why it's not, they do offer such a service, so why they're not showing up, I don't know, because if you go into PCB Card, or PCB Way, or anyone like that,

**Dave Jones:** if you go into their website directly, they will give you an option, ah, for, you know, really fast turnaround boards, so, yeah, I don't think this is complete, I would not take this as, ah, gospel, so yeah, here's an example of that, if I go over to PCB Way,

**Dave Jones:** for example, ah, whoop, they're closing now for two days holidays, too bad if you want to get your boards made, ah, like, as in, ah, I'm going to have to go out for another day also, ah, beware Chinese New Year, ah, two to three days,

**Dave Jones:** look at this, so I've put in like all my, you know, 185 by 69, I only, with different designs on panel one, and they're, they're going to give me five boards as the minimum you can get made, ah, and they're going to do that for 32 bucks,

**Dave Jones:** with two to three days turn, ah, but of course, ah, you know, once you choose DHL to Australia, ah, that's still pretty good, 57 US dollars, for three to five, that's, see, that's really good, we didn't get that option, over in PCB, ah,

**Dave Jones:** PCBWay, here it is, 114 bucks, with six days, so, there's something, going on there, something's not right, the website is, sorry, PCBShopper has, ah, failed us, I'm afraid, and check this out, express 24 hours, 55 US bucks, for five boards, you've got to be kidding me,

**Dave Jones:** David thinks it's, David, David, David, David thinks it's, David thinks they're lying, why do you think they're lying David? It's crazy fast, It's crazy fast, isn't it, for that price, that's just insane, how big must their facility be, to have a spare line,

**Dave Jones:** for you, to bump everything out, like, you know, how quick are they replying with emails, ah, that's just, that's nuts, 24 hours turn, I don't know, they have the boards quicker, than my digi key parts, almost, wow, that's crazy, I don't know, wow,

**Dave Jones:** tempted to try, tempted to try, okay, I'm on the, Elecro website, they actually offered me, a 50% discount, ah, coupon, they have a ridiculous, array of options here, I just wanted to show you this, like this is a, five pieces, two layer PCB,

**Dave Jones:** it seems, expensive, in quote marks, but this is a rush, 12 hour job, ah, rush 12, well, shipped in two working days, ah, so whether or not, they actually manufacture it, in 12 hours, but it takes them, two days to ship it, I don't,

**Dave Jones:** or is that include shipping, I'm not, not sure, but it's just, crazy, and if you go back here, like, look they have like, a four layer, piece, you can get like a hundred, pieces, of a four layer board, ah, I haven't costed this out,

**Dave Jones:** on other sites, so it may actually be, a similar price or cheaper, but five centimetres, by five centimetres, okay, but what if you wanted, like, five centimetres, by 30 centimetres, it's only 369 bucks, for a four layer board, with all the bells, and whistles,

**Dave Jones:** right, well, no, it doesn't, okay, gold is 16 bucks, okay, wow, whoop-dee-doo, for a hundred pieces, of a four layer board, like, what world are we living in, this is insanely cheap, right, so I'm looking at the, ah, five pieces, two layer PCB here,

**Dave Jones:** I've got to choose, the 10 centimetre, by 20 centimetre max, because I'm 185, by 69, so it's not, it's not nearly optimised, you've got, ah, jumps up there, but red, red, ah, ah, solder mask goes faster, everyone knows that, so I'll choose the red,

**Dave Jones:** we don't want, ah, 12 bucks for our gold, um, but check this out, stencil, stencil, with a frame, I'm gonna, like, this must be a stainless steel stencil, right, because you only get stainless steel stencils in frames, um, well, they, the only ones that come with,

**Dave Jones:** frame option, they come in a pretty decent size, for 18 bucks, 18 dollars, a lousy, it's practically free, when I was a boy, like, a 500 buck, stainless steel stencil, was cheap as, right, this is, like, we're living in a world, where things are practically free,

**Dave Jones:** and people take it for granted, unbelievable, so anyway, I can, rush 12 hour, ah, man, it's just, ah, wouldn't want to go back to the old days, that's for sure, when I was a boy, I, okay, I won't bore you with the process of,

**Dave Jones:** ordering that board, through, ah, Elecro, but I did, um, it'll come in, well, it'll be manufactured in like, two to three days, or something, they gave me, very kindly gave me a discount, ah, code, so it was a bit cheaper than PCBWay, and,

**Dave Jones:** ah, anyway, not sure what happened to the Oshpark one there, but no shortage, of, um, services, these days to, manufacture your boards, it's just crazy, has grown up in a world, where, he has not had, a, ah, low-cost PCB manufacturing, service, so, yep,

**Dave Jones:** crazy, anyway, when I was a boy, ah, we didn't have these low-cost PCBs, so, there you go, um, that's just a, a quick walkthrough, this is not, wasn't designed to be a tutorial, otherwise it would have been, ah, a bit more, ah, concise,

**Dave Jones:** than this, it's just me waffling on, getting this board made, so, ah, in the next part of the video, we'll, we'll get the board in, I'll order the parts from Digikey, or wherever, and, ah, because the, ah, driver, chip has to come specifically from Digikey,

**Dave Jones:** or Mouser, or someone like that, you can't get it, um, here in Australia, so, we'll get the parts in, we'll assemble it, and, um, we'll get it working, and I'll show you the, final product, anyway, hope you enjoyed it, if you did, please,

**Dave Jones:** like, comment, and, subscribe, and, leave a comment, and, I'll see you in, the next one, bye, bye, bye, bye, bye, bye, bye, bye, bye, bye, bye, bye, bye, bye, bye, bye, bye, bye, bye,
