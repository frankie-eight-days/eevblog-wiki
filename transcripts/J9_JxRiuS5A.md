---
video_id: J9_JxRiuS5A
title: Tektronix MDO4000 Oscilloscope Teardown - EEVblog #199
url: https://www.youtube.com/watch?v=J9_JxRiuS5A
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 40, "3": 54, "4": 92, "5": 107, "6": 125, "7": 145, "8": 161, "9": 173, "10": 185, "11": 199, "12": 213, "13": 227, "14": 241, "15": 256, "16": 274, "17": 294, "18": 307, "19": 322, "20": 340, "21": 357, "22": 370, "23": 387, "24": 403, "25": 420, "26": 434, "27": 449, "28": 465, "29": 479, "30": 493, "31": 507, "32": 521, "33": 533, "34": 571, "35": 586, "36": 599, "37": 619, "38": 637, "39": 655, "40": 671, "41": 687, "42": 700, "43": 712, "44": 732, "45": 757, "46": 782, "47": 824, "48": 848, "49": 860, "50": 877, "51": 894, "52": 924, "53": 939, "54": 961, "55": 976, "56": 991, "57": 1003, "58": 1022, "59": 1040, "60": 1059, "61": 1072, "62": 1085, "63": 1101, "64": 1122, "65": 1191, "66": 1203, "67": 1217, "68": 1343}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. 30,000 bucks worth of brand new Tektronix MDO4000 series oscilloscope. You know what we say here on the

**Dave Jones:** EEVblog, don't turn it on, take it apart. That back case came off incredibly easily and here's the um uh flip out feet mechanism. They just use a uh metal lever bar there and that works quite well. I like it. And I got to admit, I'm

**Dave Jones:** very impressed with the uh metal shielding on there, just like in the Agilent ones. It's beautiful. I like it and uh you can see the power supply. Well, there's some uh here is a huge metal black metal heat sink down in

**Dave Jones:** there. The massive uh fan on the back here, which we'll look at and uh very well shielded. I like it. It looks pretty easy to take apart with some uh torques screws, so let's give it a go.

**Dave Jones:** And there it is. That came apart relatively easily. Quite a few uh torque screws and a few uh jack nuts and uh and the BNC nuts, but uh apart from that, it's uh it came apart fairly smoothly. I was

**Dave Jones:** quite impressed. Now, there's actually quite a few rather interesting aspects to the building this thing. I think it's rather interesting. Let's take a closer look. One of the first things I noticed is the is the arrangement here of these clamp

**Dave Jones:** downs bars for the various heat sinks here. There's each heat sink has got one. So they except the ones under the bottom here which are on a lower board down there and they're they're rather interesting. They haven't just gone for the thermal easy.

**Dave Jones:** They've actually gone for these these bars. So I'm prodding the that yellow stuff under there and it's it's thermal paste or maybe even thermal adhesive. I don't know what they've used there but presumably if we try and take

**Dave Jones:** off those heat sinks, I don't think we're going to be able to see the chip numbers under there and they're custom anyway. So I don't think I'll I'll bother to do that but yeah, it's just rather interesting that they've gone to

**Dave Jones:** that much effort to hold them on there. Now if we take a look at the power supply here, of course it's a top quality one. It's from Emerson Networks. You can see that right up in the top in

**Dave Jones:** there and it's they're doing all the right things. It's a high quality power supply as you'd expect. And for the main supply output here, they soldered those directly onto the board with multiple cables. So they're not marking around

**Dave Jones:** there. They haven't bothered using a connector. Really solid connection. There's a connection down on the main board of course and there's a smaller one up here. That's probably for some auxiliary voltage or some power monitoring or something like that. As

**Dave Jones:** with the Agilent, there's got to be a feedback button to from the soft start circuit to switch this power supply off and on or at least switch the output off and on anyway. And they've dispensed with that mounting

**Dave Jones:** hardware here of course. They're just using some thermal pads here to attach it to the back heat sink here and same on the top side as well. I find this very curious indeed. There's a second board up in here which we'll take a look

**Dave Jones:** at and it's got the all the rear panel connectors, but look at this little connector here. It's got two leads coming out which then go down into the active and the neutral. They're actually heat shrunk into They're actually put inside the

**Dave Jones:** heat shrink and then they go down the active and neutral and then they actually terminate just here. So they're like a sense to pick up the mains frequency. Is is that for the mains sync? I I wonder what the mains trigger or

**Dave Jones:** something like that perhaps. I don't know. It's very interesting. And curiously they've got this PCI connector down on the main board down there and it actually connects into the rear panel connector board up there and it's got the ethernet and the VGA and

**Dave Jones:** the auxiliary coax outputs and the USB and stuff like that and it's got the USB on the front and the back. You can actually see the ones on the on the front panel here and they connect through to the

**Dave Jones:** same ones on the back. That's quite a novel technique to actually get board like those USB ones. I would have expected them to just mount them on the main board so that they protrude out the front, but I guess they decided to

