---
video_id: NnBPLuw-LnY
title: EEVblog 1398 - Western Digital RED 6TB WD60EFRX Hard Drive TEARDOWN
url: https://www.youtube.com/watch?v=NnBPLuw-LnY
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 30, "3": 44, "4": 63, "5": 75, "6": 90, "7": 106, "8": 137, "9": 152, "10": 162, "11": 179, "12": 198, "13": 215, "14": 239, "15": 245, "16": 255, "17": 267, "18": 274, "19": 292, "20": 311, "21": 320, "22": 332, "23": 349, "24": 359, "25": 378, "26": 389, "27": 402, "28": 420, "29": 433, "30": 443, "31": 453, "32": 465, "33": 477, "34": 486, "35": 499, "36": 510, "37": 521, "38": 538, "39": 549, "40": 568, "41": 584, "42": 607, "43": 616, "44": 626, "45": 640, "46": 652, "47": 660, "48": 672, "49": 687, "50": 695, "51": 704, "52": 719, "53": 729, "54": 743, "55": 761, "56": 773, "57": 788, "58": 795, "59": 807, "60": 821, "61": 833, "62": 849, "63": 864, "64": 882, "65": 896, "66": 905, "67": 920, "68": 929, "69": 940, "70": 954, "71": 967, "72": 979, "73": 991, "74": 1005, "75": 1020, "76": 1034, "77": 1048, "78": 1060, "79": 1070, "80": 1080, "81": 1091, "82": 1106, "83": 1117, "84": 1131, "85": 1137, "86": 1151, "87": 1167, "88": 1182, "89": 1193, "90": 1202, "91": 1218, "92": 1231, "93": 1242, "94": 1254, "95": 1276, "96": 1286, "97": 1299, "98": 1316, "99": 1328, "100": 1341, "101": 1353, "102": 1363, "103": 1377, "104": 1388, "105": 1396, "106": 1407, "107": 1432, "108": 1444, "109": 1458, "110": 1479, "111": 1494, "112": 1509, "113": 1527, "114": 1539, "115": 1558, "116": 1568, "117": 1579, "118": 1593, "119": 1610, "120": 1622, "121": 1636, "122": 1647, "123": 1665, "124": 1673, "125": 1691, "126": 1712, "127": 1731}
---

**Dave Jones:** Hi, it's teardown time in glorious 4K resolution if you've got the option to watch it like that. Anyway, we're going to a Western Digital WD60EFRX for those playing along at home, 6 TB Western Digital Red hard drive that I had in my NAS here.

**Dave Jones:** And if you've been following me on EV blog too, and you should be cuz that's where I dump a lot of interesting videos. And I'm almost like I'm only a couple of thousand away from 100,000 subscribers and getting that YouTube silver award.

**Dave Jones:** So, you know, please give me a sub on EV blog too. Anyway, if you've been following along the saga and on Twitter as well, this is a drive that failed in my four-drive DS418 NAS Synology NAS drive.

**Dave Jones:** And basically, it's it had been there for just over 3 years. Yes, it's literally 1 month out of warranty. It had like 26,000 26,000 operational hours, but technically, I looked at my old receipts and yes, 1 month out of the 3-year warranty.

**Dave Jones:** Doh! Anyway, everyone said that they wanted to see a teardown of this. So, I might be able to still get like a warranty replacement for it. Maybe if I just, you know, fill out the form, maybe they'll send me a new one.

**Dave Jones:** But anyway, a lot of people wanted to see it. So, I'm going to sacrifice this puppy cuz you do have to return them under warranty. So, and you see the build date here, 18th of January 2018, but it has been in like 24/7 operation in my NAS.

**Dave Jones:** As I said, like 26,000 odd hour operational hours. The specific model we've got here, the EFRX, this is actually what's called a CMR or continuous magnetic recording drive. It's the technology used to actually write the bits onto the platters itself inside.

