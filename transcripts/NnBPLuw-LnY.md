---
video_id: NnBPLuw-LnY
title: EEVblog 1398 - Western Digital RED 6TB WD60EFRX Hard Drive TEARDOWN
url: https://www.youtube.com/watch?v=NnBPLuw-LnY
source: youtube-asr
---

**Dave Jones:** Hi, it's teardown time in glorious 4K resolution if you've got the option to watch it like that. Anyway, we're going to a Western Digital WD60EFRX for those playing along at home, 6 TB Western Digital Red hard drive that I

**Dave Jones:** had in my NAS here. And if you've been following me on EV blog too, and you should be cuz that's where I dump a lot of interesting videos. And I'm almost like I'm only a couple of thousand away from 100,000 subscribers

**Dave Jones:** and getting that YouTube silver award. So, you know, please give me a sub on EV blog too. Anyway, if you've been following along the saga and on Twitter as well, this is a drive that failed in my four-drive

**Dave Jones:** DS418 NAS Synology NAS drive. And basically, it's it had been there for just over 3 years. Yes, it's literally 1 month out of warranty. It had like 26,000 26,000 operational hours, but technically, I looked at my old receipts

**Dave Jones:** and yes, 1 month out of the 3-year warranty. Doh! Anyway, everyone said that they wanted to see a teardown of this. So, I might be able to still get like a warranty replacement for it. Maybe if I just, you

**Dave Jones:** know, fill out the form, maybe they'll send me a new one. But anyway, a lot of people wanted to see it. So, I'm going to sacrifice this puppy cuz you do have to return them under warranty. So, and you see the

**Dave Jones:** build date here, 18th of January 2018, but it has been in like 24/7 operation in my NAS. As I said, like 26,000 odd hour operational hours. The specific model we've got here, the EFRX, this is actually what's called a CMR or

**Dave Jones:** continuous magnetic recording drive. It's the technology used to actually write the bits onto the platters itself inside. And anyway, Western Digital, like they all were CMR, but then they sneakily in their Red series drives changed them to SMR or shingled magnetic

**Dave Jones:** recording drives, which isn't as good and it's apparently much slower than CMR drives because in shingled magnetic recording, the adjacent tracks actually overlap each other, hence why it's called shingle, just like shingled roofs, you know, the shingled tiles overlap each other and

**Dave Jones:** apparently when you write a byte to this a bit to this, you've got to actually write the two adjacent bits as well. Not this one, as I said, this is CMR, but the EFAX version, which I did actually unknowingly have one of

**Dave Jones:** these in my Synology NAS drive wise. So yes, I am going to eventually replace that, but I have to reconstruct or resync my drive first with a new CMR drive, which is on the way and then I'll replace the SMR one

**Dave Jones:** I've got with the CMR. Anyway, it's actually the CMR one that failed, not the SMR, which a lot of people claimed. So anyway, that was just like an interesting aside. Western Digital have now admitted that they did that and now

**Dave Jones:** the new the reds the SMR and the red plus is actually the CMR type. So the new ones I've ordered red pluses. So anyway, let's do a teardown of this bad boy and see I will here's a video I will now try and

**Dave Jones:** record the sound from it, but unfortunately I just did that and it's not as bad as it was. But anyway, here's the video.

**Dave Jones:** Sound is nowhere near as bad as it was before. It's not sounding normal. Can hear this right across the other side of my lab when when it was failed in the NAS. The noise, you can't hear these things.

**Dave Jones:** Yeah, that's not as bad as it was, but it's still pretty bad. Like it should not be that loud. I haven't heard a hard drive that loud since like the 1980s, 1990s. So, anyway, here's the bottom of the

**Dave Jones:** drive for those playing along at home. There's no bodge wires. There we go. We've got a flat flex going in there. That's to drive the motor. That's a four-wire jobby. That's all gunked up. That's a not a hard potting compound,

**Dave Jones:** not a soft one. And, you know, do not block hole. It's got various vents or whatever. I haven't torn down a hard drive in donkey's years. Anyway, I'm like screws under there warranty seal screws or whatever. But, and for those curious, no, there

