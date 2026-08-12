---
video_id: 6nqSFYVKnP4
title: EEVblog #829 - Siglent SDM3055 Bench Multimeter Teardown
url: https://www.youtube.com/watch?v=6nqSFYVKnP4
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 23, "3": 38, "4": 52, "5": 64, "6": 82, "7": 100, "8": 110, "9": 125, "10": 136, "11": 151, "12": 159, "13": 174, "14": 187, "15": 195, "16": 214, "17": 223, "18": 233, "19": 242, "20": 257, "21": 283, "22": 292, "23": 309, "24": 317, "25": 337, "26": 348, "27": 370, "28": 381, "29": 391, "30": 407, "31": 418, "32": 426, "33": 442, "34": 466, "35": 480, "36": 495, "37": 504, "38": 516, "39": 530, "40": 540, "41": 554, "42": 568, "43": 577, "44": 596, "45": 615, "46": 626, "47": 639, "48": 652, "49": 664, "50": 676, "51": 693, "52": 712, "53": 727, "54": 736, "55": 747, "56": 757, "57": 766, "58": 781, "59": 795, "60": 804, "61": 818, "62": 835, "63": 848, "64": 859, "65": 876, "66": 888, "67": 902, "68": 916, "69": 933, "70": 951, "71": 962, "72": 972, "73": 986, "74": 1006, "75": 1016, "76": 1037, "77": 1048, "78": 1060, "79": 1070, "80": 1080, "81": 1100, "82": 1120, "83": 1133, "84": 1156, "85": 1166, "86": 1177, "87": 1191, "88": 1207, "89": 1221, "90": 1236, "91": 1251, "92": 1259, "93": 1273, "94": 1290, "95": 1304, "96": 1317, "97": 1331, "98": 1347, "99": 1362, "100": 1373, "101": 1388, "102": 1401, "103": 1418, "104": 1434, "105": 1445, "106": 1461, "107": 1479, "108": 1492, "109": 1506, "110": 1516, "111": 1525, "112": 1537, "113": 1551, "114": 1560, "115": 1569, "116": 1579, "117": 1590, "118": 1603, "119": 1611, "120": 1619, "121": 1629, "122": 1638}
---

**Dave Jones:** Hi, welcome to another Siglent teardown. This time we've got the Siglent multimeter. We haven't had a Siglent multimeter before. This is the STM3055 bench multimeter. Specifically, this is the 3055A model.

**Dave Jones:** And I believe the only difference between the A model that I've got here and the three and the much cheaper 3055 is that this one has a GPIB option and that's it.

**Dave Jones:** Now, street price of this thing for the A model that I've got here, it's about 630 odd uh US dollars. Now, that's pretty pricey. So, I wouldn't be getting the GPIB version of this unless you absolutely must have the GPIB option.

**Dave Jones:** You're much better off going for just the 3055A and its street price is currently uh 422 bucks on special. I was able to uh find this thing for US dollars, different in other countries and different currencies, of course.

**Dave Jones:** But, uh this is a five and a half digit uh meter. It's a 240,000 counts. So, it's not like 600,000 count or anything like that. So, 20 240,000 count, little bit unusual.

**Dave Jones:** Um a 0.015% uh DC basic uh accuracy class instrument. So, its specs aren't really going to set the world on fire. 150 uh samples per second, which is kind of sort of, you know, not too bad for a bench multimeter, but it's not like the higher end ones, for example.

**Dave Jones:** So, it sits in this sort of, you know, almost no man's land between like the, you know, the high end Agilent uh bench multimeters for just under or just over a thousand dollars and uh you know, a decent high end uh handheld multimeter, for example, which you can get five and a half digit multimeters.

**Dave Jones:** You don't have to go to a bench multimeter like this to actually get uh five and a half digits, but a lot of people prefer uh the bench meters cuz they sit on the bench, they're always there.

**Dave Jones:** They've got a nice big graphical display on the thing and this thing's got uh trend pot plotting, everything else. Very similar functionality uh to the Agilent uh bench meter that we've seen before, and I'll show you a comparison at the end cuz it's absolutely hilarious.

**Dave Jones:** But, of course, the downsides of bench multimeters, they are tied to the bench, and generally they're not going to have the same sort of input protection as a handheld multimeter cuz they're not designed to be used in the field.

