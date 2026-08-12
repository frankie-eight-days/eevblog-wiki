---
video_id: AHu0MGEagSo
title: EEVblog #281 - BK Precision 8500 Electronic Load Teardown
url: https://www.youtube.com/watch?v=AHu0MGEagSo
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 23, "3": 35, "4": 50, "5": 76, "6": 86, "7": 97, "8": 110, "9": 132, "10": 143, "11": 155, "12": 173, "13": 187, "14": 203, "15": 217, "16": 227, "17": 255, "18": 277, "19": 291, "20": 315, "21": 326, "22": 338, "23": 353, "24": 363, "25": 381, "26": 390, "27": 401, "28": 410, "29": 419, "30": 436, "31": 446, "32": 456, "33": 469, "34": 485, "35": 493, "36": 507, "37": 517, "38": 529, "39": 542, "40": 557, "41": 570, "42": 603, "43": 635, "44": 660, "45": 687, "46": 706, "47": 717, "48": 730, "49": 756, "50": 773, "51": 786, "52": 808, "53": 823, "54": 837, "55": 853, "56": 874, "57": 889, "58": 903, "59": 915, "60": 929, "61": 944, "62": 956, "63": 964, "64": 984, "65": 1000, "66": 1009, "67": 1016, "68": 1026, "69": 1041, "70": 1055, "71": 1066, "72": 1079, "73": 1093, "74": 1117, "75": 1135, "76": 1146, "77": 1159, "78": 1172, "79": 1182, "80": 1196, "81": 1207, "82": 1218, "83": 1228, "84": 1241, "85": 1260, "86": 1283, "87": 1293, "88": 1305}
---

**Dave Jones:** Hi, welcome to teardown Tuesday. I was going to do something slightly different today as opposed to the usual test gear teardowns I seem to be doing lately, but I couldn't resist.

**Dave Jones:** Got this really nice bit of kit in the FedEx box the other day. You can't stop me. Now, I've done a couple of power supply teardowns recently and I've got another few coming up.

**Dave Jones:** So, if you love power supplies, hang out for those, but I've got a very useful, incredibly useful companion device to power supplies and I haven't done teardown review of one of these before.

**Dave Jones:** I have done a video of how to make your own. What is it? It's the BK Precision 8500 300 W DC electronic load and this looks like a really awesome bit of kit.

**Dave Jones:** Oh, it smells good, too. I love it. So, what this is is it's a BK Precision 8500, but it's actually designed and manufactured by a company called ITech and it's sold It is also sold under the ITech brand as well, but it's not just re-badged by BK Precision because ITech is apparently a BK Precision company.

**Dave Jones:** It's all part of the one big, you know, global corporation or something like that. So, I'm expecting good things out of these because ITech, this is all they do.

**Dave Jones:** They do, you know, power supplies, electronic loads, system loads, you know, things like that. So, I'm expecting this to be really well engineered, just not some one-hung low slapped-together cheapy.

**Dave Jones:** And check out these big beefy binding posts. Look at that. How can you not love that? You know, what we say here on the EEVblog, don't turn it on, take it apart.

**Dave Jones:** Now, I've got to say thanks to Greg at BK Precision for getting me one of these puppies because it's going to be really handy for my power supply testing videos, my power supply design videos because you've seen my video with the electronic load where I built my own, you know, a very simple crude as crude as you can possibly get.

**Dave Jones:** Well, you can't beat having a proper, precision DC electronic load and this one really is a precision bit of kit and it goes up to 300 watts as well.

**Dave Jones:** It's awesome. So, thanks Greg. So, you can expect to see this thing get quite a bit of use in the EE blog lab here as I design various power supplies and things like that.

**Dave Jones:** Very handy bit of kit and probably one of the most overlooked bits of kit in any a lab. And if you're designing power supplies, you really should have any sort of power supply switch mode, linear, whatever, small or large, you should have a precision DC electronic load some sort.

**Dave Jones:** And of course, I'll do a proper review of this thing later cuz it comes with PC control software and all sorts of stuff like that. But look at these huge big binding posts on the front.

**Dave Jones:** Absolutely awesome. Lovely knob here for setting stuff, current, constant current, constant voltage, constant resistance, constant power modes, everything. More stuff than you can poke a stick at. I love it and it's a really nice big clunking power switch on here and it's a really nice solid unit.

**Dave Jones:** And check out the base of it down in here. Huge metal base with tons of screws. I love it. So, let's crack this thing open and see what's inside.

**Dave Jones:** I think just a maybe a couple of screws on the back will get the back panel off and maybe the front panel as well and then maybe those four on there and this might slide off.

**Dave Jones:** Let's find out. Yeah, and that came off pretty much exactly as I thought. The rubber surround on the front just slid off nicely. No screws holding that in. I really like that design.

