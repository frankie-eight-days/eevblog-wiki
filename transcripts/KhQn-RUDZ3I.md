---
video_id: KhQn-RUDZ3I
title: EEVblog 1699 - µTimer PROJECT Part 1 - The LCD
url: https://www.youtube.com/watch?v=KhQn-RUDZ3I
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 22, "3": 36, "4": 45, "5": 61, "6": 76, "7": 85, "8": 104, "9": 117, "10": 126, "11": 137, "12": 147, "13": 162, "14": 174, "15": 183, "16": 194, "17": 203, "18": 218, "19": 231, "20": 240, "21": 254, "22": 262, "23": 275, "24": 292, "25": 313, "26": 325, "27": 341, "28": 351, "29": 364, "30": 376, "31": 386, "32": 398, "33": 414, "34": 431, "35": 445, "36": 453, "37": 464, "38": 477, "39": 490, "40": 499, "41": 517, "42": 527, "43": 538, "44": 545, "45": 561, "46": 576, "47": 586, "48": 601, "49": 616, "50": 628, "51": 637, "52": 650, "53": 664, "54": 677, "55": 687, "56": 696, "57": 713, "58": 723, "59": 744, "60": 754, "61": 764, "62": 776, "63": 792, "64": 801, "65": 814, "66": 828, "67": 847, "68": 857, "69": 878, "70": 893, "71": 908, "72": 931, "73": 946, "74": 961, "75": 977, "76": 987, "77": 999, "78": 1015, "79": 1025, "80": 1036, "81": 1055, "82": 1065, "83": 1076, "84": 1088, "85": 1097, "86": 1105, "87": 1124, "88": 1136, "89": 1145, "90": 1169, "91": 1183, "92": 1197, "93": 1210, "94": 1221, "95": 1243, "96": 1256, "97": 1266, "98": 1275, "99": 1287, "100": 1296, "101": 1310, "102": 1327, "103": 1353, "104": 1372, "105": 1387, "106": 1396, "107": 1409, "108": 1420, "109": 1428, "110": 1442, "111": 1450, "112": 1466, "113": 1475, "114": 1490, "115": 1499, "116": 1515, "117": 1522, "118": 1532, "119": 1547, "120": 1561, "121": 1570, "122": 1583, "123": 1603, "124": 1615, "125": 1626, "126": 1639, "127": 1650, "128": 1664, "129": 1684, "130": 1697, "131": 1710, "132": 1731, "133": 1739, "134": 1753, "135": 1768, "136": 1774, "137": 1783, "138": 1797, "139": 1810, "140": 1824, "141": 1834, "142": 1847, "143": 1864, "144": 1877, "145": 1887, "146": 1904, "147": 1920, "148": 1934, "149": 1941, "150": 1954, "151": 1961, "152": 1973, "153": 1984, "154": 1996, "155": 2006, "156": 2020, "157": 2033, "158": 2050, "159": 2061, "160": 2077, "161": 2091, "162": 2099, "163": 2112, "164": 2124, "165": 2136, "166": 2148, "167": 2168, "168": 2180, "169": 2199, "170": 2217, "171": 2228, "172": 2247, "173": 2261, "174": 2275, "175": 2285, "176": 2306, "177": 2320, "178": 2337, "179": 2346, "180": 2359, "181": 2376, "182": 2394, "183": 2411, "184": 2425, "185": 2445, "186": 2453, "187": 2464, "188": 2473, "189": 2483, "190": 2496, "191": 2509, "192": 2524, "193": 2535, "194": 2550, "195": 2564, "196": 2577, "197": 2592, "198": 2603, "199": 2615, "200": 2623, "201": 2638, "202": 2648, "203": 2663, "204": 2676, "205": 2694, "206": 2704, "207": 2713, "208": 2723, "209": 2734, "210": 2747, "211": 2760, "212": 2772, "213": 2787, "214": 2797, "215": 2806, "216": 2820, "217": 2833, "218": 2845, "219": 2859, "220": 2868, "221": 2878, "222": 2888, "223": 2906, "224": 2916, "225": 2930, "226": 2937, "227": 2951, "228": 2962}
---

**Dave Jones:** Hi, it's project series time. This is part one in hopefully a project series where I develop a new product. I'm going to call this that bloody beep again. I still can't find it.

**Dave Jones:** I'm going to call it annoys everyone. Anyway, this is a project I'm going to call the micro timer as in, you know, mu, the micro symbol, the micro timer.

**Dave Jones:** And I'm going to develop a lab bench timer similar to this Brymen one here, but this is, you know, there's quite a few on the market that have like a similar sort of desktop form factor.

**Dave Jones:** And I've always wanted one of these. This one's okay. You've seen me use it. It's got some external inputs here, but they're not very versatile. But anyway, it's just a basic timer.

**Dave Jones:** It's just got, you know, start, stop, and you can just override with external inputs here. Useful for like timing projects and and things like timing processes and things like that where you might want to like automatically you know, I start and stop trigger it.

**Dave Jones:** And so you don't have to be there to actually watch it. So but this is, you know, very limited functionality. But these sort of benchtop form factor is very common in sort of the educational space, the science lab space, that kind of thing.

**Dave Jones:** So yeah, I was going to develop something similar. So the design is basically all centered around the choice of the LCD, really, because, you know, the form factor can come later.

**Dave Jones:** It really needs a good LCD now. So I originally thought that I'd get like a custom made seven segment display and I'll link in a video here if you haven't seen it where I develop a custom LCD and I show you, you know, how relatively easy that is and relatively inexpensive as well, depending on where you go.

**Dave Jones:** So a custom LCD. And I thought, you know, I want bigger digits so that you can like see it from like across the lab. So custom seven segment displays like this have like, you know, you can get like really good contrast on them.

**Dave Jones:** That's the best in terms of contrast, but it just limits the functionality. And I thought, well, I don't want this to be a jack of all trades, masters of none.

