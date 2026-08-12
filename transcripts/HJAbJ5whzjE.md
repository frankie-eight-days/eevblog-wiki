---
video_id: HJAbJ5whzjE
title: EEVblog 1423 - Flaming Magic Repair Smoke!
url: https://www.youtube.com/watch?v=HJAbJ5whzjE
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 23, "3": 37, "4": 47, "5": 62, "6": 73, "7": 88, "8": 97, "9": 108, "10": 123, "11": 133, "12": 146, "13": 158, "14": 168, "15": 181, "16": 194, "17": 201, "18": 215, "19": 225, "20": 236, "21": 249, "22": 261, "23": 272, "24": 286, "25": 304, "26": 314, "27": 326, "28": 342, "29": 354, "30": 367, "31": 377, "32": 396, "33": 408, "34": 422, "35": 432, "36": 457, "37": 468, "38": 484, "39": 498, "40": 516, "41": 534, "42": 544, "43": 559, "44": 568, "45": 586, "46": 599, "47": 614, "48": 630, "49": 649, "50": 661, "51": 678, "52": 690, "53": 704, "54": 718, "55": 730, "56": 742, "57": 756, "58": 767, "59": 784, "60": 797, "61": 809, "62": 828, "63": 838, "64": 850, "65": 862, "66": 876, "67": 893, "68": 911, "69": 928, "70": 941, "71": 951, "72": 963, "73": 994, "74": 1008, "75": 1023, "76": 1033, "77": 1050, "78": 1065, "79": 1076, "80": 1090, "81": 1101, "82": 1122, "83": 1141, "84": 1153, "85": 1172, "86": 1184, "87": 1191, "88": 1215, "89": 1226, "90": 1245, "91": 1258, "92": 1278, "93": 1290, "94": 1303, "95": 1323, "96": 1336, "97": 1347, "98": 1355, "99": 1363, "100": 1383, "101": 1395, "102": 1406, "103": 1418, "104": 1427, "105": 1438, "106": 1447, "107": 1472, "108": 1481, "109": 1494, "110": 1501, "111": 1512, "112": 1523, "113": 1541, "114": 1550, "115": 1558, "116": 1571, "117": 1581, "118": 1592}
---

**Dave Jones:** Hi, it's repair time. If you follow me on EV blog two, and you should, you would have noticed that I had a problem with one of my oyster lights in my kitchen.

**Dave Jones:** And well, it was sending alien signals or something. It looked like it looks like an alien spaceship and it was flashing a weird code. So anyway, I ripped it out.

**Dave Jones:** I've brought it into the lab here and I've hooked it up and that's what it's doing. Let me turn the lights off. So I've just got it hooked up to a LED string which I got out of ripped out of an old LCD dumpster TV.

**Dave Jones:** It's coming in very handy. I've used it for quite a few videos actually. The LEDs have got like 5-volts drop per LED. They're actually quite high and yeah, I do like they're in string configuration.

**Dave Jones:** I use them for all sorts of things. I've got two strings of those. Yeah, does anyone know their Morse code? What's that flashing? Yeah, it's hiccuping. So anyway, that is obviously hiccuping as they call it.

**Dave Jones:** That's one of the names for the fault. I don't know if you call it something else, but yeah, in the industry it's often called hiccuping and the mains power supply is hiccuping.

**Dave Jones:** Hiccup. It just can't start up. It's trying to start up the mains side of it, but the main switch inside, but it just can't do it. So it keeps restarting retrying retrying retrying and no, it just comes a gutter every time.

**Dave Jones:** So anyway, let's take this thing apart and see if we can find the culprit. All right, we're at the Tektronix microscope, but I got something a bit new for you today.

**Dave Jones:** I've now integrated my NI National Instruments virtual bench scope. It's just sitting right down here next to me and I've got my probes. I can have my oscilloscope probes.

**Dave Jones:** I can have power supply, function generator, logic analyzer, digital IO, everything integrated into my video capture system, which not only I can record with, but I can also stream as well.

**Dave Jones:** So, you'll see in my straight-ahead camera, I've also got my Tagarno microscope. Here it is, right under me. And there will be a B cam, but it's not hooked up at the moment.

