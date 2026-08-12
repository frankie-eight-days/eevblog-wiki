---
video_id: DTdycgOalG4
title: EEVblog #1336 - DT71 LCR Tweezer Destructive Teardown + Lab Update
url: https://www.youtube.com/watch?v=DTdycgOalG4
source: youtube-asr
timestamps: {"0": 1, "1": 21, "2": 37, "3": 52, "4": 67, "5": 81, "6": 98, "7": 110, "8": 120, "9": 131, "10": 147, "11": 158, "12": 172, "13": 187, "14": 202, "15": 214, "16": 227, "17": 239, "18": 252, "19": 265, "20": 284, "21": 304, "22": 321, "23": 334, "24": 348, "25": 361, "26": 377, "27": 388, "28": 405, "29": 416, "30": 432, "31": 446, "32": 463, "33": 476, "34": 491, "35": 505, "36": 525, "37": 540, "38": 552, "39": 568, "40": 580, "41": 597, "42": 609, "43": 620, "44": 636, "45": 654, "46": 671, "47": 687, "48": 700, "49": 713, "50": 728, "51": 744, "52": 756, "53": 768, "54": 779, "55": 792, "56": 809, "57": 821, "58": 839, "59": 856, "60": 873, "61": 892, "62": 912, "63": 926, "64": 942, "65": 960, "66": 972, "67": 987, "68": 1001, "69": 1022, "70": 1039, "71": 1055, "72": 1076, "73": 1094, "74": 1109, "75": 1126, "76": 1141, "77": 1155, "78": 1170, "79": 1189, "80": 1202, "81": 1215, "82": 1233, "83": 1245, "84": 1259, "85": 1273, "86": 1290, "87": 1305, "88": 1326, "89": 1343, "90": 1360, "91": 1376, "92": 1391, "93": 1406, "94": 1419, "95": 1431, "96": 1446, "97": 1458, "98": 1470}
---

**Dave Jones:** Hi, in the previous video we took a look at this miniware DT71 tweezer LCR meter. Stay on you, bastard. There we go. No. No. Why isn't it staying Why isn't it staying on? It There we go. I was going to say the TLDR from which

**Dave Jones:** is too long didn't read from the previous video is that it's not very accurate. It's got limited resolution. It's got limited ranges. There's accuracy issues between manual ranging and auto ranging modes for some reason. It uses non-standard test

**Dave Jones:** frequencies. You can't use it while it's charging with this lead. And of course, yeah, most complaints about this were like the charging system that you have to disconnect it and you have to physically charge it separately. And the

**Dave Jones:** tilt head detection was which by the way, you can actually disable the Hilton tilt head detection in the configuration file as miniware actually pointed out. So, that's good if you're always right-handed and you Yeah, just don't want it to change, then

**Dave Jones:** you can fix that. So, that's good. It's lead testing is limited. Couldn't do reverse polarity. And basically the secondary parameter measurements like the you know, ESR of a capacitor and stuff like that basically didn't work. So, there was a lot wrong with this, but

**Dave Jones:** it's 70 bucks. But as a lot of people pointed out $59 I believe you can get it for. Not including shipping though at Seed Studios. But the you know, the saving grace for this thing was that well, A it's cheap and B was the

**Dave Jones:** gorgeous probes on it. And a lot of people said that they should actually sell just the probes for this thing. You know, the batteries are in here apparently. Apparently there's a battery in there and in there. And yeah, if they and charging circuitry in

**Dave Jones:** here and a little charging lead apparently. Yeah, a lot of people said that they would buy just the tweezers if it came with like a short lead that hooked onto your LCR meter or something like that. So, I I think

**Dave Jones:** they should definitely do that cuz the probes are actually gorgeous. Anyway, a lot of people wanted to see a teardown of this thing. And the reason I didn't tear do a teardown last time is cuz I still wanted to get the review video cuz

