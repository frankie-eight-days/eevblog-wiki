---
video_id: KI7YLXhovb8
title: EEVblog #934 - Raspberry Pi Supercomputer Cluster PART 1
url: https://www.youtube.com/watch?v=KI7YLXhovb8
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 34, "3": 48, "4": 66, "5": 80, "6": 96, "7": 108, "8": 122, "9": 135, "10": 151, "11": 165, "12": 179, "13": 193, "14": 206, "15": 223, "16": 240, "17": 251, "18": 266, "19": 281, "20": 292, "21": 305, "22": 316, "23": 329, "24": 343, "25": 358, "26": 372, "27": 384, "28": 399, "29": 411, "30": 424, "31": 437, "32": 451, "33": 464, "34": 477, "35": 491, "36": 502, "37": 517, "38": 531, "39": 545, "40": 561, "41": 574, "42": 587, "43": 603, "44": 617, "45": 635, "46": 647, "47": 667, "48": 683, "49": 697, "50": 709, "51": 723, "52": 738, "53": 750, "54": 763, "55": 777, "56": 790, "57": 804, "58": 818, "59": 837, "60": 848, "61": 862, "62": 874, "63": 891, "64": 905, "65": 920, "66": 939, "67": 954, "68": 966, "69": 979, "70": 991, "71": 1001, "72": 1015, "73": 1033, "74": 1046, "75": 1064, "76": 1076, "77": 1089, "78": 1105, "79": 1116, "80": 1131, "81": 1145, "82": 1162, "83": 1178, "84": 1194, "85": 1205, "86": 1218, "87": 1232, "88": 1246, "89": 1263, "90": 1277, "91": 1290, "92": 1303, "93": 1315, "94": 1328, "95": 1341, "96": 1352, "97": 1367, "98": 1383, "99": 1391, "100": 1403, "101": 1419, "102": 1435, "103": 1447, "104": 1461, "105": 1475, "106": 1489, "107": 1502, "108": 1515, "109": 1528, "110": 1541, "111": 1556, "112": 1568, "113": 1581, "114": 1596}
---

**Dave Jones:** Hi, in a previous video, you've seen these Orange Pi ones that I got. I got like 10 of these things before use as potentially a Raspberry Pi in this case, Orange Pi little arm supercomputer. And these are actually quite popular projects where

**Dave Jones:** people get Raspberry Pis and cluster them all together and you know, it's so to speak make a super little arm supercomputer with them. I mean, it's not nearly as powerful as you know, the latest modern Intel CPUs and things like

**Dave Jones:** that, but it's fun. And this one is in particular, this is the Orange Pi 1 model and it's got a four-core processor in it and it's not a bad little beast. It's generally speaking faster than the Raspberry Pi and it does

**Dave Jones:** a reasonable job and it's fun, but most importantly, it's cheap. This is only $10 for a four-core 1.2 gig or 1.3 gig is it arm arm cortex processor in it. So, it's a little bit of a beast especially for the money, 10

**Dave Jones:** bucks. And so I thought it'd be fun to make a little Whopper computer. Yes, I might even stick it inside like a something that looks like the Whopper. That'd be fantastic. So I thought I'd start out with just a video outlining my

**Dave Jones:** concept for this thing. I haven't built it yet, but hey, let's have a look at the ideas because it could be quite interesting. Now, quite a lot of people have built these Raspberry Pi cluster or supercomputers before and they generally

**Dave Jones:** all that involves is basically a case, you know, some people laser cut their own acrylic cases and stuff like that and they light them up and they look all fancy and everything else. And hey, I could do this in a day, no problems

**Dave Jones:** whatsoever. All I've got to do is basically get a whole bunch of these, stick them together maybe with some standoffs or you know, something like that. And then I get power for each one. There's a little DC jack for each one,

**Dave Jones:** so you just apply power, hook it up to a pretty beefy power supply like a PC power supply or something like that. And then you just hook up the ethernet, get yourself one of these ethernet switches here. You know, you don't need a fast

**Dave Jones:** one, just a 10 100 type one and Bob's your uncle. Basically, you've got yourself a cluster computer. So, it's just basically just arranging these physically. There's nothing special there at all, but I thought, "Hey, you know, that's not very elegant. You got

