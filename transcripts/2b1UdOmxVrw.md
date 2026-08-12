---
video_id: 2b1UdOmxVrw
title: EEVblog #244 - How To Lay Out A PCB - PSU Design Part 9
url: https://www.youtube.com/watch?v=2b1UdOmxVrw
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 28, "3": 44, "4": 58, "5": 69, "6": 83, "7": 97, "8": 114, "9": 128, "10": 143, "11": 157, "12": 171, "13": 184, "14": 203, "15": 220, "16": 233, "17": 247, "18": 261, "19": 274, "20": 285, "21": 292, "22": 308, "23": 318, "24": 336, "25": 349, "26": 361, "27": 378, "28": 392, "29": 405, "30": 418, "31": 430, "32": 444, "33": 457, "34": 472, "35": 484, "36": 495, "37": 509, "38": 521, "39": 535, "40": 552, "41": 567, "42": 580, "43": 593, "44": 608, "45": 623, "46": 636, "47": 652, "48": 665, "49": 683, "50": 696, "51": 708, "52": 721, "53": 736, "54": 754, "55": 766, "56": 779, "57": 794, "58": 810, "59": 825, "60": 840, "61": 852, "62": 866, "63": 879, "64": 894, "65": 908, "66": 921, "67": 935, "68": 947, "69": 963, "70": 975, "71": 988, "72": 1001, "73": 1014, "74": 1024, "75": 1039, "76": 1056, "77": 1070, "78": 1084, "79": 1097, "80": 1112, "81": 1127, "82": 1142, "83": 1155, "84": 1170, "85": 1184, "86": 1199, "87": 1213, "88": 1230, "89": 1243, "90": 1258, "91": 1271, "92": 1284, "93": 1296, "94": 1311, "95": 1322, "96": 1335, "97": 1351, "98": 1364, "99": 1376, "100": 1385, "101": 1400, "102": 1413, "103": 1429, "104": 1446, "105": 1461, "106": 1474, "107": 1486, "108": 1499, "109": 1514, "110": 1529, "111": 1546, "112": 1563, "113": 1579, "114": 1595, "115": 1609, "116": 1623, "117": 1636, "118": 1649, "119": 1664, "120": 1680, "121": 1696, "122": 1716, "123": 1732, "124": 1744, "125": 1758, "126": 1772, "127": 1783, "128": 1793, "129": 1806, "130": 1820, "131": 1837, "132": 1851, "133": 1864, "134": 1881, "135": 1896, "136": 1911, "137": 1927, "138": 1940, "139": 1952, "140": 1971, "141": 1984, "142": 1998, "143": 2012, "144": 2026, "145": 2041, "146": 2055, "147": 2071, "148": 2087, "149": 2101, "150": 2116, "151": 2126, "152": 2142, "153": 2156, "154": 2172, "155": 2185, "156": 2199, "157": 2219, "158": 2231, "159": 2245, "160": 2259, "161": 2274, "162": 2288, "163": 2303, "164": 2317, "165": 2332, "166": 2347, "167": 2360, "168": 2371, "169": 2384, "170": 2398, "171": 2414, "172": 2427, "173": 2442, "174": 2457, "175": 2474, "176": 2488, "177": 2503, "178": 2519, "179": 2533, "180": 2547, "181": 2561, "182": 2572, "183": 2584, "184": 2600, "185": 2614, "186": 2629, "187": 2643, "188": 2657, "189": 2669, "190": 2682, "191": 2693, "192": 2706, "193": 2717, "194": 2730, "195": 2743, "196": 2756, "197": 2768, "198": 2781, "199": 2794, "200": 2809, "201": 2824, "202": 2839, "203": 2853, "204": 2867, "205": 2881}
---

**Dave Jones:** Hi. Now, there were quite a lot of people who wanted me to take them through my PCB layout of this power supply board, and that's exactly what I'm going to do here. While I was laying out this board, I did actually uh

**Dave Jones:** capture it in real time. So, what I plan to do here is actually play that back, the complete recording of laying out the board at uh times 10 speed, and adding some commentary on top of that of how I

**Dave Jones:** was laying it out, what I was thinking, and the processes and things like that. So, let's get on to it. Now, before anybody asks, the package I'm using here is Altium Designer, okay? Say no more. That's the package I'm

**Dave Jones:** using. Yes, it's very expensive. I'm aware of that, but that's the tool I've used for 20 years. So, uh here we go. Now, the board um itself, when I'm actually uh setting this up, I've already done the outline

**Dave Jones:** of the board. That is actually the first step I'm going to do when I start laying out a board is to do the outline of it. And this is based on the box. I know I haven't done a video uh

**Dave Jones:** outline the system design and the case it's actually going into, but the template of the PCB uh that you'll see here in black, the um the black background, that is already defined as the outline of my board with the little

**Dave Jones:** cutouts required and things like that. So, uh that's the first step you're going to want to do to a board, as well as setting up your uh placement grids. Now, I've already uh done this because this is a through-hole design, instead

**Dave Jones:** of surface mount. Most of my components are on an imperial uh 0.1 in uh grid. So, what I'm going to do is set my uh grids both uh a component grid and a uh snap grid, as well. I'm going

**Dave Jones:** to set the snap grid to uh 50 mil or 50 thou. It's the same thing. Thou means mil. I'll probably use these sort of terms interchangeably throughout the video. I do tend to use both. So, mil is not millimeters.