**Dave Jones:** consolidate it into the same chipset and once again the shielding's taken care of with these little spring shield clips down in here. So when you press the two halves of the case together, the shielding meets and makes a good contact and that's how you get

**Dave Jones:** get good EMC immunity. And down in this corner here my guess would be that is a JTAG connector. You know, dual row, 10 pins. I reckon that's it. Hack away. And there's some sort of switch there, probably some sort

**Dave Jones:** of reset switch. And obviously all of the DC-to-DC converter stuff for the lower rails is all done on the main board here. This is huge heat sink. There's probably some voltage regulators on the bottom side of the board there.

**Dave Jones:** There's lots of ton of large inductors there and filter caps. So, yeah, that's a dead giveaway. And that circuitry there is obviously for the logic analyzer, dead giveaway. And from the logic analyzer circuitry there, you can see the controlled

**Dave Jones:** impedance traces going up to the main device up here with that SDRAM surrounding it. But curiously, that's the only major device on the board which doesn't have a heat sink on it. So, obviously it's it doesn't get that hot.

**Dave Jones:** It's obviously a cool processor or isn't running that quick. And that's a tech custom one made by National Semiconductor. And my guess would be this one here is the main processor that sort of runs all the operating system and everything

**Dave Jones:** because it looks like all the back panel interface devices with the USB and everything all flow into that. So, I wonder what what they're actually running there. I don't know. I'd have to take the heat sink off to find out, but that's a bit

**Dave Jones:** hard. So, we'll have to wait until Tektronix tell us or live in wonder. And those two labeled firmware flash devices are a dead giveaway. They're right next to the applications processor there. And that huge device up the top there,

**Dave Jones:** that's pretty much the biggest device on the board. It's the big daddy and it seems to tie into all those other ASICs on the left hand side of it. And here we have our six devices which are clearly uh separated into

**Dave Jones:** uh basically uh two channels. That's why we um found that effect when when we actually reviewed it. We uh saw that if you switch on more than two channels, then it uh it's um update uh performance actually uh halves. So,

**Dave Jones:** um uh there's obviously uh two devices uh three devices per two channels. Um there's I don't know one's probably I'm not sure if they're the ADC on top because I'm tempted to think that the ADCs down on the bottom board and that's

**Dave Jones:** what those heat sinks down those four heat sinks down the bottom which actually protrude through the top board. They're mounted down on the bottom board. So, I suspect uh they're probably the analog to digital uh converters and down in here that package down in there

**Dave Jones:** is uh the main 10 MHz uh reference oscillator and that's uh done by Fox um and they're a you know a big manufacturer of high quality um high stability in this case. It'll be a very high stability one. Uh you know, very

**Dave Jones:** low jitter, that sort of thing. So, uh you obviously need that when you're talking about uh these sort of um sample rates. And up the top here it looks like we've got some uh Micron brand what looks like

**Dave Jones:** uh memory. I I can only assume uh the number is uh not familiar at all. So, uh but they are um obviously coupled into these uh heat sunk uh ASICs up here. So, uh presumably sample memory?

**Dave Jones:** And there's the bottom of the main uh board. Now, there's a uh there's some more um of Micron memory down the bottom here. Another buttload of that. And I thought there was a device on this soldered onto this side of the board,

**Dave Jones:** another BGA device, but that isn't populated. Um as the same with the surrounding components there. There's nothing on the top side, no components, no BGA device. So, I wonder what that one is. I don't know. There's the rest

**Dave Jones:** of your logic analyzer circuitry and there's your logic analyzer um input input connector on the front panel. There's some extra SD RAM around here. And really there's not a huge amount else. And there's the backside of all your DC-to-DC converter

**Dave Jones:** circuitry under that heatsink. And you can see the three screws on there that screw the heatsink onto the front of the board. And the USB controller is actually on that back board there. It's a SMSC USB 2514. There you go. So, it wasn't actually on

**Dave Jones:** the front. And that's a rather interesting board. It's a rather unusual construction. And there is a There's a battery on there. There's a lithium battery for the time and date. And the fan is an absolute monster. It's a Sanyo Denki one. So, they haven't

**Dave Jones:** skimped there on the brand. But overall, the cooling's not bad on this. What the fan does is it actually sucks air in from the outside. It sucks it in, which then the only way out is to pass across the power supply and the top

**Dave Jones:** of the main board, which will be facing down in here as well. And all the that big black DC-to-DC converter heatsink we saw. And out the cage here. So, that's not a bad thermal design at all. And I was right on the money with those

**Dave Jones:** heatsinks which protrude through to the top side of the board. They're obviously the analog-to-digital uh If you look closely in there, you can see the uh control impedance uh traces coming out of them to these high-speed connectors, which actually connect

**Dave Jones:** through to the top side of the board. And of course, they're our um they're our front ends, our vertical uh front ends under the shielded uh cans. And they're uh soldered down to the board. So, unfortunately, we won't be

