---
video_id: _kI8ySvNPdQ
title: EEVblog #1284 - How Bad Product Design Kills The Environment
url: https://www.youtube.com/watch?v=_kI8ySvNPdQ
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 27, "3": 47, "4": 62, "5": 89, "6": 95, "7": 107, "8": 115, "9": 125, "10": 134, "11": 154, "12": 174, "13": 192, "14": 207, "15": 213, "16": 236, "17": 252, "18": 264, "19": 285, "20": 293, "21": 306, "22": 317, "23": 328, "24": 339, "25": 353, "26": 372, "27": 384, "28": 397, "29": 410, "30": 428, "31": 438, "32": 454, "33": 466, "34": 478, "35": 490, "36": 509, "37": 523, "38": 550, "39": 563, "40": 575, "41": 584, "42": 607, "43": 616, "44": 627, "45": 638, "46": 650, "47": 666, "48": 676, "49": 693, "50": 709, "51": 726, "52": 742, "53": 753, "54": 764, "55": 778, "56": 797, "57": 813, "58": 838, "59": 851, "60": 866, "61": 880, "62": 892, "63": 905, "64": 916, "65": 933, "66": 942, "67": 955, "68": 975, "69": 989, "70": 1002, "71": 1021, "72": 1034, "73": 1050, "74": 1067, "75": 1084, "76": 1095, "77": 1115, "78": 1126, "79": 1138, "80": 1150, "81": 1166, "82": 1179, "83": 1190, "84": 1203, "85": 1216, "86": 1230, "87": 1239, "88": 1253, "89": 1269, "90": 1280, "91": 1293, "92": 1312, "93": 1326, "94": 1337, "95": 1355, "96": 1368, "97": 1376, "98": 1388, "99": 1396, "100": 1416, "101": 1424, "102": 1438, "103": 1450, "104": 1463, "105": 1479, "106": 1489, "107": 1508, "108": 1517, "109": 1532, "110": 1541, "111": 1566, "112": 1582, "113": 1592, "114": 1604, "115": 1618, "116": 1629, "117": 1646, "118": 1655, "119": 1668, "120": 1686}
---

**Dave Jones:** Hi, I get lots of uh email technical questions and this particular case I got one from uh somebody who wanted to know how to design uh like really low standby power direct mains power supplies, i.e.

**Dave Jones:** you know, 240 V or 110 V mains rectified uh and powering a product directly non-isolated as we'll go into, but they wanted to have like really low uh standby uh power.

**Dave Jones:** So, like usually technical questions like these take a long time to uh answer. So, usually I direct uh people over to the EEVblog forum to answer such things, but I thought, "Hey, this might make an interesting video." So, I thought I'd actually get a uh mains-powered uh product like this.

**Dave Jones:** In this particular case, it's one of these uh photoelectric uh smoke alarms. It's a 240 V one that actually powers into the mains. It's actually dual battery and mains-powered because if the mains fails, you need the battery back up for safety, of course.

**Dave Jones:** Model QA 1300, it's a Quell, which is a uh big brand here in Australia. So, I thought we'd do a teardown of this and have a look at the design and uh look at how much standby current uh something like this uses and um potentially how to actually uh design or a you know, one of the ways to actually design a really low uh standby quiescent current direct

**Dave Jones:** mains power supply. So, you know, let's take a look at it. Now, just a quick uh note on the product design of this thing. I really quite uh like this.

**Dave Jones:** It's got the back in plate here and uh of course you screw this into the ceiling and then it's got a hinged uh system like this and it's got some um screw-in terminals for the mains, of course.

**Dave Jones:** You've got to uh have that. So, your 240 V uh goes directly and they look like proper cage clamps, too. None of that uh you know, spring leaf lever rubbish.

**Dave Jones:** I really like those. Um so, that's really nice. They've got an extra uh cover which then goes over that to isolate, but when it goes down, here are the pins on the PCB inside.

**Dave Jones:** So, when it goes in like this, it goes down and then slides across like that and makes uh contact in there as well as uh retaining it on the roof.

**Dave Jones:** So, yeah, hats off to the designers there. That's very nice, and we've got our 9-V battery backup in there as well. And no, it's not uh rechargeable. It just uses a regular uh 9-V uh uh PP3 alkaline or uh lithium or whatever you whack in there, and that's just you know, they've probably got diode or in will reverse engineer the circuit in here and have a squeeze.