**Dave Jones:** Hence, we're only looking at um CAT II 600 V and CAT 1000 V rating. That's very typical of a bench uh multimeters. But, of course, one of the other advantages of a bench multimeter, you typically get, and of course you do get in here, the uh four-wire measurement.

**Dave Jones:** So, you can do four-wire ohms. So, I've got the two extra uh sense terminals here. Very nice. Anyway, we'll power this puppy up at the end. Let's have a look at it.

**Dave Jones:** It feels like looks and feels like a reasonable quality uh bench meter. You know, the no problem with the buttons there. Uh banana plugs look half reasonable. And it's a nice little um it's not too deep.

**Dave Jones:** It is quite um uh shallow in that respect. So, it doesn't take up too much uh bench depth. Uh selectable 110 or 240 V operations. So, there's no worries about buying it in a particular country.

**Dave Jones:** It's now it's got uh LAN built in and uh USB uh host as well. It's got uh external uh trigger cuz you can sort of, you know, use these for a bit of automation.

**Dave Jones:** And it's got an extension card option. Now, like that must be I'm uh presuming the GPIB option, but this is the A model. And according to the um according to the data sheet and websites I've looked at, the A model is supposed to have GPIB.

**Dave Jones:** That's why you pay extra for the A, but there's nothing there. So, this one might be an oddball one. This is, you know, like got this directly from Siglent.

**Dave Jones:** Like it's a I think it's a demo unit or something. So, I'm not exactly sure what's going on there. Anyway, there's our 10 amp fuse on the back. So, let's take this puppy apart and uh have a look.

**Dave Jones:** All the volt nuts, of course, want to know what references in there. Is it going to be a you know, your old school? They've got some thread lock on there.

**Dave Jones:** That's nice. Um is it going to be your old school uh LM 3 Oh, cow sticker. Dolt. This bastard, who cares? Um is it going to be your old school LM 399 or is it going to be something different?

**Dave Jones:** All right, let's pop the hood on this and see what we've got. Oh, we're in like Flynn. We can see old school looking transformer in that thing. Wow. So, it looks like we've got just a linear power supply and the voltage tap is just a different tap on the transformer there, but like I don't have to go any further.

**Dave Jones:** It's all exposed. Right there, ready for us. Let's take a look. Oh, yeah, look at that. There's the trademark Siglent rust. I'm sure they do have a trademark on that.

**Dave Jones:** No worries whatsoever. Yep, rust a plenty. And that's the thing, the first thing you notice about this is just like the cheap quality and feel of the metal work and the rust just you know, adds It's just the icing on the cake there.

**Dave Jones:** We've got a little cheap ass fan in here and what's it doing? It's you know, we've got some vents here on the other side, but it's blocked by the transformer.

**Dave Jones:** You know, mate and through here and uh it's just like do they even need a fan on something like this? I you know, jeez, I don't know. Anyway, yeah, it just feels just looks and feels pretty cheap and just kind of like, you know, slapped together.

**Dave Jones:** I'm not going to say amateur, but it it's just not a high quality bit of kit. If you put the I know it's not the same price bracket as the Agilent, but if you put the two side by side, it's chalk and cheese.

**Dave Jones:** At least they have gone to the effort to actually the ribbon cable going over here, going over to the front panel. At least they've gone to the effort to put in this insulating shield on here, but why they had to run it on on that side and why they just couldn't, you know, you know, the system designers couldn't actually move the connector over to the low voltage side here.

**Dave Jones:** I don't, you know, like I don't know. It's it's almost as if, you know, bit of an afterthought. Oh, we have to put the connector over here. Oh, well, we'll just punch a hole in here, run it over.

**Dave Jones:** We'll just put some insulating stuff on here and, you know, like it just seems a bit cludgy. And then our earth connection here is just a little bit of a It's not loosey-goosey, but it's not tied either.

**Dave Jones:** It's just a a spade lug, you know, like give me a proper, you know, shake-proof washer and everything. I I don't like that. And at least they have bent the metal work over there so there's no sharp edges on that cable gland there.

**Dave Jones:** So, that's all right. And it's just funny. They've got like the fan cut out here. It's like, "Oh, we weren't sure whether or not we'll put the fan here or over there." It's just, you know, a little lack of systems engineering.

**Dave Jones:** And as I said, we've got a linear power supply here. It doesn't need much power, so hence why you know, couldn't they have got away without using a fan?

**Dave Jones:** It'd be interesting put the uh thermal camera on this thing later, but anyway, small little up PCB mount heat sink. It's not flapping around in the breeze. It's actually one of the proper stud ones that are soldered onto the board, so nice.

