---
video_id: jhAXPnm8BP0
title: EEVblog #1216 - PCB Layout + FPGA Deep Dive
url: https://www.youtube.com/watch?v=jhAXPnm8BP0
source: youtube-asr
timestamps: {"0": 1, "1": 12, "2": 22, "3": 37, "4": 53, "5": 72, "6": 89, "7": 107, "8": 121, "9": 134, "10": 148, "11": 160, "12": 175, "13": 190, "14": 205, "15": 217, "16": 233, "17": 247, "18": 260, "19": 276, "20": 291, "21": 304, "22": 322, "23": 338, "24": 352, "25": 365, "26": 378, "27": 389, "28": 405, "29": 418, "30": 431, "31": 443, "32": 455, "33": 470, "34": 484, "35": 497, "36": 512, "37": 526, "38": 540, "39": 558, "40": 576, "41": 592, "42": 608, "43": 622, "44": 635, "45": 651, "46": 665, "47": 678, "48": 695, "49": 714, "50": 727, "51": 744, "52": 759, "53": 777, "54": 792, "55": 811, "56": 830, "57": 847, "58": 863, "59": 879, "60": 892, "61": 912, "62": 924, "63": 937, "64": 953, "65": 972, "66": 990, "67": 1008, "68": 1021, "69": 1037, "70": 1055, "71": 1072, "72": 1084, "73": 1098, "74": 1111, "75": 1122, "76": 1135, "77": 1155, "78": 1170, "79": 1185, "80": 1202, "81": 1220, "82": 1235, "83": 1250, "84": 1267, "85": 1282, "86": 1294, "87": 1308, "88": 1325, "89": 1343, "90": 1361, "91": 1386, "92": 1401, "93": 1417, "94": 1428, "95": 1444, "96": 1457, "97": 1469, "98": 1483, "99": 1499, "100": 1511, "101": 1522, "102": 1538, "103": 1552, "104": 1567, "105": 1580, "106": 1592, "107": 1604, "108": 1618, "109": 1631, "110": 1645, "111": 1658, "112": 1672, "113": 1690, "114": 1703, "115": 1716, "116": 1729, "117": 1743, "118": 1756, "119": 1772, "120": 1786, "121": 1796, "122": 1809, "123": 1826, "124": 1838, "125": 1849, "126": 1861, "127": 1876, "128": 1889, "129": 1905, "130": 1924, "131": 1938, "132": 1949, "133": 1962, "134": 1977, "135": 1989, "136": 2002, "137": 2015, "138": 2031, "139": 2042, "140": 2057, "141": 2071, "142": 2085, "143": 2098, "144": 2111, "145": 2128, "146": 2143, "147": 2158, "148": 2176, "149": 2187, "150": 2199, "151": 2220, "152": 2239, "153": 2255, "154": 2270, "155": 2287, "156": 2301, "157": 2315, "158": 2330, "159": 2345, "160": 2358, "161": 2371, "162": 2383, "163": 2399, "164": 2411, "165": 2427, "166": 2440, "167": 2454, "168": 2474, "169": 2488, "170": 2503, "171": 2516, "172": 2531, "173": 2544, "174": 2560, "175": 2575, "176": 2591, "177": 2608, "178": 2623, "179": 2634, "180": 2647, "181": 2658, "182": 2668, "183": 2680, "184": 2696, "185": 2708, "186": 2721, "187": 2733, "188": 2748, "189": 2770, "190": 2784, "191": 2797, "192": 2812, "193": 2823, "194": 2840, "195": 2852, "196": 2863, "197": 2877, "198": 2890, "199": 2906, "200": 2920, "201": 2931, "202": 2944, "203": 2958, "204": 2971, "205": 2983, "206": 2998, "207": 3010, "208": 3025, "209": 3041, "210": 3054, "211": 3069, "212": 3079, "213": 3090, "214": 3105, "215": 3117, "216": 3130, "217": 3146, "218": 3161, "219": 3173, "220": 3188, "221": 3201, "222": 3215, "223": 3228, "224": 3241, "225": 3255, "226": 3268, "227": 3279, "228": 3291, "229": 3304, "230": 3317, "231": 3329, "232": 3342, "233": 3353, "234": 3370, "235": 3384, "236": 3395, "237": 3408, "238": 3421, "239": 3434, "240": 3445, "241": 3458, "242": 3469, "243": 3482, "244": 3497, "245": 3511, "246": 3523}
---

**Dave Jones:** Hi, in my previous video on the IBM T221 4K monitor from the year 2000, which has been very popular, highly recommend you watch it. I'll link it in down below and at the end if you haven't seen it cuz

**Dave Jones:** this will make a bit more sense. I go into quite some detail on the board which we're going to take a look at here, but I got one comment on the video which got me thinking. Thank you very

**Dave Jones:** much Toads Gebber. It's not Gerba, it's Gebber. Anyway, um so how wide do you have to make the traces to carry the same amount of current as a properly executed jumper wire? Whole lot of road, here's a fat jumper wire, you don't need

**Dave Jones:** roads. So this got me thinking, this could make an interesting video. And if you don't recall, you have to watch the video, this is the main processor board out of the IBM 221 monitor. It's got two huge Altera Apex

**Dave Jones:** FPGAs, which were state-of-the-art at the time, very expensive, multi-thousand dollar FPGAs. And this is the back of the same board, and you can see here that there's these two big jumper wires on here which basically bypass the PCB traces on the board to get lower

**Dave Jones:** impedance. So I talked about this a bit in the video, but I thought this will make an interesting deep dive into PCB plane impedances, FPGAs, margins, power supplies, all sorts of stuff because I think this might be a real interesting

**Dave Jones:** example how how something seemingly as simple as a couple of wires on a board actually has really deep technical meaning behind it. And the engineers who designed this board probably spent countless hours actually analyzing and solving this and why they actually

**Dave Jones:** needed to put the wires in place. So I I think we're going to go deep down the rabbit hole today. I haven't planned this video at all, but I can think of stuff that is yeah, buckle up Dorothy.

**Dave Jones:** Kansas is going bye-bye. Right, so we'll do this with two high-res photos of the board here. This is the top side with the FPGAs here, and then we've got the bottom side down here, which is like looking through the

**Dave Jones:** board. So you can see the connector here, for example, and that matches up with the connector on the top there. Okay, so everything's kind of like it's like when you're designing a PCB, you're looking through the board essentially.

**Dave Jones:** All right, let's start out. What's going on here? Here's our power input connector. This comes from our 130 W power brick here, and you can see that they've got a bunch of vias all in here like this, and that of course and the

**Dave Jones:** through holes of course go through the bottom side. So okay, nice low impedance connector there directly onto the board. They've got some fuse in here, and just some filters there, and lots of vias stitching in there to go down through to