**Dave Jones:** And also, there's my National Instruments screen. But one of the cool things I can do now is I've set it up so that I can now overlay Ta-da! This I can overlay the multimeter here.

**Dave Jones:** So, here's Here's the multimeter. Winner. And all the power supplies as well. And there's some digital IO in there as well. And I can stream that. And yeah, that's really cool, huh?

**Dave Jones:** So, anyway, let's get to it. Let's have a look at Sorry. Let's have a look at this. Okay, so let's have a look at the driver here. It's a Lucci thing.

**Dave Jones:** Model number for those playing along at home, it's a it's a dimmable jobbie. And it's a a 2 W LED that's individual LED. It's actually up up to 20 or 22 W output.

**Dave Jones:** So, it's actually rated for up to 80°. But yeah, anyway, let's have a look at what's failed here. Here's the output section. Now, I wouldn't expect There's no bulges in those caps, of course.

**Dave Jones:** The first thing you look for is bulges in the caps. But oh, I forgot to tell you that this actually comes with a heat sink over here. And it's just screwed in there.

**Dave Jones:** And I've taken that out because we want to see some stuff under there. There's a couple of extra caps. And anytime you see caps near or under heat sinks like this, yeah, you want to be suspicious of those puppies.

**Dave Jones:** So, anyway, I've taken that off. So, yeah, it's just a plastic package. So, that's just like they didn't even bother with the heat sink compound. So, they just bit how you doing?

**Dave Jones:** They just slapped it on there. But you know, better than nothing, I guess. These are a Shai caps on the output. Now, it's not going to be the output A because those caps looking good Nick and B there's multiple ones in parallel.

**Dave Jones:** So, like you know, I wouldn't be concerned with that and that's not going to cause uh the power supply to hiccup. Now, is this a secondary regulator? Yes, it is.

**Dave Jones:** This is a secondary regulator, okay? Cuz here's the primary secondary split. So, this is all the secondary side. This is the mains input over here. Like this and so these are my initial thoughts.

**Dave Jones:** I I'm pretty sure it's not going to be this secondary side. I mean, you can go in there obviously you do a visual on the uh caps but they these have got the vents on the top.

**Dave Jones:** I can't see any bulges whatsoever. They'd be in parallel if you actually follow the money on there. Yeah, parallel parallel parallel um and another one there. Is it? Don't know if there's four in parallel or what not.

**Dave Jones:** No, there's another one that's not in parallel. So, we've got three in parallel. So, when you got three caps in parallel like that, it like it's not going to be the output caps and really the output driver side of things um you're generally not going to see like a uh hiccup hiccup hiccup hiccup um as we call it.

**Dave Jones:** That's usually a primary side thing where this converter can't start up. So, yeah, I would not be looking at the secondary side. I'd be looking at the primary side.

**Dave Jones:** Now, they've actually rubbed number off this chip. So, we can't see what this is. Maybe I can get a knife on there and try and scrape it off but I think that they've actually scraped the number off that chip.

**Dave Jones:** Anyway, you want to give a visual on here and uh one of the first things I notice is that there's discoloration around there. That resistor in there. Is that my imagination or is that a bit discolored, too?

**Dave Jones:** Uh that looks a bit how you doing, doesn't it? So, we'll get in there and measure that and you can see that on the bottom as well. Look, you can see the fiberglass and like you start seeing like the the the weave in the fiberglass pattern, right?

**Dave Jones:** You You don't see that anywhere else. That means this has been heated up to buggery, and uh yeah, it's just the fiberglass is not uh you know, your high-temperature, high-quality stuff.

**Dave Jones:** So, it's just start to discolor and and yeah, it's it's not looking good. Also, you can see the same thing effect happening over here, as well. So, that's under um what's that under?

**Dave Jones:** That's these big resistors over here. These are just um input resistors, are they? Yep. So, yeah, they're just input um limiting surge resistors, whatever. Anyway, um yeah, there's no major caps on the uh input, even though this is a full-wave bridge rectifier.

**Dave Jones:** Um they just don't need a massive amount of uh capacitance on the input. Now, of course, as I said, these caps are under and near the heatsinks here. So, you would suspect these puppies, right?

