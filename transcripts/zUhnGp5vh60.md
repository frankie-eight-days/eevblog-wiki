---
video_id: zUhnGp5vh60
title: EEVblog #373 - Multimeter Input Protection Tutorial
url: https://www.youtube.com/watch?v=zUhnGp5vh60
source: youtube-asr
timestamps: {"0": 1, "1": 30, "2": 42, "3": 58, "4": 73, "5": 88, "6": 105, "7": 120, "8": 133, "9": 147, "10": 158, "11": 180, "12": 192, "13": 202, "14": 221, "15": 234, "16": 249, "17": 273, "18": 295, "19": 318, "20": 336, "21": 350, "22": 366, "23": 377, "24": 398, "25": 412, "26": 425, "27": 437, "28": 451, "29": 466, "30": 488, "31": 501, "32": 514, "33": 529, "34": 546, "35": 560, "36": 573, "37": 600, "38": 613, "39": 637, "40": 658, "41": 677, "42": 686, "43": 707, "44": 718, "45": 730, "46": 741, "47": 752, "48": 767, "49": 784, "50": 796, "51": 806, "52": 823, "53": 839, "54": 853, "55": 876, "56": 888, "57": 898, "58": 907, "59": 923, "60": 938, "61": 953, "62": 964, "63": 976, "64": 989, "65": 1002, "66": 1014, "67": 1027, "68": 1046, "69": 1068, "70": 1085, "71": 1099, "72": 1110, "73": 1121, "74": 1141, "75": 1149, "76": 1165, "77": 1176, "78": 1188, "79": 1202, "80": 1221, "81": 1237, "82": 1249, "83": 1260, "84": 1274, "85": 1297, "86": 1311, "87": 1337, "88": 1354, "89": 1362, "90": 1378, "91": 1391, "92": 1418, "93": 1433, "94": 1448, "95": 1462, "96": 1470, "97": 1487, "98": 1506, "99": 1518, "100": 1538, "101": 1551, "102": 1560, "103": 1578, "104": 1596, "105": 1609, "106": 1629, "107": 1642, "108": 1668, "109": 1686, "110": 1699, "111": 1713, "112": 1729, "113": 1747, "114": 1763, "115": 1780, "116": 1794, "117": 1808, "118": 1824, "119": 1834, "120": 1844, "121": 1854, "122": 1875, "123": 1893, "124": 1908, "125": 1925, "126": 1939, "127": 1954, "128": 1973, "129": 1994, "130": 2005, "131": 2022, "132": 2037, "133": 2053, "134": 2062, "135": 2069, "136": 2080, "137": 2091, "138": 2104, "139": 2123, "140": 2140, "141": 2151, "142": 2169, "143": 2189, "144": 2200, "145": 2215, "146": 2241, "147": 2260, "148": 2277, "149": 2300, "150": 2318, "151": 2339, "152": 2361, "153": 2373}
---

**Dave Jones:** Hi, quite a few people have asked me to do a video on multimeter input protection and how it actually works and how it relates to cat ratings and surge overloads and HRC fuses and you know, isolation slots which if you've seen me tear down a multimeter, I'm explaining all this stuff all the time, but a few people have asked can I actually explain how a typical multimeter like this Fluke 27 that I

**Dave Jones:** just had we just had a look at it in the previous video, how the input protection on this works. So, I thought we'd take the schematic for the Fluke 27 and we'd have a shot at explaining input protection.

**Dave Jones:** Let's go. Now, as with any typical multimeter, we've got a common jack. We've got a volts, ohms, and diode jack which also does capacitance and other things and usually we've got a separate amps and a separate milliamps and microamps jack.

**Dave Jones:** Now, I know some multimeters, some cheap ones will actually combine milliamps and microamps with the volt ohm diode one. Don't worry about that. This one we'll focus on separate amps and milliamps and you'll notice that they're also fused.

**Dave Jones:** This one's fused at 320 milliamps maximum and well, at 10 amps maximum so the fuses are going to be slightly above that. In this case, 440 milliamps and 11 amps for the amps input jack there.

**Dave Jones:** Now, these fuses in multimeters, we'll talk about what HRC fuses are, but these fuses only protect the amps and milliamp ranges. They have nothing to do with protecting the voltage input jacks and we'll take a look at the circuitry and see why.

