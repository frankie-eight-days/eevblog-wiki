---
video_id: jhAXPnm8BP0
title: EEVblog #1216 - PCB Layout + FPGA Deep Dive
url: https://www.youtube.com/watch?v=jhAXPnm8BP0
source: youtube-asr
timestamps: {"0": 1, "1": 12, "2": 20, "3": 31, "4": 50, "5": 72, "6": 98, "7": 112, "8": 125, "9": 141, "10": 151, "11": 162, "12": 175, "13": 190, "14": 214, "15": 223, "16": 237, "17": 252, "18": 263, "19": 276, "20": 288, "21": 301, "22": 320, "23": 331, "24": 346, "25": 363, "26": 374, "27": 387, "28": 396, "29": 416, "30": 429, "31": 439, "32": 449, "33": 467, "34": 480, "35": 493, "36": 514, "37": 528, "38": 540, "39": 555, "40": 571, "41": 584, "42": 603, "43": 614, "44": 626, "45": 640, "46": 651, "47": 666, "48": 689, "49": 700, "50": 714, "51": 723, "52": 732, "53": 748, "54": 761, "55": 779, "56": 790, "57": 802, "58": 811, "59": 828, "60": 855, "61": 874, "62": 886, "63": 902, "64": 915, "65": 926, "66": 937, "67": 951, "68": 964, "69": 979, "70": 995, "71": 1005, "72": 1017, "73": 1032, "74": 1040, "75": 1058, "76": 1069, "77": 1091, "78": 1102, "79": 1117, "80": 1123, "81": 1140, "82": 1155, "83": 1174, "84": 1188, "85": 1202, "86": 1216, "87": 1230, "88": 1243, "89": 1258, "90": 1270, "91": 1287, "92": 1306, "93": 1322, "94": 1336, "95": 1349, "96": 1361, "97": 1382, "98": 1399, "99": 1413, "100": 1424, "101": 1435, "102": 1446, "103": 1457, "104": 1469, "105": 1485, "106": 1501, "107": 1518, "108": 1529, "109": 1548, "110": 1557, "111": 1574, "112": 1585, "113": 1597, "114": 1607, "115": 1618, "116": 1639, "117": 1650, "118": 1658, "119": 1669, "120": 1692, "121": 1701, "122": 1718, "123": 1729, "124": 1752, "125": 1772, "126": 1795, "127": 1807, "128": 1818, "129": 1834, "130": 1842, "131": 1852, "132": 1863, "133": 1876, "134": 1886, "135": 1896, "136": 1922, "137": 1936, "138": 1942, "139": 1952, "140": 1964, "141": 1975, "142": 1987, "143": 2000, "144": 2008, "145": 2022, "146": 2037, "147": 2048, "148": 2062, "149": 2082, "150": 2093, "151": 2118, "152": 2130, "153": 2140, "154": 2153, "155": 2176, "156": 2187, "157": 2195, "158": 2208, "159": 2244, "160": 2254, "161": 2264, "162": 2290, "163": 2308, "164": 2322, "165": 2333, "166": 2345, "167": 2358, "168": 2366, "169": 2380, "170": 2391, "171": 2402, "172": 2415, "173": 2440, "174": 2451, "175": 2481, "176": 2490, "177": 2505, "178": 2520, "179": 2536, "180": 2552, "181": 2565, "182": 2575, "183": 2591, "184": 2603, "185": 2613, "186": 2624, "187": 2644, "188": 2655, "189": 2661, "190": 2670, "191": 2682, "192": 2693, "193": 2708, "194": 2730, "195": 2742, "196": 2759, "197": 2772, "198": 2795, "199": 2805, "200": 2825, "201": 2846, "202": 2854, "203": 2868, "204": 2880, "205": 2891, "206": 2908, "207": 2920, "208": 2943, "209": 2951, "210": 2959, "211": 2969, "212": 2978, "213": 3005, "214": 3021, "215": 3031, "216": 3046, "217": 3069, "218": 3076, "219": 3086, "220": 3099, "221": 3110, "222": 3117, "223": 3132, "224": 3149, "225": 3163, "226": 3176, "227": 3192, "228": 3205, "229": 3215, "230": 3225, "231": 3235, "232": 3243, "233": 3254, "234": 3266, "235": 3273, "236": 3283, "237": 3291, "238": 3301, "239": 3309, "240": 3321, "241": 3339, "242": 3347, "243": 3368, "244": 3390, "245": 3400, "246": 3409, "247": 3427, "248": 3435, "249": 3453, "250": 3469, "251": 3492, "252": 3502, "253": 3515, "254": 3527}
---

**Dave Jones:** Hi, in my previous video on the IBM T221 4K monitor from the year 2000, which has been very popular, highly recommend you watch it. I'll link it in down below and at the end if you haven't seen it cuz this will make a bit more sense.

**Dave Jones:** I go into quite some detail on the board which we're going to take a look at here, but I got one comment on the video which got me thinking.

**Dave Jones:** Thank you very much Toads Gebber. It's not Gerba, it's Gebber. Anyway, um so how wide do you have to make the traces to carry the same amount of current as a properly executed jumper wire?

**Dave Jones:** Whole lot of road, here's a fat jumper wire, you don't need roads. So this got me thinking, this could make an interesting video. And if you don't recall, you have to watch the video, this is the main processor board out of the IBM 221 monitor.

**Dave Jones:** It's got two huge Altera Apex FPGAs, which were state-of-the-art at the time, very expensive, multi-thousand dollar FPGAs. And this is the back of the same board, and you can see here that there's these two big jumper wires on here which basically bypass the PCB traces on the board to get lower impedance.

**Dave Jones:** So I talked about this a bit in the video, but I thought this will make an interesting deep dive into PCB plane impedances, FPGAs, margins, power supplies, all sorts of stuff because I think this might be a real interesting example how how something seemingly as simple as a couple of wires on a board actually has really deep technical meaning behind it.

**Dave Jones:** And the engineers who designed this board probably spent countless hours actually analyzing and solving this and why they actually needed to put the wires in place. So I I think we're going to go deep down the rabbit hole today.

**Dave Jones:** I haven't planned this video at all, but I can think of stuff that is yeah, buckle up Dorothy. Kansas is going bye-bye. Right, so we'll do this with two high-res photos of the board here.

**Dave Jones:** This is the top side with the FPGAs here, and then we've got the bottom side down here, which is like looking through the board. So you can see the connector here, for example, and that matches up with the connector on the top there.

**Dave Jones:** Okay, so everything's kind of like it's like when you're designing a PCB, you're looking through the board essentially. All right, let's start out. What's going on here? Here's our power input connector.

**Dave Jones:** This comes from our 130 W power brick here, and you can see that they've got a bunch of vias all in here like this, and that of course and the through holes of course go through the bottom side.

**Dave Jones:** So okay, nice low impedance connector there directly onto the board. They've got some fuse in here, and just some filters there, and lots of vias stitching in there to go down through to the bottom or inner layers.

