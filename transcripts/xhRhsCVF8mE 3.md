---
video_id: xhRhsCVF8mE
title: EEVblog #1323 - PCB Layout Review & Analysis
url: https://www.youtube.com/watch?v=xhRhsCVF8mE
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 32, "3": 49, "4": 60, "5": 75, "6": 87, "7": 105, "8": 119, "9": 133, "10": 146, "11": 161, "12": 176, "13": 189, "14": 207, "15": 221, "16": 233, "17": 247, "18": 264, "19": 276, "20": 287, "21": 300, "22": 312, "23": 326, "24": 339, "25": 353, "26": 369, "27": 383, "28": 396, "29": 408, "30": 419, "31": 431, "32": 444, "33": 456, "34": 471, "35": 483, "36": 496, "37": 513, "38": 525, "39": 538, "40": 550, "41": 564, "42": 577, "43": 591, "44": 606, "45": 615, "46": 625, "47": 638, "48": 656, "49": 673, "50": 691, "51": 703, "52": 716, "53": 728, "54": 741, "55": 755, "56": 769, "57": 783, "58": 796, "59": 808, "60": 823, "61": 837, "62": 854, "63": 869, "64": 882, "65": 898, "66": 912, "67": 924, "68": 943, "69": 956, "70": 969, "71": 981, "72": 997, "73": 1012, "74": 1027, "75": 1041, "76": 1053, "77": 1067, "78": 1081, "79": 1095, "80": 1106, "81": 1119, "82": 1137, "83": 1154, "84": 1168, "85": 1182, "86": 1194, "87": 1207, "88": 1219, "89": 1235, "90": 1248, "91": 1260, "92": 1276, "93": 1289, "94": 1301, "95": 1316, "96": 1329, "97": 1344, "98": 1356, "99": 1374, "100": 1387, "101": 1400, "102": 1415, "103": 1427, "104": 1439, "105": 1454, "106": 1466, "107": 1479, "108": 1494, "109": 1511, "110": 1525, "111": 1537, "112": 1547, "113": 1561, "114": 1575, "115": 1589, "116": 1602, "117": 1613, "118": 1623, "119": 1638, "120": 1650, "121": 1667, "122": 1681, "123": 1696, "124": 1713, "125": 1723, "126": 1737, "127": 1752, "128": 1763, "129": 1777, "130": 1790, "131": 1806, "132": 1820, "133": 1836, "134": 1849, "135": 1862, "136": 1876, "137": 1889, "138": 1900, "139": 1914, "140": 1927, "141": 1940, "142": 1953, "143": 1967, "144": 1982, "145": 1995, "146": 2008, "147": 2021, "148": 2038, "149": 2055, "150": 2068, "151": 2079, "152": 2091, "153": 2106, "154": 2119, "155": 2134, "156": 2145, "157": 2160, "158": 2176, "159": 2187, "160": 2199, "161": 2210, "162": 2223}
---

**Dave Jones:** Hi, it's PCB layout review time again. Haven't done this in a while and this comes from the EV blog forum from forum user so FP G from Germany. Hi to all my German viewers and has got this project and

**Dave Jones:** wants some opinions on a layout and I thought, you know, it's probably an interesting example. So we might learn a thing or two here hopefully. So let's go through it. Now now what it is is basically an image sensor here. We've got an FPGA

**Dave Jones:** here which is a little mark 32 mark XO2 in a 32 pin QFN package here. And then we've got a little microcontroller up there. Don't know what that is. Don't care. Doesn't matter. And we've got a USB UART thing over here

**Dave Jones:** and a little buck converter over here. So this is not a finished layout. This is just like an in progress thing that he did just to you know, show like am I on the right track and he talked about

**Dave Jones:** stackups and things like that. Now I don't know the exact part used in here for this image sensor but look it's a little 20 pin BGA in here. 5 by 4 pins. The only equivalent pinout I could find

**Dave Jones:** for this on Digikey for example looks like it's the right business. I don't know like I don't actually have the Altium files to actually load in the proper thing. So we'll just go from the posted image but you know, this looks

**Dave Jones:** like it's one of these image sensor things. He says it's low low resolution like it's you know, like low end camera. So 640 by 480 you know, sounds pretty viable. So obviously doing some FPGA processing of the image taken from the

**Dave Jones:** sensor probably in real time doing some I don't know masking thing or running you know, some sort of image detection algorithm or open CV or one of those uh, you know, image algorithm type processing things and obviously the