**Dave Jones:** Mil is thou, 1/1000 of an inch. So, because the components are things like DIP packages are on a 100 thou or 0.1 inch grid, I'm going to set my snap grid to half that value when I'm routing. Maybe

**Dave Jones:** drop that snap grid down to 25 thou or something like that. And the reason you want a multiple of this is so that your tracks when you take them between pins of your IC go smack bang through the center. And

**Dave Jones:** if you try and lay out an imperial board like this uh instead of a metric board, which is what new surface mount components use, if you used a metric grid with imperial components, you're going to end up with

**Dave Jones:** the tracks not go quite going through the centerings or going to get a bit messy. But, I went on designing and laying out a board like this. I You have to. You're forced to use both imperial and metric

**Dave Jones:** dimensions because I will use metric for things like whole sizes. I'll use 0.8 mm hole instead of X amount of thou. So, I'll also use metric for the dimensions of the board and possibly placing components and the center of components and things like

**Dave Jones:** that. So, when I'm dragging around my components, I will actually I might switch to a metric grid instead of my imperial grid so that a lot of the components themselves, especially on the front panel components, when you're lining them up,

**Dave Jones:** they will be on a metric grid. So, I've already set these things up in the background and I've dumped all my components down because it's a very important step to get your schematic and all your footprints correct in your

**Dave Jones:** libraries as a first step and then dump them all onto your board. So, that's what you'll see here. I've started off. I didn't capture this process on video, unfortunately, but what you'll see when I start out here, I've got a blank board

**Dave Jones:** that has the outline already done. I've placed some of the components around the edges because it's in very important. The first thing you want to do is place those fixed components that poke out your front panel on the edges

**Dave Jones:** of your board, your connectors, your switches, your you know, all sorts of things like that. You want those to be exactly where you want them on the edge of the board and then you fix them, you lock them in place and then your

**Dave Jones:** components can that's when you start to get to the art of PCB design is where do you put your components? How do you lay them out? How do you which area of the board do you put them in? And so on. So,

**Dave Jones:** I've already done that. I've placed the components around the outside. So, let's get into it.

**Dave Jones:** All right, here we are. We've got our main schematic, of course, and I've dumped down all the components, as I've said, and you'll see the menus are flash up. Sorry, I can't actually slow this thing down as I'm actually recording this

**Dave Jones:** audio narration on top of it, but as you can see what I'm doing around at the top of the screen there is I'm moving the heat sink around now. I'm playing and at the moment I'm getting that power

**Dave Jones:** connector. There's that 2.5 mm sorry, 5 mm DC power jack and I'm just mucking around that top area of the board there just to make sure I've got that power connector on the side I want. And I'm also

**Dave Jones:** thinking about the system design at this point cuz I still don't have a complete idea in my mind about where everything's going to go and how it's all going to work. And this will actually um evolve as I lay out the

**Dave Jones:** board cuz a lot of this might be dependent upon you know things I see when I'm laying out. So what I'm doing now is I'm placing down the power traces there from the um there I think close to

**Dave Jones:** 100 thou wide 80 thou really big beefy power tracks from the DC input jack and you'll notice all these wires actually connecting all the components that I've dumped down there. The Altium Designer the program has just done this for me it's it's dumped all

**Dave Jones:** the components down and they're actually net wise they're called from twos in Altium. Speaking other packages they might be called you know a rubber nets rubber banded nets highlights like that. Now what I'm doing here this is a key

**Dave Jones:** part of laying out a board. You'll notice that I started to group together functional components functional block and if you got the schematic and you're playing along at home here you'll you'll see that I've divided the schematic into these

**Dave Jones:** functional blocks and that's what I've started laying out here is I've started laying out just that functional block. I've moved in the components. I'm doing this outside of the area of the board. That's another key thing. I'm doing this

**Dave Jones:** out in the dead area and when I've laid out this little subsection of the circuit I then I will take that highlight it all and then drag it into the board somewhere as a little module. So I'm developing this thing as a

**Dave Jones:** module. You'll notice the one I'm laying out now is actually there's the MOSFET that's this is the micro current part of the circuit. So that's its own little module and there's the drive transistor and there's the base resistor for the or the pull up

**Dave Jones:** resistor or whatever for that that little micro current part of the circuit. And if your circuit is modular like this then that's what you're going to want to do. And here are the current shunt resistors all 10 of them in

**Dave Jones:** parallel there and once again you'll notice that the location of those 10 parallel resistors will change later as the board evolves and I move things around, but that's where I put them for starters because it was it seemed like a

**Dave Jones:** convenient location. It was down near the power switch on the front panel. The front panel is actually the bottom of the board to give you some orientation. The front panel, the lower the bottom section of the board is the

**Dave Jones:** front panel, the top half is the heat sink. That's going to be the back of the project. And if you're not that familiar with PCBs, you always do it looking down from the top or through the board. So,

**Dave Jones:** even when you're laying tracks on the bottom layer, which I'm not actually, the tracks I'm laying down at the moment are on all on the top. So, red will be the color red traces will means the top layer and any

**Dave Jones:** traces you see in blue will be on the bottom layer. Now, my goal is to actually with a double-sided board like this, there's only two layers on this board. What I want to do, what I'm trying to do here and what you'll see is

**Dave Jones:** all the traces are in red. You won't see me for a quite a long time in this video actually put any traces on the bottom layer because I want to try and add all of these traces onto the top layer of the board. So, I'm

**Dave Jones:** effectively routing this board as a single-sided layout at the moment and and just keeping that bottom side free for possibly any last-minute tracks, power tracks, and a big ground plane that I can put all over the bottom of