**Dave Jones:** able to uh take those off today. And curiously, over here we have um a connector which goes nowhere. That's obviously for uh testing, programming, diagnostic purposes, whatever. And of course, all of the magic, the new RF magic happens under this huge uh

**Dave Jones:** shielded um custom uh diecast metal box. Awesome. And for fans of power supplies, here it is.

**Dave Jones:** And here's the back board in closer detail. As you can see those wires coming off that connector and going down into the mains, wiring like that, and then just terminating right there on the end of the um just before the connector.

**Dave Jones:** And let's have a pan over the bottom side of the main board. Board here looks like a JTAG once again a 5x2 and the date code 20th week 2011.

**Dave Jones:** And behold there it is. We have the bottom of the ADC board. And you'll notice the serpentine controlled impedance traces running around here like crazy. We have a rather curious device here that obviously has some firmware on it.

**Dave Jones:** That's the only reason that it'd have that sticker. I wonder what it is. And let's go for a tour of the backside of our ADC with our BNCs already screwed into there. I won't bother taking those out. There'll be nothing of

**Dave Jones:** note under there. And we have that device which is obviously programmable. Maybe some sort of micro or something. I don't know. There are the backside of the BGAs for the four channel analog to digital converter. There's four separate

**Dave Jones:** devices. That looks like some sort of localized power supply for the ADC. Probably a low noise supply. What else have we got? Not sure what that sort of stuff is there. Just some miscellaneous Oh, there's obviously a espresso oscillator

**Dave Jones:** there. So maybe that's some sort of local oscillator. And we've got a magic can there. There's obviously some real black magic going on under that and some other miscellaneous stuff. Let's see if we can take off the RF shield.

**Dave Jones:** Oh, here we go. This is exciting stuff. This will be pornographic. What's under here? Oh, you don't do a big die solid die cast metal thing like this on on an RF spectrum analyzer without having some magic under here. Let's lift

**Dave Jones:** the skirt up. Tada! Oh, beautiful. Oh, this sort of stuff just brings a tear to the eye. Real RF engineering, it's just a thing of beauty and a joy forever. Oh. I'm not an RF guy, so I won't even begin

**Dave Jones:** to explain what's going on here cuz I'd probably be talking out my ass really. There's a a high filter here and a low filter. Everything on here by the way you see is a transmission line. This is serious

**Dave Jones:** business. All right, this is absolutely serious. Let's start with the RF connector up here. I mean, that is some dodgy looking soldering. I'm not too impressed with that. I mean, granted it's onto a big whopping ground plane and it's a big N

**Dave Jones:** connector, but I don't know. I expected a bit better than that, but I guess it's good enough.

**Dave Jones:** And the connector leads down into this off-the-shelf can device. I don't recognize the manufacturer there. It's probably a manufacturer of precision RF components and there's not much else surrounding that. And that leads down into these devices down here which then

**Dave Jones:** are uh cascaded like that all the way through down to this bottom circuitry. And here it is. It brings us in and this is a little that there as you can see. Some sort of chip, I don't know, some sort of uh passive

**Dave Jones:** components surrounding it. And then the output of that branches off up here and then splits into your high and your low filter there, which then go across into here. Oh, it's like a little mini racetrack. It's brilliant. And it also

**Dave Jones:** splits off down here, which goes all the way over, all the way over, all the way over through some circuitry there. All the way over to more circuitry over there and then it splits again and goes all around. Ah,

**Dave Jones:** try and follow this baby. Love to see the schematic. I guess the RF fans and all the hams out there are drooling themselves right about now. When it comes out of there, it goes up here and it goes into

**Dave Jones:** this ferrite surrounded some sort of I don't know, is it some sort of delay line, wave guide? I don't know. I have no idea what that is. Some sort of transformer? Who knows? I got no idea. RF experts will tell me and uh

**Dave Jones:** tell me how obvious all this circuitry is. One thing I do know though, it's just beautiful. It really is. Oh. And of course, you're not going to get crosstalk with anything with this custom-designed huge die-cast shield with all of the traces, all the

**Dave Jones:** matching traces cut out of it. Beautiful. That's how you get zero crosstalk and zero interference on a in a good quality RF spectrum analyzer.

**Dave Jones:** And the can we saw on the top side of the board is for this device here which obviously has to have a cutout in the board so well you can't just let all the magic escape so you got

**Dave Jones:** to shield it on the other side with the can but apart from that everything else is shielded by the copper layers of the board and by the by the diecast shielding can. And you can bet your bottom dollar that

**Dave Jones:** ain't regular FR4 material either. Now the big test, will it actually boot? Let's see. It's going through the motions, it's making the noises, screen's working, but uh we're going to have to wait a minute and a half to find out. And look at that,

**Dave Jones:** works like a bought one. What were you worried about, Tektronix?