**Dave Jones:** So, it's really easy. So, let's This should just slide right open. Ah, tada. And there's no major surprises here at all. It looks off the bat looks very well built, very well designed as you'd expect from a specialist designer and manufacturer of these sort of electronic loads.

**Dave Jones:** And no surprises in the layout and the amount and type of circuitry in here. We've got a mains transformer for powering the thing. We've got We've got some big current shunts over here.

**Dave Jones:** We've got some current shunt power resistors down in here. We've got some MOSFETs hooked onto some large heat sinks with some pretty decent fans here on each one. I rather like this actually, this dual arrangement here with the fan inside sucking the air from these vent holes here through the heat sink and boom, out the back like that separately on both of these.

**Dave Jones:** And that mains input over here and some control circuitry. We'll take a look at that. We've got a number rubbed off there. Don't like that. We've got a couple of relays, which I love, of course.

**Dave Jones:** I love products that have relays in there. Bit of miscellaneous power supply to power the control circuitry and the input stuff. So, this looks really neat. Let's take a look at the individual parts in more detail.

**Dave Jones:** Now, I find this rather strange. Here's the IEC input connector. It's a shrunk, of course. I've got some uh ferrite beads there for a bit of RFI going into uh decent connectors onto the board there.

**Dave Jones:** And the voltage selection switch on the back panel, 240 V 110, is there as well. And that goes down to a second connector uh down in the bottom, down in there.

**Dave Jones:** But, the transformer is all the way over here. So, it's it's right down in here. So, those mains tracks have to run all the way around here, down the board, probably maybe on the top side or the underside there, down into the transformer, down in here.

**Dave Jones:** And uh why they didn't just uh run some cable in down there, you know, neatly lay it around the side or something like that, cable tie it, I don't know.

**Dave Jones:** But, they decided to do it all through the tracks. I guess it's neater um that way. But, they've got the 240 V uh traces, mains traces, looks like, uh running under the heatsinks.

**Dave Jones:** It could be on the uh bottom side of the board. It can't just run down the center here cuz there's all that um all that uh current sense circuitry down there.

**Dave Jones:** So, it looks like the traces go off here somewhere under the heatsink here, and they pop out down here. And you can actually see the silkscreen on top of the mains traces there.

**Dave Jones:** So, presumably they have actually got them running on the top of the board. And here's the big clunking power switch down in here. I love that. And uh here's the um output connector, which the mains output connector, 240 V, which goes into the primary of the transformer.

**Dave Jones:** So, I don't know. It's There's nothing uh inherently wrong with that. I'm sure they've uh done all their design uh calculations and clearance uh things like that. So, it's not a problem.

**Dave Jones:** Um one thing it is certainly is neat. And if you have a careful look down there, you can see a couple of signal traces here. These are the 240 V mains traces.

**Dave Jones:** And there's another power supply um you know, a low voltage um the secondary side power supply trace down there. It looks like it's only maybe 5 or 6 mm uh clearance tops in there.

**Dave Jones:** Uh there I see it. It does actually drop down to the bottom layer there. So, it looks like it may not actually run under the heat sink. And you'll notice they've gone to a fair bit of trouble to actually celastic down that IDC uh ribbon cable there on the header.

**Dave Jones:** They've celastic down uh these connectors down in here, the mains connector, and the ribbon cable down on that side. And they've done that in uh quite a few places.

**Dave Jones:** So, they've certainly uh taken vibration into account here. And we'll see that again over on the um input connectors over here. And by the way, the transformer's uh held down very nicely with uh shake-proof washers.

**Dave Jones:** They've done that really well. And the uh earth connection down there has some uh Loctite on it as well, so it can't come loose. And here's the input connectors.

**Dave Jones:** Aren't they beautiful? Check that out. Huge big solid threaded bolt coming from the input connector cuz remember, this is a 30-A um input, 30-A capable, and high voltage as well.

**Dave Jones:** We're talking about a 300-W DC electronic load here. And then that comes up into a a custom uh right-angle bracket, which is soldered um directly onto the board there.

**Dave Jones:** That's a really nice implementation. And of course, you can see the red Loctite around there as well to stop them shaking loose. I love it. Very well engineered. And the other input circuitry around here, we've got a couple of big uh 1-A power resistors here.

**Dave Jones:** Once again, celastic uh down so they don't uh vibrate loose. We've got a couple of uh high-voltage caps. We've got some MOVs. And uh we've got some uh high-voltage um isolation slots cut through the board down in there.

**Dave Jones:** So, they've uh paid a bit of attention to detail to there. I like it. And I'm going to presume that these two large uh shunts here the main input current shunts and they would have possibly been tweaked to value or they're or they're tweaked in software of course to actually know that out because this is a real high precision unit by the way we're talking 0.05 percent class voltage measurement and at