**Dave Jones:** I thought that not only would I have a bigger display, but I'd make it full dot matrix as well, just for some versatility. So, you can change the size of the font if you want.

**Dave Jones:** You can have like multiple timers going and things like that. So, you can't really get that flexibility with a like a custom seven segment LCD. You're you're just fixed.

**Dave Jones:** So, yeah, I thought I'd get a low power because it's got to be battery powered from like a couple of double A batteries. Haven't decided on the power source yet, but so we need like, you know, sub 1 milliamp kind of consumption.

**Dave Jones:** So, I was looking around at LCDs and I figured that a 4-in diagonal one like this should This is actually I think 4.1 in visible area or something like that.

**Dave Jones:** But, yeah, basically at least a 4-in display would give like nice big digits that you could see across the lab. And of course, it's got to have good contrast as well.

**Dave Jones:** It's got to be low power, so it's battery powered so that you could have like a clock on this thing during the day when for example, when you're not using it as a lab timer.

**Dave Jones:** So, I was looking around at 4-in LCDs and I found this East Rising one. They're at They've even put their website on there. buydisplay.com. And so, I got this sample.

**Dave Jones:** This is an ERC 19264-1. And this is about $9 one off and the price drops in volume, of course. Now, it does include a backlight on here, but this is what's called a transflective display.

**Dave Jones:** And I think I've done a tutorial video on LCDs and the different types. So, transflective means is that it combines the best of a reflective This is a 100% reflective LCD.

**Dave Jones:** Like there's no back you don't need a backlight. It it doesn't have the ability to have a backlight. It's 100% reflective back in on it. So that's called a reflective LCD.

**Dave Jones:** And this one is also reflective, but it's transflective in that it will also allow a backlight through. And this one does come with the like a nice white backlight on it where it allows the light to come through.

**Dave Jones:** But I don't really need the backlight, but I guess I could put a backlight button on it. So you you know, if you want a temporary put the turn the backlight on you can.

**Dave Jones:** But otherwise it's going to chew too much battery power. So ideally I wanted a fully reflective LCD display, but I couldn't readily find one in 4 in. So anyway, I got this one and I thought we'd try it out.

**Dave Jones:** It's 196 by 64 in like as I said like four over four inches visible diameter. And it's got chip on glass COG. You can see down there cuz that's a glass back in in the chips are mounted on the glass in there.

**Dave Jones:** That's the driver chip for it. We've got a 36 way flat flex here with a 0.5. I hate the 0.5 mm pitch on it. And this one actually comes with an an optional font chip which stores all the fonts in there so that you don't have to install the fonts in your compile the fonts that you're going to use for all your text inside your microcontroller.

**Dave Jones:** And that just means that you can use a smaller simpler cheaper microcontroller and then you can simply read the fonts from here and then transfer them directly into the chip as you need them.

**Dave Jones:** So yeah, it just frees up memory space in the microcontroller that would otherwise be taken up with fonts. So anyway, that's handy. So if you do know of a 4 in fully reflective LCD instead of the transflective one like this.

**Dave Jones:** This is a FSTN one and I'll link in all the data sheets for all these things uh down below. So, anyway, uh for you film aficionados, we have the film on it.

**Dave Jones:** Oh, look at there. There we go. A thing of beauty, joy forever. So, basically, this uh video is just testing out what I think about the uh contrast of this LCD and yeah, how it looks.

**Dave Jones:** So, I wanted to get this up and running very quickly, so I ordered the uh demo board as well. This is actually quite uh cheap. It's an 8051 uh demo board specifically for this LCD.

**Dave Jones:** Well, they will match it to the LCD you buy. They've got like, you know, tons of different LCDs, and they will match it. So, um this is the uh driver board for it, and uh it's got like example programs built in.

**Dave Jones:** So, we should be able to get this thing uh talking straight away, and then it comes with an an interface board like this, and you can see that they've already pre-programmed on the 36-way uh flat flex connector, .5-in pitch.

**Dave Jones:** So, these are different pitches. We've got the uh .5 we're using here. We got .6, .62, uh .65, .7, .8, .9, so one, etc. So, we've got all the different uh different pin pitches here.

**Dave Jones:** So, this is a very handy board, and you'll notice that you can also tie any of the pins. I think this is like the positive side. They should label it uh a bit better, but uh anyway, like you can tie um each individual pin down to uh ground up here.

**Dave Jones:** So, they've installed like some caps up here, so you can put capacitors down to ground. They would be for the uh internal contrast um boost converters, for example, the bias uh uh capacitors, the bias pins on the LCD.

**Dave Jones:** So, you have to put those, you know, in various configurations. Yeah, they've got a capacitor across two pins there, or they've got others going down to ground like this, and they've strapped these pins here.

**Dave Jones:** So, I haven't gone through the exact pinout of this thing. Um they're only using uh some of the pins here. I think I specified an SPI interface, cuz this LCD is capable of SPI serial interface.

**Dave Jones:** I think it might do I squared C as well, as well as 4-bit and 8-bit parallel interfaces as well. So, it's very flexible, but I think it might be working serial, but haven't 100% confirmed that.

**Dave Jones:** Anyway, let's plug it in and see if we can get this thing working straight out of the box. All right, so we put that in there. We get that shut like that, and let's power this thing up.

**Dave Jones:** All right, I've plugged in the USB here. Haven't plugged in the backlight yet. Let's just see, cuz I really care about what it can do without the backlight. So, let's power on.

**Dave Jones:** Hey, there we go. EastRising buy-display.com, and boom, straight off the bat, it is giving us all our outputs. Look, and it's changing the fonts as well. So, it'd be I don't know if it's reading from that actual font chip on there or whether or not it's just got them programmed in.

**Dave Jones:** But, of course, when we're like having big digits, I might have to do like custom fonts. So, not sure if I'd use the font chip anyway, but might as well include it in the design, I guess.