**Dave Jones:** So all the power comes through this one connector. The power brick 16 V at 10 A. I believe it takes about 130 W, so we're talking you know, just over 8 A for the total power consumption here.

**Dave Jones:** Now we have to look at where the power goes, because the entire premise here is why did the designers choose to put these big huge thick gauge jumper wires in here, and you can see they actually designed into the PCB, cuz they've actually got this silk screen, even though when they when they manufactured this, they just hot snotted it here and ran the cables over here.

**Dave Jones:** I'm not sure why, cuz they've actually the PCB designer went to the trouble to put silk screen path right on there to show them exactly, and even put little glue markers.

**Dave Jones:** Please put some glue there, there, there. Very nice. Okay, the PCB designer was thinking about this when they were it. So, why have they run these wires? Why couldn't they use the internal traces on here?

**Dave Jones:** Now, this is I haven't looked at all any layer markers on this board, but assume it's like an eight-layer board or something like that. You You might get away with six on something like this just, but it's more likely an eight-layer board.

**Dave Jones:** So, usually you're going to have a big one of those layers will be dedicated to one big ground plane. And this is where we'll get into all sorts of tricky business and why you might want to run these wires directly over you.

**Dave Jones:** You'll notice that they're running the negative wire as well, not just the positive. So, obviously, they're trying to bypass the internal ground plane in here. Why is it so?

**Dave Jones:** So, why did they do this? Well, there's usually two reasons behind doing something like this. One is that you simply ran out of room on your PCB to put in in this case the high current traces required.

**Dave Jones:** Big thick traces in there so you can get low impedance, low voltage drop. You simply ran out of routing room on your PCB. But on an eight-layer board like this, you're really you're not going to run out of room.

**Dave Jones:** So, the next reason is DC impedance. Now, there's two issues on a PCB. One is AC impedance, one is DC impedance. When you see a huge big thick jumper wire like this, means somebody's trying to fix a DC well, resistance basically.

**Dave Jones:** You shouldn't say impedance with DC. A DC resistance problem. There's too much voltage drop on that. They're trying to lower the resistance to decrease the voltage drop at a particular current.

**Dave Jones:** Remember Ohm's law, voltage is current times resistance. So, the more current, well, in this case, let's say we've got our eight amps flowing across our board like this, then you're going to get X amount of drop over that distance based on the resistance of the traces.

**Dave Jones:** It's non-zero. Even a nice big fat ground plane is not zero resistance. But I hear you saying, "Well, Dave, in practice, a big ground plane, that's going to be good enough for anything." Well, that's not so, as we'll take a look when we go further down the rabbit hole.

**Dave Jones:** So, now we've got to look at actually where this current is going and where these wires are running and why. Okay, so let's look at our board here. As you can see, it jumps from here over to here.

**Dave Jones:** Now, on the top side, that's our big ass FPGA in there. Don't worry about the FPGA on the other side. We'll just look at this one for now. So, it's jumping from here and it's going over to here.

**Dave Jones:** That's the red wire. Basically, you can see all those little vias in there. So, that's jumping over to there and then your ground is jumping over to this side.

**Dave Jones:** So, these three caps over here are just some bulk decoupling. That's obviously powering. You can see it snaking through. So, the positive wire is coming in here and that's obviously going into this inductor here and then that's we've got a switch mode controller, of course, and then our outputs over to here.

**Dave Jones:** So, this will be one of the rails of the like the internal core voltage of the FPGA, I'd say. You know, that internal core voltage is probably going to take the majority of current in the FPGA.

**Dave Jones:** The IO is going to take less. So, this one here might be the 5 V regulator cuz I believe all this logic is 5 V. Okay, you can see that positive comes in here.

**Dave Jones:** There's an extra fuse here. This goes out to this connector which buggers off to the bottom board, which is the IO driver board. That's neither here nor there in terms of the power consumption of this thing.

**Dave Jones:** Well, that'll actually that'll be for the LCD, too, because that's where all the LCD is getting its power from, as well. So, and that'll be for the IO board and the LCD, as well, but I think most of our issue here is going to we're going to focus on the FPGA.

**Dave Jones:** So, how could you have gotten yourself in a situation where you're you have to run these wires across here? Well, one could be a placement of your board. You've got to look at that first.

**Dave Jones:** We'll go into voltage drops, you know, I've mentioned the voltage drops are the issue here, but why? Placement. Well, in this case, they physically needed this connector right here cuz it's on the back of for product, you know, usability reasons.

**Dave Jones:** The user has to be able to plug it in. This is all one big like interface on the back panel. So, it's got to be here, for example. So, you might think, well, you know, you could say that the layout person probably should have if it was me, I wouldn't have had my big switching regs all the way distant from the power connector here.

**Dave Jones:** I would have like put them here. Look at all this unused space around here. That's where I would have whacked it, but the problem is our FPGA is here and all of this routing comes on the bottom side.

**Dave Jones:** Here's our big connector here like this. So, all this high-speed routing's got to come out to go off to the LCD on the bottom here. And well, you could argue, well, this could have been up the top and stuff like that.

**Dave Jones:** And well, you know, anyway, there's layout reasons why So, the PCB designer went, well, okay, I'm forced to put my switching regulators up here. That means I've got to get a reasonably low impedance path over here.

**Dave Jones:** And if you use the ground plane inside the board going from here over to here, that's a lot of distance there. We're talking probably 20 cm there to get your 8 amps over to here.

**Dave Jones:** And you've got your big FPGA under here like this. So, any switching of your switching power supply or your load on the other side of the power supply, even the FPGA itself, is going to cause quite a few issues.

**Dave Jones:** So, did they goof this from a layout point of view? Maybe, but I'm not going to like, you know, there's lots of reasons that goes into this. This is a month's worth of layout, so yeah, let's let's just not say that they goofed here, but it's possible.

**Dave Jones:** Now, everyone thinks about when they think about PCB layouts, it's all about bypassing. And you can see all the bypass caps in here under the FPGA, right? They've done that well.

**Dave Jones:** Look, you've got your large bypass caps. a video on why you need, like they've got three different sizes. One there, like a like a 1206, 0805, and then 0603s.

**Dave Jones:** They've got all different sizes, all the different values for the different frequencies. I've done a whole video on that, it's great, I'll link it in. And I but that there are two different things you have to consider when you're laying out PCBs and designing products like this.

**Dave Jones:** One is your AC impedance, and this has to do with all your decoupling and stuff like that. Now, that's one thing, but a lot of designers will forget about DC resistance.

**Dave Jones:** And this is why they've come a gutsy here and had to add these wires in because it's not uncommon at the end of a design to lay out your board, you build it up, your first prototype, you're testing it out, and you go, "Hmm, things aren't quite working.

