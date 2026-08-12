---
video_id: SFrUINyYcEA
title: EEVblog #1262 - Designing a Flex PCB + uSupply Update
url: https://www.youtube.com/watch?v=SFrUINyYcEA
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 25, "3": 39, "4": 50, "5": 62, "6": 79, "7": 94, "8": 106, "9": 121, "10": 144, "11": 160, "12": 169, "13": 184, "14": 202, "15": 219, "16": 237, "17": 247, "18": 258, "19": 266, "20": 280, "21": 297, "22": 313, "23": 341, "24": 353, "25": 368, "26": 381, "27": 397, "28": 413, "29": 425, "30": 445, "31": 462, "32": 471, "33": 486, "34": 497, "35": 510, "36": 521, "37": 534, "38": 548, "39": 569, "40": 585, "41": 600, "42": 609, "43": 621, "44": 630, "45": 647, "46": 665, "47": 688, "48": 700, "49": 709, "50": 722, "51": 733, "52": 749, "53": 757, "54": 766, "55": 781, "56": 800, "57": 809, "58": 818, "59": 833, "60": 855, "61": 870, "62": 883, "63": 892, "64": 914, "65": 920, "66": 930, "67": 942, "68": 953, "69": 962, "70": 977, "71": 985, "72": 997, "73": 1010, "74": 1022, "75": 1041, "76": 1050, "77": 1064, "78": 1073, "79": 1083, "80": 1103, "81": 1115, "82": 1122, "83": 1133, "84": 1146, "85": 1175, "86": 1184, "87": 1202, "88": 1212, "89": 1225, "90": 1243, "91": 1251, "92": 1266, "93": 1274, "94": 1291, "95": 1308, "96": 1326, "97": 1339, "98": 1357, "99": 1368, "100": 1388, "101": 1397, "102": 1408, "103": 1413, "104": 1424, "105": 1441, "106": 1456, "107": 1470, "108": 1483, "109": 1495, "110": 1505, "111": 1525, "112": 1536, "113": 1547, "114": 1559, "115": 1570, "116": 1586, "117": 1602, "118": 1613, "119": 1625, "120": 1633, "121": 1642, "122": 1657, "123": 1667, "124": 1677, "125": 1688, "126": 1696, "127": 1708, "128": 1721, "129": 1736, "130": 1749, "131": 1765, "132": 1776, "133": 1788, "134": 1799, "135": 1809, "136": 1825, "137": 1845, "138": 1852, "139": 1862, "140": 1870, "141": 1881, "142": 1891, "143": 1902, "144": 1915, "145": 1924, "146": 1934, "147": 1945, "148": 1955, "149": 1965, "150": 1979, "151": 1999, "152": 2012, "153": 2027, "154": 2043, "155": 2061, "156": 2073, "157": 2082, "158": 2095, "159": 2108, "160": 2120, "161": 2133, "162": 2145, "163": 2156, "164": 2170, "165": 2181, "166": 2196, "167": 2209, "168": 2216, "169": 2227, "170": 2238, "171": 2248, "172": 2258, "173": 2269, "174": 2286, "175": 2308, "176": 2325, "177": 2341, "178": 2355, "179": 2370, "180": 2385, "181": 2397, "182": 2407, "183": 2426, "184": 2444, "185": 2453, "186": 2471, "187": 2480, "188": 2495, "189": 2508, "190": 2517, "191": 2528, "192": 2537, "193": 2552, "194": 2566, "195": 2578, "196": 2594, "197": 2608, "198": 2617, "199": 2633, "200": 2650, "201": 2662, "202": 2676, "203": 2687, "204": 2699, "205": 2708, "206": 2721, "207": 2729, "208": 2740, "209": 2755, "210": 2764, "211": 2785, "212": 2811, "213": 2821, "214": 2838, "215": 2850, "216": 2865, "217": 2873, "218": 2885, "219": 2902, "220": 2919, "221": 2936, "222": 2948, "223": 2964, "224": 2976, "225": 2993, "226": 3009, "227": 3019, "228": 3031, "229": 3042, "230": 3050, "231": 3062, "232": 3073, "233": 3083, "234": 3099, "235": 3111, "236": 3131, "237": 3141, "238": 3159, "239": 3172, "240": 3190, "241": 3203, "242": 3213, "243": 3232, "244": 3244, "245": 3256, "246": 3265, "247": 3276, "248": 3284}
---

**Dave Jones:** Hi, in a recent video, which I'll link in, where I explained all of the PCB manufacturing options that a typical manufacturer would give you when you go and check out and get your board manufactured.

**Dave Jones:** And I asked in that would people like to see one on flex PCBs and a ton of people said yes. So a flex a full on flex PCB video will have to follow this cuz it'll be quite in-depth.

**Dave Jones:** But as it turns out um just yesterday we had a requirement come up for a flex PCB adapter that we required for the new micro supply project. So I thought we'd just take a look at rather than just me do it and just send it away.

**Dave Jones:** I'll press record and we'll talk about the various options here. So this won't be an in-depth flex PCB tutorial. This just happens to be a real world thing that we need for the micro supply.

**Dave Jones:** If you want to see the micro supply, tada, here it is. Doesn't it look sexy? Here we go. Oh, look at that. Micro supply. Beautiful. Thing of beauty, a joy forever.

**Dave Jones:** Doesn't have the LCD in there, but anyway. Um yes, this actually really does exist and we have it working and as it turns out we just got the USB power delivery circuit of it working the other day and herein lies the problem.

**Dave Jones:** And it this video will start out with a rant about ST as in ST semiconductor because well, we've had an issue with this. So let's take a look at it before we get to the flex PCB.

**Dave Jones:** Well, bloody Altium Designer first time I'm using version 19 actually and I get object reference not set to instance of an object. I don't know. Whatever. Send it. Do I have to send and close?

**Dave Jones:** Can I just close? I don't want to send and close. Here we go. Anyway, this is the schematic for the USB portion of the the isolated USB side of the micro supply and yes, micro supply videos will come in due course.

**Dave Jones:** And what we've got over here is we've got an STM 32F070F6P6TR microcontroller cuz all those letters on the end matter. That's rant number one. The STM32F070 micro is very different depending on the letters you put on the end of it and it's really freaking annoying.

**Dave Jones:** Anyway, so in the hardware prototypes that we've built, we chose this relatively low cost STM32 micro cuz we're also using STM32 micro as the main micro on the isolated side as the main control element as well.