**Dave Jones:** They've got Lelon brand caps, so, you know, yawn. They've got separate taps, of course. This This is the digital processing board, which we'll take a look at. It's got its own AC transformer tap electrically isolated from the input and acquisition side of things, so it's got its own little full wave bridge rectifier down there.

**Dave Jones:** It's got another Leel on cap. That's probably like a, you know, a 3.3 V. That looks like a switching supply over there to generate all the, you know, probably 1.2 V, 1.8 V, or whatever is required for the processor down here.

**Dave Jones:** So, that's all That's all hunky-dory, but yeah, once again, looks like we've got a couple of taps here. We've got a couple of two possibly two full wave bridge rectifiers there, and hence the two different caps.

**Dave Jones:** And then we've got our digital isolation between the processor board and the acquisition board here. That's this little flat flex ribbon cable. There's a We might actually take a look.

**Dave Jones:** That's one of those analog devices puppies, so that's an opto isolator. Got another opto isolator there. You'll notice that the big cutout there on the board. You can see cutout of the ground plane and everything else.

**Dave Jones:** So, they've got it nicely isolated. All hunky-dory. And there's our front end side of things. We'll take a closer look, but the first thing I notice, of course, is the uh thin film resistor network here from Caddock.

**Dave Jones:** They're one of the top makers. So, they're not unlike, you know, Fluke and Agilent who who roll their own ones, of course. So, they get Caddock to make it.

**Dave Jones:** So, no worries there at all. That's top notch. Then we've got some Looks like we've got ourselves a high voltage resistor network here. They're, you know, they they They're not They're not using those for their power dissipation, those large case resistors.

**Dave Jones:** They're using those for large voltage strings. So, that's a high voltage string. That's why they got them all in series. They're not that big for power dissipation reasons. And um you can see that they've got the gold trace going around there.

**Dave Jones:** That's our guard trace for leakage, so that's all right. Can see a couple of more guard traces down in here. I might get the macro lens and take a look at.

**Dave Jones:** And this high voltage string here, actually, if you follow the wires, follow the money, it goes up here, goes up here, goes up here. They're our sense terminals. They're our positive and negative sense terminals, so they're our positive and negative sense resistor chains like that.

**Dave Jones:** So, they're doing that, of course, for high voltage overload overload protection because, you know, people could accidentally mix up those connectors on the front, and they do. So, yeah, you've got to protect about against some idiot plugging, you know, 240 V mains into the sense terminals.

**Dave Jones:** But check it out, we have ourselves a genuine budge. Look at this. They have this big power resistor, which is, according to the footprint down there, is supposed to be a surface mount jobby.

**Dave Jones:** And they've got that flying lead coming over to this PTC. I mean, that's just horrible. There's no excuse for that in a bit of production gear like this. There's just, yeah, absolutely no excuse.

**Dave Jones:** Geez. I mean, come on. And this is rather unusual. Look at that. That looks like a ceramic resistor network. It almost looks like like it's a BGA package or or something like that.

**Dave Jones:** And there's like almost like a dip alternative part. That is that is bizarre. What on earth are they doing there? Anyway, the input protection is not too shabby here.

**Dave Jones:** This red wire is coming from our input banana plug. Then we've got a couple of gas discharge two tubes here. Couple of big beefy looking mobs. No worries whatsoever.

**Dave Jones:** And then we've got a nice looking big ass relay, but I'm not entirely sure what they're what they're switching there. Hmm. And they've got very beefy diode bridge protection there, which I've done a video on input protection arrangements and things like that.

**Dave Jones:** You'll typically find a diode bridge for clamping protection and oh yeah, that's a that's a decent beast and there are current sense resistors right down in there because our white our white cable coming over here is our current input and it goes off to these two cables.

**Dave Jones:** That goes off to the 10 amp fuse connector on the back. So I'm not sure why they're running this they've got a ceramic fuse in there, a little M205, but I don't you know, which is encapsulated, very nice.

**Dave Jones:** But yeah, why they've got that secondary fuse in there cuz this doesn't have a low current range. It's only got one single 10 amp current input and that's it.

**Dave Jones:** So yeah, I'm not sure why they ran the current input, that's a white wire there onto the board. They soldered that directly in. They got then they got some spade lugs coming over here to the fuse.

