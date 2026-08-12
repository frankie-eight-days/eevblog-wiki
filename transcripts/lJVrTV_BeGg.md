---
video_id: lJVrTV_BeGg
title: EEVblog #675 - How To Reverse Engineer A Rigol DS1054Z
url: https://www.youtube.com/watch?v=lJVrTV_BeGg
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 30, "3": 44, "4": 60, "5": 72, "6": 89, "7": 99, "8": 117, "9": 126, "10": 141, "11": 151, "12": 161, "13": 170, "14": 180, "15": 192, "16": 211, "17": 226, "18": 235, "19": 245, "20": 272, "21": 283, "22": 299, "23": 308, "24": 329, "25": 338, "26": 352, "27": 375, "28": 391, "29": 401, "30": 413, "31": 428, "32": 439, "33": 448, "34": 460, "35": 475, "36": 487, "37": 509, "38": 521, "39": 540, "40": 554, "41": 569, "42": 582, "43": 593, "44": 603, "45": 616, "46": 626, "47": 645, "48": 657, "49": 668, "50": 678, "51": 698, "52": 713, "53": 730, "54": 746, "55": 757, "56": 772, "57": 786, "58": 800, "59": 811, "60": 822, "61": 838, "62": 859, "63": 875, "64": 890, "65": 899, "66": 914, "67": 928, "68": 940, "69": 949, "70": 964, "71": 980, "72": 991, "73": 1005, "74": 1011, "75": 1021, "76": 1033, "77": 1044, "78": 1056, "79": 1073, "80": 1089, "81": 1102, "82": 1114, "83": 1124, "84": 1136, "85": 1147, "86": 1159, "87": 1168, "88": 1180, "89": 1191, "90": 1207, "91": 1227, "92": 1241, "93": 1251, "94": 1263, "95": 1275, "96": 1288, "97": 1298, "98": 1307, "99": 1319, "100": 1336, "101": 1345, "102": 1357, "103": 1370, "104": 1390, "105": 1406, "106": 1427, "107": 1450, "108": 1465, "109": 1478, "110": 1488, "111": 1498, "112": 1510, "113": 1527, "114": 1542, "115": 1552, "116": 1567, "117": 1579, "118": 1596, "119": 1608, "120": 1620, "121": 1630, "122": 1642, "123": 1656, "124": 1667, "125": 1686, "126": 1698, "127": 1711, "128": 1718, "129": 1731, "130": 1749, "131": 1761, "132": 1771, "133": 1785, "134": 1801, "135": 1808, "136": 1821, "137": 1830, "138": 1845, "139": 1858, "140": 1874, "141": 1886, "142": 1899, "143": 1910, "144": 1925, "145": 1935, "146": 1946, "147": 1974, "148": 1993, "149": 2018, "150": 2027, "151": 2053, "152": 2074, "153": 2085, "154": 2096, "155": 2110, "156": 2123, "157": 2133, "158": 2152, "159": 2171, "160": 2188, "161": 2200, "162": 2209, "163": 2219, "164": 2227, "165": 2239, "166": 2252, "167": 2271, "168": 2288, "169": 2301, "170": 2311, "171": 2321}
---

**Dave Jones:** Hi, in my previous video I did a teardown of the new Rigol DS1052Z. There it is, it's still in bits. And an amazingly low cost oscilloscope for four channels, 399 bucks.

**Dave Jones:** It's absolutely incredible. So, I was curious to know how they've actually re-engineered the the input analog front-end channels on these to lower the price point and get four channels for the price of two.

**Dave Jones:** And as we saw in the previous teardown, which if if you haven't seen, I'll link it in down below, check it out first. I noted that they had gone for a an entirely discrete transistor-based front-end pretty much.

**Dave Jones:** So, I figured how are they doing it? And also, how are they doing the bandwidth limiting on this thing because the model, whether it's 50 MHz, 70 MHz, or 100 MHz, it's just a software-configurable thing.

**Dave Jones:** So, how are they changing that and limiting the bandwidth inside the scope? There's only one way to find out, reverse engineer it. Let's go. And the first thing you're going to want to do is take a photo of both sides of the board.

**Dave Jones:** So, I got my camera set up on the tripod here, and I'm actually using a high F-stop here so that I get a really deep depth of field so that high components aren't out of focus, and I'm making sure I'm focusing directly on like the smallest dot surface mount component on the board.

**Dave Jones:** So, I'm going to keep that. So, hence using the high F-stop value is going to give me a long shutter speed. In this case, it's like half a second or something.