**Dave Jones:** Things are playing up and stuff like that." And you might find that, well, your ground paths weren't lower impedance enough. Getting it from one side to the other over here, 20 cm was just too far, and you're getting too much DC voltage drop, and that can interfere with your FPGA under here, which is why we need to go to the videotape.

**Dave Jones:** We need to go to the data sheet of the FPGA and have a look why this might be a problem, why DC can be even more important than AC decoupling.

**Dave Jones:** All right, this is a data sheet for the Apex 20K logic family and this dates from 1998, something like that. So, quite an old device, but we've got the EP20K400E here.

**Dave Jones:** So, I'll spare you the details. Let's go all the way down, all the way with LBJ and what we're looking for is voltage. And here we go, operating conditions.

**Dave Jones:** This is what we have to look at. And this is just This is not even a deep dive into FPGA data sheets. Have I done a video on that?

**Dave Jones:** Anyway, supply voltage. Here we go. So, 5-V tolerant recommended operating conditions. Our internal voltage FPGAs will have an internal core voltage as well as an IO voltage like this and sometimes they've got even more than that.

**Dave Jones:** But this is a fairly old-school FPGA. The more modern ones, they can have, four, five, or even more different voltage cores for various things. You have separate ones for PLLs and all sorts of stuff.

**Dave Jones:** We won't go into anyway. Look, here we go. Minimum 2.375 V and 2.625 V. So, you can So, one of those switch-mode converters that we looked at on the board, that's going to be a 2.5-V switching converter to provide the VCC int voltage.

**Dave Jones:** And as I said, and the other one will be VCCIO, which is your nominal 3.3 V, which of course powers every all the other 3.3-V stuff on the board as well.

**Dave Jones:** And this is a 5-V tolerant FPGA, so it will tolerate 5-V in even though it's only got a VCCIO of 3.6 V. Now, look, your 3.6-V rail here, okay?

**Dave Jones:** It's got a fairly wide margin. It's got nominal 3.3, so it's got a 300 mV. Minimum is 3 V here. It's got 300 mV margin on the low side.

**Dave Jones:** But, have a look at VCCINT here. That's only 2.375 V. That's only 125 mV less than the nominal 2.5 V core voltage. So, I've only got 125 mV to play with.

**Dave Jones:** So, that's going to include the drop not only on our power rail, but also on our ground rail because, remember, it's a big, complex system. So, not only do you need a minimum of 2.375 V at the FPGA chip itself, if you don't apply proper star grounding techniques where you just have the input connector and then you just run the grounds off separately, then the interaction between your different chips

**Dave Jones:** can cause logic threshold issues and all sorts of stuff. So, if the DC voltage drop on your power and your ground connections going to that FPGA a greater than 125 mV, wah wah wah wah, you've come a cropper, and your FPGA you're now operating outside of the recommended conditions, and all bets are off.

**Dave Jones:** So, 125 mV might sound like a lot to play with, but yeah, let's run the numbers on this. And remember, this is an old FPGA. This is not one of the newfangled ones with very low core voltages.

**Dave Jones:** If we quickly check out data sheet of one of those, we'll see we probably don't have much margin to play with. So, although it's not directly relevant to this particular almost 20-year-old design, let's look at a modern, say, Altera Stratix FPGA, for example.

**Dave Jones:** They've got data sheets just for the AC and DC electrical switching characteristics of these chips. The data sheets are phenomenal. It's not just one data sheet, it's multiple ones.

**Dave Jones:** They've got one data sheet just dedicated to getting the power right on FPGAs. This is how important it is. So, if we scroll down here, look at all the different types.

**Dave Jones:** They've got VCC, which is the core voltage, um which is also called VCC int. So, yes, they've changed that over the years. VCCPT, programmable power technology, uh for the configure just for the configuration pins.

**Dave Jones:** They've got auxiliary ones. Uh they've got battery backup power supply. They've got the IO pre-driver power supply. And they've got the IO power supply. And not done yet, the PLL digital power supply, the PLL analog power supply.

**Dave Jones:** So, how many are we up to now? 2 4 6 7 8 9 9. And then a regular VI set 9 10 different power rails. 10. 10 different power rails.

**Dave Jones:** Modern FPGAs are insane. Like I said before, it's not uncommon to get four, five, or more in this particular case with these high-end FPGAs. And but let's go down and have a look here at the requirements.

**Dave Jones:** VCC. Here is the requirements for the just the core voltage of the FPGA. Pain in the ass. Look at this. 0.9 V volts core voltage. Ridiculous. And then for the programmable stuff, 1.5.

**Dave Jones:** Then you need another 2.5. Then you need your 3.3s and 1.8s for all your different power buffers and something like and then your programming voltages, your PLLs are another 1.5 and 2.5.

**Dave Jones:** Often you can't share them cuz you need clean uh power for your PLLs, for example. You don't want to switch that in with your core voltages or your IO voltages and stuff like that.

**Dave Jones:** Anyway, the key point I want to make here is 0.9 V volts. Look at the tolerance. 30 mV. 30 mV. That's all you've a 0.87 is the minimum. If you go below that, all bets are off.

**Dave Jones:** Your FPGA may not work or may start playing up, doing weird stuff. And you don't want weird stuff in the FPGA. They're already weird enough as it is and incredibly difficult to debug.

**Dave Jones:** So, at 30 mV drop, that's nothing. You remember we had 125 mV with the 20-year-old Apex FPGAs. These ones, 30 mV, and that includes your positive and your negative rails.

**Dave Jones:** You can now see how absolutely vital it is not only to get an accurate power supply, but ensure that there's a minimum of drop on your power and your ground traces going to the FPGA.

**Dave Jones:** So, often, you will tweak. It's very common to actually tweak your supply voltage up instead of nominal 0.9. You don't want to set it to that. You might want to set it to 0.93 knowing that you're going to get some drop on your traces, and then instead of 30 mV, you've now got the difference between that and that.

**Dave Jones:** So, you've now got 60 mV drop to play with when you're laying out your PCB traces. And we'll go to a calculator soon and calculate all this stuff. But as you can see, there's not much to play with there.

**Dave Jones:** But thankfully, the Apex one is a bit more tolerant, 125 mV anyway. But let's go back to our power supply here because we're not done yet. Those 125 mV and 30 mV margins, as I said, and it's got to get over to your FPGA over to here like this.

**Dave Jones:** Not only power, but the ground as well. It's got to get through there. It's got to get through all the vias. It's got to get through the local bypassing.

**Dave Jones:** Remember, these are DC values. It's got nothing. You can have all the bypassing in the world. It's not going to help you. That's the difference between AC and DC characteristics of a complex device like this FPGA.

**Dave Jones:** These are the most complex devices available today, these FPGAs. You think your Intel your bleeding-edge Intel processors? No, they're like five times smaller in die size, five times less transistor counts in some of these high-end FPGAs today.

**Dave Jones:** These are the most complex beasts on the planet. But, it's not only DC, you've also got like low-frequency transient characteristics as well. So, let's say your voltage is like that, and then it starts suddenly starts to draw a bit of current, whoop, it might drop down like that a little bit at higher current and go back up like that.