**Dave Jones:** But anyway, rather like the uh design of that, and also the design of this. This little latch here, when you put the battery in there, it pushes down and moves that lever out, and that means that uh you can't actually close this up and then slide this in and install it without the battery physically being installed.

**Dave Jones:** That's really nice design touch. I love it. Yeah, uh this is a photoelectric one, as I said, uh photoelectric uh sensor. So, what that means is that it just um like the smoke particles uh go into the sensor here, and then it uses uh optical uh measuring to see if there's any particles within the air inside the uh sensor.

**Dave Jones:** So, it doesn't have any of that nuclear rubbish. And right off the bat here, the spec, it's only got a maximum spec, but look at this, 80 milliamps, uh 240 V AC.

**Dave Jones:** Oh, jeez, that's a fair bit of current draw. But yeah, it won't be that max. We'll have to measure it. And there you go. Wow, that is truly horrendous.

**Dave Jones:** 563 mW. WOW, THAT'S AWFUL. And look at the power factor, 0.062 power factor. So, that gives is a VA of over nine well nine VA? Got to be kidding me.

**Dave Jones:** This is like obviously they're using an like just a bridge rectifier in their Zener diode type configuration or something like that. Absolutely no thought given whatsoever to actually minimizing the quiescent current of this thing.

**Dave Jones:** And what what's the big deal Dave, you know, it's only half a watt. What's the big deal? Well, I've done videos which I'll link in on why that can be a big deal.

**Dave Jones:** And sure you're only in like residential situations generally it might vary in some countries, but you're only going to pay for the half a watt here. You're not going to pay for the nine VA here, but that is current that has to come from the grid.

**Dave Jones:** So even though you're not paying for it, the grid infrastructure has to be there to enable this. So we're looking at 36 and a half milliamps at 247 volts.

**Dave Jones:** Yes, I am right on the high side of the mains voltage which is normally 230 volts here in Australia. So it did give us our nine VA. So that's just yeah, that's nuts.

**Dave Jones:** Let's run some numbers, shall we? So that power consumption is absolutely atrocious. We'll go through the numbers in a minute, but I thought that well, it maybe it's just this Quell design.

**Dave Jones:** So I went out and bought this sort of like no name fire pro I guess. Well, let's check this out. It's not promising though. Look, 100 milliamps max. The other one was only like 80 milliamps or something.

**Dave Jones:** So I'll measure this one, but I reckon it's going to be a shocker too. Built down to a price. And the design of this one is nowhere near as polished as that Quell one.

**Dave Jones:** Anyway, let's power it up. Wow, this is an absolute shocker. 1.36 watts. Are you kidding me? That's enormous. It's Once again, same power factor as we're getting before. So, our VA is getting 19 and 1/2 VA.

**Dave Jones:** Are you kidding me? People have like half a dozen of these things installed in their house. This is shocking. I I'm going to call it. This seems to be a systemic design problem with this with these like 240 volt home smoke alarms.

**Dave Jones:** Let's run the numbers on this. It's insane. So, let's run some numbers here. Let's say we had this Fire Pro brand installed all over Australia. Oh, don't touch the dangerous part here.

**Dave Jones:** Um yeah. Anyway, let's say we had these Let's say, you know, a typical large home might have like five of these installed. You've got to have them installed in front of every or inside every bedroom and stuff like that.

**Dave Jones:** There's new requirements these days, things like that. Let's say we have a million homes in Australia. I think there's like 2 and 1/2 million, but just, you know, Let's just round Let's say we've got a million homes installed with five of these each, right?

**Dave Jones:** We're talking Let's just round this up to 20 VA, okay? And because, even though the residential customer is only paying for the watts, okay, 1.3 watts, the grid has to be designed to deliver this entire 78 milliamps, right?

**Dave Jones:** You don't get that for free. That's losses in the grid, even though you're not paying for it. So, the generator has to produce that, the transmission capability has to be in there for that.

**Dave Jones:** So, let's just call that 20 VA, right? So, this is apparent power or complex power as opposed to real power or active power as it's called. But, as I said, you've got to have you've got to generate this at the generation station.

**Dave Jones:** Just goes to show how bad product design like this or really essentially cheap product design, cuz we'll have a look at better product design in a minute that's more expensive that can solve this problem.

**Dave Jones:** This can have a real huge environmental and cost impact on the planet. When you start talking millions and tens of millions and hundreds of millions of homes that all have these smoke alarms mandated.

