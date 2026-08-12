---
video_id: 1QBFIfKlvHU
title: EEVblog #470 - Agilent N9344C 20GHz Spectrum Analyser Teardown
url: https://www.youtube.com/watch?v=1QBFIfKlvHU
source: youtube-asr
timestamps: {"0": 1, "1": 20, "2": 36, "3": 52, "4": 67, "5": 80, "6": 92, "7": 107, "8": 118, "9": 133, "10": 148, "11": 168, "12": 187, "13": 208, "14": 222, "15": 235, "16": 249, "17": 271, "18": 285, "19": 299, "20": 315, "21": 334, "22": 354, "23": 373, "24": 383, "25": 396, "26": 413, "27": 429, "28": 445, "29": 456, "30": 473, "31": 486, "32": 500, "33": 514, "34": 531, "35": 547, "36": 563, "37": 578, "38": 590, "39": 607, "40": 622, "41": 636, "42": 648, "43": 662, "44": 676, "45": 690, "46": 706, "47": 722, "48": 737, "49": 752, "50": 764, "51": 776, "52": 788, "53": 801, "54": 816, "55": 840, "56": 856, "57": 874, "58": 889, "59": 900, "60": 916, "61": 933, "62": 949, "63": 964, "64": 973, "65": 987, "66": 1006, "67": 1022, "68": 1042, "69": 1055, "70": 1070, "71": 1082, "72": 1099, "73": 1114, "74": 1126, "75": 1142, "76": 1157, "77": 1174, "78": 1189, "79": 1202, "80": 1217, "81": 1229, "82": 1243, "83": 1258, "84": 1276, "85": 1291, "86": 1306, "87": 1322, "88": 1338, "89": 1349, "90": 1367, "91": 1381, "92": 1396, "93": 1410, "94": 1423, "95": 1437, "96": 1452, "97": 1468, "98": 1488, "99": 1503, "100": 1518, "101": 1535, "102": 1548, "103": 1560, "104": 1579, "105": 1600, "106": 1617, "107": 1630, "108": 1646, "109": 1663, "110": 1678, "111": 1691, "112": 1708, "113": 1720, "114": 1746, "115": 1762, "116": 1775, "117": 1789, "118": 1807, "119": 1827, "120": 1842, "121": 1858, "122": 1874, "123": 1888, "124": 1904, "125": 1921, "126": 1933, "127": 1946, "128": 1962, "129": 1974, "130": 1991, "131": 2004, "132": 2019, "133": 2035, "134": 2049, "135": 2062, "136": 2077, "137": 2094, "138": 2110, "139": 2127, "140": 2143, "141": 2156, "142": 2171, "143": 2184, "144": 2201, "145": 2216, "146": 2232, "147": 2243, "148": 2258, "149": 2271, "150": 2289, "151": 2307, "152": 2322, "153": 2341, "154": 2359, "155": 2376, "156": 2392, "157": 2405, "158": 2420, "159": 2436, "160": 2450, "161": 2470, "162": 2486, "163": 2504, "164": 2518, "165": 2533, "166": 2545, "167": 2560, "168": 2570, "169": 2588, "170": 2600, "171": 2615, "172": 2631, "173": 2645, "174": 2661, "175": 2678, "176": 2694, "177": 2705, "178": 2716, "179": 2732, "180": 2746, "181": 2761, "182": 2777, "183": 2791, "184": 2805, "185": 2821, "186": 2837, "187": 2849, "188": 2863, "189": 2879, "190": 2893, "191": 2912, "192": 2926, "193": 2942, "194": 2954, "195": 2971, "196": 2993, "197": 3010, "198": 3024, "199": 3038, "200": 3052, "201": 3067, "202": 3080, "203": 3095, "204": 3112}
---

**Dave Jones:** Hi, what's inside an $18,000 Agilent 9344C 20 GHz spectrum analyzer? Well, the people at the RF design division at Agilent thought we'd like to know, so they sent one for the teardown. You know what we say here on the EEVblog, don't

**Dave Jones:** turn it on, take it apart. So, unlike Tektronix who were scared that I would break their precious spectrum analyzer, Agilent uh well, the RF design division said, "Yeah, no worries. Take this, tear it down, have your way with it." Beauty.

**Dave Jones:** Thank you very much uh the RF design division at Agilent for supplying this. Oh, I can see myself. Reflective screen on this thing. Um we have the N9344C. Geez, I wish they'd get better model numbers that I mean, who pulls that one?

**Dave Jones:** Who pulls that model number out of their ass? Really, fair enough. Anyway, 1 MHz to 20 GHz, awesome. So, we're going to have some excellent RF uh magic in here. Fantastic handheld spectrum analyzer, real high-end bit of kit, as I said,

**Dave Jones:** about uh $18,000 Australian uh dollars, designed for field use. It's got overmolded uh rubber around the outside just in case you drop it. It's really hefty. I don't know, it's at like 3 and a 3 kilos or something like that.

**Dave Jones:** And um it's got a nice little springy stand on the back. Oh, look at that. Oh, I could play with that all day long. Nicely screwed in there. It looks like it would uh survive. I don't want to

**Dave Jones:** rip that off, but yeah, seems pretty rugged to me. It comes from the uh Chengdu instrument division at Agilent Technologies from the marketing department. Hello, Song Tian. Good on you. Um so, this is obviously one of their demo units or something,

**Dave Jones:** lithium-ion battery in there. And uh we'll take a look inside to see what's in there, but let's have a quick uh peek at the top here, shall we? What have we got here? We've got our RF input here,

**Dave Jones:** 50 ohms of course, our 50 ohm RF output, both N connectors, all standard and that's for the uh tracking generator, of course. And it's got little protective caps on there, beauty. External trigger reference, GPS antenna, very nice. You

