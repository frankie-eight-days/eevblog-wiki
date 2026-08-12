---
video_id: FjlyLIpf4HU
title: EEVblog #1165 - Cypres Parachute Safety AAD Teardown
url: https://www.youtube.com/watch?v=FjlyLIpf4HU
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 18, "2": 41, "3": 59, "4": 73, "5": 104, "6": 125, "7": 145, "8": 167, "9": 185, "10": 211, "11": 231, "12": 244, "13": 263, "14": 283, "15": 300, "16": 312, "17": 327, "18": 342, "19": 362, "20": 379, "21": 397, "22": 411, "23": 428, "24": 444, "25": 457, "26": 475, "27": 490, "28": 504, "29": 528, "30": 544, "31": 563, "32": 580, "33": 600, "34": 618, "35": 634, "36": 660, "37": 681, "38": 707, "39": 726, "40": 743, "41": 758, "42": 776, "43": 795, "44": 811, "45": 827, "46": 846, "47": 863, "48": 884, "49": 898, "50": 910, "51": 929, "52": 945, "53": 963, "54": 981, "55": 1007, "56": 1013, "57": 1019, "58": 1025, "59": 1031, "60": 1037, "61": 1043, "62": 1049, "63": 1055, "64": 1061, "65": 1067, "66": 1073, "67": 1079, "68": 1085, "69": 1091, "70": 1097, "71": 1103, "72": 1109, "73": 1115, "74": 1121, "75": 1127, "76": 1133, "77": 1139, "78": 1145, "79": 1151, "80": 1157, "81": 1163, "82": 1169, "83": 1175, "84": 1181, "85": 1187, "86": 1193, "87": 1199, "88": 1205, "89": 1211, "90": 1217, "91": 1223, "92": 1229, "93": 1235, "94": 1241, "95": 1247, "96": 1253, "97": 1259, "98": 1265, "99": 1271, "100": 1277, "101": 1283, "102": 1289, "103": 1295, "104": 1301, "105": 1307, "106": 1313, "107": 1319, "108": 1325, "109": 1331, "110": 1337, "111": 1343, "112": 1349, "113": 1355, "114": 1361, "115": 1367, "116": 1373, "117": 1379, "118": 1385, "119": 1391, "120": 1397, "121": 1403, "122": 1409, "123": 1415, "124": 1421, "125": 1427, "126": 1433, "127": 1439, "128": 1445, "129": 1451, "130": 1457, "131": 1463, "132": 1469, "133": 1475, "134": 1481, "135": 1487, "136": 1493, "137": 1499, "138": 1505, "139": 1511, "140": 1517, "141": 1523, "142": 1529, "143": 1535, "144": 1541, "145": 1547, "146": 1553, "147": 1559, "148": 1565, "149": 1571, "150": 1577, "151": 1583, "152": 1589, "153": 1595, "154": 1601, "155": 1607, "156": 1613, "157": 1619, "158": 1625, "159": 1631, "160": 1637, "161": 1643, "162": 1649, "163": 1655, "164": 1661, "165": 1667, "166": 1673, "167": 1679, "168": 1685, "169": 1691, "170": 1697, "171": 1703, "172": 1709, "173": 1715, "174": 1721, "175": 1727, "176": 1733, "177": 1739, "178": 1745, "179": 1751, "180": 1757, "181": 1763, "182": 1769, "183": 1775, "184": 1781, "185": 1787, "186": 1793, "187": 1799, "188": 1805, "189": 1811, "190": 1817, "191": 1823, "192": 1829, "193": 1835, "194": 1841, "195": 1847, "196": 1853, "197": 1859, "198": 1865, "199": 1871, "200": 1877, "201": 1883, "202": 1889, "203": 1895, "204": 1901, "205": 1907, "206": 1913, "207": 1919, "208": 1925, "209": 1931, "210": 1937, "211": 1943, "212": 1949, "213": 1955, "214": 1961, "215": 1967, "216": 1973, "217": 1979}
---

**Dave Jones:** Hi, it's teardown time again and deja vu. You may remember the Cypress automatic activation device for parachuting that I did a teardown of many years ago and I'll link it in at the end of this video and down below if you haven't seen that.

**Dave Jones:** And that was an older model of this, as I said, Cypress automatic activation device it's called. It's designed for parachutists and it's a bit of life-saving equipment. Hence why this will be a very interesting teardown because the design and qualification of a life-saving product like this is a real big deal.

**Dave Jones:** So what it's designed to do is it's got a pressure sensor in here, an altitude sensor effectively. That continuously measures your altitude and if you're a parachutist and let's say you jumped out of your plane and you went, I don't know, unconscious for some reason.

