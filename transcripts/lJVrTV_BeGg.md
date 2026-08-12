---
video_id: lJVrTV_BeGg
title: EEVblog #675 - How To Reverse Engineer A Rigol DS1054Z
url: https://www.youtube.com/watch?v=lJVrTV_BeGg
source: youtube-asr
timestamps: {"0": 1, "1": 20, "2": 35, "3": 54, "4": 70, "5": 82, "6": 96, "7": 108, "8": 121, "9": 134, "10": 145, "11": 156, "12": 170, "13": 182, "14": 196, "15": 213, "16": 228, "17": 242, "18": 251, "19": 268, "20": 283, "21": 296, "22": 307, "23": 318, "24": 332, "25": 345, "26": 358, "27": 373, "28": 386, "29": 399, "30": 413, "31": 426, "32": 439, "33": 454, "34": 468, "35": 481, "36": 494, "37": 512, "38": 529, "39": 543, "40": 559, "41": 571, "42": 582, "43": 597, "44": 607, "45": 620, "46": 640, "47": 655, "48": 668, "49": 681, "50": 697, "51": 715, "52": 728, "53": 739, "54": 752, "55": 766, "56": 782, "57": 795, "58": 809, "59": 822, "60": 838, "61": 853, "62": 869, "63": 881, "64": 893, "65": 904, "66": 918, "67": 933, "68": 945, "69": 959, "70": 976, "71": 991, "72": 1008, "73": 1019, "74": 1031, "75": 1047, "76": 1058, "77": 1070, "78": 1083, "79": 1097, "80": 1111, "81": 1121, "82": 1136, "83": 1149, "84": 1164, "85": 1178, "86": 1194, "87": 1208, "88": 1227, "89": 1242, "90": 1258, "91": 1275, "92": 1291, "93": 1305, "94": 1319, "95": 1335, "96": 1348, "97": 1363, "98": 1376, "99": 1393, "100": 1408, "101": 1422, "102": 1440, "103": 1453, "104": 1468, "105": 1481, "106": 1492, "107": 1509, "108": 1522, "109": 1539, "110": 1552, "111": 1567, "112": 1583, "113": 1598, "114": 1610, "115": 1624, "116": 1638, "117": 1656, "118": 1669, "119": 1684, "120": 1698, "121": 1709, "122": 1721, "123": 1733, "124": 1752, "125": 1765, "126": 1782, "127": 1799, "128": 1810, "129": 1824, "130": 1835, "131": 1854, "132": 1866, "133": 1881, "134": 1897, "135": 1912, "136": 1929, "137": 1942, "138": 1959, "139": 1974, "140": 1988, "141": 2001, "142": 2018, "143": 2033, "144": 2048, "145": 2062, "146": 2078, "147": 2089, "148": 2107, "149": 2125, "150": 2138, "151": 2154, "152": 2173, "153": 2189, "154": 2202, "155": 2213, "156": 2225, "157": 2239, "158": 2252, "159": 2268, "160": 2280, "161": 2292, "162": 2305, "163": 2317}
---

**Dave Jones:** Hi, in my previous video I did a teardown of the new Rigol DS1052Z. There it is, it's still in bits. And an amazingly low cost oscilloscope for four channels, 399 bucks. It's absolutely incredible. So, I was curious to know how they've

**Dave Jones:** actually re-engineered the the input analog front-end channels on these to lower the price point and get four channels for the price of two. And as we saw in the previous teardown, which if if you haven't seen, I'll link it in

**Dave Jones:** down below, check it out first. I noted that they had gone for a an entirely discrete transistor-based front-end pretty much. So, I figured how are they doing it? And also, how are they doing the bandwidth limiting on this thing because the model,

**Dave Jones:** whether it's 50 MHz, 70 MHz, or 100 MHz, it's just a software-configurable thing. So, how are they changing that and limiting the bandwidth inside the scope? There's only one way to find out, reverse engineer it. Let's go. And the first thing you're going to want

**Dave Jones:** to do is take a photo of both sides of the board. So, I got my camera set up on the tripod here, and I'm actually using a high F-stop here so that I get a really deep depth of field so that high

**Dave Jones:** components aren't out of focus, and I'm making sure I'm focusing directly on like the smallest dot surface mount component on the board. So, I'm going to keep that. So, hence using the high F-stop value is going to give

**Dave Jones:** me a long shutter speed. In this case, it's like half a second or something. So, I can't hand hold this thing. Got to set up on the tripod, and I'm going to just set the frame just right, and I'm going to try and

