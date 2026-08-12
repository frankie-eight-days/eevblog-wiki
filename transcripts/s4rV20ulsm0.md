---
video_id: s4rV20ulsm0
title: EEVblog #511 - Rigol DP832 Power Supply Teardown
url: https://www.youtube.com/watch?v=s4rV20ulsm0
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 33, "3": 47, "4": 59, "5": 73, "6": 88, "7": 108, "8": 128, "9": 140, "10": 156, "11": 179, "12": 192, "13": 203, "14": 219, "15": 243, "16": 259, "17": 272, "18": 284, "19": 303, "20": 316, "21": 329, "22": 344, "23": 363, "24": 375, "25": 388, "26": 407, "27": 414, "28": 433, "29": 460, "30": 481, "31": 494, "32": 515, "33": 527, "34": 541, "35": 553, "36": 562, "37": 575, "38": 601, "39": 615, "40": 633, "41": 645, "42": 661, "43": 672, "44": 683, "45": 702, "46": 714, "47": 725, "48": 734, "49": 750, "50": 758, "51": 775, "52": 785, "53": 805, "54": 816, "55": 829, "56": 838, "57": 854, "58": 872, "59": 884, "60": 905, "61": 917, "62": 945, "63": 960, "64": 976, "65": 1001, "66": 1016, "67": 1034, "68": 1045, "69": 1054, "70": 1065, "71": 1081, "72": 1091, "73": 1103, "74": 1115, "75": 1128, "76": 1141, "77": 1153, "78": 1178, "79": 1197, "80": 1220, "81": 1237, "82": 1251, "83": 1267, "84": 1277, "85": 1295, "86": 1305, "87": 1321, "88": 1335, "89": 1354, "90": 1365, "91": 1376, "92": 1400, "93": 1411, "94": 1426, "95": 1434, "96": 1443, "97": 1455, "98": 1472, "99": 1483, "100": 1500, "101": 1523, "102": 1533, "103": 1547, "104": 1562, "105": 1574, "106": 1587}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We're going to take a look at the Rigol DP832 power supply because a lot of people asked for it. So, we'll just do a teardown pretty quickly to see what makes this thing tick.

**Dave Jones:** Now, the interesting thing about this, of course, is that it is a software upgradeable power supply. So, that means that uh of course, the hardware in this could be identical to the 832A, which of course has all the options in the back plus the uh color screen.

**Dave Jones:** I mean, this one has a color screen, but it's just uh software limited to monochrome and uh stuff like that. So, this should be interesting and I think we will find that the hardware in this is identical to the 832A model.

**Dave Jones:** But, we won't find out for absolute sure until we open it up. Now, there was a report on the EVBlog forum about somebody found a bit of rust inside their unit.

**Dave Jones:** So, we'll see if that's the same case here. I rust on the chassis, I would uh presume so. We're going to whip whip this apart and it doesn't look like I need to take these rubber feet off here.

**Dave Jones:** It looks like it's just going to slide off. And it looks like my warranty void if uh broken sticker is already a bit broken due to the fact that, you know, the chassis does uh bend a little bit of give on the bottom like that and it uh has almost peeled off.

**Dave Jones:** Ah, well. We can fix that. Ta-da! Now, it's completely gone. It turns out that we do have to take off the side handle here cuz that's the uh the two main screws, actually the only two screws actually holding this case on apart from the uh rubber feet at the back, which weren't directly connecting the chassis in.

**Dave Jones:** But, anyway, um so, what we expect to find in this is a basic uh you You a fairly not a high-end processor. Of course, there'll be, you know, a huge, whopping big, uh, transformer in this, uh, sucker, big linear transformer, plus, um, some basic, uh, processing handle all the user interface and the networking and all that.

**Dave Jones:** Enough to, you know, it's going to have to be powerful enough to, uh, run a little OS in there and and do all the, uh, networking and and, you know, file, uh, stuff and handle the display and all that.

