---
video_id: 6nqSFYVKnP4
title: EEVblog #829 - Siglent SDM3055 Bench Multimeter Teardown
url: https://www.youtube.com/watch?v=6nqSFYVKnP4
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 32, "3": 49, "4": 64, "5": 80, "6": 93, "7": 106, "8": 119, "9": 131, "10": 144, "11": 155, "12": 167, "13": 185, "14": 195, "15": 212, "16": 225, "17": 238, "18": 253, "19": 268, "20": 285, "21": 301, "22": 313, "23": 328, "24": 342, "25": 352, "26": 366, "27": 378, "28": 389, "29": 404, "30": 416, "31": 429, "32": 446, "33": 463, "34": 478, "35": 495, "36": 508, "37": 522, "38": 537, "39": 550, "40": 566, "41": 579, "42": 596, "43": 612, "44": 626, "45": 644, "46": 661, "47": 676, "48": 693, "49": 708, "50": 722, "51": 736, "52": 750, "53": 761, "54": 777, "55": 793, "56": 804, "57": 822, "58": 840, "59": 856, "60": 874, "61": 891, "62": 906, "63": 920, "64": 933, "65": 948, "66": 963, "67": 977, "68": 993, "69": 1008, "70": 1024, "71": 1037, "72": 1052, "73": 1065, "74": 1080, "75": 1098, "76": 1113, "77": 1128, "78": 1141, "79": 1158, "80": 1173, "81": 1187, "82": 1204, "83": 1221, "84": 1238, "85": 1253, "86": 1265, "87": 1283, "88": 1300, "89": 1315, "90": 1329, "91": 1343, "92": 1360, "93": 1375, "94": 1392, "95": 1406, "96": 1423, "97": 1438, "98": 1452, "99": 1466, "100": 1476, "101": 1487, "102": 1503, "103": 1517, "104": 1532, "105": 1546, "106": 1558, "107": 1569, "108": 1581, "109": 1594, "110": 1608, "111": 1621, "112": 1632}
---

**Dave Jones:** Hi, welcome to another Siglent teardown. This time we've got the Siglent multimeter. We haven't had a Siglent multimeter before. This is the STM3055 bench multimeter. Specifically, this is the 3055A model. And I believe the only difference between the A model that I've got here

**Dave Jones:** and the three and the much cheaper 3055 is that this one has a GPIB option and that's it. Now, street price of this thing for the A model that I've got here, it's about 630 odd uh US dollars. Now, that's pretty

**Dave Jones:** pricey. So, I wouldn't be getting the GPIB version of this unless you absolutely must have the GPIB option. You're much better off going for just the 3055A and its street price is currently uh 422 bucks on special. I was able to uh

**Dave Jones:** find this thing for US dollars, different in other countries and different currencies, of course. But, uh this is a five and a half digit uh meter. It's a 240,000 counts. So, it's not like 600,000 count or anything like that. So, 20 240,000

**Dave Jones:** count, little bit unusual. Um a 0.015% uh DC basic uh accuracy class instrument. So, its specs aren't really going to set the world on fire. 150 uh samples per second, which is kind of sort of, you know, not too bad for a

**Dave Jones:** bench multimeter, but it's not like the higher end ones, for example. So, it sits in this sort of, you know, almost no man's land between like the, you know, the high end Agilent uh bench multimeters for just under or just over

**Dave Jones:** a thousand dollars and uh you know, a decent high end uh handheld multimeter, for example, which you can get five and a half digit multimeters. You don't have to go to a bench multimeter like this to actually get uh five and a half digits,

**Dave Jones:** but a lot of people prefer uh the bench meters cuz they sit on the bench, they're always there. They've got a nice big graphical display on the thing and this thing's got uh trend pot plotting, everything else. Very similar

**Dave Jones:** functionality uh to the Agilent uh bench meter that we've seen before, and I'll show you a comparison at the end cuz it's absolutely hilarious. But, of course, the downsides of bench multimeters, they are tied to the bench, and generally

**Dave Jones:** they're not going to have the same sort of input protection as a handheld multimeter cuz they're not designed to be used in the field. Hence, we're only looking at um CAT II 600 V and CAT 1000 V rating. That's very typical of a bench

**Dave Jones:** uh multimeters. But, of course, one of the other advantages of a bench multimeter, you typically get, and of course you do get in here, the uh four-wire measurement. So, you can do four-wire ohms. So, I've got the two

