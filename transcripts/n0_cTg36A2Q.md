---
video_id: n0_cTg36A2Q
title: EEVblog 1620 - Deye Solar Hybrid Inverter EXTREME TEARDOWN
url: https://www.youtube.com/watch?v=n0_cTg36A2Q
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 23, "3": 37, "4": 54, "5": 70, "6": 95, "7": 111, "8": 123, "9": 136, "10": 151, "11": 163, "12": 178, "13": 189, "14": 203, "15": 217, "16": 233, "17": 248, "18": 263, "19": 275, "20": 298, "21": 315, "22": 328, "23": 344, "24": 363, "25": 380, "26": 398, "27": 416, "28": 430, "29": 448, "30": 466, "31": 488, "32": 507, "33": 518, "34": 534, "35": 551, "36": 567, "37": 585, "38": 602, "39": 615, "40": 632, "41": 649, "42": 662, "43": 680, "44": 694, "45": 708, "46": 722, "47": 736, "48": 755, "49": 771, "50": 787, "51": 799, "52": 816, "53": 835, "54": 850, "55": 865, "56": 882, "57": 900, "58": 920, "59": 933, "60": 947, "61": 959, "62": 970, "63": 984, "64": 1000, "65": 1014, "66": 1027, "67": 1039, "68": 1052, "69": 1068, "70": 1083, "71": 1096, "72": 1110, "73": 1122, "74": 1138, "75": 1151, "76": 1170, "77": 1185, "78": 1197, "79": 1214, "80": 1231, "81": 1244, "82": 1258, "83": 1273, "84": 1286, "85": 1303, "86": 1320, "87": 1336, "88": 1353, "89": 1375, "90": 1389, "91": 1401, "92": 1413, "93": 1425, "94": 1438, "95": 1448, "96": 1461, "97": 1474, "98": 1489, "99": 1503, "100": 1517, "101": 1530, "102": 1543, "103": 1556, "104": 1571, "105": 1586, "106": 1600, "107": 1613, "108": 1627, "109": 1640, "110": 1656, "111": 1675, "112": 1689, "113": 1706, "114": 1721, "115": 1738, "116": 1752, "117": 1768, "118": 1783, "119": 1796, "120": 1811, "121": 1829, "122": 1842, "123": 1855, "124": 1869, "125": 1882, "126": 1896, "127": 1913, "128": 1927, "129": 1942, "130": 1958, "131": 1974, "132": 1994, "133": 2007, "134": 2021, "135": 2032, "136": 2049, "137": 2064, "138": 2078, "139": 2093, "140": 2106, "141": 2119, "142": 2133, "143": 2143, "144": 2155, "145": 2170, "146": 2185, "147": 2203, "148": 2216, "149": 2228, "150": 2244, "151": 2264, "152": 2277, "153": 2291, "154": 2303, "155": 2315, "156": 2330, "157": 2343, "158": 2353, "159": 2365, "160": 2377, "161": 2391, "162": 2404, "163": 2415, "164": 2429, "165": 2445, "166": 2457, "167": 2469}
---

**Dave Jones:** Hi, do you remember this DIY solar hybrid inverter that I attempted to tear down in my previous video cuz I'm going to install one of these on my home and my spidey sense told me, "Uh, don't take it apart too far because

**Dave Jones:** it's going to come a gutser. It's going to be a real mess." And my spidey sense turned out to be correct. And if I tried to tear it down properly, uh, do a full tear down, then, yeah, getting it back

**Dave Jones:** together is a real problem. But as it so happens, one of my viewers had the exact same model already torn down. So, thank you very much to the viewer who sent this in so we can do a full tear down on

**Dave Jones:** this. And even better, we have the brochure, which claims a few things. So, let's, uh, trust but verify. So, this is the exact same one that I've got, the Sun 5K SGO4LP1, and it's the Aussie, uh, version. But

**Dave Jones:** let's take a look at this brochure here from 2023 from DI, um, world-leading energy storage system provider. You know, they have a blurb about their company and everything else, right? It's all looking the glossy brochure and, you know, everything's looking fantastic.

**Dave Jones:** And, uh, what do we have here? World-class component suppliers, Infineon MOSFETs and IGBTs, ON Semi, Alpha Omega. We've got Nippon Chemi-Con capacitors, TDK, Fairchild, uh, Panasonic relays, Texas Instruments IC, Toshiba. All these big names. So, let's see if it's actually

**Dave Jones:** got these, especially the Nippon Chemi-Con caps. Hmm. Now, although I haven't used it yet, they actually do look like a, you know, a reasonably quality, uh, manufacturer and they've got, you know, one of the best bang per buck on the market. Uh, you can have a

**Dave Jones:** look at the, uh, specs, uh, for yourself in terms of their solar hybrid inverters. So, anyway, I'll be able to tell you that uh long-term after I get my one uh installed and we get, you know, some data back that over, you

