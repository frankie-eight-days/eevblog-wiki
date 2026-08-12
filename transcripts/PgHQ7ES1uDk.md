---
video_id: PgHQ7ES1uDk
title: EEVblog 1512 - Why Bypass Your PCB Like THIS?
url: https://www.youtube.com/watch?v=PgHQ7ES1uDk
source: youtube-asr
timestamps: {"0": 1, "1": 10, "2": 19, "3": 29, "4": 37, "5": 45, "6": 70, "7": 83, "8": 92, "9": 102, "10": 114, "11": 125, "12": 138, "13": 148, "14": 161, "15": 174, "16": 188, "17": 204, "18": 227, "19": 236, "20": 249, "21": 260, "22": 270, "23": 281, "24": 294, "25": 302, "26": 310, "27": 323, "28": 335, "29": 348, "30": 358, "31": 368, "32": 378, "33": 394, "34": 412, "35": 424, "36": 450, "37": 458, "38": 468, "39": 480, "40": 491, "41": 507, "42": 514, "43": 524, "44": 535, "45": 543, "46": 556, "47": 564, "48": 580, "49": 590, "50": 602, "51": 612, "52": 623, "53": 636, "54": 646, "55": 655, "56": 668, "57": 678, "58": 686, "59": 698, "60": 707, "61": 721, "62": 731, "63": 742, "64": 750, "65": 765, "66": 774, "67": 794, "68": 803, "69": 813, "70": 825, "71": 835, "72": 848, "73": 861, "74": 882, "75": 894, "76": 904, "77": 917, "78": 931, "79": 949, "80": 963, "81": 975, "82": 993, "83": 1000, "84": 1018, "85": 1034, "86": 1051, "87": 1064, "88": 1078, "89": 1104, "90": 1114, "91": 1130}
---

**Dave Jones:** Hi, I thought I'd do a video answering a Twitter question even though I've already answered it on Twitter. I thought it might be of interest to others and I wanted to test out my new rig here.

**Dave Jones:** It's not fully finished yet, but I thought I'd do a video trying it. I've got my pen tablet here hooked up to my Blackmagic ATEM and I'm doing this all sitting with this backdrop.

**Dave Jones:** Let me know what you think instead of over at my regular desktop. Leave comments down below what you think of this form factor. It's not polished yet, but we'll get around to it.

**Dave Jones:** Anyway, let's see what we've got here. Um this question comes from um Ian Hanshin. Follow me on Twitter by the way. Ask me questions on there all day every day.

**Dave Jones:** It's all I do, answering questions on Twitter. He's posted this and I thought this was really interesting. It says every once in a while I see a board like this.

**Dave Jones:** I figure maybe it's for some kind of noise or decoupling purpose or something, but perhaps someone could tell me if this has a name and more about it. Well, I don't know about a name for it, but he's talking about what he's talking about here is the bypass caps here and how they're all like hey because there's a lot of them and they're all neatly surrounding the chips as you can see

**Dave Jones:** here and all the passive just the sheer number of passives and how they've laid out in sort of a grid arrangement. So, let's take a look here. So, I go over to my Drawboard PDF program for those who don't know.

**Dave Jones:** It's an Aussie program and I can just draw on this. So, let's take a look at what's actually going on here. Okay, well, first of all, what is this board?

**Dave Jones:** It dates from you can see it down here. Haven't figured out how to pan with this thing yet. It's from 2004. So, this would have been designed early 2000.

**Dave Jones:** So, we're talking at least 20 years ago. It's a bit younger than I expected. I thought this was like late '80s or something. But anyway, what this is is it's a VGA card apparently with some video capture as well.

**Dave Jones:** So, presumably this is your VGA output here and these are video capture. I don't know what kind of video inputs. If you know, leave it in the comments down below.

**Dave Jones:** I'll put a link down to a page which has info on this and it's a super Savage IXC and it's an 86C 584. As you can see, manufactured 26 week 02 here.

