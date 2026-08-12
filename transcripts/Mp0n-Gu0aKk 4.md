---
video_id: Mp0n-Gu0aKk
title: EEVblog #234 - Agilent U1733C LCR Meter Teardown
url: https://www.youtube.com/watch?v=Mp0n-Gu0aKk
source: youtube-asr
timestamps: {"0": 0, "1": 35, "2": 52, "3": 82, "4": 117, "5": 141, "6": 159, "7": 186, "8": 217, "9": 244, "10": 258, "11": 288, "12": 318, "13": 345, "14": 380, "15": 420, "16": 458, "17": 475, "18": 496, "19": 527, "20": 554, "21": 589, "22": 625, "23": 654, "24": 691, "25": 709, "26": 739, "27": 755, "28": 781, "29": 792, "30": 822, "31": 842}
---

**Dave Jones:** Hi, it's another teardown. Yes, it's another LCR meter. We love them. This time it's the Agilent U1733C. It's the new C model as opposed to the B model which I just happen to have. So, we'll do a side-by-side teardown comparison. You beauty. And the B was the original Escort design when the Agilent bought out the Escort design group. That became their handheld instruments division or something like that. And this was the old traditional Escort design. So, it'll have Escort branded I think an Escort custom device in there under many sold under

**Dave Jones:** many different names. But they decided Agilent not they'll redesign it themselves. It looks identical but I've been told that the new C model is the proper Agilent handheld test group design from the ground up. So, we'll see what the differences are.

**Dave Jones:** Let's go. And you know what we say, don't turn it on, take them apart. Now, as you can see they've stuck with the same case design. And the B model was redesigned with the new orange case as you know, the new Agilent stuff is all the fancy orange which I rather like actually. And the new C, they haven't really changed the look at all. It's pretty much an identical case. They've kept the same molding by the looks of it. It's got the same CE markings molded into it. So, they

**Dave Jones:** haven't really changed that changed that design at all. But the interface has changed a little bit because this is a more functional instrument with more ranges of frequency ranges and functions and stuff. So, they've got some extra stuff on the keys there. But apart from that, well, you can't tell the difference. But I think we might see a big difference when we crack these things open. So, let's do it.

**Dave Jones:** And on the battery holder here, that's actually one of the screws. There's two screws up the top there are self-tappers, uh rather unfortunately, but of course you never have to take these things apart really. Um but there is a metal uh threaded insert for the battery holder, which is nice because LCR meters don't have a huge battery life like uh like you know your multimeter might have 2 300 hours or something like that.

**Dave Jones:** These things have 20 or 30 hours uh battery life, so you often got to change them. Would have been nice if they used uh double A's or something like that, which would have gave which would have given greater capacity, but they've stuck with the 9-V versions. Anyway, let's uh take it open. This is the C model.

**Dave Jones:** And uh whoop. There we go. No extra turn on the screw required. There we go. Ta-da. Whoop. Ta-da. Beautiful. Ho, it's it's feature-packed. So, that's the new C model down here and well, let's crack open the B model and the older one and see what the differences are.

**Dave Jones:** Uh uh well, some. Now, what we've got is the new C model on the bottom and the older B model on the top and clearly they've taken the existing design and use that as a reference and just uh uh changed some uh things around it because a lot of the uh components and even the layout is uh is quite sort of similar between the two, but uh clearly they've um you know, they've changed a few things. The uh processor looks like it's changed, we'll take a look at that. Um

**Dave Jones:** the ADC which they had up here before in this big um SO package is gone, probably replaced by this device here. They've changed the uh buzzer there to a different type. They've changed the input protection. We have a um RF uh bead here for uh that looks like uh for the DC input down there. That's a DC input circuitry. They've added that just for some RFI. The input protection is uh different. We'll go into that uh later.

**Dave Jones:** It looks a lot better on the newer one. The older one up the top had a glass uh M205 fuse up here, whereas the new one has uh PTCs and uh poly switches and um it looks like some moves there or something like that diode protection.