**Dave Jones:** Why not just run that you know, if you're going to fuse it on the back here, why not just run that fuse wire straight over to here and then just have a single wire running back.

**Dave Jones:** I don't get it. And I wonder what's under the shielded can. Is that the It it seems too near to the input here to to be like the voltage reference.

**Dave Jones:** So I reckon that's probably like the AC stuff, the possibly the true RMS converter. So we'll pop the hood on there. It looks like there's a screw accessed from the other side, but yeah, I can't traditional LM399 on here.

**Dave Jones:** It's not You probably don't wouldn't expect to find an LM399 class voltage reference in a instrument of you know, five and a half digit meter of this class. But yeah, we'll find that eventually, but let's pop the hood on that.

**Dave Jones:** It's near the front end. And I was right, but I was always going to be right because just based on its location and the functionality, that's what it had to be.

**Dave Jones:** No surprises for finding the venerable AD5632 RMS converter. So, that's just doing the AC range stuff. Bit of a kludge with the two resistors there. They've actually got those soldered together at the same point.

**Dave Jones:** Like And there, folks, is the money shot. There's our ADC. It's an Analog Devices AD7190, 24-bit delta-sigma converter, 4.8 kHz conversion rate, four channels. It's got built-in programmable again amplifier.

**Dave Jones:** Yeah, yeah, yeah, yeah. Fairly typical of what you'd expect to find in a 5 and 1/2 digit multimeter. Of course, unlike like Fluke and Keysight, they haven't like rolled their own, you know, dual slope converter and stuff like that.

**Dave Jones:** Just used an off-the-shelf delta-sigma. Good enough for a 5 and 1/2 digit meter, no worries whatsoever. And there's our voltage reference right next to it. It's the MAX6325, uh the CSA version.

**Dave Jones:** It's, you know, a reasonably schmick reference. It's a 0.5 ppm initial accuracy of 0.02%, but of course that doesn't matter a rat's ass. It's all about the temperature drift because this thing's got a nominal DC spec of 0.015%.

**Dave Jones:** So, actually better than this chip's initial spec. And that's possible because they calibrate these things and they adjust them. They program into them the calibration offsets at the factory.

**Dave Jones:** But of course the 0.5 ppm is only short-term drift. Long-term drift, spec sheet says about 30 ppm per 1,000 hours. So, you know, it's not going to set the world on fire, but hey, it's a 5 and 1/2 digit meter.

**Dave Jones:** So, it's good enough. Haven't gone through the calculations and all that really deep into the data sheet. I'll leave that up to the volt nuts to decide whether or not that's a suitable reference for the claimed specs and everything else and how it compares.

**Dave Jones:** I'm sure there's no shortage of people who will be uh willing to uh compare this to various other meters on the market. But once again, it's probably not fair to compare it to and you know, a Keysight or a Fluke that costs, you know, twice as much or more than this thing, three times more in uh some cases.

**Dave Jones:** So, yeah, you know, it it's good enough for the job, I guess. And there's a couple of these in here. These Analog Devices AD uh 8629. These are uh fairly schmic uh chopper amplifiers, a zero drift chopper amps like I use in my uh microcurrent.

**Dave Jones:** Tell you what, I must say, I'm not blown away by the uh soldering quality in this thing. I mean, it's not bad, but um yeah, you know, this lead-free rubbish.

**Dave Jones:** Mhm. But yeah, it's not the best. It's just a little bit sloppy. Little bit sloppy. Look, you know, excess paste on uh on that. Where is it? Where's my pointer?

**Dave Jones:** Sorry, can't get my pointer in. Excess paste on that cap and you know, like mhm. And as I showed you before, the uh guard traces, they they're those gold uh traces there have the solder mask removed.

**Dave Jones:** They're actually uh providing uh leakage and uh contaminant protection between uh critical traces. So, I guess they're not. They're doing there those ADG uh chips are a dead giveaway where as soon as you see um the ADG uh prefix like that, you know, they're um you know, some form of uh analog switch.

**Dave Jones:** And there are our current shunt resistors for you current shunt resistor fanboys. I know you're down there. You can see the uh serpentine trace on the one on the uh left there.

**Dave Jones:** And no surprises for finding just a little uh FPGA in there. That's a Lattice uh MachXO part. Really cheap, really uh not high density at all. It's just it would just be doing the uh sample uh you know, handling the sampling, the 150 uh samples per second, probably buffering that, and just feeding that across the digital interface.