**Dave Jones:** in the manual it specifically tells you if you open this thing you can't get it back together. So, obviously like this is all like ultrasonically welded together or something like that. But, yeah, apparently yeah, this will be a destructive

**Dave Jones:** teardown. But anyway, I do actually have another like sub I think it's just under 100 bucks. You can get it from Mouser. It's a global specialties LCR meter. I've got one of those on the way. I'm going to do

**Dave Jones:** a review of that. And then somebody else pointed out that there's an LCR research one as well. Coincidentally another Canadian one as well as these smart tweezers. Smart tweezers very expensive. I've got the old model. They got a new

**Dave Jones:** model, but you know, it's many hundreds of dollars. And LCR research in Canada as well. They actually make ones too which actually come with a NIST calibration certificate. Very nice for the price. But they're very expensive as well. But they have a lower

**Dave Jones:** end model for 169 Yankee bucks that comes with the NIST certificate everything. So, that might be worth checking it out as well. But anyway, I've got another one on order. But anyway, this video, let's do a teardown, shall we? And after we get the probes

**Dave Jones:** off you can see in there that they're just the contacts inside there. All of these LCR tweezers, they all pretty much either come with or you can get replaceable probe tips cuz you know, sooner or later after a couple of years

**Dave Jones:** heavy use you're going to be wearing down those nice sharp tips. Take these screws out here and you can see there's a magnet in there. You can see the magnet in there. That's the attractive one apparently according to the 3D

**Dave Jones:** model. And then there's another magnet in does the do these come out? How do you I don't know. I've got the screws off. Can I Whoa, I might have to break it apart. I don't know, but there's you can see another magnet down

**Dave Jones:** in there. That's what repels them. So, that's what gives it a really nice gorgeous feel. And I forgot to mention that it looks like these are actually just two wire probes. Some of the more expensive ones I believe are like four

**Dave Jones:** wire. So, they'll have like a sense wire coming up there. So, it just eliminates the leads in there from the test. But, you know, you can like two wires okay for something cheap and simple like this. Well, I don't know what those

**Dave Jones:** screws do either side because I take them out and I can't get this apart anyway. So, yeah, might just have to do a a wishing bone thing. I don't don't really want to. Geez, I'd love to like I don't know. All right, screw it. Here

**Dave Jones:** it goes. Come on. No, is it still going to pull out? No. No. Damn. Oh, I don't want to. No, want to. Like there we go. There's something. Okay, there's a trick. There was a trick to it. Okay, I think I had to get my

**Dave Jones:** screwdriver in there. Did I or something like a little spudger in there and I pry that out. Oops. Well, this is interesting. It's got some sort of like uh Oh, that that's a flat flex. Okay, yep, I can see. Yeah, I can see the traces on

**Dave Jones:** it now. You don't often see like a black gloss black flat flex like that. But, yeah, I can see traces in there now. So, I believe that the batteries are in here. So, yeah, looks like I can probably maybe pry that

**Dave Jones:** No, it's either glued or something in there. But, anyway, we've got our magnets. So, that's how they're connecting into the charging circuitry using these little flat flexes. Yeah, they weren't kidding that uh thing wouldn't come apart. That's why they put

**Dave Jones:** in the manual. They said, "Yeah, don't try and take it apart cuz you won't get it back together." And there we have it, 3.7 V, 0.185 Wh. Thank you very much. They're going to have one of these uh 50 mAh in uh each

**Dave Jones:** side there. So, that's uh the total capacity. Uh as I mentioned in the review video, I believe uh like uh what is it? Uh 20 hours runtime or something. So, with a 2-hour recharge, yep, two identical batteries. But yeah, that was

**Dave Jones:** uh glued in. That wasn't coming out easily. Like it was glued in at the ends here. And yeah, you just had to pry it all out. And there you go, the contact is just an extension uh an exposed um