**Dave Jones:** Look, that's quite a large font, but that's still not as big as we want. But, yeah, there you go. So, cool bananas. So, right out of the box, they've they've sent me this demo board, and there you go.

**Dave Jones:** And it does series, and they've got their panda. There you go. And it's got a stop button on it, too, so we can Yes, yes, we can freeze that.

**Dave Jones:** So, there you go. It works out of the box. It's not a bad viewing angle. So, when you order LCDs, either custom or off-the-shelf like this one, they will have what's called a bias angle or a view position or something like that.

**Dave Jones:** The terminology can interchange, but we'll just stick with bias angle. And what that means is that you can get them in two types, either 6:00 or 12:00. And it refers to either up or down on a clock, basically.

**Dave Jones:** And and one's a 6:00 one if you look at the data sheet. And what that means is that this is the bottom of the LCD. So, it's designed to be viewed from a lower angle like that.

**Dave Jones:** So, you know, if if your eyes are over here, you're looking up at the screen. So, that's called a 6:00 bias or viewing angle like that. And if you get a 12:00 one, it's actually over here like this.

**Dave Jones:** So, you're looking down on the LCD. So, if you've got a product like this, if you're viewing it from like a long way across the lab, and if you've got it sitting on a bench, you'd be viewing it in from looking up at the LCD.

**Dave Jones:** So, you want this 6:00 one that we've got here. But if you had something that was flat like this, and you're looking down on it like this, then you would want the 12:00 bias angle like that.

**Dave Jones:** And on top of the bias angle, which say it's a 6:00 like this from the bottom, you will then have the viewing angle. Please excuse the crude little model.

**Dave Jones:** Didn't have time to build a scale or to paint it. You will have the viewing angle, which is then plus minus a certain number of degrees. Say Say you've got a 60° viewing angle, then it would be plus minus 30° from that bias angle.

**Dave Jones:** So, if it's 12:00, then you'll have a viewing angle like that from the positive side. But this is a 6:00 one, and it'll have a viewing angle. But anyway, but you can see this actually has quite a large viewing angle.

**Dave Jones:** It's hard to capture this on a camera, but anyway, yeah, you probably want a 6:00 viewing angle for a product that's shaped like this. You certainly wouldn't want a 12:00 looking down like that.

**Dave Jones:** That would be That would be wrong, especially when you got the tilted angle already. It's hard to show LCDs on uh through the camera, but that's basically that is direct.

**Dave Jones:** And if I tilt it like that at the lower 6:00 angle, you see, yeah, that's that's probably a better optimal contrast, but there's not much in it. It's pretty darn good.

**Dave Jones:** So, I think this LCD is definitely a contender. I I really like it. Oh, what's happened there? What's happened at the top there? Can you see that? Look. There's some light There's some bleeding or something.

**Dave Jones:** What What's going on there? That That wasn't there at the start, right? I'll have to review my footage. I'm sure that wasn't there at the start. What the heck?

**Dave Jones:** They're They're individual pixels. It's No, there's nothing physical there. Anyway, this also has some contrast buttons. Yeah, I can adjust the contrast. There you go. So, can take the contrast right down, so there's nothing on the display, and bring it up.

**Dave Jones:** There There you go. So, it was set. That's pretty optimal That's That's really That is quite dark. I'm I'm really quite happy with that. As I said, it won't be as good as a custom seven-segment display.

**Dave Jones:** You can really, you know, a proper reflective one, but jeez, yeah, that's not too shabby at all. Check it out. I just went to record the Amp Hour podcast, came back, and I noticed that it's all gone.

**Dave Jones:** Not entirely gone, but it's actually now slowly starting to come back. Look at the Look at the pixels up there. And if I sort of Maybe is it a static thing?

**Dave Jones:** If I rub my feet Something's going on. It was completely gone before, but you can see how it's starting to Now it's starting to come back. Again, that could be some sort of static build-up on some unused pixels around the edge or something.

**Dave Jones:** Anyway, we'll leave that as a curious oddity for now. Might have to come back to that later. And I thought I'd measure the battery current, but I've just come a gutser.

**Dave Jones:** I tried to pull the pin out here, which is the uh power pin, but the actual clip didn't come out and I pulled the wire out. Oops. One of the annoying things is is that they've actually offset.

**Dave Jones:** They haven't put this right over the pin one over here. They've soldered it offset on the pin five and six over here and they've done the same thing over to here, but that's so pin five becomes pin one here.

**Dave Jones:** So, when looking at the data sheet, I've now got to add five onto it. Why? Yeah, that bleeding there at the top, that is just um some excess liquid crystals outside of the main dot matrix display area and yes, it is my uh static charges actually uh turning those on.

**Dave Jones:** So, it's interesting though. And you can see there outside of the area cuz if I turn the contrast right up, yeah, you see those at the top there. So, just some extra liquidy crystals.

**Dave Jones:** Bonus. Well, doll, I've got the correct uh power pin now, which is uh pin 19 down here and which is offset by four um because I got the data sheets goofed up because I have another uh display here, which is uh completely different, which I'll show you later.

**Dave Jones:** Anyway, um you can see yes, that it is actually working with no power pin because I've done a video on that uh and I'll link that in. So, but let me now plug in the power pin, which will override it being driven elsewhere.

**Dave Jones:** There we go. It's making contact. 280. Well, and you can see it just reset. It dropped down to what, 180? As you can see, it's putting more as it's putting more data on the screen, it's going to yeah, increase and it'll increase as it puts more on there.

**Dave Jones:** But that's the data sheet value 800 microamps, but uh yeah, it looks 650. Okay. So, yes, if all dots are on, then yeah, it could take 800. Um and really, I'm after a low power display, so drawing like say 250 microamps displaying say a clock or a timer as it's ticking over or something like that.

