---
video_id: _QpApuKdcqQ
title: EEVblog #723 - Keysight 34470A 7.5 Digit Multimeter Teardown
url: https://www.youtube.com/watch?v=_QpApuKdcqQ
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 33, "3": 45, "4": 56, "5": 71, "6": 88, "7": 100, "8": 113, "9": 129, "10": 151, "11": 165, "12": 186, "13": 200, "14": 213, "15": 230, "16": 250, "17": 266, "18": 280, "19": 291, "20": 304, "21": 313, "22": 343, "23": 355, "24": 369, "25": 385, "26": 401, "27": 419, "28": 431, "29": 449, "30": 465, "31": 471, "32": 481, "33": 504, "34": 527, "35": 539, "36": 551, "37": 565, "38": 576, "39": 589, "40": 601, "41": 608, "42": 623, "43": 635, "44": 645, "45": 657, "46": 669, "47": 686, "48": 704, "49": 720, "50": 740, "51": 753, "52": 762, "53": 772, "54": 781, "55": 793, "56": 812, "57": 827, "58": 838, "59": 848, "60": 857, "61": 873, "62": 884, "63": 896, "64": 907, "65": 917, "66": 929, "67": 946, "68": 961, "69": 976, "70": 992, "71": 1003, "72": 1013, "73": 1026, "74": 1037, "75": 1062, "76": 1073, "77": 1087, "78": 1098, "79": 1119, "80": 1137, "81": 1152, "82": 1165, "83": 1178, "84": 1200, "85": 1208, "86": 1220, "87": 1234, "88": 1252, "89": 1262, "90": 1286, "91": 1296, "92": 1307, "93": 1316, "94": 1327, "95": 1339, "96": 1350, "97": 1364, "98": 1378, "99": 1395, "100": 1407, "101": 1422, "102": 1438, "103": 1449, "104": 1461, "105": 1492, "106": 1506, "107": 1523, "108": 1534, "109": 1547, "110": 1559, "111": 1574, "112": 1585, "113": 1598, "114": 1607, "115": 1616, "116": 1642, "117": 1663, "118": 1672, "119": 1687, "120": 1698, "121": 1713, "122": 1723, "123": 1737, "124": 1754, "125": 1766, "126": 1781, "127": 1791, "128": 1811, "129": 1823, "130": 1833, "131": 1847, "132": 1859, "133": 1875, "134": 1885, "135": 1899, "136": 1911, "137": 1922, "138": 1934, "139": 1950, "140": 1964, "141": 1974, "142": 1983, "143": 2001, "144": 2009, "145": 2022, "146": 2033, "147": 2047, "148": 2057, "149": 2070, "150": 2082, "151": 2095, "152": 2104, "153": 2121, "154": 2137, "155": 2145, "156": 2159, "157": 2179, "158": 2189, "159": 2204, "160": 2220, "161": 2245}
---

**Dave Jones:** Hi, welcome to another teardown. This one's been anticipated on the forum ever since somebody on the forum actually found out about this puppy before it was released. It's the new Agilent Keysight.

**Dave Jones:** Look at this Look at this ridiculous looking logo. Isn't that the most boring, pathetic looking, bland, black logo you've ever seen? Unbelievable. Anyway, this new 34470A seven and a half digit multimeter.

**Dave Jones:** Agilent Keysight. have never made, actually, a seven and a half digit multimeter before, apparently. They've done the six and a half digit ones with the new 34461A series we've seen before.

**Dave Jones:** They've also done, of course, their famous eight and a half digit, you know, transfer standard meter. But, this is their first entry to the seven and a half digit market.

**Dave Jones:** And, of course, they're using the same model and form factor as the 34461A. It's their true volt series. So, they're now actually got two models. There's also the 34465A, which is around about 1,400 bucks.

**Dave Jones:** And, it's a six and a half digit one. It's got in some improvements over the 34461A. Which All these bloody model numbers, so confusing. Anyway, we've looked at the 34461A before.

**Dave Jones:** There's the new 34465A, which is a bit more expensive. And, there's a couple of people on the forum actually who've traded in already their almost brand new 34461A for the 65A.

**Dave Jones:** So, cuz it offers some nice advantages for not much extra cost. Anyway, this one is 2,900 US dollars or thereabouts. That's the street price that I found. And, it's for the seven and a half digit model.