**Dave Jones:** 50 V, and they would be to do with the startup as well. I don't know what that What's that in there? Is that a ST25C? Is that just an external uh switching transistor?

**Dave Jones:** I have to look that one up. ST25C, it's a BJT. It's an NPN BJT. Um yeah, it's just a jelly looks like it's just a jelly bean BJT. No worries.

**Dave Jones:** And we've got a bunch of diodes in here, as well. Uh you could go in and you could uh measure those as a matter of course, but I'm I'm really quite concerned that that resistor there is heated up a lot, and it's right next to the caps as well, and little alone the heat from the heatsink, but that that that resistor um that's obviously gotten hot because it's just

**Dave Jones:** yeah. Um so, anyway, let's get turn on our multimeter, shall we? And let's have a probe in there. What what value is that? Brown black? Something or brown black burnt.

**Dave Jones:** Brown black burnt is the is the value of that resistor. Now, when resistors get hot like this, obviously they're not going to be in the kiloohms or the hundreds of kiloohms cuz Ohm's law, you'd need like thousands of volts before you do anything.

**Dave Jones:** Um actually heat them up. So, this is going to be a low value uh low value resistor. And was that a gold band on there? Like you know, like a silver or something like this one over here.

**Dave Jones:** Anyway, so that's supposed to be a low value. So, let's measure that, shall we? 287 K. K, no. No. That's nope. Um Houston, we've had a problem. Um the resistor is that that is goneski.

**Dave Jones:** That is goneski. I don't need to measure anything else. I mean, I could. I mean, I could whack I could go diode mode and I could go start checking my diodes and stuff, but you want to fix anything you come across 0.56.

**Dave Jones:** No, 0.67. I think we're good on the diodes. Just check diodes cuz they're easy, you know, and you can generally check them in circuit. 0.7, you know. No. No No workers.

**Dave Jones:** So, yeah, I can't see visually anything else. Really, I mean, these suckers they like it it's discolored. I mean, it's it's discolored and it's 270 K. No, that doesn't add up.

**Dave Jones:** That does not add up. So, we have come across a there and we could have found a culprit. Is it that easy? Is it one resistor? Let's hope so.

**Dave Jones:** Makes for a boring video, but anyway. Oh, wow. Wow, that that other joint I I haven't even desoldered that and that other joint's gonsky. That's the other thing that I should have looked for on my visual was joints and let's actually go down here.

**Dave Jones:** Oh, hang on. There there's a pin sticking out. No, that can't that can't be it. And oh, yeah, yeah, that one look yeah, yeah, yeah, there you go. It's is that just a that's just a trans that's just a transformer leg.

**Dave Jones:** Okay, that's right. Yeah, there you go. This sucker has heated up so much that it's just delaminated. The copper's just delaminated from that. Wow, yeah, that's gonsky. Need to turn it the right angle there.

**Dave Jones:** Geez, there we go. Got that characteristic burny smell, that earny burny smell. And yeah, that that is one sick Oh, look at that. That's cracked the buggery. Wow. Wow, that sucker's had a harsh life.

**Dave Jones:** Look at that. So, that's Well, no, I thought that was brown black something. It's red. What is it? Red brown? Something. I don't know. That's just that's terrible, Muriel.

**Dave Jones:** Wow. Yeah, that is completely gone. No wonder. Wonder if we can just like is it just going to fall apart? I wonder if we just grab that with two pliers, is that going to come apart?

**Dave Jones:** I don't know. Still strong as a melee ball. But uh yep, it's it is completely cracked. It's gonsky. And that of course is probably open. The 270k was measuring in circuit and yep, yep, it's just it's it's gonsky.

**Dave Jones:** So, it could just be the resistor that just heated up so much that it eventually went open and I can guarantee it'll do exactly the same thing now if we power this up because is resistor's missing.

**Dave Jones:** It was open before. It's still open. So, yeah, maybe that's it. Maybe did they have the wrong resistor value? So, it's got to be like a piss-poor design because like you wouldn't design it so that resistor heated up so much that it failed like that.