**Dave Jones:** And anyway, Western Digital, like they all were CMR, but then they sneakily in their Red series drives changed them to SMR or shingled magnetic recording drives, which isn't as good and it's apparently much slower than CMR drives because in shingled magnetic recording, the adjacent tracks actually overlap each other, hence why it's called shingle, just like shingled roofs, you know, the shingled tiles overlap each other and apparently when you write a

**Dave Jones:** byte to this a bit to this, you've got to actually write the two adjacent bits as well. Not this one, as I said, this is CMR, but the EFAX version, which I did actually unknowingly have one of these in my Synology NAS drive wise.

**Dave Jones:** So yes, I am going to eventually replace that, but I have to reconstruct or resync my drive first with a new CMR drive, which is on the way and then I'll replace the SMR one I've got with the CMR.

**Dave Jones:** Anyway, it's actually the CMR one that failed, not the SMR, which a lot of people claimed. So anyway, that was just like an interesting aside. Western Digital have now admitted that they did that and now the new the reds the SMR and the red plus is actually the CMR type.

**Dave Jones:** So the new ones I've ordered red pluses. So anyway, let's do a teardown of this bad boy and see I will here's a video I will now try and record the sound from it, but unfortunately I just did that and it's not as bad as it was.

**Dave Jones:** But anyway, here's the video. Sound is nowhere near as bad as it was before. It's not sounding normal. Can hear this right across the other side of my lab when when it was failed in the NAS.

**Dave Jones:** The noise, you can't hear these things. Yeah, that's not as bad as it was, but it's still pretty bad. Like it should not be that loud. I haven't heard a hard drive that loud since like the 1980s, 1990s.

**Dave Jones:** So, anyway, here's the bottom of the drive for those playing along at home. There's no bodge wires. There we go. We've got a flat flex going in there. That's to drive the motor.

**Dave Jones:** That's a four-wire jobby. That's all gunked up. That's a not a hard potting compound, not a soft one. And, you know, do not block hole. It's got various vents or whatever.

**Dave Jones:** I haven't torn down a hard drive in donkey's years. Anyway, I'm like screws under there warranty seal screws or whatever. But, and for those curious, no, there was no indication that this was going to fail.

**Dave Jones:** There was no bad sectors or anything like that. None of my other drives have any bad sectors. So, that's not an issue. Oh, that just Oh, that's that's nice.

**Dave Jones:** I like that. No cabling whatsoever. Just a board-to-board pressure contact. Look at that. That's beautiful. Got some foam in there. It's just for some anti-vibration stuff so that the you know, board doesn't contribute to any vibration noise I would presume.

**Dave Jones:** So, yeah, I like that. So, that's stuck down. Let's take that off. So, yeah, no no indications at all that this thing was going to fail. All I heard about it was that all of a sudden I was writing some video to it cuz this NAS drive I actually do read write edit all of my video on this NAS drive.

**Dave Jones:** I don't edit video locally. It's all done on my external NAS. And no, it's not slower to do that. Trust me, I've done videos on that. Anyway, yeah, so that's pretty cool.

**Dave Jones:** And we've got another pressure contact over here on the for the motor drive as well. And they've got a That's also buggering off into there. So, that's interesting. I'm not sure why they're going off under there.

**Dave Jones:** Is there another They're all in parallel. So, huh. Anyway, there you go. There's the main board there. I've taken off the thermal pad on top of that. So, like I won't go into any into any details on the chips of the designer or anything like that, but that looks very nice.

**Dave Jones:** No worries whatsoever. You can explore that in your heart's content in 4K resolution. There you go. It just gives you some additional detail. Not sure if you can see the part number on that.

**Dave Jones:** If anyone cares. All I want to see is the big gouge taken out. Hopefully taken out of the platter inside this thing cuz when you get the grinding noises like that, the old click of death from these things, then yeah, that's the head doing some nasty business against the platters inside.

**Dave Jones:** I don't know how many platters these modern 6 TB drive use. Got no idea. We'll find out. Take out that. Yep. There's the other screw. So, I'll take out all of them.