**Dave Jones:** And it's a little 20-pin TSOP package and it's got 32K of flash. We thought 32K of flash is plenty cuz we you know, we don't need to do much.

**Dave Jones:** All we need to do is some USB power delivery configuration type stuff and of course USB comms like serial type comms, HID interface stuff and you know, things like that.

**Dave Jones:** And it seemed at the at the time, it seemed like a good choice. 32K was plenty. But as we've found out through great personal anguish mostly on David's side, personal anguish of the development of this thing, USB PD libraries that come from the manufacturer are actually huge.

**Dave Jones:** They're enormous and we actually chose a Richtek part down here. It's the RT1716 and that's the USB PD controller. So you can see these lines here, CC1 and CC2.

**Dave Jones:** They're control lines which go over to the USB-C connector here. Over here, CC1, CC2 and they actually configure the USB power delivery specification. They negotiate how much power you can, you know, the host can deliver and how much the load needs and all that sort of stuff.

**Dave Jones:** And then we want wanted to do it properly. By the way, when we chose this micro, as we'll look into another ST micro that had USB power delivery built-in was not available.

**Dave Jones:** The Well, the cheaper version of it wasn't available, as we'll see, at the time of making that uh decision. But, and the one that did, I think was was grossly more expensive.

**Dave Jones:** So, it was a cheaper solution to go for this two-chip solution here for uh So, the STM32, of course, has USB built-in. Here it is here, USB. There it is.

**Dave Jones:** There's the uh twisted pair up there. And so, it's got the USB controller, but the USB power delivery is handled via the I²C bus down here in this little uh tiny eight-pin um RT17 Richtek RT1716.

**Dave Jones:** As it turns out, which we didn't know at the time, the Richtek library for USB power delivery is enormous. So is the ST micro one. The ST micro one is uh I think it's like 2 megabits or something enormous like that.

**Dave Jones:** And the Richtek one was huge as well. And David's actually And it wouldn't fit. Neither of them would fit in the 32K of flash on our STM32 micro, let alone all the other stuff that we wanted to put in, the serial comms, the HID, and the uh US regular USB stuff, and, you know, all sorts of stuff.

**Dave Jones:** Just the power delivery library was absolutely enormous. So, um yeah, uh David's had to work with uh the design engineers at Richtek to get the the library down, and we've finally got it pruned down where we can actually fit the Richtek USB PD library into the 32K of flash on this ST micro that we're using.

**Dave Jones:** Unfortunately, uh we can't fit anything else. So, we can't fit all our other and maybe if we keep working with them uh for longer, we might be able to get it down further where we can just squeeze everything in this 32K.

**Dave Jones:** But anyway, we've decided bugger that, we're just going to put in a larger micro. And of course, Murphy's law says that the package we chose, this 20-pin TSOP package, the largest part is a 32K part.

**Dave Jones:** So to get say a 128K part, we have to move to an entirely different package. And at this stage, we've got like half a dozen prototype boards built up, and you know, they cost a fair bit to get these manufactured, and they're all working.

**Dave Jones:** So we don't want to just scrap those and have to rebuild boards from scratch on a tight timeline at the moment. And like we just want a little flex adapter board that converts a TSOP package like this into a larger footprint for the larger part.

**Dave Jones:** Right, so here's a photo of the board here, and this is the offending chip right here that we have to convert. So what we need is a flex PCB because you can't really do this with a rigid.

**Dave Jones:** This is where a flex PCB comes in real handy. What we need is some sort of flex PCB which goes like this up here like this and goes down there like that.

**Dave Jones:** Please excuse the crudity of the model. Didn't have time to build it to scale or to paint it. There's our new chip which is a quad flat pack. And then we will have pads on here like this with little via holes in them so that we can actually solder down to this board here to the existing pads.

**Dave Jones:** So we remove this chip, we get our flex PCB which is very thin polyput the kettle on material, polyamide material, that is it'll be like a regular double-sided board, but it'll just be flexible so that we possibly fold it up or something like that.

**Dave Jones:** Although, you can see that this connector is in the way here. So, we could go So, we could actually, you know, do it something like this, perhaps. That might work.

**Dave Jones:** And But, then you've got it's a quite difficult cuz these are very thin. You got to get down and solder it onto the pads down here. We might have to physically remove this capacitor here, but that's okay.

**Dave Jones:** That little tiny BGA there, that's that Richtek package. Isn't it a little pain in the ass? Anyway, it's cheap and it does USB micro USB power delivery negotiation stuff in it.

**Dave Jones:** So, yeah, that's you know, so we need some sort of flex board. So, at this stage I'm thinking something like that. But, the issue here is, okay, this is a real fine pitch.

**Dave Jones:** I think it's I'll have to double-check. I think it's 0.5 mm pin pitch. So, it's a real pain in the ass. So, you know, really if There's a couple of ways we can do it.

**Dave Jones:** Either to have little vias on the board on the flex like that, then you just put your iron on top of that and put your solder on, and then it just flows down through the vias and attaches to the pads underneath.

**Dave Jones:** And you could actually stagger your vias like this. Perhaps, you know, that's a common technique used on you know, LCD ribbons and all sorts of you know, commercial products like that.

**Dave Jones:** That just gives you a bit more clearance there to do those pads. So, we could do that. Or, what we could actually do is have our flex going like this through the pads like this, and then have little castellated pads on here.

**Dave Jones:** Right? Little half moon castellated pads. And I've shown those on I'll do exaggerated here, okay? So, imagine that's one little pad and then you slice through them just like you would on a regular FR4 fiberglass PCB.

**Dave Jones:** You can do that on flex as well and then you could like sort of like just solder in like that and then the board could actually be like this if we didn't have room up the top here.

**Dave Jones:** Like cuz you know, we've got this in the way. This is a large package. So, that the flex would have to flip up like that and we could you know, it it it gets a bit messy.

**Dave Jones:** So, we could have a flex shape like that for example and then all of your traces just run around here like this and then you know, our chip can just be flapped around in the breeze over here.

**Dave Jones:** No problems whatsoever and then we don't need to fold the flex. But, there's lots of things. This is what I'll go into in if I do a specific flex PCB, but I'll just touch on something like this.

**Dave Jones:** Like you wouldn't do right angles like this on a flex. You you round everything. On flexes you round everything including you wouldn't do your traditional right angle traces like 45° traces like that.