**Dave Jones:** So, I can't hand hold this thing. Got to set up on the tripod, and I'm going to just set the frame just right, and I'm going to try and keep the same frame for both shots when I flip the board over just so that I can get pretty close to the correct scale factor inside the camera.

**Dave Jones:** You don't have to do that. You might you can and might ultimately have to scale the images in software later, but anyway, it's nice if you can just get it first go.

**Dave Jones:** And also, just make sure you've got decent lighting. The reason I've got it at a big angle like this is because if I had it flat like that, straight up like that, it would get a shadow in from the cans up here due to my overhead lights.

**Dave Jones:** So, you really want some decent light. You know, if you got one of those light tents or something like that, then you can get really good shots. And what you also want to do is get a torch.

**Dave Jones:** Maybe not a point source like this, but I'm going to use one of my light boxes or something like that and put it behind so that you can see the traces through the board.

**Dave Jones:** And hopefully, you can actually see if there's any inner traces happening in there. So, anyway, if you got a nice even light source, you can light up the whole thing at once.

**Dave Jones:** And that can help on multi-layer boards. But hey, if you got like an internal ground plane, I mean, this one is reasonably flood filled, then yeah, there's not a lot you can do about that.

**Dave Jones:** And then once you got your images loaded in, then you can do various processing techniques on them to in this case, I've converted to black and white here, which sometimes helps.

**Dave Jones:** And then I've converted added a filter to find all the edges like this. And then you can further reduce the color. So, when you go to print these sorts of things on overhead transparencies, for example, you're pretty much left with just the traces and the pads and components and outlines of the components.

**Dave Jones:** And that's what you want to do when you it's handier to do that when you're using the overhead transparencies comparing the top and bottom layers. Okay, what I've chosen to do here as a first pass is actually get a negative of this board image here.

**Dave Jones:** And it looks pretty funky when you've done a negative. And I've scaled them to exactly the same size, done some micro rotations and things like that. I think I'm getting fairly close.

**Dave Jones:** So, I'll print out one as a reference and then because you'll need one as a reference and then you print out the other one and then you can just micro scale that if you have to.

**Dave Jones:** So, I think I'll print this one out on my black and white printer and see how that works out. And then what you do is print each layer out onto overhead transparency like this so that you can see through it and you line them up and if you scaled correctly, ta-da, they will overlay like that and all the vias you basically use the vias as alignment markers on there and

**Dave Jones:** too easy. You can now see and follow signals through top and bottom of the board and then you can either put a white page on the bottom or insert it if you just want to do one side and you just go on like that.

**Dave Jones:** So, that makes it real easy to play with and the good thing about transparencies like this is that you can now come along with some whiteboard markers like this or highlighters and you can highlight all the traces one by one as you do them in different colors.

**Dave Jones:** So, you can have all your ground all in green and all your you know, your positive rail in red and all that sort of stuff. So, you can you know, really make sure you don't miss anything.

**Dave Jones:** And I'll try and show you some of that layer alignment up close. If you have a look at those three holes over there, they're nice ones to sort of line up and you can see that there's holes on the top side of that and they just line up perfectly and then over this side we can get get some there and we can just line those up brilliantly in

**Dave Jones:** one corner and the next. But often as I said you'll print out like the first one and then do some micro adjustments on the second one. It often pays just to print it out on paper first.

**Dave Jones:** Don't waste your overhead transparencies cuz often you're not going to get it quite right on the first pass. Depends on um how you're good at how good you are at uh doing this sort of stuff in your um edit programs.

**Dave Jones:** I'm not that crash hot, but I managed to eyeball it, no problems. So, now comes the fun part of tracing out your circuit, and you're pretty much only going to need a basic multimeter just to uh measure and confirm some resistances, and uh maybe try and measure some capacitors in circuit, although that's usually uh not easy to do, but uh ideally what you want uh for measuring in-circuit resistances.

**Dave Jones:** So, unless you want to desolder the parts or lift one end of the part, not easy on SMD parts, for example, as opposed to the old-fashioned through-hole type, where you could lift one uh leg on the end of it pretty easily, then what you want, ideally, is a multimeter with a low-voltage ohms function.

**Dave Jones:** And neither of these multimeters here, for example, have it, but I'll show you how to check to see if it's got uh a low-voltage uh functionality on the resistance range.

**Dave Jones:** And the reason this is important is because you're measuring in-circuit. If the output voltage of your meter here is too high, then you risk turning on uh PN junctions in your circuit, and that can upset your reading.

**Dave Jones:** So, you want as low an output voltage as possible. And some old old meters, particularly back in the uh day, I'm talking the '80s, something like that, 1980s, it was very popular to have a button on there for low-voltage ohms function, but it seems pretty rare these days.