**Dave Jones:** keep the same frame for both shots when I flip the board over just so that I can get pretty close to the correct scale factor inside the camera. You don't have to do that. You might you can and might

**Dave Jones:** ultimately have to scale the images in software later, but anyway, it's nice if you can just get it first go. And also, just make sure you've got decent lighting. The reason I've got it at a big angle like this is because if I had

**Dave Jones:** it flat like that, straight up like that, it would get a shadow in from the cans up here due to my overhead lights. So, you really want some decent light. You know, if you got one of those light

**Dave Jones:** tents or something like that, then you can get really good shots. And what you also want to do is get a torch. Maybe not a point source like this, but I'm going to use one of my light boxes

**Dave Jones:** or something like that and put it behind so that you can see the traces through the board. And hopefully, you can actually see if there's any inner traces happening in there. So, anyway, if you got a nice even light source, you can

**Dave Jones:** light up the whole thing at once. And that can help on multi-layer boards. But hey, if you got like an internal ground plane, I mean, this one is reasonably flood filled, then yeah, there's not a lot you can do about that. And then once

**Dave Jones:** you got your images loaded in, then you can do various processing techniques on them to in this case, I've converted to black and white here, which sometimes helps. And then I've converted added a filter to find all the edges like this. And

**Dave Jones:** then you can further reduce the color. So, when you go to print these sorts of things on overhead transparencies, for example, you're pretty much left with just the traces and the pads and components and outlines of the components. And that's what you want to

**Dave Jones:** do when you it's handier to do that when you're using the overhead transparencies comparing the top and bottom layers. Okay, what I've chosen to do here as a first pass is actually get a negative of this board image here. And it looks pretty

**Dave Jones:** funky when you've done a negative. And I've scaled them to exactly the same size, done some micro rotations and things like that. I think I'm getting fairly close. So, I'll print out one as a reference and then because you'll need one as a reference

**Dave Jones:** and then you print out the other one and then you can just micro scale that if you have to. So, I think I'll print this one out on my black and white printer and see how that works out. And then

**Dave Jones:** what you do is print each layer out onto overhead transparency like this so that you can see through it and you line them up and if you scaled correctly, ta-da, they will overlay like that and all the vias you basically use the vias

**Dave Jones:** as alignment markers on there and too easy. You can now see and follow signals through top and bottom of the board and then you can either put a white page on the bottom or insert it if you just want to do one

**Dave Jones:** side and you just go on like that. So, that makes it real easy to play with and the good thing about transparencies like this is that you can now come along with some whiteboard markers like this or highlighters and you can highlight

**Dave Jones:** all the traces one by one as you do them in different colors. So, you can have all your ground all in green and all your you know, your positive rail in red and all that sort of stuff. So, you can

**Dave Jones:** you know, really make sure you don't miss anything. And I'll try and show you some of that layer alignment up close. If you have a look at those three holes over there, they're nice ones to sort of line up and you can see that there's

**Dave Jones:** holes on the top side of that and they just line up perfectly and then over this side we can get get some there and we can just line those up brilliantly in one corner and the next. But often as I

**Dave Jones:** said you'll print out like the first one and then do some micro adjustments on the second one. It often pays just to print it out on paper first. Don't waste your overhead transparencies cuz often you're not going to get it quite right

**Dave Jones:** on the first pass. Depends on um how you're good at how good you are at uh doing this sort of stuff in your um edit programs. I'm not that crash hot, but I managed to eyeball it, no problems. So, now comes the fun part of

**Dave Jones:** tracing out your circuit, and you're pretty much only going to need a basic multimeter just to uh measure and confirm some resistances, and uh maybe try and measure some capacitors in circuit, although that's usually uh not easy to do, but uh ideally what you want

**Dave Jones:** uh for measuring in-circuit resistances. So, unless you want to desolder the parts or lift one end of the part, not easy on SMD parts, for example, as opposed to the old-fashioned through-hole type, where you could lift one uh leg on the end of it pretty

**Dave Jones:** easily, then what you want, ideally, is a multimeter with a low-voltage ohms function. And neither of these multimeters here, for example, have it, but I'll show you how to check to see if it's got uh a low-voltage uh

**Dave Jones:** functionality on the resistance range. And the reason this is important is because you're measuring in-circuit. If the output voltage of your meter here is too high, then you risk turning on uh PN junctions in your circuit, and that can

**Dave Jones:** upset your reading. So, you want as low an output voltage as possible. And some old old meters, particularly back in the uh day, I'm talking the '80s, something like that, 1980s, it was very popular to have a button on there for low-voltage