**Dave Jones:** So, you can rip those fuses out of your multimeter and you're still going to be able to measure volts, ohms, and capacitance and diodes and all that sort of regular stuff except current and that has its own input protection circuitry as well.

**Dave Jones:** That's where the MOVs and the PTCs you've heard me talk of come into it. So, let's get the whiteboard. And here it is. We're going to have a crack at basic input protection circuitry on a multimeter.

**Dave Jones:** And this is actually the exact input circuitry, or pretty close to the exact input circuitry for the Fluke 27 multimeter. And I'll link in the service manual down there in the description, and you can download it and have a look at it yourself.

**Dave Jones:** So, we'll be able to actually physically see these components and how they work, and we'll show inside shots of the multimeter as well. But I did the teardown in the last video.

**Dave Jones:** So, this is fairly typical, but I'll just say up front the input protection of multimeters changes a fair bit from manufacturer to manufacturer, depends on how the ADCs out here work, and the the requirements for protecting those, and the network dividers they the input they use, and all sorts of things, and the measurement ranges and types.

**Dave Jones:** It varies a lot, okay? So, this is typical of a basic multimeter, volts, ohms, amps, and that's, you know, pretty much it. So, let's have a look at what we have here.

**Dave Jones:** We have our input jacks, our four input jacks. We've got ground down here. We've got our amps input jack, our 10 amp input jack. We've got our milliamps and microamp input jack.

**Dave Jones:** And we've got our volts, ohms, and diode jack up here. And as I said before, they are completely separate input protection circuits. So, basically, let's look at the amps and the fuse protection first, and forget all about this circuitry up the top.

**Dave Jones:** Does not exist. So, let's look at the 10 amp input jack first, and you're probably familiar with this, and it works exactly as you'd you'd We've got our ground input here, and it goes through a current shunt resistor.

**Dave Jones:** In this case, 5 mΩ. It's that little copper strap that you can see inside the multimeter. And it then where it goes through our 11-A fuse here. In this case, it's a HRC or a high rupture capacity fuse.

**Dave Jones:** So, if you accidentally short this to a power supply, which is capable of delivering say 50 A, and you have 50 A flowing through this thing, this fuse is going to the element inside's going to heat up, and it's going to blow fairly quickly in the case of 50 A, but if you only if a multimeter has say 10 A uh input uh input range, and you've

**Dave Jones:** got an 11-A fuse, it's not going to suddenly blow at 11 A. It'll take quite a hell of a amount of time to actually do that. So, some multimeters um say, for example, they'll actually say in the specs, "Oh, it can measure 20 A for, you know, 10 seconds or something like that." So, the fuse isn't going to blow, and your uh input current shunt's not going to heat up too much and be

**Dave Jones:** damaged, and it can uh absorb those minor overload conditions. But, the idea with a HRC fuse like this, high rupture capacity, if you accidentally connect this amps jack across the mains, for example, 240 V or 110 V supply, there's a lot of energy in the mains system, right?

**Dave Jones:** At 2,400 W, for example, for our 240-V Australian thing here, that's continuous energy, 2,400 W, but it's actually capable of a lot more energy than that instantaneously. And that's the point with using high rupture capacity fuses.

**Dave Jones:** If you connect accidentally connect this up to a high energy system, energy with lots of joules, go look that up. Um then it's capable of delivering a lot of energy into your multimeter.

**Dave Jones:** And if you're familiar with like a bar radiator heater that uses those bars, 2400 W, that's a lot of heat, right? All of that trying to be dissipated in your tiny little multimeter input circuitry, something's going to go boom like that.

**Dave Jones:** And it's just going to blow the crap out of your meter and blast everywhere. Sometimes flames will shoot out, all sorts of stuff. Pretty horrible thing and the multimeter can catch on fire, all sorts of stuff.

**Dave Jones:** So, what this HRC fuse does is tries to contain all of that energy within inside its body. It's actually the fuse wire itself. If you see a regular glass fuse, it's only just a, you know, a bit of wire, a fuse wire inside a glass tube.

**Dave Jones:** And that can actually blast open and then arc over and the energy continues to flow. But these HRC fuses have got sand inside them or other material that can absorb the energy and stops all of that arcing over.

**Dave Jones:** So, it's very important to have a multimeter with HRC fuses. And also, uh, the test leads you use in the test, uh, system can have inductance in it as well.

**Dave Jones:** So, when the fuse actually opens, you can get an inductive kickback back into your multimeter, which then can cause an extra voltage high voltage overload. It can get really nasty.

