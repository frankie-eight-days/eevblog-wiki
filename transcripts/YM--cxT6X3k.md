---
video_id: YM--cxT6X3k
title: EEVblog #884 - EEVBlog BM235 Multimeter REPAIR
url: https://www.youtube.com/watch?v=YM--cxT6X3k
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 32, "3": 47, "4": 60, "5": 71, "6": 87, "7": 104, "8": 120, "9": 139, "10": 159, "11": 175, "12": 191, "13": 216, "14": 232, "15": 253, "16": 268, "17": 278, "18": 291, "19": 315, "20": 329, "21": 351, "22": 367, "23": 381, "24": 395, "25": 406, "26": 420, "27": 433, "28": 443, "29": 456, "30": 471, "31": 483, "32": 501, "33": 520, "34": 536, "35": 553, "36": 569, "37": 582, "38": 596, "39": 609, "40": 623, "41": 638, "42": 655, "43": 666, "44": 679, "45": 695, "46": 718, "47": 734, "48": 763, "49": 779, "50": 801, "51": 818, "52": 838, "53": 859, "54": 879, "55": 903, "56": 920, "57": 935, "58": 952, "59": 968, "60": 984, "61": 1001, "62": 1016, "63": 1030, "64": 1044, "65": 1057, "66": 1073, "67": 1088, "68": 1105, "69": 1120, "70": 1132, "71": 1145, "72": 1158, "73": 1173, "74": 1186, "75": 1202, "76": 1216, "77": 1230, "78": 1248, "79": 1270}
---

**Dave Jones:** Hi, I thought we'd take a look at the first return to EEVblog BM235 multimeter. Um, Frank actually bought one of these. He's in Jacksonville in Florida and unfortunately he got it and it didn't work. And he's yeah, he described all sorts of things

**Dave Jones:** in that it would you know measuring say a 1.5 volt battery and it'd measure 0.6 volts and then it'd drift down to zero and and all sorts of stuff weird things didn't work at all. And um, I have sold

**Dave Jones:** I think over a thousand of these meters so far and this is the first one that's reported any issues like this at all. So yeah, you expect this sort of thing to happen even though each meter is individually tested at the factory. It

**Dave Jones:** has to be because it has to be calibrated at the factory. So each one would have been tested but you expect some sort of infant mortality rate on virtually any product out there. It's not just this meter but any electronic uh

**Dave Jones:** product. There is going to be some percentage of failure rate um, after they're tested and they hit the field. It's just you know the way it is for whatever reason. Um, and that's no reflection on the quality of the thing

**Dave Jones:** or well, it could be. Okay, but in this case sold over a thousand no problems and this is the only one. So you know, who knows Murphy's law. Uh, we're we've got one. We got one. And sorry my voice is still

**Dave Jones:** terrible. Um, I haven't made any videos this week because um yeah, I just yeah, you don't probably don't want to see me on camera either. So I look and feel pretty terrible at the moment. And uh, if you haven't been following me on

**Dave Jones:** Twitter, I am breaking in all sorts of ways. I've busted my ACL joint in my knee is completely busted. Anyway, um, there's the probes. So yeah, I might have to get surgery on that. So, yeah, I'm doing wonderful at the moment.

**Dave Jones:** Let's unwrap this puppy and have a look. And see if A, it's repeatable. Um but yeah, I'm pretty sure, you know, from the stuff he was uh was saying it was pretty obvious that this thing was dead. So, let's turn it on

**Dave Jones:** and uh see what we've got here. Switch on. He said it worked on AC, curiously. Now, that, you know, function-wise, it's it's displaying the right stuff. Okay. So, there we go. Okay, no drama at all. I've got a um

**Dave Jones:** I've got my voltage reference here. I've got it set to a volt. This is my lab reference one of my lab reference standards. So, let's plug it in and um see if we get a volt. What what what what. He's right, look.

**Dave Jones:** It's going down and down. It's not like it's on AC mode, it's on DC mode. And sure enough, I mean, if I bring in a good one over here and of course it will uh measure a volt. No worries whatsoever. So, um

**Dave Jones:** yeah, that is one sick puppy. What is wrong with it? Wow. Let's maybe whack it on ohms here and uh disconnect that and okay, ohms works. Oh, no, that was continuity. That was con- Oh, continuity mode, look. Nope.

**Dave Jones:** Okay, ohms is just showing direct short. That's interesting. That's interesting. I well, I was going to maybe there's some sort of um solder short on the board or something that's causing that. I mean, obviously our chip set's working

