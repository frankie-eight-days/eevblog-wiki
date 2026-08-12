---
video_id: G-6BBF3HyRU
title: EEVblog #613 - Prema 6047 Multimeter Teardown
url: https://www.youtube.com/watch?v=G-6BBF3HyRU
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 31, "3": 51, "4": 65, "5": 78, "6": 104, "7": 111, "8": 124, "9": 136, "10": 148, "11": 163, "12": 177, "13": 185, "14": 214, "15": 239, "16": 259, "17": 277, "18": 294, "19": 313, "20": 324, "21": 336, "22": 352, "23": 368, "24": 384, "25": 403, "26": 413, "27": 425, "28": 441, "29": 447, "30": 460, "31": 474, "32": 492, "33": 506, "34": 521, "35": 535, "36": 557, "37": 567, "38": 589, "39": 599, "40": 620, "41": 631, "42": 639, "43": 652, "44": 665, "45": 678, "46": 688, "47": 699, "48": 713, "49": 728, "50": 749, "51": 764, "52": 783, "53": 793, "54": 806, "55": 818, "56": 832, "57": 840, "58": 857, "59": 872, "60": 890, "61": 906, "62": 914, "63": 937, "64": 948, "65": 963, "66": 975, "67": 988, "68": 998, "69": 1011, "70": 1036, "71": 1044, "72": 1053, "73": 1067, "74": 1079, "75": 1092, "76": 1104, "77": 1117, "78": 1128, "79": 1142, "80": 1158, "81": 1171, "82": 1181, "83": 1194, "84": 1211, "85": 1221, "86": 1230, "87": 1239, "88": 1254, "89": 1268, "90": 1282, "91": 1296, "92": 1308, "93": 1322, "94": 1335, "95": 1351, "96": 1370, "97": 1387, "98": 1400, "99": 1422, "100": 1436, "101": 1445, "102": 1456, "103": 1467, "104": 1486, "105": 1502, "106": 1525, "107": 1547, "108": 1561, "109": 1573, "110": 1586, "111": 1600, "112": 1612, "113": 1627, "114": 1642, "115": 1654, "116": 1662, "117": 1677, "118": 1691, "119": 1715, "120": 1726, "121": 1732, "122": 1745, "123": 1760, "124": 1776, "125": 1791, "126": 1808, "127": 1822, "128": 1834, "129": 1845}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Yes. I think I'm officially a volt nut. What is a volt nut? Well, anyone who has an 8 and 1/2 digit multimeter pretty much.

**Dave Jones:** I think that's probably the definition. And yes, I've got one. I foolishly went and bought an 8 and 1/2 digit multimeter. No, it's not a classic HP 3458A of course, which is the world's best, but this one's not bad.

**Dave Jones:** It's an oldie, but maybe a goodie. We'll find out. Anyway, it's from a company you've probably never heard of. They're called Prema. And they're still around, but they're like a semiconductor company basically and they specify and specialize in what semiconductors.

**Dave Jones:** They roll their own ADCs and things like that. And DC voltage standards and back in the day in this case the late 80s, they designed and sold an 8 and 1/2 digit multimeter.

**Dave Jones:** So, I got this on eBay and well, I'm I don't know. I just got it from the post office and I'm a bit horrified by the lack of packaging.

**Dave Jones:** You can just tell by the physical size of this cuz these are large multimeters. So, there can't be much in the way of packaging in this thing and they The person at the post office went out the back and got it, brought it back and sort of tossed it down on the counter and sort of went thud and inside I just went And well, yeah, I don't know if it's

**Dave Jones:** made it intact. That's one of the things with buying test gear on eBay. Not only do you not know if if it works or not and is still within spec.

**Dave Jones:** This one I think was Um, as you know, it powered up, but it was, you know, it hadn't been touched. It'd been in storage in a case or something since it was last calibrated or something like that.

**Dave Jones:** So, you know, a reasonable level of confidence that it's going to work, I think, but certainly not guaranteed. Um, and obviously they clearly don't know how to package uh, test gear properly cuz I don't think there's much in the way.

