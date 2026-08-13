---
video_id: bMFNk9af1qA
title: EEVBlog #736 - World's First IR Thermal Camera Watch
url: https://www.youtube.com/watch?v=bMFNk9af1qA
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 33, "3": 49, "4": 73, "5": 89, "6": 109, "7": 129, "8": 145, "9": 162, "10": 182, "11": 198, "12": 210, "13": 230, "14": 246, "15": 262, "16": 283, "17": 299, "18": 315, "19": 331, "20": 347, "21": 363, "22": 379, "23": 396, "24": 412, "25": 428, "26": 444, "27": 456, "28": 472, "29": 488, "30": 504, "31": 525, "32": 537, "33": 553, "34": 577, "35": 589, "36": 614, "37": 630, "38": 646, "39": 663, "40": 679, "41": 695, "42": 711, "43": 727, "44": 744, "45": 756, "46": 772, "47": 784, "48": 800, "49": 821, "50": 837, "51": 849, "52": 873, "53": 894, "54": 918, "55": 938, "56": 954, "57": 971, "58": 983}
---

**Dave Jones:** Hi. In a video some time back you saw me do a teardown of this FLIR TG165 thermal imaging camera, one of those cheaper gun-type cameras, and I kind of sort of destroyed it getting it apart because, well, I didn't know how to take it apart

**Dave Jones:** properly and it was destroyed in the process. But all of the guts still worked out of it. Like the, you know, the lepton sensor and the LCD and the board and everything else, and it was pretty much gone. So I thought, well, what can I do with the guts

**Dave Jones:** out of it? I've got to do something cool. I know! How about the world's first thermal camera watch? Yeah! Let's check it out. Beauty. And here it is. Check it out. And that's Dave too there. Show us your moves, Dave. Yeah. Show us some John Travolta.

**Dave Jones:** Saturday Night Fever. Come on. Nah. I think he's too young for that. He's got no idea. But there you go. That's the world's first thermal imaging watch. Awesome! So here it is. Uses all the guts out of the FLIR TG165 and including the lepton sensor there in the front.

**Dave Jones:** Please excuse the crudity of this 3D printed model here, it's not actually stuck together, because I'm going to show you the insides in a minute, so it would look better. This is our first shot at printing a 3D case for it. We got it first go, and we'll show you some

**Dave Jones:** of that in a minute. But yeah, it uses the existing board, there's our charging thing, micro SD card there for storing photos on. Uses the original keypad here to turn off and on. We don't have any silk screen on there yet. And the lepton sensor in the front.

**Dave Jones:** And there you go. In a 3D printed case. The world's first thermal imaging camera watch. Awesome! So as you can see, we've got the lepton sensor sitting in there. It doesn't have the original germanium lens from the thing, but it seems to work, you know, reasonably

**Dave Jones:** well without it. It's got the shutter on top, this lepton sensor is, it comes with an optional shutter. And you might see that click there, maybe it might try and compensate itself every now and then. A little micro shutter comes across in there, it might have fallen off actually.

**Dave Jones:** It's a bit how you do it at the moment, this whole thing. But it's definitely a proof of concept. So let's take a squiz inside this thing, and I'll show you what we've done here. There you go, we bodged in a little flat lithium battery there.

**Dave Jones:** It's going to get decent life, but we haven't measured the power consumption. The original one of course used an 18650 battery, this one isn't the same capacity as an 18650, but you know, it's going to get like half an hour of use, or maybe even an hour or something like that.

**Dave Jones:** I don't know, we've got our lepton sensor down the bottom in there, which fits on that part of the case. The watch strap is just a you can see at the moment we just bodged in a earbud thing. What are they called? A q-tip or something, right?

**Dave Jones:** Whatever you call them in your country. So we just put those in there, stuck it in, you know, because we need the 3D printer separate thing to hold that watch band in. So there's our 600 milliamp hour battery, it's like 20c, it's a real high discharge one,

**Dave Jones:** you know, designed for little model aircraft and things like that, but we're only using it at a much lower discharge level than that. And if we whip that off there, you can see that we've actually removed the original board connector here, which went off to the 18650 battery, that just used a

**Dave Jones:** 2-pin header, but that was like too high. So we just decided to get extra low profile, disconnect that, solder wires directly in. Now this original button here for the photo button, it was straight on the board like that, so you press from the top.

**Dave Jones:** But of course we couldn't press from the top, we didn't want that, so we just bodged in a new one in here, and made it right angle like that, so we can just have it sticking outside the case, so that we can just press that and save

**Dave Jones:** images to our micro SD card over here. But apart from that, it's basically exactly the same board. We didn't really have to cut anything off here, we designed the case to like fit and then hold it in here like this. You'll see the 3D model shortly, but that was designed to just