**Dave Jones:** was no indication that this was going to fail. There was no bad sectors or anything like that. None of my other drives have any bad sectors. So, that's not an issue. Oh, that just Oh, that's that's nice. I like that. No

**Dave Jones:** cabling whatsoever. Just a board-to-board pressure contact. Look at that. That's beautiful. Got some foam in there. It's just for some anti-vibration stuff so that the you know, board doesn't contribute to any vibration noise I would presume. So, yeah, I like

**Dave Jones:** that. So, that's stuck down. Let's take that off. So, yeah, no no indications at all that this thing was going to fail. All I heard about it was that all of a sudden I was writing some video to it

**Dave Jones:** cuz this NAS drive I actually do read write edit all of my video on this NAS drive. I don't edit video locally. It's all done on my external NAS. And no, it's not slower to do that. Trust me, I've done videos on that. Anyway,

**Dave Jones:** yeah, so that's pretty cool. And we've got another pressure contact over here on the for the motor drive as well. And they've got a That's also buggering off into there. So, that's interesting. I'm not sure why they're going off under there. Is

**Dave Jones:** there another They're all in parallel. So, huh. Anyway, there you go. There's the main board there. I've taken off the thermal pad on top of that. So, like I won't go into any into any details on the chips of the designer or anything

**Dave Jones:** like that, but that looks very nice. No worries whatsoever. You can explore that in your heart's content in 4K resolution. There you go. It just gives you some additional detail. Not sure if you can see the part number on that. If

**Dave Jones:** anyone cares. All I want to see is the big gouge taken out. Hopefully taken out of the platter inside this thing cuz when you get the grinding noises like that, the old click of death from these things, then yeah, that's the head doing

**Dave Jones:** some nasty business against the platters inside. I don't know how many platters these modern 6 TB drive use. Got no idea. We'll find out. Take out that. Yep. There's the other screw. So, I'll take out all of them.

**Dave Jones:** No, you only need one, don't you? Really? I mean, you can't, you know, you can't take out every single screw to take this off. I guess it's just harder to fake, you know, six of them instead of like five of them or whatever instead

**Dave Jones:** of one. Now, of course, this is not something that you'd ordinarily do in a just a normal lab with normal air and stuff like that because if you get any dust and crap in there, yeah, you'd want to do this in a

**Dave Jones:** relatively clean air environment if you are like looking to get the data off it or repair it or do whatever. But yeah, not one care given here. But anyway, yeah, you can probably see they've got some sort of gunky seal

**Dave Jones:** under there like that. So, I've missed a screw under here. Oh, yeah, might have. Sneaky bugger. Yeah, isn't there a bloody another one under there? And this one looks like it's smack in the middle of the platter. That's kind of

**Dave Jones:** important. Now, I thought there was another one under there. That's an air vent, is it? Yep. Pretty sure that shiny thing in there is the platter. Sure there's some trick to this. I don't know. Sorry. Don't take this video as how to take apart hard

**Dave Jones:** drives. It's not my business. I did expect there to be a lot of force on that uh rubber gasket holding it Oh, yeah. Yeah. Yeah, there you go. I think you need a big wide-ass screwdriver like I'm using

**Dave Jones:** at the moment. That seems to be the go. Yeah. Yeah, it seems to be popping. Okay. Yeah, can't use the little piss ant one I used before. Once the seal's off, yeah, it's done. Come on. You can do it.

**Dave Jones:** Tada! We're in like Flynn. Look at that. There's our platters. Jeez, there are uh quite a few platters. Let's have a look on the bottom. There's some sort of pad, I guess, to stop it I I if there is any vibration or wobble in

**Dave Jones:** there. I don't know. Like a you know, these are incredibly, probably the most complex mechanical device you own would be a hard drive. I I think there's probably no doubt in that. All right. There you go. Yeah, that's our big

**Dave Jones:** rubber seal around the thing. It's like uh it's like it's not even rubber. It's some sort of gel kind of I don't know. If anyone knows what type of stuff that is, yeah, let us know. And silly me, just put a mark on the uh

**Dave Jones:** platter. There it is. That's the mark on the platter that, unfortunately, um yeah, dumbass Dave, you probably screamed at the camera, that came from this, which was um yeah, don't do that. Anyway, good thing is I'm not trying to recover the