**Dave Jones:** We've got a box in here and Oh, anyway. Uh, yes. The thing is you don't really know on uh, eBay what you're going to get or how they're going to package the things, even if it is good.

**Dave Jones:** When it gets shipped around the world like this, who knows, you know, just yeah, tossed on the counter at the local Australia post office. But, hey, what happened on the 747 flying here in the cargo hold and the baggage handlers and everything else?

**Dave Jones:** Well, and not baggage handlers, the commercial uh, handlers, I guess. But, gee, I don't know. Only one way to find out. Let's take it apart. Unfortunately, I'm not going to have to do the uh, don't turn it on, take it apart thing.

**Dave Jones:** I'm going to have to plug it in straight away and see if it still works, I think. But, after that, we'll tear it down. Let's go. All right, here we go.

**Dave Jones:** It There's bubble wrap in there. There's going to be like one layer of bubble wrap or maybe two at most. Um, but you know, usually when I get test gear like this and if it comes from a good uh, you know, reputable test gear uh, reseller, for example, they will know how to package it and they'll like a vacuum uh, pack it in the, you know, the um,

**Dave Jones:** uh, custom uh, foam or something like that or at least heavily pack it in uh, uh, you know, foam peanuts and things like that. But, this is really quite hodgepodge and yeah, look, there's one or two layers of thin bubble wrap and of course the um look, nothing on the corners here.

**Dave Jones:** Look, nothing on the corners. So, the problem with that, when you ship things like that, um all of the shock gets taken on there. So, when this thing gets, you know, thrown around, bang, you're really going to get the shock transferred into here and then of course that being all originally mounted inside, that's going to transfer through to the uh PCB inside.

**Dave Jones:** And curiously, it's got a bit of cardboard in there as well. So, oh, there we go. They've at least done the right thing. And at the very least, they've put cardboard covering on the front panel.

**Dave Jones:** So, that's not too bad. Okay, I'll give them props for that. They've at least thought of that, but they haven't thought of uh transferring that shock through to the uh yeah, through to the chassis, but it doesn't look physically damaged.

**Dave Jones:** So, looks like it's made it in one piece. Woohoo! Will it work? I don't know. So, yeah, it's in reasonable nick. I don't mind it at all. Looks like the uh cal seals might be uh broken on the thing, but yeah, really old school look of it.

**Dave Jones:** Look at this uh old school seven segment red LED display and the old illuminated push buttons. Really old style banana jacks on these things. I mean, check that out.

**Dave Jones:** That is just oh that's really old school uh shrouded banana plugs and a couple of more uh seven digit displays, but uh seven segment displays, but well, let's power it up.

**Dave Jones:** This is by the way the 6047. There also is a hot slightly higher spec 6048, but this is 8 and 1/2 digits, uh 1 ppm stability or thereabouts uh short-term stability.

**Dave Jones:** I think the 6048 is 0.5 ppm stability. I will link in the manual for this thing down below, but I did get a full manual with it. So, that's that's pretty good.

**Dave Jones:** Got the original PRINTED MANUAL. OH, LOOK, SCHEMATICS. SCHEMATICS. AWESOME. What a god. The full schematics. I haven't checked online if the online schematics have if the online manuals have the schematics, but look, there's the whole front end and there is the ADC.

**Dave Jones:** There it is, look. Uh they rolled their own custom pre-amp ADC in this thing. So, yeah, there you go. I think this uses either the LM 399 voltage reference or the LTZ1000.

**Dave Jones:** I think the higher-end one might use the LTZ1000, but anyway, let's power the thing up and see if it works. And yeah, that cal seal looks slightly broken. Ah, well.

**Dave Jones:** And on the back, there's not much. Uh it looks like I don't have the multi channel option on the thing, but there you go. I've got serial number 1041.

**Dave Jones:** They didn't make many of these. I'm not sure of the exact age. There's no date code, but we'll find out from the chips inside. And it's got a GPIB and a external trigger using a a 3 and 1/2 mil jack and um standard uh two-foot well, I don't know if it's universal.