**Dave Jones:** could get some nice applications with that. External power for the charging, building LAN, USB, headphones as well for getting the modulation output. Fantastic. And there you go. User interface on the front. We're not going to turn it on because we're going to

**Dave Jones:** take it apart. Now, it looks like there's a few torques screws on this thing, but this one here is a Up. Look like a Phillips. Smells like a Phillips, but I ain't getting anything on that. If I get my flathead in there,

**Dave Jones:** hang on. No. Smaller flathead. There we go. We've got some sort of port here. Wonder what that is. Ah, that's the That's the battery. There we go. We'll take the battery out. Uh TDK Electronics. There you go. 4.6

**Dave Jones:** amp hour, 10.8 volt. Must be recycled. Oh, look at that. Battery gauge on it, beautiful. Fully charged. I can smell it. Mhm. Whee! All right. We got $20,000 instrument smell and uh it looks like Oh, yeah, look at that. Even first

**Dave Jones:** cab off the rank here. Uh I probably can't won't be able to see in there, but they got little springs attached to the top of the case all the way through there just to put some extra uh downward force on

**Dave Jones:** the battery pack. Nice attention to detail there. I'd probably have to turn the uh uh contrast up for you to uh the There you go. You can see them. Nice in there so it doesn't uh vibrate and uh

**Dave Jones:** all that sort of jazz. So, very nice attention to detail. I like that. That's a good start. So, let's whip this puppy open and uh we have a Torx. It must be a T10 and a T15 in there.

**Dave Jones:** There we go. T10's the ticket. And of course, um I'll post some links to uh spectrum analyzer teardowns or RF teardowns I've done before and uh we Oh, my Is my Oh, my Torx isn't going to fit in there. Oh, bugger. Hang on.

**Dave Jones:** Oh, I can just get that one. There we go. All right. Yes, folks, it is teardown Tuesday. There we go, 3:00 p.m. Hopefully, I can uh finish this before I have to head home. Apologies if I can't. But anyway, we

**Dave Jones:** expect to see inside here um not much on the processing side of stuff. We don't care about all that sort of stuff. You know, it'll just be a some sort of processor. I'm not sure whether it runs like embedded Windows CE

**Dave Jones:** or something like that. Most likely runs sort of some sort of embedded OS, but uh yeah, not too fussed. What we want to see is inside the RF cans, of course. They'll be all uh fully machined cans with RF shielding gaskets on them and uh

**Dave Jones:** um we will see lots of PCB uh component technology as well. Lots of inductors and stuff um embedded into the PCB and capacitors and uh various components and way and um bandpass filters and things like that all sort of

**Dave Jones:** There we go. All embedded into the PCB, which won't be a regular material. It'll be special controlled impedance and uh it'll be very very nice. These spectrum analyzers, they cost a lot of money for a reason. And to get 20 gig bandwidth is quite

**Dave Jones:** quite an achievement. There we go. We're straight off. Here we go. Ta-da! Oh, look at that. Look at that. Beautiful. There it is. Precision machining. Look at all the Look at Look the big fully machined aluminum blocks there for all the RF stuff. We've got

**Dave Jones:** some rigid coax down here we'll take a look at. Two FPGA to display, calm.

**Dave Jones:** And on the back of the case here we have little slots for the handle on the side. Looks robust enough. I guess I would have maybe have liked to have seen that be screwed into the aluminum blocks or something like that

**Dave Jones:** just for rigidity, but obviously a quite a good quality impact resistant polymer plastic they'll be using on this thing, no doubt. But interestingly, have a look at the shielding tape they've put on there. That'll be some sort of you know ferrite

**Dave Jones:** impregnated shielding tape or something like that. I don't think that is regular tape there, folks. So, just a little bit more shielding on the back side of the case, I think. But isn't this a thing of beauty? Look at that.

**Dave Jones:** Fully machined aluminum blocks. You can see the PCB wedged down in there. There it is. You can see the PCB down in there. And so, they've got a top shielding block, bottom shielding block. So, if we take off these top shields, we'll be able to

**Dave Jones:** see the top half of the board. Then we'd have to get the board out. Presumably to see any components on the back side of the board. Then we've got another board down in there. And then we've got at

**Dave Jones:** least a third board right down the bottom there with its own cover shielding plate and there's that rigid coax I was telling you about joining these two blocks here. So, they got that rigid coax. You know, that'll be like 20 gig bandwidth or

**Dave Jones:** whatever they need. They looks like they got SMA connectors on there going from board to board. Look at all the vias on there. Look at all that via stitching there to get the impedance uh get the inductance right

**Dave Jones:** down. So, fantastic. That one's got a and they've got center mount board connectors in there mounted right on the center so the pin that comes out doesn't we'll probably see that when we take the board out. The pin's on the top side and

**Dave Jones:** it goes direct the center pin sorry is um on the well the bottom side of the board here and that's connected directly to the correct width trace on the bottom side of the board. So, there's no pin which comes out and then goes right

**Dave Jones:** angle down like that because well at 20 gig that sort of stuff matters. So, look down in here. Looks like we have some status status LEDs down there. They're not marked though but obviously they're some sort of internal service status.

**Dave Jones:** We've got some sort of a that could be like a JTAG programming or debug header or a something like that. We've obviously got another uh um micro board coax connector on there and probably used for another option or

**Dave Jones:** something like that but then we've got some regular coaxes going around to here which then we follow them around. Let's have a look at where the inputs are. So, oh here's our RF output. So, here's our RF signal output. Then we've got rigid

**Dave Jones:** coax there. So, this is our generator board. So, that looks like probably I'd say that module there is our tracking gen perhaps. It just makes sense to keep it completely separate and that's why then they've got the join going out like

**Dave Jones:** that. So then the output frequency of this can go into the tracking gen. So the sweep frequency in here of the spectrum analyzer, this will be the spectrum analyzer module, then that can drive the tracking gen over here