**Dave Jones:** On flexes you want to round your traces like that. So, when it flexes there's less uh you know, mechanical stress on sharp junctions and stuff like that. So, you want to just you know, radii everything like that.

**Dave Jones:** Just because it's nice for flex because they flex and you don't want sharp corners when things flex. All the mechanical engineers can tell you all about that. So, even though this board that we're doing for this particular application won't actually flex so to speak, it'll just sort of you know, sit relatively flat like this on top of you know, the existing chips and things like that.

**Dave Jones:** Just be careful if you've got exposed pads on the bottom. Uh make sure they don't short out to the tops of any other components and things like that. So, you'd have to put some sort of insulative layer on the back.

**Dave Jones:** So, you can actually have another layer of poly put the kettle on material stuck on the bottom of your board so that none of your vias are exposed. And of course, you could do tented vias and stuff like that.

**Dave Jones:** But just be careful that you don't nothing shorts out cuz if you had a via that just happens to be here and it was an exposed one and then that's sitting flush on this on the top of this capacitor here which is going to be larger than the physical height of the resistors there.

**Dave Jones:** Oops, you can come a gutser and it's short and it might be intermittent and that'll really ruin your day. Murphy didn't ensure that it'd be intermittent at the worst possible inconvenient time.

**Dave Jones:** Yeah, so I'm not actually sure how I'm going to run this one. Whether or not I'll shape it. I I think I'll put the chip cuz there is Well, there's not room for it here, but here there's room for it before it gets to this planar transformer up up the top here.

**Dave Jones:** So, there's certainly room for the chip cuz as we'll see in a minute, it's not a huge amount bigger than this one here and even though it's a quad flat pack.

**Dave Jones:** But you know, as I said, it's got to like go on the top of this and it's got to sort of bend upwards and I don't know. Six of one, half a dozen of the other.

**Dave Jones:** Like it I I I haven't chosen yet. I'm about to lay this out and I haven't chosen which way to do it. Like whether or not I go for like little holes here like this, whether or not I just go for little holes like this, little vias like that, staggered vias.

**Dave Jones:** That'll that'll probably and just just have the board shaped like that. I think I think that'll probably do the business. I Yeah, I'll just run with that cuz then we can we can remove that capacitor and we can either put it on top of the flex or we can do some months in and physically take out the capacitor because it's not you know, it's not a big deal.

**Dave Jones:** It's just a bypass cap and well, you know, you can put it on the flex if you want. I could put a pad down for it, but eh, it'll work.

**Dave Jones:** So, anyway, that's the story behind what we're doing today. We're going to manufacture a flex manufacture manufacture. That's a new word. I'm going to run with that. We're going to manufacture a new flex piece PCB.

**Dave Jones:** Just a mod PCB that literally has just the two, well, one chip on it plus a pad to solder down uh onto the top of this chip here. And you would design this like you would any other PCB.

**Dave Jones:** There's nothing special about flex PCB design here unless it does actually flex. And then as I said, you want to use curved traces. Uh by the way, bend radius of uh flex PCBs, uh you as a general rule of thumb, you want to keep the bend radius to 10 times at minimum 10 times the thickness of the material.

**Dave Jones:** So, if the material is, you know, half a millimeter, you the bend radius you want at least 5 millimeters. That's just a rule of thumb. So, I think with the pin pitch, we're probably going to have trouble with the castellations on here.

**Dave Jones:** I don't like our chances of getting castellations with 0.5 mm pin pitch on a flex. I've never actually tried it at that pitch before, so I I don't know.

**Dave Jones:** I think I think the safer option is just to go for um staggered via arrangements like that, and we'll just let the solder flow down through the vias like that.

**Dave Jones:** I think we'll give that a go. Right. So, let's go over to the adapter schematic here. And what we've got is uh we've just got the two chips. The new one is an but it's the CBT6 as opposed to the F6P6TR chip.

**Dave Jones:** God. I TR I you don't need the TR. TR's just tape and reel. Um that's just the package that it comes in. I've I've a whole video on that, haven't I?

**Dave Jones:** I'm sure I have. Hmm. Anyway, but this new chip has more pins, which we don't need. Uh but it it comes in a quad flat pack, hence why we need this little flex adapter board.

**Dave Jones:** But it's a functionally identical chip, except it's got 128k of flash. So, let's actually, just for a rant, let's go look at the ST website. So, uh David is starting He used to like ST.

**Dave Jones:** He was a bit of an ST fanboy, and then he started to greatly dislike them because they would uh and now it's all these chips without having like a real proper support for them and stuff like that.

**Dave Jones:** And this STM32G0 series, which is a new one, as I said before, this wasn't out. This wasn't available when we originally uh chose the chip for the micro supply.

**Dave Jones:** The development's been quite some time. So, it it is a new one. Bloody modern websites. Look at this. USB PD. USB power delivery. The STM 32G, this is their new value series line, has USB PD in.

**Dave Jones:** So, we can completely get rid of, well, a couple of bottom bottom items here. Not only the Richtek chip, but also these resistors here for the pull-ups, a couple of caps here.

**Dave Jones:** We can consolidate our bomb, and it's cheaper. But aha, it ain't that easy. Because if you're if you're just reading the the top level here, you might think, "Oh, fantastic.

**Dave Jones:** USB PD." But let's go have a look at the data sheet, shall we? While you're searching for the data sheet for power delivery, you search for USB. And what?

**Dave Jones:** There's no mention of USB. Wah. Wah. Wah. Wah. Not only, if you actually go into the correct data sheet, not only does it say for the USB power delivery, it just says, "Oh, data coming soon." or whatever.

**Dave Jones:** Um There there is no USB controller inside this thing. So, we've come a gata right there. But if you were looking at uh sort of like the top level things like this, just trying to pick a micro at at like first shot, You might see oh, it's got USB PD, but it doesn't have an actual USB transceiver in it.

**Dave Jones:** So, it's absolutely useless. So, we can't use that value line series. What we have to go to if you go I will I'll save you the time of going through all the parametric searches and stuff like that.

**Dave Jones:** Well, you have to actually go to the G4 series down here before you can find one that has USB um interface with power delivery including the physical layer like that.

**Dave Jones:** And that one is about three times the cost of the dual chip solution with the Richtek power delivery controller and the F series micro that we're going to choose.

**Dave Jones:** So, yeah, it's not we've we've come a cropper there. Anyway, they've got a wanky video over here. I won't bother playing it, but it's how to create a USB power delivery sink in less than 10 minutes.