**Dave Jones:** So, it's a VGA chipset and obviously the the Altera Cyclone up here is probably doing like the video Well, no, this is probably the video capture. Ah, yeah, it's a Philips.

**Dave Jones:** I can see the Philips symbol. I can't make out the symbol. So, this is probably the This is This would be the capture memory for the video input. Anyway, this is Anyway, let's not worry about the details of the card.

**Dave Jones:** Why does the layout look like this? Why are all these Look, look at all these bypass caps. Why are they all surrounding the chip like this and why are Why is everything like in rows and columns like this?

**Dave Jones:** It's all beautifully, neatly laid out. Why is this case? Well, there's several reasons for this. The first of all is this This appears to be a single-sided load. There are load.

**Dave Jones:** There are a couple of components on the back, but they're not populated. He didn't post a photo, but I found another photo online and they're not populated. So, you got to think of the mindset of the designer of this board, not only the PCB designer, but also the actual designer of the circuitry.

**Dave Jones:** Right, typically there's multiple engineers on a design like this, especially one of this complexity and there'll be, you know, software and firmware people and there'll be, you know, production people, probably not people, but, you know, at least a production person involved and there'll be a PCB designer usually and then there'll be the designer of the actual circuit who'll be doing the schematic and, you know, everything else.

**Dave Jones:** So, multiple engineers. So, you've got to put yourself in the mindset. Now, when they're manufacturing this, they probably wanted to lower the cost, so they went for a single-sided load.

**Dave Jones:** So, all the components are on one side. And the problem is, when you've got a uh BGA uh package like this, and you've only got components on one side, you've got all your little individual pins in there, okay?

**Dave Jones:** Please excuse the crudity of the model. Didn't have time to build it to scale or to paint it. You can see how my tablet is actually uh touch-sensitive. So, get different sized pins, bloody BGA chips.

**Dave Jones:** Anyway, right? So, you've got all your pins under your BGA uh chip like that. Now, of course, a chip of this complexity will have multiple power pins and multiple ground pins.

**Dave Jones:** And the multiple power pins, they could be for different voltage cores uh inside. Though, this one, I haven't looked at the data sheet. Can't seem to find the data sheet readily for it, but let's just assume it's just a single uh rail, okay?

**Dave Jones:** It's not that uh complex, but you've got multiple power pins. And ideally, you would have a bypass, or the recommendation from the manufacturer will be a bypass uh capacitor per pin.

**Dave Jones:** Or, even if it's not recommended in the data sheet, that will often be the mindset of uh designers. It's just sort of like the done thing. It's the de facto standard.

**Dave Jones:** Oh, yeah, if you have a power pin, you have a bypass pin with it. You don't always need it. It's kind of like one of those belt and braces things.

**Dave Jones:** You're just like, nobody ever got fired for putting a bypass cap on a pin. Unless you're pinching pennies and you're doing months in. I have to link up my video uh a months in and reducing uh capacitors in the circuit until they stop working.

**Dave Jones:** It's very interesting stuff. The designer of this thing probably just went, well, I like however many uh bypass uh caps are here, probably is how many power pins it actually had.

**Dave Jones:** Some of them aren't uh bypass caps, but all of them are They're probably all like 100N. They don't look any And remember, we're talking a long time ago, so none of this, you know, 10 microfarad bypass ceramic uh capacitor rubbish, right?

**Dave Jones:** Back then, you know, one mic was like big. So, yeah, so there's no huge value. So, if they want to bulk a capacitance, that's why they're using these tantalums around here.

**Dave Jones:** So, that's the first reason what's happened here is that the designer has simply used one bypass capacitor per pin. And then they threw the schematic over the cubicle wall to the PCB designer.

**Dave Jones:** And the PCB designer has got the schematic, they import it, and and then, you know, they've got all their parts and they're laying it in they're starting to lay out the board and they go, "Well, I've got to put all the bypass caps.

