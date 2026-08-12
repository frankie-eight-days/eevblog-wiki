---
video_id: AHu0MGEagSo
title: EEVblog #281 - BK Precision 8500 Electronic Load Teardown
url: https://www.youtube.com/watch?v=AHu0MGEagSo
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 35, "3": 76, "4": 106, "5": 140, "6": 171, "7": 187, "8": 210, "9": 247, "10": 262, "11": 289, "12": 322, "13": 353, "14": 372, "15": 393, "16": 422, "17": 451, "18": 469, "19": 485, "20": 503, "21": 520, "22": 550, "23": 584, "24": 628, "25": 663, "26": 695, "27": 711, "28": 730, "29": 756, "30": 773, "31": 813, "32": 849, "33": 889, "34": 926, "35": 956, "36": 970, "37": 1000, "38": 1026, "39": 1041, "40": 1076, "41": 1108, "42": 1135, "43": 1165, "44": 1187, "45": 1201, "46": 1214, "47": 1244, "48": 1276, "49": 1293}
---

**Dave Jones:** Hi, welcome to teardown Tuesday. I was going to do something slightly different today as opposed to the usual test gear teardowns I seem to be doing lately, but I couldn't resist. Got this really nice bit of kit in the FedEx box the other day.

**Dave Jones:** You can't stop me. Now, I've done a couple of power supply teardowns recently and I've got another few coming up. So, if you love power supplies, hang out for those, but I've got a very useful, incredibly useful companion device to power supplies and I haven't done teardown review of one of these before.

**Dave Jones:** I have done a video of how to make your own. What is it? It's the BK Precision 8500 300 W DC electronic load and this looks like a really awesome bit of kit. Oh, it smells good, too. I love it. So, what this is is it's a BK Precision 8500, but it's actually designed and manufactured by a company called ITech and it's sold It is also sold under the ITech brand as well, but it's not just re-badged by BK Precision because ITech is apparently a BK Precision

**Dave Jones:** company. It's all part of the one big, you know, global corporation or something like that. So, I'm expecting good things out of these because ITech, this is all they do. They do, you know, power supplies, electronic loads, system loads, you know, things like that. So, I'm expecting this to be really well engineered, just not some one-hung low slapped-together cheapy. And check out these big beefy binding posts. Look at that. How can you not love that?

**Dave Jones:** You know, what we say here on the EEVblog, don't turn it on, take it apart. Now, I've got to say thanks to Greg at BK Precision for getting me one of these puppies because it's going to be really handy for my power supply testing videos, my power supply design videos because you've seen my video with the electronic load where I built my own, you know, a very simple crude as crude as you can possibly get. Well, you can't beat having a proper, precision DC electronic load and this

**Dave Jones:** one really is a precision bit of kit and it goes up to 300 watts as well. It's awesome. So, thanks Greg. So, you can expect to see this thing get quite a bit of use in the EE blog lab here as I design various power supplies and things like that. Very handy bit of kit and probably one of the most overlooked bits of kit in any a lab. And if you're designing power supplies, you really should have any sort of power supply switch mode, linear, whatever, small or

**Dave Jones:** large, you should have a precision DC electronic load some sort. And of course, I'll do a proper review of this thing later cuz it comes with PC control software and all sorts of stuff like that. But look at these huge big binding posts on the front.

**Dave Jones:** Absolutely awesome. Lovely knob here for setting stuff, current, constant current, constant voltage, constant resistance, constant power modes, everything. More stuff than you can poke a stick at. I love it and it's a really nice big clunking power switch on here and it's a really nice solid unit. And check out the base of it down in here.

**Dave Jones:** Huge metal base with tons of screws. I love it. So, let's crack this thing open and see what's inside. I think just a maybe a couple of screws on the back will get the back panel off and maybe the front panel as well and then maybe those four on there and this might slide off. Let's find out.

**Dave Jones:** Yeah, and that came off pretty much exactly as I thought. The rubber surround on the front just slid off nicely. No screws holding that in. I really like that design. So, it's really easy. So, let's This should just slide right open.

**Dave Jones:** Ah, tada. And there's no major surprises here at all. It looks off the bat looks very well built, very well designed as you'd expect from a specialist designer and manufacturer of these sort of electronic loads. And no surprises in the layout and the amount and type of circuitry in here. We've got a mains transformer for powering the thing.