**Dave Jones:** the ethernet cables hanging out and you got routing problems and dicky little DC jacks and things like that. Wouldn't it be nice if actually designed like a custom motherboard like this and these can just plug in. You can just have a

**Dave Jones:** whole bunch of them plug in, no cables, no nothing. That'd be fantastic. So, let's take a look at doing that. And yes, before you mention it, I know this is not going to be as powerful as a modern Intel CPU and GPU and things like

**Dave Jones:** that for like for my intended application running BOINC on it and doing SETI and other compute research, I know it's not as powerful as that in terms of dollar per watt potentially and in terms of performance per watt is

**Dave Jones:** basically one of the more critical things for this sort of thing, but hey, these things are fun. So, I'm just going to have some fun with this. I know it might not be the most efficient thing, you know, an Nvidia GPU card will

**Dave Jones:** likely kill this array in terms of performance per watt. But hey, I want to do it just because. That's it. Just because. Now, the first thing to note is that the Orange Pi 1 is not compatible with the Raspberry Pi 2

**Dave Jones:** in terms of its physical plug-in ability. Why? Because the header connector here is actually reversed. It's the same pinout and functionality, but it's reversed. They physically reversed it so that the shield things, the hats or whatever they are,

**Dave Jones:** go actually don't sit over the board like this like they do on the Raspberry Pi. They sit in here. This one actually reversed it so they sit outside here. And the reason for that is a smaller form factor board and the ethernet and

**Dave Jones:** USB connectors actually getting in the way here. So that's really annoying. So any solution we make where we can plug these into a any sort of motherboard or something like that, it's not going to be compatible with the Raspberry Pi. The

**Dave Jones:** connector is going to be physically back to front. Bummer. Now of course the first thing is is how do you plug this into a motherboard? Now you know, we could put it upside down maybe and have a 40-pin vertical header

**Dave Jones:** on the board and then you can stack them like that, but that takes up a lot of board space. That's a lot of physical space on your motherboard actually wasted. If you've got multiple boards side by side like like that,

**Dave Jones:** you know, a motherboard this big you might only be able to fit five in. But if you mount them vertically like this, you can potentially get much greater density for a given motherboard size. And that's what we want. Now

**Dave Jones:** unfortunately this thing comes with the header pre-soldered on like this. So you know, we're not going to go suck off the header and put a right angle one in on there. That would have been awesome if we had a right angle. We could have just

**Dave Jones:** went bang bang bang bang bang on a motherboard. That'd have been fantastic, but we're not going to go suck those out. So we have to come up with some other solution if we want to use this Orange Pi One or a Raspberry Pi for that

**Dave Jones:** matter. It's just because the pin out's different. They've both got these vertical headers on them. Now you can actually get right angle female header sockets for PCB. So instead of plugging in vertically, it'd like the connector would be like this. Here's a image of

**Dave Jones:** it. I'll get an image and then you just plug it in on the side like that. So, you might think, "Hey, there's our solution." But, uh-uh, trap for young players. You'll notice that this header sits significantly off the

**Dave Jones:** board like that. And this is actually, if you go look at the data sheet for the header, it's actually, going to be much smaller than this gap here. So, you'd even have to grind off some of the board and be

**Dave Jones:** careful not to get the traces, uh you know, hit any traces or short out any ground planes or anything like that or cut any ground planes. Um so, you don't want to do that. That's just a ridiculous solution. Or, we've got to

**Dave Jones:** come up with some other way to uh get these things physically lifted off the board. Now, of course, you could get the header connector, uh female header connector for the board, put something under it, and then, uh you know, right lift it off the board

**Dave Jones:** or something, some sort of spacer. Yeah, that's a solution. But, there's another way, too. Now, please excuse the crudity of this model. I didn't have time to build it to scale or to paint it. What you do is you have your

**Dave Jones:** uh right-angle female header connector, actually, you know, through-hole or could be Well, probably not surface mount cuz they're going to have the pins coming out the side, which is going to be troublesome. So, probably a through-hole uh version here. And

**Dave Jones:** they've got the holes basically on either side of the connector, and then you just route out paths like this on one side of the connector, and you get your board, and then you just put it into the slot like this so that it goes

**Dave Jones:** down into the board, and then you slide it in like that. Bob's your uncle. Beauty. But, of course, it's not as dense a solution as it could be because the width of this has to cater for the fact that you've got to put this in and