**Dave Jones:** the bottom or inner layers. So all the power comes through this one connector. The power brick 16 V at 10 A. I believe it takes about 130 W, so we're talking you know, just over 8 A for the total power consumption here.

**Dave Jones:** Now we have to look at where the power goes, because the entire premise here is why did the designers choose to put these big huge thick gauge jumper wires in here, and you can see they actually designed into

**Dave Jones:** the PCB, cuz they've actually got this silk screen, even though when they when they manufactured this, they just hot snotted it here and ran the cables over here. I'm not sure why, cuz they've actually the PCB designer went to the

**Dave Jones:** trouble to put silk screen path right on there to show them exactly, and even put little glue markers. Please put some glue there, there, there. Very nice. Okay, the PCB designer was thinking about this when they were it.

**Dave Jones:** So, why have they run these wires? Why couldn't they use the internal traces on here? Now, this is I haven't looked at all any layer markers on this board, but assume it's like an eight-layer board or something like that. You You might get away with

**Dave Jones:** six on something like this just, but it's more likely an eight-layer board. So, usually you're going to have a big one of those layers will be dedicated to one big ground plane. And this is where we'll get into all sorts of tricky

**Dave Jones:** business and why you might want to run these wires directly over you. You'll notice that they're running the negative wire as well, not just the positive. So, obviously, they're trying to bypass the internal ground plane in here. Why is it

**Dave Jones:** so? So, why did they do this? Well, there's usually two reasons behind doing something like this. One is that you simply ran out of room on your PCB to put in in this case the high current traces required. Big thick traces in

**Dave Jones:** there so you can get low impedance, low voltage drop. You simply ran out of routing room on your PCB. But on an eight-layer board like this, you're really you're not going to run out of room. So, the next reason is DC

**Dave Jones:** impedance. Now, there's two issues on a PCB. One is AC impedance, one is DC impedance. When you see a huge big thick jumper wire like this, means somebody's trying to fix a DC well, resistance basically. You shouldn't say impedance

**Dave Jones:** with DC. A DC resistance problem. There's too much voltage drop on that. They're trying to lower the resistance to decrease the voltage drop at a particular current. Remember Ohm's law, voltage is current times resistance. So, the more current, well, in this case,

**Dave Jones:** let's say we've got our eight amps flowing across our board like this, then you're going to get X amount of drop over that distance based on the resistance of the traces. It's non-zero. Even a nice big fat ground plane is not

**Dave Jones:** zero resistance. But I hear you saying, "Well, Dave, in practice, a big ground plane, that's going to be good enough for anything." Well, that's not so, as we'll take a look when we go further down the rabbit hole. So, now we've got

**Dave Jones:** to look at actually where this current is going and where these wires are running and why. Okay, so let's look at our board here. As you can see, it jumps from here over to here. Now, on the top

**Dave Jones:** side, that's our big ass FPGA in there. Don't worry about the FPGA on the other side. We'll just look at this one for now. So, it's jumping from here and it's going over to here. That's the red wire.

**Dave Jones:** Basically, you can see all those little vias in there. So, that's jumping over to there and then your ground is jumping over to this side. So, these three caps over here are just some bulk decoupling. That's obviously powering. You can see

**Dave Jones:** it snaking through. So, the positive wire is coming in here and that's obviously going into this inductor here and then that's we've got a switch mode controller, of course, and then our outputs over to here. So, this will be

**Dave Jones:** one of the rails of the like the internal core voltage of the FPGA, I'd say. You know, that internal core voltage is probably going to take the majority of current in the FPGA. The IO is going to take

**Dave Jones:** less. So, this one here might be the 5 V regulator cuz I believe all this logic is 5 V. Okay, you can see that positive comes in here. There's an extra fuse here. This goes out to this connector

**Dave Jones:** which buggers off to the bottom board, which is the IO driver board. That's neither here nor there in terms of the power consumption of this thing. Well, that'll actually that'll be for the LCD, too, because that's where all the LCD is

**Dave Jones:** getting its power from, as well. So, and that'll be for the IO board and the LCD, as well, but I think most of our issue here is going to we're going to focus on the FPGA. So, how could you have gotten

**Dave Jones:** yourself in a situation where you're you have to run these wires across here? Well, one could be a placement of your board. You've got to look at that first. We'll go into voltage drops, you know, I've mentioned the voltage

**Dave Jones:** drops are the issue here, but why? Placement. Well, in this case, they physically needed this connector right here cuz it's on the back of for product, you know, usability reasons. The user has to be able to plug it in. This is

**Dave Jones:** all one big like interface on the back panel. So, it's got to be here, for example. So, you might think, well, you know, you could say that the layout person probably should have if it was me, I wouldn't have had my big switching

**Dave Jones:** regs all the way distant from the power connector here. I would have like put them here. Look at all this unused space around here. That's where I would have whacked it, but the problem is our FPGA is here and

**Dave Jones:** all of this routing comes on the bottom side. Here's our big connector here like this. So, all this high-speed routing's got to come out to go off to the LCD on the bottom here. And well, you could argue, well, this could have been up the

**Dave Jones:** top and stuff like that. And well, you know, anyway, there's layout reasons why So, the PCB designer went, well, okay, I'm forced to put my switching regulators up here. That means I've got to get a reasonably low impedance path over here. And if you use

**Dave Jones:** the ground plane inside the board going from here over to here, that's a lot of distance there. We're talking probably 20 cm there to get your 8 amps over to here. And you've got your big FPGA under here like this. So, any

**Dave Jones:** switching of your switching power supply or your load on the other side of the power supply, even the FPGA itself, is going to cause quite a few issues. So, did they goof this from a layout point of view? Maybe, but I'm not going to

**Dave Jones:** like, you know, there's lots of reasons that goes into this. This is a month's worth of layout, so yeah, let's let's just not say that they goofed here, but it's possible. Now, everyone thinks about when they think about PCB layouts, it's

**Dave Jones:** all about bypassing. And you can see all the bypass caps in here under the FPGA, right? They've done that well. Look, you've got your large bypass caps. a video on why you need, like they've got three different sizes. One there, like a

**Dave Jones:** like a 1206, 0805, and then 0603s. They've got all different sizes, all the different values for the different frequencies. I've done a whole video on that, it's great, I'll link it in. And I but that there are two different things

**Dave Jones:** you have to consider when you're laying out PCBs and designing products like this. One is your AC impedance, and this has to do with all your decoupling and stuff like that. Now, that's one thing, but a lot of designers will forget about

**Dave Jones:** DC resistance. And this is why they've come a gutsy here and had to add these wires in because it's not uncommon at the end of a design to lay out your board, you build it up, your first prototype, you're testing it out, and

**Dave Jones:** you go, "Hmm, things aren't quite working. Things are playing up and stuff like that." And you might find that, well, your ground paths weren't lower impedance enough. Getting it from one side to the other over here, 20 cm was