**Dave Jones:** data from this thing. Well, I don't see any damage to that top platter. All right. Yep, highly reflective these things. But um no, I expect to see like some maybe some big grooves taken out of this thing somewhere. So, there you go. You can see

**Dave Jones:** the entire platter. Of course, it's going It's just going to reflect absolutely everything cuz these are the mirror finish on these is just absolutely incredible. And there's our head array. Five six um arms on there. So, that would would uh

**Dave Jones:** 12 surfaces. so six platter, uh 12 surface on there. So, beautiful. And uh yeah, there's a little parking frame over here for the heads. Very nice. And of course, like the As I said, the technology which goes into these is absolutely incredible. The

**Dave Jones:** most precise engineered product uh that you'll ever buy. It's just like People don't realize the insane materials technology, the engineering, uh the production technology that goes into making these hard drives. And 6 TB is, you know, not a big drive these

**Dave Jones:** days. You can get much bigger and denser. And you can get them in smaller form factors and all sorts of things. Um and yes, they do contain uh very powerful neodymium magnets. So, uh yeah, you can get those out and have some fun

**Dave Jones:** down in there. You can see the coil. Just a uh like a DC servo motor. These are all like these aren't stepper motors, I believe. These are like uh you know, DC servo uh controlled. And it's just like I don't know the resolutions

**Dave Jones:** involved in something like this, but it's absolutely ridiculous. So, I'm going to say not a huge amount in there, but a huge amount of technology goes into that. Um it's just absolutely incredible. Anyway, unfortunately, Murphy says that the top of this disk

**Dave Jones:** does not have any marks. Of course, it doesn't. So, we're going to have to go further. But what I'll do is I'll actually plug it in like this. See if it does anything. Now, I assume that these are like filled with an inert uh gas. Um

**Dave Jones:** let me know in the comments down below. There we go. And there would be no um sensor I don't know what they'd be a And are they pressurized? Would there be a pressure sensor in there? Probably not. Oh, there

**Dave Jones:** we go. It's seeking. Beautiful. Geez, it sounds much louder without the uh case on. Oh, it's going back to park. Oh, is that normal? I don't know. Does anyone know? There you go. It's trying to the business. It's trying to

**Dave Jones:** like read the exact point. Is that where it keeps the disk index or whatever? But yes, this this drive does not work at all. And I think this is only like 5600 or 5200 RPM or something like that. It's

**Dave Jones:** not one of the fast jobbies. There you go, it's working doing its thing and it's just done the shutdown and it's going to stop spinning, stop spinning, stop spinning, stop spinning cuz it's realized that whether or not Windows

**Dave Jones:** shut that down or whether or not it's it's done that of its own accord. If you do know that, leave it in the comments. But there you go. Um yeah, it I want to see the gouge. That's little on a little compliant

**Dave Jones:** mount. Maybe I can take that out. Well, hello. Do we have a little desiccant bag in there? That's got to be a desiccant bag, right? So yeah, to keep the moisture out of this sucker. Hmm. Aha, of course. That assembly there is

**Dave Jones:** just the interface from that flat flex. It's just to hold the flat flex in place. It does absolutely nothing else and then it Yeah, and then it just folds over and goes over to the the head. So that's

**Dave Jones:** all the head and motor drive. You can see the the thicker traces in there versus the thin. Of course, the I assume that the head amplifiers, you know, they're all going to be in there. It's not going to get all those teeny weeny

**Dave Jones:** little signals all the way back over here, I don't think. Now, I'm totally unsure how these platters come out and I'm sure there's a lot of people who have disassembled these and they're probably screaming at me, "Do this step,

**Dave Jones:** Dave. Do this step." or whatever. I'm just going to wing it. Haven't looked at any guides. Have we got some screws on top there? So maybe we've got to take them out one by one. Suck it and see.

**Dave Jones:** Once again, this is like I don't care. I'm not trying to save data here. Woohoo! That's fun. Yeah, you probably shouldn't do that, but well, the heads are parked. Why not? As you'd probably expect, those are really Loctited Oh, they're Loctited in

**Dave Jones:** there. Wow, tight as a nun's nasty. Actually, I don't see any evidence of Loctite on those. That's um it's rather surprising. Although, I guess you don't want to be applying liquids around hard drives like this in this sort of