**Dave Jones:** extra uh sense terminals here. Very nice. Anyway, we'll power this puppy up at the end. Let's have a look at it. It feels like looks and feels like a reasonable quality uh bench meter. You know, the no problem with the buttons

**Dave Jones:** there. Uh banana plugs look half reasonable. And it's a nice little um it's not too deep. It is quite um uh shallow in that respect. So, it doesn't take up too much uh bench depth. Uh selectable 110 or 240 V operations.

**Dave Jones:** So, there's no worries about buying it in a particular country. It's now it's got uh LAN built in and uh USB uh host as well. It's got uh external uh trigger cuz you can sort of, you know, use these

**Dave Jones:** for a bit of automation. And it's got an extension card option. Now, like that must be I'm uh presuming the GPIB option, but this is the A model. And according to the um according to the data sheet and websites

**Dave Jones:** I've looked at, the A model is supposed to have GPIB. That's why you pay extra for the A, but there's nothing there. So, this one might be an oddball one. This is, you know, like got this directly from Siglent. Like it's a I

**Dave Jones:** think it's a demo unit or something. So, I'm not exactly sure what's going on there. Anyway, there's our 10 amp fuse on the back. So, let's take this puppy apart and uh have a look. All the volt nuts, of course, want to know what

**Dave Jones:** references in there. Is it going to be a you know, your old school? They've got some thread lock on there. That's nice. Um is it going to be your old school uh LM 3 Oh, cow sticker. Dolt. This bastard, who cares?

**Dave Jones:** Um is it going to be your old school LM 399 or is it going to be something different? All right, let's pop the hood on this and see what we've got. Oh, we're in like Flynn. We can see old school looking

**Dave Jones:** transformer in that thing. Wow. So, it looks like we've got just a linear power supply and the voltage tap is just a different tap on the transformer there, but like I don't have to go any further. It's all exposed. Right there, ready for

**Dave Jones:** us. Let's take a look. Oh, yeah, look at that. There's the trademark Siglent rust. I'm sure they do have a trademark on that. No worries whatsoever. Yep, rust a plenty. And that's the thing, the first thing you notice about

**Dave Jones:** this is just like the cheap quality and feel of the metal work and the rust just you know, adds It's just the icing on the cake there. We've got a little cheap ass fan in here and what's it doing? It's

**Dave Jones:** you know, we've got some vents here on the other side, but it's blocked by the transformer. You know, mate and through here and uh it's just like do they even need a fan on something like this? I you

**Dave Jones:** know, jeez, I don't know. Anyway, yeah, it just feels just looks and feels pretty cheap and just kind of like, you know, slapped together. I'm not going to say amateur, but it it's just not a high quality bit

**Dave Jones:** of kit. If you put the I know it's not the same price bracket as the Agilent, but if you put the two side by side, it's chalk and cheese. At least they have gone to the effort to actually the

**Dave Jones:** ribbon cable going over here, going over to the front panel. At least they've gone to the effort to put in this insulating shield on here, but why they had to run it on on that side and why they just couldn't, you know,

**Dave Jones:** you know, the system designers couldn't actually move the connector over to the low voltage side here. I don't, you know, like I don't know. It's it's almost as if, you know, bit of an afterthought. Oh, we have to put the

**Dave Jones:** connector over here. Oh, well, we'll just punch a hole in here, run it over. We'll just put some insulating stuff on here and, you know, like it just seems a bit cludgy. And then our earth connection here is just a little

**Dave Jones:** bit of a It's not loosey-goosey, but it's not tied either. It's just a a spade lug, you know, like give me a proper, you know, shake-proof washer and everything. I I don't like that. And at least they have bent the metal work over

**Dave Jones:** there so there's no sharp edges on that cable gland there. So, that's all right. And it's just funny. They've got like the fan cut out here. It's like, "Oh, we weren't sure whether or not we'll put the fan here or over there." It's just,

**Dave Jones:** you know, a little lack of systems engineering. And as I said, we've got a linear power supply here. It doesn't need much power, so hence why you know, couldn't they have got away without using a fan? It'd be interesting put the

**Dave Jones:** uh thermal camera on this thing later, but anyway, small little up PCB mount heat sink. It's not flapping around in the breeze. It's actually one of the proper stud ones that are soldered onto the board, so nice. They've got Lelon brand caps, so, you

