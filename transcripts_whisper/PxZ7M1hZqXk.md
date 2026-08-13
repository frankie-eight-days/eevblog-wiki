---
video_id: PxZ7M1hZqXk
title: EEVblog #811 - How The Varta 15 Minute Battery Charger Works
url: https://www.youtube.com/watch?v=PxZ7M1hZqXk
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 37, "3": 55, "4": 73, "5": 91, "6": 109, "7": 121, "8": 133, "9": 157, "10": 175, "11": 199, "12": 217, "13": 235, "14": 253, "15": 271, "16": 289, "17": 301, "18": 319, "19": 331, "20": 355, "21": 373, "22": 391, "23": 403, "24": 421, "25": 433, "26": 457, "27": 475, "28": 487, "29": 505, "30": 523, "31": 535, "32": 559, "33": 577, "34": 595, "35": 613, "36": 631, "37": 649, "38": 661, "39": 685, "40": 697, "41": 727, "42": 745, "43": 763, "44": 781, "45": 799, "46": 817, "47": 835, "48": 853, "49": 871, "50": 889, "51": 907, "52": 925, "53": 943, "54": 961, "55": 973, "56": 997, "57": 1015, "58": 1039, "59": 1057, "60": 1081, "61": 1099, "62": 1111, "63": 1135, "64": 1159, "65": 1177, "66": 1201, "67": 1219, "68": 1237, "69": 1255, "70": 1273, "71": 1291, "72": 1309, "73": 1327, "74": 1345, "75": 1357, "76": 1381, "77": 1393, "78": 1417, "79": 1435, "80": 1447, "81": 1459, "82": 1477, "83": 1495, "84": 1513, "85": 1537, "86": 1555, "87": 1573, "88": 1597, "89": 1615, "90": 1633, "91": 1651, "92": 1669, "93": 1687, "94": 1705, "95": 1723, "96": 1741, "97": 1759, "98": 1777, "99": 1801, "100": 1819, "101": 1831, "102": 1855, "103": 1873, "104": 1891, "105": 1909, "106": 1933, "107": 1951, "108": 1969, "109": 1987, "110": 2005, "111": 2023, "112": 2041, "113": 2059, "114": 2077, "115": 2095, "116": 2107, "117": 2125, "118": 2149, "119": 2161, "120": 2179, "121": 2197, "122": 2215, "123": 2233}
---

**Dave Jones:** Hi. Back in EEVblog number 35, yes, that was in a galaxy far, far away, I tore down, had a look at this Varda fast battery charger, and for nickel metal hydride batteries. It can charge them in 15 minutes. And we took a look at that.

**Dave Jones:** Well, I've got the new one, the upgraded model to this thing, so I thought we'd just tear it down, see if anything's changed between this original model and this new one. Let's check it out. Now the first thing that's changed between these is the input plug packet rating.

**Dave Jones:** The old one here had a 15 volt DC plug packet, 4.7 amps, so basically 75 watt plug packet was actually supplied with. This one, even though the charge rate's exactly the same, is only supplied with, here it is, a 45 watt plug pack.

**Dave Jones:** It's the same 12 to 15 volt input, you do actually get a car charger lead with it, so you can actually recharge your batteries 15 minutes in the car, which is very handy. But it's only 45 watts maximum plug pack. Still, that is a decent sized plug pack.

**Dave Jones:** Am I the only one who hates plug packs with these stupid ears on them? Why? What does that do? It's just a pain in the arse, it just fouls with ones next to it, argh. And the other main difference is, if I power it on, this one has

**Dave Jones:** a funky LCD here, backlit, blue, ooh, fancy-pansy, that's got individual voltage and current readouts for the individual charging on each cell here, whereas the old one just had you know, nothing at all, just 4 LEDs, that's it. Bob's your uncle. And it had these rather

**Dave Jones:** nice little contact terminals here, and just like the old one, it's got a fan in here, it has to to keep these things cool, so that just sucks that in from the bottom. I do like this design here, if you put the batteries

**Dave Jones:** in like this, it just allows you to get your finger in there and just pop it out. That's a really nice touch. Anyway, it needs a fan because these batteries are going to get hot. You can charge these up to 70% of their capacity in 15 minutes, it's got an 8 amp charge rate.

