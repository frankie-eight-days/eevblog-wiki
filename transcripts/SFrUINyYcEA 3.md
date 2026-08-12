---
video_id: SFrUINyYcEA
title: EEVblog #1262 - Designing a Flex PCB + uSupply Update
url: https://www.youtube.com/watch?v=SFrUINyYcEA
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 27, "3": 42, "4": 54, "5": 73, "6": 92, "7": 106, "8": 121, "9": 144, "10": 160, "11": 174, "12": 191, "13": 213, "14": 233, "15": 243, "16": 258, "17": 270, "18": 288, "19": 303, "20": 315, "21": 332, "22": 352, "23": 364, "24": 378, "25": 391, "26": 411, "27": 428, "28": 440, "29": 455, "30": 469, "31": 484, "32": 500, "33": 514, "34": 529, "35": 546, "36": 565, "37": 583, "38": 598, "39": 611, "40": 624, "41": 635, "42": 653, "43": 671, "44": 688, "45": 700, "46": 709, "47": 719, "48": 729, "49": 744, "50": 755, "51": 766, "52": 778, "53": 792, "54": 803, "55": 815, "56": 831, "57": 845, "58": 861, "59": 876, "60": 892, "61": 903, "62": 921, "63": 936, "64": 947, "65": 960, "66": 974, "67": 987, "68": 1004, "69": 1020, "70": 1034, "71": 1047, "72": 1061, "73": 1076, "74": 1089, "75": 1107, "76": 1118, "77": 1130, "78": 1146, "79": 1164, "80": 1178, "81": 1192, "82": 1206, "83": 1218, "84": 1235, "85": 1248, "86": 1263, "87": 1274, "88": 1289, "89": 1306, "90": 1320, "91": 1333, "92": 1349, "93": 1362, "94": 1376, "95": 1389, "96": 1401, "97": 1413, "98": 1428, "99": 1443, "100": 1456, "101": 1473, "102": 1486, "103": 1497, "104": 1511, "105": 1523, "106": 1533, "107": 1547, "108": 1561, "109": 1573, "110": 1586, "111": 1602, "112": 1613, "113": 1627, "114": 1640, "115": 1653, "116": 1664, "117": 1680, "118": 1692, "119": 1705, "120": 1719, "121": 1734, "122": 1749, "123": 1762, "124": 1778, "125": 1793, "126": 1807, "127": 1823, "128": 1834, "129": 1851, "130": 1862, "131": 1875, "132": 1888, "133": 1900, "134": 1912, "135": 1927, "136": 1940, "137": 1953, "138": 1967, "139": 1980, "140": 1993, "141": 2008, "142": 2024, "143": 2041, "144": 2056, "145": 2073, "146": 2086, "147": 2105, "148": 2118, "149": 2131, "150": 2145, "151": 2162, "152": 2173, "153": 2185, "154": 2194, "155": 2209, "156": 2220, "157": 2234, "158": 2248, "159": 2260, "160": 2279, "161": 2296, "162": 2312, "163": 2327, "164": 2337, "165": 2348, "166": 2361, "167": 2379, "168": 2391, "169": 2405, "170": 2417, "171": 2429, "172": 2442, "173": 2455, "174": 2471, "175": 2484, "176": 2495, "177": 2510, "178": 2523, "179": 2537, "180": 2552, "181": 2566, "182": 2578, "183": 2595, "184": 2613, "185": 2628, "186": 2642, "187": 2653, "188": 2667, "189": 2685, "190": 2697, "191": 2711, "192": 2724, "193": 2735, "194": 2749, "195": 2761, "196": 2780, "197": 2799, "198": 2814, "199": 2831, "200": 2842, "201": 2856, "202": 2867, "203": 2880, "204": 2898, "205": 2910, "206": 2924, "207": 2942, "208": 2956, "209": 2971, "210": 2988, "211": 3001, "212": 3013, "213": 3027, "214": 3041, "215": 3050, "216": 3065, "217": 3077, "218": 3094, "219": 3109, "220": 3126, "221": 3139, "222": 3159, "223": 3172, "224": 3190, "225": 3206, "226": 3223, "227": 3234, "228": 3246, "229": 3260, "230": 3272, "231": 3286}
---

**Dave Jones:** Hi, in a recent video, which I'll link in, where I explained all of the PCB manufacturing options that a typical manufacturer would give you when you go and check out and get your board manufactured. And I asked in that would

**Dave Jones:** people like to see one on flex PCBs and a ton of people said yes. So a flex a full on flex PCB video will have to follow this cuz it'll be quite in-depth. But as it turns out um

**Dave Jones:** just yesterday we had a requirement come up for a flex PCB adapter that we required for the new micro supply project. So I thought we'd just take a look at rather than just me do it and just send it away. I'll press record and

**Dave Jones:** we'll talk about the various options here. So this won't be an in-depth flex PCB tutorial. This just happens to be a real world thing that we need for the micro supply. If you want to see the micro supply, tada, here it is. Doesn't

**Dave Jones:** it look sexy? Here we go. Oh, look at that. Micro supply. Beautiful. Thing of beauty, a joy forever. Doesn't have the LCD in there, but anyway. Um yes, this actually really does exist and we have it working and as it turns out

**Dave Jones:** we just got the USB power delivery circuit of it working the other day and herein lies the problem. And it this video will start out with a rant about ST as in ST semiconductor because well, we've had an issue with this. So let's

**Dave Jones:** take a look at it before we get to the flex PCB. Well, bloody Altium Designer first time I'm using version 19 actually and I get object reference not set to instance of an object. I don't know. Whatever. Send it. Do I have to send and

**Dave Jones:** close? Can I just close? I don't want to send and close. Here we go. Anyway, this is the schematic for the USB portion of the the isolated USB side of the micro supply and yes, micro supply videos will

**Dave Jones:** come in due course. And what we've got over here is we've got an STM 32F070F6P6TR microcontroller cuz all those letters on the end matter. That's rant number one. The STM32F070 micro is very different depending on the letters you put on the end of it and

**Dave Jones:** it's really freaking annoying. Anyway, so in the hardware prototypes that we've built, we chose this relatively low cost STM32 micro cuz we're also using STM32 micro as the main micro on the isolated side as the main control element as

**Dave Jones:** well. And it's a little 20-pin TSOP package and it's got 32K of flash. We thought 32K of flash is plenty cuz we you know, we don't need to do much. All we need to do is some USB power delivery