**Dave Jones:** No, there's the voltage on there. I have to switch that around. So, better make sure I get that right or I'll done a blow the ass out of it.

**Dave Jones:** All right, here we go. Have I bought a dud? Controller one, whatever that is, but that's promising. That means the processor is working and it's booting up. Controller four, whatever.

**Dave Jones:** Hey, there we go. We're in. We're in like Flynn. It's in milliamp mode, but uh volts DC, there we go. 200 millivolts. There we go. Let's switch to two-volt mode.

**Dave Jones:** Obviously, it's got uh high input impedance because it's counting up. So, there you go. Excellent. 200-volt range. There you go. Once you get to 200-volt range, it's not high input impedance anymore, so that's why it's uh quite low.

**Dave Jones:** But, you switch it down to 20, and yep, it's got that high input impedance. Now, just a very quick check with my uh little resistance box here, 10K. It's around about that, you know, down to the fourth uh digit there, pretty much.

**Dave Jones:** Let's whack it in here and see what we get. 20K. Yeah, there we go. Hey, winner winner chicken dinner. It's interesting that on the resistance range here, if it goes over range, it actually tells you error one.

**Dave Jones:** I was a bit mortified when I first switched on the resistance range. Oh, error. And here we go. I've hooked it up to my 10-volt uh EDC lab standard here, but I just plugged it in like a minute ago.

**Dave Jones:** So, really nothing's warmed up and and the and the Prema 2 has only been on for, you know, 5 minutes or whatever I've been filming. So, yeah, we're a little bit out, but our Agilent is uh much closer there, 9999.6, whereas uh down here, yeah, yeah, it's a bit out.

**Dave Jones:** So, whether or not it just hasn't warmed up yet, I have no idea. I have to leave it going. I haven't, you know, to do proper performance tests on this could take days or something.

**Dave Jones:** It's not easy, but it basically uh works. So, you know, whether or not it's uh within spec cuz we're talking. Um the Agilent 34461A 6 and 1/2 digit multimeter, typically in the order of point double 0 5% uh accuracy in terms of like a 1-year accuracy.

**Dave Jones:** This Prema 8 and 1/2 digits, um two full digits more, uh pretty much. Although, this is 10,000 count. Anyway, this is 8 and 1/2 digits. Goes up to what?

**Dave Jones:** 20. So, it's 19999. Um and it's in the order of point triple 0 5%. So, an order of magnitude 10 times better uh basic DC volt accuracy spec than a 6 and 1/2 digit top-of-the-range 6 and 1/2 digit meter like the Agilent 34461A.

**Dave Jones:** So, that's the sort of, you know, even though you're jumping up two digits, you're only jumping up one order of accuracy pretty much. Yeah, and basically the same on the 1-V range as well.

**Dave Jones:** Look, the Agilent's pretty darn close to spot-on. I've done previous videos on this. This thing I've taken it to the local cal lab. I'll actually link in that down below.

**Dave Jones:** And this thing is bang on when you let it uh warm up. But, yeah, look at that. Point 99999. So, we've got five nines there. We go over to here.

**Dave Jones:** And we're on the 2-V range. 99998. So, yeah, something's out. I don't know. As I said, got to let it warm up, do some more tests. But, not that great on the DC volts.

**Dave Jones:** I was expecting more. I don't actually know how to switch in the extra couple of digits here. Don't know how to work this thing uh yet, you know. It's got all sorts of measurement uh modes and integra- You can set the integration time and all sorts of stuff.

**Dave Jones:** That would do it um by changing the integration time, you'd uh likely get your increased resolution there. And if you're curious to know how much uh power it takes, there we go.

**Dave Jones:** I've got it hooked up to my uh power meter here. And it's taking about 16 odd watts or thereabouts or 18.5 VA. Woohoo! With a power factor of .863.

**Dave Jones:** Terrific. Well, it basically works, so there's only one thing left to do and that's take it apart. Now, of course, what we expect in this sucker is uh uh pretty much uh you know, late '80s vintage.