**Dave Jones:** So, that is your dynamic characteristics of your converter. Because these switch-mode converters in here, I don't know which chip they're using, we can probably look it up, but anyway, these are going to have dynamic characteristics as well.

**Dave Jones:** The output impedance of these switching converters is something at DC and something slightly different again. Only has to be a smidgen difference, cuz remember, we're leading edge FPGA, only have 30 mV to work with.

**Dave Jones:** So, that includes not just your PCB traces, but all your switching characteristics of the output MOSFETs and switching elements inside your switching converter. So, we This is a deep rabbit hole.

**Dave Jones:** If you actually want to do this, you can spend a designer can spend weeks and weeks or a month just getting this power system right. Bloody scrolling. Anyway, so it looks like on the bottom there, there's our MOSFETs.

**Dave Jones:** You can tell they're MOSFETs cuz all the all the pins are tied together like that, and there's just the one gate pin here and here. Okay, so these these MOSFET switching here for our two converters, and then the controller, was that on the top side?

**Dave Jones:** These have internal voltage references which set those DC characteristics. So, all of the dynamic switching characteristics you could have if you don't have proper layout in your switch-mode converter like this.

**Dave Jones:** If you don't keep your tight loops, and I've done videos on this, and if you don't keep that tight, you can get extra DC error or switching or dynamic switching errors when you when your output loads.

**Dave Jones:** So, if your output switches like this, it might have, you know, two different current levels. You might be drawing, say, 5 amps up here, then it might drop down to 1 amp down here, different modes, and it might do this at sort of lowish frequency, might do it at higher frequency, and stuff like that.

**Dave Jones:** Then, if you don't get your If this is, you know, This is This is very crude, but if you don't get your star grounding like this, like this one is going off to your load, for example, and this one might be going off to, you know, some other load, or whatever, and this one goes to your chip.

**Dave Jones:** It goes to your converter, for example. If you don't If you have your large switching currents going up like this, and then you connect here your chip off to this point here, then you're going to get that voltage drop all the way along there.

**Dave Jones:** That's do very crude diagram, but you then you've got an internal reference voltage inside this thing that you've just like you're dynamically switching when your load switches, your current's going to switch.

**Dave Jones:** You might have only 5 or 10 millivolts, but that could change your output reference voltage from your 0.9 volts, it could easily change it down to 0.8, and you're screwed.

**Dave Jones:** And that's just with the layout of your like little switch mode controller chip. That doesn't include actually going off to your big ass FPGA up here, and the voltage drop on those.

**Dave Jones:** So, that that's just ground. We're Like I'm just considering ground, not considering power here. It It's just fits, and uh they the two big ass inductors that we saw there.

**Dave Jones:** And we can go down and we can find lots of various information about this that is pertinent um to this particular case. Once again, you're going to have like your your voltage references that's going to be a thing and it's going to vary over uh temperature and stuff like that.

**Dave Jones:** So, you'd have to look into uh potentially things like that. But really, what we're interested in is like dynamic uh characteristics, for example. So, let's go down circuit protection all sorts of hysteresis voltages and things like that.

**Dave Jones:** We won't worry about any of that. Typical application circuit switching frequency, of course switching frequency is going to change. It's a complex equation which changes with all sorts of things and then it can affect various things.

**Dave Jones:** And uh you can come a gutser just there alone. That'd be a whole video. Anyway, uh undervoltage, here we go. Output efficiency, system efficient load regulation, there we go.

**Dave Jones:** 3.3 V output load regulation, that's pretty tight. So, no worries there over like 5 amps. Um so, that's you know, load regulation's not a problem, but usually something that you've got to uh consider.

**Dave Jones:** That's load regulation is how uh tight, as you can see, how tight the voltage remains over the entire output current capability of this thing. 1.8 V output load regulation, that's pretty good.

**Dave Jones:** So, we're only uh yeah, 5 mV, you know, like not even. Just a couple of mV. So, you know, it's nice and tight. But look, output voltage ripple is you can come a gutser just on the output voltage ripple.

**Dave Jones:** Look at this. I mean, we're talking like 50 mV. I mean, we've only got a 125 mV margin. That's not including any of our DC drop. So, when you include the dynamic characteristics, like well, the output's not a dynamic characteristic, but it's a fixed and DC rail characteristic.

**Dave Jones:** Output voltage ripple, it it and you add that onto your uh drop due So, you add the ripple onto the drop due to to PCB traces, uh your PCB you might calculate your PCB traces just fine, and it could be hunky-dory.

**Dave Jones:** It could be within inside that 125 mV limit. And then but you add on your ripple, you forget about that. Oops. Or your product enters some other different operating mode or something like that, and and it draws that extra current, and then the ripple gets bigger and bigger, and and that can change with temperature and all sorts of like what?

**Dave Jones:** Like it's all over the place, right? This is complex. Power off sequencing, we don't care about that. Transient response. Transient response. This is what we want. Look at how much it can change.

**Dave Jones:** This is 100 mV per division, remember? We're only talking about 120 mV margin here. That's not including the DC margin, right? That's That's including everything. It doesn't care. If you transient outside that for a split second, then as your the FPGA might change modes, your product changes modes or whatever.

**Dave Jones:** It drops from a, you know, 5 amps down to 1 amp or something like that, you're going to have a transient response. You can come up That's a right there on these dynamic characteristics.

**Dave Jones:** Undershooting, overshooting. That's all that on on top of your DC characteristics. Like There's a lot involved here. But I know what you're saying, "Dave, just switch to a You know, just use huge ground and power planes, and it's going to solve all your problems.

**Dave Jones:** Don't worry about this star grounding and layout and routing and all that sort of stuff." Well, a couple of things. One is that you can often Look at all these vias in here.

**Dave Jones:** There's vias, vias, vias, vias, vias everywhere. That's chopping up your ground planes every time you do it. Yeah, you can have blind and very buried vias where if your board's like this, then your via only goes between a couple of layers.

**Dave Jones:** It doesn't go It's not drilled all the way through like this. And so if you've got your ground and power down here, they can be a nice solid ground plane, but then you got a more expensive board, and it's a trade-off and stuff like that.

**Dave Jones:** But even if you had a big gigantic ground plane in here, which is very common for these high-end FPGAs for that Stratix one we looked at with the 10 power rails.

**Dave Jones:** So, you know, in a common implementation, you might have seven or eight rails, something like that. You might dedicate not a whole ground plane to each one. You would have one or two ground planes, but then you would dedicate like a couple of your layers to power, and you'd be routing you'd be like routing your different paths for your power as well.

**Dave Jones:** Typically, you'd have them all coming back on the one ground plane. But, the problem is big ground planes aren't magic because it goes back to ta-da! Bring back a You remember this?