**Dave Jones:** We've got We've got some big current shunts over here. We've got some current shunt power resistors down in here. We've got some MOSFETs hooked onto some large heat sinks with some pretty decent fans here on each one. I rather like this actually, this dual arrangement here with the fan inside sucking the air from these vent holes here through the heat sink and boom, out the back like that separately on both of these. And that mains input over here and some control circuitry. We'll take a look at that. We've got a number rubbed

**Dave Jones:** off there. Don't like that. We've got a couple of relays, which I love, of course. I love products that have relays in there. Bit of miscellaneous power supply to power the control circuitry and the input stuff. So, this looks really neat. Let's take a look at the individual parts in more detail. Now, I find this rather strange. Here's the IEC input connector. It's a shrunk, of course. I've got some uh ferrite beads there for a bit of RFI going into uh decent connectors onto the board there.

**Dave Jones:** And the voltage selection switch on the back panel, 240 V 110, is there as well. And that goes down to a second connector uh down in the bottom, down in there. But, the transformer is all the way over here. So, it's it's right down in here.

**Dave Jones:** So, those mains tracks have to run all the way around here, down the board, probably maybe on the top side or the underside there, down into the transformer, down in here. And uh why they didn't just uh run some cable in down there, you know, neatly lay it around the side or something like that, cable tie it, I don't know. But, they decided to do it all through the tracks.

**Dave Jones:** I guess it's neater um that way. But, they've got the 240 V uh traces, mains traces, looks like, uh running under the heatsinks. It could be on the uh bottom side of the board. It can't just run down the center here cuz there's all that um all that uh current sense circuitry down there. So, it looks like the traces go off here somewhere under the heatsink here, and they pop out down here. And you can actually see the silkscreen on top of the mains traces there. So,

**Dave Jones:** presumably they have actually got them running on the top of the board. And here's the big clunking power switch down in here. I love that. And uh here's the um output connector, which the mains output connector, 240 V, which goes into the primary of the transformer. So, I don't know. It's There's nothing uh inherently wrong with that. I'm sure they've uh done all their design uh calculations and clearance uh things like that. So, it's not a problem. Um one thing it is certainly is neat. And

**Dave Jones:** if you have a careful look down there, you can see a couple of signal traces here. These are the 240 V mains traces. And there's another power supply um you know, a low voltage um the secondary side power supply trace down there. It looks like it's only maybe 5 or 6 mm uh clearance tops in there.

**Dave Jones:** Uh there I see it. It does actually drop down to the bottom layer there. So, it looks like it may not actually run under the heat sink. And you'll notice they've gone to a fair bit of trouble to actually celastic down that IDC uh ribbon cable there on the header.

**Dave Jones:** They've celastic down uh these connectors down in here, the mains connector, and the ribbon cable down on that side. And they've done that in uh quite a few places. So, they've certainly uh taken vibration into account here. And we'll see that again over on the um input connectors over here.

**Dave Jones:** And by the way, the transformer's uh held down very nicely with uh shake-proof washers. They've done that really well. And the uh earth connection down there has some uh Loctite on it as well, so it can't come loose. And here's the input connectors. Aren't they beautiful?

**Dave Jones:** Check that out. Huge big solid threaded bolt coming from the input connector cuz remember, this is a 30-A um input, 30-A capable, and high voltage as well. We're talking about a 300-W DC electronic load here. And then that comes up into a a custom uh right-angle bracket, which is soldered um directly onto the board there. That's a really nice implementation. And of course, you can see the red Loctite around there as well to stop them shaking loose. I love it.

**Dave Jones:** Very well engineered. And the other input circuitry around here, we've got a couple of big uh 1-A power resistors here. Once again, celastic uh down so they don't uh vibrate loose. We've got a couple of uh high-voltage caps. We've got some MOVs. And uh we've got some uh high-voltage um isolation slots cut through the board down in there. So, they've uh paid a bit of attention to detail to there. I like it. And I'm going to presume that these two large uh shunts here the main input current shunts and they

**Dave Jones:** would have possibly been tweaked to value or they're or they're tweaked in software of course to actually know that out because this is a real high precision unit by the way we're talking 0.05 percent class voltage measurement and at least 0.1 percent class current measurement as well very precise bit of kit so I expect it to that would be a very low tempco metal to use as the current shunt and we should have some some precision voltage reference and ADC circuitry elsewhere but it looks like there's room for two more

