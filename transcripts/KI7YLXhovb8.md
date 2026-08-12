---
video_id: KI7YLXhovb8
title: EEVblog #934 - Raspberry Pi Supercomputer Cluster PART 1
url: https://www.youtube.com/watch?v=KI7YLXhovb8
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 27, "3": 44, "4": 61, "5": 76, "6": 88, "7": 104, "8": 117, "9": 128, "10": 139, "11": 149, "12": 163, "13": 186, "14": 198, "15": 209, "16": 225, "17": 244, "18": 253, "19": 264, "20": 284, "21": 294, "22": 307, "23": 315, "24": 329, "25": 341, "26": 353, "27": 368, "28": 378, "29": 389, "30": 399, "31": 406, "32": 420, "33": 440, "34": 451, "35": 460, "36": 482, "37": 491, "38": 508, "39": 521, "40": 533, "41": 545, "42": 572, "43": 581, "44": 595, "45": 613, "46": 630, "47": 651, "48": 671, "49": 683, "50": 697, "51": 709, "52": 719, "53": 730, "54": 742, "55": 755, "56": 765, "57": 781, "58": 795, "59": 807, "60": 821, "61": 837, "62": 846, "63": 859, "64": 880, "65": 893, "66": 903, "67": 927, "68": 944, "69": 963, "70": 974, "71": 985, "72": 994, "73": 1006, "74": 1024, "75": 1042, "76": 1062, "77": 1079, "78": 1091, "79": 1103, "80": 1112, "81": 1134, "82": 1145, "83": 1168, "84": 1178, "85": 1190, "86": 1198, "87": 1207, "88": 1220, "89": 1234, "90": 1243, "91": 1257, "92": 1273, "93": 1285, "94": 1294, "95": 1305, "96": 1312, "97": 1328, "98": 1349, "99": 1358, "100": 1383, "101": 1398, "102": 1412, "103": 1421, "104": 1438, "105": 1447, "106": 1472, "107": 1482, "108": 1493, "109": 1507, "110": 1517, "111": 1528, "112": 1539, "113": 1551, "114": 1563, "115": 1575, "116": 1586}
---

**Dave Jones:** Hi, in a previous video, you've seen these Orange Pi ones that I got. I got like 10 of these things before use as potentially a Raspberry Pi in this case, Orange Pi little arm supercomputer.

**Dave Jones:** And these are actually quite popular projects where people get Raspberry Pis and cluster them all together and you know, it's so to speak make a super little arm supercomputer with them.

**Dave Jones:** I mean, it's not nearly as powerful as you know, the latest modern Intel CPUs and things like that, but it's fun. And this one is in particular, this is the Orange Pi 1 model and it's got a four-core processor in it and it's not a bad little beast.

**Dave Jones:** It's generally speaking faster than the Raspberry Pi and it does a reasonable job and it's fun, but most importantly, it's cheap. This is only $10 for a four-core 1.2 gig or 1.3 gig is it arm arm cortex processor in it.

**Dave Jones:** So, it's a little bit of a beast especially for the money, 10 bucks. And so I thought it'd be fun to make a little Whopper computer. Yes, I might even stick it inside like a something that looks like the Whopper.

**Dave Jones:** That'd be fantastic. So I thought I'd start out with just a video outlining my concept for this thing. I haven't built it yet, but hey, let's have a look at the ideas because it could be quite interesting.

**Dave Jones:** Now, quite a lot of people have built these Raspberry Pi cluster or supercomputers before and they generally all that involves is basically a case, you know, some people laser cut their own acrylic cases and stuff like that and they light them up and they look all fancy and everything else.

**Dave Jones:** And hey, I could do this in a day, no problems whatsoever. All I've got to do is basically get a whole bunch of these, stick them together maybe with some standoffs or you know, something like that.

**Dave Jones:** And then I get power for each one. There's a little DC jack for each one, so you just apply power, hook it up to a pretty beefy power supply like a PC power supply or something like that.

**Dave Jones:** And then you just hook up the ethernet, get yourself one of these ethernet switches here. You know, you don't need a fast one, just a 10 100 type one and Bob's your uncle.

**Dave Jones:** Basically, you've got yourself a cluster computer. So, it's just basically just arranging these physically. There's nothing special there at all, but I thought, "Hey, you know, that's not very elegant.