**Dave Jones:** Now, similar sort of thing's going to happen on your milliamp and your microamp range as well. They use a separate input jack and a lower 440 milliamp fuse in this case, but it's also a HRC fuse cuz the same sort of gross overload conditions can apply.

**Dave Jones:** But in this case, the, uh, milliamp and microamp range, instead of flowing through straight through the high current shunt like that, actually, um it goes through the range switch itself.

**Dave Jones:** Hence, if you get a really gross overload the microamps and milliamps jack, you might blow your range switch, too, potentially, if it's not designed well enough. Cuz they'll have those, you know, PCB traces on your, you know, you know, those range switches can be designed on your PCB traces, and if the contacts aren't designed right, bang, you can blow the ass out of your range switch, too.

**Dave Jones:** But, basically, on say the amp range, what it does is it just from a circuit topology point of view, it actually puts in, in this case, in the case of the Fluke 27, it's a 4.995 ohm resistor.

**Dave Jones:** Why that oddball value? Why not five? Because it's in series with the .005 ohm resistor here. So, it's 5 ohms total. Um that's your shunt resistor for your milliamp range.

**Dave Jones:** And then, uh when you switch to microamp range, it disconnects these two resistors here and connects a 500 ohm range. So, your shunt resistor is higher on your microamp range like that.

**Dave Jones:** But, in both cases, okay, the voltage is tapped off here, and that goes into your uh ADC and your, you know, measurement circuitry and dividers and all sorts of stuff to measure your signal.

**Dave Jones:** But, what's all this weird-looking diode bridge and whole bunch of diodes doing around here? Well, if you've looked inside a lot of multimeters on their input protection circuitry, you may see a typical diode bridge there.

**Dave Jones:** It's not huge powered, you know, basic 1N4007s or might actually have a, you know, a four-terminal uh diode bridge itself in there. Why is that there? And how is it connected?

**Dave Jones:** Well, it's actually connected directly across your shunt measurement input here. Be it your microamp one, your milliamp one, it's connected directly across your input circuitry. And the reason it does that is because if you short out a power supply accidentally and there's a huge amount of current flowing through here, well, these resistors here, they can actually heat up as well.

**Dave Jones:** If you get a large voltage connected directly across your shunt resistor in here, then you can blow your shunt resistor before you blow your fuse because the fuse actually takes some time to heat up as we explained.

**Dave Jones:** So, what they do is they add this diode protection across here. Not only does it protect your input circuitry here by limiting to one diode, we'll explain how this works, this complex arrangement works at the in a minute, but it basically clamps the voltage across here and hence the voltage across your shunt resistor to a low voltage.

**Dave Jones:** And that will ensure that during that time current will flow through the diodes and then it will ensure that the fuse has time to blow. So, it's basically a protection mechanism not only for your input circuitry, but also to ensure that the fuse blows instead of your shunt resistor.

**Dave Jones:** So, how does this work exactly and why are all these diodes here? Well, let's assume that we input a positive voltage here, for example, and we've got a positive voltage here respect to down here and it's an overload input condition, okay?

**Dave Jones:** And the fuse hasn't blown yet, okay? So, let's say, you know, it's 10 volts or something, right? Now, normally the voltage across your shunt resistor is going to be uh quite small.

**Dave Jones:** That's your burden voltage. You remember I've done videos on that. My microcurrent solves that sort of issue. I've done a whole article on it in Silicon Chip. If you want to go read that sort of thing, your input shunt resistor on your current ranges is usually only going to going to drop, you know, a couple hundred millivolts or a volt or, you know, some one some really

**Dave Jones:** bad multimeters might be a couple of volts or up to 10 volts typically, but the Fluke 27, they've decided that they need one diode bridge plus four extra diodes in here.

**Dave Jones:** And let's have a look at what happens here. Okay, you've got a positive input voltage here. So, current's going to flow down here like this. It's not going to flow through there because that diode is reverse biased.

**Dave Jones:** It's going to flow through here, and then it's not going to flow through there cuz that diode is reverse biased. You remember, follow the arrow on the diode. That's how That's the great thing about the diode symbol.

**Dave Jones:** So, it's going to go flow through here, through here, through here, through here, through here. It can't go back up there cuz it's reverse biased. So, it's going to go through here and flow down there to ground.