**Dave Jones:** the board and ideally for a double-sided board like this, you'll notice that I've dragged I've dragged and dropped the that subsection up in the top left-hand corner of the board there. There we go. I just moved the power I just moved the

**Dave Jones:** sorry, the current shunt resistors, those 10 current shunt resistors there. There's my current amplifier U7, which is going to be right next to the current shunt resistors because it's the current sense amplifier, so it has to be right

**Dave Jones:** next to the resistors. You can't have those traces going all the way across the board. Uh the bypass caps are going to be near those caps. This uh plate one I'm placing at the moment, that's the output of my voltage regulator. I'm

**Dave Jones:** trying to get that down to the front panel somehow, so there's less wiring inside the unit. But, you'll probably see that uh trace change further along in the design process. And you'll a few pauses in the video here, and that's

**Dave Jones:** just me just sitting in the background, thinking, maybe sipping some water, having a uh scratching my head, and just having a general think about the system design, the layout. And And remember, I don't have a clear idea of how this

**Dave Jones:** layout's going to go. In fact, I have really no idea apart from that the that the regulators are mounted on the heat sink at the back, and the uh switches and and pots and and uh and and connectors are mounted on the front, and

**Dave Jones:** that's about it. Um so, but see, because I've got those fixed voltage regulators at the back mounted on the heat sink, it makes sense to put the circuitry around the voltage regulators up near the top of the board there, or the back um the

**Dave Jones:** back end of the board, which is the uh top edge up there near the heat sink, because you don't want to have to run traces all the way across the board. That will kill your layout completely dead. So, the goal of any

**Dave Jones:** PCB layout um is to try and get uh functional groups of components and keep them together nice and tight. So, that's why I lay them out functional groups often on the side of the board outside of the routing area. I

**Dave Jones:** sort of uh route them and then move the entire routed block into the board. Uh you might see a little bit of that here today. You've already um seen some of that up there, but uh there we go. That um that big circle

**Dave Jones:** there with number three in it, that's actually one of my mounting holes. That's a PCB mounting hole. Once again, that's a fixed thing. Once you place down those mounting holes and connectors, you want to lock those in place so you don't accidentally move

**Dave Jones:** them. Um that's a very important concept when you're routing out boards, you're doing a lot of stuff, a lot of things happening, you're editing things, moving stuff, and you don't want things to get automatically pushed and shoved or

**Dave Jones:** accidentally moved. So, that that mounting hole there, number three, will be um will actually be fixed in location. Now, here it is, I'm concentrating on the top uh the upper left uh corner of the board here, and this is where all my analog

**Dave Jones:** stuff will go. This is all my uh low-power um analog-to-digital converter, uh digital-to-analog converter, and the op-amps and things like that. I've shunted all those up in the one corner of the board because um that's I want that to be the quiet

**Dave Jones:** section of the board. So, I don't want to have them on the opposite uh side of the board and run traces all the way across, and it can cause um all sorts of issues with um it just uh ground noise

**Dave Jones:** and EMC and all sorts of stuff. I won't I don't have uh the capability to go into all that uh detail today. I'll have to do separate videos on uh actual each element of PCB design. This is just

**Dave Jones:** me just giving you a general um overview of what I'm thinking about when I'm laying out this board. There's my 3.3-V voltage regulator, I believe it is there. So, I've moved that up in the top corner up there because all that analog a lot of

**Dave Jones:** that analog circuitry is powered from that uh 3.3-V voltage regulator. My voltage reference will be up there as well, the 2.04-V uh voltage reference. And oops, what am I There I'm dragging in my microcurrent. There you go. That microcurrent circuit

**Dave Jones:** I routed before, I'm actually dragging that. I've dragged it from the outside into the board there. So, it's already partially routed. And there we go, I'm moving my power trace again to fit that down because the trace was in the way.

**Dave Jones:** And I'm just sort of you'll notice there will be a lot of shuffling in this. There we go, I've decided to route out that whole area because now I want to drag in I believe my micro controller. Oh, that's what I thought

**Dave Jones:** about there by moving that power trace. I thought my microcontroller would fit in the center of the board there, but now I'm wiring in the USB connector just to get that over and done with cuz there's four resistors that are

**Dave Jones:** associated with that. So, I put them near the connector down the bottom. And here I am, this is the microcontroller, the AVR, and I'm wiring in the ISP connector. And of course, I'm going to put the in-circuit programming connector

**Dave Jones:** right next to the chip because that's where it needs to be. It needs to talk to that chip. I'm not going to put it all the way on the board. Now, here's an interesting thing, I'm actually changing my schematic on the fly here. I can't

**Dave Jones:** remember what I've done. Oh, I added an extra bypass cap or I did uh something there. I've modified my schematic design and I've pushed that through to the PCB. Any changes I make in the schematic, I push them through. Oh,

**Dave Jones:** that's right. I added a second bypass cap cuz there's power on both sides of the chip. So, I added an extra bypass cap and there I am attempting to rotate the chip around. You'll find that that's probably not the

**Dave Jones:** that's definitely not the final orientation. I will end up rotating that chip again. So, as you'll see, pin one is on the right-hand side at the moment, U6 directly in the center there. And that connector I just placed, um,

**Dave Jones:** that eight-pin connector, that's the, uh, serial interface connector. No, sorry, it's the LCD connector. There we go. It's got LCD written on it. And because, um, that talks to the microcontroller, um, then I want it very close to the