**Dave Jones:** just too far, and you're getting too much DC voltage drop, and that can interfere with your FPGA under here, which is why we need to go to the videotape. We need to go to the data sheet of the FPGA and have a look why this

**Dave Jones:** might be a problem, why DC can be even more important than AC decoupling. All right, this is a data sheet for the Apex 20K logic family and this dates from 1998, something like that. So, quite an old device, but we've got the EP20K400E

**Dave Jones:** here. So, I'll spare you the details. Let's go all the way down, all the way with LBJ and what we're looking for is voltage. And here we go, operating conditions. This is what we have to look at. And this is

**Dave Jones:** just This is not even a deep dive into FPGA data sheets. Have I done a video on that? Anyway, supply voltage. Here we go. So, 5-V tolerant recommended operating conditions. Our internal voltage FPGAs will have an internal core

**Dave Jones:** voltage as well as an IO voltage like this and sometimes they've got even more than that. But this is a fairly old-school FPGA. The more modern ones, they can have, four, five, or even more different voltage cores for various things. You

**Dave Jones:** have separate ones for PLLs and all sorts of stuff. We won't go into anyway. Look, here we go. Minimum 2.375 V and 2.625 V. So, you can So, one of those switch-mode converters that we looked at on the board, that's going to be a 2.5-V

**Dave Jones:** switching converter to provide the VCC int voltage. And as I said, and the other one will be VCCIO, which is your nominal 3.3 V, which of course powers every all the other 3.3-V stuff on the board as well. And this is a 5-V

**Dave Jones:** tolerant FPGA, so it will tolerate 5-V in even though it's only got a VCCIO of 3.6 V. Now, look, your 3.6-V rail here, okay? It's got a fairly wide margin. It's got nominal 3.3, so it's got a 300 mV. Minimum is 3 V here. It's

**Dave Jones:** got 300 mV margin on the low side. But, have a look at VCCINT here. That's only 2.375 V. That's only 125 mV less than the nominal 2.5 V core voltage. So, I've only got 125 mV to play with. So, that's going to include

**Dave Jones:** the drop not only on our power rail, but also on our ground rail because, remember, it's a big, complex system. So, not only do you need a minimum of 2.375 V at the FPGA chip itself, if you don't apply proper star grounding

**Dave Jones:** techniques where you just have the input connector and then you just run the grounds off separately, then the interaction between your different chips can cause logic threshold issues and all sorts of stuff. So, if the DC voltage drop on your power and your ground

**Dave Jones:** connections going to that FPGA a greater than 125 mV, wah wah wah wah, you've come a cropper, and your FPGA you're now operating outside of the recommended conditions, and all bets are off. So, 125 mV might sound like a lot to play

**Dave Jones:** with, but yeah, let's run the numbers on this. And remember, this is an old FPGA. This is not one of the newfangled ones with very low core voltages. If we quickly check out data sheet of one of those, we'll see we probably don't have

**Dave Jones:** much margin to play with. So, although it's not directly relevant to this particular almost 20-year-old design, let's look at a modern, say, Altera Stratix FPGA, for example. They've got data sheets just for the AC and DC electrical switching characteristics of

**Dave Jones:** these chips. The data sheets are phenomenal. It's not just one data sheet, it's multiple ones. They've got one data sheet just dedicated to getting the power right on FPGAs. This is how important it is. So, if we scroll down

**Dave Jones:** here, look at all the different types. They've got VCC, which is the core voltage, um which is also called VCC int. So, yes, they've changed that over the years. VCCPT, programmable power technology, uh for the configure just for the configuration

**Dave Jones:** pins. They've got auxiliary ones. Uh they've got battery backup power supply. They've got the IO pre-driver power supply. And they've got the IO power supply. And not done yet, the PLL digital power supply, the PLL analog power supply. So, how many are we up to

**Dave Jones:** now? 2 4 6 7 8 9 9. And then a regular VI set 9 10 different power rails. 10. 10 different power rails. Modern FPGAs are insane. Like I said before, it's not uncommon to get four, five, or more in

**Dave Jones:** this particular case with these high-end FPGAs. And but let's go down and have a look here at the requirements. VCC. Here is the requirements for the just the core voltage of the FPGA. Pain in the ass. Look at this. 0.9

**Dave Jones:** V volts core voltage. Ridiculous. And then for the programmable stuff, 1.5. Then you need another 2.5. Then you need your 3.3s and 1.8s for all your different power buffers and something like and then your programming voltages, your PLLs are another 1.5 and 2.5. Often

**Dave Jones:** you can't share them cuz you need clean uh power for your PLLs, for example. You don't want to switch that in with your core voltages or your IO voltages and stuff like that. Anyway, the key point I want to make here

**Dave Jones:** is 0.9 V volts. Look at the tolerance. 30 mV. 30 mV. That's all you've a 0.87 is the minimum. If you go below that, all bets are off. Your FPGA may not work or may start playing up, doing weird stuff. And

**Dave Jones:** you don't want weird stuff in the FPGA. They're already weird enough as it is and incredibly difficult to debug. So, at 30 mV drop, that's nothing. You remember we had 125 mV with the 20-year-old Apex FPGAs. These ones, 30 mV, and that

**Dave Jones:** includes your positive and your negative rails. You can now see how absolutely vital it is not only to get an accurate power supply, but ensure that there's a minimum of drop on your power and your ground traces going to the FPGA. So,

**Dave Jones:** often, you will tweak. It's very common to actually tweak your supply voltage up instead of nominal 0.9. You don't want to set it to that. You might want to set it to 0.93 knowing that you're going to get some

**Dave Jones:** drop on your traces, and then instead of 30 mV, you've now got the difference between that and that. So, you've now got 60 mV drop to play with when you're laying out your PCB traces. And we'll go to a calculator

**Dave Jones:** soon and calculate all this stuff. But as you can see, there's not much to play with there. But thankfully, the Apex one is a bit more tolerant, 125 mV anyway. But let's go back to our power supply here because we're not done yet. Those

**Dave Jones:** 125 mV and 30 mV margins, as I said, and it's got to get over to your FPGA over to here like this. Not only power, but the ground as well. It's got to get through there. It's got to get through

**Dave Jones:** all the vias. It's got to get through the local bypassing. Remember, these are DC values. It's got nothing. You can have all the bypassing in the world. It's not going to help you. That's the difference between AC and DC

**Dave Jones:** characteristics of a complex device like this FPGA. These are the most complex devices available today, these FPGAs. You think your Intel your bleeding-edge Intel processors? No, they're like five times smaller in die size, five times less transistor counts in some of these

**Dave Jones:** high-end FPGAs today. These are the most complex beasts on the planet. But, it's not only DC, you've also got like low-frequency transient characteristics as well. So, let's say your voltage is like that, and then it starts suddenly starts to draw a bit of current, whoop,