**Dave Jones:** So, we now have 1 2 3 4 5 6 diodes in series across there. Bingo. We've just protected, I mean, you know, 6 times 0.6 volts, you know, 3.6 volts or something like that drop.

**Dave Jones:** So, really that is a protection mechanism, diode protection mechanism, for the input voltage here is going to be limited to the drop across those diodes, and hence the voltage across your shunt resistor is also going to be limited.

**Dave Jones:** Use Ohm's law, work out the power maximum power in the resistor during the time it takes for the fuses to blow. That's how That's why they use a diode bridge circuit like that.

**Dave Jones:** And why do they use a diode bridge? Because you might put a negative voltage in here and a positive voltage on here. Who knows what the idiot user's is going to do?

**Dave Jones:** They could swap their leads around, and or you've got AC or something like that, then that is going to work either way. In the case in the case of negative here and positive here, it'll just flow the just flow the other way through these diodes.

**Dave Jones:** And of course, you don't actually need these diodes here. They're you only add those extra diodes in if you want to increase that voltage because you've got a high burden voltage multimeter for whatever reason to do with your ADCs or whatever it is.

**Dave Jones:** It doesn't matter. So, they've added so you can add in those extra diodes if you need to increase that for your burden voltage, or you can simply short out your diode bridge like that if your burden voltage is under two diode drops or 1.2 volts.

**Dave Jones:** And this diode bridge and these diodes don't particularly have to be all that fast or all that high power. You know, standard 1N4007 stuff is what's used inside the Fluke 27, perfectly adequate to dissipate enough power and to be fast enough it doesn't have to be that quick because the fuse is going to take some time to blow anyway.

**Dave Jones:** Fuses don't blow instantly. They take seconds to blow. So, any properly designed multimeter is going to have some sort of diode bridge protection on the current ranges like that.

**Dave Jones:** It's just a belt and braces approach, additional protection for your input circuitry and for your current shunt resistors over and above the fuses because fuses blow all the time, right?

**Dave Jones:** People set it to the wrong current range, they accidentally measure volts or whatever, and you blow the ass out of your fuses. You know, you should keep half a dozen of things in stock just because it happens all the time.

**Dave Jones:** And just add in this extra input circuitry can can ensure that the fuse blows and nothing else. So, if you see a multimeter without some sort of additional amps protection like this diode bridge, uh it's not designed that well.

**Dave Jones:** And you'll notice there's one extra resistor down here, 100k resistor, and that goes off to the rest of the circuitry. In this case, it doesn't actually go to the signal ground inside uh the multimeter because they're a differential input ADC.

**Dave Jones:** So, it goes to the ADC low input pin like that. So, you've also got some extra I mean, you know, there's only so much current that can flow through 100k resistor even after you've clamped all your voltages and stuff like that.

**Dave Jones:** Super duper safe. So, now we're going to have a look at the volts, ohms, and diode jack, and capacitance jack, for that matter. So, all this no longer exists.

**Dave Jones:** The These fuses have nothing at all to do with protecting the voltage jack. Common misconception out there. So, let's have a look at it. And the input protection is actually pretty basic.

**Dave Jones:** It's not as complicated as it looks because actually pretend that these two components don't exist. These are just extra components that happen to be in the Fluke because of its 80s type of ADC and its input uh combination.

**Dave Jones:** So, these two do not exist. All we've got is these resistory looking devices here. So, let's take a look at them. Right? Our voltage input jack here, we've got a standard resistor.

**Dave Jones:** In the case of the Fluke 27, it's a five a 3.5k wirewound resistor. It's going to be a high temperature one, high power one, you know, it's going to be a pretty big input resistor there.

**Dave Jones:** And then, that's in series permanently in series with the input. That's the first thing you're going to have. Then, you're going to have what's called uh I often call them PTCs, or the other name for them is or the more correct name is a thermistor.

**Dave Jones:** And it's PTC PTC stands for positive temperature coefficient. It's a nominal 1k resistor, hence the value and the little dot. That's what the symbol for a thermistor is. If you see a resistor, every zig-zaggy one or a square one with a little dot next to it, it means it's a thermistor.

**Dave Jones:** And what it does is if the temperature of that device rises, i.e. positive temperature going up, it's got a positive temperature coefficient. So, the resistance goes up. So, if you get an overload condition where there's too much current flowing through here and using Ohm's law, too much power dissipated in this resistor, then the resistance is going to go up.