**Dave Jones:** then slide it across like that. So, you know, the slot actually doesn't have to come all the way up, and you could use a surface mount one, actually. The pins come out here and here. This side's not a problem, but coming out this side, the

**Dave Jones:** slot doesn't have to go right up to the connector like this. You can have the right uh the surface mount pins coming out like that, and then the slot only and because you've got a distance in there, so you can actually see there's a

**Dave Jones:** thickness of the uh plastic base of this header, so it doesn't actually come all the way in. So, you've got So, the pins on here can actually see any surface mount pins, and the slot can actually be further out from the connector than what

**Dave Jones:** I've shown there. So, you only have to put it in and then slide it in like that. So, you know, the slot basically has to be the width of these uh pins, so to speak, set out somewhat, and then the

**Dave Jones:** distance between boards is going to be set by these pain-in-the-ass Ethernet connectors and USB, which we're not going to use. So, it's not the densest solution, but it's better than flipping this board upside down, plugging it into a verti- into a vertical header like

**Dave Jones:** that, and then having two three like, you know, on a board that size, we're only going to get three in there. But this one, we can potentially get one, two, oh yeah, one, two, three, four, five. You know, I'm just

**Dave Jones:** eyeballing this, but, you know, basically double the density, easy. Now, a nicer solution to this is the Raspberry Pi Zero. Now, it's only five bucks. It's half the price of this, but in terms of dollars per watt, um it's

**Dave Jones:** not as good. This is a four-core 1.3 gig uh processor or greater than 1 gig, and the Raspberry Pi Zero is only 1 gig at um with a single core, but it comes with the um header connector not populated,

**Dave Jones:** so you can solder in your own right-angle header connector, and then you can use those vertical standard vertical connectors, and you wouldn't need to uh put in any slot like this. So, it'll just bang bang bang, and you

**Dave Jones:** can get and And they don't have the um big ethernet connector and USB connector on there, they're much thinner and you can get double the density again. So, the Raspberry Pi Zero, it's not too bad if you can get twice

**Dave Jones:** the density uh, for half the cost, but you'll lose, ultimately going to lose like half of your performance in the end. So, yeah, I don't know. Which one do you go for? Hmm, the Raspberry Pi Zero is nice

**Dave Jones:** a solution. It could be lower power because, hey, it's, you know, it's not running any of the ethernet uh, functionality and it's just generally a lower power, uh, board than this one, I believe. But, this motherboard idea, it's all going to come to naught unless

**Dave Jones:** we can actually get internet connectivity through these header pins. And the Orange Pi One ethernet over to here, these ethernet pins do not come these physical ethernet pins, uh, do not come down to this header. It doesn't have it. So,

**Dave Jones:** we're in trouble there, but, uh-huh, I think I've found a solution for this. As luck would have it, if you have a look at the, uh, pinout for the Raspberry Pi, it's the same on the Orange Pi One here,

**Dave Jones:** there is an SPI port that actually comes out on these pins. So, uh-huh, can we convert the SPI into an ethernet interface? Yes, we can. Now, as it turns out, the, uh, Raspberry Pi Linux, uh, build, I believe, has a built-in driver

**Dave Jones:** for the Microchip, um, ENC28J60 SPI to ethernet, uh, converter chip. So, all we need is to put one of those chips on our board for each one. We can have one for each one and these things are cheap. They're available from Digikey,

**Dave Jones:** they're only a couple of bucks. We can solder those onto our motherboard here and bingo, we can get connectivity to each one of our boards, be it an Orange Pi uh one or a Raspberry Pi zero or whatever other uh board that we want to

**Dave Jones:** plug into this system. Beauty. And although I haven't tried this, I believe that all you got to do is add in one uh line to the uh boot uh config file in your build and then bingo, it just

**Dave Jones:** automatically works. This um ENC28J60 chip just handles it. You plug it into Ethernet and away you go. Now, of course, it's not going to be the uh fastest solution via the SPI bus. You can change the speed in the uh

**Dave Jones:** configuration and stuff like that, but it's not going to be nearly as fast, but you know, this thing is basically a uh compute system, you know? It's not really a you know, high throughput uh high bandwidth type of system. So, hey,