**Dave Jones:** So, and it's got some nice new features on it which I'm really interested in seeing particularly the current range. It's only still only got the 3 amp jack on here, but it actually has a 1 micro amp full scale current range.

**Dave Jones:** Wow, so I can't wait to do a review on this and have a play around with that. But anyway, that's not what we're doing today. We're going to take a look inside cuz a lot of people have been asking what is the voltage reference used inside this thing cuz it's a lot better than the 34461A and also the 65A which still uses the LM399.

**Dave Jones:** And we suspect this one doesn't use the LM399 cuz it's specs probably not good enough. The specs are too good to be using that reference which is it's like they quote about 16 ppm basic DC volts accuracy or something for this thing.

**Dave Jones:** Pretty kickass meter and it's reasonable value for a 7 and 1/2 digit meter at the you know almost 3 grand price point. Yeah, it's not sort of you know hobbyist or your basic lab pricing, but hey, you know, when you're paying for 7 and 1/2 digit meter, you're paying for the huge performance in the thing.

**Dave Jones:** And as you can see practically identical to the 34461A here. So, nothing is really changed except this one it does have auto cal you can go shift auto cal like that.

**Dave Jones:** That one the 61A doesn't have that, but apart from that everything looks identical and absolutely no difference on the back either. If I swap those over, you wouldn't have even known which one's which.

**Dave Jones:** So, you know, what we say here on the EV blog, don't turn it on, take it apart. And here we go. Of course, we expect it to look near identical to the um previous one the 34461A.

**Dave Jones:** Ta-da! We're in like Flynn. at that. Isn't that really neat and tidy? I've mentioned this before with the 34461A teardown, but that is just Yeah, that is just gorgeous construction, well-thought-out, and nice tidy wiring on their uh mains transformer there.

**Dave Jones:** Got a good old-fashioned uh linear one there. I like that. Although, there is a switch mode down in there. Hmm. Let's We'll get into that, but yeah. That's uh all the magic is going to happen under Aha!

**Dave Jones:** That I think I might see the magic under the shield here. There's some sort of plastic holder. That's got to be the reference. That's got to be it. Absolutely.

**Dave Jones:** So, yeah, let me uh try and take that off and uh we'll be in like Flynn cuz everything looks pretty much the same as what we've got last time.

**Dave Jones:** So, I probably won't go through all the details. It looks near identical and a nice huge HRC fuses over here. Absolutely massive there. Fairly easily user-replaceable. There's only three screws to get this uh case cover off.

**Dave Jones:** There is a bit of a trap for young players. These little clips here, um you've got to sort of like pull this out a bit before the case will actually pull off.

**Dave Jones:** So, it's a bit annoying and uh and not obvious at first. Anyway, um Seba brand fuses in there. So, they have spared no expense. We've got our uh tellurium the exactly the same uh uh custom-molded uh tellurium copper uh contacts low thermal EMF uh contacts front and rear, of course, and uh and the big physical uh clunking switch in here going into this ganged switch down here, which then um Well, it's not

**Dave Jones:** ganged switch. It's a uh just a multi uh multiway switch down in there, which uh switches between the front and rear panel terminals and everything looks very similar if memory serves me correctly.

**Dave Jones:** Of course, I'll have all the high-res photos available on eevblog.com and you'll be able to compare it with the 344 uh 61A. Got ourselves a nice spark gap over there, nice isolation slots.

**Dave Jones:** Anyway, that is just gorgeous and I also loved how My point is gone. I loved how they have these little um uh hooks in here. The board just starts slides into these hooks and then just slides forward and out of the case.

**Dave Jones:** It is very, very nice, but that's what everyone wants to see. That's the money shot under there. Let's get to it. Check this out. This is really interesting. This is more than what I expected in this thing.

**Dave Jones:** I expected like a just a Linear Tech LTC-1000 voltage reference and we might still have that, but look at this like module here. This is like You can bet I don't know what's under here, but you can bet your bottom dollar this is the reference.

**Dave Jones:** They don't go to this amount of trouble to make a second daughter board like this with some custom plastic carrier like this and a header on top and just for you know, some miscellaneous thing.

**Dave Jones:** This is definitely the voltage reference which they've no doubt The reason they've put on the second board is so that they can maybe thermally age these things separately and test and characterize each individual one as a separate process to building the multimeter itself.