**Dave Jones:** So, it's a self-protecting mechanism. But, these things, just like similar to fuses, they act quite slowly. They have that thermal inertia and require heating up, that thermal mass inside in order for the value to go up.

**Dave Jones:** So, they're not an instantaneous device. This is a slow effectively a slow-blow protection device, for want of a better term, for your input jack. So, this is for These are very slow-rising inputs.

**Dave Jones:** You know, if it's a 1,000-V multimeter and you slowly ramp it up to, you know, 2,000 V or something, then this thing is going to eventually kick in. It's for that slow stuff.

**Dave Jones:** So, if your multimeter doesn't have at least one PTC, one thermistor in series with with the input, usually you can see it, you can follow the trace in, it's pretty simple.

**Dave Jones:** And if it's not in series with the input in somehow, then it's a piss-poor design multimeter. Piece of junk. You shouldn't touch it. Now, the next thing we need uh something to handle the transients, those really fast inputs, because this is something a lot of people don't understand with multimeters.

**Dave Jones:** They think, uh it's, you know, I'm only measuring the mains. It's only 230, you know, 240 V or something like that. You know, I my multimeter is rated to 1,000 V.

**Dave Jones:** What's the problem? It's all about transients, very fast transients. Is there a lightning strike on the line? Is there a you know, a huge industrial motor on there or other industrial machinery that's causing inductive kickback onto your line?

**Dave Jones:** You can get massive surges on your power lines all the time, and that's where the CAT ratings come into it. Um I won't go into CAT ratings fully here.

**Dave Jones:** You can look that up, but basically CAT I, you know, the lowest rating means don't use it on anything to do with a high energy circuit that can have these high energy impulses on them potentially.

**Dave Jones:** These low impedance circuits like a mains thing. So, a CAT II is the minimum you need for that. CAT III again would be say a So, CAT II might be your typical mains outlet, something like that.

**Dave Jones:** CAT III would be your typical switchboard or something like that. And CAT IV on top of that means your real you know, your substation, you know, your main distribution panel for a whole site because that's where the high energy spikes can be higher in energy, big voltage spikes, things like that.

**Dave Jones:** So, this is where we need some input protection circuitry that sees very fast transient pulses. And those CAT ratings will be defined by how many high voltage transient pulses they can survive and anywhere up to 8 kV.

**Dave Jones:** So, your 1,000 V rated meter is CAT III. It's actually designed to survive 6 or 8 kV transient voltages. And the way it does that, that PTC is not going to help you at all.

**Dave Jones:** It doesn't have time to heat up and raise the temperature. So, we use MOVs, metal oxide varistors. You've heard me mention these before. I'll point them out. They're usually these round radial devices inside the multimeter.

**Dave Jones:** You know, they're really big and chunky usually. And we'll get into that why that's important in the moment. and you need one of those from here to ground. When I say ground, it's the internal ground of the multimeter.

**Dave Jones:** It's i.e. back to the input jack here. It's not necess- Sorry, when I say ground, it's the input jack ground, not necessarily the logic ground inside the multimeter. Now, a MOV, or metal oxide varistor, is has a symbol like this, a standard resistor symbol with that little uh uh squiggly line going through it like that.

**Dave Jones:** And a metal oxide varistor, they're normally open circuit, completely open circuit. So, you can have one of these. Usually, just ignore that there's four there at the moment. Let's assume that that one goes down to our ground point down there.

**Dave Jones:** Cuz in theory, you only need the one. Okay? And normally, it's open circuit. So, that resistor doesn't exist doesn't exist. It doesn't affect anything at all, but if it exceeds its nominal rated voltage, in this case, in the Fluke 27, 430 V, then it will very quickly clamp down, hence sort of the hysteresis kind of symbol in there like that.

**Dave Jones:** Once it reaches that threshold, bang, it'll clamp down and go very low impedance and shunt all of the current down through there like that, which then will cause the PTC to heat up relatively quickly.

**Dave Jones:** So, this absorbs all of that pulse energy like that. And because it's very low impedance, there's going to be a very low voltage across it to then go into the multimeter.

**Dave Jones:** But these things can act, you know, extremely quickly, you know, microseconds, nanoseconds, that kind of stuff, very quickly. And then, that causes the PTC to heat up, which then, let's have a look at Let's draw a quick little crude graph here.

**Dave Jones:** So, this is I, okay? You got current like this and this is T for time, okay? So, your current is down like this and it suddenly goes wham, straight up like that.