**Dave Jones:** configuration type stuff and of course USB comms like serial type comms, HID interface stuff and you know, things like that. And it seemed at the at the time, it seemed like a good choice. 32K was plenty. But as we've found out

**Dave Jones:** through great personal anguish mostly on David's side, personal anguish of the development of this thing, USB PD libraries that come from the manufacturer are actually huge. They're enormous and we actually chose a Richtek part down here. It's the RT1716

**Dave Jones:** and that's the USB PD controller. So you can see these lines here, CC1 and CC2. They're control lines which go over to the USB-C connector here. Over here, CC1, CC2 and they actually configure the USB power delivery specification. They negotiate how much

**Dave Jones:** power you can, you know, the host can deliver and how much the load needs and all that sort of stuff. And then we want wanted to do it properly. By the way, when we chose this micro, as we'll look

**Dave Jones:** into another ST micro that had USB power delivery built-in was not available. The Well, the cheaper version of it wasn't available, as we'll see, at the time of making that uh decision. But, and the one that did, I think was was grossly

**Dave Jones:** more expensive. So, it was a cheaper solution to go for this two-chip solution here for uh So, the STM32, of course, has USB built-in. Here it is here, USB. There it is. There's the uh twisted pair up there. And so, it's got

**Dave Jones:** the USB controller, but the USB power delivery is handled via the I²C bus down here in this little uh tiny eight-pin um RT17 Richtek RT1716. As it turns out, which we didn't know at the time, the Richtek library for USB power delivery

**Dave Jones:** is enormous. So is the ST micro one. The ST micro one is uh I think it's like 2 megabits or something enormous like that. And the Richtek one was huge as well. And David's actually And it wouldn't fit. Neither of them would fit

**Dave Jones:** in the 32K of flash on our STM32 micro, let alone all the other stuff that we wanted to put in, the serial comms, the HID, and the uh US regular USB stuff, and, you know, all sorts of stuff. Just

**Dave Jones:** the power delivery library was absolutely enormous. So, um yeah, uh David's had to work with uh the design engineers at Richtek to get the the library down, and we've finally got it pruned down where we can actually fit

**Dave Jones:** the Richtek USB PD library into the 32K of flash on this ST micro that we're using. Unfortunately, uh we can't fit anything else. So, we can't fit all our other and maybe if we keep working with them uh for longer, we might be able to get

**Dave Jones:** it down further where we can just squeeze everything in this 32K. But anyway, we've decided bugger that, we're just going to put in a larger micro. And of course, Murphy's law says that the package we chose, this 20-pin TSOP

**Dave Jones:** package, the largest part is a 32K part. So to get say a 128K part, we have to move to an entirely different package. And at this stage, we've got like half a dozen prototype boards built up, and you

**Dave Jones:** know, they cost a fair bit to get these manufactured, and they're all working. So we don't want to just scrap those and have to rebuild boards from scratch on a tight timeline at the moment. And like we just want a little flex adapter board

**Dave Jones:** that converts a TSOP package like this into a larger footprint for the larger part. Right, so here's a photo of the board here, and this is the offending chip right here that we have to convert. So what we need is a flex PCB

**Dave Jones:** because you can't really do this with a rigid. This is where a flex PCB comes in real handy. What we need is some sort of flex PCB which goes like this up here like this and goes down there like that. Please

**Dave Jones:** excuse the crudity of the model. Didn't have time to build it to scale or to paint it. There's our new chip which is a quad flat pack. And then we will have pads on here like this with little

**Dave Jones:** via holes in them so that we can actually solder down to this board here to the existing pads. So we remove this chip, we get our flex PCB which is very thin polyput the kettle on material, polyamide material,

**Dave Jones:** that is it'll be like a regular double-sided board, but it'll just be flexible so that we possibly fold it up or something like that. Although, you can see that this connector is in the way here. So, we could go So, we could

**Dave Jones:** actually, you know, do it something like this, perhaps. That might work. And But, then you've got it's a quite difficult cuz these are very thin. You got to get down and solder it onto the pads down here. We might have to physically

**Dave Jones:** remove this capacitor here, but that's okay. That little tiny BGA there, that's that Richtek package. Isn't it a little pain in the ass? Anyway, it's cheap and it does USB micro USB power delivery negotiation stuff in it. So, yeah,

**Dave Jones:** that's you know, so we need some sort of flex board. So, at this stage I'm thinking something like that. But, the issue here is, okay, this is a real fine pitch. I think it's I'll have to double-check. I think it's 0.5 mm pin

**Dave Jones:** pitch. So, it's a real pain in the ass. So, you know, really if There's a couple of ways we can do it. Either to have little vias on the board on the flex like that, then you just put your iron on top of that

**Dave Jones:** and put your solder on, and then it just flows down through the vias and attaches to the pads underneath. And you could actually stagger your vias like this. Perhaps, you know, that's a common technique used on you know, LCD ribbons

**Dave Jones:** and all sorts of you know, commercial products like that. That just gives you a bit more clearance there to do those pads. So, we could do that. Or, what we could actually do is have our flex going like this through

**Dave Jones:** the pads like this, and then have little castellated pads on here. Right? Little half moon castellated pads. And I've shown those on I'll do exaggerated here, okay? So, imagine that's one little pad and then you slice through them just like you

**Dave Jones:** would on a regular FR4 fiberglass PCB. You can do that on flex as well and then you could like sort of like just solder in like that and then the board could actually be like this if we didn't have

**Dave Jones:** room up the top here. Like cuz you know, we've got this in the way. This is a large package. So, that the flex would have to flip up like that and we could you know, it it it gets a bit messy. So,

**Dave Jones:** we could have a flex shape like that for example and then all of your traces just run around here like this and then you know, our chip can just be flapped around in the breeze over here. No problems whatsoever and then we don't

**Dave Jones:** need to fold the flex. But, there's lots of things. This is what I'll go into in if I do a specific flex PCB, but I'll just touch on something like this. Like you wouldn't do right angles like this

**Dave Jones:** on a flex. You you round everything. On flexes you round everything including you wouldn't do your traditional right angle traces like 45° traces like that. On flexes you want to round your traces like that. So, when it flexes there's

**Dave Jones:** less uh you know, mechanical stress on sharp junctions and stuff like that. So, you want to just you know, radii everything like that. Just because it's nice for flex because they flex and you don't want sharp corners when things flex. All the