**Dave Jones:** it might drop down like that a little bit at higher current and go back up like that. So, that is your dynamic characteristics of your converter. Because these switch-mode converters in here, I don't know which chip they're using, we can probably look it up, but

**Dave Jones:** anyway, these are going to have dynamic characteristics as well. The output impedance of these switching converters is something at DC and something slightly different again. Only has to be a smidgen difference, cuz remember, we're leading edge FPGA, only have 30 mV

**Dave Jones:** to work with. So, that includes not just your PCB traces, but all your switching characteristics of the output MOSFETs and switching elements inside your switching converter. So, we This is a deep rabbit hole. If you actually want to do this, you can spend

**Dave Jones:** a designer can spend weeks and weeks or a month just getting this power system right. Bloody scrolling. Anyway, so it looks like on the bottom there, there's our MOSFETs. You can tell they're MOSFETs cuz all the all the pins are tied together like

**Dave Jones:** that, and there's just the one gate pin here and here. Okay, so these these MOSFET switching here for our two converters, and then the controller, was that on the top side? These have internal voltage references which set those DC characteristics. So, all of the

**Dave Jones:** dynamic switching characteristics you could have if you don't have proper layout in your switch-mode converter like this. If you don't keep your tight loops, and I've done videos on this, and if you don't keep that tight, you can get extra DC error or switching or

**Dave Jones:** dynamic switching errors when you when your output loads. So, if your output switches like this, it might have, you know, two different current levels. You might be drawing, say, 5 amps up here, then it might drop down to 1 amp down

**Dave Jones:** here, different modes, and it might do this at sort of lowish frequency, might do it at higher frequency, and stuff like that. Then, if you don't get your If this is, you know, This is This is very crude, but if you

**Dave Jones:** don't get your star grounding like this, like this one is going off to your load, for example, and this one might be going off to, you know, some other load, or whatever, and this one goes to your chip. It goes to your converter, for

**Dave Jones:** example. If you don't If you have your large switching currents going up like this, and then you connect here your chip off to this point here, then you're going to get that voltage drop all the way along there. That's do very crude

**Dave Jones:** diagram, but you then you've got an internal reference voltage inside this thing that you've just like you're dynamically switching when your load switches, your current's going to switch. You might have only 5 or 10 millivolts, but that could change your output reference

**Dave Jones:** voltage from your 0.9 volts, it could easily change it down to 0.8, and you're screwed. And that's just with the layout of your like little switch mode controller chip. That doesn't include actually going off to your big ass FPGA up here, and the voltage drop

**Dave Jones:** on those. So, that that's just ground. We're Like I'm just considering ground, not considering power here. It It's just fits, and uh they the two big ass inductors that we saw there. And we can go down and we can find lots of various

**Dave Jones:** information about this that is pertinent um to this particular case. Once again, you're going to have like your your voltage references that's going to be a thing and it's going to vary over uh temperature and stuff like that. So, you'd have to look into uh

**Dave Jones:** potentially things like that. But really, what we're interested in is like dynamic uh characteristics, for example. So, let's go down circuit protection all sorts of hysteresis voltages and things like that. We won't worry about any of that. Typical application circuit

**Dave Jones:** switching frequency, of course switching frequency is going to change. It's a complex equation which changes with all sorts of things and then it can affect various things. And uh you can come a gutser just there alone. That'd be a

**Dave Jones:** whole video. Anyway, uh undervoltage, here we go. Output efficiency, system efficient load regulation, there we go. 3.3 V output load regulation, that's pretty tight. So, no worries there over like 5 amps. Um so, that's you know, load regulation's not a problem, but

**Dave Jones:** usually something that you've got to uh consider. That's load regulation is how uh tight, as you can see, how tight the voltage remains over the entire output current capability of this thing. 1.8 V output load regulation, that's pretty

**Dave Jones:** good. So, we're only uh yeah, 5 mV, you know, like not even. Just a couple of mV. So, you know, it's nice and tight. But look, output voltage ripple is you can come a gutser just on the output

**Dave Jones:** voltage ripple. Look at this. I mean, we're talking like 50 mV. I mean, we've only got a 125 mV margin. That's not including any of our DC drop. So, when you include the dynamic characteristics, like well, the output's not a dynamic

**Dave Jones:** characteristic, but it's a fixed and DC rail characteristic. Output voltage ripple, it it and you add that onto your uh drop due So, you add the ripple onto the drop due to to PCB traces, uh your PCB you might calculate your PCB traces

**Dave Jones:** just fine, and it could be hunky-dory. It could be within inside that 125 mV limit. And then but you add on your ripple, you forget about that. Oops. Or your product enters some other different operating mode or something like that,

**Dave Jones:** and and it draws that extra current, and then the ripple gets bigger and bigger, and and that can change with temperature and all sorts of like what? Like it's all over the place, right? This is complex. Power off

**Dave Jones:** sequencing, we don't care about that. Transient response. Transient response. This is what we want. Look at how much it can change. This is 100 mV per division, remember? We're only talking about 120 mV margin here. That's not including the DC margin,

**Dave Jones:** right? That's That's including everything. It doesn't care. If you transient outside that for a split second, then as your the FPGA might change modes, your product changes modes or whatever. It drops from a, you know, 5 amps down to 1 amp or something like

**Dave Jones:** that, you're going to have a transient response. You can come up That's a right there on these dynamic characteristics. Undershooting, overshooting. That's all that on on top of your DC characteristics. Like There's a lot involved here. But I know

**Dave Jones:** what you're saying, "Dave, just switch to a You know, just use huge ground and power planes, and it's going to solve all your problems. Don't worry about this star grounding and layout and routing and all that sort of stuff." Well,

**Dave Jones:** a couple of things. One is that you can often Look at all these vias in here. There's vias, vias, vias, vias, vias everywhere. That's chopping up your ground planes every time you do it. Yeah, you can have blind and very buried

**Dave Jones:** vias where if your board's like this, then your via only goes between a couple of layers. It doesn't go It's not drilled all the way through like this. And so if you've got your ground and power down here, they can be a nice

**Dave Jones:** solid ground plane, but then you got a more expensive board, and it's a trade-off and stuff like that. But even if you had a big gigantic ground plane in here, which is very common for these high-end FPGAs for that Stratix one we

**Dave Jones:** looked at with the 10 power rails. So, you know, in a common implementation, you might have seven or eight rails, something like that. You might dedicate not a whole ground plane to each one. You would have one or two ground planes,

**Dave Jones:** but then you would dedicate like a couple of your layers to power, and you'd be routing you'd be like routing your different paths for your power as well. Typically, you'd have them all coming back on the one ground plane. But, the problem is

**Dave Jones:** big ground planes aren't magic because it goes back to ta-da! Bring back a You remember this? If you've been watching for a long time, the resistor grid. It's What was this video five or something 10 or something? I don't know.

**Dave Jones:** Anyway, it was quite old. And you can think of your ground plane as a grid of resistors like this because that's effectively what it is. Your current it the higher for I've done a video on this. The higher your