**Dave Jones:** So, we're looking at all through-hole uh components or DIP packages, stuff like that. I'd be surprised if there's any surface mount in here um because they wouldn't have optimized this for manufacture, that's for sure.

**Dave Jones:** This is only serial number 1,000. So, not not exactly huge. Can I lift that up? Here we go. We're in. Ah, look at that. Beautiful. Check that out. Three boards and Oh, hang on.

**Dave Jones:** Hang on. Oh, yeah. Vintage precision test equipment smell. Love it. Well, it looks like I was pretty bang on when I said they wouldn't have optimized this thing for production.

**Dave Jones:** They sure haven't. Look, uh this is a sort of the construction you'd find in sort of you know, that one-off or low-volume uh test gear you might uh typically I've typically designed in the past for like you know, production testing and uh stuff like that.

**Dave Jones:** You know, you mean you want to manufacture 10 of them. You know, this is probably what you'd end up looking like. Look, three separate boards just sort of you know, tied into rails down on the bottom there.

**Dave Jones:** Looks like they've got a couple of rails through there. Just a couple of standoffs, so nothing fancy in that respect. No fancy mounting or anything like that. By the way, there's no fan in this thing um at all.

**Dave Jones:** Uh completely silent. As you saw, it only draw drew uh 15 odd watts or thereabouts. But anyway, transformer up here, right right hand board construction soldered directly onto that.

**Dave Jones:** Then a little board, very nice looking board to board interconnect there. And looks like out there, there's our main voltage reference there. Couple of huge relays in here, but really just double-sided board construction.

**Dave Jones:** We've got all our processing happening over here, good old EPROM in there. Don't want to lose that data out of that. You may not get that one that back in a hurry.

**Dave Jones:** Ooh. Is that a real-time clock chip? One of those Dallas real-time clock chips under there perhaps? But yeah, we've got some precision front-end stuff happening over here. We've got it under a under a shield, but yeah, nothing fancy whatsoever.

**Dave Jones:** So socketed, everything is basically socketed. Looks like we've got some precision foil resistors here. They look like Vishay ones, Z-foil construction if they were around back in the late '80s, but that's what they look like to me.

**Dave Jones:** And um yeah, I just basic through-hole technology. Nothing fancy whatsoever, all off-the-shelf parts. This thing would be entirely repairable, especially when you got the schematics. Even without it, jeez, you could easily trace this circuit out circuit out and figure what it's doing.

**Dave Jones:** Unless of course the custom ADC, which is probably under here see a couple of custom chips with weird ass part numbers. They're most likely Prema custom chips because they are a silicon company and I know for a fact they rolled their own analog to digital converter inside this thing.

**Dave Jones:** And it's all a bit how you doing, too. I mean, we've got this single in line thing. I have to look at the other side, but it's just bent over at an angle there.

**Dave Jones:** Look at these precision uh, resistors here. They we got like they're they're only 1% of course. They're not high tolerance, but they would be, you know, practically zero tempco, zero drift in these things because, you know, they're they're probably paid a couple of hundred bucks each for those resistors to get them.

**Dave Jones:** They probably got the best Vishay had to offer at the time. And, yeah, nothing but the best would have gone into these things because the drift in this unit, as I said, even in this unit is 1 ppm.

**Dave Jones:** So, that's its uh, nominal uh, drift spec or something like that. And the higher end one is half that at 0.5 ppm or something like that. And look, then they've got this metal can package just bodgied into this dip socket up here.

**Dave Jones:** And it is all very handmade. It's not like this is uh, you know, any sort of, you know, high volume production at all. Probably each one of these was individually handmade to order, most likely.

**Dave Jones:** And I think that is the widest clearance I've ever seen on any standoff uh, uh, bolt at all. Look at that. They were really paranoid. Let's not go anywhere near those suckers.

**Dave Jones:** Could be guard traces on there. I see a couple of these are missing the uh, solder mask. So, that's what they could be doing there. Then you find weird stuff like this.

**Dave Jones:** There's a 74HCT4046 there. And just a crusty single turn trim pot on the board. You think, you know, this doesn't look like a precision world-class eight and a half digit DMM, that's for sure.

