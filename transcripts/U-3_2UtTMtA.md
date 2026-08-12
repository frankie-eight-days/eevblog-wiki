---
video_id: U-3_2UtTMtA
title: EEVblog #638 - Apollo Saturn V LVDC Testing
url: https://www.youtube.com/watch?v=U-3_2UtTMtA
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 39, "3": 51, "4": 85, "5": 95, "6": 111, "7": 123, "8": 135, "9": 145, "10": 164, "11": 176, "12": 188, "13": 215, "14": 235, "15": 246, "16": 260, "17": 274, "18": 286, "19": 302, "20": 311, "21": 322, "22": 333, "23": 345, "24": 363, "25": 387, "26": 408, "27": 417, "28": 429, "29": 442, "30": 456, "31": 473, "32": 490, "33": 504, "34": 520, "35": 533, "36": 547, "37": 558, "38": 573, "39": 589, "40": 604, "41": 615, "42": 627, "43": 645, "44": 654, "45": 673, "46": 689, "47": 702, "48": 714, "49": 723, "50": 736, "51": 751, "52": 764, "53": 772, "54": 786, "55": 801, "56": 811, "57": 823, "58": 833, "59": 843, "60": 855, "61": 868, "62": 886, "63": 900, "64": 915, "65": 933, "66": 948, "67": 965, "68": 980, "69": 991, "70": 1001, "71": 1013, "72": 1022, "73": 1039, "74": 1051, "75": 1065, "76": 1076, "77": 1088, "78": 1101, "79": 1115, "80": 1125, "81": 1135, "82": 1146, "83": 1157, "84": 1175, "85": 1192, "86": 1210, "87": 1225, "88": 1239, "89": 1247, "90": 1258, "91": 1271, "92": 1288, "93": 1304, "94": 1316, "95": 1328, "96": 1341, "97": 1351, "98": 1361, "99": 1375, "100": 1388, "101": 1411, "102": 1421, "103": 1438, "104": 1456, "105": 1470, "106": 1481, "107": 1511, "108": 1526, "109": 1542, "110": 1555, "111": 1565, "112": 1587, "113": 1603, "114": 1617, "115": 1627, "116": 1651, "117": 1666, "118": 1681, "119": 1689, "120": 1700, "121": 1711, "122": 1729}
---

**Dave Jones:** Hi, welcome to the Apollo launch vehicle digital computer video. Yes, this is the LV DC board from an Apollo Saturn 5 rocket that took humans to the moon of course back in the 1960s.

**Dave Jones:** This was designed in the 60s and this comes by courtesy of fellow video blogger Fran Blanche and she's done some awesome reverse engineering stuff on this and I'll link to her videos down below and she passed this on to me to do something with and well, what am I going to do with it that she hasn't already done?

**Dave Jones:** Well, I've got myself a precision source measure unit. So I thought that I'd measure some of these semiconductors inside here and see if they're still working after all these years.

**Dave Jones:** This was designed and built in the 1960s. So are the semiconductors still viable in these things? Do they still perform as diodes and transistors? Well, let's find out. Now all of this Apollo hardware of course was state-of-the-art designed to get humans to the moon, a very difficult task and designing the early computers like this, this was groundbreaking stuff that really helped future computer technology, manufacturing technology, electronics, ICs,

**Dave Jones:** all sorts of things that we take for granted these days. A lot of it came from this sort of Apollo era hardware. So really fantastic legacy stuff we've got here.

**Dave Jones:** I love it. And as the name says, the launch vehicle digital computer is basically exactly as it says. This is the computer or part of it. It's one of the many boards that comprised the computer that controlled the Saturn 5 rocket as it launched, i.e.

**Dave Jones:** the guidance and everything else as it flew up and then was ultimately uh discarded and there's a a few of these littering the bottom of the ocean, of course, because well, the rockets just fell into the ocean.

**Dave Jones:** I don't think they ever recovered them, or they might have recovered some bits from them or something like that, but this one never flew, obviously, otherwise it would have we wouldn't have it in this sort of condition.

**Dave Jones:** And yeah, it's not in great condition because that friend has already done some work on it. She's deep hoted some of these chips and here's a photo of uh actually deep hoting these things.

**Dave Jones:** It wasn't pretty. They had a a pink sort of, you know, epoxy type potting side with a ceramic top and these these chips actually slide out from these little uh clips based on this board and it's a very complex manufactured board for its era.