**Dave Jones:** microcontroller. I'm not going to shove it on some side of the board somewhere where I've got a route over eight traces from the microcontroller right over to the other side of the board. So, naturally, I'm going to put something

**Dave Jones:** like a serial or a that, um, that LCD connector close to its source, which is the microcontroller. And, uh, I know things are happening a bit, uh, fast here. I don't have the capability to really, uh, slow this thing down. I've just got

**Dave Jones:** it in 10 times, uh, speed. But, as you can see, it is actually taking shape. And, uh, once again, I must have been having a a breather here. And, uh, maybe I've, uh, gone for a drink or something

**Dave Jones:** like that. And or just, uh, generally, maybe I'm measuring some stuff because I will have the component components and the box and things next to me, uh, right here while I'm actually, uh, doing this. Here Here you go, I'm back into it. So,

**Dave Jones:** I'm making, um, a lot of system changes as well. There you go, I just moved my voltage regulator there, too, because I decided that I wanted my serial connector, that's, uh, CN3 there, I wanted that over that side of the board

**Dave Jones:** because I thought I would make like a little riser board, little daughter board that could rises up out of that at right angles and then goes out the back of my case to avoid the, uh, heat sink. So, that's why I added the serial

**Dave Jones:** connector over in that corner. On the rev B, uh, part of the board, you'll see that I've I actually changed that. But, uh, we're only doing the rev A board at the moment, which is not the one that I

**Dave Jones:** actually built up. Um, if you've watched the previous videos, you'll see that I didn't actually end up I got this rev A manufactured, but I never built it up. I, um, went went directly to the, uh, rev B. And there you go. I mentioned

**Dave Jones:** before how I might rotate the microcontroller again, and I've done just that there. So, now I've got the ISP connector on the right-hand side of the microcontroller. And uh there we go. I'm just shuffling around like that, highlighting a bunch

**Dave Jones:** of components, moving it around, and you can see I can If you've routed things in blocks like that, then and you keep them isolated until later in your layout process, then you'll find that it's far easier than to just, you know,

**Dave Jones:** shuffle around a bunch of components. You can highlight them, including all their traces, and shuffle things around. Now, you'll still notice that it's all the traces are red. I'm still on the top layer of the board. And that's That's

**Dave Jones:** very important when you're doing a double-sided layout like this to try and do as much as you can on the uh top side of the board. And there's lots of stuff going on in my head which I can't really

**Dave Jones:** uh which I don't really have the capability to speak about here. A lot Some of it's even uh subconscious, things like that. But when I'm laying out a board, I do find that um some It just magically works in the end where almost the last

**Dave Jones:** trace, after laying out hundreds of components, thousands of traces, that last trace just sort of magically fits into place. And that's part of the art of PCB design. And it's actually quite difficult to uh teach cuz a lot of it is

**Dave Jones:** a lot of experience, a lot of innate ability to think about the entire system and how things fit together. And um this is one thing. If you're laying out a board which you didn't actually design, then uh it's going to be harder

**Dave Jones:** than if you actually designed the whole thing. But because I designed this, I have the circuit in my head, or I've got it next to me on paper. I know exactly Everything's modular on the schematic. I know where the modules go and I sort of

**Dave Jones:** have an idea of the system design as far as the case goes and where the connectors go and and things like that. So, now I'm working on that micro current part again. I've got all the resistors associated with that

**Dave Jones:** max chip there, the U21 along with the a couple of transistors there, the MOSFET and the drive transistor and the bypass cap and I've routed that in bam. I just I'm dragging that in. I tried to drag it

**Dave Jones:** in and I found it didn't quite fit. Oh, it's a bit it's a bit tight there. The uh But, I managed to do it. It just fitted in there. It squeezed in below the LCD connector there on the top part of the screen

**Dave Jones:** there and the connector's in the bottom and because I'm laying out a single sided board, it's going to be a kit and you know, it's fairly important to get the silk screen designators as well visible. So, you'll notice like R18,

**Dave Jones:** R17, things like that. I've got those outside of the component instead of on the inside where they're only visible after before you place components. So, I if you've got the room, then you can actually put those silk screen

**Dave Jones:** designators next to the component that you're actually doing. But, sometimes if you've got a really tight layout, you can't afford to do that or you might have to get rid of the silk screen designators. You might have to ignore them when

**Dave Jones:** you're placing components like this. If the silk screen designators are overlapping other components, you'll take care of that later as a final pass. At the moment, I'm not really caring about the silk screen designators as such. I might shuffle a few around,

**Dave Jones:** but generally I would do that as a last pass. So, now I'm I'm sort of starting to join all these modules together now because I'm now starting to think that, you know, I'm this is looking good. It's looking like it's going to fit. I'm

**Dave Jones:** always looking at how many components are left over, how much area I've got left. So, I've decided at this point that it looks like it's all pretty much going to fit as I expected. So, I'm starting to get a bit more

**Dave Jones:** confident. I'm joining the modules together, doing a bit more final layout. There I am mucking around with a few traces, trying to keep them nice and tight. So, I know there's going to be more traces through that area later.

**Dave Jones:** There you go. I've laid a couple more. So, I I know intrinsically how many more traces that I've got to sort of join those sections together. And you can see by those rubber band nets as well. There you go.

**Dave Jones:** I needed to create a bit more space. Ran out of bit of room. I highlighted a bunch of components, shifted them across a bit. I've made a little bit more room there. What am I doing there? I'm changing the