**Dave Jones:** You got the ethernet cables hanging out and you got routing problems and dicky little DC jacks and things like that. Wouldn't it be nice if actually designed like a custom motherboard like this and these can just plug in.

**Dave Jones:** You can just have a whole bunch of them plug in, no cables, no nothing. That'd be fantastic. So, let's take a look at doing that. And yes, before you mention it, I know this is not going to be as powerful as a modern Intel CPU and GPU and things like that for like for my intended application running BOINC on it and doing SETI and other compute research, I

**Dave Jones:** know it's not as powerful as that in terms of dollar per watt potentially and in terms of performance per watt is basically one of the more critical things for this sort of thing, but hey, these things are fun.

**Dave Jones:** So, I'm just going to have some fun with this. I know it might not be the most efficient thing, you know, an Nvidia GPU card will likely kill this array in terms of performance per watt.

**Dave Jones:** But hey, I want to do it just because. That's it. Just because. Now, the first thing to note is that the Orange Pi 1 is not compatible with the Raspberry Pi 2 in terms of its physical plug-in ability.

**Dave Jones:** Why? Because the header connector here is actually reversed. It's the same pinout and functionality, but it's reversed. They physically reversed it so that the shield things, the hats or whatever they are, go actually don't sit over the board like this like they do on the Raspberry Pi.

**Dave Jones:** They sit in here. This one actually reversed it so they sit outside here. And the reason for that is a smaller form factor board and the ethernet and USB connectors actually getting in the way here.

**Dave Jones:** So that's really annoying. So any solution we make where we can plug these into a any sort of motherboard or something like that, it's not going to be compatible with the Raspberry Pi.

**Dave Jones:** The connector is going to be physically back to front. Bummer. Now of course the first thing is is how do you plug this into a motherboard? Now you know, we could put it upside down maybe and have a 40-pin vertical header on the board and then you can stack them like that, but that takes up a lot of board space.

**Dave Jones:** That's a lot of physical space on your motherboard actually wasted. If you've got multiple boards side by side like like that, you know, a motherboard this big you might only be able to fit five in.

**Dave Jones:** But if you mount them vertically like this, you can potentially get much greater density for a given motherboard size. And that's what we want. Now unfortunately this thing comes with the header pre-soldered on like this.

**Dave Jones:** So you know, we're not going to go suck off the header and put a right angle one in on there. That would have been awesome if we had a right angle.

**Dave Jones:** We could have just went bang bang bang bang bang on a motherboard. That'd have been fantastic, but we're not going to go suck those out. So we have to come up with some other solution if we want to use this Orange Pi One or a Raspberry Pi for that matter.

**Dave Jones:** It's just because the pin out's different. They've both got these vertical headers on them. Now you can actually get right angle female header sockets for PCB. So instead of plugging in vertically, it'd like the connector would be like this.

**Dave Jones:** Here's a image of it. I'll get an image and then you just plug it in on the side like that. So, you might think, "Hey, there's our solution." But, uh-uh, trap for young players.

**Dave Jones:** You'll notice that this header sits significantly off the board like that. And this is actually, if you go look at the data sheet for the header, it's actually, going to be much smaller than this gap here.

**Dave Jones:** So, you'd even have to grind off some of the board and be careful not to get the traces, uh you know, hit any traces or short out any ground planes or anything like that or cut any ground planes.

**Dave Jones:** Um so, you don't want to do that. That's just a ridiculous solution. Or, we've got to come up with some other way to uh get these things physically lifted off the board.

**Dave Jones:** Now, of course, you could get the header connector, uh female header connector for the board, put something under it, and then, uh you know, right lift it off the board or something, some sort of spacer.

**Dave Jones:** Yeah, that's a solution. But, there's another way, too. Now, please excuse the crudity of this model. I didn't have time to build it to scale or to paint it.

**Dave Jones:** What you do is you have your uh right-angle female header connector, actually, you know, through-hole or could be Well, probably not surface mount cuz they're going to have the pins coming out the side, which is going to be troublesome.

**Dave Jones:** So, probably a through-hole uh version here. And they've got the holes basically on either side of the connector, and then you just route out paths like this on one side of the connector, and you get your board, and then you just put it into the slot like this so that it goes down into the board, and then you slide it in like that.