**Dave Jones:** Now, we can actually check this Brymen meter here, for example, BM257, nice little uh sort of $100 class multimeter, by the way, if you're looking for one. It's a really quite a nice meter.

**Dave Jones:** Anyway, what we can do is measure use a second meter to measure the output voltage here on our uh ohms range, and then change the range to see what output voltage we're getting.

**Dave Jones:** And look, on the uh 20 meg uh range here, or at I think it goes up to 60,000 counts, or whatever, uh we're only outputting 0.26 V, so that's not enough to turn on a a typical silicon PM uh junction.

**Dave Jones:** So, we can change our change our range here, and there we go, half a volt. That's getting towards something that would start turning on a PN junction, but still it's not bad.

**Dave Jones:** So, and you just go through and check all the ranges to see basically if it's under half a volt, you're probably doing okay. It should ordinarily be around, you know, if you're getting like 0.3 volts or under, then it's pretty good.

**Dave Jones:** So, the maximum we're getting out of that is 5 half a volt. So, that's not a bad meter for tracing out that circuit, but if we went the other direction and tried to use this Agilent U1272A, once again an excellent meter, look, we're still only getting out half a volt, but if we change our ranges, okay, that's not bad.

**Dave Jones:** It's not bad, but whoa, look, down at the ohms range, we're getting 3.2 volts. Holy crap. That's enough to even on the kilohms range. Look, 3.2 volts. There you go.

**Dave Jones:** So, that's not the best for using for taking in-circuit resistance measurements. It's going to switch on PN junctions. Anyway, if you really want to make sure and you are measuring in-circuit, measure one way like that, get a reading on your ohms range, and then swap the leads over and read it again just to see that the value is repeatable.

**Dave Jones:** And if that value is repeatable in both directions, then you know, you can be pretty certain that your meter is not turning on any in-circuit diode junctions, but not 100% guaranteed, but it's a good quick test.

**Dave Jones:** Anyway, that's just a little in-circuit measuring tip. So, we're ready to trace this circuit down, and this is the painstaking part, and pretty much resign yourself to the fact that you're going to miss something, but anyway, we can at least get a good first pass on this thing.

**Dave Jones:** So, we've got ourselves the pin outs and and get pin outs of the data sheets and all that sort of stuff. So, I've written down some pin outs of uh the most uh common parts on here that I uh didn't know or didn't want to goof up uh from memory.

**Dave Jones:** And then uh we've got our uh transparencies ready to go like this. We've got our multicolored uh highlighter uh pens, our whiteboard markers, and we've got ourselves a pencil.

**Dave Jones:** Pencil's important. And remember, always have a rubber on your pencil. And the next thing we're going to want to do is search for these pesky SMD transistor codes, and they can be a real pain in the butt.

**Dave Jones:** So, I just type in SMD transistor codes into Google, and well, look the first four hits here. I've got various uh the SMD codebook, which allows you to like the first character of the code and the bases, uh all that sort of stuff.

**Dave Jones:** I've got a search one, for example. So, I can bring in my picture on my board. Look here, we've got uh 7AT on a whole bunch of these transistors here.

**Dave Jones:** So, we can type in 7AT and see what we get. SMD search. an MMBT3904, your standard 3904 uh NPN transistor. No problems whatsoever. And then they've got entire uh catalogs like this all the way around here.

**Dave Jones:** And then we've got a There's one on the Digi-Key website, a Micro Commercial Components Corp uh SMD marking. And unfortunately, the issue is is that um there's not a huge amount of standardization on these codes.

**Dave Jones:** So, even uh with the same manufacturer, they can actually use the same code for different uh parts, and it's just it gets a bit messy. So, it's not an exact science, this.

**Dave Jones:** But uh yeah, it's it's not too hard to at least get a first ballpark of the codes. And here's an example of where you can get confused over exactly what a part might be.

**Dave Jones:** In this case, we've got two parts on the backside of the board that are labeled 1B. They're a SOT-23, and it can either be a standard 2222 NPN transistor, as you're familiar with here, bipolar, or it could be this one here, which is an IRLM L2803.

**Dave Jones:** And this is an N-channel MOSFET. So, it could either be a bipolar device, a regular, you know, just a regular switching transistor, 2222, or it could be this power MOSFET here.

**Dave Jones:** And of course, the only way to actually find that out is to just draw up your circuit and then look and analyze your circuit and go, "Well, does it make sense for it be to be a bipolar transistor here, or does it make sense for it to have a little power MOSFET in this particular position?" So, yeah, we just don't know at this stage.