**Dave Jones:** Unbelievable. And for those who haven't seen it, here's the Vata Ready to Use, they call them. They're basically equivalent to the Sanyo Any Loops, which everyone knows. These are long-life batteries, these particular ones, you charge them and they still retain 75% of their charge after a year.

**Dave Jones:** Not quite as good as the latest generation Any Loops, but you know, not too far off it. This is 2100 mAh capacity, this is what came with the charger but they are available in up to 2600 mAh capacity. But the amazing thing about these is that

**Dave Jones:** well, these batteries and this charger is that they actually charge at 8 amps. 4 times what's called 4C, or 4 times the capacity rating almost. You know, 2100 mAh times 4 is going to be 8.4, but you know, near enough to 4C. For the Sanyo Any Loops, the fastest charger I've seen, and please correct me if I'm wrong, is just 1C.

**Dave Jones:** Or even, I think Sanyo's fast charger in quote marks for the Sanyo Any Loops is just under 1C or something like that. So it takes much longer to charge the Sanyos. But I suspect there's actually nothing special about these Vata Ready to Use ones

**Dave Jones:** that enables fast charging. I reckon you can probably do it with the Any Loops too. I think they're actually pushing these things beyond their, you know, I don't want to say beyond their design capability but you're not going to get the, I don't think, I haven't tested this, but I don't think you're going to get

**Dave Jones:** the claimed number of recharges on this if you abuse them basically by charging them at 8 amps. But, you know, it's still going to work. You can actually charge these super quick. Now, I tried but I couldn't find it, so please, if you can find it, please link in the data sheet to these Vata

**Dave Jones:** Ready to Use batteries. I could not find it for the life of me. Maybe I'm just dumb and I missed it. But anyway, I've got the Sanyo Any Loop ones here, and it says the fastest charging rate here, fast charge, is 2000 mAh for basically a 2000 mAh

**Dave Jones:** typical cell. So that's a 1C charge rate. So it doesn't say that you can actually charge it any faster than that. Presumably because that's what their specification is for the 1500 recharge cycles or something. You know, you've got to charge it at 1C, but if you have a look at the charge and discharge curves

**Dave Jones:** here, it does actually show you, look, the charge rate at 2000 mAh, so 1C. But of course the discharge curve, they actually have a discharge curve for 2C or 4000 mAh. So if you can discharge it at 4 amps, why can't you charge the thing at 4 amps?

**Dave Jones:** So it basically you know, they don't tell you this in the data sheet, but it comes down to the fact that typical metal hydride batteries, be it the Sanyo Any Loops or some of the others or these VARTA ones, can most likely be charged

**Dave Jones:** at a higher rate, a much higher rate than the 1C. But you're probably not going to get the full number of recharge cycles out of them. But if you don't care about that, and you want your batteries charged in 15 minutes or half an hour or whatever, then you can probably do it.

**Dave Jones:** Now this charger is really funky. Not only does it have individual cell charging, which the cheaper VARTA battery charger for these things, which is like half the price, does not have. You have to actually put two in series. But of course that's not going to work when you're charging the damn things at 8 amps like this puppy does.

**Dave Jones:** So it's got individual cell charging, individual temperature sensing, which as we saw on the previous demo, and I'm sure when we do the teardown in a minute, we'll find individual temperature sensors connected directly onto the pads down in there, or probably, I don't know, maybe this one down the bottom or something

**Dave Jones:** like that. It's got to be connected right on there to get the thermal heat transfer as efficiently as possible down through the temperature sensing. Because when you're charging them at a super high rate it's critical that you measure the temperature, so you have individual cell temperature cut off with this thing

**Dave Jones:** as well. And yes, this can do double A's and triple A's and triple A's charge at a nominally slower rate because it's got a separate contact down in there. But the great thing about this charger is we'll whack it in, and here we go, it's charging.

**Dave Jones:** And it's actually got 8000 on there, so it's actually charging at 8 amps and we can actually put 2 in and it'll charge 2 at 8 amps, but eh, it won't do, our plug pack cannot supply the power, the internal charging circuitry cannot handle it