**Dave Jones:** And it goes through and you've got all the it doesn't explain Well, it doesn't explain No, music. And it just you know, it's it's using their their cube software or whatever and it just it's not explaining anything.

**Dave Jones:** It's just say do all this, do all this, do all this and you can implement a USB power delivery in 10 minutes, but it it ain't that easy. But you have to actually I think you have to contact them to get this library.

**Dave Jones:** You might even have to pay for it or something like that. I do I don't know. I don't want to know the details, but yeah, it it just isn't this easy.

**Dave Jones:** They they don't explain anything. So, it's anyway, that's the that's their new cube software. Apparently, you know, they make it out to be you know, you can just snap your fingers and you've got USB power delivery.

**Dave Jones:** No. Um talk to David about this if you want. It is USB power delivery implementing it correctly and thoroughly is pretty horrific experience. Okay, so let's actually go down here.

**Dave Jones:** USB PD dead battery support. The content of this section will be provided later. Thanks a lot, ST. Like, yeah, you're buying to these chips, they advertise them, and yeah, you might design it into your design, and then you go it if you didn't read this, you might go, "Well, how do I implement my USB PD?" Uh yeah, do I follow some little YouTube tutorial video with all wanky music on

**Dave Jones:** top, and that's it? Like, it it's just no. No, no, no, no, no. So, yeah, ST, pain in the ass, but then again, you know, a lot of manufacturers, Richtek hasn't been ideal, for example.

**Dave Jones:** Uh the Richtek one is unfortunately not open source. Come on, Richtek, open source your USB PD. Anyway, we're trying to work with them so that all of our firmware and implementations will be open source, but I think we're going to have to rely upon some Richtek binary libraries, unfortunately.

**Dave Jones:** But they're trying to strip out all of the we're working with them to strip out all the crap so that we can get a minimal implementation of USB PD that we need.

**Dave Jones:** So, yeah, otherwise, it's just it's too big, and they've got undocumented registers, and we've had to get special spreadsheets from them which document these undocumented registers, and well, to document these undocumented registers.

**Dave Jones:** There's a phrase. Anyway, which detail these registers that we didn't know anything about cuz we found it in the software. They're accessing these registers that wasn't in the data sheets and app notes and things like that, and we had to ask them what what's going on, and they do have the details, but yeah, they don't make them relatively public.

**Dave Jones:** So, like, a lot of manufacturers are like this. They just Oh man, the devil's always in the detail. Anyway, what are we, 30 minutes into the video already? Sorry.

**Dave Jones:** Anyway, we've got a PLCC chip, and we want to convert that to an STM32 like package over here. So, we've got the adapter PCB. Now, here's where you can come a cropper real easy.

**Dave Jones:** So, this is our uh chip, obviously the red it's on the uh top layer there, as you can see. And then we've got a bottom layer down here. So, we've only got a two-layer PCB.

**Dave Jones:** Like I said, we won't do anything different to a regular We wouldn't design this any different to a regular PCB. It's going to be exactly the same as you would lay out except uh you when you go to the checkout of the manufacturer's website, you'll choose flex PCB instead of this.

**Dave Jones:** Now, because this is a 100% flex PCB. It is not what's called a rigid-flex PCB, which I'll show you. This is an example of a rigid-flex PCB. It's like I can't make these bend that I'm aware of.

**Dave Jones:** Anyway, um you can see that these uh they've got some caps and I presumably they're they're LEDs, right? So, um yeah, those those caps and LEDs are on this flex PCB section, and then you've got two other uh rigid boards, hence the name flex-rigid, and that's got a battery on the bottom like that.

**Dave Jones:** I don't know what this board does, just an example which came with Altium. When I do my video, I might show a more uh complex example. But, you can see how the flex material, in this case, usually it's uh sandwiched in the middle.

**Dave Jones:** So, if you've got a four-layer board, for example, then your uh flex material will be the two inner layers, and it extends into the PCB so that you can then fold the boards up like this and create all sorts of You can make as many boards as you want.

**Dave Jones:** But, you basically lay these out as one big uh PCB. Like, you've got multiple PCBs, but it's effectively done as one large board including all the separate You can have as many of these as you want.

**Dave Jones:** You can have 10 different rigid PCBs like this all connected with all these flex functionality. Uh do I have an example? Now, here's an example of a uh traditional uh PCB that's connected with a flat flex and you can see the ribbon connector cable there and on the other end of the board over here, okay?

**Dave Jones:** And of course you need the connectors and well, that's you know, expensive extra bomber items, more things that can go wrong or you can integrate I'm sorry, I don't have the best example.

**Dave Jones:** We'll get a better example next time. But in this one here, you can see that this PCB, if I flip it over, is actually flat flex on the bottom of the PCB.

**Dave Jones:** It's not in the inner layer as I said, but it's on the bottom. And then they've got this extra bit over here which then goes off to another board.

**Dave Jones:** So it's all integrated so you don't need the connectors on there. And that's what they're doing here. You don't need any connectors cuz this flex PCB here extends as a layer inside the PCB.

**Dave Jones:** Now as I said, ordinarily you would wedge it, sandwich it in the middle so it'd be the inner two layers of the PCB because I ordinarily I wouldn't recommend that you put it on the outside like this one because it it doesn't flex.

**Dave Jones:** There's more stress and the adhesion can come off and stuff like that. It is more rigid, no pun intended. I'm here all week. When it's sandwiched in the middle, but you can put it on the bottom like this and the manufacturers will do whatever you want.

**Dave Jones:** But you can see that the bottom layers like that the flex PCB. And that is called a rigid flex cuz it can combines rigid FR4 PCBs with flex. But in this particular case, we're not going to do this.

**Dave Jones:** We're going to have flex. And if you want to see how that works in the layer stack manager here, like here it is. Here's the bottom layer here. They've actually specified the bottom layer as poly put the kettle on polyimide material.

**Dave Jones:** So the the dielectric one dielectric twos. So this is actually a four layer board, but it's got so they could have put it in the middle, but they've actually sandwiched it and they've specified the polyimide on the bottom.

**Dave Jones:** Now this isn't the sort of data that would be automatically given to the PCB manufacturer. This is the sort of data that you might you could just specify in the Gerber.

**Dave Jones:** You could just say, you know, like instructions on the Gerber or instructions in an email or whatever. You can just say, "Right, my bottom layer is the polyimide material, so the flex on the bottom." Or if you wanted the flex on the top, you wouldn't actually have to change So, if we go into single layer mode here, you can see that the that's the layer on the on the

