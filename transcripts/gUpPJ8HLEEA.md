---
video_id: gUpPJ8HLEEA
title: EEVblog #173 - Gossen Metrahit Energy Multimeter Teardown
url: https://www.youtube.com/watch?v=gUpPJ8HLEEA
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 24, "3": 39, "4": 63, "5": 73, "6": 106, "7": 121, "8": 136, "9": 148, "10": 163, "11": 179, "12": 191, "13": 204, "14": 212, "15": 230, "16": 243, "17": 263, "18": 273, "19": 288, "20": 302, "21": 314, "22": 341, "23": 353, "24": 372, "25": 388, "26": 400, "27": 419, "28": 436, "29": 447, "30": 453, "31": 467, "32": 477, "33": 491, "34": 501, "35": 518, "36": 534, "37": 545, "38": 559, "39": 581, "40": 599, "41": 616, "42": 627, "43": 639, "44": 648, "45": 659, "46": 672, "47": 681, "48": 707, "49": 727, "50": 746, "51": 754, "52": 766, "53": 780, "54": 792, "55": 809, "56": 821, "57": 834, "58": 853, "59": 866, "60": 888, "61": 917, "62": 928, "63": 940, "64": 952}
---

**Dave Jones:** Hi, welcome to the AAV blog and electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's product review time again.

**Dave Jones:** Yep, it's another multimeter and we haven't had one of these for a while. It's a German Gossen Metrawatt. Made in Germany, you beauty. What have these wacky Germans been up to this time with the Metrahit Energy?

**Dave Jones:** It's part of their uh Starline series, very similar to the Metrahit Xtra uh system multimeter I've reviewed donkey's years ago and this is the new Energy multimeter. Triple display, measures power and energy consumption.

**Dave Jones:** It's brilliant. It's one of my favorite METERS ON MY BENCH. Let's crack it open and see what's inside. Here it is up close. It uses exactly the same case as the Metrahit uh Xtra series which I've reviewed before, but of course it now it measures uh energy, power, watts, and VA, um power factor, and all sorts of stuff, voltage and current at the same time and that's why

**Dave Jones:** you've got the triple digit display up here, which is beautiful. I love it. It's got full count and resolution on each display. Haha, beautiful. And it's exactly the same case.

**Dave Jones:** It's got the IR interface and uh the same tilting bail and everything else. There it is, made in Germany. Got to love it. Love German made gear. Uh it's got a separate battery compartment up here, separate fuse compartment, and a couple of um uh security screws down the bottom which we'll crack open and see if we can get inside the case.

**Dave Jones:** And there you have it. You opened it up and you immediately uh like the construction except for one glaring thing which you are immediately drawn to and that is a mod resistor on the back of this board here.

**Dave Jones:** Look at it. Um granted, I do I believe I have like an early uh unit cuz I've had this one for quite some time. So, um I would presume that they've uh sorted that out and they've upgraded that in their production boards.

**Dave Jones:** I may even have a pre-production board or something like that there. Um but as you can see, it's uh two-board uh construction with the input circuitry which looks quite nice.

**Dave Jones:** Let's take a more detailed look. Now, what looks like at first to be a two-board uh construction here, it's not. It's actually a three-board construction. There's a third board under there, presumably a display board uh going through that connector there.

**Dave Jones:** And as you would expect, there is complete O-ring protection right around the outside of the case. But uh the main uh top part of the case though does not have really deep uh ridges on it uh for, you know, maximum blast protection.

**Dave Jones:** But uh Gossen do know what they're doing in this area. They are one of the leaders in um uh multimeter input protection and stuff like that. So, I'm sure they know what exactly what they're doing.

**Dave Jones:** And they've done the right thing with this uh fuse compartment design here. There's an extended uh part here which mates up with the um isolation slot, high-voltage isolation slot on the board here.

**Dave Jones:** So, it's for blast protection as well as arc over uh protection as well between the um input uh side and ground. That's a really nice design. I like it.

**Dave Jones:** There's one thing Gossen's uh done which is interesting on the uh DC input jack here. It's highly recessed on the back of the case. And presumably that's to stop the connector, when you put the connector in there, it's to stop it um shearing off uh to actually give it some uh stress protection.

**Dave Jones:** So, that's a really nice uh really nice aspect of the design. You can see the extended tube here for it, but unfortunately, it does go out to just basic flying leads, which are just hand soldered onto the board there.

**Dave Jones:** I would have much preferred to see a high quality connector there. And the input jacks here I really like. They're quite a unique design. They've got a single solid piece coming out of here with a single integrated lead coming out and then it's fed into a slot on the board like that and then hand soldered down there.

**Dave Jones:** There's a bit of solder residue on there, but it's not a big deal. So, that ensures a rigid connection because it's actually gone through that slot and held in place with that slot.

