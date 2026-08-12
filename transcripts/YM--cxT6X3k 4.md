---
video_id: YM--cxT6X3k
title: EEVblog #884 - EEVBlog BM235 Multimeter REPAIR
url: https://www.youtube.com/watch?v=YM--cxT6X3k
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 29, "3": 45, "4": 54, "5": 68, "6": 77, "7": 95, "8": 112, "9": 126, "10": 137, "11": 152, "12": 167, "13": 177, "14": 195, "15": 213, "16": 230, "17": 241, "18": 257, "19": 278, "20": 286, "21": 307, "22": 326, "23": 341, "24": 358, "25": 373, "26": 383, "27": 395, "28": 404, "29": 414, "30": 433, "31": 447, "32": 458, "33": 471, "34": 489, "35": 508, "36": 528, "37": 538, "38": 564, "39": 572, "40": 582, "41": 594, "42": 606, "43": 621, "44": 633, "45": 647, "46": 660, "47": 671, "48": 684, "49": 698, "50": 718, "51": 729, "52": 746, "53": 766, "54": 782, "55": 797, "56": 806, "57": 821, "58": 838, "59": 859, "60": 883, "61": 903, "62": 915, "63": 929, "64": 944, "65": 954, "66": 972, "67": 995, "68": 1010, "69": 1022, "70": 1041, "71": 1049, "72": 1060, "73": 1073, "74": 1083, "75": 1102, "76": 1114, "77": 1126, "78": 1135, "79": 1147, "80": 1158, "81": 1170, "82": 1184, "83": 1196, "84": 1218, "85": 1233, "86": 1250, "87": 1266}
---

**Dave Jones:** Hi, I thought we'd take a look at the first return to EEVblog BM235 multimeter. Um, Frank actually bought one of these. He's in Jacksonville in Florida and unfortunately he got it and it didn't work.

**Dave Jones:** And he's yeah, he described all sorts of things in that it would you know measuring say a 1.5 volt battery and it'd measure 0.6 volts and then it'd drift down to zero and and all sorts of stuff weird things didn't work at all.

**Dave Jones:** And um, I have sold I think over a thousand of these meters so far and this is the first one that's reported any issues like this at all. So yeah, you expect this sort of thing to happen even though each meter is individually tested at the factory.

**Dave Jones:** It has to be because it has to be calibrated at the factory. So each one would have been tested but you expect some sort of infant mortality rate on virtually any product out there.

**Dave Jones:** It's not just this meter but any electronic uh product. There is going to be some percentage of failure rate um, after they're tested and they hit the field. It's just you know the way it is for whatever reason.

**Dave Jones:** Um, and that's no reflection on the quality of the thing or well, it could be. Okay, but in this case sold over a thousand no problems and this is the only one.

**Dave Jones:** So you know, who knows Murphy's law. Uh, we're we've got one. We got one. And sorry my voice is still terrible. Um, I haven't made any videos this week because um yeah, I just yeah, you don't probably don't want to see me on camera either.

**Dave Jones:** So I look and feel pretty terrible at the moment. And uh, if you haven't been following me on Twitter, I am breaking in all sorts of ways. I've busted my ACL joint in my knee is completely busted.

**Dave Jones:** Anyway, um, there's the probes. So yeah, I might have to get surgery on that. So, yeah, I'm doing wonderful at the moment. Let's unwrap this puppy and have a look.

**Dave Jones:** And see if A, it's repeatable. Um but yeah, I'm pretty sure, you know, from the stuff he was uh was saying it was pretty obvious that this thing was dead.

**Dave Jones:** So, let's turn it on and uh see what we've got here. Switch on. He said it worked on AC, curiously. Now, that, you know, function-wise, it's it's displaying the right stuff.

**Dave Jones:** Okay. So, there we go. Okay, no drama at all. I've got a um I've got my voltage reference here. I've got it set to a volt. This is my lab reference one of my lab reference standards.

**Dave Jones:** So, let's plug it in and um see if we get a volt. What what what what. He's right, look. It's going down and down. It's not like it's on AC mode, it's on DC mode.

**Dave Jones:** And sure enough, I mean, if I bring in a good one over here and of course it will uh measure a volt. No worries whatsoever. So, um yeah, that is one sick puppy.

**Dave Jones:** What is wrong with it? Wow. Let's maybe whack it on ohms here and uh disconnect that and okay, ohms works. Oh, no, that was continuity. That was con- Oh, continuity mode, look.

**Dave Jones:** Nope. Okay, ohms is just showing direct short. That's interesting. That's interesting. I well, I was going to maybe there's some sort of um solder short on the board or something that's causing that.

