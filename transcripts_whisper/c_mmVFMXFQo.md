---
video_id: c_mmVFMXFQo
title: EEVblog 1665 - Keithley VFD REPAIR 2 - Electric Boogaloo
url: https://www.youtube.com/watch?v=c_mmVFMXFQo
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 20, "3": 68, "4": 94, "5": 112, "6": 132, "7": 138, "8": 144, "9": 150, "10": 156, "11": 162, "12": 168, "13": 174, "14": 180, "15": 186, "16": 192, "17": 198, "18": 204, "19": 210, "20": 216, "21": 222, "22": 228, "23": 234, "24": 240, "25": 246, "26": 252, "27": 258, "28": 264, "29": 270, "30": 276, "31": 282, "32": 288, "33": 294, "34": 300, "35": 306, "36": 312, "37": 318, "38": 324, "39": 330, "40": 336, "41": 342, "42": 348, "43": 354, "44": 360, "45": 366, "46": 372, "47": 378, "48": 384, "49": 390, "50": 396, "51": 402, "52": 408, "53": 414, "54": 420, "55": 426, "56": 432, "57": 438, "58": 444, "59": 450, "60": 456, "61": 462, "62": 468, "63": 474, "64": 480, "65": 486, "66": 492, "67": 498, "68": 504, "69": 510, "70": 516, "71": 522, "72": 528, "73": 534, "74": 540, "75": 546, "76": 552, "77": 558, "78": 564, "79": 570, "80": 576, "81": 582, "82": 588, "83": 594, "84": 600, "85": 606, "86": 612, "87": 618, "88": 624, "89": 630, "90": 636, "91": 642, "92": 648, "93": 654, "94": 660, "95": 666, "96": 672, "97": 678, "98": 684, "99": 690, "100": 696, "101": 702, "102": 708, "103": 714, "104": 720, "105": 726, "106": 732, "107": 738, "108": 744, "109": 750, "110": 756, "111": 762, "112": 768, "113": 774, "114": 780, "115": 786, "116": 792, "117": 798, "118": 804, "119": 810, "120": 816, "121": 822, "122": 828, "123": 834, "124": 840, "125": 846, "126": 852, "127": 858, "128": 864, "129": 870, "130": 876, "131": 882, "132": 888, "133": 894, "134": 900, "135": 906, "136": 912, "137": 918, "138": 924, "139": 930, "140": 936, "141": 942, "142": 948, "143": 954, "144": 960, "145": 966, "146": 972, "147": 978, "148": 984, "149": 990, "150": 996, "151": 1002, "152": 1008, "153": 1014, "154": 1020, "155": 1026, "156": 1032, "157": 1038, "158": 1044, "159": 1050, "160": 1056, "161": 1062, "162": 1068, "163": 1074, "164": 1080, "165": 1086, "166": 1092, "167": 1098, "168": 1104, "169": 1110, "170": 1116, "171": 1122, "172": 1128, "173": 1134, "174": 1140, "175": 1146, "176": 1152, "177": 1158, "178": 1164, "179": 1170, "180": 1176, "181": 1182, "182": 1188, "183": 1194, "184": 1200, "185": 1206, "186": 1212, "187": 1218, "188": 1224, "189": 1230, "190": 1236, "191": 1242, "192": 1248, "193": 1254, "194": 1260, "195": 1266, "196": 1272, "197": 1278, "198": 1284, "199": 1290, "200": 1296, "201": 1302, "202": 1308, "203": 1314, "204": 1320, "205": 1326, "206": 1332, "207": 1338, "208": 1344, "209": 1350, "210": 1356, "211": 1362, "212": 1368, "213": 1374, "214": 1380, "215": 1386, "216": 1392, "217": 1398, "218": 1404, "219": 1410, "220": 1416, "221": 1422, "222": 1428, "223": 1434, "224": 1440, "225": 1446, "226": 1452, "227": 1458}
---

**Dave Jones:** Hi. A couple of people in the previous repair video of the Keithley 2302 with the failed vacuum fluorescent display here, they pointed out that it may actually not be the vacuum fluorescent display because there's no indicator of, like, potentially, like, losing its vacuum.

**Dave Jones:** For example, the getter down here has not, like, turned to a different color, like white. So there may not be an actual failure in the vacuum fluorescent display itself, the VFD display. Like, it may not, it may still contain its vacuum and it might still work.

**Dave Jones:** And that is certainly possible. Now, the getter down here, this is, like, basically a seal where they seal it up and it uses barium, usually, I think, in there. And it basically stops any other potential, it doesn't stop the vacuum getting out, it stops other gases getting in there and actually contaminating in the vacuum fluorescent display where you can, typical failure mode might be, like, you know, dark spots or something like that.

**Dave Jones:** I thought we'd take a look at, did anything else actually fail? Because, obviously, the vacuum fluorescent display needs a higher voltage. It doesn't just run off, you know, a 5 volt TTL type stuff. That's what this boost converter here is for. So, yeah, but basically you feed 5 volts in here and all the logic and everything else is running off 5 volts, but you need to generate a higher voltage for the vacuum fluorescent display.

**Dave Jones:** That's what this little boost converter here is actually doing. That's why they've got a 50 volt cap over on this side here. They've only got, like, a 10 volt cap. Because this is obviously on the input and I'm sure if you follow the money, I'd be willing to bet that would go over to the positive input here, which I've soldered some headers on.

**Dave Jones:** Yeah, yeah, there it is. It goes over to the 5 volt input there. So we've got a 5 volt, so we've got a 100 mic input cap there and we've got a 10 mic output cap on the boost converter here. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof. And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.

**Dave Jones:** And if the magic smoke escapes, the magic electrolyte inside there escapes, the ESR goes through the roof.