**Dave Jones:** So, it's really quite nice and there's automatic isolation between the front side and the back side of the board here and it's just it's really quite nice. As you'd expect with a top quality Gosund meter, you get a ton of input protection.

**Dave Jones:** Here's some high power input protection resistors, a couple of PTC poly switches here and here. That's your AC input coupling cap. You've got a couple of gas discharge tubes here, surface mount versions, nice to see.

**Dave Jones:** You've got a MOV here. And curiously, there's a couple of what looks like half amp fuses here and I'm not sure what they're actually protecting. Your guess is as good as mine.

**Dave Jones:** I've removed the main fuse here and you can see the current sense resistor under there and they've actually used a proper surface mount full terminal current sense resistor instead of the bent piece of metal basically that almost every other meter uses and you can see the extra you can see the voltage sense terminals there tapping directly off that directly off the terminals or the pads of that resistor

**Dave Jones:** and that's the proper way to do it. It's really nice. Now, curiously, there's a couple of MOSFET big power MOSFETs here like this, which switch the fuse. Now, I did a quick check and I've actually got a DaveCad drawing of that here.

**Dave Jones:** Let's so let's take a look at it. Here's your amps jack over here and your ground jack here. There's a 10 milli-ohm four terminal current sense resistor there. The those that voltage goes off there to a to a differential amplifier and these are your two MOSFETs.

**Dave Jones:** They're an IRL 2203 and a pretty standard device. It's a nice device. It's got a 7 milli-ohm on resistance, very low 30 volt rated, 116 amp, big beefy power MOSFET and they're put back to back like that.

**Dave Jones:** And of course there's internal parasitic diodes with that as well. Now, this secondary board here, that's rather interesting. You don't see that very often these days and I like it.

**Dave Jones:** It's just uses standard 0.1 inch pin headers like that. It really is quite nice. The circuitry under there we'll take a look at, but this is actually the power monitoring board which enables all the all the power factor correction and energy monitoring devices.

**Dave Jones:** This device here is actually a It's hard to get the number on that, but it's actually a Cirrus Logic CS5463 and that's a bidirectional power energy monitor IC specifically designed for this application.

**Dave Jones:** So, they've used it as you would. You would use an off-the-shelf chip for this. They've already perfected the energy measurement technology and and the various techniques used to measure all that sort of stuff.

**Dave Jones:** So, it's all on chip. It's got a built-in voltage references. It's just support circuitry. I'm not sure what it does. A bunch of op amps, few transistors and things.

**Dave Jones:** Pretty much discrete stuff, but I rather like that board. The bodgy resistor, I don't know. I'm going to assume they've fixed it in the production version. I'm not going to mark them down for that because, well, I don't know.

**Dave Jones:** It's Gos and, well, they actually have, um, a a history of doing us Germany company German companies like to make mods like this. It's not unusual at all, but I'm sure they fixed it.

**Dave Jones:** And check it out. This brings tears of joy. We've got two uh high sensitivity 3-V relays on here. Real manly relays that you switch stuff with. No this electronic switching.

**Dave Jones:** Stick in a relay. I love it when you turn the range switch and you hear that click of that relay, you know? Uh you just know it's designed and it's going to measure properly.

**Dave Jones:** I love it. And if you're wondering what this device here, it looks rather curious. I have, uh, I don't think I've ever seen one of these before or very rarely, but, uh, what I believe it is is I believe it's a, um, thick film hybrid precision resistor.

**Dave Jones:** And I measure it and it's pretty darn close to spot on to 20 megaohms. So, um, I believe that's what it is and, uh, it's just unusual because one thing you won't find on this board overall is a thick film precision hybrid resistor network.

**Dave Jones:** So, uh, obviously they're, well, that that's probably one of them and maybe they're using some dis- discretes. I don't know. But, as you can see, the rest of the board is lovely constructed.

**Dave Jones:** The, uh, lovely, nicely laid out. The, uh, soldering, the construction, the components are, uh, first class. We've got a a couple of, um, surface mount electrolytic caps here. There's a couple of tantalums in there as well.

**Dave Jones:** There's lots of, uh, 404,000 series, uh, switching like there's some max, uh, 4053 devices, uh, down here. There's a max 4052 over here somewhere. And this device down in here is actually the, uh, true RMS converter chip and they haven't used the analog devices one.

**Dave Jones:** They've gone with a uh Cirrus Tech um brand, which is a uh I believe it's a Taiwanese uh brand who do multimeter chipsets. They also do a uh true RMS converter chip and it's the ES636, which presumably is uh maybe uh pin compatible.