**Dave Jones:** completely separate. Of course, you don't want any crosstalk between those at all. Absolutely essential. And then here's our main RF input here. Very short rigid coax. Of course, if you don't know um what rigid coax are, they're uh

**Dave Jones:** various technologies go into them, but it basically feels like it's like a complete copper rigid outer pipe. I mean, there's no flex in that at all. It's not a regular cable. It's basically a solid coax cable. That's basically

**Dave Jones:** what you've got there. And um then we've got our Yeah, that's our uh What's that? That's our external trigger input. And then we've got a GPS. So they Oh, there there's our there's our GPS antenna. There it is. Just spotted it.

**Dave Jones:** There it is there. We've just got It's just got a patch antenna there. Nothing particularly special at all. GPS module that goes off and then the external antenna over here. So it looks like they've got an internal patch antenna

**Dave Jones:** and then an external optional external antenna as well. So it will work with the internal antenna. You can see it's patch antenna due to that center point and then the uh then the antenna pad on the top there.

**Dave Jones:** So typical patch antenna. Their performance isn't that great, but certainly adequate for uh getting reasonable uh well, you know, something out of the thing anyway. So There's our Yeah, our GPS antenna goes around. External trigger. So that's the

**Dave Jones:** external trigger coming around here. The external trigger's going down to the main board. So the trigger's not going into the processor. Of course, it's not going into the spectrum analyzer module up there. Um What else have we got? Then we've got

**Dave Jones:** our Yeah, what else we've got interconnect wise? We've got our main processor board here going up to our that looks like the bottom Well, there's one board There's one complete board going across both of those modules. So, I'm presuming the spectrum

**Dave Jones:** analyzer module here and the tracking gen looks like that second board there goes all the way between the two modules. So, interesting. But, uh yeah, obviously you've got to connect the processor over to there. And then we've just got some

**Dave Jones:** flat flex here going down to the keypad display whatever. Some dip switches and uh not much else. But, uh interestingly, there is, of course, going to be an FPGA in here. There's a display. Looks like we can take off this uh panel here. And

**Dave Jones:** there we go. We've got our JTAG for our uh processor and our FPGA as well. And uh interestingly, I love this. Check it out. They've got a big inductor there. Obviously, it was uh too high for the main you know, for the main uh to get

**Dave Jones:** under the main cover. So, they went, "Oh, bugger it. Let's just put a little cutout in there. And then we'll put the uh plate over that. It'll all be nicely shielded anyway. Beautiful. But, check out that. I mean, even the plate,

**Dave Jones:** they've had to machine out a cutout in there so it doesn't short out the pins that actually uh aren't flush with that. They do it Those pins actually stick out a little bit there. Just, you know, attention to detail. That's why These

**Dave Jones:** things aren't mass manufactured in their tens or hundreds of thousands, you know? So, they can afford to just machine a single plate just to do that. Brilliant. Now, of course, to get all this apart, I'm actually going to have to take off

**Dave Jones:** these uh rigid coaxes here. I'm going to have to unscrew those, get a spanner in, and uh unscrew those suckers out. And by doing that, I'm probably avoiding the calibration on this thing, of course, because when you're talking about a 20

**Dave Jones:** GHz bandwidth uh connector like this, even the torque on the thing matters. Um really really or it very likely could. So, yeah, the odds are that you know, I'm not going to damage anything by taking it off, but

**Dave Jones:** the thing actually might need a recall after this. Certainly. And off we come. And they should just pull out like that. So, there you go. There's a 20 gig rigid coax. And there's a close-up money shot for you connector

**Dave Jones:** aficionados. And of course, each rigid coax has its own you know, custom assembly and is probably you know, individually tested and characterized as well. I wonder how much just that individual component cost them. One of the things I love about

**Dave Jones:** this construction with all the machine solid aluminum block is like this connector is not going to break off. You know, you get some heavy ham-fisted production or field operator or something like that. And look, it's just you know, screwed directly into the full

**Dave Jones:** chassis of this thing. Unbelievable. And I love it when PCB layout people put these visual layer guides right on the side of the board. They just bring the copper right out to the routed edge. One of the dangers with that of course is

**Dave Jones:** that you can actually short these out. Now, a bit of context here if you're not sure what you're actually looking at. You've got the top aluminum block up here. Sorry, I got this propped on an angle. It's going to bounce around a

**Dave Jones:** bit. Bottom aluminum block in here. And the PCB multi-layer PCB wedged in there. This is actually the tracking gen module or what I believe is a tracking gen module. And you can count the copper layers in there. Have a look. Oh, my

**Dave Jones:** pointer's not uh fine enough, but 1 2 3 4 5 6 7 8 layer board in there over up, you know, alternate ground and power layers and stuff like that. But, that allows you to see the actual copper

**Dave Jones:** in there and that there If you're wondering what that thing that is obviously an RF gasket on there sealing the top of that board. That's what it looks like anyway. Now, of course, if the layout person is smart, that won't actually be that

**Dave Jones:** copper there won't actually be connected to anything at all because of course you could easily get shorts on the outside of this board when it's routed, snapped, or or whatever or you're connecting to something, you know, touching metal next

**Dave Jones:** to or something like that you can short it out. So, what they'll do is just Well, I'm not sure it's not on the side. I have to show you a top view, but they would just have an isolated

**Dave Jones:** island pad in there which isn't connected to anything just floating copper which then goes right to the edge which then gets routed off when this board gets machined. Now, I think I have all the screws out for this top

**Dave Jones:** one this top connector module up here. Ta-da! There is our spectrum analyzer module. Well, presumably. Well, the front end for it anyway. It's probably the front end. They're probably a lot of the spectrum analyzer stuff is on that secondary board down the bottom and