**Dave Jones:** And well, somebody told me from production that we can only afford a single-sided load, so I can't put the bypass capacitors where they should be, which would actually be like on the bottom here." So, you would actually have like, you know, a bypass cap right next to the pin.

**Dave Jones:** And then you'd have the via. Typically not a via in pad, but you know, it'll be very close to it. And this is why flip over any modern board, and if you see a bunch of bypass caps, they're you almost certainly on the back of an FPGA or a, you know, a BGA micro.

**Dave Jones:** My pen's died. Oh, goodness. So, yeah, usually you add bypass caps on the bottom of the pins. That's as close to the pin as possible. You minimize the trace inductance and everything else.

**Dave Jones:** So, in this particular case, they there was no option, right? The bypass pins caps had to go around outside the chip like this. And of course, you've got some like excess space in here, but this is probably, once again, this could be a production requirement in that the pick and place machines that using at the particular assembly house, for example, might have had requirements that, you know, "Hey, we don't want caps

**Dave Jones:** close to the chip." Or we don't want This is why the footprints are actually quite large as well. If you have a look at the size of the footprints, right?

**Dave Jones:** This is Jeez, you can drive a truck through there, right? So, there are once again, this could come from an in-house requirement, for example, where they have an approved footprint.

**Dave Jones:** And this is a thing in big companies, you will have a certain, you know, if you've got an 0603 or an 0805 cap, for example, you will have an approved footprint for a specific contract manufacturer for your board, for example.

**Dave Jones:** It'll be all set up and done, and then they might have, you know, they just went, "Well, I've got to use that, and I've got to have this spacing requirement as well." So, that could have been driven by the manufacturer.

**Dave Jones:** Although, this looks quite large and spaced out. So, I would say that probably, you know, good bet is that the PCB designer just, well, they had room, and they like to lay it, you know, and they didn't want the silk screens overlapping and stuff like that, you know, cuz that's sort of like ugly.

**Dave Jones:** They don't want them overlapping, and so they spaced them out nicely around the chip like this. They could have put them a bit closer, but as I said, there might have been requirements for that.

**Dave Jones:** So, you simply place them, all your bypass caps around the outside, and you want to have them all in line, because you're a, you know, you take pride in your PCB layout.

**Dave Jones:** So, you want to have them, you know, in nice vertical and horizontal arrangements. And then, if we zoom in there, you can actually see they've got the vias there and there, like either side there.

**Dave Jones:** Like, well, that one, oh, yeah, that one's there. I don't know why they didn't put it there. Oh, jeez, you know, they went to all this effort to make it aesthetically pleasing, and they put the put the via there.

**Dave Jones:** I would have been disappointed in myself if I did that. You know, symmetry, come on. Anyway, so these these caps are obviously being via stitched directly down to the ground and power layers.

**Dave Jones:** Probably just one power layer on here. It's probably all just 5-V logic or something like that back then. Or could there could be an extra 3.3-V layer in there, but who knows, right?

**Dave Jones:** Anyway, so the other reason for the amount of the sheer amount of bypass caps, like all in here like this, like, you know, there's just tons of them like this, is because there was no pushback from the PCB designer.

**Dave Jones:** The PCB designer, if they knew, you know, designer layout, which a PCB designer often does, although not always. I've worked with top-notch PCB designers who come from a drafting background.

**Dave Jones:** They've got no electronics knowledge at all, but you pick up, you know, you do pick up stuff over the years. This is back when, you know, things weren't as advanced as they are now, and you know, you got to understand signal integrity and all sorts of stuff, right?

**Dave Jones:** It's not that an engineer can't do a PCB layout. It's just it helps if you have. So, there was probably no pushback from the PCB designer going, "Hey, look, come on.

**Dave Jones:** You're making me do a single-sided load. We don't need 20 bypass caps. You don't need a power a bypass cap per pin. It's just going to be sufficient to rely on some bulk decoupling.