**Dave Jones:** know, data over like 6 months, 12 months, and stuff like that. But, let's do a teardown and see if they actually have the quality components in here they claim to. So, we actually have all the boards already taken out and all

**Dave Jones:** individually wrapped up and we've got the uh carcass over here, of course, which has all the uh various inputs and uh whatnot. And I gone over that in the uh previous uh video. It's got the It's even got a PV isolation uh switch on it.

**Dave Jones:** I do believe that mine's going to get installed using this uh isolation switch cuz I've got two strings coming into this. So, it's a dual uh string isolation uh switch on it. And of course, there's all the uh specs for

**Dave Jones:** those playing along at home. And we've also got one more board in here. Oh, look at that. That's the uh LCD display board. Won't go too much into that, but for those playing along at home, there you go. You can view this in 4K resolution.

**Dave Jones:** You can have a squeeze at that uh little display. Has it got more uh actual processing on the other boards? I guess we'll find out. It's interesting to note that I'm not sure if you're going to Yeah, you can pick up the shine on that.

**Dave Jones:** Uh you can tell by the shine that this actually has a conformal coat on it. Or at least it's got a partial conformal coat over the uh components. Of course, you're going to get that um to prevent moisture ingress uh onto your components

**Dave Jones:** and, you know, causing leakage across the board and subsequent uh problems. Of course, this unit uh is of course mounted outdoors uh potentially in the sun and in the cold. It gets thermal cycled. Uh you're going to get, you know, dew inside this thing

**Dave Jones:** and all sorts of stuff. Um so, yeah, moisture build-up inside this thing. So, yeah, that's conformally coated. Uh that's nice. And you can see the chassis just welded together there. And check out this gigantic, what looks like potted uh Maybe we can try and dig that

**Dave Jones:** out. That could be a lot of effort, but uh basically this is where they mount huge heat sink on the back. Uh panel's got a little temperature sensor there, but all of the power MOSFETs or IGBTs that are in there, they all mount on the

**Dave Jones:** bottom. But obviously, you can see it's got another section here, which is potted. And if you have a look on the back, you can see that is actually a an entirely separate heat sunk uh section. So, yeah, they've got this one here. Um

**Dave Jones:** you know, there's nothing under that. So, these transistors here just mount in directly use those big finned heat sinks here. And but these ones have their own separate little things. So, here you go. We have all the boards out of this

**Dave Jones:** thing. Look at this. We can do a complete analysis of the design and construction of this thing. Let's go. Beauty. World-class component suppliers. Nippon Chemicon. Reality? Uh Aishi?

**Dave Jones:** Yeah. Um so much for our Nippon Chemicon Japanese capacitors. Um these are Aishi brand, which they're not a bad Chinese brand, but they're like they're probably one of the better Chinese brands out there, but they're not what they claim

**Dave Jones:** in the brochure, which is weird cuz we saw in the previous video how I did I showed a video of somebody else tearing down a similar model DI inverter, and they did use Nippon Chemicon. So, somewhere along the line they decided

**Dave Jones:** and screw the brochure and the marking that we claimed. No, we're going to put in these Chinese capacitors instead. And this bank over here, these are also Aishi capacitors. So, not only the DC battery bank capacitors here, but also

**Dave Jones:** the AC side capacitor bank. They're all Chinese shy brand, not Nippon Chemi-Con as claimed. Unbelievable. Been diddled. And here are these two huge blocks that we've got on the that are on the back heatsink, but they're actually separate

**Dave Jones:** devices themselves with their own integrated heatsink. And these are all silicone potted, but thankfully it looks like I've tried to dig it out. I can see that it is going to be fairly easy. So, we'll do an extreme teardown on that in a minute.

**Dave Jones:** But basically what we've got here is this block here seems to contain a couple of boost inductors cuz we've got L1 and L2. And yeah, boost boost and L1. So, yeah, they could be coupled in there perhaps. Don't know until we tear it

**Dave Jones:** down. This one here looks like it's got two separate windings. It's got TRA1 and TRA2. So, that would be a transformer. So, that is a nice thumping transformer. And it gets hot enough cuz this is you know, it's a 5 kW jobby here we're talking

**Dave Jones:** about that yeah, it requires its own little you know, enclosure heatsink and everything. It's very nice that they've gone to that effort. And there's actually two extra leads here. They're SH something. So, not sure what's going on there. And there's an extra little

**Dave Jones:** two-pin lead coming out here. That's probably a temp sensor. Thermocouple down in there I would imagine. Just to check that the wheels aren't falling off the transformer billy cart here. So, yeah, let's crack it open. Well, this is fun, let me tell you. And of

**Dave Jones:** course, when you got big inverters and boosters and converters like you've got in a solar hybrid inverter like this, um all of your all of your power dissipation, most of it is going to be in your switching and your storage energy