**Dave Jones:** microcontroller here just drives that with the nice squared C line. But as I said, this layout is not finished. Um, so let's just talk about several things of like stack up and other issues to do with routing and component

**Dave Jones:** placement and stuff like that because these discussions are always quite interesting. So, let's go over and have a look at the board here. All right, so let's have a look here. Now, I'm not too concerned about the uh, buck converter

**Dave Jones:** here. That's not really what I'm after. I'm more in terms of, like, component component placement for bypassing and layer stack up and just other general things. But actually this layout for this buck converter looks really tight, by the way. I'll just

**Dave Jones:** mention it for a second. It's about keeping your loop area as small as possible. Um, and here's the bypass cap and you know, the traces are only small, so I wouldn't have done that. And what's that? What's that down in there?

**Dave Jones:** Oh, you don't want like, yeah, put a right angle in there with a chamfer. You don't need the chamfer. It's okay. Anyway, I'm not going to talk about the buck converter. Obviously, we've got a USB input over here and then an SO

**Dave Jones:** package UART, you know, serial converter. Looks like we have a trace length matched trace here for the UART input. You don't necessarily, like, the distance here here is so small, it's not going to really make a difference, but you know,

**Dave Jones:** yeah, if you want to do it, decent practice. I don't know why a everything else is surface mount on here except for the connectors and we've got a through hole crystal. Why? I just would have used a surface mount

**Dave Jones:** crystal. Anyway, okay, so let's start getting into the layout. Let's assume that, you know, the placement of the parts is exactly where they should be. Obviously, the image sensor goes in the middle and there's off this big and

**Dave Jones:** there's two big mounting holes and it's obviously you know some bigger assembly that's actually assembled on that. So we're assuming that's that can go under that or is it yeah cuz they're all on the top side so there has to be

**Dave Jones:** space under here cuz this shows this keepout for this module is like this. So I'm assuming that the components all fit under so assuming that's all okay. Let's just run with this. So just start with the USB UART chip here. You might think

**Dave Jones:** there's not much going on but and this is a four layer board and he said he had to go to four layers because of the couldn't really route out the five mil the five thou traces in between these

**Dave Jones:** pads in here. I'm going to assume he's got the pads fine. He's done the clearance rules and all that sort of stuff. He said he couldn't route those out on a two layer board using the JLCPCB manufacturing process and that's

**Dave Jones:** quite common. If you have a manufacturer in mind and they the four layer process tolerances might be different to the two layer process tolerances and that could be a thing. So you just don't get the you know you can't do five thou five

**Dave Jones:** thou on a two layer for example. I haven't checked that. Doesn't matter. Let's just assume that's been checked and we're going to a four layer. Now ordinarily a four layer board like this luxurious. It gives you plenty of

**Dave Jones:** options for like controlled impedance traces if you need it and you know good EMC and all sorts of stuff and routing flexibility and everything. Absolutely fantastic. So the first thing is the stack up which is one of which is the

**Dave Jones:** first question he posted in the forum. Now for a layout like this you might typically have power and you'd have power and ground in the middle and if you're running it looks like we've got some controlled impedance traces here.

**Dave Jones:** We'll talk about this shortly. If you got controlled impedance traces the microstrip on the top layer routing this is inner layer but anyway we'll get to that. Assuming it's on the top layer, then you would have then the next layer down. So, the top

**Dave Jones:** layer would be signal layer, your next layer down, the first inner layer would be your ground, and then the layer below that would be your power. You typically uh wouldn't put uh signal, power, and then ground. It's still okay, but it's not quite as good

**Dave Jones:** as having the ground directly under it. Uh because then it it changes your loop area bypassing and all sorts of stuff we won't go into. So, top signal layer, ground plane, power plane, and then bottom signal layer. And that's uh

**Dave Jones:** generally how you do it. Now, the first rule of this, as and and I see it over here, which we'll talk about in a second and several other uh places, is that you for a surface mount design like this,

**Dave Jones:** ideally, what you want to do is try and route as much as possible on the top layer. Uh so, you want to avoid any vias jumping down uh to the bottom layers and things like that. So, do as much as you

**Dave Jones:** can, choose your component placement, do as much as your routing as you can, all on the top layer. Only if you have to, then jump down to the bottom layer, or, you know, even one of the inner layers or