**Dave Jones:** I mean, obviously our chip set's working fine. Um and there's not much in this apart from a the multimeter chipset. That's pretty much the only active circuitry and the LCD driver chip.

**Dave Jones:** Um the capacitance Oh, that seems a bit high. 13 nF, I'm not Hang on. I've got a reference cap here. Here we go. Let's check it out. I've got myself a um These are very nice if you can pick them up on eBay cheap.

**Dave Jones:** They're old, but uh these Arco standard capacitors, they're very very nice. And um you can often get them quite cheap. Uh that's low. That's low. Put it over here, but at least it's functional.

**Dave Jones:** There we go. No dramas whatsoever. That's well within spec. Um so yeah, this one is a bit there and I've checked other meters. I think that is, yeah. So this one's a bit low on cap.

**Dave Jones:** Let's measure some current, shall we? Here we go. I'm feeding in 1 mA current range works. Current range works. 10 mA, 100 mA Hey. Okay. That's interesting. That shows that well, because the the current uses a different input arrangement.

**Dave Jones:** So yeah, there's something with that main common terminal which, you know, is like So it's not the chipset. It's not like I don't know, ESD or something else has gone wrong with the chipset and it's damaged because the current just works fine.

**Dave Jones:** Let's try the microamp range. 100 microamps There you go. Yep. It works just fine and dandy. And hold on to your hats, the millivolt range works fine and dandy as well.

**Dave Jones:** So um yeah, Okay, interesting. So millivolt range works. Current ranges work. Uh so, chipset is just fine, but all the other functionality, like if we go back here to our volts, you know, like that is that is dead.

**Dave Jones:** And let's just jiggle the range switch around here. Jiggle is a technical term. And um it's not that. So, looks like something on the front end of this thing is gone on particular ranges.

**Dave Jones:** The millivolt range is basically straight in. It doesn't go through the input divider or anything else. Um unfortunately, I do not have the schematic for this. Um Brymen will not uh release it uh to me.

**Dave Jones:** They say it's proprietary, blah blah blah. Yeah, okay, fair enough. Um so, we don't have that, but hey, we can at least have a look around. Let's go. The serial number for those playing along at home.

**Dave Jones:** And we're in like Flynn. Um unfortunately, we're going to have to take this uh top board out here. That's uh one of the downsides of uh having the CAT IV rating in such such a small meter.

**Dave Jones:** That's the only way they can physically uh do it. And that's where uh a bit of the input uh circuitry is around there, but we can see other stuff on here.

**Dave Jones:** And uh I might actually uh get out the uh Tiganu microscope. Just get the two side by side and see what we can see. Oh, and the other annoying thing about having the secondary board here is cuz I do have to actually desolder this and unplug um essentially unplug the uh jacks and everything else to get in there.

**Dave Jones:** We can't sort of like feed in stuff and then measure it on the main board underneath at the same time. So, that's uh well, you can if you go to a lot of trouble to wire it back in and stuff, but yeah, uh just makes it a bit trickier to troubleshoot.

**Dave Jones:** But, the first uh thing you do with troubleshooting something like this is visual, especially if you've got a unit to compare it against. All right, let's check this out.

**Dave Jones:** We've got our unhappy camper on the left here and our happy camper on the right. And, uh I'll probably just just because you can, do a quick uh visual inspection to see if there's any missing parts.

**Dave Jones:** Now, this, you know, shouldn't be the case because, as I said, it would have passed factory test, factory calibration, everything else to do that. It would have had to have everything um in place, but I don't know, something might have made poor contact, and then in shipping it might have vanished or something like that.

**Dave Jones:** But, um I I can't obviously see under the uh uh input board yet, but it doesn't look to be any issue here at all. I wouldn't expect that. But, uh see the nice little uh star grounding point there.

**Dave Jones:** Very nice. Just going off. Someone knew what they were doing in terms of uh PCB layout. But, uh yeah, there's nothing obvious going on there at all. As I said, um the main chipset down here, which is um BTC, which is Biwin Technology Corp uh branded.

**Dave Jones:** I don't know exactly what one it is. They won't tell me. Um but, uh that is obviously not failed because half the functions work, and the other half don't.

**Dave Jones:** So, there's got to be something screwy with some with something to do with the input. So, that all looks hunky-dory. The other thing, next thing I would look for is uh any um shorts, like uh little solder balls or anything like that um as part of the production process, which could have uh got in there.

**Dave Jones:** And, they may not have been an issue during the uh during the process. I love my Takano microscope here. It's beautiful, isn't it? Um I can go all the way in.