**Dave Jones:** If you've been watching for a long time, the resistor grid. It's What was this video five or something 10 or something? I don't know. Anyway, it was quite old.

**Dave Jones:** And you can think of your ground plane as a grid of resistors like this because that's effectively what it is. Your current it the higher for I've done a video on this.

**Dave Jones:** The higher your switching frequency, the more the current is going to remain say say you're switching for your your source and your loads here for example, then your current at high frequencies due to a spreading inductance on your board will the loop will follow the path directly under the power traces on your board.

**Dave Jones:** So, there won't be as much current flowing out here and here. But, DC in theory, it kind of will start flowing out. But, once again, you've got spreading resistance in here.

**Dave Jones:** It's not magic. Think of it as an array of resistor. It is an array of resistances like this, and this is how that you actually analyze. But, unfortunately, to analyze something like a ground plane, how much drop do I get on a ground plane, how much voltage drop for a given current, not easy to calculate.

**Dave Jones:** In fact, there's no simple calculators out there to do it. Might be a couple of rules of thumb, but they're not hugely accurate. So, you have to use what's called a finite element analysis.

**Dave Jones:** You have to You can get real expensive tools to do it, but they very complex mathematical modeling. In this particular case, modeling the drop, like if we had a big ground plane, modeling the drop right across this board over from this power connector over to here like this, and then this over to your and the or the output, sorry, uh to your FPGAs and stuff like that.

**Dave Jones:** It's really, you know, it's almost don't bother calculating something like that. So, you can do it in theory, but in practice, yeah, no. Okay? So, that's why they probably went for the wires because it it's actually a more predictable resistance we can actually get in here like this.

**Dave Jones:** So, uh just putting in a thick gauge wire, you can calculate the resistance of that. It's a really easy. And if you're running PCB traces, for example, if you're running power, the positive one, on the internal layers, if if you had a big, you know, I would make the trace like hugely wide like this, you know, a big thick trace going over there like that, you know, like 20 mm

**Dave Jones:** wide or something going right over or even depends on how much room you got. Maximize your amount of room. But anyway, you can start Once you get traces like that, you can then start to calculate the DC resistance and the resultant voltage drops.

**Dave Jones:** And another thing to overcome the voltage drops at high currents coming from the output of our switcher converter over to our FPGA over here, some switcher converters you can get a remote reference voltage.

**Dave Jones:** So, it might take a reference uh trace, like it's a four-terminal measurement, so to speak. It'll take ground and power references from under here. So, you might have a big power square under here, for example, it's quite common.

**Dave Jones:** You'll lay out like a big power square like that, for example, and all your uh so, that's how you get high-frequency bypass, but it's also just one big brick.

**Dave Jones:** But, of course, all the vias that you've got to drop through from your pain-in-the-ass BGA package on here, drop through, they all split up that plane. So, anyway, it gets complicated.

**Dave Jones:** I have I done a video on that? But, anyway, you'll have a big thing like this, and then you'll have Forgive me, it's uh vanishing. Then, you'll have one little trace, a sense trace coming off, which goes back to your power supply.

**Dave Jones:** You have, you know, sense traces, and then it actually adjusts for the voltage actually on this square, and it eliminates any of your voltage drop going across here like this.

**Dave Jones:** It compensates for it. But, as I said, there's dynamic switching characteristics as well to take into play. So, it's not necessarily that simple. And if you've only got 30 mV to play with, woof.

**Dave Jones:** Okay, so let's do some calculations. Now, I've actually uh recommended this tool before, and I'll recommend it again. It's the best thing out there, and it's free. It's the Saturn PCB design tool.

**Dave Jones:** Search for it. It's absolutely fantastic. It does uh it does everything. Differential pairs, via resistances, it even does Ohm's law, does heat sink thermal stuff, it's got pad stack calculators, crosstalk conductor uh via impedance, and uh parts per million calculators, embedded resistors on your board substrate resistors, and uh it's just it's insane.

**Dave Jones:** It's the best tool ever. All right, so we'll go to conductor properties here. And as I said, there is a DC and AC element to this. We're not interested in our AC characteristics, we're just looking at our DC voltage drop here.

**Dave Jones:** So, let's not complicate things. So, let's just set it to DC mode here. Uh well, let's have a look here. We'll have to go over to imperial, none of this micrometers rubbish.

**Dave Jones:** Oh, I'll be swapping back and forth. It's just a habit. Anyway, let's look at our base copper weight, which we've got in our PCB. Now, everyone's used to 1 oz copper.

**Dave Jones:** Now, you don't automatically get 1 oz copper on a big eight-layer board like this. you might get 1-oz copper on the outside layers. Uh but more often than not, you'll get 0.5-oz copper.

**Dave Jones:** Or you might even point get quarter-ounce copper. Um but half-ounce copper is the most common on the inside. And then you've got the plating thickness here. This is whether or not your board is plated.

**Dave Jones:** In most cases, your traces are not going to be plated. Or your internal layers, they're just bare copper. Um it's just they just etch it as bare copper, then they sandwich the extra layers on top and on top and on top.

**Dave Jones:** And even your top and bottom layers usually aren't plated. It's what's called solder mask over bare copper or SM OBC. So, if you scrape away, that's why if you scrape away the solder mask on a trace, you'll just get the raw copper.

**Dave Jones:** So, there is no plating. But if you had it tin-plated or something like that, you can add that. And you might see that the resistance down here might halve.

**Dave Jones:** Yeah, about half if you plate it, something like that. Cuz your plating might be another half ounce plating, for example. So, anyway. So, there you go. So, we'll set a bare PCB like this, assuming we've got like an internal layer.

**Dave Jones:** Half-ounce copper. Uh I'm going to go over. And an external or internal layers makes a difference. Well, it doesn't make a difference to the conductor resistance here. The conductor resistance is going to be the same, but it'll make a difference to power dissipation.

**Dave Jones:** And whether or not a plane is present here, you'll see that it only affects the power dissipation figures, which we're not really you know, we're that's not a concern.

**Dave Jones:** All we're concerned about is the DC resistance and uh the current and the voltage drop at a particular current. Because in this case, the plane, you'll see how when you enable that, it puts on a distance to plane like that, 10 mils, 10 thou between the planes.

**Dave Jones:** Because then you'll get conduction or you know, radiation from the power trace through to the power plane. And then that power plane can kind of act as a poorish heat sink, and that's why your power dissipation will be more if and further away if you drop, you'll notice our power dissipation will Can we resolve that?

**Dave Jones:** There you go. It goes down. So, you know, 100 mils like that. Anyway, that's got nothing to do with what we're doing today. It's just a side thing, but there's lots of complex stuff that goes into PCB layout.

**Dave Jones:** People are like, "I did PCB layout and designer, they just lay out some traces and you know, Bob's your uncle." No, there's a ton of stuff. If you got bleeding edge parts pulling lots of power like we do on this one, and all these different voltage rails with all these different DC, AC, dynamic, and static power uh conditions to meet very tight tolerances, you know, it's it's it's nuts.