**Dave Jones:** And then, it's going to roll off something like that as that PTC heats up. And that's also why you need a big high wattage wire wound high voltage resistor here, high power high temperature resistor in series with this cuz it needs to dissipate that heat as well when that MOV is switched on absorbing that, you know, the MOV doesn't magically absorb the energy.

**Dave Jones:** It's got to flow through these two resistors as well. So, this has to uh have adequate power dissipation as well during that time before the PTC goes way up in value and it goes up in the megaohms range and there's no more current flowing through there and your multimeter's protected.

**Dave Jones:** But, you're asking, why is there four in series like this? So, remember, this doesn't exist yet. We're not talking about that yet. This is Why are they using Fluke in the Fluke 27 using four of them in series instead of one?

**Dave Jones:** Well, you can actually get away with using one. You could have one, a big one, at 1,000 V, but it's better to actually put multiple ones in series. Not only can you dissipate more power, but then you get greater creepage distance by the physical gap.

**Dave Jones:** So, you'll see them all physically in series. So, the gap might be, you know, 2 or 3 mm between there. That's going to have X amount of voltage breakdown.

**Dave Jones:** And then you've got another couple of millimeters as you step up to the next one and the next one and the next one. So, you're you're increasing your creepage distance so you don't get arc over the single MOV like that for high voltage transients.

**Dave Jones:** And then you're you're dissipating energy in multiple devices, which is much much better than relying on a single MOV for uh both your input creepage distance. I mean, you could have a single MOV and then you can cut an isolation slot under I I a physical isolation slot in the board between it like that.

**Dave Jones:** And you know, you can probably get away with that. Um not a problem, but you can avoid having to do that and design an extra safety margin by having multiple ones in series.

**Dave Jones:** In the case of the uh Fluke 27, they got four uh 430 V ones in series. So, that's about 1,700 V. So, the Fluke 27 won't start clamping until the input gets to about 1,700 V, well above the rated 1,000 V input measurement range.

**Dave Jones:** But, of course, you can bet your bottom dollar that the rest of the input circuitry all in here is going to survive that 1,700 V just fine. It's uh measurement range is just limited to 1,000 V.

**Dave Jones:** Now, of course, the rest of this input circuitry here is where your 10 megohm input input resistor might be. And sometimes you'll have a higher value input resistor in here as well.

**Dave Jones:** So, that's why um your nominal 10 megohm input resistance multimeter might actually be 11 megohms or something higher than 10 megohms because there's the 10 megohm resistor plus the input protection resistors as well.

**Dave Jones:** And a good multimeter will actually have additional clamping past this point as well. And in terms of the Fluke, I haven't drawn it here, didn't really have room. In terms of the Fluke 27, if you go look at the schematic diagram, it's got actually extra transistors which switch on when the voltage level gets over a certain point.

**Dave Jones:** So, they switch on and clamp the voltage down. So, you can have or you could have extra, you know, an extra MOV or something or some other extra input protection circuitry after this main one.

**Dave Jones:** This one here, what I've shown, is the main one that's designed to absorb all of that input energy and meet that CAT rating requirement that the and get the certification for the CAT rating so that it meets a certain input uh pulse in terms of voltage and energy level and time.

**Dave Jones:** So, that's the important stuff. Anything else over here is just bonus stuff the manufacturer will include just to add some extra built-in braces protection for the ADC and the rest of the circuitry.

**Dave Jones:** And what's this, I hear you ask? Well, this is actually just a quirk due to the input switching requirements and stuff like that. In the case of the Fluke 27, they have a 1-M high voltage uh hybrid ceramic resistor there and they have another 430-V MOV there which just uses that existing It's just another path to protect another input over here to the ADC.

**Dave Jones:** All multimeters, they all the ADCs and chipsets and voltage dividers all over here will have lots of different complex configurations often and they will require other configurations. So, that's why I just showed this one here because when we open the multimeter, we'll see this stuff.

**Dave Jones:** So, let's do that. Let's see if we can see all this stuff inside our multimeter. And in previous videos of multimeter teardowns, you've seen me point out high voltage isolation slots and they're typically between input jacks between components.

**Dave Jones:** So, they might physically have a barrier between the voltage jack and ground or the current jacks. They might physically have a as we've mentioned, physically have a barrier you know, underneath or between or around.