**Dave Jones:** That's actually reasonably significant. So, it would have been nice if the LCD had less than that. So, interestingly, in the data sheet, have a look here. Um it has a high-power and low-power pin.

**Dave Jones:** So, I wonder what's doing there. So, I wanted to try out this other LCD that I got, which supposedly has according to the data sheet lower power consumption and it's the same part number, but it's a dash six instead of the dash one.

**Dave Jones:** And yeah, oopsie. Turns out has an entirely different chipset in it. That means that the firmware that's programmed into the demo board is not going to be able to almost certainly not going to be able to talk to this.

**Dave Jones:** And I looked at the website. Website's absolutely fantastic. You can download the schematics for the demo board. You can download the programming software for it and all sorts of things.

**Dave Jones:** They've got all these documents that tell you how to like like install the programming software and do all sorts of things, which is great if you want to like they tell you how to like download your own fonts and stuff like that and like images and things like that.

**Dave Jones:** But what they don't tell you is how to actually drive another different LCD. So, essentially it looks like you've got to like buy another demo board, which they've pre-programmed and pre-setup and wired for this particular board.

**Dave Jones:** And I didn't know that when I got it. I thought, "Oh yeah, I'll be able to you know, fairly easily maybe change some jumpers or something." But it doesn't look like that's the case.

**Dave Jones:** Anyway, so what I thought I did actually get the connector for it cuz this is a different it's not as many pins, doesn't have the font chip built in, but that uh doesn't matter.

**Dave Jones:** So, what I thought I'd do is actually hook up this LCD to this uh board so that then I can get, you know, nice pin headers like this and then I can like get an Arduino or something to actually program this and maybe I can uh vibe code AI code um just to get it running very quickly and see if I can just get something on this um screen to

**Dave Jones:** be able to, you know, like actually demonstrate and like see how good the contrast is cuz this is lower cost, lower power um but same resolution and same size.

**Dave Jones:** So, yeah, um it's it's definitely worth trying out. Now, I could just order the demo board, of course, and it'd get here, but it's another week or something. So, I thought I'd at least try this now and the demo board's cheap.

**Dave Jones:** It's only like 22 bucks, but you got to pay postage on top of that. Um so, you know, it's it's not really worth an hour of my time just around here, but I do kind of want to sort of like get this running now.

**Dave Jones:** So, I thought I'd at least spend a little bit of time actually just trying to, you know, hook this up, get it, you know, figuring just get figure out which pins I need to strap and everything else.

**Dave Jones:** Um you know, what caps I need to put in, etc. And then just try and like uh program it with an Arduino and just get some AI code to just pump out anything.

**Dave Jones:** I don't care what it is. Just want something on the screen. Now, this is 0.5 pin pitch and sometimes you'll win cuz look at this. Look at this. I I can't fit it this way, like this, but I can fit it in this direction, like this, and it perfectly fits with one pin.

**Dave Jones:** This This last pin, which looks like it's soldered in, is not. There's It's got some solder on it, but there's no actual pin there. So, I can put it in this direction and beautiful.

**Dave Jones:** Yeah, so pin one will be over here. So, I've got to like flip the numbers and everything, but everything's routed out. So, yes. Yes, that's a win. So, I'm going to um solder that on.

**Dave Jones:** So, let's solder this on. I'll just put down some flux. There we go. Bobby dazzler and we'll place this on here and because these are really hard to like hold keep holding down while you actually drag solder, I'm just going to hold it in place with some Kapton tape.

**Dave Jones:** It's not going to sit flat, so probably have to put some little bit of downward pressure on it like that, but apart from that we should be right. So, we just use my well tip.

**Dave Jones:** Oh, accidentally whoa. There we go. Come we got some bit there. Can fix that up later with some wick. That's pretty poor effort. Yeah, couldn't get that one in there.

**Dave Jones:** Might need a small Yeah, I need a smaller tip to get in there. Unfortunately, I made accidental contact when I first did that. So, anyway, let's wick some Let's wick some solder away from there.

**Dave Jones:** Unfortunately, my small tip desperately needs to be tinned, but I can't find my um I can't find my tinning stuff. It was here the other My tin of tinning stuff was here the other day, I swear.

**Dave Jones:** There we go. That's the ticket. Yeah, get rid of that ball. All right, there we have it. It's not pretty, but that is soldered. So, oh, it just dawned on me that these four pins over here are the four most outer ones aren't actually routed out to any of these down here.

**Dave Jones:** Um that's why this one over here they started this four pin This is why they started it five with on the fifth pin. Cuz the fifth pin is the first one that's actually routed out.

**Dave Jones:** That's why it's C5 down here cuz it's pin five. So, pins one to four aren't actually routed out there. I don't know why. I'll I'll up the schematic for this board here.

**Dave Jones:** I'll I'll overlay it and you can see that they don't route out those pins, which is I don't know why. There's you know, there's enough room on the board.

**Dave Jones:** Just make the board slightly bigger if you need more routing room or something cuz there is nothing on the other side. This is a single-sided board. But anyway, luckily they do actually route out down to here.

**Dave Jones:** So, I can actually connect physically down to here. So, that's that that's good. But yeah, if I just want to strap things easily, it's just it's just not as nice on those four pins.

**Dave Jones:** But those four I believe pin four is the power pin and some of the others are yeah, like a drive voltage or something. And my winning continues. I don't have the right-angled ones like this.

**Dave Jones:** And okay, so what I'll do is I'll just put it in there on a flat plate and then I will stick this down so that just it it holds them aligned and that will give me enough room under there to solder each individual pin.

**Dave Jones:** I'll spare you the boring details. So, what I'm going to do now is reprogram this thing and they do actually provide the software and the example file. So, I've got to compile going to install the programming software for this chip, which is the which is the STC 12 LE5A60S2 and they provide so I got the programming software for that.

**Dave Jones:** Um And the compiler as well. They provide the source code for it. So, they give you step-by-step instructions on how to do this and then download it hopefully via the USB connector here and reprogram this flash 8051-ish microcontroller.

