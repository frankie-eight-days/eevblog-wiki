---
video_id: J9_JxRiuS5A
title: Tektronix MDO4000 Oscilloscope Teardown - EEVblog #199
url: https://www.youtube.com/watch?v=J9_JxRiuS5A
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 33, "3": 44, "4": 59, "5": 94, "6": 104, "7": 130, "8": 145, "9": 167, "10": 180, "11": 189, "12": 203, "13": 210, "14": 225, "15": 234, "16": 245, "17": 260, "18": 274, "19": 300, "20": 314, "21": 330, "22": 349, "23": 364, "24": 377, "25": 394, "26": 407, "27": 424, "28": 440, "29": 452, "30": 465, "31": 477, "32": 499, "33": 516, "34": 528, "35": 535, "36": 574, "37": 588, "38": 597, "39": 613, "40": 627, "41": 640, "42": 651, "43": 663, "44": 674, "45": 689, "46": 702, "47": 715, "48": 738, "49": 782, "50": 824, "51": 848, "52": 856, "53": 869, "54": 883, "55": 896, "56": 924, "57": 937, "58": 956, "59": 970, "60": 982, "61": 991, "62": 1017, "63": 1035, "64": 1053, "65": 1066, "66": 1081, "67": 1090, "68": 1105, "69": 1124, "70": 1207, "71": 1326, "72": 1341}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. 30,000 bucks worth of brand new Tektronix MDO4000 series oscilloscope.

**Dave Jones:** You know what we say here on the EEVblog, don't turn it on, take it apart. That back case came off incredibly easily and here's the um uh flip out feet mechanism.

**Dave Jones:** They just use a uh metal lever bar there and that works quite well. I like it. And I got to admit, I'm very impressed with the uh metal shielding on there, just like in the Agilent ones.

**Dave Jones:** It's beautiful. I like it and uh you can see the power supply. Well, there's some uh here is a huge metal black metal heat sink down in there. The massive uh fan on the back here, which we'll look at and uh very well shielded.

**Dave Jones:** I like it. It looks pretty easy to take apart with some uh torques screws, so let's give it a go. And there it is. That came apart relatively easily.

**Dave Jones:** Quite a few uh torque screws and a few uh jack nuts and uh and the BNC nuts, but uh apart from that, it's uh it came apart fairly smoothly.

**Dave Jones:** I was quite impressed. Now, there's actually quite a few rather interesting aspects to the building this thing. I think it's rather interesting. Let's take a closer look. One of the first things I noticed is the is the arrangement here of these clamp downs bars for the various heat sinks here.

**Dave Jones:** There's each heat sink has got one. So they except the ones under the bottom here which are on a lower board down there and they're they're rather interesting. They haven't just gone for the thermal easy.

**Dave Jones:** They've actually gone for these these bars. So I'm prodding the that yellow stuff under there and it's it's thermal paste or maybe even thermal adhesive. I don't know what they've used there but presumably if we try and take off those heat sinks, I don't think we're going to be able to see the chip numbers under there and they're custom anyway.

**Dave Jones:** So I don't think I'll I'll bother to do that but yeah, it's just rather interesting that they've gone to that much effort to hold them on there. Now if we take a look at the power supply here, of course it's a top quality one.

**Dave Jones:** It's from Emerson Networks. You can see that right up in the top in there and it's they're doing all the right things. It's a high quality power supply as you'd expect.

**Dave Jones:** And for the main supply output here, they soldered those directly onto the board with multiple cables. So they're not marking around there. They haven't bothered using a connector. Really solid connection.

**Dave Jones:** There's a connection down on the main board of course and there's a smaller one up here. That's probably for some auxiliary voltage or some power monitoring or something like that.

**Dave Jones:** As with the Agilent, there's got to be a feedback button to from the soft start circuit to switch this power supply off and on or at least switch the output off and on anyway.

**Dave Jones:** And they've dispensed with that mounting hardware here of course. They're just using some thermal pads here to attach it to the back heat sink here and same on the top side as well.

**Dave Jones:** I find this very curious indeed. There's a second board up in here which we'll take a look at and it's got the all the rear panel connectors, but look at this little connector here.

**Dave Jones:** It's got two leads coming out which then go down into the active and the neutral. They're actually heat shrunk into They're actually put inside the heat shrink and then they go down the active and neutral and then they actually terminate just here.

**Dave Jones:** So they're like a sense to pick up the mains frequency. Is is that for the mains sync? I I wonder what the mains trigger or something like that perhaps.

**Dave Jones:** I don't know. It's very interesting. And curiously they've got this PCI connector down on the main board down there and it actually connects into the rear panel connector board up there and it's got the ethernet and the VGA and the auxiliary coax outputs and the USB and stuff like that and it's got the USB on the front and the back.

**Dave Jones:** You can actually see the ones on the on the front panel here and they connect through to the same ones on the back. That's quite a novel technique to actually get board like those USB ones.