**Dave Jones:** So, you just draw it in as a generic symbol, make a note, and then, you know, fill in the blanks later. And of course, the way you'd start something like this, oscilloscope, because it's got basically a single input down here on the BNC, and it's going to have an output over here.

**Dave Jones:** And that's pretty much it. And circuits are always drawn from inputs on the left-hand side, outputs on the right-hand side. That's just the common convention. So, you would start with your input here.

**Dave Jones:** There's our input center pin for the BNC going through a resistor here, going into our relay there. We've got our pinout for our relay. And then we just start drawing it step-by-step and then highlighting both the top and bottom sheets here as we go in multiple colors if you need to.

**Dave Jones:** And then every now and then you'll get to a point in the circuit here where you like I couldn't see where that one went to. So, I originally had a question mark there because it it went down into a middle layer and I couldn't see it.

**Dave Jones:** It wasn't on any of my transparent overlays. But once I drew the rest of it here, I managed I realized, "Well, these two bases must be coupled here." So, sure enough, I measured the two and they are shorted out.

**Dave Jones:** So, that one ends up being straight across there like that. Beauty. And likewise here, I've got another point, the resistor on the base of these two coupled transistors. I don't know where that goes.

**Dave Jones:** It went down to the bottom went down to the middle rail. Wasn't on my transparency layers. So, once again, I busted out. I knew it's a pretty sure bet it's going to be the negative rail down in there.

**Dave Jones:** And sure enough, it is. And just remember that if you're using this transparency technique, these transistors here on the bottom end all active devices will be a mirror image of what they are on the top.

**Dave Jones:** So, if we've got the top here and we've got ourselves Well, let's have a look at the photo overlay. It's a bit clearer here. If we've got a this pin here is the base, emitter, and collector of this transistor, the same transistor on the bottom here, because this is actually a mirror image photo, this one is not the base.

**Dave Jones:** This one's the base. This one's the emitter, and this one's the collector. So, it's just it's often hard to actually remember that when you're doing this. You can often, you know, just have a little brain fart and forget that and goof up the schematic.

**Dave Jones:** So, it's different if you prefer the physical technique of having the board like this and then just flipping it over and trying to trace things directly like that. Because then when you flip it over, you have the correct orientation as per your the pin out in your data sheet.

**Dave Jones:** You don't have to mentally flip things. And Murphy will, of course, ensure that you end up with a via that drops through to the inner layer, which you can't see on your top and bottom plots here like this.

**Dave Jones:** So, you get out your continuity tester. This is where a fast continuity tester comes in. And you put it on the point you want, for example, and then you can drag it along IC pins and every other point in the circuit.

**Dave Jones:** And yes, it is a systematic approach, pretty much. I mean, if you've already reverse engineered half the circuit, you might be able to sort of guess where it goes next depending on its function in the circuit, the the via and net that you have.

**Dave Jones:** But, you know, basically it's it's a systematic search for where that thing goes. And yes, it is tedious and this sort of stuff does take time. So, yeah, multi-layer boards can be a real pain.

**Dave Jones:** And yes, it can be even more annoying when your net is on this side of the board and you think it goes to the other side or you've checked everything on one side.

**Dave Jones:** So, you're going to go like this. And get the tongue at the right angle, apply just the right amount of pressure so that you pierce any oxide coating on the solder joint.

**Dave Jones:** That's another trap. And then get on the other side and start probing. Man, this is taking forever. And then the next thing you got to watch out for is traces under chips which you can't see like this TLV274 quad op-amp here.

**Dave Jones:** Now, I originally didn't trace this one. I was too busy. I got to the input to the op-amp and I was too busy tracing the FET amplifier around here and just got carried away and extended that out.

**Dave Jones:** Anyway, I've come back to here and I started tracing it out and the inverting terminal down here, pin two, drops down to a via down in here. And let's have a look at that.

**Dave Jones:** And you can see that it Okay, it drops down to the bottom side. So, we we go down to the bottom side here and it goes through a capacitor like that.

**Dave Jones:** So, I drew it. You know, so I drew it as I saw it. But, of course, that doesn't make any sense. You've got to have some sort of negative feedback happening here.

**Dave Jones:** So, you look at the top side again and you go, "Well, is is it going to an internal layer and then going out?" Well, it could be. I've already found traces on the internal layers.

**Dave Jones:** But, check this out. Check out these resistors here. These look like uh classic feedback resistors uh for the op-amp. And you'll notice that there's a trace going off underneath there.

**Dave Jones:** So, aha, does that one go off under there under the chip to that the backside of that pin which you can't see? Well, you get your multimeter out and you buzz it and it turns out, yep, it does.