**Dave Jones:** process. Geez. Oh, this is ridiculous. Yeah, imagine being the design engineer that actually proposes, "Oh, let's put some Loctite on those." And the production engineers are just going, "What? Give me a break. You want us to put liquids

**Dave Jones:** around these platters?" Well, this is totally not fun. I can assure you. Come on. Bastard. There's got to be an easy way to do this. There's no like locking point that I can find. Anyway, I just took out that head

**Dave Jones:** parking thing and I did sort of scrape the heads as I took them out. So, yeah, it's probably not the correct assembly step. There you go. There's the teeny tiny heads. Double-sided, of course. And yeah, going to get medieval on its ass.

**Dave Jones:** Can they actually spring apart? Like that. You know that? Springy springy. Science that goes into the engineering that goes into the aerodynamics of these heads and how they uh rest on the surface and stuff is um yeah, really

**Dave Jones:** something. Do actually have another seal on the bottom of the case under the PCB here. Let's take that off. Oh, there you go. That's the bottom of the platter. So, that's rather interesting. That accesses like it's obviously something

**Dave Jones:** to do with uh some sort of production testing, production alignment, uh you know, inspection, you know, physio-optically inspect the heads as they scan the surface or something like that. I don't know. Anyone knows? The center of the platter is here and

**Dave Jones:** then the head just Here's the head motor here and it just sweeps the head across like that. It's now got Oh, I got a fingerprint. Fingerprint. Oh, no, it's ruined. Care factor zero at this point. So, yeah, anyone know why that's

**Dave Jones:** there? Uh, let us know. Good news is it looks like I can unscrew the head assembly by taking this puppy off and then the So, the head assembly should now come out. Now, unfortunately, the final screw in there seems to be

**Dave Jones:** stripping. Okay, what I've done is looked at this screw under the microscope and like a T7 like it fits and it feels fantastic. There is actually a tiny bit of play in it. So, and and a T8 doesn't fit. So, it's

**Dave Jones:** almost as if there's a T7.5 or one of the Is there an imperial rubbish? I don't know. I've never encountered that. Um, but yeah, I cannot get that bloody last screw out and it's just stripping now with the T7 that got

**Dave Jones:** all the others out. And of course, I just noticed the two notches in there. Clearly, there's a custom tool designed to go into the center and then hold in those two points to stop this sucker spinning around. And I do believe we can

**Dave Jones:** actually get that out of there. Watch it snap back. Now, those neodymium's Whoa. There we go. There we go. Got it. Got it. Beautiful. Now, I can access the screws and actually get the head out. Yeah, that's one powerful magnet. So, yeah,

**Dave Jones:** that's a keeper. So, you can now see the coil which is an interesting what trapezoidal kind of like but it's bowed at the bottom and I don't know what shape that is. Does that officially have a name that shape? But uh yeah, that

**Dave Jones:** would be once again highly engineered. Um it's probably not that shape by accident. So, now we can actually lift that out of there. And of course, we're going to have the magnet on the bottom. Ta-da! There's the entire

**Dave Jones:** head assembly. Wow, isn't that fantastic? Here you can see the thickness of the coil there. You can see all the turns on that. And yep, there's our other magnet assembly. So, does that just lift out? Comes out somehow. All right, let's have a quick

**Dave Jones:** look at the head under the Tagarno microscope. Now, it's all Yeah, that's just the flat flex interface like that. There's nothing else on there at all. And uh that's just a holder for all the flat flex. There's our head amplifier

**Dave Jones:** silicon. There you go. Because there wasn't the number of connections required to actually do that. And there we go. There's our head driver chip. So, that's a chip on flex uh technology. They've got the gunk around there just to keep

**Dave Jones:** the moisture out and whatnot. And uh yeah, you can see all the traces coming in here from the head. And then there's only a few going out here which goes across the flat flex to the main PCB. So, of course, you can't have the uh you

**Dave Jones:** know, the tiny output from the heads. I mean, the the signal levels are Oh! Ooh! Careful. Yeah, I'm going to break these anyway. Anyway, the signal levels from the head are incredibly small. Um so, yeah. Um you need a custom head