**Dave Jones:** if you want to put more in, bingo, it changes them all to 4 amps, so it halves. But you can charge all 4 at 4 amps, or twice at 2C. But if you only want 2 of them I like that, just get your finger under, that's a beautiful design, it's absolutely beautiful.

**Dave Jones:** Look at that, in any of the combinations of the spacers here, you can get 4C charging, absolutely incredible. And I'm not sure if you can hear that fan going, it's not massively loud, I think the old one was louder, but it is distracting if you use it in a quiet

**Dave Jones:** environment. But it's got it, you've got to get the airflow over these to attempt to at least cool these things down because that is a massive charge rate, 4C. Now it's actually got different display modes, that was the charging current now we're looking at the charging voltage here, these are already charged, it's probably about to cut off

**Dave Jones:** any second, I'm not sure what cutoff voltage they're going to cut off at, but very close. And it will also tell you the accumulated charge as well, there we go, 137, it's counting up. So how much charge we're actually putting into these things, it's able to measure that.

**Dave Jones:** And if you have a look at the modes here, it's charging at the moment, well we can change it, we can actually discharge the batteries as well, so it's going to have a load inside there that we can discharge, the previous one I don't think had that, it was just purely

**Dave Jones:** discharges, so that's very nice. But not only have we got discharge mode, we've also got refresh mode as well. And what refresh mode will do is it will actually discharge the batteries and then recharge them just so, you know, like cycle the batteries, so it attempts to get some extra life out of it, whether or not

**Dave Jones:** that's, you know, it's going to do the business, I don't know, you'd have to go into the chemistry of the electrochemistry of this particular type of VARTA battery and whether or not that's worthwhile. But anyway, you've got that mode, and you've also got test mode as well.

**Dave Jones:** And what test mode will do, what it's doing now, is it's showing 2000, so it's discharging at 2 amps. Discharging these batteries, as soon as it's finished discharging, just like the refresh mode, it'll start charging up again, but when it charges up it will actually add up and calculate the accumulated capacity in the cell, and it'll give you

**Dave Jones:** a readout for the milliamp hour capacity of the cell. Once it, like, it's going to take some time to fully discharge this at 2 amps and then recharge it, but hey, we can actually, it's a battery capacity tester. Fantastic. But hey, that capability basically comes for free, because it's basically a software function.

**Dave Jones:** If you add in the ability to discharge these cells, well, it's just, you know, a micro software stuff that just calculates the milliamp hour capacity and can do that sort of stuff. So, you know, no surprises that they've added that. And naturally this thing has all the bells and whistles, it's got to be safe in terms of

**Dave Jones:** charging, so it's got negative delta V cut off, and it's going to have, as I said, individual temperature sensors on the contact terminals here, so it's going to have temperature delta cut off as well, because, you know, once these batteries hit, like, I believe it's like around about 1 or 2 degrees

**Dave Jones:** C per minute temperature change, then you know they've basically reached their full charge and you need to cut them off immediately. You don't want these things to go completely thermic and explode on you. And that is a poor attempt to try and keep us out.

**Dave Jones:** We can fix that security screw. And I can get these ones out, but unfortunately, the hole down in the shaft down in there is just too narrow to actually fit the entire shank of this thing, this security bit in there, so it doesn't work.

**Dave Jones:** But here's one I prepared earlier. Nothing you can't fix with a Dremel. And ta-da! There it is, we're in like Flynn, and it wouldn't surprise me if this is very similar or the same as the previous model, although we didn't have that quite flat pack last time, I don't think.

**Dave Jones:** We can see where they've removed solder mask all around here, that's to, and then to get some solder coating on that, just increase the current handling capacity of these tracers just a bit. You don't want to spend extra coin for, you know, the 2 ounce thick copper on your PCB, no siree Bob.

**Dave Jones:** So you just remove some solder mask and let the solder coat do the business there. Not as effective as, you know, proper thick copper, but meh, does the job. And this board's actually fairly easy to lift out, so it's a double-sided load. And ta-da!

**Dave Jones:** We can see there's our MOSFETs obviously, down in there for our individual driving channels. We've got two per channel here, or is it one separate one, one for AA, one for AAA contacts, I'm not entirely sure. We've got right angle charging contacts on there, here's the springy ones at the back, there's nothing fancy going on there, it's just, you know