**Dave Jones:** You don't think all the smoke alarms take a naff all power and it does when you power them from your little 9-V battery here cuz normally these things will last a couple of years off a 9-V battery.

**Dave Jones:** So the actual electronics in here detecting the smoke takes naff all power. It really does. So all of that like 99.9% of it is being wasted in the mains rectifier in here and the power supply that needs to power that circuitry.

**Dave Jones:** It's insane. And well, to the surprise of absolutely none of my audience whatsoever, yeah, this is the cheap Firex Pro one and this is the more expensive one. It's actually designed by Kidde.

**Dave Jones:** I've heard of them before so yeah, Quell don't design their own but yep, these things are built down to a price as you'd expect and we're paying the price in terms of environmental cost because these mains power sensors use like in the order of 65,000 times more power than the equivalent just being powered from the battery.

**Dave Jones:** The same thing. It's just insane. Absolutely insane. And we've got our piezo transducer as well and this is actually the sensor. And you can see where the smoke's actually going to get into this one.

**Dave Jones:** If we have a look at this Kidde / Quell one over here, you can see that this is where the smoke goes in around here. I was actually wrong that the smoke goes in through here.

**Dave Jones:** This is actually the buzzer. It goes around the outside and then goes inside the unit and then makes its way through the grill here into our photo sensor here and here.

**Dave Jones:** It's interesting to note that this cheaper one actually uses a tactile switch here for the test button, but the more expensive [laughter] one over here, well, I presume it's more expensive, actually just uses a PCB contact and just some bent metal like that making contact to a link over there.

**Dave Jones:** So, I do wonder which one's actually cheaper cuz, you know, you can get these for cents at the Shenzhen market. I wonder how much this solution here cost. It's interesting.

**Dave Jones:** Anyway, this one is this a double side? This one looks like a double-sided FR4 board. This one over here, single-sided jobbie cuz you save a few cents on that.

**Dave Jones:** Anyway, both of them have a MOV because you don't want any surges, of course, on the power line cuz these things are hooked up 24/7. So, both of them have a little MOV.

**Dave Jones:** That one's got a little slot cut out underneath for isolation, but basically, it's a capacitor divider and a big resistor. Capacitor, of course, at 50 Hz, none of that 60 Hz American rubbish.

**Dave Jones:** 50 Hz Australian mains and, of course, a capacitance will have a given impedance and then that works in combination with a resistor here to give you a resistor divider and it looks like is that our Zener up there?

**Dave Jones:** Could be. So, this one here uses a one mic. Both of these are X2 class capacitors. Of course, you know, proper mains rated self-healing types with all the requisite approvals on them.

**Dave Jones:** So, this is the Kidde/Quell. This is the Firex Pro here. You got a smoke alarm controller IC here. It's a custom ASIC. We've got bridge rectifier down here. I can't see a bridge rectifier over on here.

**Dave Jones:** Might be a just a half wave jobbie. Not sure if you can see that, but the more expensive one, there you go, got the shine on it. It looks like it has a at least partial conformal coating on it just to stop moisture causing a problem.

**Dave Jones:** So, I've reverse engineered the mains input power supply on both of these and as suspected they're just a simple Zener diode based rectifier. That's it. So, we've got our 240 volts in here, line and neutral.

**Dave Jones:** We've got a series resistor here. That's a big 2 watt jobbie in both places. Then we've got that X2 240 volt rated, you know, mains capacitor. We've got a MOV here doing some protection after the resistor, so that's good.

**Dave Jones:** We've got some bleeder resistors across here, just some high value ones. One of them had three resistors in series just to get the voltage cuz they're SMD ones, so they're only rated like couple hundred volts each tops.

**Dave Jones:** So, they put them in series to get the voltage rating. Then we've got a Zener diode. In the case of this one, it actually used Sorry, this one over here used two Zener diodes here and here in series.

**Dave Jones:** This one over here only uses one Zener diode, but works exactly the same. Then we've just got a regular Joe Blog's diode here and then an electrolytic cap and then that buggers off to the ground in here.

**Dave Jones:** Now, of course, these are what's called a direct mains connection non-isolated power supply and these are inherently dangerous. You do not design these except in products that are fully enclosed like this where the user can never ever touch the electronics in them or shouldn't.

**Dave Jones:** That's the entire point because it's more cost and complexity to put in like a mains isolation transformer and everything else. But in these types of products, um it's it's no problem and it's completely legal to have uh your circuitry over here mains referenced over here.