**Dave Jones:** we've got our tracking gen there. But, look at the number of screws we've got to take out and look at that board-to-board interconnect. Ta-da! Of course, that's not taking, you know, RF frequencies and stuff like that. It's probably only taking the

**Dave Jones:** lower stuff frequency out to the analog-to-digital converter plus all the control signals and stuff like that, of course. So, that doesn't need to be particularly high frequency. And this pink cover here that just comes off is likely just a thermal pad like a seal type pad

**Dave Jones:** just to get good thermal coupling between the block which presumably gets quite warm and the rest of the aluminum here which can also act as a bigger heat sink as well. And there's that board to board interconnect for those

**Dave Jones:** curious in such things. There you go, you can see the center power connect center power tabs down in there. They can carry reasonably high current likely. Anyway, I don't think they're just Oh, they could just be a ground shielding tabs or

**Dave Jones:** something like that. These are usually quite, you know, high frequency connectors, but obviously it's not being used for here for the you know, the high end RF signals. That's all contained within the block. So as I said, just

**Dave Jones:** control and probably the final IF output as well or that might come via one of the coax's over there perhaps. And I think I got the screws out here. These have some screws on the bottom. So I'm not going to get this top plate off

**Dave Jones:** without taking out this whole board. Yep. Yep. Yep. There we go. There's probably some interconnects here. There's some interconnects down in here and uh that sort of stuff. I'll be able to show you that in a second, but there you go.

**Dave Jones:** You can disconnect those. Not terribly exciting stuff down in here. You know, like I you know, would you even bother taking that off? It's just the LCD controller. So yes, there's absolutely no shortage of shielding on this thing.

**Dave Jones:** There's the LCD display. It looks like it's an NEC model NL644 880 or something like that. I don't know. I don't think I'll even bother taking off that and then you've got your keypad down in here. That's not what

**Dave Jones:** we're here for today. There will be some microcontroller goodness under here. So let's check it out. Check out that big pulse brand inductor there or common mode choke. Absolutely massive, sticking out the bottom side of the board there.

**Dave Jones:** There we go. Haha, look at that. We're in like Flynn. And interestingly, check out the bottom here. Thermal pads have actually, uh, molded the aluminum, uh, plate so that it actually, um, used as, uh, thermal, uh, you know, a heat

**Dave Jones:** sink, um, designed in to, uh, connect onto all of the major, uh, heat generating packages in there. Brilliant bit of systems engineering. I love that. A lot of thought and attention to detail has gone into that thing. And you can

**Dave Jones:** see the, uh, thermal, um, seal pad on top of each one of those chips lines up. So, you know, there's got to be a, uh, a lot of, um, uh, you know, communication going on between the, uh, PCB layout guys and all

**Dave Jones:** the mechanical, uh, housing guys and all that sort of stuff. So, excellent work. Well done. Huge thumbs up on that. Well, another really interesting part about this, which I didn't expect to see, is, uh, yet more shielding blocks inside

**Dave Jones:** here. Um, my only guess would be that would be the, um, analog-to-digital, uh, converter. Uh, something like that. This one's got a relay, uh, poking out of it there by the looks of it. Um, but yeah, so it's uh

**Dave Jones:** obviously taking the, uh, input, um, signals from outside the main, um, shield here, rounding them under the, uh, outside shield into these shielded blocks. You can see all the uh grounding vias all the way around the outside of

**Dave Jones:** those to, uh, add some extra shielding, lower the, uh, ground inductance, yada yada yada. But, uh, yeah, obviously those, um, RF, uh, well, intermediate, uh, frequency lower, you know, it's not the full 20 GHz bandwidth. They actually, uh, mix that down to a lower frequency

**Dave Jones:** before it goes into a relatively, uh, slow analog-to-digital converter in the, you know, uh, tens of megahertz range. We'll have a quick look at a couple of the major parts on here. We've got ourselves an Epson S1D1374A LCD controller. Nothing special. It's a

**Dave Jones:** bit of a beast. It's got 1 mega SRAM built in. And then we've got our LCD driver up there. And there's our LCD interface cable. And there's our DSP analog devices 21363. Yes, it's one of those shark processors

**Dave Jones:** we've seen a lot recently in Rigol gear and other stuff. Bit of a beast. 3 meg internal SRAM and that's coupled directly into an Actel FPGA there, which we'll have to take a look at by peeling the sticker off. Then up here we've got

**Dave Jones:** ourselves a crystal ethernet controller. Nothing else major on this side here. We've got some memory down there. And that looks like our main processor. I can see I think I can see arm down in there because basically we

**Dave Jones:** have three technologies coupled in here. We've got our DSP which would be doing all the heavy lifting in terms of the stuff from the analog and stuff from the ADCs down in here. And then we've got an FPGA. It's just I

**Dave Jones:** don't know doing some glue logic some really fast process parallel processing or something like that. And then well, we don't know the complexity of that one yet. And then we've got our main processor over here which would be

**Dave Jones:** controlling the user interface and everything else. And you probably can't read that but that's an Actel IGLOO up you know microsemi IGLOO AGL 400 V5. So that's actually quite a sizable FPGA 400K gates about a $50 FPGA. And then

**Dave Jones:** we've got some nice looking power supply stuff up there in the corner. Beautiful. Nicely laid out. High current traces you can see that. We've got more power supply stuff happening over here. And you know lots of little local regulation

**Dave Jones:** and core voltages everywhere, but yeah, that pretty much does the business. It looks like we have a real-time clock down here. You can tell from the 32 kHz watch crystal down in there by the looks of it and a little tiny package.

**Dave Jones:** External ADC and that about does it for this side of the board. So, I suspect there's more on the other side. So, let's flip it over. Nothing terribly exciting on here. Some more power supply stuff. There's that huge pulse common