**Dave Jones:** amplifier ASIC there. There's nothing else on there. Oh, there's one one bypass cap. And that's all she wrote. And there's our head drive uh coil there. And that's it. There's no other feedback on the head drive coil by the looks of it. So,

**Dave Jones:** yeah, we've got all our test points here. And check this out though. This is interesting. These large traces here seem to have like large little chunks taken out of them around the bend there. And I haven't seen that before.

**Dave Jones:** I I can't see how that's sort of any controlled impedance type thing. So, I'm left to imagine that's a mechanical stress kind of thing on the flat flex. I don't know. Um if anyone knows for sure, please leave it in the comments.

**Dave Jones:** Anyway, isn't that beautifully machined? I mean, absolutely fantastic. That's all machined in one block. Look at that. That is not joined or anything, right? Wow. How do they do that? That is remarkable. Oh, jeez. That's a bit How you doing?

**Dave Jones:** Check out the wires just going down to the coil. Oh, no. There you go. Oh, no. I thought that was soldered down there, but it's not. They just go into some um insulated sleeve in there. Anyway, you can see the

**Dave Jones:** thickness of the coil there. There's lots of turns in that. Those playing along at home want to count that? Knock yourself out. It's so the head plate, that's actually attached on the underside of cuz this is all part of the big

**Dave Jones:** machined part, right? So, that's actually head's actually attached to the underside of that. So, are these these big test pads on the top? You can see this is going off to uh some test pads here. And you can see that the trace is actually

**Dave Jones:** split around this gap in the um in the head in the part of the metal there. I'm not sure why that's the case. Is that aerodynamic reasons or something? Yeah, I can only assume that's aerodynamics. Anyway, there's our head. Might have to

**Dave Jones:** sacrifice one of them. Might have to Well, yep. That one's gone. Oh, no. OH, NO. COME ON, gutsy there. Believe it or not, that's actually maximum zoom. Now, you can see that the ferrite head, I mean, there's amazing material science

**Dave Jones:** technology going on inside these ferrite heads in here. So, there's another close-up of the head. You can see how tiny that is compared to my fingerprint. Wow. Yeah, that's amazing. And yeah, it's all flat flex, of course. There's a

**Dave Jones:** lots of Once again, there's lots of aerodynamics in this. There would be a lot of engineering that goes into the aerodynamics to to make sure these heads actually uh just float above the surface. So, that's uh yeah, that's really something.

**Dave Jones:** Wow. If you think you understand the every aspect of the engineering that goes into this, you're probably wrong. Third like 40 years, 50 years of advancement in technology. I've still got somewhere the magnetic recording handbook. It's this thick. Almost a well, a lot of it's not

**Dave Jones:** obsolete, but uh in terms of like manufacturing technology, it would be. So, so yeah, these heads are just amazing technology. Absolutely amazing. So, yeah, there you go. But yeah, there's no feedback on that coil at all. Yeah, that that is one machined

**Dave Jones:** piece, isn't it? Wow. That's great. How much does it cost to turn out one of those? Any Any machining experts out there? Is it It No, it did have to be cast, wouldn't it? It did have to be cast. You

**Dave Jones:** wouldn't machine that properly, right? In fact, it doesn't look like there's machining uh No, there's machining marks on the top. For all the world, look like machining marks. Did they just like polish it off? I don't know. If anyone

**Dave Jones:** knows, is it a combination of cast and machine or something? I don't know, but that's yeah. That's I guess that's the only way you can get the rigidity on on that head and the arms and everything. It's absolutely

**Dave Jones:** remarkable. So, yeah, there's not much in these things. It's uh it's just the platters and the head assembly and that's that's it. All the electronics is outside. Yeah, there we go. You can just pull that out. So, we've got the

**Dave Jones:** matching assemblies. I won't try and snap them together because uh yeah, it could be quite dangerous. These are incredibly powerful and of course um yeah, rare earth metals used in these and well, I think uh isn't China the

**Dave Jones:** dominant player in rare earth metals? Um yeah, very precious resource. Trigger warning. Look away now.

**Dave Jones:** Think I got it. Winner, winner, chicken dinner. Wow, that was a real bastard, that one. Ta-da! There we go. We're in. There's our separator for each one. So, nothing on that one. Beautiful. Look at that. I mean, polished mirror. That's