**Dave Jones:** something like that, then you would do that. So, anyway, so that's the thinking you should be going into when you're laying out a board like this. And he's clearly done that up here. Look, he's laid out this entire block up here,

**Dave Jones:** apart from this um input trace going up here on the bottom layer, which is fine. Um even though that could have been done on the top layer, look, that that could have been routed around there and across like that, and there's no reason for

**Dave Jones:** that tight tolerance against the edge of the board there. Um in fact, some of the component um components are quite uh close to the edge of board and has got rounded. I'm just going to assume that he wants a fully routed round edge

**Dave Jones:** board. Um there might be some, you know, fit to envelope reason for that, and that's fine. So, we won't question that at all. But, anyway, you can see that he's routed all of the signal traces all on the top without So, that's

**Dave Jones:** that's good. That's a reasonable buck converter layout. We won't worry about thickness of traces and actual, you know, like real tightness of the loop area and things like that. So, that's fine. So, he's obviously had that thinking up

**Dave Jones:** there and then it's good. But, you can see that that sort of thinking has like gone out the window here. Um look, these are like these are your serial. These are transmit and receive lines, okay? And it's immediately like

**Dave Jones:** jumped to the bottom layer here. Like, why? Why wouldn't you try and route and why wouldn't you try and route your signal layers on the top like that? So, I would typically you would reserve um your top signal layer for your signal

**Dave Jones:** traces. And then, if you need, you know, I okay, this can't get through here because this power trace is going down here like this. But, you then you could say that well, all of your power traces like, you know, these ones and

**Dave Jones:** everything else, they should probably be on the bottom layer, for example, the bottom signal traces and then just pop up with a via there to, you know, to come up. And then you've got all this routing room going through here like

**Dave Jones:** this to, uh you know, get your signals over. So, really there was no need to drop that down there. And, you know, I I know this like the board's going to work either way. It doesn't matter. This is

**Dave Jones:** not a complex route. It's more just getting in a good mindset of laying it out. So, when you have to do a larger, a bigger, more complicated board, you're not going to come a cropper later um by, you know, routing your power

**Dave Jones:** paths like this. In fact, on a board like this, you'd be routing all your signal traces first and then doing power later except for the bypassing here and uh over here, which we'll talk about. I just moved my floating Dave head here

**Dave Jones:** so it's like over that box anyway. All right, let's get back into it. Right, so let's assume that all the chips are placed like this. I mean this one at at a diagonal. This is a common uh technique if you're to mount your

**Dave Jones:** chip at 45° like that. Don't worry about doing that. The pick and place machines can handle that uh just fine. There's no worries doing that. And for uh square packages like, you know, quad flat packs and uh QFPs like this one. If your chip

**Dave Jones:** was down right against the board, say you had like, you know, a your chip down there like that, then you wouldn't be able to get all the pins out of the bottom in here. You'd run out of routing

**Dave Jones:** room. So, it's common to turn them 45°. You'll see that on large PCBs like graphics cards and and like specially the older school graphics cards and things like that. You'll see like the main graphic uh chip with, you know, a

**Dave Jones:** big old school quad flat pack with, you know, hundreds of pins is just rotated 45 uh degrees. It just allows you to get your traces out at a, you know, a more reasonable angle. There's just more routing rooms. So, anyway, after you've

**Dave Jones:** placed your chips like this, it's probably worthwhile placing your bypass capacitors because they're going to be important. And there's a bit of discussion about this on the forum and the criticality of bypass capacitors. And if we actually go into here uh for

**Dave Jones:** the MachXO uh Lattice FPGA, Lattice have a specific power decoupling and bypass filtering for their programmable logic devices. And because this is a little kind of piss-ant FPGA, it's not, you know, a little piss-weak thing. Um it doesn't require, you know, massive

**Dave Jones:** amounts of decoupling. Uh it's only got two VCC pins plus uh VCCIO. So, you know, really VCC, you only need like this is not a big grunty FPGA. It's not going to take huge gulps of current like when you power the thing up uh which

**Dave Jones:** some of your real big grunty FPGAs can, and then you need massive amounts of bypassing and it's real critical and all sorts of stuff. Um, in in this particular case, like, uh, Lattice, you know, they recommend very the use of .1,

**Dave Jones:** uh, you know, well, 100 n, 10 n caps, uh, per device power pin is a good rule of thumb. So, it's it's not critical, and of course I've talked about this as well. Beware of ESR and self-resonant frequencies, but you don't know that