**Dave Jones:** Bob's your uncle. Beauty. But, of course, it's not as dense a solution as it could be because the width of this has to cater for the fact that you've got to put this in and then slide it across like that.

**Dave Jones:** So, you know, the slot actually doesn't have to come all the way up, and you could use a surface mount one, actually. The pins come out here and here.

**Dave Jones:** This side's not a problem, but coming out this side, the slot doesn't have to go right up to the connector like this. You can have the right uh the surface mount pins coming out like that, and then the slot only and because you've got a distance in there, so you can actually see there's a thickness of the uh plastic base of this header, so it doesn't actually come all

**Dave Jones:** the way in. So, you've got So, the pins on here can actually see any surface mount pins, and the slot can actually be further out from the connector than what I've shown there.

**Dave Jones:** So, you only have to put it in and then slide it in like that. So, you know, the slot basically has to be the width of these uh pins, so to speak, set out somewhat, and then the distance between boards is going to be set by these pain-in-the-ass Ethernet connectors and USB, which we're not going to use.

**Dave Jones:** So, it's not the densest solution, but it's better than flipping this board upside down, plugging it into a verti- into a vertical header like that, and then having two three like, you know, on a board that size, we're only going to get three in there.

**Dave Jones:** But this one, we can potentially get one, two, oh yeah, one, two, three, four, five. You know, I'm just eyeballing this, but, you know, basically double the density, easy.

**Dave Jones:** Now, a nicer solution to this is the Raspberry Pi Zero. Now, it's only five bucks. It's half the price of this, but in terms of dollars per watt, um it's not as good.

**Dave Jones:** This is a four-core 1.3 gig uh processor or greater than 1 gig, and the Raspberry Pi Zero is only 1 gig at um with a single core, but it comes with the um header connector not populated, so you can solder in your own right-angle header connector, and then you can use those vertical standard vertical connectors, and you wouldn't need to uh put in any slot like this.

**Dave Jones:** So, it'll just bang bang bang, and you can get and And they don't have the um big ethernet connector and USB connector on there, they're much thinner and you can get double the density again.

**Dave Jones:** So, the Raspberry Pi Zero, it's not too bad if you can get twice the density uh, for half the cost, but you'll lose, ultimately going to lose like half of your performance in the end.

**Dave Jones:** So, yeah, I don't know. Which one do you go for? Hmm, the Raspberry Pi Zero is nice a solution. It could be lower power because, hey, it's, you know, it's not running any of the ethernet uh, functionality and it's just generally a lower power, uh, board than this one, I believe.

**Dave Jones:** But, this motherboard idea, it's all going to come to naught unless we can actually get internet connectivity through these header pins. And the Orange Pi One ethernet over to here, these ethernet pins do not come these physical ethernet pins, uh, do not come down to this header.

**Dave Jones:** It doesn't have it. So, we're in trouble there, but, uh-huh, I think I've found a solution for this. As luck would have it, if you have a look at the, uh, pinout for the Raspberry Pi, it's the same on the Orange Pi One here, there is an SPI port that actually comes out on these pins.

**Dave Jones:** So, uh-huh, can we convert the SPI into an ethernet interface? Yes, we can. Now, as it turns out, the, uh, Raspberry Pi Linux, uh, build, I believe, has a built-in driver for the Microchip, um, ENC28J60 SPI to ethernet, uh, converter chip.

**Dave Jones:** So, all we need is to put one of those chips on our board for each one. We can have one for each one and these things are cheap. They're available from Digikey, they're only a couple of bucks.

**Dave Jones:** We can solder those onto our motherboard here and bingo, we can get connectivity to each one of our boards, be it an Orange Pi uh one or a Raspberry Pi zero or whatever other uh board that we want to plug into this system.

**Dave Jones:** Beauty. And although I haven't tried this, I believe that all you got to do is add in one uh line to the uh boot uh config file in your build and then bingo, it just automatically works.

**Dave Jones:** This um ENC28J60 chip just handles it. You plug it into Ethernet and away you go. Now, of course, it's not going to be the uh fastest solution via the SPI bus.

**Dave Jones:** You can change the speed in the uh configuration and stuff like that, but it's not going to be nearly as fast, but you know, this thing is basically a uh compute system, you know?

