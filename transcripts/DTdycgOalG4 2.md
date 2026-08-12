---
video_id: DTdycgOalG4
title: EEVblog #1336 - DT71 LCR Tweezer Destructive Teardown + Lab Update
url: https://www.youtube.com/watch?v=DTdycgOalG4
source: youtube-asr
timestamps: {"0": 1, "1": 30, "2": 61, "3": 79, "4": 108, "5": 131, "6": 160, "7": 191, "8": 218, "9": 246, "10": 276, "11": 294, "12": 312, "13": 340, "14": 357, "15": 371, "16": 402, "17": 420, "18": 436, "19": 468, "20": 487, "21": 513, "22": 534, "23": 561, "24": 582, "25": 600, "26": 627, "27": 654, "28": 671, "29": 687, "30": 705, "31": 728, "32": 744, "33": 760, "34": 785, "35": 797, "36": 819, "37": 856, "38": 894, "39": 918, "40": 933, "41": 950, "42": 982, "43": 994, "44": 1014, "45": 1031, "46": 1051, "47": 1068, "48": 1089, "49": 1105, "50": 1119, "51": 1136, "52": 1165, "53": 1185, "54": 1210, "55": 1243, "56": 1268, "57": 1290, "58": 1318, "59": 1351, "60": 1370, "61": 1386, "62": 1410, "63": 1436, "64": 1463, "65": 1482}
---

**Dave Jones:** Hi, in the previous video we took a look at this miniware DT71 tweezer LCR meter. Stay on you, bastard. There we go. No. No. Why isn't it staying Why isn't it staying on? It There we go. I was going to say the TLDR from which is too long didn't read from the previous video is that it's not very accurate. It's got limited resolution. It's got limited ranges.

**Dave Jones:** There's accuracy issues between manual ranging and auto ranging modes for some reason. It uses non-standard test frequencies. You can't use it while it's charging with this lead. And of course, yeah, most complaints about this were like the charging system that you have to disconnect it and you have to physically charge it separately. And the tilt head detection was which by the way, you can actually disable the Hilton tilt head detection in the configuration file as miniware actually pointed out.

**Dave Jones:** So, that's good if you're always right-handed and you Yeah, just don't want it to change, then you can fix that. So, that's good. It's lead testing is limited. Couldn't do reverse polarity. And basically the secondary parameter measurements like the you know, ESR of a capacitor and stuff like that basically didn't work.

**Dave Jones:** So, there was a lot wrong with this, but it's 70 bucks. But as a lot of people pointed out $59 I believe you can get it for. Not including shipping though at Seed Studios. But the you know, the saving grace for this thing was that well, A it's cheap and B was the gorgeous probes on it. And a lot of people said that they should actually sell just the probes for this thing. You know, the batteries are in here apparently. Apparently there's a battery in there and in there. And

**Dave Jones:** yeah, if they and charging circuitry in here and a little charging lead apparently. Yeah, a lot of people said that they would buy just the tweezers if it came with like a short lead that hooked onto your LCR meter or something like that. So, I I think they should definitely do that cuz the probes are actually gorgeous. Anyway, a lot of people wanted to see a teardown of this thing. And the reason I didn't tear do a teardown last time is cuz I still wanted to get the review video cuz

**Dave Jones:** in the manual it specifically tells you if you open this thing you can't get it back together. So, obviously like this is all like ultrasonically welded together or something like that. But, yeah, apparently yeah, this will be a destructive teardown. But anyway, I do actually have another like sub I think it's just under 100 bucks. You can get it from Mouser. It's a global specialties LCR meter. I've got one of those on the way. I'm going to do a review of that. And then somebody else

**Dave Jones:** pointed out that there's an LCR research one as well. Coincidentally another Canadian one as well as these smart tweezers. Smart tweezers very expensive. I've got the old model. They got a new model, but you know, it's many hundreds of dollars. And LCR research in Canada as well. They actually make ones too which actually come with a NIST calibration certificate. Very nice for the price. But they're very expensive as well. But they have a lower end model for 169 Yankee bucks that comes with the NIST certificate

**Dave Jones:** everything. So, that might be worth checking it out as well. But anyway, I've got another one on order. But anyway, this video, let's do a teardown, shall we? And after we get the probes off you can see in there that they're just the contacts inside there. All of these LCR tweezers, they all pretty much either come with or you can get replaceable probe tips cuz you know, sooner or later after a couple of years heavy use you're going to be wearing down those nice sharp tips. Take these

