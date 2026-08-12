---
video_id: VJJmtm0VmIs
title: EEVblog #1306 (2 of 5): PCB SMD Hand Soldering & Assembly
url: https://www.youtube.com/watch?v=VJJmtm0VmIs
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 38, "3": 63, "4": 77, "5": 91, "6": 110, "7": 120, "8": 136, "9": 157, "10": 168, "11": 186, "12": 204, "13": 221, "14": 234, "15": 252, "16": 268, "17": 280, "18": 297, "19": 309, "20": 333, "21": 353, "22": 364, "23": 383, "24": 406, "25": 412, "26": 436, "27": 455, "28": 479, "29": 511, "30": 533, "31": 550, "32": 568, "33": 590, "34": 611, "35": 627, "36": 643, "37": 660, "38": 684, "39": 703, "40": 720, "41": 739, "42": 759, "43": 775, "44": 793, "45": 809, "46": 829, "47": 847, "48": 866, "49": 881, "50": 898, "51": 918, "52": 937, "53": 959, "54": 977, "55": 999, "56": 1024, "57": 1049, "58": 1065, "59": 1079, "60": 1093, "61": 1097, "62": 1117, "63": 1131, "64": 1152, "65": 1152, "66": 1173, "67": 1187, "68": 1207, "69": 1222, "70": 1240, "71": 1266, "72": 1276, "73": 1288, "74": 1309, "75": 1330, "76": 1347, "77": 1360, "78": 1377, "79": 1387, "80": 1401, "81": 1414, "82": 1425, "83": 1440, "84": 1452, "85": 1467, "86": 1486, "87": 1499, "88": 1516, "89": 1538, "90": 1562, "91": 1581, "92": 1599, "93": 1616, "94": 1628, "95": 1644, "96": 1662, "97": 1684, "98": 1706, "99": 1724, "100": 1742, "101": 1763, "102": 1784, "103": 1805, "104": 1821, "105": 1842, "106": 1860, "107": 1876, "108": 1893, "109": 1907, "110": 1923, "111": 1939, "112": 1956, "113": 1970, "114": 1995, "115": 2001}
---

**Dave Jones:** Hi, this is part two of the Padauk 3-cent microcontroller programming series, where we build up open source programmer hardware and install the open source software to program these 3-cent microcontrollers. So part two here is just going to cover assembling this PCB. So there's lots of like soldering and assembly tips and stuff like that.

**Dave Jones:** Let's go. Ta-da! A little while later, all your stuff just magically appears. PCBs and all your parts baggied straight from Willy Wonka's chocolate factory. All right, let's have a look at our PCB here using our Tagano and we're in like Flynn. Check it out.

**Dave Jones:** All right, doesn't that look neato? Unfortunately, of course, there's no silkscreen overlay, so we have to like use an overlay diagram if we're going to assemble this sucker. And let's just check we didn't get any of that gold flash rubbish. So let's just go in and check out the alignment on the solder mask expansion.

**Dave Jones:** You can see we've got our solder mask going between pads there. No worries. That's pretty good. That's a reasonable alignment for a proto like this. No problems whatsoever. There's no, you know, they're not overhanging the pads or you could argue that there's a little bit of overhang

**Dave Jones:** on the pad there, but you know, nothing to write home to your mum about for however couple of years we've played for these things. It's just, yeah, it's just fine. And the registration on the vias, hey look, bang on. Look at that. Smack in the middle.

**Dave Jones:** No wuckers. And of course, this board is, has tinted vias, which means that the solder mask comes over the via like that. No, they're not actually plugged. It's just that the solder mask happens. You can actually get plugged vias. That's a separate process.

**Dave Jones:** This is just the solder mask just goes over the top. And sometimes you get it to like, oh, has that got a little pinhole in it? Sometimes you get like complete coverage like that. And these ones down here, other times you'll get it.

**Dave Jones:** You'll actually get a hole through there. Do we actually have a hole through there? Do we actually have light coming through that hole? No, I don't think so. No. Anyway, sometimes you get it going through and sometimes you don't. Just depends on how the dice rolls.

**Dave Jones:** Anyway, that board looks pretty decent. More than decent enough for a proto. When I was a boy, you couldn't even get something like this for a hundred bucks, let alone a couple of bucks. If you paid a hundred bucks and you'd get a, it was