**Dave Jones:** And this is really interesting. They've got an eight-pin header on there. So, that's obviously how they plug into their production test jig for these things. So, whether or not that's I it's likely to be analog.

**Dave Jones:** Um you know, just like you know, power so it can supply power to the thing from the from the production chest test jig. They've probably got a huge board.

**Dave Jones:** They plug like a hundred of these things maybe you know, upside down or something perhaps. I don't know. It doesn't matter. Anyway, they plug them in. Uh it might have to be upside down cuz this head is on the top.

**Dave Jones:** So, you might have to actually flip it upside down to put it inside the in inside the on onto the production test board. Anyway, uh regardless of the physical arrangement, they've probably got like a hundred of these, put them on a big tray and then they maybe put them in a big thermal chamber and they can then read out and log no doubt data from each individual one.

**Dave Jones:** So, but this opens the possibility that maybe is there digital compensation on here perhaps. Where they can actually software trim this thing. But that's probably unlikely. I'm getting a bit too excited there because um that would that would be a bit too much cuz you don't need to go to that sort of effort for a voltage reference on here.

**Dave Jones:** As I've always said, with voltage reference is is all about the stability. The absolute accuracy of the voltage reference does not matter. This voltage reference board could be you know, one or two percent accurate absolute accurate.

**Dave Jones:** It doesn't matter whether it's you know, 10.1 volts or 10 volts because when you put it in to the multimeter, you can software calibrate that value out. It's all about the drift.

**Dave Jones:** In this case, it's a 16 ppm accurate one or I think it's 0.5 ppm per degree C temperature drift. I have to double check that. So, let's take a brief look at the specs here cuz it's very worthwhile.

**Dave Jones:** Look at this. It's best spec here is going to be on is on the 10 volt range here. And like usually like on cheaper meters, they might use like a 200 mV reference or or something like that.

**Dave Jones:** So, the best DC volts accuracy is going to be on your millivolt range, but this is likely using a 10-V reference in here. So, it's no surprise for finding our best spec here, absolute spec, is on our 10-V range for DC volts.

**Dave Jones:** And of course, for any multimeter, that's the DC voltage range which is going to have the best spec. Current is going to be lower, AC voltage is going to be worse.

**Dave Jones:** AC voltage is going to be worse. Resistance, current, all that sort of stuff. It's DC volts is where the business is at, and this is how they get the banner spec of 16 ppm.

**Dave Jones:** And you can see where they get their banner spec of 16 ppm here, 0.00016% absolute after 1 year for a plus minus 5° differential from the temperature that it was calibrated at.

**Dave Jones:** But, look at the 24-hour spec here. Look at this, 8 ppm. Woohoo! Absolute. Oh, now we're talking. That's the percentage of the reading plus the percentage of the range.

**Dave Jones:** You're going to have a 2 ppm percentage of the range. And when you're down there counting your you know, counting your least significant digits, that's all going to add up and matter.

**Dave Jones:** But, anyway, this one is like only like a transfer standard spec because it's within plus minus 1° C of when it was calibrated. So, you usually can't like ship the thing within 24 hours and then use it somewhere else.

**Dave Jones:** So, that's really like within the same lab standard. But, even something more practical here, look at 90-day spec, it's still 13 ppm absolute. Um, and then that goes up to 16 ppm after a year, 20 ppm after 2 years.

**Dave Jones:** So, very, very nice. Now, here's one of the interesting things, the auto cal feature which we saw on the front panel before. What it does is it compensates well, improves the temperature coefficient, the temperature drift of this thing.

**Dave Jones:** So, without the auto cal feature, i.e. just like the 34461A, for example, then it's going to drift by 5 ppm per degree C of the reading plus 1 ppm of the full scale range as well.

**Dave Jones:** And that's basically either doesn't matter whether it's within this plus minus 5° or outside it. It's just going to always drift by that amount. But you turn auto cal on, bingo, it drops that from 5 ppm down to 1 ppm plus 1 down here, of course.

**Dave Jones:** And it's a bit worse down here, probably as you'd expect on the 100 mV range there. But yeah, it gives you down to 1 ppm. So you're basically with the auto cal feature on, you're looking at sort of like a worst case of 2 ppm per degree C temperature drift within the operational range of the instrument.

**Dave Jones:** But as with all data sheet values like this from a reputable manufacturer like Keysight, who really know what they're doing and do take care with this stuff, these specs are going to be conservative.