**Dave Jones:** hold that existing board in place like that. And then if we lift the whole board out here, it was designed to be press fit. There we go, you can see that the LCD is still attached to the base of it as it originally was, that's actually

**Dave Jones:** taped down to the board like that. We've got our original tactile dome switches on here, and this originally had this rubber membrane keypad on top to actually press those buttons, but that was too thick and it had protruded from the case and it would look ugly.

**Dave Jones:** So what we did is just 3D print some buttons that just went, look, they just went straight through the case like that. We've got four little buttons in there, so that's really quite neat. They do work, it's not the best solution, maybe the little

**Dave Jones:** plungers could have been longer on them, but yeah, they do work, and we got all this on the first go, on the first print. So there you go. This piece on top here, as you'll see in the 3D model in a minute, is a separate one, and that's just taped down at the moment.

**Dave Jones:** We didn't want to glue that, so it's just a separate piece that was printed and then taped down to the top. And of course we could have printed this all as like one big part, but then we wanted like a nice, you know, shiny surface on here.

**Dave Jones:** There's multiple ways to do this. No, we haven't acetone finished this or anything. It is printed with ABS plastic, this particular one. We didn't use the PLA material print on the MakerBot replicator, which you'll see in a minute. I've got some footage of

**Dave Jones:** making that, but yeah, so we just printed that as a second part and then just stuck that on. But yeah, otherwise, you can see that this flat surface, we actually printed that face down like that, so it got a nice surface. And the buttons and everything were, you know,

**Dave Jones:** just made more sense to actually design it and print it that way than just a, you know, one part with this big protruding thing and all that. That would have been a little bit messy to print. Now as far as the Lepton sensor board goes, this one's actually taped

**Dave Jones:** in there, so I have to be very careful taking that out. In fact, I might not be able to get that out. But you'll notice that this board has been chopped right along here. It originally was, you know, a fair bit longer than this, and it would have been like too high, but

**Dave Jones:** thankfully the layout person who designed this board sort of just kept all the traces, as you would, kept the traces short. It didn't like extend them right out here like this, so we could actually just shear that off. We just missed a via

**Dave Jones:** or a trace down in there. Just shear it off, and then not have to repair any of the traces. Although if a trace did go out there, we could have repaired it, put in a little mod wire to do that, but we didn't have to.

**Dave Jones:** So the board was physically longer in the other one, just because of, you know, how, like mounting purposes and things like that in the TG165 case. So we just chopped that off, and got a minimum height in there. Of course it has to be

**Dave Jones:** in the correct orientation as well to use the thing on the wrist and then, you know, show up. There's only one orientation it can go in. Now this nice case that you see here, I lack the 3D CAD skills to do this. So this was

**Dave Jones:** done by Dave too, who's quite good at 3D modelling in SOLIDWORKS. This was like, I originally just did a prototype to try and fit this. So this is one that I designed and printed out before Dave come along, and that's why this video's taken too long.

**Dave Jones:** And I was originally going to have like the buttons in there and things like that. And yeah, anyway, that was just a first shot at it to fit things in. Not nearly as nice as this nicely moulded and 3D modelled package. And yes, it was all done in

**Dave Jones:** scale and modelled in SOLIDWORKS, and Dave even modelled the PCBs and the screens and the buttons and where they were going to go and everything, so he knew it was going to fit in here before we actually printed it. And sure enough, it fitted like a glove.

**Dave Jones:** Oh, well, kind of like an OJ Simpson glove. But yeah, it worked, first go. So yeah, that was just one of my first quick and dirty 3D drafts for this thing. But well, you know, original concept just to get stuff and size things up.

**Dave Jones:** And I did this in eMachine shop software, but the reason I didn't finish it off properly is because I found a bug when I tried to export from eMachine shop into the 3D MakerBot software, and like things were vanishing, you know, like extrusions were just vanishing and all over the place, and it was really

**Dave Jones:** it was just a pain in the arse. Anyway, so Dave did it all in SOLIDWORKS. But during the assembly of this thing, while we had no real issues with the 3D case, we did have with this pain in the arse flat flex cable which connects over to the lepton sensor.

**Dave Jones:** Now I can barely see it on the screen here, but if you've got a sharp eye, you can see, in fact I'll get something a bit sharper, you can see in there, there's little tiny breaks in that trace there. And this is quite a common fault with these flat flexes.

**Dave Jones:** This is obviously the pinch line where it exited from the board mount connector, and then you know, if you flex it too many times, then you can get little micro breaks in your traces like that. We had that, and we had all sorts of intermittent

**Dave Jones:** operation, wondering what the problem was, and you look at it under reasonable magnification, you know, just ordinary magnification. Like one of those, you know, head-mounted ones or something like that, low-power ones, well you can't really see the break. But you know, you put it under decent magnification and you can see these tiny little breaks

