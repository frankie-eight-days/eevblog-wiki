---
video_id: ETopbGankfo
title: EEVblog 1663 - BM786 Multimeter REPAIR + InEr Error Investigation
url: https://www.youtube.com/watch?v=ETopbGankfo
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 18, "2": 34, "3": 55, "4": 73, "5": 92, "6": 109, "7": 122, "8": 137, "9": 153, "10": 176, "11": 197, "12": 215, "13": 230, "14": 250, "15": 268, "16": 284, "17": 307, "18": 329, "19": 344, "20": 361, "21": 377, "22": 390, "23": 402, "24": 419, "25": 438, "26": 458, "27": 471, "28": 483, "29": 490, "30": 498, "31": 504, "32": 510, "33": 516, "34": 522, "35": 528, "36": 534, "37": 540, "38": 546, "39": 552, "40": 558, "41": 564, "42": 570, "43": 576, "44": 582, "45": 588, "46": 594, "47": 600, "48": 606, "49": 612, "50": 618, "51": 624, "52": 630, "53": 636, "54": 642, "55": 648, "56": 654, "57": 660, "58": 666, "59": 672, "60": 678, "61": 684, "62": 690, "63": 696, "64": 702, "65": 708, "66": 714, "67": 720, "68": 726, "69": 732, "70": 738, "71": 744, "72": 750, "73": 756, "74": 762, "75": 768, "76": 774, "77": 780, "78": 786, "79": 792, "80": 798, "81": 804, "82": 810, "83": 816, "84": 822, "85": 828, "86": 834, "87": 840, "88": 846, "89": 852, "90": 858, "91": 864, "92": 870, "93": 876, "94": 882, "95": 888, "96": 894, "97": 900, "98": 906, "99": 912, "100": 918, "101": 924, "102": 930, "103": 936, "104": 942, "105": 948, "106": 954, "107": 960, "108": 966, "109": 972, "110": 978, "111": 984, "112": 990, "113": 996, "114": 1002, "115": 1008, "116": 1014, "117": 1020, "118": 1026, "119": 1032, "120": 1038, "121": 1044, "122": 1050, "123": 1056, "124": 1062, "125": 1068, "126": 1074, "127": 1080, "128": 1086, "129": 1092, "130": 1098, "131": 1104, "132": 1110, "133": 1116, "134": 1122, "135": 1128, "136": 1134, "137": 1140, "138": 1146, "139": 1152, "140": 1158, "141": 1164, "142": 1170, "143": 1176, "144": 1182, "145": 1188, "146": 1194, "147": 1200, "148": 1206, "149": 1212, "150": 1218, "151": 1224, "152": 1230, "153": 1236, "154": 1242, "155": 1248, "156": 1254, "157": 1260, "158": 1266, "159": 1272, "160": 1278, "161": 1284, "162": 1290, "163": 1296, "164": 1302, "165": 1308, "166": 1314, "167": 1320, "168": 1326, "169": 1332, "170": 1338, "171": 1344, "172": 1350, "173": 1356, "174": 1362, "175": 1368, "176": 1374, "177": 1380, "178": 1386, "179": 1392, "180": 1398, "181": 1404, "182": 1410, "183": 1416, "184": 1422, "185": 1428, "186": 1434, "187": 1440, "188": 1446, "189": 1452, "190": 1458, "191": 1464, "192": 1470, "193": 1476, "194": 1482, "195": 1488, "196": 1494, "197": 1500, "198": 1506, "199": 1512, "200": 1518, "201": 1524, "202": 1530, "203": 1536, "204": 1542, "205": 1548, "206": 1554, "207": 1560, "208": 1566}
---

**Dave Jones:** Hi, I've got another returned Bryman BM786 multimeter. Yes, all the electrons have fallen out of this one. It's been returned for an insertion error fault where it gives the insertion error message, the input jack alert, basically. In fact, I've got another one here.

**Dave Jones:** So this one was another one failed, insertion error on all ranges. So I'll turn this one on and you'll see, put it on volts and it just beeps insertion error. So it's going to beep on all ranges, so it'll only turn off. Oh, does it on milliamps and microamps too?

**Dave Jones:** Anyway, this one that was sent back, it only happened on the volts and ohms ranges. It didn't happen on the milliamp ranges. So, of course, there's input jack detection on the milliamp and the amps jack here that actually detects whether or not you've got the probe plugged in,

**Dave Jones:** just so that you can't, you know. Goof it up and accidentally measure amps when you're meant to measure a voltage. And this is why you get split jacks like this. You can see they've got isolation split in there and physically, these two are actually connected down to the fuse down here, all right?

**Dave Jones:** So that's the actual contact that makes contact with the probe. There's also another contact here, which is a sense terminal and goes through a resistor over here. So this is the amps jack and this is the milliamps jack here. And it just jumps over to here and also, we're sensing off that one as well.

**Dave Jones:** Now, I suspect what's causing this, and I have had, quite a few people have had this before, and I said, well, my first response is clean the contacts, the input jacks with, you know, isopropyl and, you know, get them out, even take the board out and give it a wipe and a flush and everything.

**Dave Jones:** And that has actually gotten rid of the problem because if you get contamination down through your input jacks here, you know, you're in a grubby environment and stuff. I used to work in a factory environment where we would have mineral oil around everywhere

**Dave Jones:** because that was part of our product. So it'd always get in the jacks and stuff like that and it can pick up contaminants. And even if it's insulative in its own right or whatever you put in there, whatever crap you get in there might be insulative, but it can carry, you know,