**Dave Jones:** No, you only need one, don't you? Really? I mean, you can't, you know, you can't take out every single screw to take this off. I guess it's just harder to fake, you know, six of them instead of like five of them or whatever instead of one.

**Dave Jones:** Now, of course, this is not something that you'd ordinarily do in a just a normal lab with normal air and stuff like that because if you get any dust and crap in there, yeah, you'd want to do this in a relatively clean air environment if you are like looking to get the data off it or repair it or do whatever.

**Dave Jones:** But yeah, not one care given here. But anyway, yeah, you can probably see they've got some sort of gunky seal under there like that. So, I've missed a screw under here.

**Dave Jones:** Oh, yeah, might have. Sneaky bugger. Yeah, isn't there a bloody another one under there? And this one looks like it's smack in the middle of the platter. That's kind of important.

**Dave Jones:** Now, I thought there was another one under there. That's an air vent, is it? Yep. Pretty sure that shiny thing in there is the platter. Sure there's some trick to this.

**Dave Jones:** I don't know. Sorry. Don't take this video as how to take apart hard drives. It's not my business. I did expect there to be a lot of force on that uh rubber gasket holding it Oh, yeah.

**Dave Jones:** Yeah. Yeah, there you go. I think you need a big wide-ass screwdriver like I'm using at the moment. That seems to be the go. Yeah. Yeah, it seems to be popping.

**Dave Jones:** Okay. Yeah, can't use the little piss ant one I used before. Once the seal's off, yeah, it's done. Come on. You can do it. Tada! We're in like Flynn.

**Dave Jones:** Look at that. There's our platters. Jeez, there are uh quite a few platters. Let's have a look on the bottom. There's some sort of pad, I guess, to stop it I I if there is any vibration or wobble in there.

**Dave Jones:** I don't know. Like a you know, these are incredibly, probably the most complex mechanical device you own would be a hard drive. I I think there's probably no doubt in that.

**Dave Jones:** All right. There you go. Yeah, that's our big rubber seal around the thing. It's like uh it's like it's not even rubber. It's some sort of gel kind of I don't know.

**Dave Jones:** If anyone knows what type of stuff that is, yeah, let us know. And silly me, just put a mark on the uh platter. There it is. That's the mark on the platter that, unfortunately, um yeah, dumbass Dave, you probably screamed at the camera, that came from this, which was um yeah, don't do that.

**Dave Jones:** Anyway, good thing is I'm not trying to recover the data from this thing. Well, I don't see any damage to that top platter. All right. Yep, highly reflective these things.

**Dave Jones:** But um no, I expect to see like some maybe some big grooves taken out of this thing somewhere. So, there you go. You can see the entire platter. Of course, it's going It's just going to reflect absolutely everything cuz these are the mirror finish on these is just absolutely incredible.

**Dave Jones:** And there's our head array. Five six um arms on there. So, that would would uh 12 surfaces. so six platter, uh 12 surface on there. So, beautiful. And uh yeah, there's a little parking frame over here for the heads.

**Dave Jones:** Very nice. And of course, like the As I said, the technology which goes into these is absolutely incredible. The most precise engineered product uh that you'll ever buy. It's just like People don't realize the insane materials technology, the engineering, uh the production technology that goes into making these hard drives.

**Dave Jones:** And 6 TB is, you know, not a big drive these days. You can get much bigger and denser. And you can get them in smaller form factors and all sorts of things.

**Dave Jones:** Um and yes, they do contain uh very powerful neodymium magnets. So, uh yeah, you can get those out and have some fun down in there. You can see the coil.

**Dave Jones:** Just a uh like a DC servo motor. These are all like these aren't stepper motors, I believe. These are like uh you know, DC servo uh controlled. And it's just like I don't know the resolutions involved in something like this, but it's absolutely ridiculous.