**Dave Jones:** mechanical engineers can tell you all about that. So, even though this board that we're doing for this particular application won't actually flex so to speak, it'll just sort of you know, sit relatively flat like this on top of you know, the existing chips and

**Dave Jones:** things like that. Just be careful if you've got exposed pads on the bottom. Uh make sure they don't short out to the tops of any other components and things like that. So, you'd have to put some sort of insulative layer on the back.

**Dave Jones:** So, you can actually have another layer of poly put the kettle on material stuck on the bottom of your board so that none of your vias are exposed. And of course, you could do tented vias and stuff like

**Dave Jones:** that. But just be careful that you don't nothing shorts out cuz if you had a via that just happens to be here and it was an exposed one and then that's sitting flush on this on the top of this

**Dave Jones:** capacitor here which is going to be larger than the physical height of the resistors there. Oops, you can come a gutser and it's short and it might be intermittent and that'll really ruin your day. Murphy didn't ensure that it'd

**Dave Jones:** be intermittent at the worst possible inconvenient time. Yeah, so I'm not actually sure how I'm going to run this one. Whether or not I'll shape it. I I think I'll put the chip cuz there is Well, there's not room for it here, but

**Dave Jones:** here there's room for it before it gets to this planar transformer up up the top here. So, there's certainly room for the chip cuz as we'll see in a minute, it's not a huge amount bigger than this one

**Dave Jones:** here and even though it's a quad flat pack. But you know, as I said, it's got to like go on the top of this and it's got to sort of bend upwards and I don't know. Six of one, half a dozen

**Dave Jones:** of the other. Like it I I I haven't chosen yet. I'm about to lay this out and I haven't chosen which way to do it. Like whether or not I go for like little holes here like this, whether or not I

**Dave Jones:** just go for little holes like this, little vias like that, staggered vias. That'll that'll probably and just just have the board shaped like that. I think I think that'll probably do the business. I Yeah, I'll just run with that cuz then

**Dave Jones:** we can we can remove that capacitor and we can either put it on top of the flex or we can do some months in and physically take out the capacitor because it's not you know, it's not a big deal. It's just a bypass cap and

**Dave Jones:** well, you know, you can put it on the flex if you want. I could put a pad down for it, but eh, it'll work. So, anyway, that's the story behind what we're doing today. We're going to manufacture a flex manufacture

**Dave Jones:** manufacture. That's a new word. I'm going to run with that. We're going to manufacture a new flex piece PCB. Just a mod PCB that literally has just the two, well, one chip on it plus a pad to solder down uh onto the top of this chip

**Dave Jones:** here. And you would design this like you would any other PCB. There's nothing special about flex PCB design here unless it does actually flex. And then as I said, you want to use curved traces. Uh by the way, bend radius of uh

**Dave Jones:** flex PCBs, uh you as a general rule of thumb, you want to keep the bend radius to 10 times at minimum 10 times the thickness of the material. So, if the material is, you know, half a millimeter, you the bend radius you want

**Dave Jones:** at least 5 millimeters. That's just a rule of thumb. So, I think with the pin pitch, we're probably going to have trouble with the castellations on here. I don't like our chances of getting castellations with 0.5 mm pin

**Dave Jones:** pitch on a flex. I've never actually tried it at that pitch before, so I I don't know. I think I think the safer option is just to go for um staggered via arrangements like that, and we'll just let the solder flow down through

**Dave Jones:** the vias like that. I think we'll give that a go. Right. So, let's go over to the adapter schematic here. And what we've got is uh we've just got the two chips. The new one is an but it's the

**Dave Jones:** CBT6 as opposed to the F6P6TR chip. God. I TR I you don't need the TR. TR's just tape and reel. Um that's just the package that it comes in. I've I've a whole video on that, haven't I? I'm sure

**Dave Jones:** I have. Hmm. Anyway, but this new chip has more pins, which we don't need. Uh but it it comes in a quad flat pack, hence why we need this little flex adapter board. But it's a functionally identical chip, except it's got 128k of

**Dave Jones:** flash. So, let's actually, just for a rant, let's go look at the ST website. So, uh David is starting He used to like ST. He was a bit of an ST fanboy, and then he started to greatly dislike them

**Dave Jones:** because they would uh and now it's all these chips without having like a real proper support for them and stuff like that. And this STM32G0 series, which is a new one, as I said before, this wasn't out. This wasn't

**Dave Jones:** available when we originally uh chose the chip for the micro supply. The development's been quite some time. So, it it is a new one. Bloody modern websites. Look at this. USB PD. USB power delivery. The STM 32G, this is

**Dave Jones:** their new value series line, has USB PD in. So, we can completely get rid of, well, a couple of bottom bottom items here. Not only the Richtek chip, but also these resistors here for the pull-ups, a couple of caps here. We can

**Dave Jones:** consolidate our bomb, and it's cheaper. But aha, it ain't that easy. Because if you're if you're just reading the the top level here, you might think, "Oh, fantastic. USB PD." But let's go have a look at the data sheet, shall we? While

**Dave Jones:** you're searching for the data sheet for power delivery, you search for USB. And what? There's no mention of USB. Wah. Wah. Wah. Wah. Not only, if you actually go into the correct data sheet, not only does it say for the USB power

**Dave Jones:** delivery, it just says, "Oh, data coming soon." or whatever. Um There there is no USB controller inside this thing. So, we've come a gata right there. But if you were looking at uh sort of like the top level things like this, just trying

**Dave Jones:** to pick a micro at at like first shot, You might see oh, it's got USB PD, but it doesn't have an actual USB transceiver in it. So, it's absolutely useless. So, we can't use that value line series. What we have to go to if

**Dave Jones:** you go I will I'll save you the time of going through all the parametric searches and stuff like that. Well, you have to actually go to the G4 series down here before you can find one that has USB um interface with power delivery

**Dave Jones:** including the physical layer like that. And that one is about three times the cost of the dual chip solution with the Richtek power delivery controller and the F series micro that we're going to choose. So, yeah, it's not we've we've

**Dave Jones:** come a cropper there. Anyway, they've got a wanky video over here. I won't bother playing it, but it's how to create a USB power delivery sink in less than 10 minutes. And it goes through and you've got all the it doesn't explain