**Dave Jones:** spring metal. And bingo! There is our temperature sensor, looks like they've got diode temperature sensing right down on the contacts down in there. You've got to have that for a fast charger like this. Absolutely critical, otherwise your batteries will explode and catch on fire

**Dave Jones:** So just silicon diode temperature sensing like that, you know, it's good enough for the crude type of stuff we're doing you know, it's roughly, what is it, 10 millivolts per degree C temperature coefficient, if memory serves me correctly, for a regular silicon diode, it's just good enough, you know

**Dave Jones:** you want to measure that temperature differential, that change over, you know, the span of a couple of minutes You don't have to be, you know, 0.1% accurate on your bloody temperature, so you know, they're going to do the job Actually I think I'm going to stand corrected on that, it's not a silicon diode, it's a DO35

**Dave Jones:** glass package, similar to what some diodes come in, but NTC gives it away here negative temperature coefficient, that indicates this is a thermistor, and you can get thermistors in DO35 glass packages like this, so that's what it must be, so they're not just using a silicon diode there

**Dave Jones:** And this might look a bit strange here, how they're splitting around these contacts here but what they're basically doing is they, you know, these pads are shorter, they might look like they're like isolated some sort of, you know, four terminal sense measurement or something like that

**Dave Jones:** they're actually shorted out just like this one, you'll notice that all the copper is basically this terminal here they're using all of the available space right around here, so this is, this trace here on this side is for this terminal here, and this one on, well if we can flip it

**Dave Jones:** can we flip it over? I'm not sure, yeah we can, there we go, and this one here is using this top side Okay, so this one goes on the bottom side, this one here goes on the top side all the way across and likewise for these two over here, you'll notice that this one here is for, is it for this terminal here?

**Dave Jones:** Yes it is, and all this on the bottom here is going to this terminal over here So, you know, they have to do that, they've got to fit around the fan, you've got this huge big cutout for the fan which is absolutely mandatory, you've got to have it right over the batteries, so they had to use

**Dave Jones:** all the space there, and they can just snake the little temperature sense terminals right around the outside there just. Now this is interesting, these two pins here are the triple A terminals and these two here are the double A terminals, and you notice there's just some parallel resistors

**Dave Jones:** there, there's actually three on this side, and they, are they 1R0? 1 ohm? I think they're are they three 1 ohm resistors in parallel? And it's got another three I think on the other side as well And I can't actually see any voltage tap directly off the double A terminal

**Dave Jones:** either on the bottom here or the top, but what they're doing is you can actually see this trace here going from R79 there, that is actually tapping off right under the triple A terminal which is fine, okay, so you're voltage sensing the, you know, four wire terminal sensing

**Dave Jones:** so to speak, the triple A terminal here, but if you don't have the triple A battery installed, then these 1 ohm series resistors, or less, because you've got them in parallel, you know, sub, you know, hundreds of milli-ohms, in series is not going to matter

**Dave Jones:** so you're essentially directly tapping off the triple A terminals as well, that's neat, so they're not you know, they're not bothering to actually tap separately the triple A and the double A you can actually do it in one, that's actually quite elegant. And you can forget about finding out what that

**Dave Jones:** actually, it's a micro, it's got to be like a off-the-shelf micro, but they've rubbed the numbers off it so, and all the, you know, the hand solder connections, oh, very how you're doing, quite ugly you know, very messy work, not hugely impressed by that.

**Dave Jones:** And you can see the solder thieves there, those pads, those large pads, these are designed so when this thing goes through the soldering process, then it just bleeds some of the solder off there, or thieves the solder away, so you don't get shorts on the rest of the pins, I've covered that in previous videos

**Dave Jones:** so obviously this board was wave-soldered, it needs to be wave-soldered to get all the extra solder on these pads here, so double-sided, all these components would be stuck down with glue you can actually see the glue just oozing out from the bottom of those parts there, so they're going to stick those down