**Dave Jones:** a miracle when paid a hundred bucks and you could get like a tin plate board. None of this solder mask rubbish. You get tin plate. So yeah. Anyway, that's good enough for Australia. So what do we need for this? Well, we need our schematic.

**Dave Jones:** That's always handy. Then we need our diagram. Yes, the distortion in that, in barrel distortion there is caused by the lens on the Tagano. It doesn't go away unless I zoom, you know, it's still there, still a little bit there, but you know, you zoom in near enough and then it's all right.

**Dave Jones:** There we go. I'm going to zoom in a long way before it actually becomes fine. That's to do with the lens that I've got on this thing. Cause this thing's got like 30 times zoom. It is huge. I mean, this is why I can go from a

**Dave Jones:** wide view like this with my hands to all the way in. And this is not digital zoom. This is optical zoom. Thank you very much. And that's the price you pay for all that zoomity goodness. Anyway, there you go. Got to have our overlay and we got our bill of materials just in case, you know,

**Dave Jones:** you want to do some cross references and stuff like that. Um, we don't actually have the designator in here, so it's not entirely useful, but anyway, you might want to do a cross reference and the age old debate, of course, whether or not you should actually

**Dave Jones:** put values on the silk screen overlay in this particular case. Um, you didn't want this overlay because you wouldn't want to get this overlay printed because this, uh, the designator here would be smack on the pads and you don't want your, um, your silk screen overlay overlaying

**Dave Jones:** your pads. That's going to ruin your day. So like, you know, this has been optimized for not for printing on the board, but it's been optimized for, uh, you know, assembly. But yeah, there's a bunch of fanboys out there who love putting the component designator and

**Dave Jones:** the value on there and for assembly and for troubleshooting and repair and stuff like that. Good idea. So with this board, the first thing I'll put on, because it's the biggest and it's just super satisfying to do it up front, um, put the chippy on first.

**Dave Jones:** And especially if you've got lots of parts, like really surrounding the chips like this, like close to the pins, if you had lots of bypass caps, there's not really that case here. You could argue this one's a little bit close. It's just that if you got, if you put all those

**Dave Jones:** passive parts on first around your chip, then it can be hard to get in there and do, uh, you know, get your ironing. You've got to come in at a much higher angle like that, rather than just rest your, uh, hand on the bench like that and come in at your normal angle.

**Dave Jones:** You've got to tilt it right up and that can be annoying and that can, um, impact your soldering technique. All right, there's our little chippy. So we want it according to the diagram. We want it like that, up in the top right pin one, in the top right corner, beauty.

**Dave Jones:** All right, before anyone asks, I'm using my Pace ADS, uh, 200 iron here, because I just like it. It's very nice. And I'm using 0.38 millimeter, uh, tin copper, i.e. lead-free solder. So it's a five core, uh, flux multi-core brand. And, uh, I like using fine solder for surface

**Dave Jones:** mount stuff like this, because you can just feed much finer control than if you use like 0.8 millimeter stuff like that. You can just, you know, when you're feeding onto the, oh, you can see the heat, the shimmer in the video from the heat.

**Dave Jones:** Love it. Anyway, um, yeah, you can just feed in a more precise control over that solder. So there we go. It's maybe a bit more suitable, although you can't use big tip. No whackers. And no, I'm not using any, uh, PCB holder or anything like that.

**Dave Jones:** See, even with this tiny solder, look at the amount of solder that we've put on that pad already. No, I'm not using any, uh, PCB holder at all. So there you go. We've tacked, oh, I was a little bit off. There you go.

**Dave Jones:** That's a bit better. It's a bit how you're doing before. There you go. We tacked down one pin. And then you just want to go in the opposite corner. Like this. And tack that down as well. Just tack that one down there like that.

**Dave Jones:** And bingo, chippity-doo-dah is not going to move anymore. So now we can get in there and we can solder. So I'll get my flux. I just use a chem tools, uh, local brand. No clean flux pen does the job. Some flux. There we go.

**Dave Jones:** We can go all the way around if you want. Just put some flux on there so that our joints are going to be cleaner. All right, should we do drag soldering or not? Oh yeah, why not? Look, I'll go to my well base tip.

**Dave Jones:** And there we go. You can see that's got a well in there and that helps the surface tension drag the solder away. Oh, some daggies. Had some daggies. Hang on. Don't know where that came from. There we go. So we'll just feed some solder into there like that until it bulges out a little bit.