**Dave Jones:** Well, it doesn't explain No, music. And it just you know, it's it's using their their cube software or whatever and it just it's not explaining anything. It's just say do all this, do all this, do all this and you can

**Dave Jones:** implement a USB power delivery in 10 minutes, but it it ain't that easy. But you have to actually I think you have to contact them to get this library. You might even have to pay for it or something like

**Dave Jones:** that. I do I don't know. I don't want to know the details, but yeah, it it just isn't this easy. They they don't explain anything. So, it's anyway, that's the that's their new cube software. Apparently, you know, they make it out

**Dave Jones:** to be you know, you can just snap your fingers and you've got USB power delivery. No. Um talk to David about this if you want. It is USB power delivery implementing it correctly and thoroughly is pretty horrific experience. Okay, so

**Dave Jones:** let's actually go down here. USB PD dead battery support. The content of this section will be provided later. Thanks a lot, ST. Like, yeah, you're buying to these chips, they advertise them, and yeah, you might design it into your design,

**Dave Jones:** and then you go it if you didn't read this, you might go, "Well, how do I implement my USB PD?" Uh yeah, do I follow some little YouTube tutorial video with all wanky music on top, and that's it? Like, it it's just

**Dave Jones:** no. No, no, no, no, no. So, yeah, ST, pain in the ass, but then again, you know, a lot of manufacturers, Richtek hasn't been ideal, for example. Uh the Richtek one is unfortunately not open source. Come on, Richtek, open source

**Dave Jones:** your USB PD. Anyway, we're trying to work with them so that all of our firmware and implementations will be open source, but I think we're going to have to rely upon some Richtek binary libraries, unfortunately. But they're trying to strip out all of the we're

**Dave Jones:** working with them to strip out all the crap so that we can get a minimal implementation of USB PD that we need. So, yeah, otherwise, it's just it's too big, and they've got undocumented registers, and we've had to get special

**Dave Jones:** spreadsheets from them which document these undocumented registers, and well, to document these undocumented registers. There's a phrase. Anyway, which detail these registers that we didn't know anything about cuz we found it in the software. They're accessing these registers that wasn't in the data sheets

**Dave Jones:** and app notes and things like that, and we had to ask them what what's going on, and they do have the details, but yeah, they don't make them relatively public. So, like, a lot of manufacturers are like this. They just Oh man, the devil's

**Dave Jones:** always in the detail. Anyway, what are we, 30 minutes into the video already? Sorry. Anyway, we've got a PLCC chip, and we want to convert that to an STM32 like package over here. So, we've got the adapter PCB. Now, here's

**Dave Jones:** where you can come a cropper real easy. So, this is our uh chip, obviously the red it's on the uh top layer there, as you can see. And then we've got a bottom layer down here. So, we've only got a

**Dave Jones:** two-layer PCB. Like I said, we won't do anything different to a regular We wouldn't design this any different to a regular PCB. It's going to be exactly the same as you would lay out except uh you when you go to the checkout of the

**Dave Jones:** manufacturer's website, you'll choose flex PCB instead of this. Now, because this is a 100% flex PCB. It is not what's called a rigid-flex PCB, which I'll show you. This is an example of a rigid-flex PCB. It's like I

**Dave Jones:** can't make these bend that I'm aware of. Anyway, um you can see that these uh they've got some caps and I presumably they're they're LEDs, right? So, um yeah, those those caps and LEDs are on this flex PCB section, and then you've

**Dave Jones:** got two other uh rigid boards, hence the name flex-rigid, and that's got a battery on the bottom like that. I don't know what this board does, just an example which came with Altium. When I do my video, I might show a more uh

**Dave Jones:** complex example. But, you can see how the flex material, in this case, usually it's uh sandwiched in the middle. So, if you've got a four-layer board, for example, then your uh flex material will be the two inner layers, and it extends

**Dave Jones:** into the PCB so that you can then fold the boards up like this and create all sorts of You can make as many boards as you want. But, you basically lay these out as one big uh PCB. Like, you've got

**Dave Jones:** multiple PCBs, but it's effectively done as one large board including all the separate You can have as many of these as you want. You can have 10 different rigid PCBs like this all connected with all these flex functionality. Uh do I

**Dave Jones:** have an example? Now, here's an example of a uh traditional uh PCB that's connected with a flat flex and you can see the ribbon connector cable there and on the other end of the board over here, okay? And of course you need the

**Dave Jones:** connectors and well, that's you know, expensive extra bomber items, more things that can go wrong or you can integrate I'm sorry, I don't have the best example. We'll get a better example next time. But in this one here, you can

**Dave Jones:** see that this PCB, if I flip it over, is actually flat flex on the bottom of the PCB. It's not in the inner layer as I said, but it's on the bottom. And then they've got this extra bit over here

**Dave Jones:** which then goes off to another board. So it's all integrated so you don't need the connectors on there. And that's what they're doing here. You don't need any connectors cuz this flex PCB here extends as a layer inside the PCB. Now

**Dave Jones:** as I said, ordinarily you would wedge it, sandwich it in the middle so it'd be the inner two layers of the PCB because I ordinarily I wouldn't recommend that you put it on the outside like this one because it it doesn't flex. There's more

**Dave Jones:** stress and the adhesion can come off and stuff like that. It is more rigid, no pun intended. I'm here all week. When it's sandwiched in the middle, but you can put it on the bottom like this and the manufacturers will do whatever

**Dave Jones:** you want. But you can see that the bottom layers like that the flex PCB. And that is called a rigid flex cuz it can combines rigid FR4 PCBs with flex. But in this particular case, we're not going to do this. We're going to have flex.

**Dave Jones:** And if you want to see how that works in the layer stack manager here, like here it is. Here's the bottom layer here. They've actually specified the bottom layer as poly put the kettle on polyimide material. So the the

**Dave Jones:** dielectric one dielectric twos. So this is actually a four layer board, but it's got so they could have put it in the middle, but they've actually sandwiched it and they've specified the polyimide on the bottom. Now this isn't the sort

**Dave Jones:** of data that would be automatically given to the PCB manufacturer. This is the sort of data that you might you could just specify in the Gerber. You could just say, you know, like instructions on the Gerber or instructions in an email or whatever.

**Dave Jones:** You can just say, "Right, my bottom layer is the polyimide material, so the flex on the bottom." Or if you wanted the flex on the top, you wouldn't actually have to change So, if we go into single layer mode here, you can see