**Dave Jones:** unless you have the specific simulation tools, and we won't go into that. For a little piece, uh, weak FPGA like this, you just like, you know, just I I'd just whack like, you know, one or two one microfarad capacitors. Wouldn't even

**Dave Jones:** bother with any .1s or anything like that, or any 10 n higher frequency ones. I'd just whack one large bulk decoupling, uh, cap through there, really. And it's, you know, they say it's going to eliminate the low frequency, uh, stuff. It's going to do

**Dave Jones:** the high frequency stuff, too. You know, generally, maybe you might put a, you know, a 10 n on there if you you really want to, but anyway, this is not a critical design where, uh, bypassing is going to matter. We're

**Dave Jones:** talking about a tiny FPGA like this, um, and the image sensor, I don't know. I haven't looked I haven't don't have the full data sheet for that. We've only got like a little brochure, um, kind of thing. And, uh, these uh, bypass caps

**Dave Jones:** are quite large, by the way. What are they? Um, like they look like 0805 size with a large pad or something like that. Beauty. I don't hate those you know, like 0402 rubbish or something like that. Only if you have to. Anyway, so,

**Dave Jones:** this is one of the main things I wanted to talk about with this design is the layout of these bypass caps, uh, here and here, but in particular, the image sensor. This struck me. This is the first thing I noticed when I glanced at

**Dave Jones:** this image. I went, "What? These are the bypass caps? He hasn't done any of the ground yet." This is obviously the ground side. This is the ground side. This is the ground side. Haven't stitched those through yet, which you

**Dave Jones:** should, by the way, Uh, um just as a uh tip. When you're placing bypass caps and you're routing them in there as a first step, put in the uh via or vias you need for the ground and the power and things like that.

**Dave Jones:** Route those in because then you'll know exactly how much room you've got to route out all of your signal traces out of here like this. Okay? So, the first thing I notice is why on earth is this trace running around here like this?

**Dave Jones:** This is the bypass capacitor. This is the bypass capacitor for this pin here. Wow. And this bypass cap is for this pin here. And this bypass cap is for this pin here. And like and this bypass cap is for this pin here. It's

**Dave Jones:** all It's almost as if they've all been rotated like they they should all be rotated like 90° like this. And this is one of the issues that you have. Like you might uh your schematic, of course, when you uh

**Dave Jones:** draw your schematic and you put a bypass capacitor per pin, it'll be C1, C2, C3, C4. And then when you when it automatically imports those onto your PCB, then you might go, "Oh, I'll just place the caps anywhere." And then the

**Dave Jones:** your netlist will tell you, "Okay, this connects through to here." And you go, "Oh, okay. I've got to run a trace all the way." No. This is where you have to think from the get-go that component placement is everything. So, especially in regards

**Dave Jones:** to bypass capacitors, just like this buck converter up here, you have to get what's called a small loop area. And that is the area from say this power pin here, okay? This has to go through this trace here.

**Dave Jones:** And that has to go through the capacitor, through some vias here to the ground plane, and then back to the ground pin on the chip. I'm not sure which is the ground pin on the chip, right? But it's got to go through

**Dave Jones:** and that is your total loop area, it's called, okay? And the larger your loop area, I've done videos on this, the greater your EMC uh you know, issues in terms of like radiation and immunity as well. So, the larger the

**Dave Jones:** loop area, the more problems you're going to have. So, you want to minimize that. So, this capacitor So, this pin here, let's say if we're bypassing this one, it should be this bypass capacitor here. And if it doesn't match the schematic,

**Dave Jones:** well, move it away and move this one here. So, that this this pad here is right next to here. Like this this amount of distance is fine, you know, it's neither here nor there. So, you simply route that directly

**Dave Jones:** through to there and then it goes through and it goes through to the power pin. You see how much smaller that loop area will be? And if you take this example up here, which is absolutely enormous, look at

**Dave Jones:** this. This loop area is massive. And that goes through Well, goes through your ground pin and up to here. Like it's an absolutely enormous loop area. You may as well not even have the bypass capacitor in that case, really. It could

**Dave Jones:** even do more harm than good. So, yeah, really. Yeah, I would you know, dedicate it if you want to have four bypass caps for this image sensor, that's just fine. Just tie that one to there, tie this one to here,

**Dave Jones:** tie this one to There's nothing on that side, is there? Then I would have put So, I would have I'd move this one down to here, down under here. So, I'd have one like that and another one like that and then run