**Dave Jones:** So I'm pretty sure it's actually going to be a better temperature coefficient than what you can get here. This is just what is guaranteed. So yeah, it could certainly be better.

**Dave Jones:** One thing I really like though is that they do give you a 2-year spec for plus minus 5°. A lot of companies won't give you a 2-year spec on the thing.

**Dave Jones:** They'll even give you a a year or some only give you like a 90-day spec. In fact, I think HP used to do that back in the day on some of them meters that only give you a 90-day spec.

**Dave Jones:** But they're pretty confident on this sucker, so they're giving you a 2-year spec. Very nice. 20 ppm class instrument after 2 years. Switch on the auto cal, it compensates for the temperature coefficient in that thing.

**Dave Jones:** So it must have a good temperature sensor inside this thing. It must be pretty schmick. We might find that on the board there somewhere perhaps. So I'm wondering, is that puppy there a temperature sensor, three-pin um TO-92 package, could very well be.

**Dave Jones:** Although, it is labeled Q. Q1 there, so hmm Q is for transistor. Aha, it's a bottom-entry socket. That's the thing I was talking about before, how they would put these on a big uh production uh test panel, and they might have to flip it upside down.

**Dave Jones:** No, this is a bottom-entry socket. So, if I just Ooh, it it wiggles. Look at that, I'm wiggling the voltage reference. If I just pull on that, it should just pull up.

**Dave Jones:** Yep. There we go, cuz we've got our pin header on the board, and that just fits neatly around that uh crystal there. They've designed that in, and tada. There is our voltage reference.

**Dave Jones:** There's not much on there at all, so I suspect that's just like an LTC uh 1000 voltage reference. Let's take that plastic clip off and see if we're right.

**Dave Jones:** And I was right. There you go, LTZ1000. No surprises whatsoever for finding that in there. The date code on that, the 27th week uh 2013. So, that's a reasonably old beast.

**Dave Jones:** Anyway, it is the LTZ1000ACH. I'll link it in down below. It's one of the best voltage references you can get. And to get the specs in this thing, it couldn't have used anything else.

**Dave Jones:** Basically, it couldn't have used your traditional LM 399, which we're um so used to seeing in um you know, six and a half digit meters. It's been the standard in six and a half digit meters for like ever.

**Dave Jones:** So, uh yeah, no surprises. It's still in the new model of the um What is it? The three uh 34465A, as well as the 61A we've uh seen before.

**Dave Jones:** But anyway, we have ourselves a Linear Tech um uh probably that's just a op-amp, is it? Yeah, a 1013. I think we just got ourselves an op-amp there, and a couple of uh miscellaneous parts.

**Dave Jones:** That's just forming the uh voltage reference, probably just based on the um uh application note from the LTZ 1000 and that's all she wrote. There's nothing on the bottom here.

**Dave Jones:** We've got our holes for our um our header to come through. So, that's quite clever. So, as I said, there's a big big production test board, no doubt, that individually soaks each one of these and of course each one is individually uh serial numbered.

**Dave Jones:** There we go, 344708. Specifically designed for this and in case you're wondering, well, well, it looks like they had a uh looks like they had some pads on there, maybe for a bypass cap or something they decided not to fit.

**Dave Jones:** Anyway, in case you're wondering what these slots around here are, this big one here and around like that, that is to take the stress off the leads. That's for thermal expansion of the board of the uh PCB material.

**Dave Jones:** It looks like it's standard, you know, um FR4 class uh fiberglass board. May not be. May have a lower uh thermal expansion uh coefficient, perhaps, but that's what they're trying to do there cuz any expansion of this board, they're just trying to take out the stress from the leads.

**Dave Jones:** Um that's one technique of doing moons like that. Often you'd like put it on like a cutout right on the edge of the board uh for example. Either way, you know, works.

**Dave Jones:** I think the this one's probably not quite as efficient as the other way, just having like it right on the edge of the board and then cutting a slot out like that.

**Dave Jones:** But anyway, it's obviously going to do the business and that's what it's there for. Because any stress on those leads, any mechanical stress on those leads, uh translates into um stress inside the die.

**Dave Jones:** I mean, we're really down to the physics level here and uh it stress on the die in there or whatever and it can cause the thing to um drift.