**Dave Jones:** I mean, obviously, absolutely state-of-the-art for its time. And this is not a chip as you know them today. This is basically just got diodes and transistors in them. It's DTL diode transistor logic.

**Dave Jones:** And that's pretty much it, but we do actually have a data sheet for a couple of the these chips, so we do actually know the pin outs, so we can test them.

**Dave Jones:** You can hopefully see some of those clips there that held in these chips and they'll basically just slide in like that. Look at those vias. I mean, that's you know, not unlike what you don't see these days, but the construction technology of this board is very significantly different to what you'd see these days on a board, but on a physical, you know, typical printed circuit board these days, but

**Dave Jones:** anyway, look at those clips. Yeah, there's a lot of corrosion and gunk and all sorts of stuff on these things, but hopefully we can probe some of these things and or slide out a couple of these chips because we've only got data sheet on a couple of these uh parts, but we do know the pin outs, so we can slide them out and hopefully still be able to

**Dave Jones:** probe the metallized pads on the side of these things. So, right down in there, we've got to uh I slide them out intact. I don't know how easy that's going to be.

**Dave Jones:** Fran has actually done it, so uh yeah, well, I've got to give it a go, and I've only got a couple of shots at it, so well, fingers crossed, and whether or not we can still make contact to the metallized uh pads actually on that substrate material.

**Dave Jones:** Now, I have actually had a bit of success probing the back here, and even before I got the data sheet from Fran, I was able to actually uh probe out a couple of uh what appeared to be uh PN semiconductor junctions, i.e.

**Dave Jones:** diodes, um inside this thing just by random uh probing. And you'll notice that there's no traces on the bottom at all. These are all It's all internal layer stuff, so incredibly complex uh construction.

**Dave Jones:** This is a very multi-layer board. And uh as I said, you know, pretty different construction techniques, but not too dissimilar to the overall uh structure of what you get in a PCB these days, but yeah, nothing on the bottom whatsoever.

**Dave Jones:** It's got this sort of covering on it. I don't even know what that covering is, but we can actually chip that away. It's all been chipped away from this area down here.

**Dave Jones:** So, we'll just see if we can get a just a closer up version of this board. I'll switch on my uh Tagarno microscope here, and let's go to the videotape.

**Dave Jones:** All right, here we go. It looks fantastic under the microscope here, and here is the top view internal uh diagram of what's inside this inver- uh inverter module here, INV.

**Dave Jones:** We only have the data sheet for two of them, the uh inverter and this what's called the AA chip here. So, I've only got one inverter on this whole board, so ooh, fingers crossed, and two AA chips like this.

**Dave Jones:** And of course we can't measure them um in circuit because we'll get errors due to however it's wired inside. You know, so really we have to try and get the chips, slide them out of these connectors on here to try and access the pins on these things.

**Dave Jones:** And basically that's the internal circuit diagram. We've got one transistor, two back-to-back diodes here and some and some resistors. That's pretty much all that's inside this inverter module here and this is why they call it diode transistor logic, DTL, because it uses diodes and transistors and pull-up resistors and it forms your gates and your logic that way.

**Dave Jones:** So, there you go. That's inside that one and the AA module is even simpler than that. It doesn't even have any transistors. Here we go. These AA modules here, just a couple of back common back anode common back-to-back diodes like that going out to separate pins there with a 2.5k pull-up resistor.

**Dave Jones:** And what we can do is zoom in here and take a look at a couple of these chips that friends already depotted for us. Look at that. Oh, I love this Tagarno microscope.

**Dave Jones:** Very nice. And this one still has the chip in it. Look at that. You can see the chip there and physically these two pins physically connected. That one's going off there.

**Dave Jones:** So, that looks like a three-pin device. These have She's obviously accidentally or purposely ripped out the chips from these two here and you can see some of that potting compound still still in the corner down in there.

**Dave Jones:** Look at that. Ah. That's terrific. Can I zoom in any closer than that? That's the maximum zoom I can get on this Tagarno microscope yet. Look at that. So, it was potted with that whatever material that is.

**Dave Jones:** I don't want to know. Um, but you can see the metallized traces laid down in there. Very, very interesting. And if we angle that, we can really see those those clips there.

**Dave Jones:** Check it out, and it is horribly corroded and rusted. But, uh, hopefully can slide out these chips and then probe what's left of the metal. You can see parts of the metallized contacts still on there going inside the chip.

**Dave Jones:** And then they've then they've got this wall around it with a ceramic top on it, and then they fill them with that potting compound. And these clips are somehow welded onto these metallized pads down on the board.