**Dave Jones:** the trace directly down to the chips and then straight through vias. I'd whack a via in there, two if you want, you know, if you're really really fussy. But yeah, a via there directly down to the ground plane, which is the

**Dave Jones:** layer just below it. And then, you'll have the optimized small loop area for your bypassing. And then, you've got the same thing going on over here. This one's a bit This one's a bit more awkward, but okay. Look, this is the

**Dave Jones:** bypass capacitor for this pin. Okay? So, that's exactly where I'd put it. I probably would have flipped it out that way just so that you could route those traces out cuz, look, right? You've already cornered yourself in here,

**Dave Jones:** right? We By putting this here, you've and putting all these power traces in here like this, you've instantly created a bottleneck where you have no choice but to route this out through this via here and here and drop down to the

**Dave Jones:** bottom layer. There's no need to constrain constrain yourself like that. So, I would simply flip this capacitor and just move it in that direction there and have the ground pad over here, for example. And then, you can get your

**Dave Jones:** traces out like that. And then, route your power traces on the bottom layer. Well, actually, by bottom layer uh because we've got a four-layer board, we would have a power plane. So, you can use the internal power plane. That can

**Dave Jones:** either be a split power plane. I won't get into the intricacies of split power planes and split grounds and things like that. Let's just, you know, and power plane usually shouldn't be a problem cuz when you start to split your grounds up and

**Dave Jones:** things like that, that can be generally speaking be an issue. And once again, this power trace over here, it's instantly cut out all of these two two four six traces like the seven traces. Okay? The seven traces that had

**Dave Jones:** to be routed out here, so you've prioritized one lousy power trace for against seven signal traces. And now, you're forced because you put that power trace in there, you're forced to drop all seven like this down to the

**Dave Jones:** bottom layer. Now, uh so you so you wouldn't make that sacrifice. This is why I said route signal layers first and then worry about your power later, especially when you got the flexibility of a four-layer board. But now I realize why he might

**Dave Jones:** have done this. You see, we've got wiggle wiggle wiggle yeah traces on here. These are to match the length. So this trace here matches the length of the one next to it. Now, you can argue whether or not that is required. I don't

**Dave Jones:** think that's required in this case. It might be required if you got a real high-speed MIPI interface, for example, but I don't think this is a MIPI a high-speed MIPI sensor. It's just a low-end 640 by 480. It uses the serial

**Dave Jones:** digital interface system. Oh no, sorry. This is a parallel one. Sorry, now I was looking at another one. This is like an 8-bit parallel output. You know, if you want to match the lengths and just because that's that's fine. And generally speaking

**Dave Jones:** though, you don't want to waste time uh like over-engineering something if it doesn't matter. If you want to you know, muck around with your trace lengths and things like that. I know the tools can do them automatically and things like

**Dave Jones:** that and it's it doesn't cost you a huge amount of time. But anyway, um let's not worry about why the traces are matched like this. What uh what he might be trying to do here, let's assume that you do let match the

**Dave Jones:** trace lengths like this. You might want to match also the impedance of things. So you might be doing a controlled impedance. But these aren't controlled impedance wouldn't be a thing for this particular design. But if it was, let's

**Dave Jones:** let's just assume if it was. Here's a Saturn PCB calculator. This is a microstrip one where you've got the trace Oh, sorry. I can't draw on that. You've got the trace on the top layer and then the ground plane underneath.

**Dave Jones:** And that's a controlled impedance trace. Now, the one in the middle where it's actually dropped through to one of the middle layers here cuz the bottom layer is blue and the mid layer is the mid layer which should be a ground

**Dave Jones:** plane or and or power plane. You could run these on the power plane for example. Like you you might want to run what's called a strip line like this which has a ground plane up here, a ground plane up here and your uh signal

**Dave Jones:** is sandwiched in the middle. Now, I won't go into the pros and cons of strip line versus micro strip. It doesn't matter but that might be one of the reasons that you do that. But in this case, there's absolutely no reason

**Dave Jones:** to be running to use one of your internal layers to uh do that. So, yeah, I I don't know what's going on there. Right, I I would have simply I would have run all of these traces directly over there. Trace length match them if

**Dave Jones:** you want. Um I wouldn't have added this much wiggle in but yeah, I would trace length match uh trace length match those. In fact, actually the I was going to say I would have chosen the location and the layout