**Dave Jones:** storage and transformation components. Hence, energy storage in these large inductors here. That's why they need massive heat sinking on them. And of course, switching with all your switching transistors up here and and or diodes, of course. And of course, then you've got energy

**Dave Jones:** transformation in your transformer. Hence the name, transformer. It transforms energy. But, there's going to be losses in there. So, yeah, heat sinking it is. Well, unfortunately, it is going to be diminishing returns in terms of energy expended to try and get

**Dave Jones:** these inductors out of here. Anyway, I think we've seen all we want to see here cuz like these are all going to be stuck right to the bottom. And to try and get all those out, it's going to

**Dave Jones:** be really ugly. Time consuming, but hey, we've got four separate toroidal two of them way bigger than the other two over here. And looks like there's no coupling between them. They're just putting them in this thermally conductive, of course.

**Dave Jones:** This is not thermally insulated. This is thermally conductive silicone potting compound in there. So, it's pretty groovy, huh? And of course, because this is actually on the outside of the case, which is exposed to the elements, you have a nice

**Dave Jones:** rubber grommet going around there as well for your weather sealing. It's beautiful. And again, that's a yeah, nah, forget that out of there. That's just not going to happen. Anyway, check it out. Yeah, the Of course, there's no internal connections

**Dave Jones:** at all. The huge big like how many strands are they? Like couple hundred strands or something? Unbelievable. You can see that they're wrapped around a big toroidal core right in there. So, you can see that the inner layer like that is wrapped on the bottom

**Dave Jones:** and then the larger tap is on the top there. So, yeah, go in you know, it's not entirely symmetrical all the way around, but it doesn't need to be because you've got the circular toroidal core in there. No worries. That's just a

**Dave Jones:** thing of beauty, a joy forever. Look at that. There you go. It count the number of strands. I know someone wants to. Go for it. Now, where do we start on the topology of this thing? Trying to not

**Dave Jones:** completely reverse engineer it, but at least have a look at some subsections here and it is rather confusing because some of these standoffs here are actually used as electrical high current electrical connections actually between the two boards here and it actually took

**Dave Jones:** me a while looking at this thing going like where's the battery input cuz I know that obviously, right? This over here is going to be the DC battery array here, right? This is the DC for the DC battery capacitor bank, right?

**Dave Jones:** So, we've got the branded caps. So, we've completely been diddled there. You can tell there for the DC battery bank because of the voltage rating on them and they're all in parallel, of course, 63 V rated here and this is actually a

**Dave Jones:** what's deemed to be a low voltage in quote marks like battery bank hybrid inverter, a 48 V battery. It's not a very high voltage battery. So, the higher voltage ones have advantage in terms of less copper losses and things like that in the

**Dave Jones:** in the connecting cables and everything else, but the lower voltage batteries, they're safer etc. So, there's a trade-off. So, this entire battery bank here is clearly for uh these are all in parallel and these are clearly for uh

**Dave Jones:** the uh DC battery uh solution. And of course these big bad boys, these are for the AC side uh filtering cuz they're 316 V. These are all uh 120 uh degree C rated caps so no problems there. But

**Dave Jones:** they're certainly not the Japanese Nichicon that were advertised. We're being diddled. So I knew these were for the uh DC battery uh filtering but I didn't like it confused me at first. First I thought, "Well, okay. So where's

**Dave Jones:** that means that the uh battery uh actual connections will be on here." But no, they're not. Um you'll notice that's actually a fan connection uh down there and these are just mounting holes, these ones down in here. Sorry, it's hard to

**Dave Jones:** uh see but the actual connections uh here, these three connections over here. We can flip the board, you can see what's going on here. These three big uh standoffs uh board-to-board uh standoffs, they're what connect all of these this battery capacitor uh bank all

**Dave Jones:** in parallel here. And that's totally separate from the AC capacitor uh bank here. They just happen to mount them on the same board just because they ran out of room on what is actually the DC part of it over here. And here's the DC board

**Dave Jones:** and here is the battery input here. You can see that the positive battery input here actually goes through. Look look at this. It's just it's flopping around in the grease there but it's obviously uh screwed down and this is a 150 amp in-line fuse for the

**Dave Jones:** uh battery for the DC battery bank in here. And I thought this one was the negative but if you actually hold this board up to the light, there's actually you can see right around here there's no copper around there. That's just a

**Dave Jones:** mounting physical mounting standoff. The actual battery negative seems to be this terminal here which then goes into uh one of these big uh There it is. One of these big switching transistors down here. Got to wipe all the thermal grease

**Dave Jones:** off those. Just bloody getting everywhere. Now, we've seen that the capacitors aren't as advertised, so let's actually check these bad boys. It's a transistor cuz it's got Q, and let's see. What are they Can't read that. Anyway, let's flip a

**Dave Jones:** few of these up and see what we've got. The claim is the MOSFETs and IGBTs, insulated gate bipolar transistor if you don't know, they're just like a combined like the best aspects of MOSFETs and the ruggedness of bipolar transistors.