**Dave Jones:** there maybe different model units cuz there are various models in this entire range and they have different capabilities. And we've got a date on this sucker 10th of the 9th 06 so it looks like it is quite an old design it's been around for quite some time you know and these DC electronic loads they don't change much they don't need to be upgraded so that doesn't surprise me at all and there it is it's the IT 85 11 load and presumably this baseboard can be used for the other models as well.

**Dave Jones:** And in the logic control power supply circuitry here they've got some Lelon brand electrolytic caps which I believe are reasonably good quality they're all 105 degrees so they haven't skimped on there and that looks quite reasonable but always note that I'm not a huge fan of these free standing TO220s and they've done that a couple of times and there's the other two free standing TO220s and you can give those a little bit of a wiggle I would have liked to have seen those mounted flat or mounted on a small

**Dave Jones:** heat sink or somehow rigidly retained cuz they've done a really good job on all the other Loctite in the nuts and the connectors səlastic in those down and things like that. So, I'm always a little bit weary of that, but it's a very minor point.

**Dave Jones:** We've got our main processor here. It's a small one, tiny little microcontroller of some sort and boohoo, they've rubbed the number off. Why? Come on, people. Really? Is it that important that you got to rub the number off that chip and that chip only? Give me a break. Anyway, there's the main oscillator crystal.

**Dave Jones:** We've got another 32 kHz watch crystal over here. Once again, that one's səlastic down instead of the more usual soldering down. And here I am trying out my new 10x Opteka macro lens I've got for my Canon HFG10 camera and this is working really well and you can see the gouges taken out of the main processor there.

**Dave Jones:** They've really ground that out. They haven't, you know, they've really got in there with like a Dremel or something and really dug that out. And there's a 24LC64 E-squared prom that would hold the calibration values, one would presume.

**Dave Jones:** And there's a whole bunch of 07 precision op amps around this thing. They're all over the shop here. These op 07s there's like seven, eight, nine of them. So, no surprises there. They're the industry standard precision op amp. And there's an AD 7708 and that's a 16-bit delta sigma ADC. No surprises at all. Built-in programmable gain amp. And the reason you need a 16-bit converter in this thing is because it's got a 1 mV resolution in an 18 V range. That's one part in 18,000 and

**Dave Jones:** to do that, you could probably get away with a 15-bit converter, but they don't make those as well. So, they use a 16-bit converter, which is one part in 65,000. So, it's ideally matched and down here we have a Burr-Brown. Love Burr-Brown parts, which are now TI of course, but that's a DAC 7631 and that's a matching pretty much a matching 16-bit voltage output DAC. And there's a voltage reference for the ADC and the DAC could be shared between them. It's the ADR421 that and that's like a better than 0.05%

**Dave Jones:** class voltage reference with three ppm temp co. Very nice. And that's something a lot of people forget with precision designs like these. You don't necessarily need absolute precision components. You just need low temperature coefficient or you know, highly temperature stable components and then you can take care of the rest with software calibration. So, it's you know, you can get a really precise instrumentation by using a 1% voltage reference for example, but as long as it has a very low temp co, then you can take care of that with software

**Dave Jones:** calibration. Now, I love how in this section down here they're TL074 quad op amps and they're in old style DIP package and there's a LM324 and it's in an SO package. So, that's just really just quite strange how they've actually got those in a DIP package and look at those passives surrounding that. They're quite spread out with the traces going a long way. I just wonder why they've done that. And as you can see also, we've got a whole bunch of these um RX21 series uh silicon resin

**Dave Jones:** coated uh 8-W power resistors in there. And they're available with uh 1% uh tolerance values and about uh 250 ppm, I believe. And the big MOSFET we've got on here is an IRFP250, and it's quite uh hard to get the camera in there, but there you go. There's a couple of There's um quite a few of these devices scattered around the heat sinks to spread the load. And they're 30-A 200-V MOSFETs, and you can see uh a couple over here.

**Dave Jones:** You can see another couple up there, as well. So, that's four, but if you look down the side of the heat sinks, they've got another one and two there. So, uh they've got a total of four uh MOSFETs per side here.

**Dave Jones:** So, a total of eight um of those huge power MOSFETs. That's to um share That's where all of most of your load gets uh dissipated into these MOSFETs and through to these large heat sinks here. There's a little bit in your uh current shunts and uh things like that, but uh most of your power most of that 300-W capability is going to be delivered into these large heat sinks, and the fans are going to suck the air in from the side here, suck it through the fins, and take