**Dave Jones:** that the that's the layer on the on the top layer, then the middle layer is there's no copper on the flex at all because there is no flex in the middle layer. It's it's only when you get to

**Dave Jones:** mid layer two or the one from the bottom that this one is flex. So, you can see like the bottom layer is all flex, it's all ground plane. By the way, another recommendation is not to use solid ground planes like

**Dave Jones:** this on flex wherever possible. Usually, you would crosshatch them. So, you might put your plane out here like this, but then I'd start my crosshatch from inside here, and then all of this would be a crosshatch ground fill. And you might if

**Dave Jones:** you tear down products, you might see that commonly is that they'll use a crosshatch ground fill, and that's for thermal and flex and stress reasons, which all the mechanical engineers can no doubt tell you about. But once again,

**Dave Jones:** that's another like rule of thumb. Unless you absolutely need a solid ground plane, you would do flexes as a crosshatch. But when it goes inside the board like this, you can certainly make it solid because it's it ain't flexing when it's

**Dave Jones:** sandwiched inside that fiberglass. And just here's an example here's some examples of rigid flex PCBs. So, this one here you can see that they've got the two copper layers in the middle, then there's adhesive polyimide insulation with adhesive in there.

**Dave Jones:** There's another adhesive in there. Then you got the FR4 prepreg. So, these are your rigid FR4s over here, and this is your flex material sandwiched in the middle. But as we're showing on the Altium example, we've got that flex on

**Dave Jones:** the bottom two layers. So, this bit copper here and this copper here are done and manufactured as a flex. Then they manufacture the FR4 fiberglass ones separately, and then they'll stick those on the top. And it's generally nicer if

**Dave Jones:** you do it as a big panel like this, for example. That that one's only got two separate boards, but you can see how they've designed those as a flex. That one's got a little like a LCD connector or something, you know, some sort of

**Dave Jones:** ribbony thing at the bottom. So, I only got some mouse bites on there. So, that's you know, that's quite quite a nice design. And there's just two boards with some flexes sandwiched, and then there's ones with multiple that might that might have

**Dave Jones:** it look that looks like it's got a like an RF connector on there or something like that. You know, more advanced ones like this. And you know, it can get really cool. But we're just going to manufacture a

**Dave Jones:** simple and solder directly onto a flex PCB. So, you leave out the word rigid. So, we're basically doing like a flex PCB like that. We're going to solder our components directly on to the polyimide material instead of fiberglass. That's

**Dave Jones:** the only difference. So, from a like a design point of view, it it really is if you're just doing flex, there's no difference. You just specify flex in your checkout. That's it. You might have to make it have a few design

**Dave Jones:** considerations for the flex mechanical flex part. But apart from that, the design process is exactly the same. So, there you go. It's going to fold. This is Altium design here. It's just going to like flex around like this. It folds

**Dave Jones:** up, and then so the two boards like that fold up like that. And then the flexy bits go around the outside into a like a like a hockey puck puck configuration or something like that. And once again, this isn't

**Dave Jones:** really an extreme flex board. Like there's nothing really inherently like 10 years ago getting one of these manufactured very specific, you had to find a manufacturer who was willing to do it. Now, it it's practically a shopping cart checkout um

**Dave Jones:** at some manufacturers, anyway. Basically, all you got to do is tell them in your layer stack up on your Gerber's or where wherever you tell them it which layers are polyimide flex material and which layers are fiberglass material and they'll just do it.

**Dave Jones:** Easy peasy. They'll just choose the material and get the get the job done. And of course, and then they'll when they sandwich them all together, all of the vias from the uh flex uh layers will automatically line up with the and be

**Dave Jones:** bonded to the vias on the uh rigid PCBs. But, from a PCB manufacturer's point of view, the construction's exactly the same as a multi-layer PCB. They don't care that you're using a flex material instead of a rigid material. There might be a few

**Dave Jones:** little process, you know, things in there, but basically, they don't care whether or not they're making an eight-layer rigid board or whether they're making an eight-layer rigid-flex combination. It's just that one of the inner layers is made out of polyimide

**Dave Jones:** instead of fiberglass. Anyway, I'm getting way too much into that. So, now, here's where you can come a gutser. As I said, right? You got to got to be very careful here. Now, this is of course all all your PCB designs

**Dave Jones:** are always done looking through the board. So, this is the top layer um by definition, it's the top layer, so it's the red uh layer here, okay? So, this is pin one over here. Now, ordinarily, this one, pin one's in the correct

**Dave Jones:** configuration for the chip, but you'll notice it's blue. It's on the bottom. So, this one's actually been flipped twice. Not only is the component been flipped from the top side, the red side, over to the blue side, but then it's

**Dave Jones:** been mirror imaged like that because we have to connect down to another board underneath which has this particular pin configuration. So, if you didn't realize that, you could completely come a cropper and get your footprint back to front. So,

**Dave Jones:** anyway, we're just going to have a chippy on there. Haven't defined the board outline yet. But yes, we're going to have a pad This won't be a chip. This will just be some vias. So, what we need to do now

**Dave Jones:** is go in here. Geez, look at that expansion on those pads. That's a bit how you doing. That's touching. Look, there's no solder mask Slew though, if we go into 3D view, look at this. Look at this. There's no There's no solder

**Dave Jones:** mask. No solder mask between pads there. I could easily bridge your solder out. So, our solder mask expansion is too big. So, we're going to have to change that. Solder mask expansion, 4 mil. So, we'll change that. So, that's

**Dave Jones:** coming from the rules. We could have changed the rules, but you know, like who cares? Doesn't matter. This is We're not worried about this. There we go. 1 thou solder mask expansion. That'll do it. So, now, if we

**Dave Jones:** go in here like this, bloody error markers. There we go. We've got solder mask between our pads now. That's a Christmas miracle. So, we can flip that over and you can see there's a chippy there. But of course, there won't be a

**Dave Jones:** chippy because that will just have pads. Anyway, what we want now is we just want to go in and just put some manual vias. So, let's do a pad that's uh you know, a 0.3 mm hole for example. That's all you

**Dave Jones:** know, cuz you want it the solder to be able to flow through. You You don't want it to be too small that the manufacturer is going to charge you more for example. And then our pad is 0.5 mm. Here we go. There we go. Now we go