**Dave Jones:** For example, they might, you know, physically have a barrier around all these MOVs so it doesn't arc over to other components like the nearby range switch which is typically the closest thing to the input protection circuitry and the jacks.

**Dave Jones:** So, um you know, that those high voltage isolation slots will be totally dependent upon the physical design physical construction of the unit. You've got enough room inside there if you've got a huge big multimeter, you've got enough room to lay it all out, you don't necessarily need any high voltage isolation slots.

**Dave Jones:** But when your multimeter gets smaller and smaller, all that stuff sort of cramped in there, um those high voltage isolation slots can be very important cuz remember, high voltage um uh not only just DC but high voltage impulses can actually jump across distances across your board.

**Dave Jones:** Got to be careful of that. All right, let's see if we can find all this stuff in our Fluke 27 PCB here. Okay, we've got our common jack down here which has that little input choke down in there.

**Dave Jones:** Not all multimeters have that. That's just something that Fluke's added just to take the edge off input pulses, presumably. This is our voltage input jack. This is our amps jack and that's our milliamps jack down there.

**Dave Jones:** So, let's follow this through and see what we get. Here's our voltage input jack here. So, our voltage input jack is going to go through a 3.5 K wire wound resistor, then a 1 K thermistor.

**Dave Jones:** Where's that? Here it is. It's connected directly to the 3.5 K wire wound resistor there. That's a high power high energy resistor, probably high temperature as well. And there is our PTC.

**Dave Jones:** We can't actually see it. This I don't think there's any real markings on that one, but anyway, I think it's a Rohm brand uh PTC, but there it is.

**Dave Jones:** And the trace from that PTC actually goes under the bottom to here, this top part, and then goes off to the range switch, and through all the rest of it.

**Dave Jones:** And then, we've also got our 1 meg high voltage ceramic resistor here. And here it is. There's the input jack, and there's the high voltage ceramic resistor. Check that out.

**Dave Jones:** Isn't that beautiful? And then, that goes into a MOV that goes down to these four five red devices here are the MOVs. So, it goes into the extra MOV there, and you notice that a tap goes off there over into the range switch.

**Dave Jones:** That's why they need the extra protection here, cuz this bugs off to a range switch that then ultimately goes off to the ADC somewhere. So, they're just protecting this extra input that they require for some reason over on the ADC input and range switching circuitry.

**Dave Jones:** But then, the other MOVs then, of course, come back here, and three There's our three series MOVs there, plus our extra one there, and they bugger off back to return back to the ground and input.

**Dave Jones:** Actually, I'm not particularly keen on this Fluke 27 with the return path for these MOVs. It actually branches down here, goes through this via down here, and then snakes its way through a couple of trace trace down here going back to the ground point, which comes from the wire.

**Dave Jones:** Not Not the best example on a Freading this particular case of a return path back to ground for the MOVs and the high energy impulse, but it's good enough to meet the cat ratings.

**Dave Jones:** And here's an example of a little high voltage isolation slot there between this particular terminal and this one. And we've got more high voltage isolation slots up here, cuz this is all past the input protection circuitry.

**Dave Jones:** This is still high voltage. In fact, these uh caps here are rated the these little uh trimmer caps here rated to 1,700 V. No coincidence. We've got four 430-V MOVs in series there, or roughly 1,700 V.

**Dave Jones:** So, there's still potentially some high voltage flowing around this part of the circuitry. So, they've whacked in a couple of high-voltage isolation slots as required. And it's not terribly easy to see down in there, but you can see the 10-A current shunt with its dual terminals here, which I've shown tapped off like that four-terminal measurement technique on that current shunt.

**Dave Jones:** But, you can see that these This is probably not the best example the Fluke 27 in terms of physical input construction. I chose it because of its uh schematic input, which I had available.

**Dave Jones:** Its physical construction is uh quite old-school, but once again, you can see some high-voltage isolation slots in there like that, and discrete input wires, say, from the amps Well, the amps jack goes complete straight into the fuse over there.

**Dave Jones:** High rupture capacity fuse down over there, into here, back to ground, through the shunt, and ah It's hard to follow, but you get the idea. And let's take a look at the Fluke 28 Series II, the modern replacement for the Fluke 27 we've just looked at.

**Dave Jones:** And it has a much tidier input circuitry here. But, let's see if it's similar after all these years. I mean, this the Fluke 27 was designed a lot many decades ago, whereas this Fluke 28 very recent.