**Dave Jones:** unsolderable mask uh extension of the flat flex there. So, that's actually rather nicely implemented. As I said, I'm very impressed by the uh probe design on this thing. So, they put all their effort into the uh probes, unfortunately, and uh the rest of the uh

**Dave Jones:** firmware and other stuff, you know, and the charging system, it leaves a bit to be desired, which is a shame because uh yeah, it it really is a sexy bit of kit, these probes. So, yep, there's our uh

**Dave Jones:** two magnets that we got out of the arms there. And watch this. Ooh. There we go. They're the uh They're the uh neodymium magnets up either either side there. So, they're the ones that caught it They're the attractive ones. That's sort of uh Yep,

**Dave Jones:** there we go. Oh, yeah. Yeah, look, I can actually rock that now. Ooh. Nice. So, you can see it. Even though I go like that, it flicks it. So, there you go. You can see how that just draws those probes back

**Dave Jones:** together. So, they These two here pushing apart counteract the force of these two here, and it's just It really is gorgeous. Yeah, if you just had these ones on their own, it would be like it like snaps. It snaps back. But, because

**Dave Jones:** you've got these two in here, which then when you push it in, it doesn't just go, you know, it doesn't snap like that. It's just It's just gorgeously balanced out. And wow, you know, hats off to the mechanical engineer at

**Dave Jones:** e-design who came up with that cuz that is just great. Okay, so these little aluminum side plates, they're held on there with some double-sided tape. Nothing wrong with that, I guess. Uh and Oh, there you go. I can't

**Dave Jones:** actually get that apart. I actually tried to force it from the end here first, and then I realized that the side panels will just come off. And then it's just clipped together. So, so it is possible to get this apart without too much

**Dave Jones:** damage, although I've just Oh, no. Ah, those They're shield. They're shield wires, are they? Look, there's two exposed wires either side there that I presume to shield use these as shields. Although, were they I I'll have to rewatch the footage. Were

**Dave Jones:** they actually under the tape? So, but obviously that's deliberate. That is deliberate to shield those sides, I'm sure. That's got to be It's got to be the reason. But, did Was that tape covering it? That'd be a fail if like the

**Dave Jones:** designers went, "Oh yeah, let's be clever and we can use these as metal shield side plates." And then in production, um somebody's went, "Oh, we need to stick them on. Let's just put tape and then they cover it and insulate

**Dave Jones:** it. That'd be hilarious. Sure enough, you get those clips off, and this bad boy is just going to come apart. Oh, there we go. We're in. Ooh. Got some black gunk there. What are they doing that for? Is that

**Dave Jones:** You wouldn't need that for insulation. There's nothing on the other side of that. There's no nickel screening or anything like that. So, yeah. Oh, look at that. We can get the whole lot out. Just comes out as one

**Dave Jones:** assembly. There it is. Sweet. That's actually three board construction. It looks like there's something on the back of the LCD there. Let's Yep. Yep. There's a flex. There's a flex. Here you go. Oh, wow. Look at that. Yep.

**Dave Jones:** That's how they get the small form factor. Ah, there we go. That flat flex. I thought it was like embedded in the inner layer of the PCB, but it's not. That's actually I thought that was gunk. That's actually um

**Dave Jones:** the part of the flat flex and then just going on to uh the board there. So, is that Do they do they solder that on or is it conductive glue? I think they might No, that's the uh No, they're the solder

**Dave Jones:** joints. Okay. So, they're the solder joints for the uh four-pin TRS jack there. So, we've got our four pins and then our flat flex is part of that. Cuz they obviously couldn't fit all that stuff on the main board. I mean, as I said in

**Dave Jones:** the review video, like why have they gone so small with this head? I mean, it just just didn't make sense. And those wires there and there, yep, very deliberately soldered onto the ground terminal of the TRS jack. There you go.

**Dave Jones:** So, that was very deliberate uh outer case shielding. But if shielding was important, like you would like use like a I don't know, like a die-cast alloy head or something, maybe? Like a die-cast like two-part clamshell head, perhaps?