**Dave Jones:** to metric. So, I do metric for hole sizes and for dimensions and boards and stuff like that. But for trace and space, I still like to do imperial. Sue me. Now, it's going to give a clearance constraint there cuz I

**Dave Jones:** haven't set up the rules. I I done like anything. We We could actually put two vias here. There's no reason why we couldn't have two like that just in case like one doesn't make doesn't make adequate connection. Here you go. Those

**Dave Jones:** holes look enormous, don't they? But they're 0.3 mm. We could do what as I said you could do one that's staggered, but like I think that's but then again you've got to also get your soldering iron. You've got to have enough exposed

**Dave Jones:** copper on there to get your soldering iron on so then you can heat up the pad and heat up the via that it goes through and then the bottom of the the bottom side of this if you have flippity doodah, the bottom

**Dave Jones:** side of this has to then transfer the heat also through to the pad which you're trying to solder to on the bottom of this on the micro supply board. So, you know, as as a bit of bit of trickery required there. So, I I

**Dave Jones:** don't know. Should I go people are screaming at use one Dave, use two, go for the castellation ones. Now Of course, if I wanted to do the castellated holes for example, I would just specify my board outline as going right through the

**Dave Jones:** center of those pads and then they would manufacture it. They'd cut it get the laser out and straight through. Uh and then I'd be left up with the left off with the castellated pads, but anyway, I think two like that will

**Dave Jones:** probably do the business. Let's get rid of those error markers. Now, of course, um when we've just got the pads like this, of course, the soldering iron has to the only contact it's got is on the annulus ring

**Dave Jones:** around that's called the annulus ring, the exposed copper around the via like that. So, probably what you want to do once again, you could do this as a slotted hole for example, you could like bit no. Anyway, so what I'm just going to do

**Dave Jones:** is just put a fill. So, what we can do is we can actually put a fill on the top like this and of course this won't We've We've got the fill there. There's a copper fill, okay? But, the problem is

**Dave Jones:** we've got We haven't removed the solder mask expansion. So, we need to go to our solder mask, our top solder mask layer and put in another fill like that. And bingo, we now have this nice big pad that we can get our nice chisel tip iron

**Dave Jones:** onto and then the solder will flow down through these vias here. And of course, we've got the the matching um pad on the bottom like that. So, I I think that's a good solution. And we just place that

**Dave Jones:** there. You'll notice how it takes up all the uh net names. All right, so this is looking pretty nifty. I haven't uh defined the board outline yet, but there you go. We've got our nice uh pads like that. And on the bottom side there,

**Dave Jones:** we've got our matching pads down there. We've got a solder mask between pads. So, it should be all hunky-dory. Yes, I'm I'm sure the anal retentive out there Dave, pull back. Pull back just a tad on those uh on the annulus ring

**Dave Jones:** there. All right. So, we'll just go via. How about 0.45? Will that do it? Oh, yeah. Good enough for Australia. In fact, it's bang on, is it? Ha, winner winner chicken dinner. So, there you go. Um, that is

**Dave Jones:** how I well, I've decided to implement. As I said, there's many ways to skin this cat. You could do castellated holes, you could do staggered uh vias, and all sorts of stuff. You could do as a slot. If I put my thinking cap on, I

**Dave Jones:** could probably come up with half a different way dozen ways to uh do this. And now all we got to do is route that and we'll just define our board outline. As I said, I think we'll do it

**Dave Jones:** like that. I think cuz otherwise, you got these resistors in the way. If you try and bend it up this side up here, you've got the resistors in the way and you've got these and you know, we can't

**Dave Jones:** take those out. Um so, really yeah, I think I'll I'll just have it coming out like this cuz there's a bit more gap between that Richtech chip and those pads than there is between these resistors and these pads down here.

**Dave Jones:** So, and then as I said, if you put the board and if you put the flex coming up here like this, then it's going to flip up on top of that. That's quite a large thick package there, so it's really

**Dave Jones:** going to flip the chip up like this and I don't really want that. So, I think I'll have it coming out the side like that. Oh, hang on. Have I got pin one around the right way? No, pin one's over here.

**Dave Jones:** I was going to come a gutser. Let's just double check on our micro supply board here. Yep, pin number one is there. So, I need to orient it I of course I I had it oriented that way Is that the right

**Dave Jones:** correct way on the camera? Anyway, I think you know what I mean. If you've been playing along at home, then you know that I was going to come a gutser there. So, yeah, need to double-check stuff like that. So, pin one So, I want

**Dave Jones:** the flex to be coming out the bottom like this. So, cuz I don't think there's enough on the top. Yeah, I I could No, cuz you haven't got the crystal over here. Could Could have it there? Ooh, I don't think the

**Dave Jones:** the physical size of the chippy I can just measure it outline. I bet you've got the switch as well, but we can put it off to one side. That's no problem. We're talking about 8.3 mm, 9.9 mm. So, there you go. We don't have the

**Dave Jones:** physical distance, you know, always measure, don't assume. Um so, even if we butted the pins right up against here, we do not have the room to fit in the chip in there. And likewise, we don't have You can just tell. You can just

**Dave Jones:** physically We're not going to have here. Okay, so, um, let's allow for some flexi flexi, cuz once you got the chip on there, the chip's going to be like relatively Like the chip doesn't really bend. And so, this flex underneath this

**Dave Jones:** chip isn't going to bend. So, we want to add, you know, some bend radius so we can can just come up over that resistor and then And then we can like put in some insulating stuff on the bottom and

**Dave Jones:** then just stick it down with some, you know, selastic or some double-sided tape or something like that. Like just leave it flapping around in the breeze. Doesn't matter. It's just a prototype. This is not high-speed stuff. We do

**Dave Jones:** actually have a differential pair on here, and it's it's designated by these little differential pair markers, cuz it is USB. So, technically, we should route these as a You don't have to have controlled impedance, but if you were this was

**Dave Jones:** high-speed stuff, yes, you would look at controlled impedance differential pair length matching or alternate trace length matching these and and stuff like that. But this, like, we're not transferring huge amounts of data. It's basically RS232 type rates here. So,

**Dave Jones:** we don't have to worry about Just It's still route them as a pair just because you can and you should, but you don't have to worry about the nitty-gritty of that. Nah. So, what we'll do is we'll just define an outline here. We could

**Dave Jones:** So, we just put our little radii in there like that. Let's We can just make this bigger to get all our traces out, of course. And we want our radii in there because that's the part that might flex is going to flex a little bit. So,