**Dave Jones:** ohms function, but it seems pretty rare these days. Now, we can actually check this Brymen meter here, for example, BM257, nice little uh sort of $100 class multimeter, by the way, if you're looking for one. It's a really quite a

**Dave Jones:** nice meter. Anyway, what we can do is measure use a second meter to measure the output voltage here on our uh ohms range, and then change the range to see what output voltage we're getting. And look, on the uh 20 meg uh range here, or

**Dave Jones:** at I think it goes up to 60,000 counts, or whatever, uh we're only outputting 0.26 V, so that's not enough to turn on a a typical silicon PM uh junction. So, we can change our change our range here, and there we go,

**Dave Jones:** half a volt. That's getting towards something that would start turning on a PN junction, but still it's not bad. So, and you just go through and check all the ranges to see basically if it's under half a volt, you're probably doing

**Dave Jones:** okay. It should ordinarily be around, you know, if you're getting like 0.3 volts or under, then it's pretty good. So, the maximum we're getting out of that is 5 half a volt. So, that's not a bad meter for tracing out that circuit,

**Dave Jones:** but if we went the other direction and tried to use this Agilent U1272A, once again an excellent meter, look, we're still only getting out half a volt, but if we change our ranges, okay, that's not bad. It's not bad, but whoa, look, down at

**Dave Jones:** the ohms range, we're getting 3.2 volts. Holy crap. That's enough to even on the kilohms range. Look, 3.2 volts. There you go. So, that's not the best for using for taking in-circuit resistance measurements. It's going to switch on PN junctions. Anyway, if you

**Dave Jones:** really want to make sure and you are measuring in-circuit, measure one way like that, get a reading on your ohms range, and then swap the leads over and read it again just to see that the value is repeatable. And if that value is

**Dave Jones:** repeatable in both directions, then you know, you can be pretty certain that your meter is not turning on any in-circuit diode junctions, but not 100% guaranteed, but it's a good quick test. Anyway, that's just a little in-circuit measuring tip. So, we're ready to trace

**Dave Jones:** this circuit down, and this is the painstaking part, and pretty much resign yourself to the fact that you're going to miss something, but anyway, we can at least get a good first pass on this thing. So, we've got ourselves the pin

**Dave Jones:** outs and and get pin outs of the data sheets and all that sort of stuff. So, I've written down some pin outs of uh the most uh common parts on here that I uh didn't know or didn't want to goof up

**Dave Jones:** uh from memory. And then uh we've got our uh transparencies ready to go like this. We've got our multicolored uh highlighter uh pens, our whiteboard markers, and we've got ourselves a pencil. Pencil's important. And remember, always have a rubber on your

**Dave Jones:** pencil. And the next thing we're going to want to do is search for these pesky SMD transistor codes, and they can be a real pain in the butt. So, I just type in SMD transistor codes into Google, and

**Dave Jones:** well, look the first four hits here. I've got various uh the SMD codebook, which allows you to like the first character of the code and the bases, uh all that sort of stuff. I've got a search one, for example. So, I can bring

**Dave Jones:** in my picture on my board. Look here, we've got uh 7AT on a whole bunch of these transistors here. So, we can type in 7AT and see what we get. SMD search. an MMBT3904, your standard 3904 uh NPN transistor. No

**Dave Jones:** problems whatsoever. And then they've got entire uh catalogs like this all the way around here. And then we've got a There's one on the Digi-Key website, a Micro Commercial Components Corp uh SMD marking. And unfortunately, the issue is

**Dave Jones:** is that um there's not a huge amount of standardization on these codes. So, even uh with the same manufacturer, they can actually use the same code for different uh parts, and it's just it gets a bit messy. So, it's not an exact science,

**Dave Jones:** this. But uh yeah, it's it's not too hard to at least get a first ballpark of the codes. And here's an example of where you can get confused over exactly what a part might be. In this case, we've got two

**Dave Jones:** parts on the backside of the board that are labeled 1B. They're a SOT-23, and it can either be a standard 2222 NPN transistor, as you're familiar with here, bipolar, or it could be this one here, which is an IRLM

**Dave Jones:** L2803. And this is an N-channel MOSFET. So, it could either be a bipolar device, a regular, you know, just a regular switching transistor, 2222, or it could be this power MOSFET here. And of course, the only way to actually

**Dave Jones:** find that out is to just draw up your circuit and then look and analyze your circuit and go, "Well, does it make sense for it be to be a bipolar transistor here, or does it make sense for it to have a little power MOSFET in