**Dave Jones:** Can go all the way with LBJ. Look at that. You can see the uh silk screen's actually a uh dot matrix print. It's not a uh photo imageable silk screen.

**Dave Jones:** You can see the dot pattern on there. And uh but yeah, our solder balls, they could um certainly account for it. Uh as part cuz they're like sort of like a little unknown thing.

**Dave Jones:** You got slightly too much paste. You know, it's not exactly the same every time even though, you know, it might be a smidgen over or just how the, you know, the dynamics of the paste and everything else and how it melts and things like that.

**Dave Jones:** Um you can often get a stray solder ball. So, I'm just looking for anything obvious like that. Uh and I'm not so I wouldn't expect to see it up the top cuz this is like as I said, this is the LCD chipset.

**Dave Jones:** All right, here we go. Here's the top board. We've got our Here's our voltage input, of course. There's two input protection resistors. I can measure those, of course. They're uh 1K.

**Dave Jones:** Good old brown brown black red there. And I don't think it's going to be our PTCs here because otherwise we wouldn't get anything. But anyway, ooh. Is that got a little Uh somebody's had a little crimp.

**Dave Jones:** No, no, it's all right. No worries there, but we could measure those. They should be about uh a K each or something like that. But as I like if it wasn't broken like that doesn't explain like the zero ohms and things like that.

**Dave Jones:** And the mobs here, well, you know, in theory it could be, but uh doesn't explain why the 100 mV range was working, for example, and you know, it couldn't measure 1 V.

**Dave Jones:** Um so, you can measure those. They they should be open, of course. They should only start clamping at uh you know, 1,000 V or whatever they're rated for. And we've got some uh 5 meg input resistors here.

**Dave Jones:** You can measure those. Might be doing silly buggers, but we've got uh um input uh jack uh detection stuff like that. So, it's not that. Um so, there's nothing on the top board really that you would suspect.

**Dave Jones:** I'd be going straight for down here. And let's let's have a squiz around here. And once again, I'm looking for bad joints. Hello. Hello. Hang on. L9, is that my imagination?

**Dave Jones:** Hang on. Sorry. I don't may not Oh, no. No. No, that's all right. No, I thought there was no fillet on that. But, it's it's all good. So, I'm looking for bad solder joints.

**Dave Jones:** I'm looking for uh solder balls, shorts, other things. But, uh whoop. What's going on down there? That Oh, hello. Hello, L3. Tada. Hello. Look at that. L3 has cracked.

**Dave Jones:** The solder joints on L3 have cracked. We got one. Yep. Wow. How has that happened? Let's bend our wire out of the way there. Sorry about the light here.

**Dave Jones:** I can uh I can There we go. That's going to be better. Wow. I thought it looked a bit askew. And you go there and sure enough, that puppy Wow.

**Dave Jones:** That's That's an inductor, and that has sheared right off. I mean, it's not like it's a heavy part. So, that is very very interesting. I'm going to Well, it's gone.

**Dave Jones:** Look at that. There we go. Okay, so what I'm going to do is I'm going to take that out. I'm going to put some fresh solder down on there.

**Dave Jones:** Those pads I'm going to Well, I'll put fresh solder down on one, I'll wick the other off, and replace that. And I think it might come good again. The one next to it Sorry about the focus on this.

**Dave Jones:** The one next to it looks The one next to it looks good. That is weird because And okay, solder joints can crack like that, but they're usually on high mass components.

**Dave Jones:** So Wow, I find that totally fascinating how it's able to do that. Oh, check that out. Something has gone horribly wrong with that. That's the bottom of it. It's like got black goo or some crud on there.

**Dave Jones:** That is really really interesting. Wow. I wouldn't have expected it. Like, this was one of the things I was looking for was a dodgy solder joint. I wouldn't have expected a surface mount part like that to shear off, but what is Some Something's gone What?

**Dave Jones:** What on earth has happened to that? Look. Look at the side, the cap. Everything else is that blown? Wow, like there's no way that inductor could blow. It's not There's no way that could blow and not uh blow the input circuitry.

**Dave Jones:** So that is Wow, that is toast. I can't just Well, I could flip it over. I could flip it over and resolder it back on, but geez, you know.

**Dave Jones:** Flip resolder it on upside down like that. But that is horrible. Has that just been a badly produced inductor? You can get that uh it's some something's gone horribly wrong with that.

**Dave Jones:** Yep, I think we just have a bad inductor there. There's nothing on the soldering. Look at that. There's the uh there's the other half of the of the uh cap from the inductor and it's just Yeah, we have a faulty part.