**Dave Jones:** I was right on the money. So, yeah, you just got to watch out for those things. Use a bit of intuition when it comes to these sort of things, you know, know that uh you know, that can't possibly be right and uh you know, that you have to find those resistors somewhere else and they're always going to be close by.

**Dave Jones:** And once again, you end up getting stuck on ones like this. I mean, here's our input uh switching relay. Here's our main input AC coupling cap and we've got a resistor here which is uh 4.7 meg and it's going off to a via there which just goes nowhere.

**Dave Jones:** Like it's well, of course it goes somewhere. It goes into an inner layer, but we can't see traces anywhere else on the thing. Is it going off this way, that way?

**Dave Jones:** Uh you know, who knows what it's going to. This is where we, you know, we had no clue until we've done a good lot of the circuit. Now, we can have a look at the circuit and see where it can logically lead to.

**Dave Jones:** And here's the circuit that we've got so far. Please excuse the crudity of the model. I didn't have time to build it to scale or to paint it. Now, um we've got our input over here, of course.

**Dave Jones:** Then we've got an input attenuator here which is then uh which you can bypass with these two relays here. Uh relay contacts, it's actually the same physical relay on the board.

**Dave Jones:** It's the big large one you can see there. Down There we go. Um and what have we got? Here's our AC coupling cap in here. So, we've got a path going down here.

**Dave Jones:** I'll explain this later, but uh we've got our AC coupling cap here and we've got some uh clamping diodes, and here's this mystery 4.7 meg resistor. It's just going off to la-la land.

**Dave Jones:** I didn't bother tracing it back then, but where does it go now that we've got the rest of the circuit? Well, I couldn't find the output of this op-amp here either.

**Dave Jones:** It didn't make sense. It didn't go anywhere. So, you know, what the hell's going on? So, it's got to be going somewhere, the output of the op-amp, and I couldn't trace that one either.

**Dave Jones:** And I figured, well, look, this part of the circuit here, because we've got AC coming through here and DC coupling through this path selectable here via a solid state relay here.

**Dave Jones:** Well, this must be the DC path, and then over here, I figured out that we had some an e squared pot over here, the ADSR the AD 5207, and that's just buffering that, and that's feeding in.

**Dave Jones:** So, this must be the offset control for the channel, the DC offset to shift the waveform up and down, the vertical vertical position control on the front panel. So, the output of that has to be going back into here and offsetting the signal before it gets into our FET amplifier over here.

**Dave Jones:** So, by deduction, this point here must connect to this point over here. And sure enough, I buzzed it out after all this time, and bingo, that's where it went.

**Dave Jones:** So, if we have a look back at our overlay, there's our 4.7 meg resistor, and here's pin one of our chip all the way over here, the output of the op-amp there.

**Dave Jones:** So, this drops down here like this, and it must go under, well, yeah, it probably goes under because I couldn't see it through these gaps in here when you shine light through it.

**Dave Jones:** Couldn't see it. So, it's probably running under there like that, around there, and uh up to uh up to pin one. Yep, up to pin one over here like that.

**Dave Jones:** And woo, after all that work, we're finally finished. Well, as as finished as I want to be to figure out how this thing works, this front end works, and how they're doing the uh bandwidth selection.

**Dave Jones:** And yeah, this is pretty darn ugly. So, I've redrawn it a bit nicer. Here we go. Let's take a look at this sucker. It's drawn in Dave CAD, of course.

**Dave Jones:** So, let's start out here. Here's our BNC input. We've got a 75-ohm resistor, and then a selectable attenuator in here. So, you can bypass it. There's a common relay there.

**Dave Jones:** Just bypasses the whole lot. There's a little trimmer cap in there, and well, a bit of compensation across the input resistor here to smooth out the response, and well, nothing fancy at all.

**Dave Jones:** And then, uh it's AC coupled and goes into our FET input amplifier, and this is a very standard arrangement here. We've got a um a JFET on the input here, and a low impedance emitter follower output, and that goes off to the diff amp, which I've got on a separate sheet here.

**Dave Jones:** And we've just got some bias resistors here. It goes down to the negative rail, and uh also you'll see that the input here was clamped by a 599 diode.

**Dave Jones:** It might look a bit weird because I've got the ground up the top here. It's actually negative uh reference. So, we've got a Zener diode here clamping it at some uh voltage below the uh rail.

**Dave Jones:** So, you don't want the input any input uh transients to go straight onto the rail. You want them to be clamped to your Zener diode, and then you've got a 2K protection off to the rest of your rail, and that's pretty easy.