**Dave Jones:** least 0.1 percent class current measurement as well very precise bit of kit so I expect it to that would be a very low tempco metal to use as the current shunt and we should have some some precision voltage reference and ADC circuitry elsewhere but it looks like there's room for two more there maybe different model units cuz there are various models in this entire range and they have different

**Dave Jones:** capabilities. And we've got a date on this sucker 10th of the 9th 06 so it looks like it is quite an old design it's been around for quite some time you know and these DC electronic loads they don't change much they don't need to be upgraded so that doesn't surprise me at all and there it is it's the IT 85 11 load and presumably this baseboard can

**Dave Jones:** be used for the other models as well. And in the logic control power supply circuitry here they've got some Lelon brand electrolytic caps which I believe are reasonably good quality they're all 105 degrees so they haven't skimped on there and that looks quite reasonable but always note that I'm not a huge fan of these free standing TO220s and they've done that a couple of times and there's

**Dave Jones:** the other two free standing TO220s and you can give those a little bit of a wiggle I would have liked to have seen those mounted flat or mounted on a small heat sink or somehow rigidly retained cuz they've done a really good job on all the other Loctite in the nuts and the connectors səlastic in those down and things like that.

**Dave Jones:** So, I'm always a little bit weary of that, but it's a very minor point. We've got our main processor here. It's a small one, tiny little microcontroller of some sort and boohoo, they've rubbed the number off.

**Dave Jones:** Why? Come on, people. Really? Is it that important that you got to rub the number off that chip and that chip only? Give me a break. Anyway, there's the main oscillator crystal.

**Dave Jones:** We've got another 32 kHz watch crystal over here. Once again, that one's səlastic down instead of the more usual soldering down. And here I am trying out my new 10x Opteka macro lens I've got for my Canon HFG10 camera and this is working really well and you can see the gouges taken out of the main processor there.

**Dave Jones:** They've really ground that out. They haven't, you know, they've really got in there with like a Dremel or something and really dug that out. And there's a 24LC64 E-squared prom that would hold the calibration values, one would presume.

**Dave Jones:** And there's a whole bunch of 07 precision op amps around this thing. They're all over the shop here. These op 07s there's like seven, eight, nine of them. So, no surprises there.

**Dave Jones:** They're the industry standard precision op amp. And there's an AD 7708 and that's a 16-bit delta sigma ADC. No surprises at all. Built-in programmable gain amp. And the reason you need a 16-bit converter in this thing is because it's got a 1 mV resolution in an 18 V range.

**Dave Jones:** That's one part in 18,000 and to do that, you could probably get away with a 15-bit converter, but they don't make those as well. So, they use a 16-bit converter, which is one part in 65,000.

**Dave Jones:** So, it's ideally matched and down here we have a Burr-Brown. Love Burr-Brown parts, which are now TI of course, but that's a DAC 7631 and that's a matching pretty much a matching 16-bit voltage output DAC.

**Dave Jones:** And there's a voltage reference for the ADC and the DAC could be shared between them. It's the ADR421 that and that's like a better than 0.05% class voltage reference with three ppm temp co.

**Dave Jones:** Very nice. And that's something a lot of people forget with precision designs like these. You don't necessarily need absolute precision components. You just need low temperature coefficient or you know, highly temperature stable components and then you can take care of the rest with software calibration.

**Dave Jones:** So, it's you know, you can get a really precise instrumentation by using a 1% voltage reference for example, but as long as it has a very low temp co, then you can take care of that with software calibration.

**Dave Jones:** Now, I love how in this section down here they're TL074 quad op amps and they're in old style DIP package and there's a LM324 and it's in an SO package.

**Dave Jones:** So, that's just really just quite strange how they've actually got those in a DIP package and look at those passives surrounding that. They're quite spread out with the traces going a long way.

**Dave Jones:** I just wonder why they've done that. And as you can see also, we've got a whole bunch of these um RX21 series uh silicon resin coated uh 8-W power resistors in there.

**Dave Jones:** And they're available with uh 1% uh tolerance values and about uh 250 ppm, I believe. And the big MOSFET we've got on here is an IRFP250, and it's quite uh hard to get the camera in there, but there you go.

**Dave Jones:** There's a couple of There's um quite a few of these devices scattered around the heat sinks to spread the load. And they're 30-A 200-V MOSFETs, and you can see uh a couple over here.

**Dave Jones:** You can see another couple up there, as well. So, that's four, but if you look down the side of the heat sinks, they've got another one and two there.

**Dave Jones:** So, uh they've got a total of four uh MOSFETs per side here. So, a total of eight um of those huge power MOSFETs. That's to um share That's where all of most of your load gets uh dissipated into these MOSFETs and through to these large heat sinks here.