**Dave Jones:** Even though it's the neutral and technically we use the men system, the multiple earth neutral as we do here in Australia, your mileage may vary and the neutral's connected back to the earth at your switchbox, but you can't assume that the wiring in a house is correct and uh some idiot may have swapped uh new you know, active and neutral here and you could completely come a gutser

**Dave Jones:** if you uh design a product uh that was relying on the fact that uh any exposed user accessible uh ground or metal or connector or anything like that was reliant upon directly connected through the neutral, you're going to come a gutser and that's inherently unsafe.

**Dave Jones:** So, you don't want that. So, a non-isolated power supply like this um they're very common to find in these type of uh in sealed enclosures like this cuz you just don't need the isolation, but this is where the poor power factor comes from.

**Dave Jones:** It's just using the cap and the uh series resistor as a dropper effectively for the Zener diode and that's just uh no, no. That's what's resulting in the piss-poor power factor that what that we're seeing.

**Dave Jones:** So, there's just no way of avoiding uh losses in your traditional Zener based uh circuit like this. I In this particular case, I'm going to measure the voltage directly across uh the 100 ohm resistor here.

**Dave Jones:** Uh I've got it there and 7.9 volts. So, there you go. That's 79 milliamps and of course, that's going to match your 79 milliamps up here and there's absolutely nothing you can do about that.

**Dave Jones:** So, you're pissing away that 79 milliamps even though you've got essentially bugger all like microamps load on here. It it doesn't matter. It's just being wasted in the Zener diode circuit.

**Dave Jones:** So, that's just lazy and cheap design and well, they just didn't care. And of course, 89 milliamps might not sound like a lot, but when you have millions and millions, tens of millions, hundreds of millions of these sort of things out there, it makes a huge difference, especially given the poor power factor.

**Dave Jones:** That current has got to come from the generation system. There's just And you've got I squared R losses in the in all of that, and it's just it it adds up.

**Dave Jones:** And if you want to know how much current it takes with just the 9-V battery parent, it's your traditional uh smoke alarm in And this particular one, five little as five microamps, it sort of just goes up in bursts.

**Dave Jones:** It's, you know, it sense in there, whatever. Max, almost 50 microamps. So, between 5 and 50 microamps there periodically. So, you know, sniff of an oily rag stuff. So, if the actual product itself only takes like less than 50 microamps, why does the whole product have to take orders of magnitude more than that?

**Dave Jones:** Because they were just saving cost here, and they just didn't care about how much quiescent power consumption this thing is going to use, and that's terrible. Just to save like maybe a dollar or something like that on each one.

**Dave Jones:** And yeah, I can understand that might be significant, but if you explain to people, "Hey, look, our one is going to save you money cuz there's not quiescent current in there." But you could turn this into a marketing opportunity.

**Dave Jones:** You can say, "Hey, look, our one only draws like 100 microamps, for example, or a couple of 100 microamps, like sub-1 milliamp, uh for example. If you just spent, you know, a dollar or two more in the design of this thing, and you put some thought in, you could, you know, you can own the market because yours has like lower power consumption.

**Dave Jones:** I Anyway, I don't Is there one out there that claims that? I don't know. So, how can we improve this? Well, let's go have a look at Well, at least one solution, anyway.

**Dave Jones:** But it's going to be more expensive, and that's the trick. So, how can we solve this? Well, there's many ways to skin this cat, and if you've got a better way to skin this cat, then please list it down below, and you can roll your own solutions and do all sorts of stuff, but I'm just going to go with an incredibly simple and obvious solution.

**Dave Jones:** Let's take a look. Let's go straight to Digi-Key, shall we, or your favorite supplier with their parametric search tools, or as I've shown in previous videos, you can go directly to the manufacturers websites like over here, for example, and look at LDO regulators and stuff like that.

**Dave Jones:** Now, we're just going to we need a regulator, of course. These particular power sensor runs on 15 volts, so actually the chip runs from 6 to 15 volts, but this particular one has like runs on like 14 and 1/2 volts to the Zener diode voltage in this thing.

**Dave Jones:** Anyway, so we need a linear regulator, but because it is powered directly from the mains, we don't have any isolation, we need a high DC input voltage regulator, and these actually do exist.

