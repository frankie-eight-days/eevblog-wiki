---
video_id: AQK7RyecVW0
title: EEVblog 1397 - DC Fundamentals Part 2: DC Voltage & Current Sources (Thevenin & Norton Theorems)
url: https://www.youtube.com/watch?v=AQK7RyecVW0
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 26, "2": 51, "3": 71, "4": 81, "5": 101, "6": 115, "7": 121, "8": 127, "9": 133, "10": 139, "11": 145, "12": 151, "13": 157, "14": 163, "15": 169, "16": 175, "17": 181, "18": 187, "19": 193, "20": 199, "21": 205, "22": 211, "23": 217, "24": 223, "25": 229, "26": 235, "27": 241, "28": 247, "29": 253, "30": 259, "31": 265, "32": 271, "33": 277, "34": 283, "35": 289, "36": 295, "37": 301, "38": 307, "39": 313, "40": 319, "41": 325, "42": 331, "43": 337, "44": 343, "45": 349, "46": 355, "47": 361, "48": 367, "49": 373, "50": 379, "51": 385, "52": 391, "53": 397, "54": 403, "55": 409, "56": 415, "57": 421, "58": 427, "59": 433, "60": 439, "61": 445, "62": 451, "63": 457, "64": 463, "65": 469, "66": 475, "67": 481, "68": 487, "69": 493, "70": 499, "71": 505, "72": 511, "73": 517, "74": 523, "75": 529, "76": 535, "77": 541, "78": 547, "79": 553, "80": 559, "81": 565, "82": 571, "83": 577, "84": 583, "85": 589, "86": 595, "87": 601, "88": 607, "89": 613, "90": 619, "91": 625, "92": 631, "93": 637, "94": 643, "95": 649, "96": 655, "97": 661, "98": 667, "99": 673, "100": 679, "101": 685, "102": 691, "103": 697, "104": 703, "105": 709, "106": 715, "107": 721, "108": 727, "109": 733, "110": 739, "111": 745, "112": 751, "113": 757, "114": 763, "115": 769, "116": 775, "117": 781, "118": 787, "119": 793, "120": 799, "121": 805, "122": 811, "123": 817, "124": 823, "125": 829, "126": 835, "127": 841, "128": 847, "129": 853, "130": 859, "131": 865, "132": 871, "133": 877, "134": 883, "135": 889, "136": 895, "137": 901, "138": 907, "139": 913, "140": 919, "141": 925, "142": 931, "143": 937, "144": 943, "145": 949, "146": 955, "147": 961, "148": 967, "149": 973, "150": 979, "151": 985, "152": 991, "153": 997, "154": 1003, "155": 1009, "156": 1015, "157": 1021, "158": 1027, "159": 1033, "160": 1039, "161": 1045, "162": 1051, "163": 1057, "164": 1063, "165": 1069, "166": 1075, "167": 1081, "168": 1087, "169": 1093, "170": 1099, "171": 1105, "172": 1111, "173": 1117, "174": 1123, "175": 1129, "176": 1135, "177": 1141, "178": 1147, "179": 1153, "180": 1159, "181": 1165, "182": 1171, "183": 1177, "184": 1183, "185": 1189, "186": 1195, "187": 1201, "188": 1207, "189": 1213, "190": 1219, "191": 1225, "192": 1231, "193": 1237, "194": 1243, "195": 1249, "196": 1255, "197": 1261, "198": 1267, "199": 1273, "200": 1279, "201": 1285, "202": 1291, "203": 1297, "204": 1303, "205": 1309, "206": 1315, "207": 1321, "208": 1327, "209": 1333, "210": 1339, "211": 1345, "212": 1351, "213": 1357, "214": 1363, "215": 1369, "216": 1375, "217": 1381, "218": 1387, "219": 1393, "220": 1399, "221": 1405, "222": 1411, "223": 1417, "224": 1423}
---

**Dave Jones:** Hi, it's fundamentals time again, and it doesn't get much more fundamental than voltage and current sources, because one of the first things you learn in electronics is what is a voltage, what is current, what is resistance, and, you know, how a simple circuit works, and arguably the next thing you should probably learn about is voltage and current sources, at least in the DC realm anyway, because AC is a separate thing.

**Dave Jones:** So, we're going to talk about voltages and current sources, and it's very simple and almost very obvious, but quite important, so let's briefly cover it. You've probably heard me actually talk about this sort of stuff in countless videos, things to do with, you know, series resistance of batteries and power supplies and things like that, and how current sources have compliance voltages, and, well, it stems from the basic theory of voltage and current sources,

**Dave Jones:** and if we want to get a bit more technical, Thevenin equivalent and Norton equivalent. circuits, and even though this is incredibly simple, it has wide-ranging applications in terms of circuit theory, circuit analysis, and practical circuit and design implementation, so it's really important, so let's take a look at the voltage source first.

**Dave Jones:** When you have a voltage source, and it can be many different types, it can be many different things, it can be an electrochemistry battery, it can be a power supply circuit, for example, either a lab power supply, or you can build your own little, you know, square circuit, or you can build your own little, you know, square circuit, or you can build your own little, you know, square circuit, or you can build your own little, you know, square circuit, or you can build your own little, you know, square circuit, or you can build your own little, you know, square circuit, or you can build your own little, you know, square circuit.

**Dave Jones:** So, let's take a look at the voltage source first. It can be a power supply, or you can build your own little, you know, switch mode power supply, a linear power supply, something like that, it could be a solar cell, it could be a Peltier device, it could be a generator, but then we start getting into AC, and this is all about DC, but anyway, the triboelectric effects, and there's many different sources of voltage.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source represented here by just the voltage source, it actually must include, in practice, it must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor.

**Dave Jones:** And the takeaway from this video is that it's not just a voltage source, it actually must include a series resistor. Thank you.