**Dave Jones:** top layer, then the middle layer is there's no copper on the flex at all because there is no flex in the middle layer. It's it's only when you get to mid layer two or the one from the bottom that this one is flex.

**Dave Jones:** So, you can see like the bottom layer is all flex, it's all ground plane. By the way, another recommendation is not to use solid ground planes like this on flex wherever possible.

**Dave Jones:** Usually, you would crosshatch them. So, you might put your plane out here like this, but then I'd start my crosshatch from inside here, and then all of this would be a crosshatch ground fill.

**Dave Jones:** And you might if you tear down products, you might see that commonly is that they'll use a crosshatch ground fill, and that's for thermal and flex and stress reasons, which all the mechanical engineers can no doubt tell you about.

**Dave Jones:** But once again, that's another like rule of thumb. Unless you absolutely need a solid ground plane, you would do flexes as a crosshatch. But when it goes inside the board like this, you can certainly make it solid because it's it ain't flexing when it's sandwiched inside that fiberglass.

**Dave Jones:** And just here's an example here's some examples of rigid flex PCBs. So, this one here you can see that they've got the two copper layers in the middle, then there's adhesive polyimide insulation with adhesive in there.

**Dave Jones:** There's another adhesive in there. Then you got the FR4 prepreg. So, these are your rigid FR4s over here, and this is your flex material sandwiched in the middle. But as we're showing on the Altium example, we've got that flex on the bottom two layers.

**Dave Jones:** So, this bit copper here and this copper here are done and manufactured as a flex. Then they manufacture the FR4 fiberglass ones separately, and then they'll stick those on the top.

**Dave Jones:** And it's generally nicer if you do it as a big panel like this, for example. That that one's only got two separate boards, but you can see how they've designed those as a flex.

**Dave Jones:** That one's got a little like a LCD connector or something, you know, some sort of ribbony thing at the bottom. So, I only got some mouse bites on there.

**Dave Jones:** So, that's you know, that's quite quite a nice design. And there's just two boards with some flexes sandwiched, and then there's ones with multiple that might that might have it look that looks like it's got a like an RF connector on there or something like that.

**Dave Jones:** You know, more advanced ones like this. And you know, it can get really cool. But we're just going to manufacture a simple and solder directly onto a flex PCB.

**Dave Jones:** So, you leave out the word rigid. So, we're basically doing like a flex PCB like that. We're going to solder our components directly on to the polyimide material instead of fiberglass.

**Dave Jones:** That's the only difference. So, from a like a design point of view, it it really is if you're just doing flex, there's no difference. You just specify flex in your checkout.

**Dave Jones:** That's it. You might have to make it have a few design considerations for the flex mechanical flex part. But apart from that, the design process is exactly the same.

**Dave Jones:** So, there you go. It's going to fold. This is Altium design here. It's just going to like flex around like this. It folds up, and then so the two boards like that fold up like that.

**Dave Jones:** And then the flexy bits go around the outside into a like a like a hockey puck puck configuration or something like that. And once again, this isn't really an extreme flex board.

**Dave Jones:** Like there's nothing really inherently like 10 years ago getting one of these manufactured very specific, you had to find a manufacturer who was willing to do it. Now, it it's practically a shopping cart checkout um at some manufacturers, anyway.

**Dave Jones:** Basically, all you got to do is tell them in your layer stack up on your Gerber's or where wherever you tell them it which layers are polyimide flex material and which layers are fiberglass material and they'll just do it.

**Dave Jones:** Easy peasy. They'll just choose the material and get the get the job done. And of course, and then they'll when they sandwich them all together, all of the vias from the uh flex uh layers will automatically line up with the and be bonded to the vias on the uh rigid PCBs.

**Dave Jones:** But, from a PCB manufacturer's point of view, the construction's exactly the same as a multi-layer PCB. They don't care that you're using a flex material instead of a rigid material.

**Dave Jones:** There might be a few little process, you know, things in there, but basically, they don't care whether or not they're making an eight-layer rigid board or whether they're making an eight-layer rigid-flex combination.

**Dave Jones:** It's just that one of the inner layers is made out of polyimide instead of fiberglass. Anyway, I'm getting way too much into that. So, now, here's where you can come a gutser.

**Dave Jones:** As I said, right? You got to got to be very careful here. Now, this is of course all all your PCB designs are always done looking through the board.

**Dave Jones:** So, this is the top layer um by definition, it's the top layer, so it's the red uh layer here, okay? So, this is pin one over here. Now, ordinarily, this one, pin one's in the correct configuration for the chip, but you'll notice it's blue.

**Dave Jones:** It's on the bottom. So, this one's actually been flipped twice. Not only is the component been flipped from the top side, the red side, over to the blue side, but then it's been mirror imaged like that because we have to connect down to another board underneath which has this particular pin configuration.

**Dave Jones:** So, if you didn't realize that, you could completely come a cropper and get your footprint back to front. So, anyway, we're just going to have a chippy on there.

**Dave Jones:** Haven't defined the board outline yet. But yes, we're going to have a pad This won't be a chip. This will just be some vias. So, what we need to do now is go in here.

**Dave Jones:** Geez, look at that expansion on those pads. That's a bit how you doing. That's touching. Look, there's no solder mask Slew though, if we go into 3D view, look at this.

**Dave Jones:** Look at this. There's no There's no solder mask. No solder mask between pads there. I could easily bridge your solder out. So, our solder mask expansion is too big.

**Dave Jones:** So, we're going to have to change that. Solder mask expansion, 4 mil. So, we'll change that. So, that's coming from the rules. We could have changed the rules, but you know, like who cares?

**Dave Jones:** Doesn't matter. This is We're not worried about this. There we go. 1 thou solder mask expansion. That'll do it. So, now, if we go in here like this, bloody error markers.

**Dave Jones:** There we go. We've got solder mask between our pads now. That's a Christmas miracle. So, we can flip that over and you can see there's a chippy there. But of course, there won't be a chippy because that will just have pads.

**Dave Jones:** Anyway, what we want now is we just want to go in and just put some manual vias. So, let's do a pad that's uh you know, a 0.3 mm hole for example.

**Dave Jones:** That's all you know, cuz you want it the solder to be able to flow through. You You don't want it to be too small that the manufacturer is going to charge you more for example.

**Dave Jones:** And then our pad is 0.5 mm. Here we go. There we go. Now we go to metric. So, I do metric for hole sizes and for dimensions and boards and stuff like that.