**Dave Jones:** in there when you get the flex. And you know, and if you straighten it out like that it might make contact. Anyway, if you're very careful, use very low temperature, you can actually put solder back on there and join any breaks if you're really desperate.

**Dave Jones:** But as you can see, I almost did that, almost success, but I had one last little dab at it and wah, it burnt straight through. Oh, what a pain in the arse. But just a little tip with these flat flex cables, if you do get one that breaks, you can just cut it with a pair of scissors

**Dave Jones:** like that, assuming you've got the length left, we just had enough length left to cut it across with a pair of scissors and all this white stuff, you can actually get in there, if you're very careful, apply the right amount of pressure and just scrape that off and get in there

**Dave Jones:** and actually get yourself a new flat flex end which you can put into the connector. And this is the actual end of the one that we're actually using on the lepton sensor there. And it works just fine, we didn't have to buy a new cable because we couldn't actually get one in stock of the right

**Dave Jones:** type that we wanted. So we just, yeah, just scrape away and yep, Bob's your uncle. You can fix these, no problem at all. And there's a close-up of that lepton PCB which we just cut off there and that worked a treat. So here's

**Dave Jones:** an animated 3D render Dave exported directly from SolidWorks who can do this kind of thing. And you'll see how he actually modelled all of the PCB. These are exact dimensions too, he got the calipers, measured it all up and everything. The battery and the buttons and everything else and the lepton

**Dave Jones:** sensor, he's got all models for these and put that in. And you see all the buttons and the exploded view and all the separate parts that we printed there. There's not that many of them, but as you can see, this is how we ensured that it would all fit together

**Dave Jones:** when we actually 3D printed. And sure enough, it did. No worries at all. And here's a short time lapse, we can't show the whole thing of the build, it took like 3 and a half hours or 4 hours or something. But we sort of printed them all out at once, you can see all the different

**Dave Jones:** sections plus the buttons in the back corner there as well. And you can see it built up some of the support material there. We did have a bit of an issue down in the bottom right corner there with one of the holders, but generally

**Dave Jones:** it worked pretty well. And here is our final print, check it out, we've got the main base of the unit. It's upside down by the way. And we've got our top cover and our little buttons here, decided to print them all out. Had a little issue down

**Dave Jones:** here with one of the holder for the lepton sensor there. But anyway, that was really impressive, I was very impressed how it built the bridge right across there, that was just fantastic. So now we'll peel these suckers off. That was a heated bed by the way, we're using

**Dave Jones:** a 110 degree bed with a 230 degree head on that. And it's all done with ABS plastic, so there we go. Ta-da! Look at that! And of course we printed it with the raft on the bottom, so it's not that great. So we'll probably have to

**Dave Jones:** well, we definitely have to reprint this, but because this is going to be the top surface under here, it'd be better to try and either print that directly on there or print it up the other way. So that, yeah, we get a nice smooth finish on the outside.

**Dave Jones:** But anyway, that's our front cover plate. And there it is. So yeah, it bridged all the way across there, it decided only to build those two supports in there. That's very impressive. And oh, by the way, if you're wondering, yes I have had countless problems with my MakerBot, but

**Dave Jones:** I've got these new red aftermarket metal support things in here, and they have made it like really ultra-stable. And I've got a new spring-loaded, the thing that's made all the difference is a new spring-loaded extruder plunger holder-y thing that goes against the filament instead of the stupid plastic thing that went across there.

**Dave Jones:** And that stopped all blockages and things from happening in there. So that was a really, they were two really good upgrades that actually make this MakerBot quite usable these days. And that's these rafts actually peel off quite nicely, look at that. So that's our support material under there, and you can still

**Dave Jones:** see the pattern of the first layer that went down to bridge this huge gap in there. But look at that, there's the slot for the SD card and the USB connector. That turned out really, really nice. As I said, the rafts do separate quite

**Dave Jones:** nicely. Oh, I'd print it directly on the surface and then we get a nice smooth surface finish on the front. And there we go, there's the first shot at that. It is custom designed for my wrist, could have done with a bit more angling on the side there, but hey, that's

**Dave Jones:** pretty groovy. And the reason why this board didn't fix is because we accidentally printed out version 1, so oops! Yeah, version 2 actually, yeah, that wasn't, didn't cater for the roundness, the rounding on the inside there for the board, but yeah, we just printed the wrong file.

**Dave Jones:** D'oh! So there you have it, there's the world's first thermal camera watch. We just did this for a bit of fun. Hope you liked it, and if you did, please give it a big thumbs up on YouTube, because that helps a lot, a big thermal thumbs up.

**Dave Jones:** And if you want to discuss it, jump on over to the EEVblog forum. Catch you next time, and no, I didn't end up putting the laser, the triple laser on here for the predator thing. That would have been cool, but you know, going a bit far.