**Dave Jones:** Um, plus, there'll be some, um, you know, fairly precise precision this is a 0.05% class precision, uh, power supply. And, uh, really, um, not, you know, probably on a couple of boards, and not a huge amount of, uh, extra stuff.

**Dave Jones:** So, let's Woah, got a big toroid. Check this out. Tada! There we go. We're in like Flynn. And that's it. Looks like it's shielded on top. I'm rather, uh, rather surprised at that.

**Dave Jones:** You don't often, uh, yeah, it looks like there's a board on top as well. So, looks like the power supply board on top. Anyway, we'll open the sucker up, and, uh, but check out that big That's where most of your weight is, in that huge toroid.

**Dave Jones:** And I'm very impressed with the huge toroid transformer in this thing. And of course, a toroid transformer is going to be the duck's guts in something like this. It really is.

**Dave Jones:** And you're probably paying a bit of a, uh, price premium to get that, uh, toroidal transformer in there over your traditional laminated, uh, transformer. Now, there are several advantages to a toroidal transformer like this over your more traditional laminated, uh, core transformer.

**Dave Jones:** One of the biggest is that you get an increase in efficiency in, uh, terms of size and weight for a given power for these toroidal transformers. They're just much more efficient due to the fact that they don't have all those separate laminated uh, layers you get better flux efficiency inside the thing and that leads to a reduction in size and weight for a given power of that transformer.

**Dave Jones:** So this is what 195 watt power supply or something like that. In theory this toroidal transformer should be smaller and lighter than an equivalent required one in terms of efficiency for this particular wattage power supply.

**Dave Jones:** Now the second advantage is that stray magnetic fields in this thing because there effectively is no air gap inside this thing that's just a one large toroidal core like that that the wires are actually wound around inside that.

**Dave Jones:** No air gaps means less much less stray magnetic fields for these things and that's why they're used in audio, you know, really high-end audio gear and stuff like that.

**Dave Jones:** Just much nicer design than your traditional laminated core type. So huge thumbs up and it's also mounted on the little stamped out feet from the chassis here with looks like what looks like a captive nuts actually built in to the chassis down in there.

**Dave Jones:** So that really is quite neat and it does look like there are some shake proof washers down in there as well. Now I can potentially see why somebody may have complained about rust on their particular unit.

**Dave Jones:** It's a very similar folded sheet metal type thing with the riveted together that we saw in that Siglent unit but at first glance I can't see any real rust on my unit at all.

**Dave Jones:** Not even close to the Siglent unit. Hang on a sec. That I did find a little bit of rust on the back top end of this thing but once again nothing like the Siglent unit really.

**Dave Jones:** I mean, yeah, it's there. So, yes, okay, technically this unit has some rust, but the like the cutout in the back chassis, I guess we'll find out more when we get into this thing, but it just seems to have a much higher build quality than what what we saw in the Siglent.

**Dave Jones:** Even if there is a little bit of end rust there from where they've obviously lasered or you know, sheared off um that particular uh part of the metal work.

**Dave Jones:** You know, I do rather like this uh top board modular construction here. If we whip that out, hey, we've got some heat sinks. It looks like we've got Yeah, hang on.

**Dave Jones:** That just flipped out uh rather nicely there. I'm quite quite pleased with that. We're going to have to undo all the all the all the board uh interconnects and all the wiring harnesses to get that board out to have a uh proper look at it, but the board quality looks to be first class as you'd expect.

**Dave Jones:** And we'll have a brief look at the top board here cuz the top board is uh slightly different to the bottom board. The bottom board's got two channels as we'll see.

**Dave Jones:** The top board only has one channel uh essentially. So, the interesting thing is is that there's no processing uh stuff on this board at all. It's all your analog uh power supply stuff all in the center here, which and you can see the isolated path around the board here, which goes through here like this.

**Dave Jones:** And then we've got a couple of optocouplers down here for some just some uh serial data going across there. And of course, all of our output uh grounds on all of our comms stuff, our Ethernet, our USB, and our uh logic uh outputs, for example, and our RS232 are all of course electrically isolated from the output of the supplies, and they've got their own little power supply