**Dave Jones:** It's not really a you know, high throughput uh high bandwidth type of system. So, hey, you know, a few megabits or something is fine. Or a couple hundred K bits is fine.

**Dave Jones:** As long as we've got an Ethernet connection, especially for the use I want to make it to, it's just got to uh download stuff from the Boinc server. It can do that slowly and this just got to report its results back and things like that.

**Dave Jones:** Not high bandwidth stuff. Most of the time, it's basically not talking at all. So, we just need an ENC28J60 chip for each one of our modules like this. Just wire that in.

**Dave Jones:** No worries. But, hey, of course, we need an uh Ethernet uh switch up here to connect all these ones into. So, we don't want to use a physical Ethernet switch like that because well, that's just ugly cuz we've got the uh cables again.

**Dave Jones:** We'd have to have like a uh you know, an RJ45 on there going off for each one and I'll bugger that. That ruins our nice solutions. So, we take a look at a typical 10/100 uh Ethernet switchy, you can see that there's bugger all in these things.

**Dave Jones:** We've just got the main chipset here. This is a uh Realtek uh one and then we've got the magnetics. You can see the uh see the differential traces going off there um two pairs for each ethernet port.

**Dave Jones:** This is an eight-port chip. It's all in one. It's a power supply and the main chip and that's it. There's no e squared prom, there's no programming. Although these things are programmable, they just work by default, I believe.

**Dave Jones:** Anyway, I've never actually designed an ethernet switch into something before, but hey, and then the LEDs just hook up there for the monitoring and everything else. So, all we need, in theory, is one of these ethernet switch chips.

**Dave Jones:** And yes, you can just buy it from Digikey. You can't get this Realtek one. Yeah, and you can't buy this chip from Digikey. So, I'm not going to use this Realtek one, but hey, Microchip have one.

**Dave Jones:** Other Other companies have similar sort of chips. You just You've just got to choose one that is designed for stand-alone applications, so it doesn't need boot configuration and all that sort of stuff, and it's got to have the phi built in as well.

**Dave Jones:** But what do we do with these pesky magnetics here? Do we need the magnetics? I don't think so. I think we can get away cuz we're going directly This chip would be directly on our board over here, and then it'll be powering, say, eight or four or depending on how many you needed, how many you designed to have on your motherboard, then it's going directly chip to chip.

**Dave Jones:** As long These are current-driven differential outputs. So, all we need is to is some output resistors tied to ground, basically, or AC coupled to ground, and then we should get away.

**Dave Jones:** Should be able to get away without the magnet magnetics. They're only designed for driving lines. Now, once again, I've never actually tried this, but I I think, in theory, it should work.

**Dave Jones:** But I stand to be corrected. So, in theory, what you should need is just some termination resistors on the line here. Often, these are AC coupled down to ground, but you'd have to read the particular data sheet that you're actually got, and we should be able how connect the ethernet switch directly through the ethernet switch chip directly through to our SPI to ethernet interface.

**Dave Jones:** So, there you go. Then, we've got 1 2 3. Then, we got our SPI bus coming out of there into our connector. And bingo, we should be able to get a low bandwidth internet connectivity through to each board on the motherboard.

**Dave Jones:** And we can do this pretty cheaply. And then, of course, you'd have your RJ45, your external internet connection coming into the ethernet switch. And of course, you you know, we want a decent number of these on a board, eight or 10 or 12 or so, even more depending on the density that we can get in here and you know, power requirements and things like that.

**Dave Jones:** And we can, of course, we can have our ethernet switch just going off to yet another one. And then, that just drives more, and they all cascade from the one like that.

**Dave Jones:** So, you might actually have the one ethernet switch driving like, you know, two or three other ethernet switches. Now, of course, these boards have a lot of other IO on them as well.

**Dave Jones:** And you might still want to use those depending on you know, how you want this thing to work. So, you might actually have some And of course, you would want some LED status LEDs or something.

**Dave Jones:** So, you might have some LEDs, and these all go into here. And you might actually have another header next to each one or something so that you can actually like some IO or it gets some IO in and out of each one.

**Dave Jones:** So, because you might want this either it's like a supercomputer compute module, and everything just goes self-contained. You don't hook anything else up to it. Or you might use it as a, you know, a a 25- or 50-processor thing that's uh processing that's doing IO and stuff like that.