**Dave Jones:** I would have expected them to just mount them on the main board so that they protrude out the front, but I guess they decided to consolidate it into the same chipset and once again the shielding's taken care of with these little spring shield clips down in here.

**Dave Jones:** So when you press the two halves of the case together, the shielding meets and makes a good contact and that's how you get get good EMC immunity. And down in this corner here my guess would be that is a JTAG connector.

**Dave Jones:** You know, dual row, 10 pins. I reckon that's it. Hack away. And there's some sort of switch there, probably some sort of reset switch. And obviously all of the DC-to-DC converter stuff for the lower rails is all done on the main board here.

**Dave Jones:** This is huge heat sink. There's probably some voltage regulators on the bottom side of the board there. There's lots of ton of large inductors there and filter caps. So, yeah, that's a dead giveaway.

**Dave Jones:** And that circuitry there is obviously for the logic analyzer, dead giveaway. And from the logic analyzer circuitry there, you can see the controlled impedance traces going up to the main device up here with that SDRAM surrounding it.

**Dave Jones:** But curiously, that's the only major device on the board which doesn't have a heat sink on it. So, obviously it's it doesn't get that hot. It's obviously a cool processor or isn't running that quick.

**Dave Jones:** And that's a tech custom one made by National Semiconductor. And my guess would be this one here is the main processor that sort of runs all the operating system and everything because it looks like all the back panel interface devices with the USB and everything all flow into that.

**Dave Jones:** So, I wonder what what they're actually running there. I don't know. I'd have to take the heat sink off to find out, but that's a bit hard. So, we'll have to wait until Tektronix tell us or live in wonder.

**Dave Jones:** And those two labeled firmware flash devices are a dead giveaway. They're right next to the applications processor there. And that huge device up the top there, that's pretty much the biggest device on the board.

**Dave Jones:** It's the big daddy and it seems to tie into all those other ASICs on the left hand side of it. And here we have our six devices which are clearly uh separated into uh basically uh two channels.

**Dave Jones:** That's why we um found that effect when when we actually reviewed it. We uh saw that if you switch on more than two channels, then it uh it's um update uh performance actually uh halves.

**Dave Jones:** So, um uh there's obviously uh two devices uh three devices per two channels. Um there's I don't know one's probably I'm not sure if they're the ADC on top because I'm tempted to think that the ADCs down on the bottom board and that's what those heat sinks down those four heat sinks down the bottom which actually protrude through the top board.

**Dave Jones:** They're mounted down on the bottom board. So, I suspect uh they're probably the analog to digital uh converters and down in here that package down in there is uh the main 10 MHz uh reference oscillator and that's uh done by Fox um and they're a you know a big manufacturer of high quality um high stability in this case.

**Dave Jones:** It'll be a very high stability one. Uh you know, very low jitter, that sort of thing. So, uh you obviously need that when you're talking about uh these sort of um sample rates.

**Dave Jones:** And up the top here it looks like we've got some uh Micron brand what looks like uh memory. I I can only assume uh the number is uh not familiar at all.

**Dave Jones:** So, uh but they are um obviously coupled into these uh heat sunk uh ASICs up here. So, uh presumably sample memory? And there's the bottom of the main uh board.

**Dave Jones:** Now, there's a uh there's some more um of Micron memory down the bottom here. Another buttload of that. And I thought there was a device on this soldered onto this side of the board, another BGA device, but that isn't populated.

**Dave Jones:** Um as the same with the surrounding components there. There's nothing on the top side, no components, no BGA device. So, I wonder what that one is. I don't know.

**Dave Jones:** There's the rest of your logic analyzer circuitry and there's your logic analyzer um input input connector on the front panel. There's some extra SD RAM around here. And really there's not a huge amount else.

**Dave Jones:** And there's the backside of all your DC-to-DC converter circuitry under that heatsink. And you can see the three screws on there that screw the heatsink onto the front of the board.

**Dave Jones:** And the USB controller is actually on that back board there. It's a SMSC USB 2514. There you go. So, it wasn't actually on the front. And that's a rather interesting board.

**Dave Jones:** It's a rather unusual construction. And there is a There's a battery on there. There's a lithium battery for the time and date. And the fan is an absolute monster.

**Dave Jones:** It's a Sanyo Denki one. So, they haven't skimped there on the brand. But overall, the cooling's not bad on this. What the fan does is it actually sucks air in from the outside.

**Dave Jones:** It sucks it in, which then the only way out is to pass across the power supply and the top of the main board, which will be facing down in here as well.

**Dave Jones:** And all the that big black DC-to-DC converter heatsink we saw. And out the cage here. So, that's not a bad thermal design at all. And I was right on the money with those heatsinks which protrude through to the top side of the board.

**Dave Jones:** They're obviously the analog-to-digital uh If you look closely in there, you can see the uh control impedance uh traces coming out of them to these high-speed connectors, which actually connect through to the top side of the board.