**Dave Jones:** So, uh that's a You'll find this configuration pretty much standard in tons of oscilloscopes way back to the old uh analog scope days, very very common. And uh this part here is rather interesting because um all this amp is always AC coupled.

**Dave Jones:** So, it's only amplifying the high-frequency stuff. It can't amplify the DC stuff directly from the input here. To do that, it's uh tapped off right at the output to the switch here, and this is our um AC uh DC coupling selection here.

**Dave Jones:** Uh like sometimes it's done like old analog scopes is done right in the uh input here. They will have like a big AC coupling cap in here somewhere at which you can short out, but this is done differently because we need to bias the position of our waveform um inside our front-end amp here for our vertical position control.

**Dave Jones:** So, all this section here basically um passes the DC stuff and does offset as well. Um so, if you're measuring DC on your uh scope, for example, and you've got uh DC selected, and it's uh bypassing uh this AC coupling cap here, then the signal is not going through here, of course, because of that's AC coupled.

**Dave Jones:** It's got to go through here and then up to here. And then that allows us to add in another DC signal here uh for our vertical position control. And they're doing that using a um Analog Devices uh AD5207 E-squared pot.

**Dave Jones:** You'll notice the question mark here. I didn't trace I I couldn't trace where that pin went. And no, it didn't go down to ground. It's gone somewhere else, and I was just went, "Uh whatever." It doesn't affect the the functionality of the circuit anyway.

**Dave Jones:** And I likewise here with the question mark. If you see question marks anywhere, it means I uh couldn't readily uh trace them, and I just gave up. I can put some more hours into it and try and find it, but anyway.

**Dave Jones:** Um and then we've got a couple of uh muxes here. Oh, I didn't label those. Uh 74HC 4053. Uh we use a couple of these in the uh Rigol front end.

**Dave Jones:** And look, they're putting an 8K2. You can select an 8K2 resistor in series with that E squared part. And yeah, so they're just getting various settings for that. And you can put in another 2K resistor as well.

**Dave Jones:** And then they've got some sort of amp here. I couldn't figure out where it went to. Anyway, doesn't matter. That adds in a DC signal into here and allows us to shift and position that waveform up and down before it gets into the ADC here.

**Dave Jones:** Now, one interesting thing to note, this op amp, which is a TLV274 by the way, it's only like a like a low bandwidth precision low power op amp. So, it's not the full bandwidth.

**Dave Jones:** If you're wondering why it's, you know, it they can get away with like a 3 MHz bandwidth op amp here is because all the AC stuff is going directly into the FET here.

**Dave Jones:** So, this is only affecting the DC shift offset. So, you don't need a high bandwidth op amp here. Although, in the DS2000 one as we'll take a look at the schematic, they did actually use an 8 MHz bandwidth op amp here instead of this 3 MHz one here.

**Dave Jones:** But anyway, you'll notice, if you are keen, that this is open loop. Well, it's not, okay, cuz it wouldn't work as an amplifier. So, it's got to be closed loop.

**Dave Jones:** But I couldn't find where this resistor Well, I found that this resistor went to the vertical position control here, but there's no feedback from here. I mean, it's obvious that this op amp here has to be in this feedback loop here.

**Dave Jones:** So, it has to tap off here somewhere, but darned if I could find it. I'm going to have probably have to have another shot at it. And if we have a look at the old DS1052E, I think we'll find it's much simpler than this one.

**Dave Jones:** And you'll see that it does actually feedback. And here's the schematic for the DS1052E, the older one, not the 1052Z, this new one. It was drawn by A Helene, so thank you very much, A.

**Dave Jones:** So, here we go. Here they are side by side. We've got our input attenuator here. So, it's basically exactly the same thing happening with the bypass relay there. I've just drawn it a bit expanded.

**Dave Jones:** He's done it like this, so a little bit different. And look, as I said, a different op-amp here. They've got the AD8510. I've drawn mine sort of slightly separated.

**Dave Jones:** That's just how I decided to do it. I wasn't referencing this one at all. So, everyone draws things slightly differently. This uses an AD8510 and it is like an 8 MHz bandwidth one.

**Dave Jones:** It's basically the same thing. Here's the AC coupling cap we had down here, which has been bypassed by the Well, in this case, it's a solid state relay. Not sure what it is inside the 1052E.

**Dave Jones:** There's the part number if you want to go look it up. And yeah, we've got the offset amp here. The same 4.7 resistor going into the JFET here. The same clamping arrangement, except they clamp it to the rails where they've got a Zener here, but basically exactly the same thing.