**Dave Jones:** you know, a few megabits or something is fine. Or a couple hundred K bits is fine. As long as we've got an Ethernet connection, especially for the use I want to make it to, it's just got to uh

**Dave Jones:** download stuff from the Boinc server. It can do that slowly and this just got to report its results back and things like that. Not high bandwidth stuff. Most of the time, it's basically not talking at all. So, we just need an ENC28J60

**Dave Jones:** chip for each one of our modules like this. Just wire that in. No worries. But, hey, of course, we need an uh Ethernet uh switch up here to connect all these ones into. So, we don't want to use a physical Ethernet

**Dave Jones:** switch like that because well, that's just ugly cuz we've got the uh cables again. We'd have to have like a uh you know, an RJ45 on there going off for each one and I'll bugger that. That ruins our nice solutions. So, we take a

**Dave Jones:** look at a typical 10/100 uh Ethernet switchy, you can see that there's bugger all in these things. We've just got the main chipset here. This is a uh Realtek uh one and then we've got the magnetics. You can see the uh see the differential

**Dave Jones:** traces going off there um two pairs for each ethernet port. This is an eight-port chip. It's all in one. It's a power supply and the main chip and that's it. There's no e squared prom, there's no programming. Although these

**Dave Jones:** things are programmable, they just work by default, I believe. Anyway, I've never actually designed an ethernet switch into something before, but hey, and then the LEDs just hook up there for the monitoring and everything else. So, all we need, in theory, is one of these

**Dave Jones:** ethernet switch chips. And yes, you can just buy it from Digikey. You can't get this Realtek one. Yeah, and you can't buy this chip from Digikey. So, I'm not going to use this Realtek one, but hey, Microchip have one. Other Other

**Dave Jones:** companies have similar sort of chips. You just You've just got to choose one that is designed for stand-alone applications, so it doesn't need boot configuration and all that sort of stuff, and it's got to have the phi built in as well. But what do we do

**Dave Jones:** with these pesky magnetics here? Do we need the magnetics? I don't think so. I think we can get away cuz we're going directly This chip would be directly on our board over here, and then it'll be powering, say, eight or four or

**Dave Jones:** depending on how many you needed, how many you designed to have on your motherboard, then it's going directly chip to chip. As long These are current-driven differential outputs. So, all we need is to is some output resistors tied to ground, basically, or AC coupled

**Dave Jones:** to ground, and then we should get away. Should be able to get away without the magnet magnetics. They're only designed for driving lines. Now, once again, I've never actually tried this, but I I think, in theory, it should work. But I stand to be

**Dave Jones:** corrected. So, in theory, what you should need is just some termination resistors on the line here. Often, these are AC coupled down to ground, but you'd have to read the particular data sheet that you're actually got, and we should be able how connect the

**Dave Jones:** ethernet switch directly through the ethernet switch chip directly through to our SPI to ethernet interface. So, there you go. Then, we've got 1 2 3. Then, we got our SPI bus coming out of there into our connector. And bingo, we should be able

**Dave Jones:** to get a low bandwidth internet connectivity through to each board on the motherboard. And we can do this pretty cheaply. And then, of course, you'd have your RJ45, your external internet connection coming into the ethernet switch. And of course, you you

**Dave Jones:** know, we want a decent number of these on a board, eight or 10 or 12 or so, even more depending on the density that we can get in here and you know, power requirements and things like that. And

**Dave Jones:** we can, of course, we can have our ethernet switch just going off to yet another one. And then, that just drives more, and they all cascade from the one like that. So, you might actually have the one ethernet switch driving like,

**Dave Jones:** you know, two or three other ethernet switches. Now, of course, these boards have a lot of other IO on them as well. And you might still want to use those depending on you know, how you want this thing to

**Dave Jones:** work. So, you might actually have some And of course, you would want some LED status LEDs or something. So, you might have some LEDs, and these all go into here. And you might actually have another header next to each one or

**Dave Jones:** something so that you can actually like some IO or it gets some IO in and out of each one. So, because you might want this either it's like a supercomputer compute module, and everything just goes self-contained. You don't hook anything else up to it. Or

**Dave Jones:** you might use it as a, you know, a a 25- or 50-processor thing that's uh processing that's doing IO and stuff like that. And basically, just a big embedded computer that controls 40 separate things or 50 separate things or whatever. You might