**Dave Jones:** Interesting construction technique. And check that out. We can see down some of the vias in there. Look at that. See the wall of those. And as I said, manufactured in the 1960s.

**Dave Jones:** State of the art technology. Haha. Awesome. Shame it's not in better shape, but anyway, what do you expect? And there's some of the vias on the bottom side. And look at the this bottom stuff looks quite fiber-glassy.

**Dave Jones:** So, yeah, it's something like that. It does peel off relatively okay. I have chipped away a little bit of this, and it does does seem to come off. It's a bit easier towards the outside parts of the board.

**Dave Jones:** But, as you get in, gets a bit more difficult. So, it certainly is very interesting technology. I love this stuff. And, uh, no date code on this particular model.

**Dave Jones:** I can't remember if friends actually was able to get a date on this one or not. But, uh, that, folks, is 1960s Apollo technology. Ah, you got to love it.

**Dave Jones:** You know, it actually doesn't seem hugely difficult to clean up some of these pads here. I'm just using some isopropyl alcohol here, and uh that's cleaning up. Not bad at all.

**Dave Jones:** Check that out. I rather like it. There you go. Look at that. Like a bought one. Now, I do know that this was state of the art at the time, of course, but I can't help but think, why didn't they integrate this further?

**Dave Jones:** I mean, these chips that have got basically bug roll in them, an entire chip taking up this, and well, presumably, I don't know what the some of the other chips in here do, but say the inverter, for example.

**Dave Jones:** I mean, you know, we've just got like a couple of diodes and a transistor in there. Why didn't they, uh you know, this little um piece of silicon down here, well, why didn't they just make it a bit larger?

**Dave Jones:** I know that silicon manufacturing technology back then was in its absolute infancy, but uh and this was, you know, pushing the state-of-the-art technology, but I just I just can't help but think why they just didn't pack more functionality into one device like that.

**Dave Jones:** I mean, it's not like they had this, you know, gigantic die in there to do a transistor and a couple of diodes. I mean, look, you know, that that die in there is just one device.

**Dave Jones:** Why couldn't they just pack more of them in there and utilize all the pins? I mean, you know, we've got unused pins all over the state. I know it's like designed to be modular and things like that, and they have, you know, specific chips for specific purposes, but why they just couldn't do more, and I don't know.

**Dave Jones:** It just it just seems a bit limited to me, but uh you know, I mean, uh the uh the constraints of the time, they probably designed this much, much earlier, and then as technology improved, they couldn't just, you know, wham, let's just change it all, you know, 5 years into the Apollo program or something like that.

**Dave Jones:** So, really, they were probably uh stuck with what they had and uh it was good enough. It did the job. And what we've got here is an Agilent B2912A precision source measure unit or SMU or shmoo, as they're known.

**Dave Jones:** And we can use one of these to test the semiconductors to and actually characterize their voltage and current performance. I.e., get those characteristic curves that you see in the data sheets.

**Dave Jones:** I've done a teardown video on this. If you want to see it, it's a really interesting beast inside. Very expensive thing. And unfortunately, I've only got it for another uh day or two.

**Dave Jones:** So, I've got to send it back. But hopefully, we can probe some uh semiconductors here. See if they're still usable. Let's go. Now, I won't bore you with the details of how exactly shmoos work and how to set them up.

**Dave Jones:** But uh we'll start out with just measuring a basic modern uh 1N4148 diode here. And this is what we get. So, then we'll have a baseline of uh instrument setup to work against to uh characterize the diode performance inside these Apollo era chips.

**Dave Jones:** So, here we go. If we probe it and we press measure, boom, there we go. We've taken 100 sample points and we get our characteristic diode curve. There it is.

**Dave Jones:** Starting to ramp up at about 0.6 V here, going all the way up. So, that's what we'd expect of a typical uh diode from the Apollo era as well.

**Dave Jones:** I mean, you know, the voltages and currents and everything else might uh change a little bit, but we basically expect that PN junction characteristic curve shape. And what I'll do is I'll use these uh really fine pointed springy probes here.

**Dave Jones:** So, they can get decent uh pressure down on just the individual pins down in there. So, I'll be able to probe, hopefully, and get through any uh oxidized uh coating on those pins or anything like that.

**Dave Jones:** So, I'll start out just by trying to measure one in circuit on that uh inverter chip. Well, looky what we have here. It's a similar sort of characteristic curve, but not nearly sort of the voltages we expect.

