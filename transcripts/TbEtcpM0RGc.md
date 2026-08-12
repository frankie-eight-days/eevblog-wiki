---
video_id: TbEtcpM0RGc
title: EEVblog #344 - Fluke 17B Multimeter Teardown
url: https://www.youtube.com/watch?v=TbEtcpM0RGc
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 33, "3": 44, "4": 51, "5": 65, "6": 85, "7": 100, "8": 131, "9": 143, "10": 158, "11": 181, "12": 198, "13": 209, "14": 220, "15": 236, "16": 254, "17": 264, "18": 277, "19": 287, "20": 299, "21": 310, "22": 326, "23": 334, "24": 356, "25": 370, "26": 384, "27": 397, "28": 428, "29": 442, "30": 464, "31": 479, "32": 492, "33": 508, "34": 523, "35": 541, "36": 553, "37": 568, "38": 580, "39": 597, "40": 613, "41": 627, "42": 642, "43": 658, "44": 673, "45": 687, "46": 702, "47": 720, "48": 732, "49": 744, "50": 753, "51": 764, "52": 777, "53": 792, "54": 803, "55": 820, "56": 833, "57": 846, "58": 857, "59": 869, "60": 883, "61": 899, "62": 921, "63": 943, "64": 959, "65": 986, "66": 1007, "67": 1024, "68": 1055, "69": 1088, "70": 1121, "71": 1144, "72": 1163, "73": 1177, "74": 1195, "75": 1208, "76": 1224, "77": 1236, "78": 1257, "79": 1270, "80": 1283, "81": 1294, "82": 1308, "83": 1324, "84": 1337, "85": 1359, "86": 1376, "87": 1387, "88": 1399, "89": 1412, "90": 1426, "91": 1437, "92": 1456, "93": 1471, "94": 1484, "95": 1498, "96": 1513, "97": 1525, "98": 1540, "99": 1548, "100": 1562, "101": 1571}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We haven't had a moldy meter for quite some time, let alone a Fluke. So, we've got the Fluke 17B moldy meter courtesy of Todd from toddfun.com.

**Dave Jones:** Thanks, Todd. Uh you saw this in the mailbag the other day, and it's the cheap ass made in China Fluke, supposedly designed by the Fluke Group, but you know, manufactured to a low price point in China, and it's only marketed and sold in China.

**Dave Jones:** Although, I um have seen reports that it has actually gone into India as well. Go figure. But, anyway, it's like it's under 100 bucks delivered or something like that.

**Dave Jones:** I think it's retail, might be slightly uh more than that, but you can certainly get it on the street. Um some people have reported even as little as 60 or 70 dollars.

**Dave Jones:** And, well, curious to see what's inside this thing. Does it live up to the Fluke reputation? Is it as good as a Fluke 87? Well, there's only one way to find out.

**Dave Jones:** You know what we say here on the EEVblog? Don't turn it on. Take it apart. And here it is, and we'll benchmark it against the classic Fluke 87V, pretty much the industry standard meter, and the the main meter that uh Fluke one of the main meters Fluke made their reputation on, and they still do.

**Dave Jones:** Let's have a look, tear it down, see what the build quality is like inside, cuz outside it it feels just like a Fluke. It's robust and rugged. The plastic, the quality of plastic feels good.

**Dave Jones:** The range switch seems, you know, reasonable. And if we try and have a look at the quality of the plastics here, it it the 87 certainly uh which is this one here compared to the uh 17B on the left there, the quality of the plastics it it just it you know, I'm no plastics expert, but from experience the Fluke plastic just seems like a a better like it's probably

**Dave Jones:** an impact resistant polymer plastic. I'm not sure if the 17B is it just seems to be a different type and it's not just the finish either. It's All right, let's get into the screws here.

**Dave Jones:** These will be self-tappers, no doubt. And they certainly feel like self-tappers. There we go. No difference there. There I don't Oh, yeah, they're the similar thread. We'll compare the threads later.

**Dave Jones:** I don't think they're the same as the 87 5 though, but uh Yeah, I'm not surprised that they're using self-tappers there at all. It's good enough for the Fluke 87, so I guess they figure it's good enough for the 17B made in China.

**Dave Jones:** Wouldn't it be ironic if uh this one actually had nice metal threaded insert screws. Anyway, the 87 5 is quite an old uh model. This is interesting, actually. Um Just really notice this.