**Dave Jones:** before they wave-solder this thing, of course, otherwise they just float off into your solder bath, that'll ruin your day And we've got ourselves a TL494, not a genuine Texas Instruments, it's a UTC one, but whatever, that's a pulse width switch mode controller, and that's handling all the switch mode on top, we've got to have a switch mode, because

**Dave Jones:** massive amount of power involved here. So that TL494 under there is controlling our switch mode controller here, we've got a massive inductor on the top here, that looks quite nice, we've got a switching tranny over there, is it? Yep. And that is an

**Dave Jones:** SPD50PO3 for those switching tranny fanboys, there you go. Woo! And the load control MOSFET's in there, there's a new one, DTM4410 from a manufacturer I've never heard of, and I think Dintec. Go figure. And check it out we don't need no stinkin' common mode joke, no, we'll save a couple of cents, just put a couple of links in there

**Dave Jones:** Alright mate, no worries. And I love this here, look, they've put in this link from over here they went, PCB designers went, oh no, I can't get enough width through this channel, I've got to snake this signal connector through here, dammit, can't meet my current trace requirement

**Dave Jones:** with that particular width, and well, they won't let me spend the extra dosh to buy a 2 oz board, so ah, we'll just whack in a link, she'll be right. Now I've done a little bit of reverse engineering on one of the channels here, and it's a rather unusual arrangement.

**Dave Jones:** What we've got is 2 N-channel MOSFETs like this across the battery holder, directly across the AA battery holder, and we've got our DC to DC converter, and which I believe is a constant current source, and it's going into the center tap of this kind of like, for want of a better word, a

**Dave Jones:** totem pole type arrangement here, and I've drawn in the internal body diodes of the N-channel MOSFET, and if you've watched previous videos I've done, you should know that N-channel MOSFETs, or MOSFETs like this, have a, what's called a body diode, a parasitic diode inside, it's inherent in the physical construction of the diode itself, and I won't go into the

**Dave Jones:** physics of how it happens, but it's basically a reverse biased diode like this, and you know, you might think, okay, what they're doing here, you might think is actually quite clever, they're actually, this is a constant current source, current's flowing into here, and you might think that because this is an N-channel

**Dave Jones:** MOSFET, they can't turn that on, and they're actually using the body diode like that to force the charge current through the battery like that. But that's not really what's happening. This N-channel MOSFET will actually turn on, it's not a more typical arrangement you might be familiar with, because obviously the voltage at this, the output of the

**Dave Jones:** AC to DC converter, the voltage here, the compliance voltage right there, is going to be larger than this AA battery. Okay, so you might think that, you know, they should be using a P-channel in here, but an N-channel's still going to work, as long as the VGS, the gate source voltage, this is the gate terminal, this is the

**Dave Jones:** source, this is the drain up here, as long as the differential voltage between the gate and the source is positive and it's above the threshold value, then the MOSFET will effectively turn on. And then current can actually flow your more traditional way through from drain to source, but can also

**Dave Jones:** flow from source to drain as well, no problems whatsoever. So the constant current, assuming that this in charge mode, this MOSFET here is turned off, then all the current will flow through the N-channel MOSFET and bingo, down through your battery like that. So they're not actually using

**Dave Jones:** the body diode there, which at first glance you might think so, but they're not. Because this control voltage from the VGS, I mean they've got, you know, the 5 volt supply for the microcontroller or whatever in there, they're going to have enough voltage in there to actually turn on this

**Dave Jones:** N-channel MOSFET and it's going to conduct, in this case, it conducts, flows in and around and charges the battery. Neat. And of course if you want to discharge the battery, well, you can do that too. You just switch on, you switch off your DC to DC converter, which is your constant current generator, and then you turn on both

**Dave Jones:** of these MOSFETs and you can drain the battery. Too easy. But the interesting thing about this is that regardless of the gate voltage here, you can put this right down to 0, it doesn't matter and this MOSFET is switched off, you're still going to charge your battery because this is a constant current source.

**Dave Jones:** It will then use this body diode, it might blow the crap out of the MOSFET depending on how capable that body diode is, because that's, you can, you know, a lot of people do use the body diode for various things, it might be clever, but yeah, you gotta really know what you're doing.

**Dave Jones:** But in this case, even regardless of VGS, it will still actually charge the battery. It's just that the voltage here at the source will actually rise by this diode drop. Let me try and explain what I'm talking about here. Now I've got the voltage on the