**Dave Jones:** USB uh layouts there. Shuffle you saw a little slight shuffle there in a cup in like four traces. I just pushed them all down. And there we go. I managed to fit in another trace. Oh, not quite. I ran out

**Dave Jones:** of room there right in the center. So, there you go. I decided to take that around the top instead of it it's hard to sort of explain where I'm placing traces and why it's So, because I have a lot of

**Dave Jones:** the information up in my head about where I think they should go where you know, I'm going to No, okay. I know I need to at least allow another couple of traces through here. So, I better route I better not take one trace through

**Dave Jones:** there and then have to use a jumper or you know, jump to the other side of the board for two traces. So, it's a trade-off about how if I know one trace has to go from one side of the board to

**Dave Jones:** the other just because it has to. There's no other way around it. Then I'm I'm going to do that now. I'm going to leave that until last, or I'm going to take it right around the edge so it

**Dave Jones:** doesn't interfere with all the other traces which are close together and have to join modules together. So, there's a there's a bit of an order about how you do these things. You're going to do your modules first, keep

**Dave Jones:** them as tight as possible, route them as fully as possible, and then drag them into the board as a complete routed module where you need it, and then you start once you're happy with that, you start tentatively joining the modules

**Dave Jones:** together, and then you start thinking about power traces. As you'll see, I haven't really done I've done a few key power traces there. And by the way, my power traces are going to be fatter than the signal traces I'm using. I didn't

**Dave Jones:** mention it, but I am using 10 thou traces here. So, all of my traces all my signal traces are 10 thou with my power traces, and they might be 50 or 30 or something like that. They're fatter, lower impedance, and just to designate

**Dave Jones:** that they're actually power traces. That's just a good thing to do. Now, it looks like I've used my first via there. There we go. I've run out of room routing into this microcontroller, and I've determined that I need to now jump

**Dave Jones:** to the bottom layer. But, with this the key with uh making jumps to the bottom layer is to keep them as short as possible. Once again, not going to you want to use uh on the bottom layer to route a trace

**Dave Jones:** from one side of the board to the other cuz you just split the board in half, and you've completely ruined your routing space for all the other traces on that layer. So, you'll notice those blue traces under the microcontroller

**Dave Jones:** are as short as I could possibly keep them so they don't take up too much room on the bottom layer. They don't split. There's another one which was quite short. I'm shuffling a few tracks to actually get it a bit shorter. There we

**Dave Jones:** go. You'll notice that I changed a few traces there just so I could save a few millimeters extra on traces on the bottom layer so I don't cut up my ground plane as much. I mean, this is not a high-speed controlled

**Dave Jones:** impedance board. So, cutting up the ground plane isn't really a big deal here. But if I'm laying out a much more critical board, then those little aspects of just uh saving a couple of meters of trace length just to so you

**Dave Jones:** can get a slightly bigger ground plane on the bottom. And those sort of things can be very important in in high-speed designs where those sort of things matter in terms of maybe EMC compliance as well. The ground plane's a big thing and you want to chop

**Dave Jones:** that up as little as possible. So, here you go. I'm laying out the output track there. There's the um J2 is my output connector. There, that's my output mounting point. And that looks like the constant current source U4

**Dave Jones:** there. I've sort of tacked it around. It's a low current, so it has a 10 thou trace going to it. Uh and I'm mounting a few I'm placing a few resistors associated with my output current sense. They're my output current

**Dave Jones:** sense resistors and J4 I believe is the is the current sense input connector. I've decided to move a few more resistors over to this corner and I'm slowly dragging components from outside of my board into the board. So, you'll

**Dave Jones:** find if you can see, you might see a wide shot soon of how many components I've got left and there will be very few actually left outside of the board. So, I'm slowly bringing them in one by one and

**Dave Jones:** there we go. I shuffled those around, put them vertically, and you'll notice I'm lining up all of the resistors nice and straight as much as I can because that's a good it just looks good. Too, if your resistors are just odd

**Dave Jones:** board everywhere at all sorts of weird angles and spacings and it doesn't look like a professionally laid out board. So, you want your components to be nicely grouped and this is where your snap grids come in. If you're not using

**Dave Jones:** a snap grid, well, you're crazy. You should be using a snap grid, but if you're not using a very small snap grid or component snap grid, then your components going to be slightly out of alignment with each other and things

**Dave Jones:** like that and your board just ends up looking pretty horrible and amateurish, but if you keep them, you know, a big nice line of resistors will be lovely. Things like that, it just looks aesthetically pleasing and it it just shows that you

**Dave Jones:** know what you're doing when you're laying out a a professional board like this. Now, I this is actually the first through hole board I've laid out in many years, I think, cuz I'm so used to doing everything surface mount these days that

**Dave Jones:** a through hole board like this is quite a novel thing for me of late. So, it's it's a different mindset. SMD will be different again because you can't use resistors to jump things. One of the key with through hole designs like this

**Dave Jones:** because these resistors are so long, they're 0.4 inches across, you can fit many traces underneath. So, you can use resistors to actually jump other traces, four, five, or six other traces at at once and that's very handy for routing

**Dave Jones:** ability and routing density on a double-sided board like this. If you've got eight layers or something, then it's things are much going to be much easier. Your options are much greater, but uh if um but you'll see with this double-sided

**Dave Jones:** layout, I could almost have done it on a single-sided board. In fact, if I put a bit more thought and effort into it, it it almost comes down to I could have done it with maybe, you know, a dozen