**Dave Jones:** And there's your touch button. It's just a metal mesh like that, just bent over. Um so, yeah, it's like just a capacitive uh sense thing. So, then there's got to be Yeah. Yeah. There we go. A castellated edge.

**Dave Jones:** Well, it's not It's not castellated. It's a gold uh plated edge. A castellation would be the like the holes in the side. But yet they've just gone, uh, yeah, we want, uh, gold edge plating on just that little bit of the board

**Dave Jones:** there. Thank you very much. The PCB manufacturing house will say, yep, we can do that. That's a separate process. No worries. It's cost you a bit extra. Hi. Yes, I'm back in the old lab {slash} new lab, which I'm going to be moving

**Dave Jones:** into over the coming weeks. And I have moved over my soldering bench, which includes my, uh, Tagarno microscope, which we're using now. And it includes my Mantis, my soldering irons, and my, uh, PC capture bench and everything else. In fact, I can show you. Hang on.

**Dave Jones:** Hang on. Here we go. There we go. There it is. Hang on. Can I go full screen? Can I go full webcam? There we go. So, it's Yep, I've moved over precisely one bench so far. There you go. And I'm getting stuff set up.

**Dave Jones:** And, oh, sorry. You probably can't hear me. I'm way away from the mic. I'm, um, yep, starting to set up a few things, anyway. So, yes, this will be permanently set up properly, um, soon. And so the acoustics are going to suck

**Dave Jones:** until then. I'm going to do all the proper cabling, the proper acoustics. I'm going to set up everything properly. And it's going to be great. But until then, we're going to have to make do. So, I just moved all the stuff in, uh,

**Dave Jones:** yesterday. And I just cobbled together like there's just cables going everywhere to try and get this thing working. Anyway, let's zoom in with our Tagarno. Even my remote control is not like I normally have it on the side of

**Dave Jones:** the bench here. And if I rock the bench, the camera's going to wobble cuz it's sitting on top of my Tagarno. Ah, you know. Feels good to be back. All right, let's go. And yes, the lighting's going to suck, too, because I know it's,

**Dave Jones:** uh, it's dark in this corner at the moment. Anyway, what have we got down there? We've got a CPU 1017. Ah, no, that's a CPC's 1017. There you go. That's an excess, uh, opto mos relay. So, photo-mos relay.

**Dave Jones:** There you go. Yeah, I need better like a monitor up the top so I can just like see like so when I've got a camera set up, I can just meh Um yeah. All right, so we've got another set of

**Dave Jones:** discrete down there NP2300. Yep, MOSFET. So, we've got a relay switching and a MOSFET there. Oh, there's the LCD part number for those playing along at home. So, yeah, I don't know. Anyone want to reverse engineer that? There's four traces. There's one

**Dave Jones:** ground plus three signal coming in on the right-hand side there and obviously they're all they just connect through to the pins on the TRS jack there. So, they're just soldering those directly on. That's the bottom side. Version 2.31

**Dave Jones:** 402 there. Not sure. I'm presuming that's like a just little six-pin op-amp. Something like that. And NB PA83, I don't know. You'd have to know your surface mount part numbers, but uh couple of protection diodes there, I'd say, and a

**Dave Jones:** couple of resistors. So, that's interesting that that's basically in parallel with the pins on the TRS jack. Hmm. Okay, let's see what these are. Yes, you can see noise on the image like grain noise. That's due to the lack of

**Dave Jones:** light here in this corner. I'm just using the uh Takano number. Anyway, what's an A3JK? A3JK, I hate SMD part numbers. Anyway, curiously, there's two of them. Um and they're just like uh in they're just connected, I presume, through to uh

**Dave Jones:** couple of pins on the TRS jack. So, that would be connected through to the probes. Like basically straight through to the probes. Sorry if I'm too my head's too close to the camera. This is scary. All right, I'm not getting anything for the