**Dave Jones:** fine. Um and there's not much in this apart from a the multimeter chipset. That's pretty much the only active circuitry and the LCD driver chip. Um the capacitance Oh, that seems a bit high. 13 nF, I'm not Hang on. I've got a reference cap here.

**Dave Jones:** Here we go. Let's check it out. I've got myself a um These are very nice if you can pick them up on eBay cheap. They're old, but uh these Arco standard capacitors, they're very very nice. And um you can often get them

**Dave Jones:** quite cheap. Uh that's low. That's low. Put it over here, but at least it's functional.

**Dave Jones:** There we go. No dramas whatsoever. That's well within spec. Um so yeah, this one is a bit there and I've checked other meters. I think that is, yeah. So this one's a bit low on cap. Let's measure some current, shall we?

**Dave Jones:** Here we go. I'm feeding in 1 mA current range works. Current range works. 10 mA, 100 mA Hey. Okay. That's interesting. That shows that well, because the the current uses a different input arrangement. So yeah, there's something with that main common

**Dave Jones:** terminal which, you know, is like So it's not the chipset. It's not like I don't know, ESD or something else has gone wrong with the chipset and it's damaged because the current just works fine. Let's try the microamp range. 100

**Dave Jones:** microamps There you go. Yep. It works just fine and dandy. And hold on to your hats, the millivolt range works fine and dandy as well. So um yeah, Okay, interesting. So millivolt range works. Current ranges work. Uh so, chipset is

**Dave Jones:** just fine, but all the other functionality, like if we go back here to our volts, you know, like that is that is dead. And let's just jiggle the range switch around here. Jiggle is a technical term. And um it's

**Dave Jones:** not that. So, looks like something on the front end of this thing is gone on particular ranges. The millivolt range is basically straight in. It doesn't go through the input divider or anything else. Um unfortunately, I do not have

**Dave Jones:** the schematic for this. Um Brymen will not uh release it uh to me. They say it's proprietary, blah blah blah. Yeah, okay, fair enough. Um so, we don't have that, but hey, we can at least have a look around. Let's go. The serial number

**Dave Jones:** for those playing along at home. And we're in like Flynn. Um unfortunately, we're going to have to take this uh top board out here. That's uh one of the downsides of uh having the CAT IV rating in such such a small meter. That's the

**Dave Jones:** only way they can physically uh do it. And that's where uh a bit of the input uh circuitry is around there, but we can see other stuff on here. And uh I might actually uh get out the uh Tiganu microscope. Just

**Dave Jones:** get the two side by side and see what we can see. Oh, and the other annoying thing about having the secondary board here is cuz I do have to actually desolder this and unplug um essentially unplug the uh jacks and

**Dave Jones:** everything else to get in there. We can't sort of like feed in stuff and then measure it on the main board underneath at the same time. So, that's uh well, you can if you go to a lot of

**Dave Jones:** trouble to wire it back in and stuff, but yeah, uh just makes it a bit trickier to troubleshoot. But, the first uh thing you do with troubleshooting something like this is visual, especially if you've got a unit to

**Dave Jones:** compare it against. All right, let's check this out. We've got our unhappy camper on the left here and our happy camper on the right. And, uh I'll probably just just because you can, do a quick uh visual inspection to see if there's any

**Dave Jones:** missing parts. Now, this, you know, shouldn't be the case because, as I said, it would have passed factory test, factory calibration, everything else to do that. It would have had to have everything um in place, but I don't

**Dave Jones:** know, something might have made poor contact, and then in shipping it might have vanished or something like that. But, um I I can't obviously see under the uh uh input board yet, but it doesn't look to be any issue here at all.

**Dave Jones:** I wouldn't expect that. But, uh see the nice little uh star grounding point there. Very nice. Just going off. Someone knew what they were doing in terms of uh PCB layout. But, uh yeah, there's nothing obvious going on

**Dave Jones:** there at all. As I said, um the main chipset down here, which is um BTC, which is Biwin Technology Corp uh branded. I don't know exactly what one it is. They won't tell me. Um but, uh that is obviously not failed

**Dave Jones:** because half the functions work, and the other half don't. So, there's got to be something screwy with some with something to do with the input. So, that all looks hunky-dory. The other thing, next thing I would look for is uh

**Dave Jones:** any um shorts, like uh little solder balls or anything like that um as part of the production process, which could have uh got in there. And, they may not have been an issue during the uh during the process. I love my Takano