**Dave Jones:** know, yawn. They've got separate taps, of course. This This is the digital processing board, which we'll take a look at. It's got its own AC transformer tap electrically isolated from the input and acquisition side of things, so it's got

**Dave Jones:** its own little full wave bridge rectifier down there. It's got another Leel on cap. That's probably like a, you know, a 3.3 V. That looks like a switching supply over there to generate all the, you know, probably 1.2 V, 1.8 V, or whatever is

**Dave Jones:** required for the processor down here. So, that's all That's all hunky-dory, but yeah, once again, looks like we've got a couple of taps here. We've got a couple of two possibly two full wave bridge rectifiers there, and hence the two different

**Dave Jones:** caps. And then we've got our digital isolation between the processor board and the acquisition board here. That's this little flat flex ribbon cable. There's a We might actually take a look. That's one of those analog devices puppies, so

**Dave Jones:** that's an opto isolator. Got another opto isolator there. You'll notice that the big cutout there on the board. You can see cutout of the ground plane and everything else. So, they've got it nicely isolated. All hunky-dory. And there's our front end side of things.

**Dave Jones:** We'll take a closer look, but the first thing I notice, of course, is the uh thin film resistor network here from Caddock. They're one of the top makers. So, they're not unlike, you know, Fluke and Agilent who who roll their own ones,

**Dave Jones:** of course. So, they get Caddock to make it. So, no worries there at all. That's top notch. Then we've got some Looks like we've got ourselves a high voltage resistor network here. They're, you know, they they They're not They're

**Dave Jones:** not using those for their power dissipation, those large case resistors. They're using those for large voltage strings. So, that's a high voltage string. That's why they got them all in series. They're not that big for power dissipation reasons. And um

**Dave Jones:** you can see that they've got the gold trace going around there. That's our guard trace for leakage, so that's all right. Can see a couple of more guard traces down in here. I might get the macro lens and take a look at. And this

**Dave Jones:** high voltage string here, actually, if you follow the wires, follow the money, it goes up here, goes up here, goes up here. They're our sense terminals. They're our positive and negative sense terminals, so they're our positive and negative sense resistor

**Dave Jones:** chains like that. So, they're doing that, of course, for high voltage overload overload protection because, you know, people could accidentally mix up those connectors on the front, and they do. So, yeah, you've got to protect about against some idiot plugging, you know,

**Dave Jones:** 240 V mains into the sense terminals. But check it out, we have ourselves a genuine budge. Look at this. They have this big power resistor, which is, according to the footprint down there, is supposed to be a surface mount jobby.

**Dave Jones:** And they've got that flying lead coming over to this PTC. I mean, that's just horrible. There's no excuse for that in a bit of production gear like this. There's just, yeah, absolutely no excuse. Geez. I mean, come on. And this is rather

**Dave Jones:** unusual. Look at that. That looks like a ceramic resistor network. It almost looks like like it's a BGA package or or something like that. And there's like almost like a dip alternative part. That is that is bizarre. What on earth are they

**Dave Jones:** doing there? Anyway, the input protection is not too shabby here. This red wire is coming from our input banana plug. Then we've got a couple of gas discharge two tubes here. Couple of big beefy looking mobs. No worries

**Dave Jones:** whatsoever. And then we've got a nice looking big ass relay, but I'm not entirely sure what they're what they're switching there. Hmm. And they've got very beefy diode bridge protection there, which I've done a video on input protection arrangements

**Dave Jones:** and things like that. You'll typically find a diode bridge for clamping protection and oh yeah, that's a that's a decent beast and there are current sense resistors right down in there because our white our white cable coming over

**Dave Jones:** here is our current input and it goes off to these two cables. That goes off to the 10 amp fuse connector on the back. So I'm not sure why they're running this they've got a ceramic fuse in there, a little

**Dave Jones:** M205, but I don't you know, which is encapsulated, very nice. But yeah, why they've got that secondary fuse in there cuz this doesn't have a low current range. It's only got one single 10 amp current input and that's

**Dave Jones:** it. So yeah, I'm not sure why they ran the current input, that's a white wire there onto the board. They soldered that directly in. They got then they got some spade lugs coming over here to the fuse. Why not just run that