**Dave Jones:** I, you know, like you might put one bulk decoupling cap here, just, you know, like surround it, cuz this is it was one just big power plane. Like, you're not optimizing your inductance, you know, and getting close to the power pins anyway.

**Dave Jones:** So, you know, you could have said, 'Oh, you know, just a couple here, a couple here, and a couple here, just to, you know, make it nice and dandy, right?' And you don't need a cap per pin.

**Dave Jones:** So, there was probably no pushback from the PCB designer there. Or, but this should have been picked up by the actual designer. They should have, you know, they should know, right?

**Dave Jones:** If you're designing this, you should have a like a thought in mind of, you know, layout. You should be thinking about layout when you're actually designing this thing. If they knew it was single-sided load, or that was their intention.

**Dave Jones:** Obviously, clearly, they wanted this to be single-sided load. Or, definitely, you know, you would have put the bypass caps on the bottom of the chip down here. There's no absolutely no doubt about that.

**Dave Jones:** You would have done that. So, obviously, they were constrained with that. So, you would have sort of like gone back to the drawing board a bit, and you you know, rethought your bypassing strategy.

**Dave Jones:** And the same thing's happened over here on like these these chips over here, right? Some of these like there's a whole row of bypass caps there, right? There's a whole bunch of them.

**Dave Jones:** Not all of them might be bypass caps, but a good lot of them will be. And yeah, it's And there's another one there. That one's got two vias actually instead of one.

**Dave Jones:** They're trying to lower their inductance there by using the two vias, but yeah, once again, they probably had like a bypass cap per pin, but because this is a quad flat pack like this, you can actually be near the pins like this.

**Dave Jones:** So, you know, there's a reason to do that. But we've got another BGA chip up here, and probably, you know, look, they've got some larger ones here. Are these like 1206s or something?

**Dave Jones:** Actually, they look to be output from the There's a regulator there. Yeah, it's a 3.3. I don't know. We can't see that. But yeah, you're going to have a similar sort of problem around that BGA.

**Dave Jones:** And you know, these bypass caps here are probably from the Altera Cyclone. They've got a couple of more caps over here, but once again, that is a quad flat pack.

**Dave Jones:** But why have we got all these nice grid arrangements like this? Well, this could be done by an old-time PCB designer who was, you know, old school from, you know, '70s, '80s, who's used to laying stuff out in grids.

**Dave Jones:** That's if just look at any old-school board. In fact, I've probably got one. Just so happened to have an old-school board here. And this is how it was done back in the day.

**Dave Jones:** You would all the chips would be in like row arrangements like this, and they're all the correct orientation so that the auto routing of these boards, or even if you manually routed it, all of the traces on the top, for example, would go in one direction, and all the traces on the bottom would go in the other direction.

**Dave Jones:** I don't know. No, you might not be able to see through this solder mask, but I've shown this in previous videos where, yeah, all all the traces will go horizontal here, and all the traces will go vertical here.

**Dave Jones:** And that just makes laying out the board easier, and I'd say that somebody has, you know, gone in with a similar mentality here of just everything needs to be in nice rows.

**Dave Jones:** And also, PCB designers, they love symmetry, and they love just the aesthetics of boards. And I reckon the piece I would have been quite proud of this board, right?

**Dave Jones:** It did like apart from like it just from a an aesthetic point of view, having all the caps in nice rows and columns and rows like this. It's just It's beautiful.

**Dave Jones:** So, yeah, there's quite a few reasons there. One, this is a single-sided load, so that would have determined various things. B, there was no pushback from the PCB designer to go, "Hey, look, come on, this is a bit silly.

**Dave Jones:** We don't need one bypass cap per pin. We can get away with a lot less, right? This is just getting nuts." So, three, they might have had requirements for spacing requirements and things like that from the assembly house.

**Dave Jones:** And then they might have had standard footprints company footprint footprints to work from, company approved spacings and DRC requirements for the board, and you know, all sorts of like older school requirements that might have been carried on from like a decade earlier, but they still use them today, and they might have the PCB designer might have still been working around those DRC constraints and stuff like that.