**Dave Jones:** Start on the unsoldered side, shall we? And there we go. That is soldered. Got a little bit of dag left over there. That'll just fall off. No wuckers. There we go. Fortunately, our chippy's not perfectly lined up. But anyway, no wuckers. That is actually soldered, believe it or not.

**Dave Jones:** It's terrible, Muriel. Let's put our solder in there. And then let's just go along here and... Oh, there we go. That looks sweet as. Once again, all those little daggs will clean up later. Probably would have done better without the well-based tip, I think.

**Dave Jones:** I don't know. Soldering looks terrible up close, like really magnified. It's always better from a distance. Next up, well, do the most prolific thing. So 100N capacitors. I just, yeah, we've got 12 of them. So just get 12 out of the bag and then go around and populate them.

**Dave Jones:** And then if you actually count 12, then you can't get it wrong. If you've got one left over, you know, you missed one somewhere. And be careful when you tip these out because these things can... Fling around everywhere. And you can come a gutter and you can lose one.

**Dave Jones:** Trap for young players. So what you want to do now is go around and just tack one side. Of course, the right-hand side because I'm right-handed. So I tack the right-hand side of all of the capacitor pads. All 12 of them first. And then, because if you do it one by one, it's just much harder.

**Dave Jones:** So, yeah, I believe that one there. So I just put a bit of solder on there. That one there. In fact, you could argue that it's best to just simply go and do everything. Really, like go and do every single pad. So then you'll be ready and raring to place those components.

**Dave Jones:** Some people don't like to do that. But once again, components can get in the way. Well, a little bit too much solder on the previous pad there. Rather than just try and... Find them all. Maybe just go in and do them all. That was a thermal mass thing.

**Dave Jones:** That was... Yeah, the tip is actually too small. But just be consistent. If you're doing topside, do topside for all the components. And, you know, left for all the others, etc. Oh, no, I goofed it. That one goes in that direction. That one goes in that direction.

**Dave Jones:** Oops. Sometimes you do that. That's what happens when you don't have your silkscreen overlay. Your cummer guts are. You don't know what's the right way up. We'll do that for our SOP23 package there. No whackers. Even for our big daddy jobby up there.

**Dave Jones:** We'll do that. And these two tiny little... Tiny little diodes. Oh, itty bitty. And we won't... Well, okay, yes, we will. We'll do a one pin on that USB. Oh, no, that's... Oh, duh. That USB is... It's got holes there. USB connector. Shouldn't have done that.

**Dave Jones:** Well, it doesn't matter. And might as well do it for the inductor up there, too. Now, normally, I actually wouldn't be doing this on the Tegano with a digital screen like this. I'd either be using my Mantis or nothing at all. Just be using my eyes, my Mark I eyeball.

**Dave Jones:** But because I've got to shoot this video, you know. The Tegano is the best way to do it. The camera inside. The Mantis absolutely sucks for video. So, yeah. Mantis. The Tegano absolutely kills it. So, there we go. I think we've got solder on all our pads.

**Dave Jones:** Now, we can go around and place some of our caps. Where do we want to go here? Where was one? There was one C12 down here. That's definitely one. So, we'll just place our cap on there like that. I would go around and solder them all in one pass later.

**Dave Jones:** And then do a second visual inspection pass after that. That one's most likely a bypass cap because it's going to the ground plane there. Am I right? C2. I think I remember. Yep, C2. No workers. So, let's get C2. There we go. You can do this really fast if you know where they all are.

**Dave Jones:** Like, if you're doing it like I am, you've got to, like, hunt and pick to find the damn things. C8. You know, if you're assembling a whole bunch of things, a bunch of boards, you'd get used to what's what. And there we go.

**Dave Jones:** Got to have a nice pair of fine tweezers. And they've got to be wide enough, like, to place to get over chips like that as well, by the way. So, you know, you've got to have multiple. Like, get different types of tweezers. You need bent ones and all sorts of fancy-pantsy ones.

**Dave Jones:** Yeah, this chisel, this tiny little chisel tip, I don't know, like, is it like half-millimeter chisel or something? I don't know. 8.8-millimeter chisel or something. It's probably, like, it's too small. These are 0603 parts, and I just don't have the other one, another one to hand.