**Dave Jones:** the rotation of the FPGA here to match the shortest possible paths over to here. But anyway, um so yeah, it looks like we got these three pins here which have to go out. That's just yeah, another one over here. Is that another

**Dave Jones:** one? I don't know. So yeah, like there's a combination. Look, what like this one here is going on the blue. That's going on the bottom layer. So you have that on the bottom layer, this on the inner layer. No. You want to follow that you

**Dave Jones:** know, re- shoot for that holy grail of PCB layout goodness by having all your signal traces on the same layer if you can do it. Avoid links. Holy grail of like single-sided PCB layout for example which SMD layout design essentially is.

**Dave Jones:** You're doing it like a single-sided design and then filling in the rest, you know, as I said like the power and other stuff uh with your other layers as required, but you're essentially trying to shoot back to old-school single-sided

**Dave Jones:** PCB design with SM uh D components because they're not through-hole components. You don't have the luxury of essentially a via for every single pin. So, really so that's the holy grail. So, I would have simply routed all of these

**Dave Jones:** as much as I could as many as I could on the top layer. That would have been my first priority for this layout. Once I've chosen the location of my chips and I've bypassing around here and I've dropped the bypassing down to the power

**Dave Jones:** and ground uh layers, then we we would have a whole bunch of empty space all in here and I would have routed out all of the critical data lines and the clock lines and and control lines and things

**Dave Jones:** like that. And you'll find that once you get rid of this power trace, get rid of this power trace here, you know, maybe you might want to instead of having the capacitor like that, you might have it like that for example, or you know, up

**Dave Jones:** here uh for example, you'd have all this room in here completely free to route your traces across like that. And that's, you know, you want to prioritize traces, especially if they're critical like potentially they could be if you

**Dave Jones:** had like a real high-speed high-end image sensor with, you know, you might have might have to trace lengths and as I said controlled impedance maybe or you got some other thing you're running your DDR memory or whatever you're doing.

**Dave Jones:** And you know, things can get a little bit critical. So, yeah, um rather than just like use vias just to drop everything down, like I should you should not be unless you're absolutely at wit's end and you've run out of

**Dave Jones:** space, you shouldn't be running. So, we've got yeah, 1 2 3 4 5 6 7 8 9. Yes, there's nine trace length matched uh layers. So, that's eight data lines plus the clock or something like that. That's all good, but look, I mean,

**Dave Jones:** you've got something like this, right? You've got this blue trace, wiggle wiggle wiggle yeah, over to here, jumping up through a via onto a middle layer, over to here, and back down to the bottom layer. Up here and where does it go to? Does it

**Dave Jones:** go to there? No, where where does it Is that Oh, anyway, you know, it goes up there. There's no reason to jump this through a signal layer through multiple layers like that. Only you know, a large design you're getting right at the end.

**Dave Jones:** You're you're with Sandy. You can't possibly get you've been working a week on this layout. You can't possibly fit this last trace in. That's when you got to go, you know, crazy buggers. Um, which by the end of the layout by the

**Dave Jones:** way, you should only be left with non-critical traces. You should be routing all of your critical traces first as a priority. So, as I said, all the data lines, all the important data lines, all the important clock and

**Dave Jones:** control lines, and the rest, which is miscellaneous stuff like this, for example, this uh microcontroller up here is obviously controlling this the I squared C on this chip. It's got like an I squared C communication interface, which is where you set up all the

**Dave Jones:** parameters and, you know, things like that and data rates and, you know, whatever you set up in the sensor. So, there's two two wires going over here. And look. Look at how this is going, right? This is Look at I I hate these chips. Like

**Dave Jones:** that's a pad on the corner. Evil. Evil. Anyway, um yeah, look, it's going over here and then it's jumping on the to the inner layer and then it's going over here, and then it's jumping to the bottom layer, and

**Dave Jones:** then it's going back to the inner layer, over here, back to the bottom layer, back to the inner layer, and over to here. Wow. Like for starters, I could have continued to run that on the top on the

**Dave Jones:** top on the top on the top on the top on the top and did like, you know, like So, yeah, like jumping layers when there's no need to. Um now, of course, because you've got to you pri- you would

**Dave Jones:** have prioritized all of your data lines coming over like this on the top layer, you know, you would have run this around the backside cuz an I squared C line can be as long as you like, doesn't matter,

**Dave Jones:** it's not critical. And if it longer it gets, you just lower the pull down resistor by the way to counteract the extra capacitance of the line, especially if it's a very long trace over ground plane or something like that. Anyway, so yeah, so I would