**Dave Jones:** switching frequency, the more the current is going to remain say say you're switching for your your source and your loads here for example, then your current at high frequencies due to a spreading inductance on your board will the loop will follow the path directly

**Dave Jones:** under the power traces on your board. So, there won't be as much current flowing out here and here. But, DC in theory, it kind of will start flowing out. But, once again, you've got spreading resistance in here. It's not

**Dave Jones:** magic. Think of it as an array of resistor. It is an array of resistances like this, and this is how that you actually analyze. But, unfortunately, to analyze something like a ground plane, how much drop do I get on a ground

**Dave Jones:** plane, how much voltage drop for a given current, not easy to calculate. In fact, there's no simple calculators out there to do it. Might be a couple of rules of thumb, but they're not hugely accurate. So, you have to use what's called a

**Dave Jones:** finite element analysis. You have to You can get real expensive tools to do it, but they very complex mathematical modeling. In this particular case, modeling the drop, like if we had a big ground plane, modeling the drop right

**Dave Jones:** across this board over from this power connector over to here like this, and then this over to your and the or the output, sorry, uh to your FPGAs and stuff like that. It's really, you know, it's almost don't

**Dave Jones:** bother calculating something like that. So, you can do it in theory, but in practice, yeah, no. Okay? So, that's why they probably went for the wires because it it's actually a more predictable resistance we can actually get in here

**Dave Jones:** like this. So, uh just putting in a thick gauge wire, you can calculate the resistance of that. It's a really easy. And if you're running PCB traces, for example, if you're running power, the positive one, on the internal layers, if

**Dave Jones:** if you had a big, you know, I would make the trace like hugely wide like this, you know, a big thick trace going over there like that, you know, like 20 mm wide or something going right over or

**Dave Jones:** even depends on how much room you got. Maximize your amount of room. But anyway, you can start Once you get traces like that, you can then start to calculate the DC resistance and the resultant voltage drops. And another

**Dave Jones:** thing to overcome the voltage drops at high currents coming from the output of our switcher converter over to our FPGA over here, some switcher converters you can get a remote reference voltage. So, it might take a reference uh trace, like it's a four-terminal

**Dave Jones:** measurement, so to speak. It'll take ground and power references from under here. So, you might have a big power square under here, for example, it's quite common. You'll lay out like a big power square like that, for example, and

**Dave Jones:** all your uh so, that's how you get high-frequency bypass, but it's also just one big brick. But, of course, all the vias that you've got to drop through from your pain-in-the-ass BGA package on here, drop through, they all split up

**Dave Jones:** that plane. So, anyway, it gets complicated. I have I done a video on that? But, anyway, you'll have a big thing like this, and then you'll have Forgive me, it's uh vanishing. Then, you'll have one little trace, a sense

**Dave Jones:** trace coming off, which goes back to your power supply. You have, you know, sense traces, and then it actually adjusts for the voltage actually on this square, and it eliminates any of your voltage drop going across here like

**Dave Jones:** this. It compensates for it. But, as I said, there's dynamic switching characteristics as well to take into play. So, it's not necessarily that simple. And if you've only got 30 mV to play with, woof. Okay, so let's do some

**Dave Jones:** calculations. Now, I've actually uh recommended this tool before, and I'll recommend it again. It's the best thing out there, and it's free. It's the Saturn PCB design tool. Search for it. It's absolutely fantastic. It does uh it does everything. Differential pairs, via

**Dave Jones:** resistances, it even does Ohm's law, does heat sink thermal stuff, it's got pad stack calculators, crosstalk conductor uh via impedance, and uh parts per million calculators, embedded resistors on your board substrate resistors, and uh it's just it's insane. It's the best tool ever.

**Dave Jones:** All right, so we'll go to conductor properties here. And as I said, there is a DC and AC element to this. We're not interested in our AC characteristics, we're just looking at our DC voltage drop here. So, let's not complicate

**Dave Jones:** things. So, let's just set it to DC mode here. Uh well, let's have a look here. We'll have to go over to imperial, none of this micrometers rubbish. Oh, I'll be swapping back and forth. It's just a habit. Anyway, let's look at our base

**Dave Jones:** copper weight, which we've got in our PCB. Now, everyone's used to 1 oz copper. Now, you don't automatically get 1 oz copper on a big eight-layer board like this. you might get 1-oz copper on the outside layers. Uh but more often than not, you'll get

**Dave Jones:** 0.5-oz copper. Or you might even point get quarter-ounce copper. Um but half-ounce copper is the most common on the inside. And then you've got the plating thickness here. This is whether or not your board is plated. In most cases,

**Dave Jones:** your traces are not going to be plated. Or your internal layers, they're just bare copper. Um it's just they just etch it as bare copper, then they sandwich the extra layers on top and on top and on top. And even your top and bottom

**Dave Jones:** layers usually aren't plated. It's what's called solder mask over bare copper or SM OBC. So, if you scrape away, that's why if you scrape away the solder mask on a trace, you'll just get the raw copper. So, there is no plating.

**Dave Jones:** But if you had it tin-plated or something like that, you can add that. And you might see that the resistance down here might halve. Yeah, about half if you plate it, something like that. Cuz your plating might be another half

**Dave Jones:** ounce plating, for example. So, anyway. So, there you go. So, we'll set a bare PCB like this, assuming we've got like an internal layer. Half-ounce copper. Uh I'm going to go over. And an external or internal layers makes a difference.

**Dave Jones:** Well, it doesn't make a difference to the conductor resistance here. The conductor resistance is going to be the same, but it'll make a difference to power dissipation. And whether or not a plane is present here, you'll see that

**Dave Jones:** it only affects the power dissipation figures, which we're not really you know, we're that's not a concern. All we're concerned about is the DC resistance and uh the current and the voltage drop at a particular current. Because in this case, the plane, you'll

**Dave Jones:** see how when you enable that, it puts on a distance to plane like that, 10 mils, 10 thou between the planes. Because then you'll get conduction or you know, radiation from the power trace through to the power plane. And then that power

**Dave Jones:** plane can kind of act as a poorish heat sink, and that's why your power dissipation will be more if and further away if you drop, you'll notice our power dissipation will Can we resolve that? There you go. It goes down. So,

**Dave Jones:** you know, 100 mils like that. Anyway, that's got nothing to do with what we're doing today. It's just a side thing, but there's lots of complex stuff that goes into PCB layout. People are like, "I did PCB layout and designer, they just lay

**Dave Jones:** out some traces and you know, Bob's your uncle." No, there's a ton of stuff. If you got bleeding edge parts pulling lots of power like we do on this one, and all these different voltage rails with all these different DC, AC, dynamic, and

**Dave Jones:** static power uh conditions to meet very tight tolerances, you know, it's it's it's nuts. There's a ton of stuff involved. I could do a video on every single one of these properties in every single one of these tabs. Anyway,