**Dave Jones:** So, as a as a fair few differences, but you know, there there is quite a lot of um old school uh analog circuitry on there. It's very uh traditional LCR meter uh layout. They really haven't started the design uh completely from the ground up and go, "Right, we're going to fully integrate all of this and do some custom ASIC." They've just used, you know, 74 series logic and analog switches and pretty uh old school LCR meter design, but there's nothing wrong with that. They've also done away with

**Dave Jones:** the uh sampling caps up here. Look at those. They're big through hole uh caps there and they've they've really completely done away with these on the new boards. Look at the size of that monster. And uh yeah, they're completely gone. They've got a um in-circuit uh programming header up here. That's like most likely a uh JTAG in-circuit uh programming interface for the uh micro, so you could uh read that out, hack it, do whatever. Um and well, you know, apart from that, there's not a huge um you know, I

**Dave Jones:** expected to see um fairly dramatic uh differences, but I just see, you know, sort of a minor second second design kind of thing based on the first one, but I guess that makes sense. If your existing design worked, uh you don't want to tweak it too much. You just want extra precision, maybe extra frequency range, put in a few more modern uh components, things like that, but apart from that, there's uh not too many differences. Little test points are still the same.

**Dave Jones:** Oh, gee, I don't know. I'm struggling. Ah, another thing, looks like there's a dual IR transmit and receive interface, whereas the old one was only transmit. You can only transmit data out of it. This one can receive, probably because you can do maybe firmware updates through the RS232 port or something like that. Now, let's start at the DC jack on the new design down here. There it is, the external DC input. All of this stuff around here would be to do with that DC input. They've added the RFI ferrite

**Dave Jones:** bead here for some noise suppression on this thing, probably to help it pass CE compliance. They've got some diode protection here. They've got Looks like there's another power diode in there, and they've got some resettable fuses here as opposed to the glass fuses. So, really, you know, they've changed that a significant amount compared to the existing one, which was reasonably old-school and not much in terms of, you know, modern overload protection and stuff like that. And we are looking at a rev one PCB here, rev 001. I don't know.

**Dave Jones:** Are they expecting a lot? And they've really beefed up the input protection on this thing. They've got no less than now four PTC poly switches in there. And curiously, they've got three of these glass devices. They're some sort of I don't know. What are they? Some sort of spark gap input protection device, surge protection device, or something like that. So, they've added quite a bit compared to the old B design, which has the old M205 glass fuse, really old-school stuff. There's one poly switch down there. And well, that's

**Dave Jones:** about it. There's a couple of diodes in there as well. They've also got those Some of those on the new design. Have they? No, they're part of the battery input external DC input circuitry, but yeah, really input protection they've they've pretty much gone to town there.

**Dave Jones:** And they've kept the same single wire blade banana terminal system soldered directly onto the PCB down there on one side of the blade. I don't you know, I've mentioned this before. I don't particularly like this design, but you know, it's okay. It's not my favorite there. That's the B model up the top and they they really haven't changed at all.

**Dave Jones:** The reason I don't like it is because one side of the blade there effectively is fixed and it doesn't spring and then any every time you plug something in you're you're putting a little bit of force probably on that solder joint. So, it's probably not the best from a long-term design aspect point of view, but presumably they've tested it, but yeah, I don't know. It's just not as good as some other implementations I've seen where the blade where the blades are soldered directly into the PCB down the bottom at multiple

**Dave Jones:** locations like that. I think just there's a little bit of force extra force being exerted on that solder joint there. It probably would have been nice to actually solder it on the other side of the board. So, then it it wouldn't actually be on the bottom side of the board, it'd be on the top side. So, when you push down on it, it would push down on the board. So, there's some physical retention there as opposed to just the solder joint. Anyway, and of course they're stuck with the

**Dave Jones:** same battery system PCB mount 9-volt batteries and I love that. There's just no wiring inside this unit. Beautiful. That's how it should be. I'm not sure if the processor has changed, but as you can see it's a 78F0485, whereas the original design had an escort branded uh, chip in there. It was actually Escort. Whether or not it's the same device and Escort were just getting them to label it, uh, different, I don't know. But, uh, yeah, it's, um, it's seems to have changed, anyway. And the