**Dave Jones:** You can see that that's hooked up uh directly to the digital IO. So, yeah, it's just handling the sampling subsystem. And that's pretty much all she wrote on the analog front end.

**Dave Jones:** You know, it's it's got all the requisite stuff. Probably, you know, it does the job, does the business. Can't fault it too much for a, you know, a lowish cost 5 and 1/2 digit bench meter.

**Dave Jones:** Now, as for the processor board here, let's take a very quick look at it. There's not much on it, of course. Why they've got There's actually missing screw holes here.

**Dave Jones:** They've gone to the effort to put them in the PCB. I can actually see that there's threaded studs down in there in the case, but yeah, they haven't put the screws in.

**Dave Jones:** Why? Rather interesting that there's a populated flat flex connector here, which kind of sort of goes over to Well, I don't think it's to do with the digital connection over to the the isolate digital isolator connector over there, but I think it, you know, there are traces running back there, but what that thing's for, I got no idea.

**Dave Jones:** And we've got ourselves an ARM Cortex-A8 here. This is the Sitara processor from TI system-on-chip. It's got all the requisite stuff. It's got a, you know, a whiz-bang touchscreen graphics controller, all the rest of it, all the bells and whistles, all the, you know, the hard peripherals, the whole the whole shebang.

**Dave Jones:** So, yeah, no surprises, although I don't think we've seen a Sitara processor in another bit of test gear, so it's rather interesting. And then this coupled down here to this chip, which is upside down, so all the electrons are going to fall out.

**Dave Jones:** This is a DDR3 1 gigabit DRAM. So, yeah, it's got enough memory to run Linux or whatnot. And there's an unpopulated microSD card connector down there, so that'll allow them to do, you know, boot programming development, all sorts of, you know, weird and wonderful things.

**Dave Jones:** And I'm sure hackers can get in there and make use of that puppy, no worries. And there's not much else exciting going on around here, although we do have a five-pin single inline header up there.

**Dave Jones:** Could that be some sort of serial monitor interface, perhaps? I don't know, it's not labeled in any way. There you go, that's pretty much all she wrote inside this thing.

**Dave Jones:** So, you know, it's kind of built down to a price, but that's what it is. It's a cheapish, you know, five and a half digit multimeter with, you know, reasonable specs.

**Dave Jones:** And as we'll see in a minute when we power it up, um most of the functionality of the higher-priced Agilent units. So, let's check it out. And if we have a look with the Fluke, we can see inside there and you can uh see the transformer up there.

**Dave Jones:** It's about 35 degrees or thereabouts. Big hot spot there at about 50 I was getting 52 at uh 52 at one point. There we go, almost 53 at one point.

**Dave Jones:** So, that's a linear regulator up there on the acquisition uh board. Can see the processor right down there. It's a little hot spot as you'd expect, you know, one of these um Cortex thingamajobs uh running Linux or whatever.

**Dave Jones:** They're they require a fair bit. And um there's a, you know, another that well, there's the heat sink, by the way. There's that uh large heat sink on the acquisition board, so there's nothing doing there.

**Dave Jones:** I'm By the way, I'm pointing towards I'm talking about what's in the crosshair here. This temperature up here is what's on the crosshair, and this is just the min max, by the way.

**Dave Jones:** Few people get confused by that. Uh oh, sorry about the glare there. That device down there, near the input sockets, that's actually the relay. That's an input switching relay and that's obviously energized.

**Dave Jones:** You can see because it's it's warming up. The only reason that would warm up is because the coil in there is actually energized. So, there you go. But apart from that, um it's not getting No, there's no thermal issues there at all.

**Dave Jones:** Check it out. If there is a more blatant rip-off, I haven't seen it. And look at it compared to the Agilent 34461A, which has been out for quite a long time now and it's a massively popular.

**Dave Jones:** It's like the benchmark 6 and 1/2 digit multimeter. It's practically the best bang for buck on the market. And of course, it is not a fair comparison. This thing is like $422 street price.

**Dave Jones:** This thing is like I think slightly over a thousand or the 60 is slightly under is like $900 or something like that. I'll stand corrected on that. But yeah, you know, it's like two and a half times the cost and 6 and 1/2 digit meter.

**Dave Jones:** It's got you know, a a much better voltage reference in there, much better design, much tightly, much higher controlled specs, everything else. So, really, you know, like not not a fair comparison at all.