**Dave Jones:** I'm sure there's a variety of reasons why, you know, you could lose consciousness or you're just too busy enjoying the view and you forget to pull the cord. Well, this thing will detect the change in air pressure, i.e. your height, and it'll detect your rate of fall and all that sort of stuff.

**Dave Jones:** And at a predetermined altitude, which you can program on this little doodad here. It will automatically cut your cord, your reserve or primary parachute, not exactly sure how it actually loops in and configures through to the system. It comes with a little cord here, which interlocks with your chute and there's a pyrotechnic charge in here and a very sharp blade in here that then cuts through your loop, which then automatically pulls your parachute.

**Dave Jones:** And the stats on this thing is actually very impressive. They've manufactured over 200,000 of these things. There's been 123 million jumps using this thing and it's saved over 4,000 lives with zero failures that they're aware of anyway, if you believe the marketing department.

**Dave Jones:** But anyway, that's a lot of lives saved. So this is a real critical bit of safety equipment for parachutists. Now, this is the Cypress Expert unit here. And you'll notice here. It's very, you know, slimline compared to the previous one, which I actually tore down.

**Dave Jones:** But, you know, basically it has the same looking controller like this and it looks like exactly the same pyrotechnic charge cutter on here. But they do have the Cypress 2 now. So I'm not sure if this is the Cypress 1, I guess, or if this is actually the Cypress 2 and the one we tore down previously.

**Dave Jones:** It's the Cypress 1. I'm not actually quite sure. Anyway, it's the Expert model, manufactured in '04, so it's quite old. And I've got to actually thank Angus Dauby for sending this one in. It's been on my teardown shelf for, I'm not going to say how long, but, you know, my miscellaneous devices.

**Dave Jones:** It was sent into the mailbag for a teardown. So this should be a fascinating look at the progress in engineering design. I don't expect spectacular progress. But small refinement. Small refinements between the previous generation of this unit, which was very interesting teardown. It was potted with a re-enterable gel and used primary lithium batteries and like a real old school microcontroller that's super rugged.

**Dave Jones:** And Angus said that this has to meet, of course, EMI requirements as well. So, yeah, it's going to be interesting to take this puppy apart. Unfortunately, the battery is dead and I'm not sure what battery it used. I assume you have to take the end off because it's got a filter on here which is actually replaceable after getting wet.

**Dave Jones:** How wet? Well, I assume if you fall through clouds or something, you know, get some moisture or whatever, do you have to replace it every time? I'm not sure. If anyone out there actually uses, is a parachutist and uses one of these things, let us know.

**Dave Jones:** Now, by the way, they do have a new model specifically for wingsuits because wingsuits descend at a much lower rate than a typical parachutist. You know, basically in free fall. Pretty much. Wingsuits, you know, you can fly around. You can stay up there for, you know, ages and descend much, much slower.

**Dave Jones:** So obviously like the rate of change and things like that and your requirements are very different and critically different to a parachute model. So they do actually, this is the parachute model. So they do have a specific wingsuit model. And also it's important for the pilots of the parachuting planes to actually be aware that these devices are being used.

**Dave Jones:** And they actually, Cyprus actually published guidelines for the pilots that they're not to descend faster than a certain rate, not to drop below a certain preset altitude and all that sort of jazz. Because the last thing you want is a whole bunch of parachutes going off in the back of the plane, all charges being cut.

**Dave Jones:** Anyway, I'm sure they wouldn't, you know, just deploy because there's no wind to actually deploy them. But still, it wouldn't be pretty, I'm sure, if a whole bunch of parachutes went off in the back of the plane. So if the cords got cut.

**Dave Jones:** Now with the display unit, you can actually preset your, like the altitude. You can put it in different modes like expert mode and there's a student model as well or a student mode and a fast free-fall mode and, you know, various other different things.

**Dave Jones:** And you can preset the altitude that you want it to release at. Now I think the previous model didn't have automatic calibration because pressure, of course, atmospheric pressure is going to change all the time as the weather changes. And that's how it determines your altitude.

**Dave Jones:** So the last thing you want is for you to calibrate in the morning and then you go jump in the afternoon and a big low pressure system, you know, or high pressure system has come through and it's completely changed that. And you could be off by, I don't know, I haven't ran the back of the envelope numbers, but you could be off by hundreds of meters, I'm sure.

**Dave Jones:** So, you know, it could be a big deal. So this one actually has, this new model actually has automatic calibration. It actually measures the air pressure twice per minute and then it takes an average of that. So it's always continually knowing that you're on the ground because you're not falling.