**Dave Jones:** circuitry up here powered from a couple of little uh taps on the transformer up there, and then we've got our ribbon cable going off to our front panel uh board in here, which obviously contains all of the uh all of the processing for this thing, and they're just feeding that data for the Ethernet and the USB and everything else straight down to here.

**Dave Jones:** And any mystery to do with is this different hardware with the A model? Well, that's pretty much solved. There it is, DP832A. They've got this on both of the boards silkscreened on, and also the sticker as well.

**Dave Jones:** So, this is definitely um an 832A unit, and the 832 is just software crippled. That's it. So, even their uh assembly sticker there tells you it's an 832A. And if we have a look at the analog part of the main power supply board here, we can see that we have no less than four chips laser-marked off.

**Dave Jones:** This one over here, this one uh this one down here, and that one in there. Bastards! Why? It's not going to take anyone a huge amount of time to reverse engineer this.

**Dave Jones:** You've got to be kidding me. And there's our main little what looks like a processor or something like that, perhaps. Obviously, it's uh right next to a little in-circuit you know, an 8-pin in-circuit programming header there.

**Dave Jones:** Laser the thing off. You can almost see a few of the uh start letters there. Anyone want to have a guess? And that's coupled down here to another 8-pin SO package completely marked off there.

**Dave Jones:** It's got guard trace all the way around here. Look at that. So, you can actually um you know, see that's obviously, you know, not just like an I²C chip or something like that.

**Dave Jones:** It is some analog signal there that they're trying to guard against. And you'll notice that here, what looks like our voltage reference, I'm not going to try and uh you know, decode one of these SMD marks.

**Dave Jones:** They're a pain in the ass on that SO-23, but why have they routed out that little slot around there? Well, that is to isolate that device from any thermal stress on the board, cuz when this board warms up, which you'd expect to do and what would happen inside a power supply, for example, then it doesn't apply stress to the leads as the PCB material stretches just a little tiny little bit,

**Dave Jones:** half a bee's dick, but that might be enough to induce stresses into the lead of that voltage reference package there. So, that's a very common technique, just route out around like that and you get away from all the thermal stress issues.

**Dave Jones:** And we've got some retro action here, 74HC4051, fantastic, and TL074 quad op-amp. Beautiful. Couple that into a TL072, dual version of that same device, and we've got another SO8 laser marked off, and another one up here as well.

**Dave Jones:** So, whether or not they're those three SO8 chips all identical, I don't know, but, you know, it looks like it's just an it looks like it's a bloody op-amp or something like that.

**Dave Jones:** I mean, god, who cares? And to complete the retro rollout, LM393. Woohoo! More of that action down the bottom side here of the board, and we've got ourselves a free-standing LM317 there.

**Dave Jones:** You know I'm not always keen on those uh free-standing packages like that. We've got ourselves a transistor in there. Sorry, I can't make out the markings, it's really incredibly dark in there.

**Dave Jones:** And that's got its own little tiny, teeny, weeny piss-ant free-standing heat sink, but the big heat sink here has one pass transistor on it. I'll try and get the code off that, but once again, quite dark in there.

**Dave Jones:** And that's a SEP 80N15 N-channel MOSFET, of course, no surprises, 150 V 76 A nominal rating. So, pretty much what you'd expect in there. And the other one on the smaller heat sink by the way is a old school retro BD136.

**Dave Jones:** And there's our current shunt resistor, 20 m by the looks of it. 1% but once again, absolute accuracy of this thing can doesn't really matter. It's all about the temp co and how you trim this thing out in the software.

**Dave Jones:** So, 1% is certainly adequate there if you're going to software trim. No idea of the brand but there you go, SMT COA04. And no shortage of protection on this thing.

**Dave Jones:** This board has four MOVs on it and these two are associated with the main output rail there. And then our transformer tap there is protected by a 5 amp axial PCB mount fuse.