**Dave Jones:** Anyway, Infineon, On Semi, Alpha and Omega. Do we have them? Well, that's a nope. Who's NCE? There's a whole bunch of those. MagnaChip. That ain't Infineon. And what the heck is that one? I don't know. That's like three for

**Dave Jones:** three. We've got three different devices in here and none of them are the leading brands. Unbelievable. Dodgy as. Now, there's only two diodes on this thing and it looks like we may have a genuine name brand part. This is a Vishay ultra-fast

**Dave Jones:** diode. So, it looks like the genuine thing. So, yeah, I think okay, there's a Vishay in here, but all the other MOSFETs and IGBTs in here, they're not any of the claimed quality Western brands that they claim. They're just all these you know,

**Dave Jones:** Asian source brands that you've probably never heard of. Unbelievable. But the diodes are claimed to be Fairchild, not Vishay. So, and if you're wondering what these little things here, these are actually surface mount links to get increased current capacity on the

**Dave Jones:** PCB. And you'll see this like all over the board here. You can see that they've got all of these pads here. Um and what they can do is that they can either uh elect to just leave it as is, or they

**Dave Jones:** can uh in this particular case, look, this is a good example here of how and why they've actually put these links in because you notice that the copper actually bottlenecks down here, and the copper isn't as wide here, so you're

**Dave Jones:** going to have, you know, it's going to increase your resistance here. So, they've added in these little surface mount links here. You can pick and place them and put them on the uh board. So, that just decreases the resistance

**Dave Jones:** through here. I don't know why they didn't add a couple more in here and stuff like that. But, anyway, that's the purpose of these things. Yep, they've advertised those big names and they've substituted them for whatever they could

**Dave Jones:** get in China. They're probably pretty decent, but they're not as advertised. All right, let's take a more detailed look at the uh PCBs and the topology of this thing. Little bit of reverse engineering here, thanks to an EEVblog

**Dave Jones:** forum user Phoenix, uh who is actually a former uh solar inverter designer. So, thank you very much. Um it would have taken me quite some time to actually, uh you know, dig into this and get a reverse topology schematic. But, uh Phoenix is

**Dave Jones:** an expert in the field, uh has designed these before, so knows exactly what he's looking at. So, he's uh very conveniently done a uh a topology diagram here. So, this is how a solar hybrid inverter works. You've got your

**Dave Jones:** PV input here. This is actually a dual string one, and they're just in parallel. So, you've only if you've only got a single uh string inverter, then you only have the one here. But, they're actually both uh basically in parallel.

**Dave Jones:** So, we've got our solar cell uh input here, our string array. That can be up to many hundreds of volts, but uh you've got to actually uh boost that up to give you a high voltage bus across here, and

**Dave Jones:** of course you need a capacitor array there, a high voltage capacitor array, to smooth out uh that voltage. And of course that is going to be this high voltage uh bus cap array here. So, these are in uh series to give you higher

**Dave Jones:** voltage. They're 315 V each, but they put them uh in series. So, there's four parallel banks of uh two series capacitors. They're 1,000 µF each. So, you got 500 µF uh total, and multiplied by four you've got 2,000 µF uh total there for your

**Dave Jones:** total uh capacitance for your high voltage bus. Nice. And of course you've got uh Hall effect current sensors here so that you can measure the current coming from uh the uh solar array, and you can see those there uh U7 and U5

**Dave Jones:** down there. So, your solar inputs are down here. Here you go. Here's uh one of the leads going off uh to the boost inductor over there, which you uh saw. Yeah, so nice little Hall effect uh sensor connected and they're connected

**Dave Jones:** directly through to those uh boost inductors we saw in that uh separate uh the toroidal ones that we saw inside that uh can. So, here are your PV array inputs here, and they've just got some uh common mode uh chokes there by the

**Dave Jones:** looks of it. And there's a whole bunch, look at this. Um these are Y class uh caps going down to earth by the looks of it. So, they've got a ton of that. And Phoenix actually speculates that this

**Dave Jones:** relay down here is likely for PV um earthing and isolation uh testing, and they're actually monitoring the physical connection of uh your earth. So, yeah, makes sense. And there's two large genuine Vishay uh diodes that we uh saw.

**Dave Jones:** You can see those there and there, and they're part of the uh there. Uh uh There we go. For the uh boost converter, they're part of the PV solar input. So, genuine jobbies there. Now, uh Phoenix did make uh one assumption here that

**Dave Jones:** turned out to be wrong. Uh these are not in channel uh MOSFETs here. These are actually IGBTs. Uh in particular, Q3 and Q8, they are actually these are MagnaChip uh 650-V field-stop IGBTs um here. So, not N-channel MOSFETs. So, you know, a