**Dave Jones:** I could find it and put it in there, but... Oh, maybe. That one there is probably more suited, I'd say. That one is a 1 16th. I don't know. What's that bloody metric? Meh. Almost tombstoned in there. This is the problem with, um...

**Dave Jones:** Like, digital microscopes like this. It's hard to see, because they're not three-dimensional. It's hard to see whether or not, um, components tombstone. It's much better under a mantis or with your eyes. Okay, sorry. I'm not sure why the, uh, Tagano Capture froze there,

**Dave Jones:** but anyway, lost a bit of material. Now we'll do the SO-8, and I swear I've been spending at least half of my time just finding the location. Of parts. Wow, those pads are big. Very generous. Um, left a lot of, uh, generously left a lot of solder.

**Dave Jones:** Look, and I still can't find where that 4.7 might goes, I swear. Like, it'll come out in the wash, but it's just, eh, it's really annoying to, uh, you know, just have to spend most of your time just finding parts on the board.

**Dave Jones:** Where to actually place them. And for something like this SO-8, you wouldn't even bother to drag solder because it's so quick and easy just to do 'em one by one like that. Yeah, I didn't put any, uh, flux on there either, so I'm just relying on the solder flux.

**Dave Jones:** Anyway, if you don't know, um, the, the IP, official IPC standards for footprints, they come in, um, small, normal, and large size pads. And basically it has to do with the, your den- the density of your board. And if you've got a really dense board, and it basically has to do with, like, how much pad, like, overlays, like, the end.

**Dave Jones:** Like this, so that you can get your iron on. And the good thing about having them extended long like this is that you can actually use this, uh, use this, um, extended bit as a test point for a flying probe tester. So they're actually very handy, so if you've got the space and you know your board's going to be flying probe, uh, tested,

**Dave Jones:** don't use, like, the small, uh, footprint pad, which you'll have, like, you know, they'll basically be no pad, almost no pad extending over the end there. They're just very small footprint, very compact footprint. So the, uh, flying probe tester will have to come down onto the leg of the IC and then it can slip off and shorten, you know, and do all sorts of things.

**Dave Jones:** So, uh, yeah, having larger pads like that is actually, um, can be rather, uh, handy. It's, you know, it- it's a luxury if you can afford it. And then the little SOC 23-6, I have to tilt that, you can see the, the tiny little dot in the top left-hand corner.

**Dave Jones:** Uh, and that goes in there like that, so, yeah, don't, don't rely on the text, uh, always go by the actual dot. And we've got our little diode-y, and the end with the lines on it like that, that is the cathode. So that lines up nicely there, look at that, beautiful.

**Dave Jones:** Now here's where you can really come a-guts-er, with leads, look at these little suckers, always measure them. There we go, so, the negative is, i.e. the, uh, cathode, is the one that, although this one has a green line, that one necessarily doesn't. But, uh, yeah, so, that end, closer to the internal die there, is the negative end.

**Dave Jones:** Now, here's the interesting thing, is that you can't tell from the overlay which way around that lead goes. Here's the three leads. Got a chamfer. On there, what does the chamfer mean? Well, could actually mean, don't rely on what that chamfer means, 'cause there is no physical embodiment of that chamfer on these leads, right?

**Dave Jones:** So, on other types, other physical types of leads, they may, there may be. So, what does that chamfer mean? Well, you don't assume that it means anything. What you do, is you actually check out the PCB. There's our three leads. Here's our three resistors.

**Dave Jones:** And, you see, the series resistor is, uh, going up to the positive rail here. So, if you have a look at our schematic here, you'll notice that there's the resistors up the top to the positive rail. There's our anode, there's our cathode. Our cathode goes over to the chippy over here.

**Dave Jones:** And, you can physically see that embodied on the PCB. So, this would be our cathode going off to the chip, and the anode goes over there. So, bingo, I've got a flip, 'cause we said that end there was the cathode, so I've got to flip it around.

**Dave Jones:** So, bingo, I've got a flip, 'cause we said that end there was the cathode, so I've got to flip it around. So, bingo, I've got a flip, 'cause we said that end there was the cathode, so I've got to flip it around. Focus, you bastard.

**Dave Jones:** Alright, so, I flip that around like that. And, and we'll just take that over to there. And, we'll solder that in place. Be careful with leads, they really don't like heat. Um, leads aren't very forgiving. There we go. And, just for good measure, for sanity check, there you go.