**Dave Jones:** this particular position?" So, yeah, we just don't know at this stage. So, you just draw it in as a generic symbol, make a note, and then, you know, fill in the blanks later. And of course, the way you'd start something like this,

**Dave Jones:** oscilloscope, because it's got basically a single input down here on the BNC, and it's going to have an output over here. And that's pretty much it. And circuits are always drawn from inputs on the left-hand side, outputs on the

**Dave Jones:** right-hand side. That's just the common convention. So, you would start with your input here. There's our input center pin for the BNC going through a resistor here, going into our relay there. We've got our pinout for our relay. And then we just start drawing it

**Dave Jones:** step-by-step and then highlighting both the top and bottom sheets here as we go in multiple colors if you need to. And then every now and then you'll get to a point in the circuit here where you like I couldn't see where that one went to.

**Dave Jones:** So, I originally had a question mark there because it it went down into a middle layer and I couldn't see it. It wasn't on any of my transparent overlays. But once I drew the rest of it here, I managed I realized, "Well, these

**Dave Jones:** two bases must be coupled here." So, sure enough, I measured the two and they are shorted out. So, that one ends up being straight across there like that. Beauty. And likewise here, I've got another point, the resistor on the base

**Dave Jones:** of these two coupled transistors. I don't know where that goes. It went down to the bottom went down to the middle rail. Wasn't on my transparency layers. So, once again, I busted out. I knew it's a pretty sure bet it's going to be

**Dave Jones:** the negative rail down in there. And sure enough, it is. And just remember that if you're using this transparency technique, these transistors here on the bottom end all active devices will be a mirror image of what they are on the

**Dave Jones:** top. So, if we've got the top here and we've got ourselves Well, let's have a look at the photo overlay. It's a bit clearer here. If we've got a this pin here is the base, emitter, and collector of this transistor, the same transistor

**Dave Jones:** on the bottom here, because this is actually a mirror image photo, this one is not the base. This one's the base. This one's the emitter, and this one's the collector. So, it's just it's often hard to actually remember that when

**Dave Jones:** you're doing this. You can often, you know, just have a little brain fart and forget that and goof up the schematic. So, it's different if you prefer the physical technique of having the board like this and then just flipping it over

**Dave Jones:** and trying to trace things directly like that. Because then when you flip it over, you have the correct orientation as per your the pin out in your data sheet. You don't have to mentally flip things. And Murphy will, of course,

**Dave Jones:** ensure that you end up with a via that drops through to the inner layer, which you can't see on your top and bottom plots here like this. So, you get out your continuity tester. This is where a fast

**Dave Jones:** continuity tester comes in. And you put it on the point you want, for example, and then you can drag it along IC pins and every other point in the circuit. And yes, it is a systematic approach, pretty much. I mean, if you've

**Dave Jones:** already reverse engineered half the circuit, you might be able to sort of guess where it goes next depending on its function in the circuit, the the via and net that you have. But, you know, basically it's it's a systematic search

**Dave Jones:** for where that thing goes. And yes, it is tedious and this sort of stuff does take time. So, yeah, multi-layer boards can be a real pain. And yes, it can be even more annoying when your net is on

**Dave Jones:** this side of the board and you think it goes to the other side or you've checked everything on one side. So, you're going to go like this. And get the tongue at the right angle, apply just the right amount of pressure so

**Dave Jones:** that you pierce any oxide coating on the solder joint. That's another trap. And then get on the other side and start probing. Man, this is taking forever. And then the next thing you got to watch out for is traces under chips which you

**Dave Jones:** can't see like this TLV274 quad op-amp here. Now, I originally didn't trace this one. I was too busy. I got to the input to the op-amp and I was too busy tracing the FET amplifier around here and just got carried away

**Dave Jones:** and extended that out. Anyway, I've come back to here and I started tracing it out and the inverting terminal down here, pin two, drops down to a via down in here. And let's have a look at that. And you can see that it Okay, it drops

**Dave Jones:** down to the bottom side. So, we we go down to the bottom side here and it goes through a capacitor like that. So, I drew it. You know, so I drew it as I saw it. But, of course, that doesn't make any sense.

**Dave Jones:** You've got to have some sort of negative feedback happening here. So, you look at the top side again and you go, "Well, is is it going to an internal layer and then going out?" Well, it could be. I've

**Dave Jones:** already found traces on the internal layers. But, check this out. Check out these resistors here. These look like uh classic feedback resistors uh for the op-amp. And you'll notice that there's a trace going off underneath there. So, aha, does that one

**Dave Jones:** go off under there under the chip to that the backside of that pin which you can't see? Well, you get your multimeter out and you buzz it and it turns out, yep, it does. I was right on the money.