**Dave Jones:** just incredible. Wow. Anyway, so that's one. Now, we There we go. That is not a magnet uh by the way. That's just like that's just a machined brushed aluminum, is it? Something like that. Yeah, that's just a machined

**Dave Jones:** bracket. How precisely that has to be machined, I don't know. Anyway, our next one down also doesn't have any evidence of a head crash. Maybe we're not actually going to see That'll be disappointing. After all this, I'm going to be incredibly

**Dave Jones:** disappointed not to see a big gouge taken out and a big head crash. These are going to get increasingly hard to Ah, take out, I suspect. Now, third one looks okay, too. Yep, no problems whatsoever. Ah, after all this effort. Really? You're

**Dave Jones:** going to do that to me? None of them. I bet you none of them. Now, yep, none of I reckon it's none of them. That's absolutely perfect. There's nothing wrong with that. Suspect we're going to come a gutsy here.

**Dave Jones:** Lucky last. Ta-da! There we go. Absolutely nothing wrong with any of those platters. So, we haven't had a head crash. There's your five platters. Don't they look absolutely fantastic? Ah, now they got fingerprints all over them. Ah, who cares? Not

**Dave Jones:** There's no evidence of a head crash whatsoever. And we've got another uh pad under there. I don't know, is there some aerodynamics to that? I don't know. There's actually a significant amount of friction in that. I guess, once again, that'd be

**Dave Jones:** precisely engineered, there'd be a reason for that. And uh yeah, these pads they would be for, you know, aerodynamic uh reasons to keep, uh you know, the platter from uh flapping around in the breeze or whatnot. Um I would guess. Or

**Dave Jones:** that, you know, if it happens to wobble a little bit, maybe it touches the pad and doesn't touch any metallic surface, so it doesn't get damaged. Uh cuz they obviously don't need those in the middle. They don't need those uh around

**Dave Jones:** these at all. Um but yeah, these would be precisely engineered. I mean, look at I Yeah, you can see how they're just milled out. How do they finish that? I don't know. The mechanical engineers out there, like you

**Dave Jones:** can see the lip. So, that's that's really very nicely machined. That's just a thing of beauty. Joy forever. Wouldn't be cheap to do that, would it? These platters here, so precisely engineered, I can't damn well slide them apart. Um

**Dave Jones:** I can't get them apart. I swear. What the Oh, there we go. Got it. Got it. Wow, they're so precisely flat the surface is so precisely engineered. This can't do it. Unbelievable. Anyway, there you have it. That's a

**Dave Jones:** teardown of a Western Digital Red hard drive, 6 TB jobby and five platter and of course that would be a 10 heads total. Oh, yeah, I miscounted those before. So, yes, that's interesting but I didn't see the money shot. We didn't

**Dave Jones:** get it. We didn't get to see like a big part of one of the platters gouged out there. So, that's disappointing. So, that earns a wah wah wah wah wah. So, yeah, I can only assume that there was something in the head drive

**Dave Jones:** mechanism that sort of made it do the large crunchy noises and stuff like that cuz it was just so much louder than like a normal drive. I could hear it like on the other side of the lab. It was

**Dave Jones:** incredible when it first happened. Um, so, yeah, that's interesting but there you go. I hope you enjoyed that. It's a fascinating look inside a hard drive and I probably could have like got a new drive under warranty perhaps although as I said it was one

**Dave Jones:** month technically one month out from when I bought it about 26,000 something hours continuous operation and eventually came a gutser. All the others are fine though. No bad sectors at all. So, anyway, I hope you enjoyed that fascinating look

**Dave Jones:** inside absolute marvel of modern physics, electronics, uh, packaging, uh, construction, testing, material science, all sorts, everything. Amazing technology goes into these hard drives. I couldn't even begin to scratch the surface of what all the aspects of modern technology

**Dave Jones:** that go There's probably not a not a single aspect of modern technology that is not inside a modern hard drive and manufacturing technology and physics, material science, and the whole works. It's just absolutely incredible. So, hope you enjoyed that. I certainly did.

**Dave Jones:** If you did, please give it a big thumbs up. As always, discuss down below. Catch you next time.