**Dave Jones:** screws out here and you can see there's a magnet in there. You can see the magnet in there. That's the attractive one apparently according to the 3D model. And then there's another magnet in does the do these come out? How do you I don't know. I've got the screws off. Can I Whoa, I might have to break it apart. I don't know, but there's you can see another magnet down in there. That's what repels them. So, that's what gives it a really nice gorgeous feel. And I forgot to mention

**Dave Jones:** that it looks like these are actually just two wire probes. Some of the more expensive ones I believe are like four wire. So, they'll have like a sense wire coming up there. So, it just eliminates the leads in there from the test. But, you know, you can like two wires okay for something cheap and simple like this. Well, I don't know what those screws do either side because I take them out and I can't get this apart anyway. So, yeah, might just have to do a

**Dave Jones:** a wishing bone thing. I don't don't really want to. Geez, I'd love to like I don't know. All right, screw it. Here it goes. Come on. No, is it still going to pull out? No. No. Damn. Oh, I don't want to.

**Dave Jones:** No, want to. Like there we go. There's something. Okay, there's a trick. There was a trick to it. Okay, I think I had to get my screwdriver in there. Did I or something like a little spudger in there and I pry that out. Oops.

**Dave Jones:** Well, this is interesting. It's got some sort of like uh Oh, that that's a flat flex. Okay, yep, I can see. Yeah, I can see the traces on it now. You don't often see like a black gloss black flat flex like that. But, yeah, I can see traces in there now. So, I believe that the batteries are in here. So, yeah, looks like I can probably maybe pry that No, it's either glued or something in there. But, anyway, we've got our magnets. So, that's how they're

**Dave Jones:** connecting into the charging circuitry using these little flat flexes. Yeah, they weren't kidding that uh thing wouldn't come apart. That's why they put in the manual. They said, "Yeah, don't try and take it apart cuz you won't get it back together." And there we have it, 3.7 V, 0.185 Wh.

**Dave Jones:** Thank you very much. They're going to have one of these uh 50 mAh in uh each side there. So, that's uh the total capacity. Uh as I mentioned in the review video, I believe uh like uh what is it? Uh 20 hours runtime or something.

**Dave Jones:** So, with a 2-hour recharge, yep, two identical batteries. But yeah, that was uh glued in. That wasn't coming out easily. Like it was glued in at the ends here. And yeah, you just had to pry it all out. And there you go, the contact is just an extension uh an exposed um unsolderable mask uh extension of the flat flex there. So, that's actually rather nicely implemented. As I said, I'm very impressed by the uh probe design on this thing. So, they put all their effort into the uh probes,

**Dave Jones:** unfortunately, and uh the rest of the uh firmware and other stuff, you know, and the charging system, it leaves a bit to be desired, which is a shame because uh yeah, it it really is a sexy bit of kit, these probes. So, yep, there's our uh two magnets that we got out of the arms there. And watch this.

**Dave Jones:** Ooh. There we go. They're the uh They're the uh neodymium magnets up either either side there. So, they're the ones that caught it They're the attractive ones. That's sort of uh Yep, there we go. Oh, yeah. Yeah, look, I can actually rock that now.

**Dave Jones:** Ooh. Nice. So, you can see it. Even though I go like that, it flicks it. So, there you go. You can see how that just draws those probes back together. So, they These two here pushing apart counteract the force of these two here, and it's just It really is gorgeous. Yeah, if you just had these ones on their own, it would be like it like snaps. It snaps back. But, because you've got these two in here, which then when you push it in, it doesn't just go,

**Dave Jones:** you know, it doesn't snap like that. It's just It's just gorgeously balanced out. And wow, you know, hats off to the mechanical engineer at e-design who came up with that cuz that is just great. Okay, so these little aluminum side plates, they're held on there with some double-sided tape.

**Dave Jones:** Nothing wrong with that, I guess. Uh and Oh, there you go. I can't actually get that apart. I actually tried to force it from the end here first, and then I realized that the side panels will just come off. And then it's just clipped together. So, so it is possible to get this apart without too much damage, although I've just Oh, no. Ah, those They're shield. They're shield wires, are they?

**Dave Jones:** Look, there's two exposed wires either side there that I presume to shield use these as shields. Although, were they I I'll have to rewatch the footage. Were they actually under the tape? So, but obviously that's deliberate. That is deliberate to shield those sides, I'm sure.