**Dave Jones:** But look at the user interface. It is identical right down to the menu options. Look, number parameter. They even call it trend chart, which I think might even be a Agilent / Keysight.

**Dave Jones:** Sorry, still got the Agilent badge on there. Keysight It's a habit I can't get out of. I'm sorry. Jeez, I'm still getting over the change from HP to Agilent, let alone from Agilent to Keysight.

**Dave Jones:** Anyway, I believe trend chart is actually I think it might be a trademark of Keysight. And then they've got the histogram as well and even the stat menus it's exactly the same.

**Dave Jones:** Everything's in exactly the same position. But the Agilent the Keysight looks a hell of a lot better. The fonts are better. You know, it's it's a bigger display and you know, it just looks much more polished.

**Dave Jones:** But like come on. They didn't come about this by accident of course and you'll notice the key layout is almost exactly the same almost. The Keysight does actually have a capacitance function now it's they've actually added that as a firmware update which is quite nice.

**Dave Jones:** So but you know, they've mixed a few of the keys up around here but it's almost identical. Except of course the Agilent is a real bench multimeter and when I say real bench multimeter like as in a proper system bench multimeter.

**Dave Jones:** It's got the front and rear terminals. You can actually switch them whereas the Siglent of course is not you know, designed for proper system rack automation and stuff like that.

**Dave Jones:** So it's only got the terminals on the front which for a just a general purpose lab bench multimeter you'd never use the terminals on the back. So they go into waste on something like the Keysight here but the Siglent yeah, you know, nothing wrong with not having rear terminals.

**Dave Jones:** You really you know, if you building and automating a test system or something like that where you need a six and a half digit meter like this and automated and you can get rack kits for this so you know, it can mount in racks and stuff like that then you know, you're not going to be you know, cheaping out and buying the Siglent.

**Dave Jones:** You're going to go for the Agilent which has all the bells and whistles. It has the trust. It has the full support and cost really isn't an issue when you're you know, designing automated rack system and things like that.

**Dave Jones:** And if you go into trend chart here look you can see that it's the menu options, once again, identical. They've just copied it. Unbelievable. Well, you know, imitation is the sincerest form of flattery, is it not?

**Dave Jones:** So, anyway, I've got to avoid turning this thing into a review or whatever. So, yeah, it's just supposed to be a quick teardown. I always say quick and then it never is.

**Dave Jones:** I think I've got now been uh my counter on the uh camera here, 29 minutes worth of raw footage. So, that's going to edit down to you know, something over 20 minutes.

**Dave Jones:** So, maybe doing like 25 minutes or something. So, yeah, it's got a few build quality issues and things like that. But, uh you know, it is built down to a price.

**Dave Jones:** And 422 bucks probably isn't uh too bad if you're in the market for a uh you know, a feature-packed uh 5 and 1/2 digit uh bench multimeter. And well, it you know, it's probably going to do the business.

**Dave Jones:** It's worth checking out anyway, you know. Don't buy it on spec. You know, you get you try and get your hands on one uh somewhere and you know, give it a demo and stuff like that and see if you actually like it.

**Dave Jones:** See if it suits your uh purposes and stuff like that. But, I will show you just one little feature here. It can actually measure voltage and current at the same time.

**Dave Jones:** I don't know if it can actually uh calculate power. But, you can see that on the It's got a dual display, tiny little uh secondary display down here. So, I'm displaying that current up on the main display.

**Dave Jones:** And then the second display, I'm actually displaying the voltage. And of course, you can do this using a common ground. So, you know, we've got a separate um a current terminal and a separate uh voltage input terminal.

**Dave Jones:** And you can hear it. Click. Click. About every second, it switches between voltage and current and then updates the display. So, it's not a simultaneous thing. It can't do that.

**Dave Jones:** But, it can actually physically switch between them. So, that could be handy. It's like I think I did a review of the ancient uh Fluke 45 multimeter from back in the '80s.

**Dave Jones:** and it could uh it it did exactly this. So, this thing could do it. That might come in handy. So, anyway, if you like the teardown video, please give it a big thumbs up.

**Dave Jones:** And I've done a lot of teardown videos recently and I've done a lot of Siglent. I've done three Siglent teardown videos recently. But, hey, I just happened upon these instruments.

**Dave Jones:** So, but there are people who love to see the teardown videos. So, if I've got the gear, I'm going to tear it down, you bet your bottom dollar. Anyway, hope you liked it.

**Dave Jones:** Catch you next time.