**Dave Jones:** you know, if you're going to fuse it on the back here, why not just run that fuse wire straight over to here and then just have a single wire running back. I don't get it. And I wonder what's under the shielded can. Is

**Dave Jones:** that the It it seems too near to the input here to to be like the voltage reference. So I reckon that's probably like the AC stuff, the possibly the true RMS converter. So we'll pop the hood on there. It looks like there's a screw

**Dave Jones:** accessed from the other side, but yeah, I can't traditional LM399 on here. It's not You probably don't wouldn't expect to find an LM399 class voltage reference in a instrument of you know, five and a half digit meter of this class. But yeah,

**Dave Jones:** we'll find that eventually, but let's pop the hood on that. It's near the front end. And I was right, but I was always going to be right because just based on its location and the functionality, that's what it had to be.

**Dave Jones:** No surprises for finding the venerable AD5632 RMS converter. So, that's just doing the AC range stuff. Bit of a kludge with the two resistors there. They've actually got those soldered together at the same point. Like And there, folks, is the money shot.

**Dave Jones:** There's our ADC. It's an Analog Devices AD7190, 24-bit delta-sigma converter, 4.8 kHz conversion rate, four channels. It's got built-in programmable again amplifier. Yeah, yeah, yeah, yeah. Fairly typical of what you'd expect to find in a 5 and 1/2 digit multimeter. Of course, unlike

**Dave Jones:** like Fluke and Keysight, they haven't like rolled their own, you know, dual slope converter and stuff like that. Just used an off-the-shelf delta-sigma. Good enough for a 5 and 1/2 digit meter, no worries whatsoever. And there's our voltage reference right next to it. It's

**Dave Jones:** the MAX6325, uh the CSA version. It's, you know, a reasonably schmick reference. It's a 0.5 ppm initial accuracy of 0.02%, but of course that doesn't matter a rat's ass. It's all about the temperature drift because this thing's got a nominal DC

**Dave Jones:** spec of 0.015%. So, actually better than this chip's initial spec. And that's possible because they calibrate these things and they adjust them. They program into them the calibration offsets at the factory. But of course the 0.5 ppm is only

**Dave Jones:** short-term drift. Long-term drift, spec sheet says about 30 ppm per 1,000 hours. So, you know, it's not going to set the world on fire, but hey, it's a 5 and 1/2 digit meter. So, it's good enough. Haven't gone through the calculations

**Dave Jones:** and all that really deep into the data sheet. I'll leave that up to the volt nuts to decide whether or not that's a suitable reference for the claimed specs and everything else and how it compares. I'm sure there's no shortage of people who

**Dave Jones:** will be uh willing to uh compare this to various other meters on the market. But once again, it's probably not fair to compare it to and you know, a Keysight or a Fluke that costs, you know, twice as much or more than this thing, three

**Dave Jones:** times more in uh some cases. So, yeah, you know, it it's good enough for the job, I guess. And there's a couple of these in here. These Analog Devices AD uh 8629. These are uh fairly schmic uh chopper amplifiers, a zero drift chopper

**Dave Jones:** amps like I use in my uh microcurrent. Tell you what, I must say, I'm not blown away by the uh soldering quality in this thing. I mean, it's not bad, but um yeah, you know, this lead-free rubbish. Mhm.

**Dave Jones:** But yeah, it's not the best. It's just a little bit sloppy. Little bit sloppy. Look, you know, excess paste on uh on that. Where is it? Where's my pointer? Sorry, can't get my pointer in. Excess paste on that cap and you know,

**Dave Jones:** like mhm. And as I showed you before, the uh guard traces, they they're those gold uh traces there have the solder mask removed. They're actually uh providing uh leakage and uh contaminant protection between uh critical traces. So, I guess

**Dave Jones:** they're not. They're doing there those ADG uh chips are a dead giveaway where as soon as you see um the ADG uh prefix like that, you know, they're um you know, some form of uh analog switch. And there are our current shunt

**Dave Jones:** resistors for you current shunt resistor fanboys. I know you're down there. You can see the uh serpentine trace on the one on the uh left there. And no surprises for finding just a little uh FPGA in there. That's a Lattice uh MachXO part. Really

**Dave Jones:** cheap, really uh not high density at all. It's just it would just be doing the uh sample uh you know, handling the sampling, the 150 uh samples per second, probably buffering that, and just feeding that across the digital