**Dave Jones:** That's got to be It's got to be the reason. But, did Was that tape covering it? That'd be a fail if like the designers went, "Oh yeah, let's be clever and we can use these as metal shield side plates." And then in production, um somebody's went, "Oh, we need to stick them on. Let's just put tape and then they cover it and insulate it. That'd be hilarious. Sure enough, you get those clips off, and this bad boy is just going to come apart. Oh, there we go.

**Dave Jones:** We're in. Ooh. Got some black gunk there. What are they doing that for? Is that You wouldn't need that for insulation. There's nothing on the other side of that. There's no nickel screening or anything like that. So, yeah. Oh, look at that. We can get the whole lot out. Just comes out as one assembly. There it is.

**Dave Jones:** Sweet. That's actually three board construction. It looks like there's something on the back of the LCD there. Let's Yep. Yep. There's a flex. There's a flex. Here you go. Oh, wow. Look at that. Yep. That's how they get the small form factor.

**Dave Jones:** Ah, there we go. That flat flex. I thought it was like embedded in the inner layer of the PCB, but it's not. That's actually I thought that was gunk. That's actually um the part of the flat flex and then just going on to uh the board there. So, is that Do they do they solder that on or is it conductive glue? I think they might No, that's the uh No, they're the solder joints. Okay. So, they're the solder joints for the uh four-pin TRS jack there. So, we've got our four pins and

**Dave Jones:** then our flat flex is part of that. Cuz they obviously couldn't fit all that stuff on the main board. I mean, as I said in the review video, like why have they gone so small with this head? I mean, it just just didn't make sense. And those wires there and there, yep, very deliberately soldered onto the ground terminal of the TRS jack. There you go.

**Dave Jones:** So, that was very deliberate uh outer case shielding. But if shielding was important, like you would like use like a I don't know, like a die-cast alloy head or something, maybe? Like a die-cast like two-part clamshell head, perhaps?

**Dave Jones:** And there's your touch button. It's just a metal mesh like that, just bent over. Um so, yeah, it's like just a capacitive uh sense thing. So, then there's got to be Yeah. Yeah. There we go. A castellated edge.

**Dave Jones:** Well, it's not It's not castellated. It's a gold uh plated edge. A castellation would be the like the holes in the side. But yet they've just gone, uh, yeah, we want, uh, gold edge plating on just that little bit of the board there. Thank you very much. The PCB manufacturing house will say, yep, we can do that. That's a separate process.

**Dave Jones:** No worries. It's cost you a bit extra. Hi. Yes, I'm back in the old lab {slash} new lab, which I'm going to be moving into over the coming weeks. And I have moved over my soldering bench, which includes my, uh, Tagarno microscope, which we're using now. And it includes my Mantis, my soldering irons, and my, uh, PC capture bench and everything else. In fact, I can show you. Hang on.

**Dave Jones:** Hang on. Here we go. There we go. There it is. Hang on. Can I go full screen? Can I go full webcam? There we go. So, it's Yep, I've moved over precisely one bench so far. There you go. And I'm getting stuff set up.

**Dave Jones:** And, oh, sorry. You probably can't hear me. I'm way away from the mic. I'm, um, yep, starting to set up a few things, anyway. So, yes, this will be permanently set up properly, um, soon. And so the acoustics are going to suck until then. I'm going to do all the proper cabling, the proper acoustics.

**Dave Jones:** I'm going to set up everything properly. And it's going to be great. But until then, we're going to have to make do. So, I just moved all the stuff in, uh, yesterday. And I just cobbled together like there's just cables going everywhere to try and get this thing working. Anyway, let's zoom in with our Tagarno. Even my remote control is not like I normally have it on the side of the bench here. And if I rock the bench, the camera's going to wobble cuz it's sitting on top of my Tagarno.

**Dave Jones:** Ah, you know. Feels good to be back. All right, let's go. And yes, the lighting's going to suck, too, because I know it's, uh, it's dark in this corner at the moment. Anyway, what have we got down there?

**Dave Jones:** We've got a CPU 1017. Ah, no, that's a CPC's 1017. There you go. That's an excess, uh, opto mos relay. So, photo-mos relay. There you go. Yeah, I need better like a monitor up the top so I can just like see like so when I've got a camera set up, I can just meh Um yeah.