**Dave Jones:** So, yeah, you just got to watch out for those things. Use a bit of intuition when it comes to these sort of things, you know, know that uh you know, that can't possibly be right and uh you know,

**Dave Jones:** that you have to find those resistors somewhere else and they're always going to be close by. And once again, you end up getting stuck on ones like this. I mean, here's our input uh switching relay. Here's our main input AC coupling

**Dave Jones:** cap and we've got a resistor here which is uh 4.7 meg and it's going off to a via there which just goes nowhere. Like it's well, of course it goes somewhere. It goes into an inner layer, but we

**Dave Jones:** can't see traces anywhere else on the thing. Is it going off this way, that way? Uh you know, who knows what it's going to. This is where we, you know, we had no clue until we've done a good lot

**Dave Jones:** of the circuit. Now, we can have a look at the circuit and see where it can logically lead to. And here's the circuit that we've got so far. Please excuse the crudity of the model. I didn't have time to build it to scale or

**Dave Jones:** to paint it. Now, um we've got our input over here, of course. Then we've got an input attenuator here which is then uh which you can bypass with these two relays here. Uh relay contacts, it's actually the same physical relay on the

**Dave Jones:** board. It's the big large one you can see there. Down There we go. Um and what have we got? Here's our AC coupling cap in here. So, we've got a path going down here. I'll explain this later, but

**Dave Jones:** uh we've got our AC coupling cap here and we've got some uh clamping diodes, and here's this mystery 4.7 meg resistor. It's just going off to la-la land. I didn't bother tracing it back then, but where does it go now that

**Dave Jones:** we've got the rest of the circuit? Well, I couldn't find the output of this op-amp here either. It didn't make sense. It didn't go anywhere. So, you know, what the hell's going on? So, it's got to be going somewhere, the output of

**Dave Jones:** the op-amp, and I couldn't trace that one either. And I figured, well, look, this part of the circuit here, because we've got AC coming through here and DC coupling through this path selectable here via a solid state relay here. Well,

**Dave Jones:** this must be the DC path, and then over here, I figured out that we had some an e squared pot over here, the ADSR the AD 5207, and that's just buffering that, and that's feeding in. So, this must be the

**Dave Jones:** offset control for the channel, the DC offset to shift the waveform up and down, the vertical vertical position control on the front panel. So, the output of that has to be going back into here and offsetting the signal before it gets into our FET

**Dave Jones:** amplifier over here. So, by deduction, this point here must connect to this point over here. And sure enough, I buzzed it out after all this time, and bingo, that's where it went. So, if we have a look back at our

**Dave Jones:** overlay, there's our 4.7 meg resistor, and here's pin one of our chip all the way over here, the output of the op-amp there. So, this drops down here like this, and it must go under, well, yeah, it probably goes under because I

**Dave Jones:** couldn't see it through these gaps in here when you shine light through it. Couldn't see it. So, it's probably running under there like that, around there, and uh up to uh up to pin one. Yep, up to pin one over here like that.

**Dave Jones:** And woo, after all that work, we're finally finished. Well, as as finished as I want to be to figure out how this thing works, this front end works, and how they're doing the uh bandwidth selection. And yeah, this is pretty darn

**Dave Jones:** ugly. So, I've redrawn it a bit nicer. Here we go. Let's take a look at this sucker. It's drawn in Dave CAD, of course. So, let's start out here. Here's our BNC input. We've got a 75-ohm resistor, and then a selectable

**Dave Jones:** attenuator in here. So, you can bypass it. There's a common relay there. Just bypasses the whole lot. There's a little trimmer cap in there, and well, a bit of compensation across the input resistor here to smooth out the response, and

**Dave Jones:** well, nothing fancy at all. And then, uh it's AC coupled and goes into our FET input amplifier, and this is a very standard arrangement here. We've got a um a JFET on the input here, and a low impedance emitter follower output, and

**Dave Jones:** that goes off to the diff amp, which I've got on a separate sheet here. And we've just got some bias resistors here. It goes down to the negative rail, and uh also you'll see that the input here was clamped by a 599 diode. It might

**Dave Jones:** look a bit weird because I've got the ground up the top here. It's actually negative uh reference. So, we've got a Zener diode here clamping it at some uh voltage below the uh rail. So, you don't want the input any input uh transients

**Dave Jones:** to go straight onto the rail. You want them to be clamped to your Zener diode, and then you've got a 2K protection off to the rest of your rail, and that's pretty easy. So, uh that's a You'll find this configuration pretty