**Dave Jones:** yeah, you just want to take the edge off that. These corners, you don't have to worry about them. You can just keep them sharp. Doesn't really matter. Of course, that's that's showing up as like thick. I can go go there and physically,

**Dave Jones:** um, set the three-dimensional, uh, you know, thickness of that to the polyamide, um, material to make it look a bit more realistic, but who cares? That will now be a little board, but instead of being made out of fiberglass,

**Dave Jones:** it's going to be made out of poly put the kettle on. So, I don't want this to be a routing tutorial, but here's where you move your chip around, use your rats nest, and also rotate your component like this to see you can see, oh, look,

**Dave Jones:** these are all swapping over like this. This is probably not going to be pretty. So, you can see that there's all these ones down here which have to get all the way over to here. Oh, oh, I haven't switched. I'm still pad

**Dave Jones:** one over here. God, I'm dumb. What I'm going to have to do is take all of this and flippity doodah that around. So, that like you can see all those all those rats nests are those nets are crossing over, so you know that's going

**Dave Jones:** to be ugly. These ones down here have to connect up with these ones over here. Those go over to the couple over to the couple over here go over to there, things like that. Oh, oh, oh. All right,

**Dave Jones:** so let's actually just, uh, place a trace here. Just just willy-nilly, right? This is a 5 thou, uh, trace, you know, you don't want to go much smaller, but are you going to be able to get that through

**Dave Jones:** that pad? No, you're not. See, that's the problem, right? We're we're constrained, so really we've probably got no option. I really don't have an option, really, unless you want to go to really fine tolerances. Why? Cuz you're just going

**Dave Jones:** to pay more. I'll just extend, uh, this all the way up to the top. Traces all up there cuz there's nothing on the top side. Like, I don't care if that's all flapping bending up or whatever. Don't doesn't really matter. I want to be able

**Dave Jones:** to get my damn traces out of there like that. All right, I do believe that is our finished design. I'm certainly not, uh, not going to write home to my mom about that one. Look, I it's just it's just

**Dave Jones:** slapped together. 5 thou 5 thou traces, .3 mm holes. The the vias aren't even tinted, for example. So, you might want to tint over those. But, but as you can see, that is the basic I could pull back

**Dave Jones:** the width of that. And then, we'll just solder our chip onto the directly onto the flex cuz you're soldering directly onto copper. And temperatures are a different, you know, um a thing to FR4, not as tolerant, but no problems

**Dave Jones:** whatsoever. I should I done off I'll put the bypass cap on there or not. But, anyway, that should do the business. All right. So, that's our finished board. And we just generate our Gerbers exactly the same way as we would for a regular

**Dave Jones:** board. I've done videos on that. Let's just assume that we've generated our Gerbers, no problems whatsoever. Then, you'd go over to your PCB uh manufacturer. Then, you'd choose FPC rigid in whatever shopping cart options they've got. You don't want

**Dave Jones:** rigid flex PCB, of course, because we're not manufacturing rigid flex. We're just manufacturing a flexible PCB. That tells them you want polyimide material. Probably put the kettle on instead of uh fiberglass FR4 PCB. We've got a two-layer board. We just want single

**Dave Jones:** pieces. We don't want a panel. We don't care. Um you can get them to panelize it. They might panelize it for you. But, no, I'm just happy with the little single pieces. So, it's absolutely tiny. It's 22 by 12 mm. And like, we don't

**Dave Jones:** even need silkscreen on the thing. Um let's just say we want 10 of these little puppies. Uh FPC thickness, we can choose our thickness. Like, we want like .1. It looks like .1 is their standard. So, that's fine. You don't want to

**Dave Jones:** deviate from that because you might that might increase uh your lead time and stuff like that cuz you may not be able to share a panel uh, with everyone else. Yes, they'll still do these flex things as a panel. A

**Dave Jones:** rigid flex would be very custom specific. So, um, you'd almost certainly be buying your own panel there. And their minimum track space actually 0.06 mm. That's like under three thou. That's pretty good. So, we've got uh, 5 5. So,

**Dave Jones:** no problems whatsoever. Minimum hole size uh, 0.35. Oh, we've come a cropper. I should have checked this before I laid out my board. Don't from this manufacturer anyway, um, it needs to be 0.35 mm. So, yeah, they're just going to come

**Dave Jones:** back and reject that. So, I can change into 0.35. How much we looking at now? 5 to 6 days, quantity 10, 111 bucks. It's not particularly cheap, is it? What if we want five? It's not going to matter,

**Dave Jones:** five or 10 because they're so tiny. They've got to manufacture this. Are they doing it just for us? Not like somebody else may not like we may not be sharing a panel of flex material uh, for example, with them. E-test?

**Dave Jones:** No. Oh, it's a bit cheaper. There you go, without the E-test, it's cheaper. We don't need the electrical test. I I I wouldn't bother. Seriously, I wouldn't bother with the electrical test for this. I'd just just take my chances. So,

**Dave Jones:** we get our silk screen for for free. So, you know, might as well put a picture of platypus on there or something. Nah. Now, there is some concern about this is that uh, okay, our resistors, if we go look at our board

**Dave Jones:** over here, then we've got our resistors. These resistors are fairly close, okay? So, we're going to have a bend in the flex going down like this. So, you've got to flip it around. So, we've got a bend like that and then it's got to bend

**Dave Jones:** up over this little um, this little BGA down here is not, you know, it it's not that high. It may not even be as high as the resistors. I don't know. It's a tiny little thing. But anyway, a bend line

**Dave Jones:** across there, right Just after that chip. So, just whole thing will try and flex up like that, for example, and then this chip overlays that. So, you could argue that I probably should have put the chip down below the bend

**Dave Jones:** line of the top of that. And then you've got a bend in here, but I'm not really concerned about that. So, you've got two intersecting bend lines like that. So, maybe with hindsight I could have put I should have put the chip down the pins

**Dave Jones:** down around like no no higher than the other chip, because then the whole thing could flex along that axis like that, if you can see my cursor, if you know what I mean, if you know what I'm talking about. So, yeah,

**Dave Jones:** um I I I think it'd fit. I don't think it's going to be a problem. Once again, for for production, you'd fuss over this sort of stuff. All right, just to avoid that dual bending radius like intersecting bend radius at this point here, I might