**Dave Jones:** I've got five zero to five volts on the x-axis here, but it does actually curve up like a PN junction. I measured this one in circuit, of course. Just one of the diodes inside the inverter chip.

**Dave Jones:** And you know, from zero to 50 milliamps is the test currents I put in. And well, we're getting huge, you know, that's a large voltage drop across these diodes.

**Dave Jones:** I'm not sure what we would expect for the era, but you know, they've got to be like, you know, silicon or germanium technology or something like that. So, I wouldn't expect it anything like that.

**Dave Jones:** I would have expected it to ramp up, you know, similar to what we saw before. At least, you know, maybe a volt or something like that based on the current even, you know, volt and a half, something like that.

**Dave Jones:** So, that seems grossly out, but that could be because we're in circuit. We got one! Yes! Check it out. I probed pins uh one and eight here. Here we go.

**Dave Jones:** Pins one and eight of our inverter chip. And this is what you'd expect. This is a diode characteristic curve. Starts ramping up at our silicon diode characteristic curve. Starts ramping up about 0.6, exactly what the modern 1N4148 does.

**Dave Jones:** And at 50 milliamps, okay, we've got 1.1 volts drop. Okay, so it's not a particularly high current diode or but that bingo! It doesn't maybe that is not connected to anything else in circuit.

**Dave Jones:** And we have ourselves a a classic diode characteristic curve there. This chip still works. The semiconductor inside still works after all these years straight from the 1960s. Beauty! What a Bobby dazzler!

**Dave Jones:** This actually works. I can't believe it. So, if we probe these again, it really is rather a bit tricky. I've got to sort of hold it with two hands like this and get the tongue at the right angle.

**Dave Jones:** Here we go. Tongue's at the right angle. And there we go. It is really quite tricky to get the contacts right on this thing. And yeah, look, you end up with like little wiggles in here like this if you don't get the contacts right.

**Dave Jones:** I'll uh print screen that and I'll show you that one up close. And yeah, you get these awful little wiggles in there and stuff like that. You know, just through the at the microscopic level of how you're actually probing these things is you all sorts of weird and wonderful stuff.

**Dave Jones:** So, you really got to use these really sharp probes and also the ones with the pressure with the spring-loaded ones as well really quite help to you know, try and pierce these things and keep an even pressure on that joint.

**Dave Jones:** So, can't get it though. Fantastic. Well, this is a bit of a wimpy test, I think. We're only talking like 0 to 50 milliamps I'm testing this thing at.

**Dave Jones:** This is capable of a couple of amps at hundreds of volts. So, let's ramp it up. So, I'll ramp up my current limit. Here we go. Start from 0 amps.

**Dave Jones:** It's going to go up to 1 amp in I've got like 100 steps in there, which is more than adequate to get the resolution on our graph and a compliance voltage where it'll cut out at 10 volts.

**Dave Jones:** So, let's give that a whirl. If we break it, we break it. Wow, look at that. That's a rugged little bastard, isn't it? Look, 1 amp and we ramped it all the way up.

**Dave Jones:** Didn't blow at it. Well, presumably I haven't run it a second time. Those wiggles, as I said, are just little contact issues in there. We can actually get it to do straight if we probe it well enough, but yeah, it basically still ramps up at that 0.6 volts and then basically a completely linear region right up here.

**Dave Jones:** Yeah, sure we're getting like a 4. uh 2 or 4.3 volt drop at an amp, but gee, you can't blame it. Nice. Let's ramp it all the way up.

**Dave Jones:** And I've gone for these beefier uh probe master probes for the higher currents. Once again, these are incredibly sharp tips, but they got no uh spring point on there and they got nice finger grips on them so I can really get in there and probe the pins like that solid.

**Dave Jones:** And this is what we get. And I had a compliance voltage of 5 volts here. So, that's why it's crapped out there, but you can see how we had that linear ramp before, almost linear.

**Dave Jones:** It sort of sort of starts to taper off a little bit as it approaches 1 amp there at 4 volts and then it really starts to tail off. So, we're really losing the non-linearity of the diode here.

**Dave Jones:** So, really its operational range sort of seems to be like, you know, not even an amp, maybe sort of, you know, to be conservative, I'd say probably, you know, like a half amp rated diode or something like that.

**Dave Jones:** So, as you'd expect, these things are designed for low current you know, operation cuz these are a digital computer. They're you know, working in the order as we saw in the schematic before, order of like, you know, several K to sort of 10s of K pull up resistors, stuff like that.