**Dave Jones:** But then I've got to figure out how all this programming configuration matrix. Obviously, they've programmed these in for the specific uh header that we had for the display that we've just played with, but it's going to be different for this new LCD, which is a totally different pinout and everything.

**Dave Jones:** Now, um because this is already, well, I don't know. I'd have to check the source code for the old one, and then figure out which pins are the serial outputs, etc.

**Dave Jones:** But, basically, anyway, we've got the um schematic for for this new LCD. This is if I'm using the four-line SPI uh reference, this is the display uses the ST uh 7525 uh chip set.

**Dave Jones:** And uh it just, yeah, this is how you hook it up uh to the MCU here. So, all I've got to do is add a one mic cap there, a one mic cap between uh these two pins here for the bias voltage.

**Dave Jones:** This chip is actually easier uh to drive than the uh previous one. Like, you need all the you need a lot more external caps than this one. So, this one's actually uh more better.

**Dave Jones:** It's got the building It's got building capacitors, which uh generate the various uh bias voltages and things. But, still need a couple of external caps there, just uh to bypass in there, tie a couple of pins uh here, which select the mode.

**Dave Jones:** I won't go through all the complete data sheet, but this selects the SPI uh mode, and then chip select, and then um data instruction select uh pin on A0 there.

**Dave Jones:** And so, we only have to, in theory, hook up, you know, two, four, five pins um to here, plus the 3-V power uh and ground. And then, if you hook them up to the right pins on this, via this selection matrix.

**Dave Jones:** So, I've just got a wire bundle here, so I'll be using these uh pins over here. I'll uh put, you know, some of those uh caps, I'll just tie um on here, or whatever.

**Dave Jones:** And I've got all those pins coming out to this one side. So, I think at the moment it's connected to uh the power pin, but, you know, you can re-strap that, and, you know, and I'm feeding in power to different pins now.

**Dave Jones:** So, but hopefully, if I decode all this, get it correct, and I install the software to program this thing, I should, in theory, be able to use this demo board to reprogram this.

**Dave Jones:** It's just when you order it from the factory to match your LCD, they've already programmed it with the correct software. They've already done the correct pins. They've already even done the wiring harness for you, and they put it over, and then they've configured this board correctly with all the pins.

**Dave Jones:** So, they've done all the hard work for you. So, it's a Trust me, it's worth paying that $22 US to actually, if you're going to get one of these displays from them.

**Dave Jones:** And for 22 bucks, you get it all like preconfigured and working out of the box. Yeah, unfortunately, I don't have that for this new one. Anyway, be an interesting exercise, I guess.

**Dave Jones:** And just as an aside, here is the ST 7525 interface here. And you can see, this is the chip on glass, the COG chip that's actually on the glass, and how it drives all the commons here, and then all the segments going down here like this.

**Dave Jones:** It's just a assembly note gold bump is face up. And here's all the pins. So, it's actually got a lot of input pins, and they're all tied together. And you can see, this is the This is the glass, and this is the FPC.

**Dave Jones:** This is the flat flex interface, the pins for the flat flex. And then the system, it shows how you just put the, you know, the one cap we saw across the V0 and XV0 pins there.

**Dave Jones:** And yeah, there's not much else to it, but they do supply quite a lot of documentation like this. You can't fault them. It's very thorough. Actually, first cab off the rank, I'll show you here.

**Dave Jones:** It shows Look, serial data input to the LCD or output from the micro controller, that is pin P11 there. And if you enter the matrix here, you'll see that P11 here, that's this row going right across there has no solder jumpers on it whatsoever.

**Dave Jones:** So, the good thing is is that I can adjust attach one of those. So, I can go, "Okay, which pin's not being used?" Actually, they're all being used. 1 2 3 4, so like six.

**Dave Jones:** So, all these numbers here correspond with the numbers on here and they all go vertically. So, it's just an XY matrix um that needs to Anyway, I'll do that as a reference just in case I have to go back.

**Dave Jones:** Hm, reference shot just in case I have to go back and drive the old uh LCD, but yeah, it looks like I'm going to have to reconfigure this. Although, but hey, look, pin 16 isn't used, 17 isn't used, 18 isn't used, 19 and 20 are used.

**Dave Jones:** So, I've got three spare pins there and if I put some extra pins in here, unfortunately, it doesn't go all the way to 28, it only goes 21 22 23 24.

**Dave Jones:** I'm not sure why they stopped the silk screen there. The traces seem to go to it. 24 seems to be going to two locations, actually. 24 seems to be bloody black solder mask.

**Dave Jones:** It's hard to see, but is that 20 Yeah, 24 Yeah, 24 does bugger off to there. Oh, yeah, are they also going to the vertical columns as well? So, hm, anyway, there are some so there are a few spare pins there I can use without touching the rest of this matrix and just leave that intact if I need it.

**Dave Jones:** This is actually working out quite well. I've um soldered in pins 16 and 17 up here like this. Um but then ones like uh P3 uh dot four are already being used here.

**Dave Jones:** So, that goes to pin nine. So, it it's already there and three three three three is already being used. That's pin eight. So, boom, I'm pin eight there. And three five is pin 10.

**Dave Jones:** Ah, Bobby Dazzler, look at that. I I only had to use uh soldering two extra uh pins which didn't upset um the original programming at all. But I do have to reprogram this chip, but in theory in theory, if it works, I can just I can just swap between the two programs for which LCD I want to drive.

**Dave Jones:** And you got to change the wiring harness as well, but you know, yeah, should work. Similar to you setting up, um we should be able to get this working fairly easily.

**Dave Jones:** And just so I don't screw this up, pin 60 over here is now pin one. There you go. So, that'll be 3 19. Right. So, I shouldn't goof that up.

**Dave Jones:** VSS VDD, I'll check that that goes over to here and I can do whatever between the two pins. That capacitor between the two pins, I can probably put a cap like between two of the pads here.