**Dave Jones:** interface. You can see that that's hooked up uh directly to the digital IO. So, yeah, it's just handling the sampling subsystem. And that's pretty much all she wrote on the analog front end. You know, it's it's got all the requisite stuff.

**Dave Jones:** Probably, you know, it does the job, does the business. Can't fault it too much for a, you know, a lowish cost 5 and 1/2 digit bench meter. Now, as for the processor board here, let's take a very quick look at it. There's not much

**Dave Jones:** on it, of course. Why they've got There's actually missing screw holes here. They've gone to the effort to put them in the PCB. I can actually see that there's threaded studs down in there in the case, but yeah, they haven't put the screws in.

**Dave Jones:** Why? Rather interesting that there's a populated flat flex connector here, which kind of sort of goes over to Well, I don't think it's to do with the digital connection over to the the isolate digital isolator connector over there, but I think it, you know, there

**Dave Jones:** are traces running back there, but what that thing's for, I got no idea. And we've got ourselves an ARM Cortex-A8 here. This is the Sitara processor from TI system-on-chip. It's got all the requisite stuff. It's got a, you know, a

**Dave Jones:** whiz-bang touchscreen graphics controller, all the rest of it, all the bells and whistles, all the, you know, the hard peripherals, the whole the whole shebang. So, yeah, no surprises, although I don't think we've seen a Sitara processor in another bit of test

**Dave Jones:** gear, so it's rather interesting. And then this coupled down here to this chip, which is upside down, so all the electrons are going to fall out. This is a DDR3 1 gigabit DRAM. So, yeah, it's got enough memory

**Dave Jones:** to run Linux or whatnot. And there's an unpopulated microSD card connector down there, so that'll allow them to do, you know, boot programming development, all sorts of, you know, weird and wonderful things. And I'm sure hackers can get in there

**Dave Jones:** and make use of that puppy, no worries. And there's not much else exciting going on around here, although we do have a five-pin single inline header up there. Could that be some sort of serial monitor interface, perhaps? I

**Dave Jones:** don't know, it's not labeled in any way. There you go, that's pretty much all she wrote inside this thing. So, you know, it's kind of built down to a price, but that's what it is. It's a cheapish, you

**Dave Jones:** know, five and a half digit multimeter with, you know, reasonable specs. And as we'll see in a minute when we power it up, um most of the functionality of the higher-priced Agilent units. So, let's check it out. And if we have a look with

**Dave Jones:** the Fluke, we can see inside there and you can uh see the transformer up there. It's about 35 degrees or thereabouts. Big hot spot there at about 50 I was getting 52 at uh 52 at one point. There we go, almost 53

**Dave Jones:** at one point. So, that's a linear regulator up there on the acquisition uh board. Can see the processor right down there. It's a little hot spot as you'd expect, you know, one of these um Cortex thingamajobs uh running Linux or whatever. They're

**Dave Jones:** they require a fair bit. And um there's a, you know, another that well, there's the heat sink, by the way. There's that uh large heat sink on the acquisition board, so there's nothing doing there. I'm By the way, I'm pointing towards I'm

**Dave Jones:** talking about what's in the crosshair here. This temperature up here is what's on the crosshair, and this is just the min max, by the way. Few people get confused by that. Uh oh, sorry about the glare there. That

**Dave Jones:** device down there, near the input sockets, that's actually the relay. That's an input switching relay and that's obviously energized. You can see because it's it's warming up. The only reason that would warm up is because the coil in there is actually energized. So,

**Dave Jones:** there you go. But apart from that, um it's not getting No, there's no thermal issues there at all. Check it out. If there is a more blatant rip-off, I haven't seen it. And look at it compared to the Agilent 34461A,

**Dave Jones:** which has been out for quite a long time now and it's a massively popular. It's like the benchmark 6 and 1/2 digit multimeter. It's practically the best bang for buck on the market. And of course, it is not

**Dave Jones:** a fair comparison. This thing is like $422 street price. This thing is like I think slightly over a thousand or the 60 is slightly under is like $900 or something like that. I'll stand corrected on that. But yeah, you know,

**Dave Jones:** it's like two and a half times the cost and 6 and 1/2 digit meter. It's got you know, a a much better voltage reference in there, much better design, much tightly, much higher controlled specs, everything else. So, really, you

**Dave Jones:** know, like not not a fair comparison at all. But look at the user interface. It is identical right down to the menu options. Look, number parameter. They even call it trend chart, which I think might even be a