**Dave Jones:** gate here, okay? Let's assume it's 5 volts and that's enough voltage to, you know, overcome the gate the VGS threshold and switch this MOSFET on. When the MOSFET's on, it's basically you know, 0 ohms, okay? It's a short circuit, it basically switches off and on.

**Dave Jones:** So at 5 volts the MOSFET's on, and the body diode's effectively shorted out. So all the current flows through here like this. So the voltage at the source pin right here, okay, this is actually going to be exactly, because this is a short circuit, it's going to be exactly the same as the charge voltage on the battery.

**Dave Jones:** Which is, let's say it's 1.6 volts, okay, due to the electrochemistry of the battery at whatever particular current it happens to be charging at at the moment. Now if you come along and actually switch VGS down to 0 like this, the battery will still keep charging.

**Dave Jones:** I should actually so I-BAT, I should actually put that in here like this. I-BAT will basically stay, if my pen works, completely constant. Let's say it's like the 8 amps that we've actually got in here. It's regardless of what VG does, the battery

**Dave Jones:** is still going to stay the same. But VGS will actually rise, instead of being the voltage directly across the battery, it'll rise by the voltage of the body diode. Okay, so the forward conduction voltage of that body diode. So it might be like

**Dave Jones:** 0.6 volts for example, so it'll rise up, jump up to 2.2 volts. And so this point here is now 2.2 volts. But it doesn't matter, because it's a constant current source, it's going to drive that constant current through the battery. So it's going to stay the same.

**Dave Jones:** So to actually switch off the charge current, they can't just drop VGS down to 0 and try and turn off this MOSFET, it's not going to work. They have to actually turn off the output of the constant current DC to DC converter generator here.

**Dave Jones:** If we have a look at the thermal image here with our FLIR camera, we're looking at like the battery, I've only had it on there for a couple of minutes, it's already at 55 degrees. You know, I'm not counting for you know, emissivity and everything, I don't have the exact value.

**Dave Jones:** But anyway, you can see it and the board over there, very similar type of thing, you know, 50, you know, some of the diodes, I think I'm pointing at the diodes there, seem to be the hottest there. But yeah, she's a bit toasty.

**Dave Jones:** I think the emissivity on that battery was a little bit off, because yeah, I can hold that. So it definitely wasn't at over 50 degrees. And as I showed earlier, just for the AAA battery holder here, they've just got those resistors, they were like 1 ohm, so just multiple resistors in parallel in there.

**Dave Jones:** I think there was like 6 of them, 1 ohms each or thereabouts, and then the voltage sense is coming off that. So if you don't have the AAA battery installed, then you know, there's no problem having you know, a 0.2 ohm resistor or something in series with your voltage sense line, because this is a high impedance input to your analog-to-digital

**Dave Jones:** converter, so no problems whatsoever. So they're tapping off the voltage directly from the either pad there. That's rather clever. Actually I just remember I do a very similar thing on my microcurrent as well. By the way, I forgot, this is genuine DaveCAD, except no

**Dave Jones:** substitute. Now I can see some glue on that board, but nobody's home. And I actually just thought that I had these resistors for the AAA here back to front, but because like I'm going where is the current sense resistor for this thing, so they know what current they're actually

**Dave Jones:** you know, charging and discharging at. But yeah, I know, I double-checked, that's definitely right, if you don't plug in the AAAs, that those resistors the main charge current is not flowing through there. So yeah, I don't know how they're doing that. Now at first I just assumed that this point, the negative terminal batteries, was just connected to ground, but

**Dave Jones:** I decided to go down the rabbit hole a bit further and have a look at the arrangement of all the various battery holders. Now what I found is this top part up here, okay, is exactly the same configuration that we looked at before, but instead of going down to ground, it's actually

**Dave Jones:** a cascade arrangement like this. Now I've got battery holder number, I call this like battery holder number 1 up here and then 2, 3, and 4. So I've got 1, 2, 3, and 4 here, and the negative terminal of battery number 1 here, instead of going down to ground, it goes to