**Dave Jones:** have a processor for each task. I don't know. Use your imagination for something like that, but I don't really want any of that IO stuff, although I might add it just for kicks. I just want this thing to actually be an

**Dave Jones:** supercomputer cluster array thingamabob. And that's the thing. This is not really a supercomputer as such. Each processor on here or each board because this is a four-core one here, but let's just say each one has a single core. They're running their own Linux OS

**Dave Jones:** and everything else. They're entirely separate. The only way they can communicate is via the Ethernet switches here. So, you might have like some maybe some dip switches on each one that can set an address for each one or you could

**Dave Jones:** program them in of course individually stuff like that. So, they'd have each board would have its own name on the network and stuff like that. And they're all network together. You can talk like that or we could potentially try and tie

**Dave Jones:** some IO between them. Perhaps maybe you could have a bus running between them if you wanted to do something fancy like that. But then we're getting into basically multiple processor computer architecture and stuff like that. And that's not really

**Dave Jones:** what we're what what I'm trying to achieve here anyway. I just want to a nicer solution than just whacking these in a box and wiring up the power and the Ethernet. I just want to put the power and the

**Dave Jones:** Ethernet basically all onto one motherboard just to make it neat. And then if we have a look at our power consumption here in previous video I actually measured this running with the full four cores at 100% running steady

**Dave Jones:** processing on the BOINC engine and I was getting it was drawing about 3.7 W. So, that's 0.75 amps at 5 W roughly. So, if you've got a motherboard with 10 of these Raspberry Pi Zeros on it, you need

**Dave Jones:** a 7.5 amp 5 W capable supply. And well, you You get those in various solutions. You could use like a little tiny PC. What What is it? A micro ATX power supply or something like that perhaps, but probably better to use some

**Dave Jones:** sort of off-the-shelf customized Well, off-the-shelf power brick or something like that perhaps. You can actually get modules that will do that, you know, 240 volts in, 5 volts out. It basically just depends on price, availability, and form factor because we haven't even talked

**Dave Jones:** about like a case for this thing. I was thinking maybe it'd be nice to have say a big extruded aluminum case that this whole motherboard just slid into on the rails. You know, something like this. I'll add a photo here. And you know, I don't know

**Dave Jones:** if you can actually You can probably get them this big. And you know, slide in. That'd just look really sexy. But then, you know, you probably I don't know. You could have all LEDs at one end or something like that. And I don't know.

**Dave Jones:** That'd be neat cuz we got to talk about power dissipation as well. This thing gets quite hot. I can't remember the temperature I've done in the previous video, but it was too hot to touch I think. And you've got to basically will

**Dave Jones:** glue on with some thermal adhesive just a heat sink onto each one. And then, you know, just passive a largish heat heat sink. We don't have to then couple that heat sink out to the external aluminum case. We can probably just let the

**Dave Jones:** you know, let the thing passively do that. That should work okay. Anyway, I like the idea of the Raspberry Pi Zero cuz it's It's super cheap. It's only five bucks each. Yes, it's only a one core one gig processor on the thing. Not

**Dave Jones:** nearly as grunty as this four core at 1.2 gigs, but you know, they're they're a nice small form factor. They only draw about 0.7 watts each I believe. Somebody's actually measured the Orange the Raspberry Pi Zero at running at full

**Dave Jones:** tilt and about 0.7 watts or thereabouts. So, you know, it is potentially lower power than this one, but yeah, not as powerful, but the density you can get in there. Oh, beauty. And of course for this sort of current you'd need big

**Dave Jones:** beefy traces on there like a fan out either one big bus running along like that, you know, huge traces on there. You probably, you know, you wouldn't need like 2 oz copper or anything like that for this sort of current, but you

**Dave Jones:** couldn't just run little piss ant traces over to each connector. You'd get uh too much drop on the thing. So, yeah, nice big fat buses there and maybe dropping off like that or you could star arrange it. It depends on how

**Dave Jones:** much space you had on the board layout. Something like like these slots. The bad thing about having slots in your board like this is that it just kills your routing space. You have to route everything around it. Power, data,

**Dave Jones:** everything else. It, you know, can become a real pain. So, if I was to do this elegantly in terms of power, I would get a like a proper PCB mount power brick or something like that or a module that actually you could