**Dave Jones:** But for trace and space, I still like to do imperial. Sue me. Now, it's going to give a clearance constraint there cuz I haven't set up the rules. I I done like anything.

**Dave Jones:** We We could actually put two vias here. There's no reason why we couldn't have two like that just in case like one doesn't make doesn't make adequate connection. Here you go.

**Dave Jones:** Those holes look enormous, don't they? But they're 0.3 mm. We could do what as I said you could do one that's staggered, but like I think that's but then again you've got to also get your soldering iron.

**Dave Jones:** You've got to have enough exposed copper on there to get your soldering iron on so then you can heat up the pad and heat up the via that it goes through and then the bottom of the the bottom side of this if you have flippity doodah, the bottom side of this has to then transfer the heat also through to the pad which you're trying to solder to on

**Dave Jones:** the bottom of this on the micro supply board. So, you know, as as a bit of bit of trickery required there. So, I I don't know. Should I go people are screaming at use one Dave, use two, go for the castellation ones.

**Dave Jones:** Now Of course, if I wanted to do the castellated holes for example, I would just specify my board outline as going right through the center of those pads and then they would manufacture it.

**Dave Jones:** They'd cut it get the laser out and straight through. Uh and then I'd be left up with the left off with the castellated pads, but anyway, I think two like that will probably do the business.

**Dave Jones:** Let's get rid of those error markers. Now, of course, um when we've just got the pads like this, of course, the soldering iron has to the only contact it's got is on the annulus ring around that's called the annulus ring, the exposed copper around the via like that.

**Dave Jones:** So, probably what you want to do once again, you could do this as a slotted hole for example, you could like bit no. Anyway, so what I'm just going to do is just put a fill.

**Dave Jones:** So, what we can do is we can actually put a fill on the top like this and of course this won't We've We've got the fill there. There's a copper fill, okay?

**Dave Jones:** But, the problem is we've got We haven't removed the solder mask expansion. So, we need to go to our solder mask, our top solder mask layer and put in another fill like that.

**Dave Jones:** And bingo, we now have this nice big pad that we can get our nice chisel tip iron onto and then the solder will flow down through these vias here.

**Dave Jones:** And of course, we've got the the matching um pad on the bottom like that. So, I I think that's a good solution. And we just place that there. You'll notice how it takes up all the uh net names.

**Dave Jones:** All right, so this is looking pretty nifty. I haven't uh defined the board outline yet, but there you go. We've got our nice uh pads like that. And on the bottom side there, we've got our matching pads down there.

**Dave Jones:** We've got a solder mask between pads. So, it should be all hunky-dory. Yes, I'm I'm sure the anal retentive out there Dave, pull back. Pull back just a tad on those uh on the annulus ring there.

**Dave Jones:** All right. So, we'll just go via. How about 0.45? Will that do it? Oh, yeah. Good enough for Australia. In fact, it's bang on, is it? Ha, winner winner chicken dinner.

**Dave Jones:** So, there you go. Um, that is how I well, I've decided to implement. As I said, there's many ways to skin this cat. You could do castellated holes, you could do staggered uh vias, and all sorts of stuff.

**Dave Jones:** You could do as a slot. If I put my thinking cap on, I could probably come up with half a different way dozen ways to uh do this. And now all we got to do is route that and we'll just define our board outline.

**Dave Jones:** As I said, I think we'll do it like that. I think cuz otherwise, you got these resistors in the way. If you try and bend it up this side up here, you've got the resistors in the way and you've got these and you know, we can't take those out.

**Dave Jones:** Um so, really yeah, I think I'll I'll just have it coming out like this cuz there's a bit more gap between that Richtech chip and those pads than there is between these resistors and these pads down here.

**Dave Jones:** So, and then as I said, if you put the board and if you put the flex coming up here like this, then it's going to flip up on top of that.

**Dave Jones:** That's quite a large thick package there, so it's really going to flip the chip up like this and I don't really want that. So, I think I'll have it coming out the side like that.

**Dave Jones:** Oh, hang on. Have I got pin one around the right way? No, pin one's over here. I was going to come a gutser. Let's just double check on our micro supply board here.

**Dave Jones:** Yep, pin number one is there. So, I need to orient it I of course I I had it oriented that way Is that the right correct way on the camera?

**Dave Jones:** Anyway, I think you know what I mean. If you've been playing along at home, then you know that I was going to come a gutser there. So, yeah, need to double-check stuff like that.

**Dave Jones:** So, pin one So, I want the flex to be coming out the bottom like this. So, cuz I don't think there's enough on the top. Yeah, I I could No, cuz you haven't got the crystal over here.

**Dave Jones:** Could Could have it there? Ooh, I don't think the the physical size of the chippy I can just measure it outline. I bet you've got the switch as well, but we can put it off to one side.

**Dave Jones:** That's no problem. We're talking about 8.3 mm, 9.9 mm. So, there you go. We don't have the physical distance, you know, always measure, don't assume. Um so, even if we butted the pins right up against here, we do not have the room to fit in the chip in there.

**Dave Jones:** And likewise, we don't have You can just tell. You can just physically We're not going to have here. Okay, so, um, let's allow for some flexi flexi, cuz once you got the chip on there, the chip's going to be like relatively Like the chip doesn't really bend.

**Dave Jones:** And so, this flex underneath this chip isn't going to bend. So, we want to add, you know, some bend radius so we can can just come up over that resistor and then And then we can like put in some insulating stuff on the bottom and then just stick it down with some, you know, selastic or some double-sided tape or something like that.

**Dave Jones:** Like just leave it flapping around in the breeze. Doesn't matter. It's just a prototype. This is not high-speed stuff. We do actually have a differential pair on here, and it's it's designated by these little differential pair markers, cuz it is USB.

**Dave Jones:** So, technically, we should route these as a You don't have to have controlled impedance, but if you were this was high-speed stuff, yes, you would look at controlled impedance differential pair length matching or alternate trace length matching these and and stuff like that.

**Dave Jones:** But this, like, we're not transferring huge amounts of data. It's basically RS232 type rates here. So, we don't have to worry about Just It's still route them as a pair just because you can and you should, but you don't have to worry about the nitty-gritty of that.

**Dave Jones:** Nah. So, what we'll do is we'll just define an outline here. We could So, we just put our little radii in there like that. Let's We can just make this bigger to get all our traces out, of course.