**Dave Jones:** just like the DC to DC constant current output goes into the center point of the n-channel MOSFETs here, it also goes into the n-channel MOSFET. And likewise, this one, the negative terminal battery goes to the center point once again. So it's basically a

**Dave Jones:** series arrangement, so they are actually charging these things in series. So the DC current here at the 8 amps goes through this n-channel MOSFET, turns on through the battery down here, once again through this channel, MOSFET is turned on through the battery, etc.

**Dave Jones:** etc. And of course if you don't have the battery installed in any of them, it can detect that and basically they can turn on the MOSFETs to, you know, so you've got individual control over these MOSFETs, you can just switch, if this battery is not installed here, you can just switch on this

**Dave Jones:** MOSFET here, boom, straight down, and then boom, straight down, boom, straight down, and then this one here, you turn on this MOSFET, and bam, you charge this battery here. So it's quite a clever arrangement, I rather like it. But what I couldn't find on the circuit, and I haven't

**Dave Jones:** done a complete reverse engineering here, haven't gone in-depth, but I've had a quick look and I cannot find any way that they're actually measuring the individual battery current, especially the battery discharge current, because of course in this arrangement you can switch on the

**Dave Jones:** two transistors and you can discharge your battery like this, no problems whatsoever, you can discharge this one, this one, but I don't see any mechanism in here, no current shunt resistor in here to actually do that. The AAA battery, it's separate, it's got the sense line, let's assume you've got the AA, then there is no current

**Dave Jones:** sense resistor that I could find anyway in here. So, like, are they doing it really dodgy, brothers, and using the on-resistance of the MOSFET to get, you know, like, really, you can kind of sort of do it in a rough and ready way,

**Dave Jones:** but that is such bad design practice, you know, I don't know, but maybe it's good enough. Or, then I thought, oh, maybe it could be a sense, what's called a sense FET, which actually is a regular MOSFET, but actually is part of the silicon in there, it's actually got effectively

**Dave Jones:** an internal sense resistor, internal current shunt resistor as part of the silicon, which allows you to actually measure the current flowing through your actual MOSFET itself without having an external resistor. But, hey, no, that's not the case here, this particular MOSFET is just like a Joe Bloggs, you know, high current N-channel enhancement mode

**Dave Jones:** MOSFET, so nothing fancy there at all. So it's not a sense FET, so I don't know how they're actually measuring the discharge current of the battery. But I did find the current I do believe the current shunt resistor, that one down there, that little one, that one

**Dave Jones:** in there, I think they're using that as a current shunt resistor right down the bottom so that they can well, that's probably most likely feeding back because of its location here, that's actually part of the feedback loop for the constant current generator here.

**Dave Jones:** So they're actually using that to generate the constant current, so that'd be tapped off and then measuring that. But yeah, individual currents I don't know. And as for measuring the sense voltage, as I said before, you can tap in the sense voltage directly off the terminal here, which is fine, but how do you

**Dave Jones:** get the, you know, the direct, like, 4-wire measurement across the battery? You know, we're talking high currents here, so you need, like, a direct measurement. Well, they've got the thermistor in here, so there's the 4 thermistors, they're actually connected to the negative terminal, so are they, if you feed the output of that thermistor

**Dave Jones:** like up here with this sense resistor here, well this dropper resistor for the AAA batteries here, then are they actually using that into a high impedance source to actually measure the voltage at this point? In that case, they've got their two voltage taps across each battery here, so they could actually do that.

**Dave Jones:** But then you've got to use your thermistor as also, you've got to have it into a divider or a lower impedance arrangement so that you can actually measure the temperature. You can actually use the thermistor as, you know, as it was intended to

**Dave Jones:** actually do that. So I, you know, to measure the temperature, are they switching between them? I don't know. Because if you had this, just this single-ended tap voltage on here on the battery just going into a single-ended analog-to-digital converter, then well you've got all the losses in your shunt resistor and your MOSFETs and all your other connections and everything else,

**Dave Jones:** it'd be horribly inaccurate. So yeah, I'm not quite sure how they're doing the sensing there. I can't really figure it out on first little reverse engineer there. Now I'm actually discharging two batteries here, and if you have a look at the display, you can see that we've got different values there, and it does vary.