**Dave Jones:** All right, so we've got another set of discrete down there NP2300. Yep, MOSFET. So, we've got a relay switching and a MOSFET there. Oh, there's the LCD part number for those playing along at home. So, yeah, I don't know. Anyone want to reverse engineer that? There's four traces. There's one ground plus three signal coming in on the right-hand side there and obviously they're all they just connect through to the pins on the TRS jack there. So, they're just soldering those directly on. That's the bottom side. Version 2.31

**Dave Jones:** 402 there. Not sure. I'm presuming that's like a just little six-pin op-amp. Something like that. And NB PA83, I don't know. You'd have to know your surface mount part numbers, but uh couple of protection diodes there, I'd say, and a couple of resistors. So, that's interesting that that's basically in parallel with the pins on the TRS jack. Hmm. Okay, let's see what these are. Yes, you can see noise on the image like grain noise. That's due to the lack of light here in this corner. I'm just

**Dave Jones:** using the uh Takano number. Anyway, what's an A3JK? A3JK, I hate SMD part numbers. Anyway, curiously, there's two of them. Um and they're just like uh in they're just connected, I presume, through to uh couple of pins on the TRS jack. So, that would be connected through to the probes.

**Dave Jones:** Like basically straight through to the probes. Sorry if I'm too my head's too close to the camera. This is scary. All right, I'm not getting anything for the code for the A3JK code there. Oh, well, yeah, not with the first Google anyway.

**Dave Jones:** I've got a crystal over there. And it is just a crystal. It is not a crystal oscillator cuz that's one big ass pad on the end like that. So, maybe there's some sort of like you know, instrumentation amp, maybe programmable gain.

**Dave Jones:** Uh you know, one of those front-end type chips perhaps or just maybe a mux. Are they just like a mux and they're just doing everything in the micro? Which is going to be under there. So, we're going to have to desolder a couple of things here. We're going to have to desolder this entire top board to see what the micro is. Bloody soldering iron's not even plugged in yet. Damn it. I've got hardly any tools here at all. So, all I've got is a big ass tip and uh

**Dave Jones:** pair of tweezers and that's about it. So, I'm not sure if it's going to be easier to just cut those off cuz I'm not going to reuse this. Okay, I do actually have a pair of side cutters. I did try and force it apart.

**Dave Jones:** That was a real mistake. So, I'm going to There we go. Um yeah, I think I did kill a part. Um So, completely butchered it. Yeah, I think there was a sock 23 something or other in there. Oops. Um yeah, sorry.

**Dave Jones:** So, I don't know. Its remains are probably down in there somewhere. This is what happens when you've got like just like a pair of side cutters and a soldering iron and that's it. No sucker in sight. Oh, no, there it is.

**Dave Jones:** 65ZY, whatever that is. So, here we go. We have a PCB. We've got two like amps, something like that. Amps or switches. And on the other side, tada, we've got an ST. No surprises whatsoever. It's a L43 or 432.

**Dave Jones:** They've got so many bloody variants. I have no idea what that is. And there you have it. It's ultra low power arm cortex M4 100 dry stone mips 256k flash 64k of SRAM. What luxury. Wow. There you go.

**Dave Jones:** And that has and it's got rich analog peripherals. Not that poor rubbish. Independent with independent supply. That's interesting. 1 12-bit ADC. 5 5 meg samples per second. Wow, that's screaming up to 16 bits with hardware over sampling. Wow. Two 12-bit DAC outputs. Obviously, they're using those.

**Dave Jones:** So, yeah. They're So, maybe like is it just direct output and then they're just muxing those chips are just muxing those because if we go back to we go back to the video tape. Yeah, there's nothing else on there.

**Dave Jones:** There's the micro. Don't know which pins are the DACs. You can look that up, but you know, we couldn't be bothered really. Um Is that one going Uh no. Okay. This one going over to the board up there.

**Dave Jones:** And boom, it's yeah, that's coming. Is that almost coming directly in? It's coming under from the socket there. So, they're reading that back. It's the It's under the It's yeah, it's under there. Don't know. But yeah, there's not a lot to it, is there?

**Dave Jones:** Anyway, we do have a little bit more on the bottom of this board. Got another jobby. What's that? Don't know what that is. Is that like a protection? Is that just like I don't think that's an active part. And that could just be protection. Anyway, we did have another transistor on the top. There's our uh edge, of course. There you go. How they've just plated that on the side there. That's our edge contact for our Vias there for a bit of reinforcement.