**Dave Jones:** There's a ton of stuff involved. I could do a video on every single one of these properties in every single one of these tabs. Anyway, calm down, Dave. Let's go over here.

**Dave Jones:** Let's say you've got a 20-mm trace, you know, a big thick trace on your board, right? And the conductor length in this case, what did I say it was 20 cm?

**Dave Jones:** So, let's go 200 mm like this, and the PCB thickness doesn't matter. It makes no difference whatsoever. And our let's call it uh 10 m ohms there. Can we solve Yeah, now we've solved it.

**Dave Jones:** 10 m ohms there, and the current down here actually has to do with the temperature rise, and I've done this in a separate video. So, if you've got a that 20-mm wide trace over 200 mm at no normally 10 m ohms uh resistance there, it will that trace will rise by 10° C.

**Dave Jones:** It'll actually go up It'll heat up when you pass 7.2 amps through it. And you can see that we were like talking about 8 amps here, for example. And a 10° is a bit of rule of thumb for temperature rise.

**Dave Jones:** You really don't want any more than that. Um a lot of people set it to five. I'll often set it like half it to five. I don't want a 10° rise and stuff like that.

**Dave Jones:** Anyway, 10 m drop on that trace the 8 amps we're talking about, 80 mV drop. That's only one of them. That's just the power trace. What about the ground trace?

**Dave Jones:** Bingo, you've got 160 mV already. We're already over our Altera data sheet limit. Where was it? Hey, you remember? It was only 125 mV. So, if we take our power trace like this over to here and it was 20 mm wide, for example, nice big huge beefing power trace, we're going to get a voltage drop across there of 80 mV at 8 amps.

**Dave Jones:** There you go. And then then you've got the extra drop for the the same drop again for the ground or whatever. But in this case that's going to the switching converter.

**Dave Jones:** I probably should have drawn that the other way. Let's just say that we had our nice big square in here like this and then we had our 20 mm trace coming over.

**Dave Jones:** If it was like let's just say that's 100 mm there, then we'll get half the voltage drop on that. So, we'll get a 40 mV drop coming from the output of here over to our assume let's assume that once it's gotten under the FPGA like that, you get your one big solid thing that there's no more kind of little drops in here, for example.

**Dave Jones:** There will be. There might be, you know, 2 mV or something like that going from one side to the other. Whatever. Depends how many vias are in there like actually uh breaking up that uh that big nice big solid block you've got in there, but you might have you could easily have 40 mV drop going from there to there at 8 amps.

**Dave Jones:** Easy. And that's just the power, let alone the ground connection as well. But, you can argue that if you've got a nice big solid ground plane like this, for example, then you can kind of round it down to zero.

**Dave Jones:** You might add on 5 mV or something like that. But, you get you know, you might but there you go. Right? You remember we only had 120 mV margin.

**Dave Jones:** And remember that doesn't include any dynamic characteristics, that doesn't include any layout issues and how much uh you know, drop if the LCD up you remember we got our LCD over here as well.

**Dave Jones:** It's going to be drawing uh it's it's going to be drawing its own current, so you're going to get extra drop across there. And if And if you did have one big ground plane, yeah, sorry, you can't see the my drawing cursor.

**Dave Jones:** Oops. Anyway, if you got one nice big ground plane like this, getting extra power that has nothing to do with the FPGA across from one side to the other, that's got to share that space.

**Dave Jones:** You can get the voltage drop inside this power plane going from here over to here, and you know, that could be that could be an extra I don't know, 50 mV or something like that.

**Dave Jones:** Who knows? It depends on the load that you're getting, and that could interfere with your voltage drops inside your FPGA like this. You can come at that. That's uh Let's get rid of all that.

**Dave Jones:** That's why you would have a star ground, for example. You would separate If I was say let's say this was all the power Well, it is. This is all the power going off to our LCD panel over here.

**Dave Jones:** I would literally split my ground like that, and I would have ground going over separately, and then I'd I'd literally have a split in there like that. I'd have two separate grounds.

**Dave Jones:** They eventually join back here. So, we've actually split or it's effectively like a star ground. This is our This is our point and then, of course, then we might have, say, another ground plane going over here to the rest of this FPGA and maybe if we had some circuitry up here that then needed its own ground plane, we didn't want to interfere with the others, then we would actually split

**Dave Jones:** the ground plane like this, for example, under all the memory and the FPGA. That would have one ground plane, then this would have another one and it'd all come back to the star grounding point like this.

**Dave Jones:** So, this space in here you would leave blank. That doesn't have any ground plane in it. So, you've isolated your Oh, yeah. You've isolated your ground planes like this, so that the current flowing from here around here, ground and power to to the LCD connector over there, doesn't interfere with your FPGA or the switching in your FPGA doesn't interfere with the power going over there and vice

**Dave Jones:** versa, DC and AC characteristics as well. But remember, when you split power planes like this, you have to be incredibly careful because it can be really bad news for EMC.

**Dave Jones:** Uh so, in this particular case, look, we've got the the connector goes down here. This is the high-speed connector that goes off that's driving the LCD. So, in this particular case, the Altera um the signals are coming out of here.

**Dave Jones:** They're going through these buffers and then they're going across here. And if you've split your ground plane across here and that ground plane is used for those switching signals as the return path for those switching signals, you are screwed.

**Dave Jones:** It is one of the cardinal sins of uh PCB layout to split your ground planes and then have the signals running across them like that because then the currents have to flow all the way and then your loop is much bigger and larger loop creates greater EMC.

**Dave Jones:** I've done a whole video on that. And yeah, don't do that. So in this particular for this particular layout here, when I suggest doing the split ground plane like this, I don't mean split up the signal ground plane which takes that one up.

**Dave Jones:** I'd probably have separate ground planes, one that just handled the current for the LCD connector over here and one that and then a separate one that handled all the FPGAs and stuff like that.

**Dave Jones:** So yeah, I I just would have devoted one section on another layer for that. But in this particular case, the FPGA ground would have extended down here like this on a different layer.

**Dave Jones:** And you can have like grounds overlapping other grounds. That's fine. So then we can have the separate on another layer than the ground for the uh power and LCD connector coming over.

**Dave Jones:** So ultimately, I think the reason for the wires is is pretty obvious given the proximity and also this power connector going off to the dry driver and LCD board.

**Dave Jones:** It's cuz the driver and LCD takes their own fairly large amount of power and they didn't want that flowing right across the board like this which could screw up everything.

**Dave Jones:** They didn't want it flowing across the ground planes and they probably didn't have enough internal layers to add some extra ground planes to do that. Um sometimes you can fix this if you rip up your whole board and redo it.

**Dave Jones:** Like you might realize this at the last minute and like oh, you know, you're 2 weeks into your layout and you might realize oh damn, I forgot about you know, I forgot about the extra power coming over here cuz often the designers of the schematic like they may if they're good, they'll put notes on the schematic explaining how they want stuff done.