**Dave Jones:** There's a little bit in your uh current shunts and uh things like that, but uh most of your power most of that 300-W capability is going to be delivered into these large heat sinks, and the fans are going to suck the air in from the side here, suck it through the fins, and take it out the back.

**Dave Jones:** And as you can see, there's a whole bunch of factory tests it passed in each uh stage through the production uh testing. It gets a little sticker on it.

**Dave Jones:** Calibrated and it's done all the calibration and the trim pots, and they've tweaked it um because this, as I said, is a precision instrument. Very important process to calibrate it.

**Dave Jones:** Then they would have done the uh high-voltage test. It would have um some sort of uh burning test. I don't know. They might run it at full load for 24 hours or something like that.

**Dave Jones:** May possibly in a thermal chamber to see if it um you know, at an elevated uh ambient temperature to see if it keels over or something like that. Um PRT, test, I'm not sure exactly what that is.

**Dave Jones:** That's PRT is usually a production readiness test, but I think it could be like a a high pot mains compliance test or something like that. And ICT is probably in circuit test as well.

**Dave Jones:** So ultimately what that means is that when you buy this thing, you can be pretty darn sure that it's going to function correctly out of the box and continue to function correctly because it's had that burning.

**Dave Jones:** And that's what you're paying for for these quality bits of instrument from a proper manufacturer that uh specifically develops equipment like this. And there'll be a few people who are just keen to see what's on the back.

**Dave Jones:** I see input connector fused 220 110 volt selection. We've got a serial control interface. And my unit came with isolated, by the way, completely isolated RS232 and USB B cables, very nice.

**Dave Jones:** And it comes with remote sense spring terminals as well. You can just get in there and push your wire in and trigger input as well. Very nice. And there's not much doing on the front display board up here with the soft button keys and the vacuum fluorescent display apart from the two vacuum fluorescent display driver chips.

**Dave Jones:** They're they're a PT6315 and that's a serial input vacuum fluorescent display driver. And there's two of those and it is a very nice display and they've got that of course interfacing with the ribbon cable over here going down to the microcontroller.

**Dave Jones:** And there's a teensy bit of circuitry there for the very nice rotary encoder knob and a buzzer to make some sound at you. Beep. And I forgot to mention a couple of other mobs scattered around the place.

**Dave Jones:** And they've got another couple of devices connected to the heat sink here is well a uh three-pin TO220 and a bridge rectifier uh down in here as well connected to this side of the heat sink.

**Dave Jones:** So, as you can see, there's not a huge amount inside these electronic loads. There's a microprocessor to control it all. There's a DAC and an ADC to uh not only uh set the value required, but read it back.

**Dave Jones:** And there's a um a a MOSFET or a bunch of MOSFETs with some load resistors. And that's, you know, pretty much the basic operation of any DC electronic load.

**Dave Jones:** Except this one is uh really nice cuz it's high precision. And I really do like how it's nice one bit big solid bit of folded uh sheet steel which goes right over the top like that.

**Dave Jones:** It really works on the bottom. Sorry, this is the bottom of the unit. It really is quite nice. Everything uses uh shake-proof uh washers on there. And uh by the way, in case you're wondering, there is no circuitry on the bottom.

**Dave Jones:** So, there's no advantage to uh taking that part anymore, but doesn't it look really schmick? And I couldn't really uh fault the design or build quality in this thing.

**Dave Jones:** It uh it it's certainly uh first class and I would certainly give it a big thumbs up. So, there you have it. That's inside the BK Precision 8500 precision DC electronic load.

**Dave Jones:** If you're into power supply design, um I highly recommend you pick one up. This this isn't a review, but uh people want to know the price. Street pri- um sorry, uh recommended price is about 1,100 bucks for this particular model.

**Dave Jones:** Street price is around about 900 bucks or lower or you know, even substantially lower than that depending on where you get it from. And uh this is actually the IT8512 is equivalent to the BK Precision 8500, but there's like a dozen different models.

**Dave Jones:** This is the 120 V 30 A 300 W version, but they're available in different voltages and currents and power ratings. So, thanks to BK Precision for this. It'll be a very handy bit of kit and you'll no doubt um see it uh coming up when I do some more uh videos on the uh power supply design stuff cuz this is fantastic for testing any sorts of power supplies, switch

**Dave Jones:** mode, linear, it can do uh pulse loads as well. You can set it up and it can do battery discharge uh testing as well under PC control. Fantastic, very useful bit of kit.

**Dave Jones:** And remember, if you like uh teardown Tuesday, please give it a thumbs up cuz that helps a lot. And if you want to discuss this, jump on over to the EEVblog forum.

**Dave Jones:** Catch you next time.