**Dave Jones:** microscope here. It's beautiful, isn't it? Um I can go all the way in. Can go all the way with LBJ. Look at that. You can see the uh silk screen's actually a uh dot matrix print. It's not a uh photo

**Dave Jones:** imageable silk screen. You can see the dot pattern on there. And uh but yeah, our solder balls, they could um certainly account for it. Uh as part cuz they're like sort of like a little unknown thing. You got slightly

**Dave Jones:** too much paste. You know, it's not exactly the same every time even though, you know, it might be a smidgen over or just how the, you know, the dynamics of the paste and everything else and how it melts and things like that. Um you can

**Dave Jones:** often get a stray solder ball. So, I'm just looking for anything obvious like that. Uh and I'm not so I wouldn't expect to see it up the top cuz this is like as I said, this is the LCD chipset. All

**Dave Jones:** right, here we go. Here's the top board. We've got our Here's our voltage input, of course. There's two input protection resistors. I can measure those, of course. They're uh 1K. Good old brown brown black red there. And I don't think it's going to

**Dave Jones:** be our PTCs here because otherwise we wouldn't get anything. But anyway, ooh. Is that got a little Uh somebody's had a little crimp. No, no, it's all right. No worries there, but we could measure those. They should be about uh a K each or something like

**Dave Jones:** that. But as I like if it wasn't broken like that doesn't explain like the zero ohms and things like that. And the mobs here, well, you know, in theory it could be, but uh doesn't explain why the 100

**Dave Jones:** mV range was working, for example, and you know, it couldn't measure 1 V. Um so, you can measure those. They they should be open, of course. They should only start clamping at uh you know, 1,000 V or whatever they're

**Dave Jones:** rated for. And we've got some uh 5 meg input resistors here. You can measure those. Might be doing silly buggers, but we've got uh um input uh jack uh detection stuff like that. So, it's not that. Um so, there's

**Dave Jones:** nothing on the top board really that you would suspect. I'd be going straight for down here. And let's let's have a squiz around here. And once again, I'm looking for bad joints. Hello. Hello. Hang on. L9, is that my imagination?

**Dave Jones:** Hang on. Sorry. I don't may not Oh, no. No. No, that's all right. No, I thought there was no fillet on that. But, it's it's all good. So, I'm looking for bad solder joints. I'm looking for uh solder balls,

**Dave Jones:** shorts, other things. But, uh whoop. What's going on down there? That Oh, hello. Hello, L3. Tada. Hello. Look at that. L3 has cracked. The solder joints on L3 have cracked. We got one. Yep. Wow. How has that happened?

**Dave Jones:** Let's bend our wire out of the way there. Sorry about the light here. I can uh I can There we go. That's going to be better. Wow. I thought it looked a bit askew. And you go there and sure enough,

**Dave Jones:** that puppy Wow. That's That's an inductor, and that has sheared right off. I mean, it's not like it's a heavy part. So, that is very very interesting. I'm going to Well, it's gone. Look at that. There we go. Okay, so what I'm going to do is I'm

**Dave Jones:** going to take that out. I'm going to put some fresh solder down on there. Those pads I'm going to Well, I'll put fresh solder down on one, I'll wick the other off, and replace that. And I think it might come good again.

**Dave Jones:** The one next to it Sorry about the focus on this. The one next to it looks The one next to it looks good. That is weird because And okay, solder joints can crack like that, but they're usually on high mass

**Dave Jones:** components. So Wow, I find that totally fascinating how it's able to do that. Oh, check that out. Something has gone horribly wrong with that. That's the bottom of it. It's like got black goo or some crud on there.

**Dave Jones:** That is really really interesting. Wow. I wouldn't have expected it. Like, this was one of the things I was looking for was a dodgy solder joint. I wouldn't have expected a surface mount part like that to shear off, but what is Some

**Dave Jones:** Something's gone What? What on earth has happened to that? Look. Look at the side, the cap. Everything else is that blown? Wow, like there's no way that inductor could blow. It's not There's no way that could blow and not

**Dave Jones:** uh blow the input circuitry. So that is Wow, that is toast. I can't just Well, I could flip it over. I could flip it over and resolder it back on, but geez, you know. Flip resolder it on upside down like that.

**Dave Jones:** But that is horrible. Has that just been a badly produced inductor? You can get that uh it's some something's gone horribly wrong with that. Yep, I think we just have a bad inductor there. There's nothing on the soldering. Look at that.

**Dave Jones:** There's the uh there's the other half of the of the uh cap from the inductor and it's just Yeah, we have a faulty part. We have a faulty inductor. Something's gone horribly wrong with that inductor. And obviously it still made contact. When