**Dave Jones:** And we've got no shortage of protection. There's three other PCB mount fuses on there as well. Very nice. And all the caps in this thing, both the small and large ones, are all exclusively Samyoung brand.

**Dave Jones:** Now, they're actually a Korean brand. Of course, they're not one of the top tier ones, that's for sure but I don't think they're bottom of the range. They are all 105° C rated.

**Dave Jones:** So, meh. And the main 2200 mic caps there look like to be the TDA series. Once again, we've got a bit of edge rust on there but that's all it seems to be limited to is just some of the edges that have been lasered off.

**Dave Jones:** We've got ourselves a heat sink with two large bridge rectifiers in there. There's one down there on the other side. And down in there you can see two Cosmo 3021 triac drivers there.

**Dave Jones:** So, obviously, I can't get a look at those devices U17 U21 down in there but they're obviously a pair of triacs. They've gone to the effort to selastic down these two smaller caps here but they didn't bother with the larger ones.

**Dave Jones:** Now, I'm debating whether or not it's even worthwhile trying to extract this bottom board down here cuz it's clearly two not identical, but you know, fairly operationally identical channels here.

**Dave Jones:** You know, similar arrangement here. You can see the triacs over there with the triac drivers. You can see the main caps down here. You can see the output. Once again, all those MOVs protecting the output there.

**Dave Jones:** Look, huge number of them. We've got our mains input here which will take another look at, but we've got a tiny little separate heatsink down in here with our bridge rectifier.

**Dave Jones:** And well, it's pretty much you know, identical to what we just looked at. Yes, we've got our chip. There it is. It's ground off down in there. You probably can't see it, but right down in there, there's the little in-circuit serial JTAG header right next to the thing.

**Dave Jones:** And really, you know, eh, not much else except look at that, they haven't left it loosey-goosey. They've actually bolted that TO-220 down to the board. Eh, they didn't do that on the other one.

**Dave Jones:** Just couldn't be bothered. And they've knocked some EMI on the head there with that little ferrite clamp around the output leads. And in terms of packing density in this thing, it's pretty darn good.

**Dave Jones:** I mean, with the board on top that that flips over with the heatsink going down, there's not a huge amount of room between those heatsinks. And air flow, of course, is going to come in from the side vents here on the outside part of the case, sort of you know, over the transformer a bit, and then through the heatsinks, and then going to be sucked out the fan at the back.

**Dave Jones:** So, not too bad layout at all. And you'll notice the daisy-chain serial connector here going down to the bottom board. And really, that's the only data that comes from the bottom board.

**Dave Jones:** Everything else in there is just you know, input-output power wiring from the transformer, and all the front panel. So, all of your data is set and read via this serial link via the serial link here onto the main board, which then of course we've seen goes to the mains earth reference part of it here back to the main processor on the front panel.

**Dave Jones:** So, each power supply module here for each channel must have its own on-board processing and on-board voltage reference and also analog to digital and digital to analog converters. Now, if we have a look at the mains wiring here, I've actually disconnected the these red and black ones down the bottom.

**Dave Jones:** They're the two They're They come directly from the IEC mains input down here, and they go through these two cable ties here, and they go down to the switch on the front panel down in there.

**Dave Jones:** Double pole switch, and then that comes back to these two, which I've disconnected down in here. And sorry about this, it's a bit convoluted, but they come back to a little isolated section of the main board down the bottom here, which has some input protection and some filtering as well, and then that goes off all the way back here.

**Dave Jones:** It's a little bit convoluted, but it goes all the way back to the voltage selection board, which is really good cuz they've got a uh insulation on the back of that, and then that goes out from the voltage selection, goes all the way straight into our toroidal transformer.

**Dave Jones:** Now, if we have a look at our front panel terminal board, you can see this is our common grounded one, so this is our 5-V output here, and this is our 30-V with the They're the two that actually have the common ground, even though they don't actually look to be connected at this particular point.

