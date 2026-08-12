---
video_id: tqp0lEfUKTM
title: EEVblog 1641 - How DC Solar Isolators Work (TEARDOWN)
url: https://www.youtube.com/watch?v=tqp0lEfUKTM
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 25, "3": 38, "4": 48, "5": 61, "6": 75, "7": 88, "8": 100, "9": 116, "10": 126, "11": 140, "12": 150, "13": 167, "14": 176, "15": 189, "16": 199, "17": 213, "18": 228, "19": 246, "20": 266, "21": 278, "22": 290, "23": 296, "24": 308, "25": 319, "26": 334, "27": 345, "28": 357, "29": 369, "30": 380, "31": 393, "32": 405, "33": 424, "34": 445, "35": 456, "36": 470, "37": 487, "38": 497, "39": 511, "40": 521, "41": 532, "42": 543, "43": 554, "44": 564, "45": 575, "46": 583, "47": 598, "48": 611, "49": 627, "50": 638, "51": 650, "52": 662, "53": 672, "54": 693, "55": 712, "56": 725, "57": 742, "58": 754, "59": 765, "60": 775, "61": 802, "62": 817, "63": 832, "64": 847, "65": 856, "66": 872}
---

**Dave Jones:** Hi, I thought we'd do a quick teardown of a DC solar isolator switch. This one actually comes from my old installation here. It's a Benedict jobbie an LS25 PFLH4 for those playing along at home.

**Dave Jones:** You can see here it's a four pole single throw and it's got different current ratings for different voltages. So it's designed to safely switch off high voltage DC solar arrays like under load like at many amps.

**Dave Jones:** So yeah, up to 1500 V at 40 amps here depending on the switch configuration because this is a four pole single throw but you can actually wire this in different configurations here.

**Dave Jones:** So this is just the switch unit itself but it does actually come in different like enclosure and knob variants and all sorts of things and different wiring arrangements and all sorts of stuff.

**Dave Jones:** So the link in the data sheet down below which is a very comprehensive in terms of like how you can configure this. Mine was in like a neat like a waterproof weatherproof NEMA case design for outdoor use.

**Dave Jones:** So we've got four screw terminals in here and four out here but you can see that this one actually contains little shorting links on here. So they're actually putting two of them in series.

**Dave Jones:** So it's basically a two pole single throw switch but the reason you put them in series is because then you double your working voltage essentially because you're putting two switches in series.

**Dave Jones:** You're not increasing your current capability. That remains the same but now you've got two switches in series that are breaking. So you've got higher voltage arcing capability. And this hole on top is where the shaft from the big knob goes in.

**Dave Jones:** That's what she said. You can see it's a multi-layered approach here. So it's no coincidence that we got four switches and there's four of these. So I assume that they're going to have like an entire level devoted to each one of these switches.

**Dave Jones:** And you can see that in terms of like the different height arrangements here and how these are physically staggered like that. So, you can see that one lines up with there, that lines up with there like that and so on.

**Dave Jones:** So, yeah, that's how they get the larger voltage isolation in there. Now, there's actually no rating in the data sheet for like how many cycles, full cycles this thing can actually do.

**Dave Jones:** But, you know, it's probably in the order of hundreds. It's not designed for like daily use. You wouldn't be switching this like a massive high voltage load like you know 500 to 1000 volts at you know many amps off and on every day.

**Dave Jones:** You'd probably need a even better solution than this one. But, obviously it's going to be certified and rated to all sorts of industry standards. So, yes, you can actually safely switch your solar panels off under load with one of these things like in the peak middle of the day.

**Dave Jones:** No problems. You just don't want to do it like hundreds of times. But, you know, do it once or twice occasionally when you need to is fine. And that's what these things are designed to do.

**Dave Jones:** So, we've just got some self-tappers in the plastic there. Oops, it's fallen off already. And that's our knot. So, that's just a top part there. And this knob should come out.

**Dave Jones:** That's what she said. And there we go. We just have a big stiff spring arrangement like that in there. And yeah, cuz these are very big clunky like they they really require a lot of force to actually turn these things.

**Dave Jones:** So, yeah, so that's just how they do that in the top. But, we're really interested in the layered contacts and how they do the arcing prevention and stuff. So, this this will lift off here and that.

**Dave Jones:** Yeah, so that's all just the top switching mechanism like that. Then the bottom one just has two self-tapping screws. There's a DIN rail arrangement here. So, that's just a little clip for the DIN rail.

**Dave Jones:** So, we can take off our first level here. So, there we go. That's interesting already just in this plastic part here even though there's no electrical contacts in this part, they've got all little plasticky things shooting up and these walls separating in there.