**Dave Jones:** So, I'm going to say not a huge amount in there, but a huge amount of technology goes into that. Um it's just absolutely incredible. Anyway, unfortunately, Murphy says that the top of this disk does not have any marks.

**Dave Jones:** Of course, it doesn't. So, we're going to have to go further. But what I'll do is I'll actually plug it in like this. See if it does anything. Now, I assume that these are like filled with an inert uh gas.

**Dave Jones:** Um let me know in the comments down below. There we go. And there would be no um sensor I don't know what they'd be a And are they pressurized?

**Dave Jones:** Would there be a pressure sensor in there? Probably not. Oh, there we go. It's seeking. Beautiful. Geez, it sounds much louder without the uh case on. Oh, it's going back to park.

**Dave Jones:** Oh, is that normal? I don't know. Does anyone know? There you go. It's trying to the business. It's trying to like read the exact point. Is that where it keeps the disk index or whatever?

**Dave Jones:** But yes, this this drive does not work at all. And I think this is only like 5600 or 5200 RPM or something like that. It's not one of the fast jobbies.

**Dave Jones:** There you go, it's working doing its thing and it's just done the shutdown and it's going to stop spinning, stop spinning, stop spinning, stop spinning cuz it's realized that whether or not Windows shut that down or whether or not it's it's done that of its own accord.

**Dave Jones:** If you do know that, leave it in the comments. But there you go. Um yeah, it I want to see the gouge. That's little on a little compliant mount.

**Dave Jones:** Maybe I can take that out. Well, hello. Do we have a little desiccant bag in there? That's got to be a desiccant bag, right? So yeah, to keep the moisture out of this sucker.

**Dave Jones:** Hmm. Aha, of course. That assembly there is just the interface from that flat flex. It's just to hold the flat flex in place. It does absolutely nothing else and then it Yeah, and then it just folds over and goes over to the the head.

**Dave Jones:** So that's all the head and motor drive. You can see the the thicker traces in there versus the thin. Of course, the I assume that the head amplifiers, you know, they're all going to be in there.

**Dave Jones:** It's not going to get all those teeny weeny little signals all the way back over here, I don't think. Now, I'm totally unsure how these platters come out and I'm sure there's a lot of people who have disassembled these and they're probably screaming at me, "Do this step, Dave.

**Dave Jones:** Do this step." or whatever. I'm just going to wing it. Haven't looked at any guides. Have we got some screws on top there? So maybe we've got to take them out one by one.

**Dave Jones:** Suck it and see. Once again, this is like I don't care. I'm not trying to save data here. Woohoo! That's fun. Yeah, you probably shouldn't do that, but well, the heads are parked.

**Dave Jones:** Why not? As you'd probably expect, those are really Loctited Oh, they're Loctited in there. Wow, tight as a nun's nasty. Actually, I don't see any evidence of Loctite on those.

**Dave Jones:** That's um it's rather surprising. Although, I guess you don't want to be applying liquids around hard drives like this in this sort of process. Geez. Oh, this is ridiculous.

**Dave Jones:** Yeah, imagine being the design engineer that actually proposes, "Oh, let's put some Loctite on those." And the production engineers are just going, "What? Give me a break. You want us to put liquids around these platters?" Well, this is totally not fun.

**Dave Jones:** I can assure you. Come on. Bastard. There's got to be an easy way to do this. There's no like locking point that I can find. Anyway, I just took out that head parking thing and I did sort of scrape the heads as I took them out.

**Dave Jones:** So, yeah, it's probably not the correct assembly step. There you go. There's the teeny tiny heads. Double-sided, of course. And yeah, going to get medieval on its ass. Can they actually spring apart?

**Dave Jones:** Like that. You know that? Springy springy. Science that goes into the engineering that goes into the aerodynamics of these heads and how they uh rest on the surface and stuff is um yeah, really something.

**Dave Jones:** Do actually have another seal on the bottom of the case under the PCB here. Let's take that off. Oh, there you go. That's the bottom of the platter. So, that's rather interesting.