**Dave Jones:** We have a faulty inductor. Something's gone horribly wrong with that inductor. And obviously it still made contact. When they assembled this thing, it was still fine and would have passed its test.

**Dave Jones:** But uh after that it's just gone horribly wrong. But as I said, there's no way that you could um blow that inductor and not blow your inputs. So, you know, let not have your input protection uh trip and you know, blow out your traces and everything else.

**Dave Jones:** So, it hasn't been overloaded. I think we have a genuine inductor manufacturing fault. So, there you go. I desoldered that from the PCB and that And of course, what we're dealing with here uh this is actually the common terminal, this wire here, even though it's got red uh insulation on it.

**Dave Jones:** Actually, it comes from the ground terminal on the um front panel. And they're just splitting those off different traces to different parts of the circuitry up here. So, anything that relied upon this ground connection here obviously did not work.

**Dave Jones:** So, there we go. We're splitting some more. There's another uh star grounding point. Very nice. They know what they're doing there. Um so, what they're doing these you see the little uh slots in there, too?

**Dave Jones:** They've got little isolation slots down in there. What they're doing with these, these aren't um well, they're not wound inductors. These are RFI uh beads actually just for some high frequency rejection to uh like, you know, pass the emission uh standards and compliance and all that sort of jazz.

**Dave Jones:** So, yeah, I mean, you could bridge that over with a short if you wanted to. You could put in a zero ohm resistor if you didn't care about the, you know, the EMI requirements and things like that.

**Dave Jones:** Not sure I have a suitable RFI bead, so I might just potentially bridge that with a zero ohm resistor just for now, and that should get us up and running.

**Dave Jones:** All right, let's retest this puppy. 1 volt. And we will we have a winner? I think we will. Winner, winner, chicken dinner. There we go. Ta-da! That's all it was.

**Dave Jones:** We had ourselves a faulty component. I have no doubt everything else will work now. If we just do the ohms, for example, the ohms will work. Ta-da! There we go.

**Dave Jones:** Works a treat. No problems. That was the only thing wrong. It was that in was that RFI bead in there, which I'm pretty sure that's a faulty component. That hasn't happened during the soldering process or, you know, there's nothing wrong with the soldering process there.

**Dave Jones:** It was that component was crap. There was something seriously wrong with that, and well, yeah. Hmm, happens. So, I hope you found that interesting. I'm glad we actually found that.

**Dave Jones:** That was pretty darn easy in the end. Only took, you know, seconds. It was like one of the first things I saw when I opened that when I took that board off the back of it.

**Dave Jones:** So, pretty easy, and we didn't need a schematic to find that. So, component fault. These things happen. And to me, it doesn't really reflect upon the quality of the product.

**Dave Jones:** If there was more than one and this was a, you know, a systemic problem, then we might have an issue. But, I, you know, ultimately you've got to trust the components that you're buying, you know, the genuine component you're buying from the genuine manufacturer.

**Dave Jones:** They're all in the real. You expect them to be manufactured properly. It's not like the the manufacturer of the meter or whatever product it is can actually inspect those parts for themselves.

**Dave Jones:** You rely on the fact that you're buying quality parts. And well, you know, occasionally you're going to have the odd component weird component failure like that for whatever reason.

**Dave Jones:** If as I said, it would have been if it was like the entire real the entire batch of these little ferrite beads that was dodgy then yeah, there would have been, you know, I'm sure we would have had a lot more reports.

**Dave Jones:** So, I suspect this might just be a one-off. Anyway, I hope so. So, yeah, I'll definitely show Brymen this video and I'll no doubt investigate it and see if anything else.

**Dave Jones:** I might open a couple of other meters I've got in stock here. Although, this one actually, you know, I've only got the new batch. So, yeah, no, I don't think I can even open Well, I won't my current stock anyway just to have a squeeze and I'll give a little bit of a wiggle on the ferrite bead down in there and see what happens.

**Dave Jones:** But, yeah, I I'd be surprised if this was a systemic problem across all meters. I think we've just encountered one of those weird one-off Murphy's issues. Anyway, I hope you enjoyed that little hunt down of that problem.

**Dave Jones:** If you want to comment as always, links down below, leave YouTube comments, etc. Catch you next time. Hi, check this out. Look, amazing. Symmetrical multimeter stacking just like the Philadelphia mass turbulence of 1984.

**Dave Jones:** Unbelievable. No human could stack multimeters like this. That's a few multimeters, 40 to be precise. I can't explain it, but there's something very therapeutic about doing this. Oh, yeah.

**Dave Jones:** So, I've got my handy banana plug lead. Here I go. Goodness, the things I do.