**Dave Jones:** And it's not like because and like an ambient thing because it's inside the oyster light. I mean, that doesn't help, right? The fact that it's it's got no air flow in those sealed oyster lights upside down on the roof, but Oh, wow, you know?

**Dave Jones:** That's just That That's a harsh life. It's not good. Don't know. It could have been brown. It could have been black. That's just faded. It could be gold that's just faded.

**Dave Jones:** I'm That third band it does matter. It matters a lot cuz that's the That's That's the multiplier. So, I'd be tempted to go with gold, maybe. So, we're talking like 1 ohm.

**Dave Jones:** Silver would be Yeah, like It does look red on the screen here, but when I look at it with my eyes under my improper color lights here, it It looks brown.

**Dave Jones:** So, I think it's brown black. Um and it's just Yeah, it I know it does look red on camera, but when I look at it straight, it's actually it's it's more brown.

**Dave Jones:** So, Mhm. Anyway, that's what I'd expect. Yeah, I'd expect like in the order of like ohms-keys. So, where is it in circuit here? There it is there. That's one of the transformer taps.

**Dave Jones:** These are the transformer taps along here. I don't really want to reverse engineer this. So, No, that's a large value resistor in there. Yeah, so I'd say that's just a current shunt resistor.

**Dave Jones:** Is it? Don't know. I'd have to look up a typical primary side switcher for that cuz this obviously it's not doing the regulation on the primary side. It's doing the regulation on the secondary side here.

**Dave Jones:** That's the only reason why you'd have the SO8 controller there, which I think they've rubbed the numbers off that puppy as well, I think. The conformal coating doesn't help cuz, you know, you like you can still see the diode marking on the diode bridge over here.

**Dave Jones:** It Yeah, I tried to scrape that away and it says that there's there's nothing under there. But yeah, I don't know. And just throw in a couple ohms or something and see if it gets it back on track.

**Dave Jones:** So, I'll actually leave this one sticking up a bit. Why not? That's That's not going to touch the heat sink. Just leave it Leave it up there like that rather than have it right down on the board.

**Dave Jones:** That gives it some extra heat sinking due to the legs. Oops, that pad's lifted. Didn't go through. That's a bit cleaner. Hopefully, she'll go through now. That's the problem with lifted pads.

**Dave Jones:** Really rather annoying to try and get these back through. I think I got it. Yep, sweet. So, I'll just leave that flapping around in the breeze up there and Bob's your uncle.

**Dave Jones:** So, here's our main primary switching transistor over here. You can see that goes over to the coil there and that's our resistor in there now. So, I'm you know, it seems like that is not in the way of It goes under there.

**Dave Jones:** It goes over to here, which is then that small little TO-92 transistor we saw before. So, I'm not seeing how that's part of the main line. So, I'm not seeing how that resistor is in series with the main switching transistor there.

**Dave Jones:** So, that shouldn't be a problem even if we make that too low. I don't know. But yeah, if it was if it was in series, um, then obviously the value is going to matter, but, um, yeah, cuz it's in there.

**Dave Jones:** I don't know, there's this extra switching in here. That's like it's it's probably doing some like power factor correction as well, something like that. So, it's obviously doing something different.

**Dave Jones:** So, it may be as I said like it could be some other sense resistor or something like that, but it obviously heats up. So, it's important to get that value right.

**Dave Jones:** It's going to be critical and well, I don't know, cross your fingers and hope, um, I've got the value right. But anyway, um, yeah, let's just power it up, whatever.

**Dave Jones:** All right, let's give it a belt, see if we get anything. Woah! Magic smoke released. Holy crap. I guess that's the wrong value. Woah! What what what what Yep, I would say, uh, that wasn't, uh, gold that band.

**Dave Jones:** That's what happens when you underestimate the value. The actual resistor's fine, uh, but look at the input It was obviously drawing like probably an order of magnitude more current and those input resistors from the mains.

**Dave Jones:** Nothing else seems fried, um, which is really interesting, but those Wow! Look at those input resistors there. They are just uh, they're burnt. They are horrid. That is unbelievable.

**Dave Jones:** Um, yeah, I've completely come a gutser. I am I don't think I'm going to bother to fix this now. I'll just probably upload this as a hilarious what not to do.