**Dave Jones:** That accesses like it's obviously something to do with uh some sort of production testing, production alignment, uh you know, inspection, you know, physio-optically inspect the heads as they scan the surface or something like that.

**Dave Jones:** I don't know. Anyone knows? The center of the platter is here and then the head just Here's the head motor here and it just sweeps the head across like that.

**Dave Jones:** It's now got Oh, I got a fingerprint. Fingerprint. Oh, no, it's ruined. Care factor zero at this point. So, yeah, anyone know why that's there? Uh, let us know.

**Dave Jones:** Good news is it looks like I can unscrew the head assembly by taking this puppy off and then the So, the head assembly should now come out. Now, unfortunately, the final screw in there seems to be stripping.

**Dave Jones:** Okay, what I've done is looked at this screw under the microscope and like a T7 like it fits and it feels fantastic. There is actually a tiny bit of play in it.

**Dave Jones:** So, and and a T8 doesn't fit. So, it's almost as if there's a T7.5 or one of the Is there an imperial rubbish? I don't know. I've never encountered that.

**Dave Jones:** Um, but yeah, I cannot get that bloody last screw out and it's just stripping now with the T7 that got all the others out. And of course, I just noticed the two notches in there.

**Dave Jones:** Clearly, there's a custom tool designed to go into the center and then hold in those two points to stop this sucker spinning around. And I do believe we can actually get that out of there.

**Dave Jones:** Watch it snap back. Now, those neodymium's Whoa. There we go. There we go. Got it. Got it. Beautiful. Now, I can access the screws and actually get the head out.

**Dave Jones:** Yeah, that's one powerful magnet. So, yeah, that's a keeper. So, you can now see the coil which is an interesting what trapezoidal kind of like but it's bowed at the bottom and I don't know what shape that is.

**Dave Jones:** Does that officially have a name that shape? But uh yeah, that would be once again highly engineered. Um it's probably not that shape by accident. So, now we can actually lift that out of there.

**Dave Jones:** And of course, we're going to have the magnet on the bottom. Ta-da! There's the entire head assembly. Wow, isn't that fantastic? Here you can see the thickness of the coil there.

**Dave Jones:** You can see all the turns on that. And yep, there's our other magnet assembly. So, does that just lift out? Comes out somehow. All right, let's have a quick look at the head under the Tagarno microscope.

**Dave Jones:** Now, it's all Yeah, that's just the flat flex interface like that. There's nothing else on there at all. And uh that's just a holder for all the flat flex.

**Dave Jones:** There's our head amplifier silicon. There you go. Because there wasn't the number of connections required to actually do that. And there we go. There's our head driver chip. So, that's a chip on flex uh technology.

**Dave Jones:** They've got the gunk around there just to keep the moisture out and whatnot. And uh yeah, you can see all the traces coming in here from the head. And then there's only a few going out here which goes across the flat flex to the main PCB.

**Dave Jones:** So, of course, you can't have the uh you know, the tiny output from the heads. I mean, the the signal levels are Oh! Ooh! Careful. Yeah, I'm going to break these anyway.

**Dave Jones:** Anyway, the signal levels from the head are incredibly small. Um so, yeah. Um you need a custom head amplifier ASIC there. There's nothing else on there. Oh, there's one one bypass cap.

**Dave Jones:** And that's all she wrote. And there's our head drive uh coil there. And that's it. There's no other feedback on the head drive coil by the looks of it.

**Dave Jones:** So, yeah, we've got all our test points here. And check this out though. This is interesting. These large traces here seem to have like large little chunks taken out of them around the bend there.

**Dave Jones:** And I haven't seen that before. I I can't see how that's sort of any controlled impedance type thing. So, I'm left to imagine that's a mechanical stress kind of thing on the flat flex.

**Dave Jones:** I don't know. Um if anyone knows for sure, please leave it in the comments. Anyway, isn't that beautifully machined? I mean, absolutely fantastic. That's all machined in one block.