**Dave Jones:** And then what else have we got? Here we go. Our amp our FET amp is almost identical, almost identical. They've got another They've got a resistor in here, whereas this the emitter's tied to the collector here, but it doesn't matter.

**Dave Jones:** And they've got an output series resistor here. They didn't have it in this one or I couldn't find it. So, it's a slightly more compact configuration here. And by the way, they've got some, you know, fairly decent filtering here.

**Dave Jones:** They've got a two-stage filter for this supply. And then they've got a diode between these two. So, I'm not sure if this is powering something else. I didn't actually follow it off.

**Dave Jones:** So, it could be. Anyway, they've got some mark clamping between the rails there. And this open-loop configuration of this DC offset amp here that I was talking about and how it should ultimately be referenced back to here.

**Dave Jones:** Well, look, if you have a look on the 1052E schematic, bingo, here it is. Look, the inverting terminal of the DC offset amp there goes through an 806 K resistor directly to the output here as I thought it must be.

**Dave Jones:** And very curiously, look, they've got that same value 806 K resistor here. And I just had a look at that to verify and no, it's not actually connected over to here like that.

**Dave Jones:** Of course, you wouldn't, you know, have your output of your op amp on there. So, you know, but they've got exactly the same value resistor, exactly the same connected to the inverting terminal over here.

**Dave Jones:** But this one goes off to the vertical position control, whereas the 1052E just has the channel one position just adding into there at the lower part of that resistor divider there.

**Dave Jones:** So, yeah, it's, you know, they've substantially changed things. But anyway, there's got to ultimately be some feedback from here coming back and and getting through it, whether or not it comes through here, through the E squared pot and everything else.

**Dave Jones:** It could be doing that. I mean, that one there, I checked that one's not connected to there. So, I don't know what, you know, I don't know exactly what's going on there.

**Dave Jones:** But anyway, it's got to come back. Otherwise, that thing would be open-loop and it wouldn't work at all. Or it'd work as an excellent comparator. So, anyway, all of that is essentially exactly the same as what we've got here.

**Dave Jones:** Except the big difference we're going to see next. Look, this amp, here we go. This on mine, it goes off to the next page, which we'll take a look at next.

**Dave Jones:** But on this one, it goes into a, well, a rather expensive, if you're trying to save cost, an AD837 programmable gain amp here. And uh then we've got a differential driver.

**Dave Jones:** Once again, that's another uh analog uh No, it's a National uh part LMH uh 6552. And these things cost money, right? Uh they you know, even if you're uh they're not manufacturing, you know, 100 million of these scopes.

**Dave Jones:** So, they're not going to get them rock-bottom price. They're manufacturing, you know, tens of thousands of these scopes. So, the price of these chips actually matters. So, they've done away with these two chips, as we'll see, and replaced it with a complete discrete transistor solution in this design.

**Dave Jones:** And if you remember from our teardown video, that was the big uh surprise and takeaway from the teardown was that it used an all-discrete transistor solution instead of these chips, which we had before.

**Dave Jones:** So, that's how they've really uh reengineered and lowered the price of this 1054Z, and probably the reason why they can afford to put four channels in here, whereas before they could only afford to put in two.

**Dave Jones:** So, this is what I really wanted to see, how they've implemented this discrete transistor solution, and how they're implementing the bandwidth filter in between the models. Um so, let's take a look at it.

**Dave Jones:** We've basically got a very sta- it looks a bit complicated, but if you ignore that, okay? That doesn't exist there, okay? Then you've got a pretty standard uh diff uh arrangement here.

**Dave Jones:** Here's our input from our amplifier on the uh from the JFET and uh low impedance emitter follower on the previous side here, and it's a pretty standard uh differential uh configuration.

**Dave Jones:** I couldn't figure out another question mark, couldn't figure out where that uh came from. So, we've got our differential output here, and this comes around, and it goes straight into the ADC, of course, straight through.

**Dave Jones:** But then they've got these switchable uh filters hanging off here. They're switching in different value capacitors from each uh one of the differential lines down to the negative rail and they got four transistors which I didn't know where they go off to but they're you know, presumably go off to like the the micro controller the digital control so that they can switch these capacitors in and out and they're a matched pair of course

**Dave Jones:** so if you're going to switch on this one you would switch on this one as well and that would have an 820 puff cap from each differential line down to the negative rail and likewise you can switch in the 560 here and of course when you've got two different values like this you can actually have four different configurations.

**Dave Jones:** You can have none on at all so they're not having any effect on the line and it just passes straight through so that would be full bandwidth or you can turn on the 560 puff caps here and that would decrease your bandwidth again by small amount and then you can switch in your eight and then disable that one and switch in your 820 puff here and that would have yet