**Dave Jones:** They will be connected back further on the board. Now, the first thing you'll notice, of course, is that there's two wires going to each one, a power wire and a smaller sense wire.

**Dave Jones:** So, this thing does actually do front panel terminal sensing. There you go, they've got the wires going back and that's the same on all of the channels here. There's the other uh 30-V output one.

**Dave Jones:** And uh yeah, you know, obviously they've done that because they have to. This is a precision uh power supply. You've at least got to sense the load at the front panel uh terminals.

**Dave Jones:** And they've gone to all the effort to do that, as you'd expect, but you know, uh the obvious oversight is, well, if they went to all that trouble, why couldn't they include a little bit of switching and some uh sense terminals on the back panel or something like that.

**Dave Jones:** I guess, you know, I don't know. Uh feature creep, maybe perhaps, or uh you know, they leave that to the higher-end models or whatever. You know, it's one of those differentiator things, but anyway, they have done that.

**Dave Jones:** And there's no shake-proof washers on these, either. You'll notice that uh the nuts have actually been soldered down to the ground planes down there. Not sure if I like that.

**Dave Jones:** I would have liked to have seen some proper uh shake-proof washers with some Loctite. That's a bit how you doing. Fun done a couple of screws on the side, and I'm going to prise off the front panel here.

**Dave Jones:** Hopefully, I can get it out in one piece, and uh we'll be able to see all the main processing on the front. And there's really not much doing here at all.

**Dave Jones:** Might have to take this board out and flip it over to have a look at the uh part used, but obviously, look, there's only one BGA device here. You can tell by all the uh vias in there and all the uh decoupling around that, of course.

**Dave Jones:** Looks like we might have some uh JTAG uh programming interfaces here, perhaps. I don't know. We'd have to uh flip that open to uh have a look. And then we're just got some ribbon cables.

**Dave Jones:** This one goes over to the keypad. This one goes over to the LCD and as we've said the LCD is appears to be the same on both versions and that's just one of those you know module things with the some circuitry on the flex there some driver and inverter stuff on the flex circuitry and then we've got our other ribbon cable which heads off back to the main board

**Dave Jones:** for all of our um rear panel and control interfaces. Now you can't see it there but I'm a bit surprised to find a 1,000 mic output cap there. That is 1,000 mics is pretty darn high for a any power supply which has a constant current capability.

**Dave Jones:** Why? Because on a supply with constant current at any time it can switch into constant current mode but that constant current might be limited back further on the board but then this output capacitor here can deliver a spike of current you know energy directly into your load over and above that set current amount.

**Dave Jones:** So during that switch over period so it really the design goal when you're designing any lab power supply with constant current mode capability is to minimize your output capacitance there but they've whacked in 1,000 mic which is pretty darn high.

**Dave Jones:** Now whether or not they have done that because that was the minimum value that they required for output stability I have no idea. You'd have to go into the circuit and the actual design and how and the loop performance of this thing.

**Dave Jones:** And just like on the Siglent I'm very disappointed to find this just this crappy folded part of the metalwork here that the ribbon cable goes through. I don't man like the quality of the construction in terms of the metal work.

**Dave Jones:** Although, yes, admittedly this one is better than the Siglent, but still I don't know, it's a little bit ugly. But still, there's not much rust in this one at all compared to the Siglent.

**Dave Jones:** And here's the main board, and there's a bit of a surprise in here. Instead of the usual analog devices Blackfin DSP, we find in a ton of other Rigol gear, but they've gone for a Freescale i.MX283 um applications processor.

**Dave Jones:** And this has got a, you know, an arm core running in it with a whole bunch of stuff. It's got, you know, a high-end ADC and DAC and all, you know, Ethernet, fine.

**Dave Jones:** All sorts of stuff designed as sort of a one-chip solution for everything. But I guess, you know, they optimized the cost of this thing, I guess. Maybe the Blackfin DSP was more expensive, but I guess they figured, you know, that's all they needed to run this thing.