**Dave Jones:** Now, here's our ground input jack, here's our voltage input jack, and um by the way, I'll mention this one this meter has actually had the snot blown out of it.

**Dave Jones:** We hooked it up If you've seen my previous video I did with Doug, we hooked it up to a real high-energy machine, and we blew the crap out of this thing.

**Dave Jones:** That's why the MOVs are blowing here and the PTCs uh seen the better days, but here we go. Here's our voltage input jack. Nice high voltage isolation slot. Look at that.

**Dave Jones:** They've They've gone right to the edge of the board. Cut that out completely around so it doesn't interfere with the fuse over here and right around like that. Beautiful.

**Dave Jones:** That's as good as you could expect. And then, look, exactly the same input circuitry. We have a thermistor RT1 there in series with a high voltage resistor. And there it is.

**Dave Jones:** I mean, they've got them the other way around, but it doesn't matter which which way you put them in. It makes no difference. And then, we have This one actually has three MOVs, so they've maybe got more spec'd in more modern MOVs or something like that cuz this is not Yes, this is actually a CAT IV rated device.

**Dave Jones:** So, this is actually a higher rated energy device than the Fluke 27, but it's got fewer MOVs because these are probably better rated. And once again, they've put a couple in series just to get the high voltage there.

**Dave Jones:** And they have also have that additional one. Here's that same ceramic uh that that same high voltage 1 meg ceramic resistor here. They've done it exactly the same again and the MOV.

**Dave Jones:** So, they've only They've just got two here instead of what instead of the four, which is what's on the 27. So, there you go. It's exactly the same high voltage cap here and that voltage input circuitry practically identical after all these decades.

**Dave Jones:** Fluke know that that is a good input protection scheme. And as for the fuses again, once again, high voltage isolation slots around there so it protects that circuitry there from the physical jack itself.

**Dave Jones:** High rupture capacity fuses, of course, you wouldn't expect any less. There's the 10 amp current shunt with the four terminal connection technique there. And what do you know? That bridge rectifier, and it looks like a single diode.

**Dave Jones:** So, it looks like they've got bridge rectifier with a single diode across there and there. So, they don't obviously don't need as higher voltage protection on this input as they did on the Fluke 27.

**Dave Jones:** But, it's all there. It's exactly the same configuration. And one thing you've seen me talk about before is blast protection inside the multimeter. Not only on the deep ribs that go in the case like that, so all the energy and any explosions are contained or are tried to be contained within the multimeter instead of when you're holding it, bang, and it blows your damn hand off.

**Dave Jones:** For those high energy circuits, then they can be designed if they're designed nicely, not only the deep walls there, but they'll have internal blast shields as well. Like this Fluke 28 Series II that just goes in there and actually fits between Look, it actually fits between these high voltage isolation slots.

**Dave Jones:** That that there matches up perfectly with that shape around there, and it physically separates everything. Not only with the air gap on the board there, the isolation slot, but physically the blast protection between the plastic in the molded case.

**Dave Jones:** That's a perfect example of a well-designed high energy CAT IV rated input protected multimeter. So, there you have it. There's actually not much to multimeter input protection. It all pretty much comes down to HRC fuses, isolation slots, little bit of circuitry to ensure that the fuses blow instead of the shunt resistors.

**Dave Jones:** On the voltage side, the PTC is one of the keys along with the MOV. So, if your if the multimeter you open doesn't have a PTC, a MOV, a bridge rectifier, and HRC fuses, then it's probably not designed as well as a quality Fluke.

**Dave Jones:** And it's probably a heap of garbage. So, this is a very good baseline to look at when you're evaluating a multimeter yourself to see if it's safe. If you've got some brand you've never heard of before, open it up, check it out, check out the high voltage isolation slots, the HRC fuses, bridge rectifiers, PTCs, MOVs.

**Dave Jones:** If it doesn't have all that sort of stuff happening and you know, clearage and creepage distances and all that sort of thing. If all that's not going on, then you know, it's just a one hung low slapped-together cheapy multimeter and they don't really know what they're doing and it's unsafe and really should only be used for mucking around on low voltage stuff, not high energy circuits.

**Dave Jones:** So, that's pretty much the basics of multimeter input protection. I hope you enjoyed that and if you want to discuss it, jump on over to the EEVblog forum. And if you like it, please give it a big thumbs up.

**Dave Jones:** Two thumbs up. I don't think you can do that. Catch you next time.