**Dave Jones:** mode and it looks like it is a common mode choke cuz it's near the DC jack right up there that you saw poking out of the shield before. Just some more memory down the bottom there and we've got our real-time clock battery. We've

**Dave Jones:** got the bottoms of our shields which we'll take off in a minute. Micro SD card. There's no card in it, but it does certainly have an internal micro SD card slot. No idea what that's for and more power supply stuff. Well, hello. We have

**Dave Jones:** a couple of bodge wires under here. Look at that. There we go. Some enamel wire going from that trace over there over to there. Another little bodge in there. Yeah, there you go. Well, you know, the complexity of this thing and I guess

**Dave Jones:** they couldn't be bothered re-spinning the board. They just found oh yeah, let's just hack that in there a bit. No drama at all. Let's take a look at what that puppy is doing there because um I'm presuming that the traces obviously

**Dave Jones:** come under the shield in here from these two connectors here. I believe from memory this one wasn't actually connected to anything, but this one here certainly was. And surprise, surprise, AD9235 12-bit ADC 40 meg samples per second. This mod down in here is interesting.

**Dave Jones:** Take a look at this. There's a that looks like a zero ohm jumper there and it looks like and they've got that enamel coated wire going over to there, so they're like joining those grounds together. Interesting. Did they have some sort of

**Dave Jones:** grounding problem or some sort of performance issue or something like that they had to fix? I don't know. Quite unusual. And the back of that shielding block there, no surprises, just all the bypass and other miscellaneous passive stuff. Well,

**Dave Jones:** underneath the other block, there's not much at all, but it looks like for example like the here's the RF connector down here, and there's another one here. So, like that's going to flow into here somewhere. So, it looks like you know,

**Dave Jones:** it looks like we've got some RF tran- you know, probably like an RF transistor or something like that. I'm not sure. I forget what was actually connected to this point down in here. And of course, one thing we've been missing so far is

**Dave Jones:** the 10 MHz reference oscillator, and there it is. It's a Raycom. We'll get in there and have a look at the particular model number, but looks like we've got a couple of devices up here. We'll check those out. We've

**Dave Jones:** got looks like another 10 MHz oscillator down in there. Oh, and I think I see a budge cap. And no surprises as at all to find a clock generator such as this ADF4001 200 MHz programmable frequency synthesizer. We've got an AD 829 precision op-amp

**Dave Jones:** there. And down here with a little budge cap tucked in there. Hello, look at you. Um, that looks like a another oscillator. Looks like a 40 meg oscillator. There it is, 4 meg 000. And there's the Raycom VTXO210A-5

**Dave Jones:** 10 MHz presumably temperature compensated oscillator with what looks like a trimmer cap on the top there. Unfortunately, that's are going to work anymore because it is now upside down and of course with these uh precision reference oscillators you can't have

**Dave Jones:** them upside down because all the crystals just start settle to the bottom. It doesn't work anymore. And for those playing along at home, this is PCB rev 3. So, what we've got here is our main reference oscillator and frequency

**Dave Jones:** synthesizer which then gets multiplied up of course in frequency in the tracking generator and other parts of the system secondary oscillator down here. Not sure what they're doing with the secondary oscillator, but then our ADC under this block here and that is

**Dave Jones:** what I get, you know, all the low phase noise of this spectrum analyzer. Really good oscillator, really good mixes higher up and stuff like that in the RF block. So, I think it's time to take the RF block apart, but you'll see the uh

**Dave Jones:** the machine aluminum cover that they went to all that trouble. They sealed off all the individual sections all under there. Done it properly. Built in braces. They've got a couple of test pads over here on the side of the board, but as

**Dave Jones:** far as like our production test pads and things go, I really you know, don't see anything else on here in terms of that. So, all the you know, they just assemble this board and you know, do the basic

**Dave Jones:** basic programming with the FPGAs and all the program will devices and then they just do a thorough thorough you know, software defined tests in the things and calibration, you know, all that sort of stuff. So, they're not actually doing a huge amount of tests at

**Dave Jones:** the bare board level I suspect. And it goes without saying I think that the soldering on this board is first class. Just a tip for the young players. When you're reassembling something like this, make sure you have the cables actually

**Dave Jones:** sitting outside before you put the shield on. D'oh! All right, that was a fair few screws, but let's Hey, lift this off. Oh, there's our There's our gasket. Ah, ta-da. Look at that. There's our gasket. Beautiful. What's that made out of?

**Dave Jones:** Lovely. Look There you go. That's the material. It does feel metallic in some way, but uh yeah, I'm not sure. If you know the exact material actually used for this RF gasket, please leave it in the comments. So, this is

**Dave Jones:** our tracking gen board, and I think it's going to just lift out because really it is just uh shielded like the I don't think there's Oh, they No, there could be a board-to-board interconnect over here or something like that just for some

**Dave Jones:** control uh stuff, but of course all the RF goes through uh the connect Yep. Yep. There we go. Board-to-board interconnect. There it is. Connects down at the bottom. You know, you can tell by the traces in there kind of a dead

**Dave Jones:** giveaway. And there's another gasket on the bottom there. Of course. Beautiful. And uh all fully machined each individual section, of course. We've I won't go into details. I've seen this in uh RF spectrum analyzers before. This is a rev six

**Dave Jones:** board of the tracking gen in 9342. And uh that is ta-da. Oh, there it is. There's our tracking gen. And yes, ta-da. We have our first look at some PCB uh filters and stuff like that all in there. There we go. Typical RF stuff.

**Dave Jones:** And you know how I mentioned before about the uh center pin of this thing uh coming through the top of the board? Well, look, it's actually completely shielded on the other side. There you go. So, yeah, the top side is uh of

**Dave Jones:** course, you know, there's no uh center pin that popping out there and on that side, no, nothing. It's all contained in there then it's going through to an inner layer through probably popping up there somewhere and going wiggle wiggle wiggle into there