**Dave Jones:** So it's continually monitoring the discharge current, so it must know, must be able to measure and calculate the current through each of those batteries. So yeah, they must have independent current measurement somehow, but I can't see it. So there you have it, there's a little look

**Dave Jones:** inside the Vata 15 minute 8 amp battery charger. Can you believe it? 8 amps into a regular, well I believe they're pretty much regular nickel metal hydride, although they are the ready-to-use long shelf life type. But I don't believe these things are actually

**Dave Jones:** specced at the full 8 amps current. So you know, they're just basically overcharging these things. And as I said in my original video number 35, I greatly doubt you're going to get the full number of charges, what is it, like 500 or something

**Dave Jones:** rated for these that you'd get if you actually charged them in the fast charger as opposed to the regular slow charger, which is the recommended value to charge these nickel metal hydrides at. It would be interesting to know if you could actually fast charge the

**Dave Jones:** Sanyo Anyloops as well, because I can't necessarily see why not, if they can do it to this. I don't think there's any magic secret sauce in this. So I think you can probably do it to Anyloops as well, but I don't know of any data out there of, you know, people or products actually really fast charging

**Dave Jones:** the Sanyo Anyloops. So if you've got any data or stuff on that, then yeah, please leave it in the comments. But once again, if you did overcharge the Sanyo Anyloops and, you know, you're using a charger like this, it's got the proper protections, it's got over temperature, it's got negative delta V

**Dave Jones:** it's got, you know, it's got all the protections possible so that you don't actually, so these things don't actually catch on fire when you charge them at 8 amps. Because remember, nickel metal hydride batteries are exothermic. So if you didn't actually temperature sense them and cut them off when they were fully charged, they can run away

**Dave Jones:** on you and well, I don't want to know what would happen. Hmm. So I don't have any Sanyo Anyloops to hand. I've been using these Vata ones. They seem to work really well. I haven't, you know, put 500 recharges on them to actually, over the years, to actually see if, you know, the

**Dave Jones:** battery life drops, number of cycles drops on them. The Sanyo ones would drop, what are they rated for? Like 1500 charges. You'd never get that if you, I don't think, if you were charging them at 8 amps. The datasheet exists here for a reason, you know.

**Dave Jones:** There's a reason why it says, you know, only charge at 2 amps. There it is. So yeah. Like, disobey that at your own risk. And that's what Vata are doing. But this isn't a genuine official Vata charger. So, you know, they, I guess they have to stand by it.

**Dave Jones:** But as it stands, the circuit is a good example of a real minimalistic and rather clever implementation to get individual cell charging and discharging using these MOSFETs. So I'd love to do a better reverse engineering. And if anyone actually already has, knows of a schematic or anyone who's done

**Dave Jones:** any reverse engineering on this, then please let me know. At the moment I don't have time, I just want to get this video uploaded. So I might have a second shot at this, might have another look around here to see what's what and how they're doing

**Dave Jones:** with the individual cell discharge currents. And also the voltage sensing as well. Because I think it's all a bit, you know, I expected individual charge, you know, circuits for each one and proper differential voltage sensing and all that. And it just seems to be a bit rough and ready.

**Dave Jones:** But I, you know, they're doing, they're getting away with it. And you know, they're doing. So you know, they've got to stand behind their product. And the charger works. I've been using it for years, or at least the previous generation one. But yeah, I don't know.

**Dave Jones:** I haven't had one catch on fire yet. But fingers crossed. So you've got to wonder, did marketing like come up with this, oh we'd love to have a 15 minute charger. But Sanyo's not doing that. Let's come up with that. You know, really super duper fast, four times faster than what

**Dave Jones:** Sanyo can do. Let's do that and engineering go, oh well, you know, I don't know. The bloody battery chemistry's not going to get the same life out of it. It's a bit dodgy, but oh yeah, we can come up with something. And it's got to be cheap too, so you know, they've implemented it cheaply and yeah, okay.

**Dave Jones:** It kind of, yeah, kind of, sort of works. Anyway, if you like that video please give it a big thumbs up. As always, you want to discuss it, EUV blog forum, YouTube comments, or blog comments, all that sort of jazz. Catch you next time.