**Dave Jones:** But it's ultimately up to like which things are important saying, you know, look it like they'll show it as a star ground and things like that. So, the PCB layout person has to know that and and stuff like that.

**Dave Jones:** But, you can you know, your brain's not engaged. You can spend a week still in your layout and then you come and go, "It's all I couldn't be bothered redoing the whole thing.

**Dave Jones:** You've got a tight deadline or whatever." Okay, well, let's just add some wires on there. It's not a high volume product. She'll be right. But, of course, those wires aren't magic.

**Dave Jones:** They're going to have voltage drop, too. In this case, I think it's about maybe 15 AWG wire, you know, or maybe 1 and 1/2 mm, something like that. Ohms per kilometer, uh it doesn't allow you to will have to convert that.

**Dave Jones:** Let me get the confuser. Don't could have done that in my head. Divide that by 1,000. That's uh 10 mΩ per meter. So, we're looking at 2 mΩ for 20 cm.

**Dave Jones:** Uh multiply that by 8 amps. We're looking at 16 mV drop on one of those wires. That's not two of them. So, you might have to double that. Could that could be take you up to 32 mV drop just for getting your 8 amps through there like that.

**Dave Jones:** So, yeah. So, yeah, whether or not they're doing that voltage drop reasons, I think it's just like a a star routing thing. I think they're just trying to avoid all the stuff in here by just manually routing around there cuz they probably couldn't have I don't know why they couldn't have put their planes in here like I showed before, but anyway, I I wasn't there when this was laid out.

**Dave Jones:** I don't know. And I'd have to get the CAD files. You'd have to look at the actual layout on here. So, after what, 30, 40 minutes, we finally we can answer the OP's question.

**Dave Jones:** Uh what width trace do you need to be equivalent to the wire? Well, let's say it's 15 AWG wire, which is looks roughly what we've got here. 10 ohms per uh kilometer, we're talking 1 mΩ for 100 mm.

**Dave Jones:** So, that's not much, but it looks like we can do that with say 25 Oh, solve. Let let let's say just over 20 mm. So, I was I was roughly right.

**Dave Jones:** Something like that. There you go. 22 mm. And to answer the OP's question. And the thing is like this is a fairly simple board. Like as far as FPGAs go, this is you know, we've got a quite a large margin there 125 mV on our rail, which as I said you can extend it if you tweak that tweak the voltage of the converters up here.

**Dave Jones:** You put them on the high side. So, that's why often way back in the day a 5-V rail wouldn't be 5 V. They'd actually set it to 5.25 V.

**Dave Jones:** So, that all the circuitry near the connector it'd get 5.25 V, which it'd be on the upper side of your 5-V tolerance on your 5-V rail. Everything's fine, but by the time it got all the way to the other side of the board with the hundreds and hundreds and hundreds of chips on there as the old boards were, it might drop down to 4.75 and you're still right.

**Dave Jones:** You're still within the margins. But, modern devices with their 0.9 V, 0.8, even lower core voltages and if you put you know, you might have half a dozen of these large FPGAs on a big complex board, you can be talking tens of amps, 50 amps, even 100 amps.

**Dave Jones:** You can go into triple figures on the amps for a you know, a really complex board like this and it's a big deal and and that's when you might go in here and go bugger it.

**Dave Jones:** I need 2 oz copper in If you're desperate, I need 2 oz copper in at least a couple of your internal layers. You wouldn't use 2 oz copper, for example, if you had real a mix of high power stuff on your board with lots of other signal stuff.

**Dave Jones:** You wouldn't have 2 oz copper on every one of your eight layers. You'd tell the PCB manufacturer in your stack up chart you'd tell them that hey, I I I need these, you know, layers three and four.

**Dave Jones:** They They're my power rails. I want those 2 oz copper, please. Plus, 2 oz copper on your ground as well. And you might have multiple ground layers. But then your shield ground layers, for example, I don't care.

**Dave Jones:** I can use 0.25 oz copper. It's not carrying any of the current, for example. It's just like using for switching. It's, you know, it just might have lower dynamic requirements switching AC dynamic current requirements rather than the big bulky DC type stuff.

**Dave Jones:** But cuz the problem with 2 oz copper, as I mentioned in the previous video on this IBM monitor, if you got 2 oz copper on all your layers, that actually retains a lot of heat when it goes through the reflow oven.

**Dave Jones:** And then the balls on your BGA may not re- It gets, you know, much trickier. You got to hold your tongue at the right angle. You might have to call in the graybeard to operate your reflow machine to get that vapor phase setting just right so that the balls like so that you get reflow on your balls and it doesn't These boards can come out piping hot

**Dave Jones:** like a fresh pizza from an oven. And those 2 oz copper really retains a lot of heat. If you got multiple layers in there, well, it can stay hot forever.

**Dave Jones:** And that slows your cool down time cuz a lot of your There's a lot of art and science to actually setting the temperature profile. It's not just ramping up the temperature.

**Dave Jones:** People think, oh, it's just all about ramping it up like this. And then solder melts. It's also about cooling it down. You can't cool it down too slowly, either.

**Dave Jones:** Cuz then the solder can enter the plastic region and cause all sorts of dry joints and all sorts of, you know, then you get into material science. And it just never ends.

**Dave Jones:** But on a real complex board like this with thousand pin or 1,500 pin BGAs drawing, like with 2 oz copper, it's going to ruin your day. I've had boards which have used really thick 2 oz and then all of our components like tombstone, all of our resistors tomb can't stone cuz we didn't glue them down, and just the slight imbalance between the pads was enough to flip them all up, and yeah,

**Dave Jones:** it's not fun. So, have I waffled on enough? Have I explained why they put those wires in there? We can't be exactly sure, but hopefully you're still with me down this rabbit hole deep dive, and I can go further than this as well, but I I might leave it at that.

**Dave Jones:** Hopefully, I've given you a taste of what it's like to design these and lay out these high-end boards with these large current FPGA devices. There's so many things involved.

**Dave Jones:** You know, people just think about bypassing, but they often forget about that DC characteristic and the voltage drop on the traces and and how when you have big ground planes, you can't really I well, you could kind of you can sort of simulate this like on a spreadsheet.

**Dave Jones:** You can do it crudely. You can do your own poor man's finite element analysis and and try and calculate and stuff like that, but you know, generally, that's kind of why I like to separate my powers and grounds on the board not only for very good technical star grounding system reasons, but also then you can start calculating stuff like this cuz oh, I've got a block like that.

**Dave Jones:** It's going to have X amount of resistance, and then a block goes up like this. As I said, like this will actually be the shape of some of these ground planes.

**Dave Jones:** In fact, I I might pull up a board. I'll I'll show you a real board example. It's not as complex as this, but I'll I I think I've got one.