**Dave Jones:** I mean, it doesn't have to do any heavy DSP. It's just driving and a graphical LCD and reading a keypad and doing some, you know, serial and maybe some Ethernet is probably the hardest thing this thing's got to do, really.

**Dave Jones:** So, you know, I guess they optimized it down. I found that a bit surprising anyway. And obviously the JTAG header for that one is up the top here. But look at the Look at the flux residue left from the hand soldering process there of these connectors.

**Dave Jones:** I don't like that at all. They spoiled the thing. And otherwise, it's, you know, the reflow soldering quality is very good. And once again, another couple of hand soldered connectors down the bottom.

**Dave Jones:** Very sloppy. They haven't bothered to clean it up. Quite disappointing. Didn't don't really expect that from Rigol. And the other device is actually an 8051 processor. There we go.

**Dave Jones:** So, we've seen a similar sort of thing before in terms of We've got stuff like LAN clock and things like that. So, maybe that's just a small processor to control the LAN, but maybe this other connector here is just a um, well, it could be the programming interface for that 8051, but it could also be a serial monitor uh, you know, debug type thing.

**Dave Jones:** Maybe where they actually, you know, program the uh, flash memory and handles all that sort of stuff and programs the OS, allows you to get all sorts of debug information out and stuff like that.

**Dave Jones:** And in there we have a Winbond SPI flash memory tucked away. So, what that one's holding? I don't know. Your guess is as good as mine. And of course, the good thing about these application uh, processors, they always have their own or we usually have their own power management built in.

**Dave Jones:** So, you can see it's got its own uh, you know, part of the die over here is all dedicated to the uh, switching uh, circuitry for its own core.

**Dave Jones:** So, it's got all the switching built in and you just need a couple of, you know, externally inductors and caps, which can sometimes be bigger than the entire bloody processor itself.

**Dave Jones:** And that one handles all its own power. So, let's power up and see if she still works, shall we? Will the magic smoke escape? Hope I put everything back.

**Dave Jones:** Woohoo! Looks good. It's booting. Fantastic. So, there you go. That was the Rigol DP 832/832A. Uh, bench power supply. And yes, it is looks like it's an absolutely identical model to the 832A.

**Dave Jones:** You just pay for the software options, but that's not very surprising at all. That's what pretty much everyone expected. And the design and build quality is not bad at all.

**Dave Jones:** Yes, I am disappointed with the chassis with some rust on there and also, you know, just a little bit of sloppiness here and there in terms of that. But yeah, I know a lot of people complain, "Oh, it's just as as the Siglent." Well, bloody compare the two.

**Dave Jones:** It's not. This one is the finish and polishing this one is much better than the Siglent. The Siglent was absolutely shocking compared to this one still. So, yeah, there was a bit of edge rust there, but really that's where it was confined to just those laser trimmed edges on the exposed parts of the metalwork there, but you know, not nearly as bad as the Siglent.

**Dave Jones:** Not even a lot of people said, you know, there was nothing wrong with the Siglent one either. So, make up your own mind. Make up your own opinion, but I think this thing is designed and built pretty well.

**Dave Jones:** I love the big toroid transformer in there. Very nice indeed. And the dual board construction and is rather nice. And yes, it's probably, you know, you can experiment and hack around.

**Dave Jones:** You could even get access to those easily get access to those external sense terminals. So, if you wanted to really get a hacker connector on the back panel or something like that for external sensing, I can't see why you wouldn't do that.

**Dave Jones:** It's well those sense inputs are well protected as well. They got the mobs on there. And yeah, it's not too bad at all. So, there you go. That's our Rigol DP832/8328 power supply.

**Dave Jones:** Hope you enjoyed it. If you want to discuss it, jump on over to the EEVblog forum. Catch you next time. Oh, and by the way, the high-res photos of the this thing will always be available on my Flickr account.

**Dave Jones:** In fact, a lot of the teardown photos are often available on my Flickr account before I even upload the videos. So, there you go. Bye.