**Dave Jones:** So, we're really just pushing this thing silly to see where we break it at the moment. It's not really a half amp or 1 amp operational diode. That's for sure.

**Dave Jones:** And there we go. Look at this. This is interesting. I changed the compliance voltage to 10 volts here. So, um and still I'm ramping from 0 to 1.5 amps here.

**Dave Jones:** I stopped at 1.5 amps. And look at this. Here's a what we saw before with the sort of the 1 amp curve like that and it starts to taper off as we saw, but then it starts to taper back up.

**Dave Jones:** Look at that. So, there's some weird characteristic going on there. Now, it's actually better off if I don't kill this thing. So, what I'm going to do is I'm trying to get get and try and slide out this inverter chip here.

**Dave Jones:** It's the only one that I've got. So, I've only got one shot at this. So, basically, I've got to remove several of these other pins around here just so that I can sort of can I get the iron in there and yep, yep, no problem whatsoever.

**Dave Jones:** So, I can get rid of these and that'll help me slide it out, of course, otherwise they will be in the way. This is not elegant by any stretch and uh not recommended for repairing Apollo era boards.

**Dave Jones:** This is not an approved repair technique. So, please, no flame emails or comments. And there you go. There's one of those little clips designed to like a weld at the bottom part of that was welded onto the board in some way, shape, or form.

**Dave Jones:** And then yeah, they were just designed to clip into those modules. So, that has seen better days. And here we go. What I want to do is I'm going to try and sort of lever it under this end and slide it out this direction.

**Dave Jones:** And the good thing here what I was probing before, I was actually probing pins one and eight here. Yes, they're not labeled in the usual way, but that's what they're well, the modern way we're used to here.

**Dave Jones:** But pins number one and eight. So, I really only have to slide it out a little bit and then it's not making contact with there. I just You can see idea here is just to slide the chip out.

**Dave Jones:** So, then we can possibly get access to the top of those pins in there without having it in circuit. I just want to re-verify that diode in there, that PN junction.

**Dave Jones:** Just absolutely sure it's not in circuit. And here we go. It's time to brutalize it. Yes, this is awful. I'm getting my screwdriver in here, but I just want to see if it budges.

**Dave Jones:** It does budge. Look. It does budge. I'm probably going to I might destroy this chip here, but if I can slide this puppy out. Yeah, there we go. Slide in.

**Dave Jones:** Slide in. Maybe if I come in this angle and ta-da! We're out. We're out. There we go. That's good enough. And I should be able to now get in there and probe if there's any of those pads left.

**Dave Jones:** I don't know. They I don't know. Presumably they were just like press fit on there, but who knows? They may have corroded off. So, hopefully, well, we'll see if we can get in there and access.

**Dave Jones:** You can see this top one has some metal left on it by the looks of it. Not entirely sure about the bottom one. It could just be more looks than anything.

**Dave Jones:** Oh, well, we'll see if we can still probe it. If we can't, oh, well. And yes, bingo, we got it. Look at that. It is basically exactly the same as what we got before, ramping up at about, you know, 0.7 volts or thereabouts.

**Dave Jones:** And uh sort of half an amp, we're looking at like, you know, 2.2 volts or something. And then it's ramping up to an amp. I didn't take it any uh higher than that at this stage.

**Dave Jones:** And you can see it tapers off there. So, that one was pretty much uh if it was in circuit, there really wasn't uh any major effect there on it.

**Dave Jones:** So, that is the characteristic curve of a 1960s era Apollo uh chip, one of the one of the very first uh semiconductor chips ever made. Fantastic. And yet, there we go.

**Dave Jones:** I ramp it up to 1 and 1/2 again. We get exactly the same as what we got before, that little contact wiggle in there. and uh that's it. So, that's the characteristic curve going up to 1 and 1/2 amps, grossly overloaded to what this thing was designed to do.

**Dave Jones:** It's That's a bit mean. And there is the chip actually fully removed there, and we can see the bottom of that. Here we go. Nobody's seen the bottom of that uh chip since it was installed back in the 1960s, and it's got some sort of uh sort of, you know, paint or some sort of epoxy-type base on it.

**Dave Jones:** And I tried to measure some of the other internal resistors in there to see if we could get a linear uh response out of them, and I couldn't get anything.