**Dave Jones:** Okay, I found an example with a Virtex-5 FPGA. It's a fairly large one. It's 1,136 pins, and as you can see, we've fanned out, you know, a good majority of those.

**Dave Jones:** There's I don't know, 50 not used or something like that. One, this is actually a 10-layer PCB. So, let's Let's a look. This is the top layer. Okay, we can actually, and if we turn on all the layers there, doesn't that look funky?

**Dave Jones:** You can just see all the various layers. Anyway, let's go back to single layer mode. It's much easier. And so, this is our top layer. Here's all our pads.

**Dave Jones:** You can see how our vias have been like we fanned out a via from each one. I've done a video on BGA fan out and stuff like that. Don't know if I used this one as an example, but you can see the different rails in here.

**Dave Jones:** We've got 1 V 2.5 V, 3 There should be 3.3 V for IO. Yes, our 3.3 V IO's on the outside. That's quite common because the IO pins are on the outside, so your VCC pins are on the VCC.

**Dave Jones:** Your VCC IO pins are on the output. And I believe yeah, we've only got the three voltage rails there. So, not that many, okay? But this required a 10 layer board to fan this out and get the power in.

**Dave Jones:** So, let's go have a look at the second layer. Second is a GP, so that's ground power. I don't I don't remember what P stands for, but that's just one big ground plane right over the whole thing.

**Dave Jones:** So, I didn't split the ground plane up. Layer three, it's just got some high-speed differential gigabit Ethernet traces going out and just some signal layers going out. There's no power happening on there, but once again, you could have used this layer as an extra one to get power into there because all this spare space in there.

**Dave Jones:** And then there's another ground layer because of the the high-speed differential pair of the 10 I don't know, was it 8 gigabits per second? I can't remember. Anyway, so we had multiple ground layers in there.

**Dave Jones:** That's why we needed the 10 layers. And then we've got one layer dedicated to the 3.3 V rail, so that's just flood fill right over. So, this was like, you know, pretty generous on this board.

**Dave Jones:** But if you want to get your cost down, we we could have. So, this one's just a signal. And here is where we start to get into our power.

**Dave Jones:** So, this one in here is not That's that that's ground fill. That's just ground fill. Nothing Nothing special there. Just decide to put some extra flood fill in there.

**Dave Jones:** And here we go. Here's where we do that block. I didn't put a block across the whole thing, but you can see that there's an internal So, there you go.

**Dave Jones:** That's our 2.5 V. So, that's coming in from the Yeah, it's coming in from the bottom here. So, yep. There we go. It's flowing in. Whoop. There you go.

**Dave Jones:** It's flowing in from over here. So, 2.5 V. So, it's a reasonably small trace. That wasn't a particularly high current uh thing, but you can just That's an example of how that you can just put the big block in there on one layers.

**Dave Jones:** But, you know, of course, like, oh, I had to get that trace out there. Bugger it. I couldn't do it on some other layer or I didn't want to.

**Dave Jones:** Whatever. But, yeah, that's an example of having the power block. And we'll see that again. Yep, we see that again. You can see the split down here. So, this one is for the 1 V.

**Dave Jones:** This is the core voltage. So, this one's going to be higher power. So, hence why Look, it's huge. You can see the split all around here like this. Yep.

**Dave Jones:** There we go. It's that big pink block like that. Huge big low impedance block like that. And that's coming from the uh I don't think we had a regulator on here.

**Dave Jones:** I think it was coming from elsewhere. Oh, no, it could have. Anyway, so, that's coming from up here. And that's hugely low impedance going right down to the FPGA core.

**Dave Jones:** So, that's a good example there of uh doing that that power block and big low impedance running into it. And as you can see, we don't really have many traces coming out on that layer.

**Dave Jones:** Just a few on the uh outer pins and stuff like that. But, of course, when you're laying out something like this, you would make sure because of that DC requirement for your FPGA that's fairly critical, you want uh to ensure that you do route that first so that you don't try and sneak it in later.

**Dave Jones:** Um, you know, you really want to take care of that right up front and then figure out how you do your signal traces later. And then the bottom, I don't think we had anything special on the bottom.

**Dave Jones:** No, that was just ground and there we go. We had various uh just the bypassing caps and stuff on the bottom. So, there you go. That's 1,136-pin Vertex 5 FPGA, but not particularly uh major high current requirements apart from that that 1-V uh rail did take a bit but not much on the 2.5 or the 3.3.

**Dave Jones:** But, every FPGA is different. And I was actually going to get a power estimator for you cuz all the FPGA companies have these power estimator programs, spreadsheets, whatever they are or tools to you put in your number of gates, your specific family you're using, your switching speeds, what peripherals you're using, what IO and all that sort of stuff you're doing and it will simulate fairly accurately, depends you

**Dave Jones:** know, garbage in, garbage out of course, but if you put enough stuff in there it'll or if you're if you're simu- or if you're finish your design and then just run the calculator on it, uh put in all all the various factors, it'll give you a very accurate estimation.

**Dave Jones:** The power consumption, I wanted to do that for the Apex FPGA, but I went to the Altera tool power estimator tool website and it has everything but the Apex series.

**Dave Jones:** So, I I don't know what happened to it. Not that. It's probably out there somewhere. Anyway. And here's actually a better example of a larger board. Once again, a big uh 600-something pin uh BGA over here, but let's have a look at the different layers.

**Dave Jones:** This won't tell you much, but if we go that's a ground. Oh, sorry. You couldn't see that. My face is a bit If you go to the power rail, you can see how they're actually split on the bottom here.

**Dave Jones:** That just, you know, shows how you can snake things around and just avoid various things. It's not the best example, but but it shows you just how you would might split up your power planes on a board to uh to avoid voltage drops on one high power section causing issues on a lower power section, stuff like that.

**Dave Jones:** So, I think we'll call it quits there. Sorry for the length of this video, but as you can see, there's a whole bunch of stuff involved in this and we're I wouldn't go I'm not going to say we're scratch the surface, but we've probably only scratched the surface of what you can deep dive into on this sort of thing.

**Dave Jones:** There's just so many different uh you know, permutations and combinations of of different scenarios that you can get on boards like this and and how hopefully you're going to appreciate what a PCB designer, what a professional PCB designer, and professional design engineers have to go through for some of these and consider for some of these complex designs that have all these, you know, high-end FPGAs and things like that.

**Dave Jones:** And this one from 2000 and this IBM one is not that complex, but they decided we need to add the wires in there for insert my perhaps multiple reasons in there.

**Dave Jones:** Perhaps at the design stage, perhaps as an afterthought. We don't know exactly, but anyway, it's really interesting. I hope you found that useful. And if you did, please don't forget to give it a thumbs up and subscribe and notify as well.

**Dave Jones:** Hit that little bell icon wherever the hell it is. And to make sure you get notifications if YouTube will be gracious enough to send notifications to everyone when I release a new video.

**Dave Jones:** Anyway, I hope you enjoyed it. Discuss down below. Catch you next time.