**Dave Jones:** jumper links or something like that. But uh uh these days there's really, unless you're manufacturing a million of these things, then uh there's not a huge cost advantage to go into a single-sided PCB. So, I'm using the double I tend I plan

**Dave Jones:** to have all ground plane on the uh bottom. As you can see, there's a few little traces on the top there. And now I'm I'm on the bottom again because it's blue, and I'm routing uh looks like my 5-V rail. So, my 5-V

**Dave Jones:** regulator is at the top of the board or the back of the board. Um and I need to route that 5 V through to other parts of my circuit. And as you can see, I'm trying to take it around

**Dave Jones:** the outside of the board there in the top. On the top of the board, I'm trying to route that 5 V home. I think I'm going to drop through to another layer here, possibly. I'm thinking about it. Maybe

**Dave Jones:** I'm having another drink or something like that. There we go. I'm dropping down, and I'm using more than one uh via there because uh that 5 V um carries a significant amount of current or it can do. So,

**Dave Jones:** you're going to want to use more than one uh via there. As a rough rule of thumb, um roughly one via for every half amp, but you've got some serious current, you're going to want at least a minimum of two uh vias there. And I've

**Dave Jones:** used two or three uh vias there for routing the 5-V rail. And you'll notice that this board is really starting to come together now. And uh I'm probably at this point uh thinking to myself, I'm pretty darn uh

**Dave Jones:** pleased with this. And uh I don't think I actually have uh any or uh, very few components left on the outside of the board to actually drag into here. So, now I'm doing a bit more fine detail up there. I'm doing

**Dave Jones:** some bypass cap work up the top. I'm Oh, what am I doing? I'm down into design rule checking. There you go. I have actually finished the basic layout. So, I did a basic design rule check to find what the

**Dave Jones:** errors is. That will find, uh, um, points that aren't connected. Actually, you know, uh, circuit nets which aren't connected. And there might be a dozen or two, uh, left in there. So, I will I'm now starting to layout those and I'm starting to connect

**Dave Jones:** the, uh, power now. I think the, uh, 3.3 V rail because once you've finished, what I would typically do when I'm laying out, um, pretty much any board is I do all the signals first. And then, once you do that, then you start work on the,

**Dave Jones:** uh, power rails. It it it it depends though. It depends how power-centric, um, how important the power, um, the the power distribution is to that design. But, uh, in in general, I'm going to on a board like this anyway,

**Dave Jones:** I'm going to leave that power supply until later and, uh, hopefully, I if I've given it enough, uh, thought and it's up I've considered this when I'm laying out the board either subconsciously or semi-consciously, I guess you could say, then, um, the power

**Dave Jones:** shouldn't be too much of a, uh, struggle to actually, uh, route around the board. There we go. I've done another design rule check. I'm looking through the errors. There might typically be a whole bunch of errors for silk screen spacing and things like

**Dave Jones:** that. But, I'm not too concerned with stuff like that. It looks like that, uh, I've just had a couple of breaks in my power, uh, rails there and it's told me that, you know, I might have five un- unrouted

**Dave Jones:** power nets or something like that. So, I'm just tidying those up, adding in a 3.3 5-V rail nets. Trying to Now, my goal pretty much at this stage is to reduce my error net count to zero or uh well, zero for all traces and all

**Dave Jones:** power signal traces and power traces. And the only errors I have left are ground cuz you'll notice I've routed no ground connections at all. Maybe the odd one on the top layer or something like that. But because I'm going to put all

**Dave Jones:** of my ground on the bottom, I'm going to flood fill my ground in there. And this is what I'm doing now. Here we go. It was coincidental. I'm now placing the outline of my polygon around the outside of the board. This will be my ground

**Dave Jones:** polygon. So, I'm placing that on the bottom layer and you'll see it. So, I'm defining the outline and then the program will automatically fill in the ground layout. Now, what I'm doing going down the center of the board there

**Dave Jones:** is I'm going to split this ground basically into the power and signal side. So, all of my power There we go. I just filled in the flood. I got the flood fill there. I can edit that later. I'm I can tweak the

**Dave Jones:** finer things later. But there you go. I've basically created a split ground plane there in my board. And the part on the right side of the board, that ground is all power ground. So, it goes from my regulators up the top right down to the

**Dave Jones:** regular down to the output connectors at the bottom and things like that. So, all of my heavy current is going to flow through the right side of the board. And all the stuff like that ground plane, the blue ground plane there on the

**Dave Jones:** left-hand side, that's all signal ground. So, there's no real current flowing through that. So, there's going to be no voltage drop through that. And therefore, all of my sensitive signal stuff, my ADCs and the DACs, will be at the same potential

**Dave Jones:** because they're at the same ground potential because there's no current flowing through that left-hand blue part of the ground trace. And wait, here we go. I'm doing some 3D model time. Sorry. Um my video capture program didn't capture that. It looks a bit uh dodgy,

**Dave Jones:** but what I'm doing now is looking at 3D mode. And well, no, I'm going the silkscreen layer now, and I'm shuffling my silkscreen. So, I'm going through, doing my final pass, my design rule check. I'm happy with it. It passes.

**Dave Jones:** There's no nets left over. My board is effectively routed and finished. And now I'm going through and uh just shuffling all of the component designators. There you go. I'm moving them around, rotating them, and putting them next to the particular component,

**Dave Jones:** making sure they don't overlap any of the pads because you don't want the silkscreen um overlapping any of your pads. That can affect you. Generally it doesn't affect your soldering, but it's just not good. And you want your