**Dave Jones:** And of course, they're our um they're our front ends, our vertical uh front ends under the shielded uh cans. And they're uh soldered down to the board. So, unfortunately, we won't be able to uh take those off today.

**Dave Jones:** And curiously, over here we have um a connector which goes nowhere. That's obviously for uh testing, programming, diagnostic purposes, whatever. And of course, all of the magic, the new RF magic happens under this huge uh shielded um custom uh diecast metal box.

**Dave Jones:** Awesome. And for fans of power supplies, here it is. And here's the back board in closer detail. As you can see those wires coming off that connector and going down into the mains, wiring like that, and then just terminating right there on the end of the um just before the connector.

**Dave Jones:** And let's have a pan over the bottom side of the main board. Board here looks like a JTAG once again a 5x2 and the date code 20th week 2011.

**Dave Jones:** And behold there it is. We have the bottom of the ADC board. And you'll notice the serpentine controlled impedance traces running around here like crazy. We have a rather curious device here that obviously has some firmware on it.

**Dave Jones:** That's the only reason that it'd have that sticker. I wonder what it is. And let's go for a tour of the backside of our ADC with our BNCs already screwed into there.

**Dave Jones:** I won't bother taking those out. There'll be nothing of note under there. And we have that device which is obviously programmable. Maybe some sort of micro or something. I don't know.

**Dave Jones:** There are the backside of the BGAs for the four channel analog to digital converter. There's four separate devices. That looks like some sort of localized power supply for the ADC.

**Dave Jones:** Probably a low noise supply. What else have we got? Not sure what that sort of stuff is there. Just some miscellaneous Oh, there's obviously a espresso oscillator there. So maybe that's some sort of local oscillator.

**Dave Jones:** And we've got a magic can there. There's obviously some real black magic going on under that and some other miscellaneous stuff. Let's see if we can take off the RF shield.

**Dave Jones:** Oh, here we go. This is exciting stuff. This will be pornographic. What's under here? Oh, you don't do a big die solid die cast metal thing like this on on an RF spectrum analyzer without having some magic under here.

**Dave Jones:** Let's lift the skirt up. Tada! Oh, beautiful. Oh, this sort of stuff just brings a tear to the eye. Real RF engineering, it's just a thing of beauty and a joy forever.

**Dave Jones:** Oh. I'm not an RF guy, so I won't even begin to explain what's going on here cuz I'd probably be talking out my ass really. There's a a high filter here and a low filter.

**Dave Jones:** Everything on here by the way you see is a transmission line. This is serious business. All right, this is absolutely serious. Let's start with the RF connector up here.

**Dave Jones:** I mean, that is some dodgy looking soldering. I'm not too impressed with that. I mean, granted it's onto a big whopping ground plane and it's a big N connector, but I don't know.

**Dave Jones:** I expected a bit better than that, but I guess it's good enough. And the connector leads down into this off-the-shelf can device. I don't recognize the manufacturer there. It's probably a manufacturer of precision RF components and there's not much else surrounding that.

**Dave Jones:** And that leads down into these devices down here which then are uh cascaded like that all the way through down to this bottom circuitry. And here it is. It brings us in and this is a little that there as you can see.

**Dave Jones:** Some sort of chip, I don't know, some sort of uh passive components surrounding it. And then the output of that branches off up here and then splits into your high and your low filter there, which then go across into here.

**Dave Jones:** Oh, it's like a little mini racetrack. It's brilliant. And it also splits off down here, which goes all the way over, all the way over, all the way over through some circuitry there.

**Dave Jones:** All the way over to more circuitry over there and then it splits again and goes all around. Ah, try and follow this baby. Love to see the schematic. I guess the RF fans and all the hams out there are drooling themselves right about now.

**Dave Jones:** When it comes out of there, it goes up here and it goes into this ferrite surrounded some sort of I don't know, is it some sort of delay line, wave guide?

**Dave Jones:** I don't know. I have no idea what that is. Some sort of transformer? Who knows? I got no idea. RF experts will tell me and uh tell me how obvious all this circuitry is.

**Dave Jones:** One thing I do know though, it's just beautiful. It really is. Oh. And of course, you're not going to get crosstalk with anything with this custom-designed huge die-cast shield with all of the traces, all the matching traces cut out of it.

**Dave Jones:** Beautiful. That's how you get zero crosstalk and zero interference on a in a good quality RF spectrum analyzer. And the can we saw on the top side of the board is for this device here which obviously has to have a cutout in the board so well you can't just let all the magic escape so you got to shield it on the other side with the can but apart from that everything else

**Dave Jones:** is shielded by the copper layers of the board and by the by the diecast shielding can. And you can bet your bottom dollar that ain't regular FR4 material either.

**Dave Jones:** Now the big test, will it actually boot? Let's see. It's going through the motions, it's making the noises, screen's working, but uh we're going to have to wait a minute and a half to find out.

**Dave Jones:** And look at that, works like a bought one. What were you worried about, Tektronix?