**Dave Jones:** But, it is because uh, you know, that's not the important stuff. All the important stuff is happening under here and getting, you know, zero tempco uh, pretty much. Cuz uh, once you've got, you know, there's a, you know, you whack some high quality relays in there, some precision resistors, and then you get a, uh, precision hand selected, hand aged, no doubt, uh, voltage reference in here.

**Dave Jones:** And you combine those things together and and with a uh, precision ADC, which they've rolled their own in this thing. We might be able to find it eventually. And yeah, bingo.

**Dave Jones:** You can get 8 and 1/2 digit performance. Doesn't look like it just by looking at this thing. You wouldn't say that this is, you know, any sort of precision instrument at all.

**Dave Jones:** And bingo, date code, we're talking, you know, 41st week '88. That's probably like the oldest or the newest Sorry, I can find in there. Some of them are quite old.

**Dave Jones:** Like look at this over here. We're talking, you know, '85, 34th week '85. Geez. Although the Look at this. Is that '91? I guess was the last ROM code on there.

**Dave Jones:** Oh, look. That's coming off. Check out some of the soldering on this. Looks like somebody's had a hack at that from the top. Almost as if they've replaced that diode in there.

**Dave Jones:** I uh I don't like the look of that at all. And similar things, you know, happening up here. That's just That's just not great. There's like they've been bodged on and hand soldered.

**Dave Jones:** Some of it looks, you know, like it's properly wave soldered. And then other things look like it's been bodged on. Maybe I've got one that's been repaired perhaps. And that black single inline package we saw before.

**Dave Jones:** Uh-huh. Look at that. 100 milli-ohm shunt resistor. Once again, it's only a 1%. The absolute accuracy in these things does not matter. It's all about the tempco. So, Zirin In, I don't know.

**Dave Jones:** I can't pronounce that. Isabel Deshute, I don't know. Can anyone name the manufacturer or get a data sheet for that sucker? Woo. Never seen that before. And all throughout this thing they're using German SDS relays.

**Dave Jones:** So, top quality. And of course, in a precision 8 and 1/2 digit multimeter, the connections matter. Like the physical material themselves. Once again, they will probably be tellurium copper contacts, really expensive, really high grade.

**Dave Jones:** You don't want any voltage differentials in there at all. And of course, here are our custom chips. Dead giveaway, they're marked PR, which is Prima, obviously. Designed and manufactured being a silicon company.

**Dave Jones:** And this one's got BK7. I don't know, you'd have to look up the manual and schematic for that one. And of course, as far as the power supply goes here, nothing fancy at all.

**Dave Jones:** They're running a couple of taps off here. All nicely heat shrunk and they've got cardboard in here actually protecting that mains wiring stuff. So, that's really pretty good. Then we've got a big bridge rectifier here.

**Dave Jones:** We've got a small PCB mounted, well, smallish for a TO three package anyway. TO three. Yeah, it's an LM LM309K. There you go. And then just a big 4700 mic filter cap.

**Dave Jones:** So, you know, your traditional linear supply just generating the 5 volts needed for all this stuff. And then of course, they've got the board-to-board interconnect connector down in there.

**Dave Jones:** There it is. It's very quiet. It's quite nice, actually. I rather like the look of that one. And yeah, just some small local linear regulation around here as well.

**Dave Jones:** Once again, you need those for the plus minus rails. And of course, optocouplers for everything as you'd expect. That connector is all just on an angle there. Really dodgy.

**Dave Jones:** Thrown together. It's quite a Yeah, here we go. These are all on an angle like that. Anyway, here's your optocouplers here. So, between your digital processor board over here and just this this could be part of the sampling logic.

**Dave Jones:** All your analog's going to happen over here. So, you expect to find your ADC over there, but it could No, actually. Based on those kick-ass looking sampling caps in there, I'd say that's our analog-to-digital converter without having to look over here.

**Dave Jones:** So, clearly they've got to get the signal over this these ribbon cables here. But, you know, it's going to be sort of full level type stuff. So, that's probably our custom ADC our integrator ADC down in there.