**Dave Jones:** So, these things are very very susceptible. And of course, the reason that they've designed this custom little case is to keep that nice and toasty inside there. Not Not toasty, but keep it at a constant temperature so that in your unit like this, because it's got a fan inside it, okay?

**Dave Jones:** And there's air blowing through because, hey, we have to cool down the other parts and stuff like that, you don't want that air flow going over your voltage reference down in here.

**Dave Jones:** That's just going to ruin your day. So, you don't want that turbulent air flow blowing over that thing. So, that's why they've done it. They've put it in its own little custom plastic clip, and that one clips on the bottom, and it is all very very nice and well designed.

**Dave Jones:** That's brilliant. Look at that. That one goes over there, and there's a screw to hold it all together. They know what they're doing, Agilent. Sorry, Keysight. And there you go.

**Dave Jones:** There's the money shot for you, volt nuts, LTZ1000 for the win. But, look at that. It's a 2N3904 NPN transistor. What a let down. But, hey, actually, with hindsight, it's not that surprising cuz they need a drive transistor to drive the heater inside this puppy, cuz this is a a heated reference.

**Dave Jones:** There's a heating element in there, which I'll show you in a second, hence why they've put it inside here. So, that's the That's the idea behind that. So, let's take a look at the application note, and they're almost certainly running exactly the same application note as LT are supplying in their data sheet.

**Dave Jones:** Let's take a look. So, this is what we've got inside the LTZ1000. We've got a couple of transistors, the buried Zener reference, of course, that's that's doing all the main magic here, and a heater element shown like this.

**Dave Jones:** These are just uh substrate uh diodes, they tell you there. So, they're just um yeah, not actually a physical uh diode as such. But, uh that's just um a clamping as part of the um resistive element in there.

**Dave Jones:** So, that's basically all there is in there, and this puppy is capable of Look, a temperature drift of better than 0.03 ppm per degree uh C, and long-term term stability 1 micro per month.

**Dave Jones:** And, it's about 0.15 uh ppm noise is also obtained. So, that's uh you know, the noise figure is basically what Agilent might be um Keysight might be telling us here uh with the uh spec because it's the reference they're using is capable of better than the spec they've got here.

**Dave Jones:** But, hey, that's not uncommon for high-end manufacturers like uh Keysight to over spec their gear. It's sort of like a worst-case guaranteed figure they put in the data sheet.

**Dave Jones:** So, the reference is certainly capable of better than what they've um had here in their um reference of 0.1 ppm. It's capable of almost an order of magnitude better than that.

**Dave Jones:** And, no surprises that the application note here has exactly the same chip. We've got the LTC1013 as a dual uh precision reference here. There's our 2N3904, which is driving all of the current for our heater element.

**Dave Jones:** That takes a significant amount of uh current. I'm not sure what it is, but yeah, it's not uh trivial, hence why they've got the probably the TO-92 uh package there, and also have isolated it outside here because you don't want that device getting warm inside here.

**Dave Jones:** That'd be a big no-no. So, you want that out there where the airflow, the main airflow you've designed into your product can actually take that, you know, that that heat away.

**Dave Jones:** It can dissipate. If you put it under there, even, you know, that would have been a bit of a fail. So, yes, I have no doubt that this circuit matches this pretty close to precisely, because, hey, why would you do it you know, why would you try and do it against what Linear Technology, one of the masters in the field, has spent a lot of time and effort building the one

**Dave Jones:** of the world's best voltage references here and getting and characterizing a circuit? Well, you just use it and go, "Yep." Of course, you do your own uh tests and performance uh checks on it.

**Dave Jones:** And I'm sure Keysight have uh done that. They're not just going to blindly build this up and go, "Ah, yeah, she'll be right. No worries. Whack it in there and off to market we go." No, they they would have seriously uh characterized the design of this thing.

**Dave Jones:** And as I said, they've really thought about it from a a thermal um air flow point of view and uh thermal stress on the board and everything. They've really done it right.

**Dave Jones:** That's a brilliant example of how to design a nice precision reference. So, it'd be interesting to know exactly what burning they do on these, because I'm sure that they do.

**Dave Jones:** So, um and of course, there's no trimmers on here. As I said, they're not worried about uh trimming this to an absolute uh value. It doesn't matter, cuz that's taken care of in the software calibration of the uh meter itself.

**Dave Jones:** So, that capability is already built into the multimeter. There's no point trying to get an absolute reference here. So, this could be a couple of percent off. Eh, doesn't matter.