**Dave Jones:** And we want our radii in there because that's the part that might flex is going to flex a little bit. So, yeah, you just want to take the edge off that.

**Dave Jones:** These corners, you don't have to worry about them. You can just keep them sharp. Doesn't really matter. Of course, that's that's showing up as like thick. I can go go there and physically, um, set the three-dimensional, uh, you know, thickness of that to the polyamide, um, material to make it look a bit more realistic, but who cares?

**Dave Jones:** That will now be a little board, but instead of being made out of fiberglass, it's going to be made out of poly put the kettle on. So, I don't want this to be a routing tutorial, but here's where you move your chip around, use your rats nest, and also rotate your component like this to see you can see, oh, look, these are all swapping over like this.

**Dave Jones:** This is probably not going to be pretty. So, you can see that there's all these ones down here which have to get all the way over to here. Oh, oh, I haven't switched.

**Dave Jones:** I'm still pad one over here. God, I'm dumb. What I'm going to have to do is take all of this and flippity doodah that around. So, that like you can see all those all those rats nests are those nets are crossing over, so you know that's going to be ugly.

**Dave Jones:** These ones down here have to connect up with these ones over here. Those go over to the couple over to the couple over here go over to there, things like that.

**Dave Jones:** Oh, oh, oh. All right, so let's actually just, uh, place a trace here. Just just willy-nilly, right? This is a 5 thou, uh, trace, you know, you don't want to go much smaller, but are you going to be able to get that through that pad?

**Dave Jones:** No, you're not. See, that's the problem, right? We're we're constrained, so really we've probably got no option. I really don't have an option, really, unless you want to go to really fine tolerances.

**Dave Jones:** Why? Cuz you're just going to pay more. I'll just extend, uh, this all the way up to the top. Traces all up there cuz there's nothing on the top side.

**Dave Jones:** Like, I don't care if that's all flapping bending up or whatever. Don't doesn't really matter. I want to be able to get my damn traces out of there like that.

**Dave Jones:** All right, I do believe that is our finished design. I'm certainly not, uh, not going to write home to my mom about that one. Look, I it's just it's just slapped together.

**Dave Jones:** 5 thou 5 thou traces, .3 mm holes. The the vias aren't even tinted, for example. So, you might want to tint over those. But, but as you can see, that is the basic I could pull back the width of that.

**Dave Jones:** And then, we'll just solder our chip onto the directly onto the flex cuz you're soldering directly onto copper. And temperatures are a different, you know, um a thing to FR4, not as tolerant, but no problems whatsoever.

**Dave Jones:** I should I done off I'll put the bypass cap on there or not. But, anyway, that should do the business. All right. So, that's our finished board. And we just generate our Gerbers exactly the same way as we would for a regular board.

**Dave Jones:** I've done videos on that. Let's just assume that we've generated our Gerbers, no problems whatsoever. Then, you'd go over to your PCB uh manufacturer. Then, you'd choose FPC rigid in whatever shopping cart options they've got.

**Dave Jones:** You don't want rigid flex PCB, of course, because we're not manufacturing rigid flex. We're just manufacturing a flexible PCB. That tells them you want polyimide material. Probably put the kettle on instead of uh fiberglass FR4 PCB.

**Dave Jones:** We've got a two-layer board. We just want single pieces. We don't want a panel. We don't care. Um you can get them to panelize it. They might panelize it for you.

**Dave Jones:** But, no, I'm just happy with the little single pieces. So, it's absolutely tiny. It's 22 by 12 mm. And like, we don't even need silkscreen on the thing. Um let's just say we want 10 of these little puppies.

**Dave Jones:** Uh FPC thickness, we can choose our thickness. Like, we want like .1. It looks like .1 is their standard. So, that's fine. You don't want to deviate from that because you might that might increase uh your lead time and stuff like that cuz you may not be able to share a panel uh, with everyone else.

**Dave Jones:** Yes, they'll still do these flex things as a panel. A rigid flex would be very custom specific. So, um, you'd almost certainly be buying your own panel there. And their minimum track space actually 0.06 mm.

**Dave Jones:** That's like under three thou. That's pretty good. So, we've got uh, 5 5. So, no problems whatsoever. Minimum hole size uh, 0.35. Oh, we've come a cropper. I should have checked this before I laid out my board.

**Dave Jones:** Don't from this manufacturer anyway, um, it needs to be 0.35 mm. So, yeah, they're just going to come back and reject that. So, I can change into 0.35. How much we looking at now?

**Dave Jones:** 5 to 6 days, quantity 10, 111 bucks. It's not particularly cheap, is it? What if we want five? It's not going to matter, five or 10 because they're so tiny.

**Dave Jones:** They've got to manufacture this. Are they doing it just for us? Not like somebody else may not like we may not be sharing a panel of flex material uh, for example, with them.

**Dave Jones:** E-test? No. Oh, it's a bit cheaper. There you go, without the E-test, it's cheaper. We don't need the electrical test. I I I wouldn't bother. Seriously, I wouldn't bother with the electrical test for this.

**Dave Jones:** I'd just just take my chances. So, we get our silk screen for for free. So, you know, might as well put a picture of platypus on there or something.

**Dave Jones:** Nah. Now, there is some concern about this is that uh, okay, our resistors, if we go look at our board over here, then we've got our resistors. These resistors are fairly close, okay?

**Dave Jones:** So, we're going to have a bend in the flex going down like this. So, you've got to flip it around. So, we've got a bend like that and then it's got to bend up over this little um, this little BGA down here is not, you know, it it's not that high.

**Dave Jones:** It may not even be as high as the resistors. I don't know. It's a tiny little thing. But anyway, a bend line across there, right Just after that chip.

**Dave Jones:** So, just whole thing will try and flex up like that, for example, and then this chip overlays that. So, you could argue that I probably should have put the chip down below the bend line of the top of that.

**Dave Jones:** And then you've got a bend in here, but I'm not really concerned about that. So, you've got two intersecting bend lines like that. So, maybe with hindsight I could have put I should have put the chip down the pins down around like no no higher than the other chip, because then the whole thing could flex along that axis like that, if you can see my cursor, if you know what I mean, if you

**Dave Jones:** know what I'm talking about. So, yeah, um I I I think it'd fit. I don't think it's going to be a problem. Once again, for for production, you'd fuss over this sort of stuff.