**Dave Jones:** They've got this recess here, which uh I don't know what's designed to go into there. Um there doesn't seem to be anything matching on the uh Oh, that's okay.

**Dave Jones:** No, that's the holder. Yep. All right, that's the uh just the recess for the magnetic hanger holder in there, which you didn't get with it, by the way. So, let's try and open it.

**Dave Jones:** I don't think the battery has to come out, so Oh, too easy. Look at that. Beautiful. And the The reaction upon opening this is that they've done a really good job of it for such, you know, a low-cost meter.

**Dave Jones:** It's certainly uh certainly very well laid out and it looks very well built. I mean, it's built down into a price as we'll go into uh seeing a few things which uh make that happen.

**Dave Jones:** But, so they're doing all the right things here. We've got um HRC fuses which we'll get into not as good as the 87, of course, but at least they're there.

**Dave Jones:** We've got a um input protection thermistor, large input protection resistor. Uh it looks like a high-voltage uh network of 1206 resistors there all in series. We've got um MOVs on the input.

**Dave Jones:** Looks like three of them. I'm not sure if they're all paralleled up. They're probably doing uh different um input uh ranges. And, you know, they've done a reasonably good job.

**Dave Jones:** We've got a uh chip on board completely uh epoxy blob there. Obviously, room for a uh secondary uh quad flat pack uh footprint there. I guess it depends on which one they can get this week, perhaps.

**Dave Jones:** I don't know. If anyone else has a 17B open up and let us know if you actually have a QFP footprint device. So, maybe that was during development or something like that.

**Dave Jones:** And then, when they went into uh high-volume high-volume production, they probably went for the uh chip on board like that. You can see it's a multi-layer uh board. And uh you can see the shielding they've put underneath all of the main circuitry up here.

**Dave Jones:** Of course, I'm a big fan of the battery uh contacts directly on like that. That's much better than the uh 9-V battery snap in the old design uh Fluke 87.

**Dave Jones:** It's really Fluke 87's really showing its age there. But, you know, they've there's no wiring uh in this thing at all, of course, which is excellent. And it's lacking the uh thick film resistor uh hybrid, the precision resistor divider, which we'll get into when we look at the 87 five, of course.

**Dave Jones:** But that's that's what you'd expect, you know, this is you know, only a sub $100 class instrument. It's not going to use a Fluke, you know, high-end network in it.

**Dave Jones:** But they've done a reasonable job. The input jacks aren't nearly as good as the 87, which we'll get into. But generally, at first glance, this looks like a very well-designed and built $100 class multimeter.

**Dave Jones:** Now, I'll start off with the 10 amp fuse here, and it is a little fuse branded 11 amp HRC fuse with a 20 kiloamp interrupting current. And that's the basically the same.

**Dave Jones:** It's a different brand, but it's it's still a good brand. But it's the same as what's used on the Fluke 87 five. Excellent. But if you compare that to the Fluke 87 five here, they do actually have some blast shields separating that and also keeping it in place from sliding out, because there's nothing on the 17B here to stop this fuse vibrating loose and actually not making contact.

**Dave Jones:** It's very unlikely to happen, but in theory, it's possible. And on the milliamp side, we don't have the same 20 kiloamp interrupting current fuse as you do on the 87 five.

**Dave Jones:** So, they have cut costs there a bit, but it's a Seba brand fast-acting ceramic 500 milliamp fuse. You know, they're sort of they're almost high rupture capacity. I don't actually know what the interrupting uh current of this one is, but it's certainly better than a cheapo glass fuse.

**Dave Jones:** More than good enough on this class instrument. Now, as for the 10 amp current shunt here, uh it's pretty ordinary, but I've seen a lot worse. It's uh certainly not like the uh tapped one used on the Fluke 87.

**Dave Jones:** And you can see the Fluke 87 one down in there. It's just a much nicer implementation of a 10 amp uh current shunt with the uh tapped uh four-wire measurement like that coming off the side.

**Dave Jones:** And for the AC coupling cap, it's a Wima brand MKS 1000 V 10 uh nanofarad. They haven't skimped on the brand there at all. And as for the input resistors here, they've got uh five 200 K 1206s in series like that.

**Dave Jones:** The reason they've done that is to uh give a high-voltage resistor. Instead of using a single 1 mega resistor, they've gone for five 200 Ks in series, which uh increases the voltage threshold across the entire resistor.

**Dave Jones:** So, they've uh certainly um haven't skimped there at all. They could have just used the 1 mega and relied upon the uh you know, the the poor um uh voltage uh breakdown, the creepage distance between a single uh 1206 like that or two of them or something like that.