**Dave Jones:** they assembled this thing, it was still fine and would have passed its test. But uh after that it's just gone horribly wrong. But as I said, there's no way that you could um blow that inductor and not blow your inputs. So, you know, let

**Dave Jones:** not have your input protection uh trip and you know, blow out your traces and everything else. So, it hasn't been overloaded. I think we have a genuine inductor manufacturing fault. So, there you go. I desoldered that from the

**Dave Jones:** PCB and that And of course, what we're dealing with here uh this is actually the common terminal, this wire here, even though it's got red uh insulation on it. Actually, it comes from the ground terminal on the um front panel. And

**Dave Jones:** they're just splitting those off different traces to different parts of the circuitry up here. So, anything that relied upon this ground connection here obviously did not work. So, there we go. We're splitting some more. There's another uh star grounding point. Very

**Dave Jones:** nice. They know what they're doing there. Um so, what they're doing these you see the little uh slots in there, too? They've got little isolation slots down in there. What they're doing with these, these aren't um well, they're not wound inductors. These

**Dave Jones:** are RFI uh beads actually just for some high frequency rejection to uh like, you know, pass the emission uh standards and compliance and all that sort of jazz. So, yeah, I mean, you could bridge that over with a short if you wanted to. You

**Dave Jones:** could put in a zero ohm resistor if you didn't care about the, you know, the EMI requirements and things like that. Not sure I have a suitable RFI bead, so I might just potentially bridge that with a zero ohm resistor

**Dave Jones:** just for now, and that should get us up and running. All right, let's retest this puppy. 1 volt. And we will we have a winner? I think we will. Winner, winner, chicken dinner. There we go. Ta-da! That's all it was.

**Dave Jones:** We had ourselves a faulty component. I have no doubt everything else will work now. If we just do the ohms, for example, the ohms will work. Ta-da! There we go. Works a treat. No problems. That was the only thing wrong. It was

**Dave Jones:** that in was that RFI bead in there, which I'm pretty sure that's a faulty component. That hasn't happened during the soldering process or, you know, there's nothing wrong with the soldering process there. It was that component was crap.

**Dave Jones:** There was something seriously wrong with that, and well, yeah. Hmm, happens. So, I hope you found that interesting. I'm glad we actually found that. That was pretty darn easy in the end. Only took, you know, seconds. It was like one of

**Dave Jones:** the first things I saw when I opened that when I took that board off the back of it. So, pretty easy, and we didn't need a schematic to find that. So, component fault. These things happen. And to me,

**Dave Jones:** it doesn't really reflect upon the quality of the product. If there was more than one and this was a, you know, a systemic problem, then we might have an issue. But, I, you know, ultimately you've got to trust the components that

**Dave Jones:** you're buying, you know, the genuine component you're buying from the genuine manufacturer. They're all in the real. You expect them to be manufactured properly. It's not like the the manufacturer of the meter or whatever product it is can actually

**Dave Jones:** inspect those parts for themselves. You rely on the fact that you're buying quality parts. And well, you know, occasionally you're going to have the odd component weird component failure like that for whatever reason. If as I said, it would

**Dave Jones:** have been if it was like the entire real the entire batch of these little ferrite beads that was dodgy then yeah, there would have been, you know, I'm sure we would have had a lot more reports. So, I suspect this might just

**Dave Jones:** be a one-off. Anyway, I hope so. So, yeah, I'll definitely show Brymen this video and I'll no doubt investigate it and see if anything else. I might open a couple of other meters I've got in stock here. Although, this one actually, you

**Dave Jones:** know, I've only got the new batch. So, yeah, no, I don't think I can even open Well, I won't my current stock anyway just to have a squeeze and I'll give a little bit of a wiggle on the

**Dave Jones:** ferrite bead down in there and see what happens. But, yeah, I I'd be surprised if this was a systemic problem across all meters. I think we've just encountered one of those weird one-off Murphy's issues. Anyway, I hope you

**Dave Jones:** enjoyed that little hunt down of that problem. If you want to comment as always, links down below, leave YouTube comments, etc. Catch you next time. Hi, check this out. Look, amazing. Symmetrical multimeter stacking just like the Philadelphia mass turbulence of

**Dave Jones:** 1984. Unbelievable. No human could stack multimeters like this. That's a few multimeters, 40 to be precise. I can't explain it, but there's something very therapeutic about doing this. Oh, yeah. So, I've got my handy banana plug lead. Here I go.

**Dave Jones:** Goodness, the things I do.