**Dave Jones:** All right, just to avoid that dual bending radius like intersecting bend radius at this point here, I might go with what I originally proposed. Might do a one off turn it one where I just route all the traces up around here like half on the top, half on the bottom.

**Dave Jones:** They should be able to get around there. That's only 4.3 mm. Look, you know, you you don't realize how small this is. And measure that from there over to this component over here, that's six uh that's almost 7 mm.

**Dave Jones:** So, you know, the flex only comes to here. So, we've got, you know, we can make it much much longer. But as I said, cuz it's going to bend it's going to bend along that pretty sharp, cuz those resistors are, you know, close to that chip.

**Dave Jones:** You could argue that, you know, there was heaps of room here. They shouldn't have been that close to begin with, but you know, and we've already got those boards, so there's no point worrying about that now.

**Dave Jones:** And uh and so then we don't have and then we don't have to remove the bypass cap there for example. It's not a very effective bypass cap anymore with the traces doesn't matter.

**Dave Jones:** Doesn't matter. She'll be right. No worries and Yeah, I think that will that will do it. So that will remove like this crinkle radio you know that when you got two intersecting radio I like that cuz this has to bend at that point this has to bend here.

**Dave Jones:** So this will all be crinkly cut uh Smith's chips crinkly cut in here. So and to avoid our Smith's crisp crinkly cut we will add a bend radius in here cuz this is where it's all doing all the I might even move this down a little bit down here something like that.

**Dave Jones:** I'll just reroute that. Only take me 10 minutes. And because we can't get across there anymore you might I might flip it. Actually you could argue that no yeah most of them are coming from here.

**Dave Jones:** I'm just going to leave it like that I think maybe move the chip over here cuz look there's only four uh pads there that are connect Oh no no six over here but there a couple of those go over to there.

**Dave Jones:** So I might I might leave it say thereish. That's working out nicely already. How about that? I like that. I didn't even like try all that it was just like just got feel.

**Dave Jones:** Yeah, look at that Bobby Dazzler. And I'm just going to be bang on on the width of that too just like guestimating that. A winner. Ah, why can't that go to there?

**Dave Jones:** Now you could argue that I can maybe increase the the width of this for example cuz I had that available and then route some extra traces around here like this from here but really when you look at this I'm I'm looking at this guy and I don't know these ones have to go over to here anyway.

**Dave Jones:** Then they're going to have that same routing squeeze constraint that I had through there before and there's three of them and I I look couldn't be bothered. I'll just route the all these out on the bottom layer." By the way, sometimes when you're routing traces like this, often you will offset them.

**Dave Jones:** You wouldn't have You may not have one trace above the other because there can be slight mechanical things there when you're really getting into tight bendies and things like that.

**Dave Jones:** So, a technique which is sometimes used is to offset your traces like that, but for something like this doesn't matter a rat's. Actually, I've come a gutter here a little bit cuz like I can't obviously route them out in this direction.

**Dave Jones:** So, I've routed these ones lowest point down here cuz I can't I might be able to snake one up there, perhaps. Um but yeah, it's nothing like sneaking one on the side.

**Dave Jones:** Look at that. And but so these ones will come around here like this and well, what do you do? You got to go all the way around here, all the way with LBJ, all the way right around here.

**Dave Jones:** So, you got to So, it it it's Murphy will get you every time. The life of a PCB designer. No, that's actually the power ground. So, there you go.

**Dave Jones:** Uh once again, like you could leave it till later and then, you know, try and flood fill your way out of your routing problem, but like let me just get the other traces around and we'll see what's what.

**Dave Jones:** This is where I could actually go to the top layer. You know, power and ground here. You could argue that Okay, you could maybe route the top layer out like this and around.

**Dave Jones:** So, and push all those traces up. Yeah. You could argue that I could even move it one more like that, extend my board out. This is what you can do when your constraints aren't uh really, you know, major constraints.

**Dave Jones:** Now, we got a nice fat looking power trace coming around there now. Look at that. Wow. Did I already run that trace over there? Oh, they were off from there to there.

**Dave Jones:** That's all. Okay. Yeah, no workers. There we go. That's better. So, we actually got a Oh, we got a nasty nasty crossing there. So, yeah, we ran our 3.3 V uh uh USB supply around there like that, and we can probably do a similar thing to our ground.

**Dave Jones:** And of course, I could uh you know, route multiple ones at the same time. Of course, I could select them and then bring them up all over and all that sort of jazz, but yeah.

**Dave Jones:** And here's our differential pair. And as it turns out, we don't actually have to connect this on top, because this would already be connected on our board. So, there's absolutely no reason to connect those two pads there.

**Dave Jones:** But, just in case this one doesn't make connection and this one does when you're soldering, I just for completeness and for design rule checking, of course, you would then get this across here like this.

**Dave Jones:** No wackers. There we go. Almost done. Just got to join up some grounds. There we go. We are We are done. We are fully routed. I didn't uh define my I stretched my board outline just a tad there, so I'll redo that.

**Dave Jones:** But, we are done. Look at that. There's our flex. Once again, I'll just tent those vias, but uh yeah. Um that is That looks neat. That looks like a winner winner chicken dinner.

**Dave Jones:** So, we avoid that flex point in there. So, yep. I like that. Beauty. So, there's not really much left to do there. I forgot to change these hole sizes I will to point .35 mm.

**Dave Jones:** Um and basically, all we need to do is add our shopping cart, upload the gerbers, and Bob's your uncle. We should just get that flex board cuz they won't They shouldn't have any problems with that as long as you meet all the clearance guidelines, the whole guidelines, and stuff like that.

**Dave Jones:** And it's obvious in your Gerber what your board outline is on one of your mechanical layers. It is There's nothing fancy. We're not doing a fancy rigid flex, and they need to know the layer stack up and all sorts of jazz like that.

**Dave Jones:** They'll just manufacture it as a two-layer PCB. Pretty simple these days. When I was a boy, that was rocket science. Anyway, um that's it. I hope you enjoyed that.

**Dave Jones:** I don't know how long this video's been. It's been quite lengthy, but uh if you enjoyed that, please give it a big thumbs up. And as always, you can discuss it down below.

**Dave Jones:** And we'll have to do a follow-up video when we actually get this um and assemble it on the board and and see if it works. It should. Fingers crossed.

**Dave Jones:** I don't know. It's a rush job. Um and but it should. Can't see why not. Um I I don't think we've come across any way, but you never know.

**Dave Jones:** Never know your luck in the big city. So, anyway, I hope you liked it. Catch you next time.