**Dave Jones:** So, if you just simply go into the voltage regulator linear voltage regulator section here in Digi-Key, and then you sort by voltage input maximum right here, sort from highest down, look, you'll notice that there's a whole bunch of them that have 450 volt rated, and then it drops down to 150.

**Dave Jones:** 150 is you know, that's not good enough, but obviously these 450 volt ones are designed for direct mains connection. And look, there's a Microchip solution, there's an On Semi solution.

**Dave Jones:** Yep, they seem to be the only two, but hey, there's two right off the bat. So, we can go into the Microchip one here, adjustable 1.2 to 3 to 438 volt output regulation.

**Dave Jones:** This one's not the best example. Let's go to a better one. Now, let's go to these On Semiconductor ones here. You can find it on the parametric search on directly on the website here.

**Dave Jones:** Wide input voltage range, ultra low quiescent current. That's what IQ means. Quiescent I is current, Q is quiescent. Up to 10 milliamps load current. So, only designed for real low power stuff, but hey, you saw the circuit consumption is only like 50 microamps.

**Dave Jones:** So, this has got oodles. I don't like that little pain in the ass package. Look at that surface mount. So, this one's not really conducive, but look, you can it's designed for half wave rectifier mains input circuits with a full .7 mic cap there.

**Dave Jones:** That's you will see in a minute how that's not we can get one that's a bit better than that. But, if we go down here, look, here's some input gain configuration.

**Dave Jones:** There's a half wave bridge rectifier. Look, bingo, 15 volts out, 10 milliamps. It's going to do the business. We've got a full wave bridge rectifier one here, and let's have a look at this other one.

**Dave Jones:** So, they've got two ones the NCP1786 we saw before. This is the 1785 product overview. It's one of their energy efficient innovations here. They look, [gasps] shock horror, designed for smoke sensors.

**Dave Jones:** The marketing people at these companies know exactly how to target these chips to these companies. But, do they care? There's probably some out there that implement these lower power solutions, but well, the two I've got here don't.

**Dave Jones:** They just saved a few cents. We'll see the cost in a minute. But, anyway, let's have a look at this puppy, shall we? It's got a fixed 15 volt output, exactly what we want.

**Dave Jones:** Uh half wave rectifier, 2.2 microfarad cap. The smaller the capacitor, the cheaper it's going to be to actually implement that. So, there you go. There There's your There's your circuit right there.

**Dave Jones:** Just a half wave diode bridge rectifier, 2.2 mic cap, 450 volts. It's got to be proper mains rated and all that sort of stuff. You're still Yes, you're still going to get poor power factor from any bridge rectifier solution like this, but we'll take a look at a smarter solution to this in a minute.

**Dave Jones:** It's really quite nice. But still, because you aren't implementing that Zener solution, that's just pissing away like 80 milliamps or whatever. They didn't need it that high. They could have just implemented the Zener diode circuit better.

**Dave Jones:** But anyway, these are going to be a better solution cuz the quiescent current is only like a 10 microamps quiescent current there and 50 microamps for the load. So it's drawing naff all, right?

**Dave Jones:** The whole thing even probably the worst smoke sensor circuit on the chip on the market is, you know, going to be like sub 100 microamps with this thing. So yeah, we're still going to get poor power factor, but it's going to be order of magnitude better than the Zener solution that they're actually using here.

**Dave Jones:** No doubt about it. So it literally is as is as simple as that. And tell us the price, son. How much does it cost? Here we go. Yeah, they cost Okay, 55 Yankee cents each in like volume.

**Dave Jones:** Probably get it cheaper than that if you're manufacturing millions of smoke alarms, right? So they probably saved like 30 cents or something, 40 cents or something because Zener diodes are cheap.

**Dave Jones:** You get them from the Shenzhen market. Like it it it's real cheap, right? The way they did it. So they probably saved like a sub 50 cents on the bomb cost of this thing and they're just you know, [snorts] destroying the environment and putting load on the grid and they because they just don't care.

**Dave Jones:** They want to save 30 cents. It's ridiculous. Should have just used one of these puppies. But I know what you're asking. Is there a smarter solution than just the simple diode full or half wave bridge rectifier diode solution here to get a better power factor?

**Dave Jones:** Well, yes, there is. As I said, you could probably roll your own and let us know if you got links down below to like rolling your own solutions. We won't go into that.

**Dave Jones:** It's it's fairly complex. But I did find this part from TI. It wasn't easy to find, but look at this. It's 120 mA smart AC-DC low dropout linear voltage regulator.