**Dave Jones:** It's all about the drift. It'd be interesting to know and maybe Keysight can get back to us about um what sort of production testing, maybe if they've even got some photos they can share of their production test facility for these things or something like that.

**Dave Jones:** I'm sure they whack them in a thermal chamber and uh characterize each one. Bet your bottom dollar. Okay, so I won't bore you with any more uh details of the teardown in here, because I've done it all before in the 34460A video, which I'll link in down below.

**Dave Jones:** And I've done like a little Dave Cad explanations of how their multi slope converter works and all that sort of stuff. So there's some real interesting info in the previous teardown because it's an identical design basically and you'll see in a second.

**Dave Jones:** I've taken some high-res photos of both these boards as aligned as I possibly can and well, let's go to the videotape. All right, here we go. Let's compare the two boards and this is the original one.

**Dave Jones:** This is the 34461A. You can see the Agilent logo up in the top right corner here and you can see that this here is the part number 34460A which is 60/61 and it's a rev 4 board.

**Dave Jones:** Now, look at this. I can switch between them. Isn't that fantastic? I love it. Oh man, I can play with this all day long. Look at this. You can see that there's hardly any differences at all.

**Dave Jones:** It's terrific. But anyway, here's the new Keysight one. This is the 34465. So the same PCB is shared between the 65 model and the 70 which we're tearing down here.

**Dave Jones:** Once again, rev 04 again if you have a look at that. So you'll notice that one of the first thing you notice is that well, the relays have changed changed to yellow.

**Dave Jones:** Woohoo! Excellent. They've changed brands. They've gone from Omron. But look, there's a missing relay on the old 6 60 board I'll call it and the relay is populated and also there's another relay here and two SO8 packages here as well and you'll see that they just pop in there and uh so maybe they had the design of the you know, they were thinking about this right back when they designed the

**Dave Jones:** 60 and 61. So it looks like they've had the capability in there, but a few um minor things have changed. Look, the um Keysight one up here, where the cursor is, they've added a couple of parts up there.

**Dave Jones:** So, they've squeezed them in there, and they've changed the layout of this. You see how on the old one they've got uh the large uh footprint for that um oscillator there, but then they decided, "Oh, well, no, we're going on this smaller package."

**Dave Jones:** And they've changed it, and they've sort of just shuffled a few parts around there, around the um uh analog-to-digital uh converter section around here, which is based on the Lattice part.

**Dave Jones:** The Lattice part is the uh exactly the same device. It's the um LFXP2-5E. But, you'll notice that look, there's a part that's on it a resistor. They've moved that, but I think something else is uh added in there.

**Dave Jones:** No, anyway, there's minor differences in the tracking and things like that, but jeez, there's not not much at all difference. Check out this down here in the bottom uh left corner.

**Dave Jones:** Look, this R102 here is Oh, no, it's mounted upside down. All the electrons are going to fall out. Oops. But, it's Gee, look, it's everything's pretty identical. Um it's got all the same input protection.

**Dave Jones:** They still don't have that second mob uh fitted there. And this uh precision resistor R416 is still here. These two ceramic packages here and here are still the same.

**Dave Jones:** All the analog-to-digital converter is all still the same. They're just trying to squeeze out some extra resolution uh from it, of course, which they can, because the meters always had that extra resolution in in there.

**Dave Jones:** If you see my review last time, it actually um does a software calculation, gives a single-precision floating-point uh output value, which is like an equivalent to like 8 1/2 digits or or or something like that.

**Dave Jones:** It's more than the uh quoted 6 1/2 digits that uh was on the previous unit. So, it was obviously good enough for this seven and a half digit meter.

**Dave Jones:** And you'll notice, here we go. Here's the change. Here's the voltage reference, the LM399 in there. And you'll notice that they've basically just ripped out the LM399. Even that Look, even that capacitor in there and that diode in that sort 23 package there, they've basically just ripped out the LM399 and replaced it with the LTZ1000.

**Dave Jones:** So, there you go. Oh, look, there's an extra resistor there. Look, R310. Maybe I don't know. Is that a current shunt for the one microamp range? That's the other thing I haven't found, how they're doing the one microamp range, cuz that's two orders of magnitude better than the 60 model here, which only went down to 100 microamps full scale range.

**Dave Jones:** So, this one can do one microamp. How's it doing it? I don't know. So, everything looks identical on the bottom side of the board. All the current shunts look the same there.