**Dave Jones:** code for the A3JK code there. Oh, well, yeah, not with the first Google anyway. I've got a crystal over there. And it is just a crystal. It is not a crystal oscillator cuz that's one big ass pad on the end like

**Dave Jones:** that. So, maybe there's some sort of like you know, instrumentation amp, maybe programmable gain. Uh you know, one of those front-end type chips perhaps or just maybe a mux. Are they just like a mux and they're just doing everything in

**Dave Jones:** the micro? Which is going to be under there. So, we're going to have to desolder a couple of things here. We're going to have to desolder this entire top board to see what the micro is. Bloody soldering iron's not even plugged in

**Dave Jones:** yet. Damn it. I've got hardly any tools here at all. So, all I've got is a big ass tip and uh pair of tweezers and that's about it. So, I'm not sure if it's going to be easier to

**Dave Jones:** just cut those off cuz I'm not going to reuse this. Okay, I do actually have a pair of side cutters. I did try and force it apart. That was a real mistake. So, I'm going to There we go. Um yeah, I think I did kill

**Dave Jones:** a part. Um So, completely butchered it. Yeah, I think there was a sock 23 something or other in there. Oops. Um yeah, sorry. So, I don't know. Its remains are probably down in there somewhere. This is what happens when you've got

**Dave Jones:** like just like a pair of side cutters and a soldering iron and that's it. No sucker in sight. Oh, no, there it is. 65ZY, whatever that is. So, here we go. We have a PCB. We've got two like amps,

**Dave Jones:** something like that. Amps or switches. And on the other side, tada, we've got an ST. No surprises whatsoever. It's a L43 or 432. They've got so many bloody variants. I have no idea what that is. And there you

**Dave Jones:** have it. It's ultra low power arm cortex M4 100 dry stone mips 256k flash 64k of SRAM. What luxury. Wow. There you go. And that has and it's got rich analog peripherals. Not that poor rubbish. Independent with independent supply.

**Dave Jones:** That's interesting. 1 12-bit ADC. 5 5 meg samples per second. Wow, that's screaming up to 16 bits with hardware over sampling. Wow. Two 12-bit DAC outputs. Obviously, they're using those. So, yeah. They're So, maybe like is it just direct output

**Dave Jones:** and then they're just muxing those chips are just muxing those because if we go back to we go back to the video tape. Yeah, there's nothing else on there. There's the micro. Don't know which pins are the DACs. You can look that up, but

**Dave Jones:** you know, we couldn't be bothered really. Um Is that one going Uh no. Okay. This one going over to the board up there. And boom, it's yeah, that's coming. Is that almost coming directly in? It's coming under from the socket there. So,

**Dave Jones:** they're reading that back. It's the It's under the It's yeah, it's under there. Don't know. But yeah, there's not a lot to it, is there? Anyway, we do have a little bit more on the bottom of this board. Got another

**Dave Jones:** jobby. What's that? Don't know what that is. Is that like a protection? Is that just like I don't think that's an active part. And that could just be protection. Anyway, we did have another transistor on the top. There's our uh

**Dave Jones:** edge, of course. There you go. How they've just plated that on the side there. That's our edge contact for our Vias there for a bit of reinforcement. So, yeah, there's not much not much in it. Assuming that's like some sort of

**Dave Jones:** protection device, maybe, then I'm going to say that it's Well, it's not quite doing it. It's almost direct uh DAC output from other using both DACs. Are they driving both? Um and then I don't know. That one's either a mux

**Dave Jones:** or an amp or one of those, you know, front-end jobbies or something. I don't see like it I don't think it's like an I squared C interface. Like it's not a serial interface or anything like that. Anyway, so these are

**Dave Jones:** what These would be range resistors and stuff. Uh I would presume you'd need some of those. But yeah, there's not much in it, is there? I mean, jeez, that's, you know, it's a little bit over here, but uh