**Dave Jones:** have taken These are the two I squared C lines. I would have taken just both of the wires going Yeah, yeah, yeah, yeah, over to here. Okay, so it's a little bit annoying. I think it's Yeah, okay. So it's these two pins here.

**Dave Jones:** So that's annoying. Um, but it's only two lines. So yeah, I would have like Maybe you could have said, "Okay, oh, no." See, if you just dropped a via from your uh bypass cap down to your power layer, you would have

**Dave Jones:** room potentially, but all your data layers are So yeah, all your data pins would be routed out like that. So that's kind of annoying and these two are just stuck in here. These In this case, you'd route this last. And

**Dave Jones:** because they're low priority lines, you would route them last, you know, they're non-critical. So yeah, you might drop those down to the bottom layer and then just have bottom layer going straight over there like that. But potentially you could have done it on the top, but I

**Dave Jones:** doubt it because you've got to get some of these around here anyway. So offhand, we've got all these vias here. Like count how many vias we've got. I reckon we could have got away with not not counting the bypass caps,

**Dave Jones:** we could have got away with a couple of vias there, you know, three, four vias, something like that total as opposed to all these sort of stuff. And we would have lowered our loop area if we had our

**Dave Jones:** bypass cap going directly in here and a via here going directly down to the ground plane below it, and Bob's your uncle. So, yeah, and you can just see all the all the messy business going on with all these power traces here, and

**Dave Jones:** then, you know, once again, the same thing. You've boxed yourself in here, and you've got no option but to drop these four signal lines down to the bottom layer, and then route them out like this. I I would have pulled these

**Dave Jones:** two lines early in the process, even though they're not critical. Early in the process, I would have gone, "Okay." Both of them so Assume these are both lines. Let's do a larger trace, right? Both lines like this, I just would have

**Dave Jones:** routed those around the bottom there, and up to there. Is that where they're going? Anyway, I would have like routed that first. Um, you know, oh, well, you know, fairly early on in the design uh process. Just get those over, and anything that needs

**Dave Jones:** power, then I would have, you know, well, you would have had the bypass caps done already, but anyway, but the fact that you snaked all of these power traces around here, don't do that. The top layer should be for signal traces.

**Dave Jones:** So, this just looks like your JTAG interface here for your um FPGA, and like these traces here are going I can see those. They're going off to yeah, various ones. I mean, look, you've got this this pin here dropping to the lower

**Dave Jones:** layer, going around like this Oh, no, it's not that one. It's that one. It's that one there dropping, going around like that, up here, around here, around here like that. I mean, huh? Why? Um, you when you could have just, as a

**Dave Jones:** priority, routed that straight directly in like that. I mean, you know, these bypass caps don't have to be here. I mean, this this FPGA, you could have like Yeah, once again, like I wouldn't have rotated that 45°. Maybe I

**Dave Jones:** would have put it maybe, you know, there. Something like that, perhaps. I don't know. Um, yeah, it's neither here nor there. Yeah, but the point is is that uh yeah, all power traces on the chop just don't do

**Dave Jones:** that. Um, it's just it kills all your routing room and leaves you zero flexibility and forces you to go on other internal layers and things like that. And uh unless you absolutely need to, you would not be running traces on

**Dave Jones:** the internal layers. Uh why? Because you want to dedicate them to a solid power and ground plane if uh possible from a signal integrity point of view, uh EMC, and all that, it's better to have solid uh power and ground planes. And two, you

**Dave Jones:** can't like check the traces. You can't uh cut them. You can't mod them. You can't, you know, do anything like that if you're dropping them down to the middle uh layer. So, yeah, it's it's just much nicer and you can't follow

**Dave Jones:** them when you you know, if people have to like you know, repair, debug the board like that, you can't follow internal traces and things like that. It's just unless you absolutely have to, and you wouldn't have to on a four-layer

**Dave Jones:** board like this with just like what, you know, four chips on it, um no, you'd be looking to get 90% of this layout on the top layer. All of your signal traces on the top layer. 5 or 10% tops might drop

**Dave Jones:** down to the bottom layer. You'd have no signal traces on the inner layer. And there'd be no even if you were needed high-speed signal integrity, as I said, you would go for uh your microstrip, which is uh the controlled

**Dave Jones:** impedance on the top trace and the ground plane underneath. Or you can do it on the bottom layer, uh for example, but then you'd have to swap your you'd have to trade off the ground plane on a lower layer. Or you could uh you might