**Dave Jones:** calm down, Dave. Let's go over here. Let's say you've got a 20-mm trace, you know, a big thick trace on your board, right? And the conductor length in this case, what did I say it was 20 cm? So, let's go 200 mm like

**Dave Jones:** this, and the PCB thickness doesn't matter. It makes no difference whatsoever. And our let's call it uh 10 m ohms there. Can we solve Yeah, now we've solved it. 10 m ohms there, and the current down here actually has

**Dave Jones:** to do with the temperature rise, and I've done this in a separate video. So, if you've got a that 20-mm wide trace over 200 mm at no normally 10 m ohms uh resistance there, it will that trace will rise by 10° C.

**Dave Jones:** It'll actually go up It'll heat up when you pass 7.2 amps through it. And you can see that we were like talking about 8 amps here, for example. And a 10° is a bit of rule of thumb for temperature

**Dave Jones:** rise. You really don't want any more than that. Um a lot of people set it to five. I'll often set it like half it to five. I don't want a 10° rise and stuff like that. Anyway, 10 m drop on that

**Dave Jones:** trace the 8 amps we're talking about, 80 mV drop. That's only one of them. That's just the power trace. What about the ground trace? Bingo, you've got 160 mV already. We're already over our Altera data sheet limit. Where was it? Hey, you

**Dave Jones:** remember? It was only 125 mV. So, if we take our power trace like this over to here and it was 20 mm wide, for example, nice big huge beefing power trace, we're going to get a voltage drop across there

**Dave Jones:** of 80 mV at 8 amps. There you go. And then then you've got the extra drop for the the same drop again for the ground or whatever. But in this case that's going to the switching converter. I probably

**Dave Jones:** should have drawn that the other way. Let's just say that we had our nice big square in here like this and then we had our 20 mm trace coming over. If it was like let's just say that's 100 mm there,

**Dave Jones:** then we'll get half the voltage drop on that. So, we'll get a 40 mV drop coming from the output of here over to our assume let's assume that once it's gotten under the FPGA like that, you get your one big solid thing that there's no

**Dave Jones:** more kind of little drops in here, for example. There will be. There might be, you know, 2 mV or something like that going from one side to the other. Whatever. Depends how many vias are in there like actually uh breaking up that

**Dave Jones:** uh that big nice big solid block you've got in there, but you might have you could easily have 40 mV drop going from there to there at 8 amps. Easy. And that's just the power, let alone the ground connection as well. But, you can

**Dave Jones:** argue that if you've got a nice big solid ground plane like this, for example, then you can kind of round it down to zero. You might add on 5 mV or something like that. But, you get you know, you might but there you go. Right?

**Dave Jones:** You remember we only had 120 mV margin. And remember that doesn't include any dynamic characteristics, that doesn't include any layout issues and how much uh you know, drop if the LCD up you remember we got our LCD over here as

**Dave Jones:** well. It's going to be drawing uh it's it's going to be drawing its own current, so you're going to get extra drop across there. And if And if you did have one big ground plane, yeah, sorry, you can't see the my drawing cursor.

**Dave Jones:** Oops. Anyway, if you got one nice big ground plane like this, getting extra power that has nothing to do with the FPGA across from one side to the other, that's got to share that space. You can get the voltage drop inside this power

**Dave Jones:** plane going from here over to here, and you know, that could be that could be an extra I don't know, 50 mV or something like that. Who knows? It depends on the load that you're getting, and that could

**Dave Jones:** interfere with your voltage drops inside your FPGA like this. You can come at that. That's uh Let's get rid of all that. That's why you would have a star ground, for example. You would separate If I was say

**Dave Jones:** let's say this was all the power Well, it is. This is all the power going off to our LCD panel over here. I would literally split my ground like that, and I would have ground going over separately, and then I'd I'd literally

**Dave Jones:** have a split in there like that. I'd have two separate grounds. They eventually join back here. So, we've actually split or it's effectively like a star ground. This is our This is our point and then, of course, then we might have, say,

**Dave Jones:** another ground plane going over here to the rest of this FPGA and maybe if we had some circuitry up here that then needed its own ground plane, we didn't want to interfere with the others, then we would actually split

**Dave Jones:** the ground plane like this, for example, under all the memory and the FPGA. That would have one ground plane, then this would have another one and it'd all come back to the star grounding point like this. So, this space in here you would

**Dave Jones:** leave blank. That doesn't have any ground plane in it. So, you've isolated your Oh, yeah. You've isolated your ground planes like this, so that the current flowing from here around here, ground and power to to the LCD connector over there,

**Dave Jones:** doesn't interfere with your FPGA or the switching in your FPGA doesn't interfere with the power going over there and vice versa, DC and AC characteristics as well. But remember, when you split power planes like this, you have to be

**Dave Jones:** incredibly careful because it can be really bad news for EMC. Uh so, in this particular case, look, we've got the the connector goes down here. This is the high-speed connector that goes off that's driving the LCD. So, in this

**Dave Jones:** particular case, the Altera um the signals are coming out of here. They're going through these buffers and then they're going across here. And if you've split your ground plane across here and that ground plane is used for those

**Dave Jones:** switching signals as the return path for those switching signals, you are screwed. It is one of the cardinal sins of uh PCB layout to split your ground planes and then have the signals running across them like that because then the

**Dave Jones:** currents have to flow all the way and then your loop is much bigger and larger loop creates greater EMC. I've done a whole video on that. And yeah, don't do that. So in this particular for this particular layout here, when I

**Dave Jones:** suggest doing the split ground plane like this, I don't mean split up the signal ground plane which takes that one up. I'd probably have separate ground planes, one that just handled the current for the LCD connector over here

**Dave Jones:** and one that and then a separate one that handled all the FPGAs and stuff like that. So yeah, I I just would have devoted one section on another layer for that. But in this particular case, the FPGA ground would have extended down

**Dave Jones:** here like this on a different layer. And you can have like grounds overlapping other grounds. That's fine. So then we can have the separate on another layer than the ground for the uh power and LCD connector coming over.

**Dave Jones:** So ultimately, I think the reason for the wires is is pretty obvious given the proximity and also this power connector going off to the dry driver and LCD board. It's cuz the driver and LCD takes their own fairly large amount of power

**Dave Jones:** and they didn't want that flowing right across the board like this which could screw up everything. They didn't want it flowing across the ground planes and they probably didn't have enough internal layers to add some extra ground planes to do that. Um sometimes you can

**Dave Jones:** fix this if you rip up your whole board and redo it. Like you might realize this at the last minute and like oh, you know, you're 2 weeks into your layout and you might realize oh damn, I forgot about

**Dave Jones:** you know, I forgot about the extra power coming over here cuz often the designers of the schematic like they may if they're good, they'll put notes on the schematic explaining how they want stuff done. But it's ultimately up to like which things are