**Dave Jones:** So, I'm not sure what Can anyone spot it? Can anyone spot it? I don't know. Anyway, we've got our high voltage resistor hybrid over here. They've got a high voltage network here.

**Dave Jones:** And everything looks pretty identical. So, uh Here we go. No, sorry. They've uh No, look. Here we go. Well, they've changed the type of current shunt resistor used here.

**Dave Jones:** Look, R231 here. You see how it's like a That's very similar to one I use in my microcurrent. A very similar sort of design. But look, they've changed that to a much larger package now.

**Dave Jones:** It's only a 1% value. But as I said, it doesn't need to be precise, cuz it's software calibrated out. It'll be incredibly low drift. And that's a That's a weird ass four-pin package.

**Dave Jones:** You'll notice like surface mount. It's still a surface mount package, but it's a much bigger, physically much bigger, so it can handle it has a greater power dissipation in it, but it's a still a four-terminal current shunt resistor in there.

**Dave Jones:** So, maybe they've changed that, and maybe a amplifying maybe that's maybe those two there are an amplifier perhaps? With, you know, that boosts it up. Hmm, I'm going to have to um have a look Oh, I boot.

**Dave Jones:** What does that mean? Current boot? Huh, interesting. Aha, yes, my hunch was correct. These devices here that they've added two extra devices here, you'll notice uh um can I zoom in on that?

**Dave Jones:** Uh no, I can't. Um but, you'll notice that uh there's a guard ring around that trace there, and whenever you see guard rings around there, sorry about the small cursor here.

**Dave Jones:** I probably should change to a really large cursor so that you can uh see it. But, when you see guard ring like that, you know it's a sensitive node, so we're talking, you know, uh low current stuff into there.

**Dave Jones:** So, um bingo, this chip, you probably can't read it there, but it is none other than a Analog Devices um AD8638. Bingo, exactly what you need uh for like it's like my microcurrent capability.

**Dave Jones:** It's got an auto zero rail-to-rail op amp in it. I eat it's got zero DC um offset in it. There's zero offset voltage, and that's exactly what you need for measuring down at that uh sort of, you know, that low end.

**Dave Jones:** That's This is how I'm sure that they're getting their 1 microamp range. And they've got two of those in there, actually. If we go back here, we'll see this one here is still fitted.

**Dave Jones:** That one is still one of those uh devices, but they've fitted another one in here. Um uh uh U202 there, I think. U503 is just a TL071. It's just a Joe Blog's um, op-amp.

**Dave Jones:** Nothing fancy going on there at all. But, yeah, I I actually looked at using this in my uh, microcurrent uh, at one stage, I think. And this one's a pretty schmick op-amp in very low input bias current 40 40 puff.

**Dave Jones:** And uh, what's the typical um, low offset voltage? 9 microvolts maximum. So, it's actually not as good as uh, my microcurrent, but that doesn't necessarily matter. It's going to be because once again, they can calibrate that out.

**Dave Jones:** So, it's the offset drift here which is going to matter. So, it's .04 microvolts per degree C maximum. So, that's how they're probably getting um, using this device to get their 1 microamp full scale range.

**Dave Jones:** And they can still get uh, presumably their 7 and 1/2 digit precision on that. But, uh, if we if you actually went back and checked out the spec, the drift spec would actually be uh, higher for the uh, current ranges.

**Dave Jones:** And there's just other little tiny changes here. You'll notice just under the lattice chip here, you'll notice how they've just changed the uh, just rotated that component designator R uh, 808 there.

**Dave Jones:** So, somebody the PCB designer was just fussing around. Oh, I I think I'd rather have it in that orientation. That's a bit neater. They were just, you know, gilding the lily there a bit.

**Dave Jones:** And like down here around this 94V um, zero, they've added a dash in there for some reason. Who knows? And uh, uh, but like apart from this, like there's bugger all difference.

**Dave Jones:** So, I'm really, really surprised. And the other noticeable difference here is what looks like a crystal there, but it's uh, not actually. Um, sorry, I've only got the top-down photo here, but it's actually a uh, Vishay uh, Z-foil precision resistor.

**Dave Jones:** So, it's a 10K precision resistor. This one was not fitted, as you can see, it was not fitted on the, um, original uh, 6061, but it is fitted. So, it's a 324 there, but it's yeah, a really precision 10k resistor.