**Dave Jones:** and across. And we could be here all day trying to look at this thing, but this is rather interesting. Actually, look they've put some solder on top of that trace there. I wonder why. One interesting aspect to note is

**Dave Jones:** look, you can't actually see the holes in the vias there. Little micro vias obviously um using this thing and plugged of some sort, but you can see the You can see the signal coming in from the connector here to be going through a

**Dave Jones:** center layer like there. It'd be going through here like this, hence the you know, these are vias around here to reduce the shield around here and reduce the inductance of the ground plane and all that sort of jazz and it pops up here to the top

**Dave Jones:** layer. This is all controlled impedance PCB via the by the way. It's not just regular stock standard PCB you'd get from any manufacturer. Very carefully very carefully characterized of course for controlled impedance applications and AC coupled there going into that

**Dave Jones:** device there. I have no idea what some sort of well, I don't even know what this connector is used for actually. So, I'm not going to try and go through and decode every single part of this. Sorry folks, it's just not um

**Dave Jones:** not worth my time really. So, I guess you can look up that. I don't know. Is it like a RF amp or something like that? So, I'm not actually sure what these devices in here are. Haven't looked them up yet and

**Dave Jones:** splitting off and then we'll go through and we can start then seeing some RF filters and stuff in here and then are coupled here. There's a um RF uh transistor for what an RF amplifier for sure. They've uh

**Dave Jones:** And then it goes up here boom into another device, you know, all over the shop. And then we start getting into the RF wiggles in there. They're just putting in an inductor in there. All right, so let's see if we can vaguely

**Dave Jones:** follow the signal here. This is our tracking generator output. This is our 50 ohm output here. It's AC coupled. There's obviously some drivers here. So, we going actually backwards uh through this process. So, if we uh we've got a couple of

**Dave Jones:** other uh well, device. I have no idea what they're doing. I've no idea of the topology. We've got obviously some filter, maybe perhaps a mixer down in here. Perhaps. Then we've got some uh uh filtering it going on in there based on

**Dave Jones:** the PCB. Not sure what that one's doing. That's obviously an uh RF uh transistor down in there. Then it's going through. You can see then it just sneaks through a um gap in the wall of the uh shield

**Dave Jones:** down in here. Then we've got another 424LT3 device that we had down here. We had a couple of those 424LT3s. And then just off that we've got a a 74HC04 inverter. Look at that. Brilliant. Not sure what that puppy's doing in there,

**Dave Jones:** but uh anyway, we have some looks like we have uh some inductors there on the board. And then yeah, I'm going to probably get complaints about poking around on this board with a screwdriver. Shut up. Really, it's not worth

**Dave Jones:** complaining about. I know what I'm doing. And then it sneaks through. Ah, we've got another uh well, probably amp there. And then we've or buffer. And then we've got our controlling piece and impedance traces going through here. We've got

**Dave Jones:** another device there, whatever that is. And then we have some what's uh probably a band pass filter. Haven't looked at the uh topology. Haven't uh thought about it. But uh as I've mentioned in previous videos, those traces out you know, why do they have

**Dave Jones:** like a stub going out there like that? Well, that's actually an inductor in there and and it's got resistance as well and that actually adds acts as a capacitor there. So, you can actually have you know, low pass and band pass

**Dave Jones:** filtering and things actually integrated into the PCB and that's exactly what they're doing there. And then we're going over to whatever this little hybrid is here. Little apron hybrid. It's a uh uh Sim 24 MH. Whatever that is. Then

**Dave Jones:** we're going into a ceramic package. Couple of ceramic packages over here. H 564. Local oscillator uh LO 32. Okay. So, they're presumably uh local oscillators down in there. And we have our main control device. We'll have to rip that off. See

**Dave Jones:** what it is. Not sure. We have our board-to-board interconnect. Of course, there and check it out. We have a board-to-board RF connector. Doesn't that look funky? Geez, ET could phone home with that thing. And there we go. There's the mating RF connector

**Dave Jones:** through there. So, that's probably getting out the um you know, one of the local oscillator signals or something like that over to our uh tracking gen. And that's where we follow the signal around like that from our output way

**Dave Jones:** back here around there through what looks like band pass filter there. Through some local oscillators and stuff and back over to here. But then we've still got these isolated sections here. Some more filtering going on there. Uh you know, it could be like a low pass

**Dave Jones:** filter perhaps. And but these blocks, I mean there's a there's a connection between this block in here like this down to here, but it seems like that block is almost uh you know, um isolated. It could be something There's obviously There's

**Dave Jones:** probably something sneaking under through there perhaps going from there, jumping over to there, and yeah, maybe no, there's nothing going there. So, you know, these things are sneaking all over the place. You've got to be careful, but it almost looks like all of

**Dave Jones:** that is sort of its own isolated block there from this main path, which sneaks around here like this, all the way back there. Anyway, I don't have a block diagram of the tracking gen. I'm not going to try and reverse engineer it to

**Dave Jones:** get it out. If we take the other shield off here, we don't actually get anything all that interesting. Look at that, it's pretty barren. So, we should actually in like we've even got some, you know, basic SOIC packages here from Linear

**Dave Jones:** Technology. I can see and we'll go in and take a look, but here's the main RF input over here. Of course, I have to take out that rigid coax before I lift this board out, but uh yeah, nothing

**Dave Jones:** exciting there at all. As you can tell by the traces over there, that's another board-to-board interconnect, same as what we had up here, of course, and there could be another RF board-to-board. I'm not entirely sure. We'll find out, but

**Dave Jones:** yeah, let's lift that board up. There should be some more interesting stuff underneath, but first of all, once again, got our RF gasket there, and ooh, a couple of nice little traces in there. We'll check out, but let's have a