**Dave Jones:** important saying, you know, look it like they'll show it as a star ground and things like that. So, the PCB layout person has to know that and and stuff like that. But, you can you know, your brain's not engaged. You can spend a

**Dave Jones:** week still in your layout and then you come and go, "It's all I couldn't be bothered redoing the whole thing. You've got a tight deadline or whatever." Okay, well, let's just add some wires on there. It's not a high volume product.

**Dave Jones:** She'll be right. But, of course, those wires aren't magic. They're going to have voltage drop, too. In this case, I think it's about maybe 15 AWG wire, you know, or maybe 1 and 1/2 mm, something like that. Ohms per kilometer, uh it

**Dave Jones:** doesn't allow you to will have to convert that. Let me get the confuser. Don't could have done that in my head. Divide that by 1,000. That's uh 10 mΩ per meter. So, we're looking at 2 mΩ for 20 cm. Uh multiply that by 8 amps. We're

**Dave Jones:** looking at 16 mV drop on one of those wires. That's not two of them. So, you might have to double that. Could that could be take you up to 32 mV drop just for getting your 8 amps through there

**Dave Jones:** like that. So, yeah. So, yeah, whether or not they're doing that voltage drop reasons, I think it's just like a a star routing thing. I think they're just trying to avoid all the stuff in here by just manually

**Dave Jones:** routing around there cuz they probably couldn't have I don't know why they couldn't have put their planes in here like I showed before, but anyway, I I wasn't there when this was laid out. I don't know. And I'd have to get the CAD

**Dave Jones:** files. You'd have to look at the actual layout on here. So, after what, 30, 40 minutes, we finally we can answer the OP's question. Uh what width trace do you need to be equivalent to the wire? Well, let's say

**Dave Jones:** it's 15 AWG wire, which is looks roughly what we've got here. 10 ohms per uh kilometer, we're talking 1 mΩ for 100 mm. So, that's not much, but it looks like we can do that with say 25 Oh, solve. Let let let's say just over

**Dave Jones:** 20 mm. So, I was I was roughly right. Something like that. There you go. 22 mm. And to answer the OP's question. And the thing is like this is a fairly simple board. Like as far as FPGAs go,

**Dave Jones:** this is you know, we've got a quite a large margin there 125 mV on our rail, which as I said you can extend it if you tweak that tweak the voltage of the converters up here. You put them on the

**Dave Jones:** high side. So, that's why often way back in the day a 5-V rail wouldn't be 5 V. They'd actually set it to 5.25 V. So, that all the circuitry near the connector it'd get 5.25 V, which it'd be

**Dave Jones:** on the upper side of your 5-V tolerance on your 5-V rail. Everything's fine, but by the time it got all the way to the other side of the board with the hundreds and hundreds and hundreds of chips on there as the old boards were,

**Dave Jones:** it might drop down to 4.75 and you're still right. You're still within the margins. But, modern devices with their 0.9 V, 0.8, even lower core voltages and if you put you know, you might have half a dozen of these large FPGAs on a

**Dave Jones:** big complex board, you can be talking tens of amps, 50 amps, even 100 amps. You can go into triple figures on the amps for a you know, a really complex board like this and it's a big deal and

**Dave Jones:** and that's when you might go in here and go bugger it. I need 2 oz copper in If you're desperate, I need 2 oz copper in at least a couple of your internal layers. You wouldn't use 2 oz copper,

**Dave Jones:** for example, if you had real a mix of high power stuff on your board with lots of other signal stuff. You wouldn't have 2 oz copper on every one of your eight layers. You'd tell the PCB manufacturer in your stack up chart you'd tell them

**Dave Jones:** that hey, I I I need these, you know, layers three and four. They They're my power rails. I want those 2 oz copper, please. Plus, 2 oz copper on your ground as well. And you might have multiple ground layers. But then your shield

**Dave Jones:** ground layers, for example, I don't care. I can use 0.25 oz copper. It's not carrying any of the current, for example. It's just like using for switching. It's, you know, it just might have lower dynamic requirements switching AC dynamic current

**Dave Jones:** requirements rather than the big bulky DC type stuff. But cuz the problem with 2 oz copper, as I mentioned in the previous video on this IBM monitor, if you got 2 oz copper on all your layers, that actually retains a lot of heat when

**Dave Jones:** it goes through the reflow oven. And then the balls on your BGA may not re- It gets, you know, much trickier. You got to hold your tongue at the right angle. You might have to call in the graybeard

**Dave Jones:** to operate your reflow machine to get that vapor phase setting just right so that the balls like so that you get reflow on your balls and it doesn't These boards can come out piping hot like a fresh pizza from an oven. And

**Dave Jones:** those 2 oz copper really retains a lot of heat. If you got multiple layers in there, well, it can stay hot forever. And that slows your cool down time cuz a lot of your There's a lot of art and science to actually setting the

**Dave Jones:** temperature profile. It's not just ramping up the temperature. People think, oh, it's just all about ramping it up like this. And then solder melts. It's also about cooling it down. You can't cool it down too slowly, either. Cuz then the solder can enter the

**Dave Jones:** plastic region and cause all sorts of dry joints and all sorts of, you know, then you get into material science. And it just never ends. But on a real complex board like this with thousand pin or 1,500 pin

**Dave Jones:** BGAs drawing, like with 2 oz copper, it's going to ruin your day. I've had boards which have used really thick 2 oz and then all of our components like tombstone, all of our resistors tomb can't stone cuz we didn't glue them

**Dave Jones:** down, and just the slight imbalance between the pads was enough to flip them all up, and yeah, it's not fun. So, have I waffled on enough? Have I explained why they put those wires in there? We can't be

**Dave Jones:** exactly sure, but hopefully you're still with me down this rabbit hole deep dive, and I can go further than this as well, but I I might leave it at that. Hopefully, I've given you a taste of what it's like to design these

**Dave Jones:** and lay out these high-end boards with these large current FPGA devices. There's so many things involved. You know, people just think about bypassing, but they often forget about that DC characteristic and the voltage drop on the traces and and how when you have big

**Dave Jones:** ground planes, you can't really I well, you could kind of you can sort of simulate this like on a spreadsheet. You can do it crudely. You can do your own poor man's finite element analysis and and try and calculate and stuff like

**Dave Jones:** that, but you know, generally, that's kind of why I like to separate my powers and grounds on the board not only for very good technical star grounding system reasons, but also then you can start calculating stuff like this cuz

**Dave Jones:** oh, I've got a block like that. It's going to have X amount of resistance, and then a block goes up like this. As I said, like this will actually be the shape of some of these ground planes. In

**Dave Jones:** fact, I I might pull up a board. I'll I'll show you a real board example. It's not as complex as this, but I'll I I think I've got one. Okay, I found an example with a Virtex-5 FPGA. It's a