**Dave Jones:** It's like there's no internal contact in there at all. I tried three different resistors and couldn't get any of them. It was just flatlined. Uh I couldn't get the uh linear slope that we expect out of a resistor, but I've actually done this uh previously, probed around in circuit, and I did actually find one on the board.

**Dave Jones:** I just can't find one in this inverter. So, let me show you the one I found previously. So, according to my notes here, uh that pin there and that pin there and that one and that one over there should be uh to both of those should be 4K4 resistors.

**Dave Jones:** And here we go. This is really easy to probe. The back here it just goes straight down the via holes, nice. And we'll measure that. Bingo! There's our straight-line characteristic curve of a resistor.

**Dave Jones:** That's from 0 to 10 V, completely linear, exactly what you'd expect from a resistor. I can take that to higher voltage. Why not? I feel ashamed to do this to a classic Apollo era board, but here we go.

**Dave Jones:** 0 to 100 V on this poor little resistor. Let's go. Ah, out of range. What? Fail. Uh unfortunately, this bloody SMU has got an interlock uh uh circuit on it, so you can't go over 42 volts on the output unless you uh connect some digital interlock thing, and I read the manual, it didn't give me pinouts for the connector on the back where I have to connect the interlock and all that

**Dave Jones:** sort of garbage. Ah, well. Anyway, we went from 0 to 40 volts, and it's completely linear right up to 40. Awesome. And well, to get back to where this thing is realistically used, I mean, 0 to 20 milliamps, for example.

**Dave Jones:** Look, I mean, classic diode characteristic curve, perfectly fully functional diode even today, even at 20, you know, 20-odd milliamps, about 0.9 volt uh drop. Down at 5 milliamps here, only about, you know, 0.77 volts drop or something like that.

**Dave Jones:** Perfectly adequate diode for then and now, really. Yeah, it's not crash hot, but for the just the signal operations that they wanted this for, uh DTL-type stuff, diode-transistor logic computer stuff.

**Dave Jones:** And if you're curious to know the leakage there, no, basically bugger all. Of course, you just put the diode in reverse from 0 to 10 volts there. It's, you know, basically like in the order of uh 0.1 uh microamps.

**Dave Jones:** So, pretty much on par with a 1N4148. So, there you have it. That's a 1960s-era Apollo launch vehicle digital computer logic board. Fantastic. And the diodes and resistors, and you know, the uh deposited resistors and everything in it, still work, and they're still functional.

**Dave Jones:** Fantastic. So, you got to wonder, if you kept these things in pristine condition, those uh Saturn rockets that are still There's a few of these still sitting inside the Saturn rockets, I believe, that are inside the museums that you can go and see the remaining ones that they actually built.

**Dave Jones:** They would probably, good chance that the majority of them would still work today. Uh yeah, you'd probably have a few issues. You might have to swap a few boards or something, but hey, that's pretty awesome for 1960s era technology.

**Dave Jones:** I love it. And that's a perfectly usable diode characteristic curve. Uh yeah, sorry I don't have the uh time or uh anything to measure the uh transistor inside this thing.

**Dave Jones:** It was hard enough getting the damn diode, but uh the deposited resistors in here, perfectly fine and linear. Diodes, fantastic. So, it still works. My thumbs up to two thumbs up A to the uh Apollo era designers who pioneered all this stuff we take for granted these days.

**Dave Jones:** And this is one of the world's first earliest, you know, fully integrated uh digital, you know, IC-based computer. I mean, amazing. They've only got a couple of diodes, couple of transistors per chip.

**Dave Jones:** Now we're talking, you know, hundreds of millions of transistors per chip is just in our phone and in our watches. It's crazy stuff. But anyway, thank you very much uh Fran for loaning me this fantastic vintage board.

**Dave Jones:** And the idea was to pass this thing around to other people to do other stuff with. So, I think, you know, I've done my little part. I've used my source measure unit.

**Dave Jones:** Sadly, this has to go back to Agilent in a day or two. And uh yeah, so we confirmed that this thing still works or is still viable today. Fantastic.

**Dave Jones:** So, if uh you want to want this thing, I'll pass it on to you. And if you've got an idea of some videos you want to uh do, of course, it has to be made uh public, all the info and uh videos of it.

**Dave Jones:** But if you do, if you want it, please contact me. Thanks, Fran. And I'll link to Fran's uh videos and her blog page down below as well. And she's got a new uh podcast uh thing, a new uh video show happening with Bill uh Heard, I believe.

**Dave Jones:** So, check that one out, too. It'll be linked in down below. Catch you next time.