**Dave Jones:** look at some of the chips on the top first. USA, USA, USA. Well, this right here is a very interesting part of the circuit. I really like this. Check out what they've got happening over here, and trace snaking its way around there

**Dave Jones:** into this four-leaded device. I don't, you know, it's like it's, you know, a typical RF amplifier configuration kind of thing, but you know, it's just I didn't expect it to see in a square plastic package like that sort of

**Dave Jones:** rotated 45°. Bizarre, but anyway, yep, they've got some basic RF stuff happening there. I don't know what that is. Your guess is good as mine. If anyone's got any info, post it. And we've got ourselves a couple of

**Dave Jones:** Burr-Brown. I love Burr-Brown. They're now TI, of course, OPA4251 micropower op-amps. Nothing at all special there. If we move up here, I wouldn't even like to hazard a guess on that one. And then these devices, they're everywhere. Check them out.

**Dave Jones:** There we go. There's two of them there. There's another one over here. And then over here. Same device. Four of them. And on the flip side of that, uh got ourselves a RF gasket again. Ta-da! We have a couple of yeah,

**Dave Jones:** board-to-board interconnect and a couple of board-to-board RF connectors. And oh-ho, look at the back. Very sexy. Gold as far as the eye can see. Unfortunately, not something that we're going to be able to take apart cuz these things are

**Dave Jones:** usually um soldered completely shut. And yep, they are. I can't just pop the lid off that. It's not just like an RF can you can just pop the lid off. Oh, bummer. And we've got some interesting uh stuff

**Dave Jones:** happening down in here. Once again, no idea what that device is. RF section AT4 attenuator. Perhaps some sort of attenuator going on there. Low could mean a low-pass filter is going on on and there. If you want to know where

**Dave Jones:** that is relative to the other side, that one actually is the same block as that contains that funny little wiggle in there with uh that little amp or something down in there. So, that's the backside of that block.

**Dave Jones:** And what we've got under that little firmware tag there is an XC 2C128 Xilinx. That's actually not an FPGA, that's a CoolRunner CPLD, complex PLD. And we've got a couple of linear technology parts all around that. Not sure what they're

**Dave Jones:** doing, not going to look them up. Just little precision op amps or something like that. Not terribly exciting. Unfortunately, all the magic happens under these cans and we can't get to them. What's under that? Is that That wouldn't be an Is that an

**Dave Jones:** access port? Cuz that looks like copper tape. A copper No, what is it? Whoa, we've got ourselves a little hole under there. Little access hole. Wonder what's going on there. But that yeah, is sealed with copper tape. There, so it'll shield

**Dave Jones:** that. You know, we're talking about 20 gig here. Put a bit of spit back on that. She'll be right. No worries. But yeah, little access hole under each one of those. Got those lovely board-to-board RF interconnects again. Another LT part up there, but obviously

**Dave Jones:** not critical part of the anything outside of these shielded cans, of course. Nothing to do with the RF part of it there. Just basically control circuitry and stuff like that. So, nothing of terrible interest. Like likewise, this stuff around here. Yeah, it's inside the

**Dave Jones:** block. Over here, here's our block. There it is. The block has its own, you know, thing there, but obviously not quite as critical as what's deemed to be inside one of these shielded cans, but you know, still good enough to have all its

**Dave Jones:** own machine to block and everything else. That reminds me, I forgot to look at the vice on the Tracking Gen board. Yeah, exactly the same Xilinx CoolRunner CPLD for a basic control and interface. And somewhat curiously, this main block

**Dave Jones:** down here actually for the tracking gen has its own back end uh module on it like that. So, there you go. Maybe it's uh you know, independently uh tested or something like that. They assemble that as a block

**Dave Jones:** and then, you know, that's probably maybe a um a some sort of production uh test uh sticker or something like that. And then they test that separately and then just bolt it on there. That's the most likely scenario anyway, but they didn't

**Dave Jones:** do that with the rest of it here. They just That's all just in one integrated block.

**Dave Jones:** All right. That's 20 million bloody screws. All right. There we go. Got it. Got it. Got it. Woohoo! Uh check it out. Now, of course, none of this is going to make that much sense unless we do a basic block diagram here.

**Dave Jones:** And that's what I've done. If I basically a very uh top-level block diagram of how this thing is going to work. Now, over here we've got our RF input here and there's our RF input. We're going to have our attenuator

**Dave Jones:** section, of course. Uh it's a uh fully programmable attenuator, of course. That's going to be within inside this RF uh block here. Actually, uh on second thought, it could be entirely feasible that this board is just an attenuator

**Dave Jones:** board and that's uh basically it, just doing the input uh attenuation stuff and then all of the uh bandpass uh yeah, so basically, it could just be effectively um you know, just that on the front end. Maybe some extra

**Dave Jones:** filtering or something, but it's uh entirely possible that all of the you know, the spectrum the traditional spectrum analyzer stuff of the uh uh local oscillator with the uh filters and the mixers and everything else, the multi stages of those, is actually all

**Dave Jones:** done on the more complex board. Really, it makes sense because the uh the you know, the performance of these things absolutely critical that the input attenuators and you know, input preamps and stuff work absolutely you know, perfectly. So,

**Dave Jones:** that's why these are the only things that are effectively double shielded like this. I mean, they've got their own shielded can inside the already shielded block. Absolute critical performance in terms of noise floor and stuff like that. So, yeah, I reckon

**Dave Jones:** that's just the input board effectively. And that is likely popping out of one of our RF connectors here or here which correspond to that connector there and that one there. So, that one pops in just about there. Sorry, this side here

**Dave Jones:** pops in on this corner over here. That looks That looks like it could be a bandpass filter in there off to the ADC and then we've got all sorts of control stuff or it could actually be this one