**Dave Jones:** And then, well, if you told, "I've got to lay out this board, and here's all these caps." Yeah, why not? Just, you know, make them in nice neat rows and columns like this.

**Dave Jones:** And it just That's why it looks like this. So, yeah, there are like, you know, half a dozen sort of reasons that go into something like this, good or bad.

**Dave Jones:** As I said, like you really you don't need this many bypass caps. You don't In this particular case, having a bypass cap per pin just because you defined it so on the schematic, and that was, you know, like the done thing.

**Dave Jones:** It's just No. No, somebody should could you know, stopped and thought about uh this board and gone, "Yeah, nah. Um we can get away with a lot less bypass caps than all these." And look, they didn't even have room for the silkscreen designators, either.

**Dave Jones:** You'll you'll notice. Like like they put U17 here, right? There's a little fiducial. Um actually, they've done that fiducial That fiducial's done on the silkscreen layer. You don't do fiducials on your silkscreen layer because you can get offsets on your uh on your silk screen compared to your copper layers.

**Dave Jones:** And really, the alignment of a a fiducial um mark is A fiducial mark is a reference mark used by the camera for the pick-and-place um machine, so that it knows where to accurately place uh the components.

**Dave Jones:** And you don't put that on your silkscreen layer. That's a golden rule. You put it on your copper layer, um so that uh yeah, it's more accurate. So then any um offset errors on your silk screen and your copper don't matter.

**Dave Jones:** Oh yeah, there we go. That's I totally missed that 3.3-V uh rail there. So yeah, and then there's another adjustable rail there. So there's you know, there's probably some like um internal you know, uh sort of like ground uh in there, probably just for that one chip, and the bypass caps do that.

**Dave Jones:** And you just don't need all those. It's just It's it's it's just silly stuff. Um just a couple of bulk decoupling caps would have been fine for something like this.

**Dave Jones:** And this is not, you know, really huge modern like you know, high-performance like you used to uh these days. And really, the only way you can actually get better performance is, as I said, put them on the bottom of the uh chip under there, right near the pin, and then have a via going uh straight up or vias going straight up to uh the balls.

**Dave Jones:** Um and then, you know, you're actually bypassing individual uh pins. And then, you know, you'll at least get some benefit there. Otherwise, from an inductive point of view, you're talking about like one big solid, you know, 3.3-V rail, and ground will go over the whole board, of course.

**Dave Jones:** I don't think you'd have split uh planes on something like maybe up here. Like if you got like if this is like is is an analog section or something like something like that if that's your analog section with your video ends or whatnot, you know, you might have separate split grounds up there or something like that.

**Dave Jones:** But yeah, but generally speaking, yeah, like just couple of bypass caps would have been fine on something like that, you know, just a you know, one one over on the far side here one here just a bulk.

**Dave Jones:** Uh you can get away with bulk cuz there's a lot of debate and if you go and actually use the simulation tools to actually try and simulate bypassing which is really advanced really expensive software tools, you can actually do it.

**Dave Jones:** But there's specialized signal analysis tools to do this and yeah, you can often find that well, just one bulk decoupling cap is going to work. Something like that unless you're talking about real like modern complex FPGAs with multiple things and they have like, you know, 50-page documents of just how to power up and bypass and sequence the power rails on a modern FPGA or a modern processor or something

**Dave Jones:** like that. It's really strict. But yeah, maybe this VGA chip, I don't you know, it's it's kind of like old school compared to modern stuff and you could have just got away with a couple of bypass caps.

**Dave Jones:** But anyway, there's some real possible reasons why this thing looks the way it does. So I thought that was an interesting question. If you got other you know, theories why it looks the way it does, leave them in the comments down below and let me know, please, in the comments how you like this new setup.

**Dave Jones:** It's not polished yet, but it's good enough for Australia. Catch you next time.