**Dave Jones:** But no, they've gone to the effort to put five in there. The input thermistor there, I don't recognize the symbol or the brand. It's uh 111 two. And the MOVs here are marked TVR 911.

**Dave Jones:** Once again, uh not something I recognize, but uh they look like they can do the business. And down around this circuitry here, we have a Linear Technology LT 1097 by the looks of it.

**Dave Jones:** And that's a precision op-amp. So, they've used one of the most expensive brands in the business, Linear Tech. They're probably getting it very cheap, but uh still they haven't skimped there.

**Dave Jones:** And here we have a Texas Instruments 74HC148, a priority encoder there. We've got our main crystal over there. What is that? 4 MHz? Drives the processor. This will prob you know, don't ask me what uh uh chip they got under there.

**Dave Jones:** I got no idea. I could attempt to uh probe it of course, but that would uh take quite a significant uh amount of time, but you could maybe work it out from the uh pinout if you uh know your um various multimeter uh chipsets.

**Dave Jones:** So, if anyone wants to have a crack at that and uh figure out which uh chipset that possibly is and uh which means we can possibly uh mod this thing, then please go for it.

**Dave Jones:** Now, this meter um shows its heritage in the original Fluke 19 from more than a decade ago. And that the Fluke 19 was uh Fluke's first attempt at a Chinese-made multimeter, and it failed uh dismally.

**Dave Jones:** A ton of them out in the field just uh failed. I don't think there's uh many left uh you know, working these days. And um that I believe um used to use the chipset out of the Fluke 87.

**Dave Jones:** They just leveraged it. Um but this one is uh clearly not doing that. So, they've used some other presumably um off-the-shelf multimeter chipset. And of course, one of the things you'll notice on this meter is the multitude of trim pots, adjustment trim pots.

**Dave Jones:** There's five there, and there's another three over here. Eight total trim pots. And of course, a meter like the Fluke 87 of course doesn't have any trim pots at all.

**Dave Jones:** It's all electronic uh closed-case calibration and all that sort of stuff. So, you know, this clearly shows it's um uh you know, the hallmarks of uh of being, you know, a 50 or $100 class multimeter in that respect.

**Dave Jones:** But uh certainly the solder quality on this thing is uh first class. I mean, barring the uh 10 amp current shunt there, but that's um very common for these um uh I believe, you know, these are nichrome resistors.

**Dave Jones:** It's probably a nichrome resistance wire or something like that. So, that's very common. It's not actually um a bad joint on there. That's just the way that they often uh form on these current shunts.

**Dave Jones:** Uh you know, but apart from that, the soldering quality is excellent. The build quality is uh quite excellent for, you know, this class of instrument. No, you know, well above the pack.

**Dave Jones:** So, where have they saved cost on this thing? Well, you know, we've seen a few things uh already in terms of the uh 500 milliamp fuse there, for example.

**Dave Jones:** But the other one is of course the input jacks. And if you take a look at them, they're just, you know, classic uh one hung low brand uh you know, multimeter input jacks.

**Dave Jones:** The plastic receptacle here is molded into the main case and there's a uh threaded metal insert there, of course, molded into the plastic itself. And they've used a screw there.

**Dave Jones:** Um doesn't look like there's any uh shake-proof washer under that with just the bent metal going down to the PCB at the bottom. Um and they started this, I believe that's identical to the uh Fluke uh 19 of uh a decade ago.

**Dave Jones:** But anyway, that's very synonymous with um cheap meters. There's nothing in that bad with it. It's um but it's not in the same class as the ones on the Fluke 87.

**Dave Jones:** And if you take a look at the classic Fluke 87, of course, they have a fully custom uh input jack uh molded enclosure like this that would be high quality impact resistant polymer or something like that.

**Dave Jones:** They've got the O-ring seal around here to keep out uh dust and uh moisture from getting into the meter. And it, you know, it really is a different um class of input jack there.

**Dave Jones:** And you'll notice the you know, the high voltage um isolation slot cutouts between each connector. You know, there's no real uh contest there at all, but this is, you know, and don't get me wrong.

**Dave Jones:** This is certainly um adequate. And I just took that screw out, and it really I had to put a lot of force on that to get that out, and then it went snap, and then it uh unscrewed.

**Dave Jones:** But um as I suspected, there is no um uh shake-proof washer on there at all. But if you have a look at the input jacks down in there, they are a uh nice solid input jack.