**Dave Jones:** It's obviously, you know, you could use software to detect that, obviously. And it auto-calibrates your ground level. So you don't have to worry about before you take off actually setting this thing. So, you know, press once and it switches on and it goes through a self-test routine and then it goes into auto-calibration mode.

**Dave Jones:** It's always measuring the ground average. It's always measuring the ground atmospheric pressure level. So it's auto-calibrated, so that's pretty cool. Now, obviously, this thing's going to be pretty well sealed. So you can see these grommets around here and I'm sure we'll see these in the teardown.

**Dave Jones:** Looks like we've got a little choke in there. And this connector here, let's take that off. Whoa, look at that. It's got an O-ring for nice moisture sealing on there. It's a TRS type one, but it's like, you know, it really is, I'm sure, it's carefully designed

**Dave Jones:** to be quite reliable because you need a super reliable contact. You don't want, you know, vibration and everything else. I'm quite concerned that there's no lock-in mechanism on there. Maybe they heat shrink that after it's gone on or something. And this one hasn't had that happen.

**Dave Jones:** I don't know if anyone, I mean, it requires quite a lot of force to take it off. But still, I wouldn't rely on just that O-ring seal to do that. So I'm not sure what the deal is there. But anyway, it's very nicely constructed.

**Dave Jones:** The cable-ins are rated and, you know, all this stuff. I'm not sure if there's any, like, government regulations for these sorts of things. But basically, Cyprus are number one in the business. And so they do take, like, you know, the safety compliance of all this sort of stuff extremely seriously.

**Dave Jones:** So yeah, I'm sure it's, they probably invented their own standards. And if they follow, if there are any other regulations, then I'm sure they follow that as well. But yeah, it just oozes quality, this thing. Super rugged, as you'd expect. So anyway, let's get inside this thing.

**Dave Jones:** We've got four screws on the end here and four on this end. So hopefully it all just comes apart. I assume it's going to be potted like the old one, or at least part of it. There's going to be probably like a lithium primary battery in here

**Dave Jones:** because you don't want any of that rechargeable rubbish. When you've got a super reliable product like this that you have to ensure works, you want the best quality and probably certified. Batteries as well, lithium primary ones. You know, you'd probably like Panasonic. I remember when I worked on underwater stuff which used D cell lithium primary cells.

**Dave Jones:** We would specifically buy them from Panasonic and they'd actually come with a certification certificate that they're actually, you know, these batteries have been manufactured to X compliance and tested and everything else to ensure that we guarantee that we're going to get, you know,

**Dave Jones:** the 10, 12 or 15 year battery life or whatever it is we required at the time. And it would still have sufficiently low ESR and capacity to trigger, in our case, a sensor, a heating element which actually burst a flotation bag of something on the ocean surface

**Dave Jones:** which then caused it to sink and sink to the bottom of the ocean. Okay, that looks like a T3 Torx, little self-tappers. Don't know how often you'd have to replace the battery in this thing. If it was anything like the previous one, I think it was, you know,

**Dave Jones:** for the compliance life or the service life of the thing. The previous one used large, I think they were D cells. Have to re-watch the, re-watch the video. Oh, not sure what's going on there. How does your filter come out? Oh no, the filter just unscrews, oh yeah, just unscrews like that.

**Dave Jones:** There's the port for our pressure sensor. The pressure sensor, typical like a gauge type port with the extended nose on that. Okay, managed to get that off. Just got the screwdriver in there and just pulled it off. This is the end bit. And there, see the O-ring around there?

**Dave Jones:** That's what you expect to prevent moisture ingress. Oh, and we're in Lake Flynn. There's the end of it down there. We've got some sponge. Oh, that's a hard cell, that's a hard cell phone. Get that end off. Ah, there we go. There we go.

**Dave Jones:** Yeah, we've got a hard cell foam on there. Like the previous unit, we have a, like a soldered shut can for everything. So, yep, very similar to the previous one. So, there's your RFI compliance right there. Oh, something, doodad, is that a, that's a MELF, it's a MELF resistor for you.

**Dave Jones:** MELF resistor fanboys. Card carrying. There we go. Why there's a resistor on that, not sure. External? Hmm, what would be the purpose of that? Anyway, this is interesting. Check this out. They've got a wire soldered onto the can here, which goes over to this board here,

**Dave Jones:** which has a couple of little SOT23s on it. Are they little transistors or are they diodes or whatnot? But, yeah, it goes over to here. And what is going on there, they have this external and then three wires going back into, well, actually, no, onto that other PCB up the top, which has that MELF resistor.

