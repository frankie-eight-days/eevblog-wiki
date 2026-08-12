---
video_id: YM5nKvIH2vw
title: EEVblog 1644 - Mailbag: CrowView Monitor, Casio Game, 4-20mA Encoder, Wurkkos Battery, Rulerize
url: https://www.youtube.com/watch?v=YM5nKvIH2vw
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 39, "3": 58, "4": 79, "5": 95, "6": 112, "7": 126, "8": 142, "9": 152, "10": 162, "11": 178, "12": 194, "13": 210, "14": 226, "15": 242, "16": 258, "17": 274, "18": 290, "19": 306, "20": 322, "21": 338, "22": 354, "23": 370, "24": 386, "25": 402, "26": 418, "27": 434, "28": 450, "29": 466, "30": 482, "31": 498, "32": 514, "33": 530, "34": 546, "35": 562, "36": 578, "37": 594, "38": 610, "39": 626, "40": 642, "41": 658, "42": 674, "43": 690, "44": 706, "45": 722, "46": 738, "47": 754, "48": 770, "49": 786, "50": 802, "51": 818, "52": 834, "53": 850, "54": 866, "55": 882, "56": 898, "57": 914, "58": 930, "59": 946, "60": 962, "61": 978, "62": 994, "63": 1010, "64": 1026, "65": 1042, "66": 1058, "67": 1074, "68": 1090, "69": 1106, "70": 1122, "71": 1138, "72": 1154, "73": 1170, "74": 1186, "75": 1202, "76": 1218, "77": 1234, "78": 1250, "79": 1266, "80": 1282, "81": 1298, "82": 1314, "83": 1330, "84": 1346, "85": 1362, "86": 1378, "87": 1394, "88": 1410, "89": 1426, "90": 1442, "91": 1458, "92": 1474, "93": 1490, "94": 1506, "95": 1522, "96": 1538, "97": 1554, "98": 1570, "99": 1586, "100": 1602, "101": 1618, "102": 1634, "103": 1650, "104": 1666, "105": 1682, "106": 1698, "107": 1714, "108": 1730, "109": 1746, "110": 1762, "111": 1778, "112": 1792, "113": 1808, "114": 1824, "115": 1840, "116": 1856, "117": 1872, "118": 1888, "119": 1904, "120": 1920, "121": 1936, "122": 1952, "123": 1968, "124": 1984, "125": 2000, "126": 2016, "127": 2032, "128": 2048, "129": 2064, "130": 2080, "131": 2096, "132": 2112, "133": 2128, "134": 2144, "135": 2160, "136": 2176, "137": 2192, "138": 2208, "139": 2224, "140": 2240, "141": 2256, "142": 2272, "143": 2288, "144": 2304, "145": 2320, "146": 2336, "147": 2352, "148": 2368, "149": 2384, "150": 2400, "151": 2416}
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, Mailbag, where companies or just individuals can send in stuff into the mailbag, we open it and take a squiz at it. So if you want to send something in, put EEVBlog Mailbag, so I know it's for the mailbag segment, not just something I've randomly ordered that I've forgotten about.

**Dave Jones:** PO Box 7949, Norwest, New South Wales 2153, Australia, not Austria. Thank you very much, unknown person. It looks like it's been, like, reshipped here locally. So, the brown wrap, of course, that indicates that's very common in China, the brown tape like this. Does anyone know why?

**Dave Jones:** Leave it in the comments down below. I think there's, somebody did a video on it once about why this is a very popular technique in China and they just, like, wrap it, like, in, like, ten layers of just masking tape. So, is that gonna, have I got it?

**Dave Jones:** Oh, what have we got? Oh, yes. Elecrow, they have had multiple sucks of the salve over the years and they've sent in something that looks really cool. Check it out, it's a big box. It's the Crowview Note, a 14-inch portable monitor with keyboard.

**Dave Jones:** Wow, there you go. So, if you've got your Raspberry Pis or whatever it is, that you have these days, then it, it, this isn't a laptop, this is just a display and a keyboard that presumably plugs in, like, USB-C and you plug it in and Bob's your uncle.

**Dave Jones:** You've got yourself a portable little, um, like, laptop-y, you know, kind of thing for your Raspberry Pi or your other little portable computer. Cool. Alright, we'll open that on the bench. So, this is a Kickstarter, apparently. It's finished now, but you can still buy it.

**Dave Jones:** They had over 1,500 back in the day. They had over 1,500 backers. Uh, it was quite successful and, and there you go, you can connect it to your shoe phone, uh, or you can connect it to a Raspberry Pi or other devices. So, 150 Yankee bucks for this.

**Dave Jones:** It's got a built-in 5,000 milliamp hour battery, IPS panel, 14-inch, uh, full HD, uh, screen, uh, so 100, it can fold completely, um, open. And it's got, uh, USPs and whatnot. So, yeah, a 14-inch thing. We've got ourselves a little user manual here.

**Dave Jones:** Yeah, it's, oh, there you go. That shows how you can hook it up to a Raspberry Pi board or you can hook it up to a Jetson Nano as well. Cool bananas. So, we've got the unit itself and we've got a couple of boards.

**Dave Jones:** So, there you go. It's very much like a, uh, laptop. We've got, uh, USB-A, USB-C over here, headphone jack, and a, uh, DC input. And over this side, which connects to these adapter boards, we've got USB-A. Uh, we've got a, um, HDMI mini-USB port.

**Dave Jones:** Uh, we've got, uh, USB-A, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-A, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, drop test.

**Dave Jones:** Let's check it out. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.

**Dave Jones:** Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port. Uh, we've got, uh, USB-C port.