**Dave Jones:** So, why they've added that in, perhaps it has something to do with the current shunts, but it seems like yeah, it's just out of the way tucked over there.

**Dave Jones:** So, I'm not sure why they've put the extra one in there. Anyway, it is a very schmick resistor. So, very extremely low tempco. It's one of Vishay's uh best ones.

**Dave Jones:** It's the VH102 ZT. You'll notice that look here, they've changed manufacturer of that. What is it the um What is it a 74 It's a HC4053 analog mux. You'll notice that they changed manufacturers from TI to somewhere else.

**Dave Jones:** I haven't zoomed in on that one. Can't see detail, but but obviously they they're for like um they are not critical parts. They're just, you know, jelly bean parts.

**Dave Jones:** So, really it doesn't matter what manufacturer you put in there pretty much. Although, they would have characterized it, specified it, and put it in the bill of materials as that is an authorized, you know, replacement part.

**Dave Jones:** So, you know, a company the with the reputation of Agilent, they wouldn't just get whatever they can get from the Shenzhen market this week. It doesn't work like that in these kind of things.

**Dave Jones:** But, you'll notice that the in with that amplifier over there, I still don't know what that I boot is. So, um yeah, I don't know what that means. It's been removed here, I think.

**Dave Jones:** On the new unit. So, that's rather interesting and they've added that extra resistor there as well. So, they certainly have changed the current range configuration because they've got two additional current ranges, the 10 microamp and the 1 microamp.

**Dave Jones:** So, you expect a a few changes around there. But, yeah, it's basically identical. Very, very interesting. So, they haven't added a huge amount in here for the price difference.

**Dave Jones:** What they're basically cha you know, they've got a couple of extra op-amps in here. Okay, fine and dandy, but you're basically paying for the LTZ1000 reference and the characterization of that reference.

**Dave Jones:** As I said, they probably go to a lot of effort to, you know, thermal individually thermal chamber test each one of those, etc. So, yeah, that's And here's another interesting thing.

**Dave Jones:** Look, you'll notice just around that chip there that has a thermal pad on the bottom. That's why it's that gold color. It's got exposed copper there. They're using that as a little heat sink.

**Dave Jones:** It's got some got some solder. It looks like they had excess solder paste or it's flowed through the vias from the bottom or something. So, there may be a maybe changed their paste, well, they had to have changed their paste stencil because it it is there are a few differences in the layout.

**Dave Jones:** So, instantly have to go to a new solder paste stencil, but maybe they've applied some some extra paste on there and it's just flowed out. Anyway, just an interesting little insight there, but yep, everything looks pretty much damn well identical.

**Dave Jones:** I love it. All the value is in the voltage reference. And if we have a look at the bottom of the board, I won't do the same high-res photo thing here.

**Dave Jones:** Once again, teardown photos are on evblog.com if you want to have a look. This is Actually, I've lost track. This is the old one, the 61A, and this is the new 67A.

**Dave Jones:** Basically identical except look, I can actually see this one actually has an extra resistor populated in there where this one doesn't, but uh yeah, I don't know. There might be a few little miscellaneous differences, but basically big current shunt resistor up there is exactly the same from Dale.

**Dave Jones:** Yep, it's basically identical. So, there you go. I hope you enjoyed that teardown of the new Keysight 34470A. So, thanks for Keysight for getting this to me. It was a bit late.

**Dave Jones:** I was hoping to get this um before it was released, but uh yeah, there was a few shipment delay problems. But, uh thank you very much, Agilent. Very very interesting and absolutely brilliant first-class quality uh bench multimeter.

**Dave Jones:** It's It's almost impossible to fault this thing, really. Fantastic. So, hope you enjoyed that. If you did, please give it a big thumbs up and uh as always, if you want to discuss it, jump on over to the EEVblog forum, link down below, or leave YouTube comments or blog comments.

**Dave Jones:** Catch you next time. The longer your capacitor takes to charge up, the greater your resolution. But, therefore, you're trading off uh measurement resolution versus speed. But, a modern high-end uh bench multimeter like this Agilent, or even the previous model, or the previous model before that, or before that, um they don't use just basic uh run-of-the-mill dual slope um integration techniques.

**Dave Jones:** They use what's called multi uh slope integrating ADC, and it works exactly the same way. It's just that it has some extra switching in here.