**Dave Jones:** They're not actually uh split like they are on the 87V input jack um sensing. But they're uh you know, they're certainly solid enough and good enough for this uh price class of instrument.

**Dave Jones:** Now, you might notice on those uh what look like gold um pads there, that they're uh tarnished. They're fairly well tarnished. They have actually scraped away a bit of the uh pad there, and it's certainly much shinier there.

**Dave Jones:** And I don't think that's gold plated. I think that might even be uh bare copper there. That's why it's actually uh tarnished. If we compare that with the Fluke 87V five over here, you can see the gold pads here, but it's got a similar sort of um bare uh copper uh that there on the boards.

**Dave Jones:** Now, of course, another place that they've skimped is the shielding because you'll notice that there's no removable uh metal shield on this. There's no uh spring which comes up to a shielded um you know, foil uh insert in the back of the case or anything like that um as opposed to the uh Fluke 87, which we'll show you.

**Dave Jones:** Although, as I pointed out, you can see the uh um the uh ground plane shielding under on on the inner layer on the board under all the main circuitry there, but in terms of like just the overall uh shielding the input uh circuitry, it's um it's just not there.

**Dave Jones:** Whereas, the Fluke 87, of course, has the uh metal shielding on the back like that. And I I actually don't quite know why I'm comparing, you know, this class of instrument, the 87 5, to this, you know, made in China um one which is, you know, a uh quarter or a fifth of the cost or something like that um or even uh less and uh and of course, doesn't come with the

**Dave Jones:** lifetime warranty. But anyway, it gives us a benchmark to what we're uh comparing to. And they've decided to go with the uh cheap PCB mounted uh piezo there as opposed to the uh Fluke 87 5, which has, you know, the beautiful um piezoceramic um buzzer on the back with the nice gold-plated spring terminals.

**Dave Jones:** Beautiful. And although you can get reasonably loud uh versions of these, that uh most likely um explains the uh piss-weak continuity buzzer in this thing. If you uh heard if you watched the uh mail bag, I demonstrated that compared to the Fluke 87, no contest.

**Dave Jones:** This one's a shocker. And here's a comparison of the two boards side by side. I've fully extracted the uh Fluke 87 5 board uh out of here and of course one thing we're going to look at is the resistor hybrid network here because that is of course what's lacking on virtually all you know multimeters in this sort of class you really have to step up to the you know

**Dave Jones:** point zero five percent or better you know really expensive class multimeters before you start getting that resistor hybrid there. So you know in this case we've got the trimmers and just you know pretty bog standard ordinary stuff and the 87 five has Fluke branded stuff there but if we have a look at the thick film resistor hybrid there it is that's actually a precision resistor divider and these are actually

**Dave Jones:** reasonably expensive and well qualified components and you simply do not find them in the 50 or 100 dollar even the 200 sometimes the 200 dollar class meters you you just don't get them and that's what's missing in the you know 17B here and of course you would expect it to be missing cuz that's you know they can't afford to include an expensive precision low drift resistor input divider like that so

**Dave Jones:** because and effectively you don't need it because the performance you get in one of these 0.5% class multimeters you can just use all standard parts and your drift is going to be perfectly acceptable so there's absolutely nothing wrong with that not having one of those I wouldn't have expected one in here and I would have called them crazy overkill if they did use it now I've taken the board out

**Dave Jones:** let's have a look at the back side of it and there's a few things of note here one is that they've actually uh greased it up. You can see all the grease all around there, so they've obviously decided that uh they needed to grease this sucker up for good operation.

**Dave Jones:** Another interesting thing to note is the shape of the soft button contact pads in there. And if we look at the Fluke 87 5, look at that. They're identical.

**Dave Jones:** So, that really goes to show that it does look like the same design team um using probably the same component library have uh laid out the Fluke 17B. So, it looks like they you know, most likely haven't outsourced this thing.

**Dave Jones:** It's done by the same group as the 87V, I would suspect, cuz that's identical and that's not a coincidence. And that's the locking clip on the back of the range switch on the 87V.

**Dave Jones:** And if you have a look at the 17B here, very similar construction in terms of the retention clip there. And I've popped it off and you can see all the grease in there and the gold plating on those pads looks uh decent quality.

**Dave Jones:** I don't think they have skimped there. And the back of the uh range switch is a um classic uh two uh dual contact um spring arrangement. So, let's compare that to the 87V.