**Dave Jones:** Don't know why you need low dropout, but anyway, [laughter and gasps] you've got plenty of margin. But, it's for non-isolated power solutions greater than 18 V, same as before.

**Dave Jones:** Standby power consumption is only 15 mW there. Line voltage cap cap drop capacitor is as small as 1/4 the size of linear solution. So, there you go. You can save cost there cuz when you got mains-rated capacitors, they have to be not only physically larger, but they're more expensive as well.

**Dave Jones:** We'll have a look at this puppy cuz it's really quite interesting. Yes, it's about I think it's about a dollar in volume here, but anyway, work with me. Well, what do you know?

**Dave Jones:** Smoke and heat detectors. They know who they're marketing to. Now, here it is a schematic for half-wave and full-wave bridge rectification. This is direct mains input. So, here's your 240-V mains input.

**Dave Jones:** You've got a TVS surge protection here. You've got an input series capacitor and input series resistor, just like we have on the Zener circuit here. But, instead of having the lossy Zener circuit, we're putting in this active rectification chip.

**Dave Jones:** It's just got a few other support components there, but it gives you an LDO regulated voltage out from direct mains input. And the way it does it is really quite nice.

**Dave Jones:** Let's go down here is that it's got active rectification in here. So, instead of having dumbass regulation, it's got this active regulation with these two MOSFETs here and here, which control this full-wave bridge rectification.

**Dave Jones:** And it's very smart. It can control it so it can give you a better power factor direct from the mains. Anyway, it's just a really nice chip. I like this one.

**Dave Jones:** So, if you're after a direct mains-connected low quiescent current solution with a linear voltage regulator output, not isolated of course, then this is well worth a look. And yeah, it's a bit expensive, but you know, buck a chip, but it's a really nice solution.

**Dave Jones:** You want the lowest quiescent current possible, this could do the business. Unfortunately, this chip is only available in versions that we fixed output voltages up to 5 volts. It doesn't go to 15.

**Dave Jones:** Don't know why. You know, but anyway, so it's not suitable in this particular circumstance with this particular smoke sensor chip. But anyway, I thought I'd show you that cuz that is a really nice solution chip.

**Dave Jones:** If you know of another equivalent one on the market, direct AC input like this, please leave it in the comments down below cuz I think this might be the only one.

**Dave Jones:** But anyway, haven't done a hugely exhaustive search, but yeah, I really like that. Is that chip of the week? Think it is. So there you go. I hope you enjoyed this look at a typical consumer product that went from being very low power design through essentially regulation, at least here in Australia, you have to have these direct Oh, I think all new houses must have these direct mains connected

**Dave Jones:** smoke sensors. And two of them on the market, including one of like a real premium brand, brand, one of the most popular ones, they're both still awfully designed, penny pinching designed, and not giving one rat's ass about the quiescent power consumption.

**Dave Jones:** And as I showed, when you got millions of these things installed, some houses have, you know, half a dozen or more of these things, then it just really adds up.

**Dave Jones:** So next time, if you're involved in designing stuff like this, just please try and persuade the company that you're working for that this could be a potentially good and marketable solution.

**Dave Jones:** Cuz you can go, "Hey, houses eco-friendly." Everyone goes crazy over that these days. Marketing people can tell the consumer about this sort of uh uh problem. And this is by far not the only product.

**Dave Jones:** There's, you know, a countless other products on the market. If If you know of any other really badly designed products that have standby quiescent uh power like this, basically anything with Internet of Things in the title, possibly.

**Dave Jones:** Anyway, leave it in the comments down below. So, yeah, I It's a real eye-opener when you actually run the numbers and do the calculation on something like this of how much actual grid infrastructure and generation uh power is wasted just through poor product design like this.

**Dave Jones:** Unbelievable. So, anyway, I hope you found that video useful. If you did, please give it a big uh thumbs up. And as always, you can discuss down below or over on the EV blog forum.

**Dave Jones:** And check out EVblog.tv, which links to my library uh channel. Subscribe over there cuz that's going a gangbusters. And I did mention Chip of the Week. Um yes, I'm back into doing uh more regular Amp Hour episodes.

**Dave Jones:** So, if you don't know, the world's biggest electronics engineering podcast that I've only been uh co-hosting for the last decade, almost. Um theampour.com. Go check it out. It's available on all your iTune-y platforms and Spotify and all that sort of stuff.

**Dave Jones:** Catch you next time. [music]