**Dave Jones:** silkscreen designators all the right orientation, all the right size, so it all looks neat and professional. Um I'm going to add some labeling. There we go. AVRISP. I added a label right next to the connector, and I did it as an inverse.

**Dave Jones:** I'm mucking more around with the ground plane here. Probably uh decided that I found a bypass cap not going to the right plane or something like that. So, having a little muck around, and I'm uh as you can see, I'm continually

**Dave Jones:** checking the top layer. Ah, that purple one there, that purple trace was a keepout. Now, cuz I didn't want ground to touch those two pads there because I was doing a star ground system back to uh it's you'll have to look at the

**Dave Jones:** microcurrent uh circuit to to figure out what I'm doing there, but I didn't want the ground, even though these traces were ground, I've created a keepout there, which stops the flood the polygon fill actually joining. Now, what I did

**Dave Jones:** just there is I joined That's the star ground point. I joined my two ground planes in that bottom left-hand corner down there. That's the point at which was my star point around the microcurrent circuit. So, that's where I

**Dave Jones:** split and I joined the ground planes via the top layer there. And I've added some Oh, there we go. Added some nice labeling eevblog.com, micro supply. I've added a serial top left there, another label serial. I'm labeling things out.

**Dave Jones:** I'm mucking around. And now, uh-huh, what I'm doing now is doing a pass for hole sizes. So, um Whoop, there we go. I'm going in, checking a footprint to make sure I've got a footprint right. Maybe there was

**Dave Jones:** some doubt in my mind that I might have goofed that up. So, there you go. I jumped over to the net, opened the data sheet, did a double-check. I'm now modifying hole sizes here just to consolidate them. So, this will be a

**Dave Jones:** last pass. Um I'm doing a 3D view here. Not Very few of my components actually have three real 3D models in them. But, if you did go to that trouble, then you can get a very accurate representation of what your

**Dave Jones:** board is looking like. I'm checking my solder mask expansion there. That's the pink solder mask expansion to make sure that there's that they're not going to break. There's enough clearance between each of those pads, in this case for the transistor.

**Dave Jones:** There you go. I just narrowed my pad on the transistor. I wasn't happy with that footprint. Wasn't happy with the solder mask expansion on that. It would have broken through. Solder would short out between the pins during during

**Dave Jones:** hand soldering or wave soldering manufacture. So, I'm just making sure a good thickness, you know, four or five thou gap between the solder mask between pads. That would be good enough. Anything less, you get down to a couple

**Dave Jones:** of thousand, they're not going to be able to manufacture that. Just like they can't manufacture a 2000 trace reliably. Or if you want them to, it'll cost a fortune. So, really, this board is very coarse. It's in terms of, you know, it's

**Dave Jones:** like 10 10 design rules. I forgot to mention that before. When I'm design rule checking, I set 10 thou traces minimum, 10 thou clearance. So, all of my rules and all those polygon pours, they will have a 10 thou

**Dave Jones:** spacing to them. So, this is a very coarse board. I could make this at home easily. So, any PCB manufacturer in the world could make this. Any backyard manufacturer can easily meet 10 10 rules. And I'm checking my bottom solder

**Dave Jones:** mask there. Checking the top layer. I've added the open-source hardware symbol. And bingo, there we have it. Is that That's our final board. And uh pretty darn happy with that. I'm not sure what I'm doing now. I'm just

**Dave Jones:** mucking around more with 3D viewer. You'll notice the top part of the board that sticks up. That's had the solder mask removed from it. The reason I did that is just cuz I like it. It's just a different look. It

**Dave Jones:** allows you to mark the bottom of the board. Something like that. I'm checking the copper layer, silkscreen layer, individual layers in 3D view. And here's the real power of 3D view. It shows you exactly what the board is

**Dave Jones:** going to look like when you get it manufactured. Exactly how the silkscreens looking. You can see if You can get a very high contrast in this mode to see that the silkscreen doesn't overlay any pads or something like

**Dave Jones:** And bingo, there you have it. There's my final laid out board. I'm feeling pretty chuffed about myself. So, I added a little platypus there on the right-hand side. Why? Well, why not? And I was quite happy with this layout. I'm pretty

**Dave Jones:** pretty pleased. There's quite a bit of um especially on the right hand uh side of the board, you'll see there's quite a bit of uh area left. And in the next video, I'll actually show me uh editing this board from rev A to rev B to show

**Dave Jones:** you how I took a completed board and then changed things around, ripped up the uh ground plane, modified a few things, squeezed in some more circuitry, and then uh redid it. So, I'll do that as a separate video. I just wanted to

**Dave Jones:** mention um one of the final passes here I didn't uh speak enough about was the drill hole size consolidation there. I I would have spent uh maybe, you know, 10 or 20 minutes going through uh the drill size hole table just to consolidate and

**Dave Jones:** make sure um all my footprints um actually have or how many drill hole sizes I'm actually using in this design and actually consolidate them cuz you might find that some libraries in your uh component library might use a a they might use a

**Dave Jones:** uh imperial drill size so it might be 0.795 mm instead of 0.8 mm that you'll use on other ones or something like that. So, you want to go through as a final step your drill hole size table, just

**Dave Jones:** consolidate all those hole sizes into one even if they might be near enough. You might go, "Oh, okay. I'm using 50 uh 1.2 mm holes for example and I've got two that are 1.25." Well, can I just you