**Dave Jones:** want have two, you know, like I've like the odd design, you might go with two grounds in the middle and then run your if your power requirements is simplistic, which they are for this design, you might run your power on your

**Dave Jones:** top and bottom uh for example, you might have like some flood fill power top and bottom. Yeah, I wouldn't say I've never seen or done that in specific circumstances, but generally no. Power and ground in the middle layers and with

**Dave Jones:** especially with this FPGA which only needs the one power rail which is a yeah, 2.8 volts. There it is. For the No, 2.8 volts is for the image sensor. So, I think three 3.0 it might be running the micro from this Is it the

**Dave Jones:** same? Yeah, it's it's the same power. Yeah. Yeah, yeah, yeah. Yeah, it's the same power. And in terms of power distribution, look at this, right? Here's our output. I don't know why you'd run it like that and then around like you would just run

**Dave Jones:** it straight into there like that, okay? You would have Well, you'd run it into your cap, okay? Cuz you the capacitor here, this is your output capacitor. This is the inductor, okay? Of your switching regulator. This is your output

**Dave Jones:** capacitor. So, this becomes your star ground and then you would have a trace running out there power this chip. You'd have a trace running out here to power your image sensor. You'd have a trace running out here to power your

**Dave Jones:** microcontroller. You'd have another trace running out here to power your FPGA. And, you know, you might run those on the bottom layer, but that's only if your electrical circuit requirements dictated that you have a star grounding sort of thing. But, for something like

**Dave Jones:** this, we could just floodfill the inner layer, the second layer from the bottom would be our you know, the entire thing would just be floodfilled with our 4.0 2.8 volt rail there. And then it just drops a via, you know, anywhere it needs

**Dave Jones:** to down to the power plane. So, you then you don't have to worry about star grounding. But then, you wouldn't run any tra- any power traces at all down here. You would just stitch it straight down there. Now, I could waffle on about

**Dave Jones:** all this for ages. I think I'll stop. I think I've covered sort of most things that I wanted to talk about here. But yeah, you can go in-depth down the rabbit hole. Now, this design is not that critical. It's not high speed. Yes,

**Dave Jones:** I know about signal edge rates and all that sort of stuff, but like it's like the requirements for the performance requirements in terms of layout for something like this, even though it has an FPGA and people say, "Oh, you got to

**Dave Jones:** bypassing requirements in FPGA are ridiculous." No, this is a piss ant little FPGA. It has a single rail. It has hardly any, you know, power on surge requirements or anything like that. Like something like this, two bypass caps

**Dave Jones:** would more than do it. You could Anyway, I've done the months in video about how some bypass caps aren't even needed. So, yeah, you might get away with one. It depends where the power pins are. If they're like here and here, like you

**Dave Jones:** might get away with one bypass cap for your core voltage, your VCC, and maybe another bypass cap for your IO voltages. For example, and your IO IO voltages might have been different to your core voltage. For example, you

**Dave Jones:** might be running your core voltage at a lower voltage. In this case, we're only got the single 2.8 volts. So, the requirements for this, no, it's one big ground plane. I wouldn't have any power traces on here at all.

**Dave Jones:** Take priority over the critical signals first and then route your miscellaneous stuff like your I²C later and and your JTAG interface down here. Route all those last and you know, things like that. And then you wouldn't have to use

**Dave Jones:** all these vias all over the place like this. So, yeah. Shoot for the holy grail of a single-sided layout every time you do an SMD layout. So, anyway, I hope that's helped the OP there and helped some others with some general advice. I've

**Dave Jones:** done lots of videos like this over the years of general like layout advice and stuff like this. But if you like this sort of discussion and like a look at sort of critique of design, even though this wasn't

**Dave Jones:** finished. But yeah, I thought this was just an interesting example which you know brings up a couple of interesting points about layout. So I hope you found it useful. If you did, give it a big thumbs up. As always, discuss it down

**Dave Jones:** below in the comments and let me know what you think about the green screen talking head thing. I think it's better. I think it's better. I know there's some green fringe and if I move quickly, you can see the see the green halo and stuff

**Dave Jones:** like that. Lighting in here is not perfect, but I I think the green screen talking head works. I've been doing YouTube professionally for almost 10 years now. It's the first time I've got a green screen. It's got to be some kind of record.

**Dave Jones:** Anyway, catch you next time.