**Dave Jones:** So, some more hard cell foam in here. No wuckers, so they're keen on their hard cell foam. Anyway, it certainly doesn't have a user replaceable battery in this thing. As you'd expect. But, of course, the microcontroller can be ridiculously low power. And the LCD takes bugger all.

**Dave Jones:** And the pressure sensor, I can't offhand. It's been so long since I've dealt with pressure sensors. But, like, it only powers up, as I said, twice a minute or something like that. So, presumably, when it detects that you've gone up in altitude and then you're starting to jump,

**Dave Jones:** I presume it would sample faster than twice per minute. So it goes into sort of like a higher power mode. But even then, you know, your power consumption from a large -- it probably uses CR123. But not your traditional bump and then contact ones.

**Dave Jones:** You don't want contacts in here. You want a -- for the utmost in reliability for all these emission-critical applications, you want welded contacts directly onto the primary battery. So, looking at the size of this thing, I'd say, you know, probably two CR123 lithium primary batteries would be the go.

**Dave Jones:** Anyway, um, yeah, not sure what that protection doodad is. Especially like it comes out and then, like, it, like, shield and then goes into there. Some sort of, like, some sort of ESD protection or something. Why it's not internal? Why it's external and not internal?

**Dave Jones:** I don't know. Oh, no, I just noticed those wires don't go onto that PCB. They go through like that. That's a little bit how you're doing. But, of course, these things don't move once they're all in place. So, there's no problems against the, like, wear against the fiberglass or anything like that.

**Dave Jones:** But, um, yeah. And then the other one, uh, just goes -- this is the activation. The, uh, pyrotechnic charge cable. And it goes through there as well. I'm not sure if you can see that, but it does go through a hole in that PCB there.

**Dave Jones:** So, there's really nothing else connected to that board except that MELF resistor. Still don't get it. Ooh, ooh. This is easy to come apart. I just did that with my finger. Ta-da! Oh, more hard-cell foam. So, if you see the previous video, I highly recommend it.

**Dave Jones:** Then you'll know that that was all, uh, re-enterable potting gel. And it was horrible, horrible stuff. So, they've gone for the hard-cell foam in this case. So, that's interesting. But we should just be able to peel off this can quite easily. Well, the good thing is, is that it's not one continuous wrap.

**Dave Jones:** It just has these, uh, plates on here like this. So, we should be able to get the iron on there and simply remove all these plates. Sweet. Too easy. Ah, too easy. In like Flynn. Cut out for a cap there. Ah, this is much easier to get into than the previous one, I can assure you.

**Dave Jones:** My finger's going to burn before it releases. Tune in next week. Oh. The foam's going to come off. Oh, look. Oh, no. We've still got some of the re-enterable potting gel. Hang on. I'll show you in a minute. This is going to be, this is going to be an interesting tear-down.

**Dave Jones:** Well, it already is. I think there's some bloody tab there. Argh. Okay. Here we are. Oh, no. That's not a CR-123. There you go. Single battery. Makes sense. They didn't have enough room for anything else. You can see the, the re-enterable potting gel.

**Dave Jones:** There you go. Oh, no. That's not a CR-123. There you go. Single battery. Makes sense. They didn't have enough room for anything else. They didn't have enough room for anything else. You can see the, the re-enterable potting gel there. It's always fun, icky stuff to play with, but I've used this before.

**Dave Jones:** It's really good, because it means that not only does it prevent moisture ingress onto your boards, but it means that you can get through, you can, you can stick your screwdriver through it like this, and then adjust your pots on your board, which I've had to do many

**Dave Jones:** times. And then when you pull it back out. It seals shut again. So it's, it's really nice stuff. It's called re-enterable potting gel. Oh, geez. This is going to be, this is not going to be pretty. Anyway, there's wires running all, snaking all over the place.

**Dave Jones:** Didn't expect that. And there's our micro. So the hard cell phone, that'd be thermal insulation would be my guess, although why it's not, you know, on the sides and everything else, I guess you just need it over those parts. But anyway, there's the battery on the end, just to, just to provide some thermal insulation

**Dave Jones:** on there. Oh, the battery just fell out. There you go. Yep. Welded tabs on there. No worries whatsoever. There you go. That's an ER 1850, 87? Is that, no, that's not the date code. Anyway, I'll measure that. See if there's any, no, no, absolutely not a sausage left in that pot.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out. I'm going to try and get it out.

**Dave Jones:** Thank you.