**Dave Jones:** make those uh two holes 1.2 mm and that will in theory make your PCB a bit cheaper cuz there's less tool changes required. It's just a nice professional final step to actually do that and check those sort of things. And uh and once

**Dave Jones:** again, you'll do I'll do a more detailed design rule check. If I do care about silkscreen over pads, I'll be checking for things like that. Electrical uh clearances, of course, is a big thing. Maybe component spacing clearances, but

**Dave Jones:** because generally I I know the size of components or the silk screen outline defines the size of the component. I'm not too concerned about components touching each other cuz I I know what know exactly what I'm doing here. You'll

**Dave Jones:** notice that the heat sink up on top of the board or the back area of the board, they have a silk screen extending right out outside the board. And is that a problem? No, not really. The PCB manufacturer just chops that off. It's

**Dave Jones:** just chopped off in the process of manufacturing the board, but maybe as a final step I might go in and trim that silk screen just so it doesn't go off the board, but I keep it there cuz that

**Dave Jones:** is the actual size of the heat sink that I'm using the outside dimensions. So that helps me when I'm doing a bit of system engineering. So I'm going to leave that silk screen outline there outline there. I could have done it on

**Dave Jones:** one of the mechanical layers or something like that and that would be a more professional step. If I was doing a really professional level board, I would have other other mechanical layers that I'm specifying dimensions and engineering notes for manufacturing the

**Dave Jones:** board that it's 1.6 mm and it's you know, it might be gold flash finish and and where the routing areas and the routing paths and things like that are, but because you know, this is not a really complex

**Dave Jones:** complex professional level board, there's a few extra steps I wouldn't do that, but in general I'm quite quite pleased with that layout. How long did it take me? Well, how long did this video go for? Multiply that by 10 and

**Dave Jones:** that's roughly how long it took me to layout this board and there was a lot of thinking and other stuff in there. And maybe if I had the libraries better sorted out before I started, I could have saved some extra time and things

**Dave Jones:** like that. So Uh, sometimes it you know, a board might take a lot less time because you're using all existing components that you can guarantee all the footprints are right and everything like that. Other times you might be doing a lot of

**Dave Jones:** interactive processing. I might be even going through and changing um some components in the middle of the design process here. I might find, ah, you know, I might have been mucking around and thinking, oh, I might have found

**Dave Jones:** some other device in some other uh package or something like that and and change it on the fly or might find, oh, I can eliminate that bypass cap cuz they're so close to each other, I don't need that. I can drop one of the bypass

**Dave Jones:** caps or in the case you saw in there, I think I added a bypass uh cap in there just the nature of the layout that I didn't think about when or I didn't uh get that right when I was just laying

**Dave Jones:** out the schematic. So, um you might find that when you're doing stuff on the board, you might have to go and uh back annotate the schematic and make some few make a few changes and things like that. As you can see, I think it's

**Dave Jones:** a neat layout. It's got the cutouts for uh the case that it's going to fit into neatly. And I have to do a whole separate video on that cuz there's quite a bit of effort which went into actually

**Dave Jones:** figuring out where all the components went and what components I used like the inter user interface components like the knobs and the switches and uh the power connector and things like that and the heat sink went into this

**Dave Jones:** system design before I even started laying out the board. And that constrained a lot of uh things. And if this was just a board that was sitting in the middle of a case and then I had wiring going out to the front panel and

**Dave Jones:** the back panel, then it would have just been a a simpler uh design from a system and a PCB point of view cuz it would have just been a square board. There would have been no fancy cutouts. The uh whole the

**Dave Jones:** mounting holes wouldn't have to be in specific locations to meet the supports in the case. And uh a lot of stuff like that would have been a lot easier. But, when you're trying to integrate a PCB like this, like I am, that fits a

**Dave Jones:** specific uh case, then there's a bit more engineering. If you've got a custom case, you might have to worry about the 3D aspects, uh the height of components, will it foul with the case, and things like that. In this case, I didn't have

**Dave Jones:** to worry about that. I put a bit of thought into it. The case is big enough. It's not a custom molded thing. But, if you're doing a professional uh PCB layout to fit into molded enclosure, really you've got to think about the

**Dave Jones:** whole 3D aspect of the mechanical packaging, thermal performance comes into it, and uh things like that. You don't want stuff to overheat. Uh if you're doing high-speed signal design, there's lots of stuff um in there to do with uh you know,

**Dave Jones:** transmission lines and controlled impedance uh stuff, EMC requirements, and all sorts of stuff. But, this was just a fairly simple board with a simple split ground plane. I probably didn't have to split that ground plane. Actually, if you're asking exactly why, there's

**Dave Jones:** probably not a real genuine electrical reason to do that. Just good practice uh really. That I just wanted to separate the right-hand side uh power, which can carry, you know, several amps or something like that, and it may be

**Dave Jones:** switching and doing all sort the load might be at that cuz this is a power supply supplying an unknown load. So, you don't know what it's actually going to be powering, and that could be doing all sorts of putting all sorts of um uh

**Dave Jones:** strain on that uh ground system. And if that's you have one big flooded ground plane, then it might in theory cause an issue. So, I just decided to split it out, separated into low current and uh high current uh stuff. Effect not really

**Dave Jones:** analog digital um in this case. Although, I guess you could make the same uh call that similar to an analog and digital split uh plane or something like that. but anyway, uh there you go. That's the complete layout

**Dave Jones:** of the board. I hope you found that interesting. I'll do another video showing the changes from Rev A to Rev B. Catch you next time.