**Dave Jones:** And optocouplers and optocouplers out here as well. This is just to get some probably some digital data over to drive these relays all this relay switching over here. It'd probably go via these optocouplers here.

**Dave Jones:** And then your data output serial of course cuz you haven't got enough lines there for parallel. So, serial data out of your analog to digital converter straight into your processor board over here.

**Dave Jones:** Well, I took the shield off this thing and look at this. We've got more bodginess. I mean, take a look at that. It looks like we've got some what looks like polystyrene caps just like bodgily what you know paralleled up there.

**Dave Jones:** And we've got a couple you know just afterthoughts just added across this resistor divider here. You know, probably doing improve the AC performance of that thing. And well, it's it's pretty crap.

**Dave Jones:** Look, we've got ourselves some nice trimmers here. These are all available through the top of the can there. These little reed relays in there I suspect. They could certainly well be reed relays for switching in there.

**Dave Jones:** But, yeah, jeez. It's really just sort of thrown together hotchpotch. Not professional at all. And no surprises for finding the classic AD637 true RMS converter I see. That's been used in every multimeter since day dot.

**Dave Jones:** And as I said before, voltage reference classic LM299AH. There we go. And it's not that one of those rebranded ones. As I said, the uh upper model to this the um 6048, it's I believe got the LTZ uh LTZ1000 voltage reference in there.

**Dave Jones:** So, that one's a slightly better than the LM299 used in this one. But, as I said, that would have been hand-selected, hand-aged, all that sort of stuff. So, only the best would have been placed into this thing.

**Dave Jones:** Probably individually serial numbered, maybe. I don't know. I can't see anything, but yeah, they certainly would have been hand-picked. Now, the thing I find very interesting about this is all of the sockets in here, even for all your precision parts, they're just crap-sort of looking jewel-wipe contacts, not even doesn't even look like they're gold-plated at all.

**Dave Jones:** I don't like them. Made in West Germany, I presume. See, there's some of that horrible hacked-on rubbish. Those polystyrene caps just soldered across there. Oh, man. Leaves a bad taste in your mouth.

**Dave Jones:** And if you're wondering what that puppy is down in there bunched into the DIP socket, it's an LM uh 343 high-voltage op-amp. And you can see an example of the guard traces.

**Dave Jones:** This one is for the ohms range. So, there you go. These ones are that's the guard trace going all the way around there as uh seen in previous videos to stop uh leakage between critical nodes.

**Dave Jones:** Now, of course, all these trimmers you see in there, they wouldn't be setting the uh references. They're just uh trimmer caps in there designed to uh just tweak the AC uh performance of each range.

**Dave Jones:** Aw, look at that. Parathermally bonded transistors. They're in love. Wonderful to see. Now we go. We've got ourselves a hand-serial-numbered uh ceramic resistor divider or a high-voltage resistor uh network in there.

**Dave Jones:** So, yeah, it would have been individually tested and characterized, no doubt. Coax. So, well, what can you say about this? I mean, I expected a a bit more spit polish for a 8 and 1/2 digit you know, meter of this sort of performance.

**Dave Jones:** You know, it really is quite kick-ass performance, especially for its day even even today. It's a really top, you know, spec unit. Now, whether or not it's still within spec, I don't know cuz as I said, there is a non-volatile RAM up here and that could be keeping the calibration constants in it.

**Dave Jones:** I would have to read the manual and see how this presumably it holds the calibration constants in software in there and you could, you know, during during factory calibration or re-calibration adjustment of this thing, not just calibration check, but calibration adjustment, they would program in those calibration factors into there.

**Dave Jones:** So, they could be lost. So, that's maybe why it could be on very quick initial testing potentially out by a little bit. But, yeah, still anyway, that is just it's just budge central.

**Dave Jones:** It really is. It's like they just, you know, slapped these together by hand. Not a huge amount thought thought given into the production side of things and the spit and polish.

**Dave Jones:** But, hey, you know, it goes to show that you can make an an 8 and 1/2 digit, you know, world-class performance deal in DMM with you know, this sort of simple construction technique.