**Dave Jones:** Well, the 87V is uh different, of course, being that there's no grease in there. But and the um uh contact arrangement is uh different as well. They use a uh four uh leaf terminal system as opposed to the two leaf terminal contact one on the 17B.

**Dave Jones:** But really, I mean, you know, I'm uh certainly not going to complain about that at all. That range switch looks pretty good. Clearly, it's a you know, the Fluke heritage there.

**Dave Jones:** It looks pretty much identical in terms of implementation there with the plastic with the you know, the moving arms on there that sort of snap into the next location.

**Dave Jones:** The 87 5 which is the one on the right here, it differs in that it's got a metal insert in the middle there, just a metal post and the 17B doesn't.

**Dave Jones:** So they you know, skimped a little bit but it's a similar arrangement. You can see the same design and the same heritage there. Clearly, this meter is clearly done by the Fluke design group.

**Dave Jones:** But I've got to say that the 87 5 implementation is a nicer one. It just feels a little bit better but there's there's not much in it. I mean the certainly the range switch on the 17B gets the thumbs up.

**Dave Jones:** And the middle inserts on those look deep and uh these posts feel really solid too. I don't uh have any problem with those at all. I can't budge those.

**Dave Jones:** They feel really nice and well molded. I like it. And in terms of other aspects of the design, they do have a very deep tongue and groove arrangement for the case like that for blast shielding for you know, if this thing uh if you connect it to a high energy circuit, it's going to that's going to help really contain the blast in there.

**Dave Jones:** And there you have it. That's the Fluke 17 B. And what do I think? Well, I'm actually very impressed. This is probably the best built uh meter in this price class.

**Dave Jones:** I'm probably by far and it's not surprising. It's got the Fluke name on it. It's what you'd expect. What would you think of when you were going to buy, you know, a sub $100 Fluke?

**Dave Jones:** What would you expect them to get right? Well, Fluke are known, of course, for their legendary um input protection, you know, safety. And you certainly get that on this.

**Dave Jones:** This is a uh CAT II uh 600 V CAT I 1 1000 V rated input. And the input front end is designed properly and uh you know, it's well protected.

**Dave Jones:** They haven't skimped there at all. They have skimped on the places you'd expect uh them to on this class of instrument. You don't expect the uh thick film uh precision resistor hybrid in there.

**Dave Jones:** You don't expect any custom Fluke uh parts. They're probably just using an off-the-shelf uh chipset, same as uh everyone else with this uh same functionality. They've skimped on the buzzer a bit.

**Dave Jones:** I don't like that, but you know, um they've skimped in terms of uh you know, calibration of this thing. There's They're just using off-the-shelf pots. It's probably, you know, straight out of the app note this implementation for uh this particular chipset, whichever one they're using.

**Dave Jones:** Skimped a little bit on the 10 A current shunt and on uh the 500 mA fuse. They've skimped a bit on the input jacks as well. There's no, you know, O-ring sealing around the jacks or uh rubber sealing around the base of the case.

**Dave Jones:** And they've left out a true RMS uh converter as well. That uh saves them a uh significant penny on the bill of materials, I'm sure. And of course, they've skimped on the rubber holster.

**Dave Jones:** This is really lightweight and flimsy, you know, and it doesn't have the impact protection absorbers in there that the really, you know, much thicker and much uh stiffer 87-5 holster has.

**Dave Jones:** And that's where they've um you know, skimped on the price of this thing. But yeah, and that's exactly what you'd expect when you think of um you know, a a cheap $100 made in China Fluke.

**Dave Jones:** It delivers exactly as promised. And I like it. It should be should be, don't quote me, but uh I get a good vibe from this thing. It's all about the vibe.

**Dave Jones:** And uh you know, I think this will um last a long time. It's a certainly worth the dollar investment. But um as you'll probably see in the review, it is poor, very poor uh bang per buck this thing.

**Dave Jones:** Um you know, it's a very basic meter. But if you want a very well-built basic meter with that Fluke name on the front, it's a winner. So, there you go.

**Dave Jones:** Here's a teardown of the Fluke 17B digital multimeter, available only in China and India, I believe. And thanks to Todd from Todd Fun for donating this for the teardown and review.

**Dave Jones:** And if you like the uh teardown, if you like Teardown Tuesday, please give it a big thumbs up. And if you want to discuss it, jump on over to the EEVblog forum.

**Dave Jones:** The link is below in the description. Catch you next time.