**Dave Jones:** Just little pro tip, it's worth going to the effort to just do this so that you don't goof it up cuz sooner or later you're going to come a gutser.

**Dave Jones:** If I left that at 60 and then I was just continually visually counting numbers, I would have just yeah totally come a gutser. Now, I've got a 1 microfarad 0603 here.

**Dave Jones:** And unfortunately, I have to use this pin pitch here, which doesn't quite fit. I've got to go between pins two and three. Would have been good if it was two and four there.

**Dave Jones:** The other ones don't go to pin 60, unfortunately. Of course they don't. So, I kind of have to be real careful there. Woah. No, it was touching pin three, wasn't it?

**Dave Jones:** This is tricky. There you go. There you go. Oh, I think I might Oh, is it shorted down there? I don't think so. I might I might get away with this.

**Dave Jones:** I could go for an 0402, but I just had no 603. I don't know where my 0402 is. I had this one to hand. I'll use my LCR meter and and see if I've actually got that.

**Dave Jones:** Right, well, I've got it hooked up and I've installed the software. It just installed, no problems whatsoever. The driver, I had it already installed. It was a a CH 340, you can see there, set up as COM 5.

**Dave Jones:** No worries. And then, this software, the amount of support tr- like if I expand these, they just go on and on and on and on. Like if I just go like this one down here, for example, just supports all these different versions.

**Dave Jones:** It's just insane. All these variants of this part. Anyway, um this is the one we've got, the STC 12LE5A60S2. I think I've got that right. So, I've got the C file here.

**Dave Jones:** I got the source code for it. And it looks like they actually include uh the fonts in here. So, they're not reading the font chip, but this one doesn't specifically have a uh font chip.

**Dave Jones:** So, there you go. That's an 8x16 font, etc. Right? So, that's all That's all built in, which is fine and dandy, but I need to generate like do I have to go find myself an 8051 compiler that supports this?

**Dave Jones:** Doesn't make sense. This is just the programmer software. Um but I can't find the hex file. So, without that, I'm up the creek without a paddle. Right. So, at this stage, I have no real desire to go and try and find an 8051 compiler that supports this chip.

**Dave Jones:** And then, like sure, you can compile it, but then are you have you got the right fuses and everything else, right? Um whatever that micro needs. Like it would have been great if they just supplied the hex file.

**Dave Jones:** And I could just burn it in, but it doesn't seem to be on their website. So, I'm going to have to contact them. Well, it turns out their service is very good.

**Dave Jones:** They replied to my email in like 15 minutes or something. Um unfortunately, um yeah, it looks like they don't supply the hex files. Thanks for the email. The demo board you purchased can't be matched with the ERC the dash six version.

**Dave Jones:** I've got the dash one version, which is what we uh used before. Even you even if you reprogram the codes, you need to buy a new demo board. I don't think that's correct.

**Dave Jones:** Um I was asking about the hex files, but they're basically saying, um no, we're not going to give you the hex files. Um that's basically what it means, which is ridiculous because they give you the actual source code.

**Dave Jones:** You can download the actual source code for each individual demo board that's matched with each individual LCD. The full C source code. So, why don't they just give everyone the hex file?

**Dave Jones:** I don't know. I guess they don't want the support request from, you know, idiots like me trying to like reprogram the demo board because it's complicated to do as you saw with that matrix and everything and figure it all out.

**Dave Jones:** And so, I I can kind of understand why they don't want to give you the hex file, but they so they give you the source code um just because well, an example of how to actually drive the LCD.

**Dave Jones:** But yeah, they don't want you around with that hardware board because it's too hard. So anyway, I was looking around for other examples for the ST 7525. Thought I might be able to find some Arduino code or something like that.

**Dave Jones:** Couldn't really uh find anything. There was some code on Adafruit that uh worked with a 7565 or something. It's like a smaller graphics thing. I'm not sure if that's it's probably compatible enough that it would have worked.

**Dave Jones:** But anyway, back to buydisplay.com. I found that they actually have this exact one, which is SPI for for Arduino. Here, you can buy the module and it's just it comes with a board that that just has a nice little, you know, um SPI bus on it to hook up to the Arduino.

**Dave Jones:** And if you go down here, they have all the stuff. They have the data sheets, the controller data sheet. They've got an Arduino library and example, but uh yeah, then you've got a lot level converters the Arduino's 5 volts, it expects uh 3.3.

**Dave Jones:** But down here, they've got a Raspberry Pi library and example. Ha, I've got a spare Raspberry Pi. Let's give Is a whirl. But as it turns out, the Arduino library and example um doesn't actually have as much info as the library pie thing does here.

**Dave Jones:** So, so what you actually get inside the Raspberry Pi one is you get an interfacing document, and that tells you how to interface the dash four one, minus the dash six, but you know, it's the same chipset and the same resolution.

**Dave Jones:** So, it should work and tells you how to hook it up to the Raspberry Pi here. Beautiful. And if we go in here, we've got all the source code for this.

**Dave Jones:** They've got file for it. They've got a read me text, which then development OS Raspberry Raspbian for Raspberry Pi BCM2833 is the library that it uses, and they've got the table of how to hook it up to the physical Raspberry Pi 3 here.

**Dave Jones:** Look Look at this. This is great. And there's a difference between the the BCM like the library the actual chipset used, the pinout on the chipset, and the pinout on the Raspberry Pi.

**Dave Jones:** So, they tell you it's pin physical pin 22, whereas in the the actual chip itself is pin 25. But, yeah, this is great. And then they give you instructions on how to run this LCD demo test.

**Dave Jones:** So, let's give it a whirl. Right. So, I've got an old Raspberry Pi 3 Model B V1.2, and I've downloaded the latest Raspbian OS or whatever it is onto it.