**Dave Jones:** bit overkill there. But generally these days it's easier to get IGBTs, uh which there's a symbol for an IGBT if you haven't seen it. Uh it's easier to get those in high-voltage uh jobbies than it is uh to get uh MOSFETs generally in uh

**Dave Jones:** like high-voltage ones. Back when I was working on like high-voltage ones, it was hard to get a 600-V MOSFET when I was a boy. But these IGBTs here, these aren't the uh same as the one that's used over there. These are actually

**Dave Jones:** these um NCE ones, and these are 1,200 V. These are real beasties here, um which does the grid side uh switching. So, here's our grid over here. So, this does our grid side uh switching, and you can switch it up there, or you can

**Dave Jones:** switch it down there. So, so we've basically got a H-bridge here uh using these 1,200-V IGBT MOSFETs. So, uh pretty beastly. And look, there it is, a three-level solar string inverter. And Phoenix has confirmed that yeah, these would be doing uh tri-level uh switching

**Dave Jones:** here on the gate. So, you know, there's like probably lots of complexity on the gate drives for all of this stuff that's all happening here. So, you know, we're not going to go into details there. This is just an overview topology. But

**Dave Jones:** suffice it to say, you're not just going to be switching those off or on. And Phoenix adds an interesting note that uh the solar arrays effectively are like a big capacitance down to earth. So, this actually affects the high-frequency

**Dave Jones:** switching performance of this. So, your your common-mode uh issues uh when you've got these big huge solar arrays out there, literally on an Earth, like, you know, or you know, potentially like they're at ground level. Might be different for your roof, I don't know,

**Dave Jones:** but um yeah, um it can affect your switching performance here and your common mode stuff. So, you know, bit of design complexity there. And he also said if you don't do the tri-level switching on here, if you just do bi-level uh

**Dave Jones:** switching, then it requires uh twice the AC inductance and that gets more bigger, more expensive uh real quick. So, yeah, tri-level switching. And interestingly, it uses a HERETIC inverter topology. That's what these two extra IGBTs here do. And HERETIC stands

**Dave Jones:** for high-efficiency reliable inverter concept. Um and apparently it is patented and there I come and the owner will actually sue you if you use the HERETIC inverter topology um without, you know, ponying up the money. So, I don't know if DI are doing that or

**Dave Jones:** whether or not they're uh try and touch us, we're in China. And this patent is owned by Fraunhofer. Um and here they are, first worldwide family litigation filed. Thank you very much. Um and here they are boasting about it. Fraunhofer successfully

**Dave Jones:** successful in patent infringement process for inverter technology. So, the Fraunhofer Institute for Solar Energy Systems has reached out-of-court settlement with leading inverter manufacturers, plural, in seven patent infringement cases. Um no, they looks looks like they have sued companies in

**Dave Jones:** China, Taiwan, and Germany infringed on their HERETIC topology. So, those simple putting two transistors across the output and driving them in a certain way, um that's patentable and I you owe the money to the Fraunhofer Institute. Geez. Now, I won't go into detail on how

**Dave Jones:** it works, but basically it can reduce it can improve efficiency and reduce noise by taking the uh freewheeling current and just diverting it during the zero crossing uh period. period when these are actually uh switched off. And yeah,

**Dave Jones:** you just get more more better efficiency, and it reduces your common mode uh noise issues. So, there you go. Um Herrick inverter spotted. So, then you got the uh two inductors here. They're the other two large inductors uh

**Dave Jones:** that we saw inside that uh separate heatsink uh can on the back. And then, of course, you got a um Hall sensor here just to measure your mains current. Uh where's that on the board? And you can see that Hall effect uh sensor down

**Dave Jones:** there. It's quite the beastie cuz that's going onto the uh grid there. And you can see the connection to the inductor there, and that's a leakage uh current transformer. So, they're measuring the uh leakage current there. So, uh yeah,

**Dave Jones:** that's our grid connection, basically. And that's all the driving uh stuff and sensing stuff uh for that. Our grid connection is actually over here. And have a look at this resistor array here. So, basically, what we got is four

**Dave Jones:** series resistors here to give you a higher voltage uh resistor. They could have done that with one through-hole uh jobbie, but they went for surface mounts cuz they're a couple hundred volts a pop. So, you put four of them in series,

**Dave Jones:** no worries. Uh that'll be grid uh rated there. Um and then, they tap off this like there. So, they tapped them off what I I think the PCB designer was just having a bit of a, you know, a fun time

**Dave Jones:** here um by making this into like a uh triangle shape. But basically, so that just comes out as a differential voltage into a uh instrumentation amp, and then they can uh just measure the grid voltage. But these are our actual uh

**Dave Jones:** load or grid connection here, uh which the grid is the load when you've got uh an inverter like this. So, uh yeah, basically, um just two big uh thumping relays here. Um and there's a then a whole bunch of uh common mode choke and