**Dave Jones:** And basically, just a big embedded computer that controls 40 separate things or 50 separate things or whatever. You might have a processor for each task. I don't know. Use your imagination for something like that, but I don't really want any of that IO stuff, although I might add it just for kicks.

**Dave Jones:** I just want this thing to actually be an supercomputer cluster array thingamabob. And that's the thing. This is not really a supercomputer as such. Each processor on here or each board because this is a four-core one here, but let's just say each one has a single core.

**Dave Jones:** They're running their own Linux OS and everything else. They're entirely separate. The only way they can communicate is via the Ethernet switches here. So, you might have like some maybe some dip switches on each one that can set an address for each one or you could program them in of course individually stuff like that.

**Dave Jones:** So, they'd have each board would have its own name on the network and stuff like that. And they're all network together. You can talk like that or we could potentially try and tie some IO between them.

**Dave Jones:** Perhaps maybe you could have a bus running between them if you wanted to do something fancy like that. But then we're getting into basically multiple processor computer architecture and stuff like that.

**Dave Jones:** And that's not really what we're what what I'm trying to achieve here anyway. I just want to a nicer solution than just whacking these in a box and wiring up the power and the Ethernet.

**Dave Jones:** I just want to put the power and the Ethernet basically all onto one motherboard just to make it neat. And then if we have a look at our power consumption here in previous video I actually measured this running with the full four cores at 100% running steady processing on the BOINC engine and I was getting it was drawing about 3.7 W.

**Dave Jones:** So, that's 0.75 amps at 5 W roughly. So, if you've got a motherboard with 10 of these Raspberry Pi Zeros on it, you need a 7.5 amp 5 W capable supply.

**Dave Jones:** And well, you You get those in various solutions. You could use like a little tiny PC. What What is it? A micro ATX power supply or something like that perhaps, but probably better to use some sort of off-the-shelf customized Well, off-the-shelf power brick or something like that perhaps.

**Dave Jones:** You can actually get modules that will do that, you know, 240 volts in, 5 volts out. It basically just depends on price, availability, and form factor because we haven't even talked about like a case for this thing.

**Dave Jones:** I was thinking maybe it'd be nice to have say a big extruded aluminum case that this whole motherboard just slid into on the rails. You know, something like this.

**Dave Jones:** I'll add a photo here. And you know, I don't know if you can actually You can probably get them this big. And you know, slide in. That'd just look really sexy.

**Dave Jones:** But then, you know, you probably I don't know. You could have all LEDs at one end or something like that. And I don't know. That'd be neat cuz we got to talk about power dissipation as well.

**Dave Jones:** This thing gets quite hot. I can't remember the temperature I've done in the previous video, but it was too hot to touch I think. And you've got to basically will glue on with some thermal adhesive just a heat sink onto each one.

**Dave Jones:** And then, you know, just passive a largish heat heat sink. We don't have to then couple that heat sink out to the external aluminum case. We can probably just let the you know, let the thing passively do that.

**Dave Jones:** That should work okay. Anyway, I like the idea of the Raspberry Pi Zero cuz it's It's super cheap. It's only five bucks each. Yes, it's only a one core one gig processor on the thing.

**Dave Jones:** Not nearly as grunty as this four core at 1.2 gigs, but you know, they're they're a nice small form factor. They only draw about 0.7 watts each I believe.

**Dave Jones:** Somebody's actually measured the Orange the Raspberry Pi Zero at running at full tilt and about 0.7 watts or thereabouts. So, you know, it is potentially lower power than this one, but yeah, not as powerful, but the density you can get in there.

**Dave Jones:** Oh, beauty. And of course for this sort of current you'd need big beefy traces on there like a fan out either one big bus running along like that, you know, huge traces on there.

**Dave Jones:** You probably, you know, you wouldn't need like 2 oz copper or anything like that for this sort of current, but you couldn't just run little piss ant traces over to each connector.

**Dave Jones:** You'd get uh too much drop on the thing. So, yeah, nice big fat buses there and maybe dropping off like that or you could star arrange it. It depends on how much space you had on the board layout.

**Dave Jones:** Something like like these slots. The bad thing about having slots in your board like this is that it just kills your routing space. You have to route everything around it.