**Dave Jones:** And I've got to install this BCM2835 C library from Mike M. Whoever Mike M is, thank you very much, Mike M. So, I've done this. I've installed libcap, and then I've added the user, which is EE Vblog, to kmem, whatever that is.

**Dave Jones:** And then I've done these things here. This thing is slow as a wet week, by the way. Terrible. Anyway, I've downloaded the compressed library for this thing. So, now this should work, I think.

**Dave Jones:** Oh, no. Cannot open no such file or Oh, I've got to put in the number 1.75. Okay. Yep. Oops. 75. Let's try that. There you go. So, that's done that.

**Dave Jones:** And it's in the download directory. Whatever. Geez, this is not easy, is it? Is it like this for all just like toggling a few IO pins on a Raspberry Pi or is it just because do this the LCD companies just decided the programmers just decided to use this particular library or whatever.

**Dave Jones:** Is that the deal? I don't know. I don't do coding on a Raspberry Pi. Oops, it doesn't like that, does it? Nope. Get rid of that. Don't know why it added that at the end.

**Dave Jones:** There you go. Whoa. We're in. And it's configuring. Yeah. Okay. It's executing all that. Uh then I've got to make. So, let's make. Extracting directory. Yeah, it's doing stuff.

**Dave Jones:** This is good. See, how would you figure out to do all this without like instructions like this? It's just It's just crazy. This is just so that I can compile the code and then run and toggle a few IO pins.

**Dave Jones:** But hey, it's better than buying a new demo board, I guess. Pseudo make check. There we go. Oh, yep. Pass one. Yep, that sounds good. Pseudo make install. This is crazy.

**Dave Jones:** I Like I kind of like I I understand what it's doing, but there's no way I would have figured out this on my own. Absolutely no chance whatsoever. Yeah, okay.

**Dave Jones:** So, just mentions Raspberry Pi 2 to enable device tree support. Do I know? That's only for Raspberry Pi 2. Real-time performance constraints. No. Interactions with other systems. If in order for your library SPI to work, you may need to disable the SPI kernel module using this.

**Dave Jones:** Oh, well, I may have to do it. I I don't know if it's going to bit bang the pins or like this the software's going to bit bang the pins or whether or not it's going to use the uh hardware spy or what.

**Dave Jones:** I I'm not going to touch that now. I won't touch that unless it doesn't work. Unless I compile the code, run it, and then uh I can't see any data toggling on the pins.

**Dave Jones:** Then I'll know something's wrong. All right, I got the Raspberry Pi code here downloaded. I've got the uh text file which tells me how to physically uh connect it.

**Dave Jones:** Uh there it is there. And I've got to make it. So, I've got to make the file. So, I've opened the thing here and I've just got to do make cuz it should have the make configuration file.

**Dave Jones:** So, No, make LCD test is up to date. Done. Uh Okay. sudo {dot} {slash} LCD test. I'm doing this all on the USB stick. It shouldn't matter. No, command not found.

**Dave Jones:** No, it didn't make it, did it? So, there's the make file. So, it should call GCC. Don't know what wall is. Um and it should compile the code using the uh BCM2835 library which we installed previously.

**Dave Jones:** And uh it should generate the LCD test executable, but uh it's not. So, uh okay. Apparently, I can go make clean. Ah, if I make that again, okay, I've cleaned it.

**Dave Jones:** Ah, there we go. Right, I just had to clean it first. There you go, trap for young players. GCC wall, blah blah blah, it it did it. Okay. Um I expected some sort of output from it, but I guess it's done.

**Dave Jones:** So, now I can run it. Haven't actually connected up the LCD yet, but I can do that if once I get through this. sudo.lcdtest Uh no. Woo, I got it running.

**Dave Jones:** There you go. Um it didn't like the USB stick for some reason. I'm not sure why. Yeah, everyone's screaming in the comments, whatever. Um but yes, it is now running.

**Dave Jones:** So, therefore there we go. It's doing LCD begin, LCD bitmap, clear, bitmap, clear, display, time. I don't know. Don't know what the program does, but yeah, there you go.

**Dave Jones:** It's doing it's something, so I'll hook up the screen now and hopefully should work. Should be getting Those pins should be toggling if I hook them up the right way.

**Dave Jones:** And cross your fingers, tongue at the right angle, should get something on the screen. Winner winner chicken dinner. You can probably barely see that, but there is a clock.

**Dave Jones:** There is a clock that is working. So, we have a contrast issue, but uh we can fix that. So, THERE YOU GO. ALL THAT rigmarole I had to go through just to run this thing.

**Dave Jones:** Um I don't know if that's normal. I don't know. I've never written a program for a Raspberry Pi before, but we installed Mike's library or whatever it was, and then we did some uh sudo magic, and we built it with GCC, and it actually worked.

**Dave Jones:** So, yeah, that's amazing. And I didn't goof up the wiring um and over here either. So, yeah, my soldering worked, and everything worked first go. I did not expect that to work first go.

**Dave Jones:** I thought Murphy would absolutely bite me on the ass there, but no, Murphy's sleeping, and it's 7:00 p.m. Damn it, I'm going over dinner. All right, so let's measure the current consumption.

**Dave Jones:** Oh, there you go. I had disconnected the power pin and the contrast has changed because it's being powered by effectively a different voltage, a lower voltage cuz it's going through the um pins.

**Dave Jones:** It's going through the IO. Wow, there we go. It's jumping all over the place. Anyway, let's power that and oh, 5 600 microamps. Wow, so much for that. It said 180 microamps.

**Dave Jones:** I know like the there's a lot of the the contrast isn't set properly. Um that's a software uh setting so a lot of the pixels are like partially on.

**Dave Jones:** But damn, it's supposed to be like 180 microamps. So now I've got to figure out where they're setting the contrast in here and well, it's got set LCD mapping control, set output voltage.

**Dave Jones:** Is that it? Char 16 by 16, 32 by 16. Is that the uh the big clock display? Yeah, yes, yes, it would be uh cuz that's half the height of the 64 uh LCD.