**Dave Jones:** Make sure you've got them in the right way. It's so easy to come aguts, especially, you know, if you go to-- Nothing worse than going and soldering down a hundred leads, and then realizing you've got them backwards. It happens. Now, it's time for some resistors.

**Dave Jones:** Now, you should always put these in the same orientation. So... Why? Just because. It's good practice, so that you can read and inspect later. Just because. It's good practice, so that you can read and inspect later. Just because. It's good practice, so that you can read and inspect later.

**Dave Jones:** Just because. It's good practice, so that you can read and inspect later. Just because. It's good practice, so that you can read and inspect later. Just because. It's good practice, so that you can read and inspect later. Just because. It's good practice, so that you can read and inspect later.

**Dave Jones:** Just because. It's good practice, so that you can read and inspect later. And some people like to actually solder them upside down, like as in, like literally flip them upside down, just for shits and giggles. But there's actually a practical reason why some people will solder them upside down, because when you pull them out of the tape like this, they could land either way, right?

**Dave Jones:** So if they land like that, some people just go, oh, bugger it, just solder it in upside down. I couldn't be bothered flipping the little bastard. There it is. Like, oh, and it just so happened to flip in the direct orientation. Murphy must be asleep today, but yeah.

**Dave Jones:** And so if you ever see them sold, parts soldered upside down like that, you'll know why people just went, ah, screw it, couldn't be bothered. Look at all the resistor values in here. One, two, three, four, five, six, seven different resistor values. Did we really need all those different values?

**Dave Jones:** Like, just ask yourself, when you're actually designing, yeah, it could be very good reasons for it, but try to consolidate resistor values if you can. It's really handy. You know, it just means one extra, one less real you've got to put on your pick and place machine.

**Dave Jones:** And of course, for a manual assembly point of view, I've now got to take open, crack open seven different packets, you know, pull back the tape, get out. Like, this is a 10K resistor. There's one of them on the whole board. Thanks. All right, let's try and flip six of these.

**Dave Jones:** Suckers, what'll we get? Oh, five out of six. Oh, close, but no cigar. All right, I was just going to put down a couple of my last resistors, and I found that one I was supposed to put down was already populated. This one, this 20K one was actually in here, and it made sense because all these 20Ks were bundled together, and maybe that's why I thought it was okay.

**Dave Jones:** And I'm so glad I didn't solder the other end. I'm going to do that as one last pass. Because then I had to take that out and move it over to there, and it was trivial. It took, like, two seconds to do that.

**Dave Jones:** But, yeah, you're eventually going to come... Even on a simple board like this, you know, this is hardly any parts at all. But with actually eight different types of resistors, you know, odds are you're going to, like, you're going to give one of them.

**Dave Jones:** Now, here's an interesting thing. Look at these little diodes here. Little SOD 523 packages. Real pain. Look at the size of them in the tape there. Yeah. Actually, every second one in the tape, which is interesting. So, the problem with... Look, there's... This board is not a dense board.

**Dave Jones:** There's absolutely no reason to use such a tiny package like the SOD 523 like this. Because you'll have trouble. The little pick-and-place head will have trouble with these parts. Look, 06... These are actually smaller packages than 06, 03. They're kind of like down here.

**Dave Jones:** And the 0402 region, and that's, you know, okay. But there's no reason to use that. And, like, some... Depends on your assembly factory. Some pick-and-place machines won't be as capable, or most, actually, won't be as capable with 0402s as they are with 0603s.

**Dave Jones:** So, there's just no reason. Like, you'll just get, like, a lower, slightly lower yield. Or some manufacturers might go, oh, we hate 0402s or whatever. You know, like a real, you know, using real old gear or something like that. There's no reason to use...

**Dave Jones:** Such a tiny little diode like that. Anyway, can you see the mark? Oh, there we go. If we zoom in, we can see the marking on that. There it is. Tiny little cathode mark on there. A little line. But, yeah. Zoom out. Like, this is where you need...

**Dave Jones:** Like, there's no way you can see that. You know, you probably can't... Maybe when I was younger, I might be able to see that with my... With my eye. But, like, if you get the light at the right... Oh, yeah, I can. It's...

**Dave Jones:** I'm just getting glare. Just the lights at the right... The right angle. I can't see diddly squat when I'm using this... This Tagano microscope. I've got to actually look at the microscope. Because the angle of the light comes down like this. It's up in here.