**Dave Jones:** that's just like some relay and MOSFET switching. Um and maybe an amp. That little six-pin sot jobby, and it's about all she wrote. Wow. So, you can obviously tell why this thing is A, cheap, and B, its performance is not that great. Leaves a

**Dave Jones:** bit to be desired. It's because it's just like, you know, there's not a lot of hardware, and there's no, you know, really precision hardware in here or something. There might be uh but you know, the spec is loosey-goosey. What is

**Dave Jones:** it? Over a percent? Whereas some of the top better quality ones, like, well, you know, twice the price, um are like double, triple, even or, you know, you buy a $300 one, it's like five times the accuracy of uh these things. So, much

**Dave Jones:** more uh they'd have much more precision components. Don't remember if I did a I think I did a teardown of the old Smart Toys R Us one, didn't I? I think I did. Anyway, let's have a look at our OLED.

**Dave Jones:** Let's rub my fingerprints off. Oh, it didn't do a good job, did it? Now, if you get this puppy in the right light, speaking of light, I do actually have a another light, but that's not going to Oh, there we go.

**Dave Jones:** I can see Oh, you can see the lines. Look at that. You can see the traces in there. Each column. Nice. And then you can see the rows over there as well. There you go. Rows and Yeah, oh yeah. Look at that. So, you can

**Dave Jones:** see the ridiculously fine pitch on those traces there. So, there are rows, there are row connections, and these are our common connections. You see them all in there? Wow, it's hard to get the right light, of course. It's all about getting the light,

**Dave Jones:** but wow, you can really see that. So, that is an OLED display. Very grainy, but you can see it. And the max That's the maximum 40 times optical zoom on my Takano. Okay, I've amped the brightness up on the only light I

**Dave Jones:** have in here. You can almost see like the 3D nature of them of the elements in there. That's pretty groovy, huh? Yeah, but you can almost see look almost see the connections. You can see the connections on the top. And of course,

**Dave Jones:** there's a chip on glass, COG it's called. So, that's the glass substrate, and that is one big die. That's one big silicon die. None of that bond wire rubbish, and uh that's just flipped over and connected directly on the glass, and

**Dave Jones:** then all of the uh rows and column drivers looks like all the rows go up here, connected on this end of the chip. This side's the interface. All your interface connections coming over, and then all down around here,

**Dave Jones:** that's all your column drivers. So, what's that I think it's 96 by 12 or something, isn't it? So, yep, it's got to have like, you know, 130 pins or something in it, maybe. So, there you have it. That's it. Um sorry

**Dave Jones:** about the poor image and audio uh quality and setup. Yes, I could eventually put the green screen uh behind here, although it'd have to be a fair way back, cuz it it's an Elgato uh green screen. It's like 2 m wide or

**Dave Jones:** something, but I can actually put it at the back there, and it could go up oh, but then I'd need a gap between my benches to actually do that. Hmm, I might have to put a gap between Oh, but then I couldn't have the

**Dave Jones:** continuous roll of ESD. Oh, like, there's so many things in like setting up a lab specifically to do the kind of stuff I have that huge variety of stuff that I do. So, anyway, yep, that's it. If you liked the video, please give it a

**Dave Jones:** big thumbs-up, as always. Comment down below and over on the EE blog forum, and you can actually follow Supporters have already seen late discussions about moving into the new lab and uh things like that, including like, you know,

**Dave Jones:** there's even financial stuff, but you can also see those over on my library channel, as well, even if you're not a Supporter. So, there you go. So, that's it. I'm out of here. Geez, this really looks big, doesn't it? I'm just looking

**Dave Jones:** at there There's my huge nose. Look at that. And uh yeah, this looks really deep. It's not. It's 50 sq m, half the size of my current lab, but I'm going to save $40,000 a year. Beauty. Catch you next time.