**Dave Jones:** over here cuz that looks like an extensive bandpass filter as well. We'll take a good close-up look at that. Probably a mixer somewhere in there. I don't know. I'm not going to follow this all the way through and trace it, but

**Dave Jones:** it's going to have that basic functional block diagram. There's lots of control stuff and other things on here which we won't bother with, but of course the ADC as we saw is back on the main board. It's not actually on this

**Dave Jones:** particular board. There'll be no surprises under there. That'll be another cool runner Xilinx control chip, but that's about it for the block diagram. Of course, the ADC's ain't going to go into the DSP. So, all that is on the second board. So,

**Dave Jones:** I don't know. These bloody spectrum analyzers are incredibly complex beasts, let me tell you. I don't know. If you want to figure it out, go for it. So, there's our board-to-board RF interconnect there and that's of course jumping straight through there. You can

**Dave Jones:** see the lack of vias as it's jumping through series termination resistor there, through to here, up to here, and that looks like it's some sort of band pass fixed band pass filter. Of course, these big fans going off here, they're

**Dave Jones:** actually acting as capacitors. We've got little inductors in there. So, that is going to form a filter. And then of course, the output of there looks like it jumps up into here, into this device, and it comes around here. Some more

**Dave Jones:** filtering action happening there, and then we've got some more filtering, another band pass filter. You might think, "How does this work? It's not even connected." Well, of course, two plates like that is a capacitor. So, that signal can actually jump

**Dave Jones:** all the way over to there. No problem whatsoever. That's RF PCB design for you. Then we've got various Then we've got another amp here. Then we have looks like a uh a turn. Maybe that's like acting as a

**Dave Jones:** controlled impedance transmission line or something, perhaps. So, they've got a various mix of technologies, and we won't go into uh details on those. I've explained that a bit in previous videos, but apart from that, that looks like it

**Dave Jones:** ends the RF Oh, view didn't No, no. There we go. We've got another one over here. There we go. We've got another a filter happening over here. And once again, instead of the fans, they've got the little pads there. Lots of technology of

**Dave Jones:** course goes into actually designing these things and ensuring that their performance, um you know, is is smack on target. Because you can get uh better performance on the PCB than you do using uh discrete uh components. It's, you

**Dave Jones:** know, a very controlled impedance material they've got in here. They'll know the exact uh dielectric constant and characteristics of it. They can program that into their um RF uh filter layout programs, which then you can simulate and design all

**Dave Jones:** these things, but there you go. That is There's lots of sections on here, and I could uh try and decode it until the cows come home. Unfortunately, I have to go home, but I don't think the fun's over yet

**Dave Jones:** because if we pop it over, I think we're going to see a bit extra on the bottom here. Oh, hello. In fact, we get a lot extra. Look at that. Oh, beautiful. Wow, that's more than the top. Fantastic. We've got

**Dave Jones:** more little hybrid modules down there. I'm not going to look up the number. They're probably like you know, from Mini-Circuits or someone like that, one of the uh providers of such thing. We've got some complex filtering network happening here. Your

**Dave Jones:** guess is as good as mine if any RF experts out there want to actually tell us the exact you know, configuration and performance of that thing, please do. But that is absolutely brilliant. But as with all of these, you can see the signal flow. I

**Dave Jones:** mean, you know, there's obviously signal flowing through just that little gap there on the inner part of the board, then we're going through our complex network over to here. It's jumping over to here. This is probably jumping over

**Dave Jones:** to there. More low-pass and band-pass filtering happening there. Another one of those hybrid modules jumping over there. Once again, the signal just jumps straight through there on the bottom side of the board, goes up. Blah, blah, blah, all over the place, and then these

**Dave Jones:** cans look interesting. Let's take a look at those. And that's a Z-COMM CRO 3750A-LF. That's a voltage-controlled oscillator module. And if we jump up here, what do we got there? Another VCO by the looks of it, but another manufacturer, SMDI.

**Dave Jones:** I presume it's a VCO, VCO 190. Ah, look at that. That's a thing of beauty and a joy forever. Beautiful. Somebody had fun there. Ah, let's just, you know, rotate them at the odd angle there. Little bit of inductance just, you know, sneaking

**Dave Jones:** through on there. Beautiful. And then the capacitors either side. Ah, more funny business happening on that one. Check it out. They decided, oh, let's put a little extra loop up there. Wonder what that does. Oh, check it out. You can practically

**Dave Jones:** see the waveform coming out of that thing. So, that folks is all she wrote on the teardown. Unfortunately, I'd love to go into like a, you know, details and do schematic like overlays of each block and stuff like that, but that would take

**Dave Jones:** all day. It really would, or more. Absolutely phenomenal. So, I hope you enjoyed that. A big, um, uh, thumbs up to, uh, the Agilent RF division for, uh, sending this in for the teardown. Oh, pretty gutsy. I hope it goes back

**Dave Jones:** together. Hmm. I don't know. We'll see. Anyway, I'll reassemble the thing tomorrow, and hopefully it will work. But, that's it for the teardown. And if you want to, um, by all means, go through and the like, uh, what some people have done for

**Dave Jones:** the previous ones, you know, go in and actually, uh, decode all the different blocks in there, but, you know, um, jeez, it's, you know, it's pretty complicated. And you can see that each one has its own individual shielded, you

**Dave Jones:** know, section components both sides. Brilliant. We've got our voltage control oscillators, our local oscillators, our band pass filters, all sorts of RF magic. And don't you just love the, uh, filters on the PCB. Absolutely brilliant. I love that, but

**Dave Jones:** that's inside a, uh, $18,000, um, high-end Agilent handheld spectrum analyzer. So, huge thumbs up to the guys at Agilent for sending that through. And if you want to discuss it, jump on over to the EEVblog forum. That's the

**Dave Jones:** place to do it. Catch you next time.