**Dave Jones:** It's up in here. And it shines down. And then it's the perfect angle that it just gets in my eyes. And I can't... Like, I can't see any of the markings on those resistors or anything. It's hopeless. That's not my eyes. It's that.

**Dave Jones:** It's just the angle. All right. I've gotten to the point where I've put in all of my passives. Now, you don't want to put in... Put in something like a crystal. And why they used a through-hole crystal there... I don't know. Everything else is surface mount.

**Dave Jones:** Use a surface mount crystal. Doesn't make any sense. If you're going to... Oh, no. I forgot three... What happened to three resistors up the top there? All right. I know the reason why I missed those three 1K resistors for the LEDs is because I don't actually have them.

**Dave Jones:** I can't find them here. So I had all my resistor packets and I went, Right, I've gone through all my resistor packets. I assume I've placed all the parts. And I come back and... Wah, wah, wah, wah. No. Um, they're missing. So maybe I didn't order them.

**Dave Jones:** Maybe they weren't on the bomb or whatever. But, um, yeah. Yeah, I definitely haven't placed them because there's three of the... Only three on the bomb and there's three missing on the board. So, um, yeah. Missing part. It doesn't matter. I've got a kit.

**Dave Jones:** Because it's a LED dropper resistor, why use 1K when, like, it's popular value? So I'm going to use some 820 ohms. No worries. Don't use those much. So, yeah, don't want to run out of... My 1Ks. So, there we go. 820 ohms. Make the LEDs a bit brighter.

**Dave Jones:** All right. Now comes the time that we want to go in and solder the ends of them. So if you've soldered, like, everything, say, on the right-hand side, if you right-soldered, then you know you've got to get everything on the left-hand side. And if you soldered everything from the top,

**Dave Jones:** you know you've got to get everything from the bottom. So hopefully, if you go through the board, you should be able to just find them and tack them down. Just go... Systematically... Oh, that was a shocker. Too much solder, Dave. Oh, absolute atrocious...

**Dave Jones:** Oh, terrible, Muriel. Absolutely terrible. Anyway, you don't need any flux for doing the components. Just rely on the flux in the solder, unfortunately, because of the angle of my eye and the things focusing on my iron. And hopefully, if you go reasonably... Sister, I'm not.

**Dave Jones:** I'm not being... Systematically... Here's where, like, real pain to get down into that diode-y down in there. He's really trouble. I've got to go near vertical on that iron to get down into that. That's... Yeah. That's really annoying. You've got to think about stuff like that

**Dave Jones:** for hand soldering. It matters. And here's where I don't like these digital microscopes. Like, you know, you're looking... You're looking down on it. I mean, look, I can... I can actually tilt this. I can actually tilt it on an angle like that. I can tilt the Tagano.

**Dave Jones:** So it kind of gives you, like, a... Like, just a different angle on the... Because when you've got, like, a top-down view, it's not that great. And here's why I didn't solder in the USB connector, by the way. Because then it would have been a pain to...

**Dave Jones:** access those pads down in there. Oh, that's a bit how you're doing that joint. Alignment on that resistor there. That's a shocker. Absolute shocker. And, yeah, it's just... Things look a bit distorted when you've got it like that. But if you straighten it back up vertical

**Dave Jones:** and you're looking down and you don't get any depth perception, it's really, you know, it's really quite annoying. Anyway, I think I'm done. But this is where you want to go get them on an angle and go in there and inspect. Do that under the mantis.

**Dave Jones:** Mantis is better in Spectrum Microscope by far. And even though I don't need to, I'll just show you that if you are unsure about joints in there, you can just go in and, like, systematically reheat like that. And you see, that solder's actually flowing

**Dave Jones:** further up the leg there. They're already soldered, but, you know, if you just wanted to touch them up, that's how you do it. And, oh, one last inductor there because that is not... going to work. Uh, my, um, the DC-to-DC converter's not going to work

**Dave Jones:** without that inductor. Okay, with these USB connectors, I would actually recommend just putting down some flux down on there because they can be a bit of a pain. In fact, probably even whack some on the pins if you're feeling lucky. It's going to be really hard to get the iron into these suckers.

**Dave Jones:** So, anyway, I'm going to... That doesn't protrude through the board. So, we can tack down one of those pins to keep it in place. So, there we go. That looks right. There we go. I think she... I think she flowed. I think she flowed.