**Dave Jones:** Look at that. That is not joined or anything, right? Wow. How do they do that? That is remarkable. Oh, jeez. That's a bit How you doing? Check out the wires just going down to the coil.

**Dave Jones:** Oh, no. There you go. Oh, no. I thought that was soldered down there, but it's not. They just go into some um insulated sleeve in there. Anyway, you can see the thickness of the coil there.

**Dave Jones:** There's lots of turns in that. Those playing along at home want to count that? Knock yourself out. It's so the head plate, that's actually attached on the underside of cuz this is all part of the big machined part, right?

**Dave Jones:** So, that's actually head's actually attached to the underside of that. So, are these these big test pads on the top? You can see this is going off to uh some test pads here.

**Dave Jones:** And you can see that the trace is actually split around this gap in the um in the head in the part of the metal there. I'm not sure why that's the case.

**Dave Jones:** Is that aerodynamic reasons or something? Yeah, I can only assume that's aerodynamics. Anyway, there's our head. Might have to sacrifice one of them. Might have to Well, yep. That one's gone.

**Dave Jones:** Oh, no. OH, NO. COME ON, gutsy there. Believe it or not, that's actually maximum zoom. Now, you can see that the ferrite head, I mean, there's amazing material science technology going on inside these ferrite heads in here.

**Dave Jones:** So, there's another close-up of the head. You can see how tiny that is compared to my fingerprint. Wow. Yeah, that's amazing. And yeah, it's all flat flex, of course.

**Dave Jones:** There's a lots of Once again, there's lots of aerodynamics in this. There would be a lot of engineering that goes into the aerodynamics to to make sure these heads actually uh just float above the surface.

**Dave Jones:** So, that's uh yeah, that's really something. Wow. If you think you understand the every aspect of the engineering that goes into this, you're probably wrong. Third like 40 years, 50 years of advancement in technology.

**Dave Jones:** I've still got somewhere the magnetic recording handbook. It's this thick. Almost a well, a lot of it's not obsolete, but uh in terms of like manufacturing technology, it would be.

**Dave Jones:** So, so yeah, these heads are just amazing technology. Absolutely amazing. So, yeah, there you go. But yeah, there's no feedback on that coil at all. Yeah, that that is one machined piece, isn't it?

**Dave Jones:** Wow. That's great. How much does it cost to turn out one of those? Any Any machining experts out there? Is it It No, it did have to be cast, wouldn't it?

**Dave Jones:** It did have to be cast. You wouldn't machine that properly, right? In fact, it doesn't look like there's machining uh No, there's machining marks on the top. For all the world, look like machining marks.

**Dave Jones:** Did they just like polish it off? I don't know. If anyone knows, is it a combination of cast and machine or something? I don't know, but that's yeah. That's I guess that's the only way you can get the rigidity on on that head and the arms and everything.

**Dave Jones:** It's absolutely remarkable. So, yeah, there's not much in these things. It's uh it's just the platters and the head assembly and that's that's it. All the electronics is outside.

**Dave Jones:** Yeah, there we go. You can just pull that out. So, we've got the matching assemblies. I won't try and snap them together because uh yeah, it could be quite dangerous.

**Dave Jones:** These are incredibly powerful and of course um yeah, rare earth metals used in these and well, I think uh isn't China the dominant player in rare earth metals? Um yeah, very precious resource.

**Dave Jones:** Trigger warning. Look away now. Think I got it. Winner, winner, chicken dinner. Wow, that was a real bastard, that one. Ta-da! There we go. We're in. There's our separator for each one.

**Dave Jones:** So, nothing on that one. Beautiful. Look at that. I mean, polished mirror. That's just incredible. Wow. Anyway, so that's one. Now, we There we go. That is not a magnet uh by the way.

**Dave Jones:** That's just like that's just a machined brushed aluminum, is it? Something like that. Yeah, that's just a machined bracket. How precisely that has to be machined, I don't know.