**Dave Jones:** Power, data, everything else. It, you know, can become a real pain. So, if I was to do this elegantly in terms of power, I would get a like a proper PCB mount power brick or something like that or a module that actually you could mount on the board.

**Dave Jones:** So, you have this one big board. As I said, maybe slide into an extruded aluminum case and the power supply would mount on the end of it like this and you'd have like 240 volts coming in one end and then they give you the 5 volts at, you know, 10 amps out or whatever and then that just wires directly into the board then you have the huge buses running here and

**Dave Jones:** that it all just slide in as one big solution into the extruded aluminum case. That That'd be like a nice sexy solution. So, there you go. I hope you enjoyed that.

**Dave Jones:** This is just like a first thought kind of thing of how I would integrate these into a, you know, a Raspberry Pi supercomputer array or an Orange Pi supercomputer array and like which is a bit more elegant than the solutions other people have done where they've just physically wired these together with the Ethernet hub switch and everything else and wires running everywhere.

**Dave Jones:** And they can kind of look funky if you light them all up, but they're big and they're bulky, and then, you know, this is if you can do it like on one big motherboard like this, you can get some quite high density in these things depending on the type of board you use, and you could use some other compute module.

**Dave Jones:** For example, there's lots of compute modules on the market, but you basically got to get one that is that has end compatible uh you know, plug-in type thing. So, either like an SO-DIMM based uh system.

**Dave Jones:** Yes, Raspberry Pi do make the Raspberry Pi compute module, but it's like, you know, 25, 30 bucks each, and it's basically just like a an original Raspberry Pi. It's not that great.

**Dave Jones:** So, in terms of bang for buck, it's very, very poor. This Orange Pi One absolutely kills it for 10 bucks for the four cores at 1.2 gigs. So, yeah, those compute modules, unless you picked them up for a song, and I don't think they ever sold really well.

**Dave Jones:** I mean, I just checked uh Farnell have Element 14 have like, you know, tens of thousands of these things in stock or something. I don't know, thousands in stock.

**Dave Jones:** So, yeah, I don't think they sold too well. That was a bit of a fail, that the Raspberry Pi compute module, but the idea, the concept, really good. If you can just you can just have an SO connector on there, bang, bang, bang, bang, and the density you could get is absolutely incredible, but nobody, you know, if you know of any uh um Linux, you know, that sort of is compatible

**Dave Jones:** like that has a Linux build for it. Like Raspberry Pi's probably got the best and most refined build out there cuz there's so many people using it, they got so many people working on it, etc.

**Dave Jones:** As I saw as you saw in the previous video for this Orange Pi One, the software, the builds for it aren't that great and up-to-date and stuff like that, but you can make it work.

**Dave Jones:** I've yet to know if the SPI one will work for the Orange Pi one, the Microchip Inc 28J60, but I'm I believe it does work. People have done this and it does work for the Raspberry Pi.

**Dave Jones:** So, no worries. But yeah, if you know of any other compute modules that might be more suitable at a low cost. Yes, you can get them. You've been able to get these compute modules.

**Dave Jones:** I was using them back in the '90s, you know, there's nothing new about these things that play, you know, compute modules in SO in in DIMM module format and stuff like that.

**Dave Jones:** They go way, way back. And but the problem is the price, you know, the good thing about the say the this Orange Pi one or the Raspberry Pi Zero, five or 10 bucks per board.

**Dave Jones:** I mean, it's so compelling. I mean, you're going to add a couple of bucks for these SPI to Ethernet encoder chips cuz you're not buying them in, you know, 100,000, 10,000 volume or something like that.

**Dave Jones:** So, yeah, it adds significantly, but I think that's a nice could be a nice, elegant solution. So, hopefully I get the time and the motivation to actually start laying out this thing and get something working.

**Dave Jones:** So, hope you enjoyed it. If you want to discuss it, links down below, all that sort of stuff. Catch you next time. The Broadcom processor used on the Raspberry Pi 2 famously can't get the data sheet for it.

**Dave Jones:** You got to sign an NDA and all that sort of crap. But with the Allwinner H3 chipset here, they're both Cortex A7, by the way, so the same Cortex except the Allwinner A3 is actually faster.

**Dave Jones:** Now, if you take a look at the Orange Pi website very briefly, it looks kind of impressive at the top surface, but that's pretty much where it stops. I found a lot of issues with this thing trying to set it up.