**Dave Jones:** much standard in tons of oscilloscopes way back to the old uh analog scope days, very very common. And uh this part here is rather interesting because um all this amp is always AC coupled. So, it's only amplifying the

**Dave Jones:** high-frequency stuff. It can't amplify the DC stuff directly from the input here. To do that, it's uh tapped off right at the output to the switch here, and this is our um AC uh DC coupling selection here. Uh like sometimes it's

**Dave Jones:** done like old analog scopes is done right in the uh input here. They will have like a big AC coupling cap in here somewhere at which you can short out, but this is done differently because we need to bias the position of our

**Dave Jones:** waveform um inside our front-end amp here for our vertical position control. So, all this section here basically um passes the DC stuff and does offset as well. Um so, if you're measuring DC on your uh scope, for example, and you've

**Dave Jones:** got uh DC selected, and it's uh bypassing uh this AC coupling cap here, then the signal is not going through here, of course, because of that's AC coupled. It's got to go through here and then up to here. And then that allows us

**Dave Jones:** to add in another DC signal here uh for our vertical position control. And they're doing that using a um Analog Devices uh AD5207 E-squared pot. You'll notice the question mark here. I didn't trace I I couldn't trace where

**Dave Jones:** that pin went. And no, it didn't go down to ground. It's gone somewhere else, and I was just went, "Uh whatever." It doesn't affect the the functionality of the circuit anyway. And I likewise here with the question mark. If you see question marks

**Dave Jones:** anywhere, it means I uh couldn't readily uh trace them, and I just gave up. I can put some more hours into it and try and find it, but anyway. Um and then we've got a couple of uh muxes here. Oh, I

**Dave Jones:** didn't label those. Uh 74HC 4053. Uh we use a couple of these in the uh Rigol front end. And look, they're putting an 8K2. You can select an 8K2 resistor in series with that E squared part. And yeah, so they're just getting various

**Dave Jones:** settings for that. And you can put in another 2K resistor as well. And then they've got some sort of amp here. I couldn't figure out where it went to. Anyway, doesn't matter. That adds in a DC signal into here and

**Dave Jones:** allows us to shift and position that waveform up and down before it gets into the ADC here. Now, one interesting thing to note, this op amp, which is a TLV274 by the way, it's only like a like a low bandwidth precision

**Dave Jones:** low power op amp. So, it's not the full bandwidth. If you're wondering why it's, you know, it they can get away with like a 3 MHz bandwidth op amp here is because all the AC stuff is going directly into

**Dave Jones:** the FET here. So, this is only affecting the DC shift offset. So, you don't need a high bandwidth op amp here. Although, in the DS2000 one as we'll take a look at the schematic, they did actually use an 8 MHz bandwidth op amp here instead

**Dave Jones:** of this 3 MHz one here. But anyway, you'll notice, if you are keen, that this is open loop. Well, it's not, okay, cuz it wouldn't work as an amplifier. So, it's got to be closed loop. But I couldn't find where

**Dave Jones:** this resistor Well, I found that this resistor went to the vertical position control here, but there's no feedback from here. I mean, it's obvious that this op amp here has to be in this feedback loop here. So, it has to tap

**Dave Jones:** off here somewhere, but darned if I could find it. I'm going to have probably have to have another shot at it. And if we have a look at the old DS1052E, I think we'll find it's much simpler than this one. And you'll see that it

**Dave Jones:** does actually feedback. And here's the schematic for the DS1052E, the older one, not the 1052Z, this new one. It was drawn by A Helene, so thank you very much, A. So, here we go. Here they are side by side. We've got our

**Dave Jones:** input attenuator here. So, it's basically exactly the same thing happening with the bypass relay there. I've just drawn it a bit expanded. He's done it like this, so a little bit different. And look, as I said, a different op-amp here. They've got the

**Dave Jones:** AD8510. I've drawn mine sort of slightly separated. That's just how I decided to do it. I wasn't referencing this one at all. So, everyone draws things slightly differently. This uses an AD8510 and it is like an 8 MHz bandwidth one.

**Dave Jones:** It's basically the same thing. Here's the AC coupling cap we had down here, which has been bypassed by the Well, in this case, it's a solid state relay. Not sure what it is inside the 1052E. There's the part number if you

**Dave Jones:** want to go look it up. And yeah, we've got the offset amp here. The same 4.7 resistor going into the JFET here. The same clamping arrangement, except they clamp it to the rails where they've got a Zener here, but basically exactly

**Dave Jones:** the same thing. And then what else have we got? Here we go. Our amp our FET amp is almost identical, almost identical. They've got another They've got a resistor in here, whereas this the emitter's tied to the collector