**Dave Jones:** Anyway, our next one down also doesn't have any evidence of a head crash. Maybe we're not actually going to see That'll be disappointing. After all this, I'm going to be incredibly disappointed not to see a big gouge taken out and a big head crash.

**Dave Jones:** These are going to get increasingly hard to Ah, take out, I suspect. Now, third one looks okay, too. Yep, no problems whatsoever. Ah, after all this effort. Really? You're going to do that to me?

**Dave Jones:** None of them. I bet you none of them. Now, yep, none of I reckon it's none of them. That's absolutely perfect. There's nothing wrong with that. Suspect we're going to come a gutsy here.

**Dave Jones:** Lucky last. Ta-da! There we go. Absolutely nothing wrong with any of those platters. So, we haven't had a head crash. There's your five platters. Don't they look absolutely fantastic?

**Dave Jones:** Ah, now they got fingerprints all over them. Ah, who cares? Not There's no evidence of a head crash whatsoever. And we've got another uh pad under there. I don't know, is there some aerodynamics to that?

**Dave Jones:** I don't know. There's actually a significant amount of friction in that. I guess, once again, that'd be precisely engineered, there'd be a reason for that. And uh yeah, these pads they would be for, you know, aerodynamic uh reasons to keep, uh you know, the platter from uh flapping around in the breeze or whatnot.

**Dave Jones:** Um I would guess. Or that, you know, if it happens to wobble a little bit, maybe it touches the pad and doesn't touch any metallic surface, so it doesn't get damaged.

**Dave Jones:** Uh cuz they obviously don't need those in the middle. They don't need those uh around these at all. Um but yeah, these would be precisely engineered. I mean, look at I Yeah, you can see how they're just milled out.

**Dave Jones:** How do they finish that? I don't know. The mechanical engineers out there, like you can see the lip. So, that's that's really very nicely machined. That's just a thing of beauty.

**Dave Jones:** Joy forever. Wouldn't be cheap to do that, would it? These platters here, so precisely engineered, I can't damn well slide them apart. Um I can't get them apart. I swear.

**Dave Jones:** What the Oh, there we go. Got it. Got it. Wow, they're so precisely flat the surface is so precisely engineered. This can't do it. Unbelievable. Anyway, there you have it.

**Dave Jones:** That's a teardown of a Western Digital Red hard drive, 6 TB jobby and five platter and of course that would be a 10 heads total. Oh, yeah, I miscounted those before.

**Dave Jones:** So, yes, that's interesting but I didn't see the money shot. We didn't get it. We didn't get to see like a big part of one of the platters gouged out there.

**Dave Jones:** So, that's disappointing. So, that earns a wah wah wah wah wah. So, yeah, I can only assume that there was something in the head drive mechanism that sort of made it do the large crunchy noises and stuff like that cuz it was just so much louder than like a normal drive.

**Dave Jones:** I could hear it like on the other side of the lab. It was incredible when it first happened. Um, so, yeah, that's interesting but there you go. I hope you enjoyed that.

**Dave Jones:** It's a fascinating look inside a hard drive and I probably could have like got a new drive under warranty perhaps although as I said it was one month technically one month out from when I bought it about 26,000 something hours continuous operation and eventually came a gutser.

**Dave Jones:** All the others are fine though. No bad sectors at all. So, anyway, I hope you enjoyed that fascinating look inside absolute marvel of modern physics, electronics, uh, packaging, uh, construction, testing, material science, all sorts, everything.

**Dave Jones:** Amazing technology goes into these hard drives. I couldn't even begin to scratch the surface of what all the aspects of modern technology that go There's probably not a not a single aspect of modern technology that is not inside a modern hard drive and manufacturing technology and physics, material science, and the whole works.

**Dave Jones:** It's just absolutely incredible. So, hope you enjoyed that. I certainly did. If you did, please give it a big thumbs up. As always, discuss down below. Catch you next time.