**Dave Jones:** mount on the board. So, you have this one big board. As I said, maybe slide into an extruded aluminum case and the power supply would mount on the end of it like this and you'd have like 240 volts coming in one end and then they

**Dave Jones:** give you the 5 volts at, you know, 10 amps out or whatever and then that just wires directly into the board then you have the huge buses running here and that it all just slide in as one big

**Dave Jones:** solution into the extruded aluminum case. That That'd be like a nice sexy solution. So, there you go. I hope you enjoyed that. This is just like a first thought kind of thing of how I would integrate these into a, you know, a

**Dave Jones:** Raspberry Pi supercomputer array or an Orange Pi supercomputer array and like which is a bit more elegant than the solutions other people have done where they've just physically wired these together with the Ethernet hub switch and everything else and wires

**Dave Jones:** running everywhere. And they can kind of look funky if you light them all up, but they're big and they're bulky, and then, you know, this is if you can do it like on one big motherboard like this, you

**Dave Jones:** can get some quite high density in these things depending on the type of board you use, and you could use some other compute module. For example, there's lots of compute modules on the market, but you basically got to get one

**Dave Jones:** that is that has end compatible uh you know, plug-in type thing. So, either like an SO-DIMM based uh system. Yes, Raspberry Pi do make the Raspberry Pi compute module, but it's like, you know, 25, 30 bucks each, and it's

**Dave Jones:** basically just like a an original Raspberry Pi. It's not that great. So, in terms of bang for buck, it's very, very poor. This Orange Pi One absolutely kills it for 10 bucks for the four cores at 1.2 gigs. So, yeah, those

**Dave Jones:** compute modules, unless you picked them up for a song, and I don't think they ever sold really well. I mean, I just checked uh Farnell have Element 14 have like, you know, tens of thousands of these things in stock or something. I

**Dave Jones:** don't know, thousands in stock. So, yeah, I don't think they sold too well. That was a bit of a fail, that the Raspberry Pi compute module, but the idea, the concept, really good. If you can just you can just have an SO

**Dave Jones:** connector on there, bang, bang, bang, bang, and the density you could get is absolutely incredible, but nobody, you know, if you know of any uh um Linux, you know, that sort of is compatible like that has a Linux build for it. Like

**Dave Jones:** Raspberry Pi's probably got the best and most refined build out there cuz there's so many people using it, they got so many people working on it, etc. As I saw as you saw in the previous video for this Orange Pi One,

**Dave Jones:** the software, the builds for it aren't that great and up-to-date and stuff like that, but you can make it work. I've yet to know if the SPI one will work for the Orange Pi one, the Microchip Inc 28J60,

**Dave Jones:** but I'm I believe it does work. People have done this and it does work for the Raspberry Pi. So, no worries. But yeah, if you know of any other compute modules that might be more suitable at a low

**Dave Jones:** cost. Yes, you can get them. You've been able to get these compute modules. I was using them back in the '90s, you know, there's nothing new about these things that play, you know, compute modules in SO in in DIMM module format and stuff like

**Dave Jones:** that. They go way, way back. And but the problem is the price, you know, the good thing about the say the this Orange Pi one or the Raspberry Pi Zero, five or 10 bucks per board. I mean, it's so compelling. I

**Dave Jones:** mean, you're going to add a couple of bucks for these SPI to Ethernet encoder chips cuz you're not buying them in, you know, 100,000, 10,000 volume or something like that. So, yeah, it adds significantly, but I think that's a nice could be a nice,

**Dave Jones:** elegant solution. So, hopefully I get the time and the motivation to actually start laying out this thing and get something working. So, hope you enjoyed it. If you want to discuss it, links down below, all that sort of

**Dave Jones:** stuff. Catch you next time. The Broadcom processor used on the Raspberry Pi 2 famously can't get the data sheet for it. You got to sign an NDA and all that sort of crap. But with the Allwinner H3 chipset here, they're

**Dave Jones:** both Cortex A7, by the way, so the same Cortex except the Allwinner A3 is actually faster. Now, if you take a look at the Orange Pi website very briefly, it looks kind of impressive at the top surface, but that's pretty much where it

**Dave Jones:** stops. I found a lot of issues with this thing trying to set it up.