**Dave Jones:** it out the back. And as you can see, there's a whole bunch of factory tests it passed in each uh stage through the production uh testing. It gets a little sticker on it. Calibrated and it's done all the calibration and the trim pots, and they've tweaked it um because this, as I said, is a precision instrument. Very important process to calibrate it. Then they would have done the uh high-voltage test. It would have um some sort of uh burning test. I don't know. They might run it at full load for

**Dave Jones:** 24 hours or something like that. May possibly in a thermal chamber to see if it um you know, at an elevated uh ambient temperature to see if it keels over or something like that. Um PRT, test, I'm not sure exactly what that is.

**Dave Jones:** That's PRT is usually a production readiness test, but I think it could be like a a high pot mains compliance test or something like that. And ICT is probably in circuit test as well. So ultimately what that means is that when you buy this thing, you can be pretty darn sure that it's going to function correctly out of the box and continue to function correctly because it's had that burning. And that's what you're paying for for these quality bits of instrument from a proper manufacturer that uh specifically

**Dave Jones:** develops equipment like this. And there'll be a few people who are just keen to see what's on the back. I see input connector fused 220 110 volt selection. We've got a serial control interface. And my unit came with isolated, by the way, completely isolated RS232 and USB B cables, very nice. And it comes with remote sense spring terminals as well. You can just get in there and push your wire in and trigger input as well. Very nice. And there's not much doing on the front display

**Dave Jones:** board up here with the soft button keys and the vacuum fluorescent display apart from the two vacuum fluorescent display driver chips. They're they're a PT6315 and that's a serial input vacuum fluorescent display driver. And there's two of those and it is a very nice display and they've got that of course interfacing with the ribbon cable over here going down to the microcontroller.

**Dave Jones:** And there's a teensy bit of circuitry there for the very nice rotary encoder knob and a buzzer to make some sound at you. Beep. And I forgot to mention a couple of other mobs scattered around the place. And they've got another couple of devices connected to the heat sink here is well a uh three-pin TO220 and a bridge rectifier uh down in here as well connected to this side of the heat sink. So, as you can see, there's not a huge amount inside these electronic loads. There's a

**Dave Jones:** microprocessor to control it all. There's a DAC and an ADC to uh not only uh set the value required, but read it back. And there's a um a a MOSFET or a bunch of MOSFETs with some load resistors. And that's, you know, pretty much the basic operation of any DC electronic load. Except this one is uh really nice cuz it's high precision.

**Dave Jones:** And I really do like how it's nice one bit big solid bit of folded uh sheet steel which goes right over the top like that. It really works on the bottom. Sorry, this is the bottom of the unit. It really is quite nice.

**Dave Jones:** Everything uses uh shake-proof uh washers on there. And uh by the way, in case you're wondering, there is no circuitry on the bottom. So, there's no advantage to uh taking that part anymore, but doesn't it look really schmick?

**Dave Jones:** And I couldn't really uh fault the design or build quality in this thing. It uh it it's certainly uh first class and I would certainly give it a big thumbs up. So, there you have it. That's inside the BK Precision 8500 precision DC electronic load. If you're into power supply design, um I highly recommend you pick one up. This this isn't a review, but uh people want to know the price. Street pri- um sorry, uh recommended price is about 1,100 bucks for this particular model. Street price

**Dave Jones:** is around about 900 bucks or lower or you know, even substantially lower than that depending on where you get it from. And uh this is actually the IT8512 is equivalent to the BK Precision 8500, but there's like a dozen different models. This is the 120 V 30 A 300 W version, but they're available in different voltages and currents and power ratings. So, thanks to BK Precision for this. It'll be a very handy bit of kit and you'll no doubt um see it uh coming up when I do some more

**Dave Jones:** uh videos on the uh power supply design stuff cuz this is fantastic for testing any sorts of power supplies, switch mode, linear, it can do uh pulse loads as well. You can set it up and it can do battery discharge uh testing as well under PC control.

**Dave Jones:** Fantastic, very useful bit of kit. And remember, if you like uh teardown Tuesday, please give it a thumbs up cuz that helps a lot. And if you want to discuss this, jump on over to the EEVblog forum. Catch you next time.