**Dave Jones:** So that's the uh that's the font that they're using. So um just to get me started in this timer project, I can just use that um 32 by 16 uh font.

**Dave Jones:** No worries. So if we go to the chipset data sheet, uh very comprehensive of course. All LCD data sheets or uh have the not necessarily this is not the data sheet for the LCD module itself.

**Dave Jones:** You got to go into the chipset uh data sheet usually to get this sort of stuff. And here's the instruction table here and the instruction set contrast. Boom, it's a two-byte instruction set VOP voltage.

**Dave Jones:** There you go. So you put 1000 which is an eight um so in in hex um because you'll be we're hex values uh usually. We'll see that in the code in a second.

**Dave Jones:** So, that's an eight. So, eight one uh and then it sends that um eight-bit um value through to set the V um op voltage. So, if we go into the source code here, we can see that there it is.

**Dave Jones:** 0x81 set output voltage. Should have said contrast there, but you know. And then that's the value 154. So, that's what that demo board would have been doing even with the other different chipset, it would have been setting a register value in there.

**Dave Jones:** Um and it the buttons just would have incremented or decremented uh that register value for the uh contrast. You know, old-school LCDs they would have a trim pot in there and you can adjust the uh DC voltage, but modern ones like this, it's all software programmable and Bob's your uncle.

**Dave Jones:** So, yeah, all I got to do is change that um figure. Yeah, I don't have any ready buttons hooked up to it. Um I don't So, I'll just like experiment that uh recompile, it takes seconds and then run it again.

**Dave Jones:** It's It's no problem uh whatsoever. So, I'll just, you know, fiddle with that value and uh see if I can get optimal contrast. And there we go. I set it to 100.

**Dave Jones:** I didn't know what the, you know, value was good, so I just changed it from 150 to 100 and that's not bad. That's not bad at all. That's, you know, reasonably close.

**Dave Jones:** So, that's pretty good. Is that Oh, it's hard to tell. I can't really run the two side by side, unfortunately, um cuz the cabling just doesn't allow me to do that.

**Dave Jones:** This is a straight on. I'll see if I can get a screenshot from the uh previous one and try and do a comparison there. It's hard without the same information on the screen, but that's not too bad.

**Dave Jones:** Uh remember, this is a lower-cost LCD. It's about, I think, about 40% less cost or something. But uh yeah, I'm not getting the power consumption. Um that is a problem, but anyway, that still looks pretty good.

**Dave Jones:** It's, you know, it's um angles are pretty great. So, I've got no problems with that. Um yeah, I think either one of those is a contender. I'll measure the consumption now.

**Dave Jones:** Uh yeah, 440. That's actually that's more, isn't it? I was getting like What was it I was getting like a 100 So, you know, 200 and something. So, I think this one's actually more higher consumption.

**Dave Jones:** Well, I'm very surprised the main website. Maybe it's an error on the main website. That claims that that's It claims it's like 180. Uh Wow. Okay. Didn't expect that.

**Dave Jones:** Well, I think I'll call it quits there for this video. I got both of these LCD working, which I wanted to do for this uh part one. So, I hope you enjoyed that.

**Dave Jones:** Much longer than uh expected, but I wanted to share with you the whole journey, and that's the point of these uh project design videos. You know, I could just design it in the background, and then suddenly go, "Oh, here's the finished product." and then do a 15-minute montage of uh design and building.

**Dave Jones:** But, if you like um this sort of content, then please give it a big thumbs up and and discuss down below and engage and all that sort of stuff, and I can continue this uh micro timer project, and we'll see what happens.

**Dave Jones:** But, anyway, I want your uh thoughts and comments on uh the LCD selection like this. Um if you've got a better LCD in mind that's cheaper, better contrast, totally reflective.

**Dave Jones:** Oh, I forgot I did actually put the backlight of the other one on. Um and yeah, it's exactly as you expect, but it's like 80 milliamps backlight. So, I would prefer a 100% reflective um LCD, which should give better uh contrast.

**Dave Jones:** But, anyway, um yeah, we've got these uh transflective uh displays. I could hook up this This one's got backlight, too. So, I could just hook that up there and see what it's like.

**Dave Jones:** Oh, yeah. All right. Give me a second. And boom, there it is. That is a 50-mA backlight there. So, yeah, 50 milliamps is going to chew a lot from the batteries.

**Dave Jones:** I can take it down to that's 10 milliamps. Even 10 milliamps is useful, I guess. That's the resolution of the power supply I'm using at the moment. I can only go to 10, that's 20, 30, 40, 50, and right up to 100.

**Dave Jones:** And camera exposure is just going to play silly buggers. So, yeah, you know, you might as well if you if you are using this LCD, then you might as well like include backlight capability, but you wouldn't use it for normal operation, though.

**Dave Jones:** But yeah, it does certainly does not need the backlight. Turn off the exposure there, and yeah, yeah, like you'd make the characters thicker, bolder, you know, to make them look sort of like higher contrast.

**Dave Jones:** They're like two pixels wide, I think are they? Anyway, I think either of those LCDs would work, but once again, if you've got a better LCD, please leave it in the leave the model number cuz you can't include links on your YouTube these days.

**Dave Jones:** I think it automatically hides them, but please leave the model number down below. It's got to be like 4 in. Yeah. Pure reflective would be nice, and I like 192 by 64.

**Dave Jones:** I think that gives a lot of ability to, you know, work with having like, you know, a large timer like this. You know, it'd have at least tens of seconds, possibly hundreds of seconds, and then you can have like multiple timers up there.

**Dave Jones:** Then you can have text list modes, and you can do, you know, quite versatile things once you've got that dot matrix screen, of course. Anyway, we'll call that quits for part one.

**Dave Jones:** Let me know what you think. Hope you enjoyed it. Catch you next time.