**Dave Jones:** go with what I originally proposed. Might do a one off turn it one where I just route all the traces up around here like half on the top, half on the bottom. They should be able to get around there. That's only 4.3 mm. Look,

**Dave Jones:** you know, you you don't realize how small this is. And measure that from there over to this component over here, that's six uh that's almost 7 mm. So, you know, the flex only comes to here. So, we've got, you know, we can make it

**Dave Jones:** much much longer. But as I said, cuz it's going to bend it's going to bend along that pretty sharp, cuz those resistors are, you know, close to that chip. You could argue that, you know, there was heaps of room here. They

**Dave Jones:** shouldn't have been that close to begin with, but you know, and we've already got those boards, so there's no point worrying about that now. And uh and so then we don't have and then we don't have to remove the bypass cap there for

**Dave Jones:** example. It's not a very effective bypass cap anymore with the traces doesn't matter. Doesn't matter. She'll be right. No worries and Yeah, I think that will that will do it. So that will remove like this crinkle radio you

**Dave Jones:** know that when you got two intersecting radio I like that cuz this has to bend at that point this has to bend here. So this will all be crinkly cut uh Smith's chips crinkly cut in here. So and to

**Dave Jones:** avoid our Smith's crisp crinkly cut we will add a bend radius in here cuz this is where it's all doing all the I might even move this down a little bit down here something like that. I'll just reroute that. Only take me 10 minutes.

**Dave Jones:** And because we can't get across there anymore you might I might flip it. Actually you could argue that no yeah most of them are coming from here. I'm just going to leave it like that I think maybe move the chip over

**Dave Jones:** here cuz look there's only four uh pads there that are connect Oh no no six over here but there a couple of those go over to there. So I might I might leave it say thereish. That's working out nicely already. How

**Dave Jones:** about that? I like that. I didn't even like try all that it was just like just got feel. Yeah, look at that Bobby Dazzler. And I'm just going to be bang on on the width of that too just like guestimating

**Dave Jones:** that. A winner. Ah, why can't that go to there? Now you could argue that I can maybe increase the the width of this for example cuz I had that available and then route some extra traces around here like this from here but really when you

**Dave Jones:** look at this I'm I'm looking at this guy and I don't know these ones have to go over to here anyway. Then they're going to have that same routing squeeze constraint that I had through there before and there's three of them and I I

**Dave Jones:** look couldn't be bothered. I'll just route the all these out on the bottom layer." By the way, sometimes when you're routing traces like this, often you will offset them. You wouldn't have You may not have one trace above the

**Dave Jones:** other because there can be slight mechanical things there when you're really getting into tight bendies and things like that. So, a technique which is sometimes used is to offset your traces like that, but for something like this doesn't matter a rat's.

**Dave Jones:** Actually, I've come a gutter here a little bit cuz like I can't obviously route them out in this direction. So, I've routed these ones lowest point down here cuz I can't I might be able to snake one up there, perhaps. Um but

**Dave Jones:** yeah, it's nothing like sneaking one on the side. Look at that. And but so these ones will come around here like this and well, what do you do? You got to go all the way around here, all the way with

**Dave Jones:** LBJ, all the way right around here. So, you got to So, it it it's Murphy will get you every time. The life of a PCB designer. No, that's actually the power ground. So, there you go. Uh once again, like you could leave it till

**Dave Jones:** later and then, you know, try and flood fill your way out of your routing problem, but like let me just get the other traces around and we'll see what's what. This is where I could actually go to the top layer.

**Dave Jones:** You know, power and ground here. You could argue that Okay, you could maybe route the top layer out like this and around. So, and push all those traces up. Yeah. You could argue that I could even move it one more like that, extend my board

**Dave Jones:** out. This is what you can do when your constraints aren't uh really, you know, major constraints. Now, we got a nice fat looking power trace coming around there now. Look at that. Wow. Did I already run that trace over

**Dave Jones:** there? Oh, they were off from there to there. That's all. Okay. Yeah, no workers. There we go. That's better. So, we actually got a Oh, we got a nasty nasty crossing there. So, yeah, we ran our 3.3 V uh uh

**Dave Jones:** USB supply around there like that, and we can probably do a similar thing to our ground. And of course, I could uh you know, route multiple ones at the same time. Of course, I could select them and then bring them up all over and

**Dave Jones:** all that sort of jazz, but yeah. And here's our differential pair. And as it turns out, we don't actually have to connect this on top, because this would already be connected on our board. So, there's absolutely no reason

**Dave Jones:** to connect those two pads there. But, just in case this one doesn't make connection and this one does when you're soldering, I just for completeness and for design rule checking, of course, you would then get this across here like

**Dave Jones:** this. No wackers. There we go. Almost done. Just got to join up some grounds. There we go. We are We are done. We are fully routed. I didn't uh define my I stretched my board outline just a tad there, so I'll redo that.

**Dave Jones:** But, we are done. Look at that. There's our flex. Once again, I'll just tent those vias, but uh yeah. Um that is That looks neat. That looks like a winner winner chicken dinner. So, we avoid that flex point in there.

**Dave Jones:** So, yep. I like that. Beauty. So, there's not really much left to do there. I forgot to change these hole sizes I will to point .35 mm. Um and basically, all we need to do is add our shopping cart, upload the gerbers, and

**Dave Jones:** Bob's your uncle. We should just get that flex board cuz they won't They shouldn't have any problems with that as long as you meet all the clearance guidelines, the whole guidelines, and stuff like that. And it's obvious in

**Dave Jones:** your Gerber what your board outline is on one of your mechanical layers. It is There's nothing fancy. We're not doing a fancy rigid flex, and they need to know the layer stack up and all sorts of jazz like that. They'll just manufacture it

**Dave Jones:** as a two-layer PCB. Pretty simple these days. When I was a boy, that was rocket science. Anyway, um that's it. I hope you enjoyed that. I don't know how long this video's been. It's been quite lengthy, but uh

**Dave Jones:** if you enjoyed that, please give it a big thumbs up. And as always, you can discuss it down below. And we'll have to do a follow-up video when we actually get this um and assemble it on the board

**Dave Jones:** and and see if it works. It should. Fingers crossed. I don't know. It's a rush job. Um and but it should. Can't see why not. Um I I don't think we've come across any way, but you never know. Never know your luck

**Dave Jones:** in the big city. So, anyway, I hope you liked it. Catch you next time.