**Dave Jones:** If you know what you're doing, anyone can do it. But, hey, there is a bit of secret sauce that goes into that custom ASIC analog to digital converter there and that's where the manual has to step in and you can read all about it.

**Dave Jones:** Oh, no, I should have read the specs of this thing better. It looks like the 6047 that I've got is only a 7 and 1/2 digit resolution. It's not the 8 and 1/2 digit, which is the 6048.

**Dave Jones:** There you go. Ah, so I'm not officially a volt nut. Here I was thinking that I'd gotten an eight-and-a-half digit meter, but I don't think I have. Bummer. Oh, they're really big on math.

**Dave Jones:** Look at this. These are all the functions built in. Uh, ratio, power, polynomials, uh, what do we non-linear function? Got logarithm, square roots, tangents, arc tangents, all sorts of fantastic stuff.

**Dave Jones:** Variance, standard deviation, all that sort of stuff built in. Terrific. And there you go. If you want to calibrate the thing, there's a calibration uh, button on the switch on the back, which you've got to uh, set first and you enter program 99.

**Dave Jones:** Now I can see that that cal sticker is still in place on mine on the switch on the back panel. So, presumably nobody's tried to fiddle with this thing.

**Dave Jones:** And for those who want to know the specs, here you go. The 6047, look at that. This is a 24-hour uh, drift specs. Look, point 0011 ppm or half a ppm there for the 6048.

**Dave Jones:** Haha, killer accuracy. 90-day accuracy, you know, even at this one. See, the 6047 isn't a huge amount better than the 6048, for example. Look, it's, you know, bugger it like one digit in it there, 0.004 instead of 0.003.

**Dave Jones:** Not a huge difference there between the two. And as I said right at the start, the one-year uh, nominal accuracy 0.007 uh, percent there. So, yeah, that is like an order of magnitude better than my um, Agilent uh, And even the one-year specs on the resistance here, pretty impressive.

**Dave Jones:** Goes down to as low as uh, 0.009% there for one-year accuracy. And there you go. The uh, ADC uh, multiple ramp. They've got a patent on this thing, German patent.

**Dave Jones:** Anyway, you can go look that one up if you want. I mean, you know, old hat these days, but uh back in the day would have been a big deal.

**Dave Jones:** And yeah, it's just an integrator. That's pretty much what it is. Now, as always, uh I'll link in down below to the EVblog.com website for the high-res teardown photos of this thing, plus the uh schematics as well.

**Dave Jones:** And this is the uh 6048 schematic. Uh so, that's the higher-end model, and that's the 6047. So, check the difference. There we go. I can see we've got some extra circuitry up here.

**Dave Jones:** As starters, what else have we got? Ah, yeah, there's quite quite significant differences happening down around here. And this is the 6048. This is uh some of the additional circuitry, obviously, to power the uh better reference, the LTZ1000.

**Dave Jones:** As you get uh same one you get in the Classica HP uh 3458A. And once again, would have been individually hand-selected. And if we flip over to the 80 um uh the 47 that we've got here, where there we go, the LM399.

**Dave Jones:** Even though what they what they got installed is an LM299, but basically the same thing. Ah, lovely relay sound. Beautiful. Anyway, I hope you enjoyed that uh teardown of this uh rather unusual Prema 6047 integrating digital multimeter.

**Dave Jones:** Bit embarrassed. I thought it was 8 1/2 digit. This is when you're rushing to buy stuff, just randomly, you know, you don't do your research properly. I thought it was an 8 1/2 digit uh meter, and I thought that the specs were the only difference between the two.

**Dave Jones:** But uh it's 7 1/2 digits. Anyway, I got to do some more uh work on this sucker, and um uh see if it is within spec. It just may need some uh warm-up time or something like that.

**Dave Jones:** Anyway, needs a fair bit more playing around, but yeah, rather unusual beast from the late '80s. Hope you enjoyed it. And as always, if you want to discuss it, EV blog forum is the place to do it.

**Dave Jones:** Catch you next time.