**Dave Jones:** I don't think they're just for uh strength. So, these are probably designed to prevent like flashover from like one circuit to the other in here even like if it can get up here through the plastic even if it manages, you know, huge big plasma arc up here through the plastic, it's it's still got all these little traps in here, I think.

**Dave Jones:** I I don't think that's for show. I think that's uh that's part of the game. So, it looks like we're going to have to slice through the label on the various levels there and that's our first that's our first one.

**Dave Jones:** There you go. Aha, a similar sort of thing happening here. Wow. So, there you have it. That's inside one layer or one switch contact uh inside of this thing.

**Dave Jones:** And you can see how it's all horizontally arranged. Now, I thought it would have gone out uh from there to there, but it doesn't. It goes from this one over to that one.

**Dave Jones:** So, yeah, that's interesting. Um you have to know how these things are uh wired up in like in designed internally. So, uh yeah, I was wrong. I thought it would have gone straight over, but no.

**Dave Jones:** It goes diagonally opposite like that and the different layers will have different arrangements. So, how this works is obviously you've got a one contact here, one contact here and hopefully you can see down in there.

**Dave Jones:** You can see that it's actually a dual wipe uh contact there and you basically just uh swing this around like this. So, at the moment it's off because uh the metal is over here and it's complete the path is completely broken.

**Dave Jones:** So, you'd switch it around 90° clunk and then those metal contacts just make you know, they're just wiping contacts over here. And you've got to remember these are not particularly high current.

**Dave Jones:** I mean, we're not talking hundreds of amps here, only talking like amps, really. You know, sub 10 amp uh kind of stuff, even though they're rated for like 25 amps uh really, but you know, in practice, you're going to actually use them at less than that.

**Dave Jones:** The whole idea of these is for high voltage arc discharging. And you can see how this uh arc extinguishing happens here. It's all in the physical design of the plastic around here.

**Dave Jones:** And you can see these are what's called arc shoots here, right? Cuz they're like little shoots shooting off like this. But you've also got arc barriers here as well, like this.

**Dave Jones:** And you'll notice that the top of this has this ring going all the way around like that. And that is to contain any plasma arcs, right? So, that will go on top of here, so the plasma really has nowhere else to go but sort of through this open gap here.

**Dave Jones:** So, when you switch this thing off, okay, the uh the arc wants to the high voltage, it can arc over, and it wants to maintain, so it's going to you know, generate this high voltage uh plasma field.

**Dave Jones:** Sorry, I'm not a physicist if I'm not explaining, you know, the plasma physics of it correctly. Um but yeah, it basically has this open area. It goes, "Oh, I can go through here." And then it goes, "Oh, I can go down this path and this one and this one and this one." And it just slowly dissipates out into the nether regions out here, right?

**Dave Jones:** So, that's how uh the plasma escapes like that, and it's confined within that switch mechanism by that plastic around there. But yeah, these little arc shoots, and that's how they get the high voltage isolation in in combination with arc barriers, which uh sort of like channel the flow of any potential plasma arcing.

**Dave Jones:** Cool, huh? So, if we get that off, and you can see the same thing is just going to be in on different levels, but obviously like this one probably goes over to this one here, and that one goes over there, etc.

**Dave Jones:** Uh like that. So, let me get that out, cuz you have to remember that uh DC switches are different to AC. You remember like AC actually switches its voltage every single cycle.

**Dave Jones:** So, you naturally going to get like a almost self-discharging type thing on switching high voltage AC currents. But high voltage DC, it's just it's just one DC path and it doesn't change value.

**Dave Jones:** So, it wants to sort of like it continue the current wants to continue and it'll find any gap. Anyway, there's one of the copper shorting links there so we can take that off.

**Dave Jones:** So, this is just going to be multiple layers of the same thing and that's how they Yeah, that's how they design them. There you go. And you can see inside here once again, we've got an arc barrier like this, but just in case it like sneaks through the gaps.

**Dave Jones:** You remember cuz there's no lip on these, right? So, it can it can go through the gap in these. It depends on how, you know, the uh pressure of the plastic between them.

**Dave Jones:** But technically, like there's going to be a, you know, little microns level gaps between here and the other when you mate two plastic surfaces together cuz there's no like lip in there.

**Dave Jones:** I guess if you really designed even a higher voltage one again, you would put you would like mold in lips into here so that like they overlap. So, but anyway, these are just pressed together.

**Dave Jones:** So, we've got an arc barrier here, but just in case it sneaks through the barrier between the two pressed bits of plastic, we've got more arc shoots out here.

**Dave Jones:** So, it just slowly dissipates those out. Cool, huh? Even though there's no electrical contacts in there, the plasma just wants to go everywhere. The arcs just want to go everywhere.