**Dave Jones:** main ADC in the new design is the, uh, ADS1243. It's a 24-bit, uh, eight-channel, um, delta-sigma ADC. It's got, you know, a built-in PGA, uh, with a gain of 128. And it's got, you know, 50-60 hertz uh, notch filters in it. So, uh, it's very capable. And a, uh, but a fairly, uh, substantial step up from the, um, from the TLC7135, which they used in the old design, which is a, uh, triton board traditional, uh, dual slope, uh, four and a half digit, um, integrating ADC, which is just over,

**Dave Jones:** uh, 14 bits, you know, 20,000 count resolution, something like that. So, uh, they really have stepped up the ADC in this thing. Okay, we'll just go through some of the devices they've got on here. There's really, uh, no surprises, uh, at all. That's a HC74HC, uh, 112 is an OPA, uh, 2364 op amp one and OPA, uh, 2376, uh, op amps. Um, HC4053s.

**Dave Jones:** Um, uh, jeez, what else we got? Another, uh, OPA precision, uh, op amp. This is actually a, um, max, uh, 7400. That's actually an eighth order, uh, low pass, uh, switched cap filter they've got in there. So, um, they have actually got, uh, a switched cap, uh, filter, go figure. And, uh, once again, another 4053, couple of 4053s. We've got another OPA device. It looks like they love these, uh, TI, uh, OPA devices. They're absolutely obsessed with them. There's another three, um, three precision OPA 2376s

**Dave Jones:** down here, precision op amps. Um and they've got uh some maximum uh devices here, max 43 uh 82. They're an eight-channel uh mux. And well, apart from that, a few more precision op amps and yada yada. And there you go. That's um inside a typical uh LCR meter design.

**Dave Jones:** It's really um hardly any different to the previous design. Oops, and I missed that one up there. That one's actually a uh TI 27 uh 11 uh low-power uh precision op amp. And then of course, this one up here is the uh E-squared PROM for the processor.

**Dave Jones:** The 4-mm banana sockets down here are quite nice. They've got uh recessed uh metal uh base in there like that with uh metal threaded tapped screws which go through there. And there's the uh input um uh blade terminals on the other side.

**Dave Jones:** And I thought they were just soldered onto the top. So, I may stand corrected uh here. These are actually better than I thought. I thought they were just soldered on the top, but they're not. They're actually a through-hole device which does go through to the bottom side of the board there. So, that is uh a lot better than I thought. But obviously, you can see that when you push that in there, it's really only this bottom side here which moves. This top side has a bit of spring to it, but you know, it's

**Dave Jones:** it really is uh it's putting a bit of stress on that solder joint. But it's not nearly as bad as I thought. So, I declare that to be okay. And as you can see, there's really um nothing on top.

**Dave Jones:** No surprises there, just a rubber membrane uh keypad like that. And that's about it. Um they've got the polycarbonate uh front window, the LCD. There'll be nothing under there. There will just be a couple of zebra strips uh top and bottom or just at the top side there, and that's about it. Really haven't had no problems with the board at all. It's a first class quality construction. Seems well laid out, well designed, as you'd expect from Agilent. And inside the back of the case, they've gone to town on the

**Dave Jones:** shielding. Of course, very common in these LCR meters. The old one is exactly the same. They haven't changed a thing there. And the PCB's only held down with that one screw there, and the three screws on the banana jacks here, plus these two little plastic retaining clips on the side. It does actually fit in there quite well.

**Dave Jones:** Got no problems with it, so there you go. That's inside the Agilent U17 33C LCR meter. I like it. I've no hesitations in giving that one a thumbs-up. And next up, we'll have to do a review of this thing and compare it with the previous model, and see how it handles itself. So, that'll be quite extensive, I think. So, it could be a little bit of time before I get around to doing that, but anyway, the internal construction's a beauty. I'll catch you next time.