**Dave Jones:** Um, yeah, I got a bad my spidey sense gave me a bad feeling just before I was about to switch it on. I thought, "Oh, no, I'm going to come a guts or I think I've got I should have gone up in value rather than down.

**Dave Jones:** Um, yeah, that was dumb, wasn't it? Actually, I presume that's an input fuse there. That just it goes to show how poorly that's rated. That input I'm going to cut that off because like that that should have popped before all of those just absolutely cooked.

**Dave Jones:** Um, yeah, I think they've rated that wrong. Oh, no, so much for that. I thought that that'd be a little axial fuse in there, but it's not. It's just a resistor.

**Dave Jones:** Anyway, oh boy, those puppies cooked. Sorry if you got that fan noise in the background. That's my filter going berserk here trying to get rid of the wretched smell from this sucker.

**Dave Jones:** Uh, yeah, well, that's embarrassing. That's double facepalm worthy. Yeah, please leave it in the comments down below. I'm an absolute dill, but I thought I had the right value, but then I like I knew that.

**Dave Jones:** I should have actually like at least attempted to reverse engineer this, see what was going on there, see exactly where the resistor was. The lower value was always going to be a concern, but I I thought it was gold in there, but uh, it's yeah, that multiplier band is going to come a guts or obviously.

**Dave Jones:** Yeah, I was off by at least an order of magnitude, but it seemed a reasonable at the time cuz if you have a look here, here's the resistor here, and it goes under there, and it goes to this small TO-92 um, MPN transistor that we looked at.

**Dave Jones:** So, it's not like, you know, that's going to be carrying amps or anything, so it's not the like emitter resistor in the main switching transistor which you'll be in series with the uh transformer over here.

**Dave Jones:** So, it's like it's not that. It's somewhere else in here doing something, but obviously, given the uh size of that uh resistor and the fact that it's heating up, yeah, it was obviously um doing something more important and dissipating a fair bit of power.

**Dave Jones:** So, with hindsight, yeah, that was just a dumb 1.8 ohms was a dumb choice. Um yeah, just didn't put the thinking cap on enough. No. All right, I've decided to do a basic reverse engineering here.

**Dave Jones:** It's not complete, so please excuse the crudity of the model. Didn't have time to build it to scale or to paint it. So, I'm going to work out where I goofed up.

**Dave Jones:** Uh my first goof was uh not remembering that this is a dimmable uh LED controller, which means that it has to start up at low voltages, which means it's going to need some sort of low voltage uh start up, you know, just in case the dimmer when you turn it on is like set to like a low voltage, like, you know, 50 volts, you know, something like that or whatever it is.

**Dave Jones:** Anyway, um yeah, we've got 240 in, you know, there's some filtering and other stuff over here. And including the resistors that burnt the hell out. And then we've got a bridge diode bridge rectifier.

**Dave Jones:** And then we've just got a main small uh filter cap, which is uh here. And then um here is our mystery resistor right here. And it looks like yeah, we've got a Zener basic Zener um circuit here with a emitter follower transistor here.

**Dave Jones:** That's a little uh TO-92 jobby in there. And um and that just powers the eight-pin chip. I still don't know what that uh chip is. Look up uh dimmable flyback uh LED controller or something like that.

**Dave Jones:** And there's 10 million of them. But it's more likely to be one of like the lesser-known like Asian variants or something like that. Anyway, um yeah, and then of course, the DC, the main couple hundred volts DC, powers the transformer over here, just like I suspected with of course the main switching MOSFET here.

**Dave Jones:** And then the other one watt resistor down in here, which I knew was the series resistor for that. And obviously that like then they're tapping that off somewhere else.

**Dave Jones:** I didn't bother, you know, going into details around the controller chip. But then you've got a tap coming off the primary of the transformer here, which goes via a diode, and that goes into buy basically bypassing the 180k.

**Dave Jones:** And the other resistor up here, the 180k one watt jobby, that's the other one watt resistor up here, which wasn't cooked at all. So, you wouldn't expect that 180k to be dissipating much at all, because it's basically in parallel with the coil over here, and which of course can be low impedance to then drive directly into our main Zener dropper down here.