**Dave Jones:** Yep, yep, she's holding in place. There you go. There we go. Now, yes, they are supposed to be shorted. Beautiful. You'll notice that there's no solder mask down between the pins. There's no solder mask down between those pins either. So, you really want to be careful about bridging on these pins.

**Dave Jones:** It's really tricky to get in there to the extra pin. You almost have to heat up the one next to it. I could have got my smaller conical tip, but, nah, she'll be right. Bobby Dazzler, look at that. Oh, you could say that pin over there hasn't wetted, actually.

**Dave Jones:** Now, it has. Ah, thing of beauty is a joy forever. Now, the through-hole stuff. And, you'll see that the solder will wick down in there like that. And, it won't always go all the way through. This one's actually going to require a fair bit of heat.

**Dave Jones:** Now, you'll see the solder wick down through the board once it's gone through. There we go. It's gone a bit concave-y. So, has it actually flown through to the other side? Oh. Almost, almost. Don't actually need to put any more on there. That's more than taken up.

**Dave Jones:** But, that's now, yeah, like, more than enough. And, same with those ones. They'll actually flow down into there. That looks a bit messy, but, should have actually flown a good lot of the way down in there. Yep. So, I'll put the tactile switch and a little pin header on there.

**Dave Jones:** One tip with these, you see how these aren't, really, as tight as a nun's nasty. They're loosey-goosey in there. And, you can solder those at the wrong angle. So, just a little tip in there. Actually, go and get a dip chip and actually insert it into there.

**Dave Jones:** And, that will physically hold them in place, perfectly lined up while you solder them. Then, you just lift the chip back out. And, just for a bit of street cred, there you go. A UA-709 Texas Instruments 37th Week 1978. I just, little, like, that was just one of the first ones

**Dave Jones:** that came off my, um, sponge. My, you know, I, like, I obviously salvaged, I de-soldered this when I was a kid. I would have de-soldered this. Um, anyway, still comes in handy. Just another tip. When you're laying out boards like this, look at the size of these annular rings,

**Dave Jones:** i.e. how much exposed ring there is on each pad. It's naff all. Like, why would you do that? This is not a high-density board. There's absolutely no reason to do that whatsoever. The thing about a small annulus ring like that is it's hard, then, to get your sold...

**Dave Jones:** your eye... your tip, sorry, your tip onto there to make contact with the pad so that you can then feed the solder onto it because you put your soldering iron on there first, you heat up your annulus ring and your, um, component leg

**Dave Jones:** and then you solder. That looks... Oh, no, that... Is that a trick? No. Yeah, that's a... That's a shadow trick. It looks like there's a hole there, but I don't think there is. I think that's a lightened shadow. So, yes, bigger annular rings, please.

**Dave Jones:** There's absolutely no reason to go tight-ass. I hate a small ring. And there we go. It's like a bought one. Just cleaned it up with some flux remover. It's still got some, uh, residue and stuff left on there. So what we want to do now is, um,

**Dave Jones:** before we power it up, just, you know, buzz a few things out to make sure, like, things like the power, rail and stuff like that's not shorted. So, let's do that. So, first thing, C6... Uh, sorry, I don't have the, uh, schematic here to show you.

**Dave Jones:** But this one here, this is actually the input. You can see it coming over there like that. So, this is actually the input cap. Make sure it's not shorted. And it's not. We're not. And a cap on the, uh, 3 and 3.3 volt rail.

**Dave Jones:** C5 here. There you go. That one's not shorted either. So, both of our rails are not shorted. So, winner. You can power that up. Oh, did I say power that up? Well, we can't because we haven't programmed the thing. It's got nothing in it.

**Dave Jones:** So, yeah. Oops. So, we're gonna go ahead and do that. So, we're gonna go ahead and do that. So, we're gonna go ahead and do that. So, we're gonna go ahead and do that. So, we're gonna go ahead and do that. So, we're gonna go ahead and do that.

**Dave Jones:** So, we're gonna go ahead and do that. So, we're gonna go ahead and do that. So, we're gonna go ahead and do that. So, we're gonna go ahead and do that. So, we're gonna go ahead and do that. So, we're gonna go ahead and do that.

**Dave Jones:** So, we're gonna go ahead and do that. So, we're gonna go ahead and do that. So, we're gonna go ahead and do that.