**Dave Jones:** So, yeah, there's not much not much in it. Assuming that's like some sort of protection device, maybe, then I'm going to say that it's Well, it's not quite doing it. It's almost direct uh DAC output from other using both DACs. Are they driving both?

**Dave Jones:** Um and then I don't know. That one's either a mux or an amp or one of those, you know, front-end jobbies or something. I don't see like it I don't think it's like an I squared C interface. Like it's not a serial interface or anything like that. Anyway, so these are what These would be range resistors and stuff. Uh I would presume you'd need some of those. But yeah, there's not much in it, is there?

**Dave Jones:** I mean, jeez, that's, you know, it's a little bit over here, but uh that's just like some relay and MOSFET switching. Um and maybe an amp. That little six-pin sot jobby, and it's about all she wrote. Wow. So, you can obviously tell why this thing is A, cheap, and B, its performance is not that great. Leaves a bit to be desired. It's because it's just like, you know, there's not a lot of hardware, and there's no, you know, really precision hardware in here or something. There might be uh but you

**Dave Jones:** know, the spec is loosey-goosey. What is it? Over a percent? Whereas some of the top better quality ones, like, well, you know, twice the price, um are like double, triple, even or, you know, you buy a $300 one, it's like five times the accuracy of uh these things. So, much more uh they'd have much more precision components. Don't remember if I did a I think I did a teardown of the old Smart Toys R Us one, didn't I?

**Dave Jones:** I think I did. Anyway, let's have a look at our OLED. Let's rub my fingerprints off. Oh, it didn't do a good job, did it? Now, if you get this puppy in the right light, speaking of light, I do actually have a another light, but that's not going to Oh, there we go.

**Dave Jones:** I can see Oh, you can see the lines. Look at that. You can see the traces in there. Each column. Nice. And then you can see the rows over there as well. There you go. Rows and Yeah, oh yeah. Look at that. So, you can see the ridiculously fine pitch on those traces there. So, there are rows, there are row connections, and these are our common connections.

**Dave Jones:** You see them all in there? Wow, it's hard to get the right light, of course. It's all about getting the light, but wow, you can really see that. So, that is an OLED display. Very grainy, but you can see it. And the max That's the maximum 40 times optical zoom on my Takano. Okay, I've amped the brightness up on the only light I have in here. You can almost see like the 3D nature of them of the elements in there.

**Dave Jones:** That's pretty groovy, huh? Yeah, but you can almost see look almost see the connections. You can see the connections on the top. And of course, there's a chip on glass, COG it's called. So, that's the glass substrate, and that is one big die. That's one big silicon die.

**Dave Jones:** None of that bond wire rubbish, and uh that's just flipped over and connected directly on the glass, and then all of the uh rows and column drivers looks like all the rows go up here, connected on this end of the chip. This side's the interface.

**Dave Jones:** All your interface connections coming over, and then all down around here, that's all your column drivers. So, what's that I think it's 96 by 12 or something, isn't it? So, yep, it's got to have like, you know, 130 pins or something in it, maybe. So, there you have it. That's it. Um sorry about the poor image and audio uh quality and setup.

**Dave Jones:** Yes, I could eventually put the green screen uh behind here, although it'd have to be a fair way back, cuz it it's an Elgato uh green screen. It's like 2 m wide or something, but I can actually put it at the back there, and it could go up oh, but then I'd need a gap between my benches to actually do that. Hmm, I might have to put a gap between Oh, but then I couldn't have the continuous roll of ESD. Oh, like, there's so many things in like setting

**Dave Jones:** up a lab specifically to do the kind of stuff I have that huge variety of stuff that I do. So, anyway, yep, that's it. If you liked the video, please give it a big thumbs-up, as always. Comment down below and over on the EE blog forum, and you can actually follow Supporters have already seen late discussions about moving into the new lab and uh things like that, including like, you know, there's even financial stuff, but you can also see those over on my library channel, as well, even if you're not a

**Dave Jones:** Supporter. So, there you go. So, that's it. I'm out of here. Geez, this really looks big, doesn't it? I'm just looking at there There's my huge nose. Look at that. And uh yeah, this looks really deep. It's not. It's 50 sq m, half the size of my current lab, but I'm going to save $40,000 a year. Beauty.

**Dave Jones:** Catch you next time.