**Dave Jones:** Obviously, this is going to be a Zener. I don't know the voltage, but I did, there it is, tiny little jobby down there. It's a sad looking thing, but it has had the snot blown out of it.

**Dave Jones:** It's measuring like three ohms, so yeah, that's no good at all. So, that probably that's not one of the original faults. That would have happened in my goof up.

**Dave Jones:** And we can see how it's blown here. This I totally goofed up. I you know, I thought it was some other, you know, current sense resistor or something dumb like that.

**Dave Jones:** I just, you know, I didn't have my brain engaged, and of course it's a if you did some basic reverse engineering, you would have seen that this was a Zener dropper, basically.

**Dave Jones:** So, this needs to be in the order of tens of Ks. So, that resistor value probably is either 10k or 20k. So, that third band, which I thought was gold, was actually I think it was orange.

**Dave Jones:** So, uh yeah. So, I think this was originally a 20K resistor. And here I am going putting in a 1.8 ohm. So, I was only out by four orders of magnitude.

**Dave Jones:** D'oh! So, we can see now how it snotted itself. Um yeah, we've got our high voltage DC here basically going straight through the coil like this and then straight across through the diode.

**Dave Jones:** I'm surprised like the diode uh survived and a straight through basically a short circuit, which then um snotted the uh Zener down here. So, it it turned it failed uh short circuit.

**Dave Jones:** So, if either of those failed open, then um yeah, we wouldn't have had the magic smoke escape. It just would have went pop. And uh pop goes the weasel.

**Dave Jones:** And yeah, it it would have been fine. We wouldn't have burnt the um in- input protection resistors over here. They wouldn't have turned completely black and charred like that.

**Dave Jones:** So, yeah, we just um it looks like I haven't measured this other diode. That could be shorted as well. Um likely. So, yeah, it just boom went straight down like that.

**Dave Jones:** So, this should have been, you know, 10 or 20K, something like that. And yeah, complete goofarama. I chose poorly. You chose poorly. And what that Zener voltage there would have uh been, uh you know, it's like in the order of maybe 20s, you know, the tens of volts, 20 volt.

**Dave Jones:** I mean, there's, you know, a 50-V uh rated cap. Both of these caps are 50-V uh rated here. And I won't go into details about, you know, how all this works.

**Dave Jones:** It doesn't really matter. If anyone does know, um they can, you know, guess based on the basic at least some of the pinout I've got here, um exactly what chip that is, please leave it in the uh comments down below.

**Dave Jones:** And if you do want me to do a complete reverse engineering, Well, if we got that chip, we probably shouldn't have to. They probably got an example circuit in there.

**Dave Jones:** It's probably almost identical to the example application circuit. They usually are. Very few differences usually. Anyway, if you want me to do a full reverse engineering, then you know, leave it in the comments down below.

**Dave Jones:** But I like we just needed to know where I goofed. And that's what it is. It looks like it was a Zener dropper circuit doll. So yeah, that was embarrassing, wasn't it?

**Dave Jones:** But anyway, I hope you found that valuable. My goof is your gain, I guess in terms of yeah, just you know, like a couple of more minutes. If I didn't rush this thing, a couple of more minutes just figuring out exactly what that resistor was doing would have prevented this.

**Dave Jones:** Obviously, if I knew it was a Zener dropper like this, there's no way I would have made that like, you know, ohms. I would have made it tens of ohms, something like that.

**Dave Jones:** And I would have probably guessed you know, it's not going to be like in the hundreds of K region. It's going to be in the tens of K region.

**Dave Jones:** If you do your Zener dropper calculation and stuff like that assuming like, you know, a milliamp or two drawing here and the minimum Zener current. You can work out, you know, a basic you know, ballpark resistor value.

**Dave Jones:** And it's going to be in the tens of K region, something like that. So yeah, I definitely wouldn't have made that mistake if I simply went spent a little bit more time doing the reverse engineering.

**Dave Jones:** So that let that be a lesson to you. Anyway, I hope you found that valuable. If you did, please give it a big thumbs up. As always, discuss down below.

**Dave Jones:** Catch you next time. Mhm.