**Dave Jones:** I haven't checked. Probably pin compatible with the analog devices past cuz as you can see, they're putting a dual footprint there, so maybe they can uh decide at at the time of production whether or not to use the uh Cirrus Tech one or maybe use a different package or a different brand entirely.

**Dave Jones:** No major surprises whatsoever. The main processor is a TI MSP430 low-power 16-bit uh micro and uh there's another device here which might be a custom one. I don't know.

**Dave Jones:** It's got a sticker over it. I'm going to have to take that off. Uh there's a bunch of other uh discrete um just uh discrete devices around here. There's nothing uh terribly interesting there.

**Dave Jones:** And the battery terminals uh lovely. The double A battery terminals soldered directly onto the board. I love it. There are three uh three terminal mount like that. Really nice.

**Dave Jones:** And they've got a proper uh through-hole buzzer like that. None of this external little uh piezo crap which is stick on the side of the case with a couple of flying leads.

**Dave Jones:** And there's the infrared transceiver. Now curiously, it's actually a fair distance back from the uh window on the back part of the device here, but I guess that's not a big deal.

**Dave Jones:** It still works just fine. I've taken the sticker off that chip and I can't see any identifiable markings at all. There's a bit of residue on there which I can't get off, but I can't see a thing.

**Dave Jones:** So maybe it's a fully custom Gossamer ASIC. Who knows? Gossamer, you got an answer on that one? Well, I'm trying to get this top board out here. One of the really annoying things is that it looks like you have to desolder the input connectors here before you can actually lift the board out.

**Dave Jones:** What a bummer. There we go. I've desoldered the three terminals there, which was actually quite easy. And tada! There we go. It lifts straight up and we can access the bottom board.

**Dave Jones:** And here's the famous Goswami range switch. That's how they implemented. They've got springs either side here with large notches and this is how they make it feel and sound so magnificent when it switches ranges like that and the positive retention you get on each one.

**Dave Jones:** Ah, it's just pornographic. It really is. And here's the bottom part of the board. They've got extra some extra power resistors on here. They've got this large metal shielding can.

**Dave Jones:** There's not much under there. There's just pretty much more of the same. They've got a whole bunch of other passive devices on the bottom here and not much else really.

**Dave Jones:** But yeah, there's quite a significant amount of extra passives on the bottom side. There you go. There's more hybrid resistors on the bottom here. A couple more there a couple of meg each and there's another device down here which looks similar.

**Dave Jones:** It's green coded with like a green mask on it which looks different to those but it's a the the tracking work on the top is identical but that one is not high value.

**Dave Jones:** That one's around about 2 ohms or thereabouts. I've swung away the top LCD board and once again they've spared no expense here. Instead of just the rubber membrane type interface they've got proper tactile switches.

**Dave Jones:** surface mount switches there. Beautiful. And the LCD just isn't a standard uh LCD a cheap LCD uh with just the uh zebra strip for the contacts, it's actually a chip on board.

**Dave Jones:** Those Those two little uh things you see down in there are actually the uh chip on glass. They're actually the chip chips mounted directly on the glass. And as you can see, there's not many connection interfaces.

**Dave Jones:** There's just a a few down here and a couple of extra uh support ones uh top and bottom here. And that's actually got the circuitry built on to drive all of the many many hundreds of circuits for the triple digit display on there, cuz really uh without that, you wouldn't you'd have a hell of a time driving it from just a generic micro.

**Dave Jones:** It's just got too many segments with that triple display. So, they've gone to a lot of effort there to do a fully custom uh chip on glass or uh COG display, it's called.

**Dave Jones:** And I've put it back together, and it all works, of course, but listen to these lovely relays. Ah. Isn't that just beautiful? Let's hear that again. Ah. After tearing something down, there's usually a screw left over, but not in this case.

**Dave Jones:** I'm missing the fuse. I'm lucky for me, I have no idea where the thing went. Unbelievable. One thing which uh is hard to get a a real gauge of is the quality of the plastics used in the construction, but you can just uh after a while, you get some experience, you can just tell that this is a real high-quality ABS, probably an impact-resistant uh polymer type uh ABS material, real high-quality

**Dave Jones:** uh stuff, as you'd expect in a high-end meter like a Gossen. I'm sure they spared no expense. It's not those cheap, brittle plastics you get in the real one-hung low brand meters.

**Dave Jones:** So, there you have it. That's the Gossen Metrawatt energy multimeter. As you'd expect, superbly designed and built. I'm thoroughly impressed. That dodgy resistor aside, well, you know, I'm sure they'll fix that.

**Dave Jones:** There's no excuse for that. But, anyway, unbelievably good. I love the quality, the design, and the construction. But, you pay through the nose for it. So, that's what you expect.

**Dave Jones:** Now, where's that freaking fuse? Man.