**Dave Jones:** here, but it doesn't matter. And they've got an output series resistor here. They didn't have it in this one or I couldn't find it. So, it's a slightly more compact configuration here. And by the way, they've got some,

**Dave Jones:** you know, fairly decent filtering here. They've got a two-stage filter for this supply. And then they've got a diode between these two. So, I'm not sure if this is powering something else. I didn't actually follow it off. So, it

**Dave Jones:** could be. Anyway, they've got some mark clamping between the rails there. And this open-loop configuration of this DC offset amp here that I was talking about and how it should ultimately be referenced back to here. Well, look, if

**Dave Jones:** you have a look on the 1052E schematic, bingo, here it is. Look, the inverting terminal of the DC offset amp there goes through an 806 K resistor directly to the output here as I thought it must be. And

**Dave Jones:** very curiously, look, they've got that same value 806 K resistor here. And I just had a look at that to verify and no, it's not actually connected over to here like that. Of course, you wouldn't, you know, have your output of your op

**Dave Jones:** amp on there. So, you know, but they've got exactly the same value resistor, exactly the same connected to the inverting terminal over here. But this one goes off to the vertical position control, whereas the 1052E just has the channel one position just

**Dave Jones:** adding into there at the lower part of that resistor divider there. So, yeah, it's, you know, they've substantially changed things. But anyway, there's got to ultimately be some feedback from here coming back and and getting through it, whether or not it comes through here,

**Dave Jones:** through the E squared pot and everything else. It could be doing that. I mean, that one there, I checked that one's not connected to there. So, I don't know what, you know, I don't know exactly what's going on there. But anyway, it's

**Dave Jones:** got to come back. Otherwise, that thing would be open-loop and it wouldn't work at all. Or it'd work as an excellent comparator. So, anyway, all of that is essentially exactly the same as what we've got here. Except the big

**Dave Jones:** difference we're going to see next. Look, this amp, here we go. This on mine, it goes off to the next page, which we'll take a look at next. But on this one, it goes into a, well, a rather

**Dave Jones:** expensive, if you're trying to save cost, an AD837 programmable gain amp here. And uh then we've got a differential driver. Once again, that's another uh analog uh No, it's a National uh part LMH uh 6552. And these things cost money, right? Uh

**Dave Jones:** they you know, even if you're uh they're not manufacturing, you know, 100 million of these scopes. So, they're not going to get them rock-bottom price. They're manufacturing, you know, tens of thousands of these scopes. So, the price of these chips actually matters. So,

**Dave Jones:** they've done away with these two chips, as we'll see, and replaced it with a complete discrete transistor solution in this design. And if you remember from our teardown video, that was the big uh surprise and takeaway from the teardown

**Dave Jones:** was that it used an all-discrete transistor solution instead of these chips, which we had before. So, that's how they've really uh reengineered and lowered the price of this 1054Z, and probably the reason why they can afford to put four channels in here, whereas

**Dave Jones:** before they could only afford to put in two. So, this is what I really wanted to see, how they've implemented this discrete transistor solution, and how they're implementing the bandwidth filter in between the models. Um so, let's take a look at it. We've basically

**Dave Jones:** got a very sta- it looks a bit complicated, but if you ignore that, okay? That doesn't exist there, okay? Then you've got a pretty standard uh diff uh arrangement here. Here's our input from our amplifier on the uh from the JFET and uh low

**Dave Jones:** impedance emitter follower on the previous side here, and it's a pretty standard uh differential uh configuration. I couldn't figure out another question mark, couldn't figure out where that uh came from. So, we've got our differential output here, and

**Dave Jones:** this comes around, and it goes straight into the ADC, of course, straight through. But then they've got these switchable uh filters hanging off here. They're switching in different value capacitors from each uh one of the differential lines down to the negative rail and they

**Dave Jones:** got four transistors which I didn't know where they go off to but they're you know, presumably go off to like the the micro controller the digital control so that they can switch these capacitors in and out and they're a matched pair of course

**Dave Jones:** so if you're going to switch on this one you would switch on this one as well and that would have an 820 puff cap from each differential line down to the negative rail and likewise you can switch in the 560 here and of course

**Dave Jones:** when you've got two different values like this you can actually have four different configurations. You can have none on at all so they're not having any effect on the line and it just passes straight through so that would be full

**Dave Jones:** bandwidth or you can turn on the 560 puff caps here and that would decrease your bandwidth again by small amount and then you can switch in your eight and then disable that one and switch in your 820 puff here and that would have yet