**Dave Jones:** filtering, and that eventually gets down to this leakage current circuit, and then then we've got two more Y class uh caps here, and then that eventually gets to our um Hall effect uh sensor down here. So, there you go. So, there was a

**Dave Jones:** lot Yeah, there were those um there were those X-class uh caps we saw, and that Hall effect uh sensor is down here. Now, as for our battery uh down here, of course we've seen that uh battery uh that capacitor array here, which is this

**Dave Jones:** big capacitor array here. These are all These are 63-V jobbies. It's a 48-V battery. Uh as I said, this is a low-voltage hybrid inverter. You can get like high-voltage versions that use, you know, battery packs in the hundreds of

**Dave Jones:** volts, and there's uh loss, you know, cable I-squared-R loss uh reasons for that, but it's a more dangerous uh you know, battery uh to have around if you got, you know, a couple hundred volt DC battery. So, the

**Dave Jones:** 40 That's a trade-off. If you want a little bit more loss, but a safer sort of lower voltage battery technology, no worries. Um you can use the 48, and that's what these These are 63-V uh rated. So, they're all in parallel, a

**Dave Jones:** whole bunch of them. So, there you go. And of course, this is bidirectional. Of course, the battery can supply power to your uh to to either the grid or this actually has an emergency load output. So, if the grid fails, uh this this

**Dave Jones:** hybrid inverter still continues to work and charge the batteries during the day. So, it's bidirectional. It can go in this direction like this and charge the battery, but then uh at night um or when you're off the grid's physically disconnected, uh power

**Dave Jones:** fails, then it can still supply current in this direction. It can still uh switch. It can do all the switching, goes through that large transformer. Once again, that's that large transformer we saw with the big uh toroidal uh core in there on its own

**Dave Jones:** heat sink uh in the back. Cuz I think the battery can do 5 or 6 kW or something like that, you know, it can charge and deliver um a load up to that uh value as well, as well as all of this

**Dave Jones:** being a 5 kW in like solar inverter up here, I think the battery's around about the similar power or even more. And of course, you got your current transformer here to measure the battery current, and of course, that can measure the current

**Dave Jones:** going in both directions, of course. Um and of course and on this side, because this is across the high voltage bus here, you need the IG you need the high voltage IGBTs, same as what we had over here, and they're those NCE jobbies,

**Dave Jones:** those 1,200 V jobbies that we saw. But on the low voltage side, remember this is only a 48 V battery, 63 V capacitor array, these are just regular lowish voltage N-channel uh MOSFETs. So, these are the China Resources Microelectronics

**Dave Jones:** Chongqing Limited um CRS Sky Mos MOSFET, 100 V jobby, 240 A, so very grunty. As you saw here, the fuse, the big fuse, is got labeled here. This is 150 A, so we've got 240 A capable MOSFETs there, so no worries.

**Dave Jones:** Yeah, so the battery comes in here, and this goes up, as I said, through these three big gigantic spaces here, they go up to the capacitor array, and they would return back to ground somewhere in here. Is that those there? I'm not sure, but

**Dave Jones:** anyway, yeah, they use those board-to-board spacers just as big high current interconnects. Works fine. So, once again, this is a H-bridge thing. Oh, and they put two of those MOSFETs in parallel, by the way. Um so, yeah, well, well, they're 240 A rated, so

**Dave Jones:** yeah, two of them in parallel, pretty beasty, but standard H-bridge arrangement here on both sides. And of course, what the H-bridge means is that each side of the transformer tap, in this particular case, can be driven down to

**Dave Jones:** ground, like that, or it can be driven up high. So, you can just switch and alternate and or disconnect either side of your transformer here. So, that's what a H-bridge does. Same thing for motor drives, whatever. Now, Phoenix

**Dave Jones:** questions, "Where is the DC blocking capacitor on the secondary?" And that is a good point cuz there should be a capacitor in here just like there's one here. So, DC blocking. So, you know, if these MOSFETs like short on or something

**Dave Jones:** like that, um you know, they come and got to fail, maybe you're having a bad day with Murphy, then you're not going to get just a basic like you know, pretty much DC short circuit across your battery. So,

**Dave Jones:** and then we've just got a few other tidbits here like we've got an auxiliary supply up here derived from the battery cuz as I said, this thing has to work if the grid fails. So, you've got to get power from the board. So, this is

**Dave Jones:** an auxiliary supply from the battery. It has to continue to operate in the case of grid failure cuz this is a hybrid inverter with an emergency AC power output. And you can see that emergency output here, which is a which is these

**Dave Jones:** load outputs here, which is different from the grid connection over here. So, it's got the two series relays there to disconnect those when you physically connect the load and this has like a quite large load capability. It's like you know, 4-5 kW

**Dave Jones:** or something like that. Almost equivalent to the grid inverter itself. So, it looks like this is our inverter drive stage going on here and then the secondary half DC to DC stage for the for the top half and that's for the high