**Dave Jones:** fairly large one. It's 1,136 pins, and as you can see, we've fanned out, you know, a good majority of those. There's I don't know, 50 not used or something like that. One, this is actually a 10-layer PCB. So, let's Let's

**Dave Jones:** a look. This is the top layer. Okay, we can actually, and if we turn on all the layers there, doesn't that look funky? You can just see all the various layers. Anyway, let's go back to single layer mode. It's much easier. And so, this is

**Dave Jones:** our top layer. Here's all our pads. You can see how our vias have been like we fanned out a via from each one. I've done a video on BGA fan out and stuff like that. Don't know if I used this one as an example,

**Dave Jones:** but you can see the different rails in here. We've got 1 V 2.5 V, 3 There should be 3.3 V for IO. Yes, our 3.3 V IO's on the outside. That's quite common because the IO pins are on the

**Dave Jones:** outside, so your VCC pins are on the VCC. Your VCC IO pins are on the output. And I believe yeah, we've only got the three voltage rails there. So, not that many, okay? But this required a 10 layer board

**Dave Jones:** to fan this out and get the power in. So, let's go have a look at the second layer. Second is a GP, so that's ground power. I don't I don't remember what P stands for, but that's just one big

**Dave Jones:** ground plane right over the whole thing. So, I didn't split the ground plane up. Layer three, it's just got some high-speed differential gigabit Ethernet traces going out and just some signal layers going out. There's no power happening on there, but once again, you

**Dave Jones:** could have used this layer as an extra one to get power into there because all this spare space in there. And then there's another ground layer because of the the high-speed differential pair of the 10 I don't know, was it 8 gigabits

**Dave Jones:** per second? I can't remember. Anyway, so we had multiple ground layers in there. That's why we needed the 10 layers. And then we've got one layer dedicated to the 3.3 V rail, so that's just flood fill right over. So, this was like, you

**Dave Jones:** know, pretty generous on this board. But if you want to get your cost down, we we could have. So, this one's just a signal. And here is where we start to get into our power. So, this one in here is not That's that

**Dave Jones:** that's ground fill. That's just ground fill. Nothing Nothing special there. Just decide to put some extra flood fill in there. And here we go. Here's where we do that block. I didn't put a block across the whole thing, but you can see that

**Dave Jones:** there's an internal So, there you go. That's our 2.5 V. So, that's coming in from the Yeah, it's coming in from the bottom here. So, yep. There we go. It's flowing in. Whoop. There you go. It's flowing in from over

**Dave Jones:** here. So, 2.5 V. So, it's a reasonably small trace. That wasn't a particularly high current uh thing, but you can just That's an example of how that you can just put the big block in there on one layers. But, you know, of course, like,

**Dave Jones:** oh, I had to get that trace out there. Bugger it. I couldn't do it on some other layer or I didn't want to. Whatever. But, yeah, that's an example of having the power block. And we'll see that again. Yep, we see

**Dave Jones:** that again. You can see the split down here. So, this one is for the 1 V. This is the core voltage. So, this one's going to be higher power. So, hence why Look, it's huge. You can see the split

**Dave Jones:** all around here like this. Yep. There we go. It's that big pink block like that. Huge big low impedance block like that. And that's coming from the uh I don't think we had a regulator on here. I think it was coming from elsewhere. Oh,

**Dave Jones:** no, it could have. Anyway, so, that's coming from up here. And that's hugely low impedance going right down to the FPGA core. So, that's a good example there of uh doing that that power block and big low impedance

**Dave Jones:** running into it. And as you can see, we don't really have many traces coming out on that layer. Just a few on the uh outer pins and stuff like that. But, of course, when you're laying out something like this, you would make sure because

**Dave Jones:** of that DC requirement for your FPGA that's fairly critical, you want uh to ensure that you do route that first so that you don't try and sneak it in later. Um, you know, you really want to take care of that right up front and then

**Dave Jones:** figure out how you do your signal traces later. And then the bottom, I don't think we had anything special on the bottom. No, that was just ground and there we go. We had various uh just the bypassing caps and stuff on the bottom.

**Dave Jones:** So, there you go. That's 1,136-pin Vertex 5 FPGA, but not particularly uh major high current requirements apart from that that 1-V uh rail did take a bit but not much on the 2.5 or the 3.3. But, every FPGA is different. And I was

**Dave Jones:** actually going to get a power estimator for you cuz all the FPGA companies have these power estimator programs, spreadsheets, whatever they are or tools to you put in your number of gates, your specific family you're using, your switching speeds, what peripherals

**Dave Jones:** you're using, what IO and all that sort of stuff you're doing and it will simulate fairly accurately, depends you know, garbage in, garbage out of course, but if you put enough stuff in there it'll or if you're if you're simu- or if

**Dave Jones:** you're finish your design and then just run the calculator on it, uh put in all all the various factors, it'll give you a very accurate estimation. The power consumption, I wanted to do that for the Apex FPGA, but I went to the Altera tool

**Dave Jones:** power estimator tool website and it has everything but the Apex series. So, I I don't know what happened to it. Not that. It's probably out there somewhere. Anyway. And here's actually a better example of a larger board. Once again, a big uh

**Dave Jones:** 600-something pin uh BGA over here, but let's have a look at the different layers. This won't tell you much, but if we go that's a ground. Oh, sorry. You couldn't see that. My face is a bit If you go to the power

**Dave Jones:** rail, you can see how they're actually split on the bottom here. That just, you know, shows how you can snake things around and just avoid various things. It's not the best example, but but it shows you just how you would might split

**Dave Jones:** up your power planes on a board to uh to avoid voltage drops on one high power section causing issues on a lower power section, stuff like that. So, I think we'll call it quits there. Sorry for the length of this video, but as you can

**Dave Jones:** see, there's a whole bunch of stuff involved in this and we're I wouldn't go I'm not going to say we're scratch the surface, but we've probably only scratched the surface of what you can deep dive into on this

**Dave Jones:** sort of thing. There's just so many different uh you know, permutations and combinations of of different scenarios that you can get on boards like this and and how hopefully you're going to appreciate what a PCB designer, what a

**Dave Jones:** professional PCB designer, and professional design engineers have to go through for some of these and consider for some of these complex designs that have all these, you know, high-end FPGAs and things like that. And this one from 2000 and this IBM one is not that

**Dave Jones:** complex, but they decided we need to add the wires in there for insert my perhaps multiple reasons in there. Perhaps at the design stage, perhaps as an afterthought. We don't know exactly, but anyway, it's really interesting. I hope

**Dave Jones:** you found that useful. And if you did, please don't forget to give it a thumbs up and subscribe and notify as well. Hit that little bell icon wherever the hell it is. And to make sure you get notifications if YouTube will be

**Dave Jones:** gracious enough to send notifications to everyone when I release a new video. Anyway, I hope you enjoyed it. Discuss down below. Catch you next time.