**Dave Jones:** another bandwidth and then if you really wanted to you could switch on all four transistors and have them in parallel and that would give you your greatest bandwidth reduction.

**Dave Jones:** So there's four different selectable bandwidths there and they're doing that on the differential line. Very interesting. So it looks like they've put a bit of thought into this and the DS1052Z of course is only a recent model so but it looks like that they've planned it way back when they originally designed this thing because they've put in four different bandwidth configurations here.

**Dave Jones:** So presumably you turn them all off and that's 100 megahertz or maybe they've got the 560 puff on for the 100 megahertz or whatever and then they turn the 820 puffs on to give you the 70 megahertz bandwidth model and then they might turn both on or four on there to give you the 50 MHz DS1052Z.

**Dave Jones:** So, I think that's how they're doing the bandwidth selection. And of course, that's all going to be under software control as well. So, when they program the thing, they program the model number at the factory and it gives it your software controlled bandwidth.

**Dave Jones:** But, what's going on under this lens cap here? Well, let's take a look at that, shall we? Basically, they're duplicating the exact configuration again. So, imagine that's now gone, right?

**Dave Jones:** That's now gone and we're and we're looking at exactly the same thing cuz the input comes in here and drives both bases there, but they have selectable control over here.

**Dave Jones:** Once again, the base of these transistors, these bias transistors down the bottom have the go into a HC4053, so they can switch select one or the other. And what's the difference between the two?

**Dave Jones:** Well, the only thing I could find is look, this has a 200 ohm series resistor. This has a 680 ohm. They both have 1K twos in there, so they are different.

**Dave Jones:** So, what's happening here is I believe that is the bandwidth selection for the 20 MHz bandwidth filtering. They're doing that in the differential amplifier itself. Oh, and by the way, I haven't drawn it in, but just as an aside, from the differential output here, they were actually tapping off two of those.

**Dave Jones:** One's going into a TL072. That's what the TL072's for. They've got some PNP BC856's here and I couldn't figure out the feedback configuration there, but anyway, they're just obviously some sort of drivers, nothing to do with the bandwidth configuration.

**Dave Jones:** Anyway, I haven't gone that far. This is what I really needed to know. This was the money shot. Woo. So, there you go. Little attempt here at reverse engineering the new Rigol DS1052Z and I found some interesting stuff in there, and that's what I was after.

**Dave Jones:** This wasn't a complete reverse engineering effort to do absolutely the whole board. I really just wanted to find out what was going on in that discrete amplifier uh front end there, and there might be errors in this.

**Dave Jones:** I haven't taken it, haven't simulated it, any of that sort of stuff. That'll be the next step to make sure uh haven't even sanity checked it, haven't double checked it, done whatever.

**Dave Jones:** So, if you do see any obvious errors in here, uh please let me know, and I can correct them. But, yeah, we found some interesting stuff how they're doing the bandwidth limiting in there.

**Dave Jones:** So, I hope you enjoyed that uh little look at just one technique for reverse engineering a uh board like this. There are everyone's got their own way of doing it, and depends on the board.

**Dave Jones:** Uh you know, you might do it uh differently, but this was actually a bit of a pain in the ass being a multi-layer board, quite a few traces going off uh where I couldn't uh see them.

**Dave Jones:** And obviously, if you had if you're lucky enough to have like an X-ray machine or something, that'd be really handy to um do stuff like that. But, anyway, so this did if you think that this is like an hour or two's work, uh think again.

**Dave Jones:** A lot of hour I put a lot of hours into actually uh just getting this far. It was lots of you know, red herrings and uh little you know, dead end traps and stuff like that, and just really kind of annoying and tedious work to do.

**Dave Jones:** But, hey, if you want to reverse engineer something like this, this is what you have to do. And if you really wanted to be 100% sure, you'd have to go through and check it or get someone else to check it, and then you got to simulate it to make sure it all works, and you got the correct uh you know, configuration, you haven't left anything out.

**Dave Jones:** And I guarantee there's an error or two in there, but eh, I found out what I wanted to find out, and that's the main thing. So, as always, um I'll link in all the data sheets and everything for this these uh chips.

**Dave Jones:** I'll scan in these little uh data drawings and you can have a look at those. And uh please, if you see any errors, let me know. If you've got any comments, please leave them down below or on the EEVblog forum.

**Dave Jones:** And don't forget, if you like the video, please give it a big thumbs up cuz that helps a lot. It really does with all the YouTube-y search stuff and things like that.

**Dave Jones:** It keeps me up the top. So, thanks. Catch you next time.