**Dave Jones:** voltage. So, that's for the like say the positive side and the other's for the negative side. So, one half will be driving those and the other half will be driving those there. And all this here is our low voltage uh, side switching

**Dave Jones:** uh, stuff here. So, that's probably those little doohickeys there. Don't know what they are cuz everything's bloody conformally coded and you have to get the uh, the light at like almost horizontal coming in and you've got to turn it the right angle to try and read

**Dave Jones:** the bloody part numbers. It's really annoying. And we've got ourselves another little isolated uh, supply here and he speculates where this is uh, sourced from a separate auxiliary display, uh, you know, that display board that we uh, saw in there with the

**Dave Jones:** arm processor that needs its own uh, thing and that's where that bug is off to using that connector there. And then you've got fan control over here, some local regulation stuff. And uh, these may turn off and on the auxiliary uh,

**Dave Jones:** supplies or select the power source. Don't really know. Um, mm. And this is our main processor board interface here. So, we haven't had a look at that yet. And of course you want to know what the main MCU is. I was able to pull a number

**Dave Jones:** off that and that is this thing from Advanced Chip. Leave it in the comments if you've ever heard of Advanced Chip. It's a DSP, um, and it's a 32-bit floating point DSP. It's the AVP 32F 335. It looks like it's a rip-off of the TI

**Dave Jones:** uh, DSP. So, yeah, more cost-cutting I guess or they're more familiar with the design team is more familiar with it. I'm not sure how compatible it is um, or anything like that. Anyway, I'll link in the data sheet and you can have a look

**Dave Jones:** at it and we can well, have a quick squeeze. Probably good luck getting an English uh, version here. It's yeah, it's a DSP and I think it's a copy of a TI jobby. So, yeah, okay. And these chips over here that Phoenix speculated

**Dave Jones:** were analog measurement op-amps. Um, yeah, these are uh, sure enough um, three peak uh, once again this is like a native Chinese uh, brand but I have seen them before. It's the 2584 here and they're just um yeah, quad op

**Dave Jones:** amps, um nothing particularly special. They just get them over there cheap, I guess. And yep, these are uh 74 AC series uh something, and clamping diodes, and and then it's an isolated uh PSU, and then there's comms, and Phoenix

**Dave Jones:** seems to think that's a there's a secondary redundant uh microcontroller under here. Um so, that's interesting, and that's actually got uh 320 and 2802 on it. Um so, is it a Is it a genuine TI uh TMS320F2802, or is it some sort of like uh compatible

**Dave Jones:** one? I don't know, but it could have a secondary DSP in there that just, you know, keeps enough stuff If the main processor fails, just secondary one as a backup just keeps enough things going so that, you know, the magic smoke doesn't

**Dave Jones:** escape. Um yeah, perhaps, but I don't think it's exactly that, cuz it doesn't The footprint doesn't quite seem to match up, but that's what it's got on it, 320 and 2802. So, there's nothing else interesting uh to see there. If you

**Dave Jones:** do want to see the uh backside of that for those playing along at home, there's just lots more uh analoggy goodness, which goes with uh those op amps that we uh saw on the top, and those ones more

**Dave Jones:** of those digital buffers, and just a whole bunch of clamping and other stuff, and uh and EEPROM down here. And tucked away in here somewhere, which we didn't see, is uh the generator input uh and output. Um so, that's That's here. It's

**Dave Jones:** got gen It's got gen here, so I'm not sure where that's going off to, but uh there is an additional generator input and output which can actually handle uh microinverters uh in particular Enphase microinverters. So, I actually plan to

**Dave Jones:** put a couple of Enphase microinverters on the generator input, um which it'll actually keep those going when the grid uh fails, which is a really cool feature of these DIY inverters. So, yeah, without going into more detail here, I'm

**Dave Jones:** not sure and that's we haven't shown that on the topology thing here. So, as I said, the generator part actually comes out this way and goes around here like this and through these two relays here. We'll have a look at the brand of

**Dave Jones:** those in a minute. Once again, confirm that they're quality and that goes to our generator output connections here. But then how does that get to the grid? Of course, during normal operation when you're either supplying power from the

**Dave Jones:** battery or you're supplying power from the solar panels and the inverters going and all the energy is coming from your caps here, then yeah, you've got to connect that through to the grid and that's the job of this little beastie

**Dave Jones:** board here, which sits on there with once again two relays in series here. And the reason that they got two relays, that would be a regulation thing. I don't know. It might vary from country to country or something, but basically

**Dave Jones:** you don't want one of your cuz one of the failure modes of relays is for the contacts to arc over and permanently short. And well, you can come a cropper doing that. So, if you put two of them

**Dave Jones:** in series, you're less likely to have both of them short. So, you've got like a fail-safe system there. And we've got a current measurement transformer there for the grid output as well. And once again, they claim relays are the best in