**Dave Jones:** another bandwidth and then if you really wanted to you could switch on all four transistors and have them in parallel and that would give you your greatest bandwidth reduction. So there's four different selectable bandwidths there and they're doing that on the

**Dave Jones:** differential line. Very interesting. So it looks like they've put a bit of thought into this and the DS1052Z of course is only a recent model so but it looks like that they've planned it way back when they originally designed

**Dave Jones:** this thing because they've put in four different bandwidth configurations here. So presumably you turn them all off and that's 100 megahertz or maybe they've got the 560 puff on for the 100 megahertz or whatever and then they turn

**Dave Jones:** the 820 puffs on to give you the 70 megahertz bandwidth model and then they might turn both on or four on there to give you the 50 MHz DS1052Z. So, I think that's how they're doing the bandwidth selection. And of course,

**Dave Jones:** that's all going to be under software control as well. So, when they program the thing, they program the model number at the factory and it gives it your software controlled bandwidth. But, what's going on under this lens cap

**Dave Jones:** here? Well, let's take a look at that, shall we? Basically, they're duplicating the exact configuration again. So, imagine that's now gone, right? That's now gone and we're and we're looking at exactly the same thing cuz the input comes in here and drives both bases

**Dave Jones:** there, but they have selectable control over here. Once again, the base of these transistors, these bias transistors down the bottom have the go into a HC4053, so they can switch select one or the other. And what's the difference between the two? Well, the

**Dave Jones:** only thing I could find is look, this has a 200 ohm series resistor. This has a 680 ohm. They both have 1K twos in there, so they are different. So, what's happening here is I believe that is the

**Dave Jones:** bandwidth selection for the 20 MHz bandwidth filtering. They're doing that in the differential amplifier itself. Oh, and by the way, I haven't drawn it in, but just as an aside, from the differential output here, they were actually tapping off two of those. One's

**Dave Jones:** going into a TL072. That's what the TL072's for. They've got some PNP BC856's here and I couldn't figure out the feedback configuration there, but anyway, they're just obviously some sort of drivers, nothing to do with the bandwidth configuration. Anyway, I

**Dave Jones:** haven't gone that far. This is what I really needed to know. This was the money shot. Woo. So, there you go. Little attempt here at reverse engineering the new Rigol DS1052Z and I found some interesting stuff in there, and that's what I was after. This

**Dave Jones:** wasn't a complete reverse engineering effort to do absolutely the whole board. I really just wanted to find out what was going on in that discrete amplifier uh front end there, and there might be errors in this. I haven't taken it,

**Dave Jones:** haven't simulated it, any of that sort of stuff. That'll be the next step to make sure uh haven't even sanity checked it, haven't double checked it, done whatever. So, if you do see any obvious errors in here, uh please let me know,

**Dave Jones:** and I can correct them. But, yeah, we found some interesting stuff how they're doing the bandwidth limiting in there. So, I hope you enjoyed that uh little look at just one technique for reverse engineering a uh board like this. There

**Dave Jones:** are everyone's got their own way of doing it, and depends on the board. Uh you know, you might do it uh differently, but this was actually a bit of a pain in the ass being a multi-layer board, quite a few traces going off uh

**Dave Jones:** where I couldn't uh see them. And obviously, if you had if you're lucky enough to have like an X-ray machine or something, that'd be really handy to um do stuff like that. But, anyway, so this did if you think that this is like an

**Dave Jones:** hour or two's work, uh think again. A lot of hour I put a lot of hours into actually uh just getting this far. It was lots of you know, red herrings and uh little you know, dead end traps and stuff like that, and

**Dave Jones:** just really kind of annoying and tedious work to do. But, hey, if you want to reverse engineer something like this, this is what you have to do. And if you really wanted to be 100% sure, you'd have to go through and check it or get

**Dave Jones:** someone else to check it, and then you got to simulate it to make sure it all works, and you got the correct uh you know, configuration, you haven't left anything out. And I guarantee there's an error or two in there, but eh,

**Dave Jones:** I found out what I wanted to find out, and that's the main thing. So, as always, um I'll link in all the data sheets and everything for this these uh chips. I'll scan in these little uh data drawings and you can have a look at

**Dave Jones:** those. And uh please, if you see any errors, let me know. If you've got any comments, please leave them down below or on the EEVblog forum. And don't forget, if you like the video, please give it a big thumbs up cuz that helps a

**Dave Jones:** lot. It really does with all the YouTube-y search stuff and things like that. It keeps me up the top. So, thanks. Catch you next time.