**Dave Jones:** Agilent / Keysight. Sorry, still got the Agilent badge on there. Keysight It's a habit I can't get out of. I'm sorry. Jeez, I'm still getting over the change from HP to Agilent, let alone from Agilent to Keysight. Anyway,

**Dave Jones:** I believe trend chart is actually I think it might be a trademark of Keysight. And then they've got the histogram as well and even the stat menus it's exactly the same. Everything's in exactly the same position. But the Agilent the Keysight

**Dave Jones:** looks a hell of a lot better. The fonts are better. You know, it's it's a bigger display and you know, it just looks much more polished. But like come on. They didn't come about this by accident of course and you'll

**Dave Jones:** notice the key layout is almost exactly the same almost. The Keysight does actually have a capacitance function now it's they've actually added that as a firmware update which is quite nice. So but you know, they've mixed a few of the keys up

**Dave Jones:** around here but it's almost identical. Except of course the Agilent is a real bench multimeter and when I say real bench multimeter like as in a proper system bench multimeter. It's got the front and rear terminals. You can

**Dave Jones:** actually switch them whereas the Siglent of course is not you know, designed for proper system rack automation and stuff like that. So it's only got the terminals on the front which for a just a general purpose lab bench multimeter you'd never use the

**Dave Jones:** terminals on the back. So they go into waste on something like the Keysight here but the Siglent yeah, you know, nothing wrong with not having rear terminals. You really you know, if you building and automating a test system or

**Dave Jones:** something like that where you need a six and a half digit meter like this and automated and you can get rack kits for this so you know, it can mount in racks and stuff like that then you know,

**Dave Jones:** you're not going to be you know, cheaping out and buying the Siglent. You're going to go for the Agilent which has all the bells and whistles. It has the trust. It has the full support and cost really isn't an

**Dave Jones:** issue when you're you know, designing automated rack system and things like that. And if you go into trend chart here look you can see that it's the menu options, once again, identical. They've just copied it. Unbelievable. Well, you

**Dave Jones:** know, imitation is the sincerest form of flattery, is it not? So, anyway, I've got to avoid turning this thing into a review or whatever. So, yeah, it's just supposed to be a quick teardown. I always say quick and then it never is. I

**Dave Jones:** think I've got now been uh my counter on the uh camera here, 29 minutes worth of raw footage. So, that's going to edit down to you know, something over 20 minutes. So, maybe doing like 25 minutes or something. So, yeah, it's got a few

**Dave Jones:** build quality issues and things like that. But, uh you know, it is built down to a price. And 422 bucks probably isn't uh too bad if you're in the market for a uh you know, a feature-packed uh 5 and 1/2

**Dave Jones:** digit uh bench multimeter. And well, it you know, it's probably going to do the business. It's worth checking out anyway, you know. Don't buy it on spec. You know, you get you try and get your hands on one uh somewhere and you know,

**Dave Jones:** give it a demo and stuff like that and see if you actually like it. See if it suits your uh purposes and stuff like that. But, I will show you just one little feature here. It can actually measure voltage and current at the same

**Dave Jones:** time. I don't know if it can actually uh calculate power. But, you can see that on the It's got a dual display, tiny little uh secondary display down here. So, I'm displaying that current up on the main display. And then the second

**Dave Jones:** display, I'm actually displaying the voltage. And of course, you can do this using a common ground. So, you know, we've got a separate um a current terminal and a separate uh voltage input terminal. And you can hear it.

**Dave Jones:** Click. Click. About every second, it switches between voltage and current and then updates the display. So, it's not a simultaneous thing. It can't do that. But, it can actually physically switch between them. So, that could be handy. It's like I think I did a review of the

**Dave Jones:** ancient uh Fluke 45 multimeter from back in the '80s. and it could uh it it did exactly this. So, this thing could do it. That might come in handy. So, anyway, if you like the teardown video, please give it a big thumbs up. And I've

**Dave Jones:** done a lot of teardown videos recently and I've done a lot of Siglent. I've done three Siglent teardown videos recently. But, hey, I just happened upon these instruments. So, but there are people who love to see the teardown

**Dave Jones:** videos. So, if I've got the gear, I'm going to tear it down, you bet your bottom dollar. Anyway, hope you liked it. Catch you next time.