**Dave Jones:** the business. Panasonic or maybe Hongfa. Which ones did we get? Yeah, you guessed it. Here they are. We got the Hongfas. So, yeah, none of that Panasonic rubbish in here. The finest that China has to offer. Not sure if you can see that

**Dave Jones:** though, but these ones are Zetler. So, that's interesting. Zetler aren't too shabby. So, I don't know why they didn't use the Hongfas there. And on the other board we got Hongfa as well. Diddled again. And then we've actually

**Dave Jones:** got another board which actually has the current transformer for the generator here. So, yeah, that's interesting. Once again, it connects to the load and it's got gen in and that's gen low. Do we have some large varistors there as well? But yeah, anyway, I'm not

**Dave Jones:** actually quite sure where this mounts in the system, where or how it mounts, but there's lots of cables inside here. As you saw in the previous video, there's just cables going everywhere and it's a really messy kind of build with things

**Dave Jones:** on different boards and things coming back and forth and between all the daughter boards and stuff. Yeah, it's a bit of a bit of a dog's breakfast. And we saw this board in the previous video cuz it's where your where your actual

**Dave Jones:** outside cables connect to for your generator, your load, your grid. And then these are not ethernet connectors. We've got RS485 can, then a meter interface and parallel one and two. So, there's no ethernet on this thing. It's got a Wi-Fi dongle which connects to the

**Dave Jones:** RS485 thing on the back panel here. And it's got various miscellaneous interfaces for current transformers and whatnot. That goes off to a little other board up here. What's that doing? Not entirely sure. DRM interface board or something. I

**Dave Jones:** don't know. Anyway, this is a very nice you know user interface board cuz the user can access this one through the removable front panel. They can't access the rest of the board. So, you've got to take it apart. It's got a very nice 50

**Dave Jones:** amp cutout switch here. So, this will just pop out if we get overcurrent. Once again, we've got extra current handling capacity on the traces here. They've used a mixture of these surface mount jobbies we've seen before, but they just

**Dave Jones:** they didn't want to do it there cuz they had to keep the spacing in there for the voltage clearances. I don't know why they didn't run some isolation slots in there maybe, you know, just for good measure. But some very chunky looking uh

**Dave Jones:** links in there And as well. So, yeah, it's all pretty groovy. So, a huge thanks to Phoenix from the uh EV blog forum. All the best people are on the EV blog forum. Seriously, if you're not on the EV blog forum, you're not in the

**Dave Jones:** business, really. Um and yeah, for he's a former uh solar inverter designer. So, yeah, he was able to um you know, pick out all this uh stuff right off the uh top of his head. It would have taken me quite uh

**Dave Jones:** sometimes. So, saved me quite a bit of work. Uh thank you very much. But, there you go. Um as always, these uh high-res photos are available on uh EVblog.com. So, go and uh check those out cuz uh when I do teardowns, I shoot high-res uh

**Dave Jones:** photos with my macro lens and everything. But, sorry, yeah, I can't get off this uh conformal coating to get, you know, all the pin numbers in the photos and things like that. Of course, if you don't want the hybrid

**Dave Jones:** topology, if you've just got your regular solar inverter, you won't have any of this uh stuff. You'll just have your uh PV Yeah, most, you know, like a simple solar inverter will just have a single PV input like this. So, you'll

**Dave Jones:** just have your H bridge. It may or may not have the Heric inverter uh depending on whether or not um they've, you know, paid the money to Fronius. Um and you know, it's just got some filtering and some sensing and some switching. There

**Dave Jones:** you go. Um that's it. It's pretty cool. So, yeah, these hybrid inverters aren't necessarily that much more complex. They've just got, you know, a bidirectional um DC-to-DC thing happening here and that just goes straight across the internal high

**Dave Jones:** voltage uh bus. So, that at night time, you can your battery, the energy that you've stored in here during the day, and that's all under software control uh from these uh you know, current sensors and the uh grid and the external grid

**Dave Jones:** current sense that you uh put when you install the thing, and all these, and it can so it can store energy in the battery, excess energy in the battery uh during the day, or you can set it um not

**Dave Jones:** excess battery. That's all firmware uh controllable. Uh and then at night, this can just pump this out and it simulates because it's across the same bus here, it just simulate you know, these PV inverters are switched off, this boost

**Dave Jones:** converter is all uh switched off, it's all isolated and these your inverter, your software, um your house doesn't know that whether it's being supplied, it doesn't care that it's being supplied from the battery here through this like that and that there or

**Dave Jones:** whether or not it comes from your solar array or it comes from this solar array, it doesn't matter. It's all the same thing as far as your uh house is concerned and as far as the inverters are concerned from, you know, this point

**Dave Jones:** here, it doesn't matter what the actual um source is, really. So, it's very cool. Hope you enjoyed enjoyed that uh rather lengthy video. If you did, please give it a big thumbs up and thank uh Phoenix down below as well and check out

**Dave Jones:** the EV blog forum. Catch you next time.