**Dave Jones:** So, yeah, it's designed to prevent that. And then you just open this out like Oh, there we go. We got some contacts. You just open this out like a book like this.

**Dave Jones:** There we go. There we go. Anyway, there's our copper. There's our internal copper. There you go. We did want to see that copper. So, as I said, that's like a dual wipe arrangement there.

**Dave Jones:** And you know, that that's plenty for the 25 amp current capability in here. So, these are just wipe contacts like that. And you know, nothing fancy pantsy about that at all.

**Dave Jones:** It's just yeah, a dual wipe arrangement like that. I don't know, you might be able to get like special materials, but just plain old copper in there. But they do say something about the materials in the data sheet.

**Dave Jones:** They don't say what though. So, I'm not sure what sort of you know, alloy that is. But anyway, yeah, there's nothing fancy there. It's all about the arc paths and these little arc shoots and arc barriers.

**Dave Jones:** Yeah, there you go. It's all just coming apart like that. Now, this has Look at this. This has something in there. Did this get Is that that like arc charring or something?

**Dave Jones:** Or is that some water ingress? Or some moisture ingress into there? I'm not sure what's going on there. And you can see some blackness on here as well. So, I'm not sure what that is.

**Dave Jones:** Don't know if that's like a black permanent marker, some sort of factory thing, or whether or not that's actually had some charring or whatnot in it. And it's just coated itself on the plastic.

**Dave Jones:** But yeah, that does not look normal. Yeah, that doesn't look pretty, does it? So, yeah, this is not a failed DC isolator. But you know, it would have been used a couple of times.

**Dave Jones:** But yeah, maybe that's the uh that's the end result of using these things. Um something's gone wrong there. That could be some sort of like metal vaporization perhaps coming from the contacts and then and coats itself on the uh plastic.

**Dave Jones:** Uh yeah, doesn't doesn't look like it, but I don't know. I'm not a no material scientist. Now, of course, I'd love to show you uh operation and try and get uh like a demonstration of like the plasma arc in and the uh like how the little shoots like sort of extinguish that, but I don't really have that sort of energy capability here in the uh lab.

**Dave Jones:** Sure, I've got like 5 kV uh like high-voltage generators and stuff, but um yeah, it's just not going to do the business cuz I know they they only arc over small paths.

**Dave Jones:** So, it's it's not really going to happen, but I I can give it a go, but yeah, I don't think we're going to be able to see anything. Okay, I've got my Uni-T uh 5,000-V generator here, so let's generate 5,000 V on this sucker and see if we can get something to happen.

**Dave Jones:** I wouldn't be surprised if nothing happens at all because like the arc paths are quite large. Now, I can't uh because this is not a high-energy uh generator, I can't like a short it out and then switch it back on.

**Dave Jones:** I can't do that. So, I've got to only apply it when it's open, but here we go. Uh 5,000 V. And yep, zippity-doo-dah, as expected. But, I can try and rotate it.

**Dave Jones:** And for those who want to know, it's measuring 770 GΩ there. GΩ. Anyway, uh yeah, okay, let's see if I can get in here with the screwdriver. Move it.

**Dave Jones:** Does Are we going to do anything? Uh yeah, we got some got some arcing on the contacts, but Whoop. Yep, it just switched off. Hard to get my camera in there, but yeah, you can just see some arcing Turn the lights down here, and we're not going to see any The only thing we're going to really see is arcing between the contacts.

**Dave Jones:** Yeah, yeah. Yeah, you can see that. Yeah, so nothing that exciting. Sorry, I can't get the arc shoots working. I'll tell you what though, I wish this was smell-o-vision because I can smell the ozone generated from the like the arc in there.

**Dave Jones:** But anyway, I hope you found that really interesting in that basically it's all about the physical design of these arc shoots and arc barriers and arc traps to actually trap the arc in which is like a high energy like a plasma essentially.

**Dave Jones:** And yeah, it just contains that and directs it and then extinguishes it cuz it's got these long paths that it has to go down so it dissipates all the energy in the arcs and hopefully it contains it within the switch.

**Dave Jones:** But as I said, yeah, a lot of these things have been recalled over the years here in Australia. Let us know if you're aware of recalls in other countries.

**Dave Jones:** I don't I don't think this one is subject to the recall by the way. So this is one of the winner winner chicken dinners. So yeah, interesting, huh? So if you like that video, please give it a big thumbs up and as always you can discuss down below and over on the EVblog forum.

**Dave Jones:** I think that's really cool. And don't forget to check out the EVblog.store for all my merch. Catch you next time.