**Dave Jones:** particulate matter and stuff like that, which makes it conductive. And of course, these will be a high impedance path going back, but I don't have a schematic for this. So anyway, I thought we'd just take a look at it. So obviously, right, so here's our amp jack here, okay?

**Dave Jones:** And then our sense terminal goes off to this resistor here. So this jobby, which then goes off over to here, and then that goes off over to here. Now this looks like, looks like some sort of fusible resistor, is it? So yeah, I don't know because I don't have the part number, I don't have the schematic or the bill of materials.

**Dave Jones:** And there it is, 5 meg, okay? So we've got, and this one we'll be doing identically here. So if we follow, yeah, follow that one, that jumps over and that would be that 5 meg resistor jumping over to there. So we've got these two points here that will be going off to whatever sense circuit is in here.

**Dave Jones:** I don't know how they're actually detecting that, but they actually detect that it's shorted over to the other terminal. There you go, you can actually see the split. And you can see the split jacks down in there. Now split jacks aren't as reliable as like full solid jacks, but I've never had an issue with these Bryman ones.

**Dave Jones:** But in theory, they're not as solid as a, you know, a big solid machined jack or anything like that. So a sense circuit via this 5 meg resistor on the probe line, they've got this big high voltage 5 meg resistor here. So it protects all the electronics further on.

**Dave Jones:** So yeah, you want high impedance, high voltage, and to protect anything that's connected to the resistor. Of course, multimeter design 101. So yeah, so they can detect that it's actually connected over the fuse, which of course goes down to ground here. So it's easy to do that input jack alert, but I suspect because it's a high impedance circuit,

**Dave Jones:** so any contamination between these two terminals here or here, like this, any like physically inside the jack or on the PCB or whatever, then it could easily think, because it's very high impedance, it doesn't take much impedance to upset anything, but this, I'm not sure of the thresholds, I've never actually tested.

**Dave Jones:** Like I could put like a decade box on there or something and try and see at what point it triggers and stuff like that. But anyway, I'm going to measure these. So let's turn our multimeter on. And I suspect that we might have some contamination on here if my theory is correct.

**Dave Jones:** So, ah, bloody sharp probe master probes. They're ridiculously sharp, ouch. Bloody, look at them. Look at these suckers, they're just incredible. Probe master probes, amazing. So I've got a 100 megaohm range there, so I'm not sure which one it is because it only needs to be one of them.

**Dave Jones:** I don't know if it's one or both, right? So let's measure across there, and 13 meg? Is that normal? I don't know, we need to look at a reference. So, going across here, 12 meg, so both directions, so polarity doesn't really matter. So there's not like some active junction on the other side.

**Dave Jones:** That's why when you're probing stuff like this, pro tip, always change, when you measure resistance like this, just change the polarity of the probes, just to make sure that there's no active circuitry in here turning on, and it might do that if the voltage is a particular polarity.

**Dave Jones:** And this is why, back in the 1980s, not very common these days, but some multimeters had a low ohms range, which meant that it would give out less than 0.6 volts compliance voltage on the other side. So that it wouldn't actually switch on any silicon transistor junctions or anything.

**Dave Jones:** So, anyway, let's do this one over here. Ooh, 7 meg. That seems low. That seems low to me. Like, it's lower than the other one, but that seems right. I'm going to have to get a good multimeter, and I'll get back to you.

**Dave Jones:** Okay, I've got an older one here. It isn't, this is the faulty one. You'll notice that it's got a mu metal shield over the buzzer there. Just in case you get the magnet on the back of it. That's just an upgrade that they did at some point.

**Dave Jones:** Because some people, if you get, you know, the hanging magnet or whatever you get over the buzzer, you can actually influence the buzzer. So this is an older meter I just had lying over here. Didn't have a tag on it, so I don't know its condition.

**Dave Jones:** But let's measure it and see if we get lucky. Okay, let's try that again. I took the fuses out of the faulty one. 13 megs same. Okay. Well, yeah, we'll get in 30. 13, like, that, that's near enough for Australia. And 7, lower.

**Dave Jones:** So, yeah, that, yeah. That'd be within, like, the tolerance of the resistor and, like, you know, just the tolerance of whatever impedances you have in circuit there. So, yeah. I don't think it's contamination. I can rule that out by desoldering. Oh, well, let's get the faulty one back.

**Dave Jones:** And just going back to the faulty one here. I'll measure it without the fuses in. And, of course, it's open circuit. Oh. Oh, there. Oh. Oh. Hello. Ah. Look at that. 80 meg. It's going up. It's going up. Ha ha. Maybe. Yeah. 78.

**Dave Jones:** The other one was open. That's almost at the limit. It's going to go open now. 100. 100. Oh. It goes over 100 meg range. There you go. Over. So. Hmm. Is that a red herring? Am I going to be chasing a red herring?

**Dave Jones:** No. No. No. I'm going to be chasing a red herring down a rabbit hole there. I don't know. It could be a furphy. Just desolder these. Um. And, and, you know, just eliminate the jacks. So, yeah. Let me do that. A desoldering gun takes ages to warm up.

**Dave Jones:** I've been waiting like a minute and a half. Maybe I should just use the manual sucker. What do you think? Yeah. I think I need a better solder sucker. So. I got the other one out, but it didn't, didn't get this one out cleanly.

**Dave Jones:** So. So. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.

**Dave Jones:** I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that. I'm going to go ahead and do that.
