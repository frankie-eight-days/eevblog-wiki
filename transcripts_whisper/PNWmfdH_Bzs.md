---
video_id: PNWmfdH_Bzs
title: EEVblog 1384 - Halve Your Processor Power Consumption!
url: https://www.youtube.com/watch?v=PNWmfdH_Bzs
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 44, "3": 58, "4": 78, "5": 91, "6": 100, "7": 109, "8": 118, "9": 127, "10": 136, "11": 145, "12": 154, "13": 163, "14": 172, "15": 181, "16": 190, "17": 199, "18": 208, "19": 217, "20": 226, "21": 235, "22": 244, "23": 253, "24": 262, "25": 271, "26": 280, "27": 289, "28": 298, "29": 307, "30": 316, "31": 325, "32": 334, "33": 343, "34": 352, "35": 361, "36": 370, "37": 379, "38": 388, "39": 397, "40": 406, "41": 415, "42": 424, "43": 433, "44": 442, "45": 451, "46": 460, "47": 469, "48": 478, "49": 487, "50": 496, "51": 505, "52": 514, "53": 523, "54": 532, "55": 541, "56": 550, "57": 559, "58": 568, "59": 577, "60": 586, "61": 595}
---

**Dave Jones:** Hi. Just a quick video to show you a neat way that you can potentially reduce power consumption in your microcontroller products. And it has to do with the phenomenon called diffusion capacitance. And, well, we won't go into the whole physics of it because, well, yeah, it kind of is advanced semiconductor physics about how it all works.

**Dave Jones:** But you're familiar with the normal p-n junction diode, of course, has what's called junction capacitance. That's also called transition capacitance or depletion capacitance. It goes by a couple of names, but everyone just calls it basically junction capacitance. And that's where a diode has a capacitance across, effectively across its p-n junction.

**Dave Jones:** But it actually has to do with, you know, the insertion of charges and things like that acting like capacitance. And there's actually quite a little complex formula, here it is, that actually has to do with that. So, yeah, we won't go into details.

**Dave Jones:** But another aspect of semiconductors, and especially, is that a hair? Where did that come from? There's, in particular, CMOS processors like you're familiar with. Now, what I've got here is a typical, just a CMOS inverter here. And, you know, we've got our n-channel transistor and our p-channel here.

**Dave Jones:** And that simply forms an inverter. That's how CMOS gates are built. And you get multiple ones for those to create and and so on. So, we've got an inverter here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.

**Dave Jones:** We've got a p-channel here. We've got a p-channel here. We've got a p-channel here.
